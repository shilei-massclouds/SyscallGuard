from __future__ import annotations

import argparse
import os
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

from .common import (
    SCHEMA_VERSION,
    SyscallGuardError,
    atomic_write_text,
    content_hash,
    dependency_mismatch,
    ensure_target_workspace,
    entity_version,
    git,
    load_index,
    load_mapping,
    new_run_id,
    normalize_run_id,
    read_frontmatter,
    repository_snapshot_hash,
    repo_root,
    safe_relative_path,
    slug,
    transactional_write,
    utc_now,
    version_content_hash,
    yaml_text,
)
from .mapping import load_mapping_report


REPORT_KIND = "syscallguard_check_report"
TEMP_ROOT = Path(os.environ.get("SYSCALLGUARD_CHECK_TEMP_ROOT", "/tmp/syscallguard-check"))
MAX_OUTPUT_EVIDENCE_BYTES = 8 * 1024
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
    entities = {"rules": rules, "static_checks": checks, "dynamic_tests": tests}
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
            "target_branch": mapping_report.get("target", {}).get("branch"),
            "repository_identity": mapping_report.get("target", {}).get(
                "repository_identity"
            ),
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


def _scope_for_entities(
    entities: dict[str, dict[str, dict[str, Any]]]
) -> dict[str, list[str]]:
    return {kind: sorted(rows) for kind, rows in entities.items()}


def _load_open_finding_index(root: Path) -> dict[str, dict[str, Any]]:
    """Load every open confirmed finding named by the shared index."""
    index = load_index(
        root / "targets/starry/findings/index.yaml",
        "syscallguard_starry_finding_index",
    )
    findings: dict[str, dict[str, Any]] = {}
    for row in index["entities"]:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str):
            raise SyscallGuardError("finding index contains an invalid entry")
        finding_id = row["id"]
        raw_path = row.get(
            "path", f"targets/starry/findings/{slug(finding_id)}.yaml"
        )
        if not isinstance(raw_path, str):
            raise SyscallGuardError(f"finding index path is invalid for {finding_id}")
        path = root / safe_relative_path(raw_path)
        finding = load_mapping(path)
        if (
            finding.get("kind") != "syscallguard_starry_finding"
            or finding.get("finding_id") != finding_id
        ):
            raise SyscallGuardError(f"invalid finding entity: {path}")
        recorded_generation = row.get("generated_at_utc")
        recorded_hash = row.get("content_hash")
        if (
            recorded_generation != finding.get("generated_at_utc")
            or recorded_hash != version_content_hash(finding)
        ):
            raise SyscallGuardError(
                f"finding index version is stale for {finding_id}"
            )
        if finding.get("status") == "confirmed" and finding.get("resolution") == "open":
            findings[finding_id] = finding
    return findings


def _finding_sources(finding: dict[str, Any]) -> set[tuple[str, str]]:
    sources: set[tuple[str, str]] = set()
    occurrences = finding.get("occurrences", [])
    if not isinstance(occurrences, list):
        return sources
    for occurrence in occurrences:
        if not isinstance(occurrence, dict):
            continue
        kind = occurrence.get("evidence_kind")
        source_id = occurrence.get("source_id")
        if kind in {"static", "dynamic"} and isinstance(source_id, str):
            sources.add((kind, source_id))
    return sources


def _extend_revalidation_scope(
    root: Path,
    entities: dict[str, dict[str, dict[str, Any]]],
    findings: dict[str, dict[str, Any]],
    current_snapshot: str,
) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """Add executable sources for open findings from older target snapshots."""
    added = {"rules": set(), "static_checks": set(), "dynamic_tests": set()}
    unresolved: dict[str, list[str]] = {}
    for finding_id, finding in findings.items():
        if finding.get("target_snapshot_hash") == current_snapshot:
            continue
        for evidence_kind, source_id in sorted(_finding_sources(finding)):
            section = "static_checks" if evidence_kind == "static" else "dynamic_tests"
            directory = (
                "targets/starry/static-checks"
                if evidence_kind == "static"
                else "targets/starry/dynamic-tests"
            )
            id_field = "check_id" if evidence_kind == "static" else "test_id"
            expected_kind = (
                "syscallguard_starry_static_check"
                if evidence_kind == "static"
                else "syscallguard_starry_dynamic_test"
            )
            if source_id not in entities[section]:
                try:
                    loaded, _hashes = _load_entities(
                        root, [source_id], directory, id_field, expected_kind
                    )
                    entity_version(source_id, loaded[source_id])
                except SyscallGuardError as exc:
                    unresolved.setdefault(finding_id, []).append(str(exc))
                    continue
                entities[section][source_id] = loaded[source_id]
                added[section].add(source_id)
            definition = entities[section][source_id]
            refs = definition.get("rule_refs", [])
            if not isinstance(refs, list):
                refs = []
            for raw_rule_id in refs:
                rule_id = str(raw_rule_id)
                if rule_id in entities["rules"]:
                    continue
                try:
                    loaded, _hashes = _load_entities(
                        root,
                        [rule_id],
                        "library/rules",
                        "rule_id",
                        "syscallguard_rule",
                    )
                    entity_version(rule_id, loaded[rule_id])
                except SyscallGuardError as exc:
                    unresolved.setdefault(finding_id, []).append(str(exc))
                    continue
                entities["rules"][rule_id] = loaded[rule_id]
                added["rules"].add(rule_id)
    return (
        {kind: sorted(ids) for kind, ids in added.items()},
        {finding_id: sorted(set(reasons)) for finding_id, reasons in unresolved.items()},
    )


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


