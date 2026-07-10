# Step 09 - Validation

Batch: `000-regression-baseline`
Status: `ready_for_human_review`

## Purpose

Record validation evidence available to the harness.

## Available Validation Inputs

- Copied test sources:
  - `bugfix-bug-open-pathmax-no-enametoolong`
  - `syscall-test-pipe-syscalls`
  - `syscall-test-eventfd2`
  - `syscall-test-open-family`
  - `syscall-test-ltp-pilot-min`
  - `syscall-test-mmap-family`
  - `syscall-test-madvise`
  - `c-regression-test-mremap`
- Copied Starry implementation sources under `snapshots/ltp/starry-sources`.

## Harness Validation Result

No Starry build or QEMU test run was executed by this version of SyscallGuard.
Validation status is therefore recorded as `manual_audit_only` or `not_run` in
the coverage matrix, depending on behavior.

## Outputs

- `outputs/coverage-matrix.yaml`

## Gaps And Risks

- Fresh dynamic logs are required before marking dynamic behaviors fully
  confirmed.

