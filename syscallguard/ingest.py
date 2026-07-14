from __future__ import annotations

import argparse
import os
import sys
import tempfile
from pathlib import Path
from typing import Any, Iterable

import yaml

from .adapters.ltp import LtpAdapter
from .common import (
    SCHEMA_VERSION,
    SyscallGuardError,
    content_hash,
    repository_snapshot_hash,
    load_mapping,
    new_run_id,
    normalize_run_id,
    read_frontmatter,
    repo_root,
    slug,
    utc_now,
    version_content_hash,
)


GLOBAL_DEFAULT_COUNT = 20
REPORT_KIND = "syscallguard_ingest_report"
REPORT_RESULTS = {"formed_rules", "no_rules"}


def resolve_source(source: str | Path | None, root: Path) -> tuple[Path, str]:
    """Resolve an alias before treating an explicit value as a descriptor path."""
    index_path = root / "sources" / "index.yaml"
    if index_path.is_file():
        index = load_mapping(index_path)
    elif source is None:
        raise SyscallGuardError(f"missing YAML file: {index_path}")
    else:
        index = {}
    aliases = index.get("sources", index.get("aliases", {}))
    value: Any = str(source) if source is not None else index.get("default_source")
    if not isinstance(value, str) or not value:
        raise SyscallGuardError(
            f"no source was supplied and {index_path} has no default_source"
        )

    if isinstance(aliases, dict) and value in aliases:
        resolved = aliases[value]
        reason = "default_source" if source is None else "source_alias"
    elif source is None:
        raise SyscallGuardError(
            f"default source alias {value!r} is not defined in {index_path}"
        )
    else:
        resolved = value
        reason = "explicit_descriptor"
    if not isinstance(resolved, str) or not resolved:
        raise SyscallGuardError(f"source alias {value!r} has no descriptor path")
    path = Path(resolved).expanduser()
    if not path.is_absolute():
        path = root / path
    path = path.resolve()
    if not path.is_file():
        raise SyscallGuardError(f"source descriptor does not exist: {path}")
    return path, reason


def resolve_count(
    value: int | str | None, descriptor: dict[str, Any]
) -> tuple[int | None, str, str]:
    if value is not None:
        raw: Any = value
        reason = "command"
    elif "default_count" in descriptor:
        raw = descriptor["default_count"]
        reason = "descriptor"
    else:
        raw = GLOBAL_DEFAULT_COUNT
        reason = "global_default"
    if isinstance(raw, str) and raw.lower() == "all":
        return None, "all", reason
    if isinstance(raw, bool):
        raise SyscallGuardError("count must be a positive integer or 'all'")
    try:
        parsed = int(raw)
    except (TypeError, ValueError) as exc:
        raise SyscallGuardError("count must be a positive integer or 'all'") from exc
    if parsed <= 0 or str(raw).strip() != str(parsed):
        raise SyscallGuardError("count must be a positive integer or 'all'")
    return parsed, str(parsed), reason


def resolve_syscalls(value: str | None) -> list[str] | None:
    """Normalize an explicit comma-separated syscall selection."""
    if value is None:
        return None
    if not isinstance(value, str):
        raise SyscallGuardError("syscalls must be a comma-separated list")
    names = [item.strip().lower() for item in value.split(",")]
    if not names or any(not name for name in names):
        raise SyscallGuardError(
            "syscalls must be a non-empty comma-separated list without empty entries"
        )
    return sorted(set(names))


