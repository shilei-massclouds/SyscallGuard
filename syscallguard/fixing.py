from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Any

from .checking import (
    _apply_test_patches,
    _current_versions,
    _finding_index,
    _load_entities,
    _load_open_finding_index,
    _run_dynamic_test,
    _run_static_check,
    load_check_report,
)
from .common import (
    SCHEMA_VERSION,
    RunRecorder,
    SyscallGuardError,
    atomic_write_text,
    atomic_write_yaml,
    content_hash,
    dependency_mismatch,
    ensure_target_workspace,
    entity_version,
    file_hash,
    git,
    git_output,
    load_index,
    load_mapping,
    new_run_id,
    normalize_run_id,
    repo_root,
    slug,
    transactional_write,
    utc_now,
    version_content_hash,
    yaml_text,
)


FIX_TEMP_ROOT = Path(os.environ.get("SYSCALLGUARD_FIX_TEMP_ROOT", "/tmp/syscallguard-fix"))
PREPARATION_KIND = "syscallguard_fix_preparation"


def _report_text(manifest: dict[str, Any]) -> str:
    counts = manifest.get("counts", {})
    lines = [
        "# Starry Compliance Fix",
        "",
        f"Run: `{manifest.get('run_id', '')}`",
        f"Status: `{manifest['status']}`",
        f"Branch: `{manifest.get('branch', '')}`",
        "",
        f"- Source check reports: {len(manifest.get('source_check_report_ids', []))}",
        f"- Confirmed findings selected: {counts.get('selected_findings', 0)}",
        f"- Static regression failures: {counts.get('static_failures', 0)}",
        f"- Dynamic regression failures: {counts.get('dynamic_failures', 0)}",
        f"- Regression blockers: {counts.get('blockers', 0)}",
    ]
    return "\n".join(lines) + "\n"


def _report(recorder: RunRecorder) -> None:
    atomic_write_text(
        recorder.directory / "report.md", _report_text(recorder.manifest)
    )


def _failed_regression(
    recorder: RunRecorder,
    message: str,
    blockers: list[dict[str, Any]],
) -> None:
    recorder.manifest["status"] = "failed"
    recorder.manifest["completed_at_utc"] = utc_now()
    recorder.manifest["blockers"] = blockers
    recorder.manifest["error"] = message
    recorder.flush()
    _report(recorder)
    recorder.flush()


def _finding_report_ids(
    root: Path,
    findings: dict[str, dict[str, Any]],
    branch: str,
    snapshot: str,
) -> list[str]:
    report_ids: set[str] = set()
    for finding_id, finding in findings.items():
        occurrences = finding.get("occurrences", [])
        if not isinstance(occurrences, list):
            raise SyscallGuardError(f"finding {finding_id} occurrences must be a list")
        matched_current_branch = False
        for occurrence in occurrences:
            if not isinstance(occurrence, dict):
                continue
            report_id = occurrence.get("check_report_id")
            evidence_kind = occurrence.get("evidence_kind")
            source_id = occurrence.get("source_id")
            if not (
                isinstance(report_id, str)
                and evidence_kind in {"static", "dynamic"}
                and isinstance(source_id, str)
            ):
                continue
            try:
                report = load_check_report(root, report_id)
            except SyscallGuardError:
                continue
            target = report.get("target", {})
            if (
                target.get("branch") == branch
                and target.get("snapshot_hash") == snapshot
            ):
                report_ids.add(report_id)
                matched_current_branch = True
        if not matched_current_branch:
            raise SyscallGuardError(
                f"finding {finding_id} target branch or snapshot differs from the "
                f"current Starry branch: no evidence-bearing check report for "
                f"branch {branch!r}; rerun mapping and checking"
            )
    return sorted(report_ids)


