---
name: map-starry-checks
description: Map the rules selected by one SyscallGuard spec run to a pinned Starry revision, producing target mappings, executable static checks, and dynamic test definitions. Use only when the user invokes `$map-starry-checks` with from and target arguments or explicitly requests Starry mapping for one spec run. Do not modify or execute Starry.
---

# Map Starry Checks

## Execute

1. Parse exactly `from=<spec-run-id>` and `target=<starry-descriptor>`.
2. Read [references/contract.md](references/contract.md).
3. Verify that `from` is a readable `spec` run. Use only its syscall and rule IDs, then read the current shared entities and recompute their hashes.
4. Run:

   ```bash
   python3 skills/map-starry-checks/scripts/run.py --from <spec-run-id> --target <descriptor>
   ```

5. Inspect the pinned Starry commit without changing it. Refine created mappings when repository evidence supports a concrete classification, file/symbol location, static rule, or dynamic test. Leave uncertain items explicitly `needs_review`; never invent evidence.
6. Keep indexes synchronized for any refined shared entity, and update the mapping run hashes or rerun the command so the snapshot matches the current view.
7. Report the base commit, classifications, created/updated/skipped counts, and printed result paths.

## Boundaries

- Classify each selected rule as `static`, `partial_static`, `dynamic`, `unsupported`, or `needs_review`.
- A changed rule hash or Starry commit requires a new mapping result. Reuse identical inputs.
- Generate test source, build metadata, patch reference, and execution binding for dynamic checks.
- Never create a worktree, apply a patch, run a check, build Starry, or execute a test.
- Never ask for approval and never invoke another SyscallGuard skill.
