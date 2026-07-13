from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path
from types import ModuleType
from typing import Any

from . import __version__
from .common import (
    SCHEMA_VERSION,
    RunRecorder,
    SyscallGuardError,
    append_history,
    atomic_write_yaml,
    content_hash,
    entity_hash,
    git_output,
    load_mapping,
    load_yaml,
    new_run_id,
    publish_yaml_entities,
    repo_root,
    slug,
    tree_hash,
    update_index,
    utc_now,
)


ADAPTER = "ltp-extractor"
ADAPTER_VERSION = "1"


def import_extractor(path: Path) -> ModuleType:
    if not path.is_file():
        raise SyscallGuardError(f"LTP extractor does not exist: {path}")
    spec = importlib.util.spec_from_file_location("syscallguard_ltp_extractor", path)
    if spec is None or spec.loader is None:
        raise SyscallGuardError(f"cannot import LTP extractor: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    try:
        spec.loader.exec_module(module)
    except Exception as exc:
        raise SyscallGuardError(f"cannot load LTP extractor {path}: {exc}") from exc
    required = [
        "ManifestEntry",
        "build_candidates",
        "normalize_specs",
        "write_candidates",
        "write_normalized_specs",
    ]
    missing = [name for name in required if not hasattr(module, name)]
    if missing:
        raise SyscallGuardError(f"LTP extractor is missing APIs: {', '.join(missing)}")
    return module


def require_descriptor(path: Path) -> tuple[dict[str, Any], Path, Path, str]:
    descriptor = load_mapping(path)
    source_id = descriptor.get("source_id")
    if not isinstance(source_id, str) or not source_id:
        raise SyscallGuardError(f"source descriptor must define source_id: {path}")
    if descriptor.get("adapter") != ADAPTER:
        raise SyscallGuardError(
            f"unsupported source adapter {descriptor.get('adapter')!r}; expected {ADAPTER!r}"
        )
    raw_location = descriptor.get("location")
    if not isinstance(raw_location, str) or not raw_location:
        raise SyscallGuardError(f"source descriptor must define location: {path}")
    location = Path(raw_location).expanduser().resolve()
    if not location.is_dir():
        raise SyscallGuardError(f"source location does not exist: {location}")
    revision = descriptor.get("revision")
    if not isinstance(revision, str) or not revision:
        raise SyscallGuardError(f"source descriptor must define revision: {path}")
    try:
        resolved_revision = git_output(location, ["rev-parse", f"{revision}^{{commit}}"])
    except SyscallGuardError as exc:
        raise SyscallGuardError(f"cannot resolve source revision {revision!r}: {exc}") from exc
    parameters = descriptor.get("parameters", {})
    if not isinstance(parameters, dict):
        raise SyscallGuardError(f"source descriptor parameters must be a mapping: {path}")
    raw_tool = parameters.get("tool", "tools/syscall_spec_extract.py")
    if not isinstance(raw_tool, str) or not raw_tool:
        raise SyscallGuardError("source descriptor parameters.tool must be a path")
    tool = Path(raw_tool).expanduser()
    if not tool.is_absolute():
        tool = location / tool
    return descriptor, location, tool.resolve(), resolved_revision


def candidate_order(descriptor: dict[str, Any], location: Path) -> list[str]:
    parameters = descriptor.get("parameters", {})
    configured = parameters.get("syscalls")
    if configured is not None:
        if not isinstance(configured, list) or not all(
            isinstance(item, str) and item for item in configured
        ):
            raise SyscallGuardError("source descriptor parameters.syscalls must be a string list")
        result: list[str] = []
        seen: set[str] = set()
        for item in configured:
            value = item.lower()
            if value not in seen:
                result.append(value)
                seen.add(value)
        return result
    syscalls_root = location / "testcases" / "kernel" / "syscalls"
    if not syscalls_root.is_dir():
        raise SyscallGuardError(
            "cannot discover syscalls: set parameters.syscalls or provide testcases/kernel/syscalls"
        )
    return sorted(path.name.lower() for path in syscalls_root.iterdir() if path.is_dir())


def ltp_dirs(syscall: str, module: ModuleType, location: Path) -> list[str]:
    aliases = getattr(module, "ALIASES", {})
    candidates = [syscall]
    if isinstance(aliases, dict):
        raw_aliases = aliases.get(syscall, [])
        if isinstance(raw_aliases, list):
            candidates.extend(str(item) for item in raw_aliases)
    root = location / "testcases" / "kernel" / "syscalls"
    result: list[str] = []
    for candidate in candidates:
        if candidate not in result and (root / candidate).is_dir():
            result.append(candidate)
    return result


def source_fingerprint(
    descriptor: dict[str, Any],
    location: Path,
    tool: Path,
    syscall: str,
    directories: list[str],
) -> str:
    syscalls_root = location / "testcases" / "kernel" / "syscalls"
    source_paths = [syscalls_root / item for item in directories]
    payload = {
        "source_id": descriptor["source_id"],
        "adapter": ADAPTER,
        "adapter_version": ADAPTER_VERSION,
        "tool_version": __version__,
        "syscall": syscall,
        "ltp_dirs": directories,
        "source_tree_hash": tree_hash(source_paths, location),
        "extractor_hash": tree_hash([tool], location),
        "adapter_parameters": descriptor.get("parameters", {}),
    }
    return content_hash(payload)


def existing_spec_fingerprint(root: Path, syscall: str) -> str | None:
    path = root / "library" / "specs" / f"{slug(syscall)}.yaml"
    if not path.exists():
        return None
    value = load_mapping(path)
    fingerprint = value.get("source_fingerprint")
    return fingerprint if isinstance(fingerprint, str) else None


def write_extractor_outputs(
    module: ModuleType,
    run: RunRecorder,
    selected: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    entry_type = getattr(module, "ManifestEntry")
    entries = [
        entry_type(name=item["syscall"], group="syscallguard_increment", ltp_dirs=item["ltp_dirs"])
        for item in selected
    ]
    candidates, summaries = module.build_candidates(entries)
    specs = module.normalize_specs(candidates)
    raw_path = run.directory / "raw-candidates.yaml"
    normalized_path = run.directory / "normalized-specs.yaml"
    module.write_candidates(raw_path, candidates)
    module.write_normalized_specs(normalized_path, specs)
    raw_data = load_mapping(raw_path).get("candidates", [])
    normalized_data = load_mapping(normalized_path).get("specs", [])
    if not isinstance(raw_data, list) or not isinstance(normalized_data, list):
        raise SyscallGuardError("LTP extractor produced invalid candidate/spec lists")
    atomic_write_yaml(
        run.directory / "extract-summary.yaml",
        {
            "schema_version": SCHEMA_VERSION,
            "kind": "syscallguard_ltp_extract_summary",
            "candidate_summaries": summaries,
            "raw_candidates": len(raw_data),
            "normalized_specs": len(normalized_data),
        },
    )
    return raw_data, normalized_data


def semantic_for(spec: dict[str, Any]) -> dict[str, Any]:
    expected = spec.get("expected", {})
    errno: list[str] = []
    if isinstance(expected, dict) and isinstance(expected.get("errno"), str):
        errno = [expected["errno"]]
    return {
        "preconditions": spec.get("preconditions", []),
        "action": {
            "operation": "invoke_syscall",
            "syscall": spec.get("syscall"),
            "arguments": spec.get("args", []),
        },
        "expected_result": expected,
        "errno": errno,
    }


def provenance_for(spec: dict[str, Any], descriptor: dict[str, Any], revision: str) -> dict[str, Any]:
    source = spec.get("source", {})
    return {
        "source_id": descriptor["source_id"],
        "revision": revision,
        "file": source.get("file") if isinstance(source, dict) else None,
        "line": source.get("line") if isinstance(source, dict) else None,
        "case": spec.get("case"),
        "confidence": spec.get("confidence"),
    }


def merge_rule(
    root: Path,
    rule_id: str,
    semantics: dict[str, Any],
    provenance: dict[str, Any],
    run_id: str,
    conflicts: list[dict[str, Any]],
) -> tuple[str, dict[str, Any], str]:
    preferred = rule_id
    path = root / "library" / "rules" / f"{slug(preferred)}.yaml"
    action = "created"
    if path.exists():
        existing = load_mapping(path)
        if existing.get("semantics") != semantics:
            variant = content_hash(semantics).split(":", 1)[1][:12]
            rule_id = f"{preferred}--{variant}"
            path = root / "library" / "rules" / f"{slug(rule_id)}.yaml"
            conflicts.append(
                {
                    "preferred_rule_id": preferred,
                    "variant_rule_id": rule_id,
                    "reason": "same stable id has different semantics",
                }
            )
            existing = load_mapping(path) if path.exists() else {}
        provenance_rows = existing.get("provenance", [])
        if not isinstance(provenance_rows, list):
            provenance_rows = []
        if content_hash(provenance) not in {content_hash(item) for item in provenance_rows}:
            provenance_rows.append(provenance)
            action = "updated"
        else:
            action = "unchanged"
        entity = dict(existing)
        entity.update(
            {
                "schema_version": SCHEMA_VERSION,
                "kind": "syscallguard_rule",
                "rule_id": rule_id,
                "semantics": semantics,
                "provenance": provenance_rows,
                "last_processed_run": run_id,
            }
        )
    else:
        entity = {
            "schema_version": SCHEMA_VERSION,
            "kind": "syscallguard_rule",
            "rule_id": rule_id,
            "semantics": semantics,
            "provenance": [provenance],
            "last_processed_run": run_id,
        }
    return rule_id, entity, action


def merge_rule_for_run(
    root: Path,
    staged: dict[str, tuple[dict[str, Any], str]],
    preferred: str,
    semantics: dict[str, Any],
    provenance: dict[str, Any],
    run_id: str,
    conflicts: list[dict[str, Any]],
) -> tuple[str, dict[str, Any], str]:
    rule_id = preferred
    staged_row = staged.get(rule_id)
    if staged_row is not None and staged_row[0].get("semantics") != semantics:
        variant = content_hash(semantics).split(":", 1)[1][:12]
        rule_id = f"{preferred}--{variant}"
        conflicts.append(
            {
                "preferred_rule_id": preferred,
                "variant_rule_id": rule_id,
                "reason": "same stable id has different semantics",
            }
        )
        staged_row = staged.get(rule_id)
    if staged_row is None:
        return merge_rule(
            root, rule_id, semantics, provenance, run_id, conflicts
        )
    entity = dict(staged_row[0])
    provenance_rows = entity.get("provenance", [])
    if not isinstance(provenance_rows, list):
        provenance_rows = []
    action = staged_row[1]
    if content_hash(provenance) not in {content_hash(item) for item in provenance_rows}:
        provenance_rows.append(provenance)
        if action == "unchanged":
            action = "updated"
    entity["provenance"] = provenance_rows
    entity["last_processed_run"] = run_id
    return rule_id, entity, action


def run_ingest(
    source: Path,
    count: int,
    root: Path | None = None,
    requested_run_id: str | None = None,
) -> str:
    if count <= 0:
        raise SyscallGuardError("count must be a positive integer")
    root = (root or repo_root()).resolve()
    seed = {"source": str(source.resolve()), "count": count, "at": utc_now()}
    run_id = requested_run_id or new_run_id("spec", seed)
    recorder = RunRecorder(
        root,
        "spec",
        run_id,
        {"source": str(source.resolve()), "count": count},
    )
    try:
        descriptor, location, tool, revision = require_descriptor(source.resolve())
        module = import_extractor(tool)
        candidates: list[dict[str, Any]] = []
        for syscall in candidate_order(descriptor, location):
            directories = ltp_dirs(syscall, module, location)
            fingerprint = source_fingerprint(
                descriptor, location, tool, syscall, directories
            )
            candidates.append(
                {
                    "syscall": syscall,
                    "ltp_dirs": directories,
                    "fingerprint": fingerprint,
                    "prior_fingerprint": existing_spec_fingerprint(root, syscall),
                }
            )
        changed = [item for item in candidates if item["fingerprint"] != item["prior_fingerprint"]]
        selected = changed[:count]
        recorder.manifest["source"] = {
            "source_id": descriptor["source_id"],
            "adapter": ADAPTER,
            "adapter_version": ADAPTER_VERSION,
            "location": str(location),
            "revision": revision,
            "descriptor_hash": entity_hash(source.resolve()),
        }
        recorder.manifest["selection"] = {
            "stable_order": [item["syscall"] for item in candidates],
            "changed_or_new": [item["syscall"] for item in changed],
            "selected": [item["syscall"] for item in selected],
            "requested_count": count,
            "available_count": len(changed),
        }
        if not selected:
            recorder.manifest["entities"] = {"syscalls": [], "rules": []}
            recorder.manifest["counts"] = {
                "selected_syscalls": 0,
                "normalized_specs": 0,
                "rules": 0,
                "skipped_unchanged_syscalls": len(candidates),
            }
            recorder.complete()
            return run_id

        raw_rows, normalized_rows = write_extractor_outputs(module, recorder, selected)
        by_syscall: dict[str, list[dict[str, Any]]] = {
            item["syscall"]: [] for item in selected
        }
        for spec in normalized_rows:
            if isinstance(spec, dict) and spec.get("syscall") in by_syscall:
                by_syscall[str(spec["syscall"])].append(spec)

        staged_rules: dict[str, tuple[dict[str, Any], str]] = {}
        syscall_entities: list[tuple[Path, Path, Any]] = []
        rule_refs_by_syscall: dict[str, list[str]] = {}
        for item in selected:
            syscall = item["syscall"]
            rule_refs: list[str] = []
            for spec in by_syscall[syscall]:
                semantics = semantic_for(spec)
                preferred = spec.get("rule_id")
                if not isinstance(preferred, str) or not preferred:
                    preferred = "LTP_" + content_hash(semantics).split(":", 1)[1][:16].upper()
                rule_id, rule, action = merge_rule_for_run(
                    root,
                    staged_rules,
                    preferred,
                    semantics,
                    provenance_for(spec, descriptor, revision),
                    run_id,
                    recorder.changeset["conflicts"],
                )
                staged_rules[rule_id] = (rule, action)
                if rule_id not in rule_refs:
                    rule_refs.append(rule_id)
            rule_refs_by_syscall[syscall] = rule_refs
            entity = {
                "schema_version": SCHEMA_VERSION,
                "kind": "syscallguard_syscall_spec",
                "syscall": syscall,
                "source_records": [
                    {
                        "source_id": descriptor["source_id"],
                        "adapter": ADAPTER,
                        "location": str(location),
                        "revision": revision,
                        "ltp_dirs": item["ltp_dirs"],
                    }
                ],
                "normalized_behaviors": by_syscall[syscall],
                "rule_refs": rule_refs,
                "source_fingerprint": item["fingerprint"],
                "last_processed_run": run_id,
            }
            destination = root / "library" / "specs" / f"{slug(syscall)}.yaml"
            syscall_entities.append((recorder.directory, destination, entity))
            recorder.changeset["changes"].append(
                {
                    "entity_type": "syscall_spec",
                    "entity_id": syscall,
                    "action": "created" if item["prior_fingerprint"] is None else "updated",
                    "input_hash": item["fingerprint"],
                    "output_hash": content_hash(entity),
                    "path": str(destination.relative_to(root)),
                }
            )

        rule_entities: list[tuple[Path, Path, Any]] = []
        for rule_id, (entity, action) in sorted(staged_rules.items()):
            destination = root / "library" / "rules" / f"{slug(rule_id)}.yaml"
            rule_entities.append((recorder.directory, destination, entity))
            recorder.changeset["changes"].append(
                {
                    "entity_type": "rule",
                    "entity_id": rule_id,
                    "action": action,
                    "input_hash": content_hash(entity["semantics"]),
                    "output_hash": content_hash(entity),
                    "path": str(destination.relative_to(root)),
                }
            )

        publish_yaml_entities([*syscall_entities, *rule_entities])
        update_index(
            root / "library" / "specs" / "index.yaml",
            "syscallguard_spec_index",
            [
                {
                    "id": item["syscall"],
                    "path": f"library/specs/{slug(item['syscall'])}.yaml",
                    "input_hash": item["fingerprint"],
                    "processed_run": run_id,
                }
                for item in selected
            ],
        )
        update_index(
            root / "library" / "rules" / "index.yaml",
            "syscallguard_rule_index",
            [
                {
                    "id": rule_id,
                    "path": f"library/rules/{slug(rule_id)}.yaml",
                    "content_hash": content_hash(entity),
                    "processed_run": run_id,
                }
                for rule_id, (entity, _action) in sorted(staged_rules.items())
            ],
        )
        append_history(
            root,
            [
                {
                    "entity_type": "syscall_spec",
                    "entity_id": item["syscall"],
                    "input_hash": item["fingerprint"],
                    "processed_run": run_id,
                    "finding_status": "unknown",
                    "fix_status": "unknown",
                }
                for item in selected
            ],
        )
        rule_ids = sorted(staged_rules)
        recorder.manifest["entities"] = {
            "syscalls": [item["syscall"] for item in selected],
            "rules": rule_ids,
        }
        recorder.manifest["entity_hashes"] = {
            "syscall_specs": {
                item["syscall"]: entity_hash(
                    root / "library" / "specs" / f"{slug(item['syscall'])}.yaml"
                )
                for item in selected
            },
            "rules": {
                rule_id: entity_hash(root / "library" / "rules" / f"{slug(rule_id)}.yaml")
                for rule_id in rule_ids
            },
        }
        recorder.manifest["outputs"] = {
            "raw_candidates": "raw-candidates.yaml",
            "normalized_specs": "normalized-specs.yaml",
            "extract_summary": "extract-summary.yaml",
            "spec_index": "library/specs/index.yaml",
            "rule_index": "library/rules/index.yaml",
        }
        recorder.manifest["counts"] = {
            "selected_syscalls": len(selected),
            "normalized_specs": sum(len(rows) for rows in by_syscall.values()),
            "raw_candidates": len(raw_rows),
            "rules": len(rule_ids),
            "semantic_conflicts": len(recorder.changeset["conflicts"]),
            "unchanged_not_selected": len(candidates) - len(changed),
            "changed_deferred_by_count": max(0, len(changed) - len(selected)),
        }
        recorder.complete()
        return run_id
    except BaseException as exc:
        recorder.fail(exc)
        if isinstance(exc, SyscallGuardError):
            raise
        raise SyscallGuardError(str(exc)) from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Ingest incremental syscall specifications")
    parser.add_argument("--source", required=True, type=Path, help="source descriptor YAML")
    parser.add_argument("--count", required=True, type=int, help="maximum changed syscalls")
    parser.add_argument("--root", type=Path, default=repo_root(), help=argparse.SUPPRESS)
    parser.add_argument("--run-id", help=argparse.SUPPRESS)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    requested_run_id = args.run_id or new_run_id(
        "spec", {"source": str(args.source), "count": args.count}
    )
    try:
        run_id = run_ingest(args.source, args.count, args.root, requested_run_id)
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
    print(f"spec_index: {args.root.resolve() / 'library/specs/index.yaml'}")
    print(f"rule_index: {args.root.resolve() / 'library/rules/index.yaml'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
