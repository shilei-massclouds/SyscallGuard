# Step 04 - Checkability Classification

Batch: `000-regression-baseline`
Status: `ready_for_human_review`

## Purpose

Classify each behavior by how SyscallGuard can check it in version 1.

## Classification

| Behavior | Checkability | Rationale |
| --- | --- | --- |
| `path-max-enametoolong` | `partial_static` | Static path length guard plus copied dynamic regression test. |
| `pipe2-copyout-fd-rollback` | `partial_static` | Code audit can see rollback; fd leak still benefits from dynamic validation. |
| `x86-creat-alias` | `partial_static` | Dispatch and helper are static; test checks mode and fd behavior. |
| `x86-eventfd-alias` | `partial_static` | Dispatch and helper are static; eventfd2 behavior is dynamic. |
| `mmap04-visible-prot` | `dynamic` | Requires observing `/proc/self/maps`. |
| `p2-iov-guard` | `static` | Guard logic is local and source-readable. |
| `p2-offset-guard` | `static` | Guard logic is local and source-readable. |
| `p2-mremap-guard` | `partial_static` | Static guard plus broad regression test. |
| `p2-mincore-guard` | `static` | Guard logic is local and source-readable. |
| `p2-madvise-guard` | `partial_static` | Static guard plus copied regression test. |

## Outputs

- Checkability values in `outputs/coverage-matrix.yaml`.

## Gaps And Risks

- Dynamic commands were not run by this harness version.

