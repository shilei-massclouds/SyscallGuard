# Batch Process

Every batch uses the same ten steps. Step reports live in
`batches/<id>/steps/` and sign-offs live in `batches/<id>/reviews/`.

| Step | Name | Required Output |
| --- | --- | --- |
| 01 | `scope-selection` | Scope, sources, priorities, exclusions |
| 02 | `spec-ingestion` | Source snapshot versions and imported behaviors |
| 03 | `normalization-review` | Normalized behavior specs and review notes |
| 04 | `checkability-classification` | Static, partial static, dynamic, unsupported, needs review |
| 05 | `starry-evidence-mapping` | Starry code, test, log, or manual audit evidence |
| 06 | `static-check-or-audit` | Static checker result or manual audit record |
| 07 | `gap-triage` | Gap, risk, unsupported, and needs-review decisions |
| 08 | `fix-plan-and-apply-outside-harness` | External Starry fix plan and links |
| 09 | `validation` | Build, static checker, dynamic test, or manual validation result |
| 10 | `batch-closeout` | Coverage matrix, unresolved risks, final report |

## Step Gate

Each step requires:

- A Markdown step report.
- A YAML review sign-off.
- Explicit input and output paths.
- Traceability to either a snapshot, an external evidence reference, or a
  recorded gap.

## Closeout Gate

A batch cannot be marked closed unless:

- Every scoped behavior appears in the coverage matrix.
- Every coverage item references a source spec and Starry evidence or a gap.
- Every gap or risk has a triage decision.
- Every step sign-off is `confirmed` or explicitly `not_applicable`.

