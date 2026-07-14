from __future__ import annotations

import argparse
import os
import re
import shlex
import subprocess
import sys
from pathlib import Path
from typing import Any

from .common import (
    SCHEMA_VERSION,
    RunRecorder,
    SyscallGuardError,
    atomic_write_text,
    atomic_write_yaml,
    content_hash,
    dependency_mismatch,
    entity_version,
    git,
    load_mapping,
    new_run_id,
    publish_yaml_entities,
    repository_snapshot_hash,
    repo_root,
    safe_relative_path,
    slug,
    update_index,
    utc_now,
    version_content_hash,
)
from .mapping import load_mapping_report


DEFAULT_BLOCKER_PATTERNS = [
    r"No space left on device",
    r"failed to unpack",
    r"could not resolve host",
    r"network is unreachable",
    r"qemu-system-[^: ]+: (?:command not found|not found)",
    r"linker .+ not found",
    r"toolchain .+ is not installed",
]


def _load_entities(
    root: Path,
    ids: list[str],
    section: str,
    id_field: str,
    expected_kind: str,
) -> tuple[dict[str, dict[str, Any]], dict[str, str]]:
    entities: dict[str, dict[str, Any]] = {}
    hashes: dict[str, str] = {}
    for entity_id in ids:
        path = root / section / f"{slug(entity_id)}.yaml"
        entity = load_mapping(path)
        if entity.get("kind") != expected_kind or entity.get(id_field) != entity_id:
            raise SyscallGuardError(f"invalid {expected_kind} entity for {entity_id}: {path}")
        entities[entity_id] = entity
        hashes[entity_id] = version_content_hash(entity)
    return entities, hashes


def _current_input(
    root: Path, mapping_report: dict[str, Any]
) -> tuple[dict[str, dict[str, dict[str, Any]]], dict[str, dict[str, str]], str]:
    entity_ids = mapping_report.get("execution_scope", {})
    if not isinstance(entity_ids, dict):
        raise SyscallGuardError("mapping report execution_scope must be a mapping")
    rules, rule_hashes = _load_entities(
        root,
        list(entity_ids.get("rules", [])),
        "library/rules",
        "rule_id",
        "syscallguard_rule",
    )
    checks, check_hashes = _load_entities(
        root,
        list(entity_ids.get("static_checks", [])),
        "targets/starry/static-checks",
        "check_id",
        "syscallguard_starry_static_check",
    )
    tests, test_hashes = _load_entities(
        root,
        list(entity_ids.get("dynamic_tests", [])),
        "targets/starry/dynamic-tests",
        "test_id",
        "syscallguard_starry_dynamic_test",
    )
    entities = {
        "rules": rules,
        "static_checks": checks,
        "dynamic_tests": tests,
    }
    hashes = {
        "rules": rule_hashes,
        "static_checks": check_hashes,
        "dynamic_tests": test_hashes,
    }
    target_snapshot_hash = str(mapping_report.get("target", {}).get("snapshot_hash", ""))
    rule_syscalls = mapping_report.get("rule_syscalls", {})
    if not isinstance(rule_syscalls, dict):
        raise SyscallGuardError("mapping report rule_syscalls must be a mapping")
    return entities, hashes, content_hash(
        {
            "entities": hashes,
            "target_snapshot_hash": target_snapshot_hash,
            "rule_syscalls": rule_syscalls,
        }
    )


def _current_versions(
    entities: dict[str, dict[str, dict[str, Any]]]
) -> dict[str, dict[str, dict[str, str]]]:
    return {
        kind: {entity_id: entity_version(entity_id, entity) for entity_id, entity in rows.items()}
        for kind, rows in entities.items()
    }


def _mapping_staleness(
    mapping_report: dict[str, Any], entities: dict[str, dict[str, dict[str, Any]]]
) -> list[str]:
    recorded_all = mapping_report.get("entity_versions", {})
    if not isinstance(recorded_all, dict):
        return ["mapping report has no entity_versions"]
    reasons: list[str] = []
    for kind in ("rules", "static_checks", "dynamic_tests"):
        recorded = recorded_all.get(kind, {})
        current = entities.get(kind, {})
        if not isinstance(recorded, dict):
            reasons.append(f"mapping report has no {kind} versions")
            continue
        for entity_id, entity in current.items():
            row = recorded.get(entity_id)
            if not isinstance(row, dict):
                reasons.append(f"mapping report has no version for {kind}/{entity_id}")
                continue
            mismatch = dependency_mismatch(row, entity_id, entity)
            if mismatch:
                reasons.append(mismatch)
    return reasons


