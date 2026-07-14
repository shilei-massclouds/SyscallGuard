---
name: check-starry-compliance
description: Execute static checks and injected dynamic tests from one SyscallGuard mapping run in an isolated Starry Git worktree, separating confirmed implementation findings from environment blockers. Use only when the user invokes `$check-starry-compliance` with a from argument or explicitly asks to execute one Starry mapping run. Do not generate implementation fixes.
---

# Check Starry Compliance

## Execute

1. Parse exactly `from=<mapping-run-id>`.
2. Read [references/contract.md](references/contract.md).
3. Run:

   ```bash
   python3 skills/check-starry-compliance/scripts/run.py --from <mapping-run-id>
   ```

4. Calling this skill authorizes creation of an isolated worktree, test-patch injection, static checks, builds, QEMU, and bound dynamic tests. Do not request a second authorization.
5. Inspect `results.yaml` and logs. Keep build, disk, toolchain, QEMU, rootfs, and test-injection failures as blockers. Publish only evidence-backed rule failures as findings.
6. Report pass/fail/skipped/not-run counts, blockers, confirmed finding IDs, worktree path, and printed result paths.

## Boundaries

- Reject stale mappings when any recorded entity dependency or the current Starry content snapshot differs.
- Generate finding syscall ownership from the mapping run's `rule_syscalls`; never read a syscall spec.
- Version check results and findings with generation times and direct upstream dependency records. Reuse an earlier completed check only when all versions and content snapshots are identical.
- Modify only the isolated worktree. Never change the user's existing Starry worktree or branch.
- Do not write or apply implementation fixes and do not create a completion commit.
- Never ask for approval and never invoke another SyscallGuard skill.
