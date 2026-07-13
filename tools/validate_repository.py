#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "ingest-syscall-specs",
    "map-starry-checks",
    "check-starry-compliance",
    "fix-starry-compliance",
}
RUN_STATUSES = {"running", "completed", "completed_with_blockers", "failed", "superseded"}
UPSTREAM = {"mapping": "spec", "check": "mapping", "fix": "check"}
INDEXES = {
    "library/specs/index.yaml": ("syscallguard_spec_index", "syscallguard_syscall_spec"),
    "library/rules/index.yaml": ("syscallguard_rule_index", "syscallguard_rule"),
    "targets/starry/mappings/index.yaml": ("syscallguard_starry_mapping_index", "syscallguard_starry_mapping"),
    "targets/starry/static-checks/index.yaml": ("syscallguard_starry_static_check_index", "syscallguard_starry_static_check"),
    "targets/starry/dynamic-tests/index.yaml": ("syscallguard_starry_dynamic_test_index", "syscallguard_starry_dynamic_test"),
    "targets/starry/findings/index.yaml": ("syscallguard_starry_finding_index", "syscallguard_starry_finding"),
    "targets/starry/fixes/index.yaml": ("syscallguard_starry_fix_index", "syscallguard_starry_fix"),
}


def load(path: Path, errors: list[str]) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing: {path.relative_to(ROOT)}")
    except (OSError, yaml.YAMLError) as exc:
        errors.append(f"cannot read {path.relative_to(ROOT)}: {exc}")
    return None


def validate_skills(errors: list[str]) -> None:
    actual = {
        path.name
        for path in (ROOT / "skills").iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    }
    if actual != SKILLS:
        errors.append(f"expected exactly four skills {sorted(SKILLS)}, found {sorted(actual)}")
    for name in SKILLS:
        directory = ROOT / "skills" / name
        skill_path = directory / "SKILL.md"
        try:
            text = skill_path.read_text(encoding="utf-8")
            parts = text.split("---", 2)
            frontmatter = yaml.safe_load(parts[1]) if len(parts) == 3 else None
        except (OSError, yaml.YAMLError) as exc:
            errors.append(f"cannot read skills/{name}/SKILL.md: {exc}")
            frontmatter = None
        if not isinstance(frontmatter, dict) or frontmatter.get("name") != name:
            errors.append(f"invalid SKILL.md frontmatter: skills/{name}/SKILL.md")
        metadata = load(directory / "agents/openai.yaml", errors)
        if not isinstance(metadata, dict):
            continue
        prompt = metadata.get("interface", {}).get("default_prompt", "")
        if f"${name}" not in str(prompt):
            errors.append(f"default_prompt does not mention ${name}: skills/{name}/agents/openai.yaml")
        if not (directory / "scripts/run.py").is_file():
            errors.append(f"missing runner: skills/{name}/scripts/run.py")


def validate_runs(errors: list[str]) -> dict[str, dict[str, Any]]:
    manifests: dict[str, dict[str, Any]] = {}
    for path in sorted((ROOT / "runs").glob("*/manifest.yaml")):
        value = load(path, errors)
        if not isinstance(value, dict):
            continue
        run_id = value.get("run_id")
        if run_id != path.parent.name:
            errors.append(f"run id mismatch: {path.relative_to(ROOT)}")
            continue
        if value.get("kind") != "syscallguard_run":
            errors.append(f"invalid run kind: {path.relative_to(ROOT)}")
        if value.get("status") not in RUN_STATUSES:
            errors.append(f"invalid run status: {path.relative_to(ROOT)}")
        if value.get("status") == "running":
            errors.append(f"repository contains unfinished run: {run_id}")
        if not (path.parent / "changeset.yaml").is_file():
            errors.append(f"run has no changeset: {run_id}")
        manifests[str(run_id)] = value
    for run_id, value in manifests.items():
        stage = value.get("stage")
        expected = UPSTREAM.get(str(stage))
        from_id = value.get("from_run_id")
        if expected:
            upstream = manifests.get(str(from_id))
            if upstream is None:
                errors.append(f"run {run_id} references missing upstream {from_id}")
            elif upstream.get("stage") != expected:
                errors.append(
                    f"run {run_id} expects {expected} upstream, found {upstream.get('stage')}"
                )
        elif stage == "spec" and from_id is not None:
            errors.append(f"spec run {run_id} must not have from_run_id")
        if stage not in {"spec", "mapping", "check", "fix"}:
            errors.append(f"run {run_id} has invalid stage {stage!r}")
    return manifests