def _prior_identical_check(root: Path, input_hash: str, current_run_id: str) -> dict[str, Any] | None:
    runs_root = root / "runs"
    if not runs_root.is_dir():
        return None
    for manifest_path in sorted(runs_root.glob("*/manifest.yaml"), reverse=True):
        if manifest_path.parent.name == current_run_id:
            continue
        try:
            manifest = load_mapping(manifest_path)
        except SyscallGuardError:
            continue
        if (
            manifest.get("stage") == "check"
            and manifest.get("status") in {"completed", "completed_with_blockers"}
            and manifest.get("input_hash") == input_hash
        ):
            return manifest
    return None


def _mapping_target_descriptor(mapping_report: dict[str, Any]) -> dict[str, Any]:
    target = mapping_report.get("target")
    if not isinstance(target, dict) or target.get("target_id") != "starry":
        raise SyscallGuardError("mapping report has no valid target metadata")
    return target


def _worktree_path(mapping_report: dict[str, Any], run_id: str) -> Path:
    descriptor = _mapping_target_descriptor(mapping_report)
    raw_root = descriptor.get("worktree_root", "/tmp/syscallguard-worktrees")
    if not isinstance(raw_root, str) or not raw_root:
        raise SyscallGuardError("target descriptor worktree_root must be a path")
    return Path(raw_root).expanduser().resolve() / run_id


def _create_worktree(repository: Path, revision_ref: str, worktree: Path) -> None:
    if worktree.exists():
        raise SyscallGuardError(f"worktree path already exists: {worktree}")
    worktree.parent.mkdir(parents=True, exist_ok=True)
    git(repository, ["worktree", "add", "--detach", str(worktree), revision_ref])


def _artifact_path(root: Path, value: str) -> Path:
    path = Path(value).expanduser()
    return path.resolve() if path.is_absolute() else (root / path).resolve()


def _apply_test_patches(
    root: Path,
    worktree: Path,
    tests: dict[str, dict[str, Any]],
    logs: Path,
) -> tuple[set[str], list[dict[str, Any]]]:
    applied: set[str] = set()
    blocked_tests: set[str] = set()
    blockers: list[dict[str, Any]] = []
    patch_to_tests: dict[str, list[str]] = {}
    for test_id, test in tests.items():
        patch_file = test.get("patch_file")
        if isinstance(patch_file, str) and patch_file:
            patch_to_tests.setdefault(patch_file, []).append(test_id)
    for patch_value, test_ids in patch_to_tests.items():
        patch = _artifact_path(root, patch_value)
        log_path = logs / f"patch-{slug(patch.name)}.log"
        if not patch.is_file():
            detail = f"dynamic test patch is missing: {patch}"
            atomic_write_text(log_path, detail + "\n")
            blockers.append(
                {
                    "kind": "test_injection",
                    "entity_ids": test_ids,
                    "reason": detail,
                    "log": str(log_path),
                }
            )
            blocked_tests.update(test_ids)
            continue
        result = git(worktree, ["apply", "--whitespace=nowarn", str(patch)], check=False)
        atomic_write_text(log_path, result.stdout + result.stderr)
        if result.returncode != 0:
            blockers.append(
                {
                    "kind": "test_injection",
                    "entity_ids": test_ids,
                    "reason": "git apply failed for dynamic test patch",
                    "log": str(log_path),
                }
            )
            blocked_tests.update(test_ids)
        else:
            applied.add(patch_value)
    return blocked_tests, blockers


