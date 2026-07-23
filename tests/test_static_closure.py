from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path

import yaml

from syscallguard.checking import _apply_test_patches, _extend_revalidation_scope
from syscallguard.common import SyscallGuardError
from syscallguard.static_closure import (
    collect_fixed_findings,
    compute_mapping_delta,
)


def version(entity_id: str, content_hash: str) -> dict[str, str]:
    return {
        "id": entity_id,
        "generated_at_utc": "2026-07-17T00:00:00Z",
        "content_hash": content_hash,
    }


def row(
    status: str,
    checks: list[str],
    hashes: dict[str, str],
    *,
    dynamic: list[str] | None = None,
) -> dict[str, object]:
    return {
        "status": status,
        "static_check_refs": checks,
        "dynamic_test_refs": dynamic or [],
        "entity_versions": {
            "static_checks": {
                check_id: version(check_id, hashes[check_id]) for check_id in checks
            },
            "dynamic_tests": {},
        },
    }


class StaticClosureDeltaTests(unittest.TestCase):
    def reports(self) -> tuple[dict[str, object], dict[str, object]]:
        baseline = {
            "rules": {
                "MAN_A": row("covered", ["CHECK_OLD"], {"CHECK_OLD": "old"}),
                "MAN_B": row("needs_review", [], {}),
                "MAN_INACTIVE": row(
                    "covered", ["CHECK_INACTIVE"], {"CHECK_INACTIVE": "inactive"}
                ),
            },
            "rule_syscalls": {
                "MAN_A": ["alpha"],
                "MAN_B": ["beta"],
                "MAN_INACTIVE": ["retired"],
            },
        }
        final = {
            "rules": {
                "MAN_A": row("covered", ["CHECK_OLD"], {"CHECK_OLD": "updated"}),
                "MAN_B": row(
                    "covered",
                    ["CHECK_EXISTING", "CHECK_NEW", "CHECK_OLD", "CHECK_REUSE"],
                    {
                        "CHECK_EXISTING": "now-referenced",
                        "CHECK_NEW": "new",
                        "CHECK_OLD": "updated",
                        "CHECK_REUSE": "same",
                    },
                ),
                "MAN_INACTIVE": row(
                    "covered", ["CHECK_INACTIVE"], {"CHECK_INACTIVE": "inactive"}
                ),
            },
            "rule_syscalls": {
                "MAN_A": ["alpha"],
                "MAN_B": ["beta"],
                "MAN_INACTIVE": ["retired"],
            },
        }
        baseline["rules"]["MAN_A"]["static_check_refs"].append("CHECK_REUSE")
        baseline["rules"]["MAN_A"]["entity_versions"]["static_checks"][
            "CHECK_REUSE"
        ] = version("CHECK_REUSE", "same")
        final["rules"]["MAN_A"]["static_check_refs"].append("CHECK_REUSE")
        final["rules"]["MAN_A"]["entity_versions"]["static_checks"][
            "CHECK_REUSE"
        ] = version("CHECK_REUSE", "same")
        return baseline, final

    def test_active_baseline_and_incremental_sets(self) -> None:
        baseline, final = self.reports()
        delta = compute_mapping_delta(
            baseline,
            final,
            active_rule_ids={"MAN_A", "MAN_B"},
            candidate_rule_ids={"MAN_A", "MAN_B"},
            final_check_ids={
                "CHECK_EXISTING",
                "CHECK_NEW",
                "CHECK_OLD",
                "CHECK_REUSE",
                "CHECK_UNRELATED",
            },
            baseline_check_ids={"CHECK_OLD", "CHECK_REUSE", "CHECK_EXISTING"},
        )

        self.assertEqual(
            delta["new_static_candidate_rules"]["rule_ids"], ["MAN_B"]
        )
        self.assertEqual(
            delta["newly_mapped_manual_rules"]["rule_ids"], ["MAN_B"]
        )
        self.assertEqual(delta["new_rule_check_edges"]["count"], 4)
        checks = delta["new_static_check_entities"]
        self.assertEqual(checks["check_ids"], ["CHECK_NEW"])
        self.assertEqual(
            checks["updated_check_ids"], ["CHECK_EXISTING", "CHECK_OLD"]
        )
        self.assertEqual(checks["reused_check_ids"], ["CHECK_REUSE"])

    def test_empty_incremental_rerun(self) -> None:
        _baseline, final = self.reports()
        delta = compute_mapping_delta(
            final,
            final,
            active_rule_ids={"MAN_A", "MAN_B"},
            candidate_rule_ids={"MAN_A", "MAN_B"},
            final_check_ids={
                "CHECK_EXISTING",
                "CHECK_NEW",
                "CHECK_OLD",
                "CHECK_REUSE",
            },
        )
        self.assertEqual(delta["new_static_candidate_rules"]["count"], 0)
        self.assertEqual(delta["newly_mapped_manual_rules"]["count"], 0)
        self.assertEqual(delta["new_rule_check_edges"]["count"], 0)
        self.assertEqual(delta["new_static_check_entities"]["count"], 0)

    def test_unmapped_active_candidate_is_rejected(self) -> None:
        baseline, final = self.reports()
        final["rules"]["MAN_B"] = row("needs_review", [], {})

        with self.assertRaisesRegex(
            SyscallGuardError, "does not cover every active Manual static candidate"
        ):
            compute_mapping_delta(
                baseline,
                final,
                active_rule_ids={"MAN_A", "MAN_B"},
                candidate_rule_ids={"MAN_A", "MAN_B"},
                final_check_ids={"CHECK_OLD", "CHECK_REUSE"},
            )


