from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from ..common import SyscallGuardError, content_hash, file_hash, tree_hash


_KERNEL_INPUTS = (
    Path("arch/riscv/include/generated/uapi/asm/unistd_64.h"),
    Path("scripts/syscall.tbl"),
    Path("include/linux/syscalls.h"),
    Path("Makefile"),
)

# Raw syscall names which intentionally differ from the public interface used
# as the man-pages page/function name. Discovery still starts only from __NR_*.
_INTERFACE_ALIASES = {
    "newfstatat": "fstatat",
    "umount2": "umount",
    "rt_sigaction": "sigaction",
    "rt_sigprocmask": "sigprocmask",
    "rt_sigpending": "sigpending",
    "rt_sigtimedwait": "sigtimedwait",
    "rt_sigqueueinfo": "sigqueue",
    "rt_sigsuspend": "sigsuspend",
    "rt_sigreturn": "sigreturn",
    "sendfile64": "sendfile",
    "fadvise64": "posix_fadvise",
    "sync_file_range2": "sync_file_range",
}


def _resolve_alias(path: Path, root: Path) -> tuple[Path, list[Path]]:
    """Follow a bounded chain of man-page .so aliases."""
    current = path
    chain = [path]
    for _ in range(16):
        text = current.read_text(encoding="utf-8", errors="replace")
        match = re.match(r"\s*\.so\s+(\S+)\s*(?:\n|\Z)", text)
        if not match:
            return current, chain
        target = (root / match.group(1)).resolve()
        if not target.is_file():
            target = (root / "man" / match.group(1)).resolve()
        if root.resolve() not in target.parents or not target.is_file():
            raise SyscallGuardError(
                f"invalid man-pages .so alias in {current}: {match.group(1)}"
            )
        if target in chain:
            raise SyscallGuardError(f"cyclic man-pages .so alias: {path}")
        current = target
        chain.append(current)
    raise SyscallGuardError(f"man-pages .so alias chain is too deep: {path}")


