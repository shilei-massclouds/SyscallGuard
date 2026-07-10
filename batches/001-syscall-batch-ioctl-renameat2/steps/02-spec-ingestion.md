# 步骤 02 - Spec Ingestion

批次：`001-syscall-batch-ioctl-renameat2`
状态：`pending_human_review`

## 目的

记录本批 20 个 syscall 的可用来源快照、导入材料和来源缺口。本步只确认输入材料，
不判断 syscall 语义是否正确。

## 输入

- `manifest.yaml`
- `inputs/source-index.yaml`
- `snapshots/ltp/source-index.yaml`
- `snapshots/ltp/starry-sources/syscall/mod.rs`
- `snapshots/ltp/test-sources`
- `batches/syscall-check-history.yaml`

## 执行内容

- 读取 `snapshots/ltp/source-index.yaml`，确认当前快照为
  `ltp-starry-local-2026-07-10`。
- 读取 `snapshots/ltp/starry-sources/syscall/mod.rs`，确认本批 20 个 syscall 在
  Starry dispatch 中存在。
- 检查 `batches/syscall-check-history.yaml`，确认当前不存在历史记录文件。
- 搜索现有 `snapshots/ltp/test-sources`，未找到针对本批 20 个 syscall 的完整专用
  LTP/spec 测试集；仅发现 `syscall-test-open-family/src/open_path.c` 中提到
  `ioctl(2)` 作为 EBADF 示例引用。
- 记录缺失材料：独立 LTP 方法文档、100 syscall 摘要、`new_specs` 四层规格、本批
  syscall 的完整规范化行为文件。

## 导入来源

| 来源 | 状态 | 用途 |
| --- | --- | --- |
| `snapshots/ltp/source-index.yaml` | available | 快照 ID、来源仓库、缺失材料记录 |
| `snapshots/ltp/starry-sources/syscall/mod.rs` | available | 本批 syscall dispatch 入口 |
| `snapshots/ltp/test-sources` | partial | 仅提供已有测试源码快照，不覆盖本批全部 syscall |
| `batches/syscall-check-history.yaml` | missing | 当前没有历史检查结果可排除 |
| `snapshots/ltp/specs/regression-behavior-specs.yaml` | available but not authoritative for this batch | 现有 baseline 行为规格，不覆盖本批 20 个 syscall 范围 |

## Dispatch 映射

| Syscall | Dispatch 证据 |
| --- | --- |
| `ioctl` | `snapshots/ltp/starry-sources/syscall/mod.rs:84` -> `sys_ioctl` |
| `chdir` | `snapshots/ltp/starry-sources/syscall/mod.rs:85` -> `sys_chdir` |
| `fchdir` | `snapshots/ltp/starry-sources/syscall/mod.rs:86` -> `sys_fchdir` |
| `chroot` | `snapshots/ltp/starry-sources/syscall/mod.rs:87` -> `sys_chroot` |
| `mkdir` | `snapshots/ltp/starry-sources/syscall/mod.rs:89` -> `sys_mkdir` |
| `mkdirat` | `snapshots/ltp/starry-sources/syscall/mod.rs:90` -> `sys_mkdirat` |
| `mknod` | `snapshots/ltp/starry-sources/syscall/mod.rs:92` -> `sys_mknod` |
| `mknodat` | `snapshots/ltp/starry-sources/syscall/mod.rs:93` -> `sys_mknodat` |
| `getdents64` | `snapshots/ltp/starry-sources/syscall/mod.rs:99` -> `sys_getdents64` |
| `link` | `snapshots/ltp/starry-sources/syscall/mod.rs:101` -> `sys_link` |
| `linkat` | `snapshots/ltp/starry-sources/syscall/mod.rs:102` -> `sys_linkat` |
| `rmdir` | `snapshots/ltp/starry-sources/syscall/mod.rs:110` -> `sys_rmdir` |
| `unlink` | `snapshots/ltp/starry-sources/syscall/mod.rs:112` -> `sys_unlink` |
| `unlinkat` | `snapshots/ltp/starry-sources/syscall/mod.rs:113` -> `sys_unlinkat` |
| `getcwd` | `snapshots/ltp/starry-sources/syscall/mod.rs:114` -> `sys_getcwd` |
| `symlink` | `snapshots/ltp/starry-sources/syscall/mod.rs:116` -> `sys_symlink` |
| `symlinkat` | `snapshots/ltp/starry-sources/syscall/mod.rs:117` -> `sys_symlinkat` |
| `rename` | `snapshots/ltp/starry-sources/syscall/mod.rs:119` -> `sys_rename` |
| `renameat` | `snapshots/ltp/starry-sources/syscall/mod.rs:121` -> `sys_renameat` |
| `renameat2` | `snapshots/ltp/starry-sources/syscall/mod.rs:127` -> `sys_renameat2` |

## 输出

- 来源导入记录写入本文件。
- 审核门禁：`reviews/02-spec-ingestion-signoff.yaml`。

## 缺口和风险

- 本批缺少权威 syscall 语义规格输入；后续第 03 步需要基于可用快照先形成规范化草案，
  并把权威来源缺口保留为 risk。
- 当前 Starry 源码快照未包含这些 syscall 具体实现所在文件，只包含 dispatch 入口；
  后续第 05 步证据映射可能需要补充 Starry 实现快照或记录证据 gap。
- 缺少历史检查文件，不影响本批启动，但会影响跨批去重的可靠性。

## 审核

- Sign-off：`reviews/02-spec-ingestion-signoff.yaml`
- 请确认这些来源和缺口记录是否准确；如有额外规格或测试来源，请先补到输入快照或在本文件中记录。
