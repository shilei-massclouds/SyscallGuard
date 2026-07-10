# 步骤 05 - Starry Evidence Mapping

批次：`000-regression-baseline`
状态：`ready_for_human_review`

## 目的

将归一化行为映射到复制的 Starry 实现或测试证据。

## 证据映射

| 行为 | 证据 |
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

## 输出

- 证据引用已写入 `outputs/coverage-matrix.yaml`。

## 缺口和风险

- 证据来自本地复制快照，不是不可变的上游 release tag。
