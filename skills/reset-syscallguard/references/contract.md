# Reset Contract

The reset boundary is the target-independent ingestion state. Remove every YAML file directly under
`library/rules/` and every `runs/spec-*/report.md`. These reports are both history and incremental
state, so the next ingest treats every discovered syscall as new.

Do not delete `sources/`, recognition configuration, schemas, constraints, Starry shared mappings,
static checks, dynamic tests, findings, fixes, or mapping/check/fix runs. Do not follow symlinks or
delete unrelated files from a non-empty ingest report directory.