def load_check_report(root: Path, report_id: str) -> dict[str, Any]:
    report_id = normalize_run_id(report_id)
    path = root / "runs" / report_id / "report.md"
    report, _body = read_frontmatter(path)
    if report.get("kind") != REPORT_KIND or report.get("report_id") != report_id:
        raise SyscallGuardError(f"not a SyscallGuard check report: {path}")
    if report.get("status") not in {"completed", "completed_with_blockers"}:
        raise SyscallGuardError(
            f"check report {report_id} is not readable: status={report.get('status')!r}"
        )
    recorded_hash = report.get("content_hash")
    if not isinstance(recorded_hash, str) or recorded_hash != version_content_hash(report):
        raise SyscallGuardError(f"check report content hash mismatch: {path}")
    return report


def _prior_identical_check(root: Path, input_hash: str, current_report_id: str) -> dict[str, Any] | None:
    runs_root = root / "runs"
    if not runs_root.is_dir():
        return None
    candidates: list[dict[str, Any]] = []
    for report_path in sorted(runs_root.glob("check-*/report.md"), reverse=True):
        if report_path.parent.name == current_report_id:
            continue
        try:
            report = load_check_report(root, report_path.parent.name)
        except SyscallGuardError:
            continue
        if report.get("input_hash") == input_hash:
            candidates.append(report)
    return candidates[0] if candidates else None


def _check_workspace(report_id: str) -> Path:
    return TEMP_ROOT / normalize_run_id(report_id)


def _artifact_path(root: Path, value: str) -> Path:
    path = Path(value).expanduser()
    return path.resolve() if path.is_absolute() else (root / path).resolve()


def _apply_test_patches(
    root: Path,
    worktree: Path,
    tests: dict[str, dict[str, Any]],
    logs: Path,
) -> tuple[set[str], list[dict[str, Any]], set[str]]:
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
                    "diagnostic_log": str(log_path),
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
                    "diagnostic_log": str(log_path),
                }
            )
            blocked_tests.update(test_ids)
        else:
            applied.add(patch_value)
    return blocked_tests, blockers, applied


def _revert_test_patches(
    root: Path,
    repository: Path,
    applied: set[str],
    logs: Path,
) -> list[dict[str, Any]]:
    blockers: list[dict[str, Any]] = []
    for patch_value in sorted(applied, reverse=True):
        patch = _artifact_path(root, patch_value)
        log_path = logs / f"patch-revert-{slug(patch.name)}.log"
        result = git(
            repository,
            ["apply", "--reverse", "--whitespace=nowarn", str(patch)],
            check=False,
        )
        atomic_write_text(log_path, result.stdout + result.stderr)
        if result.returncode != 0:
            blockers.append(
                {
                    "kind": "test_cleanup",
                    "entity_ids": [patch_value],
                    "reason": "injected dynamic test patch could not be reverted",
                    "diagnostic_log": str(log_path),
                }
            )
    return blockers


