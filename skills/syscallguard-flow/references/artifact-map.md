# SyscallGuard Artifact Map

Use this reference when creating or validating batch files.

## Directory Shape

```text
batches/<batch-id>/
├── manifest.yaml
├── inputs/
│   └── source-index.yaml
├── steps/
│   ├── 01-scope-selection.md
│   └── ...
├── reviews/
│   ├── 01-scope-selection-signoff.yaml
│   └── ...
└── outputs/
    ├── coverage-matrix.yaml
    └── batch-report.md
batches/syscall-check-history.yaml
```

Snapshot paths such as `snapshots/ltp/...` are repository-root relative. Batch-local paths such as `steps/...`, `reviews/...`, `inputs/...`, and `outputs/...` are relative to `batches/<batch-id>/`. External source paths or URLs belong in `inputs/source-index.yaml`; do not add large external source trees to the manifest by default.

## Source Evidence Policy

Use `inputs/source-index.yaml` to record source evidence. Prefer immutable external references:

- source ID and kind;
- repository path or URL;
- branch, tag, and commit;
- captured paths;
- file hash when available;
- captured timestamp.

Only copy source files into `snapshots/` when the external source cannot be restored reliably, the review must be self-contained, or the copied file is a small evidence excerpt. Record the reason in the source index. For copied evidence, keep the subset minimal and avoid committing whole external source trees.

## Fixed Step IDs

1. `01-scope-selection`
2. `02-spec-ingestion`
3. `03-normalization-review`
4. `04-checkability-classification`
5. `05-starry-evidence-mapping`
6. `06-static-check-or-audit`
7. `07-gap-triage`
8. `08-fix-plan-and-apply-outside-harness`
9. `09-validation`
10. `10-batch-closeout`

For each step, the report path is `steps/<step-id>.md` and the review path is `reviews/<step-id>-signoff.yaml`.

## Manifest

Start new manifests from `templates/manifest.yaml`. Required top-level keys are:

- `batch_id`
- `title`
- `status`
- `created_at_utc`
- `scope`
- `workflow`
- `artifacts`

`workflow` must list all ten fixed steps in order. Each workflow item must include:

- `step_id`
- `report`
- `review`

`scope.included_behaviors` is the authoritative behavior set for closeout coverage.

For syscall-oriented batches, `scope.included_syscalls` may be used as the authoritative syscall list for the batch. Default to 20 entries. Keep syscall names as Starry `Sysno` names, for example `openat`, `read`, or `mmap`.

## Step Reports

Start reports from `templates/step-report.md`. Keep these sections unless a step has a stronger local convention:

- `目的`
- `输入`
- `执行内容`
- `输出`
- `缺口和风险`
- `审核`

The report status should reflect the batch state for that step, commonly `draft`, `ready_for_human_review`, or `closed`.

Step reports are batch evidence artifacts. Keep them focused on inputs, work performed, evidence,
outputs, and limitations. Do not add conversational review instructions, command prompts such as
"type approve", or general tool suitability discussion unless the tool was actually used to produce
or validate the step artifact. Put review guidance in the assistant response or human-review docs.

## Review Sign-Off

Start reviews from `templates/review-signoff.yaml`. Required fields are:

- `batch_id`
- `step_id`
- `artifact`
- `status`
- `reviewer`
- `reviewed_at_utc`
- `decision_summary`
- `required_changes`
- `follow_up`

Allowed review statuses:

- `pending_human_review`
- `confirmed`
- `changes_requested`
- `not_applicable`

When Codex creates a sign-off after completing a step, default to:

```yaml
status: "pending_human_review"
reviewer: ""
reviewed_at_utc: ""
required_changes: []
follow_up: []
```

Use `confirmed`, `changes_requested`, or `not_applicable` only when the user gives an explicit reviewer decision.

## Coverage Matrix

`outputs/coverage-matrix.yaml` must include:

- `batch_id`
- `generated_at_utc`
- `coverage`

Each coverage item must include:

- `behavior_id`
- `title`
- `source_refs`
- `checkability`
- `starry_evidence`
- `validation`
- `triage`
- `review_status`

Allowed `checkability` values:

- `static`
- `partial_static`
- `dynamic`
- `unsupported`
- `needs_review`

Allowed `triage` values:

- `covered`
- `covered_pending_human_review`
- `gap`
- `risk`
- `unsupported`
- `needs_review`

Coverage closeout requires `coverage.behavior_id` to match `manifest.scope.included_behaviors` exactly. Covered rows need source references and Starry evidence. Rows without Starry evidence must be triaged as `gap`, `risk`, `unsupported`, or `needs_review`.

For syscall-oriented batches, each coverage item should include one of these optional fields so results can be recorded without ambiguity:

- `syscall: "openat"` for a single syscall result.
- `syscalls: ["read", "write"]` for a behavior covering multiple syscalls.
- `rule_id: "PATH_LONG_ENAMETOOLONG"` for reusable check-rule coverage.
- `mapping_id: "M_PATHMAX"` when a target-specific mapping is evaluated.

For syscall-oriented batches, prefer `syscall + rule_id` over syscall-only coverage. A syscall may be partially covered when some rule refs remain unchecked. If neither syscall nor rule fields exist, history recording may fall back to `behavior_id`, but future syscall batches cannot use that row to exclude a syscall-rule pair.

## Syscall Check History

Use `batches/syscall-check-history.yaml` to prevent repeated work across batches. Create it when the first syscall batch is confirmed.

Suggested structure:

```yaml
schema_version: 1
updated_at_utc: "YYYY-MM-DDT00:00:00Z"
checked_syscalls:
  - syscall: "openat"
    status: "covered"
    batch_id: "NNN-short-name"
    result_ref: "batches/NNN-short-name/outputs/coverage-matrix.yaml#openat"
    reviewed_at_utc: "YYYY-MM-DDT00:00:00Z"
checked_syscall_rules:
  - syscall: "openat"
    rule_id: "PATH_LONG_ENAMETOOLONG"
    mapping_id: "M_PATHMAX"
    status: "covered"
    batch_id: "NNN-short-name"
    result_ref: "batches/NNN-short-name/outputs/coverage-matrix.yaml#openat-pathmax"
    reviewed_at_utc: "YYYY-MM-DDT00:00:00Z"
checked_behaviors: []
```

Allowed history statuses should reuse coverage triage values when possible:

- `covered`
- `covered_pending_human_review`
- `gap`
- `risk`
- `unsupported`
- `needs_review`

Only exclude a whole syscall from future candidate lists after all rule refs in the active rule set are human-reviewed and recorded. Otherwise exclude or skip only the reviewed `syscall + rule_id` pairs recorded in `checked_syscall_rules`.

Use the bundled script for routine updates after closeout review:

```bash
python3 skills/syscallguard-flow/scripts/next_syscalls.py record --batch batches/<batch-id>
```

The command refuses to record unless `reviews/10-batch-closeout-signoff.yaml` is `confirmed` or `not_applicable`. For pre-review experiments, use `--allow-unresolved` only when the user explicitly requests it.

## Closeout

Do not change `manifest.status` to `closed` until:

- all ten reports and sign-offs exist;
- all sign-offs are `confirmed` or justified `not_applicable`;
- every scoped behavior is represented exactly once in the coverage matrix;
- every coverage row and top-level gap/risk has triage;
- remaining risks are listed in `outputs/batch-report.md` or the step 10 report.
