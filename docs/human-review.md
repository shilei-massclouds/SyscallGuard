# Human Review

Human review is the primary quality gate for version 1. Automation may prepare
artifacts, but acceptance requires an explicit review record.

## Required Fields

Each sign-off file records:

- `batch_id`
- `step_id`
- `artifact`
- `status`
- `reviewer`
- `reviewed_at`
- `decision_summary`
- `required_changes`
- `follow_up`

## Status Semantics

- `pending_human_review`: default state for new artifacts.
- `confirmed`: accepted for this batch.
- `changes_requested`: blocked until the listed changes are addressed.
- `not_applicable`: skipped by policy with a written justification.

## Reviewer Checklist

- Inputs match the batch manifest and source index.
- Behavior statements are precise enough to be tested or audited.
- Evidence paths and commits are concrete.
- Unsupported or uncertain behavior is triaged, not hidden.
- The coverage matrix matches the final step reports.

