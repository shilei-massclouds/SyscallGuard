---
name: check-starry-compliance
description: Execute static checks and injected dynamic tests from one SyscallGuard mapping report in an isolated Starry Git worktree, aggregate every current open finding, and revalidate historical findings after Starry snapshot changes. Use when the user invokes `$合规检查` or the compatible `$check-starry-compliance` alias with a from argument. Do not generate implementation fixes.
---

# 合规检查

## Execute

1. Parse exactly `from=<mapping-report-id>`.
2. Read [references/contract.md](references/contract.md).
3. Run:

   ```bash
   python3 skills/check-starry-compliance/scripts/run.py --from <mapping-report-id>
   ```

4. Calling this skill authorizes creation of an isolated worktree, test-patch injection, static checks, builds, QEMU, and bound dynamic tests. Do not request a second authorization.
5. Inspect the Chinese report and its trailing `syscallguard_check_report` metadata. Keep build, disk, toolchain, QEMU, rootfs, and test-injection failures as blockers. Publish only evidence-backed rule failures as findings.
6. Report pass/fail/skipped/not-run/error counts, blockers, the complete current-snapshot open finding IDs, new/carried/revalidated/needs-revalidation IDs, retained diagnostic path when present, and the report path.

## Boundaries

- Reject stale mappings when any recorded entity dependency or the current Starry content snapshot differs.
- Use the mapping report's `execution_scope` as the base. Add original static/dynamic sources for open findings from older snapshots as the revalidation scope, and record base, revalidation, and effective scopes separately.
- Carry forward same-snapshot open findings outside the effective scope. A conclusive old-snapshot failure supersedes the old finding with a current-snapshot finding; all-pass marks it `no_longer_reproduces`; missing definitions or blockers leave it open under `needs_revalidation`.
- Persist only `runs/check-*/report.md` plus the shared finding index/details. Do not create a check manifest, changeset, separate results file, or successful-run log directory.
- Reuse an earlier completed check only when all versions, content snapshots, and current open finding selection are identical and no older-snapshot finding needs revalidation; record `reused_from` and do not add occurrences.
- Use `/tmp/syscallguard-check/<check-id>` for execution. Delete it and its worktree after a blocker-free publication; retain it for blockers or failures.
- Modify only the isolated worktree. Never change the user's existing Starry worktree or branch.
- Do not write or apply implementation fixes and do not create a completion commit.
- Never ask for approval and never invoke another SyscallGuard skill.
