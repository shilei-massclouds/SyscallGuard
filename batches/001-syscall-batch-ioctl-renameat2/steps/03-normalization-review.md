# 步骤 03 - Normalization Review

批次：`001-syscall-batch-ioctl-renameat2`
状态：`pending_human_review`

## 目的

将本批 20 个 syscall 归一化为可复用检查模型，而不是为每个 syscall 展开一份独立
草案。本步采用参考模型 `syscall -> check rule refs -> target mapping`，但不继承
`~/gitStudy/ltp` 中已有的处理进度或 pass/fix 结论。

## 输入

- `manifest.yaml`
- `steps/01-scope-selection.md`
- `steps/02-spec-ingestion.md`
- `snapshots/ltp/starry-sources/syscall/mod.rs`
- 参考模型：`~/gitStudy/ltp/syscalls-100-check-specs.zh.md`
- 参考模型：`~/gitStudy/ltp/new_specs/syscalls-100-spec-refs.yaml`
- 参考模型：`~/gitStudy/ltp/new_specs/ltp-check-specs.yaml`
- 参考模型：`~/gitStudy/ltp/new_specs/starry-target-mappings.yaml`

## 执行内容

- 保留第 01 步选出的 20 个 syscall。
- 参考 LTP `new_specs` 的结构，将归一化结果拆成：
  - syscall 引用表：每个 syscall 引用一组 `rule_refs`。
  - reusable check rule 表：每个 `rule_id` 只定义一次，可被多个 syscall 复用。
  - Starry target mapping 草案：只记录后续需要找的 Starry 证据类型，不继承参考项目的已完成状态。
- 将历史记录粒度从“syscall 已检查”调整为后续应记录 `syscall + rule_id` 或
  `syscall + rule_id + mapping_id`，避免未来新增规则时误跳过已出现过的 syscall。

## Syscall 引用表

| Syscall | Priority | Rule refs |
| --- | --- | --- |
| `ioctl` | `needs_review` | `SYSCALL_ENTRY_ALIAS`, `BAD_FD_EBADF`, `FD_TYPE_ERRNO`, `FLAG_MASK_REJECTS_UNKNOWN`, `USERPTR_EFAULT` |
| `chdir` | `P0_baseline` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `FD_TYPE_ERRNO`, `FS_SIDE_EFFECT` |
| `fchdir` | `P1_high_static` | `SYSCALL_ENTRY_ALIAS`, `BAD_FD_EBADF`, `FD_TYPE_ERRNO`, `FS_SIDE_EFFECT` |
| `chroot` | `P1_high_static` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `VFS_PERMISSION`, `FS_SIDE_EFFECT` |
| `mkdir` | `P1_high_static` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `MODE_UID_GID_GUARD`, `VFS_PERMISSION`, `FS_SIDE_EFFECT` |
| `mkdirat` | `P0_baseline` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `DIRFD_AND_AT_FLAGS`, `MODE_UID_GID_GUARD`, `VFS_PERMISSION`, `FS_SIDE_EFFECT` |
| `mknod` | `P1_high_static` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `MODE_UID_GID_GUARD`, `VFS_PERMISSION`, `FS_SIDE_EFFECT` |
| `mknodat` | `P1_high_static` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `DIRFD_AND_AT_FLAGS`, `MODE_UID_GID_GUARD`, `VFS_PERMISSION`, `FS_SIDE_EFFECT` |
| `getdents64` | `P0_baseline` | `SYSCALL_ENTRY_ALIAS`, `BAD_FD_EBADF`, `FD_TYPE_ERRNO`, `USERPTR_EFAULT`, `DIRENT_ENUMERATION` |
| `link` | `P1_high_static` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `FS_SIDE_EFFECT`, `VFS_PERMISSION` |
| `linkat` | `P0_baseline` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `DIRFD_AND_AT_FLAGS`, `FS_SIDE_EFFECT`, `VFS_PERMISSION` |
| `rmdir` | `P1_high_static` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `FS_SIDE_EFFECT`, `VFS_PERMISSION` |
| `unlink` | `P1_high_static` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `FS_SIDE_EFFECT`, `VFS_PERMISSION` |
| `unlinkat` | `P0_baseline` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `DIRFD_AND_AT_FLAGS`, `FS_SIDE_EFFECT`, `VFS_PERMISSION` |
| `getcwd` | `P0_baseline` | `SYSCALL_ENTRY_ALIAS`, `USERPTR_EFAULT`, `FS_SIDE_EFFECT` |
| `symlink` | `P1_high_static` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `FS_SIDE_EFFECT`, `VFS_PERMISSION` |
| `symlinkat` | `P0_baseline` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `DIRFD_AND_AT_FLAGS`, `FS_SIDE_EFFECT`, `VFS_PERMISSION` |
| `rename` | `P1_high_static` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `FS_SIDE_EFFECT`, `VFS_PERMISSION` |
| `renameat` | `P0_baseline` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `DIRFD_AND_AT_FLAGS`, `FS_SIDE_EFFECT`, `VFS_PERMISSION` |
| `renameat2` | `P1_high_static` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `DIRFD_AND_AT_FLAGS`, `FLAG_MASK_REJECTS_UNKNOWN`, `FS_SIDE_EFFECT`, `VFS_PERMISSION` |

## Reusable Check Rule 表