def require_descriptor(
    path: Path, root: Path
) -> tuple[dict[str, Any], Path, str, LtpAdapter]:
    descriptor = load_mapping(path)
    source_id = descriptor.get("source_id")
    if not isinstance(source_id, str) or not source_id:
        raise SyscallGuardError(f"source descriptor must define source_id: {path}")
    adapter_name = descriptor.get("adapter")
    if adapter_name != "ltp":
        raise SyscallGuardError(f"unsupported source adapter: {adapter_name!r}")
    location_value = descriptor.get("location")
    if not isinstance(location_value, str) or not location_value:
        raise SyscallGuardError(f"source descriptor must define location: {path}")
    location = Path(location_value).expanduser().resolve()
    if not location.is_dir():
        raise SyscallGuardError(f"source location does not exist: {location}")
    snapshot_hash = repository_snapshot_hash(location)
    rules_path = root / "sources" / "adapters" / "ltp" / "recognition-rules.yaml"
    if not rules_path.is_file():
        rules_path = repo_root() / "sources" / "adapters" / "ltp" / "recognition-rules.yaml"
    return descriptor, location, snapshot_hash, LtpAdapter(location, rules_path)


def _report_source_id(report: dict[str, Any]) -> str | None:
    source = report.get("source")
    if not isinstance(source, dict):
        return None
    value = source.get("id", source.get("source_id"))
    return value if isinstance(value, str) and value else None


def _report_syscalls(report: dict[str, Any]) -> list[dict[str, Any]]:
    rows = report.get("syscalls", [])
    if not isinstance(rows, list):
        return []
    return [row for row in rows if isinstance(row, dict)]


def load_ingest_report(root: Path, report_id: str) -> dict[str, Any]:
    report_id = normalize_run_id(report_id)
    path = root / "runs" / report_id / "report.md"
    report, _body = read_frontmatter(path)
    if report.get("kind") != REPORT_KIND or report.get("report_id") != report_id:
        raise SyscallGuardError(f"not a SyscallGuard ingest report: {path}")
    if not isinstance(report.get("generated_at_utc"), str):
        raise SyscallGuardError(f"ingest report has no generated_at_utc: {path}")
    source_id = _report_source_id(report)
    if source_id is None:
        raise SyscallGuardError(f"ingest report has no source id: {path}")
    for row in _report_syscalls(report):
        if not isinstance(row.get("syscall"), str):
            raise SyscallGuardError(f"ingest report has an invalid syscall row: {path}")
        if row.get("result") not in REPORT_RESULTS:
            raise SyscallGuardError(f"ingest report has an invalid result: {path}")
    return report


def scan_ingest_reports(
    root: Path,
) -> tuple[
    dict[tuple[str, str], dict[str, Any]],
    dict[str, dict[str, Any]],
]:
    """Return the latest report row per (source, syscall) and all valid reports."""
    latest: dict[tuple[str, str], dict[str, Any]] = {}
    reports: dict[str, dict[str, Any]] = {}
    runs = root / "runs"
    if not runs.is_dir():
        return latest, reports
    for path in sorted(runs.glob("spec-*/report.md")):
        try:
            report, _body = read_frontmatter(path)
        except SyscallGuardError:
            # Legacy Markdown reports are not state and are ignored.
            continue
        report_id = report.get("report_id")
        generated = report.get("generated_at_utc")
        source_id = _report_source_id(report)
        if (
            report.get("kind") != REPORT_KIND
            or report_id != path.parent.name
            or not isinstance(generated, str)
            or source_id is None
        ):
            continue
        reports[str(report_id)] = report
        for row in _report_syscalls(report):
            syscall = row.get("syscall")
            if not isinstance(syscall, str) or row.get("result") not in REPORT_RESULTS:
                continue
            candidate = {
                "report_id": report_id,
                "generated_at_utc": generated,
                "source_id": source_id,
                **row,
            }
            key = (source_id, syscall)
            prior = latest.get(key)
            order = (generated, str(report_id))
            prior_order = (
                str(prior.get("generated_at_utc", "")),
                str(prior.get("report_id", "")),
            ) if prior else ("", "")
            if prior is None or order > prior_order:
                latest[key] = candidate
    return latest, reports


