# Step 03 - Normalization Review

Batch: `000-regression-baseline`
Status: `ready_for_human_review`

## Purpose

Check that imported behavior statements are precise enough for classification
and evidence mapping.

## Inputs

- `snapshots/ltp/specs/regression-behavior-specs.yaml`

## Normalization Decisions

- Architecture-specific aliases are scoped to `x86_64`.
- Error-return behaviors retain expected errno names.
- `pipe2-copyout-fd-rollback` keeps both externally visible `EFAULT` and the
  internal fd rollback requirement.
- `mmap04-visible-prot` is scoped to `/proc/self/maps` visible permissions,
  not to hardware page-table permissions.
- P2 guard entries are split by area: iov, offset, mremap, mincore, madvise.

## Outputs

- Normalized behavior records remain in
  `snapshots/ltp/specs/regression-behavior-specs.yaml`.

## Gaps And Risks

- No upstream spec reviewer has confirmed the hand-normalized records yet.

