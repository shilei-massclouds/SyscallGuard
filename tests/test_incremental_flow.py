from __future__ import annotations

import io
import shutil
import subprocess
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path
from typing import Any
from unittest import mock

import yaml

from syscallguard.checking import (
    TEMP_ROOT as CHECK_TEMP_ROOT,
    load_check_report,
    run_check,
)
from syscallguard.common import (
    SyscallGuardError,
    atomic_write_text,
    atomic_write_yaml,
    content_hash,
    entity_version,
    load_mapping,
    new_run_id,
    normalize_run_id,
    read_frontmatter,
    slug,
    update_index,
    version_content_hash,
)
from syscallguard.fixing import (
    FIX_TEMP_ROOT,
    build_parser as build_fix_parser,
    finalize_fix,
    prepare_fix,
    run_fix,
)
from syscallguard.ingest import (
    build_parser as build_ingest_parser,
    resolve_count,
    resolve_source,
    resolve_syscalls,
    run_ingest,
)
from syscallguard.mapping import (
    TEMP_ROOT,
    build_parser as build_mapping_parser,
    finalize_mapping,
    load_mapping_report,
    prepare_mapping,
    resolve_syscalls as resolve_mapping_syscalls,
    run_mapping,
)
from syscallguard.reset import reset_project
from tools import validate_repository


def command(args: list[str], cwd: Path) -> str:
    result = subprocess.run(args, cwd=cwd, check=True, capture_output=True, text=True)
    return result.stdout.strip()


def init_repo(path: Path, files: dict[str, str]) -> str:
    path.mkdir(parents=True)
    command(["git", "init", "-q"], path)
    command(["git", "config", "user.name", "Test"], path)
    command(["git", "config", "user.email", "test@example.invalid"], path)
    for relative, text in files.items():
        destination = path / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text, encoding="utf-8")
    command(["git", "add", "-A"], path)
    command(["git", "commit", "-q", "-m", "initial"], path)
    return command(["git", "rev-parse", "HEAD"], path)


def commit_file(repo: Path, relative: str, text: str, message: str = "change") -> str:
    path = repo / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    command(["git", "add", relative], repo)
    command(["git", "commit", "-q", "-m", message], repo)
    return command(["git", "rev-parse", "HEAD"], repo)


def markdown_report(frontmatter: dict[str, Any]) -> str:
    return (
        "---\n"
        + yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True)
        + "---\n\n# Test ingest report\n"
    )


def write_ingest_report(
    root: Path,
    report_id: str,
    rows: list[dict[str, Any]],
    generated_at: str = "2026-01-01T00:00:00.000000Z",
    source_id: str = "fixture-ltp",
) -> None:
    frontmatter = {
        "schema_version": 1,
        "kind": "syscallguard_ingest_report",
        "report_id": report_id,
        "generated_at_utc": generated_at,
        "source": {
            "id": source_id,
            "type": "ltp",
            "snapshot_hash": "sha256:fixture-source-snapshot",
            "descriptor_hash": "sha256:fixture-descriptor",
            "recognition_rules_hash": "sha256:fixture-recognizers",
            "resolution": "explicit_descriptor",
        },
        "count": {"value": str(len(rows)), "source": "command"},
        "pending_count": len(rows),
        "selected_syscalls": [row["syscall"] for row in rows],
        "syscalls": rows,
    }
    atomic_write_text(root / "runs" / report_id / "report.md", markdown_report(frontmatter))


def report(root: Path, report_id: str) -> dict[str, Any]:
    value, _body = read_frontmatter(root / "runs" / report_id / "report.md")
    return value


def target_branch(root: Path) -> str:
    descriptor = load_mapping(root / "targets/starry/target.yaml")
    return command(
        ["git", "branch", "--show-current"], Path(descriptor["repository"])
    )


class FlowTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "syscallguard"
        self.root.mkdir()
        rules_source = (
            Path(__file__).resolve().parents[1]
            / "sources/adapters/ltp/recognition-rules.yaml"
        )
        rules_target = self.root / "sources/adapters/ltp/recognition-rules.yaml"
        rules_target.parent.mkdir(parents=True)
        rules_target.write_text(rules_source.read_text(encoding="utf-8"), encoding="utf-8")

    def tearDown(self) -> None:
        if TEMP_ROOT.is_dir():
            for workspace in TEMP_ROOT.iterdir():
                preparation = workspace / "preparation.yaml"
                try:
                    value = load_mapping(preparation)
                except SyscallGuardError:
                    continue
                if value.get("root") == str(self.root.resolve()):
                    shutil.rmtree(workspace)
        for path in (self.root / "runs").glob("check-*/report.md"):
            try:
                value = load_check_report(self.root, path.parent.name)
            except SyscallGuardError:
                continue
            diagnostic = value.get("diagnostic_directory")
            if isinstance(diagnostic, str):
                shutil.rmtree(diagnostic, ignore_errors=True)
        for report_id in (
            "check-stale",
            "check-manual-stale",
            "check-publish-failure",
            "check-wrong-branch",
        ):
            shutil.rmtree(CHECK_TEMP_ROOT / report_id, ignore_errors=True)
        for workspace in FIX_TEMP_ROOT.glob("*"):
            preparation = workspace / "preparation.yaml"
            try:
                value = load_mapping(preparation)
            except SyscallGuardError:
                continue
            if value.get("root") == str(self.root.resolve()):
                shutil.rmtree(workspace, ignore_errors=True)
        self.temp.cleanup()

    def update_executable_index(
        self,
        section: str,
        index_kind: str,
        id_field: str,
        entity_id: str,
        path: Path,
        rule_refs: list[str],
        syscalls: list[str] | None = None,
    ) -> None:
        index_path = self.root / "targets/starry" / f"{section}.yaml"
        if index_path.is_file():
            index = load_mapping(index_path)
        else:
            index = {
                "schema_version": 1,
                "kind": index_kind,
                "updated_at_utc": None,
                "syscalls": {},
            }
        row = {
            id_field: entity_id,
            "path": str(path.relative_to(self.root)),
            "rule_refs": rule_refs,
        }
        for syscall in syscalls or ["alpha"]:
            rows = [
                item
                for item in index["syscalls"].get(syscall, [])
                if item.get(id_field) != entity_id
            ]
            rows.append(row)
            index["syscalls"][syscall] = sorted(rows, key=lambda item: item[id_field])
        atomic_write_yaml(index_path, index)

    def make_ltp(self) -> tuple[Path, Path]:
        source = Path(self.temp.name) / "ltp"
        init_repo(
            source,
            {
                "testcases/kernel/syscalls/alpha/alpha01.c": (
                    "void run(void) { TST_EXP_FAIL(alpha(), EBADF); }\n"
                ),
                "testcases/kernel/syscalls/beta/beta01.c": (
                    "void run(void) { TST_EXP_FAIL(beta(), EINVAL); }\n"
                ),
            },
        )
        descriptor = self.root / "sources/fixture.yaml"
        atomic_write_yaml(
            descriptor,
            {
                "source_id": "fixture-ltp",
                "adapter": "ltp",
                "location": str(source),
                "revision": "HEAD",
            },
        )
        atomic_write_yaml(
            self.root / "sources/index.yaml",
            {
                "schema_version": 1,
                "kind": "syscallguard_source_index",
                "default_source": "fixture",
                "sources": {"fixture": "sources/fixture.yaml"},
            },
        )
        return source, descriptor

    def make_target(self, code: str = "bad\n") -> tuple[Path, Path, str]:
        repo = Path(self.temp.name) / "starry"
        commit = init_repo(repo, {"code.txt": code})
        descriptor = self.root / "targets/starry/target.yaml"
        atomic_write_yaml(
            descriptor,
            {
                "target_id": "starry",
                "repository": str(repo),
            },
        )
        return repo, descriptor, commit

    def prepare_spec_run(self) -> None:
        rule = {
            "schema_version": 1,
            "kind": "syscallguard_rule",
            "rule_id": "RULE_ONE",
            "category": "fixture",
            "semantics": {
                "preconditions": [],
                "action": {"operation": "read code"},
                "expected_result": "good",
                "errno": [],
            },
            "semantic_hash": "",
            "generated_at_utc": "2026-01-01T00:00:00.000000Z",
            "sources": [],
        }
        rule["semantic_hash"] = content_hash(
            {"category": rule["category"], "semantics": rule["semantics"]}
        )
        atomic_write_yaml(self.root / "library/rules/rule-one.yaml", rule)
        atomic_write_yaml(
            self.root / "library/syscalls.yaml",
            {
                "schema_version": 1,
                "kind": "syscallguard_syscall_index",
                "syscalls": {
                    "alpha": [
                        {
                            "rule_id": "RULE_ONE",
                            "path": "library/rules/rule-one.yaml",
                        }
                    ]
                },
            },
        )
        write_ingest_report(
            self.root,
            "spec-fixture",
            [
                {
                    "syscall": "alpha",
                    "source_fingerprint": "sha256:source-alpha",
                    "recognition_fingerprint": "sha256:recognition-alpha",
                    "selection_reason": "new",
                    "result": "formed_rules",
                    "rules": [entity_version("RULE_ONE", rule)],
                    "evidence_count": 1,
                    "unresolved_evidence_count": 0,
                    "reason": "all_evidence_resolved",
                }
            ],
        )

    def add_static_check(
        self, regex: str = "good", applies_to: list[str] | None = None
    ) -> None:
        entity = {
            "schema_version": 1,
            "kind": "syscallguard_starry_static_check",
            "check_id": "CHECK_ONE",
            "rule_refs": ["RULE_ONE"],
            "applies_to_syscalls": applies_to if applies_to is not None else ["alpha"],
            "path": "code.txt",
            "patterns": [{"label": "expected", "regex": regex}],
        }
        atomic_write_yaml(self.root / "targets/starry/static-checks/check-one.yaml", entity)
        self.update_executable_index(
            "static-checks",
            "syscallguard_starry_static_check_index",
            "check_id",
            "CHECK_ONE",
            self.root / "targets/starry/static-checks/check-one.yaml",
            ["RULE_ONE"],
            ["alpha"],
        )

    def add_dynamic_test(
        self,
        test_id: str,
        command_value: list[str],
        patch_file: str | None = None,
    ) -> None:
        entity: dict[str, Any] = {
            "schema_version": 1,
            "kind": "syscallguard_starry_dynamic_test",
            "test_id": test_id,
            "rule_refs": ["RULE_ONE"],
            "applies_to_syscalls": ["alpha"],
            "test_source": "test-marker.txt",
            "build": {"kind": "fixture"},
            "command": command_value,
            "timeout_seconds": 30,
        }
        if patch_file:
            entity["patch_file"] = patch_file
        path = self.root / "targets/starry/dynamic-tests" / f"{slug(test_id)}.yaml"
        atomic_write_yaml(path, entity)
        self.update_executable_index(
            "dynamic-tests",
            "syscallguard_starry_dynamic_test_index",
            "test_id",
            test_id,
            path,
            ["RULE_ONE"],
            ["alpha"],
        )

    def map_fixture(self, descriptor: Path, run_id: str = "mapping-fixture") -> str:
        self.assertEqual(descriptor, self.root / "targets/starry/target.yaml")
        return run_mapping(None, self.root, run_id, target_branch(self.root))


