from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path
from typing import Any

import yaml

from syscallguard.checking import run_check
from syscallguard.common import SyscallGuardError, atomic_write_yaml, load_mapping, slug, update_index
from syscallguard.fixing import run_fix
from syscallguard.ingest import run_ingest
from syscallguard.mapping import run_mapping


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


def write_run(
    root: Path,
    run_id: str,
    stage: str,
    status: str,
    entities: dict[str, list[str]],
    from_run: str | None = None,
) -> None:
    directory = root / "runs" / run_id
    directory.mkdir(parents=True, exist_ok=True)
    atomic_write_yaml(
        directory / "manifest.yaml",
        {
            "schema_version": 1,
            "kind": "syscallguard_run",
            "run_id": run_id,
            "stage": stage,
            "status": status,
            "created_at_utc": "2026-01-01T00:00:00Z",
            "completed_at_utc": "2026-01-01T00:00:00Z",
            "from_run_id": from_run,
            "invocation": {},
            "entities": entities,
            "entity_hashes": {},
            "outputs": {},
            "counts": {},
            "blockers": [],
            "error": None,
        },
    )
    atomic_write_yaml(directory / "changeset.yaml", {"changes": [], "conflicts": []})


FAKE_EXTRACTOR = '''\
from dataclasses import dataclass
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
ALIASES = {}

@dataclass
class ManifestEntry:
    name: str
    group: str
    ltp_dirs: list[str]

def build_candidates(entries):
    rows = []
    for entry in entries:
        value = (ROOT / "testcases/kernel/syscalls" / entry.name / "case.txt").read_text().strip()
        rows.append({"syscall": entry.name, "source": {"file": f"testcases/kernel/syscalls/{entry.name}/case.txt", "line": 1}, "errno": value})
    return rows, [{"syscall": row["syscall"]} for row in rows]

def normalize_specs(candidates):
    return [{"syscall": row["syscall"], "case": row["syscall"] + "_case", "rule_id": "SHARED_RULE", "source": row["source"], "args": [], "preconditions": [], "expected": {"kind": "return_errno", "errno": row["errno"]}, "confidence": "A", "checkability": "static_direct", "status": "normalized"} for row in candidates]

def write_candidates(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump({"candidates": rows}, sort_keys=False))

def write_normalized_specs(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump({"specs": rows}, sort_keys=False))
'''


class FlowTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "syscallguard"
        self.root.mkdir()
        (self.root / "batches").mkdir()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def make_ltp(self) -> tuple[Path, Path]:
        source = Path(self.temp.name) / "ltp"
        init_repo(
            source,
            {
                "tools/syscall_spec_extract.py": FAKE_EXTRACTOR,
                "testcases/kernel/syscalls/alpha/case.txt": "EBADF\n",
                "testcases/kernel/syscalls/beta/case.txt": "EINVAL\n",
            },
        )
        descriptor = self.root / "source.yaml"
        atomic_write_yaml(
            descriptor,
            {
                "source_id": "fixture-ltp",
                "adapter": "ltp-extractor",
                "location": str(source),
                "revision": "HEAD",
                "parameters": {
                    "tool": "tools/syscall_spec_extract.py",
                    "syscalls": ["alpha", "beta"],
                },
            },
        )
        return source, descriptor

    def make_target(self, code: str = "bad\n") -> tuple[Path, Path, str]:
        repo = Path(self.temp.name) / "starry"
        commit = init_repo(repo, {"code.txt": code})
        descriptor = self.root / "target.yaml"
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
        spec = {
            "schema_version": 1,
            "kind": "syscallguard_syscall_spec",
            "syscall": "alpha",
            "source_records": [],
            "normalized_behaviors": [],
            "rule_refs": ["RULE_ONE"],
            "source_fingerprint": "sha256:fixture",
            "last_processed_run": "spec-fixture",
        }
        rule = {
            "schema_version": 1,
            "kind": "syscallguard_rule",
            "rule_id": "RULE_ONE",
            "semantics": {
                "preconditions": [],
                "action": {"operation": "read code"},
                "expected_result": "good",
                "errno": [],
            },
            "provenance": [],
            "last_processed_run": "spec-fixture",
        }
        atomic_write_yaml(self.root / "library/specs/alpha.yaml", spec)
        atomic_write_yaml(self.root / "library/rules/rule-one.yaml", rule)
        update_index(
            self.root / "library/specs/index.yaml",
            "syscallguard_spec_index",
            [{"id": "alpha", "path": "library/specs/alpha.yaml"}],
        )
        update_index(
            self.root / "library/rules/index.yaml",
            "syscallguard_rule_index",
            [{"id": "RULE_ONE", "path": "library/rules/rule-one.yaml"}],
        )
        write_run(
            self.root,
            "spec-fixture",
            "spec",
            "completed",
            {"syscalls": ["alpha"], "rules": ["RULE_ONE"]},
        )

    def add_static_check(self, regex: str = "good") -> None:
        entity = {
            "schema_version": 1,
            "kind": "syscallguard_starry_static_check",
            "check_id": "CHECK_ONE",
            "rule_refs": ["RULE_ONE"],
            "applies_to_syscalls": ["alpha"],
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
        return run_mapping("spec-fixture", descriptor, self.root, run_id)


class IngestTests(FlowTestCase):
    def test_new_unchanged_changed_shortage_and_conflict(self) -> None:
        source, descriptor = self.make_ltp()
        first = run_ingest(descriptor, 1, self.root, "spec-first")
        first_manifest = load_mapping(self.root / "runs" / first / "manifest.yaml")
        self.assertEqual(first_manifest["selection"]["selected"], ["alpha"])

        second = run_ingest(descriptor, 5, self.root, "spec-second")
        second_manifest = load_mapping(self.root / "runs" / second / "manifest.yaml")
        self.assertEqual(second_manifest["selection"]["selected"], ["beta"])
        self.assertEqual(second_manifest["selection"]["available_count"], 1)
        self.assertEqual(second_manifest["counts"]["semantic_conflicts"], 1)
        self.assertTrue(second_manifest["entities"]["rules"][0].startswith("SHARED_RULE--"))

        third = run_ingest(descriptor, 5, self.root, "spec-third")
        self.assertEqual(
            load_mapping(self.root / "runs" / third / "manifest.yaml")["counts"]["selected_syscalls"],
            0,
        )

        commit_file(source, "testcases/kernel/syscalls/alpha/case.txt", "EFAULT\n")
        fourth = run_ingest(descriptor, 5, self.root, "spec-fourth")
        self.assertEqual(
            load_mapping(self.root / "runs" / fourth / "manifest.yaml")["selection"]["selected"],
            ["alpha"],
        )

    def test_invalid_count_and_missing_source(self) -> None:
        _source, descriptor = self.make_ltp()
        with self.assertRaisesRegex(SyscallGuardError, "positive integer"):
            run_ingest(descriptor, 0, self.root, "spec-invalid")
        value = load_mapping(descriptor)
        value["location"] = str(Path(self.temp.name) / "missing")
        atomic_write_yaml(descriptor, value)
        with self.assertRaisesRegex(SyscallGuardError, "does not exist"):
            run_ingest(descriptor, 1, self.root, "spec-missing")
        self.assertEqual(
            load_mapping(self.root / "runs/spec-missing/manifest.yaml")["status"], "failed"
        )


class MappingTests(FlowTestCase):
    def test_manual_rule_edit_reprocesses_and_target_change_stales_old_mapping(self) -> None:
        self.prepare_spec_run()
        repo, descriptor, old_commit = self.make_target()
        self.map_fixture(descriptor, "mapping-old")
        rule_path = self.root / "library/rules/rule-one.yaml"
        rule = load_mapping(rule_path)
        rule["manual_note"] = "edited"
        atomic_write_yaml(rule_path, rule)
        run_mapping("spec-fixture", descriptor, self.root, "mapping-edited")
        changes = load_mapping(self.root / "runs/mapping-edited/changeset.yaml")["changes"]
        mapping_change = next(row for row in changes if row["entity_type"] == "mapping")
        self.assertEqual(mapping_change["action"], "updated")

        new_commit = commit_file(repo, "code.txt", "new target\n")
        self.assertNotEqual(old_commit, new_commit)
        stale_check = run_check("mapping-edited", self.root, "check-stale")
        stale_manifest = load_mapping(self.root / "runs" / stale_check / "manifest.yaml")
        self.assertEqual(stale_manifest["status"], "completed_with_blockers")
        self.assertEqual(stale_manifest["blockers"][0]["kind"], "stale_mapping")
        run_mapping("spec-fixture", descriptor, self.root, "mapping-new-target")
        self.assertEqual(
            load_mapping(self.root / "runs/mapping-new-target/manifest.yaml")["target"]["base_commit"],
            new_commit,
        )

    def test_bad_from_run_rejected(self) -> None:
        self.prepare_spec_run()
        _repo, descriptor, _commit = self.make_target()
        write_run(self.root, "failed-spec", "spec", "failed", {"syscalls": [], "rules": []})
        with self.assertRaisesRegex(SyscallGuardError, "not readable"):
            run_mapping("failed-spec", descriptor, self.root, "mapping-from-failed")
        write_run(self.root, "wrong-stage", "mapping", "completed", {})
        with self.assertRaisesRegex(SyscallGuardError, "expected 'spec'"):
            run_mapping("wrong-stage", descriptor, self.root, "mapping-from-wrong")
        with self.assertRaisesRegex(SyscallGuardError, "missing YAML"):
            run_mapping("does-not-exist", descriptor, self.root, "mapping-from-missing")


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
        self.assertGreaterEqual(len(manifest["entities"]["findings"]), 1)
        for finding_id in manifest["entities"]["findings"]:
            finding = load_mapping(
                self.root / "targets/starry/findings" / f"{finding_id.lower()}.yaml"
            )
            self.assertNotIn("No space left on device", yaml.safe_dump(finding))


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
        self.assertEqual((repo / "code.txt").read_text(encoding="utf-8"), "bad\n")
        self.assertEqual(
            command(["git", "show", f"{manifest['commit']}:test-marker.txt"], repo),
            "test retained",
        )
        self.assertEqual(command(["git", "show", f"{manifest['commit']}:code.txt"], repo), "good")

    def test_failed_regression_keeps_worktree_and_creates_no_branch(self) -> None:
        repo, _base_commit = self.prepare_failed_check()
        patch = self.root / "runs/check-finding/implementation-fix.patch"
        patch.write_text(self.INEFFECTIVE_PATCH, encoding="utf-8")
        run_fix("check-finding", None, self.root, "fix-failed")
        manifest = load_mapping(self.root / "runs/fix-failed/manifest.yaml")
        self.assertEqual(manifest["status"], "failed")
        self.assertTrue(Path(manifest["worktree"]).is_dir())
        self.assertEqual(
            command(["git", "branch", "--list", "syscallguard/fix-failed"], repo), ""
        )


if __name__ == "__main__":
    unittest.main()
