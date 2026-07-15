#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "ingest-syscall-specs",
    "map-starry-checks",
    "check-starry-compliance",
    "fix-starry-compliance",
    "reset-syscallguard",
}
RUN_STATUSES = {"running", "completed", "completed_with_blockers", "failed", "superseded"}
TARGET_INDEXES = {
    "targets/starry/findings/index.yaml": (
        "syscallguard_starry_finding_index",
        "syscallguard_starry_finding",
    ),
    "targets/starry/fixes/index.yaml": (
        "syscallguard_starry_fix_index",
        "syscallguard_starry_fix",
    ),
}
EXECUTABLE_INDEXES = {
    "targets/starry/static-checks.yaml": (
        "syscallguard_starry_static_check_index",
        "syscallguard_starry_static_check",
        "check_id",
        "targets/starry/static-checks",
    ),
    "targets/starry/dynamic-tests.yaml": (
        "syscallguard_starry_dynamic_test_index",
        "syscallguard_starry_dynamic_test",
        "test_id",
        "targets/starry/dynamic-tests",
    ),
}


def content_hash(value: Any) -> str:
    data = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(data).hexdigest()


def version_hash(entity: dict[str, Any]) -> str:
    if entity.get("kind") == "syscallguard_rule":
        return content_hash(
            {"category": entity.get("category"), "semantics": entity.get("semantics")}
        )
    payload = dict(entity)
    payload.pop("generated_at_utc", None)
    payload.pop("content_hash", None)
    return content_hash(payload)


def valid_version(row: Any) -> bool:
    return (
        isinstance(row, dict)
        and isinstance(row.get("id"), str)
        and isinstance(row.get("generated_at_utc"), str)
        and isinstance(row.get("content_hash"), str)
    )


def load(path: Path, errors: list[str]) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing: {path.relative_to(ROOT)}")
    except (OSError, yaml.YAMLError) as exc:
        errors.append(f"cannot read {path.relative_to(ROOT)}: {exc}")
    return None


def frontmatter(path: Path, errors: list[str]) -> dict[str, Any] | None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"cannot read {path.relative_to(ROOT)}: {exc}")
        return None
    marker = "<!-- syscallguard-metadata -->\n```yaml\n"
    if not text.startswith("---") and marker in text:
        encoded = text.split(marker, 1)[1]
        payload, separator, _tail = encoded.partition("\n```\n")
        if not separator:
            errors.append(f"unclosed Markdown metadata: {path.relative_to(ROOT)}")
            return None
        try:
            value = yaml.safe_load(payload)
        except yaml.YAMLError as exc:
            errors.append(f"invalid Markdown metadata in {path.relative_to(ROOT)}: {exc}")
            return None
        return value if isinstance(value, dict) else None
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        errors.append(f"missing Markdown metadata: {path.relative_to(ROOT)}")
        return None
    try:
        closing = lines[1:].index("---") + 1
    except ValueError:
        errors.append(f"unclosed Markdown frontmatter: {path.relative_to(ROOT)}")
        return None
    try:
        value = yaml.safe_load("\n".join(lines[1:closing]))
    except yaml.YAMLError as exc:
        errors.append(f"invalid Markdown frontmatter in {path.relative_to(ROOT)}: {exc}")
        return None
    if not isinstance(value, dict):
        errors.append(f"frontmatter is not a mapping: {path.relative_to(ROOT)}")
        return None
    return value


def validate_skills(errors: list[str]) -> None:
    actual = {
        path.name
        for path in (ROOT / "skills").iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    }
    if actual != SKILLS:
        errors.append(f"expected exactly five skills {sorted(SKILLS)}, found {sorted(actual)}")
    for name in sorted(SKILLS):
        directory = ROOT / "skills" / name
        metadata = frontmatter(directory / "SKILL.md", errors)
        if not isinstance(metadata, dict) or metadata.get("name") != name:
            errors.append(f"invalid SKILL.md name: skills/{name}/SKILL.md")
        agent = load(directory / "agents/openai.yaml", errors)
        prompt = agent.get("interface", {}).get("default_prompt", "") if isinstance(agent, dict) else ""
        if f"${name}" not in str(prompt):
            errors.append(f"default_prompt does not mention ${name}: skills/{name}/agents/openai.yaml")
        if name == "check-starry-compliance" and (
            not isinstance(agent, dict)
            or agent.get("interface", {}).get("display_name") != "$合规检查"
        ):
            errors.append("check-starry-compliance display name must be $合规检查")
        if name == "fix-starry-compliance" and (
            not isinstance(agent, dict)
            or agent.get("interface", {}).get("display_name") != "$修复缺口"
        ):
            errors.append("fix-starry-compliance display name must be $修复缺口")
        if not (directory / "scripts/run.py").is_file():
            errors.append(f"missing runner: skills/{name}/scripts/run.py")


