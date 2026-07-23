from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .common import (
    SCHEMA_VERSION,
    SyscallGuardError,
    atomic_write_yaml,
    load_mapping,
    repo_root,
    slug,
)
from .mapping import (
    _load_indexed_entities,
    _result_locations,
    _rule_library,
    _strip_generated,
    _workspace,
    finalize_mapping,
    prepare_mapping,
)


CATALOG_PATH = Path("targets/starry/man-static-checks.yaml")
CATALOG_KIND = "syscallguard_starry_man_static_check_catalog"
CHECK_KIND = "syscallguard_starry_static_check"


def load_man_static_catalog(root: Path | None = None) -> dict[str, Any]:
    root = (root or repo_root()).resolve()
    catalog = load_mapping(root / CATALOG_PATH)
    if catalog.get("kind") != CATALOG_KIND:
        raise SyscallGuardError(f"invalid man static check catalog: {root / CATALOG_PATH}")
    existing = catalog.get("existing_check_refs")
    checks = catalog.get("checks")
    if not isinstance(existing, dict) or not isinstance(checks, list):
        raise SyscallGuardError("man static check catalog must contain existing_check_refs and checks")
    return catalog


def _rule_refs(value: Any, owner: str, *, allow_empty: bool = False) -> list[str]:
    if not isinstance(value, list) or (not value and not allow_empty) or not all(
        isinstance(item, str) and item for item in value
    ):
        raise SyscallGuardError(f"{owner} must have non-empty string rule_refs")
    if len(value) != len(set(value)):
        raise SyscallGuardError(f"{owner} contains duplicate rule_refs")
    return sorted(value)


