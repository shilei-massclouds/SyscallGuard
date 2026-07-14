---
name: map-starry-checks
description: Map the rules selected by one SyscallGuard ingest report to a pinned Starry revision, producing target mappings, executable static checks, and dynamic test definitions. Use only when the user invokes `$map-starry-checks` with from and target arguments or explicitly requests Starry mapping for one ingest report. Do not modify or execute Starry.
---

# Map Starry Checks

## Execute

1. Parse exactly `from=<report-id>` and `target=<starry-descriptor>`.
2. Read [references/contract.md](references/contract.md).
3. Verify that `from` is a valid ingest report and is the newest report for every syscall it contains. Compare each rule timestamp first and semantic hash second.
4. Run:

   ```bash
   python3 skills/map-starry-checks/scripts/run.py --from <report-id> --target <descriptor>
   ```

5. Inspect the pinned Starry commit without changing it. Refine created mappings when repository evidence supports a concrete classification, file/symbol location, static rule, or dynamic test. Leave uncertain items explicitly `needs_review`; never invent evidence.
6. Keep indexes synchronized for any refined shared entity, and update the mapping run hashes or rerun the command so the snapshot matches the current view.
7. Report the base commit, classifications, created/updated/skipped counts, and printed result paths.

## Boundaries

- Classify each selected rule as `static`, `partial_static`, `dynamic`, `unsupported`, or `needs_review`.
- Record `{id, generated_at_utc, content_hash}` for every direct rule dependency. A timestamp, semantic hash, or Starry commit mismatch is stale and must be rejected.
- Save `from_report_id` and the report's rule-to-syscall ownership as `rule_syscalls` in the mapping manifest.
- Preserve an entity's generation time when its dependencies and mapped target are unchanged.
- Generate test source, build metadata, patch reference, and execution binding for dynamic checks.
- Never create a worktree, apply a patch, run a check, build Starry, or execute a test.
- Never ask for approval and never invoke another SyscallGuard skill.
