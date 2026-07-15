from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from .adapters.ltp import LtpAdapter
from .common import (
    SCHEMA_VERSION,
    SyscallGuardError,
    atomic_write_yaml,
    content_hash,
    load_mapping,
    repo_root,
    utc_now,
)
from .ingest import require_descriptor, resolve_source, resolve_syscalls


AUDIT_ROOT = Path("/tmp/syscallguard-ltp-audit")
AUDIT_STATUSES = {
    "unchanged",
    "added",
    "removed",
    "changed",
    "resolved",
    "regressed",
    "conflict",
}
COMPARISON_FIELDS = (
    "semantic_hash",
    "preconditions",
    "arguments",
    "expected_result",
    "errno",
    "recognizer_id",
    "file",
    "line",
    "case",
)


def _record_from_normalized(row: dict[str, Any]) -> dict[str, Any]:
    semantics = row.get("semantics", {})
    action = semantics.get("action", {}) if isinstance(semantics, dict) else {}
    source = row.get("source", {})
    expansion = row.get("expansion", {})
    category = str(row.get("category", "syscall_behavior"))
    return {
        "syscall": str(row.get("syscall", "")),
        "semantic_hash": content_hash({"category": category, "semantics": semantics}),
        "category": category,
        "semantics": semantics,
        "preconditions": semantics.get("preconditions", [])
        if isinstance(semantics, dict)
        else [],
        "arguments": action.get("arguments", []) if isinstance(action, dict) else [],
        "expected_result": semantics.get("expected_result")
        if isinstance(semantics, dict)
        else None,
        "errno": semantics.get("errno", []) if isinstance(semantics, dict) else [],
        "recognizer_id": row.get("recognizer_id"),
        "file": source.get("file") if isinstance(source, dict) else None,
        "line": source.get("line") if isinstance(source, dict) else None,
        "case": row.get("case"),
        "case_index": expansion.get("case_index")
        if isinstance(expansion, dict)
        else None,
        "change_origin": "struct"
        if isinstance(expansion, dict) and expansion.get("array")
        else "existing_logic",
    }


def _published_records(root: Path, source_id: str) -> dict[str, list[dict[str, Any]]]:
    result: dict[str, list[dict[str, Any]]] = {}
    directory = root / "library" / "rules"
    if not directory.is_dir():
        return result
    for path in sorted(directory.glob("*.yaml")):
        entity = load_mapping(path)
        if entity.get("kind") != "syscallguard_rule":
            continue
        semantics = entity.get("semantics", {})
        action = semantics.get("action", {}) if isinstance(semantics, dict) else {}
        syscall = action.get("syscall") if isinstance(action, dict) else None
        if not isinstance(syscall, str):
            continue
        for source in entity.get("sources", []):
            if (
                not isinstance(source, dict)
                or source.get("source_type") != "ltp"
                or source.get("source_id") != source_id
            ):
                continue
            case = source.get("case")
            case_index: int | None = None
            if isinstance(case, str):
                suffix = case.rsplit("_", 1)[-1]
                if suffix.isdigit():
                    case_index = int(suffix)
            result.setdefault(syscall, []).append(
                {
                    "syscall": syscall,
                    "rule_id": entity.get("rule_id"),
                    "semantic_hash": entity.get("semantic_hash"),
                    "category": entity.get("category"),
                    "semantics": semantics,
                    "preconditions": semantics.get("preconditions", [])
                    if isinstance(semantics, dict)
                    else [],
                    "arguments": action.get("arguments", [])
                    if isinstance(action, dict)
                    else [],
                    "expected_result": semantics.get("expected_result")
                    if isinstance(semantics, dict)
                    else None,
                    "errno": semantics.get("errno", [])
                    if isinstance(semantics, dict)
                    else [],
                    "recognizer_id": source.get("recognizer_id"),
                    "file": source.get("file"),
                    "line": source.get("line"),
                    "case": case,
                    "case_index": case_index,
                    "change_origin": "published",
                    "path": str(path.relative_to(root)),
                }
            )
    return result