| Rule ID | Category | Expected / property | Default checkability |
| --- | --- | --- | --- |
| `SYSCALL_ENTRY_ALIAS` | entry | syscall 有可达 Starry dispatch 入口或明确 alias | `static_direct` |
| `BAD_FD_EBADF` | fd | invalid/closed fd 返回 `EBADF` | `static_direct` |
| `FD_TYPE_ERRNO` | fd | fd object type 不匹配返回 `ENOTDIR`、`EISDIR`、`ESPIPE`、`EINVAL` 或 `EBADF` | `static_interprocedural` |
| `FLAG_MASK_REJECTS_UNKNOWN` | flags | unknown flag bits 返回 `EINVAL` | `static_direct` |
| `PATH_LONG_ENAMETOOLONG` | pathname | pathname 长度达到或超过 `PATH_MAX` 返回 `ENAMETOOLONG` | `static_interprocedural` |
| `PATH_RESOLUTION_ERRNO` | pathname | missing path、component-not-directory、symlink loop 返回对应 errno | `static_interprocedural` |
| `DIRFD_AND_AT_FLAGS` | pathname | dirfd、absolute path、`AT_*` flags 按入口规则处理，非法 flags 返回 `EINVAL` | `static_interprocedural` |
| `USERPTR_EFAULT` | user_pointer | bad input/output pointer 返回 `EFAULT` | `static_interprocedural` |
| `MODE_UID_GID_GUARD` | ownership_mode | mode bits、uid/gid preserve、ownership flags 被校验 | `partial_static` |
| `VFS_PERMISSION` | permission | credential、search permission、readonly fs 等返回 `EACCES`、`EPERM` 或 `EROFS` | `dynamic_required` |
| `FS_SIDE_EFFECT` | filesystem_state | 创建、删除、rename、link count、目录内容等副作用符合 Linux 选定场景 | `dynamic_required` |
| `DIRENT_ENUMERATION` | directory_entries | `getdents64` 返回目录项内容、record size 和 offset 语义符合选定场景 | `dynamic_required` |

## Starry Target Mapping 草案

| Mapping ID | Source rules | 后续 Starry 证据需求 |
| --- | --- | --- |
| `M_ENTRY_DISPATCH` | `SYSCALL_ENTRY_ALIAS` | `snapshots/ltp/starry-sources/syscall/mod.rs` 中有 `Sysno::*` dispatch；legacy alias 需有 wrapper 等价关系。 |
| `M_PATHMAX` | `PATH_LONG_ENAMETOOLONG` | pathname 参数使用 `vm_load_path_string` 或等价 helper；`AxError::NameTooLong` 映射到 `ENAMETOOLONG`。 |
| `M_PATH_DIRFD_FLAGS` | `DIRFD_AND_AT_FLAGS`, `PATH_RESOLUTION_ERRNO` | handler 解析 dirfd/path/flags；非法 flags 返回 `EINVAL`；路径错误映射稳定。 |
| `M_FD_EBADF` | `BAD_FD_EBADF` | fd table lookup 在对象使用前发生；bad fd 映射 `EBADF`。 |
| `M_FD_TYPE` | `FD_TYPE_ERRNO` | helper 或 downcast 区分 file/directory/pipe/socket 等对象类型并返回稳定 errno。 |
| `M_FLAG_MASK` | `FLAG_MASK_REJECTS_UNKNOWN` | 使用 `from_bits` 或显式 mask；unsupported/mutually exclusive flags 有显式拒绝路径。 |
| `M_USERPTR_EFAULT` | `USERPTR_EFAULT` | 用户内存读写经 `vm_read`、`vm_write`、`UserPtr` 或等价 helper，错误映射 `EFAULT`。 |
| `DM_VFS_PERMISSION` | `VFS_PERMISSION` | 后续需要动态测试构造权限、credential、readonly fs 等场景。 |
| `DM_FS_SIDE_EFFECT` | `FS_SIDE_EFFECT` | 后续需要动态测试检查文件系统状态变化。 |
| `DM_DIRENT_ENUMERATION` | `DIRENT_ENUMERATION` | 后续需要动态测试检查目录项枚举内容和 offset。 |

## 归一化决策

- 本批第 03 步使用参考模型的结构和规则命名，但不继承参考项目的当前状态、fix commit
  或 pass/gap 结论。
- `ioctl` 不在参考 100 syscall refs 的当前表内，本批先按 `needs_review` 收敛到入口、
  fd、flag、user pointer 等通用规则；具体 request 空间需后续拆分或人工补充规则。
- `mkdir`、`mknod`、`link`、`rmdir`、`unlink`、`symlink`、`rename` 作为 legacy path
  syscall 保留在范围中；后续映射要检查其是否 alias 到对应 `*at` 现代入口。
- 第 04 步应按 rule 粒度分类 checkability，而不是按 syscall 单点分类。
- 第 05 步应映射 `syscall + rule_id` 到 Starry 证据或 gap。
- closeout/history 不能只记录 `checked_syscalls`；应记录 `checked_syscall_rules`，至少包含
  `syscall`、`rule_id`、`triage`、`batch_id`、`result_ref`。

## 输出

- 本步输出为两表/三层归一化模型，记录在本文件。
- 后续 coverage matrix 应至少包含 `syscall` 和 `rule_id` 字段。
- 审核门禁：`reviews/03-normalization-review-signoff.yaml`。

## 缺口和风险

- 当前 SyscallGuard 快照未复制 `~/gitStudy/ltp/new_specs`，本步只参考其模型，不把它登记为本批输入事实。
- `ioctl` 的规则拆分不足，后续很可能需要根据具体 fd/request 增补专项规则。
- 动态规则 `VFS_PERMISSION`、`FS_SIDE_EFFECT`、`DIRENT_ENUMERATION` 不能靠静态审计完全关闭。

## 审核

- Sign-off：`reviews/03-normalization-review-signoff.yaml`
- 请确认 syscall 引用表、可复用 rule 表和 Starry mapping 草案是否符合预期；如认可，再进入第 04 步 checkability 分类。
