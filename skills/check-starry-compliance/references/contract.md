# Compliance Check Contract

Read entity IDs from the mapping run, but load current shared mappings and check definitions and
recompute their hashes. Apply each unique dynamic `patch_file` once in a detached worktree at the
recorded `base_commit`.

Static results are `pass`, `fail`, or `error`. Dynamic results are `pass`, `fail`, `skipped`, or
`not_run`. A nonzero dynamic command is an implementation failure only when it produced reliable
test evidence. Match known environment errors and each test's `blocker_patterns` as blockers.

Store confirmed gaps at `targets/starry/findings/<id>.yaml`, keyed by syscall, rule ID, and target
revision. Store blockers only in `runs/<run-id>/manifest.yaml` and `results.yaml`; never convert a
blocker into a finding.