def _exact_key(record: dict[str, Any]) -> tuple[Any, ...]:
    return (
        record.get("syscall"),
        record.get("file"),
        record.get("line"),
        record.get("recognizer_id"),
        record.get("case"),
    )


def _relaxed_key(record: dict[str, Any]) -> tuple[Any, ...]:
    return (
        record.get("syscall"),
        record.get("file"),
        record.get("recognizer_id"),
        record.get("case_index"),
    )


def _anchor_key(record: dict[str, Any]) -> tuple[Any, ...]:
    return (
        record.get("syscall"),
        record.get("file"),
        record.get("line"),
        record.get("recognizer_id"),
    )


def _pair_records(
    left: list[dict[str, Any]], right: list[dict[str, Any]]
) -> tuple[
    list[tuple[dict[str, Any], dict[str, Any]]],
    list[dict[str, Any]],
    list[dict[str, Any]],
]:
    pairs: list[tuple[dict[str, Any], dict[str, Any]]] = []
    remaining_left = list(left)
    remaining_right = list(right)
    for key_function in (_exact_key, _relaxed_key, _anchor_key):
        left_groups: dict[tuple[Any, ...], list[dict[str, Any]]] = {}
        right_groups: dict[tuple[Any, ...], list[dict[str, Any]]] = {}
        for row in remaining_left:
            left_groups.setdefault(key_function(row), []).append(row)
        for row in remaining_right:
            right_groups.setdefault(key_function(row), []).append(row)
        matched_left: set[int] = set()
        matched_right: set[int] = set()
        for key in sorted(set(left_groups).intersection(right_groups), key=str):
            left_rows = left_groups[key]
            right_rows = right_groups[key]
            if key_function is not _anchor_key and (
                len(left_rows) != 1 or len(right_rows) != 1
            ):
                continue
            ordered_left = sorted(
                left_rows,
                key=lambda row: (int(row.get("line", 0) or 0), str(row.get("case", ""))),
            )
            ordered_right = sorted(
                right_rows,
                key=lambda row: (int(row.get("line", 0) or 0), str(row.get("case", ""))),
            )
            for left_row, right_row in zip(ordered_left, ordered_right):
                pairs.append((left_row, right_row))
                matched_left.add(id(left_row))
                matched_right.add(id(right_row))
        remaining_left = [row for row in remaining_left if id(row) not in matched_left]
        remaining_right = [row for row in remaining_right if id(row) not in matched_right]
    return pairs, remaining_left, remaining_right


def _changes(left: dict[str, Any], right: dict[str, Any]) -> list[str]:
    return [field for field in COMPARISON_FIELDS if left.get(field) != right.get(field)]


def _anchor_from_raw(row: dict[str, Any]) -> tuple[Any, ...]:
    source = row.get("source", {})
    return (
        row.get("syscall"),
        source.get("file") if isinstance(source, dict) else None,
        source.get("line") if isinstance(source, dict) else None,
        row.get("recognizer_id"),
    )


def _anchor_from_record(row: dict[str, Any]) -> tuple[Any, ...]:
    return (
        row.get("syscall"),
        row.get("file"),
        row.get("line"),
        row.get("recognizer_id"),
    )