def _merge_report_scope(reports: dict[str, dict[str, Any]]) -> dict[str, list[str]]:
    scope = {"rules": set(), "static_checks": set(), "dynamic_tests": set()}
    for report_id, report in reports.items():
        raw_scope = report.get("execution_scope")
        if not isinstance(raw_scope, dict):
            raise SyscallGuardError(f"check report {report_id} has no execution scope")
        for kind in scope:
            ids = raw_scope.get(kind, [])
            if not isinstance(ids, list) or not all(isinstance(item, str) for item in ids):
                raise SyscallGuardError(
                    f"check report {report_id} has an invalid {kind} execution scope"
                )
            scope[kind].update(ids)
    return {kind: sorted(ids) for kind, ids in scope.items()}


def _load_regression_entities(
    root: Path,
    scope: dict[str, list[str]],
) -> dict[str, dict[str, dict[str, Any]]]:
    rules, _ = _load_entities(
        root, scope["rules"], "library/rules", "rule_id", "syscallguard_rule"
    )
    checks, _ = _load_entities(
        root,
        scope["static_checks"],
        "targets/starry/static-checks",
        "check_id",
        "syscallguard_starry_static_check",
    )
    tests, _ = _load_entities(
        root,
        scope["dynamic_tests"],
        "targets/starry/dynamic-tests",
        "test_id",
        "syscallguard_starry_dynamic_test",
    )
    return {"rules": rules, "static_checks": checks, "dynamic_tests": tests}


def _report_scope_mismatches(
    reports: dict[str, dict[str, Any]],
    entities: dict[str, dict[str, dict[str, Any]]],
) -> list[str]:
    reasons: list[str] = []
    for report_id, report in reports.items():
        raw_scope = report.get("execution_scope", {})
        recorded_all = report.get("entity_versions", {})
        if not isinstance(recorded_all, dict):
            reasons.append(f"check report {report_id} has no entity versions")
            continue
        for kind in ("rules", "static_checks", "dynamic_tests"):
            recorded = recorded_all.get(kind, {})
            ids = raw_scope.get(kind, []) if isinstance(raw_scope, dict) else []
            if not isinstance(recorded, dict) or not isinstance(ids, list):
                reasons.append(f"check report {report_id} has invalid {kind} versions")
                continue
            for entity_id in ids:
                row = recorded.get(entity_id)
                current = entities[kind].get(str(entity_id))
                if not isinstance(row, dict) or current is None:
                    reasons.append(
                        f"check report {report_id} cannot resolve {kind}/{entity_id}"
                    )
                    continue
                mismatch = dependency_mismatch(row, str(entity_id), current)
                if mismatch:
                    reasons.append(f"check report {report_id}: {mismatch}")
    return reasons


def _fix_workspace(run_id: str) -> Path:
    return FIX_TEMP_ROOT / normalize_run_id(run_id)


def _seal_preparation(preparation: dict[str, Any]) -> None:
    preparation["content_hash"] = version_content_hash(preparation)


def _load_preparation(run_id: str) -> dict[str, Any]:
    path = _fix_workspace(run_id) / "preparation.yaml"
    preparation = load_mapping(path)
    if (
        preparation.get("kind") != PREPARATION_KIND
        or preparation.get("run_id") != normalize_run_id(run_id)
    ):
        raise SyscallGuardError(f"invalid fix preparation: {path}")
    if preparation.get("content_hash") != version_content_hash(preparation):
        raise SyscallGuardError(f"fix preparation content hash mismatch: {path}")
    return preparation


