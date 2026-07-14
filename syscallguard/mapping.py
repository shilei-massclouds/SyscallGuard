from __future__ import annotations

import argparse
import os
import re
import sys
import tempfile
from pathlib import Path
from typing import Any, Iterable

import yaml

from .common import (
    SCHEMA_VERSION,
    RunRecorder,
    SyscallGuardError,
    atomic_write_text,
    atomic_write_yaml,
    content_hash,
    dependency_mismatch,
    ensure_target_workspace,
    entity_hash,
    entity_version,
    load_index,
    load_mapping,
    new_run_id,
    repo_root,
    safe_relative_path,
    slug,
    utc_now,
    version_content_hash,
)


CLASSIFICATIONS = {"static", "partial_static", "dynamic", "unsupported", "needs_review"}
MAPPED_CLASSIFICATIONS = {"static", "partial_static", "dynamic"}
COVERAGE_STATUSES = {"pending", "mapped", "needs_review", "unsupported"}
TARGET_DESCRIPTOR = Path("targets/starry/target.yaml")
COVERAGE_PATH = Path("targets/starry/rule-coverage.yaml")
INDEX_SPECS = {
    "mappings": (
        Path("targets/starry/mappings/index.yaml"),
        "syscallguard_starry_mapping_index",
        "mapping_id",
        "syscallguard_starry_mapping",
    ),
    "static_checks": (
        Path("targets/starry/static-checks/index.yaml"),
        "syscallguard_starry_static_check_index",
        "check_id",
        "syscallguard_starry_static_check",
    ),
    "dynamic_tests": (
        Path("targets/starry/dynamic-tests/index.yaml"),
        "syscallguard_starry_dynamic_test_index",
        "test_id",
        "syscallguard_starry_dynamic_test",
    ),
}


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

    return (
        {key: rules[key] for key in sorted(rules)},
        {key: versions[key] for key in sorted(versions)},
        {key: sorted(value) for key, value in sorted(rule_syscalls.items())},
        {key: sorted(set(value)) for key, value in sorted(syscall_rules.items())},
        entity_hash(index_path),
    )


def _default_coverage() -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "kind": "syscallguard_starry_rule_coverage",
        "updated_at_utc": None,
        "target": {
            "target_id": "starry",
            "repository_identity": None,
            "descriptor_hash": None,
            "last_snapshot_hash": None,
        },
        "rules": {},
    }


def _load_coverage(root: Path) -> tuple[dict[str, Any], str | None]:
    path = root / COVERAGE_PATH
    if not path.exists():
        return _default_coverage(), None
    value = load_mapping(path)
    if value.get("kind") != "syscallguard_starry_rule_coverage":
        raise SyscallGuardError(f"invalid Starry rule coverage table: {path}")
    if not isinstance(value.get("rules"), dict):
        raise SyscallGuardError(f"coverage rules must be a mapping: {path}")
    return value, entity_hash(path)


def _indexed_entities(root: Path, section: str) -> dict[str, dict[str, Any]]:
    relative, index_kind, id_field, entity_kind = INDEX_SPECS[section]
    index = load_index(root / relative, index_kind)
    result: dict[str, dict[str, Any]] = {}
    for row in index["entities"]:
        if not isinstance(row, dict):
            continue
        entity_id = row.get("id")
        raw_path = row.get("path")
        if not isinstance(entity_id, str) or not isinstance(raw_path, str):
            raise SyscallGuardError(f"invalid index row in {relative}")
        path = root / safe_relative_path(raw_path)
        entity = load_mapping(path)
        if entity.get("kind") != entity_kind or entity.get(id_field) != entity_id:
            raise SyscallGuardError(f"invalid indexed entity {entity_id}: {path}")
        result[entity_id] = entity
    return result


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
            line.strip()
            for line in text.splitlines()
            if re.search(rf"\b{escaped}\b", line)
        ]
    return content_hash(snippets) if snippets else None


def _fingerprint_location(repository: Path, location: dict[str, Any]) -> dict[str, Any]:
    raw_path = location.get("path")
    if not isinstance(raw_path, str) or not raw_path:
        raise SyscallGuardError("target location must contain a non-empty path")
    relative = safe_relative_path(raw_path)
    path = repository / relative
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return {
            "path": raw_path,
            "symbols": sorted(set(str(item) for item in location.get("symbols", []))),
            "scope": "missing",
            "file_hash": None,
            "symbol_hashes": {},
            "content_hash": content_hash({"missing": raw_path}),
        }
    except OSError as exc:
        raise SyscallGuardError(f"cannot read Starry target path {path}: {exc}") from exc
    raw_symbols = location.get("symbols", [])
    if not isinstance(raw_symbols, list) or not all(
        isinstance(item, str) and item for item in raw_symbols
    ):
        raise SyscallGuardError(f"target location symbols must be strings: {raw_path}")
    symbols = sorted(set(raw_symbols))
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


