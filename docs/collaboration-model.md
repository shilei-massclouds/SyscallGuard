# Collaboration Model

SyscallGuard separates process ownership from external implementation work.

## Roles

- Harness owner: maintains workflow, templates, constraints, schemas, and batch
  consistency.
- Spec reviewer: checks whether a behavior statement is source-backed and
  normalized enough for classification.
- Starry evidence reviewer: checks mappings from behavior to Starry code,
  tests, logs, or manual audit notes.
- Validation owner: records build, static check, dynamic test, or manual
  validation results from external repositories.
- Closeout reviewer: confirms traceability, triage decisions, and unresolved
  risk before archival.

## Review Status Values

- `pending_human_review`: the artifact is ready for review but not accepted.
- `confirmed`: the reviewer accepts the artifact for the batch.
- `changes_requested`: the reviewer rejects the artifact until issues are fixed.
- `not_applicable`: the gate is explicitly skipped with justification.

## Rules

- A reviewer must not mark a step `confirmed` without checking its inputs and
  outputs.
- A step can be drafted by automation, but it is not accepted until a human
  sign-off file is updated.
- Evidence from external repositories must include path, commit or branch when
  available, and capture date.
- If evidence is missing, the batch records a gap rather than silently omitting
  the behavior.

