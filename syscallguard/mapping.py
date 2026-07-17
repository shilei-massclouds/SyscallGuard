from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any, Iterable

import yaml

from .common import (
    SCHEMA_VERSION,
    SyscallGuardError,
    atomic_write_yaml,
    content_hash,
    dependency_mismatch,
    ensure_target_workspace,
    entity_hash,
    entity_version,
    load_mapping,
    new_run_id,
    normalize_run_id,
    read_frontmatter,
    repo_root,
    safe_relative_path,
    slug,
    utc_now,
    version_content_hash,
)


REPORT_KIND = "syscallguard_mapping_report"
REPORT_STATUSES = {"covered", "needs_review", "unsupported", "pending"}
ANALYSIS_STATUSES = {"covered", "needs_review", "unsupported"}
COVERAGE_MODES = {"full", "static-only"}
TARGET_DESCRIPTOR = Path("targets/starry/target.yaml")
TEMP_ROOT = Path("/tmp/syscallguard-map")
INDEX_SPECS = {
    "static_checks": {
        "index": Path("targets/starry/static-checks.yaml"),
        "directory": Path("targets/starry/static-checks"),
        "index_kind": "syscallguard_starry_static_check_index",
        "entity_kind": "syscallguard_starry_static_check",
        "id_field": "check_id",
    },
    "dynamic_tests": {
        "index": Path("targets/starry/dynamic-tests.yaml"),
        "directory": Path("targets/starry/dynamic-tests"),
        "index_kind": "syscallguard_starry_dynamic_test_index",
        "entity_kind": "syscallguard_starry_dynamic_test",
        "id_field": "test_id",
    },
}

_RULE_LIBRARY_CACHE: dict[
    Path,
    tuple[
        tuple[tuple[str, int, int], ...],
        tuple[
            dict[str, dict[str, Any]],
            dict[str, dict[str, str]],
            dict[str, list[str]],
            dict[str, list[str]],
            str,
        ],
    ],
] = {}
_MAPPING_REPORT_CACHE: dict[
    Path, tuple[dict[Path, tuple[int, int]], dict[str, dict[str, Any]]]
] = {}


def resolve_syscalls(value: str | None) -> list[str] | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise SyscallGuardError("syscalls must be a comma-separated list")
    names = [item.strip().lower() for item in value.split(",")]
    if not names or any(not item for item in names):
        raise SyscallGuardError(
            "syscalls must be a non-empty comma-separated list without empty entries"
        )
    return sorted(set(names))


def resolve_coverage(value: str | None) -> str:
    mode = value or "full"
    if mode not in COVERAGE_MODES:
        raise SyscallGuardError("coverage must be 'full' or 'static-only'")
    return mode


def _yaml_text(value: Any) -> str:
    return yaml.safe_dump(
        value,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=100,
    )


def _rule_library(
    root: Path,
) -> tuple[
    dict[str, dict[str, Any]],
    dict[str, dict[str, str]],
    dict[str, list[str]],
    dict[str, list[str]],
    str,
]:
    index_path = root / "library/syscalls.yaml"
    index = load_mapping(index_path)
    if index.get("kind") != "syscallguard_syscall_index":
        raise SyscallGuardError(f"invalid syscall rule index: {index_path}")
    raw_syscalls = index.get("syscalls")
    if not isinstance(raw_syscalls, dict):
        raise SyscallGuardError(f"syscall rule index has no syscalls mapping: {index_path}")

    referenced_paths = [index_path]
    for refs in raw_syscalls.values():
        if not isinstance(refs, list):
            continue
        for ref in refs:
            if isinstance(ref, dict) and isinstance(ref.get("path"), str):
                referenced_paths.append(root / safe_relative_path(ref["path"]))
    signature = tuple(
        sorted(
            (
                str(path),
                path.stat().st_mtime_ns if path.is_file() else -1,
                path.stat().st_size if path.is_file() else -1,
            )
            for path in set(referenced_paths)
        )
    )
    cached = _RULE_LIBRARY_CACHE.get(root)
    if cached is not None and cached[0] == signature:
        return cached[1]

    rules: dict[str, dict[str, Any]] = {}
    versions: dict[str, dict[str, str]] = {}
    rule_syscalls: dict[str, list[str]] = {}
    syscall_rules: dict[str, list[str]] = {}
    for raw_syscall, refs in raw_syscalls.items():
        if not isinstance(raw_syscall, str) or not raw_syscall.strip():
            raise SyscallGuardError("syscall rule index contains an invalid syscall name")
        syscall = raw_syscall.strip().lower()
        if syscall in syscall_rules:
            raise SyscallGuardError(f"duplicate normalized syscall in rule index: {syscall}")
        if not isinstance(refs, list):
            raise SyscallGuardError(f"rule references for {syscall} must be a list")
        syscall_rules[syscall] = []
        for ref in refs:
            if not isinstance(ref, dict):
                raise SyscallGuardError(f"invalid rule reference for syscall {syscall}")
            rule_id = ref.get("rule_id")
            raw_path = ref.get("path")
            if not isinstance(rule_id, str) or not isinstance(raw_path, str):
                raise SyscallGuardError(f"invalid rule reference for syscall {syscall}")
            path = root / safe_relative_path(raw_path)
            rule = load_mapping(path)
            if rule.get("kind") != "syscallguard_rule" or rule.get("rule_id") != rule_id:
                raise SyscallGuardError(f"invalid rule entity for {rule_id}: {path}")
            current = rules.get(rule_id)
            if current is not None and current != rule:
                raise SyscallGuardError(f"conflicting indexed rule entity: {rule_id}")
            rules[rule_id] = rule
            versions[rule_id] = entity_version(rule_id, rule)
            syscall_rules[syscall].append(rule_id)
            rule_syscalls.setdefault(rule_id, [])
            if syscall not in rule_syscalls[rule_id]:
                rule_syscalls[rule_id].append(syscall)

    result = (
        {key: rules[key] for key in sorted(rules)},
        {key: versions[key] for key in sorted(versions)},
        {key: sorted(value) for key, value in sorted(rule_syscalls.items())},
        {key: sorted(set(value)) for key, value in sorted(syscall_rules.items())},
        entity_hash(index_path),
    )
    _RULE_LIBRARY_CACHE[root] = (signature, result)
    return result


def load_mapping_report(root: Path, report_id: str) -> dict[str, Any]:
    report_id = normalize_run_id(report_id)
    path = root / "runs" / report_id / "report.md"
    value, _body = read_frontmatter(path)
    if (
        value.get("kind") != REPORT_KIND
        or value.get("report_id") != report_id
        or value.get("status") != "completed"
    ):
        raise SyscallGuardError(f"not a completed SyscallGuard mapping report: {path}")
    if not isinstance(value.get("rules"), dict):
        raise SyscallGuardError(f"mapping report has no complete rules mapping: {path}")
    if not isinstance(value.get("execution_scope"), dict):
        raise SyscallGuardError(f"mapping report has no execution_scope: {path}")
    return value


