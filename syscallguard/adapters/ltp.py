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


@dataclass(frozen=True)
class StructArray:
    name: str
    fields: list[str]
    rows: list[dict[str, str]]


def clean_expr(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


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
            )
        )
    return calls


def _struct_arrays(text: str) -> list[StructArray]:
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
    adapter_version = "2"

    def __init__(self, location: Path, rules_path: Path) -> None:
        self.location = location
        self.rules_path = rules_path
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
                return {
                    "kind": "return_errno",
                    "return": clean_expr(return_match.group(1)) if return_match else "-1",
                    "errno": errno_match.group(1),
                }
            if return_match:
                return {"kind": "return_value", "return": clean_expr(return_match.group(1))}
            return None
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

    def _expand(self, syscall: str, expression: str, expected: dict[str, Any], arrays: list[StructArray]) -> list[tuple[list[str], dict[str, Any], dict[str, Any]]]:
        used = set(re.findall(r"tc->([A-Za-z_][A-Za-z0-9_]*)", expression + " " + str(expected)))
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
            result.append((args, expanded_expected, {"array": selected.name, "case_index": index}))
        return result

    def extract(self, item: dict[str, Any]) -> dict[str, Any]:
        raw: list[dict[str, Any]] = []
        normalized: list[dict[str, Any]] = []
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
            arrays = _struct_arrays(text)
            relative = str(source.relative_to(self.location))
            for call in find_calls(text, source, names):
                for recognizer in recognizers:
                    if not self._recognizer_matches(recognizer, call, text, item["syscall"]):
                        continue
                    expression = call.text if recognizer.get("kind") == "safe_helper" else call.args[int(recognizer.get("call_argument", 0))]
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
                    evidence["evidence_hash"] = content_hash(evidence)
                    raw.append(evidence)
                    if expected is None or recognizer.get("emit_rule", True) is False:
                        continue
                    cases = self._expand(item["syscall"], expression, expected, arrays)
                    if not cases and "tc->" not in expression:
                        cases = [(evidence["args"], expected, {})]
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
                        category = template.get("category", "syscall_behavior") if isinstance(template, dict) else "syscall_behavior"
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
        return {"raw": raw, "normalized": normalized}
