---
name: fix-starry-compliance
description: Automatically repair every open confirmed finding for the current Starry content snapshot in one isolated worktree, merge evidence-bearing check scopes, retain injected tests, run regression, and commit successful fixes on an isolated branch. Use when the user invokes `$修复缺口` or the compatible `$fix-starry-compliance` alias without arguments. Never fix environment blockers.
---

# 修复缺口

## Execute

1. Accept no user arguments. In particular, reject the removed `from=` interface. Read [references/contract.md](references/contract.md).
2. Run the prepare phase:

   ```bash
   python3 skills/fix-starry-compliance/scripts/run.py
   ```

3. If prepare reports `no_open_findings`, report success and stop. Do not create a worktree, branch, or formal fix run.
4. Otherwise read the printed preparation, all selected finding evidence, and the pinned Starry source. Generate one smallest combined implementation patch that resolves every selected finding. Save it only at the printed `/tmp/syscallguard-fix/<run-id>/implementation-fix.patch` path.
5. Run the printed finalize command. Finalize revalidates the prepared snapshot and every selected dependency before applying the patch and merged regression scope.
6. Calling this skill authorizes patch generation/application and regression. Do not ask for patch approval.
7. Report all selected findings and source check reports, regression results, blockers, retained worktree, and fix paths. On success also report the `syscallguard/<run-id>` branch. Do not merge it or persist its commit ID in SyscallGuard data.

## Boundaries

- Select findings from the shared finding index, not from a latest check report. Include exactly all `status: confirmed`, `resolution: open` findings matching the current Starry content snapshot.
- Collect every evidence-bearing check report from finding occurrences. Merge each report's complete static/dynamic/rule scope by ID and apply each unique dynamic test patch once.
- Refuse finalize when a selected finding, source check report, scoped entity, or Starry content snapshot changed after prepare.
- Preserve the syscall ownership recorded by the mapping report; never reconstruct it from removed syscall specs or ingest reports.
- Apply the scoped dynamic test patches before the implementation patch so tests are retained in a successful commit.
- Require every static and enabled dynamic regression to pass. A skipped disabled test is allowed; `not_run` is not.
- On regression or commit failure, create no completion commit and retain the worktree, patch, and logs.
- Version the patch, regression result, finding update, and fix. Record every evidence source in `source_check_report_ids`; do not write `from_run_id` in new manifests.
- Never modify or merge the user's existing Starry branch and never invoke another SyscallGuard skill.
