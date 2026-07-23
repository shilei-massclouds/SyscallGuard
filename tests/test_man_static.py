from __future__ import annotations

import unittest
from pathlib import Path

from syscallguard.man_static import materialize_man_static_checks


class ManStaticCatalogTests(unittest.TestCase):
    def test_catalog_resolves_active_man_rules_and_executable_checks(self) -> None:
        root = Path(__file__).resolve().parents[1]
        checks, rule_to_checks = materialize_man_static_checks(root)
        man_rules = {
            rule_id for rule_id in rule_to_checks if rule_id.startswith("MAN_")
        }

        self.assertEqual(len(man_rules), 106)
        self.assertEqual(len(checks), 60)
        self.assertIn("STARRY_MAN_SECCOMP_VALIDATION", checks)
        self.assertIn("MAN_58936D050A8879DE", rule_to_checks)
        self.assertTrue(
            all(
                check.get("patterns") and check.get("path")
                for check in checks.values()
            )
        )


if __name__ == "__main__":
    unittest.main()
