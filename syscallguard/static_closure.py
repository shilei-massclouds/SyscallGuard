from __future__ import annotations

from pathlib import Path
from typing import Any, Iterable

from .common import (
    SCHEMA_VERSION,
    SyscallGuardError,
    atomic_write_text,
    load_mapping,
    normalize_run_id,
    repo_root,
    utc_now,
    yaml_text,
)
from .mapping import load_mapping_report


REPORT_KIND = "syscallguard_static_closure_report"


def _static_manual_rules(
    report: dict[str, Any], active_rule_ids: set[str]
) -> set[str]:
    rows = report.get("rules", {})
    if not isinstance(rows, dict):
        raise SyscallGuardError("mapping report rules must be a mapping")
    return {
        rule_id
        for rule_id in active_rule_ids
        if rule_id.startswith("MAN_")
        and isinstance(rows.get(rule_id), dict)
        and rows[rule_id].get("status") == "covered"
        and bool(rows[rule_id].get("static_check_refs"))
        and not rows[rule_id].get("dynamic_test_refs")
    }


def _manual_edges(
    report: dict[str, Any], active_rule_ids: set[str]
) -> set[tuple[str, str]]:
    rows = report.get("rules", {})
    if not isinstance(rows, dict):
        raise SyscallGuardError("mapping report rules must be a mapping")
    return {
        (rule_id, check_id)
        for rule_id in active_rule_ids
        if rule_id.startswith("MAN_") and isinstance(rows.get(rule_id), dict)
        for check_id in rows[rule_id].get("static_check_refs", [])
        if isinstance(check_id, str)
    }


def _check_versions(
    report: dict[str, Any], active_rule_ids: set[str] | None = None
) -> dict[str, str]:
    rows = report.get("rules", {})
    if not isinstance(rows, dict):
        raise SyscallGuardError("mapping report rules must be a mapping")
    versions: dict[str, str] = {}
    for rule_id, row in rows.items():
        if active_rule_ids is not None and rule_id not in active_rule_ids:
            continue
        if not isinstance(row, dict):
            continue
        entities = row.get("entity_versions", {})
        static = entities.get("static_checks", {}) if isinstance(entities, dict) else {}
        if not isinstance(static, dict):
            continue
        for check_id, version in static.items():
            if not isinstance(check_id, str) or not isinstance(version, dict):
                continue
            content_hash = version.get("content_hash")
            if not isinstance(content_hash, str):
                continue
            previous = versions.setdefault(check_id, content_hash)
            if previous != content_hash:
                raise SyscallGuardError(
                    f"mapping report contains conflicting versions for {check_id}"
                )
    return versions


def _syscalls(report: dict[str, Any], rule_ids: Iterable[str]) -> list[str]:
    owners = report.get("rule_syscalls", {})
    if not isinstance(owners, dict):
        raise SyscallGuardError("mapping report rule_syscalls must be a mapping")
    return sorted(
        {
            syscall
            for rule_id in rule_ids
            for syscall in owners.get(rule_id, [])
            if isinstance(syscall, str)
        }
    )


