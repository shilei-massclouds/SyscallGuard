# 步骤 04 - Checkability Classification

批次：`001-syscall-batch-ioctl-renameat2`
状态：`pending_human_review`

## 目的

按第 03 步的 `syscall + rule_id` 粒度分类可检查性。分类只表示后续证据采集方式，
不表示当前已经 pass，也不继承 `~/gitStudy/ltp` 中任何已有审计结论。

## 输入

- `manifest.yaml`
- `steps/03-normalization-review.md`
- `inputs/source-index.yaml#inputs.syscall_dispatch`

## 执行内容

- 读取第 03 步的 syscall 引用表和 reusable rule 表。
- 将每个 `rule_id` 分类为静态直接检查、跨 helper 静态检查、部分静态、动态必需或
  需要人工拆分。
- 将规则分类汇总到每个 syscall，形成后续第 05 步证据映射的工作队列。

## Rule Checkability 表

| Rule ID | Checkability | 理由 |
| --- | --- | --- |
| `SYSCALL_ENTRY_ALIAS` | `static` | 可直接从 `syscall/mod.rs` dispatch 或 wrapper alias 关系检查。 |
| `BAD_FD_EBADF` | `static` | 可静态检查 fd lookup 与 `EBADF` 映射路径。 |
| `FD_TYPE_ERRNO` | `partial_static` | 可静态检查对象类型分支和 errno 集，但完整类型矩阵通常需要动态/专项补充。 |
| `FLAG_MASK_REJECTS_UNKNOWN` | `static` | 可静态检查 flag mask、`from_bits` 或显式拒绝路径。 |
| `PATH_LONG_ENAMETOOLONG` | `partial_static` | 可静态追踪 path loader 和 errno 映射，但依赖 helper contract。 |
| `PATH_RESOLUTION_ERRNO` | `partial_static` | 可静态追踪路径错误映射，复杂路径状态需动态补充。 |
| `DIRFD_AND_AT_FLAGS` | `partial_static` | 可静态检查 dirfd/flags 分支，完整路径解析语义需动态补充。 |
| `USERPTR_EFAULT` | `partial_static` | 可静态追踪用户内存 helper 和 `EFAULT` 映射，具体 bad pointer case 需动态抽样。 |
| `MODE_UID_GID_GUARD` | `partial_static` | mode/uid/gid 参数 guard 可静态审计，权限矩阵需动态验证。 |
| `VFS_PERMISSION` | `dynamic` | credential、search permission、readonly fs 等必须通过场景运行验证。 |
| `FS_SIDE_EFFECT` | `dynamic` | 创建、删除、rename、link count、目录内容等副作用必须通过运行时状态验证。 |
| `DIRENT_ENUMERATION` | `dynamic` | `getdents64` 的目录项内容、record size 和 offset 语义依赖运行时目录状态。 |

## Syscall 汇总表