def validate_rules(errors: list[str]) -> dict[str, dict[str, Any]]:
    rules: dict[str, dict[str, Any]] = {}
    for path in sorted((ROOT / "library/rules").glob("*.yaml")):
        entity = load(path, errors)
        if not isinstance(entity, dict):
            continue
        rule_id = entity.get("rule_id")
        if entity.get("kind") != "syscallguard_rule" or not isinstance(rule_id, str):
            errors.append(f"invalid rule entity: {path.relative_to(ROOT)}")
            continue
        if rule_id in rules:
            errors.append(f"duplicate rule id: {rule_id}")
        rules[rule_id] = entity
        if not isinstance(entity.get("generated_at_utc"), str):
            errors.append(f"rule has no generated_at_utc: {path.relative_to(ROOT)}")
        if entity.get("semantic_hash") != version_hash(entity):
            errors.append(f"rule semantic_hash mismatch: {path.relative_to(ROOT)}")
        if not isinstance(entity.get("sources"), list):
            errors.append(f"rule sources is not a list: {path.relative_to(ROOT)}")
        forbidden = {"last_processed_run", "mapping_refs", "finding_refs", "fix_refs"}
        if forbidden.intersection(entity):
            errors.append(f"downstream state leaked into rule: {path.relative_to(ROOT)}")
    return rules


def validate_syscall_index(errors: list[str], rules: dict[str, dict[str, Any]]) -> None:
    path = ROOT / "library/syscalls.yaml"
    if not path.exists():
        if rules:
            errors.append("missing: library/syscalls.yaml")
        return
    index = load(path, errors)
    if not isinstance(index, dict):
        return
    if index.get("kind") != "syscallguard_syscall_index":
        errors.append("invalid syscall index kind: library/syscalls.yaml")
    syscalls = index.get("syscalls")
    if not isinstance(syscalls, dict):
        errors.append("syscall index has no syscalls mapping")
        return
    index_text = path.read_text(encoding="utf-8")
    for syscall, refs in syscalls.items():
        if not isinstance(syscall, str) or not isinstance(refs, list):
            errors.append(f"invalid syscall index row: {syscall!r}")
            continue
        for ref in refs:
            if not isinstance(ref, dict) or set(ref) != {"rule_id", "path"}:
                errors.append(f"invalid rule reference for syscall {syscall}")
                continue
            rule_id = ref["rule_id"]
            if rule_id not in rules:
                errors.append(f"unknown rule {rule_id!r} for syscall {syscall}")
            filename = re.sub(r"[^a-z0-9]+", "-", str(rule_id).lower()).strip("-")
            expected = f"library/rules/{filename}.yaml"
            if ref["path"] != expected:
                errors.append(f"wrong rule path for {rule_id!r} in syscall index")
                continue
            rule_path = ROOT / expected
            if rule_path.is_file():
                comment = rule_path.read_text(encoding="utf-8").splitlines()[0]
                needle = f"  {comment}\n  - rule_id: {rule_id}\n"
                if not comment.startswith("# 合规检查：") or needle not in index_text:
                    errors.append(f"missing matching Chinese comment for {rule_id!r} in syscall index")