def scan_mapping_reports(root: Path) -> tuple[dict[str, Any] | None, dict[str, dict[str, Any]]]:
    runs = root / "runs"
    if not runs.is_dir():
        return None, {}
    paths = sorted(runs.glob("mapping-*/report.md"))
    signatures = {
        path: (path.stat().st_mtime_ns, path.stat().st_size) for path in paths
    }
    cached = _MAPPING_REPORT_CACHE.get(root)
    cached_signatures, cached_reports = cached if cached is not None else ({}, {})
    reports: dict[str, dict[str, Any]] = {
        report_id: report
        for report_id, report in cached_reports.items()
        if (path := runs / report_id / "report.md") in signatures
        and cached_signatures.get(path) == signatures[path]
    }
    for path in paths:
        if cached_signatures.get(path) == signatures[path] and path.parent.name in reports:
            continue
        try:
            value, _body = read_frontmatter(path)
        except SyscallGuardError:
            continue
        report_id = path.parent.name
        if (
            value.get("kind") != REPORT_KIND
            or value.get("report_id") != report_id
            or value.get("status") != "completed"
            or not isinstance(value.get("generated_at_utc"), str)
            or not isinstance(value.get("rules"), dict)
        ):
            continue
        reports[report_id] = value
    _MAPPING_REPORT_CACHE[root] = (signatures, reports)
    latest = max(
        reports.values(),
        key=lambda row: (str(row.get("generated_at_utc", "")), str(row.get("report_id", ""))),
        default=None,
    )
    return latest, reports


def _balanced_block(text: str, opening: int) -> str | None:
    depth = 0
    state = "code"
    index = opening
    while index < len(text):
        char = text[index]
        nxt = text[index + 1] if index + 1 < len(text) else ""
        if state == "code":
            if char == "/" and nxt == "/":
                state = "line"
                index += 1
            elif char == "/" and nxt == "*":
                state = "block"
                index += 1
            elif char == '"':
                state = "string"
            elif char == "'":
                state = "char"
            elif char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    return text[opening : index + 1]
        elif state == "line":
            if char == "\n":
                state = "code"
        elif state == "block":
            if char == "*" and nxt == "/":
                state = "code"
                index += 1
        else:
            quote = '"' if state == "string" else "'"
            if char == "\\":
                index += 1
            elif char == quote:
                state = "code"
        index += 1
    return None


def _symbol_fingerprint(text: str, symbol: str) -> str | None:
    escaped = re.escape(symbol)
    definitions = list(
        re.finditer(
            rf"(?:\b(?:fn|struct|enum|trait|type|const|static)\s+{escaped}\b|"
            rf"\b{escaped}\s*\([^;{{}}]*\)\s*\{{)",
            text,
            re.MULTILINE,
        )
    )
    snippets: list[str] = []
    for match in definitions:
        opening = text.find("{", match.start(), min(len(text), match.end() + 600))
        if opening >= 0:
            block = _balanced_block(text, opening)
            if block is not None:
                line_start = text.rfind("\n", 0, match.start()) + 1
                snippets.append(text[line_start:opening] + block)
    if not snippets:
        snippets = [
            line.strip() for line in text.splitlines() if re.search(rf"\b{escaped}\b", line)
        ]
    return content_hash(snippets) if snippets else None


def _fingerprint_location(repository: Path, location: dict[str, Any]) -> dict[str, Any]:
    raw_path = location.get("path")
    if not isinstance(raw_path, str) or not raw_path:
        raise SyscallGuardError("target location must contain a non-empty path")
    relative = safe_relative_path(raw_path)
    path = repository / relative
    raw_symbols = location.get("symbols", [])
    if not isinstance(raw_symbols, list) or not all(
        isinstance(item, str) and item for item in raw_symbols
    ):
        raise SyscallGuardError(f"target location symbols must be strings: {raw_path}")
    symbols = sorted(set(raw_symbols))
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return {
            "path": raw_path,
            "symbols": symbols,
            "scope": "missing",
            "file_hash": None,
            "symbol_hashes": {},
            "missing_symbols": symbols,
            "content_hash": content_hash({"missing": raw_path}),
        }
    except OSError as exc:
        raise SyscallGuardError(f"cannot read Starry target path {path}: {exc}") from exc
    file_fingerprint = content_hash(text)
    symbol_hashes = {symbol: _symbol_fingerprint(text, symbol) for symbol in symbols}
    missing = [symbol for symbol, value in symbol_hashes.items() if value is None]
    effective = (
        content_hash({"path": raw_path, "symbols": symbol_hashes})
        if symbols
        else content_hash({"path": raw_path, "file_hash": file_fingerprint})
    )
    return {
        "path": raw_path,
        "symbols": symbols,
        "scope": "symbols" if symbols else "file",
        "file_hash": file_fingerprint,
        "symbol_hashes": symbol_hashes,
        "missing_symbols": missing,
        "content_hash": effective,
    }


def _fingerprint_locations(
    repository: Path, locations: Iterable[dict[str, Any]]
) -> list[dict[str, Any]]:
    unique: dict[tuple[str, tuple[str, ...]], dict[str, Any]] = {}
    for location in locations:
        if not isinstance(location, dict):
            raise SyscallGuardError("target_locations entries must be mappings")
        path = location.get("path")
        symbols = location.get("symbols", [])
        if not isinstance(path, str) or not isinstance(symbols, list):
            raise SyscallGuardError("invalid target location")
        key = (path, tuple(sorted(set(str(item) for item in symbols))))
        unique[key] = {"path": path, "symbols": list(key[1])}
    return [_fingerprint_location(repository, unique[key]) for key in sorted(unique)]


def _load_indexed_entities(root: Path, section: str) -> dict[str, dict[str, Any]]:
    spec = INDEX_SPECS[section]
    path = root / spec["index"]
    if not path.exists():
        return {}
    index = load_mapping(path)
    if index.get("kind") != spec["index_kind"] or not isinstance(
        index.get("syscalls"), dict
    ):
        raise SyscallGuardError(f"invalid grouped index: {path}")
    result: dict[str, dict[str, Any]] = {}
    for syscall, rows in index["syscalls"].items():
        if not isinstance(syscall, str) or not isinstance(rows, list):
            raise SyscallGuardError(f"invalid syscall group in {path}")
        for row in rows:
            if not isinstance(row, dict):
                raise SyscallGuardError(f"invalid index row in {path}")
            entity_id = row.get(spec["id_field"])
            raw_path = row.get("path")
            if not isinstance(entity_id, str) or not isinstance(raw_path, str):
                raise SyscallGuardError(f"invalid index row in {path}")
            entity_path = root / safe_relative_path(raw_path)
            entity = load_mapping(entity_path)
            if (
                entity.get("kind") != spec["entity_kind"]
                or entity.get(spec["id_field"]) != entity_id
            ):
                raise SyscallGuardError(f"invalid indexed entity {entity_id}: {entity_path}")
            if entity_id in result and result[entity_id] != entity:
                raise SyscallGuardError(f"conflicting indexed entity: {entity_id}")
            result[entity_id] = entity
    return result