class IngestTests(FlowTestCase):
    def test_generated_run_id_is_valid(self) -> None:
        run_id = new_run_id("spec", {"fixture": True})
        self.assertEqual(normalize_run_id(run_id), run_id)

    def test_only_report_index_and_rules_are_persisted(self) -> None:
        _source, descriptor = self.make_ltp()
        before = {path.relative_to(self.root) for path in self.root.rglob("*") if path.is_file()}
        run_ingest(descriptor, 1, self.root, "spec-only-two-kinds")
        after = {path.relative_to(self.root) for path in self.root.rglob("*") if path.is_file()}
        created = after - before
        self.assertIn(Path("runs/spec-only-two-kinds/report.md"), created)
        self.assertIn(Path("library/syscalls.yaml"), created)
        self.assertTrue(any(path.parent == Path("library/rules") for path in created))
        self.assertTrue(
            all(
                path == Path("runs/spec-only-two-kinds/report.md")
                or path == Path("library/syscalls.yaml")
                or path.parent == Path("library/rules")
                for path in created
            )
        )

    def test_new_unchanged_changed_and_semantic_update(self) -> None:
        source, descriptor = self.make_ltp()
        run_ingest(descriptor, 1, self.root, "spec-first")
        first = report(self.root, "spec-first")
        self.assertEqual(first["selected_syscalls"], ["alpha"])
        original_rule = first["syscalls"][0]["rules"][0]["id"]
        rule_path = self.root / "library/rules" / f"{slug(original_rule)}.yaml"
        original_generated = load_mapping(rule_path)["generated_at_utc"]

        run_ingest(descriptor, 5, self.root, "spec-second")
        second = report(self.root, "spec-second")
        self.assertEqual(second["selected_syscalls"], ["beta"])
        self.assertEqual(second["pending_count"], 1)
        run_ingest(descriptor, 5, self.root, "spec-third")
        self.assertEqual(report(self.root, "spec-third")["selected_syscalls"], [])

        commit_file(
            source,
            "testcases/kernel/syscalls/alpha/alpha01.c",
            "void run(void) { TST_EXP_FAIL(alpha(), EFAULT); }\n",
        )
        run_ingest(descriptor, 5, self.root, "spec-fourth")
        fourth = report(self.root, "spec-fourth")
        self.assertEqual(fourth["selected_syscalls"], ["alpha"])
        self.assertEqual(fourth["syscalls"][0]["selection_reason"], "source_changed")
        self.assertNotEqual(load_mapping(rule_path)["generated_at_utc"], original_generated)

    def test_default_alias_descriptor_and_count_precedence(self) -> None:
        _source, descriptor = self.make_ltp()
        self.assertEqual(resolve_source(None, self.root)[0], descriptor.resolve())
        self.assertEqual(resolve_source("fixture", self.root)[0], descriptor.resolve())
        self.assertEqual(resolve_source("sources/fixture.yaml", self.root)[0], descriptor.resolve())
        self.assertEqual(resolve_count(None, {})[:2], (20, "20"))
        self.assertEqual(resolve_count(None, {"default_count": 7})[:2], (7, "7"))
        self.assertEqual(resolve_count("all", {"default_count": 7})[:2], (None, "all"))
        for invalid in (0, -1, "0", "nope", "1.5"):
            with self.assertRaisesRegex(SyscallGuardError, "positive integer"):
                resolve_count(invalid, {})

    def test_syscall_list_normalization_and_cli(self) -> None:
        self.assertEqual(
            resolve_syscalls(" beta, Alpha,alpha, BETA "), ["alpha", "beta"]
        )
        self.assertIsNone(resolve_syscalls(None))
        for invalid in ("", "   ", ",", "alpha,", ",alpha", "alpha,,beta"):
            with self.subTest(invalid=invalid):
                with self.assertRaisesRegex(SyscallGuardError, "non-empty"):
                    resolve_syscalls(invalid)
        args = build_ingest_parser().parse_args(["--syscalls", "alpha,beta"])
        self.assertEqual(args.syscalls, "alpha,beta")

    def test_syscall_list_selection_is_incremental_and_global_pending_is_retained(self) -> None:
        _source, descriptor = self.make_ltp()
        run_ingest(
            descriptor,
            root=self.root,
            requested_run_id="spec-list-beta",
            syscalls=" BETA,beta ",
        )
        first = report(self.root, "spec-list-beta")
        self.assertEqual(first["requested_syscalls"], ["beta"])
        self.assertEqual(first["count"], {"value": None, "source": "explicit_syscalls"})
        self.assertEqual(first["pending_count"], 2)
        self.assertEqual(first["selected_syscalls"], ["beta"])
        body = (self.root / "runs/spec-list-beta/report.md").read_text(encoding="utf-8")
        self.assertIn("指定 syscall：`beta`", body)
        self.assertNotIn("提取数量：", body)
        self.assertLess(body.index("# Syscall 合规性规则提取报告"), body.index("机器可读元数据"))
        index = load_mapping(self.root / "library/syscalls.yaml")
        self.assertEqual(list(index["syscalls"]), ["beta"])
        rule_path = self.root / index["syscalls"]["beta"][0]["path"]
        comment = rule_path.read_text(encoding="utf-8").splitlines()[0]
        self.assertTrue(comment.startswith("# 合规检查：条件："))
        index_text = (self.root / "library/syscalls.yaml").read_text(encoding="utf-8")
        rule_id = index["syscalls"]["beta"][0]["rule_id"]
        self.assertIn(f"  {comment}\n  - rule_id: {rule_id}\n", index_text)

        run_ingest(
            descriptor,
            root=self.root,
            requested_run_id="spec-list-partial",
            syscalls="beta, ALPHA,alpha",
        )
        partial = report(self.root, "spec-list-partial")
        self.assertEqual(partial["requested_syscalls"], ["alpha", "beta"])
        self.assertEqual(partial["pending_count"], 1)
        self.assertEqual(partial["selected_syscalls"], ["alpha"])

        run_ingest(
            descriptor,
            root=self.root,
            requested_run_id="spec-list-unchanged",
            syscalls="alpha,beta",
        )
        unchanged = report(self.root, "spec-list-unchanged")
        self.assertEqual(unchanged["pending_count"], 0)
        self.assertEqual(unchanged["selected_syscalls"], [])
        errors: list[str] = []
        with mock.patch.object(validate_repository, "ROOT", self.root):
            validate_repository.validate_reports(errors)
        self.assertEqual(errors, [])

    def test_syscall_list_ignores_descriptor_default_count(self) -> None:
        _source, descriptor = self.make_ltp()
        value = load_mapping(descriptor)
        value["default_count"] = 1
        atomic_write_yaml(descriptor, value)
        run_ingest(
            descriptor,
            root=self.root,
            requested_run_id="spec-list-ignore-default",
            syscalls="beta,alpha",
        )
        selected = report(self.root, "spec-list-ignore-default")
        self.assertEqual(selected["selected_syscalls"], ["alpha", "beta"])

    def test_syscall_list_reacts_to_source_and_recognizer_changes(self) -> None:
        source, descriptor = self.make_ltp()
        run_ingest(
            descriptor,
            root=self.root,
            requested_run_id="spec-list-baseline",
            syscalls="alpha",
        )
        commit_file(
            source,
            "testcases/kernel/syscalls/alpha/alpha01.c",
            "void run(void) { TST_EXP_FAIL(alpha(), EFAULT); ALPHA_EXP(alpha()); }\n",
        )
        run_ingest(
            descriptor,
            root=self.root,
            requested_run_id="spec-list-source-change",
            syscalls="alpha",
        )
        changed = report(self.root, "spec-list-source-change")
        self.assertEqual(changed["selected_syscalls"], ["alpha"])
        self.assertEqual(changed["syscalls"][0]["selection_reason"], "source_changed")

        rules_path = self.root / "sources/adapters/ltp/recognition-rules.yaml"
        rules = load_mapping(rules_path)
        rules["recognizers"].append(
            {
                "id": "fixture.alpha-list",
                "enabled": True,
                "kind": "tst_exp",
                "names": ["ALPHA_EXP"],
                "call_argument": 0,
                "expected": {"kind": "success", "return": "SUCCESS"},
            }
        )
        atomic_write_yaml(rules_path, rules)
        run_ingest(
            descriptor,
            root=self.root,
            requested_run_id="spec-list-recognizer-change",
            syscalls="alpha",
        )
        recognized = report(self.root, "spec-list-recognizer-change")
        self.assertEqual(recognized["selected_syscalls"], ["alpha"])
        self.assertEqual(
            recognized["syscalls"][0]["selection_reason"], "recognition_changed"
        )

    def test_invalid_syscall_lists_write_nothing(self) -> None:
        _source, descriptor = self.make_ltp()
        cases = [
            ("spec-list-empty", None, "", "non-empty"),
            ("spec-list-gap", None, "alpha,,beta", "non-empty"),
            ("spec-list-unknown", None, "missing", "do not exist"),
            ("spec-list-conflict", 1, "alpha", "mutually exclusive"),
        ]
        for run_id, count, syscalls, message in cases:
            with self.subTest(run_id=run_id):
                with self.assertRaisesRegex(SyscallGuardError, message):
                    run_ingest(
                        descriptor,
                        count,
                        self.root,
                        run_id,
                        syscalls,
                    )
                self.assertFalse((self.root / "runs" / run_id).exists())
        self.assertEqual(list((self.root / "library/rules").glob("*.yaml")), [])

    def test_failure_writes_nothing_and_retries(self) -> None:
        _source, descriptor = self.make_ltp()
        with mock.patch(
            "syscallguard.ingest.LtpAdapter.extract", side_effect=RuntimeError("boom")
        ):
            with self.assertRaisesRegex(SyscallGuardError, "boom"):
                run_ingest(descriptor, 1, self.root, "spec-failed")
        self.assertFalse((self.root / "runs/spec-failed").exists())
        self.assertEqual(list((self.root / "library/rules").glob("*.yaml")), [])
        run_ingest(descriptor, 1, self.root, "spec-retry")
        self.assertEqual(report(self.root, "spec-retry")["selected_syscalls"], ["alpha"])

    def test_recognizer_change_is_precise(self) -> None:
        source, descriptor = self.make_ltp()
        commit_file(
            source,
            "testcases/kernel/syscalls/alpha/alpha01.c",
            "void run(void) { TST_EXP_FAIL(alpha(), EBADF); ALPHA_EXP(alpha()); }\n",
        )
        run_ingest(descriptor, "all", self.root, "spec-baseline")
        rules_path = self.root / "sources/adapters/ltp/recognition-rules.yaml"
        rules = load_mapping(rules_path)
        rules["recognizers"].append(
            {
                "id": "fixture.alpha-only",
                "enabled": True,
                "kind": "tst_exp",
                "names": ["ALPHA_EXP"],
                "call_argument": 0,
                "expected": {"kind": "success", "return": "SUCCESS"},
            }
        )
        atomic_write_yaml(rules_path, rules)
        run_ingest(descriptor, "all", self.root, "spec-recognizer")
        changed = report(self.root, "spec-recognizer")
        self.assertEqual(changed["selected_syscalls"], ["alpha"])
        self.assertEqual(changed["syscalls"][0]["selection_reason"], "recognition_changed")

    def test_formed_zero_unresolved_and_mixed_results(self) -> None:
        source = Path(self.temp.name) / "mixed-ltp"
        init_repo(
            source,
            {
                "testcases/kernel/syscalls/alpha/alpha.c": (
                    "void run(void) { TST_EXP_FAIL(alpha(), EBADF); "
                    "TST_EXP_EXPR(alpha()); }\n"
                ),
                "testcases/kernel/syscalls/beta/beta.c": (
                    "void run(void) { TST_EXP_EXPR(beta()); }\n"
                ),
                "testcases/kernel/syscalls/gamma/gamma.c": (
                    "static struct test_case_t { int expected_errno; } tests[] = "
                    "{{EBADF}};\n"
                    "void run(void) { TST_EXP_FAIL(gamma(), EBADF); }\n"
                ),
                "testcases/kernel/syscalls/zero/zero.c": "void run(void) { helper(); }\n",
            },
        )
        descriptor = self.root / "mixed.yaml"
        atomic_write_yaml(
            descriptor,
            {"source_id": "mixed", "adapter": "ltp", "location": str(source), "revision": "HEAD"},
        )
        run_ingest(descriptor, "all", self.root, "spec-mixed")
        rows = {row["syscall"]: row for row in report(self.root, "spec-mixed")["syscalls"]}
        self.assertEqual(rows["alpha"]["result"], "formed_rules")
        self.assertTrue(rows["alpha"]["rules"])
        self.assertEqual(rows["alpha"]["unresolved_evidence_count"], 0)
        self.assertEqual(rows["beta"]["result"], "no_rules")
        self.assertEqual(rows["beta"]["unresolved_evidence_count"], 0)
        self.assertEqual(rows["beta"]["rules"], [])
        self.assertEqual(rows["gamma"]["result"], "no_rules")
        self.assertEqual(rows["gamma"]["unresolved_evidence_count"], 1)
        self.assertEqual(rows["gamma"]["rules"], [])
        self.assertEqual(rows["zero"]["reason"], "no_evidence")

    def test_sources_only_merge_keeps_version_and_old_report_usable(self) -> None:
        _source, descriptor = self.make_ltp()
        run_ingest(descriptor, 1, self.root, "spec-first-source")
        first = report(self.root, "spec-first-source")
        version = first["syscalls"][0]["rules"][0]
        rule_path = self.root / "library/rules" / f"{slug(version['id'])}.yaml"

        second_source = Path(self.temp.name) / "ltp-second"
        init_repo(
            second_source,
            {"testcases/kernel/syscalls/alpha/alpha.c": "void run(void) { TST_EXP_FAIL(alpha(), EBADF); }\n"},
        )
        second_descriptor = self.root / "sources/second.yaml"
        atomic_write_yaml(
            second_descriptor,
            {"source_id": "second", "adapter": "ltp", "location": str(second_source), "revision": "HEAD"},
        )
        run_ingest(second_descriptor, "all", self.root, "spec-second-source")
        merged = load_mapping(rule_path)
        self.assertEqual(merged["generated_at_utc"], version["generated_at_utc"])
        self.assertEqual(len(merged["sources"]), 2)
        _repo, target, _commit = self.make_target()
        run_mapping(None, self.root, "mapping-after-provenance", target_branch(self.root))

    def test_explicit_stable_rule_id_conflict_creates_variant(self) -> None:
        _source, descriptor = self.make_ltp()
        rules_path = self.root / "sources/adapters/ltp/recognition-rules.yaml"
        rules = load_mapping(rules_path)
        rules["rule_template"]["rule_id"] = "FIXED_RULE"
        atomic_write_yaml(rules_path, rules)
        run_ingest(descriptor, "all", self.root, "spec-conflict")
        value = report(self.root, "spec-conflict")
        ids = {
            version["id"]
            for row in value["syscalls"]
            for version in row["rules"]
        }
        self.assertIn("FIXED_RULE", ids)
        self.assertTrue(any(rule_id.startswith("FIXED_RULE--") for rule_id in ids))
        self.assertEqual(len(value["conflicts"]), 1)