def assert_latest_ingest_report(root: Path, report: dict[str, Any]) -> None:
    latest, _reports = scan_ingest_reports(root)
    report_id = str(report["report_id"])
    source_id = _report_source_id(report)
    assert source_id is not None
    superseded: list[str] = []
    for row in _report_syscalls(report):
        syscall = str(row["syscall"])
        current = latest.get((source_id, syscall))
        if current is not None and current.get("report_id") != report_id:
            superseded.append(
                f"{syscall} -> {current.get('report_id')}"
            )
    if superseded:
        raise SyscallGuardError(
            f"ingest report {report_id} is superseded: " + ", ".join(superseded)
        )


def _needs_processing(
    item: dict[str, Any], prior: dict[str, Any] | None
) -> tuple[bool, str]:
    if prior is None:
        return True, "new"
    if prior.get("source_fingerprint") != item["source_fingerprint"]:
        return True, "source_changed"
    if prior.get("recognition_fingerprint") != item["recognition_fingerprint"]:
        return True, "recognition_changed"
    return False, "unchanged"


def _rule_files(root: Path) -> dict[str, tuple[Path, dict[str, Any]]]:
    result: dict[str, tuple[Path, dict[str, Any]]] = {}
    directory = root / "library" / "rules"
    if not directory.is_dir():
        return result
    for path in sorted(directory.glob("*.yaml")):
        entity = load_mapping(path)
        if entity.get("kind") != "syscallguard_rule":
            raise SyscallGuardError(f"invalid rule entity: {path}")
        rule_id = entity.get("rule_id")
        if not isinstance(rule_id, str) or not rule_id:
            raise SyscallGuardError(f"rule has no rule_id: {path}")
        if rule_id in result:
            raise SyscallGuardError(f"duplicate rule id {rule_id}: {path}")
        expected_hash = version_content_hash(entity)
        if entity.get("semantic_hash") != expected_hash:
            raise SyscallGuardError(f"rule semantic_hash mismatch: {path}")
        result[rule_id] = (path, entity)
    return result


def _source_identity(source: dict[str, Any]) -> tuple[str, str, int, str, str]:
    return (
        str(source.get("source_id", "")),
        str(source.get("file", "")),
        int(source.get("line", 0) or 0),
        str(source.get("recognizer_id", "")),
        str(source.get("case", "")),
    )


def _provenance(
    normalized: dict[str, Any], descriptor: dict[str, Any], source_snapshot_hash: str
) -> dict[str, Any]:
    source = normalized.get("source", {})
    if not isinstance(source, dict):
        source = {}
    return {
        "source_id": descriptor["source_id"],
        "source_type": descriptor["adapter"],
        "source_snapshot_hash": source_snapshot_hash,
        "file": source.get("file"),
        "line": source.get("line"),
        "recognizer_id": normalized.get("recognizer_id"),
        "evidence_hash": normalized.get("evidence_hash"),
        "case": normalized.get("case"),
    }


