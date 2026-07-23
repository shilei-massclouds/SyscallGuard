#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from syscallguard.common import SyscallGuardError
from syscallguard.man_static import (
    materialize_man_static_checks,
    publish_man_static_checks,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate or publish curated man-pages Starry static checks"
    )
    parser.add_argument("--branch", help="clean user-created Starry branch")
    parser.add_argument("--run-id", help="requested mapping run ID")
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    try:
        checks, rule_to_checks = materialize_man_static_checks(ROOT)
        man_rules = [rule_id for rule_id in rule_to_checks if rule_id.startswith("MAN_")]
        if args.validate_only:
            print(f"checks={len(checks)} man_rules={len(man_rules)}")
            return 0
        if not args.branch:
            parser.error("--branch is required unless --validate-only is used")
        run_id = publish_man_static_checks(args.branch, ROOT, args.run_id)
        print(run_id)
        return 0
    except SyscallGuardError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