def prepare_fix(
    root: Path | None = None,
    requested_run_id: str | None = None,
) -> dict[str, Any]:
    """Freeze every open finding for the current snapshot without creating a fix run."""
    root = (root or repo_root()).resolve()
    _descriptor, repository, branch, repository_identity, snapshot = ensure_target_workspace(
        root / "targets/starry/target.yaml"
    )
    open_findings = _load_open_finding_index(root)
    findings = {
        finding_id: finding
        for finding_id, finding in open_findings.items()
        if finding.get("target_snapshot_hash") == snapshot
    }
    if not findings:
        return {
            "status": "no_open_findings",
            "target_snapshot_hash": snapshot,
            "selected_finding_ids": [],
        }

    source_ids = _finding_report_ids(root, findings, branch, snapshot)
    reports = {report_id: load_check_report(root, report_id) for report_id in source_ids}
    for report_id, report in reports.items():
        report_target = report.get("target", {})
        report_snapshot = report_target.get("snapshot_hash")
        report_branch = report_target.get("branch")
        if report_snapshot != snapshot or report_branch != branch:
            raise SyscallGuardError(
                f"check report {report_id} target branch or snapshot differs from the current Starry branch"
            )
    scope = _merge_report_scope(reports)
    entities = _load_regression_entities(root, scope)
    mismatches = _report_scope_mismatches(reports, entities)
    if mismatches:
        raise SyscallGuardError("stale evidence: " + "; ".join(mismatches))

    run_id = normalize_run_id(
        requested_run_id
        or new_run_id(
            "fix", {"findings": sorted(findings), "snapshot": snapshot, "at": utc_now()}
        )
    )
    workspace = _fix_workspace(run_id)
    if workspace.exists() or (root / "runs" / run_id).exists():
        raise SyscallGuardError(f"fix run or preparation already exists: {run_id}")
    target = {
        "target_id": "starry",
        "repository": str(repository),
        "repository_identity": repository_identity,
        "descriptor_hash": file_hash(root / "targets/starry/target.yaml"),
        "branch": branch,
        "snapshot_hash": snapshot,
    }
    preparation = {
        "schema_version": SCHEMA_VERSION,
        "kind": PREPARATION_KIND,
        "run_id": run_id,
        "status": "prepared",
        "prepared_at_utc": utc_now(),
        "root": str(root),
        "target": target,
        "selected_finding_ids": sorted(findings),
        "finding_versions": {
            finding_id: entity_version(finding_id, finding)
            for finding_id, finding in findings.items()
        },
        "source_check_report_ids": source_ids,
        "source_check_report_versions": {
            report_id: entity_version(report_id, report)
            for report_id, report in reports.items()
        },
        "regression_scope": scope,
        "entity_versions": _current_versions(entities),
        "implementation_patch": str(workspace / "implementation-fix.patch"),
    }
    _seal_preparation(preparation)
    atomic_write_yaml(workspace / "preparation.yaml", preparation)
    return preparation


def _finalize_inputs(
    root: Path, preparation: dict[str, Any]
) -> tuple[
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
    dict[str, dict[str, dict[str, Any]]],
    list[str],
]:
    reasons: list[str] = []
    target = preparation.get("target", {})
    expected_branch = target.get("branch") if isinstance(target, dict) else None
    if not isinstance(expected_branch, str) or not expected_branch:
        raise SyscallGuardError("fix preparation has no negotiated Starry branch")
    descriptor_path = root / "targets/starry/target.yaml"
    _descriptor, repository, branch, repository_identity, current_snapshot = (
        ensure_target_workspace(descriptor_path, expected_branch)
    )
    snapshot = str(target.get("snapshot_hash", ""))
    if (
        target.get("repository") != str(repository)
        or target.get("repository_identity") != repository_identity
        or target.get("descriptor_hash") != file_hash(descriptor_path)
        or branch != expected_branch
    ):
        reasons.append("Starry branch identity changed after fix preparation")
    if current_snapshot != snapshot:
        reasons.append("Starry content changed after fix preparation")

    current_open = _load_open_finding_index(root)
    selected_ids = preparation.get("selected_finding_ids", [])
    selected = {
        finding_id: current_open[finding_id]
        for finding_id in selected_ids
        if isinstance(finding_id, str) and finding_id in current_open
    }
    current_snapshot_ids = sorted(
        finding_id
        for finding_id, finding in current_open.items()
        if finding.get("target_snapshot_hash") == snapshot
    )
    if current_snapshot_ids != sorted(selected_ids):
        reasons.append("open finding selection changed after fix preparation")
    recorded_findings = preparation.get("finding_versions", {})
    for finding_id, finding in selected.items():
        row = recorded_findings.get(finding_id) if isinstance(recorded_findings, dict) else None
        if not isinstance(row, dict):
            reasons.append(f"fix preparation has no version for finding {finding_id}")
            continue
        mismatch = dependency_mismatch(row, finding_id, finding)
        if mismatch:
            reasons.append(mismatch)

    source_ids = preparation.get("source_check_report_ids", [])
    reports: dict[str, dict[str, Any]] = {}
    recorded_reports = preparation.get("source_check_report_versions", {})
    for report_id in source_ids if isinstance(source_ids, list) else []:
        try:
            report = load_check_report(root, str(report_id))
        except SyscallGuardError as exc:
            reasons.append(str(exc))
            continue
        reports[str(report_id)] = report
        row = recorded_reports.get(report_id) if isinstance(recorded_reports, dict) else None
        if not isinstance(row, dict):
            reasons.append(f"fix preparation has no version for check report {report_id}")
        else:
            mismatch = dependency_mismatch(row, str(report_id), report)
            if mismatch:
                reasons.append(mismatch)

    scope = preparation.get("regression_scope", {})
    if not isinstance(scope, dict):
        raise SyscallGuardError("fix preparation regression scope is invalid")
    entities = _load_regression_entities(root, scope)
    recorded_entities = preparation.get("entity_versions", {})
    for kind, rows in entities.items():
        recorded = recorded_entities.get(kind, {}) if isinstance(recorded_entities, dict) else {}
        for entity_id, entity in rows.items():
            row = recorded.get(entity_id) if isinstance(recorded, dict) else None
            if not isinstance(row, dict):
                reasons.append(f"fix preparation has no version for {kind}/{entity_id}")
                continue
            mismatch = dependency_mismatch(row, entity_id, entity)
            if mismatch:
                reasons.append(mismatch)
    return selected, reports, entities, sorted(set(reasons))