def validate_reports(errors: list[str]) -> dict[str, dict[str, Any]]:
    reports: dict[str, dict[str, Any]] = {}
    for path in sorted((ROOT / "runs").glob("spec-*/report.md")):
        value = frontmatter(path, errors)
        if not isinstance(value, dict):
            continue
        report_id = path.parent.name
        if value.get("kind") != "syscallguard_ingest_report" or value.get("report_id") != report_id:
            errors.append(f"invalid ingest report identity: {path.relative_to(ROOT)}")
            continue
        reports[report_id] = value
        required = {
            "generated_at_utc",
            "source",
            "count",
            "pending_count",
            "selected_syscalls",
            "syscalls",
        }
        missing = sorted(required.difference(value))
        if missing:
            errors.append(f"ingest report {report_id} missing {missing}")
            continue
        source = value.get("source")
        if not isinstance(source, dict) or not all(
            isinstance(source.get(key), str)
            for key in ("id", "type", "snapshot_hash", "descriptor_hash", "recognition_rules_hash")
        ):
            errors.append(f"ingest report {report_id} has invalid source metadata")
        rows = value.get("syscalls")
        if not isinstance(rows, list):
            errors.append(f"ingest report {report_id} syscalls is not a list")
            continue
        selected = value.get("selected_syscalls")
        row_ids = [row.get("syscall") for row in rows if isinstance(row, dict)]
        if selected != row_ids:
            errors.append(f"ingest report {report_id} selected_syscalls mismatch")
        count = value.get("count")
        if not isinstance(count, dict) or set(count) != {"value", "source"}:
            errors.append(f"ingest report {report_id} has invalid count metadata")
        if "requested_syscalls" in value:
            requested = value.get("requested_syscalls")
            if (
                not isinstance(requested, list)
                or not requested
                or not all(
                    isinstance(item, str) and item and item == item.strip().lower()
                    for item in requested
                )
                or requested != sorted(set(requested))
            ):
                errors.append(f"ingest report {report_id} has invalid requested_syscalls")
            elif not isinstance(selected, list) or not set(selected).issubset(requested):
                errors.append(f"ingest report {report_id} selects unrequested syscalls")
            if count != {"value": None, "source": "explicit_syscalls"}:
                errors.append(f"ingest report {report_id} has invalid syscall-list count")
        elif isinstance(count, dict) and count.get("source") == "explicit_syscalls":
            errors.append(f"ingest report {report_id} has no requested_syscalls")
        elif isinstance(count, dict):
            count_value = count.get("value")
            count_source = count.get("source")
            valid_count = count_value == "all" or (
                isinstance(count_value, str)
                and count_value.isdigit()
                and int(count_value) > 0
                and str(int(count_value)) == count_value
            )
            if not valid_count or count_source not in {
                "command",
                "descriptor",
                "global_default",
            }:
                errors.append(f"ingest report {report_id} has invalid resolved count")
        for row in rows:
            if not isinstance(row, dict) or row.get("result") not in {"formed_rules", "no_rules"}:
                errors.append(f"ingest report {report_id} has invalid syscall result")
                continue
            for key in ("source_fingerprint", "recognition_fingerprint", "reason"):
                if not isinstance(row.get(key), str):
                    errors.append(f"ingest report {report_id} syscall has invalid {key}")
            versions = row.get("rules")
            if not isinstance(versions, list) or not all(valid_version(item) for item in versions):
                errors.append(f"ingest report {report_id} has invalid rule versions")
            if row.get("result") == "no_rules" and versions:
                errors.append(f"ingest report {report_id} publishes rules for no_rules")
            if not isinstance(row.get("evidence_count"), int) or not isinstance(
                row.get("unresolved_evidence_count"), int
            ):
                errors.append(f"ingest report {report_id} has invalid evidence counts")
        extras = [item.name for item in path.parent.iterdir() if item.name != "report.md"]
        if extras:
            errors.append(f"ingest report directory {report_id} has extra artifacts: {sorted(extras)}")
    return reports


