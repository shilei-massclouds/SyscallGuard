#!/usr/bin/env python3
"""Read-only progress reporter for SyscallGuard ten-step batches."""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - environment failure path
    yaml = None


@dataclass(frozen=True)
class StepMetadata:
    step_id: str
    summary: str


STEP_METADATA = [
    StepMetadata(
        "01-scope-selection",
        "范围选择：确定本批次 syscall、优先级和排除项。",
    ),
    StepMetadata(
        "02-spec-ingestion",
        "规范导入：记录规格来源、版本、路径和缺失资料。",
    ),
    StepMetadata(
        "03-normalization-review",
        "规范化审查：整理 syscall、复用规则和目标映射。",
    ),
    StepMetadata(
        "04-checkability-classification",
        "可检查性分类：标记 static、partial_static、dynamic 等类型。",
    ),
    StepMetadata(
        "05-starry-evidence-mapping",
        "Starry 证据映射：定位实现、测试、日志或证据缺口。",
    ),
    StepMetadata(
        "06-static-check-or-audit",
        "静态检查或审计：执行静态规则并记录人工审计结果。",
    ),
    StepMetadata(
        "07-gap-triage",
        "缺口分诊：判断 gap、risk、needs_review 及阻塞性。",
    ),
    StepMetadata(
        "08-fix-plan-and-apply-outside-harness",
        "动态验证计划：生成可执行验证用例并记录环境阻塞。",
    ),
    StepMetadata(
        "09-validation",
        "验证与补丁候选：执行用例并生成 Starry 补丁候选。",
    ),
    StepMetadata(
        "10-batch-closeout",
        "应用与收尾：应用已批准补丁、回归验证并完成批次关闭。",
    ),
]

STEPS = [metadata.step_id for metadata in STEP_METADATA]

RESOLVED_REVIEW_STATUSES = {"confirmed", "not_applicable"}
UNRESOLVED_REVIEW_STATUSES = {"pending_human_review", "changes_requested"}
KNOWN_REVIEW_STATUSES = RESOLVED_REVIEW_STATUSES | UNRESOLVED_REVIEW_STATUSES


@dataclass
class StepState:
    number: int
    step_id: str
    report_path: Path
    review_path: Path
    report_state: str
    signoff_state: str
    gate_state: str

    @property
    def is_resolved(self) -> bool:
        return self.report_state == "present" and self.signoff_state in RESOLVED_REVIEW_STATUSES

    @property
    def has_unresolved_gate(self) -> bool:
        return self.signoff_state in UNRESOLVED_REVIEW_STATUSES

    @property
    def has_bad_gate(self) -> bool:
        return self.signoff_state in {
            "missing",
            "malformed",
            "invalid_status",
        } or self.signoff_state.endswith("(step_id_mismatch)")


def load_yaml(path: Path) -> tuple[Any, str | None]:
    if yaml is None:
        return None, "PyYAML is required: python3 -m pip install PyYAML"
    if not path.exists():
        return None, "missing"
    try:
        with path.open("r", encoding="utf-8") as handle:
            return yaml.safe_load(handle), None
    except yaml.YAMLError as exc:
        return None, f"malformed: {exc}"
    except OSError as exc:
        return None, f"cannot_read: {exc}"