def _merge_rules(
    root: Path,
    normalized_rows: list[dict[str, Any]],
    descriptor: dict[str, Any],
    source_snapshot_hash: str,
    now: str,
) -> tuple[
    dict[str, tuple[Path, dict[str, Any], str]],
    dict[str, list[str]],
    list[dict[str, Any]],
]:
    rules = _rule_files(root)
    staged: dict[str, tuple[Path, dict[str, Any], str]] = {}
    refs: dict[str, list[str]] = {}
    conflicts: list[dict[str, Any]] = []

    def available() -> dict[str, tuple[Path, dict[str, Any]]]:
        current = dict(rules)
        current.update((key, (row[0], row[1])) for key, row in staged.items())
        return current

    for normalized in normalized_rows:
        syscall = str(normalized["syscall"])
        semantics = normalized["semantics"]
        category = str(normalized.get("category", "syscall_behavior"))
        semantic_hash = content_hash({"category": category, "semantics": semantics})
        provenance = _provenance(normalized, descriptor, source_snapshot_hash)
        current = available()
        same = next(
            (
                (rule_id, path, entity)
                for rule_id, (path, entity) in current.items()
                if entity.get("semantic_hash") == semantic_hash
            ),
            None,
        )
        action = "reused"
        old_entity: dict[str, Any] | None = None
        if same is not None:
            rule_id, path, old_entity = same
            entity = dict(old_entity)
            if rule_id in staged:
                action = staged[rule_id][2]
        else:
            identity = _source_identity(provenance)
            prior = next(
                (
                    (rule_id, path, entity)
                    for rule_id, (path, entity) in current.items()
                    if any(
                        _source_identity(row) == identity
                        for row in entity.get("sources", [])
                        if isinstance(row, dict)
                    )
                ),
                None,
            )
            explicit = normalized.get("rule_id")
            if prior is not None and not explicit and len(prior[2].get("sources", [])) == 1:
                rule_id, path, old_entity = prior
                entity = dict(old_entity)
                entity.update(
                    {
                        "category": category,
                        "semantics": semantics,
                        "semantic_hash": semantic_hash,
                        "generated_at_utc": now,
                    }
                )
                entity["sources"] = []
                action = "semantic_updated"
            else:
                if prior is not None and not explicit:
                    prior_rule_id, prior_path, prior_entity = prior
                    detached = dict(prior_entity)
                    detached["sources"] = [
                        row
                        for row in detached.get("sources", [])
                        if not isinstance(row, dict)
                        or _source_identity(row) != identity
                    ]
                    staged[prior_rule_id] = (prior_path, detached, "sources_updated")
                preferred = (
                    str(explicit)
                    if isinstance(explicit, str) and explicit
                    else "LTP_" + semantic_hash.split(":", 1)[1][:16].upper()
                )
                rule_id = preferred
                if (
                    rule_id in current
                    and current[rule_id][1].get("semantic_hash") != semantic_hash
                ):
                    rule_id = f"{preferred}--{semantic_hash.split(':', 1)[1][:12]}"
                    conflicts.append(
                        {
                            "preferred_rule_id": preferred,
                            "variant_rule_id": rule_id,
                            "reason": "stable rule id has different semantics",
                        }
                    )
                    action = "conflict_variant"
                else:
                    action = "created"
                path = root / "library" / "rules" / f"{slug(rule_id)}.yaml"
                entity = {
                    "schema_version": SCHEMA_VERSION,
                    "kind": "syscallguard_rule",
                    "rule_id": rule_id,
                    "category": category,
                    "semantics": semantics,
                    "semantic_hash": semantic_hash,
                    "generated_at_utc": now,
                    "sources": [],
                }

        sources = entity.get("sources", [])
        sources = list(sources) if isinstance(sources, list) else []
        identity = _source_identity(provenance)
        same_identity = [
            row
            for row in sources
            if isinstance(row, dict) and _source_identity(row) == identity
        ]
        if not any(row == provenance for row in same_identity):
            # A source location is a current provenance record, not an event log.
            sources = [
                row
                for row in sources
                if not isinstance(row, dict) or _source_identity(row) != identity
            ]
            sources.append(provenance)
        entity["sources"] = sorted(
            sources,
            key=lambda row: (
                str(row.get("source_id", "")),
                str(row.get("file", "")),
                int(row.get("line", 0) or 0),
                str(row.get("recognizer_id", "")),
                str(row.get("case", "")),
            ),
        )
        if old_entity is not None and entity != old_entity and action == "reused":
            action = "sources_updated"
        staged[rule_id] = (path, entity, action)
        refs.setdefault(syscall, [])
        if rule_id not in refs[syscall]:
            refs[syscall].append(rule_id)
    return staged, refs, conflicts


def _yaml_text(value: Any) -> str:
    return yaml.safe_dump(
        value,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=100,
    )


def _condition_text(semantics: dict[str, Any]) -> str:
    preconditions = semantics.get("preconditions", [])
    names = {
        "INVALID_FD": "文件描述符无效",
    }
    if preconditions:
        return "、".join(names.get(str(item), str(item)) for item in preconditions)
    arguments = semantics.get("action", {}).get("arguments", [])
    if "fd_closed" in arguments:
        return "文件描述符已经关闭"
    if any("get_fd()" in str(item) for item in arguments):
        return "文件描述符有效且处于打开状态"
    return "无额外前置条件"


