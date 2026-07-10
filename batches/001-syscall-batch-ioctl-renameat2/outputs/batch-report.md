# Batch Report - 001-syscall-batch-ioctl-renameat2

Status: not closed

## Summary

- Scoped syscalls: 20
- Starry patch candidates from Step 09: 0
- Starry patches applied in Step 10: 0
- Dynamic validation cases: 7
- Dynamic validation executed: 0
- Dynamic validation blocked: 7
- Coverage result: all scoped syscalls remain `risk` or `needs_review`

## Closeout Decision

The batch is not eligible for `closed`.

Reasons:

- Step 09 produced no Starry patch candidates.
- All dynamic validation cases were blocked because no runnable command or environment binding was registered.
- Runtime risks from Step 07 remain unresolved.
- `ioctl` request split, source/spec basis, and automated static checker coverage remain `needs_review`.

## Outputs

- Coverage matrix: `outputs/coverage-matrix.yaml`
- Validation results: `outputs/validation-results.yaml`
- Starry patch candidates: `outputs/starry-patch-candidates.yaml`
- Step 10 report: `steps/10-batch-closeout.md`