def _section(text: str, name: str) -> tuple[str, int] | None:
    match = re.search(
        rf'^\.SH\s+"?{re.escape(name)}"?\s*$\n(?P<body>.*?)(?=^\.SH\s|\Z)',
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        return None
    return match.group("body"), text.count("\n", 0, match.start("body")) + 1


def _roff_plain(text: str) -> str:
    """Produce compact facts from the small roff subset used by man-pages."""
    result: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith('.\\"'):
            continue
        if line.startswith("."):
            macro, _, payload = line[1:].partition(" ")
            if macro in {
                "SH",
                "SS",
                "TH",
                "nf",
                "fi",
                "P",
                "PP",
                "LP",
                "RS",
                "RE",
                "TP",
                "TQ",
                "IP",
                "EX",
                "EE",
                "in",
                "ad",
                "nh",
            }:
                if macro in {"SH", "SS"} and payload:
                    result.append(payload)
                continue
            line = payload
        line = re.sub(r"\\f(?:\[[^]]+\]|.)", "", line)
        line = re.sub(r"\\s[+-]?\d+", "", line)
        line = line.replace(r"\-", "-").replace(r"\e", "\\")
        line = line.replace(r"\(aq", "'").replace(r"\(dq", '"')
        line = re.sub(r"\\\[[^]]+\]", " ", line)
        line = line.replace(r"\&", "").replace(r"\~", " ").replace(r"\ ", " ")
        line = line.replace('"', "")
        line = re.sub(r"\s+", " ", line).strip()
        if line:
            result.append(line)
    return re.sub(r"\s+", " ", " ".join(result)).strip()


def _name_functions(text: str) -> list[str]:
    found = _section(text, "NAME")
    if not found:
        return []
    plain = _roff_plain(found[0])
    head = re.split(r"\s+-\s+", plain, maxsplit=1)[0]
    return list(dict.fromkeys(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\b", head)))


def _referenced_contexts(text: str, root: Path) -> list[Path]:
    refs: set[Path] = set()
    for name, section in re.findall(
        r'^\.(?:BR|IR|RB|BI)\s+"?([A-Za-z0-9_.+-]+)"?\s+\((2const|2type|7)\)',
        text,
        re.MULTILINE,
    ):
        path = root / "man" / f"man{section}" / f"{name}.{section}"
        if path.is_file():
            canonical, chain = _resolve_alias(path, root)
            refs.update(chain)
            refs.add(canonical)
    return sorted(refs)


def _argument_roles(text: str, interface: str) -> list[str]:
    found = _section(text, "SYNOPSIS")
    if not found:
        return []
    plain = _roff_plain(found[0])
    match = re.search(rf"\b{re.escape(interface)}\s*\((.*?)\)\s*;", plain)
    if not match:
        match = re.search(
            rf"\bsyscall\s*\(\s*SYS_{re.escape(interface)}\s*,(.*?)\)\s*;", plain
        )
    if not match:
        return []
    roles: list[str] = []
    for index, argument in enumerate(match.group(1).split(","), start=1):
        argument = argument.strip()
        if not argument or argument == "void":
            continue
        names = re.findall(r"[A-Za-z_][A-Za-z0-9_]*", argument)
        role = names[-1] if names else f"arg{index}"
        if role in {
            "const",
            "struct",
            "unsigned",
            "signed",
            "void",
            "int",
            "long",
        }:
            role = f"arg{index}"
        roles.append(role)
    return roles


def _summary(text: str) -> str:
    plain = _roff_plain(text)
    plain = re.sub(r"\s+", " ", plain).strip(" .")
    if len(plain) <= 160:
        return plain
    shortened = plain[:157].rsplit(" ", 1)[0]
    return (shortened or plain[:157]) + "..."


def _precondition(summary: str, roles: list[str], errno: str) -> dict[str, Any]:
    lower = summary.lower()
    subject = next(
        (
            role
            for role in roles
            if re.search(rf"\b{re.escape(role.lower())}\b", lower)
        ),
        "call",
    )
    if any(
        word in lower
        for word in ("pointer", "address space", "accessible address", "null")
    ):
        kind, predicate = "pointer", "invalid_or_inaccessible"
    elif "file descriptor" in lower or re.search(r"\bfd\b|\bdirfd\b", lower):
        kind, predicate = "fd", "invalid_or_wrong_type"
    elif any(
        word in lower for word in ("path", "directory", "symbolic link", "pathname")
    ):
        kind, predicate = "path", "documented_path_condition"
    elif any(
        word in lower
        for word in ("permission", "privilege", "capability", "uid", "gid")
    ):
        kind, predicate = "credential", "insufficient_permission"
    elif any(
        word in lower for word in ("memory", "space", "quota", "resource", "limit")
    ):
        kind, predicate = "resource", "unavailable_or_exhausted"
    elif any(
        word in lower for word in ("exists", "busy", "state", "read-only", "mounted")
    ):
        kind, predicate = "object_state", "documented_state_condition"
    elif any(
        word in lower for word in ("flag", "argument", "value", "size", "range", "mode")
    ):
        kind, predicate = "argument", "invalid_value"
    else:
        kind, predicate = "documented", "documented_condition"
    return {
        "kind": kind,
        "subject": subject,
        "predicate": predicate,
        "value": errno,
        "summary": summary,
    }


def _function_qualifiers(block: str, functions: list[str]) -> set[str]:
    # Function-limited ERRORS entries put the qualifier at the start. Looking
    # only at the first few source lines avoids treating references as limits.
    head = "\n".join(block.split("\n", 8)[:8])
    plain = _roff_plain(head)
    return {
        name
        for name in functions
        if re.search(rf"\b{re.escape(name)}\s*\(\)", plain)
    }


class ManPagesAdapter:
    """Linux RISC-V UAPI universe backed by local Linux man-pages."""

    adapter_id = "man_pages"
    adapter_version = "2"

    def __init__(
        self, location: Path, linux_location: Path, arch: str = "riscv64"
    ) -> None:
        self.location = location.resolve()
        self.linux_location = linux_location.resolve()
        self.arch = arch
        if arch != "riscv64":
            raise SyscallGuardError(
                f"man_pages currently supports arch=riscv64, got {arch!r}"
            )
        if not (self.location / "man/man2").is_dir():
            raise SyscallGuardError(
                f"man-pages man2 directory does not exist: {self.location}"
            )
        self.header = self.linux_location / _KERNEL_INPUTS[0]
        if not self.header.is_file():
            raise SyscallGuardError(
                "generated RISC-V64 UAPI header is missing: "
                f"{self.header}\nGenerate headers with:\n"
                "make -C ~/gitStudy/linux-6.12.37 \\\n+  O=/tmp/linux-6.12.37-riscv \\\n+  ARCH=riscv headers_install \\\n+  INSTALL_HDR_PATH=~/gitStudy/linux-uapi-6.12.37"
            )
        missing = [
            self.linux_location / path
            for path in _KERNEL_INPUTS
            if not (self.linux_location / path).is_file()
        ]
        if missing:
            raise SyscallGuardError(
                "missing Linux ABI fingerprint input: " + ", ".join(map(str, missing))
            )
        self.kernel_fingerprint = content_hash(
            {
                str(path): file_hash(self.linux_location / path)
                for path in _KERNEL_INPUTS
            }
        )
        manual_files = [
            path
            for section in ("man2", "man2const", "man2type", "man7")
            for path in (self.location / "man" / section).glob("*")
            if path.is_file()
        ]
        self.manual_fingerprint = tree_hash(manual_files, self.location)
        self.snapshot_hash = content_hash(
            {
                "kernel_uapi": self.kernel_fingerprint,
                "manual_context": self.manual_fingerprint,
                "arch": self.arch,
            }
        )
        self.rules_hash = content_hash(
            {
                "adapter": self.adapter_id,
                "version": self.adapter_version,
                "aliases": _INTERFACE_ALIASES,
                "precondition_schema": [
                    "kind",
                    "subject",
                    "predicate",
                    "value",
                    "summary",
                ],
            }
        )
        self._page_index = self._build_page_index()

    def _build_page_index(self) -> dict[str, list[Path]]:
        index: dict[str, list[Path]] = {}
        for alias_path in sorted((self.location / "man/man2").glob("*.2")):
            canonical, _chain = _resolve_alias(alias_path, self.location)
            text = canonical.read_text(encoding="utf-8", errors="replace")
            # A man2 shim may intentionally point to a man3 page because the
            # wrapper is layered on a same-named syscall.  The man2 filename
            # remains valid syscall documentation, but unrelated man3 names
            # are never added to the ABI universe.
            for function in [alias_path.stem, *_name_functions(text)]:
                index.setdefault(function, [])
                if alias_path not in index[function]:
                    index[function].append(alias_path)
        return index

    def discover(self) -> list[dict[str, Any]]:
        text = self.header.read_text(encoding="utf-8", errors="replace")
        rows: list[dict[str, Any]] = []
        for match in re.finditer(
            r"^#define\s+__NR_([A-Za-z0-9_]+)\s+(\d+)\s*$", text, re.MULTILINE
        ):
            syscall, number = match.group(1), int(match.group(2))
            if syscall == "syscalls":
                continue
            interface = _INTERFACE_ALIASES.get(syscall, syscall)
            candidates = (
                self._page_index.get(syscall)
                or self._page_index.get(interface)
                or []
            )
            page = (
                sorted(
                    candidates,
                    key=lambda path: (path.stem != interface, path.name),
                )[0]
                if candidates
                else None
            )
            rows.append(
                {
                    "syscall": syscall,
                    "number": number,
                    "interface": interface,
                    "page": page,
                    "documentation_status": (
                        "documented" if page else "missing_documentation"
                    ),
                }
            )
        return sorted(rows, key=lambda row: str(row["syscall"]))

    def prescan(self, item: dict[str, Any]) -> dict[str, Any]:
        page = item.get("page")
        files: list[Path] = []
        canonical: Path | None = None
        if isinstance(page, Path):
            canonical, chain = _resolve_alias(page, self.location)
            files.extend(chain)
            text = canonical.read_text(encoding="utf-8", errors="replace")
            files.extend(_referenced_contexts(text, self.location))
        unique = sorted(set(files))
        source_fingerprint = content_hash(
            {
                "kernel": self.kernel_fingerprint,
                "number": item["number"],
                "documentation_status": item["documentation_status"],
                "manual_files": {
                    str(path.relative_to(self.location)): file_hash(path)
                    for path in unique
                },
            }
        )
        return {
            **item,
            "canonical_page": canonical,
            "files": unique,
            "source_fingerprint": source_fingerprint,
            "recognition_fingerprint": content_hash(
                {
                    "rules_hash": self.rules_hash,
                    "page": (
                        str(canonical.relative_to(self.location)) if canonical else None
                    ),
                    "interface": item["interface"],
                }
            ),
            "recognition": [
                {
                    "recognizer_id": "man_pages.roff.sections",
                    "definition_hash": self.rules_hash,
                    "matches": [
                        str(path.relative_to(self.location)) for path in unique
                    ],
                }
            ],
        }

    def extract(self, item: dict[str, Any]) -> dict[str, Any]:
        canonical = item.get("canonical_page")
        if not isinstance(canonical, Path):
            return {
                "raw": [],
                "normalized": [],
                "reason": "missing_documentation",
                "documentation_status": "missing_documentation",
            }
        text = canonical.read_text(encoding="utf-8", errors="replace")
        relative = str(canonical.relative_to(self.location))
        functions = _name_functions(text)
        interface = str(item["interface"])
        roles = _argument_roles(text, interface)
        raw: list[dict[str, Any]] = []
        normalized: list[dict[str, Any]] = []

        for context in item.get("files", []):
            if not isinstance(context, Path) or context == canonical:
                continue
            evidence = {
                "syscall": item["syscall"],
                "source": {
                    "file": str(context.relative_to(self.location)),
                    "line": 1,
                },
                "recognizer_id": "man_pages.semantic_context",
                "evidence_class": "context",
                "context_hash": file_hash(context),
            }
            evidence["evidence_hash"] = content_hash(evidence)
            raw.append(evidence)

        errors = _section(text, "ERRORS")
        if errors:
            body, section_line = errors
            starts = [
                match.start()
                for match in re.finditer(r"^\.T[QP]\s*$", body, re.MULTILINE)
            ]
            starts.append(len(body))
            for index in range(len(starts) - 1):
                block = body[starts[index] : starts[index + 1]]
                errno_match = re.search(
                    r"^\.(?:B|BR)\s+(E[A-Z0-9_]+)\b", block, re.MULTILINE
                )
                if not errno_match:
                    continue
                errno = errno_match.group(1)
                qualifiers = _function_qualifiers(block, functions)
                if (
                    qualifiers
                    and interface not in qualifiers
                    and str(item["syscall"]) not in qualifiers
                ):
                    continue
                summary = _summary(block[errno_match.end() :])
                if not summary:
                    summary = f"The documented {errno} condition applies."
                line = section_line + body.count("\n", 0, starts[index])
                evidence = {
                    "syscall": item["syscall"],
                    "source": {"file": relative, "line": line},
                    "recognizer_id": "man_pages.errors.clause",
                    "evidence_class": "authoritative",
                    "case": f"errors_{errno.lower()}_{line}",
                    "errno": errno,
                    "function_qualifiers": sorted(qualifiers),
                }
                evidence["evidence_hash"] = content_hash(evidence)
                raw.append(evidence)
                precondition = _precondition(summary, roles, errno)
                normalized.append(
                    {
                        **evidence,
                        "category": "syscall_behavior",
                        "preconditions": [precondition],
                        "semantics": {
                            "preconditions": [precondition],
                            "action": {
                                "operation": "invoke_syscall",
                                "syscall": item["syscall"],
                                "arguments": roles,
                            },
                            "expected_result": {
                                "kind": "return_errno",
                                "return": "-1",
                                "errno": errno,
                            },
                            "errno": [errno],
                        },
                    }
                )

        returns = _section(text, "RETURN VALUE")
        if returns:
            body, line = returns
            plain = _summary(body)
            lower = plain.lower()
            expected: dict[str, Any] | None = None
            if re.search(
                r"on success[^.]{0,100}\b(?:a |the )?file descriptor\b", lower
            ):
                expected = {"kind": "return_fd", "return": "FD"}
            elif re.search(
                r"on success[^.]{0,100}\b(?:positive|greater than zero)\b", lower
            ):
                expected = {"kind": "positive_return", "return": ">0"}
            elif re.search(
                r"on success[^.]{0,140}\bzero is returned\b|"
                r"\breturns zero on success\b",
                lower,
            ):
                expected = {"kind": "success", "return": "0"}
            else:
                fixed = re.search(
                    r"on success[^.]{0,100}\b(?:returns?|returned)\s+(-?\d+)\b",
                    lower,
                )
                if fixed:
                    expected = {"kind": "return_value", "return": fixed.group(1)}
            if expected is not None:
                evidence = {
                    "syscall": item["syscall"],
                    "source": {"file": relative, "line": line},
                    "recognizer_id": "man_pages.return.simple",
                    "evidence_class": "authoritative",
                    "case": f"return_value_{line}",
                }
                evidence["evidence_hash"] = content_hash(evidence)
                raw.append(evidence)
                condition = {
                    "kind": "documented",
                    "subject": "call",
                    "predicate": "documented_success_condition",
                    "value": "success",
                    "summary": "The syscall completes successfully.",
                }
                normalized.append(
                    {
                        **evidence,
                        "category": "syscall_behavior",
                        "preconditions": [condition],
                        "semantics": {
                            "preconditions": [condition],
                            "action": {
                                "operation": "invoke_syscall",
                                "syscall": item["syscall"],
                                "arguments": roles,
                            },
                            "expected_result": expected,
                            "errno": [],
                        },
                    }
                )

        return {
            "raw": raw,
            "normalized": normalized,
            "reason": "all_evidence_resolved" if normalized else "no_simple_rules",
            "documentation_status": "documented",
        }