def validate_mapping_reports(
    errors: list[str], rules: dict[str, dict[str, Any]]
) -> dict[str, dict[str, Any]]:
    reports: dict[str, dict[str, Any]] = {}
    for path in sorted((ROOT / "runs").glob("mapping-*/report.md")):
        value = frontmatter(path, errors)
        if not isinstance(value, dict):
            continue
        report_id = path.parent.name
        if (
            value.get("kind") != "syscallguard_mapping_report"
            or value.get("report_id") != report_id
            or value.get("status") != "completed"
        ):
            errors.append(f"invalid mapping report identity: {path.relative_to(ROOT)}")
            continue
        reports[report_id] = value
        extras = [item.name for item in path.parent.iterdir() if item.name != "report.md"]
        if extras:
            errors.append(f"mapping report directory {report_id} has extra artifacts: {sorted(extras)}")
        if not isinstance(value.get("generated_at_utc"), str):
            errors.append(f"mapping report {report_id} has no generated_at_utc")
        if not isinstance(value.get("rule_index_hash"), str):
            errors.append(f"mapping report {report_id} has no rule_index_hash")
        target = value.get("target")
        if not isinstance(target, dict) or not all(
            isinstance(target.get(key), str)
            for key in (
                "target_id",
                "repository",
                "repository_identity",
                "revision",
                "worktree_root",
                "descriptor_hash",
                "snapshot_hash",
            )
        ):
            errors.append(f"mapping report {report_id} has invalid target metadata")
        scope = value.get("execution_scope")
        if not isinstance(scope, dict) or not all(
            isinstance(scope.get(key), list)
            for key in ("rules", "static_checks", "dynamic_tests")
        ):
            errors.append(f"mapping report {report_id} has invalid execution_scope")
        relation = value.get("rule_syscalls")
        rows = value.get("rules")
        if not isinstance(relation, dict) or not isinstance(rows, dict):
            errors.append(f"mapping report {report_id} has invalid complete rule state")
            continue
        for rule_id, row in rows.items():
            if not isinstance(row, dict):
                errors.append(f"mapping report {report_id} has invalid rule row {rule_id}")
                continue
            if row.get("status") not in {"covered", "needs_review", "unsupported", "pending"}:
                errors.append(f"mapping report {report_id} has invalid status for {rule_id}")
            if not valid_version(row.get("rule_version")):
                errors.append(f"mapping report {report_id} has invalid rule version for {rule_id}")
            if row.get("syscalls") != relation.get(rule_id):
                errors.append(f"mapping report {report_id} syscall relation mismatch for {rule_id}")
            for key in ("static_check_refs", "dynamic_test_refs", "target_dependencies"):
                if not isinstance(row.get(key), list):
                    errors.append(f"mapping report {report_id} has invalid {key} for {rule_id}")
            if not isinstance(row.get("entity_versions"), dict):
                errors.append(f"mapping report {report_id} has no entity versions for {rule_id}")
            if not isinstance(row.get("last_processed_report"), (str, type(None))):
                errors.append(f"mapping report {report_id} has invalid last report for {rule_id}")
    if reports:
        latest = max(
            reports.values(),
            key=lambda row: (str(row.get("generated_at_utc", "")), str(row.get("report_id", ""))),
        )
        latest_rows = latest.get("rules", {})
        if set(latest_rows) != set(rules):
            errors.append("latest mapping report does not exactly cover the general rule library")
        for rule_id, entity in rules.items():
            row = latest_rows.get(rule_id, {})
            if isinstance(row, dict) and row.get("rule_version", {}).get("content_hash") != version_hash(
                entity
            ):
                errors.append(f"latest mapping report has stale rule version for {rule_id}")
    return reports


def validate_runs(
    errors: list[str], check_reports: dict[str, dict[str, Any]]
) -> dict[str, dict[str, Any]]:
    runs: dict[str, dict[str, Any]] = {}
    for path in sorted((ROOT / "runs").glob("*/manifest.yaml")):
        value = load(path, errors)
        if not isinstance(value, dict):
            continue
        run_id = path.parent.name
        stage = value.get("stage")
        if value.get("kind") != "syscallguard_run" or value.get("run_id") != run_id:
            errors.append(f"invalid run identity: {path.relative_to(ROOT)}")
        if stage != "fix":
            errors.append(f"run {run_id} has invalid stage {stage!r}")
        if value.get("status") not in RUN_STATUSES:
            errors.append(f"run {run_id} has invalid status {value.get('status')!r}")
        if value.get("status") == "running":
            errors.append(f"repository contains unfinished run: {run_id}")
        if not (path.parent / "changeset.yaml").is_file():
            errors.append(f"run has no changeset: {run_id}")
        source_ids = value.get("source_check_report_ids")
        legacy_parent = value.get("from_run_id")
        if not (
            isinstance(source_ids, list)
            and source_ids
            and all(isinstance(item, str) for item in source_ids)
        ) and not isinstance(legacy_parent, str):
            errors.append(
                f"run {run_id} has neither source_check_report_ids nor historical from_run_id"
            )
        runs[run_id] = value
    for run_id, value in runs.items():
        stage = value.get("stage")
        if stage == "fix":
            raw_sources = value.get("source_check_report_ids")
            parent_ids = (
                raw_sources
                if isinstance(raw_sources, list) and raw_sources
                else [value.get("from_run_id")]
            )
            for parent_id in parent_ids:
                if not isinstance(parent_id, str) or parent_id not in check_reports:
                    errors.append(
                        f"fix run {run_id} has no check report parent {parent_id!r}"
                    )
    return runs