def compute_mapping_delta(
    baseline: dict[str, Any],
    final: dict[str, Any],
    *,
    active_rule_ids: set[str],
    candidate_rule_ids: set[str],
    final_check_ids: set[str],
    baseline_check_ids: set[str] | None = None,
) -> dict[str, Any]:
    """Compute static-only increments using active rules and the active check index."""

    active_candidates = {
        rule_id
        for rule_id in candidate_rule_ids.intersection(active_rule_ids)
        if rule_id.startswith("MAN_")
    }
    baseline_static = _static_manual_rules(baseline, active_rule_ids)
    final_static = _static_manual_rules(final, active_rule_ids)
    unmapped_candidates = sorted(active_candidates - final_static)
    if unmapped_candidates:
        raise SyscallGuardError(
            "final mapping does not cover every active Manual static candidate: "
            + ", ".join(unmapped_candidates)
        )
    new_candidates = sorted(active_candidates - baseline_static)
    newly_mapped = sorted(
        rule_id
        for rule_id in final_static
        if rule_id not in baseline_static
        and isinstance(baseline.get("rules", {}).get(rule_id), dict)
    )

    baseline_edges = _manual_edges(baseline, active_rule_ids)
    final_edges = _manual_edges(final, active_rule_ids)
    new_edges = sorted(final_edges - baseline_edges)
    affected_checks = {check_id for _rule_id, check_id in new_edges}

    baseline_versions = _check_versions(baseline, active_rule_ids)
    final_versions = _check_versions(final, active_rule_ids)
    baseline_check_ids = set(baseline_check_ids or baseline_versions)
    # Only entities attributable to the incremental Manual edges belong in
    # this closure.  The final primary index can contain older checks that
    # were never part of the baseline mapping execution scope; those are not
    # newly created by this batch.
    new_entities = sorted(
        affected_checks.intersection(final_check_ids) - baseline_check_ids
    )
    reused_entities = sorted(
        check_id
        for check_id in affected_checks.intersection(baseline_check_ids)
        if check_id in baseline_versions
        and baseline_versions[check_id] == final_versions.get(check_id)
    )
    updated_entities = sorted(
        check_id
        for check_id in affected_checks.intersection(baseline_check_ids)
        if check_id not in baseline_versions
        or baseline_versions[check_id] != final_versions.get(check_id)
    )

    return {
        "new_static_candidate_rules": {
            "count": len(new_candidates),
            "syscall_count": len(_syscalls(final, new_candidates)),
            "rule_ids": new_candidates,
            "syscalls": _syscalls(final, new_candidates),
        },
        "newly_mapped_manual_rules": {
            "count": len(newly_mapped),
            "syscall_count": len(_syscalls(final, newly_mapped)),
            "rule_ids": newly_mapped,
            "syscalls": _syscalls(final, newly_mapped),
        },
        "new_rule_check_edges": {
            "count": len(new_edges),
            "edges": [
                {"rule_id": rule_id, "check_id": check_id}
                for rule_id, check_id in new_edges
            ],
        },
        "new_static_check_entities": {
            "count": len(new_entities),
            "check_ids": new_entities,
            "reused_count": len(reused_entities),
            "reused_check_ids": reused_entities,
            "updated_count": len(updated_entities),
            "updated_check_ids": updated_entities,
        },
    }


def _active_rule_ids(root: Path) -> set[str]:
    index = load_mapping(root / "library/syscalls.yaml")
    syscalls = index.get("syscalls", {})
    if not isinstance(syscalls, dict):
        raise SyscallGuardError("active syscall index has no syscalls mapping")
    return {
        str(ref["rule_id"])
        for refs in syscalls.values()
        if isinstance(refs, list)
        for ref in refs
        if isinstance(ref, dict) and isinstance(ref.get("rule_id"), str)
    }


def _active_check_ids(root: Path) -> set[str]:
    index = load_mapping(root / "targets/starry/static-checks.yaml")
    syscalls = index.get("syscalls", {})
    if not isinstance(syscalls, dict):
        raise SyscallGuardError("active static check index has no syscalls mapping")
    return {
        str(ref["check_id"])
        for refs in syscalls.values()
        if isinstance(refs, list)
        for ref in refs
        if isinstance(ref, dict) and isinstance(ref.get("check_id"), str)
    }


def _baseline_check_ids(
    root: Path, report_id: str, baseline: dict[str, Any]
) -> set[str]:
    path = root / "runs" / report_id / "static-closure-baseline.yaml"
    if not path.is_file():
        return set(_check_versions(baseline))
    snapshot = load_mapping(path)
    if (
        snapshot.get("kind") != "syscallguard_static_closure_baseline"
        or snapshot.get("report_id") != report_id
    ):
        raise SyscallGuardError(f"invalid static closure baseline: {path}")
    values = snapshot.get("active_static_check_ids")
    if not isinstance(values, list) or any(not isinstance(item, str) for item in values):
        raise SyscallGuardError(f"invalid active_static_check_ids in {path}")
    if len(values) != len(set(values)):
        raise SyscallGuardError(f"duplicate active static check IDs in {path}")
    return set(values)


