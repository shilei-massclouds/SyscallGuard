# Step 05 - Starry Evidence Mapping

Batch: `000-regression-baseline`
Status: `ready_for_human_review`

## Purpose

Map normalized behaviors to copied Starry implementation or test evidence.

## Evidence Map

| Behavior | Evidence |
| --- | --- |
| `path-max-enametoolong` | `snapshots/ltp/starry-sources/mm/access.rs`; `bugfix-bug-open-pathmax-no-enametoolong` |
| `pipe2-copyout-fd-rollback` | `snapshots/ltp/starry-sources/syscall/fs/pipe.rs`; `syscall-test-pipe-syscalls` |
| `x86-creat-alias` | `snapshots/ltp/starry-sources/syscall/mod.rs`; `syscall/fs/fd_ops.rs`; `syscall-test-open-family` |
| `x86-eventfd-alias` | `snapshots/ltp/starry-sources/syscall/mod.rs`; `syscall/fs/event.rs`; `syscall-test-eventfd2` |
| `mmap04-visible-prot` | `snapshots/ltp/starry-sources/syscall/mm/mmap.rs`; `pseudofs/proc.rs`; `syscall-test-ltp-pilot-min` |
| `p2-iov-guard` | `snapshots/ltp/starry-sources/syscall/fs/io.rs` |
| `p2-offset-guard` | `snapshots/ltp/starry-sources/syscall/fs/io.rs`; `syscall/mm/mmap.rs` |
| `p2-mremap-guard` | `snapshots/ltp/starry-sources/syscall/mm/mmap.rs`; `c-regression-test-mremap` |
| `p2-mincore-guard` | `snapshots/ltp/starry-sources/syscall/mm/mincore.rs` |
| `p2-madvise-guard` | `snapshots/ltp/starry-sources/syscall/mm/mmap.rs`; `syscall-test-madvise` |

## Outputs

- Evidence references copied into `outputs/coverage-matrix.yaml`.

## Gaps And Risks

- Evidence is from local copied snapshots, not immutable upstream release tags.

