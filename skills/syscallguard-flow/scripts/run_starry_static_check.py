#!/usr/bin/env python3
"""Run parameterized Starry static pattern checks for a SyscallGuard batch."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - environment failure path
    yaml = None


DEFAULT_RULES = Path("skills/syscallguard-flow/references/starry-static-rules.yaml")
RUN_KEY = "starry_static_check"
STARRY_MARKERS = [
    Path("os/StarryOS/kernel/src/syscall/mod.rs"),
    Path("os/StarryOS/kernel/src/syscall/fs/ctl.rs"),
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_yaml(path: Path) -> Any:
    if yaml is None:
        raise SystemExit("ERROR: PyYAML is required: python3 -m pip install PyYAML")
    try:
        with path.open("r", encoding="utf-8") as handle:
            return yaml.safe_load(handle)
    except yaml.YAMLError as exc:
        raise SystemExit(f"ERROR: malformed YAML in {path}: {exc}") from exc
    except OSError as exc:
        raise SystemExit(f"ERROR: cannot read {path}: {exc}") from exc


def write_yaml(path: Path, data: dict[str, Any]) -> None:
    if yaml is None:
        raise SystemExit("ERROR: PyYAML is required: python3 -m pip install PyYAML")
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("w", encoding="utf-8") as handle:
            yaml.safe_dump(data, handle, allow_unicode=True, sort_keys=False)
    except OSError as exc:
        raise SystemExit(f"ERROR: cannot write {path}: {exc}") from exc


def git_output(repo: Path, args: list[str]) -> str:
    try:
        proc = subprocess.run(
            ["git", "-C", str(repo), *args],
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return ""
    if proc.returncode != 0:
        return ""
    return proc.stdout.strip()


def load_batch_manifest(batch_dir: Path) -> dict[str, Any]:
    manifest = load_yaml(batch_dir / "manifest.yaml")
    if not isinstance(manifest, dict):
        raise SystemExit(f"ERROR: {batch_dir / 'manifest.yaml'} must contain a YAML mapping")
    return manifest


def included_syscalls(manifest: dict[str, Any]) -> list[str]:
    scope = manifest.get("scope")
    if not isinstance(scope, dict):
        raise SystemExit("ERROR: manifest scope must be a mapping")
    raw = scope.get("included_syscalls")
    if not isinstance(raw, list) or not all(isinstance(item, str) for item in raw):
        return []
    return [item.lower() for item in raw]


def infer_starry_repo(source_index: dict[str, Any]) -> Path | None:
    inputs = source_index.get("inputs")
    if not isinstance(inputs, dict):
        return None
    for value in inputs.values():
        if not isinstance(value, dict):
            continue
        raw_path = value.get("external_path")
        if not isinstance(raw_path, str):
            continue
        path = Path(raw_path)
        for marker in STARRY_MARKERS:
            marker_parts = marker.parts
            path_parts = path.parts
            if len(path_parts) >= len(marker_parts) and path_parts[-len(marker_parts) :] == marker_parts:
                return Path(*path_parts[: -len(marker_parts)])
    return None


def resolve_starry_repo(batch_dir: Path, requested: Path | None) -> Path:
    if requested is not None:
        repo = requested.expanduser().resolve()
        if not repo.is_dir():
            raise SystemExit(f"ERROR: Starry repo not found: {repo}")
        return repo

    source_index_path = batch_dir / "inputs" / "source-index.yaml"
    if source_index_path.exists():
        source_index = load_yaml(source_index_path)
        if isinstance(source_index, dict):
            inferred = infer_starry_repo(source_index)
            if inferred is not None and inferred.is_dir():
                return inferred.resolve()
    raise SystemExit("ERROR: cannot infer Starry repo; pass --starry-repo")


def load_rules(path: Path) -> list[dict[str, Any]]:
    data = load_yaml(path)
    if not isinstance(data, dict):
        raise SystemExit(f"ERROR: {path} must contain a YAML mapping")
    rules = data.get("rules")
    if not isinstance(rules, list):
        raise SystemExit(f"ERROR: {path} rules must be a list")
    result: list[dict[str, Any]] = []
    for index, rule in enumerate(rules):
        if not isinstance(rule, dict):
            raise SystemExit(f"ERROR: rule[{index}] must be a mapping")
        result.append(rule)
    return result


def selected_rules(rules: list[dict[str, Any]], syscalls: list[str], batch_id: str) -> list[dict[str, Any]]:
    syscall_set = set(syscalls)
    selected: list[dict[str, Any]] = []
    for rule in rules:
        rule_batch = rule.get("batch_id")
        if isinstance(rule_batch, str) and rule_batch != batch_id:
            continue
        applies = rule.get("applies_to_syscalls")
        if isinstance(applies, list) and applies:
            applies_set = {item.lower() for item in applies if isinstance(item, str)}
            if syscall_set and not syscall_set.intersection(applies_set):
                continue
        selected.append(rule)
    return selected


def line_for(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def check_rule(repo: Path, rule: dict[str, Any]) -> dict[str, Any]:
    rule_id = str(rule.get("id", ""))
    relpath = rule.get("path")
    if not rule_id:
        raise SystemExit("ERROR: every static rule needs an id")
    if not isinstance(relpath, str) or not relpath:
        raise SystemExit(f"ERROR: {rule_id} path must be a non-empty string")

    path = repo / relpath
    patterns = rule.get("patterns")
    if not isinstance(patterns, list) or not patterns:
        raise SystemExit(f"ERROR: {rule_id} patterns must be a non-empty list")

    pattern_results: list[dict[str, Any]] = []
    if not path.exists():
        return {
            "id": rule_id,
            "title": rule.get("title", ""),
            "rule_refs": rule.get("rule_refs", []),
            "applies_to_syscalls": rule.get("applies_to_syscalls", []),
            "path": relpath,
            "status": rule.get("missing_file_status", "needs_review"),
            "error": f"missing file: {path}",
            "patterns": pattern_results,
        }

    text = path.read_text(encoding="utf-8", errors="replace")
    matched_all = True
    invalid_regex = False
    for raw_pattern in patterns:
        if not isinstance(raw_pattern, dict):
            raise SystemExit(f"ERROR: {rule_id} pattern entries must be mappings")
        label = str(raw_pattern.get("label", ""))
        regex = raw_pattern.get("regex")
        if not isinstance(regex, str) or not regex:
            raise SystemExit(f"ERROR: {rule_id} pattern {label!r} regex must be non-empty")
        try:
            match = re.search(regex, text, re.MULTILINE | re.DOTALL)
        except re.error as exc:
            invalid_regex = True
            matched_all = False
            pattern_results.append(
                {
                    "label": label,
                    "regex": regex,
                    "matched": False,
                    "line": None,
                    "error": f"invalid regex: {exc}",
                }
            )
            continue
        if match:
            pattern_results.append(
                {
                    "label": label,
                    "regex": regex,
                    "matched": True,
                    "line": line_for(text, match.start()),
                }
            )
        else:
            matched_all = False
            pattern_results.append(
                {"label": label, "regex": regex, "matched": False, "line": None}
            )

    if invalid_regex:
        status = "needs_review"
    elif matched_all:
        status = rule.get("pass_status", "static_audit_supports")
    else:
        status = rule.get("fail_status", "missing_pattern")

    return {
        "id": rule_id,
        "title": rule.get("title", ""),
        "rule_refs": rule.get("rule_refs", []),
        "applies_to_syscalls": rule.get("applies_to_syscalls", []),
        "path": relpath,
        "status": status,
        "patterns": pattern_results,
    }


def write_markdown(path: Path, payload: dict[str, Any]) -> None:
    lines = [
        "# Starry Static Check Summary",
        "",
        f"Batch: `{payload['batch_id']}`",
        f"Generated: `{payload['generated_at_utc']}`",
        f"Starry repo: `{payload['starry_repo']}`",
        f"Starry commit: `{payload['starry_commit']}`",
        "",
        "These results are static audit inputs only. They do not mark behavior as covered.",
        "",
        "| Status | Rule | Source | Evidence |",
        "| --- | --- | --- | --- |",
    ]
    for result in payload["results"]:
        evidence: list[str] = []
        if result.get("error"):
            evidence.append(str(result["error"]))
        for pattern in result.get("patterns", []):
            label = pattern.get("label", "")
            if pattern.get("matched"):
                evidence.append(f"{label}: line {pattern.get('line')}")
            else:
                evidence.append(f"missing {label}")
        lines.append(
            f"| `{result['status']}` | `{result['id']}` | `{result['path']}` | "
            f"{'<br>'.join(evidence)} |"
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def output_paths(batch_dir: Path) -> dict[str, Path]:
    out = batch_dir / "outputs"
    return {
        "structured_results": out / "starry-static-check-results.yaml",
        "summary": out / "starry-static-check-summary.md",
    }


def rel_to_batch(batch_dir: Path, path: Path) -> str:
    try:
        return str(path.relative_to(batch_dir))
    except ValueError:
        return str(path)


def update_source_index(batch_dir: Path, run_metadata: dict[str, Any]) -> None:
    source_index_path = batch_dir / "inputs" / "source-index.yaml"
    data = load_yaml(source_index_path) if source_index_path.exists() else {}
    if data is None:
        data = {}
    if not isinstance(data, dict):
        raise SystemExit(f"ERROR: {source_index_path} must contain a YAML mapping")
    tool_runs = data.setdefault("tool_runs", {})
    if not isinstance(tool_runs, dict):
        raise SystemExit(f"ERROR: {source_index_path} tool_runs must be a mapping")
    tool_runs[RUN_KEY] = run_metadata
    write_yaml(source_index_path, data)


def run(args: argparse.Namespace) -> int:
    batch_dir = args.batch.resolve()
    if not batch_dir.is_dir():
        raise SystemExit(f"ERROR: batch directory not found: {batch_dir}")
    rules_path = args.rules.resolve()
    if not rules_path.exists():
        raise SystemExit(f"ERROR: rules file not found: {rules_path}")

    manifest = load_batch_manifest(batch_dir)
    batch_id = manifest.get("batch_id")
    if not isinstance(batch_id, str) or not batch_id:
        raise SystemExit("ERROR: manifest batch_id must be a non-empty string")
    syscalls = included_syscalls(manifest)
    repo = resolve_starry_repo(batch_dir, args.starry_repo)
    rules = selected_rules(load_rules(rules_path), syscalls, batch_id)
    results = [check_rule(repo, rule) for rule in rules]

    summary: dict[str, int] = {}
    for result in results:
        status = str(result["status"])
        summary[status] = summary.get(status, 0) + 1

    paths = output_paths(batch_dir)
    output_refs = {name: rel_to_batch(batch_dir, path) for name, path in paths.items()}
    generated_at = utc_now()
    run_metadata = {
        "ref_kind": "local_tool_run",
        "tool": "skills/syscallguard-flow/scripts/run_starry_static_check.py",
        "rules": str(rules_path),
        "starry_repo": str(repo),
        "starry_commit": git_output(repo, ["rev-parse", "HEAD"]),
        "starry_dirty": bool(git_output(repo, ["status", "--short"])),
        "generated_at_utc": generated_at,
        "batch_id": batch_id,
        "rules_evaluated": len(results),
        "summary": summary,
        "outputs": output_refs,
        "review_policy": "static_audit_input_only_not_coverage_closeout",
    }
    payload = {
        "schema_version": 1,
        "kind": "syscallguard_starry_static_check_results",
        **run_metadata,
        "results": results,
    }
    write_yaml(paths["structured_results"], payload)
    write_markdown(paths["summary"], payload)
    if not args.no_source_index_update:
        update_source_index(batch_dir, run_metadata)

    print(f"batch: {batch_dir}")
    print(f"starry_repo: {repo}")
    print(f"rules_evaluated: {len(results)}")
    for status, count in sorted(summary.items()):
        print(f"{status}: {count}")
    for name, path in paths.items():
        print(f"{name}: {path}")

    has_missing = any(result["status"] == "missing_pattern" for result in results)
    has_review = any(result["status"] == "needs_review" for result in results)
    if args.fail_on_missing and (has_missing or has_review):
        return 1
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run parameterized static Starry checks for one SyscallGuard batch."
    )
    parser.add_argument("batch", type=Path, help="Path to batches/<batch-id>")
    parser.add_argument("--rules", type=Path, default=DEFAULT_RULES)
    parser.add_argument("--starry-repo", type=Path)
    parser.add_argument(
        "--no-source-index-update",
        action="store_true",
        help="Write outputs only; do not register the tool run in inputs/source-index.yaml.",
    )
    parser.add_argument(
        "--fail-on-missing",
        action="store_true",
        help="Return non-zero when any rule has missing patterns or needs review.",
    )
    return parser


def main(argv: list[str]) -> int:
    return run(build_parser().parse_args(argv))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