def _line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _run_static_check(
    worktree: Path, check_id: str, check: dict[str, Any]
) -> tuple[dict[str, Any], dict[str, Any] | None]:
    raw_path = check.get("path")
    patterns = check.get("patterns")
    base = {"check_id": check_id, "rule_refs": check.get("rule_refs", [])}
    if not isinstance(raw_path, str) or not raw_path:
        row = {**base, "result": "error", "reason": "missing path"}
        return row, {"kind": "static_definition", "entity_ids": [check_id], "reason": "missing path"}
    if not isinstance(patterns, list) or not patterns:
        row = {**base, "result": "error", "reason": "missing patterns"}
        return row, {
            "kind": "static_definition",
            "entity_ids": [check_id],
            "reason": "missing patterns",
        }
    path = worktree / safe_relative_path(raw_path)
    if not path.is_file():
        return (
            {
                **base,
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
            row = {**base, "result": "error", "reason": "invalid pattern entry"}
            return row, {
                "kind": "static_definition",
                "entity_ids": [check_id],
                "reason": "invalid pattern entry",
            }
        try:
            match = re.search(item["regex"], text, re.MULTILINE | re.DOTALL)
        except re.error as exc:
            reason = f"invalid regex: {exc}"
            row = {**base, "result": "error", "reason": reason}
            return row, {"kind": "static_definition", "entity_ids": [check_id], "reason": reason}
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
            **base,
            "result": "pass" if all_match else "fail",
            "path": raw_path,
            "patterns": pattern_results,
            "reason": "all required patterns matched" if all_match else "one or more required patterns did not match",
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


def _as_text(value: str | bytes | None) -> str:
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    return value or ""


def _output_tail(text: str, limit: int = MAX_OUTPUT_EVIDENCE_BYTES) -> tuple[str, bool]:
    encoded = text.encode("utf-8", errors="replace")
    if len(encoded) <= limit:
        return text, False
    return encoded[-limit:].decode("utf-8", errors="ignore"), True


def _run_dynamic_test(
    worktree: Path,
    test_id: str,
    test: dict[str, Any],
    log_path: Path,
    blocked_by_patch: bool,
) -> tuple[dict[str, Any], dict[str, Any] | None]:
    base = {"test_id": test_id, "rule_refs": test.get("rule_refs", [])}
    if test.get("enabled", True) is False:
        atomic_write_text(log_path, "test disabled by mapping\n")
        return {**base, "result": "skipped", "reason": "disabled by mapping"}, None
    if blocked_by_patch:
        atomic_write_text(log_path, "test injection failed; command not run\n")
        blocker = {
            "kind": "test_injection",
            "entity_ids": [test_id],
            "reason": "test patch was not applied",
            "diagnostic_log": str(log_path),
        }
        return (
            {**base, "result": "not_run", "reason": blocker["reason"], "diagnostic_log": str(log_path)},
            blocker,
        )
    command = _command_list(test.get("command"))
    if not command:
        atomic_write_text(log_path, "dynamic test has no execution command\n")
        blocker = {
            "kind": "dynamic_binding",
            "entity_ids": [test_id],
            "reason": "dynamic test has no execution command",
            "diagnostic_log": str(log_path),
        }
        return (
            {**base, "result": "not_run", "reason": blocker["reason"], "diagnostic_log": str(log_path)},
            blocker,
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
        log = _as_text(exc.stdout) + _as_text(exc.stderr)
        atomic_write_text(log_path, log + f"\nTIMEOUT after {timeout}s\n")
        tail, truncated = _output_tail(log)
        blocker = {
            "kind": "environment",
            "entity_ids": [test_id],
            "reason": f"command timed out after {timeout}s",
            "diagnostic_log": str(log_path),
        }
        row = {
            **base,
            "result": "not_run",
            "command": command,
            "reason": blocker["reason"],
            "output_tail": tail,
            "output_truncated": truncated,
            "diagnostic_log": str(log_path),
        }
        return row, blocker
    except OSError as exc:
        reason = f"dynamic command could not be executed: {exc}"
        atomic_write_text(log_path, reason + "\n")
        blocker = {
            "kind": "environment",
            "entity_ids": [test_id],
            "reason": reason,
            "diagnostic_log": str(log_path),
        }
        return (
            {
                **base,
                "result": "not_run",
                "command": command,
                "reason": reason,
                "diagnostic_log": str(log_path),
            },
            blocker,
        )
    tail, truncated = _output_tail(log)
    row = {
        **base,
        "result": "pass" if result.returncode == 0 else "fail",
        "exit_code": result.returncode,
        "command": command,
        "reason": "command exited successfully" if result.returncode == 0 else "command produced reliable implementation failure evidence",
        "output_tail": tail,
        "output_truncated": truncated,
    }
    if result.returncode != 0 and _matches_blocker(log, test):
        row["result"] = "not_run"
        row["reason"] = "command failed before reliable implementation evidence was produced"
        row["diagnostic_log"] = str(log_path)
        blocker = {
            "kind": "environment",
            "entity_ids": [test_id],
            "reason": row["reason"],
            "diagnostic_log": str(log_path),
        }
        return row, blocker
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


def _stable_result(result: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in result.items() if key != "diagnostic_log" and key != "finding_ids"}


def _finding_entities(
    root: Path,
    report_id: str,
    target_snapshot_hash: str,
    rule_syscalls: dict[str, list[str]],
    static_results: list[dict[str, Any]],
    dynamic_results: list[dict[str, Any]],
    checks: dict[str, dict[str, Any]],
    tests: dict[str, dict[str, Any]],
    versions: dict[str, dict[str, dict[str, str]]],
    generated_at: str,
) -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], list[str]]]:
    findings: dict[str, dict[str, Any]] = {}
    result_findings: dict[tuple[str, str], list[str]] = {}
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
        source_id = str(result["check_id"] if evidence_kind == "static" else result["test_id"])
        for raw_rule_id in refs or ["unmapped-rule"]:
            rule_id = str(raw_rule_id)
            syscalls = _syscalls_for_rules(
                rule_syscalls, [rule_id], definition.get("applies_to_syscalls")
            )
            if refs and not syscalls:
                continue
            for syscall in syscalls or ["unmapped-syscall"]:
                snapshot_suffix = target_snapshot_hash.removeprefix("sha256:")[:12]
                finding_id = f"finding-{slug(syscall)}-{slug(rule_id)}-{snapshot_suffix}"
                existing_path = root / "targets/starry/findings" / f"{slug(finding_id)}.yaml"
                if finding_id in findings:
                    existing = findings[finding_id]
                else:
                    existing = load_mapping(existing_path) if existing_path.exists() else {}
                occurrences = existing.get("occurrences", [])
                if not isinstance(occurrences, list):
                    occurrences = []
                occurrence = {
                    "check_report_id": report_id,
                    "evidence_kind": evidence_kind,
                    "source_id": source_id,
                    "evidence": _stable_result(result),
                }
                if content_hash(occurrence) not in {content_hash(item) for item in occurrences}:
                    occurrences.append(occurrence)
                changed = content_hash(occurrences) != content_hash(existing.get("occurrences", []))
                dependencies = [versions[f"{evidence_kind}_checks" if evidence_kind == "static" else "dynamic_tests"][source_id]]
                if rule_id in versions["rules"]:
                    dependencies.append(versions["rules"][rule_id])
                dependency_rows = existing.get("upstream_dependencies", [])
                if not isinstance(dependency_rows, list):
                    dependency_rows = []
                by_dependency = {
                    str(row.get("id")): row
                    for row in dependency_rows + dependencies
                    if isinstance(row, dict) and isinstance(row.get("id"), str)
                }
                findings[finding_id] = {
                    "schema_version": SCHEMA_VERSION,
                    "kind": "syscallguard_starry_finding",
                    "finding_id": finding_id,
                    "syscall": syscall,
                    "rule_id": rule_id,
                    "target_snapshot_hash": target_snapshot_hash,
                    "status": "confirmed",
                    "resolution": "open",
                    "occurrences": occurrences,
                    "generated_at_utc": generated_at
                    if changed or not existing.get("generated_at_utc")
                    else existing["generated_at_utc"],
                    "upstream_dependencies": [
                        by_dependency[key] for key in sorted(by_dependency)
                    ],
                }
                result_findings.setdefault((evidence_kind, source_id), []).append(finding_id)
    for key in result_findings:
        result_findings[key] = sorted(set(result_findings[key]))
    return findings, result_findings