def _action_text(semantics: dict[str, Any]) -> str:
    action = semantics.get("action", {})
    syscall = action.get("syscall", "未知 syscall")
    arguments = ", ".join(str(item) for item in action.get("arguments", []))
    return f"调用 {syscall}({arguments})"


def _expected_text(semantics: dict[str, Any]) -> str:
    expected = semantics.get("expected_result", {})
    if expected.get("kind") == "return_errno":
        return f"返回 {expected.get('return')}，errno 为 {expected.get('errno')}"
    if expected.get("kind") == "success":
        return f"调用成功，返回 {expected.get('return')}"
    return str(expected)


def _rule_explanation(entity: dict[str, Any]) -> str:
    semantics = entity.get("semantics", {})
    return (
        f"条件：{_condition_text(semantics)}；"
        f"检查：{_action_text(semantics)}；"
        f"预期：{_expected_text(semantics)}。"
    )


def _rule_comment(entity: dict[str, Any]) -> str:
    return f"# 合规检查：{_rule_explanation(entity)}"


def _syscall_index_text(
    entity: dict[str, Any], rule_comments: dict[str, str]
) -> str:
    lines: list[str] = []
    for line in _yaml_text(entity).splitlines():
        if line.startswith("  - rule_id: "):
            rule_id = line.split(": ", 1)[1]
            comment = rule_comments.get(rule_id)
            if comment:
                lines.append(f"  {comment}")
        lines.append(line)
    return "\n".join(lines) + "\n"


def _entity_text(
    entity: dict[str, Any], rule_comments: dict[str, str] | None = None
) -> str:
    text = _yaml_text(entity)
    if entity.get("kind") == "syscallguard_rule":
        return f"{_rule_comment(entity)}\n{text}"
    if entity.get("kind") == "syscallguard_syscall_index":
        return _syscall_index_text(entity, rule_comments or {})
    return text


def _report_text(frontmatter: dict[str, Any]) -> str:
    selected = frontmatter["syscalls"]
    formed = [row for row in selected if row["result"] == "formed_rules"]
    total_rules = sum(len(row["rules"]) for row in formed)
    names = "、".join(row["syscall"] for row in selected) or "无"
    lines = [
        "# Syscall 合规性规则提取报告",
        "",
        "## 结论",
        "",
        f"本次分析了 {names}，发现 {total_rules} 条可执行的合规性规则。",
        "",
    ]
    for row in selected:
        lines.extend([f"## `{row['syscall']}`", ""])
        if row["result"] != "formed_rules":
            lines.append("没有形成可发布的合规性规则。")
            lines.append("")
            continue
        lines.extend(
            [
                f"共形成 {len(row['rules'])} 条规则：",
                "",
                "| 规则 | 条件 | 检查内容 | 预期结果 |",
                "| --- | --- | --- | --- |",
            ]
        )
        for version in row["rules"]:
            rule = frontmatter["rule_details"][version["id"]]
            semantics = rule["semantics"]
            path = f"../../library/rules/{slug(version['id'])}.yaml"
            lines.append(
                f"| [`{version['id']}`]({path}) | {_condition_text(semantics)} | "
                f"{_action_text(semantics)} | {_expected_text(semantics)} |"
            )
    source = frontmatter["source"]
    count = frontmatter["count"]
    lines.extend(
        [
            "",
            "## 技术参考",
            "",
            f"- 报告 ID：`{frontmatter['report_id']}`",
            f"- 来源：`{source['id']}`，内容快照 `{source['snapshot_hash']}`",
            f"- 全局待处理 syscall：{frontmatter['pending_count']}",
        ]
    )
    if "requested_syscalls" in frontmatter:
        requested = "、".join(f"`{name}`" for name in frontmatter["requested_syscalls"])
        lines.append(f"- 指定 syscall：{requested}")
    else:
        lines.append(f"- 提取数量：`{count['value']}`（来源：`{count['source']}`）")
    for row in selected:
        lines.append(
            f"- `{row['syscall']}`：证据 {row['evidence_count']} 条，"
            f"未解析 {row['unresolved_evidence_count']} 条"
        )
    metadata = dict(frontmatter)
    metadata.pop("rule_details", None)
    lines.extend(
        [
            "",
            "<details>",
            "<summary>机器可读元数据</summary>",
            "",
            "<!-- syscallguard-metadata -->",
            "```yaml",
            _yaml_text(metadata).rstrip(),
            "```",
            "</details>",
        ]
    )
    return "\n".join(lines) + "\n"


