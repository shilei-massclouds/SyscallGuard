# Ingestion Contract

Resolve an omitted source through `sources/index.yaml:default_source`; resolve an explicit value as
an alias first and then as a descriptor path. Resolve count in this order: command, descriptor
`default_count`, global default 20. Accept only a positive integer or `all`.

Alternatively, accept `syscalls=<name1,name2,...>` as an explicit candidate restriction. Reject it
when command count is also explicit; descriptor `default_count` does not apply in list mode. Split on
commas, trim, lowercase, deduplicate, and sort syscall names. Reject an empty item, an empty list, or
any name that the resolved source does not contain before writing output. Apply the usual fingerprint
skip to requested names, so only new or changed requested syscalls are selected. Keep `pending_count`
global. In list-mode reports, store normalized names in `requested_syscalls` and store count as
`{value: null, source: explicit_syscalls}`.

Implement every source adapter with `discover`, `prescan`, and `extract`. The current `ltp` adapter
reads source instances containing only `source_id`, `adapter`, `location`, `revision`, and optional
`default_count`. Keep all macro, helper, old-API, array, normalization, precondition, and rule-template
choices in `sources/adapters/ltp/recognition-rules.yaml`; never import tools from the LTP checkout.
The `man_pages` adapter discovers only raw `__NR_*` entries from the configured RISC-V64 generated
UAPI header, excludes `__NR_syscalls`, follows man2 `.so` aliases, and uses directly referenced
man2const, man2type, and man7 pages only as hashed semantic context. Missing man2 documentation is a
non-blocking `no_rules: missing_documentation` result. Treat `ERRORS` as the primary rule-analysis
index: emit one independent rule per errno clause after applying its function qualifier. Use
`RETURN VALUE` only for unambiguous simple success, positive, fd, or fixed-value results.

Write only `runs/<report-id>/report.md`, `library/syscalls.yaml`, and created or updated
`library/rules/*.yaml`. `library/syscalls.yaml` is the first-level active syscall-to-rule index. Its
`inactive_rules` section retains retired/conflicted paths and original syscall ownership for
historical validation; new mapping selects active rules only. The rule
files are the second-level details. Prefix each rule YAML with a Chinese summary comment and repeat
the exact comment above its reference in `library/syscalls.yaml`. The report
starts with a concise Chinese explanation of rule conditions and expected results, and keeps its
machine-readable incremental state in a trailing metadata block. Scan all prior
`runs/spec-*/report.md` files and use the newest row per source ID and syscall. Publish the index and
rules atomically and publish the report last. Skip unchanged
`formed_rules` and `no_rules` rows. A failed call writes no report and advances no state.

Each syscall row records source and recognition fingerprints, result, versioned rules, raw evidence
count, unresolved evidence count, and reason. If any non-isolated evidence is unresolved or no rule
forms, record `no_rules` and publish none of that syscall's candidates. Explicitly invalid expected
errno and same-condition conflicts are isolated and never become active rules. Context evidence does
not participate in this gate. Do not persist raw or normalized evidence.

Hash rule category and semantics into `semantic_hash`. Reuse identical semantics and merge `sources`.
Do not advance `generated_at_utc` for a sources-only change. Record every rule source with source ID
and type, source content snapshot hash, file, line, recognizer ID, and evidence hash. Never store downstream references
or run progress in a rule.
