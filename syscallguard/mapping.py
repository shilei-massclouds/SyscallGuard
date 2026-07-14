from __future__ import annotations

import argparse
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
    ensure_target_descriptor,
    entity_hash,
    load_index,
    load_mapping,
    new_run_id,
    publish_yaml_entities,
    repo_root,
    slug,
    update_index,
    utc_now,
    version_content_hash,
)
from .ingest import assert_latest_ingest_report, load_ingest_report


CLASSIFICATIONS = {"static", "partial_static", "dynamic", "unsupported", "needs_review"}


def _entity_path(root: Path, section: str, entity_id: str) -> Path:
    return root / section / f"{slug(entity_id)}.yaml"


def _matching_index_entries(
    root: Path,
    index_path: Path,
    kind: str,
    rule_ids: set[str],
) -> list[dict[str, Any]]:
    index = load_index(index_path, kind)
    result: list[dict[str, Any]] = []
    for entry in index["entities"]:
        if not isinstance(entry, dict):
            continue
        refs = entry.get("rule_refs", [])
        if isinstance(refs, list) and rule_ids.intersection(str(item) for item in refs):
            result.append(entry)
    return result


def _load_index_entity(root: Path, entry: dict[str, Any]) -> tuple[Path, dict[str, Any]]:
    raw_path = entry.get("path")
    if not isinstance(raw_path, str) or not raw_path:
        raise SyscallGuardError(f"index entry is missing path: {entry!r}")
    path = root / raw_path
    return path, load_mapping(path)


def _rule_hashes(
    root: Path, rule_ids: list[str]
) -> tuple[dict[str, str], dict[str, Any], dict[str, dict[str, str]]]:
    hashes: dict[str, str] = {}
    rules: dict[str, Any] = {}
    versions: dict[str, dict[str, str]] = {}
    for rule_id in rule_ids:
        path = _entity_path(root, "library/rules", rule_id)
        rule = load_mapping(path)
        if rule.get("kind") != "syscallguard_rule" or rule.get("rule_id") != rule_id:
            raise SyscallGuardError(f"invalid rule entity for {rule_id}: {path}")
        hashes[rule_id] = version_content_hash(rule)
        rules[rule_id] = rule
        versions[rule_id] = entity_version(rule_id, rule)
    return hashes, rules, versions


def _report_rules(
    report: dict[str, Any],
) -> tuple[list[str], list[str], dict[str, list[str]], dict[str, dict[str, str]]]:
    syscall_ids: list[str] = []
    rule_syscalls: dict[str, list[str]] = {}
    versions: dict[str, dict[str, str]] = {}
    rows = report.get("syscalls", [])
    if not isinstance(rows, list):
        raise SyscallGuardError(f"ingest report {report.get('report_id')} has invalid syscalls")
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("syscall"), str):
            raise SyscallGuardError(f"ingest report {report.get('report_id')} has invalid syscalls")
        syscall = row["syscall"]
        syscall_ids.append(syscall)
        rule_rows = row.get("rules", [])
        if not isinstance(rule_rows, list):
            raise SyscallGuardError(f"ingest report {report.get('report_id')} has invalid rules")
        if row.get("result") == "no_rules" and rule_rows:
            raise SyscallGuardError(
                f"ingest report {report.get('report_id')} publishes rules for no_rules syscall {syscall}"
            )
        for version in rule_rows:
            if not isinstance(version, dict) or not all(
                isinstance(version.get(key), str)
                for key in ("id", "generated_at_utc", "content_hash")
            ):
                raise SyscallGuardError(
                    f"ingest report {report.get('report_id')} has an invalid rule version"
                )
            rule_id = version["id"]
            normalized = {
                "id": rule_id,
                "generated_at_utc": version["generated_at_utc"],
                "content_hash": version["content_hash"],
            }
            if rule_id in versions and versions[rule_id] != normalized:
                raise SyscallGuardError(
                    f"ingest report {report.get('report_id')} records conflicting versions for {rule_id}"
                )
            versions[rule_id] = normalized
            rule_syscalls.setdefault(rule_id, [])
            if syscall not in rule_syscalls[rule_id]:
                rule_syscalls[rule_id].append(syscall)
    return (
        sorted(versions),
        sorted(set(syscall_ids)),
        {rule_id: sorted(syscalls) for rule_id, syscalls in sorted(rule_syscalls.items())},
        versions,
    )


def _assert_report_versions(
    report: dict[str, Any],
    versions: dict[str, dict[str, str]],
    rules: dict[str, dict[str, Any]],
) -> None:
    for rule_id, recorded in versions.items():
        mismatch = dependency_mismatch(recorded, rule_id, rules[rule_id])
        if mismatch:
            raise SyscallGuardError(
                f"stale ingest report {report.get('report_id')}: {mismatch}"
            )