def _annotate_findings(
    static_results: list[dict[str, Any]],
    dynamic_results: list[dict[str, Any]],
    result_findings: dict[tuple[str, str], list[str]],
) -> None:
    for row in static_results:
        row["finding_ids"] = result_findings.get(("static", str(row["check_id"])), [])
    for row in dynamic_results:
        row["finding_ids"] = result_findings.get(("dynamic", str(row["test_id"])), [])


def _counts(
    static_results: list[dict[str, Any]],
    dynamic_results: list[dict[str, Any]],
    findings: dict[str, Any],
    blockers: list[dict[str, Any]],
    lifecycle: dict[str, list[str]] | None = None,
) -> dict[str, int]:
    result = {
        "static_pass": sum(row.get("result") == "pass" for row in static_results),
        "static_fail": sum(row.get("result") == "fail" for row in static_results),
        "static_error": sum(row.get("result") == "error" for row in static_results),
        "dynamic_pass": sum(row.get("result") == "pass" for row in dynamic_results),
        "dynamic_fail": sum(row.get("result") == "fail" for row in dynamic_results),
        "dynamic_skipped": sum(row.get("result") == "skipped" for row in dynamic_results),
        "dynamic_not_run": sum(row.get("result") == "not_run" for row in dynamic_results),
        "findings": len(findings),
        "blockers": len(blockers),
    }
    for key, ids in (lifecycle or {}).items():
        result[key] = len(ids)
    return result


def _finding_index(
    root: Path, findings: dict[str, dict[str, Any]], generated_at: str
) -> dict[str, Any]:
    path = root / "targets/starry/findings/index.yaml"
    index = load_index(path, "syscallguard_starry_finding_index")
    by_id = {
        str(row["id"]): row
        for row in index["entities"]
        if isinstance(row, dict) and isinstance(row.get("id"), str)
    }
    for finding_id, finding in findings.items():
        by_id[finding_id] = {
            "id": finding_id,
            "path": f"targets/starry/findings/{slug(finding_id)}.yaml",
            "syscall": finding["syscall"],
            "rule_id": finding["rule_id"],
            "target_snapshot_hash": finding["target_snapshot_hash"],
            "status": finding["status"],
            "resolution": finding["resolution"],
            "generated_at_utc": finding["generated_at_utc"],
            "content_hash": version_content_hash(finding),
        }
    index["entities"] = [by_id[key] for key in sorted(by_id)]
    index["updated_at_utc"] = generated_at
    return index


def _result_syscalls(
    definition: dict[str, Any], rule_syscalls: dict[str, list[str]]
) -> list[str]:
    refs = definition.get("rule_refs", [])
    return _syscalls_for_rules(
        rule_syscalls,
        [str(item) for item in refs] if isinstance(refs, list) else [],
        definition.get("applies_to_syscalls"),
    )