class StaticClosureFindingTests(unittest.TestCase):
    def write_yaml(self, path: Path, value: object) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")

    def test_fixed_findings_are_deduplicated_and_source_split(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            run_id = "fix-current"
            self.write_yaml(
                root / "runs" / run_id / "manifest.yaml",
                {
                    "kind": "syscallguard_run",
                    "stage": "fix",
                    "status": "completed",
                    "entities": {"findings": ["finding-man", "finding-ltp"]},
                },
            )
            self.write_yaml(
                root / "runs" / run_id / "regression-results.yaml",
                {
                    "static": [{"result": "pass"}],
                    "dynamic": [{"result": "skipped"}],
                    "blockers": [],
                },
            )
            for finding_id, rule_id, syscall in (
                ("finding-man", "MAN_A", "alpha"),
                ("finding-ltp", "LTP_B", "beta"),
            ):
                self.write_yaml(
                    root / "targets/starry/findings" / f"{finding_id}.yaml",
                    {
                        "finding_id": finding_id,
                        "status": "confirmed",
                        "resolution": "fixed",
                        "fixed_by_run": run_id,
                        "rule_id": rule_id,
                        "syscall": syscall,
                    },
                )

            result = collect_fixed_findings(
                root,
                [run_id, run_id],
                active_rule_ids={"MAN_A", "LTP_B"},
                baseline_fixed_finding_ids=set(),
            )
            self.assertEqual(result["count"], 2)
            self.assertEqual(result["fix_run_count"], 1)
            self.assertEqual(result["source_split"]["manual"], 1)
            self.assertEqual(result["source_split"]["ltp"], 1)

            excluded = collect_fixed_findings(
                root,
                [run_id],
                active_rule_ids={"MAN_A", "LTP_B"},
                baseline_fixed_finding_ids={"finding-man"},
            )
            self.assertEqual(excluded["finding_ids"], ["finding-ltp"])


class ExistingDynamicSourceTests(unittest.TestCase):
    def test_static_only_revalidation_does_not_load_dynamic_evidence(self) -> None:
        entities = {
            "rules": {},
            "static_checks": {},
            "dynamic_tests": {},
        }
        finding = {
            "target_snapshot_hash": "old",
            "occurrences": [
                {"evidence_kind": "dynamic", "source_id": "DYNAMIC_OLD"}
            ],
        }

        added, unresolved = _extend_revalidation_scope(
            Path("/does/not/need/to/exist"),
            entities,
            {"finding-old": finding},
            "current",
            "branch",
            allowed_evidence_kinds={"static"},
        )

        self.assertEqual(added["dynamic_tests"], [])
        self.assertEqual(unresolved, {})
        self.assertEqual(entities["dynamic_tests"], {})

    def test_superseding_test_source_satisfies_patch_injection(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "guard"
            worktree = Path(directory) / "starry"
            logs = Path(directory) / "logs"
            root.mkdir()
            worktree.mkdir()
            subprocess.run(["git", "init"], cwd=worktree, check=True, capture_output=True)
            source = worktree / "tests/source.c"
            source.parent.mkdir()
            source.write_text("new upstream test\n", encoding="utf-8")
            patch = root / "test.patch"
            patch.write_text(
                "diff --git a/tests/source.c b/tests/source.c\n"
                "new file mode 100644\n"
                "--- /dev/null\n"
                "+++ b/tests/source.c\n"
                "@@ -0,0 +1 @@\n"
                "+old injected test\n",
                encoding="utf-8",
            )
            tests = {
                "TEST": {
                    "patch_file": "test.patch",
                    "test_source": "tests/source.c",
                }
            }

            blocked, blockers, applied = _apply_test_patches(
                root, worktree, tests, logs
            )
            self.assertEqual(blocked, set())
            self.assertEqual(blockers, [])
            self.assertEqual(applied, set())
            self.assertIn(
                "all selected test sources are already present",
                (logs / "patch-test-patch.log").read_text(encoding="utf-8"),
            )


if __name__ == "__main__":
    unittest.main()
