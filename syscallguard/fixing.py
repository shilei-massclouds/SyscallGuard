from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

from .checking import (
    _apply_test_patches,
    _create_worktree,
    _current_input,
    _current_versions,
    _mapping_staleness,
    _mapping_target_descriptor,
    _run_dynamic_test,
    _run_static_check,
    _worktree_path,
)
from .common import (
    SCHEMA_VERSION,
    RunRecorder,
    SyscallGuardError,
    atomic_write_text,
    atomic_write_yaml,
    content_hash,
    dependency_mismatch,
    entity_version,
    file_hash,
    entity_hash,
    git,
    git_output,
    load_mapping,
    new_run_id,
    publish_yaml_entities,
    read_run,
    repository_snapshot_hash,
    repo_root,
    slug,
    update_index,
    utc_now,
    version_content_hash,
)
from .mapping import load_mapping_report


def _open_findings(root: Path, check_run: dict[str, Any]) -> dict[str, dict[str, Any]]:
    ids = check_run.get("entities", {}).get("findings", [])
    if not isinstance(ids, list):
        raise SyscallGuardError("check run finding ids must be a list")
    findings: dict[str, dict[str, Any]] = {}
    for finding_id in ids:
        if not isinstance(finding_id, str):
            raise SyscallGuardError("check run finding id must be a string")
        path = root / "targets/starry/findings" / f"{slug(finding_id)}.yaml"
        finding = load_mapping(path)
        if finding.get("finding_id") != finding_id or finding.get("kind") != "syscallguard_starry_finding":
            raise SyscallGuardError(f"invalid finding entity: {path}")
        if finding.get("status") == "confirmed" and finding.get("resolution") == "open":
            findings[finding_id] = finding
    return findings


def _check_staleness(
    root: Path,
    check_run: dict[str, Any],
    _findings: dict[str, dict[str, Any]],
) -> list[str]:
    reasons: list[str] = []
    result_path = root / "runs" / str(check_run.get("run_id")) / "results.yaml"
    recorded_result = check_run.get("result_version")
    if not result_path.is_file() or not isinstance(recorded_result, dict):
        reasons.append("check run has no versioned results")
    else:
        result = load_mapping(result_path)
        mismatch = dependency_mismatch(recorded_result, str(check_run.get("run_id")), result)
        if mismatch:
            reasons.append(mismatch)
    recorded_findings = check_run.get("entity_versions", {}).get("findings", {})
    if not isinstance(recorded_findings, dict):
        reasons.append("check run has no finding versions")
    else:
        for finding_id, row in recorded_findings.items():
            if not isinstance(row, dict):
                reasons.append(f"check run has an invalid version for finding {finding_id}")
                continue
            path = root / "targets/starry/findings" / f"{slug(finding_id)}.yaml"
            if not path.is_file():
                reasons.append(f"finding {finding_id} no longer exists")
                continue
            mismatch = dependency_mismatch(row, finding_id, load_mapping(path))
            if mismatch:
                reasons.append(mismatch)
    return reasons


def _copy_patch(source: Path, destination: Path) -> None:
    try:
        text = source.read_text(encoding="utf-8")
    except OSError as exc:
        raise SyscallGuardError(f"cannot read implementation patch {source}: {exc}") from exc
    atomic_write_text(destination, text)


def _report(recorder: RunRecorder) -> None:
    counts = recorder.manifest.get("counts", {})
    lines = [
        "# Starry Compliance Fix",
        "",
        f"Run: `{recorder.run_id}`",
        f"Status: `{recorder.manifest['status']}`",
        f"Worktree: `{recorder.manifest.get('worktree', '')}`",
        f"Branch: `{recorder.manifest.get('branch', '')}`",
        "",
        f"- Confirmed findings selected: {counts.get('selected_findings', 0)}",
        f"- Static regression failures: {counts.get('static_failures', 0)}",
        f"- Dynamic regression failures: {counts.get('dynamic_failures', 0)}",
        f"- Regression blockers: {counts.get('blockers', 0)}",
    ]
    atomic_write_text(recorder.directory / "report.md", "\n".join(lines) + "\n")


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


