from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

from .common import SyscallGuardError, repo_root


def reset_project(root: Path | None = None) -> dict[str, Any]:
    """Reset only the target-independent ingestion state to an empty baseline."""
    root = (root or repo_root()).resolve()
    if not (root / "sources").is_dir() or not (root / "syscallguard").is_dir():
        raise SyscallGuardError(f"not a SyscallGuard repository: {root}")

    rule_paths = sorted((root / "library" / "rules").glob("*.yaml"))
    report_paths = sorted((root / "runs").glob("spec-*/report.md"))
    removed_rules: list[str] = []
    removed_reports: list[str] = []

    for path in rule_paths:
        if path.is_file() or path.is_symlink():
            path.unlink()
            removed_rules.append(str(path.relative_to(root)))
    for path in report_paths:
        if path.is_file() or path.is_symlink():
            path.unlink()
            removed_reports.append(str(path.relative_to(root)))
        try:
            path.parent.rmdir()
        except OSError:
            pass
    return {
        "removed_rule_count": len(removed_rules),
        "removed_report_count": len(removed_reports),
        "removed_rules": removed_rules,
        "removed_reports": removed_reports,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Reset SyscallGuard rule ingestion to an empty baseline"
    )
    parser.add_argument("--root", type=Path, default=repo_root(), help=argparse.SUPPRESS)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        result = reset_project(args.root)
    except SyscallGuardError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(f"rules_removed: {result['removed_rule_count']}")
    print(f"ingest_reports_removed: {result['removed_report_count']}")
    print(f"rule_library: {args.root.resolve() / 'library/rules'}")
    print(f"report_root: {args.root.resolve() / 'runs'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
