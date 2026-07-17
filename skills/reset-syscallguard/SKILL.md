---
name: reset-syscallguard
description: Reset SyscallGuard's target-independent ingestion state by deleting the syscall index, every shared rule YAML, and every ingest report. Use only when the user invokes `$项目重置` or the compatible `$reset-syscallguard` alias, or explicitly asks to return syscall rule ingestion to an empty initial state. Before deleting anything, warn that the rule library and ingest history will be cleared, explain what is preserved, and wait for a separate explicit confirmation.
---

# 项目重置

## Execute

1. Read [references/contract.md](references/contract.md).
2. Warn the user that this operation deletes the general rule library and all ingest history. State explicitly that source configuration, mapping reports, checks, tests, findings, fixes, and other non-ingest artifacts will be preserved. Ask whether to continue and wait for a separate explicit confirmation.
3. Only after the user explicitly confirms the warning, run:

   ```bash
   python3 skills/reset-syscallguard/scripts/run.py
   ```

4. Report both removal counts and the printed library/report roots.

## Boundaries

- Treat invocation as a reset request, not as authorization to delete. Never run the script unless the user explicitly confirms after receiving the warning in step 2.
- Delete only `library/syscalls.yaml`, `library/rules/*.yaml`, and `runs/spec-*/report.md`; prune an ingest report directory only when it becomes empty.
- Preserve source descriptors, recognition rules, mapping reports, Starry shared entities, check/fix runs, and every non-ingest artifact.
- Do not invoke ingestion or any other SyscallGuard skill after reset.
