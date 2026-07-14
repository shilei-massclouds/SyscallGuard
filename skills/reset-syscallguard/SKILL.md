---
name: reset-syscallguard
description: Reset SyscallGuard's target-independent ingestion state by deleting the syscall index, every shared rule YAML, and every ingest report. Use only when the user invokes `$reset-syscallguard` or explicitly asks to return syscall rule ingestion to an empty initial state. Preserve source configuration, mapping reports, checks, tests, findings, fixes, and non-ingest run artifacts.
---

# Reset SyscallGuard

## Execute

1. Read [references/contract.md](references/contract.md).
2. Run:

   ```bash
   python3 skills/reset-syscallguard/scripts/run.py
   ```

3. Report both removal counts and the printed library/report roots.

## Boundaries

- Treat explicit invocation as authorization for the deletion described by the contract.
- Delete only `library/syscalls.yaml`, `library/rules/*.yaml`, and `runs/spec-*/report.md`; prune an ingest report directory only when it becomes empty.
- Preserve source descriptors, recognition rules, mapping reports, Starry shared entities, check/fix runs, and every non-ingest artifact.
- Do not invoke ingestion or any other SyscallGuard skill after reset.