def validate_check_reports(
    errors: list[str], mapping_reports: dict[str, dict[str, Any]]
) -> dict[str, dict[str, Any]]:
    reports: dict[str, dict[str, Any]] = {}
    for path in sorted((ROOT / "runs").glob("check-*/report.md")):
        value = frontmatter(path, errors)
        if not isinstance(value, dict):
            continue
        report_id = path.parent.name
        if (
            value.get("kind") != "syscallguard_check_report"
            or value.get("report_id") != report_id
            or value.get("status") not in {"completed", "completed_with_blockers"}
        ):
            errors.append(f"invalid check report identity: {path.relative_to(ROOT)}")
            continue
        reports[report_id] = value
        extras = [item.name for item in path.parent.iterdir() if item.name != "report.md"]
        if extras:
            errors.append(f"check report directory {report_id} has extra artifacts: {sorted(extras)}")
        if value.get("content_hash") != version_hash(value):
            errors.append(f"check report {report_id} content hash mismatch")
        parent_id = value.get("mapping_report_id")
        if not isinstance(parent_id, str) or parent_id not in mapping_reports:
            errors.append(f"check report {report_id} has no mapping report parent")
        elif not valid_version(value.get("mapping_report_version")):
            errors.append(f"check report {report_id} has invalid mapping report version")
        else:
            parent = mapping_reports[parent_id]
            recorded_parent = value["mapping_report_version"]
            if (
                recorded_parent.get("id") != parent_id
                or recorded_parent.get("generated_at_utc") != parent.get("generated_at_utc")
                or recorded_parent.get("content_hash") != version_hash(parent)
            ):
                errors.append(f"check report {report_id} mapping report version mismatch")
        target = value.get("target")
        if not isinstance(target, dict) or not isinstance(target.get("snapshot_hash"), str):
            errors.append(f"check report {report_id} has invalid target metadata")
        scope = value.get("execution_scope")
        versions = value.get("entity_versions")
        if not isinstance(scope, dict) or not all(
            isinstance(scope.get(key), list)
            for key in ("rules", "static_checks", "dynamic_tests")
        ):
            errors.append(f"check report {report_id} has invalid execution scope")
        lifecycle_fields = {
            "new_findings": "new_finding_ids",
            "carried_findings": "carried_finding_ids",
            "revalidated_findings": "revalidated_finding_ids",
            "needs_revalidation": "needs_revalidation_finding_ids",
        }
        if any(field in value for field in lifecycle_fields.values()):
            for count_key, field in lifecycle_fields.items():
                ids = value.get(field)
                if not isinstance(ids, list) or not all(
                    isinstance(item, str) for item in ids
                ):
                    errors.append(f"check report {report_id} has invalid {field}")
                elif isinstance(value.get("counts"), dict) and value["counts"].get(
                    count_key
                ) != len(ids):
                    errors.append(
                        f"check report {report_id} count mismatch for {count_key}"
                    )
            for field in (
                "base_execution_scope",
                "revalidation_scope",
                "effective_execution_scope",
            ):
                extra_scope = value.get(field)
                if not isinstance(extra_scope, dict) or not all(
                    isinstance(extra_scope.get(key), list)
                    for key in ("rules", "static_checks", "dynamic_tests")
                ):
                    errors.append(f"check report {report_id} has invalid {field}")
            if value.get("effective_execution_scope") != scope:
                errors.append(
                    f"check report {report_id} effective execution scope mismatch"
                )
        if not isinstance(versions, dict) or not all(
            isinstance(versions.get(key), dict)
            for key in ("rules", "static_checks", "dynamic_tests")
        ):
            errors.append(f"check report {report_id} has invalid entity versions")
        static = value.get("static")
        dynamic = value.get("dynamic")
        if not isinstance(static, list) or not all(
            isinstance(row, dict) and row.get("result") in {"pass", "fail", "error"}
            for row in static
        ):
            errors.append(f"check report {report_id} has invalid static results")
        if not isinstance(dynamic, list) or not all(
            isinstance(row, dict)
            and row.get("result") in {"pass", "fail", "skipped", "not_run"}
            for row in dynamic
        ):
            errors.append(f"check report {report_id} has invalid dynamic results")
        if isinstance(scope, dict) and isinstance(static, list) and isinstance(dynamic, list):
            static_ids = [row.get("check_id") for row in static if isinstance(row, dict)]
            dynamic_ids = [row.get("test_id") for row in dynamic if isinstance(row, dict)]
            if static_ids != scope.get("static_checks"):
                errors.append(f"check report {report_id} static scope mismatch")
            if dynamic_ids != scope.get("dynamic_tests"):
                errors.append(f"check report {report_id} dynamic scope mismatch")
            for row in static + dynamic:
                if not isinstance(row, dict) or not isinstance(row.get("finding_ids"), list):
                    errors.append(f"check report {report_id} result has invalid finding IDs")
            for row in dynamic:
                if not isinstance(row, dict):
                    continue
                output = row.get("output_tail", "")
                if not isinstance(output, str) or len(output.encode("utf-8")) > 8 * 1024:
                    errors.append(f"check report {report_id} has oversized dynamic evidence")
                if row.get("result") == "fail" and not isinstance(row.get("exit_code"), int):
                    errors.append(f"check report {report_id} reliable failure has no exit code")
        blockers = value.get("blockers")
        if not isinstance(blockers, list):
            errors.append(f"check report {report_id} blockers is not a list")
        elif (value.get("status") == "completed_with_blockers") != bool(blockers):
            errors.append(f"check report {report_id} status/blocker mismatch")
        counts = value.get("counts")
        if not isinstance(counts, dict):
            errors.append(f"check report {report_id} counts is not a mapping")
        elif isinstance(static, list) and isinstance(dynamic, list) and isinstance(blockers, list):
            expected_counts = {
                "static_pass": sum(row.get("result") == "pass" for row in static),
                "static_fail": sum(row.get("result") == "fail" for row in static),
                "static_error": sum(row.get("result") == "error" for row in static),
                "dynamic_pass": sum(row.get("result") == "pass" for row in dynamic),
                "dynamic_fail": sum(row.get("result") == "fail" for row in dynamic),
                "dynamic_skipped": sum(row.get("result") == "skipped" for row in dynamic),
                "dynamic_not_run": sum(row.get("result") == "not_run" for row in dynamic),
                "blockers": len(blockers),
            }
            finding_ids_for_count = value.get("finding_ids")
            if isinstance(finding_ids_for_count, list):
                expected_counts["findings"] = len(finding_ids_for_count)
            for key, expected in expected_counts.items():
                if counts.get(key) != expected:
                    errors.append(f"check report {report_id} count mismatch for {key}")
        finding_ids = value.get("finding_ids")
        finding_versions = value.get("finding_versions")
        if (
            not isinstance(finding_ids, list)
            or not isinstance(finding_versions, dict)
            or sorted(finding_versions) != sorted(finding_ids)
            or not all(valid_version(row) for row in finding_versions.values())
        ):
            errors.append(f"check report {report_id} has invalid finding versions")
    return reports


