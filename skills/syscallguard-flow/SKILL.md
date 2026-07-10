---
name: syscallguard-flow
description: Orchestrate SyscallGuard's fixed ten-step batch workflow. Use when Codex needs to rehearse, create, inspect, advance, review, sign off, validate, or close out a SyscallGuard batch; determine the current or next step; enforce pending human review gates; check coverage matrices; or work with batch manifest files, steps, reviews, and outputs.
---

# SyscallGuard Flow

## Core Rules

- Use Chinese for user-facing explanations, review guidance, and gate messages. Keep paths, behavior IDs, field names, enum values, source excerpts, and command names unchanged.
- Read `README.md`, `docs/batch-process.md`, and the target batch `manifest.yaml` before changing batch artifacts.
- Process exactly one workflow step per user request. After producing or checking that step, stop at review sign-off and do not advance automatically.
- Before continuing to a later step, require the previous step sign-off status to be `confirmed` or a justified `not_applicable`. If it is `pending_human_review` or `changes_requested`, stop and tell the user which review file must be resolved.
- Write new or refreshed sign-off files with `status: "pending_human_review"` unless the user explicitly provides a reviewer decision.
- Preserve the harness boundary: SyscallGuard records specifications, evidence, gaps, review gates, and coverage. Do not modify Starry or LTP sources from this skill unless the user explicitly asks for work outside the harness.
- Do not mark a batch `closed` unless all closeout gates pass.

## Workflow

1. Resolve the batch path from the user's request. If no batch is named and exactly one `batches/<id>/manifest.yaml` exists, use it; otherwise ask for the batch ID.
2. Load the batch state from `manifest.yaml`, `steps/`, `reviews/`, and `outputs/coverage-matrix.yaml` when it exists.
3. Determine the requested step:
   - "current", "next", or "continue" means the first workflow step whose sign-off is absent, unresolved, or whose report needs work, after checking the previous step gate.
   - An explicit step number or step ID means that step only.
   - "closeout" means step `10-batch-closeout` plus closeout gate checks.
4. Read `references/ten-step-flow.md` for the selected step's inputs, outputs, checks, and stop condition.
5. Read `references/artifact-map.md` when creating or validating manifests, step reports, sign-off files, coverage matrices, batch reports, or directory structure.
6. Create or update only the artifacts for the selected step. Use existing repository templates:
   - `templates/step-report.md`
   - `templates/review-signoff.yaml`
   - `templates/manifest.yaml` for new batches
7. Finish by reporting the step completed or blocked, the artifacts touched, and the exact sign-off file awaiting human confirmation.

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