def _md(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def _report_text(
    metadata: dict[str, Any],
    checks: dict[str, dict[str, Any]],
    tests: dict[str, dict[str, Any]],
) -> str:
    counts = metadata["counts"]
    relation = metadata["rule_syscalls"]
    lines = [
        "# Starry 合规检查报告",
        "",
        "## 本轮结论",
        "",
        f"- 状态：`{metadata['status']}`",
        f"- 静态检查：pass {counts['static_pass']}、fail {counts['static_fail']}、error {counts['static_error']}",
        f"- 动态测试：pass {counts['dynamic_pass']}、fail {counts['dynamic_fail']}、skipped {counts['dynamic_skipped']}、not_run {counts['dynamic_not_run']}",
        f"- confirmed finding：{counts['findings']}",
        f"- 新增：{counts.get('new_findings', 0)}、carry forward：{counts.get('carried_findings', 0)}、已重验：{counts.get('revalidated_findings', 0)}、待重验：{counts.get('needs_revalidation', 0)}",
        f"- 环境或执行 blocker：{counts['blockers']}（不视为实现缺口）",
        "",
        "## 静态检查",
        "",
    ]
    if not metadata["static"]:
        lines.extend(["本轮没有静态检查。", ""])
    for row in metadata["static"]:
        check_id = str(row["check_id"])
        definition = checks.get(check_id, {})
        syscalls = _result_syscalls(definition, relation)
        refs = definition.get("rule_refs", [])
        lines.extend(
            [
                f"### `{check_id}`",
                "",
                f"- 类型：`static`",
                f"- 关联 syscall：{('、'.join(f'`{item}`' for item in syscalls) or '—')}",
                f"- 通用规则：{('、'.join(f'`{item}`' for item in refs) or '—')}",
                f"- 结果：`{row['result']}`",
                f"- 原因：{_md(row.get('reason', ''))}",
            ]
        )
        patterns = row.get("patterns", [])
        if patterns:
            lines.extend(["- pattern 证据：", ""])
            for pattern in patterns:
                location = f"第 {pattern['line']} 行" if pattern.get("line") else "未匹配"
                lines.append(
                    f"  - `{_md(pattern.get('regex', ''))}`：matched=`{str(bool(pattern.get('matched'))).lower()}`，{location}"
                )
        finding_ids = row.get("finding_ids", [])
        lines.extend(
            [
                f"- finding：{('、'.join(f'`{item}`' for item in finding_ids) or '—')}",
                "",
            ]
        )
    lines.extend(["## 动态测试", ""])
    if not metadata["dynamic"]:
        lines.extend(["本轮没有动态测试。", ""])
    for row in metadata["dynamic"]:
        test_id = str(row["test_id"])
        definition = tests.get(test_id, {})
        syscalls = _result_syscalls(definition, relation)
        refs = definition.get("rule_refs", [])
        lines.extend(
            [
                f"### `{test_id}`",
                "",
                "- 类型：`dynamic`",
                f"- 关联 syscall：{('、'.join(f'`{item}`' for item in syscalls) or '—')}",
                f"- 通用规则：{('、'.join(f'`{item}`' for item in refs) or '—')}",
                f"- 结果：`{row['result']}`",
                f"- 原因：{_md(row.get('reason', ''))}",
            ]
        )
        if "exit_code" in row:
            lines.append(f"- 退出码：`{row['exit_code']}`")
        output = row.get("output_tail")
        if output:
            lines.extend(["- 精简输出证据：", "", "```text", str(output).rstrip(), "```"])
        finding_ids = row.get("finding_ids", [])
        lines.extend(
            [
                f"- finding：{('、'.join(f'`{item}`' for item in finding_ids) or '—')}",
                "",
            ]
        )
    blockers = metadata.get("blockers", [])
    if blockers:
        lines.extend(["## Blockers（非实现缺口）", ""])
        for blocker in blockers:
            ids = blocker.get("entity_ids", [])
            lines.append(
                f"- `{blocker.get('kind', 'unknown')}` {('、'.join(f'`{item}`' for item in ids))}：{_md(blocker.get('reason', ''))}"
            )
        lines.append("")
    lines.extend(
        [
            "<details>",
            "<summary>机器可读元数据</summary>",
            "",
            "<!-- syscallguard-metadata -->",
            "```yaml",
            yaml_text(metadata).rstrip(),
            "```",
            "</details>",
        ]
    )
    return "\n".join(lines) + "\n"


def _base_metadata(
    report_id: str,
    mapping_report_id: str,
    mapping_report: dict[str, Any],
    input_hash: str,
    hashes: dict[str, dict[str, str]],
    versions: dict[str, dict[str, dict[str, str]]],
) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "kind": REPORT_KIND,
        "report_id": report_id,
        "status": "completed",
        "generated_at_utc": utc_now(),
        "mapping_report_id": mapping_report_id,
        "mapping_report_version": entity_version(mapping_report_id, mapping_report),
        "target": dict(mapping_report.get("target", {})),
        "input_hash": input_hash,
        "entity_hashes": hashes,
        "entity_versions": versions,
        "base_execution_scope": {
            key: sorted(values)
            for key, values in mapping_report.get("execution_scope", {}).items()
            if key in {"rules", "static_checks", "dynamic_tests"}
        },
        "revalidation_scope": {
            "rules": [],
            "static_checks": [],
            "dynamic_tests": [],
        },
        "effective_execution_scope": {},
        "execution_scope": {},
        "rule_syscalls": mapping_report.get("rule_syscalls", {}),
        "static": [],
        "dynamic": [],
        "counts": {},
        "blockers": [],
        "finding_ids": [],
        "finding_versions": {},
        "new_finding_ids": [],
        "carried_finding_ids": [],
        "revalidated_finding_ids": [],
        "needs_revalidation_finding_ids": [],
    }