class MappingTests(FlowTestCase):
    def test_only_report_and_two_level_libraries_are_persisted(self) -> None:
        self.prepare_spec_run()
        _repo, _descriptor, _snapshot = self.make_target("good\n")
        run_mapping(None, self.root, "mapping-first-attempt", target_branch(self.root))
        report = load_mapping_report(self.root, "mapping-first-attempt")
        self.assertEqual(report["counts"]["added"], 1)
        self.assertEqual(report["rules"]["RULE_ONE"]["status"], "needs_review")
        self.assertEqual(
            {item.name for item in (self.root / "runs/mapping-first-attempt").iterdir()},
            {"report.md"},
        )
        self.assertTrue((self.root / "targets/starry/static-checks.yaml").is_file())
        self.assertTrue((self.root / "targets/starry/dynamic-tests.yaml").is_file())
        self.assertFalse((self.root / "targets/starry/rule-coverage.yaml").exists())
        self.assertFalse((self.root / "targets/starry/mappings").exists())
        self.assertFalse((TEMP_ROOT / "mapping-first-attempt").exists())

    def test_report_state_uses_relevant_target_content(self) -> None:
        self.prepare_spec_run()
        self.add_static_check("good")
        repo, descriptor, _old_commit = self.make_target("good\n")
        self.map_fixture(descriptor, "mapping-old")
        first = load_mapping_report(self.root, "mapping-old")
        self.assertEqual(first["rules"]["RULE_ONE"]["status"], "covered")
        self.assertEqual(first["execution_scope"]["static_checks"], ["CHECK_ONE"])
        self.assertEqual(first["rule_syscalls"], {"RULE_ONE": ["alpha"]})

        target_descriptor = load_mapping(descriptor)
        target_descriptor["workflow_note"] = "branch negotiation metadata only"
        atomic_write_yaml(descriptor, target_descriptor)
        run_mapping(
            None, self.root, "mapping-descriptor-only", target_branch(self.root)
        )
        descriptor_only = load_mapping_report(self.root, "mapping-descriptor-only")
        self.assertEqual(descriptor_only["counts"]["processed"], 0)
        self.assertEqual(descriptor_only["target"]["branch"], target_branch(self.root))

        commit_file(repo, "unrelated.txt", "unrelated\n")
        run_mapping(None, self.root, "mapping-unrelated", target_branch(self.root))
        unrelated = load_mapping_report(self.root, "mapping-unrelated")
        self.assertEqual(unrelated["counts"]["processed"], 0)
        self.assertEqual(unrelated["execution_scope"]["static_checks"], [])

        commit_file(repo, "code.txt", "changed target\n")
        prepared = prepare_mapping(
            None, self.root, "mapping-related", target_branch(self.root)
        )
        preparation = load_mapping(TEMP_ROOT / prepared / "preparation.yaml")
        self.assertEqual(preparation["selected_rule_ids"], ["RULE_ONE"])

        with self.assertRaisesRegex(SyscallGuardError, "stale mapping"):
            run_check("mapping-old", self.root, "check-stale")
        self.assertFalse((self.root / "runs/check-stale").exists())
        self.assertTrue((CHECK_TEMP_ROOT / "check-stale/failure.yaml").is_file())

    def test_syscall_filter_and_needs_review_retry(self) -> None:
        self.prepare_spec_run()
        rule_two = load_mapping(self.root / "library/rules/rule-one.yaml")
        rule_two["rule_id"] = "RULE_TWO"
        rule_two["generated_at_utc"] = "2026-01-02T00:00:00.000000Z"
        atomic_write_yaml(self.root / "library/rules/rule-two.yaml", rule_two)
        index = load_mapping(self.root / "library/syscalls.yaml")
        index["syscalls"]["beta"] = [
            {"rule_id": "RULE_TWO", "path": "library/rules/rule-two.yaml"}
        ]
        atomic_write_yaml(self.root / "library/syscalls.yaml", index)
        repo, _descriptor, _commit = self.make_target()
        run_mapping("alpha", self.root, "mapping-alpha", target_branch(self.root))
        first = load_mapping_report(self.root, "mapping-alpha")
        self.assertEqual(first["rules"]["RULE_ONE"]["status"], "needs_review")
        self.assertEqual(first["rules"]["RULE_TWO"]["status"], "pending")
        self.assertEqual(first["remaining"]["needs_review"], ["RULE_ONE"])
        self.assertEqual(first["remaining"]["pending"], ["RULE_TWO"])

        run_id = prepare_mapping(
            " alpha,ALPHA ", self.root, "mapping-same", target_branch(self.root)
        )
        same = load_mapping(TEMP_ROOT / run_id / "preparation.yaml")
        self.assertEqual(same["selected_rule_ids"], [])
        finalize_mapping(run_id, self.root)
        commit_file(repo, "code.txt", "new content\n")
        retry_id = prepare_mapping(
            "alpha", self.root, "mapping-retry", target_branch(self.root)
        )
        retry = load_mapping(TEMP_ROOT / retry_id / "preparation.yaml")
        self.assertEqual(retry["selected_rule_ids"], ["RULE_ONE"])

        self.assertEqual(resolve_mapping_syscalls(" beta,Alpha,alpha "), ["alpha", "beta"])
        self.assertIsNone(resolve_mapping_syscalls(None))
        args = build_mapping_parser().parse_args(["--syscalls", "alpha,beta"])
        self.assertEqual(args.syscalls, "alpha,beta")
        self.assertIsNone(args.branch)
        with self.assertRaisesRegex(SyscallGuardError, "user-created Starry branch"):
            prepare_mapping("alpha", self.root, "mapping-no-branch")
        with self.assertRaisesRegex(SyscallGuardError, "Starry branch changed"):
            prepare_mapping(
                "alpha", self.root, "mapping-wrong-branch", "not-the-current-branch"
            )
        with mock.patch("sys.stderr", new=io.StringIO()):
            with self.assertRaisesRegex(SystemExit, "2"):
                build_mapping_parser().parse_args(["--from", "spec-old"])
        with self.assertRaisesRegex(SyscallGuardError, "do not exist"):
            prepare_mapping(
                "missing", self.root, "mapping-missing", target_branch(self.root)
            )

    def test_all_result_kinds_publish_resolvable_two_level_references(self) -> None:
        self.prepare_spec_run()
        index = load_mapping(self.root / "library/syscalls.yaml")
        base = load_mapping(self.root / "library/rules/rule-one.yaml")
        rule_ids = {
            "RULE_ONE": "static",
            "RULE_DYNAMIC": "dynamic",
            "RULE_BOTH": "both",
            "RULE_UNSUPPORTED": "unsupported",
            "RULE_REVIEW": "needs_review",
        }
        refs = index["syscalls"]["alpha"]
        for offset, rule_id in enumerate(sorted(set(rule_ids) - {"RULE_ONE"}), start=2):
            entity = dict(base)
            entity["rule_id"] = rule_id
            entity["generated_at_utc"] = f"2026-01-0{offset}T00:00:00.000000Z"
            path = self.root / "library/rules" / f"{slug(rule_id)}.yaml"
            atomic_write_yaml(path, entity)
            refs.append({"rule_id": rule_id, "path": str(path.relative_to(self.root))})
        atomic_write_yaml(self.root / "library/syscalls.yaml", index)
        _repo, _descriptor, _snapshot = self.make_target("fn implementation() {}\n")
        run_id = prepare_mapping(
            None, self.root, "mapping-five-kinds", target_branch(self.root)
        )
        workspace = TEMP_ROOT / run_id
        staged_root = workspace / "staged/targets/starry"

        for rule_id, result_kind in rule_ids.items():
            static_refs = [f"CHECK_{rule_id}"] if result_kind in {"static", "both"} else []
            dynamic_refs = [f"TEST_{rule_id}"] if result_kind in {"dynamic", "both"} else []
            status = result_kind if result_kind in {"needs_review", "unsupported"} else "covered"
            result = {
                "schema_version": 1,
                "kind": "syscallguard_starry_rule_mapping_result",
                "rule_id": rule_id,
                "status": status,
                "target_locations": (
                    [{"path": "code.txt", "symbols": []}]
                    if status == "covered"
                    else []
                ),
                "static_check_refs": static_refs,
                "dynamic_test_refs": dynamic_refs,
                "reason": f"fixture {result_kind}",
            }
            atomic_write_yaml(
                workspace / "staged/rule-results" / f"{slug(rule_id)}.yaml", result
            )
            for check_id in static_refs:
                atomic_write_yaml(
                    staged_root / "static-checks" / f"{slug(check_id)}.yaml",
                    {
                        "schema_version": 1,
                        "kind": "syscallguard_starry_static_check",
                        "check_id": check_id,
                        "rule_refs": [rule_id],
                        "path": "code.txt",
                        "patterns": [{"label": "implementation", "regex": "implementation"}],
                    },
                )
            for test_id in dynamic_refs:
                dynamic = {
                    "schema_version": 1,
                    "kind": "syscallguard_starry_dynamic_test",
                    "test_id": test_id,
                    "rule_refs": [rule_id],
                    "test_source": "fixture.c",
                    "build": {"kind": "fixture"},
                    "command": ["/bin/true"],
                }
                if rule_id == "RULE_DYNAMIC":
                    dynamic["patch_file"] = "targets/starry/dynamic-tests/assets/fixture.patch"
                    atomic_write_text(
                        staged_root / "dynamic-tests/assets/fixture.patch",
                        "fixture patch\n",
                    )
                atomic_write_yaml(
                    staged_root / "dynamic-tests" / f"{slug(test_id)}.yaml",
                    dynamic,
                )

        finalize_mapping(run_id, self.root)
        report = load_mapping_report(self.root, run_id)
        self.assertEqual(report["rules"]["RULE_ONE"]["status"], "covered")
        self.assertEqual(report["rules"]["RULE_DYNAMIC"]["dynamic_test_refs"], ["TEST_RULE_DYNAMIC"])
        self.assertEqual(report["rules"]["RULE_BOTH"]["status"], "covered")
        self.assertEqual(report["rules"]["RULE_UNSUPPORTED"]["status"], "unsupported")
        self.assertEqual(report["rules"]["RULE_REVIEW"]["status"], "needs_review")
        self.assertEqual(report["counts"]["static_checks"], 2)
        self.assertEqual(report["counts"]["dynamic_tests"], 2)
        static_index = load_mapping(self.root / "targets/starry/static-checks.yaml")
        dynamic_index = load_mapping(self.root / "targets/starry/dynamic-tests.yaml")
        self.assertIn("alpha", static_index["syscalls"])
        self.assertIn("alpha", dynamic_index["syscalls"])
        detail = load_mapping(self.root / "targets/starry/static-checks/check-rule-one.yaml")
        self.assertTrue(detail["target_dependencies"])
        self.assertIn("target_content_fingerprint", detail)
        self.assertEqual(
            (self.root / "targets/starry/dynamic-tests/assets/fixture.patch").read_text(
                encoding="utf-8"
            ),
            "fixture patch\n",
        )

    def test_finalizer_failure_does_not_advance_shared_state(self) -> None:
        self.prepare_spec_run()
        _repo, _descriptor, _snapshot = self.make_target("good\n")
        run_id = prepare_mapping(
            None,
            self.root,
            "mapping-publish-failure",
            target_branch(self.root),
        )
        with mock.patch(
            "syscallguard.mapping._transactional_write", side_effect=OSError("publish failed")
        ):
            with self.assertRaisesRegex(SyscallGuardError, "publish failed"):
                finalize_mapping(run_id, self.root)
        self.assertFalse((self.root / f"runs/{run_id}").exists())
        self.assertFalse((self.root / "targets/starry/static-checks.yaml").exists())
        self.assertFalse((self.root / "targets/starry/dynamic-tests.yaml").exists())
        self.assertTrue((TEMP_ROOT / run_id / "failure.yaml").is_file())


