---
name: check-starry-compliance
description: Execute static checks and injected dynamic tests from one SyscallGuard mapping report in an isolated Starry Git worktree, separating confirmed implementation findings from environment blockers. Use when the user invokes `$合规检查` or the compatible `$check-starry-compliance` alias with a from argument. Do not generate implementation fixes.
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
6. Report pass/fail/skipped/not-run/error counts, blockers, confirmed finding IDs, retained diagnostic path when present, and the report path.

## Boundaries

- Reject stale mappings when any recorded entity dependency or the current Starry content snapshot differs.
- Execute only the mapping report's `execution_scope`; generate finding syscall ownership from its complete `rule_syscalls`.
- Persist only `runs/check-*/report.md` plus the shared finding index/details. Do not create a check manifest, changeset, separate results file, or successful-run log directory.
- Reuse an earlier completed check only when all versions and content snapshots are identical; record `reused_from` in the new report and do not add finding occurrences for reuse.
- Use `/tmp/syscallguard-check/<check-id>` for execution. Delete it and its worktree after a blocker-free publication; retain it for blockers or failures.
- Modify only the isolated worktree. Never change the user's existing Starry worktree or branch.
- Do not write or apply implementation fixes and do not create a completion commit.
- Never ask for approval and never invoke another SyscallGuard skill.
