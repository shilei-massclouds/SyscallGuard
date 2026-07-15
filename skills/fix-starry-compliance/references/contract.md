# Starry Fix Contract

With no user arguments, scan the shared finding index and select every entity with `status: confirmed`,
`resolution: open`, and a target snapshot equal to the current Starry content snapshot. The English
`$fix-starry-compliance` name is an alias for `$修复缺口`; `from=` is not accepted. Do not create patches for
any check-report blocker.

Before prepare, derive the single branch recorded by the selected findings' source reports and ask the user to
confirm it. The branch must already be checked out and clean; the tool never creates or switches it.

Prepare writes `/tmp/syscallguard-fix/<run-id>/preparation.yaml`, pins all selected finding versions, and collects
all evidence-bearing check reports from their occurrences. Merge the complete regression scope of every source
report by entity ID. Finalize revalidates the pinned findings, source reports, entities, branch, and snapshot,
reapplies every unique test patch once, applies the combined `implementation-fix.patch`, and runs the merged static
and dynamic set directly on the negotiated branch. It commits that same branch only after regression succeeds. If
prepare finds nothing open, return success without a preparation directory, formal run, branch modification, or
commit.

Write fix entities to `targets/starry/fixes/<id>.yaml`, update the corresponding findings to
`resolution: fixed`, and record the negotiated branch, patch, and regression result. The Git commit ID is not a
SyscallGuard dependency and must not be persisted. Failed runs keep their artifacts and uncommitted dedicated-branch
changes but do not update completed fix entities.

Read each source report directly from trailing `syscallguard_check_report` metadata. Store its IDs in
`source_check_report_ids`; validators may still read historical manifests that use `from_run_id`. The implementation
patch staging path is `/tmp/syscallguard-fix/<run-id>/`; never add downstream artifacts to a check report directory.

Compare dependency timestamps before hashes and reject manual edits that did not advance a
timestamp. Record generation times and direct dependency versions on the patch metadata, regression
result, fix, and updated finding. Treat finding syscall ownership as immutable evidence from the
mapping report. Never write fix state back into a general rule.