def validate_indexes(errors: list[str]) -> dict[str, dict[str, Any]]:
    entities: dict[str, dict[str, Any]] = {}
    for relative, (index_kind, entity_kind) in TARGET_INDEXES.items():
        index = load(ROOT / relative, errors)
        if not isinstance(index, dict):
            continue
        if index.get("kind") != index_kind or not isinstance(index.get("entities"), list):
            errors.append(f"invalid index: {relative}")
            continue
        seen: set[str] = set()
        for row in index["entities"]:
            if not isinstance(row, dict) or not isinstance(row.get("id"), str):
                errors.append(f"invalid index row in {relative}")
                continue
            entity_id = row["id"]
            if entity_id in seen:
                errors.append(f"duplicate id {entity_id} in {relative}")
            seen.add(entity_id)
            raw_path = row.get("path")
            if not isinstance(raw_path, str):
                errors.append(f"index row {entity_id} has no path in {relative}")
                continue
            entity = load(ROOT / raw_path, errors)
            if not isinstance(entity, dict):
                continue
            entities[entity_id] = entity
            if entity.get("kind") != entity_kind:
                errors.append(f"wrong entity kind: {raw_path}")
            generated = entity.get("generated_at_utc")
            if not isinstance(generated, str):
                errors.append(f"entity has no generated_at_utc: {raw_path}")
            if row.get("generated_at_utc") != generated:
                errors.append(f"index generation mismatch: {raw_path}")
            if row.get("content_hash") != version_hash(entity):
                errors.append(f"index content hash mismatch: {raw_path}")
    return entities


def validate_finding_evidence(
    errors: list[str],
    entities: dict[str, dict[str, Any]],
    check_reports: dict[str, dict[str, Any]],
) -> None:
    for entity_id, entity in entities.items():
        if entity.get("kind") != "syscallguard_starry_finding":
            continue
        if entity.get("resolution") not in {
            "open",
            "fixed",
            "superseded",
            "no_longer_reproduces",
        }:
            errors.append(f"finding {entity_id} has invalid resolution")
        occurrences = entity.get("occurrences")
        if not isinstance(occurrences, list):
            errors.append(f"finding {entity_id} occurrences is not a list")
            continue
        for occurrence in occurrences:
            if not isinstance(occurrence, dict):
                errors.append(f"finding {entity_id} has invalid occurrence")
                continue
            report_id = occurrence.get("check_report_id")
            evidence = occurrence.get("evidence")
            if not isinstance(report_id, str) or report_id not in check_reports:
                errors.append(f"finding {entity_id} occurrence has no check report")
            if not isinstance(evidence, dict):
                errors.append(f"finding {entity_id} occurrence has invalid evidence")
                continue
            if {"log", "diagnostic_log"}.intersection(evidence):
                errors.append(f"finding {entity_id} occurrence references temporary logs")
            output = evidence.get("output_tail", "")
            if not isinstance(output, str) or len(output.encode("utf-8")) > 8 * 1024:
                errors.append(f"finding {entity_id} has oversized dynamic evidence")