def _artifact_invalid(root: Path, row: dict[str, Any]) -> str | None:
    versions = row.get("artifact_versions", {})
    if not isinstance(versions, dict):
        return "missing_artifact_versions"
    for section, (_relative, _kind, id_field, entity_kind) in INDEX_SPECS.items():
        recorded = versions.get(section, {})
        if not isinstance(recorded, dict):
            return f"invalid_{section}_versions"
        directory = INDEX_SPECS[section][0].parent
        for entity_id, version in recorded.items():
            if not isinstance(entity_id, str) or not isinstance(version, dict):
                return f"invalid_{section}_version"
            path = root / directory / f"{slug(entity_id)}.yaml"
            if not path.is_file():
                return f"missing_{section}:{entity_id}"
            entity = load_mapping(path)
            if entity.get("kind") != entity_kind or entity.get(id_field) != entity_id:
                return f"invalid_{section}:{entity_id}"
            if dependency_mismatch(version, entity_id, entity):
                return f"changed_{section}:{entity_id}"
    return None


def _pending_reasons(
    root: Path,
    repository: Path,
    snapshot_hash: str,
    descriptor_hash: str,
    repository_identity: str,
    rule_id: str,
    rule_version: dict[str, str],
    row: Any,
) -> list[str]:
    if not isinstance(row, dict):
        return ["new_rule"]
    if row.get("rule_version") != rule_version:
        return ["rule_version_changed"]
    if row.get("repository_identity") != repository_identity:
        return ["target_repository_changed"]
    if row.get("target_descriptor_hash") != descriptor_hash:
        return ["target_descriptor_changed"]
    status = row.get("status")
    if status not in COVERAGE_STATUSES:
        return ["invalid_coverage_status"]
    if status == "pending":
        reason = row.get("reason")
        return [str(reason) if reason else "still_pending"]
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
        "upstream_dependencies",
        "generated_at_utc",
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


def _prepare_staged_entities(
    root: Path,
    run_directory: Path,
    selected: list[str],
) -> None:
    indexed = {section: _indexed_entities(root, section) for section in INDEX_SPECS}
    staged_checks: dict[str, dict[str, Any]] = {}
    staged_tests: dict[str, dict[str, Any]] = {}
    for rule_id in selected:
        existing_mappings = {
            key: value
            for key, value in _matching_entities(indexed["mappings"], rule_id).items()
            if value.get("rule_refs") == [rule_id]
        }
        checks = _matching_entities(indexed["static_checks"], rule_id)
        tests = _matching_entities(indexed["dynamic_tests"], rule_id)
        if existing_mappings:
            mapping_id, mapping = sorted(existing_mappings.items())[0]
            staged_mapping = _strip_generated(mapping)
            staged_mapping["static_check_refs"] = sorted(checks)
            staged_mapping["dynamic_test_refs"] = sorted(tests)
        else:
            mapping_id = f"STARRY_{rule_id}"
            locations = [
                {"path": entity["path"], "symbols": []}
                for entity in checks.values()
                if isinstance(entity.get("path"), str)
            ]
            if checks and tests:
                classification = "partial_static"
            elif checks:
                classification = "static"
            else:
                classification = "needs_review"
            staged_mapping = {
                "schema_version": SCHEMA_VERSION,
                "kind": "syscallguard_starry_mapping",
                "mapping_id": mapping_id,
                "rule_refs": [rule_id],
                "classification": classification,
                "target_locations": locations,
                "static_check_refs": sorted(checks),
                "dynamic_test_refs": sorted(tests) if locations else [],
                "reason": (
                    "复用现有检查定义，仍需核对目标实现位置。"
                    if locations
                    else "尚无足够的 Starry 实现证据；需要只读分析目标代码。"
                ),
            }
        staged_checks.update(
            (key, _strip_generated(checks[key]))
            for key in staged_mapping.get("static_check_refs", [])
            if key in checks
        )
        staged_tests.update(
            (key, _strip_generated(tests[key]))
            for key in staged_mapping.get("dynamic_test_refs", [])
            if key in tests
        )
        atomic_write_yaml(
            run_directory / "staged/targets/starry/mappings" / f"{slug(mapping_id)}.yaml",
            staged_mapping,
        )
    for entity_id, entity in staged_checks.items():
        atomic_write_yaml(
            run_directory / "staged/targets/starry/static-checks" / f"{slug(entity_id)}.yaml",
            entity,
        )
    for entity_id, entity in staged_tests.items():
        atomic_write_yaml(
            run_directory / "staged/targets/starry/dynamic-tests" / f"{slug(entity_id)}.yaml",
            entity,
        )


