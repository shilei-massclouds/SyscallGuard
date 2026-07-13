---
name: ingest-syscall-specs
description: Incrementally ingest syscall specifications from a declared source, normalize target-independent behavior, and update SyscallGuard's shared spec and rule library. Use only when the user invokes `$ingest-syscall-specs` with source and count arguments or explicitly asks to import a bounded number of new or changed syscall specs. Do not map or inspect Starry.
---

# Ingest Syscall Specs

## Execute

1. Parse exactly `source=<source-descriptor>` and `count=<N>`. Require a positive integer count and an existing YAML source descriptor.
2. Read [references/contract.md](references/contract.md) before changing source adapters or shared entities.
3. Run:

   ```bash
   python3 skills/ingest-syscall-specs/scripts/run.py --source <descriptor> --count <N>
   ```

4. Inspect the produced manifest, changeset, raw candidates, normalized specs, and semantic-conflict rows. Correct malformed normalization in the shared entity files before reporting completion.
5. Report the run status, selected syscall IDs, counts, conflicts, and the printed run/spec/rule paths.

## Boundaries

- Select only new or source-fingerprint-changed syscalls, in adapter order, capped by `count`.
- Treat a smaller available set as a successful run and report the shortage.
- Merge identical rule semantics across provenance sources. Preserve conflicting semantics as explicit variants.
- Publish specs and target-independent rules only after extraction succeeds.
- Never inspect, map, modify, build, or test Starry.
- Never ask for approval and never invoke another SyscallGuard skill.