def validate_executable_indexes(
    errors: list[str], rules: dict[str, dict[str, Any]]
) -> dict[str, dict[str, Any]]:
    entities: dict[str, dict[str, Any]] = {}
    referenced_assets: set[Path] = set()
    for relative, (index_kind, entity_kind, id_field, directory) in EXECUTABLE_INDEXES.items():
        index = load(ROOT / relative, errors)
        if not isinstance(index, dict):
            continue
        groups = index.get("syscalls")
        if index.get("kind") != index_kind or not isinstance(groups, dict):
            errors.append(f"invalid grouped executable index: {relative}")
            continue
        seen_rows: dict[str, dict[str, Any]] = {}
        for syscall, rows in groups.items():
            if not isinstance(syscall, str) or not isinstance(rows, list):
                errors.append(f"invalid syscall group in {relative}")
                continue
            for row in rows:
                if not isinstance(row, dict) or set(row) != {id_field, "path", "rule_refs"}:
                    errors.append(f"invalid grouped index row in {relative}")
                    continue
                entity_id = row.get(id_field)
                raw_path = row.get("path")
                refs = row.get("rule_refs")
                if (
                    not isinstance(entity_id, str)
                    or not isinstance(raw_path, str)
                    or not isinstance(refs, list)
                ):
                    errors.append(f"invalid grouped index row in {relative}")
                    continue
                expected = f"{directory}/{re.sub(r'[^a-z0-9]+', '-', entity_id.lower()).strip('-')}.yaml"
                if raw_path != expected:
                    errors.append(f"wrong detail path for {entity_id} in {relative}")
                prior = seen_rows.get(entity_id)
                if prior is not None and prior != row:
                    errors.append(f"conflicting grouped index row for {entity_id}")
                seen_rows[entity_id] = row
                entity = load(ROOT / raw_path, errors)
                if not isinstance(entity, dict):
                    continue
                entities[entity_id] = entity
                if entity.get("kind") != entity_kind or entity.get(id_field) != entity_id:
                    errors.append(f"invalid executable detail: {raw_path}")
                if entity.get("rule_refs") != refs or not refs or not set(refs).issubset(rules):
                    errors.append(f"invalid rule_refs for executable detail: {raw_path}")
                expected_syscalls = {
                    owner
                    for rule_id in refs
                    for owner, rule_refs in _rule_syscall_relation().items()
                    if rule_id in rule_refs
                }
                if syscall not in expected_syscalls:
                    errors.append(f"wrong syscall group for {entity_id}: {syscall}")
                if not isinstance(entity.get("generated_at_utc"), str):
                    errors.append(f"executable detail has no generated_at_utc: {raw_path}")
                if not isinstance(entity.get("target_dependencies"), list) or not isinstance(
                    entity.get("target_content_fingerprint"), str
                ):
                    errors.append(f"executable detail has no target fingerprint: {raw_path}")
                if not isinstance(entity.get("upstream_dependencies"), list):
                    errors.append(f"executable detail has no rule dependencies: {raw_path}")
                if id_field == "test_id":
                    for key in ("patch_file", "test_source"):
                        value = entity.get(key)
                        if isinstance(value, str) and value.startswith(
                            "targets/starry/dynamic-tests/assets/"
                        ):
                            asset = Path(value)
                            referenced_assets.add(asset)
                            if not (ROOT / asset).is_file():
                                errors.append(f"dynamic test asset is missing: {value}")
                    patch_file = entity.get("patch_file")
                    if isinstance(patch_file, str) and patch_file and not patch_file.startswith(
                        "targets/starry/dynamic-tests/assets/"
                    ):
                        errors.append(f"dynamic test patch is outside assets: {raw_path}")
        detail_directory = ROOT / directory
        indexed = set(seen_rows)
        actual = {
            str(entity.get(id_field))
            for path in detail_directory.glob("*.yaml")
            if isinstance((entity := load(path, errors)), dict)
        }
        if actual != indexed:
            errors.append(f"grouped index/detail mismatch for {relative}")
    assets_root = ROOT / "targets/starry/dynamic-tests/assets"
    actual_assets = (
        {
            Path("targets/starry/dynamic-tests/assets") / path.relative_to(assets_root)
            for path in assets_root.rglob("*")
            if path.is_file()
        }
        if assets_root.is_dir()
        else set()
    )
    if actual_assets != referenced_assets:
        errors.append("dynamic test assets and detail references do not match")
    return entities