def prepare_mapping(
    syscalls: str | None = None,
    root: Path | None = None,
    requested_run_id: str | None = None,
) -> str:
    root = (root or repo_root()).resolve()
    requested_syscalls = resolve_syscalls(syscalls)
    rules, versions, rule_syscalls, syscall_rules, rule_index_hash = _rule_library(root)
    if requested_syscalls is not None:
        unknown = sorted(set(requested_syscalls) - set(syscall_rules))
        if unknown:
            raise SyscallGuardError(
                "requested syscalls do not exist in the rule library: " + ", ".join(unknown)
            )
    descriptor_path = root / TARGET_DESCRIPTOR
    descriptor, repository, _revision_ref, repo_identity, snapshot_hash = ensure_target_workspace(
        descriptor_path
    )
    descriptor_hash = entity_hash(descriptor_path)
    coverage, coverage_hash = _load_coverage(root)
    old_rows = coverage["rules"]
    pending_reasons = {
        rule_id: _pending_reasons(
            root,
            repository,
            snapshot_hash,
            descriptor_hash,
            repo_identity,
            rule_id,
            versions[rule_id],
            old_rows.get(rule_id),
        )
        for rule_id in rules
    }
    pending = sorted(rule_id for rule_id, reasons in pending_reasons.items() if reasons)
    if requested_syscalls is None:
        scope = set(rules)
    else:
        scope = {
            rule_id
            for syscall in requested_syscalls
            for rule_id in syscall_rules.get(syscall, [])
        }
    selected = sorted(scope.intersection(pending))
    skipped = sorted(scope - set(selected))
    run_id = requested_run_id or new_run_id(
        "mapping", {"syscalls": requested_syscalls, "snapshot": snapshot_hash, "at": utc_now()}
    )
    recorder = RunRecorder(
        root,
        "mapping",
        run_id,
        {"syscalls": requested_syscalls},
    )
    try:
        preparation = {
            "schema_version": SCHEMA_VERSION,
            "kind": "syscallguard_starry_mapping_preparation",
            "run_id": run_id,
            "rule_index_hash": rule_index_hash,
            "coverage_hash": coverage_hash,
            "requested_syscalls": requested_syscalls,
            "pending_rule_ids": pending,
            "selected_rule_ids": selected,
            "skipped_rule_ids": skipped,
            "pending_reasons": {key: value for key, value in pending_reasons.items() if value},
            "rule_versions": versions,
            "rule_syscalls": rule_syscalls,
            "target": {
                "target_id": "starry",
                "repository": str(repository),
                "repository_identity": repo_identity,
                "descriptor_hash": descriptor_hash,
                "snapshot_hash": snapshot_hash,
            },
        }
        atomic_write_yaml(recorder.directory / "preparation.yaml", preparation)
        atomic_write_yaml(recorder.directory / "target-descriptor.yaml", descriptor)
        _prepare_staged_entities(root, recorder.directory, selected)
        recorder.manifest["phase"] = "analysis"
        recorder.manifest["rule_index_hash"] = rule_index_hash
        recorder.manifest["selected_rule_versions"] = {
            rule_id: versions[rule_id] for rule_id in selected
        }
        recorder.manifest["target"] = preparation["target"]
        recorder.manifest["counts"] = {
            "rules_total": len(rules),
            "pending_before": len(pending),
            "selected_pending": len(selected),
            "skipped": len(skipped),
            "pending_remaining": len(set(pending) - set(selected)),
        }
        recorder.manifest["outputs"] = {
            "preparation": "preparation.yaml",
            "staged_entities": "staged/",
            "target_descriptor": "target-descriptor.yaml",
        }
        recorder.flush()
        return run_id
    except BaseException as exc:
        recorder.fail(exc)
        if isinstance(exc, SyscallGuardError):
            raise
        raise SyscallGuardError(str(exc)) from exc