def _mapping_for_rule(
    root: Path,
    rule_id: str,
    rule_version: dict[str, str],
    base_commit: str,
    target_hash: str,
    generated_at: str,
) -> tuple[str, dict[str, Any], str]:
    mapping_id = f"starry-{slug(rule_id)}"
    path = _entity_path(root, "targets/starry/mappings", mapping_id)
    if path.exists():
        mapping = load_mapping(path)
        same_input = mapping.get("upstream_dependencies") == [rule_version]
        same_target = mapping.get("target_hash") == target_hash
        action = "skipped" if same_input and same_target else "updated"
        mapping = dict(mapping)
    else:
        action = "created"
        mapping = {
            "schema_version": SCHEMA_VERSION,
            "kind": "syscallguard_starry_mapping",
            "mapping_id": mapping_id,
            "rule_refs": [rule_id],
            "classification": "needs_review",
            "target_locations": [],
            "static_check_refs": [],
            "dynamic_test_refs": [],
            "reason": "No reusable Starry mapping exists yet; inspect the pinned target revision.",
        }
    classification = mapping.get("classification")
    if classification not in CLASSIFICATIONS:
        raise SyscallGuardError(
            f"mapping {mapping_id} has invalid classification {classification!r}"
        )
    mapping.update(
        {
            "schema_version": SCHEMA_VERSION,
            "kind": "syscallguard_starry_mapping",
            "mapping_id": mapping_id,
            "rule_refs": [rule_id],
            "upstream_dependencies": [rule_version],
            "base_commit": base_commit,
            "target_hash": target_hash,
            "generated_at_utc": mapping.get("generated_at_utc")
            if action == "skipped"
            else generated_at,
        }
    )
    return mapping_id, mapping, action


def _refresh_existing_entity(
    entity: dict[str, Any],
    dependencies: list[dict[str, str]],
    base_commit: str,
    target_hash: str,
    generated_at: str,
    recorded_hash: str | None,
) -> tuple[dict[str, Any], str]:
    same_target = entity.get("target_hash") == target_hash
    same_input = entity.get("upstream_dependencies") == dependencies
    same_content = recorded_hash == version_content_hash(entity)
    result = dict(entity)
    result.update(
        {
            "upstream_dependencies": dependencies,
            "base_commit": base_commit,
            "target_hash": target_hash,
            "generated_at_utc": entity.get("generated_at_utc")
            if same_target and same_input and same_content
            else generated_at,
        }
    )
    return result, "skipped" if same_target and same_input and same_content else "updated"


def _report(recorder: RunRecorder) -> None:
    counts = recorder.manifest["counts"]
    lines = [
        "# Starry Mapping Result",
        "",
        f"Run: `{recorder.run_id}`",
        f"Base commit: `{recorder.manifest['target']['base_commit']}`",
        "",
        f"- Rules: {counts['rules']}",
        f"- Mappings: {counts['mappings']}",
        f"- Static checks: {counts['static_checks']}",
        f"- Dynamic tests: {counts['dynamic_tests']}",
        f"- Skipped unchanged entities: {counts['skipped_unchanged']}",
        f"- Needs review: {counts['needs_review']}",
        "",
        "Shared entities are the current editable view. The run manifest records their hashes.",
    ]
    atomic_write_text(recorder.directory / "report.md", "\n".join(lines) + "\n")


