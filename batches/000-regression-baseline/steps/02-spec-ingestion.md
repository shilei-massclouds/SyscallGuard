# Step 02 - Spec Ingestion

Batch: `000-regression-baseline`
Status: `ready_for_human_review`

## Purpose

Import behavior specs from available local snapshots and record source versions.

## Inputs

- `snapshots/ltp/source-index.yaml`
- `snapshots/ltp/specs/regression-behavior-specs.yaml`
- `snapshots/ltp/test-sources/`
- `snapshots/ltp/starry-sources/`

## Work Performed

- Captured local `tgoskits` branch `dev-ltp-spec-2`.
- Captured local `tgoskits` commit
  `4f30e12d17e4da175233bb3a51889efe747a45f9`.
- Copied relevant test and Starry source files into `snapshots/ltp/`.
- Recorded unavailable LTP method, 100 syscall summary, and `new_specs/`
  materials as snapshot gaps.

## Outputs

- `inputs/source-index.yaml`
- `snapshots/ltp/source-index.yaml`
- `snapshots/ltp/specs/regression-behavior-specs.yaml`

## Gaps And Risks

- Behavior specs for this batch are hand-normalized from copied tests and Starry
  evidence. A future batch should replace or supplement them with upstream LTP
  four-layer specs when available.