class CheckTests(FlowTestCase):
    def test_pass_and_identical_input_reuse_on_negotiated_branch(self) -> None:
        self.prepare_spec_run()
        self.add_static_check("bad")
        repo, descriptor, commit = self.make_target()
        self.map_fixture(descriptor)
        before = command(["git", "status", "--short"], repo)
        run_check("mapping-fixture", self.root, "check-first")
        first = load_check_report(self.root, "check-first")
        self.assertEqual(first["status"], "completed")
        self.assertEqual(first["counts"]["static_pass"], 1)
        self.assertEqual(
            {item.name for item in (self.root / "runs/check-first").iterdir()},
            {"report.md"},
        )
        report_text = (self.root / "runs/check-first/report.md").read_text(encoding="utf-8")
        self.assertIn("# Starry 合规检查报告", report_text)
        self.assertIn("`CHECK_ONE`", report_text)
        self.assertIn("matched=`true`", report_text)
        self.assertTrue((self.root / "targets/starry/findings/index.yaml").is_file())
        self.assertFalse((CHECK_TEMP_ROOT / "check-first").exists())
        self.assertEqual(command(["git", "rev-parse", "HEAD"], repo), commit)
        self.assertEqual(command(["git", "status", "--short"], repo), before)

        run_check("mapping-fixture", self.root, "check-second")
        second = load_check_report(self.root, "check-second")
        self.assertEqual(second["reused_from"], "check-first")
        self.assertEqual(second["counts"]["reused"], 1)
        self.assertFalse((CHECK_TEMP_ROOT / "check-second").exists())

    def test_findings_use_mapping_syscall_ownership(self) -> None:
        self.prepare_spec_run()
        self.add_static_check("good", ["alpha", "beta"])
        repo, descriptor, _commit = self.make_target()
        self.map_fixture(descriptor)
        run_check("mapping-fixture", self.root, "check-ownership")
        check_report = load_check_report(self.root, "check-ownership")
        self.assertTrue(check_report["finding_ids"])
        for finding_id in check_report["finding_ids"]:
            finding = load_mapping(
                self.root / "targets/starry/findings" / f"{slug(finding_id)}.yaml"
            )
            self.assertEqual(finding["syscall"], "alpha")
            self.assertNotIn("diagnostic_log", yaml.safe_dump(finding))

    def test_check_rejects_a_different_current_branch(self) -> None:
        self.prepare_spec_run()
        self.add_static_check("bad")
        repo, descriptor, _commit = self.make_target()
        self.map_fixture(descriptor)
        command(["git", "switch", "-c", "different-check-branch"], repo)
        with self.assertRaisesRegex(SyscallGuardError, "Starry branch changed"):
            run_check("mapping-fixture", self.root, "check-wrong-branch")
        self.assertFalse((self.root / "runs/check-wrong-branch").exists())

    def test_reuse_does_not_add_finding_occurrence(self) -> None:
        self.prepare_spec_run()
        self.add_static_check("good")
        repo, descriptor, _commit = self.make_target()
        self.map_fixture(descriptor)
        run_check("mapping-fixture", self.root, "check-reuse-first")
        first = load_check_report(self.root, "check-reuse-first")
        finding_id = first["finding_ids"][0]
        finding_path = self.root / "targets/starry/findings" / f"{slug(finding_id)}.yaml"
        occurrence_count = len(load_mapping(finding_path)["occurrences"])

        run_check("mapping-fixture", self.root, "check-reuse-second")
        second = load_check_report(self.root, "check-reuse-second")
        self.assertEqual(second["reused_from"], "check-reuse-first")
        self.assertEqual(len(load_mapping(finding_path)["occurrences"]), occurrence_count)

    def test_same_snapshot_open_finding_is_carried_by_empty_mapping_scope(self) -> None:
        self.prepare_spec_run()
        self.add_static_check("good")
        _repo, descriptor, _commit = self.make_target()
        self.map_fixture(descriptor)
        run_check("mapping-fixture", self.root, "check-gap")
        first = load_check_report(self.root, "check-gap")
        self.assertEqual(len(first["finding_ids"]), 1)

        run_mapping(None, self.root, "mapping-empty", target_branch(self.root))
        empty_mapping = load_mapping_report(self.root, "mapping-empty")
        self.assertEqual(empty_mapping["execution_scope"]["static_checks"], [])
        run_check("mapping-empty", self.root, "check-carried")
        carried = load_check_report(self.root, "check-carried")
        self.assertEqual(carried["finding_ids"], first["finding_ids"])
        self.assertEqual(carried["carried_finding_ids"], first["finding_ids"])
        self.assertEqual(carried["counts"]["findings"], 1)
        self.assertEqual(carried["counts"]["carried_findings"], 1)

    def test_same_snapshot_legacy_finding_is_revalidated_on_negotiated_branch(self) -> None:
        self.prepare_spec_run()
        self.add_static_check("good")
        _repo, descriptor, _commit = self.make_target()
        self.map_fixture(descriptor)
        run_check("mapping-fixture", self.root, "check-legacy-evidence")
        legacy = load_check_report(self.root, "check-legacy-evidence")
        finding_id = legacy["finding_ids"][0]
        legacy.pop("content_hash", None)
        legacy["target"] = dict(legacy["target"])
        legacy["target"].pop("branch")
        legacy["content_hash"] = version_content_hash(legacy)
        atomic_write_text(
            self.root / "runs/check-legacy-evidence/report.md",
            markdown_report(legacy),
        )

        run_mapping(
            None, self.root, "mapping-branch-migration", target_branch(self.root)
        )
        run_check(
            "mapping-branch-migration", self.root, "check-branch-migration"
        )
        migrated = load_check_report(self.root, "check-branch-migration")
        self.assertEqual(migrated["finding_ids"], [finding_id])
        self.assertEqual(
            migrated["revalidation_scope"]["static_checks"], ["CHECK_ONE"]
        )
        finding = load_mapping(
            self.root / "targets/starry/findings" / f"{slug(finding_id)}.yaml"
        )
        self.assertEqual(
            finding["occurrences"][-1]["check_report_id"],
            "check-branch-migration",
        )
        preparation = prepare_fix(self.root, "fix-branch-migration")
        self.assertEqual(
            preparation["source_check_report_ids"], ["check-branch-migration"]
        )

        run_mapping(
            None, self.root, "mapping-after-migration", target_branch(self.root)
        )
        run_check("mapping-after-migration", self.root, "check-after-migration")
        carried = load_check_report(self.root, "check-after-migration")
        self.assertEqual(carried["revalidation_scope"]["static_checks"], [])
        self.assertEqual(carried["counts"]["carried_findings"], 1)

    def test_old_snapshot_failure_is_superseded_by_current_finding(self) -> None:
        self.prepare_spec_run()
        self.add_static_check("good")
        repo, descriptor, _commit = self.make_target()
        self.map_fixture(descriptor)
        run_check("mapping-fixture", self.root, "check-old-gap")
        old_id = load_check_report(self.root, "check-old-gap")["finding_ids"][0]

        commit_file(repo, "code.txt", "still bad\n")
        run_mapping(
            None, self.root, "mapping-new-snapshot", target_branch(self.root)
        )
        run_check("mapping-new-snapshot", self.root, "check-revalidated-fail")
        current = load_check_report(self.root, "check-revalidated-fail")
        self.assertEqual(len(current["finding_ids"]), 1)
        self.assertNotEqual(current["finding_ids"][0], old_id)
        self.assertIn(old_id, current["revalidated_finding_ids"])
        old = load_mapping(
            self.root / "targets/starry/findings" / f"{slug(old_id)}.yaml"
        )
        self.assertEqual(old["resolution"], "superseded")
        self.assertEqual(old["superseded_by"], current["finding_ids"][0])
        index = load_mapping(self.root / "targets/starry/findings/index.yaml")
        row = next(item for item in index["entities"] if item["id"] == old_id)
        self.assertEqual(row["generated_at_utc"], old["generated_at_utc"])
        self.assertEqual(row["content_hash"], version_content_hash(old))

    def test_fixed_old_snapshot_is_a_regression_seed_without_reopening_history(self) -> None:
        self.prepare_spec_run()
        self.add_static_check("good")
        repo, descriptor, _commit = self.make_target("bad\n")
        self.map_fixture(descriptor)
        run_check("mapping-fixture", self.root, "check-fixed-history-source")
        old_id = load_check_report(
            self.root, "check-fixed-history-source"
        )["finding_ids"][0]
        old_path = self.root / "targets/starry/findings" / f"{slug(old_id)}.yaml"
        old = load_mapping(old_path)
        old["resolution"] = "fixed"
        old["generated_at_utc"] = "2026-02-01T00:00:00.000000Z"
        old["fix_ref"] = "fixture-fix"
        old["fixed_by_run"] = "fixture-fix-run"
        atomic_write_yaml(old_path, old)
        index_path = self.root / "targets/starry/findings/index.yaml"
        index = load_mapping(index_path)
        row = next(item for item in index["entities"] if item["id"] == old_id)
        row["resolution"] = "fixed"
        row["generated_at_utc"] = old["generated_at_utc"]
        row["content_hash"] = version_content_hash(old)
        atomic_write_yaml(index_path, index)

        commit_file(repo, "unrelated.txt", "new snapshot\n")
        run_mapping(
            None, self.root, "mapping-fixed-history-regression", target_branch(self.root)
        )
        mapping = load_mapping_report(self.root, "mapping-fixed-history-regression")
        self.assertEqual(mapping["execution_scope"]["static_checks"], [])

        run_check(
            "mapping-fixed-history-regression",
            self.root,
            "check-fixed-history-regression",
        )
        current = load_check_report(self.root, "check-fixed-history-regression")
        self.assertEqual(
            current["historical_regression_scope"]["static_checks"], ["CHECK_ONE"]
        )
        self.assertEqual(current["revalidation_scope"]["static_checks"], [])
        self.assertEqual(len(current["finding_ids"]), 1)
        self.assertNotEqual(current["finding_ids"][0], old_id)
        self.assertEqual(current["revalidated_finding_ids"], [])
        self.assertEqual(load_mapping(old_path)["resolution"], "fixed")

    def test_old_snapshot_pass_is_marked_no_longer_reproduces(self) -> None:
        self.prepare_spec_run()
        self.add_static_check("good")
        repo, descriptor, _commit = self.make_target()
        self.map_fixture(descriptor)
        run_check("mapping-fixture", self.root, "check-old-failing")
        old_id = load_check_report(self.root, "check-old-failing")["finding_ids"][0]

        commit_file(repo, "code.txt", "good\n")
        run_mapping(
            None, self.root, "mapping-fixed-snapshot", target_branch(self.root)
        )
        run_check("mapping-fixed-snapshot", self.root, "check-revalidated-pass")
        current = load_check_report(self.root, "check-revalidated-pass")
        self.assertEqual(current["finding_ids"], [])
        self.assertIn(old_id, current["revalidated_finding_ids"])
        old = load_mapping(
            self.root / "targets/starry/findings" / f"{slug(old_id)}.yaml"
        )
        self.assertEqual(old["resolution"], "no_longer_reproduces")
        index = load_mapping(self.root / "targets/starry/findings/index.yaml")
        row = next(item for item in index["entities"] if item["id"] == old_id)
        self.assertEqual(row["generated_at_utc"], old["generated_at_utc"])
        self.assertEqual(row["content_hash"], version_content_hash(old))

    def test_old_snapshot_blocker_remains_open_and_needs_revalidation(self) -> None:
        self.prepare_spec_run()
        self.add_static_check("bad")
        self.add_dynamic_test("DYNAMIC_FAIL", ["/bin/false"])
        repo, descriptor, _commit = self.make_target("bad\n")
        self.map_fixture(descriptor)
        run_check("mapping-fixture", self.root, "check-dynamic-old")
        old_id = load_check_report(self.root, "check-dynamic-old")["finding_ids"][0]

        commit_file(repo, "code.txt", "different snapshot\n")
        dynamic_path = self.root / "targets/starry/dynamic-tests/dynamic-fail.yaml"
        dynamic = load_mapping(dynamic_path)
        dynamic["command"] = [
            "/bin/sh",
            "-c",
            "echo 'No space left on device' >&2; exit 1",
        ]
        dynamic["generated_at_utc"] = "2026-02-01T00:00:00.000000Z"
        atomic_write_yaml(dynamic_path, dynamic)
        run_mapping(
            None, self.root, "mapping-blocked-snapshot", target_branch(self.root)
        )
        run_check("mapping-blocked-snapshot", self.root, "check-revalidated-blocked")
        current = load_check_report(self.root, "check-revalidated-blocked")
        self.assertEqual(current["status"], "completed_with_blockers")
        self.assertIn(old_id, current["needs_revalidation_finding_ids"])
        self.assertNotIn(old_id, current["finding_ids"])
        old = load_mapping(
            self.root / "targets/starry/findings" / f"{slug(old_id)}.yaml"
        )
        self.assertEqual(old["resolution"], "open")

    def test_reliable_dynamic_failure_keeps_only_eight_kib_tail(self) -> None:
        self.prepare_spec_run()
        self.add_static_check("bad")
        self.add_dynamic_test(
            "DYNAMIC_LONG_FAIL",
            ["/bin/sh", "-c", "printf '%09000d' 0; exit 9"],
        )
        _repo, descriptor, _commit = self.make_target()
        self.map_fixture(descriptor)
        run_check("mapping-fixture", self.root, "check-long-output")
        check_report = load_check_report(self.root, "check-long-output")
        result = check_report["dynamic"][0]
        self.assertEqual(result["result"], "fail")
        self.assertEqual(result["exit_code"], 9)
        self.assertTrue(result["output_truncated"])
        self.assertLessEqual(len(result["output_tail"].encode("utf-8")), 8 * 1024)
        finding = load_mapping(
            self.root
            / "targets/starry/findings"
            / f"{slug(result['finding_ids'][0])}.yaml"
        )
        evidence = finding["occurrences"][-1]["evidence"]
        self.assertLessEqual(len(evidence["output_tail"].encode("utf-8")), 8 * 1024)
        self.assertNotIn("diagnostic_log", evidence)

    def test_static_and_dynamic_findings_do_not_absorb_environment_blocker(self) -> None:
        self.prepare_spec_run()
        self.add_static_check("good")
        self.add_dynamic_test(
            "DYNAMIC_BLOCKER",
            ["/bin/sh", "-c", "echo 'No space left on device' >&2; exit 1"],
        )
        self.add_dynamic_test("DYNAMIC_FAIL", ["/bin/sh", "-c", "exit 7"])
        self.add_dynamic_test("DYNAMIC_SKIPPED", ["/bin/false"])
        skipped_path = self.root / "targets/starry/dynamic-tests/dynamic-skipped.yaml"
        skipped = load_mapping(skipped_path)
        skipped["enabled"] = False
        atomic_write_yaml(skipped_path, skipped)
        repo, descriptor, _commit = self.make_target()
        self.map_fixture(descriptor)
        run_check("mapping-fixture", self.root, "check-mixed-report")
        check_report = load_check_report(self.root, "check-mixed-report")
        self.assertEqual(check_report["status"], "completed_with_blockers")
        self.assertEqual(
            {row["test_id"]: row["result"] for row in check_report["dynamic"]},
            {
                "DYNAMIC_BLOCKER": "not_run",
                "DYNAMIC_FAIL": "fail",
                "DYNAMIC_SKIPPED": "skipped",
            },
        )
        self.assertTrue(Path(check_report["diagnostic_directory"]).is_dir())
        self.assertNotIn("worktree", check_report)
        self.assertEqual(command(["git", "status", "--short"], repo), "")
        self.assertEqual(
            {item.name for item in (self.root / "runs/check-mixed-report").iterdir()},
            {"report.md"},
        )
        for finding_id in check_report["finding_ids"]:
            finding = load_mapping(
                self.root / "targets/starry/findings" / f"{slug(finding_id)}.yaml"
            )
            self.assertNotIn("No space left on device", yaml.safe_dump(finding))
        dynamic_finding = next(
            row for row in check_report["dynamic"] if row["test_id"] == "DYNAMIC_FAIL"
        )
        self.assertTrue(dynamic_finding["finding_ids"])
        self.assertEqual(dynamic_finding["exit_code"], 7)

    def test_manual_check_edit_without_timestamp_is_rejected(self) -> None:
        self.prepare_spec_run()
        self.add_static_check("bad")
        _repo, descriptor, _commit = self.make_target()
        self.map_fixture(descriptor)
        path = self.root / "targets/starry/static-checks/check-one.yaml"
        entity = load_mapping(path)
        entity["patterns"][0]["regex"] = "manual-change"
        atomic_write_yaml(path, entity)
        with self.assertRaisesRegex(SyscallGuardError, "content changed"):
            run_check("mapping-fixture", self.root, "check-manual-stale")
        self.assertFalse((self.root / "runs/check-manual-stale").exists())
        self.assertTrue((CHECK_TEMP_ROOT / "check-manual-stale/failure.yaml").is_file())

    def test_publication_failure_does_not_partially_publish(self) -> None:
        self.prepare_spec_run()
        self.add_static_check("good")
        _repo, descriptor, _commit = self.make_target()
        self.map_fixture(descriptor)
        with mock.patch(
            "syscallguard.checking.transactional_write", side_effect=OSError("publish failed")
        ):
            with self.assertRaisesRegex(SyscallGuardError, "publish failed"):
                run_check("mapping-fixture", self.root, "check-publish-failure")
        self.assertFalse((self.root / "runs/check-publish-failure").exists())
        self.assertFalse((self.root / "targets/starry/findings/index.yaml").exists())
        self.assertFalse((self.root / "targets/starry/findings").exists())
        self.assertTrue((CHECK_TEMP_ROOT / "check-publish-failure/failure.yaml").is_file())


