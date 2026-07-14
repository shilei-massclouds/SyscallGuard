---
name: fix-starry-compliance
description: Repair confirmed implementation findings from one SyscallGuard check report in an isolated Starry worktree, retain injected tests, run full regression, and commit successful fixes on an isolated branch. Use only when the user invokes `$fix-starry-compliance` with a from argument or explicitly requests automatic repair of one check report. Never fix environment blockers.
---

# Fix Starry Compliance

## Execute

1. Parse exactly `from=<check-report-id>` and read [references/contract.md](references/contract.md).
2. Read the input `syscallguard_check_report` metadata and load only its versioned findings whose `status` is `confirmed` and whose `resolution` is `open`. Ignore environment blockers.
3. Inspect the finding evidence and pinned source in an isolated detached worktree. Generate the smallest implementation patch that resolves all selected findings. Save it as `/tmp/syscallguard-fix/<check-report-id>/implementation-fix.patch`.
4. Run:

   ```bash
   python3 skills/fix-starry-compliance/scripts/run.py --from <check-report-id>
   ```

5. Calling this skill authorizes patch generation/application and regression. Do not ask for patch approval.
6. Report selected findings, regression results, blockers, retained worktree, and printed fix paths. On success also report the `syscallguard/<run-id>` branch. Do not merge it or persist its commit ID in SyscallGuard data.

## Boundaries

- Refuse a stale check when the check result, finding, scoped entity, or Starry content snapshot changed after checking.
- Preserve the syscall ownership recorded by the mapping report; never reconstruct it from removed syscall specs or ingest reports.
- Apply the scoped dynamic test patches before the implementation patch so tests are retained in a successful commit.
- Require every static and enabled dynamic regression to pass. A skipped disabled test is allowed; `not_run` is not.
- On regression or commit failure, create no completion commit and retain the worktree, patch, and logs.
- Version the patch, regression result, finding update, and fix; record only direct upstream dependencies.
- Never modify or merge the user's existing Starry branch and never invoke another SyscallGuard skill.
