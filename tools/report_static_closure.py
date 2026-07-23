#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from syscallguard.common import SyscallGuardError
from syscallguard.man_static import materialize_man_static_checks
from syscallguard.static_closure import publish_static_closure


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Publish Manual static-closure increments from two mapping reports"
    )
    parser.add_argument("--baseline", required=True)
    parser.add_argument("--final", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--fix-run", action="append", default=[])
    args = parser.parse_args()
    try:
        _checks, rule_to_checks = materialize_man_static_checks(ROOT)
        candidates = {
            rule_id for rule_id in rule_to_checks if rule_id.startswith("MAN_")
        }
        run_id = publish_static_closure(
            args.baseline,
            args.final,
            candidates,
            args.fix_run,
            root=ROOT,
            requested_run_id=args.run_id,
        )
        print(run_id)
        return 0
    except SyscallGuardError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
