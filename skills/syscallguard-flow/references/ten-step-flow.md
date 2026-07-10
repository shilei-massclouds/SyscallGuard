# SyscallGuard Ten-Step Flow

Use this reference after selecting exactly one step to execute or inspect. Preserve this order for every batch.

## State Progression

- A step is ready to start only when all earlier sign-offs are `confirmed` or intentionally `not_applicable`.
- A completed step has a Markdown report and a YAML sign-off.
- A newly completed step normally stops with `status: "pending_human_review"`.
- Do not continue into the next step until the user confirms the current step's sign-off.

## Step Checklist

| Step | Inputs | Work | Outputs | Required Checks | Stop Condition |
| --- | --- | --- | --- | --- | --- |
| `01-scope-selection` | `manifest.yaml`, source index, candidate specs | Select included behavior IDs, priority, exclusions, and batch purpose. | `steps/01-scope-selection.md`, `reviews/01-scope-selection-signoff.yaml`, manifest `scope`. | Included behavior IDs are stable; exclusions explain why they are outside this batch; no Starry/LTP edits are planned inside the harness. | Ask for human confirmation of scope. |
| `02-spec-ingestion` | Source snapshots, behavior specs, `inputs/source-index.yaml` | Record snapshot IDs, imported specs, missing source documents, and provenance. | `steps/02-spec-ingestion.md`, `reviews/02-spec-ingestion-signoff.yaml`, input artifact references. | Every imported behavior points to a snapshot path or an explicit source gap. | Ask for human confirmation of source completeness and gaps. |
| `03-normalization-review` | Imported behavior specs from step 02 | Normalize syscall behavior into stable IDs, preconditions, action, expected result, errno, and source refs. | `steps/03-normalization-review.md`, `reviews/03-normalization-review-signoff.yaml`, normalized spec updates if needed. | Each scoped behavior has enough normalized detail to classify and map evidence. | Ask for human confirmation of normalized semantics. |
| `04-checkability-classification` | Normalized behavior specs | Assign `static`, `partial_static`, `dynamic`, `unsupported`, or `needs_review`. | `steps/04-checkability-classification.md`, `reviews/04-checkability-classification-signoff.yaml`. | Classification is justified per behavior; `unsupported` and `needs_review` have reasons. | Ask for human confirmation of checkability labels. |
| `05-starry-evidence-mapping` | Scoped behaviors, Starry snapshot paths, tests, logs, audit notes | Map each behavior to Starry code, test source, log, manual audit evidence, or a recorded gap. | `steps/05-starry-evidence-mapping.md`, `reviews/05-starry-evidence-mapping-signoff.yaml`. | Evidence paths exist or are documented external references; covered behaviors have Starry evidence unless triaged as gap/risk/unsupported/needs_review. | Ask for human confirmation of evidence paths and sufficiency. |
| `06-static-check-or-audit` | Checkability labels, Starry evidence | Run available static checks or perform manual audit for static/partial_static items. | `steps/06-static-check-or-audit.md`, `reviews/06-static-check-or-audit-signoff.yaml`. | Results are tied to behavior IDs; manual audit notes name files and logic reviewed. | Ask for human confirmation of audit/check result. |
| `07-gap-triage` | Evidence gaps, source gaps, unsupported/needs_review items | Classify each gap or risk and decide whether it blocks this batch. | `steps/07-gap-triage.md`, `reviews/07-gap-triage-signoff.yaml`, gap records. | Every gap/risk has a triage decision and follow-up or non-blocking rationale. | Ask for human confirmation of triage decisions. |
| `08-fix-plan-and-apply-outside-harness` | Gap triage and evidence status | Record external Starry fix plan, links, commits, or decision that no harness-side fix is applied. | `steps/08-fix-plan-and-apply-outside-harness.md`, `reviews/08-fix-plan-and-apply-outside-harness-signoff.yaml`. | Any implementation change is outside the harness and referenced as evidence; the harness itself only records the plan/result. | Ask for human confirmation of external-fix boundary and evidence. |
| `09-validation` | Fix evidence, tests, build logs, static checks, manual validation | Record validation performed or explicitly not run. | `steps/09-validation.md`, `reviews/09-validation-signoff.yaml`, validation report if used. | Each behavior has validation status; missing fresh runs are recorded as risk or limitation. | Ask for human confirmation of validation state. |
| `10-batch-closeout` | All prior reports/sign-offs, coverage matrix, batch report | Check closeout gates, update final coverage and batch summary when allowed. | `steps/10-batch-closeout.md`, `reviews/10-batch-closeout-signoff.yaml`, `outputs/coverage-matrix.yaml`, `outputs/batch-report.md`. | All scoped behaviors are in coverage; all gaps/risks are triaged; all sign-offs are resolved before status becomes `closed`. | If gates pass, ask for closeout confirmation; if not, list blockers and leave batch open. |

## Step Selection Rules

- If the user asks for "第 N 步", execute only that numbered step.
- If the user asks to "继续下一步", inspect prior sign-offs first. Stop immediately on the first unresolved prior sign-off.
- If the user asks to "演练当前批次", explain current batch state and identify the next eligible step; only create or update artifacts if the user also asks to execute.
- If the user asks to "检查能否 closeout", run the closeout checks without changing manifest status.
