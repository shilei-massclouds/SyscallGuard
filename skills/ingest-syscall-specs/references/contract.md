# Ingestion Contract

Resolve an omitted source through `sources/index.yaml:default_source`; resolve an explicit value as
an alias first and then as a descriptor path. Resolve count in this order: command, descriptor
`default_count`, global default 20. Accept only a positive integer or `all`.

Implement every source adapter with `discover`, `prescan`, and `extract`. The current `ltp` adapter
reads source instances containing only `source_id`, `adapter`, `location`, `revision`, and optional
`default_count`. Keep all macro, helper, old-API, array, normalization, precondition, and rule-template
choices in `sources/adapters/ltp/recognition-rules.yaml`; never import tools from the LTP checkout.

Write only `runs/<report-id>/report.md` and created or updated `library/rules/*.yaml`. The report's
YAML frontmatter is the human report, incremental state, and downstream input. Scan all prior
`runs/spec-*/report.md` files and use the newest row per source ID and syscall. Skip unchanged
`formed_rules` and `no_rules` rows. A failed call writes no report and advances no state.

Each syscall row records source and recognition fingerprints, result, versioned rules, raw evidence
count, unresolved evidence count, and reason. If any evidence is unresolved or no rule forms, record
`no_rules` and publish none of that syscall's candidates. Do not persist raw or normalized evidence.

Hash rule category and semantics into `semantic_hash`. Reuse identical semantics and merge `sources`.
Do not advance `generated_at_utc` for a sources-only change. Record every rule source with source ID
and type, revision, file, line, recognizer ID, and evidence hash. Never store downstream references
or run progress in a rule.
