from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ..common import SyscallGuardError, content_hash, load_mapping, tree_hash


@dataclass(frozen=True)
class Call:
    name: str
    args: list[str]
    file: Path
    line: int
    text: str
    end: int
    start: int = 0


@dataclass(frozen=True)
class StructArray:
    name: str
    fields: list[str]
    rows: list[dict[str, str]]
    type_name: str = ""
    line: int = 0
    mutable_fields: frozenset[str] = frozenset()


@dataclass(frozen=True)
class PointerAlias:
    name: str
    array: str
    index: str
    start: int


@dataclass(frozen=True)
class DocumentBlock:
    text: str
    line: int
    content_hash: str
    syscalls: tuple[str, ...]
    direction: str | None
    errnos: tuple[str, ...]


def clean_expr(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def _code_mask(text: str) -> str:
    """Blank comments and literals while preserving offsets and newlines."""
    result = list(text)
    state = "code"
    index = 0
    while index < len(text):
        char = text[index]
        nxt = text[index + 1] if index + 1 < len(text) else ""
        if state == "code":
            if char == "/" and nxt == "/":
                result[index] = result[index + 1] = " "
                state = "line"
                index += 1
            elif char == "/" and nxt == "*":
                result[index] = result[index + 1] = " "
                state = "block"
                index += 1
            elif char == '"':
                result[index] = " "
                state = "string"
            elif char == "'":
                result[index] = " "
                state = "char"
        elif state == "line":
            if char == "\n":
                state = "code"
            else:
                result[index] = " "
        elif state == "block":
            if char == "*" and nxt == "/":
                result[index] = result[index + 1] = " "
                state = "code"
                index += 1
            elif char != "\n":
                result[index] = " "
        else:
            quote = '"' if state == "string" else "'"
            if char == "\\":
                result[index] = " "
                if index + 1 < len(text):
                    index += 1
                    if text[index] != "\n":
                        result[index] = " "
            elif char == quote:
                result[index] = " "
                state = "code"
            elif char != "\n":
                result[index] = " "
        index += 1
    return "".join(result)


def _matching(text: str, start: int, opening: str, closing: str) -> int | None:
    depth = 0
    state = "code"
    index = start
    while index < len(text):
        char = text[index]
        nxt = text[index + 1] if index + 1 < len(text) else ""
        if state == "code":
            if char == "/" and nxt == "/":
                state = "line"
                index += 1
            elif char == "/" and nxt == "*":
                state = "block"
                index += 1
            elif char == '"':
                state = "string"
            elif char == "'":
                state = "char"
            elif char == opening:
                depth += 1
            elif char == closing:
                depth -= 1
                if depth == 0:
                    return index
        elif state == "line":
            if char == "\n":
                state = "code"
        elif state == "block":
            if char == "*" and nxt == "/":
                state = "code"
                index += 1
        elif state in {"string", "char"}:
            quote = '"' if state == "string" else "'"
            if char == "\\":
                index += 1
            elif char == quote:
                state = "code"
        index += 1
    return None


def split_top_level(text: str) -> list[str]:
    parts: list[str] = []
    start = 0
    depth = 0
    state = "code"
    index = 0
    while index < len(text):
        char = text[index]
        nxt = text[index + 1] if index + 1 < len(text) else ""
        if state == "code":
            if char == "/" and nxt == "/":
                state = "line"
                index += 1
            elif char == "/" and nxt == "*":
                state = "block"
                index += 1
            elif char == '"':
                state = "string"
            elif char == "'":
                state = "char"
            elif char in "([{":
                depth += 1
            elif char in ")]}":
                depth -= 1
            elif char == "," and depth == 0:
                parts.append(clean_expr(text[start:index]))
                start = index + 1
        elif state == "line":
            if char == "\n":
                state = "code"
        elif state == "block":
            if char == "*" and nxt == "/":
                state = "code"
                index += 1
        elif state in {"string", "char"}:
            quote = '"' if state == "string" else "'"
            if char == "\\":
                index += 1
            elif char == quote:
                state = "code"
        index += 1
    tail = clean_expr(text[start:])
    if tail or parts:
        parts.append(tail)
    return parts


def find_calls(text: str, source: Path, names: set[str] | None = None) -> list[Call]:
    calls: list[Call] = []
    pattern = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(")
    for match in pattern.finditer(text):
        name = match.group(1)
        if names is not None and name not in names:
            continue
        opening = text.find("(", match.start())
        closing = _matching(text, opening, "(", ")")
        if closing is None:
            continue
        calls.append(
            Call(
                name,
                split_top_level(text[opening + 1 : closing]),
                source,
                text.count("\n", 0, match.start()) + 1,
                text[match.start() : closing + 1],
                closing,
                match.start(),
            )
        )
    return calls


def _legacy_struct_arrays(text: str) -> list[StructArray]:
    result: list[StructArray] = []
    pattern = re.compile(
        r"static\s+struct\s+[A-Za-z_][A-Za-z0-9_]*\s*\{(?P<fields>.*?)\}\s*"
        r"(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*\[\]\s*=\s*\{(?P<body>.*?)\}\s*;",
        re.S,
    )
    for match in pattern.finditer(text):
        fields: list[str] = []
        for raw in match.group("fields").split(";"):
            field = re.search(r"([A-Za-z_][A-Za-z0-9_]*)\s*(?:\[[^]]*\])?\s*$", raw.strip())
            if field:
                fields.append(field.group(1))
        rows: list[dict[str, str]] = []
        body = match.group("body")
        index = 0
        while index < len(body):
            opening = body.find("{", index)
            if opening < 0:
                break
            closing = _matching(body, opening, "{", "}")
            if closing is None:
                break
            values = split_top_level(body[opening + 1 : closing])
            row: dict[str, str] = {}
            if any(value.startswith(".") for value in values):
                for value in values:
                    item = re.match(r"\.([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)", value)
                    if item:
                        row[item.group(1)] = clean_expr(item.group(2))
            else:
                row.update((field, clean_expr(value)) for field, value in zip(fields, values))
            if row:
                rows.append(row)
            index = closing + 1
        if fields and rows:
            result.append(StructArray(match.group("name"), fields, rows))
    return result


def _field_names(body: str) -> list[str]:
    fields: list[str] = []
    for declaration in body.split(";"):
        declaration = _code_mask(declaration).strip()
        if not declaration:
            continue
        for part in split_top_level(declaration):
            function_pointer = re.search(
                r"\(\s*\*\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)", part
            )
            if function_pointer:
                fields.append(function_pointer.group(1))
                continue
            field = re.search(
                r"([A-Za-z_][A-Za-z0-9_]*)\s*(?:\[[^]]*\])?\s*(?::\s*\d+)?\s*$",
                part,
            )
            if field:
                fields.append(field.group(1))
    return fields


def _initializer_rows(body: str, fields: list[str]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for raw_entry in split_top_level(body):
        entry = re.sub(r"^\s*\[[^]]+\]\s*=\s*", "", raw_entry, count=1)
        entry_mask = _code_mask(entry)
        opening = entry_mask.find("{")
        prefix = entry_mask[:opening].strip() if opening >= 0 else ""
        if opening < 0 or (prefix and not prefix.startswith("#")):
            continue
        entry = entry[opening:]
        closing = _matching(entry, 0, "{", "}")
        if closing is None:
            continue
        values = split_top_level(entry[1:closing])
        row: dict[str, str] = {}
        if any(re.match(r"^\.[A-Za-z_]", value) for value in values):
            for value in values:
                item = re.match(r"\.([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)", value, re.S)
                if item:
                    row[item.group(1)] = clean_expr(item.group(2))
        else:
            row.update((field, clean_expr(value)) for field, value in zip(fields, values))
        if row:
            rows.append(row)
    return rows


def _statement_end(mask: str, start: int) -> int | None:
    depths = {"(": 0, "[": 0, "{": 0}
    pairs = {")": "(", "]": "[", "}": "{"}
    for index in range(start, len(mask)):
        char = mask[index]
        if char in depths:
            depths[char] += 1
        elif char in pairs:
            opening = pairs[char]
            depths[opening] = max(0, depths[opening] - 1)
        elif char == ";" and not any(depths.values()):
            return index
    return None


def _array_from_declaration(
    text: str,
    mask: str,
    start: int,
    end: int,
    fields: list[str],
    type_name: str,
) -> StructArray | None:
    declaration_mask = mask[start:end]
    match = re.search(
        r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\[[^]]*\]\s*=\s*\{", declaration_mask
    )
    if not match:
        return None
    name = match.group(1)
    opening = start + declaration_mask.find("{", match.start())
    closing = _matching(text, opening, "{", "}")
    if closing is None or closing > end:
        return None
    rows = _initializer_rows(text[opening + 1 : closing], fields)
    if not rows:
        return None
    return StructArray(
        name=name,
        fields=fields,
        rows=rows,
        type_name=type_name,
        line=text.count("\n", 0, start) + 1,
    )


def _struct_arrays(text: str) -> list[StructArray]:
    """Parse inline and separately declared C struct test-case arrays."""
    mask = _code_mask(text)
    definitions: dict[str, list[str]] = {}
    result: list[StructArray] = []
    definition_spans: list[tuple[int, int]] = []
    pattern = re.compile(
        r"\b(?P<typedef>typedef\s+)?struct(?:\s+(?P<tag>[A-Za-z_][A-Za-z0-9_]*))?\s*\{"
    )
    for match in pattern.finditer(mask):
        opening = mask.find("{", match.start(), match.end())
        closing = _matching(mask, opening, "{", "}")
        if closing is None:
            continue
        end = _statement_end(mask, closing + 1)
        if end is None:
            continue
        fields = _field_names(text[opening + 1 : closing])
        if not fields:
            continue
        tail = mask[closing + 1 : end]
        tag = match.group("tag") or ""
        aliases: list[str] = [tag] if tag else []
        if match.group("typedef"):
            alias = re.match(r"\s*([A-Za-z_][A-Za-z0-9_]*)\s*;?\s*$", tail)
            if alias:
                aliases.append(alias.group(1))
        for alias in aliases:
            definitions[alias] = fields
        array = _array_from_declaration(
            text, mask, closing + 1, end, fields, tag or (aliases[-1] if aliases else "")
        )
        if array:
            result.append(array)
        definition_spans.append((match.start(), end + 1))

    if definitions:
        type_names = "|".join(sorted((re.escape(name) for name in definitions), key=len, reverse=True))
        separated = re.compile(
            rf"\b(?:static\s+)?(?:const\s+)?(?:struct\s+)?(?P<type>{type_names})\s+"
            r"(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*\[[^]]*\]\s*=\s*\{"
        )
        for match in separated.finditer(mask):
            if any(start <= match.start() < end for start, end in definition_spans):
                continue
            end = _statement_end(mask, match.start())
            if end is None:
                continue
            array = _array_from_declaration(
                text,
                mask,
                match.start(),
                end,
                definitions[match.group("type")],
                match.group("type"),
            )
            if array:
                result.append(array)

    arrays: list[StructArray] = []
    for array in sorted(result, key=lambda item: (item.line, item.name)):
        aliases = _pointer_aliases(text, [array])
        mutable: set[str] = set()
        direct = rf"\b{re.escape(array.name)}\s*\[[^]]+\]\s*\.\s*([A-Za-z_][A-Za-z0-9_]*)"
        for match in re.finditer(direct, mask):
            tail = mask[match.end() : match.end() + 6]
            if re.match(r"\s*(?:[+\-*/%]?=(?!=)|\+\+|--)", tail):
                mutable.add(match.group(1))
        for alias in aliases:
            indirect = rf"\b{re.escape(alias.name)}\s*->\s*([A-Za-z_][A-Za-z0-9_]*)"
            for match in re.finditer(indirect, mask[alias.start + 1 :]):
                absolute_end = alias.start + 1 + match.end()
                tail = mask[absolute_end : absolute_end + 6]
                if re.match(r"\s*(?:[+\-*/%]?=(?!=)|\+\+|--)", tail):
                    mutable.add(match.group(1))
        arrays.append(
            StructArray(
                array.name,
                array.fields,
                array.rows,
                array.type_name,
                array.line,
                frozenset(mutable),
            )
        )
    return arrays


def _pointer_aliases(text: str, arrays: list[StructArray]) -> list[PointerAlias]:
    if not arrays:
        return []
    names = "|".join(sorted((re.escape(array.name) for array in arrays), key=len, reverse=True))
    mask = _code_mask(text)
    patterns = [
        re.compile(
            rf"\b(?P<alias>[A-Za-z_][A-Za-z0-9_]*)\s*=\s*&?\s*"
            rf"(?P<array>{names})\s*\[\s*(?P<index>[^]]+)\s*\]"
        ),
        re.compile(
            rf"\b(?P<alias>[A-Za-z_][A-Za-z0-9_]*)\s*=\s*"
            rf"(?P<array>{names})\s*\+\s*(?P<index>[A-Za-z_][A-Za-z0-9_]*|\d+)"
        ),
    ]
    aliases: list[PointerAlias] = []
    for pattern in patterns:
        for match in pattern.finditer(mask):
            aliases.append(
                PointerAlias(
                    match.group("alias"),
                    match.group("array"),
                    clean_expr(match.group("index")),
                    match.start(),
                )
            )
    return sorted(set(aliases), key=lambda item: item.start)


def _document_blocks(text: str) -> list[DocumentBlock]:
    include = re.search(r"^\s*#\s*include\b", text, re.M)
    boundary = include.start() if include else min(len(text), 16000)
    result: list[DocumentBlock] = []
    for match in re.finditer(r"/\*\\(?P<body>.*?)\*/", text[:boundary], re.S):
        prefix = re.sub(r"^\s*#.*$", "", _code_mask(text[: match.start()]), flags=re.M)
        if prefix.strip():
            continue
        lines = []
        for line in match.group("body").splitlines():
            lines.append(re.sub(r"^\s*\*?\s?", "", line).rstrip())
        normalized = clean_expr("\n".join(lines))
        if not normalized:
            continue
        lowered = normalized.lower()
        failure = bool(re.search(r"\b(?:fail(?:s|ed|ure)?|error)\b|returns?\s+-1|sets?\s+errno", lowered))
        success = bool(re.search(r"\b(?:succeed(?:s|ed)?|success(?:ful(?:ly)?)?)\b", lowered))
        direction = "failure" if failure and not success else "success" if success and not failure else None
        # Function names in quoted commit subjects and implementation notes
        # are not specification targets. Syscall mentions belong near the
        # beginning of an LTP documentation block.
        syscall_text = normalized[:600]
        syscalls = tuple(
            dict.fromkeys(
                value.lower()
                for value in re.findall(
                    r"(?:`)?\b([a-z][a-z0-9_]*)\s*\(\s*(?:2)?\s*\)(?:`)?",
                    syscall_text,
                )
            )
        )
        errnos = tuple(
            value
            for value in dict.fromkeys(re.findall(r"\bE[A-Z0-9]{2,}\b", normalized))
            if value not in {"EOF", "ELF", "EPOLL", "EVENT", "EXEC", "EXIT"}
        )
        result.append(
            DocumentBlock(
                normalized,
                text.count("\n", 0, match.start()) + 1,
                content_hash({"text": normalized}),
                syscalls,
                direction,
                errnos,
            )
        )
    return result


def _substitute(expr: str, row: dict[str, str]) -> str:
    result = expr
    for field, value in sorted(row.items(), key=lambda item: -len(item[0])):
        pointer = value[1:] if value.startswith("&") else f"*{value}"
        result = re.sub(rf"\*tc->{re.escape(field)}\b", pointer, result)
        result = re.sub(rf"\btc->{re.escape(field)}\b", value, result)
    return clean_expr(result)


class LtpAdapter:
    """Configuration-driven, conservative LTP source adapter.

    The adapter protocol is deliberately only ``discover``, ``prescan`` and
    ``extract`` so another source can implement the same ingestion contract.
    """

    adapter_id = "ltp"
    adapter_version = "3"

    def __init__(
        self, location: Path, rules_path: Path, extractor_profile: str = "candidate"
    ) -> None:
        self.location = location
        self.rules_path = rules_path
        if extractor_profile not in {"baseline", "candidate"}:
            raise SyscallGuardError(f"invalid LTP extractor profile: {extractor_profile}")
        self.extractor_profile = extractor_profile
        self.config = load_mapping(rules_path)
        if self.config.get("adapter") != "ltp":
            raise SyscallGuardError(f"invalid LTP recognition configuration: {rules_path}")
        rows = self.config.get("recognizers")
        if not isinstance(rows, list):
            raise SyscallGuardError("LTP recognition configuration needs recognizers")
        self.recognizers: list[dict[str, Any]] = []
        seen: set[str] = set()
        for row in rows:
            if not isinstance(row, dict) or not isinstance(row.get("id"), str):
                raise SyscallGuardError("every LTP recognizer needs a stable id")
            if row["id"] in seen:
                raise SyscallGuardError(f"duplicate LTP recognizer id: {row['id']}")
            seen.add(row["id"])
            if row.get("enabled", True):
                self.recognizers.append(row)
        aliases = self.config.get("aliases", {})
        self.aliases = aliases if isinstance(aliases, dict) else {}
        self.rules_hash = content_hash(self.config)

    @property
    def syscalls_root(self) -> Path:
        return self.location / "testcases" / "kernel" / "syscalls"

    def discover(self) -> list[dict[str, Any]]:
        if not self.syscalls_root.is_dir():
            raise SyscallGuardError(f"LTP syscall directory does not exist: {self.syscalls_root}")
        result: list[dict[str, Any]] = []
        directory_names = {path.name.lower() for path in self.syscalls_root.iterdir() if path.is_dir()}
        consumed: set[str] = set()
        for canonical, configured in self.aliases.items():
            if not isinstance(configured, list):
                continue
            directories = sorted({str(item) for item in configured if str(item) in directory_names})
            if not directories:
                continue
            result.append({"syscall": str(canonical).lower(), "directories": directories})
            consumed.update(item for item in directories if item != canonical)
        existing = {item["syscall"] for item in result}
        for syscall in sorted(directory_names - consumed):
            if syscall in existing:
                continue
            directories = [syscall]
            raw_aliases = self.aliases.get(syscall, [])
            if isinstance(raw_aliases, list):
                directories.extend(str(item) for item in raw_aliases)
            unique = sorted({item for item in directories if (self.syscalls_root / item).is_dir()})
            result.append({"syscall": syscall, "directories": unique})
        return sorted(result, key=lambda item: item["syscall"])

    def _files(self, item: dict[str, Any]) -> list[Path]:
        files: list[Path] = []
        for directory in item["directories"]:
            files.extend((self.syscalls_root / directory).glob("*.c"))
        return sorted(set(files))

    def _infer_call(self, expr: str, syscall: str) -> tuple[str | None, list[str]]:
        expr = clean_expr(expr)
        assignment = re.match(r"^[A-Za-z_][A-Za-z0-9_]*(?:\[[^]]+\])?\s*=\s*(.*)$", expr, re.S)
        if assignment:
            expr = clean_expr(assignment.group(1))
        nr = re.search(r"__NR_([A-Za-z0-9_]+)", expr)
        direct = re.match(r"([A-Za-z_][A-Za-z0-9_]*)\s*\((.*)\)\s*$", expr, re.S)
        if nr and direct:
            args = split_top_level(direct.group(2))
            return nr.group(1), args[1:] if args and args[0].startswith("__NR_") else args
        if not direct:
            return None, []
        function = direct.group(1)
        valid = {syscall}
        configured = self.aliases.get(syscall, [])
        if isinstance(configured, list):
            valid.update(str(item) for item in configured)
        return (syscall if function in valid else function), split_top_level(direct.group(2))

    def _recognizer_matches(self, recognizer: dict[str, Any], call: Call, text: str, syscall: str) -> bool:
        kind = recognizer.get("kind")
        names = recognizer.get("names", [])
        if not isinstance(names, list) or call.name not in names:
            return False
        if kind == "safe_helper":
            targets = recognizer.get("syscalls", {})
            return isinstance(targets, dict) and call.name in targets.get(syscall, [])
        call_index = int(recognizer.get("call_argument", 0))
        if call_index >= len(call.args):
            return False
        inferred, _args = self._infer_call(call.args[call_index], syscall)
        if inferred != syscall and recognizer.get("target_match") == "source_directory":
            candidates = {syscall}
            aliases = self.aliases.get(syscall, [])
            if isinstance(aliases, list):
                candidates.update(str(item) for item in aliases)
            inferred = syscall if any(f"/{name}/" in str(call.file) for name in candidates) else inferred
        if inferred != syscall:
            return False
        if kind == "old_test":
            window = text[call.end + 1 : call.end + 1 + int(recognizer.get("window", 900))]
            markers = recognizer.get("markers", [])
            return isinstance(markers, list) and any(re.search(str(marker), window) for marker in markers)
        return True

    def prescan(self, item: dict[str, Any]) -> dict[str, Any]:
        files = self._files(item)
        matches: dict[str, list[dict[str, Any]]] = {}
        names = {
            str(name)
            for recognizer in self.recognizers
            for name in recognizer.get("names", [])
            if isinstance(name, str)
        }
        for source in files:
            text = source.read_text(encoding="utf-8", errors="replace")
            for call in find_calls(text, source, names):
                for recognizer in self.recognizers:
                    if self._recognizer_matches(recognizer, call, text, item["syscall"]):
                        matches.setdefault(recognizer["id"], []).append(
                            {
                                "file": str(source.relative_to(self.location)),
                                "line": call.line,
                                "name": call.name,
                            }
                        )
        recognition = [
            {
                "recognizer_id": recognizer["id"],
                "definition_hash": content_hash(recognizer),
                "normalization_hash": content_hash(
                    {
                        key: self.config.get(key)
                        for key in (
                            "array_expansion",
                            "expected_normalization",
                            "preconditions",
                            "rule_template",
                        )
                    }
                ),
                "matches": matches[recognizer["id"]],
            }
            for recognizer in self.recognizers
            if recognizer["id"] in matches
        ]
        if self.extractor_profile == "candidate":
            # The engine row intentionally participates in every recognition
            # fingerprint. Parser changes therefore invalidate earlier ingest
            # decisions even for sources which had no macro match.
            recognition.append(
                {
                    "recognizer_id": "ltp.extractor.engine",
                    "definition_hash": content_hash(
                        {
                            "adapter_version": self.adapter_version,
                            "profile": self.extractor_profile,
                            "struct_evidence": self.config.get("struct_evidence", {}),
                            "document_context": self.config.get("document_context", {}),
                        }
                    ),
                    "normalization_hash": content_hash(
                        {
                            "array_expansion": self.config.get("array_expansion", {}),
                            "expected_normalization": self.config.get(
                                "expected_normalization", {}
                            ),
                        }
                    ),
                    "matches": [
                        {"file": str(path.relative_to(self.location)), "line": 1, "name": "source"}
                        for path in files
                    ],
                }
            )
        return {
            **item,
            "files": files,
            "source_fingerprint": tree_hash(files, self.location),
            "recognition_fingerprint": content_hash(recognition),
            "recognition": recognition,
        }

    def _expected(self, recognizer: dict[str, Any], call: Call, text: str) -> dict[str, Any] | None:
        extraction = recognizer.get("expected", {})
        if not isinstance(extraction, dict):
            return None
        kind = extraction.get("kind")
        if recognizer.get("kind") == "old_test":
            window = text[call.end + 1 : call.end + 1 + int(recognizer.get("window", 900))]
            next_test = re.search(r"\bTEST\s*\(", window)
            if next_test:
                window = window[: next_test.start()]
            if self.extractor_profile == "candidate":
                candidate_expected = self._comparison_expected(window)
                if candidate_expected is not None:
                    return candidate_expected
                if re.search(r"(?:->|\[[^]]+\]\s*\.)", window):
                    return None
            errno_patterns = recognizer.get("errno_patterns", [])
            return_patterns = recognizer.get("return_patterns", [])
            errno_match = next(
                (match for pattern in errno_patterns if (match := re.search(str(pattern), window))),
                None,
            ) if isinstance(errno_patterns, list) else None
            return_match = next(
                (match for pattern in return_patterns if (match := re.search(str(pattern), window))),
                None,
            ) if isinstance(return_patterns, list) else None
            if errno_match:
                fallback = {
                    "kind": "return_errno",
                    "return": clean_expr(return_match.group(1)) if return_match else "-1",
                    "errno": errno_match.group(1),
                }
            elif return_match:
                fallback = {
                    "kind": "return_value",
                    "return": clean_expr(return_match.group(1)),
                }
            else:
                return None
            if self.extractor_profile == "candidate" and any(
                re.search(r"(?:->|\[[^]]+\]\s*\.)", str(value))
                for value in fallback.values()
            ):
                return None
            return fallback
        result: dict[str, Any] = {"kind": kind}
        for key, value in extraction.items():
            if key == "kind":
                continue
            if key.endswith("_argument"):
                index = int(value)
                if index >= len(call.args):
                    return None
                result[key[: -len("_argument")]] = call.args[index]
            else:
                result[key] = value
        normalization = self.config.get("expected_normalization", {})
        definition = normalization.get(kind, {}) if isinstance(normalization, dict) else {}
        if isinstance(definition, dict):
            for key, value in definition.items():
                if key.endswith("_default"):
                    result.setdefault(key[: -len("_default")], value)
                else:
                    result[key] = value
        return result

    @staticmethod
    def _comparison_expected(window: str) -> dict[str, Any] | None:
        marker_groups = {
            "return": ("TEST_RETURN", "TST_RET"),
            "errno": ("TEST_ERRNO", "TST_ERR"),
        }

        def operands(markers: tuple[str, ...]) -> list[str]:
            names = "|".join(markers)
            simple = (
                r"(?:(?:[A-Za-z_][A-Za-z0-9_]*\s*\[[^]\n]+\]\s*\.\s*"
                r"[A-Za-z_][A-Za-z0-9_]*)|"
                r"(?:[A-Za-z_][A-Za-z0-9_]*\s*->\s*[A-Za-z_][A-Za-z0-9_]*)|"
                r"(?:\(\s*-?[A-Za-z_][A-Za-z0-9_]*\s*\))|-?\d+|"
                r"(?:-?[A-Za-z_][A-Za-z0-9_]*(?!\s*(?:\[|->|\.))))"
            )
            patterns = [
                re.compile(rf"\b(?:{names})\b\s*(?:==|!=)\s*(?P<value>{simple})"),
                re.compile(rf"(?P<value>{simple})\s*(?:==|!=)\s*\b(?:{names})\b"),
            ]
            found: list[tuple[int, str]] = []
            for pattern in patterns:
                for match in pattern.finditer(window):
                    value = clean_expr(match.group("value")).strip("() ")
                    found.append((match.start(), value))
            return [value for _start, value in sorted(set(found))]

        returns = operands(marker_groups["return"])
        errnos = operands(marker_groups["errno"])
        if len(returns) > 1 or len(errnos) > 1:
            return None
        if errnos:
            return {
                "kind": "return_errno",
                "return": returns[0] if returns else "-1",
                "errno": errnos[0],
            }
        if returns:
            return {"kind": "return_value", "return": returns[0]}
        return None

    def _preconditions(self, syscall: str, args: list[str], expected: dict[str, Any], source: str) -> list[str]:
        rules = self.config.get("preconditions", [])
        haystack = " ".join([syscall, source, *[str(arg) for arg in args], str(expected)])
        tags: list[str] = []
        if isinstance(rules, list):
            for row in rules:
                if not isinstance(row, dict) or not isinstance(row.get("tag"), str):
                    continue
                patterns = row.get("any", [])
                errno = row.get("errno")
                matched = errno is not None and expected.get("errno") == errno
                if isinstance(patterns, list):
                    matched = matched or any(re.search(str(pattern), haystack) for pattern in patterns)
                if matched and row["tag"] not in tags:
                    tags.append(row["tag"])
        return tags

    def _expand_baseline(
        self,
        syscall: str,
        expression: str,
        expected: dict[str, Any],
        arrays: list[StructArray],
    ) -> list[tuple[list[str], dict[str, Any], dict[str, Any]]]:
        used = set(
            re.findall(r"tc->([A-Za-z_][A-Za-z0-9_]*)", expression + " " + str(expected))
        )
        if not used:
            _name, args = self._infer_call(expression, syscall)
            return [(args, expected, {})]
        selected = next((array for array in arrays if used.issubset(array.fields)), None)
        if selected is None:
            return []
        result: list[tuple[list[str], dict[str, Any], dict[str, Any]]] = []
        for index, row in enumerate(selected.rows):
            expanded = _substitute(expression, row)
            inferred, args = self._infer_call(expanded, syscall)
            if inferred != syscall:
                continue
            expanded_expected = {
                key: _substitute(str(value), row) if isinstance(value, str) else value
                for key, value in expected.items()
            }
            result.append(
                (args, expanded_expected, {"array": selected.name, "case_index": index})
            )
        return result

    def _candidate_field(self, field: str) -> bool:
        definition = self.config.get("struct_evidence", {})
        configured = (
            definition.get("expected_field_pattern")
            if isinstance(definition, dict)
            else None
        )
        pattern = (
            configured
            if isinstance(configured, str) and configured
            else r"^(?:exp(?:ected)?_?(?:errno|err|error|ret(?:urn|val|value)?|result)|experrno|retval|errno)$"
        )
        return bool(re.match(pattern, field, re.I))

    @staticmethod
    def _nearest_alias(
        name: str, aliases: list[PointerAlias], before: int
    ) -> PointerAlias | None:
        eligible = [alias for alias in aliases if alias.name == name and alias.start < before]
        return max(eligible, key=lambda alias: alias.start) if eligible else None

    @staticmethod
    def _substitute_array_accesses(
        value: str, array: StructArray, alias_names: set[str], row: dict[str, str]
    ) -> str:
        result = value
        patterns = [
            rf"\b{re.escape(array.name)}\s*\[[^]]+\]\s*\.\s*"
            r"(?P<field>[A-Za-z_][A-Za-z0-9_]*)"
        ]
        patterns.extend(
            rf"\b{re.escape(alias)}\s*->\s*(?P<field>[A-Za-z_][A-Za-z0-9_]*)"
            for alias in sorted(alias_names)
        )

        def dereference(field: str) -> str:
            raw = row[field]
            return clean_expr(raw[1:] if raw.startswith("&") else f"*{raw}")

        for access in patterns:
            result = re.sub(
                rf"\*\s*\(\s*(?:{access})\s*\)",
                lambda match: dereference(match.group("field")),
                result,
            )
            result = re.sub(
                rf"\*\s*(?:{access})",
                lambda match: dereference(match.group("field")),
                result,
            )
            result = re.sub(
                access,
                lambda match: row[match.group("field")],
                result,
            )
        return clean_expr(result)

    def _expand_candidate(
        self,
        syscall: str,
        expression: str,
        expected: dict[str, Any],
        arrays: list[StructArray],
        aliases: list[PointerAlias],
        call: Call,
    ) -> tuple[
        list[tuple[list[str], dict[str, Any], dict[str, Any]]],
        str | None,
        set[tuple[str, str]],
    ]:
        combined = " ".join(
            [expression, *[str(value) for value in expected.values() if isinstance(value, str)]]
        )
        selected: dict[str, dict[str, Any]] = {}
        array_by_name = {array.name: array for array in arrays}
        for array in arrays:
            pattern = re.compile(
                rf"\b{re.escape(array.name)}\s*\[\s*(?P<index>[^]]+)\s*\]\s*\.\s*"
                r"(?P<field>[A-Za-z_][A-Za-z0-9_]*)"
            )
            for match in pattern.finditer(combined):
                state = selected.setdefault(
                    array.name, {"fields": set(), "indices": set(), "aliases": set()}
                )
                state["fields"].add(match.group("field"))
                state["indices"].add(clean_expr(match.group("index")))

        pointer_uses = list(
            re.finditer(
                r"\b(?P<alias>[A-Za-z_][A-Za-z0-9_]*)\s*->\s*"
                r"(?P<field>[A-Za-z_][A-Za-z0-9_]*)",
                combined,
            )
        )
        unresolved_pointer_fields: dict[str, set[str]] = {}
        for match in pointer_uses:
            name = match.group("alias")
            field = match.group("field")
            alias = self._nearest_alias(name, aliases, call.start)
            if alias is not None and field in array_by_name[alias.array].fields:
                state = selected.setdefault(
                    alias.array, {"fields": set(), "indices": set(), "aliases": set()}
                )
                state["fields"].add(field)
                state["indices"].add(alias.index)
                state["aliases"].add(name)
            elif any(field in array.fields for array in arrays):
                unresolved_pointer_fields.setdefault(name, set()).add(field)

        for name, fields in unresolved_pointer_fields.items():
            candidates = [array for array in arrays if fields.issubset(array.fields)]
            if len(candidates) != 1:
                return [], "ambiguous_pointer_alias", set()
            array = candidates[0]
            state = selected.setdefault(
                array.name, {"fields": set(), "indices": set(), "aliases": set()}
            )
            state["fields"].update(fields)
            state["indices"].add("implicit")
            state["aliases"].add(name)

        if not selected:
            inferred, args = self._infer_call(expression, syscall)
            if inferred != syscall:
                return [], "syscall_not_inferred", set()
            return [(args, expected, {})], None, set()
        if len(selected) != 1:
            return [], "multiple_struct_arrays", set()
        array_name, state = next(iter(selected.items()))
        array = array_by_name[array_name]
        used_fields = set(state["fields"])
        if not used_fields.issubset(array.fields):
            return [], "unknown_struct_field", set()
        if used_fields.intersection(array.mutable_fields):
            return [], "runtime_modified_struct_field", set()
        indices = set(state["indices"])
        simple = {
            value
            for value in indices
            if value == "implicit" or re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*|\d+", value)
        }
        if len(simple) != len(indices):
            return [], "complex_struct_index", set()
        numeric = {int(value) for value in indices if value.isdigit()}
        symbolic = {value for value in indices if not value.isdigit() and value != "implicit"}
        if len(numeric) > 1 or len(symbolic) > 1 or (numeric and symbolic):
            return [], "ambiguous_struct_index", set()
        row_indices = sorted(numeric) if numeric else list(range(len(array.rows)))
        if any(index >= len(array.rows) for index in row_indices):
            return [], "struct_index_out_of_range", set()

        result: list[tuple[list[str], dict[str, Any], dict[str, Any]]] = []
        for index in row_indices:
            row = array.rows[index]
            if not used_fields.issubset(row):
                return [], "missing_designated_field", set()
            expanded = self._substitute_array_accesses(
                expression, array, set(state["aliases"]), row
            )
            inferred, args = self._infer_call(expanded, syscall)
            if inferred != syscall:
                return [], "expanded_syscall_not_inferred", set()
            expanded_expected = {
                key: self._substitute_array_accesses(
                    str(value), array, set(state["aliases"]), row
                )
                if isinstance(value, str)
                else value
                for key, value in expected.items()
            }
            result.append(
                (
                    args,
                    expanded_expected,
                    {"array": array.name, "case_index": index, "origin": "struct"},
                )
            )
        linked = {
            (array.name, field)
            for field in used_fields
            if self._candidate_field(field)
            and any(
                re.search(
                    rf"(?:\.|->)\s*{re.escape(field)}\b",
                    str(value),
                )
                for value in expected.values()
                if isinstance(value, str)
            )
        }
        return result, None, linked

    def _expected_field_refs(
        self,
        expected: dict[str, Any],
        arrays: list[StructArray],
        aliases: list[PointerAlias],
        call: Call,
    ) -> set[tuple[str, str]]:
        text = " ".join(str(value) for value in expected.values() if isinstance(value, str))
        result: set[tuple[str, str]] = set()
        for array in arrays:
            for match in re.finditer(
                rf"\b{re.escape(array.name)}\s*\[[^]]+\]\s*\.\s*"
                r"([A-Za-z_][A-Za-z0-9_]*)",
                text,
            ):
                if self._candidate_field(match.group(1)):
                    result.add((array.name, match.group(1)))
        for match in re.finditer(
            r"\b([A-Za-z_][A-Za-z0-9_]*)\s*->\s*([A-Za-z_][A-Za-z0-9_]*)",
            text,
        ):
            alias_name, field = match.groups()
            if not self._candidate_field(field):
                continue
            alias = self._nearest_alias(alias_name, aliases, call.start)
            if alias:
                result.add((alias.array, field))
                continue
            candidates = [array for array in arrays if field in array.fields]
            if len(candidates) == 1:
                result.add((candidates[0].name, field))
        return result

    def _document_diagnostics(
        self,
        syscall: str,
        relative: str,
        documents: list[DocumentBlock],
        normalized: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        diagnostics: list[dict[str, Any]] = []
        valid_names = {syscall}
        configured = self.aliases.get(syscall, [])
        if isinstance(configured, list):
            valid_names.update(str(item).lower() for item in configured)
        for document in documents:
            if document.syscalls and not set(document.syscalls).intersection(valid_names):
                diagnostics.append(
                    {
                        "severity": "conflict",
                        "kind": "document_syscall_conflict",
                        "message": (
                            f"document names {', '.join(document.syscalls)} but executable assertions "
                            f"target {syscall}"
                        ),
                        "document": {
                            "file": relative,
                            "line": document.line,
                            "content_hash": document.content_hash,
                        },
                        "resolution": "code_assertion_wins",
                    }
                )
            for row in normalized:
                expected = row.get("expected", {})
                if not isinstance(expected, dict):
                    continue
                kind = expected.get("kind")
                code_direction = (
                    "failure"
                    if kind == "return_errno"
                    else "success"
                    if kind in {"success", "return_fd", "positive_return"}
                    else None
                )
                source = row.get("source", {})
                code = {
                    "file": source.get("file") if isinstance(source, dict) else relative,
                    "line": source.get("line") if isinstance(source, dict) else None,
                    "recognizer_id": row.get("recognizer_id"),
                    "case": row.get("case"),
                }
                if (
                    document.direction
                    and code_direction
                    and document.direction != code_direction
                ):
                    diagnostics.append(
                        {
                            "severity": "conflict",
                            "kind": "document_direction_conflict",
                            "message": (
                                f"document expects {document.direction} but executable assertion "
                                f"expects {code_direction}"
                            ),
                            "document": {
                                "file": relative,
                                "line": document.line,
                                "content_hash": document.content_hash,
                            },
                            "code": code,
                            "resolution": "code_assertion_wins",
                        }
                    )
                errno = expected.get("errno")
                if (
                    isinstance(errno, str)
                    and re.fullmatch(r"E[A-Z0-9]{2,}", errno)
                    and document.errnos
                    and errno not in document.errnos
                ):
                    diagnostics.append(
                        {
                            "severity": "conflict",
                            "kind": "document_errno_conflict",
                            "message": (
                                f"document errno set does not contain executable errno {errno}"
                            ),
                            "document": {
                                "file": relative,
                                "line": document.line,
                                "content_hash": document.content_hash,
                                "errnos": list(document.errnos),
                            },
                            "code": code,
                            "resolution": "code_assertion_wins",
                        }
                    )
        unique: dict[str, dict[str, Any]] = {}
        for diagnostic in diagnostics:
            unique[content_hash(diagnostic)] = diagnostic
        return list(unique.values())

    def extract(self, item: dict[str, Any]) -> dict[str, Any]:
        raw: list[dict[str, Any]] = []
        normalized: list[dict[str, Any]] = []
        diagnostics: list[dict[str, Any]] = []
        matched_ids = {row["recognizer_id"] for row in item["recognition"]}
        recognizers = [row for row in self.recognizers if row["id"] in matched_ids]
        names = {
            str(name)
            for recognizer in recognizers
            for name in recognizer.get("names", [])
            if isinstance(name, str)
        }
        for source in item["files"]:
            text = source.read_text(encoding="utf-8", errors="replace")
            arrays = (
                _legacy_struct_arrays(text)
                if self.extractor_profile == "baseline"
                else _struct_arrays(text)
            )
            aliases = _pointer_aliases(text, arrays) if self.extractor_profile == "candidate" else []
            documents = _document_blocks(text) if self.extractor_profile == "candidate" else []
            relative = str(source.relative_to(self.location))
            linked_fields: set[tuple[str, str]] = set()
            file_normalized: list[dict[str, Any]] = []
            for document in documents:
                evidence = {
                    "syscall": item["syscall"],
                    "source": {"file": relative, "line": document.line},
                    "recognizer_id": "ltp.document.context",
                    "evidence_class": "context",
                    "document": {
                        "text": document.text,
                        "content_hash": document.content_hash,
                        "syscalls": list(document.syscalls),
                        "direction": document.direction,
                        "errnos": list(document.errnos),
                    },
                }
                evidence["evidence_hash"] = content_hash(evidence)
                raw.append(evidence)
            for call in find_calls(text, source, names):
                for recognizer in recognizers:
                    if not self._recognizer_matches(recognizer, call, text, item["syscall"]):
                        continue
                    expression = (
                        call.text
                        if recognizer.get("kind") == "safe_helper"
                        else call.args[int(recognizer.get("call_argument", 0))]
                    )
                    _inferred, syscall_args = self._infer_call(expression, item["syscall"])
                    expected = self._expected(recognizer, call, text)
                    evidence = {
                        "syscall": item["syscall"],
                        "source": {"file": relative, "line": call.line},
                        "recognizer_id": recognizer["id"],
                        "macro": call.name,
                        "call": expression,
                        "args": syscall_args if recognizer.get("kind") != "safe_helper" else call.args,
                        "expected": expected,
                    }
                    if self.extractor_profile == "candidate":
                        if recognizer.get("emit_rule", True) is False:
                            evidence["evidence_class"] = "context"
                            evidence["resolution_reason"] = "context_only_recognizer"
                            evidence["evidence_hash"] = content_hash(evidence)
                            raw.append(evidence)
                            continue
                        if expected is None:
                            evidence["evidence_class"] = "unresolved"
                            evidence["resolution_reason"] = "expected_result_not_resolved"
                            evidence["evidence_hash"] = content_hash(evidence)
                            raw.append(evidence)
                            continue
                        linked_fields.update(
                            self._expected_field_refs(expected, arrays, aliases, call)
                        )
                        cases, unresolved_reason, resolved_fields = self._expand_candidate(
                            item["syscall"], expression, expected, arrays, aliases, call
                        )
                        linked_fields.update(resolved_fields)
                        if unresolved_reason or not cases:
                            evidence["evidence_class"] = "unresolved"
                            evidence["resolution_reason"] = unresolved_reason or "no_struct_cases"
                            evidence["evidence_hash"] = content_hash(evidence)
                            raw.append(evidence)
                            continue
                        evidence["evidence_class"] = "authoritative"
                    else:
                        if expected is None or recognizer.get("emit_rule", True) is False:
                            evidence["evidence_hash"] = content_hash(evidence)
                            raw.append(evidence)
                            continue
                        cases = self._expand_baseline(
                            item["syscall"], expression, expected, arrays
                        )
                        if not cases and "tc->" not in expression:
                            cases = [(evidence["args"], expected, {})]
                    evidence["evidence_hash"] = content_hash(evidence)
                    raw.append(evidence)
                    if expected is None or recognizer.get("emit_rule", True) is False:
                        continue
                    for args, case_expected, expansion in cases:
                        preconditions = self._preconditions(item["syscall"], args, case_expected, relative)
                        semantics = {
                            "preconditions": preconditions,
                            "action": {
                                "operation": "invoke_syscall",
                                "syscall": item["syscall"],
                                "arguments": args,
                            },
                            "expected_result": case_expected,
                            "errno": [case_expected["errno"]]
                            if isinstance(case_expected.get("errno"), str) and case_expected["errno"]
                            else [],
                        }
                        template = self.config.get("rule_template", {})
                        category = (
                            template.get("category", "syscall_behavior")
                            if isinstance(template, dict)
                            else "syscall_behavior"
                        )
                        normalized_row = {
                            **evidence,
                            "case": re.sub(
                                r"[^A-Za-z0-9_]+",
                                "_",
                                f"{source.stem}_{call.line}_{expansion.get('case_index', 'raw')}",
                            ),
                            "args": args,
                            "preconditions": preconditions,
                            "semantics": semantics,
                            "category": category,
                            "expansion": expansion,
                        }
                        stable_rule_id = recognizer.get("rule_id")
                        if not isinstance(stable_rule_id, str) and isinstance(template, dict):
                            stable_rule_id = template.get("rule_id")
                        if isinstance(stable_rule_id, str) and stable_rule_id:
                            normalized_row["rule_id"] = stable_rule_id.format(
                                syscall=item["syscall"], recognizer_id=recognizer["id"]
                            )
                        normalized.append(normalized_row)
                        file_normalized.append(normalized_row)
            if self.extractor_profile == "candidate":
                for array in arrays:
                    for field in array.fields:
                        identity = (array.name, field)
                        if not self._candidate_field(field) or identity in linked_fields:
                            continue
                        evidence = {
                            "syscall": item["syscall"],
                            "source": {"file": relative, "line": array.line},
                            "recognizer_id": "ltp.struct.expected-candidate",
                            "evidence_class": "unresolved",
                            "resolution_reason": "expected_field_not_linked_to_assertion",
                            "struct": {
                                "array": array.name,
                                "field": field,
                                "case_count": len(array.rows),
                            },
                        }
                        evidence["evidence_hash"] = content_hash(evidence)
                        raw.append(evidence)
                diagnostics.extend(
                    self._document_diagnostics(
                        item["syscall"], relative, documents, file_normalized
                    )
                )
        return {"raw": raw, "normalized": normalized, "diagnostics": diagnostics}