def _fix_index(
    root: Path, fixes: dict[str, dict[str, Any]], generated_at: str
) -> dict[str, Any]:
    path = root / "targets/starry/fixes/index.yaml"
    index = load_index(path, "syscallguard_starry_fix_index")
    by_id = {
        str(row["id"]): row
        for row in index["entities"]
        if isinstance(row, dict) and isinstance(row.get("id"), str)
    }
    for fix_id, entity in fixes.items():
        by_id[fix_id] = {
            "id": fix_id,
            "path": f"targets/starry/fixes/{slug(fix_id)}.yaml",
            "finding_refs": entity["finding_refs"],
            "status": entity["status"],
            "generated_at_utc": entity["generated_at_utc"],
            "content_hash": version_content_hash(entity),
        }
    index["entities"] = [by_id[key] for key in sorted(by_id)]
    index["updated_at_utc"] = generated_at
    return index


def _finalize_fix(
    preparation_run_id: str,
    root: Path | None = None,
    patch: Path | None = None,
) -> str:
    run_id = normalize_run_id(preparation_run_id)
    preparation = _load_preparation(run_id)
    recorded_root = Path(str(preparation.get("root", ""))).resolve()
    root = (root or recorded_root).resolve()
    if root != recorded_root:
        raise SyscallGuardError("fix preparation belongs to a different SyscallGuard root")
    patch = (patch or Path(str(preparation.get("implementation_patch", "")))).resolve()
    if not patch.is_file():
        raise SyscallGuardError(f"implementation patch is missing: {patch}")

    findings, reports, entities, stale_reasons = _finalize_inputs(root, preparation)
    source_ids = list(preparation["source_check_report_ids"])
    recorder = RunRecorder(
        root,
        "fix",
        run_id,
        {"patch": str(patch)},
        None,
    )
    recorder.manifest["source_check_report_ids"] = source_ids
    recorder.manifest["target"] = dict(preparation["target"])
    recorder.manifest["entities"] = {"findings": sorted(findings), "fixes": []}
    finding_versions = {
        finding_id: entity_version(finding_id, finding)
        for finding_id, finding in findings.items()
    }
    recorder.manifest["entity_versions"] = {
        "findings": finding_versions,
        "check_reports": {
            report_id: entity_version(report_id, report)
            for report_id, report in reports.items()
        },
        **_current_versions(entities),
    }
    recorder.manifest["entity_hashes"] = {
        kind: {
            entity_id: version_content_hash(entity)
            for entity_id, entity in rows.items()
        }
        for kind, rows in entities.items()
    }
    recorder.manifest["regression_scope"] = preparation["regression_scope"]
    recorder.manifest["input_hash"] = content_hash(
        {
            "findings": finding_versions,
            "check_reports": recorder.manifest["entity_versions"]["check_reports"],
            "regression_entities": recorder.manifest["entity_hashes"],
            "target": preparation["target"],
        }
    )
    # Persist provenance before mutating the negotiated Starry branch so even
    # an environmental failure leaves a valid, attributable formal run.
    recorder.flush()
    if stale_reasons:
        recorder.manifest["counts"] = {
            "selected_findings": 0,
            "static_failures": 0,
            "dynamic_failures": 0,
            "blockers": 1,
        }
        recorder.manifest["outputs"] = {"report": "report.md"}
        recorder.complete(
            [
                {
                    "kind": "stale_preparation",
                    "reason": "fix inputs changed after preparation",
                    "dependency_mismatches": stale_reasons,
                }
            ]
        )
        _report(recorder)
        recorder.flush()
        return run_id

    target = preparation["target"]
    repository = Path(str(target["repository"])).resolve()
    checked_snapshot = str(target["snapshot_hash"])
    branch = str(target["branch"])
    recorder.manifest["branch"] = branch
    recorder.flush()
    logs = recorder.directory / "logs"
    logs.mkdir(parents=True, exist_ok=True)
    saved_patch = recorder.directory / "implementation.patch"
    atomic_write_text(saved_patch, patch.read_text(encoding="utf-8"))
    recorder.manifest["patch_version"] = {
        "id": "implementation.patch",
        "generated_at_utc": utc_now(),
        "content_hash": file_hash(saved_patch),
    }

    blocked_tests, blockers, _applied_test_patches = _apply_test_patches(
        root, repository, entities["dynamic_tests"], logs
    )
    apply_result = git(
        repository, ["apply", "--whitespace=nowarn", str(saved_patch)], check=False
    )
    atomic_write_text(
        logs / "implementation-patch-apply.log",
        apply_result.stdout + apply_result.stderr,
    )
    if apply_result.returncode != 0:
        recorder.manifest["counts"] = {
            "selected_findings": len(findings),
            "static_failures": 0,
            "dynamic_failures": 0,
            "blockers": len(blockers),
        }
        recorder.manifest["outputs"] = {
            "patch": "implementation.patch",
            "logs": "logs/",
            "report": "report.md",
        }
        _failed_regression(recorder, "implementation patch failed to apply", blockers)
        return run_id

    static_results: list[dict[str, Any]] = []
    for check_id, definition in sorted(entities["static_checks"].items()):
        result, blocker = _run_static_check(repository, check_id, definition)
        static_results.append(result)
        if blocker:
            blockers.append(blocker)
    dynamic_results: list[dict[str, Any]] = []
    for test_id, definition in sorted(entities["dynamic_tests"].items()):
        result, blocker = _run_dynamic_test(
            repository,
            test_id,
            definition,
            logs / f"dynamic-{slug(test_id)}.log",
            test_id in blocked_tests,
        )
        dynamic_results.append(result)
        if blocker and content_hash(blocker) not in {content_hash(item) for item in blockers}:
            blockers.append(blocker)

    regression_generated_at = utc_now()
    regression_dependencies = [
        version
        for kind in ("static_checks", "dynamic_tests")
        for _entity_id, version in sorted(
            recorder.manifest["entity_versions"][kind].items()
        )
    ]
    results = {
        "schema_version": SCHEMA_VERSION,
        "kind": "syscallguard_fix_regression",
        "run_id": run_id,
        "generated_at_utc": regression_generated_at,
        "upstream_dependencies": regression_dependencies,
        "target_snapshot_hash": checked_snapshot,
        "static": static_results,
        "dynamic": dynamic_results,
        "blockers": blockers,
    }
    atomic_write_yaml(recorder.directory / "regression-results.yaml", results)
    regression_version = entity_version(run_id, results)
    recorder.manifest["regression_result_version"] = regression_version
    static_failures = sum(row.get("result") != "pass" for row in static_results)
    dynamic_failures = sum(
        row.get("result") not in {"pass", "skipped"} for row in dynamic_results
    )
    recorder.manifest["counts"] = {
        "selected_findings": len(findings),
        "static_failures": static_failures,
        "dynamic_failures": dynamic_failures,
        "blockers": len(blockers),
    }
    recorder.manifest["outputs"] = {
        "patch": "implementation.patch",
        "regression_results": "regression-results.yaml",
        "logs": "logs/",
        "report": "report.md",
    }
    if blockers or static_failures or dynamic_failures:
        _failed_regression(
            recorder,
            "regression did not pass; no completion commit was created",
            blockers,
        )
        return run_id

    git(repository, ["add", "-A"])
    if not git_output(repository, ["status", "--short"]):
        _failed_regression(recorder, "patch produced no committable changes", [])
        return run_id
    commit_result = git(
        repository,
        [
            "-c",
            "user.name=SyscallGuard",
            "-c",
            "user.email=syscallguard@localhost",
            "commit",
            "-m",
            f"fix(starry): resolve SyscallGuard findings ({run_id})",
        ],
        check=False,
    )
    atomic_write_text(
        logs / "commit.log",
        "completion commit created\n"
        if commit_result.returncode == 0
        else "commit creation failed\n",
    )
    if commit_result.returncode != 0:
        _failed_regression(
            recorder, "regression passed but commit creation failed", []
        )
        return run_id
    fix_generated_at = utc_now()
    check_versions = [
        recorder.manifest["entity_versions"]["check_reports"][report_id]
        for report_id in source_ids
    ]
    fix_entities: dict[str, dict[str, Any]] = {}
    updated_findings: dict[str, dict[str, Any]] = {}
    for finding_id, finding in findings.items():
        fix_id = f"fix-{slug(finding_id)}"
        fix_entity = {
            "schema_version": SCHEMA_VERSION,
            "kind": "syscallguard_starry_fix",
            "fix_id": fix_id,
            "finding_refs": [finding_id],
            "source_check_report_ids": source_ids,
            "patch": f"runs/{run_id}/implementation.patch",
            "starry_repository": str(repository),
            "starry_branch": branch,
            "regression": f"runs/{run_id}/regression-results.yaml",
            "status": "fixed",
            "generated_at_utc": fix_generated_at,
            "upstream_dependencies": [
                finding_versions[finding_id],
                *check_versions,
                recorder.manifest["patch_version"],
                regression_version,
            ],
        }
        fix_entities[fix_id] = fix_entity
        updated = dict(finding)
        updated["resolution"] = "fixed"
        updated["fix_ref"] = fix_id
        updated["fixed_by_run"] = run_id
        updated["generated_at_utc"] = fix_generated_at
        updated["upstream_dependencies"] = [entity_version(fix_id, fix_entity)]
        updated_findings[finding_id] = updated

    files: list[tuple[Path, bytes]] = []
    for fix_id, entity in sorted(fix_entities.items()):
        files.append(
            (
                root / "targets/starry/fixes" / f"{slug(fix_id)}.yaml",
                yaml_text(entity).encode("utf-8"),
            )
        )
    for finding_id, entity in sorted(updated_findings.items()):
        files.append(
            (
                root / "targets/starry/findings" / f"{slug(finding_id)}.yaml",
                yaml_text(entity).encode("utf-8"),
            )
        )
    files.append(
        (
            root / "targets/starry/fixes/index.yaml",
            yaml_text(_fix_index(root, fix_entities, fix_generated_at)).encode("utf-8"),
        )
    )
    files.append(
        (
            root / "targets/starry/findings/index.yaml",
            yaml_text(_finding_index(root, updated_findings, fix_generated_at)).encode(
                "utf-8"
            ),
        )
    )
    transactional_write(files)
    recorder.manifest["entity_versions"]["fixes"] = {
        fix_id: entity_version(fix_id, entity)
        for fix_id, entity in fix_entities.items()
    }
    recorder.manifest["entities"]["fixes"] = sorted(fix_entities)
    recorder.manifest["outputs"]["fix_index"] = "targets/starry/fixes/index.yaml"
    recorder.manifest["outputs"]["finding_index"] = "targets/starry/findings/index.yaml"
    recorder.complete()
    _report(recorder)
    recorder.flush()
    return run_id