class FixTests(FlowTestCase):
    TEST_PATCH = """diff --git a/test-marker.txt b/test-marker.txt
new file mode 100644
--- /dev/null
+++ b/test-marker.txt
@@ -0,0 +1 @@
+test retained
"""
    FIX_PATCH = """diff --git a/code.txt b/code.txt
--- a/code.txt
+++ b/code.txt
@@ -1 +1 @@
-bad
+good
"""
    INEFFECTIVE_PATCH = """diff --git a/unrelated.txt b/unrelated.txt
new file mode 100644
--- /dev/null
+++ b/unrelated.txt
@@ -0,0 +1 @@
+unrelated
"""

    def prepare_failed_check(self) -> tuple[Path, str]:
        self.prepare_spec_run()
        self.add_static_check("good")
        test_patch = self.root / "targets/starry/dynamic-tests/assets/test.patch"
        test_patch.parent.mkdir(parents=True, exist_ok=True)
        test_patch.write_text(self.TEST_PATCH, encoding="utf-8")
        self.add_dynamic_test(
            "DYNAMIC_PASS",
            ["/bin/true"],
            "targets/starry/dynamic-tests/assets/test.patch",
        )
        repo, descriptor, base_commit = self.make_target()
        self.map_fixture(descriptor)
        run_check("mapping-fixture", self.root, "check-finding")
        check_report = load_check_report(self.root, "check-finding")
        self.assertEqual(check_report["counts"]["static_fail"], 1)
        self.assertEqual(check_report["counts"]["dynamic_pass"], 1)
        return repo, base_commit

    def add_second_rule_and_checks(self) -> None:
        rule = {
            "schema_version": 1,
            "kind": "syscallguard_rule",
            "rule_id": "RULE_TWO",
            "category": "fixture",
            "semantics": {
                "preconditions": [],
                "action": {"operation": "read second code rule"},
                "expected_result": "good",
                "errno": [],
            },
            "semantic_hash": "",
            "generated_at_utc": "2026-01-02T00:00:00.000000Z",
            "sources": [],
        }
        rule["semantic_hash"] = content_hash(
            {"category": rule["category"], "semantics": rule["semantics"]}
        )
        atomic_write_yaml(self.root / "library/rules/rule-two.yaml", rule)
        index = load_mapping(self.root / "library/syscalls.yaml")
        index["syscalls"]["beta"] = [
            {"rule_id": "RULE_TWO", "path": "library/rules/rule-two.yaml"}
        ]
        atomic_write_yaml(self.root / "library/syscalls.yaml", index)

        check = {
            "schema_version": 1,
            "kind": "syscallguard_starry_static_check",
            "check_id": "CHECK_TWO",
            "rule_refs": ["RULE_TWO"],
            "applies_to_syscalls": ["beta"],
            "path": "code.txt",
            "patterns": [{"label": "expected", "regex": "good"}],
        }
        check_path = self.root / "targets/starry/static-checks/check-two.yaml"
        atomic_write_yaml(check_path, check)
        self.update_executable_index(
            "static-checks",
            "syscallguard_starry_static_check_index",
            "check_id",
            "CHECK_TWO",
            check_path,
            ["RULE_TWO"],
            ["beta"],
        )
        self.add_dynamic_test(
            "DYNAMIC_TWO",
            ["/bin/true"],
            "targets/starry/dynamic-tests/assets/test.patch",
        )
        dynamic_path = self.root / "targets/starry/dynamic-tests/dynamic-two.yaml"
        dynamic = load_mapping(dynamic_path)
        dynamic["rule_refs"] = ["RULE_TWO"]
        dynamic["applies_to_syscalls"] = ["beta"]
        atomic_write_yaml(dynamic_path, dynamic)
        self.update_executable_index(
            "dynamic-tests",
            "syscallguard_starry_dynamic_test_index",
            "test_id",
            "DYNAMIC_TWO",
            dynamic_path,
            ["RULE_TWO"],
            ["beta"],
        )

    def test_success_commits_fix_and_injected_test_to_negotiated_branch(self) -> None:
        repo, base_commit = self.prepare_failed_check()
        patch = self.root / "fix-input/success.patch"
        patch.parent.mkdir(parents=True, exist_ok=True)
        patch.write_text(self.FIX_PATCH, encoding="utf-8")
        run_fix(patch, self.root, "fix-success")
        manifest = load_mapping(self.root / "runs/fix-success/manifest.yaml")
        self.assertEqual(manifest["status"], "completed")
        self.assertEqual(manifest["branch"], target_branch(self.root))
        self.assertNotEqual(command(["git", "rev-parse", "HEAD"], repo), base_commit)
        self.assertNotIn("commit", manifest)
        self.assertNotIn("from_run_id", manifest)
        self.assertEqual(manifest["source_check_report_ids"], ["check-finding"])
        self.assertEqual(
            {item.name for item in (self.root / "runs/check-finding").iterdir()},
            {"report.md"},
        )
        self.assertEqual(
            command(["git", "show", "HEAD:code.txt"], repo), "good"
        )
        self.assertEqual(command(["git", "show", "HEAD:test-marker.txt"], repo), "test retained")

    def test_failed_regression_keeps_changes_on_negotiated_branch_without_commit(self) -> None:
        repo, base_commit = self.prepare_failed_check()
        patch = self.root / "fix-input/ineffective.patch"
        patch.parent.mkdir(parents=True)
        patch.write_text(self.INEFFECTIVE_PATCH, encoding="utf-8")
        run_fix(patch, self.root, "fix-failed")
        manifest = load_mapping(self.root / "runs/fix-failed/manifest.yaml")
        self.assertEqual(manifest["status"], "failed")
        self.assertNotIn("worktree", manifest)
        self.assertEqual(manifest["branch"], target_branch(self.root))
        self.assertEqual(command(["git", "rev-parse", "HEAD"], repo), base_commit)
        self.assertIn("unrelated.txt", command(["git", "status", "--short"], repo))

    def test_manual_finding_edit_without_timestamp_is_rejected(self) -> None:
        _repo, _base_commit = self.prepare_failed_check()
        check = load_check_report(self.root, "check-finding")
        finding_id = check["finding_ids"][0]
        path = self.root / "targets/starry/findings" / f"{slug(finding_id)}.yaml"
        finding = load_mapping(path)
        finding["manual_note"] = "edited without generation update"
        atomic_write_yaml(path, finding)
        with self.assertRaisesRegex(SyscallGuardError, "finding index version is stale"):
            prepare_fix(self.root, "fix-stale-finding")
        self.assertFalse((self.root / "runs/fix-stale-finding").exists())

    def test_prepare_rejects_a_different_current_branch(self) -> None:
        repo, _base_commit = self.prepare_failed_check()
        command(["git", "switch", "-c", "different-fix-branch"], repo)
        with self.assertRaisesRegex(SyscallGuardError, "target branch or snapshot differs"):
            prepare_fix(self.root, "fix-wrong-branch")

    def test_no_open_findings_creates_no_run_or_branch_change(self) -> None:
        self.prepare_spec_run()
        self.add_static_check("bad")
        _repo, descriptor, _commit = self.make_target()
        self.map_fixture(descriptor)
        run_check("mapping-fixture", self.root, "check-clean")
        result = prepare_fix(self.root, "fix-empty")
        self.assertEqual(result["status"], "no_open_findings")
        self.assertFalse((self.root / "runs/fix-empty").exists())
        self.assertFalse((FIX_TEMP_ROOT / "fix-empty").exists())

    def test_prepare_uses_index_when_newest_legacy_report_has_no_findings(self) -> None:
        self.prepare_failed_check()
        older = load_check_report(self.root, "check-finding")
        newest = dict(older)
        newest.pop("content_hash", None)
        newest["report_id"] = "check-newest-empty"
        newest["generated_at_utc"] = "2026-12-31T23:59:59.000000Z"
        newest["finding_ids"] = []
        newest["finding_versions"] = {}
        newest["counts"] = dict(newest["counts"])
        newest["counts"]["findings"] = 0
        newest["content_hash"] = version_content_hash(newest)
        atomic_write_text(
            self.root / "runs/check-newest-empty/report.md",
            markdown_report(newest),
        )

        preparation = prepare_fix(self.root, "fix-index-discovery")
        self.assertEqual(preparation["status"], "prepared")
        self.assertEqual(len(preparation["selected_finding_ids"]), 1)
        self.assertEqual(
            preparation["source_check_report_ids"], ["check-finding"]
        )

    def test_cli_has_no_from_parameter_and_supports_internal_finalize(self) -> None:
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            build_fix_parser().parse_args(["--from", "check-old"])
        parsed = build_fix_parser().parse_args([])
        self.assertIsNone(parsed.finalize)
        self.assertEqual(
            build_fix_parser().parse_args(["--finalize", "fix-prepared"]).finalize,
            "fix-prepared",
        )

    def test_finalize_revalidates_prepared_finding_version(self) -> None:
        _repo, _base_commit = self.prepare_failed_check()
        preparation = prepare_fix(self.root, "fix-prepared-stale")
        Path(preparation["implementation_patch"]).write_text(
            self.FIX_PATCH, encoding="utf-8"
        )
        finding_id = preparation["selected_finding_ids"][0]
        path = self.root / "targets/starry/findings" / f"{slug(finding_id)}.yaml"
        finding = load_mapping(path)
        finding["generated_at_utc"] = "2026-12-31T00:00:00.000000Z"
        atomic_write_yaml(path, finding)
        index = load_mapping(self.root / "targets/starry/findings/index.yaml")
        row = next(item for item in index["entities"] if item["id"] == finding_id)
        row["generated_at_utc"] = finding["generated_at_utc"]
        row["content_hash"] = version_content_hash(finding)
        atomic_write_yaml(self.root / "targets/starry/findings/index.yaml", index)
        finalize_fix("fix-prepared-stale", self.root)
        manifest = load_mapping(self.root / "runs/fix-prepared-stale/manifest.yaml")
        self.assertEqual(manifest["status"], "completed_with_blockers")
        self.assertEqual(manifest["blockers"][0]["kind"], "stale_preparation")

    def test_branch_execution_failure_keeps_attributable_terminal_run(self) -> None:
        self.prepare_failed_check()
        preparation = prepare_fix(self.root, "fix-worktree-blocked")
        Path(preparation["implementation_patch"]).write_text(
            self.FIX_PATCH, encoding="utf-8"
        )
        with mock.patch(
            "syscallguard.fixing._apply_test_patches",
            side_effect=SyscallGuardError("branch execution denied"),
        ):
            with self.assertRaisesRegex(SyscallGuardError, "branch execution denied"):
                finalize_fix("fix-worktree-blocked", self.root)
        manifest = load_mapping(
            self.root / "runs/fix-worktree-blocked/manifest.yaml"
        )
        self.assertEqual(manifest["status"], "failed")
        self.assertEqual(manifest["source_check_report_ids"], ["check-finding"])
        self.assertEqual(len(manifest["entities"]["findings"]), 1)
        self.assertTrue(
            (self.root / "runs/fix-worktree-blocked/report.md").is_file()
        )

    def test_repairs_all_findings_from_multiple_reports_with_merged_scope(self) -> None:
        self.prepare_spec_run()
        self.add_static_check("good")
        test_patch = self.root / "targets/starry/dynamic-tests/assets/test.patch"
        test_patch.parent.mkdir(parents=True, exist_ok=True)
        test_patch.write_text(self.TEST_PATCH, encoding="utf-8")
        self.add_dynamic_test(
            "DYNAMIC_ONE",
            ["/bin/true"],
            "targets/starry/dynamic-tests/assets/test.patch",
        )
        repo, descriptor, base_commit = self.make_target()
        self.map_fixture(descriptor)
        run_check("mapping-fixture", self.root, "check-first-source")
        first_ids = load_check_report(self.root, "check-first-source")["finding_ids"]
        self.assertEqual(len(first_ids), 1)

        self.add_second_rule_and_checks()
        run_mapping(
            None, self.root, "mapping-second-source", target_branch(self.root)
        )
        run_check("mapping-second-source", self.root, "check-second-source")
        second = load_check_report(self.root, "check-second-source")
        self.assertEqual(len(second["finding_ids"]), 2)

        patch = self.root / "fix-input/combined.patch"
        patch.parent.mkdir(parents=True, exist_ok=True)
        patch.write_text(self.FIX_PATCH, encoding="utf-8")
        run_fix(patch, self.root, "fix-combined")
        manifest = load_mapping(self.root / "runs/fix-combined/manifest.yaml")
        self.assertEqual(manifest["status"], "completed")
        self.assertEqual(manifest["counts"]["selected_findings"], 2)
        self.assertEqual(
            manifest["source_check_report_ids"],
            ["check-first-source", "check-second-source"],
        )
        self.assertEqual(
            set(manifest["regression_scope"]["static_checks"]),
            {"CHECK_ONE", "CHECK_TWO"},
        )
        self.assertEqual(
            set(manifest["regression_scope"]["dynamic_tests"]),
            {"DYNAMIC_ONE", "DYNAMIC_TWO"},
        )
        self.assertNotEqual(command(["git", "rev-parse", "HEAD"], repo), base_commit)
        self.assertEqual(
            command(["git", "show", "HEAD:test-marker.txt"], repo),
            "test retained",
        )
        for finding_id in second["finding_ids"]:
            finding = load_mapping(
                self.root / "targets/starry/findings" / f"{slug(finding_id)}.yaml"
            )
            self.assertEqual(finding["resolution"], "fixed")
            index = load_mapping(self.root / "targets/starry/findings/index.yaml")
            row = next(item for item in index["entities"] if item["id"] == finding_id)
            self.assertEqual(row["generated_at_utc"], finding["generated_at_utc"])
            self.assertEqual(row["content_hash"], version_content_hash(finding))


