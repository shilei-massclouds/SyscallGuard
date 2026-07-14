# Starry Fix Contract

Fix only shared finding entities referenced by the input check run with `status: confirmed` and
`resolution: open`. Do not create patches for any check-run blocker.

The execution engine creates a new detached worktree matching the checked content snapshot, reapplies all scoped
test patches, applies `implementation-fix.patch`, and runs the mapping report's scoped static and dynamic
set. It creates `syscallguard/<run-id>` and a commit only after regression succeeds.

Write fix entities to `targets/starry/fixes/<id>.yaml`, update the corresponding findings to
`resolution: fixed`, and record the branch, patch, and regression result. The Git commit ID is not a
SyscallGuard dependency and must not be persisted. Failed runs keep
their artifacts and worktree but do not update completed fix entities.

Compare dependency timestamps before hashes and reject manual edits that did not advance a
timestamp. Record generation times and direct dependency versions on the patch metadata, regression
result, fix, and updated finding. Treat finding syscall ownership as immutable evidence from the
mapping report. Never write fix state back into a general rule.