def _load_staged(
    run_directory: Path, section: str
) -> dict[str, tuple[Path, dict[str, Any]]]:
    _relative, _kind, id_field, entity_kind = INDEX_SPECS[section]
    directory = run_directory / "staged/targets/starry" / INDEX_SPECS[section][0].parent.name
    result: dict[str, tuple[Path, dict[str, Any]]] = {}
    if not directory.is_dir():
        return result
    for path in sorted(directory.glob("*.yaml")):
        entity = load_mapping(path)
        entity_id = entity.get(id_field)
        if entity.get("kind") != entity_kind or not isinstance(entity_id, str):
            raise SyscallGuardError(f"invalid staged {section} entity: {path}")
        if entity_id in result:
            raise SyscallGuardError(f"duplicate staged {section} id: {entity_id}")
        result[entity_id] = (path, entity)
    return result


def _validate_staged(
    selected: set[str],
    staged: dict[str, dict[str, tuple[Path, dict[str, Any]]]],
) -> dict[str, str]:
    ownership: dict[str, str] = {}
    referenced_checks: set[str] = set()
    referenced_tests: set[str] = set()
    for mapping_id, (_path, mapping) in staged["mappings"].items():
        refs = mapping.get("rule_refs")
        classification = mapping.get("classification")
        locations = mapping.get("target_locations")
        static_refs = mapping.get("static_check_refs", [])
        dynamic_refs = mapping.get("dynamic_test_refs", [])
        if not isinstance(refs, list) or not refs or not all(isinstance(item, str) for item in refs):
            raise SyscallGuardError(f"mapping {mapping_id} has invalid rule_refs")
        if not set(refs).issubset(selected):
            raise SyscallGuardError(f"mapping {mapping_id} references an unselected rule")
        if classification not in CLASSIFICATIONS:
            raise SyscallGuardError(f"mapping {mapping_id} has invalid classification")
        if not isinstance(locations, list):
            raise SyscallGuardError(f"mapping {mapping_id} target_locations must be a list")
        if not isinstance(static_refs, list) or not all(isinstance(item, str) for item in static_refs):
            raise SyscallGuardError(f"mapping {mapping_id} has invalid static_check_refs")
        if not isinstance(dynamic_refs, list) or not all(isinstance(item, str) for item in dynamic_refs):
            raise SyscallGuardError(f"mapping {mapping_id} has invalid dynamic_test_refs")
        for rule_id in refs:
            if rule_id in ownership:
                raise SyscallGuardError(f"rule {rule_id} has more than one staged mapping")
            ownership[rule_id] = mapping_id
        for location in locations:
            if not isinstance(location, dict):
                raise SyscallGuardError(f"mapping {mapping_id} has an invalid target location")
            raw_path = location.get("path")
            if not isinstance(raw_path, str) or not raw_path:
                raise SyscallGuardError(f"mapping {mapping_id} has a target location without path")
            safe_relative_path(raw_path)
        if classification in MAPPED_CLASSIFICATIONS and not locations:
            raise SyscallGuardError(f"mapping {mapping_id} has no implementation location")
        if classification == "static" and (not static_refs or dynamic_refs):
            raise SyscallGuardError(f"static mapping {mapping_id} must reference only static checks")
        if classification == "dynamic" and (not dynamic_refs or static_refs):
            raise SyscallGuardError(f"dynamic mapping {mapping_id} must reference only dynamic tests")
        if classification == "partial_static" and (not static_refs or not dynamic_refs):
            raise SyscallGuardError(
                f"partial_static mapping {mapping_id} needs static and dynamic references"
            )
        if classification in {"needs_review", "unsupported"}:
            if static_refs or dynamic_refs:
                raise SyscallGuardError(
                    f"{classification} mapping {mapping_id} must not invent executable checks"
                )
            if not isinstance(mapping.get("reason"), str) or not mapping["reason"].strip():
                raise SyscallGuardError(f"{classification} mapping {mapping_id} needs a reason")
        referenced_checks.update(static_refs)
        referenced_tests.update(dynamic_refs)
    missing_rules = sorted(selected - set(ownership))
    if missing_rules:
        raise SyscallGuardError("staged mappings do not cover rules: " + ", ".join(missing_rules))
    if set(staged["static_checks"]) != referenced_checks:
        raise SyscallGuardError("staged static checks and mapping references do not match")
    if set(staged["dynamic_tests"]) != referenced_tests:
        raise SyscallGuardError("staged dynamic tests and mapping references do not match")
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
    return ownership