def read_mapping(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    data, error = load_yaml(path)
    if error is not None:
        return None, error
    if not isinstance(data, dict):
        return None, "malformed"
    return data, None


def report_state(path: Path) -> str:
    if not path.exists():
        return "missing"
    try:
        if path.stat().st_size == 0:
            return "empty"
    except OSError:
        return "unreadable"
    return "present"


def signoff_state(path: Path, expected_step: str) -> str:
    data, error = read_mapping(path)
    if error is not None:
        if error == "missing":
            return "missing"
        return "malformed"

    status = data.get("status")
    step_id = data.get("step_id")
    if status not in KNOWN_REVIEW_STATUSES:
        return "invalid_status"
    if step_id is not None and step_id != expected_step:
        return f"{status} (step_id_mismatch)"
    return str(status)


def gate_state(report: str, signoff: str) -> str:
    if report != "present":
        return "needs_work"
    if signoff in RESOLVED_REVIEW_STATUSES:
        return "resolved"
    if signoff in UNRESOLVED_REVIEW_STATUSES:
        return "blocked"
    return "needs_review_file"


def collect_steps(batch_dir: Path) -> list[StepState]:
    states: list[StepState] = []
    for index, metadata in enumerate(STEP_METADATA, start=1):
        step_id = metadata.step_id
        report_path = batch_dir / "steps" / f"{step_id}.md"
        review_path = batch_dir / "reviews" / f"{step_id}-signoff.yaml"
        report = report_state(report_path)
        signoff = signoff_state(review_path, step_id)
        states.append(
            StepState(
                number=index,
                step_id=step_id,
                report_path=report_path,
                review_path=review_path,
                report_state=report,
                signoff_state=signoff,
                gate_state=gate_state(report, signoff),
            )
        )
    return states


def manifest_summary(batch_dir: Path) -> tuple[str, list[str]]:
    manifest_path = batch_dir / "manifest.yaml"
    manifest, error = read_mapping(manifest_path)
    if error is not None:
        return f"manifest=missing_or_malformed ({error})", []

    batch_id = manifest.get("batch_id", "<unknown>")
    status = manifest.get("status", "<unknown>")
    workflow = manifest.get("workflow")
    notes: list[str] = []
    if isinstance(workflow, list):
        workflow_ids = [item.get("step_id") if isinstance(item, dict) else None for item in workflow]
        if workflow_ids != STEPS:
            notes.append("workflow_order_mismatch")
    else:
        notes.append("workflow_missing_or_malformed")

    scope = manifest.get("scope")
    scoped_count = 0
    if isinstance(scope, dict):
        included_behaviors = scope.get("included_behaviors")
        included_syscalls = scope.get("included_syscalls")
        if isinstance(included_behaviors, list):
            scoped_count = len(included_behaviors)
        elif isinstance(included_syscalls, list):
            scoped_count = len(included_syscalls)
    return f"batch_id={batch_id} status={status} scoped_items={scoped_count}", notes


def coverage_summary(batch_dir: Path) -> tuple[str, list[str]]:
    coverage_path = batch_dir / "outputs" / "coverage-matrix.yaml"
    matrix, error = read_mapping(coverage_path)
    if error is not None:
        return f"coverage=missing_or_malformed ({error})", []

    rows = matrix.get("coverage")
    if not isinstance(rows, list):
        return "coverage=malformed coverage list", []

    review_statuses: Counter[str] = Counter()
    triage: Counter[str] = Counter()
    for row in rows:
        if not isinstance(row, dict):
            review_statuses["malformed_row"] += 1
            continue
        review_statuses[str(row.get("review_status", "<missing>"))] += 1
        triage[str(row.get("triage", "<missing>"))] += 1

    review_text = ", ".join(f"{key}:{value}" for key, value in sorted(review_statuses.items()))
    triage_text = ", ".join(f"{key}:{value}" for key, value in sorted(triage.items()))
    return f"coverage_rows={len(rows)} review_status=[{review_text}] triage=[{triage_text}]", []


def first_current_step(states: list[StepState]) -> StepState | None:
    for state in states:
        if not state.is_resolved:
            return state
    return None


def first_blocking_gate(states: list[StepState]) -> StepState | None:
    current = first_current_step(states)
    if current is None:
        return None
    if current.has_unresolved_gate:
        return current
    if current.has_bad_gate and (current.report_state == "present" or current.review_path.exists()):
        return current
    return None


def next_executable_step(states: list[StepState]) -> StepState | None:
    for state in states:
        previous = states[: state.number - 1]
        if all(item.is_resolved for item in previous) and not state.is_resolved:
            if state.report_state != "present" and state.signoff_state == "missing":
                return state
            if state.gate_state == "needs_work":
                return state
            return None
    return None


def print_table(states: list[StepState]) -> None:
    print("步骤进度")
    print("#  step_id                                      report    sign-off                 gate")
    for state in states:
        print(
            f"{state.number:02d} {state.step_id:<44} "
            f"{state.report_state:<9} {state.signoff_state:<24} {state.gate_state}"
        )


def print_step_summaries() -> None:
    print("十步简述")
    for number, metadata in enumerate(STEP_METADATA, start=1):
        print(f"{number}. {metadata.summary}")


def print_report(batch_dir: Path, states: list[StepState]) -> None:
    manifest_text, manifest_notes = manifest_summary(batch_dir)
    coverage_text, coverage_notes = coverage_summary(batch_dir)
    current = first_current_step(states)
    blocking = first_blocking_gate(states)
    executable = next_executable_step(states)

    print_step_summaries()
    print()
    print(f"Batch: {batch_dir}")
    print(f"Manifest: {manifest_text}")
    for note in manifest_notes:
        print(f"Manifest note: {note}")
    print(f"Coverage: {coverage_text}")
    for note in coverage_notes:
        print(f"Coverage note: {note}")
    print()
    print_table(states)
    print()

    if current is None:
        print("当前步骤: 全部十步 sign-off 已解决")
    else:
        print(f"当前步骤: 第{current.number}步 {current.step_id} ({current.gate_state})")

    if blocking is None:
        print("阻塞 review gate: 无")
    else:
        print(
            "阻塞 review gate: "
            f"第{blocking.number}步 {blocking.step_id} "
            f"{blocking.signoff_state} -> {blocking.review_path}"
        )

    if executable is None:
        print("下一可执行步骤: 无")
    else:
        print(f"下一可执行步骤: 第{executable.number}步 {executable.step_id}")

    if blocking is not None:
        print(
            "下一条建议输入: 命令：批准进入下一步，或先处理 "
            f"{blocking.review_path}"
        )
    elif executable is not None:
        print(f"下一条建议输入: 命令：执行第{executable.number}步")
    else:
        print("下一条建议输入: 无（批次十步均已完成）")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Read-only progress report for a SyscallGuard batch."
    )
    parser.add_argument(
        "--batch",
        type=Path,
        required=True,
        help="Path such as batches/001-syscall-batch-ioctl-renameat2",
    )
    args = parser.parse_args(argv)

    batch_dir = args.batch
    if not batch_dir.exists() or not batch_dir.is_dir():
        print(f"ERROR: batch directory not found: {batch_dir}", file=sys.stderr)
        return 2
    if yaml is None:
        print("ERROR: PyYAML is required: python3 -m pip install PyYAML", file=sys.stderr)
        return 2

    states = collect_steps(batch_dir)
    print_report(batch_dir, states)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
