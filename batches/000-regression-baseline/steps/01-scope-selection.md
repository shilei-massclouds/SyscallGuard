# Step 01 - Scope Selection

Batch: `000-regression-baseline`
Status: `ready_for_human_review`

## Purpose

Select a process-baseline scope using already repaired Starry syscall
regressions. This batch is not intended to discover new gaps.

## Inputs

- `manifest.yaml`
- `inputs/source-index.yaml`
- `snapshots/ltp/specs/regression-behavior-specs.yaml`

## Selected Behaviors

- `path-max-enametoolong`
- `pipe2-copyout-fd-rollback`
- `x86-creat-alias`
- `x86-eventfd-alias`
- `mmap04-visible-prot`
- `p2-iov-guard`
- `p2-offset-guard`
- `p2-mremap-guard`
- `p2-mincore-guard`
- `p2-madvise-guard`

## Exclusions

- New syscall gap discovery.
- Direct Starry or LTP code changes.
- Automated CLI/checker implementation.

## Outputs

- Scope recorded in `manifest.yaml`.
- Review gate: `reviews/01-scope-selection-signoff.yaml`.

## Gaps And Risks

- Independent LTP and `new_specs/` inputs were not present locally. This is
  recorded as a snapshot gap, not a batch blocker for this process baseline.

