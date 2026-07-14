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
    "targets/starry/mappings/index.yaml": (
        "syscallguard_starry_mapping_index",
        "syscallguard_starry_mapping",
    ),
    "targets/starry/static-checks/index.yaml": (
        "syscallguard_starry_static_check_index",
        "syscallguard_starry_static_check",
    ),
    "targets/starry/dynamic-tests/index.yaml": (
        "syscallguard_starry_dynamic_test_index",
        "syscallguard_starry_dynamic_test",
    ),
    "targets/starry/findings/index.yaml": (
        "syscallguard_starry_finding_index",
        "syscallguard_starry_finding",
    ),
    "targets/starry/fixes/index.yaml": (
        "syscallguard_starry_fix_index",
        "syscallguard_starry_fix",
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


def validate_runs(errors: list[str], reports: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    runs: dict[str, dict[str, Any]] = {}
    for path in sorted((ROOT / "runs").glob("*/manifest.yaml")):
        value = load(path, errors)
        if not isinstance(value, dict):
            continue
        run_id = path.parent.name
        stage = value.get("stage")
        if value.get("kind") != "syscallguard_run" or value.get("run_id") != run_id:
            errors.append(f"invalid run identity: {path.relative_to(ROOT)}")
        if stage not in {"mapping", "check", "fix"}:
            errors.append(f"run {run_id} has invalid stage {stage!r}")
        if value.get("status") not in RUN_STATUSES:
            errors.append(f"run {run_id} has invalid status {value.get('status')!r}")
        if value.get("status") == "running":
            errors.append(f"repository contains unfinished run: {run_id}")
        if not (path.parent / "changeset.yaml").is_file():
            errors.append(f"run has no changeset: {run_id}")
        if stage == "mapping":
            if not isinstance(value.get("rule_index_hash"), str):
                errors.append(f"mapping run {run_id} has no rule_index_hash")
            if not isinstance(value.get("selected_rule_versions"), dict):
                errors.append(f"mapping run {run_id} has no selected_rule_versions")
            if not isinstance(value.get("rule_syscalls"), dict):
                errors.append(f"mapping run {run_id} has no rule_syscalls")
            if "from_run_id" in value:
                errors.append(f"mapping run {run_id} must not use from_run_id")
            if "from_report_id" in value:
                errors.append(f"mapping run {run_id} must not use from_report_id")
        elif stage in {"check", "fix"} and not isinstance(value.get("from_run_id"), str):
            errors.append(f"run {run_id} has no from_run_id")
        runs[run_id] = value
    for run_id, value in runs.items():
        stage = value.get("stage")
        if stage == "check":
            parent = runs.get(str(value.get("from_run_id")))
            if parent is not None and parent.get("stage") != "mapping":
                errors.append(f"check run {run_id} has non-mapping parent")
        if stage == "fix":
            parent = runs.get(str(value.get("from_run_id")))
            if parent is not None and parent.get("stage") != "check":
                errors.append(f"fix run {run_id} has non-check parent")
    return runs


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


def validate_sources(errors: list[str]) -> None:
    index = load(ROOT / "sources/index.yaml", errors)
    if not isinstance(index, dict) or index.get("default_source") != "ltp-local":
        errors.append("source index must define default_source: ltp-local")
    rules = load(ROOT / "sources/adapters/ltp/recognition-rules.yaml", errors)
    recognizers = rules.get("recognizers", []) if isinstance(rules, dict) else []
    ids = [row.get("id") for row in recognizers if isinstance(row, dict)]
    if not ids or len(ids) != len(set(ids)):
        errors.append("LTP recognizers need unique stable ids")


def validate_rule_coverage(
    errors: list[str], rules: dict[str, dict[str, Any]]
) -> None:
    path = ROOT / "targets/starry/rule-coverage.yaml"
    value = load(path, errors)
    if not isinstance(value, dict):
        return
    if value.get("kind") != "syscallguard_starry_rule_coverage":
        errors.append("invalid Starry rule coverage kind")
    rows = value.get("rules")
    if not isinstance(rows, dict):
        errors.append("Starry rule coverage has no rules mapping")
        return
    if set(rows) != set(rules):
        errors.append("Starry rule coverage does not exactly cover the general rule library")
    for rule_id, row in rows.items():
        if not isinstance(row, dict):
            errors.append(f"invalid coverage row for {rule_id}")
            continue
        if row.get("status") not in {"pending", "mapped", "needs_review", "unsupported"}:
            errors.append(f"invalid coverage status for {rule_id}")
        if not valid_version(row.get("rule_version")):
            errors.append(f"invalid coverage rule version for {rule_id}")
        if rule_id in rules and row.get("rule_version", {}).get("content_hash") != version_hash(
            rules[rule_id]
        ):
            errors.append(f"stale coverage rule version for {rule_id}")
        for key in ("mapping_refs", "static_check_refs", "dynamic_test_refs"):
            if not isinstance(row.get(key), list):
                errors.append(f"coverage {rule_id} has invalid {key}")


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
    runs = validate_runs(errors, reports)
    validate_indexes(errors)
    validate_rule_coverage(errors, rules)
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
        f"rules={len(rules)} downstream_runs={len(runs)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
