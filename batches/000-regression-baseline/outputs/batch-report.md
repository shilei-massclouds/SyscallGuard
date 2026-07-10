# Batch Report - 000 Regression Baseline

Status: `ready_for_human_review`
Generated: `2026-07-10T00:00:00Z`

## Scope

This batch establishes the first SyscallGuard process baseline using known
repaired Starry syscall regression items: `PATH_MAX`, pipe/pipe2 fd rollback,
x86_64 `creat` and `eventfd` aliases, mmap04-style visible prot, and P2 guard
items for iov, offsets, mremap, mincore, and madvise.

## Artifacts

- Manifest: `manifest.yaml`
- Source index: `inputs/source-index.yaml`
- Step reports: `steps/01-*.md` through `steps/10-*.md`
- Review records: `reviews/01-*-signoff.yaml` through
  `reviews/10-*-signoff.yaml`
- Coverage matrix: `outputs/coverage-matrix.yaml`

## Evidence

Evidence was copied from local `tgoskits` branch `dev-ltp-spec-2` at commit
`4f30e12d17e4da175233bb3a51889efe747a45f9`. The copied snapshot includes
relevant Starry system tests and implementation files.

## Results

- All scoped behaviors appear in the coverage matrix.
- Every coverage item traces to a behavior spec and Starry evidence.
- No new Starry gap is claimed.
- Missing upstream LTP/new_specs materials and missing fresh dynamic run logs
  are recorded as risks.

## Review State

The batch is ready for human review. All sign-off files currently have
`pending_human_review`; the batch must not be considered closed until those
records are resolved.

