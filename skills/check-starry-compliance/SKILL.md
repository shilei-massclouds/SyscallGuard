---
name: check-starry-compliance
description: After confirming the mapping-negotiated Starry branch with the user, execute static checks and temporarily injected dynamic tests directly on that clean branch, aggregate every current open finding, and revalidate historical findings after content changes. Use when the user invokes `$合规检查` or the compatible `$check-starry-compliance` alias with a from argument. Do not generate implementation fixes.
---

# 合规检查

## Execute

1. Parse exactly `from=<mapping-report-id>`.
2. Read [references/contract.md](references/contract.md).
3. Read `target.branch` from the mapping report and ask the user to confirm that compliance checking should still use that branch. Wait for confirmation, and require that branch to be currently checked out and clean.
4. Run:

   ```bash
   python3 skills/check-starry-compliance/scripts/run.py --from <mapping-report-id>
   ```

5. Confirmation authorizes temporary test-patch injection on that branch, static checks, builds, QEMU, and bound dynamic tests. Do not request another authorization. Revert injected test patches before publishing the report.
6. Inspect the Chinese report and its trailing `syscallguard_check_report` metadata. Keep build, disk, toolchain, QEMU, rootfs, test-injection, and cleanup failures as blockers. Publish only evidence-backed rule failures as findings. Treat fixed findings from another content snapshot only as historical regression seeds: keep them unchanged and create a current-snapshot finding only when their source fails again.
7. Report the confirmed branch, pass/fail/skipped/not-run/error counts, blockers, the complete current-snapshot open finding IDs, new/carried/revalidated/needs-revalidation IDs, retained diagnostic path when present, and the report path.

## Boundaries

- Reject stale mappings when any recorded entity dependency or the current Starry content snapshot differs.
- Use the mapping report's `execution_scope` as the base. Add original static/dynamic sources for open findings from older snapshots as the revalidation scope, and record base, revalidation, and effective scopes separately.
- Also revalidate a same-snapshot open finding when all of its occurrences predate the negotiated branch workflow or belong to another branch, so a new current-branch occurrence can become authoritative for fixing.
- Carry forward same-snapshot open findings outside the effective scope. A conclusive old-snapshot failure supersedes the old finding with a current-snapshot finding; all-pass marks it `no_longer_reproduces`; missing definitions or blockers leave it open under `needs_revalidation`.
- Persist only `runs/check-*/report.md` plus the shared finding index/details. Do not create a check manifest, changeset, separate results file, or successful-run log directory.
- Reuse an earlier completed check only when all versions, content snapshots, and current open finding selection are identical and no older-snapshot finding needs revalidation; record `reused_from` and do not add occurrences.
- Use `/tmp/syscallguard-check/<check-id>` only for logs. Delete it after a blocker-free publication; retain it for blockers or failures.
- Execute on the negotiated branch. It must be clean before execution and return to the mapped content snapshot after temporary test patches are reverted.
- Do not write or apply implementation fixes and do not create a completion commit.
- Never ask for approval and never invoke another SyscallGuard skill.