def compare_syscall(
    syscall: str,
    baseline: dict[str, Any],
    candidate: dict[str, Any],
    published: list[dict[str, Any]],
) -> dict[str, Any]:
    baseline_rules = [
        _record_from_normalized(row)
        for row in baseline.get("normalized", [])
        if isinstance(row, dict)
    ]
    candidate_rules = [
        _record_from_normalized(row)
        for row in candidate.get("normalized", [])
        if isinstance(row, dict)
    ]
    baseline_unresolved = {
        _anchor_from_raw(row)
        for row in baseline.get("raw", [])
        if isinstance(row, dict)
        and row.get("evidence_hash")
        not in {
            normalized.get("evidence_hash")
            for normalized in baseline.get("normalized", [])
            if isinstance(normalized, dict)
        }
    }
    candidate_unresolved_rows: dict[tuple[Any, ...], list[dict[str, Any]]] = {}
    for row in candidate.get("raw", []):
        if isinstance(row, dict) and row.get("evidence_class") == "unresolved":
            candidate_unresolved_rows.setdefault(_anchor_from_raw(row), []).append(row)
    candidate_unresolved = set(candidate_unresolved_rows)

    pairs, baseline_only, candidate_only = _pair_records(
        baseline_rules, candidate_rules
    )
    comparisons: list[dict[str, Any]] = []
    for old, new in pairs:
        changes = _changes(old, new)
        comparisons.append(
            {
                "status": "changed" if changes else "unchanged",
                "change_origin": new.get("change_origin", "existing_logic"),
                "changes": changes,
                "baseline": old,
                "candidate": new,
            }
        )
    for old in baseline_only:
        status = (
            "regressed"
            if _anchor_from_record(old) in candidate_unresolved
            else "removed"
        )
        comparisons.append(
            {
                "status": status,
                "change_origin": old.get("change_origin", "existing_logic"),
                "changes": [],
                "baseline": old,
                "candidate": None,
            }
        )
    for new in candidate_only:
        status = (
            "resolved"
            if _anchor_from_record(new) in baseline_unresolved
            else "added"
        )
        comparisons.append(
            {
                "status": status,
                "change_origin": new.get("change_origin", "existing_logic"),
                "changes": [],
                "baseline": None,
                "candidate": new,
            }
        )

    candidate_rows = [row["candidate"] for row in comparisons if row.get("candidate")]
    published_pairs, published_only, _candidate_without_published = _pair_records(
        published, candidate_rows
    )
    published_by_candidate = {id(candidate_row): pub for pub, candidate_row in published_pairs}
    for comparison in comparisons:
        candidate_row = comparison.get("candidate")
        if not isinstance(candidate_row, dict):
            continue
        published_row = published_by_candidate.get(id(candidate_row))
        if published_row is None:
            comparison["publication"] = "missing"
            continue
        comparison["published"] = published_row
        publication_changes = _changes(published_row, candidate_row)
        if publication_changes:
            comparison["status"] = "conflict"
            comparison["publication"] = "different"
            comparison["changes"] = sorted(
                set(comparison.get("changes", [])).union(publication_changes)
            )
        else:
            comparison["publication"] = "matching"
    baseline_rows = [
        row["baseline"]
        for row in comparisons
        if isinstance(row.get("baseline"), dict) and not row.get("published")
    ]
    baseline_published_pairs, published_only, _baseline_without_published = _pair_records(
        published_only, baseline_rows
    )
    published_by_baseline = {
        id(baseline_row): published_row
        for published_row, baseline_row in baseline_published_pairs
    }
    for comparison in comparisons:
        baseline_row = comparison.get("baseline")
        if not isinstance(baseline_row, dict) or comparison.get("published"):
            continue
        published_row = published_by_baseline.get(id(baseline_row))
        if published_row is not None:
            comparison["published"] = published_row
            comparison["publication"] = "candidate_missing"
    for row in published_only:
        comparisons.append(
            {
                "status": "removed",
                "change_origin": "existing_logic",
                "changes": [],
                "baseline": None,
                "candidate": None,
                "published": row,
                "publication": "orphaned",
            }
        )

    # A candidate may intentionally reject a baseline-only rule because the
    # new parser found runtime mutation or ambiguous data flow. That is an
    # explicit conflict for review, not a regression of published behavior.
    for comparison in comparisons:
        if comparison.get("status") != "regressed" or comparison.get("published"):
            continue
        baseline_row = comparison.get("baseline")
        if not isinstance(baseline_row, dict):
            continue
        unresolved_rows = candidate_unresolved_rows.get(
            _anchor_from_record(baseline_row), []
        )
        reasons = sorted(
            {
                str(row.get("resolution_reason", "unresolved"))
                for row in unresolved_rows
            }
        )
        comparison["status"] = "conflict"
        comparison["changes"] = ["candidate_unresolved"]
        comparison["diagnostic"] = {
            "severity": "conflict",
            "kind": "candidate_conservative_rejection",
            "reasons": reasons,
            "resolution": "manual_review_required",
        }

    for diagnostic in candidate.get("diagnostics", []):
        if not isinstance(diagnostic, dict) or diagnostic.get("severity") != "conflict":
            continue
        comparisons.append(
            {
                "status": "conflict",
                "change_origin": "comment",
                "changes": [str(diagnostic.get("kind", "document"))],
                "baseline": None,
                "candidate": None,
                "published": None,
                "diagnostic": diagnostic,
            }
        )
    comparisons.sort(
        key=lambda row: (
            str(row.get("status")),
            str((row.get("candidate") or row.get("baseline") or row.get("published") or {}).get("file", "")),
            int((row.get("candidate") or row.get("baseline") or row.get("published") or {}).get("line", 0) or 0),
            str((row.get("candidate") or row.get("baseline") or row.get("published") or {}).get("case", "")),
        )
    )
    counts = Counter(row["status"] for row in comparisons)
    return {
        "syscall": syscall,
        "counts": {status: counts.get(status, 0) for status in sorted(AUDIT_STATUSES)},
        "evidence": {
            "baseline": {
                "raw": len(baseline.get("raw", [])),
                "rules": len(baseline_rules),
                "unresolved": len(baseline_unresolved),
            },
            "candidate": {
                "raw": len(candidate.get("raw", [])),
                "rules": len(candidate_rules),
                "authoritative": sum(
                    row.get("evidence_class") == "authoritative"
                    for row in candidate.get("raw", [])
                    if isinstance(row, dict)
                ),
                "context": sum(
                    row.get("evidence_class") == "context"
                    for row in candidate.get("raw", [])
                    if isinstance(row, dict)
                ),
                "unresolved": len(candidate_unresolved),
            },
            "published_rules": len(published),
        },
        "rules": comparisons,
    }