def finalize_fix(
    preparation_run_id: str,
    root: Path | None = None,
    patch: Path | None = None,
) -> str:
    """Finalize a preparation and leave any created formal run terminal."""
    run_id = normalize_run_id(preparation_run_id)
    try:
        return _finalize_fix(run_id, root, patch)
    except BaseException as exc:
        resolved_root = root.resolve() if root is not None else None
        if resolved_root is None:
            try:
                resolved_root = Path(str(_load_preparation(run_id).get("root", ""))).resolve()
            except BaseException:
                resolved_root = None
        if resolved_root is not None:
            manifest_path = resolved_root / "runs" / run_id / "manifest.yaml"
            if manifest_path.is_file():
                try:
                    manifest = load_mapping(manifest_path)
                    if manifest.get("status") == "running":
                        manifest["status"] = "failed"
                        manifest["completed_at_utc"] = utc_now()
                        manifest["error"] = f"{type(exc).__name__}: {exc}"
                        atomic_write_yaml(manifest_path, manifest)
                        atomic_write_text(
                            manifest_path.parent / "report.md", _report_text(manifest)
                        )
                except BaseException:
                    pass
        if isinstance(exc, SyscallGuardError):
            raise
        raise SyscallGuardError(str(exc)) from exc


def run_fix(
    patch: Path | None = None,
    root: Path | None = None,
    requested_run_id: str | None = None,
) -> str | None:
    """Convenience API for tests and non-interactive callers."""
    preparation = prepare_fix(root, requested_run_id)
    if preparation["status"] == "no_open_findings":
        return None
    run_id = str(preparation["run_id"])
    destination = Path(str(preparation["implementation_patch"]))
    if patch is not None and patch.resolve() != destination.resolve():
        atomic_write_text(destination, patch.resolve().read_text(encoding="utf-8"))
    return finalize_fix(run_id, root)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="自动修复当前 Starry 快照的全部合规缺口")
    parser.add_argument(
        "--finalize", metavar="RUN_ID", help=argparse.SUPPRESS
    )
    parser.add_argument("--root", type=Path, default=repo_root(), help=argparse.SUPPRESS)
    parser.add_argument("--run-id", help=argparse.SUPPRESS)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.finalize:
            run_id = finalize_fix(args.finalize, args.root)
            path = args.root.resolve() / "runs" / run_id
            manifest = load_mapping(path / "manifest.yaml")
            print(f"run_id: {run_id}")
            print(f"status: {manifest['status']}")
            print(f"result: {path}")
            if manifest.get("branch"):
                print(f"branch: {manifest['branch']}")
            print(
                f"fix_index: {args.root.resolve() / 'targets/starry/fixes/index.yaml'}"
            )
            return 1 if manifest["status"] == "failed" else 0

        preparation = prepare_fix(args.root, args.run_id)
        if preparation["status"] == "no_open_findings":
            print("status: no_open_findings")
            print("message: 当前 Starry 内容快照没有可修复的 open confirmed finding")
            return 0
        print(f"run_id: {preparation['run_id']}")
        print("status: prepared")
        print(
            "finding_ids: " + ",".join(preparation["selected_finding_ids"])
        )
        print(
            "source_check_report_ids: "
            + ",".join(preparation["source_check_report_ids"])
        )
        print(f"preparation: {_fix_workspace(str(preparation['run_id'])) / 'preparation.yaml'}")
        print(f"implementation_patch: {preparation['implementation_patch']}")
        print(
            "finalize: python3 skills/fix-starry-compliance/scripts/run.py "
            f"--finalize {preparation['run_id']}"
        )
        return 0
    except SyscallGuardError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
