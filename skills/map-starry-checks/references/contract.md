# Starry Mapping Contract

Use a target descriptor with these fields:

```yaml
target_id: starry
repository: /path/to/tgoskits
revision: HEAD
worktree_root: /tmp/syscallguard-worktrees
```

Mapping entities live in `targets/starry/mappings/`. Static checks live in
`targets/starry/static-checks/` and contain `check_id`, `rule_refs`, `path`, and regex `patterns`.
Dynamic tests live in `targets/starry/dynamic-tests/` and contain `test_id`, `rule_refs`, test source
metadata, `patch_file`, a list or shell-style `command`, target architecture, timeout, and optional
environment-blocker patterns. Each directory has an `index.yaml`.

Pin `base_commit`, `target_hash`, `generated_at_utc`, and direct rule `upstream_dependencies` on every
selected entity. Read rule versions and syscall ownership from ingest report frontmatter. Reject a
report when a newer report exists for any included source/syscall. Compare dependency time before
hash and reject stale reports. Record `from_report_id` and `rule_syscalls`; do not read a syscall
spec or rule index. Do not carry pass/fail status from a different target revision. Complete a
missing mapping as `needs_review` only
with a concrete reason and no invented executable check. Never write mapping references back to a
general rule.