class ResetTests(unittest.TestCase):
    def test_reset_removes_only_rules_and_ingest_reports(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            (root / "sources").mkdir()
            (root / "syscallguard").mkdir()
            atomic_write_yaml(root / "library/rules/one.yaml", {"rule": "one"})
            atomic_write_yaml(root / "library/syscalls.yaml", {"one": ["rule-one"]})
            atomic_write_text(root / "runs/spec-one/report.md", "history\n")
            atomic_write_text(root / "runs/spec-kept/note.txt", "keep\n")
            atomic_write_text(root / "runs/spec-kept/report.md", "history\n")
            atomic_write_text(root / "runs/mapping-one/report.md", "keep\n")
            atomic_write_yaml(root / "targets/starry/static-checks.yaml", {"keep": True})
            result = reset_project(root)
            self.assertEqual(result["removed_rule_count"], 1)
            self.assertEqual(result["removed_report_count"], 2)
            self.assertFalse((root / "library/rules/one.yaml").exists())
            self.assertFalse((root / "library/syscalls.yaml").exists())
            self.assertTrue((root / "runs/spec-kept/note.txt").exists())
            self.assertTrue((root / "runs/mapping-one/report.md").exists())
            self.assertTrue((root / "targets/starry/static-checks.yaml").exists())


class RepositoryMappingScopeTests(unittest.TestCase):
    def test_current_rule_library_has_expected_full_and_filtered_scopes(self) -> None:
        root = Path(__file__).resolve().parents[1]
        index = load_mapping(root / "library/syscalls.yaml")["syscalls"]
        all_rules = {
            row["rule_id"] for refs in index.values() for row in refs
        }
        self.assertEqual(len(all_rules), 386)
        self.assertEqual(len({row["rule_id"] for row in index["mmap"]}), 9)
        self.assertEqual(len({row["rule_id"] for row in index["close"]}), 5)


if __name__ == "__main__":
    unittest.main()
