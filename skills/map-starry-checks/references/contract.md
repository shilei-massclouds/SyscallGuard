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

Pin `base_commit` and `target_hash` on every selected entity. Do not carry pass/fail status from a
different target revision. A missing mapping may be completed as `needs_review` with a concrete
reason and no executable check.
