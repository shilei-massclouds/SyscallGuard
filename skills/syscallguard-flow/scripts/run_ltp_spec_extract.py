#!/usr/bin/env python3
"""Run the external LTP syscall spec extractor for one SyscallGuard batch.

This adapter is intentionally read-only with respect to the LTP tree. It imports
the extractor implementation from the external LTP checkout and writes all run
artifacts into the SyscallGuard batch directory.
"""

from __future__ import annotations

import argparse
import importlib.util
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from types import ModuleType
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - environment failure path
    yaml = None


DEFAULT_LTP_REPO = Path.home() / "gitStudy" / "ltp"
DEFAULT_TOOL_REL = Path("tools/syscall_spec_extract.py")
RUN_KEY = "ltp_spec_extract"


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
        raise SystemExit("ERROR: manifest scope.included_syscalls must be a list of strings")
    return [item.lower() for item in raw]


def import_external_tool(tool_path: Path) -> ModuleType:
    if not tool_path.exists():
        raise SystemExit(f"ERROR: external extractor not found: {tool_path}")
    spec = importlib.util.spec_from_file_location("ltp_syscall_spec_extract", tool_path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"ERROR: cannot import external extractor: {tool_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


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


def existing_ltp_dirs(syscall: str, module: ModuleType, ltp_repo: Path) -> list[str]:
    syscalls_root = ltp_repo / "testcases" / "kernel" / "syscalls"
    aliases = getattr(module, "ALIASES", {})
    candidates: list[str] = [syscall]
    if isinstance(aliases, dict):
        candidates.extend(str(item) for item in aliases.get(syscall, []))

    result: list[str] = []
    seen: set[str] = set()
    for candidate in candidates:
        if candidate in seen:
            continue
        seen.add(candidate)
        if (syscalls_root / candidate).is_dir():
            result.append(candidate)
    return result


def build_entries(
    syscalls: list[str], module: ModuleType, ltp_repo: Path
) -> tuple[list[Any], list[dict[str, Any]]]:
    entries: list[Any] = []
    manifest_rows: list[dict[str, Any]] = []
    entry_type = getattr(module, "ManifestEntry")

    for syscall in syscalls:
        ltp_dirs = existing_ltp_dirs(syscall, module, ltp_repo)
        entries.append(entry_type(name=syscall, group="syscallguard_batch", ltp_dirs=ltp_dirs))
        manifest_rows.append(
            {
                "name": syscall,
                "group": "syscallguard_batch",
                "ltp_dirs": ltp_dirs,
                "status": "ready" if ltp_dirs else "missing_ltp_dir",
            }
        )
    return entries, manifest_rows


def write_extractor_manifest(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("w", encoding="utf-8") as handle:
            handle.write("# Generated by SyscallGuard run_ltp_spec_extract.py.\n")
            handle.write("syscalls:\n")
            for row in rows:
                dirs = ", ".join(row["ltp_dirs"])
                handle.write(
                    f"  - {{name: {row['name']}, group: {row['group']}, ltp_dirs: [{dirs}]}}\n"
                )
    except OSError as exc:
        raise SystemExit(f"ERROR: cannot write {path}: {exc}") from exc


def rel_to_batch(batch_dir: Path, path: Path) -> str:
    try:
        return str(path.relative_to(batch_dir))
    except ValueError:
        return str(path)


def output_paths(batch_dir: Path) -> dict[str, Path]:
    out = batch_dir / "outputs"
    return {
        "extractor_manifest": out / "ltp-spec-extract-manifest.yaml",
        "raw_candidates": out / "ltp-spec-raw-candidates.yaml",
        "raw_summary": out / "ltp-spec-extract-summary.md",
        "normalized_specs": out / "ltp-spec-normalized.yaml",
        "normalized_summary": out / "ltp-spec-normalized-summary.md",
        "run_metadata": out / "ltp-spec-extract-run.yaml",
    }


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

    ltp_repo = args.ltp_repo.expanduser().resolve()
    tool_path = args.tool.expanduser()
    if not tool_path.is_absolute():
        tool_path = ltp_repo / tool_path
    tool_path = tool_path.resolve()

    manifest = load_batch_manifest(batch_dir)
    batch_id = manifest.get("batch_id")
    if not isinstance(batch_id, str) or not batch_id:
        raise SystemExit("ERROR: manifest batch_id must be a non-empty string")

    module = import_external_tool(tool_path)
    syscalls = included_syscalls(manifest)
    entries, manifest_rows = build_entries(syscalls, module, ltp_repo)
    paths = output_paths(batch_dir)

    write_extractor_manifest(paths["extractor_manifest"], manifest_rows)
    candidates, summaries = module.build_candidates(entries)
    normalized_specs = module.normalize_specs(candidates)
    module.write_candidates(paths["raw_candidates"], candidates)
    module.write_summary(paths["raw_summary"], candidates, summaries)
    module.write_normalized_specs(paths["normalized_specs"], normalized_specs)
    module.write_normalized_summary(paths["normalized_summary"], normalized_specs)

    missing_dirs = [row["name"] for row in manifest_rows if not row["ltp_dirs"]]
    output_refs = {
        name: rel_to_batch(batch_dir, path) for name, path in paths.items() if name != "run_metadata"
    }
    generated_at = utc_now()
    run_metadata = {
        "ref_kind": "external_tool_run",
        "tool": "tools/syscall_spec_extract.py",
        "tool_path": str(tool_path),
        "repository_path": str(ltp_repo),
        "repository_commit": git_output(ltp_repo, ["rev-parse", "HEAD"]),
        "repository_dirty": bool(git_output(ltp_repo, ["status", "--short"])),
        "generated_at_utc": generated_at,
        "batch_id": batch_id,
        "syscalls_requested": syscalls,
        "syscalls_without_ltp_dir": missing_dirs,
        "outputs": output_refs,
        "counts": {
            "syscalls": len(syscalls),
            "raw_candidates": len(candidates),
            "normalized_specs": len(normalized_specs),
        },
        "review_policy": "candidate_input_only_not_closeout_evidence_until_step_review",
    }
    metadata_file = {
        "schema_version": 1,
        "kind": "syscallguard_ltp_spec_extract_run",
        **run_metadata,
    }
    write_yaml(paths["run_metadata"], metadata_file)
    if not args.no_source_index_update:
        update_source_index(batch_dir, run_metadata)

    print(f"batch: {batch_dir}")
    print(f"ltp_repo: {ltp_repo}")
    print(f"raw_candidates: {len(candidates)}")
    print(f"normalized_specs: {len(normalized_specs)}")
    print(f"missing_ltp_dirs: {len(missing_dirs)}")
    for name, path in paths.items():
        print(f"{name}: {path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run LTP syscall spec extraction for one SyscallGuard batch."
    )
    parser.add_argument("batch", type=Path, help="Path to batches/<batch-id>")
    parser.add_argument("--ltp-repo", type=Path, default=DEFAULT_LTP_REPO)
    parser.add_argument("--tool", type=Path, default=DEFAULT_TOOL_REL)
    parser.add_argument(
        "--no-source-index-update",
        action="store_true",
        help="Write outputs only; do not register the tool run in inputs/source-index.yaml.",
    )
    return parser


def main(argv: list[str]) -> int:
    return run(build_parser().parse_args(argv))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