def _new_check(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise SyscallGuardError("man static check definition must be a mapping")
    check_id = value.get("check_id")
    if not isinstance(check_id, str) or not check_id:
        raise SyscallGuardError("man static check definition has no check_id")
    required = ("title", "applies_to_syscalls", "path", "patterns", "rule_refs")
    if any(key not in value for key in required):
        raise SyscallGuardError(f"man static check {check_id} is missing a required field")
    entity = {
        "schema_version": SCHEMA_VERSION,
        "kind": CHECK_KIND,
        **value,
        "rule_refs": _rule_refs(value.get("rule_refs"), check_id),
    }
    return entity


def materialize_man_static_checks(
    root: Path | None = None,
) -> tuple[dict[str, dict[str, Any]], dict[str, list[str]]]:
    root = (root or repo_root()).resolve()
    catalog = load_man_static_catalog(root)
    rules, _versions, rule_syscalls, _syscall_rules, _index_hash = _rule_library(root)
    indexed = _load_indexed_entities(root, "static_checks")

    checks: dict[str, dict[str, Any]] = {}
    raw_existing = catalog["existing_check_refs"]
    for check_id, raw_refs in sorted(raw_existing.items()):
        if not isinstance(check_id, str) or check_id not in indexed:
            raise SyscallGuardError(f"catalog references unknown static check: {check_id}")
        refs = _rule_refs(raw_refs, check_id, allow_empty=True)
        entity = dict(indexed[check_id])
        entity["rule_refs"] = sorted(
            set(
                str(item)
                for item in entity.get("rule_refs", [])
                if item in rules and not str(item).startswith("MAN_")
            ).union(refs)
        )
        entity["applies_to_syscalls"] = sorted(
            set(str(item) for item in entity.get("applies_to_syscalls", []))
            | {
                syscall
                for rule_id in refs
                for syscall in rule_syscalls.get(rule_id, [])
            }
        )
        checks[check_id] = entity

    for raw in catalog["checks"]:
        definition = _new_check(raw)
        check_id = definition["check_id"]
        if check_id in checks:
            raise SyscallGuardError(f"duplicate man static check id: {check_id}")
        if check_id in indexed:
            entity = {
                **indexed[check_id],
                **definition,
                "rule_refs": sorted(
                    set(
                        str(item)
                        for item in indexed[check_id].get("rule_refs", [])
                        if item in rules and not str(item).startswith("MAN_")
                    ).union(definition["rule_refs"])
                ),
            }
        else:
            entity = definition
        checks[check_id] = entity

    rule_to_checks: dict[str, list[str]] = {}
    for check_id, entity in sorted(checks.items()):
        applies = entity.get("applies_to_syscalls")
        if not isinstance(applies, list) or not applies or not all(
            isinstance(item, str) and item for item in applies
        ):
            raise SyscallGuardError(f"static check {check_id} has invalid applies_to_syscalls")
        path = entity.get("path")
        if not isinstance(path, str) or not path:
            raise SyscallGuardError(f"static check {check_id} has no target path")
        patterns = entity.get("patterns")
        if not isinstance(patterns, list) or not patterns:
            raise SyscallGuardError(f"static check {check_id} has no patterns")
        for pattern in patterns:
            if not isinstance(pattern, dict) or not isinstance(pattern.get("regex"), str):
                raise SyscallGuardError(f"static check {check_id} has an invalid pattern")
            try:
                re.compile(pattern["regex"], re.MULTILINE | re.DOTALL)
            except re.error as exc:
                raise SyscallGuardError(
                    f"static check {check_id} has invalid regex: {exc}"
                ) from exc
        for rule_id in entity["rule_refs"]:
            rule = rules.get(rule_id)
            if rule is None:
                raise SyscallGuardError(
                    f"static check {check_id} references inactive or unknown rule {rule_id}"
                )
            if rule_id.startswith("MAN_") and not any(
                isinstance(source, dict) and source.get("source_type") == "man_pages"
                for source in rule.get("sources", [])
            ):
                raise SyscallGuardError(f"catalog rule {rule_id} has no man-pages provenance")
            owners = set(rule_syscalls.get(rule_id, []))
            if not owners.intersection(applies):
                raise SyscallGuardError(
                    f"static check {check_id} does not apply to owner of {rule_id}: "
                    + ", ".join(sorted(owners))
                )
            rule_to_checks.setdefault(rule_id, []).append(check_id)

    return checks, {key: sorted(value) for key, value in sorted(rule_to_checks.items())}


def publish_man_static_checks(
    branch: str,
    root: Path | None = None,
    requested_run_id: str | None = None,
) -> str:
    root = (root or repo_root()).resolve()
    checks, rule_to_checks = materialize_man_static_checks(root)
    indexed = _load_indexed_entities(root, "static_checks")
    man_rule_ids = sorted(rule_id for rule_id in rule_to_checks if rule_id.startswith("MAN_"))
    prior_man_rule_ids = {
        str(rule_id)
        for check_id in checks
        for rule_id in indexed.get(check_id, {}).get("rule_refs", [])
        if str(rule_id).startswith("MAN_")
    }
    retired_man_rule_ids = sorted(prior_man_rule_ids - set(man_rule_ids))
    forced = sorted(set(rule_to_checks).union(retired_man_rule_ids))
    run_id = prepare_mapping(
        root=root,
        requested_run_id=requested_run_id,
        branch=branch,
        coverage="static-only",
        force_rule_ids=forced,
    )
    workspace = _workspace(run_id)

    for check_id, entity in checks.items():
        stage_entity = _strip_generated(entity)
        atomic_write_yaml(
            workspace
            / "staged/targets/starry/static-checks"
            / f"{slug(check_id)}.yaml",
            stage_entity,
        )

    for rule_id in man_rule_ids:
        result_path = workspace / "staged/rule-results" / f"{slug(rule_id)}.yaml"
        result = load_mapping(result_path)
        mapped_checks = {check_id: checks[check_id] for check_id in rule_to_checks[rule_id]}
        result.update(
            {
                "status": "covered",
                "target_locations": _result_locations(mapped_checks, {}),
                "static_check_refs": sorted(mapped_checks),
                "dynamic_test_refs": [],
                "reason": "man-pages 条款已对应到可执行的 Starry 源码静态检查。",
            }
        )
        result.pop("deferred", None)
        atomic_write_yaml(result_path, result)

    for rule_id in retired_man_rule_ids:
        result_path = workspace / "staged/rule-results" / f"{slug(rule_id)}.yaml"
        result = load_mapping(result_path)
        result.update(
            {
                "status": "needs_review",
                "target_locations": [],
                "static_check_refs": [],
                "dynamic_test_refs": [],
                "reason": "现有静态证据不足以完整证明该 man-pages 条款。",
                "deferred": "dynamic_test",
            }
        )
        atomic_write_yaml(result_path, result)

    return finalize_mapping(run_id, root)
