#!/usr/bin/env python3
"""Non-destructive SyscallGuard batch integrity checker."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - environment failure path
    yaml = None


STEPS = [
    "01-scope-selection",
    "02-spec-ingestion",
    "03-normalization-review",
    "04-checkability-classification",
    "05-starry-evidence-mapping",
    "06-static-check-or-audit",
    "07-gap-triage",
    "08-fix-plan-and-apply-outside-harness",
    "09-validation",
    "10-batch-closeout",
]

REVIEW_REQUIRED = [
    "batch_id",
    "step_id",
    "artifact",
    "status",
    "reviewer",
    "reviewed_at_utc",
    "decision_summary",
    "required_changes",
    "follow_up",
]

REVIEW_STATUSES = {
    "pending_human_review",
    "confirmed",
    "changes_requested",
    "not_applicable",
}
RESOLVED_REVIEW_STATUSES = {"confirmed", "not_applicable"}

COVERAGE_REQUIRED = [
    "behavior_id",
    "title",
    "source_refs",
    "checkability",
    "starry_evidence",
    "validation",
    "triage",
    "review_status",
]
COVERAGE_CHECKABILITY = {
    "static",
    "partial_static",
    "dynamic",
    "unsupported",
    "needs_review",
}
COVERAGE_TRIAGE = {
    "covered",
    "covered_pending_human_review",
    "gap",
    "risk",
    "unsupported",
    "needs_review",
}
TRIAGE_WITHOUT_STARRY_EVIDENCE = {"gap", "risk", "unsupported", "needs_review"}


class Reporter:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.gates: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def gate(self, message: str) -> None:
        self.gates.append(message)


def load_yaml(path: Path, reporter: Reporter) -> Any:
    if yaml is None:
        reporter.error("PyYAML is required: python3 -m pip install PyYAML")
        return None
    if not path.exists():
        reporter.error(f"Missing YAML file: {path}")
        return None
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
    except yaml.YAMLError as exc:
        reporter.error(f"Malformed YAML in {path}: {exc}")
        return None
    except OSError as exc:
        reporter.error(f"Cannot read {path}: {exc}")
        return None
    if data is None:
        reporter.error(f"Empty YAML file: {path}")
        return None
    return data


def find_repo_root(batch_dir: Path) -> Path:
    for candidate in [batch_dir, *batch_dir.parents]:
        if (candidate / "README.md").exists() and (candidate / "docs").exists():
            return candidate
    return Path.cwd()


def resolve_artifact(batch_dir: Path, repo_root: Path, raw_path: str) -> Path:
    batch_path = batch_dir / raw_path
    if batch_path.exists():
        return batch_path
    return repo_root / raw_path


def require_mapping(data: Any, path: Path, reporter: Reporter) -> dict[str, Any] | None:
    if not isinstance(data, dict):
        reporter.error(f"Expected mapping in {path}")
        return None
    return data


def check_manifest(
    batch_dir: Path, repo_root: Path, manifest: dict[str, Any], reporter: Reporter
) -> tuple[str | None, list[str], list[str]]:
    required = [
        "batch_id",
        "title",
        "status",
        "created_at_utc",
        "scope",
        "workflow",
        "artifacts",
    ]
    for key in required:
        if key not in manifest:
            reporter.error(f"manifest.yaml missing key: {key}")

    batch_id = manifest.get("batch_id")
    if not isinstance(batch_id, str) or not batch_id:
        reporter.error("manifest.yaml batch_id must be a non-empty string")
        batch_id = None
    elif batch_dir.name != batch_id:
        reporter.warn(
            f"manifest batch_id {batch_id!r} does not match directory {batch_dir.name!r}"
        )

    workflow = manifest.get("workflow")
    if not isinstance(workflow, list):
        reporter.error("manifest.yaml workflow must be a list")
    else:
        workflow_ids = [
            item.get("step_id") if isinstance(item, dict) else None for item in workflow
        ]
        if workflow_ids != STEPS:
            reporter.error("manifest.yaml workflow does not list the ten fixed steps in order")
        for index, step in enumerate(STEPS):
            if index >= len(workflow) or not isinstance(workflow[index], dict):
                continue
            item = workflow[index]
            expected_report = f"steps/{step}.md"
            expected_review = f"reviews/{step}-signoff.yaml"
            if item.get("report") != expected_report:
                reporter.error(
                    f"workflow {step} report should be {expected_report}, got {item.get('report')!r}"
                )
            if item.get("review") != expected_review:
                reporter.error(
                    f"workflow {step} review should be {expected_review}, got {item.get('review')!r}"
                )

    scope = manifest.get("scope")
    included: list[str] = []
    included_syscalls: list[str] = []
    if not isinstance(scope, dict):
        reporter.error("manifest.yaml scope must be a mapping")
    else:
        raw_included = scope.get("included_behaviors")
        raw_syscalls = scope.get("included_syscalls")
        if raw_included is None and raw_syscalls is None:
            reporter.error(
                "manifest.yaml scope must include included_behaviors or included_syscalls"
            )
        elif raw_included is not None:
            if not isinstance(raw_included, list) or not all(
                isinstance(item, str) for item in raw_included
            ):
                reporter.error(
                    "manifest.yaml scope.included_behaviors must be a list of strings"
                )
            else:
                included = raw_included
                duplicates = sorted({item for item in included if included.count(item) > 1})
                for behavior_id in duplicates:
                    reporter.error(f"Duplicate scoped behavior in manifest: {behavior_id}")
        if raw_syscalls is not None:
            if not isinstance(raw_syscalls, list) or not all(
                isinstance(item, str) for item in raw_syscalls
            ):
                reporter.error(
                    "manifest.yaml scope.included_syscalls must be a list of strings"
                )
            else:
                included_syscalls = [item.lower() for item in raw_syscalls]
                duplicates = sorted(
                    {item for item in included_syscalls if included_syscalls.count(item) > 1}
                )
                for syscall in duplicates:
                    reporter.error(f"Duplicate scoped syscall in manifest: {syscall}")

    artifacts = manifest.get("artifacts")
    if isinstance(artifacts, dict):
        for section_name in ("inputs", "outputs"):
            section = artifacts.get(section_name)
            if isinstance(section, dict):
                for name, raw_path in section.items():
                    if not isinstance(raw_path, str):
                        reporter.error(f"manifest artifacts.{section_name}.{name} must be a path string")
                        continue
                    if not resolve_artifact(batch_dir, repo_root, raw_path).exists():
                        reporter.warn(
                            f"Referenced artifact does not exist yet: artifacts.{section_name}.{name} -> {raw_path}"
                        )

    return batch_id, included, included_syscalls


def check_steps_and_reviews(
    batch_dir: Path, batch_id: str | None, reporter: Reporter
) -> dict[str, str | None]:
    review_statuses: dict[str, str | None] = {}
    for step in STEPS:
        report_path = batch_dir / "steps" / f"{step}.md"
        review_path = batch_dir / "reviews" / f"{step}-signoff.yaml"

        if not report_path.exists():
            reporter.error(f"Missing step report: {report_path}")
        elif report_path.stat().st_size == 0:
            reporter.error(f"Empty step report: {report_path}")

        review_data = load_yaml(review_path, reporter)
        review = require_mapping(review_data, review_path, reporter) if review_data else None
        if review is None:
            review_statuses[step] = None
            reporter.gate(f"{step}: missing or malformed sign-off")
            continue

        for field in REVIEW_REQUIRED:
            if field not in review:
                reporter.error(f"{review_path} missing field: {field}")

        if batch_id and review.get("batch_id") != batch_id:
            reporter.error(f"{review_path} batch_id does not match manifest batch_id")
        if review.get("step_id") != step:
            reporter.error(f"{review_path} step_id should be {step}")
        expected_artifact = f"steps/{step}.md"
        if review.get("artifact") != expected_artifact:
            reporter.error(f"{review_path} artifact should be {expected_artifact}")

        status = review.get("status")
        if status not in REVIEW_STATUSES:
            reporter.error(f"{review_path} has invalid review status: {status!r}")
            review_statuses[step] = None
            reporter.gate(f"{step}: invalid sign-off status {status!r}")
        else:
            review_statuses[step] = status
            if status not in RESOLVED_REVIEW_STATUSES:
                reporter.gate(f"{step}: sign-off is {status}")

        if not isinstance(review.get("required_changes"), list):
            reporter.error(f"{review_path} required_changes must be a list")
        if not isinstance(review.get("follow_up"), list):
            reporter.error(f"{review_path} follow_up must be a list")

    return review_statuses


def check_coverage(
    batch_dir: Path,
    batch_id: str | None,
    included_behaviors: list[str],
    included_syscalls: list[str],
    reporter: Reporter,
) -> None:
    coverage_path = batch_dir / "outputs" / "coverage-matrix.yaml"
    data = load_yaml(coverage_path, reporter)
    matrix = require_mapping(data, coverage_path, reporter) if data else None
    if matrix is None:
        reporter.gate("coverage matrix is missing or malformed")
        return

    for key in ("batch_id", "generated_at_utc", "coverage"):
        if key not in matrix:
            reporter.error(f"{coverage_path} missing key: {key}")

    if batch_id and matrix.get("batch_id") != batch_id:
        reporter.error("coverage matrix batch_id does not match manifest batch_id")

    coverage = matrix.get("coverage")
    if not isinstance(coverage, list):
        reporter.error("coverage matrix coverage must be a list")
        reporter.gate("coverage matrix has no usable coverage list")
        return

    seen: list[str] = []
    seen_syscalls: list[str] = []
    for index, item in enumerate(coverage):
        label = f"coverage[{index}]"
        if not isinstance(item, dict):
            reporter.error(f"{label} must be a mapping")
            continue
        for field in COVERAGE_REQUIRED:
            if field not in item:
                reporter.error(f"{label} missing field: {field}")

        behavior_id = item.get("behavior_id")
        if isinstance(behavior_id, str):
            seen.append(behavior_id)
        else:
            reporter.error(f"{label}.behavior_id must be a string")

        syscall = item.get("syscall")
        if syscall is not None:
            if isinstance(syscall, str):
                seen_syscalls.append(syscall.lower())
            else:
                reporter.error(f"{label}.syscall must be a string when present")
        syscalls = item.get("syscalls")
        if syscalls is not None:
            if isinstance(syscalls, list) and all(isinstance(value, str) for value in syscalls):
                seen_syscalls.extend(value.lower() for value in syscalls)
            else:
                reporter.error(f"{label}.syscalls must be a list of strings when present")

        checkability = item.get("checkability")
        if checkability not in COVERAGE_CHECKABILITY:
            reporter.error(f"{label} has invalid checkability: {checkability!r}")

        triage = item.get("triage")
        if triage not in COVERAGE_TRIAGE:
            reporter.error(f"{label} has invalid triage: {triage!r}")

        source_refs = item.get("source_refs")
        if not isinstance(source_refs, list) or not source_refs:
            reporter.error(f"{label}.source_refs must be a non-empty list")

        evidence = item.get("starry_evidence")
        has_evidence = isinstance(evidence, list) and bool(evidence)
        if triage in {"covered", "covered_pending_human_review"} and not has_evidence:
            reporter.error(f"{label} is {triage} but has no Starry evidence")
        if not has_evidence and triage not in TRIAGE_WITHOUT_STARRY_EVIDENCE:
            reporter.error(f"{label} lacks Starry evidence and is not triaged as a gap/risk")

    if included_behaviors:
        scoped = set(included_behaviors)
        covered = set(seen)
        for behavior_id in sorted(scoped - covered):
            reporter.gate(f"Scoped behavior missing from coverage matrix: {behavior_id}")
        for behavior_id in sorted(covered - scoped):
            reporter.gate(f"Coverage behavior is not in manifest scope: {behavior_id}")
        duplicates = sorted({item for item in seen if seen.count(item) > 1})
        for behavior_id in duplicates:
            reporter.error(f"Duplicate coverage behavior: {behavior_id}")

    if included_syscalls:
        scoped_syscalls = set(included_syscalls)
        covered_syscalls = set(seen_syscalls)
        for syscall in sorted(scoped_syscalls - covered_syscalls):
            reporter.gate(f"Scoped syscall missing from coverage matrix: {syscall}")
        for syscall in sorted(covered_syscalls - scoped_syscalls):
            reporter.gate(f"Coverage syscall is not in manifest scope: {syscall}")
        duplicates = sorted({item for item in seen_syscalls if seen_syscalls.count(item) > 1})
        for syscall in duplicates:
            reporter.error(f"Duplicate coverage syscall: {syscall}")

    gaps = matrix.get("gaps", [])
    if gaps is None:
        return
    if not isinstance(gaps, list):
        reporter.error("coverage matrix gaps must be a list when present")
        return
    for index, gap in enumerate(gaps):
        label = f"gaps[{index}]"
        if not isinstance(gap, dict):
            reporter.error(f"{label} must be a mapping")
            continue
        if not gap.get("gap_id"):
            reporter.error(f"{label} missing gap_id")
        if gap.get("triage") not in COVERAGE_TRIAGE:
            reporter.error(f"{label} missing valid triage")


def print_report(batch_dir: Path, reporter: Reporter) -> None:
    print(f"Batch: {batch_dir}")
    if reporter.errors:
        print("\nERRORS")
        for message in reporter.errors:
            print(f"- {message}")
    if reporter.warnings:
        print("\nWARNINGS")
        for message in reporter.warnings:
            print(f"- {message}")
    if reporter.gates:
        print("\nREVIEW GATES")
        for message in reporter.gates:
            print(f"- {message}")

    print("\nSUMMARY")
    print(f"- structural_errors: {len(reporter.errors)}")
    print(f"- warnings: {len(reporter.warnings)}")
    print(f"- unresolved_review_gates: {len(reporter.gates)}")
    if reporter.errors:
        print("- result: invalid")
    elif reporter.gates:
        print("- result: structurally valid, not closeable")
    else:
        print("- result: closeout gates satisfied")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Check SyscallGuard batch structure, review gates, and coverage."
    )
    parser.add_argument("batch_dir", type=Path, help="Path such as batches/001-syscall-batch-ioctl-renameat2")
    args = parser.parse_args(argv)

    batch_dir = args.batch_dir
    reporter = Reporter()
    if not batch_dir.exists() or not batch_dir.is_dir():
        print(f"ERROR: batch directory not found: {batch_dir}", file=sys.stderr)
        return 2

    repo_root = find_repo_root(batch_dir.resolve())
    manifest_path = batch_dir / "manifest.yaml"
    manifest_data = load_yaml(manifest_path, reporter)
    manifest = require_mapping(manifest_data, manifest_path, reporter) if manifest_data else None

    batch_id: str | None = None
    included_behaviors: list[str] = []
    included_syscalls: list[str] = []
    if manifest is not None:
        batch_id, included_behaviors, included_syscalls = check_manifest(
            batch_dir, repo_root, manifest, reporter
        )

    check_steps_and_reviews(batch_dir, batch_id, reporter)
    check_coverage(batch_dir, batch_id, included_behaviors, included_syscalls, reporter)

    if manifest is not None and manifest.get("status") == "closed" and (
        reporter.errors or reporter.gates
    ):
        reporter.error("manifest status is closed but closeout gates are not satisfied")

    print_report(batch_dir, reporter)
    return 1 if reporter.errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
