from __future__ import annotations

import io
import subprocess
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest import mock

import yaml

from syscallguard.checking import run_check
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
)
from syscallguard.fixing import run_fix
from syscallguard.ingest import (
    build_parser as build_ingest_parser,
    resolve_count,
    resolve_source,
    resolve_syscalls,
    run_ingest,
)
from syscallguard.mapping import (
    build_parser as build_mapping_parser,
    finalize_mapping,
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
        self.temp.cleanup()

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
                "revision": "HEAD",
                "worktree_root": str(self.root / "worktrees"),
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
        update_index(
            self.root / "targets/starry/static-checks/index.yaml",
            "syscallguard_starry_static_check_index",
            [
                {
                    "id": "CHECK_ONE",
                    "path": "targets/starry/static-checks/check-one.yaml",
                    "rule_refs": ["RULE_ONE"],
                }
            ],
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
        update_index(
            self.root / "targets/starry/dynamic-tests/index.yaml",
            "syscallguard_starry_dynamic_test_index",
            [
                {
                    "id": test_id,
                    "path": str(path.relative_to(self.root)),
                    "rule_refs": ["RULE_ONE"],
                }
            ],
        )

    def map_fixture(self, descriptor: Path, run_id: str = "mapping-fixture") -> str:
        self.assertEqual(descriptor, self.root / "targets/starry/target.yaml")
        return run_mapping(None, self.root, run_id)


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
                    "void run(void) { TST_EXP_FAIL(alpha(), EBADF); }\n"
                ),
                "testcases/kernel/syscalls/beta/beta.c": (
                    "void run(void) { TST_EXP_EXPR(beta()); }\n"
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
        self.assertEqual(rows["beta"]["result"], "no_rules")
        self.assertEqual(rows["beta"]["unresolved_evidence_count"], 1)
        self.assertEqual(rows["beta"]["rules"], [])
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
        run_mapping(None, self.root, "mapping-after-provenance")

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
    def test_preseeded_pending_rule_is_counted_as_added(self) -> None:
        self.prepare_spec_run()
        rule = load_mapping(self.root / "library/rules/rule-one.yaml")
        atomic_write_yaml(
            self.root / "targets/starry/rule-coverage.yaml",
            {
                "schema_version": 1,
                "kind": "syscallguard_starry_rule_coverage",
                "updated_at_utc": None,
                "target": {
                    "target_id": "starry",
                    "repository_identity": None,
                    "descriptor_hash": None,
                    "last_snapshot_hash": None,
                },
                "rules": {
                    "RULE_ONE": {
                        "syscalls": ["alpha"],
                        "rule_version": entity_version("RULE_ONE", rule),
                        "status": "pending",
                        "classification": None,
                        "mapping_refs": [],
                        "static_check_refs": [],
                        "dynamic_test_refs": [],
                        "artifact_versions": {},
                        "target_dependencies": [],
                        "repository_identity": None,
                        "target_descriptor_hash": None,
                        "last_verified_snapshot_hash": None,
                        "last_processed_run": None,
                        "reason": "initial_coverage",
                    }
                },
            },
        )
        _repo, _descriptor, _snapshot = self.make_target("good\n")
        run_mapping(None, self.root, "mapping-first-attempt")
        manifest = load_mapping(self.root / "runs/mapping-first-attempt/manifest.yaml")
        self.assertEqual(manifest["counts"]["added"], 1)
        self.assertEqual(manifest["counts"]["updated"], 0)

    def test_rule_library_manifest_and_content_staleness(self) -> None:
        self.prepare_spec_run()
        self.add_static_check("good")
        repo, descriptor, _old_commit = self.make_target("good\n")
        self.map_fixture(descriptor, "mapping-old")
        manifest = load_mapping(self.root / "runs/mapping-old/manifest.yaml")
        self.assertNotIn("from_report_id", manifest)
        self.assertNotIn("base_commit", manifest["target"])
        self.assertIn("rule_index_hash", manifest)
        self.assertEqual(manifest["selected_rule_versions"]["RULE_ONE"]["id"], "RULE_ONE")
        self.assertEqual(manifest["rule_syscalls"], {"RULE_ONE": ["alpha"]})
        coverage = load_mapping(self.root / "targets/starry/rule-coverage.yaml")
        self.assertEqual(coverage["rules"]["RULE_ONE"]["status"], "mapped")

        unrelated_snapshot = commit_file(repo, "unrelated.txt", "unrelated\n")
        self.assertTrue(unrelated_snapshot)
        run_mapping(None, self.root, "mapping-unrelated")
        unrelated = load_mapping(self.root / "runs/mapping-unrelated/manifest.yaml")
        self.assertEqual(unrelated["counts"]["processed"], 0)
        self.assertEqual(unrelated["counts"]["skipped"], 1)

        commit_file(repo, "code.txt", "changed target\n")
        prepared = prepare_mapping(None, self.root, "mapping-related")
        preparation = load_mapping(self.root / f"runs/{prepared}/preparation.yaml")
        self.assertEqual(preparation["selected_rule_ids"], ["RULE_ONE"])

        run_check("mapping-old", self.root, "check-stale")
        stale = load_mapping(self.root / "runs/check-stale/manifest.yaml")
        self.assertEqual(stale["blockers"][0]["kind"], "stale_mapping")

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
        run_mapping("alpha", self.root, "mapping-alpha")
        coverage = load_mapping(self.root / "targets/starry/rule-coverage.yaml")
        self.assertEqual(coverage["rules"]["RULE_ONE"]["status"], "needs_review")
        self.assertEqual(coverage["rules"]["RULE_TWO"]["status"], "pending")

        run_id = prepare_mapping(" alpha,ALPHA ", self.root, "mapping-same")
        same = load_mapping(self.root / f"runs/{run_id}/preparation.yaml")
        self.assertEqual(same["selected_rule_ids"], [])
        finalize_mapping(run_id, self.root)
        commit_file(repo, "code.txt", "new content\n")
        retry_id = prepare_mapping("alpha", self.root, "mapping-retry")
        retry = load_mapping(self.root / f"runs/{retry_id}/preparation.yaml")
        self.assertEqual(retry["selected_rule_ids"], ["RULE_ONE"])

        self.assertEqual(resolve_mapping_syscalls(" beta,Alpha,alpha "), ["alpha", "beta"])
        self.assertIsNone(resolve_mapping_syscalls(None))
        args = build_mapping_parser().parse_args(["--syscalls", "alpha,beta"])
        self.assertEqual(args.syscalls, "alpha,beta")
        with mock.patch("sys.stderr", new=io.StringIO()):
            with self.assertRaisesRegex(SystemExit, "2"):
                build_mapping_parser().parse_args(["--from", "spec-old"])
        with self.assertRaisesRegex(SyscallGuardError, "do not exist"):
            prepare_mapping("missing", self.root, "mapping-missing")

    def test_all_mapping_classifications_publish_resolvable_references(self) -> None:
        self.prepare_spec_run()
        index = load_mapping(self.root / "library/syscalls.yaml")
        base = load_mapping(self.root / "library/rules/rule-one.yaml")
        rule_ids = {
            "RULE_ONE": "static",
            "RULE_DYNAMIC": "dynamic",
            "RULE_PARTIAL": "partial_static",
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
        run_id = prepare_mapping(None, self.root, "mapping-five-kinds")
        staged_root = self.root / f"runs/{run_id}/staged/targets/starry"

        for rule_id, classification in rule_ids.items():
            static_refs = [f"CHECK_{rule_id}"] if classification in {"static", "partial_static"} else []
            dynamic_refs = [f"TEST_{rule_id}"] if classification in {"dynamic", "partial_static"} else []
            mapping = {
                "schema_version": 1,
                "kind": "syscallguard_starry_mapping",
                "mapping_id": f"STARRY_{rule_id}",
                "rule_refs": [rule_id],
                "classification": classification,
                "target_locations": (
                    [{"path": "code.txt", "symbols": []}]
                    if classification in {"static", "partial_static", "dynamic"}
                    else []
                ),
                "static_check_refs": static_refs,
                "dynamic_test_refs": dynamic_refs,
                "reason": f"fixture {classification}",
            }
            atomic_write_yaml(
                staged_root / "mappings" / f"{slug(mapping['mapping_id'])}.yaml", mapping
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
                atomic_write_yaml(
                    staged_root / "dynamic-tests" / f"{slug(test_id)}.yaml",
                    {
                        "schema_version": 1,
                        "kind": "syscallguard_starry_dynamic_test",
                        "test_id": test_id,
                        "rule_refs": [rule_id],
                        "test_source": "fixture.c",
                        "build": {"kind": "fixture"},
                        "command": ["/bin/true"],
                    },
                )

        finalize_mapping(run_id, self.root)
        coverage = load_mapping(self.root / "targets/starry/rule-coverage.yaml")["rules"]
        self.assertEqual(coverage["RULE_ONE"]["status"], "mapped")
        self.assertEqual(coverage["RULE_DYNAMIC"]["classification"], "dynamic")
        self.assertEqual(coverage["RULE_PARTIAL"]["classification"], "partial_static")
        self.assertEqual(coverage["RULE_UNSUPPORTED"]["status"], "unsupported")
        self.assertEqual(coverage["RULE_REVIEW"]["status"], "needs_review")
        manifest = load_mapping(self.root / f"runs/{run_id}/manifest.yaml")
        self.assertEqual(manifest["counts"]["static_checks"], 2)
        self.assertEqual(manifest["counts"]["dynamic_tests"], 2)

    def test_finalizer_failure_does_not_advance_shared_state(self) -> None:
        self.prepare_spec_run()
        _repo, _descriptor, _snapshot = self.make_target("good\n")
        run_id = prepare_mapping(None, self.root, "mapping-publish-failure")
        with mock.patch(
            "syscallguard.mapping._transactional_write", side_effect=OSError("publish failed")
        ):
            with self.assertRaisesRegex(SyscallGuardError, "publish failed"):
                finalize_mapping(run_id, self.root)
        self.assertFalse((self.root / "targets/starry/rule-coverage.yaml").exists())
        self.assertFalse(
            (self.root / "targets/starry/mappings/starry-rule-one.yaml").exists()
        )
        manifest = load_mapping(self.root / f"runs/{run_id}/manifest.yaml")
        self.assertEqual(manifest["status"], "failed")


class CheckTests(FlowTestCase):
    def test_pass_and_identical_input_skip_in_isolated_worktree(self) -> None:
        self.prepare_spec_run()
        self.add_static_check("bad")
        repo, descriptor, commit = self.make_target()
        self.map_fixture(descriptor)
        before = command(["git", "status", "--short"], repo)
        run_check("mapping-fixture", self.root, "check-first")
        first = load_mapping(self.root / "runs/check-first/manifest.yaml")
        self.assertEqual(first["status"], "completed")
        self.assertEqual(first["counts"]["static_pass"], 1)
        self.assertEqual(command(["git", "rev-parse", "HEAD"], repo), commit)
        self.assertEqual(command(["git", "status", "--short"], repo), before)

        run_check("mapping-fixture", self.root, "check-second")
        second = load_mapping(self.root / "runs/check-second/manifest.yaml")
        self.assertEqual(second["reused_run"], "check-first")
        self.assertEqual(second["counts"]["skipped_unchanged"], 1)

    def test_findings_use_mapping_syscall_ownership(self) -> None:
        self.prepare_spec_run()
        self.add_static_check("good", ["alpha", "beta"])
        _repo, descriptor, _commit = self.make_target()
        self.map_fixture(descriptor)
        run_check("mapping-fixture", self.root, "check-ownership")
        manifest = load_mapping(self.root / "runs/check-ownership/manifest.yaml")
        self.assertTrue(manifest["entities"]["findings"])
        for finding_id in manifest["entities"]["findings"]:
            finding = load_mapping(
                self.root / "targets/starry/findings" / f"{slug(finding_id)}.yaml"
            )
            self.assertEqual(finding["syscall"], "alpha")

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
        _repo, descriptor, _commit = self.make_target()
        self.map_fixture(descriptor)
        run_check("mapping-fixture", self.root, "check-mixed")
        manifest = load_mapping(self.root / "runs/check-mixed/manifest.yaml")
        results = load_mapping(self.root / "runs/check-mixed/results.yaml")
        self.assertEqual(manifest["status"], "completed_with_blockers")
        self.assertEqual(
            {row["test_id"]: row["result"] for row in results["dynamic"]},
            {
                "DYNAMIC_BLOCKER": "not_run",
                "DYNAMIC_FAIL": "fail",
                "DYNAMIC_SKIPPED": "skipped",
            },
        )
        for finding_id in manifest["entities"]["findings"]:
            finding = load_mapping(
                self.root / "targets/starry/findings" / f"{slug(finding_id)}.yaml"
            )
            self.assertNotIn("No space left on device", yaml.safe_dump(finding))

    def test_manual_check_edit_without_timestamp_is_rejected(self) -> None:
        self.prepare_spec_run()
        self.add_static_check("bad")
        _repo, descriptor, _commit = self.make_target()
        self.map_fixture(descriptor)
        path = self.root / "targets/starry/static-checks/check-one.yaml"
        entity = load_mapping(path)
        entity["patterns"][0]["regex"] = "manual-change"
        atomic_write_yaml(path, entity)
        run_check("mapping-fixture", self.root, "check-manual-stale")
        manifest = load_mapping(self.root / "runs/check-manual-stale/manifest.yaml")
        self.assertEqual(manifest["status"], "completed_with_blockers")
        self.assertIn("content changed", manifest["blockers"][0]["dependency_mismatches"][0])


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
        test_patch = self.root / "test.patch"
        test_patch.write_text(self.TEST_PATCH, encoding="utf-8")
        self.add_dynamic_test("DYNAMIC_PASS", ["/bin/true"], "test.patch")
        repo, descriptor, base_commit = self.make_target()
        self.map_fixture(descriptor)
        run_check("mapping-fixture", self.root, "check-finding")
        check_manifest = load_mapping(self.root / "runs/check-finding/manifest.yaml")
        self.assertEqual(check_manifest["counts"]["static_fail"], 1)
        self.assertEqual(check_manifest["counts"]["dynamic_pass"], 1)
        return repo, base_commit

    def test_success_commits_fix_and_injected_test_without_touching_original_branch(self) -> None:
        repo, base_commit = self.prepare_failed_check()
        patch = self.root / "runs/check-finding/implementation-fix.patch"
        patch.write_text(self.FIX_PATCH, encoding="utf-8")
        run_fix("check-finding", None, self.root, "fix-success")
        manifest = load_mapping(self.root / "runs/fix-success/manifest.yaml")
        self.assertEqual(manifest["status"], "completed")
        self.assertEqual(manifest["branch"], "syscallguard/fix-success")
        self.assertEqual(command(["git", "rev-parse", "HEAD"], repo), base_commit)
        self.assertNotIn("commit", manifest)
        self.assertEqual(
            command(["git", "show", f"{manifest['branch']}:code.txt"], repo), "good"
        )

    def test_failed_regression_keeps_worktree_and_creates_no_branch(self) -> None:
        repo, _base_commit = self.prepare_failed_check()
        patch = self.root / "runs/check-finding/implementation-fix.patch"
        patch.write_text(self.INEFFECTIVE_PATCH, encoding="utf-8")
        run_fix("check-finding", None, self.root, "fix-failed")
        manifest = load_mapping(self.root / "runs/fix-failed/manifest.yaml")
        self.assertEqual(manifest["status"], "failed")
        self.assertTrue(Path(manifest["worktree"]).is_dir())
        self.assertEqual(command(["git", "branch", "--list", "syscallguard/fix-failed"], repo), "")

    def test_manual_finding_edit_without_timestamp_is_rejected(self) -> None:
        _repo, _base_commit = self.prepare_failed_check()
        check = load_mapping(self.root / "runs/check-finding/manifest.yaml")
        finding_id = check["entities"]["findings"][0]
        path = self.root / "targets/starry/findings" / f"{slug(finding_id)}.yaml"
        finding = load_mapping(path)
        finding["manual_note"] = "edited without generation update"
        atomic_write_yaml(path, finding)
        run_fix("check-finding", None, self.root, "fix-stale-finding")
        manifest = load_mapping(self.root / "runs/fix-stale-finding/manifest.yaml")
        self.assertEqual(manifest["status"], "completed_with_blockers")
        self.assertEqual(manifest["blockers"][0]["kind"], "stale_check")


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
            atomic_write_yaml(root / "targets/starry/mappings/index.yaml", {"keep": True})
            result = reset_project(root)
            self.assertEqual(result["removed_rule_count"], 1)
            self.assertEqual(result["removed_report_count"], 2)
            self.assertFalse((root / "library/rules/one.yaml").exists())
            self.assertFalse((root / "library/syscalls.yaml").exists())
            self.assertTrue((root / "runs/spec-kept/note.txt").exists())
            self.assertTrue((root / "runs/mapping-one/report.md").exists())
            self.assertTrue((root / "targets/starry/mappings/index.yaml").exists())


if __name__ == "__main__":
    unittest.main()