def _audit_id() -> str:
    stamp = re.sub(r"[-:.]", "", utc_now()).lower().replace("+", "")
    return f"audit-{stamp}-{content_hash({'at': stamp})[-8:]}"


def run_audit(
    source: str | Path | None = None,
    root: Path | None = None,
    syscalls: str | None = None,
    audit_id: str | None = None,
    output_root: Path = AUDIT_ROOT,
) -> tuple[str, Path, dict[str, Any]]:
    root = (root or repo_root()).resolve()
    requested = resolve_syscalls(syscalls)
    descriptor_path, source_resolution = resolve_source(source, root)
    descriptor, location, snapshot_hash, candidate_adapter = require_descriptor(
        descriptor_path, root
    )
    baseline_adapter = LtpAdapter(
        location, candidate_adapter.rules_path, extractor_profile="baseline"
    )
    discovered = candidate_adapter.discover()
    available = {str(item["syscall"]) for item in discovered}
    if requested is not None:
        unknown = sorted(set(requested) - available)
        if unknown:
            raise SyscallGuardError(
                "requested syscalls do not exist in source: " + ", ".join(unknown)
            )
    published = _published_records(root, str(descriptor["source_id"]))
    details: list[dict[str, Any]] = []
    for item in discovered:
        baseline_item = baseline_adapter.prescan(item)
        candidate_item = candidate_adapter.prescan(item)
        baseline = baseline_adapter.extract(baseline_item)
        candidate = candidate_adapter.extract(candidate_item)
        details.append(
            compare_syscall(
                str(item["syscall"]),
                baseline,
                candidate,
                published.get(str(item["syscall"]), []),
            )
        )
    full_counts: Counter[str] = Counter()
    for detail in details:
        full_counts.update(detail["counts"])
    selected_details = (
        details
        if requested is None
        else [detail for detail in details if detail["syscall"] in set(requested)]
    )
    selected_counts: Counter[str] = Counter()
    for detail in selected_details:
        selected_counts.update(detail["counts"])
    full_published_counts = Counter(
        row["status"]
        for detail in details
        for row in detail["rules"]
        if row.get("published")
    )
    selected_published_counts = Counter(
        row["status"]
        for detail in selected_details
        for row in detail["rules"]
        if row.get("published")
    )
    generated_at = utc_now()
    resolved_id = audit_id or _audit_id()
    if not re.fullmatch(r"audit-[a-z0-9][a-z0-9._-]*", resolved_id):
        raise SyscallGuardError(f"invalid audit id: {resolved_id}")
    resolved_output_root = output_root.expanduser().resolve()
    if not resolved_output_root.is_relative_to(Path("/tmp")):
        raise SyscallGuardError("LTP audit output root must be under /tmp")
    if resolved_output_root.is_relative_to(root) or resolved_output_root.is_relative_to(
        location
    ):
        raise SyscallGuardError("LTP audit output must not be inside a managed repository")
    output = resolved_output_root / resolved_id / "report.yaml"
    if output.parent.exists():
        raise SyscallGuardError(f"audit output already exists: {output.parent}")
    report = {
        "schema_version": SCHEMA_VERSION,
        "kind": "syscallguard_ltp_audit_report",
        "audit_id": resolved_id,
        "generated_at_utc": generated_at,
        "read_only": True,
        "status_definitions": {
            "unchanged": "baseline and candidate rule fields match",
            "added": "candidate rule has no baseline counterpart",
            "removed": "baseline rule has no candidate evidence counterpart",
            "changed": "paired baseline and candidate rule fields differ",
            "resolved": "candidate formed a rule from baseline-unresolved evidence",
            "regressed": "a published rule became unresolved in the candidate",
            "conflict": "code, comment, publication, or conservative resolution disagrees",
        },
        "source": {
            "id": descriptor["source_id"],
            "descriptor": str(descriptor_path),
            "location": str(location),
            "snapshot_hash": snapshot_hash,
            "recognition_rules_hash": candidate_adapter.rules_hash,
            "resolution": source_resolution,
        },
        "scope": {
            "discovered_syscall_count": len(discovered),
            "selected_syscalls": requested or [detail["syscall"] for detail in details],
            "filter": requested,
        },
        "full_counts": {
            status: full_counts.get(status, 0) for status in sorted(AUDIT_STATUSES)
        },
        "selected_counts": {
            status: selected_counts.get(status, 0)
            for status in sorted(AUDIT_STATUSES)
        },
        "full_published_counts": {
            status: full_published_counts.get(status, 0)
            for status in sorted(AUDIT_STATUSES)
        },
        "selected_published_counts": {
            status: selected_published_counts.get(status, 0)
            for status in sorted(AUDIT_STATUSES)
        },
        "syscalls": selected_details,
    }
    atomic_write_yaml(output, report)
    return resolved_id, output, report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Read-only three-way audit of all LTP extraction rules"
    )
    parser.add_argument("--source", help="source alias or descriptor YAML")
    parser.add_argument("--syscalls", help="comma-separated syscall names")
    parser.add_argument("--root", type=Path, default=repo_root(), help=argparse.SUPPRESS)
    parser.add_argument("--audit-id", help=argparse.SUPPRESS)
    parser.add_argument("--output-root", type=Path, default=AUDIT_ROOT, help=argparse.SUPPRESS)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        audit_id, output, report = run_audit(
            args.source,
            args.root,
            args.syscalls,
            args.audit_id,
            args.output_root,
        )
    except SyscallGuardError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(f"source: {report['source']['id']} ({report['source']['snapshot_hash']})")
    print(f"audited_syscalls: {report['scope']['discovered_syscall_count']}")
    if report["scope"]["filter"]:
        print("filter: " + ", ".join(report["scope"]["filter"]))
    print(
        "full: "
        + " ".join(
            f"{status}={report['full_counts'][status]}"
            for status in sorted(AUDIT_STATUSES)
        )
    )
    print(
        "published: "
        + " ".join(
            f"{status}={report['full_published_counts'][status]}"
            for status in sorted(AUDIT_STATUSES)
        )
    )
    if report["scope"]["filter"]:
        print(
            "selected: "
            + " ".join(
                f"{status}={report['selected_counts'][status]}"
                for status in sorted(AUDIT_STATUSES)
            )
        )
    print(f"audit_id: {audit_id}")
    print(f"report: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