def run_fix(
    from_run_id: str,
    patch: Path | None = None,
    root: Path | None = None,
    requested_run_id: str | None = None,
) -> str:
    root = (root or repo_root()).resolve()
    check_run = read_run(root, from_run_id, "check")
    mapping_report_id = check_run.get("from_run_id")
    if not isinstance(mapping_report_id, str) or not mapping_report_id:
        raise SyscallGuardError(f"check run {from_run_id} has no mapping report parent")
    mapping_report = load_mapping_report(root, mapping_report_id)
    run_id = requested_run_id or new_run_id("fix", {"from": from_run_id, "at": utc_now()})
    recorder = RunRecorder(
        root,
        "fix",
        run_id,
        {"from": from_run_id, "patch": str(patch.resolve()) if patch else None},
        from_run_id,
    )
    try:
        findings = _open_findings(root, check_run)
        target = check_run.get("target", mapping_report.get("target", {}))
        if not isinstance(target, dict):
            raise SyscallGuardError("check target metadata must be a mapping")
        repository = Path(str(target.get("repository", ""))).expanduser().resolve()
        revision_ref = str(_mapping_target_descriptor(mapping_report).get("revision", "HEAD"))
        checked_snapshot = str(target.get("snapshot_hash", ""))
        if not repository.is_dir() or not checked_snapshot:
            raise SyscallGuardError(f"check run {from_run_id} has invalid target metadata")
        current_snapshot = repository_snapshot_hash(repository)
        recorder.manifest["target"] = dict(target)
        recorder.manifest["entities"] = {"findings": sorted(findings), "fixes": []}
        finding_versions = {
            key: entity_version(key, value) for key, value in findings.items()
        }
        recorder.manifest["entity_versions"] = {"findings": finding_versions}
        recorder.manifest["input_hash"] = content_hash(
            {
                "check_run": from_run_id,
                "findings": {key: content_hash(value) for key, value in findings.items()},
                "target": target,
            }
        )
        stale_reasons = _check_staleness(root, check_run, findings)
        mapping_entities, _mapping_hashes, _mapping_input = _current_input(root, mapping_report)
        stale_reasons.extend(_mapping_staleness(mapping_report, mapping_entities))
        if current_snapshot != checked_snapshot or stale_reasons:
            recorder.manifest["counts"] = {"selected_findings": 0, "blockers": 1}
            recorder.complete(
                [
                    {
                        "kind": "stale_check",
                        "reason": "Starry content changed after compliance check; remap and recheck before fixing",
                        "checked_snapshot_hash": checked_snapshot,
                        "current_snapshot_hash": current_snapshot,
                        "dependency_mismatches": stale_reasons,
                    }
                ]
            )
            _report(recorder)
            recorder.flush()
            return run_id
        if not findings:
            inherited = check_run.get("blockers", [])
            blockers = inherited if isinstance(inherited, list) else []
            recorder.manifest["counts"] = {
                "selected_findings": 0,
                "skipped_no_open_findings": 1,
                "blockers": len(blockers),
            }
            recorder.manifest["outputs"] = {"report": "report.md"}
            recorder.complete(blockers)
            _report(recorder)
            recorder.flush()
            return run_id

        if patch is None:
            candidate = root / "runs" / from_run_id / "implementation-fix.patch"
            if candidate.exists():
                patch = candidate
        if patch is None or not patch.resolve().is_file():
            raise SyscallGuardError(
                "confirmed findings require an implementation patch; generate "
                f"runs/{from_run_id}/implementation-fix.patch or pass --patch"
            )

        entities, hashes, regression_input_hash = mapping_entities, _mapping_hashes, _mapping_input
        recorder.manifest["entity_hashes"] = hashes
        recorder.manifest["entity_versions"].update(_current_versions(entities))
        recorder.manifest["regression_input_hash"] = regression_input_hash
        worktree = _worktree_path(mapping_report, run_id)
        _create_worktree(repository, revision_ref, worktree)
        if repository_snapshot_hash(worktree) != checked_snapshot:
            raise SyscallGuardError("isolated Starry worktree does not match the checked content snapshot")
        recorder.manifest["worktree"] = str(worktree)
        logs = recorder.directory / "logs"
        logs.mkdir(parents=True, exist_ok=True)
        saved_patch = recorder.directory / "implementation.patch"
        _copy_patch(patch.resolve(), saved_patch)
        patch_generated_at = utc_now()
        recorder.manifest["patch_version"] = {
            "id": "implementation.patch",
            "generated_at_utc": patch_generated_at,
            "content_hash": file_hash(saved_patch),
        }

        blocked_tests, blockers = _apply_test_patches(
            root, worktree, entities["dynamic_tests"], logs
        )
        apply_result = git(
            worktree,
            ["apply", "--whitespace=nowarn", str(saved_patch)],
            check=False,
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
        for check_id, definition in entities["static_checks"].items():
            result, blocker = _run_static_check(worktree, check_id, definition)
            static_results.append(result)
            if blocker:
                blockers.append(blocker)
        dynamic_results: list[dict[str, Any]] = []
        for test_id, definition in entities["dynamic_tests"].items():
            result, blocker = _run_dynamic_test(
                worktree,
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
            for _entity_id, version in sorted(recorder.manifest["entity_versions"][kind].items())
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

        git(worktree, ["add", "-A"])
        if not git_output(worktree, ["status", "--short"]):
            _failed_regression(recorder, "patch produced no committable changes", [])
            return run_id
        branch = f"syscallguard/{run_id}"
        git(worktree, ["switch", "-c", branch])
        commit_result = git(
            worktree,
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
            "completion commit created\n" if commit_result.returncode == 0 else "commit creation failed\n",
        )
        if commit_result.returncode != 0:
            _failed_regression(recorder, "regression passed but commit creation failed", [])
            return run_id
        recorder.manifest["branch"] = branch

        fix_entities: dict[str, dict[str, Any]] = {}
        updated_findings: dict[str, dict[str, Any]] = {}
        fix_generated_at = utc_now()
        for finding_id, finding in findings.items():
            fix_id = f"fix-{slug(finding_id)}"
            fix_entity = {
                "schema_version": SCHEMA_VERSION,
                "kind": "syscallguard_starry_fix",
                "fix_id": fix_id,
                "finding_refs": [finding_id],
                "patch": f"runs/{run_id}/implementation.patch",
                "starry_repository": str(repository),
                "starry_branch": branch,
                "regression": f"runs/{run_id}/regression-results.yaml",
                "status": "fixed",
                "generated_at_utc": fix_generated_at,
                "upstream_dependencies": [
                    finding_versions[finding_id],
                    check_run["result_version"],
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
        publish_yaml_entities(
            [
                (
                    recorder.directory,
                    root / "targets/starry/fixes" / f"{slug(fix_id)}.yaml",
                    entity,
                )
                for fix_id, entity in fix_entities.items()
            ]
            + [
                (
                    recorder.directory,
                    root / "targets/starry/findings" / f"{slug(finding_id)}.yaml",
                    entity,
                )
                for finding_id, entity in updated_findings.items()
            ]
        )
        update_index(
            root / "targets/starry/fixes/index.yaml",
            "syscallguard_starry_fix_index",
            [
                {
                    "id": fix_id,
                    "path": f"targets/starry/fixes/{slug(fix_id)}.yaml",
                    "finding_refs": entity["finding_refs"],
                    "status": "fixed",
                    "generated_at_utc": entity["generated_at_utc"],
                    "content_hash": version_content_hash(entity),
                }
                for fix_id, entity in fix_entities.items()
            ],
        )
        update_index(
            root / "targets/starry/findings/index.yaml",
            "syscallguard_starry_finding_index",
            [
                {
                    "id": finding_id,
                    "path": f"targets/starry/findings/{slug(finding_id)}.yaml",
                    "syscall": entity["syscall"],
                    "rule_id": entity["rule_id"],
                    "target_snapshot_hash": entity["target_snapshot_hash"],
                    "status": entity["status"],
                    "resolution": "fixed",
                    "generated_at_utc": entity["generated_at_utc"],
                    "content_hash": version_content_hash(entity),
                }
                for finding_id, entity in updated_findings.items()
            ],
        )
        recorder.manifest["entity_versions"]["fixes"] = {
            fix_id: entity_version(fix_id, entity) for fix_id, entity in fix_entities.items()
        }
        recorder.manifest["entities"]["fixes"] = sorted(fix_entities)
        recorder.manifest["outputs"]["fix_index"] = "targets/starry/fixes/index.yaml"
        recorder.manifest["outputs"]["finding_index"] = "targets/starry/findings/index.yaml"
        recorder.complete()
        _report(recorder)
        recorder.flush()
        return run_id
    except BaseException as exc:
        recorder.fail(exc)
        if isinstance(exc, SyscallGuardError):
            raise
        raise SyscallGuardError(str(exc)) from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Fix confirmed Starry compliance findings")
    parser.add_argument("--from", dest="from_run_id", required=True, help="check run id")
    parser.add_argument("--patch", type=Path, help=argparse.SUPPRESS)
    parser.add_argument("--root", type=Path, default=repo_root(), help=argparse.SUPPRESS)
    parser.add_argument("--run-id", help=argparse.SUPPRESS)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    requested_run_id = args.run_id or new_run_id("fix", {"from": args.from_run_id})
    try:
        run_id = run_fix(args.from_run_id, args.patch, args.root, requested_run_id)
    except SyscallGuardError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        failed_path = args.root.resolve() / "runs" / requested_run_id
        if failed_path.exists():
            print(f"result: {failed_path}", file=sys.stderr)
        return 2
    path = args.root.resolve() / "runs" / run_id
    manifest = load_mapping(path / "manifest.yaml")
    print(f"run_id: {run_id}")
    print(f"status: {manifest['status']}")
    print(f"result: {path}")
    if manifest.get("worktree"):
        print(f"worktree: {manifest['worktree']}")
    if manifest.get("branch"):
        print(f"branch: {manifest['branch']}")
    print(f"fix_index: {args.root.resolve() / 'targets/starry/fixes/index.yaml'}")
    return 1 if manifest["status"] == "failed" else 0


if __name__ == "__main__":
    raise SystemExit(main())
