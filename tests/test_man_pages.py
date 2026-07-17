from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from syscallguard.adapters.man_pages import ManPagesAdapter
from syscallguard.common import SyscallGuardError, atomic_write_yaml, load_mapping
from syscallguard.ingest import run_ingest


class ManPagesAdapterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.manual = self.root / "man-pages"
        self.linux = self.root / "linux"
        for section in ("man2", "man2const", "man2type", "man7"):
            (self.manual / "man" / section).mkdir(parents=True, exist_ok=True)
        inputs = {
            "arch/riscv/include/generated/uapi/asm/unistd_64.h": (
                "#define __NR_alpha 1\n"
                "#define __NR_beta 2\n"
                "#define __NR_missing 3\n"
                "#define __NR_syscalls 4\n"
            ),
            "scripts/syscall.tbl": "1 common alpha sys_alpha\n",
            "include/linux/syscalls.h": "asmlinkage long sys_alpha(void);\n",
            "Makefile": "VERSION = 6\nPATCHLEVEL = 12\nSUBLEVEL = 37\n",
        }
        for relative, text in inputs.items():
            path = self.linux / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        (self.manual / "man/man7/path_resolution.7").write_text(
            ".TH path_resolution 7\n.SH NAME\npath_resolution \\- resolve paths\n",
            encoding="utf-8",
        )
        (self.manual / "man/man2/alpha.2").write_text(
            r'''.TH alpha 2
.SH NAME
alpha, beta \- fixture calls
.SH SYNOPSIS
.BI "int alpha(int " fd ", const char *" path );
.BI "int beta(int " fd );
.SH RETURN VALUE
On success, zero is returned.
.SH ERRORS
.TP
.B EBADF
.RB ( alpha ())
.I fd
is not a valid file descriptor.
.TP
.B EINVAL
.RB ( beta ())
The flags argument is invalid.
.TP
.B EINVAL
.RB ( alpha ())
The path argument is invalid.
.BR path_resolution (7).
''',
            encoding="utf-8",
        )
        (self.manual / "man/man2/beta.2").write_text(
            ".so man2/alpha.2\n", encoding="utf-8"
        )
        (self.manual / "man/man3").mkdir(parents=True)
        (self.manual / "man/man3/libc_only.3").write_text(
            ".TH libc_only 3\n.SH NAME\nlibc_only \\- not a syscall\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_uapi_alias_multi_function_and_missing_documentation(self) -> None:
        adapter = ManPagesAdapter(self.manual, self.linux)
        discovered = adapter.discover()
        self.assertEqual([row["syscall"] for row in discovered], ["alpha", "beta", "missing"])
        self.assertEqual(
            [row["documentation_status"] for row in discovered],
            ["documented", "documented", "missing_documentation"],
        )
        alpha = adapter.extract(adapter.prescan(discovered[0]))
        beta = adapter.extract(adapter.prescan(discovered[1]))
        self.assertEqual(
            [row["semantics"]["expected_result"].get("errno") for row in alpha["normalized"]],
            ["EBADF", "EINVAL", None],
        )
        self.assertEqual(
            [row["semantics"]["expected_result"].get("errno") for row in beta["normalized"]],
            ["EINVAL", None],
        )
        self.assertTrue(
            all(
                set(condition) == {"kind", "subject", "predicate", "value", "summary"}
                and len(condition["summary"]) <= 160
                for row in alpha["normalized"]
                for condition in row["semantics"]["preconditions"]
            )
        )
        missing = adapter.extract(adapter.prescan(discovered[2]))
        self.assertEqual(missing["reason"], "missing_documentation")
        self.assertEqual(missing["normalized"], [])

    def test_generated_header_error_contains_generation_command(self) -> None:
        (self.linux / "arch/riscv/include/generated/uapi/asm/unistd_64.h").unlink()
        with self.assertRaisesRegex(SyscallGuardError, "make -C ~/gitStudy/linux-6.12.37"):
            ManPagesAdapter(self.manual, self.linux)

    def test_multi_interface_provenance_keeps_syscall_semantics_separate(self) -> None:
        output = self.root / "output"
        descriptor = self.root / "man-pages.yaml"
        atomic_write_yaml(
            descriptor,
            {
                "source_id": "manual-fixture",
                "adapter": "man_pages",
                "location": str(self.manual),
                "linux_location": str(self.linux),
                "arch": "riscv64",
                "default_count": "all",
            },
        )
        run_ingest(descriptor, "all", output, "spec-man-multi")
        index = load_mapping(output / "library/syscalls.yaml")
        alpha_ids = {row["rule_id"] for row in index["syscalls"]["alpha"]}
        beta_ids = {row["rule_id"] for row in index["syscalls"]["beta"]}
        self.assertFalse(alpha_ids.intersection(beta_ids))
        for syscall in ("alpha", "beta"):
            for ref in index["syscalls"][syscall]:
                rule = load_mapping(output / ref["path"])
                self.assertEqual(rule["semantics"]["action"]["syscall"], syscall)
                self.assertTrue(
                    all(source.get("syscall") == syscall for source in rule["sources"])
                )

    def test_real_checkout_has_expected_riscv64_baseline(self) -> None:
        manual = Path("/home/cloud/gitLinux/man-pages")
        linux = Path("/home/cloud/gitStudy/linux-6.12.37")
        if not manual.is_dir() or not linux.is_dir():
            self.skipTest("real local source checkouts are unavailable")
        discovered = ManPagesAdapter(manual, linux).discover()
        documented = [row for row in discovered if row["documentation_status"] == "documented"]
        missing = [row for row in discovered if row["documentation_status"] != "documented"]
        self.assertEqual((len(discovered), len(documented), len(missing)), (319, 302, 17))


if __name__ == "__main__":
    unittest.main()
