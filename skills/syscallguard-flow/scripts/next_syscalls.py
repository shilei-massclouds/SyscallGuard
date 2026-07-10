#!/usr/bin/env python3
"""List or record checked Starry syscalls for SyscallGuard batches."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - environment failure path
    yaml = None


DEFAULT_SOURCE = Path("snapshots/ltp/starry-sources/syscall/mod.rs")
DEFAULT_HISTORY = Path("batches/syscall-check-history.yaml")
DEFAULT_LIMIT = 20
REVIEWED_HISTORY_STATUSES = {"covered", "gap", "risk", "unsupported", "needs_review"}
RESOLVED_REVIEW_STATUSES = {"confirmed", "not_applicable"}


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise SystemExit(f"ERROR: cannot read {path}: {exc}") from exc


def extract_dispatch_body(source: str) -> str:
    marker = "let result = match sysno {"
    start = source.find(marker)
    if start < 0:
        return source
    body = source[start + len(marker) :]
    end = body.find("_ =>")
    return body if end < 0 else body[:end]


def extract_syscalls(source_path: Path) -> list[str]:
    body = extract_dispatch_body(read_text(source_path))
    seen: set[str] = set()
    syscalls: list[str] = []
    for raw_name in re.findall(r"\bSysno::([A-Za-z_][A-Za-z0-9_]*)\b", body):
        name = raw_name.lower()
        if name in seen:
            continue
        seen.add(name)
        syscalls.append(name)
    return syscalls


def load_yaml(path: Path) -> Any:
    if yaml is None:
        raise SystemExit("ERROR: PyYAML is required: python3 -m pip install PyYAML")
    if not path.exists():
        return None
    try:
        with path.open("r", encoding="utf-8") as handle:
            return yaml.safe_load(handle)
    except yaml.YAMLError as exc:
        raise SystemExit(f"ERROR: malformed YAML in {path}: {exc}") from exc
    except OSError as exc:
        raise SystemExit(f"ERROR: cannot read {path}: {exc}") from exc


def write_yaml(path: Path, data: dict[str, Any]) -> None:
    if yaml is None:
        raise SystemExit("ERROR: PyYAML is required: python3 -m pip install PyYAML")
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("w", encoding="utf-8") as handle:
            yaml.safe_dump(data, handle, allow_unicode=True, sort_keys=False)
    except OSError as exc:
        raise SystemExit(f"ERROR: cannot write {path}: {exc}") from exc


def checked_syscalls(history_path: Path) -> set[str]:
    data = load_yaml(history_path)
    if data is None:
        return set()
    if not isinstance(data, dict):
        raise SystemExit(f"ERROR: {history_path} must contain a YAML mapping")

    checked: set[str] = set()
    rows = data.get("checked_syscalls", [])
    if rows is None:
        return checked
    if not isinstance(rows, list):
        raise SystemExit(f"ERROR: {history_path} checked_syscalls must be a list")

    for row in rows:
        if not isinstance(row, dict):
            continue
        syscall = row.get("syscall")
        status = row.get("status")
        if isinstance(syscall, str) and status in REVIEWED_HISTORY_STATUSES:
            checked.add(syscall.lower())
    return checked


def emit_yaml(payload: dict[str, Any]) -> None:
    if yaml is None:
        raise SystemExit("ERROR: PyYAML is required: python3 -m pip install PyYAML")
    print(yaml.safe_dump(payload, allow_unicode=True, sort_keys=False).rstrip())


def emit_text(payload: dict[str, Any]) -> None:
    print(f"source: {payload['source']}")
    print(f"history: {payload['history']}")
    print(f"history_found: {str(payload['history_found']).lower()}")
    print(f"limit: {payload['limit']}")
    print(f"total_candidates: {payload['total_candidates']}")
    print(f"already_checked: {payload['already_checked']}")
    print("selected:")
    for index, syscall in enumerate(payload["selected"], start=1):
        print(f"{index:02d}. {syscall}")


def load_mapping(path: Path) -> dict[str, Any]:
    data = load_yaml(path)
    if not isinstance(data, dict):
        raise SystemExit(f"ERROR: {path} must contain a YAML mapping")
    return data


def list_next(args: argparse.Namespace) -> int:
    source_path = args.source
    history_path = args.history
    candidates = extract_syscalls(source_path)
    checked = checked_syscalls(history_path)
    selected = [name for name in candidates if name not in checked][: args.limit]

    payload: dict[str, Any] = {
        "source": str(source_path),
        "history": str(history_path),
        "history_found": history_path.exists(),
        "limit": args.limit,
        "total_candidates": len(candidates),
        "already_checked": len(checked),
        "selected": selected,
    }
    if args.format == "text":
        emit_text(payload)
    else:
        emit_yaml(payload)
    return 0


def signoff_resolved(batch_dir: Path) -> bool:
    signoff_path = batch_dir / "reviews" / "10-batch-closeout-signoff.yaml"
    if not signoff_path.exists():
        return False
    data = load_yaml(signoff_path)
    return isinstance(data, dict) and data.get("status") in RESOLVED_REVIEW_STATUSES


def coverage_syscalls(item: dict[str, Any]) -> list[str]:
    result: list[str] = []
    syscall = item.get("syscall")
    if isinstance(syscall, str):
        result.append(syscall.lower())
    syscalls = item.get("syscalls")
    if isinstance(syscalls, list):
        result.extend(value.lower() for value in syscalls if isinstance(value, str))
    return result


def history_index(history: dict[str, Any], key: str, field: str) -> dict[str, dict[str, Any]]:
    rows = history.setdefault(key, [])
    if not isinstance(rows, list):
        raise SystemExit(f"ERROR: history field {key} must be a list")
    indexed: dict[str, dict[str, Any]] = {}
    for row in rows:
        if isinstance(row, dict) and isinstance(row.get(field), str):
            indexed[row[field].lower()] = row
    return indexed


def record_checked(args: argparse.Namespace) -> int:
    batch_dir = args.batch
    if not batch_dir.is_dir():
        raise SystemExit(f"ERROR: batch directory not found: {batch_dir}")
    if not args.allow_unresolved and not signoff_resolved(batch_dir):
        raise SystemExit(
            "ERROR: closeout sign-off is not confirmed; use --allow-unresolved only for dry review work"
        )

    manifest = load_mapping(batch_dir / "manifest.yaml")
    batch_id = manifest.get("batch_id")
    if not isinstance(batch_id, str) or not batch_id:
        raise SystemExit("ERROR: manifest batch_id must be a non-empty string")

    matrix = load_mapping(batch_dir / "outputs" / "coverage-matrix.yaml")
    coverage = matrix.get("coverage")
    if not isinstance(coverage, list):
        raise SystemExit("ERROR: coverage matrix coverage must be a list")

    history_data = load_yaml(args.history)
    if history_data is None:
        history: dict[str, Any] = {
            "schema_version": 1,
            "updated_at_utc": "",
            "checked_syscalls": [],
            "checked_behaviors": [],
        }
    elif isinstance(history_data, dict):
        history = history_data
        history.setdefault("schema_version", 1)
        history.setdefault("checked_syscalls", [])
        history.setdefault("checked_behaviors", [])
    else:
        raise SystemExit(f"ERROR: {args.history} must contain a YAML mapping")

    reviewed_at = args.reviewed_at or datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    history["updated_at_utc"] = reviewed_at

    syscall_rows = history_index(history, "checked_syscalls", "syscall")
    behavior_rows = history_index(history, "checked_behaviors", "behavior_id")
    recorded_syscalls = 0
    recorded_behaviors = 0

    for item in coverage:
        if not isinstance(item, dict):
            continue
        triage = item.get("triage")
        if triage not in REVIEWED_HISTORY_STATUSES:
            continue
        behavior_id = item.get("behavior_id")
        result_ref = f"{batch_dir}/outputs/coverage-matrix.yaml#{behavior_id or 'coverage'}"
        names = coverage_syscalls(item)
        if names:
            for syscall in names:
                row = {
                    "syscall": syscall,
                    "status": triage,
                    "batch_id": batch_id,
                    "result_ref": result_ref,
                    "reviewed_at_utc": reviewed_at,
                }
                if syscall in syscall_rows:
                    syscall_rows[syscall].update(row)
                else:
                    history["checked_syscalls"].append(row)
                    syscall_rows[syscall] = row
                recorded_syscalls += 1
        elif isinstance(behavior_id, str):
            row = {
                "behavior_id": behavior_id,
                "status": triage,
                "batch_id": batch_id,
                "result_ref": result_ref,
                "reviewed_at_utc": reviewed_at,
            }
            key = behavior_id.lower()
            if key in behavior_rows:
                behavior_rows[key].update(row)
            else:
                history["checked_behaviors"].append(row)
                behavior_rows[key] = row
            recorded_behaviors += 1

    write_yaml(args.history, history)
    print(f"history: {args.history}")
    print(f"recorded_syscalls: {recorded_syscalls}")
    print(f"recorded_behaviors: {recorded_behaviors}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Select the next unchecked Starry syscalls for a SyscallGuard batch."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="List the next unchecked syscalls")
    list_parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    list_parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    list_parser.add_argument("--history", type=Path, default=DEFAULT_HISTORY)
    list_parser.add_argument("--format", choices=("yaml", "text"), default="yaml")
    list_parser.set_defaults(func=list_next)

    record_parser = subparsers.add_parser(
        "record", help="Record reviewed syscall results from a batch coverage matrix"
    )
    record_parser.add_argument("--batch", type=Path, required=True)
    record_parser.add_argument("--history", type=Path, default=DEFAULT_HISTORY)
    record_parser.add_argument("--reviewed-at", default="")
    record_parser.add_argument(
        "--allow-unresolved",
        action="store_true",
        help="Allow recording before closeout sign-off is confirmed",
    )
    record_parser.set_defaults(func=record_checked)
    return parser


def main(argv: list[str]) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if hasattr(args, "limit") and args.limit <= 0:
        parser.error("--limit must be positive")
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