def validate_indexes(errors: list[str]) -> None:
    for relative, (index_kind, entity_kind) in INDEXES.items():
        index_path = ROOT / relative
        index = load(index_path, errors)
        if not isinstance(index, dict):
            continue
        if index.get("kind") != index_kind:
            errors.append(f"wrong index kind in {relative}")
        entities = index.get("entities")
        if not isinstance(entities, list):
            errors.append(f"index entities is not a list in {relative}")
            continue
        ids: set[str] = set()
        for row in entities:
            if not isinstance(row, dict) or not isinstance(row.get("id"), str):
                errors.append(f"invalid index row in {relative}")
                continue
            if row["id"] in ids:
                errors.append(f"duplicate id {row['id']} in {relative}")
            ids.add(row["id"])
            entity_path = ROOT / str(row.get("path", ""))
            entity = load(entity_path, errors)
            if isinstance(entity, dict) and entity.get("kind") != entity_kind:
                errors.append(f"wrong entity kind in {entity_path.relative_to(ROOT)}")


def validate_migration(errors: list[str], runs: dict[str, dict[str, Any]]) -> None:
    required = {
        "spec-migrated-batch-001": "spec",
        "mapping-migrated-batch-001": "mapping",
        "check-migrated-batch-001": "check",
        "fix-migrated-batch-001": "fix",
    }
    for run_id, stage in required.items():
        if runs.get(run_id, {}).get("stage") != stage:
            errors.append(f"missing migrated {stage} run: {run_id}")
    specs_index = load(ROOT / "library/specs/index.yaml", errors)
    rules_index = load(ROOT / "library/rules/index.yaml", errors)
    static_index = load(ROOT / "targets/starry/static-checks/index.yaml", errors)
    dynamic_index = load(ROOT / "targets/starry/dynamic-tests/index.yaml", errors)
    expected_counts = [(specs_index, 20, "syscalls"), (rules_index, 12, "rules"), (static_index, 9, "static checks"), (dynamic_index, 7, "dynamic tests")]
    for index, expected, label in expected_counts:
        actual = len(index.get("entities", [])) if isinstance(index, dict) else -1
        if actual != expected:
            errors.append(f"migration expected {expected} {label}, found {actual}")
    behavior_count = 0
    if isinstance(specs_index, dict):
        for row in specs_index.get("entities", []):
            entity = load(ROOT / row["path"], errors)
            if isinstance(entity, dict):
                behaviors = entity.get("normalized_behaviors", [])
                behavior_count += len(behaviors) if isinstance(behaviors, list) else 0
    if behavior_count != 289:
        errors.append(f"migration expected 289 normalized specs, found {behavior_count}")
    reviews = list((ROOT / "runs").glob("*/legacy-artifacts/reviews/*-signoff.yaml"))
    if len(reviews) != 10:
        errors.append(f"migration expected 10 legacy review records, found {len(reviews)}")


def validate_finding_boundary(errors: list[str]) -> None:
    index = load(ROOT / "targets/starry/findings/index.yaml", errors)
    if not isinstance(index, dict):
        return
    for row in index.get("entities", []):
        entity = load(ROOT / row["path"], errors)
        if not isinstance(entity, dict):
            continue
        if entity.get("status") != "confirmed":
            errors.append(f"finding is not confirmed: {row['id']}")
        if "blocker" in entity or "blockers" in entity:
            errors.append(f"blocker field leaked into finding: {row['id']}")
        occurrences = entity.get("occurrences", [])
        if not isinstance(occurrences, list):
            errors.append(f"finding occurrences is not a list: {row['id']}")
            continue
        for occurrence in occurrences:
            result = occurrence.get("result", {}) if isinstance(occurrence, dict) else {}
            if not isinstance(result, dict) or result.get("result") != "fail":
                errors.append(f"non-failure evidence leaked into finding: {row['id']}")


def main() -> int:
    errors: list[str] = []
    validate_skills(errors)
    runs = validate_runs(errors)
    validate_indexes(errors)
    validate_migration(errors, runs)
    validate_finding_boundary(errors)
    history = load(ROOT / "batches/syscall-check-history.yaml", errors)
    if not isinstance(history, dict) or history.get("kind") != "syscallguard_entity_history":
        errors.append("history is not entity-hash based")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("repository validation: OK")
    print("skills=4 runs=4 syscalls=20 normalized_specs=289 rules=12 static_checks=9 dynamic_tests=7")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
