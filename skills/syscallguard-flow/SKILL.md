---
name: syscallguard-flow
description: Orchestrate SyscallGuard's fixed ten-step batch workflow. Use when a user issues `命令：开始检查系统调用`, `命令：批准进入下一步`, `命令：检查当前进度`, or `命令：执行第1步` through `命令：执行第10步` (also accept the half-width `命令:` prefix); or when Codex needs to pick the next syscall batch, rehearse, create, inspect, advance, review, sign off, validate, or close out a SyscallGuard batch; determine the current or next step; enforce pending human review gates; check coverage matrices; avoid rechecking completed syscalls; or work with batch manifest files, steps, reviews, and outputs.
---

# SyscallGuard Flow

## Core Rules

- Use Chinese for user-facing explanations, review guidance, and gate messages. Keep paths, behavior IDs, field names, enum values, source excerpts, and command names unchanged.
- Read `README.md`, `docs/batch-process.md`, and the target batch `manifest.yaml` before changing batch artifacts.
- If the user issues `命令：开始检查系统调用` or the compatible half-width form `命令:开始检查系统调用`, immediately start with step `01-scope-selection`: show progress, derive the next syscall candidate list, and display the default batch of 20 syscalls before doing deeper analysis.
- Default to 20 syscalls per new batch unless the user gives another size.
- Exclude syscalls already recorded as checked in `batches/syscall-check-history.yaml`. If the history file is absent, say that no prior syscall history was found and start from the dispatch order.
- Record completed syscall check results in `batches/syscall-check-history.yaml` after human review confirms the relevant batch result, so future batches do not repeat them. Use `next_syscalls.py record` for this; do not record unresolved review results unless the user explicitly asks for dry review work.
- Process exactly one workflow step per user request. After producing or checking that step, stop at review sign-off and do not advance automatically.
- Keep batch artifacts factual. Do not put conversational review instructions, "what the user should do next", or tool suitability discussion into step reports unless that tool was actually used as evidence for the step.
- Before continuing to a later step, require the previous step sign-off status to be `confirmed` or a justified `not_applicable`. If it is `pending_human_review` or `changes_requested`, stop and tell the user which review file must be resolved.
- Write new or refreshed sign-off files with `status: "pending_human_review"` unless the user explicitly provides a reviewer decision.
- Preserve the harness boundary: SyscallGuard records specifications, evidence, gaps, review gates, and coverage. Do not modify Starry or LTP sources from this skill unless the user explicitly asks for work outside the harness.
- Do not default to copying or committing external Starry/LTP source trees. Prefer source-index entries with repository path/URL, branch or tag, commit, captured paths, and hashes. Copy only a minimal evidence subset when the source cannot be restored reliably or review must be self-contained.
- Do not mark a batch `closed` unless all closeout gates pass.

## High-Level Guide Commands

Treat only these prefixed Chinese phrases as first-class guide commands. Accept both the full-width `命令：` and half-width `命令:` prefixes as input, but always use the full-width `命令：` form in assistant prompts and suggested inputs:

- `命令：开始检查系统调用`: start or continue the syscall-oriented batch flow at step `01-scope-selection`; first show progress and the default 20 unchecked syscall candidates.
- `命令：批准进入下一步`: inspect the previous step's sign-off gate and proceed only if the relevant review status is `confirmed` or `not_applicable`.
- `命令：检查当前进度`: read only `manifest.yaml`, `steps/`, `reviews/`, and `outputs/coverage-matrix.yaml`; do not create, update, or confirm any artifacts. Prefer:

```bash
python3 skills/syscallguard-flow/scripts/progress.py --batch batches/<batch-id>
```

Then summarize the ten fixed steps, each report/sign-off state, the current step, the next executable step, any blocking review gate, and the next suggested user input. If all ten sign-offs are resolved, report that there is no next suggested input instead of suggesting another progress check.
- `命令：执行第X步`: execute exactly the numbered step `X`, where `X` must be 1 through 10. If `X` is outside 1 through 10, do not execute a step; say the legal range is `命令：执行第1步` through `命令：执行第10步`.

If the user issues a bare `开始检查系统调用`, `批准进入下一步`, `检查当前进度`, or `执行第X步` as a guide command, do not execute the workflow. Prompt with the corresponding full-width prefixed form. This restriction applies only to these four high-level guide commands; natural-language questions or discussion about the workflow remain allowed.

Step number mapping:

| Command | Step ID |
| --- | --- |
| `命令：执行第1步` | `01-scope-selection` |
| `命令：执行第2步` | `02-spec-ingestion` |
| `命令：执行第3步` | `03-normalization-review` |
| `命令：执行第4步` | `04-checkability-classification` |
| `命令：执行第5步` | `05-starry-evidence-mapping` |
| `命令：执行第6步` | `06-static-check-or-audit` |
| `命令：执行第7步` | `07-gap-triage` |
| `命令：执行第8步` | `08-fix-plan-and-apply-outside-harness` |
| `命令：执行第9步` | `09-validation` |
| `命令：执行第10步` | `10-batch-closeout` |

