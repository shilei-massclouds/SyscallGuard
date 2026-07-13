# Starry Fix Contract

Fix only shared finding entities referenced by the input check run with `status: confirmed` and
`resolution: open`. Do not create patches for any check-run blocker.

The execution engine creates a new detached worktree at the checked commit, reapplies all mapped
test patches, applies `implementation-fix.patch`, and runs the complete mapped static and dynamic
set. It creates `syscallguard/<run-id>` and a commit only after regression succeeds.

Write fix entities to `targets/starry/fixes/<id>.yaml`, update the corresponding findings to
`resolution: fixed`, and record the branch, commit, patch, and regression result. Failed runs keep
their artifacts and worktree but do not update completed fix entities.
