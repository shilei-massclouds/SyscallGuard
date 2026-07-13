# SyscallGuard Ten-Step Flow

Use this reference after selecting exactly one step to execute or inspect. Preserve this order for every batch.

## State Progression

- A step is ready to start only when all earlier sign-offs are `confirmed` or intentionally `not_applicable`.
- A completed step has a Markdown report and a YAML sign-off.
- For syscall-oriented batches, step `01-scope-selection` must immediately present the next candidate syscall list. The default batch size is 20.
- Do not repeat syscalls already listed as checked in `batches/syscall-check-history.yaml`.
- A newly completed step normally stops with `status: "pending_human_review"`.
- Do not continue into the next step until the user confirms the current step's sign-off.

## Screen Review Contract

At every stop condition, the assistant response must show a concrete review block in chat. This
block is user guidance, not part of the step report.

Use this order:

1. Current step and status.
2. Files to review.
3. Concrete list of items produced or checked in this step.
4. Numbered confirmation checklist tied to that concrete list.
5. Accepted responses, such as `命令：批准进入下一步` or `修改 <编号>: ...`.

For Step 01, replace the general numbered checklist with exactly one confirmation question:
`是否同意处理这一批系统调用？` Do not add confirmation questions about scope details,
priority, exclusions, duplicates, or harness boundaries. After the question, show both accepted
responses: `命令：批准进入下一步` for approval and `修改：<调整内容>` for rejection or changes.
Do not use `修改 <编号>: ...` for Step 01.

For Step 02, list the investigated specification sources and missing materials, then ask exactly
`对这批系统调用规格来源的调查结果是否接受？` Do not add other confirmation questions. Show
`命令：批准进入下一步` and `修改：<调整内容>` as the two response paths; do not use numbered
modification syntax for Step 02.

For Step 03, briefly list the normalized syscall rule references, reusable rules, and target mappings,
then ask exactly `对这批系统调用检查规则的整理结果是否接受？` Do not add other confirmation
questions. Show `命令：批准进入下一步` and `修改：<调整内容>` as the two response paths; do not
use numbered modification syntax for Step 03.

Examples of concrete lists:

- Step 01 lists the selected syscall names, then asks only `是否同意处理这一批系统调用？`.
- Step 02 lists the investigated specification sources and missing materials, then asks only `对这批系统调用规格来源的调查结果是否接受？`.
- Step 03 briefly lists the normalized syscall rule references, reusable rules, and target mappings, then asks only `对这批系统调用检查规则的整理结果是否接受？`.
- Step 03 lists reusable rule IDs and any syscall groups with special handling.
- Step 04 lists rule classification rows such as `static`, `partial_static`, and `dynamic`.
- Step 05 lists evidence refs or source files located.
- Step 06 lists audited rule IDs and syscall groups before asking for confirmation.
- Step 07 lists each gap/risk/needs_review item before asking for triage confirmation.
- Step 08 lists dynamic validation cases and any missing execution bindings before asking the user to confirm the test case list.
- Step 09 executes the Step 08 approved validation cases, combines dynamic results with Step 06 static check/audit results, generates Starry patch candidates when gaps are confirmed, and asks whether those patches should be applied in Step 10.
- Step 10 applies user-approved Starry patches outside the harness, runs static and dynamic regression, lists resolved and unresolved items, and asks for human confirmation of the final result.

## Step Checklist