def _artifact_invalid(root: Path, row: dict[str, Any]) -> str | None:
    versions = row.get("entity_versions")
    if not isinstance(versions, dict):
        return "missing_entity_versions"
    for section in INDEX_SPECS:
        recorded = versions.get(section, {})
        refs = row.get("static_check_refs" if section == "static_checks" else "dynamic_test_refs")
        if not isinstance(recorded, dict) or not isinstance(refs, list):
            return f"invalid_{section}_versions"
        spec = INDEX_SPECS[section]
        for entity_id in refs:
            if not isinstance(entity_id, str):
                return f"invalid_{section}_reference"
            version = recorded.get(entity_id)
            if not isinstance(version, dict):
                return f"missing_{section}_version:{entity_id}"
            path = root / spec["directory"] / f"{slug(entity_id)}.yaml"
            if not path.is_file():
                return f"missing_{section}:{entity_id}"
            entity = load_mapping(path)
            if (
                entity.get("kind") != spec["entity_kind"]
                or entity.get(spec["id_field"]) != entity_id
            ):
                return f"invalid_{section}:{entity_id}"
            if dependency_mismatch(version, entity_id, entity):
                return f"changed_{section}:{entity_id}"
    return None


def _pending_reasons(
    root: Path,
    repository: Path,
    snapshot_hash: str,
    repository_identity: str,
    rule_version: dict[str, str],
    row: Any,
    coverage_mode: str = "full",
    prior_coverage_mode: str = "full",
) -> list[str]:
    if not isinstance(row, dict):
        return ["new_rule"]
    if row.get("rule_version") != rule_version:
        return ["rule_version_changed"]
    if row.get("repository_identity") != repository_identity:
        return ["target_repository_changed"]
    status = row.get("status")
    if status not in REPORT_STATUSES:
        return ["invalid_rule_status"]
    if status == "pending":
        return [str(row.get("reason") or "still_pending")]
    if coverage_mode == "static-only" and row.get("dynamic_test_refs"):
        return ["static_only_dynamic_reference"]
    if (
        coverage_mode == "full"
        and prior_coverage_mode == "static-only"
        and row.get("deferred") == "dynamic_test"
    ):
        return ["deferred_dynamic_test_retry"]
    if status in {"needs_review", "unsupported"}:
        if row.get("last_verified_snapshot_hash") != snapshot_hash:
            return ["target_snapshot_changed_retry"]
        return []
    artifact_reason = _artifact_invalid(root, row)
    if artifact_reason:
        return [artifact_reason]
    dependencies = row.get("target_dependencies")
    if not isinstance(dependencies, list) or not dependencies:
        return ["missing_target_dependencies"]
    for dependency in dependencies:
        if not isinstance(dependency, dict):
            return ["invalid_target_dependency"]
        current = _fingerprint_location(repository, dependency)
        if current.get("content_hash") != dependency.get("content_hash"):
            return [f"target_dependency_changed:{dependency.get('path', '')}"]
    return []


def _strip_generated(entity: dict[str, Any]) -> dict[str, Any]:
    result = dict(entity)
    for key in (
        "base_commit",
        "target_hash",
        "target_snapshot_hash",
        "target_dependencies",
        "target_content_fingerprint",
        "upstream_dependencies",
        "generated_at_utc",
        "content_hash",
    ):
        result.pop(key, None)
    return result


def _matching_entities(
    entities: dict[str, dict[str, Any]], rule_id: str
) -> dict[str, dict[str, Any]]:
    return {
        entity_id: entity
        for entity_id, entity in entities.items()
        if isinstance(entity.get("rule_refs"), list) and rule_id in entity["rule_refs"]
    }


def _expand_shared_entity_selection(
    root: Path,
    selected: set[str],
    known_rules: set[str],
    pending_reasons: dict[str, list[str]],
    coverage_mode: str = "full",
) -> set[str]:
    """Close a mapping selection over shared executable entities.

    A static check or dynamic test is versioned as one atomic entity.  If one
    of its rules must be remapped, every other rule referenced by that entity
    must participate in the same publication.  Otherwise the staged entity
    either contains references outside the selected set or would have to drop
    still-valid ownership from the published two-level library.
    """

    sections = (
        ("static_checks",) if coverage_mode == "static-only" else tuple(INDEX_SPECS)
    )
    indexed = {section: _load_indexed_entities(root, section) for section in sections}
    expanded = set(selected)
    changed = True
    while changed:
        changed = False
        for entities in indexed.values():
            for entity_id, entity in entities.items():
                refs = entity.get("rule_refs", [])
                if not isinstance(refs, list) or not all(isinstance(item, str) for item in refs):
                    raise SyscallGuardError(f"executable {entity_id} has invalid rule_refs")
                if not expanded.intersection(refs):
                    continue
                active_refs = set(refs).intersection(known_rules)
                for rule_id in sorted(active_refs - expanded):
                    expanded.add(rule_id)
                    reason = f"shared_entity_dependency:{entity_id}"
                    if reason not in pending_reasons[rule_id]:
                        pending_reasons[rule_id].append(reason)
                    changed = True
    return expanded