def _line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _run_static_check(
    worktree: Path, check_id: str, check: dict[str, Any]
) -> tuple[dict[str, Any], dict[str, Any] | None]:
    raw_path = check.get("path")
    patterns = check.get("patterns")
    if not isinstance(raw_path, str) or not raw_path:
        return (
            {"check_id": check_id, "result": "error", "reason": "missing path"},
            {"kind": "static_definition", "entity_ids": [check_id], "reason": "missing path"},
        )
    if not isinstance(patterns, list) or not patterns:
        return (
            {"check_id": check_id, "result": "error", "reason": "missing patterns"},
            {
                "kind": "static_definition",
                "entity_ids": [check_id],
                "reason": "missing patterns",
            },
        )
    path = worktree / safe_relative_path(raw_path)
    if not path.is_file():
        return (
            {
                "check_id": check_id,
                "result": "fail",
                "path": raw_path,
                "patterns": [],
                "reason": "expected target file is missing",
            },
            None,
        )
    text = path.read_text(encoding="utf-8", errors="replace")
    pattern_results: list[dict[str, Any]] = []
    all_match = True
    for item in patterns:
        if not isinstance(item, dict) or not isinstance(item.get("regex"), str):
            return (
                {"check_id": check_id, "result": "error", "reason": "invalid pattern entry"},
                {
                    "kind": "static_definition",
                    "entity_ids": [check_id],
                    "reason": "invalid pattern entry",
                },
            )
        try:
            match = re.search(item["regex"], text, re.MULTILINE | re.DOTALL)
        except re.error as exc:
            return (
                {"check_id": check_id, "result": "error", "reason": f"invalid regex: {exc}"},
                {
                    "kind": "static_definition",
                    "entity_ids": [check_id],
                    "reason": f"invalid regex: {exc}",
                },
            )
        matched = match is not None
        all_match = all_match and matched
        pattern_results.append(
            {
                "label": item.get("label", ""),
                "regex": item["regex"],
                "matched": matched,
                "line": _line_number(text, match.start()) if match else None,
            }
        )
    return (
        {
            "check_id": check_id,
            "result": "pass" if all_match else "fail",
            "path": raw_path,
            "rule_refs": check.get("rule_refs", []),
            "patterns": pattern_results,
        },
        None,
    )


def _command_list(value: Any) -> list[str]:
    if isinstance(value, list) and all(isinstance(item, str) for item in value):
        return value
    if isinstance(value, str) and value:
        return shlex.split(value)
    return []


def _matches_blocker(log: str, test: dict[str, Any]) -> bool:
    patterns = list(DEFAULT_BLOCKER_PATTERNS)
    configured = test.get("blocker_patterns", [])
    if isinstance(configured, list):
        patterns.extend(str(item) for item in configured)
    return any(re.search(pattern, log, re.IGNORECASE) for pattern in patterns)


def _run_dynamic_test(
    worktree: Path,
    test_id: str,
    test: dict[str, Any],
    log_path: Path,
    blocked_by_patch: bool,
) -> tuple[dict[str, Any], dict[str, Any] | None]:
    if test.get("enabled", True) is False:
        atomic_write_text(log_path, "test disabled by mapping\n")
        return {"test_id": test_id, "result": "skipped", "log": str(log_path)}, None
    if blocked_by_patch:
        atomic_write_text(log_path, "test injection failed; command not run\n")
        return (
            {"test_id": test_id, "result": "not_run", "log": str(log_path)},
            {
                "kind": "test_injection",
                "entity_ids": [test_id],
                "reason": "test patch was not applied",
                "log": str(log_path),
            },
        )
    command = _command_list(test.get("command"))
    if not command:
        atomic_write_text(log_path, "dynamic test has no execution command\n")
        return (
            {"test_id": test_id, "result": "not_run", "log": str(log_path)},
            {
                "kind": "dynamic_binding",
                "entity_ids": [test_id],
                "reason": "dynamic test has no execution command",
                "log": str(log_path),
            },
        )
    raw_cwd = test.get("working_directory", ".")
    if not isinstance(raw_cwd, str):
        raw_cwd = "."
    cwd = worktree / safe_relative_path(raw_cwd)
    timeout = test.get("timeout_seconds", 1800)
    if not isinstance(timeout, int) or timeout <= 0:
        timeout = 1800
    environment = os.environ.copy()
    configured_env = test.get("environment", {})
    if isinstance(configured_env, dict):
        environment.update({str(key): str(value) for key, value in configured_env.items()})
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout,
            env=environment,
        )
        log = result.stdout + result.stderr
        atomic_write_text(log_path, log)
    except subprocess.TimeoutExpired as exc:
        log = (exc.stdout or "") + (exc.stderr or "")
        atomic_write_text(log_path, log + f"\nTIMEOUT after {timeout}s\n")
        return (
            {
                "test_id": test_id,
                "result": "not_run",
                "command": command,
                "log": str(log_path),
            },
            {
                "kind": "environment",
                "entity_ids": [test_id],
                "reason": f"command timed out after {timeout}s",
                "log": str(log_path),
            },
        )
    row = {
        "test_id": test_id,
        "result": "pass" if result.returncode == 0 else "fail",
        "exit_code": result.returncode,
        "command": command,
        "rule_refs": test.get("rule_refs", []),
        "log": str(log_path),
    }
    if result.returncode != 0 and _matches_blocker(log, test):
        row["result"] = "not_run"
        return (
            row,
            {
                "kind": "environment",
                "entity_ids": [test_id],
                "reason": "command failed before reliable implementation evidence was produced",
                "log": str(log_path),
            },
        )
    return row, None


