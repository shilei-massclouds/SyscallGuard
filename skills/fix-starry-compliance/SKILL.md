---
name: fix-starry-compliance
description: After confirming the mapping-negotiated Starry branch with the user, automatically repair every open confirmed finding on that branch, merge evidence-bearing check scopes, retain injected tests, run regression, and commit successful fixes directly to the same branch. Use when the user invokes `$修复缺口` or the compatible `$fix-starry-compliance` alias without arguments. Never fix environment blockers.
---

# 修复缺口

## Execute

1. Accept no user arguments. In particular, reject the removed `from=` interface. Read [references/contract.md](references/contract.md).
2. Resolve the branch shared by the selected finding evidence and ask the user to confirm that fixing should still use that branch. Wait for confirmation; the branch must be currently checked out and clean.
3. Run the prepare phase:

   ```bash
   python3 skills/fix-starry-compliance/scripts/run.py
   ```

4. If prepare reports `no_open_findings`, report success and stop. Do not create a formal fix run or modify the branch.
5. Otherwise read the printed preparation, all selected finding evidence, and the pinned Starry source. Generate one smallest combined implementation patch that resolves every selected finding. Save it only at the printed `/tmp/syscallguard-fix/<run-id>/implementation-fix.patch` path.
6. Run the printed finalize command. Finalize revalidates the prepared branch, snapshot, and every selected dependency before applying test patches, the implementation patch, and merged regression scope directly to that branch.
7. Confirmation authorizes patch generation/application, regression, and a successful commit on the negotiated branch. Do not ask for patch approval.
8. Report the branch, all selected findings and source check reports, regression results, blockers, and fix paths. Do not merge another branch or persist the Git commit ID in SyscallGuard data.

## Boundaries

- Select findings from the shared finding index, not from a latest check report. Include exactly all `status: confirmed`, `resolution: open` findings matching the current Starry content snapshot.
- Collect every evidence-bearing check report from finding occurrences. Merge each report's complete static/dynamic/rule scope by ID and apply each unique dynamic test patch once.
- Refuse prepare/finalize when the evidence branch is missing, the current branch differs, the working tree is dirty before execution, or a selected finding, source check report, scoped entity, or Starry content snapshot changed.
- Preserve the syscall ownership recorded by the mapping report; never reconstruct it from removed syscall specs or ingest reports.
- Apply the scoped dynamic test patches before the implementation patch so tests are retained in a successful commit.
- Require every static and enabled dynamic regression to pass. A skipped disabled test is allowed; `not_run` is not.
- On regression or commit failure, create no completion commit and retain the applied changes on the dedicated branch plus the patch and logs for diagnosis.
- Version the patch, regression result, finding update, and fix. Record every evidence source in `source_check_report_ids`; do not write `from_run_id` in new manifests.
- Modify and commit only the user-confirmed dedicated branch. Never create, switch, or merge branches, and never invoke another SyscallGuard skill.