def _seal_metadata(metadata: dict[str, Any]) -> None:
    metadata["content_hash"] = version_content_hash(metadata)


def _mark_failure(workspace: Path, exc: BaseException) -> None:
    try:
        atomic_write_text(
            workspace / "failure.yaml",
            yaml_text(
                {
                    "schema_version": SCHEMA_VERSION,
                    "kind": "syscallguard_check_failure",
                    "failed_at_utc": utc_now(),
                    "error": f"{type(exc).__name__}: {exc}",
                }
            ),
        )
    except BaseException:
        pass


def _publish_report(
    root: Path,
    report_id: str,
    metadata: dict[str, Any],
    checks: dict[str, dict[str, Any]],
    tests: dict[str, dict[str, Any]],
    findings: dict[str, dict[str, Any]],
) -> None:
    files: list[tuple[Path, bytes]] = []
    for finding_id, finding in sorted(findings.items()):
        files.append(
            (
                root / "targets/starry/findings" / f"{slug(finding_id)}.yaml",
                yaml_text(finding).encode("utf-8"),
            )
        )
    files.append(
        (
            root / "targets/starry/findings/index.yaml",
            yaml_text(_finding_index(root, findings, metadata["generated_at_utc"])).encode("utf-8"),
        )
    )
    report_path = root / "runs" / report_id / "report.md"
    files.append((report_path, _report_text(metadata, checks, tests).encode("utf-8")))
    transactional_write(files)


def _cleanup_success(workspace: Path) -> None:
    shutil.rmtree(workspace, ignore_errors=True)
    try:
        TEMP_ROOT.rmdir()
    except OSError:
        pass


def _validate_reused_findings(root: Path, prior: dict[str, Any]) -> dict[str, dict[str, str]] | None:
    recorded = prior.get("finding_versions", {})
    ids = prior.get("finding_ids", [])
    if not isinstance(recorded, dict) or not isinstance(ids, list):
        return None
    current: dict[str, dict[str, str]] = {}
    for finding_id in ids:
        if not isinstance(finding_id, str):
            return None
        path = root / "targets/starry/findings" / f"{slug(finding_id)}.yaml"
        if not path.is_file():
            return None
        finding = load_mapping(path)
        version = recorded.get(finding_id)
        if not isinstance(version, dict) or dependency_mismatch(version, finding_id, finding):
            return None
        current[finding_id] = entity_version(finding_id, finding)
    return current


def _source_results(
    static_results: list[dict[str, Any]], dynamic_results: list[dict[str, Any]]
) -> dict[tuple[str, str], str]:
    result: dict[tuple[str, str], str] = {}
    for row in static_results:
        result[("static", str(row.get("check_id", "")))] = str(row.get("result", "error"))
    for row in dynamic_results:
        result[("dynamic", str(row.get("test_id", "")))] = str(row.get("result", "not_run"))
    return result


def _updated_resolution(
    finding: dict[str, Any], resolution: str, generated_at: str, **extra: Any
) -> dict[str, Any]:
    updated = dict(finding)
    updated["resolution"] = resolution
    updated["generated_at_utc"] = generated_at
    for key in ("superseded_by", "fix_ref", "fixed_by_run"):
        if key not in extra:
            updated.pop(key, None)
    updated.update(extra)
    return updated


def _aggregate_findings(
    current_snapshot: str,
    open_findings: dict[str, dict[str, Any]],
    generated_findings: dict[str, dict[str, Any]],
    static_results: list[dict[str, Any]],
    dynamic_results: list[dict[str, Any]],
    unresolved: dict[str, list[str]],
    generated_at: str,
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]], dict[str, list[str]]]:
    """Apply finding lifecycle transitions and return all current open findings."""
    results = _source_results(static_results, dynamic_results)
    published = dict(generated_findings)
    current_open = dict(generated_findings)
    lifecycle = {
        "new_findings": sorted(set(generated_findings) - set(open_findings)),
        "carried_findings": [],
        "revalidated_findings": [],
        "needs_revalidation": [],
    }
    suffix = current_snapshot.removeprefix("sha256:")[:12]
    for finding_id, finding in open_findings.items():
        sources = _finding_sources(finding)
        source_states = [results.get(source) for source in sorted(sources)]
        missing = not sources or any(state is None for state in source_states)
        inconclusive = any(state not in {"pass", "fail"} for state in source_states if state)
        old_snapshot = finding.get("target_snapshot_hash") != current_snapshot
        if finding_id in unresolved or missing or inconclusive:
            if old_snapshot:
                lifecycle["needs_revalidation"].append(finding_id)
            else:
                lifecycle["carried_findings"].append(finding_id)
                lifecycle["needs_revalidation"].append(finding_id)
                current_open.setdefault(finding_id, finding)
            continue
        failed = any(state == "fail" for state in source_states)
        if not old_snapshot:
            lifecycle["revalidated_findings"].append(finding_id)
            if failed:
                current_open.setdefault(finding_id, generated_findings.get(finding_id, finding))
            else:
                published[finding_id] = _updated_resolution(
                    finding, "no_longer_reproduces", generated_at
                )
                current_open.pop(finding_id, None)
            continue
        lifecycle["revalidated_findings"].append(finding_id)
        if not failed:
            published[finding_id] = _updated_resolution(
                finding, "no_longer_reproduces", generated_at
            )
            continue
        replacement_id = (
            f"finding-{slug(str(finding.get('syscall', 'unmapped-syscall')))}-"
            f"{slug(str(finding.get('rule_id', 'unmapped-rule')))}-{suffix}"
        )
        if replacement_id not in generated_findings:
            lifecycle["revalidated_findings"].remove(finding_id)
            lifecycle["needs_revalidation"].append(finding_id)
            continue
        published[finding_id] = _updated_resolution(
            finding,
            "superseded",
            generated_at,
            superseded_by=replacement_id,
        )
    for key in lifecycle:
        lifecycle[key] = sorted(set(lifecycle[key]))
    return published, current_open, lifecycle


