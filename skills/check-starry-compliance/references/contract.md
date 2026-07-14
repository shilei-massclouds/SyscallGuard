# Compliance Check Contract

Read static-check and dynamic-test IDs only from the mapping report's `execution_scope`, then load their
current two-level details and recompute hashes. Apply each unique dynamic `patch_file` once in a detached
worktree matching the report's target content `snapshot_hash`.

Use the report's complete `rule_syscalls` relation to assign every failed rule to syscalls. An explicit check
`applies_to_syscalls` may narrow that ownership but may not introduce a syscall absent from the report.

Before execution, compare each scoped rule, static check, and dynamic test `generated_at_utc`, then its content
hash, against the mapping report. Refuse execution on either mismatch. Give `results.yaml` a generation time
and direct check/test dependencies. Give every finding a generation time and direct check-result dependency.

Static results are `pass`, `fail`, or `error`. Dynamic results are `pass`, `fail`, `skipped`, or `not_run`.
A nonzero dynamic command is an implementation failure only when it produced reliable test evidence. Match
known environment errors and each test's `blocker_patterns` as blockers.

Store confirmed gaps at `targets/starry/findings/<id>.yaml`, keyed by syscall, rule ID, and target content
snapshot. Store blockers only in the check manifest and `results.yaml`; never convert a blocker into a finding.
