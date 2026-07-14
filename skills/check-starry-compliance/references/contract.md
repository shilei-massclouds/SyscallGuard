# Compliance Check Contract

Read static-check and dynamic-test IDs only from the mapping report's `execution_scope`, then load their
current two-level details and recompute hashes. Apply each unique dynamic `patch_file` once in a detached
worktree matching the report's target content `snapshot_hash`.

Use the report's complete `rule_syscalls` relation to assign every failed rule to syscalls. An explicit check
`applies_to_syscalls` may narrow that ownership but may not introduce a syscall absent from the report.

Before execution, compare each scoped rule, static check, and dynamic test `generated_at_utc`, then its content
hash, against the mapping report. Refuse execution on either mismatch. Store the complete machine state in the
trailing `syscallguard_check_report` metadata of `runs/check-*/report.md`: parent mapping report, target snapshot,
input entity versions and scope, all static/dynamic results, counts, blockers, and finding IDs/versions.

Static results are `pass`, `fail`, or `error`. Dynamic results are `pass`, `fail`, `skipped`, or `not_run`.
A nonzero dynamic command is an implementation failure only when it produced reliable test evidence. Match
known environment errors and each test's `blocker_patterns` as blockers.

Reliable dynamic failures retain the exit code and at most the final 8 KiB of output. Static results retain every
pattern's match state and location. Finding occurrences embed this stable evidence and never point at temporary
logs. Store confirmed gaps at `targets/starry/findings/<id>.yaml`, keyed by syscall, rule ID, and target content
snapshot. Never convert a blocker into a finding.

Publish finding details, the finding index, and the report in one rollback-capable transaction, with the report
last. A blocker produces `completed_with_blockers` and retains `/tmp/syscallguard-check/<id>` plus its worktree.
Unexpected execution or publication failure produces no formal report or finding update and retains that
temporary diagnostic site. A blocker-free completion removes all temporary logs and its isolated worktree.