def _result_locations(
    checks: dict[str, dict[str, Any]], tests: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    locations: list[dict[str, Any]] = []
    for entity in [*checks.values(), *tests.values()]:
        dependencies = entity.get("target_dependencies", [])
        if isinstance(dependencies, list):
            for item in dependencies:
                if isinstance(item, dict) and isinstance(item.get("path"), str):
                    locations.append(
                        {"path": item["path"], "symbols": list(item.get("symbols", []))}
                    )
    for entity in checks.values():
        if isinstance(entity.get("path"), str):
            locations.append({"path": entity["path"], "symbols": []})
    unique: dict[tuple[str, tuple[str, ...]], dict[str, Any]] = {}
    for item in locations:
        key = (item["path"], tuple(sorted(set(item.get("symbols", [])))))
        unique[key] = {"path": key[0], "symbols": list(key[1])}
    return [unique[key] for key in sorted(unique)]


def _target_dispatches(repository: Path, syscalls: list[str]) -> bool:
    dispatch = repository / "os/StarryOS/kernel/src/syscall/mod.rs"
    if not dispatch.is_file():
        return False
    text = dispatch.read_text(encoding="utf-8", errors="replace")
    return any(
        re.search(rf"\bSysno::{re.escape(syscall)}\s*=>", text)
        for syscall in syscalls
    )


def _prepare_staged_entities(
    root: Path,
    workspace: Path,
    selected: list[str],
    coverage_mode: str = "full",
    repository: Path | None = None,
    rule_syscalls: dict[str, list[str]] | None = None,
) -> None:
    indexed = {section: _load_indexed_entities(root, section) for section in INDEX_SPECS}
    staged_checks: dict[str, dict[str, Any]] = {}
    staged_tests: dict[str, dict[str, Any]] = {}
    for rule_id in selected:
        checks = _matching_entities(indexed["static_checks"], rule_id)
        tests = (
            _matching_entities(indexed["dynamic_tests"], rule_id)
            if coverage_mode == "full"
            else {}
        )
        for values in (checks, tests):
            for entity_id, entity in list(values.items()):
                active_refs = sorted(set(entity.get("rule_refs", [])).intersection(selected))
                if not active_refs:
                    del values[entity_id]
                    continue
                values[entity_id] = {**entity, "rule_refs": active_refs}
        locations = _result_locations(checks, tests)
        covered = bool(checks or tests) and bool(locations)
        unsupported = (
            coverage_mode == "static-only"
            and not covered
            and repository is not None
            and not _target_dispatches(
                repository, (rule_syscalls or {}).get(rule_id, [])
            )
        )
        status = "covered" if covered else "unsupported" if unsupported else "needs_review"
        result = {
            "schema_version": SCHEMA_VERSION,
            "kind": "syscallguard_starry_rule_mapping_result",
            "rule_id": rule_id,
            "status": status,
            "target_locations": locations if covered else [],
            "static_check_refs": sorted(checks) if covered else [],
            "dynamic_test_refs": sorted(tests) if covered else [],
            "reason": (
                "复用现有可执行检查或测试，并重新校验目标内容依赖。"
                if covered
                else "Starry 没有该 syscall 的分派入口。"
                if unsupported
                else "需要运行时夹具才能证明该规则；static-only 模式已延后动态测试。"
                if coverage_mode == "static-only"
                else "尚无足够的 Starry 实现证据；需要只读分析目标代码。"
            ),
            **(
                {"deferred": "dynamic_test"}
                if coverage_mode == "static-only" and status == "needs_review"
                else {}
            ),
        }
        atomic_write_yaml(
            workspace / "staged/rule-results" / f"{slug(rule_id)}.yaml", result
        )
        if covered:
            staged_checks.update((key, _strip_generated(value)) for key, value in checks.items())
            staged_tests.update((key, _strip_generated(value)) for key, value in tests.items())
    for entity_id, entity in staged_checks.items():
        atomic_write_yaml(
            workspace / "staged/targets/starry/static-checks" / f"{slug(entity_id)}.yaml",
            entity,
        )
    for entity_id, entity in staged_tests.items():
        atomic_write_yaml(
            workspace / "staged/targets/starry/dynamic-tests" / f"{slug(entity_id)}.yaml",
            entity,
        )


def _workspace(run_id: str) -> Path:
    return TEMP_ROOT / normalize_run_id(run_id)


def _mark_failed(workspace: Path, exc: BaseException) -> None:
    try:
        atomic_write_yaml(
            workspace / "failure.yaml",
            {
                "schema_version": SCHEMA_VERSION,
                "kind": "syscallguard_mapping_failure",
                "failed_at_utc": utc_now(),
                "error": f"{type(exc).__name__}: {exc}",
            },
        )
    except BaseException:
        pass


def prepare_mapping(
    syscalls: str | None = None,
    root: Path | None = None,
    requested_run_id: str | None = None,
    branch: str | None = None,
    coverage: str = "full",
) -> str:
    root = (root or repo_root()).resolve()
    if not isinstance(branch, str) or not branch.strip():
        raise SyscallGuardError(
            "mapping requires the user-created Starry branch name"
        )
    branch = branch.strip()
    coverage_mode = resolve_coverage(coverage)
    requested_syscalls = resolve_syscalls(syscalls)
    rules, versions, rule_syscalls, syscall_rules, rule_index_hash = _rule_library(root)
    if requested_syscalls is not None:
        unknown = sorted(set(requested_syscalls) - set(syscall_rules))
        if unknown:
            raise SyscallGuardError(
                "requested syscalls do not exist in the rule library: " + ", ".join(unknown)
            )
    descriptor_path = root / TARGET_DESCRIPTOR
    descriptor, repository, current_branch, repo_identity, snapshot_hash = ensure_target_workspace(
        descriptor_path, branch
    )
    descriptor_hash = entity_hash(descriptor_path)
    prior, _reports = scan_mapping_reports(root)
    prior_rows = prior.get("rules", {}) if isinstance(prior, dict) else {}
    prior_coverage_mode = (
        str(prior.get("coverage_mode", "full")) if isinstance(prior, dict) else "full"
    )
    if not isinstance(prior_rows, dict):
        prior_rows = {}
    pending_reasons = {
        rule_id: _pending_reasons(
            root,
            repository,
            snapshot_hash,
            repo_identity,
            versions[rule_id],
            prior_rows.get(rule_id),
            coverage_mode,
            prior_coverage_mode,
        )
        for rule_id in rules
    }
    pending = sorted(rule_id for rule_id, reasons in pending_reasons.items() if reasons)
    scope = (
        set(rules)
        if requested_syscalls is None
        else {
            rule_id
            for syscall in requested_syscalls
            for rule_id in syscall_rules.get(syscall, [])
        }
    )
    selected_set = _expand_shared_entity_selection(
        root,
        scope.intersection(pending),
        set(rules),
        pending_reasons,
        coverage_mode,
    )
    selected = sorted(selected_set)
    pending = sorted(rule_id for rule_id, reasons in pending_reasons.items() if reasons)
    skipped = sorted(scope - set(selected))
    run_id = normalize_run_id(
        requested_run_id
        or new_run_id(
            "mapping",
            {
                "syscalls": requested_syscalls,
                "branch": current_branch,
                "coverage": coverage_mode,
                "snapshot": snapshot_hash,
                "at": utc_now(),
            },
        )
    )
    report_directory = root / "runs" / run_id
    workspace = _workspace(run_id)
    if report_directory.exists():
        raise SyscallGuardError(f"mapping report already exists: {report_directory}")
    if workspace.exists():
        raise SyscallGuardError(f"mapping workspace already exists: {workspace}")
    workspace.mkdir(parents=True)
    try:
        target = {
            "target_id": "starry",
            "repository": str(repository),
            "repository_identity": repo_identity,
            "branch": current_branch,
            "descriptor_hash": descriptor_hash,
            "snapshot_hash": snapshot_hash,
        }
        preparation = {
            "schema_version": SCHEMA_VERSION,
            "kind": "syscallguard_starry_mapping_preparation",
            "run_id": run_id,
            "root": str(root),
            "rule_index_hash": rule_index_hash,
            "prior_report_id": prior.get("report_id") if prior else None,
            "prior_report_hash": content_hash(prior) if prior else None,
            "requested_syscalls": requested_syscalls,
            "coverage_mode": coverage_mode,
            "pending_rule_ids": pending,
            "selected_rule_ids": selected,
            "skipped_rule_ids": skipped,
            "pending_reasons": {key: value for key, value in pending_reasons.items() if value},
            "rule_versions": versions,
            "rule_syscalls": rule_syscalls,
            "target": target,
        }
        atomic_write_yaml(workspace / "preparation.yaml", preparation)
        atomic_write_yaml(workspace / "target-descriptor.yaml", descriptor)
        _prepare_staged_entities(
            root,
            workspace,
            selected,
            coverage_mode,
            repository,
            rule_syscalls,
        )
        return run_id
    except BaseException as exc:
        _mark_failed(workspace, exc)
        if isinstance(exc, SyscallGuardError):
            raise
        raise SyscallGuardError(str(exc)) from exc


def _load_staged(
    workspace: Path, section: str
) -> dict[str, tuple[Path, dict[str, Any]]]:
    spec = INDEX_SPECS[section]
    directory = workspace / "staged/targets/starry" / spec["directory"].name
    result: dict[str, tuple[Path, dict[str, Any]]] = {}
    if not directory.is_dir():
        return result
    for path in sorted(directory.glob("*.yaml")):
        entity = load_mapping(path)
        entity_id = entity.get(spec["id_field"])
        if entity.get("kind") != spec["entity_kind"] or not isinstance(entity_id, str):
            raise SyscallGuardError(f"invalid staged {section} entity: {path}")
        if entity_id in result:
            raise SyscallGuardError(f"duplicate staged {section} id: {entity_id}")
        result[entity_id] = (path, entity)
    return result


def _load_rule_results(workspace: Path) -> dict[str, dict[str, Any]]:
    directory = workspace / "staged/rule-results"
    result: dict[str, dict[str, Any]] = {}
    if not directory.is_dir():
        return result
    for path in sorted(directory.glob("*.yaml")):
        row = load_mapping(path)
        rule_id = row.get("rule_id")
        if (
            row.get("kind") != "syscallguard_starry_rule_mapping_result"
            or not isinstance(rule_id, str)
            or rule_id in result
        ):
            raise SyscallGuardError(f"invalid staged rule result: {path}")
        result[rule_id] = row
    return result


def _validate_staged(
    root: Path,
    workspace: Path,
    selected: set[str],
    results: dict[str, dict[str, Any]],
    staged: dict[str, dict[str, tuple[Path, dict[str, Any]]]],
    coverage_mode: str = "full",
) -> None:
    if set(results) != selected:
        missing = sorted(selected - set(results))
        extra = sorted(set(results) - selected)
        raise SyscallGuardError(f"staged rule results mismatch; missing={missing}, extra={extra}")
    referenced_checks: set[str] = set()
    referenced_tests: set[str] = set()
    referenced_assets: set[Path] = set()
    for rule_id, row in results.items():
        status = row.get("status")
        static_refs = row.get("static_check_refs", [])
        dynamic_refs = row.get("dynamic_test_refs", [])
        locations = row.get("target_locations", [])
        if status not in ANALYSIS_STATUSES:
            raise SyscallGuardError(f"rule {rule_id} has invalid mapping status")
        if not isinstance(static_refs, list) or not all(isinstance(item, str) for item in static_refs):
            raise SyscallGuardError(f"rule {rule_id} has invalid static_check_refs")
        if not isinstance(dynamic_refs, list) or not all(isinstance(item, str) for item in dynamic_refs):
            raise SyscallGuardError(f"rule {rule_id} has invalid dynamic_test_refs")
        if not isinstance(locations, list):
            raise SyscallGuardError(f"rule {rule_id} target_locations must be a list")
        if status == "covered":
            if not static_refs and not dynamic_refs:
                raise SyscallGuardError(f"covered rule {rule_id} has no executable reference")
            if not locations:
                raise SyscallGuardError(f"covered rule {rule_id} has no target location")
        else:
            if static_refs or dynamic_refs:
                raise SyscallGuardError(f"{status} rule {rule_id} must not reference executables")
            if not isinstance(row.get("reason"), str) or not row["reason"].strip():
                raise SyscallGuardError(f"{status} rule {rule_id} needs a reason")
        if coverage_mode == "static-only":
            if dynamic_refs:
                raise SyscallGuardError(
                    f"static-only rule {rule_id} must not reference dynamic tests"
                )
            if status == "needs_review" and row.get("deferred") != "dynamic_test":
                raise SyscallGuardError(
                    f"static-only needs_review rule {rule_id} must defer dynamic_test"
                )
        for location in locations:
            if not isinstance(location, dict) or not isinstance(location.get("path"), str):
                raise SyscallGuardError(f"rule {rule_id} has an invalid target location")
            safe_relative_path(location["path"])
        referenced_checks.update(static_refs)
        referenced_tests.update(dynamic_refs)
    if set(staged["static_checks"]) != referenced_checks:
        raise SyscallGuardError("staged static checks and rule references do not match")
    if set(staged["dynamic_tests"]) != referenced_tests:
        raise SyscallGuardError("staged dynamic tests and rule references do not match")
    if coverage_mode == "static-only" and staged["dynamic_tests"]:
        raise SyscallGuardError("static-only mapping must not stage dynamic tests")
    for check_id, (_path, entity) in staged["static_checks"].items():
        refs = entity.get("rule_refs")
        if not isinstance(refs, list) or not refs or not set(refs).issubset(selected):
            raise SyscallGuardError(f"static check {check_id} has invalid rule_refs")
        if not isinstance(entity.get("path"), str) or not isinstance(entity.get("patterns"), list):
            raise SyscallGuardError(f"static check {check_id} is not executable")
        safe_relative_path(entity["path"])
    for test_id, (_path, entity) in staged["dynamic_tests"].items():
        refs = entity.get("rule_refs")
        if not isinstance(refs, list) or not refs or not set(refs).issubset(selected):
            raise SyscallGuardError(f"dynamic test {test_id} has invalid rule_refs")
        for key in ("test_source", "build", "command"):
            if key not in entity:
                raise SyscallGuardError(f"dynamic test {test_id} is missing {key}")
        for key in ("patch_file", "test_source"):
            value = entity.get(key)
            if not isinstance(value, str) or not value.startswith(
                "targets/starry/dynamic-tests/assets/"
            ):
                continue
            relative = safe_relative_path(value)
            referenced_assets.add(relative)
            staged_asset = workspace / "staged" / relative
            if not staged_asset.is_file() and not (root / relative).is_file():
                raise SyscallGuardError(f"dynamic test {test_id} {key} is missing: {value}")
        patch_file = entity.get("patch_file")
        if isinstance(patch_file, str) and patch_file and not patch_file.startswith(
            "targets/starry/dynamic-tests/assets/"
        ):
            raise SyscallGuardError(
                f"dynamic test {test_id} patch_file must be stored under dynamic-tests/assets"
            )
    assets_root = workspace / "staged/targets/starry/dynamic-tests/assets"
    staged_assets = (
        {
            Path("targets/starry/dynamic-tests/assets") / path.relative_to(assets_root)
            for path in assets_root.rglob("*")
            if path.is_file()
        }
        if assets_root.is_dir()
        else set()
    )
    unreferenced = sorted(str(path) for path in staged_assets - referenced_assets)
    if unreferenced:
        raise SyscallGuardError("staged dynamic assets are unreferenced: " + ", ".join(unreferenced))
    if coverage_mode == "static-only" and staged_assets:
        raise SyscallGuardError("static-only mapping must not stage dynamic assets")


def _all_rule_syscalls(
    root: Path, active: dict[str, list[str]]
) -> dict[str, list[str]]:
    result = {rule_id: list(syscalls) for rule_id, syscalls in active.items()}
    index = load_mapping(root / "library/syscalls.yaml")
    inactive = index.get("inactive_rules", [])
    if isinstance(inactive, list):
        for row in inactive:
            if not isinstance(row, dict) or not isinstance(row.get("rule_id"), str):
                continue
            owners = row.get("original_syscalls", [])
            if not isinstance(owners, list):
                continue
            result.setdefault(row["rule_id"], [])
            result[row["rule_id"]].extend(
                syscall for syscall in owners if isinstance(syscall, str)
            )
    return {key: sorted(set(value)) for key, value in result.items()}


def _versioned_output(
    destination: Path, entity: dict[str, Any], generated_at: str
) -> tuple[dict[str, Any], str]:
    candidate = dict(entity)
    candidate["generated_at_utc"] = generated_at
    if not destination.exists():
        return candidate, "created"
    existing = load_mapping(destination)
    if version_content_hash(existing) == version_content_hash(candidate):
        candidate["generated_at_utc"] = existing.get("generated_at_utc", generated_at)
        return candidate, "skipped"
    return candidate, "updated"


def _grouped_index(
    root: Path,
    section: str,
    entities: dict[str, dict[str, Any]],
    rule_syscalls: dict[str, list[str]],
    generated_at: str,
) -> dict[str, Any]:
    spec = INDEX_SPECS[section]
    groups: dict[str, list[dict[str, Any]]] = {}
    for entity_id, entity in sorted(entities.items()):
        refs = entity.get("rule_refs", [])
        if not isinstance(refs, list):
            raise SyscallGuardError(f"{section} {entity_id} has invalid rule_refs")
        syscalls = sorted(
            {
                syscall
                for rule_id in refs
                for syscall in rule_syscalls.get(str(rule_id), [])
            }
        )
        if not syscalls:
            raise SyscallGuardError(f"{section} {entity_id} has no syscall ownership")
        row = {
            spec["id_field"]: entity_id,
            "path": str(spec["directory"] / f"{slug(entity_id)}.yaml"),
            "rule_refs": sorted(set(str(item) for item in refs)),
        }
        for syscall in syscalls:
            groups.setdefault(syscall, []).append(dict(row))
    return {
        "schema_version": SCHEMA_VERSION,
        "kind": spec["index_kind"],
        "updated_at_utc": generated_at,
        "syscalls": {
            syscall: sorted(rows, key=lambda row: str(row[spec["id_field"]]))
            for syscall, rows in sorted(groups.items())
        },
    }


def _report_text(metadata: dict[str, Any]) -> str:
    counts = metadata["counts"]
    rules = metadata["rules"]
    rule_syscalls = metadata["rule_syscalls"]
    lines = [
        "# Starry 规则映射报告",
        "",
        "## 本轮结论",
        "",
        f"- 协商 Starry 分支：`{metadata['target']['branch']}`",
        f"- 本轮产生静态检查：{counts['static_checks']}",
        f"- 本轮产生动态测试：{counts['dynamic_tests']}",
        f"- 全局剩余规则：{counts['remaining']}（pending {counts['pending']}、"
        f"needs_review {counts['needs_review']}、unsupported {counts['unsupported']}）",
        "",
        "## 完整规则关系",
        "",
    ]
    by_syscall: dict[str, list[str]] = {}
    for rule_id, syscalls in rule_syscalls.items():
        for syscall in syscalls:
            by_syscall.setdefault(syscall, []).append(rule_id)
    for syscall, ids in sorted(by_syscall.items()):
        lines.extend(
            [
                f"### `{syscall}`",
                "",
                "| rule_id | 静态检查 | 动态测试 | 状态 | 原因 |",
                "| --- | --- | --- | --- | --- |",
            ]
        )
        for rule_id in sorted(ids):
            row = rules[rule_id]
            checks = "、".join(f"`{item}`" for item in row["static_check_refs"]) or "—"
            tests = "、".join(f"`{item}`" for item in row["dynamic_test_refs"]) or "—"
            reason = str(row.get("reason", "")).replace("|", "\\|").replace("\n", " ")
            lines.append(
                f"| `{rule_id}` | {checks} | {tests} | `{row['status']}` | {reason} |"
            )
        lines.append("")
    lines.extend(
        [
            "<details>",
            "<summary>机器可读元数据</summary>",
            "",
            "<!-- syscallguard-metadata -->",
            "```yaml",
            _yaml_text(metadata).rstrip(),
            "```",
            "</details>",
        ]
    )
    return "\n".join(lines) + "\n"


def _transactional_write(files: list[tuple[Path, bytes]]) -> None:
    destinations = [path for path, _content in files]
    if len(destinations) != len(set(destinations)):
        raise SyscallGuardError("transaction contains duplicate output paths")
    originals: dict[Path, bytes | None] = {}
    staged: list[tuple[Path, Path]] = []
    replaced: list[Path] = []
    created_directories: list[Path] = []
    try:
        for destination, content in files:
            missing: list[Path] = []
            parent = destination.parent
            while not parent.exists():
                missing.append(parent)
                parent = parent.parent
            destination.parent.mkdir(parents=True, exist_ok=True)
            created_directories.extend(reversed(missing))
            originals[destination] = destination.read_bytes() if destination.exists() else None
            descriptor, name = tempfile.mkstemp(
                prefix=f".{destination.name}.", dir=destination.parent
            )
            temp = Path(name)
            with os.fdopen(descriptor, "wb") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
            staged.append((destination, temp))
        for destination, temp in staged:
            os.replace(temp, destination)
            replaced.append(destination)
    except BaseException:
        for _destination, temp in staged:
            temp.unlink(missing_ok=True)
        for destination in reversed(replaced):
            original = originals[destination]
            if original is None:
                destination.unlink(missing_ok=True)
            else:
                descriptor, name = tempfile.mkstemp(
                    prefix=f".{destination.name}.rollback.", dir=destination.parent
                )
                temp = Path(name)
                with os.fdopen(descriptor, "wb") as handle:
                    handle.write(original)
                    handle.flush()
                    os.fsync(handle.fileno())
                os.replace(temp, destination)
        for directory in reversed(created_directories):
            try:
                directory.rmdir()
            except OSError:
                pass
        raise


def finalize_mapping(run_id: str, root: Path | None = None) -> str:
    root = (root or repo_root()).resolve()
    run_id = normalize_run_id(run_id)
    workspace = _workspace(run_id)
    try:
        preparation = load_mapping(workspace / "preparation.yaml")
        if preparation.get("run_id") != run_id or preparation.get("root") != str(root):
            raise SyscallGuardError(f"mapping preparation identity mismatch: {run_id}")
        report_directory = root / "runs" / run_id
        if report_directory.exists():
            raise SyscallGuardError(f"mapping report already exists: {report_directory}")

        rules, versions, rule_syscalls, _syscall_rules, rule_index_hash = _rule_library(root)
        if rule_index_hash != preparation.get("rule_index_hash"):
            raise SyscallGuardError("rule library index changed after mapping preparation")
        if versions != preparation.get("rule_versions"):
            raise SyscallGuardError("rule versions changed after mapping preparation")
        prior, _reports = scan_mapping_reports(root)
        if (prior.get("report_id") if prior else None) != preparation.get("prior_report_id") or (
            content_hash(prior) if prior else None
        ) != preparation.get("prior_report_hash"):
            raise SyscallGuardError("latest mapping report changed after mapping preparation")

        descriptor_path = root / TARGET_DESCRIPTOR
        target = preparation.get("target")
        if not isinstance(target, dict) or not isinstance(target.get("branch"), str):
            raise SyscallGuardError("mapping preparation has no negotiated Starry branch")
        descriptor, repository, current_branch, repo_identity, snapshot_hash = ensure_target_workspace(
            descriptor_path, target["branch"]
        )
        if not isinstance(target, dict) or (
            target.get("repository") != str(repository)
            or target.get("repository_identity") != repo_identity
            or target.get("branch") != current_branch
            or target.get("descriptor_hash") != entity_hash(descriptor_path)
            or target.get("snapshot_hash") != snapshot_hash
        ):
            raise SyscallGuardError("Starry target content changed after mapping preparation")

        selected_list = preparation.get("selected_rule_ids", [])
        if not isinstance(selected_list, list) or not all(
            isinstance(item, str) and item in rules for item in selected_list
        ):
            raise SyscallGuardError("mapping preparation selected rules are invalid")
        selected = set(selected_list)
        results = _load_rule_results(workspace)
        staged = {section: _load_staged(workspace, section) for section in INDEX_SPECS}
        coverage_mode = resolve_coverage(preparation.get("coverage_mode", "full"))
        _validate_staged(root, workspace, selected, results, staged, coverage_mode)
        generated_at = utc_now()

        rule_dependencies: dict[str, list[dict[str, Any]]] = {}
        for rule_id, row in results.items():
            dependencies = _fingerprint_locations(repository, row.get("target_locations", []))
            if row["status"] == "covered":
                bad = [
                    item
                    for item in dependencies
                    if item.get("scope") == "missing" or item.get("missing_symbols")
                ]
                if bad:
                    raise SyscallGuardError(
                        f"rule {rule_id} references a missing target path or symbol"
                    )
            rule_dependencies[rule_id] = dependencies

        outputs: dict[str, dict[str, tuple[Path, dict[str, Any], str]]] = {
            section: {} for section in INDEX_SPECS
        }
        for section, values in staged.items():
            spec = INDEX_SPECS[section]
            for entity_id, (_stage_path, raw) in values.items():
                entity = _strip_generated(raw)
                refs = sorted(set(entity.get("rule_refs", [])))
                entity["rule_refs"] = refs
                entity["upstream_dependencies"] = [versions[rule_id] for rule_id in refs]
                dependencies_by_hash = {
                    item["content_hash"]: item
                    for rule_id in refs
                    for item in rule_dependencies[rule_id]
                }
                dependencies = [dependencies_by_hash[key] for key in sorted(dependencies_by_hash)]
                entity["target_dependencies"] = dependencies
                entity["target_content_fingerprint"] = content_hash(dependencies)
                destination = root / spec["directory"] / f"{slug(entity_id)}.yaml"
                final, action = _versioned_output(destination, entity, generated_at)
                outputs[section][entity_id] = (destination, final, action)

        current_entities = {section: _load_indexed_entities(root, section) for section in INDEX_SPECS}
        all_entities: dict[str, dict[str, dict[str, Any]]] = {}
        for section in INDEX_SPECS:
            merged = dict(current_entities[section])
            merged.update(
                {entity_id: entity for entity_id, (_path, entity, _action) in outputs[section].items()}
            )
            all_entities[section] = merged

        prior_rows = prior.get("rules", {}) if prior else {}
        if not isinstance(prior_rows, dict):
            prior_rows = {}
        pending_ids = set(preparation.get("pending_rule_ids", []))
        pending_reasons = preparation.get("pending_reasons", {})
        new_rows: dict[str, dict[str, Any]] = {}
        for rule_id in sorted(rules):
            old = prior_rows.get(rule_id)
            if rule_id in selected:
                result = results[rule_id]
                status = result["status"]
                static_refs = sorted(set(result.get("static_check_refs", [])))
                dynamic_refs = sorted(set(result.get("dynamic_test_refs", [])))
                row_versions = {
                    "static_checks": {
                        entity_id: entity_version(entity_id, outputs["static_checks"][entity_id][1])
                        for entity_id in static_refs
                    },
                    "dynamic_tests": {
                        entity_id: entity_version(entity_id, outputs["dynamic_tests"][entity_id][1])
                        for entity_id in dynamic_refs
                    },
                }
                new_rows[rule_id] = {
                    "syscalls": rule_syscalls[rule_id],
                    "rule_version": versions[rule_id],
                    "status": status,
                    "static_check_refs": static_refs,
                    "dynamic_test_refs": dynamic_refs,
                    "entity_versions": row_versions,
                    "target_dependencies": rule_dependencies[rule_id],
                    "repository_identity": repo_identity,
                    "target_descriptor_hash": target["descriptor_hash"],
                    "last_verified_snapshot_hash": snapshot_hash,
                    "last_processed_report": run_id,
                    "reason": result.get("reason") or "映射结果已通过 finalizer 校验。",
                    **(
                        {"deferred": result["deferred"]}
                        if result.get("deferred") == "dynamic_test"
                        else {}
                    ),
                }
            elif rule_id in pending_ids and (
                not isinstance(old, dict) or old.get("status") in {"covered", "pending"}
            ):
                reasons = pending_reasons.get(rule_id, ["pending"])
                new_rows[rule_id] = {
                    "syscalls": rule_syscalls[rule_id],
                    "rule_version": versions[rule_id],
                    "status": "pending",
                    "static_check_refs": [],
                    "dynamic_test_refs": [],
                    "entity_versions": {"static_checks": {}, "dynamic_tests": {}},
                    "target_dependencies": [],
                    "repository_identity": repo_identity,
                    "target_descriptor_hash": target["descriptor_hash"],
                    "last_verified_snapshot_hash": None,
                    "last_processed_report": old.get("last_processed_report")
                    if isinstance(old, dict)
                    else None,
                    "reason": ",".join(str(item) for item in reasons),
                }
            elif isinstance(old, dict):
                current = dict(old)
                current["syscalls"] = rule_syscalls[rule_id]
                current["rule_version"] = versions[rule_id]
                current["repository_identity"] = repo_identity
                current["target_descriptor_hash"] = target["descriptor_hash"]
                if current.get("status") == "covered":
                    current["last_verified_snapshot_hash"] = snapshot_hash
                    current["reason"] = "相关 Starry 内容指纹未变化，已跳过。"
                new_rows[rule_id] = current
            else:
                raise SyscallGuardError(f"mapping state unexpectedly missing rule {rule_id}")

        all_rule_syscalls = _all_rule_syscalls(root, rule_syscalls)
        indexes = {
            section: _grouped_index(
                root, section, all_entities[section], all_rule_syscalls, generated_at
            )
            for section in INDEX_SPECS
        }
        execution_static = sorted(outputs["static_checks"])
        execution_dynamic = sorted(outputs["dynamic_tests"])
        execution_rules = sorted(
            {
                rule_id
                for section in INDEX_SPECS
                for _entity_id, (_path, entity, _action) in outputs[section].items()
                for rule_id in entity.get("rule_refs", [])
            }
        )
        statuses = {status: [] for status in REPORT_STATUSES}
        for rule_id, row in new_rows.items():
            statuses[row["status"]].append(rule_id)
        remaining = sorted(
            statuses["pending"] + statuses["needs_review"] + statuses["unsupported"]
        )
        new_selected = [
            rule_id
            for rule_id in selected_list
            if "new_rule" in preparation.get("pending_reasons", {}).get(rule_id, [])
        ]
        metadata = {
            "schema_version": SCHEMA_VERSION,
            "kind": REPORT_KIND,
            "report_id": run_id,
            "status": "completed",
            "generated_at_utc": generated_at,
            "coverage_mode": coverage_mode,
            "rule_index_hash": rule_index_hash,
            "requested_syscalls": preparation.get("requested_syscalls"),
            "selected_rule_ids": selected_list,
            "skipped_rule_ids": preparation.get("skipped_rule_ids", []),
            "target": target,
            "counts": {
                "rules_total": len(rules),
                "processed": len(selected),
                "added": len(new_selected),
                "updated": len(selected) - len(new_selected),
                "skipped": len(preparation.get("skipped_rule_ids", [])),
                "covered": len(statuses["covered"]),
                "pending": len(statuses["pending"]),
                "needs_review": len(statuses["needs_review"]),
                "unsupported": len(statuses["unsupported"]),
                "static_checks": len(execution_static),
                "dynamic_tests": len(execution_dynamic),
                "remaining": len(remaining),
            },
            "execution_scope": {
                "rules": execution_rules,
                "static_checks": execution_static,
                "dynamic_tests": execution_dynamic,
            },
            "rule_syscalls": rule_syscalls,
            "rules": new_rows,
            "entity_versions": {
                "rules": {rule_id: versions[rule_id] for rule_id in execution_rules},
                "static_checks": {
                    entity_id: entity_version(entity_id, outputs["static_checks"][entity_id][1])
                    for entity_id in execution_static
                },
                "dynamic_tests": {
                    entity_id: entity_version(entity_id, outputs["dynamic_tests"][entity_id][1])
                    for entity_id in execution_dynamic
                },
            },
            "remaining": {
                "all": remaining,
                "pending": sorted(statuses["pending"]),
                "needs_review": sorted(statuses["needs_review"]),
                "unsupported": sorted(statuses["unsupported"]),
            },
        }

        files: list[tuple[Path, bytes]] = []
        for values in outputs.values():
            files.extend(
                (path, _yaml_text(entity).encode("utf-8"))
                for path, entity, _action in values.values()
            )
        for section, index in indexes.items():
            if coverage_mode == "static-only" and section == "dynamic_tests":
                continue
            files.append((root / INDEX_SPECS[section]["index"], _yaml_text(index).encode("utf-8")))
        assets_root = workspace / "staged/targets/starry/dynamic-tests/assets"
        if assets_root.is_dir():
            for source in sorted(path for path in assets_root.rglob("*") if path.is_file()):
                destination = root / "targets/starry/dynamic-tests/assets" / source.relative_to(
                    assets_root
                )
                files.append((destination, source.read_bytes()))
        files.append((report_directory / "report.md", _report_text(metadata).encode("utf-8")))
        _transactional_write(files)
        shutil.rmtree(workspace)
        try:
            TEMP_ROOT.rmdir()
        except OSError:
            pass
        return run_id
    except BaseException as exc:
        _mark_failed(workspace, exc)
        if isinstance(exc, SyscallGuardError):
            raise
        raise SyscallGuardError(str(exc)) from exc


def run_mapping(
    syscalls: str | None = None,
    root: Path | None = None,
    requested_run_id: str | None = None,
    branch: str | None = None,
    coverage: str = "full",
) -> str:
    run_id = prepare_mapping(syscalls, root, requested_run_id, branch, coverage)
    return finalize_mapping(run_id, root)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="增量生成 Starry 规则映射")
    parser.add_argument("--syscalls", help="逗号分隔的 syscall 名称")
    parser.add_argument("--branch", help="用户创建并已切换到的 Starry 专用分支")
    parser.add_argument(
        "--coverage",
        choices=("full", "static-only"),
        default="full",
        help="覆盖模式；static-only 禁止新动态测试",
    )
    parser.add_argument(
        "--phase",
        choices=("prepare", "finalize", "auto"),
        default="prepare",
        help=argparse.SUPPRESS,
    )
    parser.add_argument("--root", type=Path, default=repo_root(), help=argparse.SUPPRESS)
    parser.add_argument("--run-id", help=argparse.SUPPRESS)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    requested = args.run_id or new_run_id("mapping", {"syscalls": args.syscalls})
    try:
        if args.phase == "finalize":
            if not args.run_id:
                raise SyscallGuardError("finalize requires --run-id")
            run_id = finalize_mapping(args.run_id, args.root)
            report = load_mapping_report(args.root.resolve(), run_id)
            counts = report["counts"]
            print(f"报告 ID：{run_id}")
            print(
                "本轮静态检查：{static_checks}，动态测试：{dynamic_tests}，"
                "全局剩余：{remaining}".format(**counts)
            )
            print(f"报告：{args.root.resolve() / 'runs' / run_id / 'report.md'}")
        elif args.phase == "auto":
            run_id = run_mapping(
                args.syscalls, args.root, requested, args.branch, args.coverage
            )
            report = load_mapping_report(args.root.resolve(), run_id)
            counts = report["counts"]
            print(f"报告 ID：{run_id}")
            print(
                "本轮静态检查：{static_checks}，动态测试：{dynamic_tests}，"
                "全局剩余：{remaining}".format(**counts)
            )
            print(f"报告：{args.root.resolve() / 'runs' / run_id / 'report.md'}")
        else:
            run_id = prepare_mapping(
                args.syscalls, args.root, requested, args.branch, args.coverage
            )
            workspace = _workspace(run_id)
            preparation = load_mapping(workspace / "preparation.yaml")
            print(f"运行 ID：{run_id}")
            print(f"待分析实体：{workspace / 'staged'}")
            print(f"准备文件：{workspace / 'preparation.yaml'}")
            print(f"协商分支：{preparation['target']['branch']}")
            print(f"固定内容快照：{preparation['target']['snapshot_hash']}")
    except SyscallGuardError as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
