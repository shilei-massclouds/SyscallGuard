# Compliance Check Contract

Start with static-check and dynamic-test IDs from the mapping report's `execution_scope`, then load their current
two-level details and recompute hashes. Load the finding index before execution. Add every resolvable original
static/dynamic source of an open older-snapshot finding to a revalidation scope. Apply each unique dynamic
`patch_file` from the resulting effective scope once in a detached worktree matching the target snapshot.

Use the report's complete `rule_syscalls` relation to assign every failed rule to syscalls. An explicit check
`applies_to_syscalls` may narrow that ownership but may not introduce a syscall absent from the report.

Before execution, compare each base-scoped rule, static check, and dynamic test `generated_at_utc`, then its content
hash, against the mapping report. Refuse execution on either mismatch. Store the complete machine state in the
trailing `syscallguard_check_report` metadata of `runs/check-*/report.md`: parent mapping report, target snapshot,
input entity versions, base/revalidation/effective scopes, all static/dynamic results, counts, blockers, complete
current open finding IDs/versions, and new/carried/revalidated/needs-revalidation IDs.

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

For an open finding on the current snapshot that the effective scope does not conclusively cover, carry it into
the report unchanged. For an open older-snapshot finding, rerun all resolvable original sources. Any missing source,
`error`, `not_run`, `skipped`, or blocker leaves the old entity open and lists it under `needs_revalidation`. If all
sources are conclusive, another failure creates a current-snapshot finding and marks the old one `superseded` with
`superseded_by`; all pass marks the old one `no_longer_reproduces`.