For `命令：执行第X步`, never bypass review gates. Before executing the requested step, ensure every earlier step's sign-off is `confirmed` or `not_applicable`. If an earlier gate is `pending_human_review`, `changes_requested`, missing, or malformed, stop and tell the user to input `命令：批准进入下一步` after resolving the named review file, or to edit that review file first.

## Workflow

1. Resolve the batch path from the user's request. If no batch is named and exactly one `batches/<id>/manifest.yaml` exists, use it; otherwise ask for the batch ID.
2. For `命令：开始检查系统调用`, first run or emulate:

```bash
python3 skills/syscallguard-flow/scripts/next_syscalls.py list --limit 20
```

Then show the 20 syscall names and the files that will hold the scope result. Do this before any long-running inspection.
3. Load the batch state from `manifest.yaml`, `steps/`, `reviews/`, and `outputs/coverage-matrix.yaml` when it exists.
4. Determine the requested step:
   - `命令：检查当前进度` means read-only progress reporting only, preferably via `scripts/progress.py`.
   - `命令：执行第X步` means map `X` to the fixed step ID table above and run only that step after prior gate checks.
   - "current", "next", or "continue" means the first workflow step whose sign-off is absent, unresolved, or whose report needs work, after checking the previous step gate.
   - An explicit step ID means that step only. A numbered high-level command must use `命令：执行第X步`.
   - "closeout" means step `10-batch-closeout` plus closeout gate checks.
5. Read `references/ten-step-flow.md` for the selected step's inputs, outputs, checks, and stop condition.
6. Read `references/artifact-map.md` when creating or validating manifests, step reports, sign-off files, coverage matrices, batch reports, syscall history, or directory structure.
7. Create or update only the artifacts for the selected step. Use existing repository templates:
   - `templates/step-report.md`
   - `templates/review-signoff.yaml`
   - `templates/manifest.yaml` for new batches
8. Finish by reporting the step completed or blocked, the artifacts touched, and the exact sign-off file awaiting human confirmation.

## Progress Messages

- On entry, respond within the first message with the current step and candidate syscall list. Do not wait until all analysis is complete.
- Before reading many files or running scripts, say what is being checked and which artifact will be produced.
- When a step finishes, show a screen review block in chat and wait for `命令：批准进入下一步`.
  The review block must first list the concrete items produced or checked by that step, then list what
  the user should confirm about those items. For step 01, list the selected syscall names, then ask only
  `是否同意处理这一批系统调用？`; do not add other confirmation questions. Show both Step 01 response paths:
  `命令：批准进入下一步` for approval and `修改：<调整内容>` for rejection or changes. Do not use numbered
  modification syntax for Step 01. Step 06 lists the audited rule/syscall groups before asking
  whether the audit scope, evidence refs, and result labels are acceptable.
- For Step 02, list the investigated specification sources and missing materials, then ask only
  `对这批系统调用规格来源的调查结果是否接受？`. Show `命令：批准进入下一步` for approval and
  `修改：<调整内容>` for rejection or changes. Do not use numbered modification syntax for Step 02.
- For Step 03, briefly list the normalized syscall rule references, reusable rules, and target mappings,
  then ask only `对这批系统调用检查规则的整理结果是否接受？`. Show `命令：批准进入下一步`
  for approval and `修改：<调整内容>` for rejection or changes. Do not use numbered modification syntax for Step 03.
- For Step 04, briefly summarize the checkability classifications, then ask only
  `是否同意对这些检查规则的分类？`. Show `命令：批准进入下一步` for approval and
  `修改：<调整内容>` for rejection or changes. Do not use numbered modification syntax for Step 04.
- Treat `命令：批准进入下一步` as permission to check the previous sign-off gate and proceed only if it is resolved.
- After step `10-batch-closeout` is confirmed for a syscall-oriented batch, record history with:

```bash
python3 skills/syscallguard-flow/scripts/next_syscalls.py record --batch batches/<id>
```

## Gate Handling

- Treat these sign-off statuses as resolved: `confirmed`, `not_applicable`.
- Treat these statuses as unresolved: `pending_human_review`, `changes_requested`, missing sign-off, malformed sign-off.
- For "continue next step", never skip over an unresolved prior sign-off.
- For "check whether this batch can close", run or emulate:

```bash
python3 skills/syscallguard-flow/scripts/check_batch.py batches/<id>
```

Report the closeout result in Chinese. If the batch is not closeable, list the blocking review files, missing coverage, or triage gaps.

## Closeout Rules

A batch can be marked `closed` only when all of these are true:

- The manifest workflow lists all ten fixed steps in order.
- All ten step reports exist.
- All ten sign-off files exist and are `confirmed` or `not_applicable`.
- Every scoped behavior appears exactly once in `outputs/coverage-matrix.yaml`.
- Every coverage row has source references and either Starry evidence or a recorded gap/risk/unsupported/needs_review triage.
- Every top-level gap or risk entry has a triage decision.

If any rule fails, leave the batch status unchanged and stop at the review gate.