def _syscalls_for_rules(
    rule_syscalls: dict[str, list[str]], rule_refs: list[str], explicit: Any
) -> list[str]:
    selected = {
        syscall
        for rule_id in rule_refs
        for syscall in rule_syscalls.get(rule_id, [])
        if isinstance(syscall, str)
    }
    if isinstance(explicit, list) and all(isinstance(item, str) for item in explicit):
        selected.intersection_update(explicit)
    return sorted(selected)


def _finding_entities(
    root: Path,
    run_id: str,
    target_snapshot_hash: str,
    rule_syscalls: dict[str, list[str]],
    static_results: list[dict[str, Any]],
    dynamic_results: list[dict[str, Any]],
    checks: dict[str, dict[str, Any]],
    tests: dict[str, dict[str, Any]],
    result_version: dict[str, str],
    generated_at: str,
) -> dict[str, dict[str, Any]]:
    findings: dict[str, dict[str, Any]] = {}
    evidence_rows: list[tuple[str, dict[str, Any], dict[str, Any]]] = []
    for row in static_results:
        if row.get("result") == "fail":
            evidence_rows.append(("static", row, checks[row["check_id"]]))
    for row in dynamic_results:
        if row.get("result") == "fail":
            evidence_rows.append(("dynamic", row, tests[row["test_id"]]))
    for evidence_kind, result, definition in evidence_rows:
        refs = definition.get("rule_refs", [])
        if not isinstance(refs, list):
            refs = []
        for rule_id in refs or ["unmapped-rule"]:
            syscalls = _syscalls_for_rules(
                rule_syscalls,
                [str(rule_id)],
                definition.get("applies_to_syscalls"),
            )
            if refs and not syscalls:
                continue
            for syscall in syscalls or ["unmapped-syscall"]:
                snapshot_suffix = target_snapshot_hash.removeprefix("sha256:")[:12]
                finding_id = f"finding-{slug(syscall)}-{slug(str(rule_id))}-{snapshot_suffix}"
                existing_path = root / "targets/starry/findings" / f"{slug(finding_id)}.yaml"
                if finding_id in findings:
                    existing = findings[finding_id]
                else:
                    existing = load_mapping(existing_path) if existing_path.exists() else {}
                occurrences = existing.get("occurrences", [])
                if not isinstance(occurrences, list):
                    occurrences = []
                occurrence = {
                    "check_run": run_id,
                    "evidence_kind": evidence_kind,
                    "result": result,
                }
                if content_hash(occurrence) not in {content_hash(item) for item in occurrences}:
                    occurrences.append(occurrence)
                changed = content_hash(occurrences) != content_hash(existing.get("occurrences", []))
                findings[finding_id] = {
                    "schema_version": SCHEMA_VERSION,
                    "kind": "syscallguard_starry_finding",
                    "finding_id": finding_id,
                    "syscall": syscall,
                    "rule_id": rule_id,
                    "target_snapshot_hash": target_snapshot_hash,
                    "status": "confirmed",
                    "resolution": existing.get("resolution", "open"),
                    "occurrences": occurrences,
                    "generated_at_utc": generated_at
                    if changed or not existing.get("generated_at_utc")
                    else existing["generated_at_utc"],
                    "upstream_dependencies": [result_version],
                }
    return findings


def _write_report(recorder: RunRecorder, results: dict[str, Any]) -> None:
    lines = [
        "# Starry Compliance Check",
        "",
        f"Run: `{recorder.run_id}`",
        f"Status: `{recorder.manifest['status']}`",
        f"Worktree: `{recorder.manifest.get('worktree', '')}`",
        "",
        f"- Static pass: {sum(row['result'] == 'pass' for row in results['static'])}",
        f"- Static fail: {sum(row['result'] == 'fail' for row in results['static'])}",
        f"- Dynamic pass: {sum(row['result'] == 'pass' for row in results['dynamic'])}",
        f"- Dynamic fail: {sum(row['result'] == 'fail' for row in results['dynamic'])}",
        f"- Dynamic skipped/not run: {sum(row['result'] in {'skipped', 'not_run'} for row in results['dynamic'])}",
        f"- Confirmed findings: {len(recorder.manifest.get('entities', {}).get('findings', []))}",
        f"- Environment blockers: {len(recorder.manifest.get('blockers', []))}",
    ]
    atomic_write_text(recorder.directory / "report.md", "\n".join(lines) + "\n")


