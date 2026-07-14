from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import yaml


SCHEMA_VERSION = 1
RUN_STATUSES = {
    "running",
    "completed",
    "completed_with_blockers",
    "failed",
    "superseded",
}
READABLE_UPSTREAM_STATUSES = {"completed", "completed_with_blockers"}
STAGES = {"spec", "mapping", "check", "fix"}
STAGE_PREFIX = {
    "spec": "spec",
    "mapping": "mapping",
    "check": "check",
    "fix": "fix",
}


class SyscallGuardError(RuntimeError):
    pass


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def load_yaml(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return yaml.safe_load(handle)
    except FileNotFoundError as exc:
        raise SyscallGuardError(f"missing YAML file: {path}") from exc
    except yaml.YAMLError as exc:
        raise SyscallGuardError(f"malformed YAML in {path}: {exc}") from exc
    except OSError as exc:
        raise SyscallGuardError(f"cannot read {path}: {exc}") from exc


def load_mapping(path: Path) -> dict[str, Any]:
    value = load_yaml(path)
    if not isinstance(value, dict):
        raise SyscallGuardError(f"expected a YAML mapping in {path}")
    return value


def _yaml_text(value: Any) -> str:
    return yaml.safe_dump(
        value,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=100,
    )


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temp_path = Path(temp_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_path, path)
    except BaseException:
        temp_path.unlink(missing_ok=True)
        raise


def atomic_write_yaml(path: Path, value: Any) -> None:
    atomic_write_text(path, _yaml_text(value))


def read_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    """Read a Markdown document with a required YAML frontmatter mapping."""
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise SyscallGuardError(f"missing Markdown file: {path}") from exc
    except OSError as exc:
        raise SyscallGuardError(f"cannot read {path}: {exc}") from exc
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        raise SyscallGuardError(f"Markdown file has no YAML frontmatter: {path}")
    closing = next(
        (index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---"),
        None,
    )
    if closing is None:
        raise SyscallGuardError(f"Markdown frontmatter is not closed: {path}")
    try:
        value = yaml.safe_load("".join(lines[1:closing]))
    except yaml.YAMLError as exc:
        raise SyscallGuardError(f"malformed YAML frontmatter in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise SyscallGuardError(f"expected YAML frontmatter mapping in {path}")
    return value, "".join(lines[closing + 1 :])


def canonical_json(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def content_hash(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_json(value)).hexdigest()


def version_content_hash(entity: dict[str, Any]) -> str:
    """Hash versioned content without its clock value.

    Rule provenance is deliberately outside the semantic version.  For every
    other entity, a manual edit is detected even when its author forgot to
    advance ``generated_at_utc``.
    """
    if entity.get("kind") == "syscallguard_rule":
        return content_hash(
            {
                "category": entity.get("category"),
                "semantics": entity.get("semantics"),
            }
        )
    payload = dict(entity)
    payload.pop("generated_at_utc", None)
    payload.pop("content_hash", None)
    return content_hash(payload)


def entity_version(entity_id: str, entity: dict[str, Any]) -> dict[str, str]:
    generated = entity.get("generated_at_utc")
    if not isinstance(generated, str) or not generated:
        raise SyscallGuardError(f"versioned entity {entity_id} has no generated_at_utc")
    return {
        "id": entity_id,
        "generated_at_utc": generated,
        "content_hash": version_content_hash(entity),
    }


def dependency_mismatch(
    recorded: dict[str, Any], current_id: str, current: dict[str, Any]
) -> str | None:
    """Compare timestamps first, then hashes as a safety check."""
    if recorded.get("id") != current_id:
        return f"dependency id changed: {recorded.get('id')!r} != {current_id!r}"
    generated = current.get("generated_at_utc")
    if recorded.get("generated_at_utc") != generated:
        return (
            f"dependency {current_id} generation changed: "
            f"{recorded.get('generated_at_utc')!r} != {generated!r}"
        )
    actual_hash = version_content_hash(current)
    if recorded.get("content_hash") != actual_hash:
        return f"dependency {current_id} content changed without a generation update"
    return None


def dependencies_by_id(value: Any, owner: str) -> dict[str, dict[str, Any]]:
    if not isinstance(value, list):
        raise SyscallGuardError(f"{owner} upstream_dependencies must be a list")
    result: dict[str, dict[str, Any]] = {}
    for row in value:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str):
            raise SyscallGuardError(f"{owner} has an invalid upstream dependency")
        result[row["id"]] = row
    return result


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    try:
        with path.open("rb") as handle:
            for block in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(block)
    except OSError as exc:
        raise SyscallGuardError(f"cannot hash {path}: {exc}") from exc
    return "sha256:" + digest.hexdigest()


def tree_hash(paths: Iterable[Path], root: Path | None = None) -> str:
    digest = hashlib.sha256()
    files: list[Path] = []
    for item in paths:
        if item.is_file():
            files.append(item)
        elif item.is_dir():
            files.extend(candidate for candidate in item.rglob("*") if candidate.is_file())
    for path in sorted(set(files), key=lambda item: str(item)):
        name = str(path.relative_to(root)) if root and path.is_relative_to(root) else str(path)
        digest.update(name.encode("utf-8"))
        digest.update(b"\0")
        with path.open("rb") as handle:
            for block in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(block)
        digest.update(b"\0")
    return "sha256:" + digest.hexdigest()


def slug(value: str) -> str:
    result = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not result:
        raise SyscallGuardError(f"cannot create an entity id from {value!r}")
    return result


def normalize_run_id(value: str) -> str:
    if not re.fullmatch(r"[a-z0-9][a-z0-9._-]{2,127}", value):
        raise SyscallGuardError(f"invalid run id: {value!r}")
    return value


def new_run_id(stage: str, seed: Any | None = None) -> str:
    if stage not in STAGES:
        raise SyscallGuardError(f"unknown stage: {stage}")
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dt%H%M%S%z").replace("+0000", "z")
    suffix = hashlib.sha256(
        canonical_json({"seed": seed if seed is not None else utc_now(), "nonce": time.time_ns()})
    ).hexdigest()[:8]
    return f"{STAGE_PREFIX[stage]}-{timestamp}-{suffix}"


def run_dir(root: Path, run_id: str) -> Path:
    return root / "runs" / normalize_run_id(run_id)


def read_run(root: Path, run_id: str, expected_stage: str | None = None) -> dict[str, Any]:
    manifest_path = run_dir(root, run_id) / "manifest.yaml"
    manifest = load_mapping(manifest_path)
    if manifest.get("kind") != "syscallguard_run":
        raise SyscallGuardError(f"not a SyscallGuard run: {manifest_path}")
    if manifest.get("run_id") != run_id:
        raise SyscallGuardError(f"run id mismatch in {manifest_path}")
    if expected_stage and manifest.get("stage") != expected_stage:
        raise SyscallGuardError(
            f"run {run_id} has stage {manifest.get('stage')!r}; expected {expected_stage!r}"
        )
    if manifest.get("status") not in READABLE_UPSTREAM_STATUSES:
        raise SyscallGuardError(
            f"run {run_id} is not readable downstream: status={manifest.get('status')!r}"
        )
    return manifest


class RunRecorder:
    def __init__(
        self,
        root: Path,
        stage: str,
        run_id: str,
        invocation: dict[str, Any],
        from_run_id: str | None = None,
    ) -> None:
        self.root = root
        self.stage = stage
        self.run_id = normalize_run_id(run_id)
        self.directory = run_dir(root, run_id)
        if self.directory.exists():
            raise SyscallGuardError(f"run already exists: {self.directory}")
        self.directory.mkdir(parents=True)
        self.manifest: dict[str, Any] = {
            "schema_version": SCHEMA_VERSION,
            "kind": "syscallguard_run",
            "run_id": self.run_id,
            "stage": stage,
            "status": "running",
            "created_at_utc": utc_now(),
            "completed_at_utc": None,
            "invocation": invocation,
            "entities": {},
            "entity_hashes": {},
            "outputs": {},
            "counts": {},
            "blockers": [],
            "error": None,
        }
        if stage == "mapping":
            self.manifest["from_report_id"] = from_run_id
        else:
            self.manifest["from_run_id"] = from_run_id
        self.changeset: dict[str, Any] = {
            "schema_version": SCHEMA_VERSION,
            "kind": "syscallguard_changeset",
            "run_id": self.run_id,
            "stage": stage,
            "changes": [],
            "conflicts": [],
        }
        self.flush()

    def flush(self) -> None:
        atomic_write_yaml(self.directory / "manifest.yaml", self.manifest)
        atomic_write_yaml(self.directory / "changeset.yaml", self.changeset)

    def complete(self, blockers: list[dict[str, Any]] | None = None) -> None:
        blockers = blockers or []
        self.manifest["blockers"] = blockers
        self.manifest["status"] = "completed_with_blockers" if blockers else "completed"
        self.manifest["completed_at_utc"] = utc_now()
        self.flush()

    def fail(self, exc: BaseException) -> None:
        self.manifest["status"] = "failed"
        self.manifest["completed_at_utc"] = utc_now()
        self.manifest["error"] = f"{type(exc).__name__}: {exc}"
        self.flush()


def default_index(kind: str) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "kind": kind,
        "updated_at_utc": None,
        "entities": [],
    }


def load_index(path: Path, kind: str) -> dict[str, Any]:
    if not path.exists():
        return default_index(kind)
    index = load_mapping(path)
    if index.get("kind") != kind:
        raise SyscallGuardError(f"unexpected index kind in {path}: {index.get('kind')!r}")
    if not isinstance(index.get("entities"), list):
        raise SyscallGuardError(f"index entities must be a list in {path}")
    return index


def update_index(
    path: Path,
    kind: str,
    entries: Iterable[dict[str, Any]],
    id_key: str = "id",
) -> None:
    index = load_index(path, kind)
    by_id: dict[str, dict[str, Any]] = {}
    for item in index["entities"]:
        if isinstance(item, dict) and isinstance(item.get(id_key), str):
            by_id[item[id_key]] = item
    for item in entries:
        entity_id = item.get(id_key)
        if not isinstance(entity_id, str) or not entity_id:
            raise SyscallGuardError(f"index entry is missing {id_key}: {item!r}")
        by_id[entity_id] = item
    index["entities"] = [by_id[key] for key in sorted(by_id)]
    index["updated_at_utc"] = utc_now()
    atomic_write_yaml(path, index)


def entity_hash(path: Path) -> str:
    return content_hash(load_yaml(path))


def git(repo: Path, args: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    try:
        result = subprocess.run(
            ["git", "-C", str(repo), *args],
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError as exc:
        raise SyscallGuardError(f"cannot execute git for {repo}: {exc}") from exc
    if check and result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip()
        raise SyscallGuardError(f"git {' '.join(args)} failed in {repo}: {detail}")
    return result


def git_output(repo: Path, args: list[str]) -> str:
    return git(repo, args).stdout.strip()


def resolve_revision(repo: Path, revision: str) -> str:
    if not repo.is_dir():
        raise SyscallGuardError(f"repository does not exist: {repo}")
    return git_output(repo, ["rev-parse", f"{revision}^{{commit}}"])


def ensure_target_descriptor(path: Path) -> tuple[dict[str, Any], Path, str]:
    descriptor = load_mapping(path)
    if descriptor.get("target_id") != "starry":
        raise SyscallGuardError(f"target descriptor must set target_id: starry: {path}")
    raw_repo = descriptor.get("repository")
    if not isinstance(raw_repo, str) or not raw_repo:
        raise SyscallGuardError(f"target descriptor repository must be a path: {path}")
    repository = Path(raw_repo).expanduser().resolve()
    revision = descriptor.get("revision", "HEAD")
    if not isinstance(revision, str) or not revision:
        raise SyscallGuardError(f"target descriptor revision must be a string: {path}")
    commit = resolve_revision(repository, revision)
    return descriptor, repository, commit


def safe_relative_path(value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise SyscallGuardError(f"target path must be relative and cannot contain '..': {value!r}")
    return path


def resolve_artifact(root: Path, run: dict[str, Any], value: str) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    run_path = run_dir(root, str(run["run_id"])) / path
    if run_path.exists():
        return run_path
    return root / path


def publish_yaml_entities(
    staged: Iterable[tuple[Path, Path, Any]],
) -> None:
    rendered: list[tuple[Path, str]] = []
    for _source, destination, value in staged:
        rendered.append((destination, _yaml_text(value)))
    for destination, text in rendered:
        atomic_write_text(destination, text)