def _rule_syscall_relation() -> dict[str, list[str]]:
    path = ROOT / "library/syscalls.yaml"
    if not path.is_file():
        return {}
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    syscalls = value.get("syscalls", {}) if isinstance(value, dict) else {}
    return {
        syscall: [str(row.get("rule_id")) for row in rows if isinstance(row, dict)]
        for syscall, rows in syscalls.items()
        if isinstance(syscall, str) and isinstance(rows, list)
    }


def validate_sources(errors: list[str]) -> None:
    index = load(ROOT / "sources/index.yaml", errors)
    if not isinstance(index, dict) or index.get("default_source") != "ltp-local":
        errors.append("source index must define default_source: ltp-local")
    rules = load(ROOT / "sources/adapters/ltp/recognition-rules.yaml", errors)
    recognizers = rules.get("recognizers", []) if isinstance(rules, dict) else []
    ids = [row.get("id") for row in recognizers if isinstance(row, dict)]
    if not ids or len(ids) != len(set(ids)):
        errors.append("LTP recognizers need unique stable ids")


def validate_no_persisted_commit_ids(errors: list[str]) -> None:
    forbidden_keys = {
        "base_commit",
        "mapped_commit",
        "current_commit",
        "checked_commit",
        "starry_commit",
        "fixed_commit",
        "target_revision",
    }

    def visit(value: Any, relative: str) -> None:
        if isinstance(value, dict):
            leaked = sorted(forbidden_keys.intersection(value))
            if leaked:
                errors.append(f"persisted Git commit fields {leaked} in {relative}")
            for child in value.values():
                visit(child, relative)
        elif isinstance(value, list):
            for child in value:
                visit(child, relative)
        elif isinstance(value, str) and re.fullmatch(r"[0-9a-fA-F]{40}|[0-9a-fA-F]{64}", value):
            errors.append(f"persisted Git commit ID in {relative}")

    roots = [ROOT / "library", ROOT / "runs", ROOT / "targets/starry"]
    for directory in roots:
        if not directory.exists():
            continue
        for path in directory.rglob("*.yaml"):
            value = load(path, errors)
            visit(value, str(path.relative_to(ROOT)))
    for path in (ROOT / "runs").glob("*/report.md"):
        value = frontmatter(path, errors)
        if isinstance(value, dict):
            visit(value, str(path.relative_to(ROOT)))


def validate_removed_legacy(errors: list[str]) -> None:
    forbidden = [
        "library/specs",
        "library/rules/index.yaml",
        "state/ingest",
        "batches/syscall-check-history.yaml",
        "runs/spec-migrated-batch-001",
        "runs/mapping-migrated-batch-001",
        "runs/check-migrated-batch-001",
        "runs/fix-migrated-batch-001",
        "targets/starry/mappings",
        "targets/starry/rule-coverage.yaml",
        "targets/starry/static-checks/index.yaml",
        "targets/starry/dynamic-tests/index.yaml",
    ]
    for relative in forbidden:
        if (ROOT / relative).exists():
            errors.append(f"legacy artifact still exists: {relative}")
    if list((ROOT / "runs").glob("*/legacy-artifacts")):
        errors.append("legacy-artifacts directories must be removed")


def validate_all_yaml(errors: list[str]) -> None:
    for path in ROOT.rglob("*.yaml"):
        if ".git" in path.parts:
            continue
        load(path, errors)


def main() -> int:
    errors: list[str] = []
    validate_skills(errors)
    rules = validate_rules(errors)
    validate_syscall_index(errors, rules)
    reports = validate_reports(errors)
    mapping_reports = validate_mapping_reports(errors, rules)
    check_reports = validate_check_reports(errors, mapping_reports)
    runs = validate_runs(errors, check_reports)
    shared_entities = validate_indexes(errors)
    validate_finding_evidence(errors, shared_entities, check_reports)
    validate_executable_indexes(errors, rules)
    validate_sources(errors)
    validate_no_persisted_commit_ids(errors)
    validate_removed_legacy(errors)
    validate_all_yaml(errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("repository validation: OK")
    print(
        f"skills={len(SKILLS)} ingest_reports={len(reports)} "
        f"mapping_reports={len(mapping_reports)} check_reports={len(check_reports)} "
        f"rules={len(rules)} fix_runs={len(runs)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
