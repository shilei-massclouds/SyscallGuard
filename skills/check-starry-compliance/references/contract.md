# Compliance Check Contract

Read entity IDs from the mapping run, but load current shared mappings and check definitions and
recompute their hashes. Apply each unique dynamic `patch_file` once in a detached worktree at the
recorded `base_commit`.

Use `rule_syscalls` from the mapping manifest to assign every failed rule to syscalls. An explicit
check `applies_to_syscalls` may narrow that ownership but may not introduce a syscall absent from
the mapping input.

Before execution, compare each mapping, static-check, and dynamic-test `generated_at_utc`, then its
content hash, against the mapping run. Refuse execution on either mismatch. Give `results.yaml` a
generation time and direct mapping/check/test dependencies. Give every finding a generation time
and direct check-result dependency.

Static results are `pass`, `fail`, or `error`. Dynamic results are `pass`, `fail`, `skipped`, or
`not_run`. A nonzero dynamic command is an implementation failure only when it produced reliable
test evidence. Match known environment errors and each test's `blocker_patterns` as blockers.

Store confirmed gaps at `targets/starry/findings/<id>.yaml`, keyed by syscall, rule ID, and target
revision. Store blockers only in `runs/<run-id>/manifest.yaml` and `results.yaml`; never convert a
blocker into a finding.
