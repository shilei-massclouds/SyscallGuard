---
name: ingest-syscall-specs
description: Import new or changed target-independent syscall rules from a configured source, defaulting to a batch of 20 from the repository's default source. Use when the user invokes `$ingest-syscall-specs`, optionally supplies a source alias or descriptor, a positive count or all, or an explicit syscall list, asks to refresh the general syscall rule library, or asks to “提取规则”或提取 syscall 规则. Do not map or inspect Starry.
---

# Ingest Syscall Specs

## Execute

1. Parse optional `source=<alias-or-descriptor>` and either `count=<positive-integer-or-all>` or
   `syscalls=<comma-separated-names>`. Reject an explicit `count` combined with `syscalls`.
2. Read [references/contract.md](references/contract.md).
3. Run the command, omitting flags the user omitted:

   ```bash
   python3 skills/ingest-syscall-specs/scripts/run.py [--source <source>] [--count <count> | --syscalls <names>]
   ```

4. Inspect the YAML frontmatter and body of `runs/<report-id>/report.md`.
5. Report the resolved source/revision, recognition-rules hash, count source, pending and selected syscalls, formed/no-rule results, rule IDs, and the report path.

## Boundaries

- Select pending syscalls by normalized name in lexical order.
- Normalize an explicit syscall list by trimming and lowercasing names, rejecting empty or unknown
  entries, removing duplicates, and sorting lexically. Ignore descriptor `default_count` in this mode.
- Restrict list-mode selection to requested syscalls while still skipping unchanged fingerprints and
  reporting the global pending count.
- Treat both `formed_rules` and `no_rules` report rows as successful incremental state until source or recognition fingerprints change.
- Publish a syscall's candidate rules only when every recognized evidence row resolves and at least one rule forms. Record unresolved counts in the report, but do not persist raw evidence.
- Publish rule files atomically and publish the report last. On failure, write neither a report nor rule updates so the next call retries automatically.
- Preserve `generated_at_utc` when only rule sources change.
- Never inspect, map, modify, build, or test Starry. Never invoke another SyscallGuard skill.