def run_mapping(
    from_report_id: str,
    target: Path,
    root: Path | None = None,
    requested_run_id: str | None = None,
) -> str:
    root = (root or repo_root()).resolve()
    report = load_ingest_report(root, from_report_id)
    assert_latest_ingest_report(root, report)
    rule_ids, syscall_ids, rule_syscalls, recorded_rule_versions = _report_rules(report)
    run_id = requested_run_id or new_run_id(
        "mapping", {"from": from_report_id, "target": str(target.resolve()), "at": utc_now()}
    )
    recorder = RunRecorder(
        root,
        "mapping",
        run_id,
        {"from": from_report_id, "target": str(target.resolve())},
        from_report_id,
    )
    try:
        descriptor, repository, base_commit = ensure_target_descriptor(target.resolve())
        descriptor_hash = entity_hash(target.resolve())
        target_hash = content_hash(
            {
                "target_id": "starry",
                "base_commit": base_commit,
                "descriptor": descriptor,
            }
        )
        rule_hashes, rules, rule_versions = _rule_hashes(root, rule_ids)
        _assert_report_versions(report, recorded_rule_versions, rules)
        generated_at = utc_now()
        atomic_write_yaml(recorder.directory / "target-descriptor.yaml", descriptor)

        existing_mapping_entries = _matching_index_entries(
            root,
            root / "targets/starry/mappings/index.yaml",
            "syscallguard_starry_mapping_index",
            set(rule_ids),
        )
        mappings: dict[str, tuple[Path, dict[str, Any], str]] = {}
        covered_rules: set[str] = set()
        for entry in existing_mapping_entries:
            path, mapping = _load_index_entity(root, entry)
            mapping_id = mapping.get("mapping_id")
            refs = mapping.get("rule_refs", [])
            if not isinstance(mapping_id, str) or not isinstance(refs, list):
                raise SyscallGuardError(f"invalid Starry mapping entity: {path}")
            selected_refs = [ref for ref in refs if ref in rule_hashes]
            if not selected_refs:
                continue
            classification = mapping.get("classification")
            if classification not in CLASSIFICATIONS:
                raise SyscallGuardError(
                    f"mapping {mapping_id} has invalid classification {classification!r}"
                )
            dependencies = [rule_versions[ref] for ref in sorted(selected_refs)]
            same_input = mapping.get("upstream_dependencies") == dependencies
            same_target = mapping.get("target_hash") == target_hash
            same_content = entry.get("content_hash") == version_content_hash(mapping)
            updated = dict(mapping)
            updated.update(
                {
                    "upstream_dependencies": dependencies,
                    "base_commit": base_commit,
                    "target_hash": target_hash,
                    "generated_at_utc": mapping.get("generated_at_utc")
                    if same_input and same_target and same_content
                    else generated_at,
                }
            )
            mappings[mapping_id] = (
                path,
                updated,
                "skipped" if same_input and same_target and same_content else "updated",
            )
            covered_rules.update(selected_refs)
        for rule_id in rule_ids:
            if rule_id in covered_rules:
                continue
            mapping_id, mapping, action = _mapping_for_rule(
                root,
                rule_id,
                rule_versions[rule_id],
                base_commit,
                target_hash,
                generated_at,
            )
            path = _entity_path(root, "targets/starry/mappings", mapping_id)
            mappings[mapping_id] = (path, mapping, action)

        static_entries = _matching_index_entries(
            root,
            root / "targets/starry/static-checks/index.yaml",
            "syscallguard_starry_static_check_index",
            set(rule_ids),
        )
        static_checks: dict[str, tuple[Path, dict[str, Any], str]] = {}
        for entry in static_entries:
            path, entity = _load_index_entity(root, entry)
            check_id = entity.get("check_id")
            if not isinstance(check_id, str):
                raise SyscallGuardError(f"static check has no check_id: {path}")
            refreshed, action = _refresh_existing_entity(
                entity,
                [rule_versions[ref] for ref in sorted(entity.get("rule_refs", [])) if ref in rule_versions],
                base_commit,
                target_hash,
                generated_at,
                str(entry.get("content_hash")) if entry.get("content_hash") else None,
            )
            static_checks[check_id] = (path, refreshed, action)

        dynamic_entries = _matching_index_entries(
            root,
            root / "targets/starry/dynamic-tests/index.yaml",
            "syscallguard_starry_dynamic_test_index",
            set(rule_ids),
        )
        dynamic_tests: dict[str, tuple[Path, dict[str, Any], str]] = {}
        for entry in dynamic_entries:
            path, entity = _load_index_entity(root, entry)
            test_id = entity.get("test_id")
            if not isinstance(test_id, str):
                raise SyscallGuardError(f"dynamic test has no test_id: {path}")
            refreshed, action = _refresh_existing_entity(
                entity,
                [rule_versions[ref] for ref in sorted(entity.get("rule_refs", [])) if ref in rule_versions],
                base_commit,
                target_hash,
                generated_at,
                str(entry.get("content_hash")) if entry.get("content_hash") else None,
            )
            dynamic_tests[test_id] = (path, refreshed, action)

        publish_yaml_entities(
            [
                (recorder.directory, path, entity)
                for path, entity, _action in [
                    *mappings.values(),
                    *static_checks.values(),
                    *dynamic_tests.values(),
                ]
            ]
        )
        update_index(
            root / "targets/starry/mappings/index.yaml",
            "syscallguard_starry_mapping_index",
            [
                {
                    "id": mapping_id,
                    "path": str(path.relative_to(root)),
                    "rule_refs": entity.get("rule_refs", []),
                    "classification": entity.get("classification"),
                    "generated_at_utc": entity["generated_at_utc"],
                    "content_hash": version_content_hash(entity),
                    "target_hash": target_hash,
                }
                for mapping_id, (path, entity, _action) in mappings.items()
            ],
        )
        update_index(
            root / "targets/starry/static-checks/index.yaml",
            "syscallguard_starry_static_check_index",
            [
                {
                    "id": check_id,
                    "path": str(path.relative_to(root)),
                    "rule_refs": entity.get("rule_refs", []),
                    "generated_at_utc": entity["generated_at_utc"],
                    "content_hash": version_content_hash(entity),
                    "target_hash": target_hash,
                }
                for check_id, (path, entity, _action) in static_checks.items()
            ],
        )
        update_index(
            root / "targets/starry/dynamic-tests/index.yaml",
            "syscallguard_starry_dynamic_test_index",
            [
                {
                    "id": test_id,
                    "path": str(path.relative_to(root)),
                    "rule_refs": entity.get("rule_refs", []),
                    "generated_at_utc": entity["generated_at_utc"],
                    "content_hash": version_content_hash(entity),
                    "target_hash": target_hash,
                }
                for test_id, (path, entity, _action) in dynamic_tests.items()
            ],
        )

        mapping_ids = sorted(mappings)
        static_ids = sorted(static_checks)
        dynamic_ids = sorted(dynamic_tests)
        recorder.manifest["target"] = {
            "target_id": "starry",
            "repository": str(repository),
            "base_commit": base_commit,
            "target_hash": target_hash,
            "descriptor_hash": descriptor_hash,
        }
        recorder.manifest["entities"] = {
            "syscalls": syscall_ids,
            "rules": rule_ids,
            "mappings": mapping_ids,
            "static_checks": static_ids,
            "dynamic_tests": dynamic_ids,
        }
        recorder.manifest["rule_syscalls"] = rule_syscalls
        recorder.manifest["entity_hashes"] = {
            "rules": rule_hashes,
            "mappings": {
                entity_id: entity_hash(path)
                for entity_id, (path, _entity, _action) in mappings.items()
            },
            "static_checks": {
                entity_id: entity_hash(path)
                for entity_id, (path, _entity, _action) in static_checks.items()
            },
            "dynamic_tests": {
                entity_id: entity_hash(path)
                for entity_id, (path, _entity, _action) in dynamic_tests.items()
            },
        }
        recorder.manifest["entity_versions"] = {
            "rules": rule_versions,
            "mappings": {
                entity_id: entity_version(entity_id, entity)
                for entity_id, (_path, entity, _action) in mappings.items()
            },
            "static_checks": {
                entity_id: entity_version(entity_id, entity)
                for entity_id, (_path, entity, _action) in static_checks.items()
            },
            "dynamic_tests": {
                entity_id: entity_version(entity_id, entity)
                for entity_id, (_path, entity, _action) in dynamic_tests.items()
            },
        }
        all_actions = [
            action
            for _path, _entity, action in [
                *mappings.values(),
                *static_checks.values(),
                *dynamic_tests.values(),
            ]
        ]
        recorder.manifest["counts"] = {
            "rules": len(rule_ids),
            "mappings": len(mapping_ids),
            "static_checks": len(static_ids),
            "dynamic_tests": len(dynamic_ids),
            "skipped_unchanged": all_actions.count("skipped"),
            "needs_review": sum(
                1 for _path, entity, _action in mappings.values()
                if entity.get("classification") == "needs_review"
            ),
        }
        for entity_type, values in (
            ("mapping", mappings),
            ("static_check", static_checks),
            ("dynamic_test", dynamic_tests),
        ):
            for entity_id, (path, entity, action) in values.items():
                recorder.changeset["changes"].append(
                    {
                        "entity_type": entity_type,
                        "entity_id": entity_id,
                        "action": action,
                        "output_hash": version_content_hash(entity),
                        "generated_at_utc": entity["generated_at_utc"],
                        "path": str(path.relative_to(root)),
                    }
                )
        recorder.manifest["outputs"] = {
            "report": "report.md",
            "target_descriptor": "target-descriptor.yaml",
            "mapping_index": "targets/starry/mappings/index.yaml",
            "static_check_index": "targets/starry/static-checks/index.yaml",
            "dynamic_test_index": "targets/starry/dynamic-tests/index.yaml",
        }
        _report(recorder)
        recorder.complete()
        return run_id
    except BaseException as exc:
        recorder.fail(exc)
        if isinstance(exc, SyscallGuardError):
            raise
        raise SyscallGuardError(str(exc)) from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Map incremental rules to Starry checks")
    parser.add_argument("--from", dest="from_report_id", required=True, help="ingest report id")
    parser.add_argument("--target", required=True, type=Path, help="Starry target descriptor")
    parser.add_argument("--root", type=Path, default=repo_root(), help=argparse.SUPPRESS)
    parser.add_argument("--run-id", help=argparse.SUPPRESS)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    requested_run_id = args.run_id or new_run_id(
        "mapping", {"from": args.from_report_id, "target": str(args.target)}
    )
    try:
        run_id = run_mapping(args.from_report_id, args.target, args.root, requested_run_id)
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
    print(f"mapping_index: {args.root.resolve() / 'targets/starry/mappings/index.yaml'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