def run_check(
    from_run_id: str,
    root: Path | None = None,
    requested_run_id: str | None = None,
) -> str:
    root = (root or repo_root()).resolve()
    mapping_report = load_mapping_report(root, from_run_id)
    report_id = normalize_run_id(
        requested_run_id or new_run_id("check", {"from": from_run_id, "at": utc_now()})
    )
    report_path = root / "runs" / report_id / "report.md"
    if report_path.parent.exists():
        raise SyscallGuardError(f"check report already exists: {report_path.parent}")
    workspace = _check_workspace(report_id)
    if workspace.exists():
        raise SyscallGuardError(f"check workspace already exists: {workspace}")
    workspace.mkdir(parents=True)
    applied_test_patches: set[str] = set()
    repository: Path | None = None
    try:
        target = mapping_report.get("target", {})
        mapped_branch = target.get("branch") if isinstance(target, dict) else None
        if not isinstance(mapped_branch, str) or not mapped_branch:
            raise SyscallGuardError(
                "mapping report predates negotiated Starry branches; rerun mapping"
            )
        _descriptor, repository, current_branch, repo_identity, current_snapshot = (
            ensure_target_workspace(
                root / "targets/starry/target.yaml", mapped_branch
            )
        )
        mapped_snapshot = str(target.get("snapshot_hash", ""))
        if (
            not mapped_snapshot
            or target.get("repository") != str(repository)
            or target.get("repository_identity") != repo_identity
            or current_branch != mapped_branch
        ):
            raise SyscallGuardError(f"mapping report {from_run_id} has invalid target metadata")
        base_entities, _base_hashes, _base_input_hash = _current_input(root, mapping_report)
        stale_reasons = _mapping_staleness(mapping_report, base_entities)
        if current_snapshot != mapped_snapshot or stale_reasons:
            raise SyscallGuardError(
                "stale mapping; run map-starry-checks again: "
                + "; ".join(
                    ([f"target snapshot changed: {mapped_snapshot} != {current_snapshot}"] if current_snapshot != mapped_snapshot else [])
                    + stale_reasons
                )
            )
        open_findings = _load_open_finding_index(root)
        entities = {kind: dict(rows) for kind, rows in base_entities.items()}
        revalidation_scope, unresolved_revalidation = _extend_revalidation_scope(
            root, entities, open_findings, mapped_snapshot
        )
        hashes = {
            kind: {
                entity_id: version_content_hash(entity)
                for entity_id, entity in rows.items()
            }
            for kind, rows in entities.items()
        }
        versions = _current_versions(entities)
        input_hash = content_hash(
            {
                "entities": hashes,
                "target_snapshot_hash": mapped_snapshot,
                "target_branch": mapped_branch,
                "repository_identity": repo_identity,
                "rule_syscalls": mapping_report.get("rule_syscalls", {}),
            }
        )
        metadata = _base_metadata(
            report_id, from_run_id, mapping_report, input_hash, hashes, versions
        )
        effective_scope = _scope_for_entities(entities)
        metadata["revalidation_scope"] = revalidation_scope
        metadata["effective_execution_scope"] = effective_scope
        metadata["execution_scope"] = effective_scope

        prior = _prior_identical_check(root, input_hash, report_id)
        reused_versions = _validate_reused_findings(root, prior) if prior else None
        current_open_ids = sorted(
            finding_id
            for finding_id, finding in open_findings.items()
            if finding.get("target_snapshot_hash") == mapped_snapshot
        )
        has_old_open = any(
            finding.get("target_snapshot_hash") != mapped_snapshot
            for finding in open_findings.values()
        )
        if (
            prior is not None
            and reused_versions is not None
            and not has_old_open
            and sorted(prior.get("finding_ids", [])) == current_open_ids
        ):
            metadata["status"] = prior["status"]
            metadata["reused_from"] = prior["report_id"]
            metadata["static"] = prior.get("static", [])
            metadata["dynamic"] = prior.get("dynamic", [])
            metadata["blockers"] = prior.get("blockers", [])
            metadata["finding_ids"] = prior.get("finding_ids", [])
            metadata["finding_versions"] = reused_versions
            metadata["new_finding_ids"] = []
            metadata["carried_finding_ids"] = current_open_ids
            metadata["revalidated_finding_ids"] = []
            metadata["needs_revalidation_finding_ids"] = []
            metadata["counts"] = _counts(
                metadata["static"],
                metadata["dynamic"],
                {key: None for key in metadata["finding_ids"]},
                metadata["blockers"],
                {
                    "new_findings": [],
                    "carried_findings": current_open_ids,
                    "revalidated_findings": [],
                    "needs_revalidation": [],
                },
            )
            metadata["counts"]["reused"] = 1
            if metadata["blockers"]:
                for key in ("diagnostic_directory",):
                    if isinstance(prior.get(key), str):
                        metadata[key] = prior[key]
            _seal_metadata(metadata)
            _publish_report(
                root,
                report_id,
                metadata,
                entities["static_checks"],
                entities["dynamic_tests"],
                {},
            )
            _cleanup_success(workspace)
            return report_id

        logs = workspace / "logs"
        logs.mkdir(parents=True)
        blocked_tests, blockers, applied_test_patches = _apply_test_patches(
            root, repository, entities["dynamic_tests"], logs
        )
        for finding_id, reasons in sorted(unresolved_revalidation.items()):
            blockers.append(
                {
                    "kind": "revalidation_definition",
                    "entity_ids": [finding_id],
                    "reason": "; ".join(reasons),
                }
            )
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
        blockers.extend(
            _revert_test_patches(
                root, repository, applied_test_patches, logs
            )
        )
        applied_test_patches.clear()
        if repository_snapshot_hash(repository) != mapped_snapshot:
            blockers.append(
                {
                    "kind": "workspace_cleanup",
                    "entity_ids": [],
                    "reason": "Starry branch changed during compliance checking",
                    "diagnostic_log": str(logs),
                }
            )
        metadata["generated_at_utc"] = utc_now()
        generated_at = metadata["generated_at_utc"]
        rule_syscalls = mapping_report.get("rule_syscalls", {})
        generated_findings, result_findings = _finding_entities(
            root,
            report_id,
            mapped_snapshot,
            rule_syscalls,
            static_results,
            dynamic_results,
            entities["static_checks"],
            entities["dynamic_tests"],
            versions,
            generated_at,
        )
        _annotate_findings(static_results, dynamic_results, result_findings)
        findings, current_open, lifecycle = _aggregate_findings(
            mapped_snapshot,
            open_findings,
            generated_findings,
            static_results,
            dynamic_results,
            unresolved_revalidation,
            generated_at,
        )
        metadata["status"] = "completed_with_blockers" if blockers else "completed"
        metadata["static"] = static_results
        metadata["dynamic"] = dynamic_results
        metadata["blockers"] = blockers
        metadata["finding_ids"] = sorted(current_open)
        metadata["finding_versions"] = {
            finding_id: entity_version(finding_id, finding)
            for finding_id, finding in current_open.items()
        }
        metadata["new_finding_ids"] = lifecycle["new_findings"]
        metadata["carried_finding_ids"] = lifecycle["carried_findings"]
        metadata["revalidated_finding_ids"] = lifecycle["revalidated_findings"]
        metadata["needs_revalidation_finding_ids"] = lifecycle["needs_revalidation"]
        metadata["counts"] = _counts(
            static_results, dynamic_results, current_open, blockers, lifecycle
        )
        if blockers:
            metadata["diagnostic_directory"] = str(workspace)
        _seal_metadata(metadata)
        _publish_report(
            root,
            report_id,
            metadata,
            entities["static_checks"],
            entities["dynamic_tests"],
            findings,
        )
        if not blockers:
            _cleanup_success(workspace)
        return report_id
    except BaseException as exc:
        if repository is not None and applied_test_patches:
            try:
                logs = workspace / "logs"
                logs.mkdir(parents=True, exist_ok=True)
                _revert_test_patches(root, repository, applied_test_patches, logs)
            except BaseException:
                pass
        _mark_failure(workspace, exc)
        if isinstance(exc, SyscallGuardError):
            raise
        raise SyscallGuardError(str(exc)) from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="检查 Starry 合规性")
    parser.add_argument("--from", dest="from_run_id", required=True, help="mapping report id")
    parser.add_argument("--root", type=Path, default=repo_root(), help=argparse.SUPPRESS)
    parser.add_argument("--run-id", help=argparse.SUPPRESS)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    requested_report_id = args.run_id or new_run_id("check", {"from": args.from_run_id})
    try:
        report_id = run_check(args.from_run_id, args.root, requested_report_id)
    except SyscallGuardError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        workspace = _check_workspace(requested_report_id)
        if workspace.exists():
            print(f"diagnostics: {workspace}", file=sys.stderr)
        return 2
    path = args.root.resolve() / "runs" / report_id / "report.md"
    report = load_check_report(args.root.resolve(), report_id)
    print(f"report_id: {report_id}")
    print(f"status: {report['status']}")
    print(f"report: {path}")
    if report.get("diagnostic_directory"):
        print(f"diagnostics: {report['diagnostic_directory']}")
    print(f"finding_index: {args.root.resolve() / 'targets/starry/findings/index.yaml'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