def _versioned_output(
    destination: Path,
    entity: dict[str, Any],
    generated_at: str,
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


def _merge_index_value(
    root: Path,
    section: str,
    entries: list[dict[str, Any]],
    updated_at: str,
) -> dict[str, Any]:
    relative, kind, _id_field, _entity_kind = INDEX_SPECS[section]
    index = load_index(root / relative, kind)
    by_id = {
        row["id"]: row
        for row in index["entities"]
        if isinstance(row, dict) and isinstance(row.get("id"), str)
    }
    for row in entries:
        by_id[row["id"]] = row
    index["entities"] = [by_id[key] for key in sorted(by_id)]
    index["updated_at_utc"] = updated_at
    return index


def _transactional_write(files: list[tuple[Path, str]]) -> None:
    originals: dict[Path, bytes | None] = {}
    staged: list[tuple[Path, Path]] = []
    replaced: list[Path] = []
    try:
        for destination, text in files:
            destination.parent.mkdir(parents=True, exist_ok=True)
            originals[destination] = destination.read_bytes() if destination.exists() else None
            descriptor, name = tempfile.mkstemp(
                prefix=f".{destination.name}.", dir=destination.parent
            )
            temp = Path(name)
            with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
                handle.write(text)
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
        raise


def _report_text(manifest: dict[str, Any], preparation: dict[str, Any]) -> str:
    counts = manifest["counts"]
    categories = manifest.get("processed", {})
    lines = [
        "# Starry 规则映射报告",
        "",
        f"- 运行：`{manifest['run_id']}`",
        f"- 目标内容快照：`{manifest['target']['snapshot_hash']}`",
        f"- 新增规则：{counts['added']}",
        f"- 更新规则：{counts['updated']}",
        f"- 跳过规则：{counts['skipped']}",
        f"- 待复核：{counts['needs_review']}",
        f"- 不支持：{counts['unsupported']}",
        f"- 静态检查：{counts['static_checks']}",
        f"- 动态测试：{counts['dynamic_tests']}",
        f"- 仍待处理：{counts['pending_remaining']}",
        "",
    ]
    for label, key in (
        ("已映射", "mapped"),
        ("待复核", "needs_review"),
        ("不支持", "unsupported"),
        ("跳过", "skipped"),
        ("仍待处理", "pending"),
    ):
        values = categories.get(key, [])
        lines.append(f"## {label}")
        lines.append("")
        lines.append("、".join(f"`{item}`" for item in values) if values else "无。")
        lines.append("")
    if preparation.get("requested_syscalls"):
        lines.extend(
            [
                "## 本次 syscall 范围",
                "",
                "、".join(f"`{item}`" for item in preparation["requested_syscalls"]),
                "",
            ]
        )
    return "\n".join(lines)


def _mark_failed(run_directory: Path, exc: BaseException) -> None:
    try:
        manifest = load_mapping(run_directory / "manifest.yaml")
        manifest["status"] = "failed"
        manifest["completed_at_utc"] = utc_now()
        manifest["error"] = f"{type(exc).__name__}: {exc}"
        atomic_write_yaml(run_directory / "manifest.yaml", manifest)
    except BaseException:
        pass


def finalize_mapping(run_id: str, root: Path | None = None) -> str:
    root = (root or repo_root()).resolve()
    run_directory = root / "runs" / run_id
    try:
        manifest = load_mapping(run_directory / "manifest.yaml")
        if (
            manifest.get("kind") != "syscallguard_run"
            or manifest.get("stage") != "mapping"
            or manifest.get("status") != "running"
        ):
            raise SyscallGuardError(f"mapping run is not awaiting finalization: {run_id}")
        preparation = load_mapping(run_directory / "preparation.yaml")
        if preparation.get("run_id") != run_id:
            raise SyscallGuardError(f"mapping preparation identity mismatch: {run_id}")
        rules, versions, rule_syscalls, _syscall_rules, rule_index_hash = _rule_library(root)
        if rule_index_hash != preparation.get("rule_index_hash"):
            raise SyscallGuardError("rule library index changed after mapping preparation")
        if versions != preparation.get("rule_versions"):
            raise SyscallGuardError("rule versions changed after mapping preparation")
        coverage, coverage_hash = _load_coverage(root)
        if coverage_hash != preparation.get("coverage_hash"):
            raise SyscallGuardError("rule coverage changed after mapping preparation")
        descriptor_path = root / TARGET_DESCRIPTOR
        _descriptor, repository, _revision_ref, repo_identity, snapshot_hash = ensure_target_workspace(
            descriptor_path
        )
        target = preparation.get("target", {})
        if not isinstance(target, dict):
            raise SyscallGuardError("mapping preparation target is invalid")
        if (
            target.get("repository") != str(repository)
            or target.get("repository_identity") != repo_identity
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
        staged = {section: _load_staged(run_directory, section) for section in INDEX_SPECS}
        ownership = _validate_staged(selected, staged)
        generated_at = utc_now()

        outputs: dict[str, dict[str, tuple[Path, dict[str, Any], str]]] = {
            section: {} for section in INDEX_SPECS
        }
        mapping_dependencies: dict[str, list[dict[str, Any]]] = {}
        for mapping_id, (_stage_path, raw) in staged["mappings"].items():
            dependencies = _fingerprint_locations(repository, raw.get("target_locations", []))
            if raw.get("classification") in MAPPED_CLASSIFICATIONS:
                bad = [
                    item
                    for item in dependencies
                    if item.get("scope") == "missing" or item.get("missing_symbols")
                ]
                if bad:
                    raise SyscallGuardError(
                        f"mapping {mapping_id} references a missing target path or symbol"
                    )
            mapping_dependencies[mapping_id] = dependencies
            entity = _strip_generated(raw)
            refs = sorted(set(entity["rule_refs"]))
            entity["rule_refs"] = refs
            entity["upstream_dependencies"] = [versions[rule_id] for rule_id in refs]
            entity["target_snapshot_hash"] = content_hash(dependencies)
            destination = root / "targets/starry/mappings" / f"{slug(mapping_id)}.yaml"
            final, action = _versioned_output(destination, entity, generated_at)
            outputs["mappings"][mapping_id] = (destination, final, action)

        for section in ("static_checks", "dynamic_tests"):
            _relative, _kind, id_field, _entity_kind = INDEX_SPECS[section]
            for entity_id, (_stage_path, raw) in staged[section].items():
                entity = _strip_generated(raw)
                refs = sorted(set(entity["rule_refs"]))
                entity["rule_refs"] = refs
                entity["upstream_dependencies"] = [versions[rule_id] for rule_id in refs]
                related = sorted({ownership[rule_id] for rule_id in refs})
                dependencies = [
                    item
                    for mapping_id in related
                    for item in mapping_dependencies[mapping_id]
                ]
                entity["target_snapshot_hash"] = content_hash(dependencies)
                destination = root / INDEX_SPECS[section][0].parent / f"{slug(entity_id)}.yaml"
                final, action = _versioned_output(destination, entity, generated_at)
                outputs[section][entity_id] = (destination, final, action)

        artifact_versions = {
            section: {
                entity_id: entity_version(entity_id, entity)
                for entity_id, (_path, entity, _action) in values.items()
            }
            for section, values in outputs.items()
        }
        old_rows = coverage["rules"]
        pending_ids = set(preparation.get("pending_rule_ids", []))
        pending_reasons = preparation.get("pending_reasons", {})
        new_rows: dict[str, dict[str, Any]] = {}
        mapped: list[str] = []
        needs_review: list[str] = []
        unsupported: list[str] = []
        for rule_id in sorted(rules):
            old = old_rows.get(rule_id)
            if rule_id in selected:
                mapping_id = ownership[rule_id]
                mapping = outputs["mappings"][mapping_id][1]
                classification = mapping["classification"]
                status = "mapped" if classification in MAPPED_CLASSIFICATIONS else classification
                refs = {
                    "mappings": [mapping_id],
                    "static_checks": sorted(
                        entity_id
                        for entity_id, (_path, entity, _action) in outputs["static_checks"].items()
                        if rule_id in entity["rule_refs"]
                    ),
                    "dynamic_tests": sorted(
                        entity_id
                        for entity_id, (_path, entity, _action) in outputs["dynamic_tests"].items()
                        if rule_id in entity["rule_refs"]
                    ),
                }
                row_versions = {
                    section: {
                        entity_id: artifact_versions[section][entity_id]
                        for entity_id in ids
                    }
                    for section, ids in refs.items()
                }
                reason = mapping.get("reason")
                new_rows[rule_id] = {
                    "syscalls": rule_syscalls[rule_id],
                    "rule_version": versions[rule_id],
                    "status": status,
                    "classification": classification,
                    "mapping_refs": refs["mappings"],
                    "static_check_refs": refs["static_checks"],
                    "dynamic_test_refs": refs["dynamic_tests"],
                    "artifact_versions": row_versions,
                    "target_dependencies": mapping_dependencies[mapping_id],
                    "repository_identity": repo_identity,
                    "target_descriptor_hash": target["descriptor_hash"],
                    "last_verified_snapshot_hash": snapshot_hash,
                    "last_processed_run": run_id,
                    "reason": reason or "映射定义已通过 finalizer 校验。",
                }
                if status == "mapped":
                    mapped.append(rule_id)
                elif status == "needs_review":
                    needs_review.append(rule_id)
                else:
                    unsupported.append(rule_id)
            elif rule_id in pending_ids:
                prior = dict(old) if isinstance(old, dict) else {}
                prior.update(
                    {
                        "syscalls": rule_syscalls[rule_id],
                        "rule_version": versions[rule_id],
                        "status": "pending",
                        "repository_identity": repo_identity,
                        "target_descriptor_hash": target["descriptor_hash"],
                        "reason": ",".join(pending_reasons.get(rule_id, ["pending"])),
                    }
                )
                prior.setdefault("classification", None)
                prior.setdefault("mapping_refs", [])
                prior.setdefault("static_check_refs", [])
                prior.setdefault("dynamic_test_refs", [])
                prior.setdefault("artifact_versions", {})
                prior.setdefault("target_dependencies", [])
                prior.setdefault("last_verified_snapshot_hash", None)
                prior.setdefault("last_processed_run", None)
                new_rows[rule_id] = prior
            else:
                if not isinstance(old, dict):
                    raise SyscallGuardError(f"coverage unexpectedly missing unchanged rule {rule_id}")
                current = dict(old)
                current["syscalls"] = rule_syscalls[rule_id]
                if current.get("status") == "mapped":
                    current["last_verified_snapshot_hash"] = snapshot_hash
                    current["reason"] = "相关 Starry 内容指纹未变化，已跳过。"
                new_rows[rule_id] = current

        new_coverage = {
            "schema_version": SCHEMA_VERSION,
            "kind": "syscallguard_starry_rule_coverage",
            "updated_at_utc": generated_at,
            "target": {
                "target_id": "starry",
                "repository_identity": repo_identity,
                "descriptor_hash": target["descriptor_hash"],
                "last_snapshot_hash": snapshot_hash,
            },
            "rules": new_rows,
        }

        index_values: dict[str, dict[str, Any]] = {}
        for section, values in outputs.items():
            if not values:
                continue
            rows = []
            for entity_id, (path, entity, _action) in values.items():
                row = {
                    "id": entity_id,
                    "path": str(path.relative_to(root)),
                    "rule_refs": entity.get("rule_refs", []),
                    "generated_at_utc": entity["generated_at_utc"],
                    "content_hash": version_content_hash(entity),
                    "target_snapshot_hash": entity["target_snapshot_hash"],
                }
                if section == "mappings":
                    row["classification"] = entity["classification"]
                rows.append(row)
            index_values[section] = _merge_index_value(root, section, rows, generated_at)

        actions = [
            action
            for values in outputs.values()
            for _path, _entity, action in values.values()
        ]
        added = sum(1 for rule_id in selected if not isinstance(old_rows.get(rule_id), dict))
        updated = len(selected) - added
        remaining = sorted(pending_ids - selected)
        skipped_rules = sorted(preparation.get("skipped_rule_ids", []))
        manifest["phase"] = "published"
        manifest["status"] = "completed"
        manifest["completed_at_utc"] = generated_at
        manifest["target"] = target
        manifest["rule_index_hash"] = rule_index_hash
        manifest["selected_rule_versions"] = {
            rule_id: versions[rule_id] for rule_id in sorted(selected)
        }
        manifest["rule_syscalls"] = {
            rule_id: rule_syscalls[rule_id] for rule_id in sorted(selected)
        }
        manifest["entities"] = {
            "syscalls": sorted(
                {syscall for rule_id in selected for syscall in rule_syscalls[rule_id]}
            ),
            "rules": sorted(selected),
            "mappings": sorted(outputs["mappings"]),
            "static_checks": sorted(outputs["static_checks"]),
            "dynamic_tests": sorted(outputs["dynamic_tests"]),
        }
        manifest["entity_hashes"] = {
            "rules": {rule_id: version_content_hash(rules[rule_id]) for rule_id in sorted(selected)},
            **{
                section: {
                    entity_id: content_hash(entity)
                    for entity_id, (_path, entity, _action) in values.items()
                }
                for section, values in outputs.items()
            },
        }
        manifest["entity_versions"] = {
            "rules": {rule_id: versions[rule_id] for rule_id in sorted(selected)},
            **artifact_versions,
        }
        manifest["counts"] = {
            "rules_total": len(rules),
            "pending_before": len(pending_ids),
            "processed": len(selected),
            "added": added,
            "updated": updated,
            "skipped": len(skipped_rules),
            "mapped": len(mapped),
            "needs_review": len(needs_review),
            "unsupported": len(unsupported),
            "static_checks": len(outputs["static_checks"]),
            "dynamic_tests": len(outputs["dynamic_tests"]),
            "created_entities": actions.count("created"),
            "updated_entities": actions.count("updated"),
            "skipped_entities": actions.count("skipped"),
            "pending_remaining": len(remaining),
        }
        manifest["processed"] = {
            "mapped": mapped,
            "needs_review": needs_review,
            "unsupported": unsupported,
            "skipped": skipped_rules,
            "pending": remaining,
        }
        manifest["outputs"] = {
            "report": "report.md",
            "preparation": "preparation.yaml",
            "target_descriptor": "target-descriptor.yaml",
            "coverage": str(COVERAGE_PATH),
            "mapping_index": str(INDEX_SPECS["mappings"][0]),
            "static_check_index": str(INDEX_SPECS["static_checks"][0]),
            "dynamic_test_index": str(INDEX_SPECS["dynamic_tests"][0]),
        }
        manifest["error"] = None
        manifest["blockers"] = []
        changeset = load_mapping(run_directory / "changeset.yaml")
        changeset["changes"] = [
            {
                "entity_type": section.rstrip("s"),
                "entity_id": entity_id,
                "action": action,
                "output_hash": version_content_hash(entity),
                "generated_at_utc": entity["generated_at_utc"],
                "path": str(path.relative_to(root)),
            }
            for section, values in outputs.items()
            for entity_id, (path, entity, action) in values.items()
        ]
        changeset["changes"].append(
            {
                "entity_type": "rule_coverage",
                "entity_id": "starry",
                "action": "created" if coverage_hash is None else "updated",
                "output_hash": content_hash(new_coverage),
                "generated_at_utc": generated_at,
                "path": str(COVERAGE_PATH),
            }
        )

        files: list[tuple[Path, str]] = []
        for values in outputs.values():
            files.extend((path, _yaml_text(entity)) for path, entity, _action in values.values())
        for section, index in index_values.items():
            files.append((root / INDEX_SPECS[section][0], _yaml_text(index)))
        files.extend(
            [
                (root / COVERAGE_PATH, _yaml_text(new_coverage)),
                (run_directory / "report.md", _report_text(manifest, preparation)),
                (run_directory / "changeset.yaml", _yaml_text(changeset)),
                (run_directory / "manifest.yaml", _yaml_text(manifest)),
            ]
        )
        _transactional_write(files)
        return run_id
    except BaseException as exc:
        _mark_failed(run_directory, exc)
        if isinstance(exc, SyscallGuardError):
            raise
        raise SyscallGuardError(str(exc)) from exc


def run_mapping(
    syscalls: str | None = None,
    root: Path | None = None,
    requested_run_id: str | None = None,
) -> str:
    run_id = prepare_mapping(syscalls, root, requested_run_id)
    return finalize_mapping(run_id, root)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="增量生成 Starry 规则映射")
    parser.add_argument("--syscalls", help="逗号分隔的 syscall 名称")
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
        elif args.phase == "auto":
            run_id = run_mapping(args.syscalls, args.root, requested)
        else:
            run_id = prepare_mapping(args.syscalls, args.root, requested)
    except SyscallGuardError as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 2
    path = args.root.resolve() / "runs" / run_id
    manifest = load_mapping(path / "manifest.yaml")
    print(f"运行 ID：{run_id}")
    print(f"状态：{manifest['status']}")
    if manifest["status"] == "running":
        print(f"待分析实体：{path / 'staged'}")
        print(f"固定内容快照：{manifest['target']['snapshot_hash']}")
    else:
        counts = manifest["counts"]
        print(
            "新增：{added}，更新：{updated}，跳过：{skipped}，待复核：{needs_review}，"
            "不支持：{unsupported}，静态检查：{static_checks}，动态测试：{dynamic_tests}".format(
                **counts
            )
        )
        print(f"覆盖表：{args.root.resolve() / COVERAGE_PATH}")
    print(f"结果：{path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
