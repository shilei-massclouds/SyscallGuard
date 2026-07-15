from __future__ import annotations

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from typing import Any

from syscallguard.adapters.ltp import LtpAdapter, _document_blocks, _struct_arrays
from syscallguard.common import atomic_write_yaml, content_hash
from syscallguard.ltp_audit import AUDIT_STATUSES, compare_syscall, run_audit


ROOT = Path(__file__).resolve().parents[1]
RULES = ROOT / "sources/adapters/ltp/recognition-rules.yaml"


class AdapterFixture(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.location = Path(self.temp.name) / "ltp"

    def tearDown(self) -> None:
        self.temp.cleanup()

    def extract(self, syscall: str, code: str) -> dict[str, Any]:
        source = (
            self.location
            / "testcases"
            / "kernel"
            / "syscalls"
            / syscall
            / f"{syscall}01.c"
        )
        source.parent.mkdir(parents=True, exist_ok=True)
        source.write_text(code, encoding="utf-8")
        adapter = LtpAdapter(self.location, RULES)
        item = adapter.prescan({"syscall": syscall, "directories": [syscall]})
        return adapter.extract(item)


class StructExtractionTests(AdapterFixture):
    def test_inline_separate_typedef_designated_and_access_forms(self) -> None:
        code = r"""
typedef struct { int fd; int exp_errno; } test_case_t;
static const test_case_t tests[] = {
    {.fd = -1, .exp_errno = EBADF},
    {.fd = 9, .exp_errno = EINVAL},
};
struct legacy_case { int fd; int exp_errno; };
static const struct legacy_case tdat[] = {{3, EACCES}};
static struct inline_case { int fd; int exp_errno; } tc[] = {{4, EPERM}};
void a(unsigned int n) { TST_EXP_FAIL(alpha(tests[n].fd), tests[n].exp_errno); }
void b(void) { TST_EXP_FAIL(alpha(tdat[0].fd), tdat[0].exp_errno); }
void c(unsigned int i) {
    struct inline_case *casep = &tc[i];
    TST_EXP_FAIL(alpha(casep->fd), casep->exp_errno);
}
"""
        arrays = _struct_arrays(code)
        self.assertEqual([array.name for array in arrays], ["tests", "tdat", "tc"])
        value = self.extract("alpha", code)
        self.assertFalse(
            [row for row in value["raw"] if row.get("evidence_class") == "unresolved"]
        )
        semantics = [row["semantics"] for row in value["normalized"]]
        self.assertEqual(len(semantics), 4)
        self.assertEqual(
            [(row["action"]["arguments"], row["expected_result"]["errno"]) for row in semantics],
            [(["-1"], "EBADF"), (["9"], "EINVAL"), (["3"], "EACCES"), (["4"], "EPERM")],
        )

    def test_expected_fields_require_assertion_and_input_fields_do_not(self) -> None:
        value = self.extract(
            "alpha",
            r"""
struct test_case_t { int fd; int flags; int expected_errno; };
static const struct test_case_t tests[] = {{-1, 0, EBADF}};
void run(unsigned int n) { helper(tests[n].fd, tests[n].flags); }
""",
        )
        unresolved = [
            row for row in value["raw"] if row.get("evidence_class") == "unresolved"
        ]
        self.assertEqual(len(unresolved), 1)
        self.assertEqual(unresolved[0]["struct"]["field"], "expected_errno")
        self.assertEqual(value["normalized"], [])

    def test_runtime_modification_and_complex_index_stay_unresolved(self) -> None:
        for code, reason in (
            (
                r"""
static struct test_case_t { int fd; int exp_errno; } tests[] = {{-1, EBADF}};
void setup(void) { tests[0].fd = bad_fd(); }
void run(unsigned int n) { TST_EXP_FAIL(alpha(tests[n].fd), tests[n].exp_errno); }
""",
                "runtime_modified_struct_field",
            ),
            (
                r"""
static const struct test_case_t { int fd; int exp_errno; } tests[] = {{-1, EBADF}};
void run(unsigned int n) { TST_EXP_FAIL(alpha(tests[n + 1].fd), tests[n + 1].exp_errno); }
""",
                "complex_struct_index",
            ),
        ):
            with self.subTest(reason=reason):
                value = self.extract("alpha", code)
                rows = [
                    row
                    for row in value["raw"]
                    if row.get("evidence_class") == "unresolved"
                    and row.get("recognizer_id") == "ltp.tst-exp.fail"
                ]
                self.assertEqual([row["resolution_reason"] for row in rows], [reason])
                self.assertEqual(value["normalized"], [])

    def test_legacy_result_comparisons_expand_expected_return_and_errno(self) -> None:
        value = self.extract(
            "alpha",
            r"""
struct test_case_t { int fd; int retval; int experrno; };
static const struct test_case_t tdat[] = {{-1, -1, EBADF}, {7, -1, EINVAL}};
void run(unsigned int testno) {
    TEST(alpha(tdat[testno].fd));
    if (TEST_RETURN != tdat[testno].retval ||
        TEST_ERRNO != tdat[testno].experrno) fail();
}
""",
        )
        self.assertEqual(len(value["normalized"]), 2)
        self.assertEqual(
            [row["semantics"]["expected_result"] for row in value["normalized"]],
            [
                {"kind": "return_errno", "return": "-1", "errno": "EBADF"},
                {"kind": "return_errno", "return": "-1", "errno": "EINVAL"},
            ],
        )

    def test_complex_legacy_field_condition_stays_unresolved(self) -> None:
        value = self.extract(
            "alpha",
            r"""
struct test_case_t { int fd; int experrno; };
static const struct test_case_t tests[] = {{-1, EBADF}};
void run(unsigned int n) {
    TEST(alpha(tests[n].fd));
    if (TST_ERR == tests[n].experrno || TST_ERR == EINVAL) fail();
}
""",
        )
        unresolved = [
            row for row in value["raw"] if row.get("evidence_class") == "unresolved"
        ]
        self.assertTrue(unresolved)
        self.assertEqual(value["normalized"], [])


class DocumentTests(AdapterFixture):
    def test_only_modern_document_block_is_context(self) -> None:
        code = r"""
// SPDX-License-Identifier: GPL-2.0
/* Copyright and history mentioning EOLD. */
/*
 * DESCRIPTION: alpha(2) used to fail with ELEGACY.
 */
/*\
 * Verify alpha(2) fails with EBADF.
 */
void run(void) { TST_EXP_FAIL(alpha(-1), EBADF); }
"""
        documents = _document_blocks(code)
        self.assertEqual(len(documents), 1)
        value = self.extract("alpha", code)
        context = [
            row
            for row in value["raw"]
            if row.get("recognizer_id") == "ltp.document.context"
        ]
        self.assertEqual(len(context), 1)
        self.assertEqual(context[0]["evidence_class"], "context")
        self.assertEqual(value["diagnostics"], [])
        self.assertEqual(_document_blocks("void x(void) {}\n/*\\ late */\n"), [])

    def test_document_conflicts_defer_to_code(self) -> None:
        value = self.extract(
            "alpha",
            r"""
/*\
 * Verify beta(2) succeeds and uses EINVAL.
 */
void run(void) { TST_EXP_FAIL(alpha(-1), EBADF); }
""",
        )
        kinds = {row["kind"] for row in value["diagnostics"]}
        self.assertEqual(
            kinds,
            {
                "document_syscall_conflict",
                "document_direction_conflict",
                "document_errno_conflict",
            },
        )
        self.assertEqual(value["normalized"][0]["semantics"]["expected_result"]["errno"], "EBADF")

    def test_document_free_text_does_not_change_rule_semantics(self) -> None:
        first = self.extract(
            "alpha",
            "/*\\ Verify alpha(2) fails with EBADF. */\n"
            "void run(void) { TST_EXP_FAIL(alpha(-1), EBADF); }\n",
        )
        second = self.extract(
            "alpha",
            "/*\\ A differently worded alpha(2) failure uses EBADF. */\n"
            "void run(void) { TST_EXP_FAIL(alpha(-1), EBADF); }\n",
        )
        self.assertNotEqual(
            first["raw"][0]["document"]["content_hash"],
            second["raw"][0]["document"]["content_hash"],
        )
        self.assertEqual(
            first["normalized"][0]["semantics"], second["normalized"][0]["semantics"]
        )


def normalized(
    syscall: str = "alpha",
    errno: str = "EBADF",
    line: int = 10,
    evidence_hash: str = "evidence",
) -> dict[str, Any]:
    semantics = {
        "preconditions": [],
        "action": {"operation": "invoke_syscall", "syscall": syscall, "arguments": [-1]},
        "expected_result": {"kind": "return_errno", "return": "-1", "errno": errno},
        "errno": [errno],
    }
    return {
        "syscall": syscall,
        "source": {"file": f"testcases/{syscall}.c", "line": line},
        "recognizer_id": "ltp.tst-exp.fail",
        "case": f"{syscall}_{line}_raw",
        "evidence_hash": evidence_hash,
        "category": "syscall_behavior",
        "semantics": semantics,
        "expansion": {},
    }


def raw(
    syscall: str = "alpha",
    line: int = 10,
    evidence_hash: str = "evidence",
    evidence_class: str | None = None,
) -> dict[str, Any]:
    row = {
        "syscall": syscall,
        "source": {"file": f"testcases/{syscall}.c", "line": line},
        "recognizer_id": "ltp.tst-exp.fail",
        "evidence_hash": evidence_hash,
    }
    if evidence_class:
        row["evidence_class"] = evidence_class
    return row


def published(errno: str = "EBADF", line: int = 10) -> dict[str, Any]:
    row = normalized(errno=errno, line=line)
    semantics = row["semantics"]
    return {
        "syscall": "alpha",
        "rule_id": "RULE",
        "semantic_hash": content_hash({"category": "syscall_behavior", "semantics": semantics}),
        "category": "syscall_behavior",
        "semantics": semantics,
        "preconditions": [],
        "arguments": [-1],
        "expected_result": semantics["expected_result"],
        "errno": [errno],
        "recognizer_id": "ltp.tst-exp.fail",
        "file": "testcases/alpha.c",
        "line": line,
        "case": f"alpha_{line}_raw",
        "case_index": None,
    }


class AuditComparisonTests(unittest.TestCase):
    def status(
        self,
        baseline: dict[str, Any],
        candidate: dict[str, Any],
        published_rows: list[dict[str, Any]] | None = None,
    ) -> list[str]:
        result = compare_syscall("alpha", baseline, candidate, published_rows or [])
        return [row["status"] for row in result["rules"]]

    def test_all_audit_statuses(self) -> None:
        scenarios = {
            "unchanged": (
                {"raw": [raw()], "normalized": [normalized()]},
                {"raw": [raw(evidence_class="authoritative")], "normalized": [normalized()]},
                [],
            ),
            "added": ({"raw": [], "normalized": []}, {"raw": [], "normalized": [normalized()]}, []),
            "removed": ({"raw": [], "normalized": [normalized()]}, {"raw": [], "normalized": []}, []),
            "changed": (
                {"raw": [], "normalized": [normalized(errno="EBADF")]},
                {"raw": [], "normalized": [normalized(errno="EINVAL")]},
                [],
            ),
            "resolved": (
                {"raw": [raw(evidence_hash="old")], "normalized": []},
                {"raw": [], "normalized": [normalized(evidence_hash="new")]},
                [],
            ),
            "regressed": (
                {"raw": [], "normalized": [normalized()]},
                {"raw": [raw(evidence_class="unresolved")], "normalized": []},
                [published()],
            ),
            "conflict": (
                {"raw": [], "normalized": [normalized()]},
                {"raw": [], "normalized": [normalized()]},
                [published(errno="EINVAL")],
            ),
        }
        self.assertEqual(set(scenarios), AUDIT_STATUSES)
        for expected, args in scenarios.items():
            with self.subTest(status=expected):
                self.assertIn(expected, self.status(*args))
        regressed = compare_syscall(
            "alpha",
            {"raw": [], "normalized": [normalized()]},
            {"raw": [raw(evidence_class="unresolved")], "normalized": []},
            [published()],
        )
        self.assertEqual(regressed["rules"][0]["status"], "regressed")
        self.assertEqual(regressed["rules"][0]["published"]["rule_id"], "RULE")
        conservative = compare_syscall(
            "alpha",
            {"raw": [], "normalized": [normalized()]},
            {"raw": [raw(evidence_class="unresolved")], "normalized": []},
            [],
        )
        self.assertEqual(conservative["rules"][0]["status"], "conflict")
        self.assertEqual(
            conservative["rules"][0]["diagnostic"]["kind"],
            "candidate_conservative_rejection",
        )


class AuditToolTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        base = Path(self.temp.name)
        self.root = base / "root"
        self.root.mkdir()
        rules = self.root / "sources/adapters/ltp/recognition-rules.yaml"
        rules.parent.mkdir(parents=True)
        shutil.copyfile(RULES, rules)
        self.source = base / "ltp"
        for syscall, errno in (("alpha", "EBADF"), ("beta", "EINVAL")):
            path = self.source / "testcases/kernel/syscalls" / syscall / f"{syscall}.c"
            path.parent.mkdir(parents=True)
            path.write_text(
                f"void run(void) {{ TST_EXP_FAIL({syscall}(), {errno}); }}\n",
                encoding="utf-8",
            )
        subprocess.run(["git", "init", "-q"], cwd=self.source, check=True)
        subprocess.run(["git", "add", "-A"], cwd=self.source, check=True)
        atomic_write_yaml(
            self.root / "sources/fixture.yaml",
            {
                "source_id": "fixture",
                "adapter": "ltp",
                "location": str(self.source),
                "revision": "HEAD",
            },
        )
        atomic_write_yaml(
            self.root / "sources/index.yaml",
            {
                "default_source": "fixture",
                "sources": {"fixture": "sources/fixture.yaml"},
            },
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_filter_preserves_full_counts_and_writes_only_tmp_report(self) -> None:
        before = sorted(
            (str(path.relative_to(self.root)), path.read_bytes())
            for path in self.root.rglob("*")
            if path.is_file()
        )
        audit_id, output, filtered = run_audit(
            root=self.root,
            syscalls="alpha",
            audit_id="audit-filtered",
            output_root=Path(self.temp.name) / "audit-output",
        )
        self.assertEqual(audit_id, "audit-filtered")
        self.assertTrue(output.is_file())
        self.assertEqual([row["syscall"] for row in filtered["syscalls"]], ["alpha"])
        self.assertEqual(filtered["scope"]["discovered_syscall_count"], 2)
        self.assertEqual(
            sum(filtered["full_counts"].values()),
            2,
        )
        after = sorted(
            (str(path.relative_to(self.root)), path.read_bytes())
            for path in self.root.rglob("*")
            if path.is_file()
        )
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