def _fixed_before(root: Path, generated_at_utc: str) -> set[str]:
    index = load_mapping(root / "targets/starry/fixes/index.yaml")
    rows = index.get("entities", [])
    if not isinstance(rows, list):
        raise SyscallGuardError("fix index entities must be a list")
    return {
        finding_id
        for row in rows
        if isinstance(row, dict)
        and isinstance(row.get("generated_at_utc"), str)
        and row["generated_at_utc"] <= generated_at_utc
        for finding_id in row.get("finding_refs", [])
        if isinstance(finding_id, str)
    }


def collect_fixed_findings(
    root: Path,
    fix_run_ids: Iterable[str],
    *,
    active_rule_ids: set[str],
    baseline_fixed_finding_ids: set[str],
) -> dict[str, Any]:
    finding_ids: set[str] = set()
    run_ids: list[str] = []
    for raw_run_id in fix_run_ids:
        run_id = normalize_run_id(raw_run_id)
        manifest = load_mapping(root / "runs" / run_id / "manifest.yaml")
        if (
            manifest.get("kind") != "syscallguard_run"
            or manifest.get("stage") != "fix"
            or manifest.get("status") != "completed"
        ):
            continue
        regression = load_mapping(root / "runs" / run_id / "regression-results.yaml")
        static = regression.get("static", [])
        dynamic = regression.get("dynamic", [])
        if (
            regression.get("blockers")
            or not isinstance(static, list)
            or not isinstance(dynamic, list)
            or any(row.get("result") != "pass" for row in static if isinstance(row, dict))
            or any(
                row.get("result") not in {"pass", "skipped"}
                for row in dynamic
                if isinstance(row, dict)
            )
        ):
            continue
        selected = manifest.get("entities", {}).get("findings", [])
        if not isinstance(selected, list):
            continue
        accepted = False
        for finding_id in selected:
            if (
                not isinstance(finding_id, str)
                or finding_id in baseline_fixed_finding_ids
            ):
                continue
            path = root / "targets/starry/findings" / f"{finding_id}.yaml"
            finding = load_mapping(path)
            if (
                finding.get("status") != "confirmed"
                or finding.get("resolution") != "fixed"
                or finding.get("fixed_by_run") != run_id
                or finding.get("rule_id") not in active_rule_ids
            ):
                continue
            finding_ids.add(finding_id)
            accepted = True
        if accepted:
            run_ids.append(run_id)

    findings = [
        load_mapping(root / "targets/starry/findings" / f"{finding_id}.yaml")
        for finding_id in sorted(finding_ids)
    ]
    rule_ids = sorted({str(finding["rule_id"]) for finding in findings})
    syscalls = sorted({str(finding["syscall"]) for finding in findings})
    manual = sorted(
        str(finding["finding_id"])
        for finding in findings
        if str(finding["rule_id"]).startswith("MAN_")
    )
    ltp = sorted(
        str(finding["finding_id"])
        for finding in findings
        if str(finding["rule_id"]).startswith("LTP_")
    )
    return {
        "count": len(findings),
        "finding_ids": sorted(finding_ids),
        "rule_count": len(rule_ids),
        "rule_ids": rule_ids,
        "syscall_count": len(syscalls),
        "syscalls": syscalls,
        "fix_run_count": len(set(run_ids)),
        "fix_run_ids": sorted(set(run_ids)),
        "source_split": {
            "manual": len(manual),
            "manual_finding_ids": manual,
            "ltp": len(ltp),
            "ltp_finding_ids": ltp,
        },
    }