| Syscall | Static / partial-static refs | Dynamic refs | 待细化规则 | 后续处理 |
| --- | --- | --- | --- | --- |
| `ioctl` | `SYSCALL_ENTRY_ALIAS`, `BAD_FD_EBADF`, `FD_TYPE_ERRNO`, `FLAG_MASK_REJECTS_UNKNOWN`, `USERPTR_EFAULT` | - | request 空间未拆分 | 先做入口/fd/flag/user pointer 审计；后续按 fd/request 增补规则。 |
| `chdir` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `FD_TYPE_ERRNO` | `FS_SIDE_EFFECT` | - | 静态先查入口、路径 guard、类型错误；cwd 副作用动态。 |
| `fchdir` | `SYSCALL_ENTRY_ALIAS`, `BAD_FD_EBADF`, `FD_TYPE_ERRNO` | `FS_SIDE_EFFECT` | - | 静态先查 fd/type；cwd 副作用动态。 |
| `chroot` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO` | `VFS_PERMISSION`, `FS_SIDE_EFFECT` | - | 静态先查路径 guard；权限和 root/cwd 副作用动态。 |
| `mkdir` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `MODE_UID_GID_GUARD` | `VFS_PERMISSION`, `FS_SIDE_EFFECT` | legacy alias 关系需确认 | 静态先查 alias/path/mode；创建副作用动态。 |
| `mkdirat` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `DIRFD_AND_AT_FLAGS`, `MODE_UID_GID_GUARD` | `VFS_PERMISSION`, `FS_SIDE_EFFECT` | - | 静态先查 dirfd/path/mode；创建副作用动态。 |
| `mknod` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `MODE_UID_GID_GUARD` | `VFS_PERMISSION`, `FS_SIDE_EFFECT` | supported node types 需确认 | 静态先查 alias/path/mode；节点类型和副作用动态/专项。 |
| `mknodat` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `DIRFD_AND_AT_FLAGS`, `MODE_UID_GID_GUARD` | `VFS_PERMISSION`, `FS_SIDE_EFFECT` | supported node types 需确认 | 静态先查 dirfd/path/mode；节点类型和副作用动态/专项。 |
| `getdents64` | `SYSCALL_ENTRY_ALIAS`, `BAD_FD_EBADF`, `FD_TYPE_ERRNO`, `USERPTR_EFAULT` | `DIRENT_ENUMERATION` | - | 静态先查 fd/type/user pointer；目录项内容动态。 |
| `link` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO` | `VFS_PERMISSION`, `FS_SIDE_EFFECT` | legacy alias 关系需确认 | 静态先查 alias/path；link count/权限动态。 |
| `linkat` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `DIRFD_AND_AT_FLAGS` | `VFS_PERMISSION`, `FS_SIDE_EFFECT` | - | 静态先查 dirfd/path/flags；link count/权限动态。 |
| `rmdir` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO` | `VFS_PERMISSION`, `FS_SIDE_EFFECT` | legacy alias 关系需确认 | 静态先查 alias/path；目录状态和权限动态。 |
| `unlink` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO` | `VFS_PERMISSION`, `FS_SIDE_EFFECT` | legacy alias 关系需确认 | 静态先查 alias/path；删除副作用和权限动态。 |
| `unlinkat` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `DIRFD_AND_AT_FLAGS` | `VFS_PERMISSION`, `FS_SIDE_EFFECT` | - | 静态先查 dirfd/path/flags；删除副作用和权限动态。 |
| `getcwd` | `SYSCALL_ENTRY_ALIAS`, `USERPTR_EFAULT` | `FS_SIDE_EFFECT` | cwd string ABI 需确认 | 静态先查入口和用户 buffer；cwd 字符串内容动态。 |
| `symlink` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO` | `VFS_PERMISSION`, `FS_SIDE_EFFECT` | legacy alias 关系需确认 | 静态先查 alias/path；target 内容和父目录权限动态。 |
| `symlinkat` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `DIRFD_AND_AT_FLAGS` | `VFS_PERMISSION`, `FS_SIDE_EFFECT` | - | 静态先查 dirfd/path；target 内容和父目录权限动态。 |
| `rename` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO` | `VFS_PERMISSION`, `FS_SIDE_EFFECT` | legacy alias 关系需确认 | 静态先查 alias/path；rename 原子性和副作用动态。 |
| `renameat` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `DIRFD_AND_AT_FLAGS` | `VFS_PERMISSION`, `FS_SIDE_EFFECT` | - | 静态先查 dirfd/path；rename 副作用动态。 |
| `renameat2` | `SYSCALL_ENTRY_ALIAS`, `PATH_LONG_ENAMETOOLONG`, `PATH_RESOLUTION_ERRNO`, `DIRFD_AND_AT_FLAGS`, `FLAG_MASK_REJECTS_UNKNOWN` | `VFS_PERMISSION`, `FS_SIDE_EFFECT` | `RENAME_*` 语义需专项 | 静态先查 flags/path/dirfd；flag 语义和副作用动态/专项。 |

## 工作队列

第 05 步证据映射应按下面顺序处理：

1. `static` 规则：先找 dispatch、alias、fd lookup、flag mask 的 Starry 证据。
2. `partial_static` 规则：找 helper contract、errno map、dirfd/path/mode guard 证据，同时保留动态补充需求。
3. `dynamic` 规则：不要求静态关闭；先记录需要的动态测试场景。
4. 待细化规则：`ioctl` request 空间、legacy alias、节点类型、`renameat2` flags 语义需要人工拆分或补充规则；这些不是 gap/risk 结论。

## 输出

- checkability 分类记录在本文件。
- 后续 coverage matrix 应按 `syscall + rule_id` 写入分类结果。
- 审核门禁：`reviews/04-checkability-classification-signoff.yaml`。

## 分类备注

- 当前分类是工作队列分类，不是 pass/fail 结论。
- `ioctl` 粒度仍不足，应在后续 review 中决定是否拆成设备/request 子规则。
- 动态规则数量较多；第 04 步只标记它们需要运行时验证，不定性为 gap 或 risk。
- `gap`、`risk`、`covered`、`covered_pending_human_review` 等 triage 结论保留到第 07 步以后。

## 审核

- Sign-off：`reviews/04-checkability-classification-signoff.yaml`
- 请确认分类粒度和动态/静态边界是否合理；如认可，再进入 Starry 证据映射。
