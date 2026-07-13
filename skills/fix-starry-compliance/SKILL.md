---
name: fix-starry-compliance
description: Repair confirmed implementation findings from one SyscallGuard check run in an isolated Starry worktree, retain injected tests, run full regression, and commit successful fixes on an isolated branch. Use only when the user invokes `$fix-starry-compliance` with a from argument or explicitly requests automatic repair of one check run. Never fix environment blockers.
---

# Fix Starry Compliance

## Execute

1. Parse exactly `from=<check-run-id>` and read [references/contract.md](references/contract.md).
2. Load only findings referenced by the check run whose `status` is `confirmed` and whose `resolution` is `open`. Ignore environment blockers.
3. Inspect the finding evidence and pinned source in an isolated detached worktree. Generate the smallest implementation patch that resolves all selected findings. Save it as `runs/<check-run-id>/implementation-fix.patch`.
4. Run:

   ```bash
   python3 skills/fix-starry-compliance/scripts/run.py --from <check-run-id>
   ```

5. Calling this skill authorizes patch generation/application and regression. Do not ask for patch approval.
6. Report selected findings, regression results, blockers, retained worktree, and printed fix paths. On success also report `syscallguard/<run-id>` and its commit. Do not merge it.

## Boundaries

- Refuse a stale check when Starry HEAD changed after checking.
- Apply the mapped dynamic test patches before the implementation patch so tests are retained in a successful commit.
- Require every static and enabled dynamic regression to pass. A skipped disabled test is allowed; `not_run` is not.
- On regression or commit failure, create no completion commit and retain the worktree, patch, and logs.
- Never modify or merge the user's existing Starry branch and never invoke another SyscallGuard skill.