def run_check(
    from_run_id: str,
    root: Path | None = None,
    requested_run_id: str | None = None,
) -> str:
    root = (root or repo_root()).resolve()
    mapping_report = load_mapping_report(root, from_run_id)
    run_id = requested_run_id or new_run_id(
        "check", {"from": from_run_id, "at": utc_now()}
    )
    recorder = RunRecorder(root, "check", run_id, {"from": from_run_id}, from_run_id)
    try:
        target = mapping_report.get("target", {})
        repository = Path(str(target.get("repository", ""))).expanduser().resolve()
        revision_ref = str(_mapping_target_descriptor(mapping_report).get("revision", "HEAD"))
        mapped_snapshot = str(target.get("snapshot_hash", ""))
        if not repository.is_dir() or not mapped_snapshot:
            raise SyscallGuardError(f"mapping report {from_run_id} has invalid target metadata")
        current_snapshot = repository_snapshot_hash(repository)
        entities, hashes, input_hash = _current_input(root, mapping_report)
        versions = _current_versions(entities)
        recorder.manifest["input_hash"] = input_hash
        recorder.manifest["entity_hashes"] = hashes
        recorder.manifest["entity_versions"] = versions
        recorder.manifest["target"] = dict(target)
        recorder.manifest["entities"] = {
            key: sorted(values) for key, values in entities.items()
        }
        recorder.manifest["rule_syscalls"] = mapping_report.get("rule_syscalls", {})
        stale_reasons = _mapping_staleness(mapping_report, entities)
        if current_snapshot != mapped_snapshot or stale_reasons:
            blocker = {
                "kind": "stale_mapping",
                "reason": "mapping dependencies or Starry content changed; run map-starry-checks again",
                "mapped_snapshot_hash": mapped_snapshot,
                "current_snapshot_hash": current_snapshot,
                "dependency_mismatches": stale_reasons,
            }
            recorder.manifest["counts"] = {"skipped_stale_mapping": 1, "findings": 0}
            recorder.complete([blocker])
            _write_report(recorder, {"static": [], "dynamic": []})
            recorder.flush()
            return run_id

        prior = _prior_identical_check(root, input_hash, run_id)
        if prior is not None:
            recorder.manifest["reused_run"] = prior["run_id"]
            recorder.manifest["entities"]["findings"] = prior.get("entities", {}).get("findings", [])
            generated_at = utc_now()
            prior_results_path = root / "runs" / str(prior["run_id"]) / "results.yaml"
            prior_results = load_mapping(prior_results_path) if prior_results_path.is_file() else {}
            dependencies = [
                version
                for kind in ("static_checks", "dynamic_tests")
                for _entity_id, version in sorted(versions[kind].items())
            ]
            reused_results = {
                "schema_version": SCHEMA_VERSION,
                "kind": "syscallguard_check_results",
                "run_id": run_id,
                "generated_at_utc": generated_at,
                "upstream_dependencies": dependencies,
                "target_snapshot_hash": mapped_snapshot,
                "reused_from": prior["run_id"],
                "static": prior_results.get("static", []),
                "dynamic": prior_results.get("dynamic", []),
                "blockers": prior.get("blockers", []),
            }
            atomic_write_yaml(recorder.directory / "results.yaml", reused_results)
            recorder.manifest["result_version"] = entity_version(run_id, reused_results)
            finding_versions: dict[str, dict[str, str]] = {}
            for finding_id in recorder.manifest["entities"]["findings"]:
                finding_path = root / "targets/starry/findings" / f"{slug(finding_id)}.yaml"
                finding_versions[finding_id] = entity_version(
                    finding_id, load_mapping(finding_path)
                )
            recorder.manifest["entity_versions"]["findings"] = finding_versions
            recorder.manifest["counts"] = {
                "skipped_unchanged": 1,
                "findings": len(recorder.manifest["entities"]["findings"]),
            }
            recorder.manifest["outputs"] = {"results": "results.yaml", "report": "report.md"}
            blockers = prior.get("blockers", [])
            recorder.complete(blockers if isinstance(blockers, list) else [])
            _write_report(recorder, {"static": [], "dynamic": []})
            recorder.flush()
            return run_id

        worktree = _worktree_path(mapping_report, run_id)
        _create_worktree(repository, revision_ref, worktree)
        if repository_snapshot_hash(worktree) != mapped_snapshot:
            raise SyscallGuardError("isolated Starry worktree does not match the mapped content snapshot")
        recorder.manifest["worktree"] = str(worktree)
        logs = recorder.directory / "logs"
        logs.mkdir(parents=True, exist_ok=True)
        blocked_tests, blockers = _apply_test_patches(
            root, worktree, entities["dynamic_tests"], logs
        )

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

        generated_at = utc_now()
        result_dependencies = [
            version
            for kind in ("static_checks", "dynamic_tests")
            for _entity_id, version in sorted(versions[kind].items())
        ]
        results = {
            "schema_version": SCHEMA_VERSION,
            "kind": "syscallguard_check_results",
            "run_id": run_id,
            "generated_at_utc": generated_at,
            "upstream_dependencies": result_dependencies,
            "target_snapshot_hash": mapped_snapshot,
            "worktree": str(worktree),
            "static": static_results,
            "dynamic": dynamic_results,
            "blockers": blockers,
        }
        atomic_write_yaml(recorder.directory / "results.yaml", results)
        result_version = entity_version(run_id, results)
        findings = _finding_entities(
            root,
            run_id,
            mapped_snapshot,
            mapping_report.get("rule_syscalls", {}),
            static_results,
            dynamic_results,
            entities["static_checks"],
            entities["dynamic_tests"],
            result_version,
            generated_at,
        )
        publish_yaml_entities(
            [
                (
                    recorder.directory,
                    root / "targets/starry/findings" / f"{slug(finding_id)}.yaml",
                    finding,
                )
                for finding_id, finding in findings.items()
            ]
        )
        update_index(
            root / "targets/starry/findings/index.yaml",
            "syscallguard_starry_finding_index",
            [
                {
                    "id": finding_id,
                    "path": f"targets/starry/findings/{slug(finding_id)}.yaml",
                    "syscall": finding["syscall"],
                    "rule_id": finding["rule_id"],
                    "target_snapshot_hash": mapped_snapshot,
                    "status": finding["status"],
                    "resolution": finding["resolution"],
                    "generated_at_utc": finding["generated_at_utc"],
                    "content_hash": version_content_hash(finding),
                }
                for finding_id, finding in findings.items()
            ],
        )
        recorder.manifest["result_version"] = result_version
        recorder.manifest["entity_versions"]["findings"] = {
            finding_id: entity_version(finding_id, finding)
            for finding_id, finding in findings.items()
        }
        recorder.manifest["entities"]["findings"] = sorted(findings)
        recorder.manifest["counts"] = {
            "static_pass": sum(row["result"] == "pass" for row in static_results),
            "static_fail": sum(row["result"] == "fail" for row in static_results),
            "dynamic_pass": sum(row["result"] == "pass" for row in dynamic_results),
            "dynamic_fail": sum(row["result"] == "fail" for row in dynamic_results),
            "dynamic_skipped": sum(row["result"] == "skipped" for row in dynamic_results),
            "dynamic_not_run": sum(row["result"] == "not_run" for row in dynamic_results),
            "findings": len(findings),
            "blockers": len(blockers),
        }
        recorder.manifest["outputs"] = {
            "results": "results.yaml",
            "report": "report.md",
            "logs": "logs/",
            "finding_index": "targets/starry/findings/index.yaml",
        }
        recorder.complete(blockers)
        _write_report(recorder, results)
        recorder.flush()
        return run_id
    except BaseException as exc:
        recorder.fail(exc)
        if isinstance(exc, SyscallGuardError):
            raise
        raise SyscallGuardError(str(exc)) from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Check Starry compliance in an isolated worktree")
    parser.add_argument("--from", dest="from_run_id", required=True, help="mapping report id")
    parser.add_argument("--root", type=Path, default=repo_root(), help=argparse.SUPPRESS)
    parser.add_argument("--run-id", help=argparse.SUPPRESS)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    requested_run_id = args.run_id or new_run_id("check", {"from": args.from_run_id})
    try:
        run_id = run_check(args.from_run_id, args.root, requested_run_id)
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
    print(f"finding_index: {args.root.resolve() / 'targets/starry/findings/index.yaml'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