def _report_text(metadata: dict[str, Any]) -> str:
    fence = chr(96) * 3
    metrics = metadata["metrics"]
    candidate = metrics["new_static_candidate_rules"]
    mapped = metrics["newly_mapped_manual_rules"]
    edges = metrics["new_rule_check_edges"]
    checks = metrics["new_static_check_entities"]
    findings = metrics["fixed_starry_findings"]
    lines = [
        "# Manual 静态收口报告",
        "",
        "## 增量结论",
        "",
        f"- 新静态候选：{candidate['count']} 条、{candidate['syscall_count']} 个 syscall",
        f"- 新映射 Manual 规则：{mapped['count']} 条、{mapped['syscall_count']} 个 syscall",
        f"- 新 rule→check 关系：{edges['count']} 条",
        f"- 新静态检查实体：{checks['count']} 个；复用 {checks['reused_count']} 个，更新 {checks['updated_count']} 个",
        f"- 修复 Starry confirmed finding：{findings['count']} 个，涉及 {findings['rule_count']} 条规则、{findings['syscall_count']} 个 syscall",
        f"- 最终 dynamic execution scope：{metadata['final_dynamic_execution_scope_count']}",
        "",
        "## 完整 ID 清单",
        "",
        f"- 新候选规则：{'、'.join(candidate['rule_ids']) or '—'}",
        f"- 新映射规则：{'、'.join(mapped['rule_ids']) or '—'}",
        f"- 新检查实体：{'、'.join(checks['check_ids']) or '—'}",
        f"- fixed finding：{'、'.join(findings['finding_ids']) or '—'}",
        "",
        "<details>",
        "<summary>机器可读元数据</summary>",
        "",
        "<!-- syscallguard-metadata -->",
        fence + "yaml",
        yaml_text(metadata).rstrip(),
        fence,
        "</details>",
        "",
    ]
    return "\n".join(lines)


def publish_static_closure(
    baseline_report_id: str,
    final_report_id: str,
    candidate_rule_ids: set[str],
    fix_run_ids: Iterable[str],
    *,
    root: Path | None = None,
    requested_run_id: str,
) -> str:
    root = (root or repo_root()).resolve()
    baseline = load_mapping_report(root, normalize_run_id(baseline_report_id))
    final = load_mapping_report(root, normalize_run_id(final_report_id))
    baseline_id = str(baseline["report_id"])
    baseline_checks = _baseline_check_ids(root, baseline_id, baseline)
    active_rules = _active_rule_ids(root)
    delta = compute_mapping_delta(
        baseline,
        final,
        active_rule_ids=active_rules,
        candidate_rule_ids=candidate_rule_ids,
        final_check_ids=_active_check_ids(root),
        baseline_check_ids=baseline_checks,
    )
    baseline_time = str(baseline.get("generated_at_utc", ""))
    fixed = collect_fixed_findings(
        root,
        fix_run_ids,
        active_rule_ids=active_rules,
        baseline_fixed_finding_ids=_fixed_before(root, baseline_time),
    )
    run_id = normalize_run_id(requested_run_id)
    destination = root / "runs" / run_id / "report.md"
    if destination.exists():
        raise SyscallGuardError(f"static closure report already exists: {destination}")
    dynamic_scope = final.get("execution_scope", {}).get("dynamic_tests", [])
    if not isinstance(dynamic_scope, list):
        raise SyscallGuardError("final mapping dynamic execution scope must be a list")
    metadata = {
        "schema_version": SCHEMA_VERSION,
        "kind": REPORT_KIND,
        "report_id": run_id,
        "status": "completed",
        "generated_at_utc": utc_now(),
        "baseline": {
            "report_id": baseline["report_id"],
            "generated_at_utc": baseline.get("generated_at_utc"),
            "target_snapshot_hash": baseline.get("target", {}).get("snapshot_hash"),
            "manual_static_rule_ids": sorted(_static_manual_rules(baseline, active_rules)),
            "static_check_versions": _check_versions(baseline, active_rules),
            "active_static_check_ids": sorted(baseline_checks),
            "fixed_finding_ids": sorted(_fixed_before(root, baseline_time)),
        },
        "final": {
            "report_id": final["report_id"],
            "generated_at_utc": final.get("generated_at_utc"),
            "target_snapshot_hash": final.get("target", {}).get("snapshot_hash"),
            "manual_static_rule_ids": sorted(_static_manual_rules(final, active_rules)),
            "active_rule_count": len(active_rules),
        },
        "metrics": {**delta, "fixed_starry_findings": fixed},
        "final_dynamic_execution_scope_count": len(dynamic_scope),
    }
    atomic_write_text(destination, _report_text(metadata))
    return run_id