def _stage_text(destination: Path, text: str) -> Path:
    destination.parent.mkdir(parents=True, exist_ok=True)
    descriptor, name = tempfile.mkstemp(prefix=f".{destination.name}.", dir=destination.parent)
    path = Path(name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
    except BaseException:
        path.unlink(missing_ok=True)
        raise
    return path


def _publish_transaction(
    rule_updates: Iterable[tuple[Path, dict[str, Any]]],
    report_path: Path,
    report_text: str,
) -> None:
    """Stage every output, publish the report last, and roll entities back on failure."""
    updates = list(rule_updates)
    rule_comments = {
        str(entity["rule_id"]): _rule_comment(entity)
        for _path, entity in updates
        if entity.get("kind") == "syscallguard_rule"
    }
    root = report_path.parents[2]
    for _path, entity in updates:
        if entity.get("kind") != "syscallguard_syscall_index":
            continue
        for refs in entity.get("syscalls", {}).values():
            for ref in refs:
                rule_id = str(ref["rule_id"])
                if rule_id in rule_comments:
                    continue
                rule_path = root / str(ref["path"])
                first_line = rule_path.read_text(encoding="utf-8").splitlines()[0]
                if first_line.startswith("# 合规检查："):
                    rule_comments[rule_id] = first_line
    staged: list[tuple[Path, Path]] = []
    originals: dict[Path, bytes | None] = {}
    report_directory_existed = report_path.parent.exists()
    changed: list[Path] = []
    try:
        for destination, entity in updates:
            originals[destination] = destination.read_bytes() if destination.exists() else None
            staged.append(
                (destination, _stage_text(destination, _entity_text(entity, rule_comments)))
            )
        report_temp = _stage_text(report_path, report_text)
        staged.append((report_path, report_temp))
        for destination, temp in staged:
            os.replace(temp, destination)
            changed.append(destination)
    except BaseException:
        for _destination, temp in staged:
            temp.unlink(missing_ok=True)
        report_path.unlink(missing_ok=True)
        for destination in reversed(changed):
            if destination == report_path:
                continue
            original = originals.get(destination)
            if original is None:
                destination.unlink(missing_ok=True)
            else:
                restore = _stage_text(destination, original.decode("utf-8"))
                os.replace(restore, destination)
        if not report_directory_existed:
            try:
                report_path.parent.rmdir()
            except OSError:
                pass
        raise


def run_ingest(
    source: str | Path | None = None,
    count: int | str | None = None,
    root: Path | None = None,
    requested_run_id: str | None = None,
    syscalls: str | None = None,
) -> str:
    root = (root or repo_root()).resolve()
    if count is not None and syscalls is not None:
        raise SyscallGuardError("count and syscalls are mutually exclusive")
    requested_syscalls = resolve_syscalls(syscalls)
    descriptor_path, source_reason = resolve_source(source, root)
    descriptor, _location, source_snapshot_hash, adapter = require_descriptor(descriptor_path, root)
    if requested_syscalls is None:
        limit, count_label, count_reason = resolve_count(count, descriptor)
    else:
        limit, count_label, count_reason = None, None, "explicit_syscalls"
    report_id = requested_run_id or new_run_id(
        "spec",
        {
            "source": str(descriptor_path),
            "count": count_label,
            "syscalls": requested_syscalls,
            "at": utc_now(),
        },
    )
    report_id = normalize_run_id(report_id)
    report_path = root / "runs" / report_id / "report.md"
    if report_path.parent.exists():
        raise SyscallGuardError(f"report already exists: {report_path.parent}")

    latest, _reports = scan_ingest_reports(root)
    discovered = adapter.discover()
    if requested_syscalls is not None:
        available = {str(item["syscall"]) for item in discovered}
        unknown = sorted(set(requested_syscalls) - available)
        if unknown:
            raise SyscallGuardError(
                "requested syscalls do not exist in source: " + ", ".join(unknown)
            )
    candidates = [adapter.prescan(item) for item in discovered]
    pending: list[dict[str, Any]] = []
    reasons: dict[str, str] = {}
    for item in candidates:
        prior = latest.get((str(descriptor["source_id"]), str(item["syscall"])))
        changed, reason = _needs_processing(item, prior)
        if changed:
            pending.append(item)
            reasons[str(item["syscall"])] = reason
    pending.sort(key=lambda item: str(item["syscall"]))
    if requested_syscalls is not None:
        requested_set = set(requested_syscalls)
        selected = [item for item in pending if str(item["syscall"]) in requested_set]
    else:
        selected = pending if limit is None else pending[:limit]

    extracted: dict[str, dict[str, Any]] = {}
    publishable_rows: list[dict[str, Any]] = []
    result_rows: list[dict[str, Any]] = []
    for item in selected:
        syscall = str(item["syscall"])
        try:
            result = adapter.extract(item)
        except SyscallGuardError:
            raise
        except BaseException as exc:
            raise SyscallGuardError(str(exc)) from exc
        raw = result.get("raw", [])
        normalized = result.get("normalized", [])
        if not isinstance(raw, list) or not isinstance(normalized, list):
            raise SyscallGuardError(f"adapter returned invalid evidence for {syscall}")
        normalized_hashes = {
            row.get("evidence_hash")
            for row in normalized
            if isinstance(row, dict) and isinstance(row.get("evidence_hash"), str)
        }
        unresolved = [
            row
            for row in raw
            if not isinstance(row, dict) or row.get("evidence_hash") not in normalized_hashes
        ]
        if unresolved:
            outcome = "no_rules"
            reason = "unresolved_evidence"
        elif not normalized:
            outcome = "no_rules"
            reason = "no_evidence" if not raw else "zero_rules"
        else:
            outcome = "formed_rules"
            reason = "all_evidence_resolved"
            publishable_rows.extend(row for row in normalized if isinstance(row, dict))
        extracted[syscall] = {
            "item": item,
            "raw": raw,
            "normalized": normalized,
            "unresolved_count": len(unresolved),
            "outcome": outcome,
            "reason": reason,
        }

    generated_at = utc_now()
    staged_rules, refs, conflicts = _merge_rules(
        root, publishable_rows, descriptor, source_snapshot_hash, generated_at
    )
    current_rules = _rule_files(root)
    for item in selected:
        syscall = str(item["syscall"])
        result = extracted[syscall]
        rule_versions: list[dict[str, str]] = []
        if result["outcome"] == "formed_rules":
            for rule_id in sorted(refs.get(syscall, [])):
                entity = staged_rules.get(rule_id, current_rules.get(rule_id))[1]
                rule_versions.append(
                    {
                        "id": rule_id,
                        "generated_at_utc": str(entity["generated_at_utc"]),
                        "content_hash": version_content_hash(entity),
                    }
                )
        result_rows.append(
            {
                "syscall": syscall,
                "source_fingerprint": item["source_fingerprint"],
                "recognition_fingerprint": item["recognition_fingerprint"],
                "selection_reason": reasons[syscall],
                "result": result["outcome"],
                "rules": rule_versions,
                "evidence_count": len(result["raw"]),
                "unresolved_evidence_count": result["unresolved_count"],
                "reason": result["reason"],
            }
        )

    frontmatter: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "kind": REPORT_KIND,
        "report_id": report_id,
        "generated_at_utc": generated_at,
        "source": {
            "id": descriptor["source_id"],
            "type": descriptor["adapter"],
            "snapshot_hash": source_snapshot_hash,
            "descriptor_hash": content_hash(descriptor),
            "recognition_rules_hash": adapter.rules_hash,
            "resolution": source_reason,
        },
        "count": {"value": count_label, "source": count_reason},
        "pending_count": len(pending),
        "selected_syscalls": [str(item["syscall"]) for item in selected],
        "syscalls": result_rows,
        "rule_details": {
            version["id"]: staged_rules.get(version["id"], current_rules.get(version["id"]))[1]
            for row in result_rows
            for version in row["rules"]
        },
    }
    if requested_syscalls is not None:
        frontmatter["requested_syscalls"] = requested_syscalls
    if conflicts:
        frontmatter["conflicts"] = conflicts

    updates: list[tuple[Path, dict[str, Any]]] = []
    for rule_id, (path, entity, _action) in staged_rules.items():
        existing = current_rules.get(rule_id)
        if existing is None or existing[1] != entity:
            updates.append((path, entity))
    indexed_rows = dict(latest)
    source_id = str(descriptor["source_id"])
    for row in result_rows:
        indexed_rows[(source_id, row["syscall"])] = row
    syscall_rules: dict[str, dict[str, dict[str, str]]] = {}
    for (_row_source, syscall), row in indexed_rows.items():
        syscall_rules.setdefault(syscall, {})
        if row.get("result") != "formed_rules":
            continue
        for version in row.get("rules", []):
            rule_id = version["id"]
            syscall_rules[syscall][rule_id] = {
                "rule_id": rule_id,
                "path": f"library/rules/{slug(rule_id)}.yaml",
            }
    syscall_index = {
        "schema_version": SCHEMA_VERSION,
        "kind": "syscallguard_syscall_index",
        "syscalls": {
            syscall: list(rule_map.values())
            for syscall, rule_map in sorted(syscall_rules.items())
        },
    }
    index_path = root / "library" / "syscalls.yaml"
    updates.append((index_path, syscall_index))
    try:
        _publish_transaction(updates, report_path, _report_text(frontmatter))
    except SyscallGuardError:
        raise
    except BaseException as exc:
        raise SyscallGuardError(str(exc)) from exc
    return report_id


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Ingest target-independent syscall specifications"
    )
    parser.add_argument("--source", help="source alias or descriptor YAML")
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--count", help="positive integer or all")
    selection.add_argument("--syscalls", help="comma-separated syscall names")
    parser.add_argument("--root", type=Path, default=repo_root(), help=argparse.SUPPRESS)
    parser.add_argument("--run-id", help=argparse.SUPPRESS)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    requested = args.run_id or new_run_id(
        "spec", {"source": args.source, "count": args.count, "syscalls": args.syscalls}
    )
    try:
        report_id = run_ingest(
            args.source, args.count, args.root, requested, args.syscalls
        )
    except SyscallGuardError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    path = args.root.resolve() / "runs" / report_id / "report.md"
    report, _body = read_frontmatter(path)
    source = report["source"]
    print(f"source: {source['id']} ({source['snapshot_hash']})")
    print(f"recognition_rules_hash: {source['recognition_rules_hash']}")
    if "requested_syscalls" in report:
        print("requested_syscalls: " + ", ".join(report["requested_syscalls"]))
    else:
        print(f"count: {report['count']['value']} ({report['count']['source']})")
    print(f"pending: {report['pending_count']}")
    print("selected: " + (", ".join(report["selected_syscalls"]) or "none"))
    for row in report["syscalls"]:
        rules = ",".join(rule["id"] for rule in row["rules"]) or "none"
        print(
            f"syscall: {row['syscall']} | result={row['result']} | rules={rules} | "
            f"evidence={row['evidence_count']} | unresolved={row['unresolved_evidence_count']}"
        )
    print(f"report_id: {report_id}")
    print(f"report: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