| Step | Inputs | Work | Outputs | Required Checks | Stop Condition |
| --- | --- | --- | --- | --- | --- |
| `01-scope-selection` | `manifest.yaml`, source index, candidate specs, `batches/syscall-check-history.yaml`, Starry syscall dispatch source or snapshot | Select included behavior IDs or syscall names, priority, exclusions, and batch purpose. For `命令：开始检查系统调用`, first display the next 20 unchecked syscall candidates. | `steps/01-scope-selection.md`, `reviews/01-scope-selection-signoff.yaml`, manifest `scope`, optional `scope.included_syscalls`. | Included behavior IDs or syscall names are stable; already checked syscalls are excluded; exclusions explain why they are outside this batch; no Starry/LTP edits are planned inside the harness. | After listing the syscall names, ask only `是否同意处理这一批系统调用？`; then show `命令：批准进入下一步` and `修改：<调整内容>` as the two response paths. |
| `02-spec-ingestion` | Source index, behavior specs, external commit refs, minimal copied snapshots if needed | Record source IDs, repository path/URL, branch or tag, commit, captured paths, hashes when available, imported specs, missing source documents, and provenance. | `steps/02-spec-ingestion.md`, `reviews/02-spec-ingestion-signoff.yaml`, input artifact references. | Every imported behavior points to a source-index entry, a copied snapshot path, or an explicit source gap. External source trees are not copied by default. | After listing the investigated sources and missing materials, ask only `对这批系统调用规格来源的调查结果是否接受？`; then show `命令：批准进入下一步` and `修改：<调整内容>` as the two response paths. |
| `03-normalization-review` | Imported behavior specs from step 02; for syscall batches, any available reference model for reusable rules | Normalize into stable IDs. For syscall batches, use `syscall -> rule_refs -> target mappings`: a syscall reference table, a reusable check rule table, and target-specific mapping drafts. | `steps/03-normalization-review.md`, `reviews/03-normalization-review-signoff.yaml`, normalized spec updates if needed. | Each scoped syscall references reusable rules; reusable rules are defined once; target mapping drafts do not inherit external pass/fix status unless imported as batch evidence. | After briefly listing the normalized results, ask only `对这批系统调用检查规则的整理结果是否接受？`; then show `命令：批准进入下一步` and `修改：<调整内容>` as the two response paths. |
| `04-checkability-classification` | Normalized behavior specs and syscall rule refs | Assign `static`, `partial_static`, `dynamic`, `unsupported`, or `needs_review` per behavior or per `syscall + rule_id`. | `steps/04-checkability-classification.md`, `reviews/04-checkability-classification-signoff.yaml`. | Classification is justified at rule granularity; `unsupported` and `needs_review` have reasons. | Ask for human confirmation of checkability labels. |
| `05-starry-evidence-mapping` | Scoped behaviors or `syscall + rule_id` pairs, Starry source refs or minimal snapshots, tests, logs, audit notes | Map each behavior or syscall-rule pair to Starry code, test source, log, manual audit evidence, or a recorded source/evidence limitation. | `steps/05-starry-evidence-mapping.md`, `reviews/05-starry-evidence-mapping-signoff.yaml`. | Evidence paths exist as copied snapshots or documented external references. "Not captured in snapshot" is not the same as "absent from Starry"; leave gap/risk triage to step 07. | Ask for human confirmation of evidence paths and sufficiency. |
| `06-static-check-or-audit` | Checkability labels, Starry evidence | Run available static checks or perform manual audit for static/partial_static items. | `steps/06-static-check-or-audit.md`, `reviews/06-static-check-or-audit-signoff.yaml`. | Results are tied to behavior IDs; manual audit notes name files and logic reviewed. | Ask for human confirmation in chat with this checklist: static/partial-static scope is correct; source refs and hashes are acceptable; support/deferred labels are reasonable; items needing step 07 triage are visible. |
| `07-gap-triage` | Evidence gaps, source gaps, unsupported/needs_review items | Classify each gap or risk and decide whether it blocks this batch. | `steps/07-gap-triage.md`, `reviews/07-gap-triage-signoff.yaml`, gap records. | Every gap/risk has a triage decision and follow-up or non-blocking rationale. | Ask for human confirmation of triage decisions. |
| `08-fix-plan-and-apply-outside-harness` | Gap triage and evidence status | Generate or register dynamic validation cases for runtime risks. Record that Starry patch generation is deferred to Step 09 after static and dynamic results are available. | `steps/08-fix-plan-and-apply-outside-harness.md`, `reviews/08-fix-plan-and-apply-outside-harness-signoff.yaml`, `outputs/validation-cases.yaml` when dynamic validation is needed. | Dynamic validation cases must be concrete enough for Step 09 to execute or to report a clear execution blocker. Step 08 does not ask about applying Starry patches. | Ask for human confirmation of the dynamic validation case list and visible execution blockers. |
| `09-validation` | Step 08 approved validation cases, Step 06 static check/audit results, dynamic test logs/results | Execute approved validation cases from Step 08, record results, combine them with Step 06 static check/audit results, and generate Starry patch candidates for confirmed implementation gaps. If execution cannot start because command/environment is missing, record that blocker as the Step 09 result and do not fabricate patches. | `steps/09-validation.md`, `reviews/09-validation-signoff.yaml`, validation report/logs and patch candidates if produced. | Each approved case has a result such as `pass`, `fail`, `skipped`, or `not_run`, with command/log evidence or an execution-blocker reason. Each patch candidate must map to Step 06 static evidence, Step 09 dynamic evidence, or both. No patch is applied in Step 09. | Ask whether the generated Starry patches should be applied in Step 10. If results or patches are rejected, return to Step 08 to modify test cases or fix evidence. |
| `10-batch-closeout` | Confirmed Step 09 patch application decision, patch candidates, all prior reports/sign-offs, coverage matrix, batch report | Apply user-approved Starry patches outside the harness, then run static and dynamic regression. Update final coverage and batch summary only after regression results are recorded. | `steps/10-batch-closeout.md`, `reviews/10-batch-closeout-signoff.yaml`, `outputs/coverage-matrix.yaml`, `outputs/batch-report.md`, regression logs if used. | Applied patch refs, static regression results, and dynamic regression results are recorded. All scoped behaviors are in coverage; all gaps/risks are triaged; all sign-offs are resolved before status becomes `closed`. | Show resolved and unresolved items, then ask for confirmation of patch application and regression outcome. |

## Step Selection Rules

- If the user issues `命令：执行第N步`, execute only that numbered step.
- If the user issues `命令：批准进入下一步` or asks in natural language to continue, inspect prior sign-offs first. Stop immediately on the first unresolved prior sign-off.
- If the user asks to "演练当前批次", explain current batch state and identify the next eligible step; only create or update artifacts if the user also asks to execute.
- If the user asks to "检查能否 closeout", run the closeout checks without changing manifest status.
