# 步骤 05 - Starry Evidence Mapping

批次：`001-syscall-batch-ioctl-renameat2`
状态：`pending_human_review`

## 目的

按第 04 步的 `syscall + rule_id` 工作队列，定位 Starry 证据。本步只做证据映射：
记录证据可定位、需要静态审计、需要动态测试或需要规则细化；不在本步定性 `gap`、
`risk` 或 `covered`。

## 输入

- `manifest.yaml`
- `inputs/source-index.yaml`
- `steps/03-normalization-review.md`
- `steps/04-checkability-classification.md`
- 外部 Starry source ref：`tgoskits-local`，branch `dev-ltp-spec-2`，commit
  `4f30e12d17e4da175233bb3a51889efe747a45f9`

## 执行内容

- 从 source index 读取外部 Starry dispatch 源文件：
  `/home/cloud/gitLinux/tgoskits/os/StarryOS/kernel/src/syscall/mod.rs`。
- 定位本批 20 个 syscall 的 dispatch 入口。
- 在外部 Starry 源码中定位这些 syscall 的具体 handler：
  `os/StarryOS/kernel/src/syscall/fs/ctl.rs`。
- 搜索通用 helper 证据：path loader、用户指针 helper、fd helper、flag mask pattern。
- 未运行动态测试；动态规则仅记录为 `dynamic_artifact_required`。

## Source Refs

| Ref | Kind | Evidence |
| --- | --- | --- |
| `syscall_dispatch` | `external_commit` | `os/StarryOS/kernel/src/syscall/mod.rs`; sha256 `0abe6a7c907f27e4be5013cad243cbf159edddd851d801530b60710103af344f` |
| `syscall_fs_ctl` | `external_commit` | `os/StarryOS/kernel/src/syscall/fs/ctl.rs`; sha256 `17bad888fff91bad602afbfae77ae880a1ee6d1b4cba12d1b560f00e0d02904e` |
| `mm_access` | `external_commit` | `os/StarryOS/kernel/src/mm/access.rs`; sha256 `f8f26299218dc2c2a97329f426c2574ce4c218a771bee8fae4cb71d4ce6982b7` |
| `fs_fd_ops` | `external_commit` | `os/StarryOS/kernel/src/syscall/fs/fd_ops.rs`; sha256 `4b500524f8f906373cf501c404ea25be1ba8771f55b60fd420d21e3ac95cd841` |
| `fs_io` | `external_commit` | `os/StarryOS/kernel/src/syscall/fs/io.rs`; sha256 `b9e10af30a6666c2862ad30987365afba0f5ef1f24e643de9528fd12f1acb731` |

## Dispatch 和 Handler 证据

| Syscall | Dispatch evidence | Handler evidence |
| --- | --- | --- |
| `ioctl` | `syscall/mod.rs:84` -> `sys_ioctl` | `syscall/fs/ctl.rs:47` |
| `chdir` | `syscall/mod.rs:85` -> `sys_chdir` | `syscall/fs/ctl.rs:86` |
| `fchdir` | `syscall/mod.rs:86` -> `sys_fchdir` | `syscall/fs/ctl.rs:96` |
| `chroot` | `syscall/mod.rs:87` -> `sys_chroot` | `syscall/fs/ctl.rs:114` |
| `mkdir` | `syscall/mod.rs:89` -> `sys_mkdir` | `syscall/fs/ctl.rs:105`; wrapper to `sys_mkdirat` |
| `mkdirat` | `syscall/mod.rs:90` -> `sys_mkdirat` | `syscall/fs/ctl.rs:160` |
| `mknod` | `syscall/mod.rs:92` -> `sys_mknod` | `syscall/fs/ctl.rs:110`; wrapper to `sys_mknodat` |
| `mknodat` | `syscall/mod.rs:93` -> `sys_mknodat` | `syscall/fs/ctl.rs:193` |
| `getdents64` | `syscall/mod.rs:99` -> `sys_getdents64` | `syscall/fs/ctl.rs:294` |
| `link` | `syscall/mod.rs:101` -> `sys_link` | `syscall/fs/ctl.rs:369`; wrapper to `sys_linkat` |
| `linkat` | `syscall/mod.rs:102` -> `sys_linkat` | `syscall/fs/ctl.rs:328` |
| `rmdir` | `syscall/mod.rs:110` -> `sys_rmdir` | `syscall/fs/ctl.rs:409`; wrapper to `sys_unlinkat` |
| `unlink` | `syscall/mod.rs:112` -> `sys_unlink` | `syscall/fs/ctl.rs:414`; wrapper to `sys_unlinkat` |
| `unlinkat` | `syscall/mod.rs:113` -> `sys_unlinkat` | `syscall/fs/ctl.rs:378` |
| `getcwd` | `syscall/mod.rs:114` -> `sys_getcwd` | `syscall/fs/ctl.rs:418` |
| `symlink` | `syscall/mod.rs:116` -> `sys_symlink` | `syscall/fs/ctl.rs:436`; wrapper to `sys_symlinkat` |
| `symlinkat` | `syscall/mod.rs:117` -> `sys_symlinkat` | `syscall/fs/ctl.rs:440` |
| `rename` | `syscall/mod.rs:119` -> `sys_rename` | `syscall/fs/ctl.rs:758`; wrapper to `sys_renameat` |
| `renameat` | `syscall/mod.rs:121` -> `sys_renameat` | `syscall/fs/ctl.rs:763`; wrapper to `sys_renameat2` |
| `renameat2` | `syscall/mod.rs:127` -> `sys_renameat2` | `syscall/fs/ctl.rs:773` |

## Rule 证据映射

| Rule ID | Evidence state | Starry evidence | Notes for later steps |
| --- | --- | --- | --- |
| `SYSCALL_ENTRY_ALIAS` | `dispatch_and_handler_located` | `syscall/mod.rs:84-127`; `syscall/fs/ctl.rs:47-773` | Legacy wrappers are visible for `mkdir`, `mknod`, `link`, `rmdir`, `unlink`, `symlink`, `rename`, and `renameat`; step 06 should audit wrapper equivalence. |
| `BAD_FD_EBADF` | `handler_path_located_static_audit_required` | `sys_ioctl` uses `get_file_like(fd)` and fd-table lookup; `sys_getdents64` uses `Directory::from_fd(fd)`; `sys_fchdir` uses `with_fs(dirfd, ...)` | Step 06 should audit exact errno mapping and priority for bad fd cases. |
| `FD_TYPE_ERRNO` | `handler_path_located_static_audit_required` | `sys_fchdir`, `sys_getdents64`, `sys_linkat`, `sys_chroot`, and helper paths distinguish fd/path object kinds | Type matrix is not closed by mapping alone; step 06 should audit reachable branches and step 09 may need dynamic samples. |
| `FLAG_MASK_REJECTS_UNKNOWN` | `direct_static_evidence_located` | `sys_linkat` rejects unknown flags at `ctl.rs:313-315`; `sys_unlinkat` at `ctl.rs:386-387`; `sys_renameat2` at `ctl.rs:780-782` | `ioctl` request space is not a simple flag mask and still needs rule refinement. |
| `PATH_LONG_ENAMETOOLONG` | `helper_contract_located` | path handlers call `vm_load_path_string`; `mm/access.rs:296-299` returns `AxError::NameTooLong` for long pathname | Step 06 should audit that each pathname parameter uses the helper and errno mapping is preserved. |
| `PATH_RESOLUTION_ERRNO` | `handler_path_located_static_audit_required` | handlers call `fs.resolve`, `resolve_at`, `resolve_parent`, `resolve_nonexistent`, `with_fs`, and related VFS helpers | Mapping is located but not yet triaged; exact errno priority needs step 06 audit and likely dynamic samples. |
| `DIRFD_AND_AT_FLAGS` | `handler_path_located_static_audit_required` | `sys_mkdirat`, `sys_mknodat`, `sys_linkat`, `sys_unlinkat`, `sys_symlinkat`, `sys_renameat`, and `sys_renameat2` expose dirfd/path handling | Illegal flag checks are direct for `linkat`, `unlinkat`, and `renameat2`; dirfd absolute-path behavior still needs audit. |
| `USERPTR_EFAULT` | `handler_and_helper_located_static_audit_required` | `sys_ioctl` uses `vm_read`; `sys_getdents64` and `sys_getcwd` use `vm_write_slice`; `mm/access.rs` defines user pointer helpers | Step 06 should audit EFAULT preservation for each user pointer path. |
| `MODE_UID_GID_GUARD` | `handler_path_located_static_audit_required` | `sys_mkdirat` applies `umask`, `fsuid`, and `fsgid`; `sys_mknodat` splits type/permission bits and rejects unsupported node types | Ownership/mode evidence exists; permission outcome still needs dynamic coverage. |
| `VFS_PERMISSION` | `dynamic_artifact_required` | Permission-sensitive handlers are located in `ctl.rs`, but no runtime permission matrix log is recorded | Step 09 needs dynamic tests or an explicit not-run limitation. |
| `FS_SIDE_EFFECT` | `dynamic_artifact_required` | Create/delete/link/rename/cwd handlers are located in `ctl.rs` | Step 09 needs runtime filesystem state checks. |
| `DIRENT_ENUMERATION` | `dynamic_artifact_required` | `DirBuffer` and `sys_getdents64` are located at `ctl.rs:233-315` | Directory entry contents, record size, and offset semantics need runtime scenarios. |

## Syscall-Rule 工作队列影响

- `SYSCALL_ENTRY_ALIAS`：本批 20 个 syscall 都有 dispatch 和 handler 证据；legacy wrapper 等价关系进入第 06 步审计。
- `PATH_*`、`DIRFD_AND_AT_FLAGS`、`MODE_UID_GID_GUARD`：handler 和 helper 证据已定位，但需要第 06 步确认 errno 优先级和 helper contract。
- `BAD_FD_EBADF`、`FD_TYPE_ERRNO`、`USERPTR_EFAULT`：相关 handler/helper 已定位；第 06 步应按 `syscall + rule_id` 审计具体路径。
- `VFS_PERMISSION`、`FS_SIDE_EFFECT`、`DIRENT_ENUMERATION`：本步只定位静态入口；仍需第 09 步动态测试或记录未运行。
- `ioctl` request 空间仍需规则细化；当前只记录入口、fd、request delegation、user pointer 相关证据。

## 输出

- Starry 证据映射记录在本文件。
- 审核门禁：`reviews/05-starry-evidence-mapping-signoff.yaml`。

## 待后续处理项

- 第 06 步静态审计应基于 external source refs，不要求复制 Starry 源码到本仓库。
- 第 07 步再对证据不足、规则不足或动态缺失做 `gap` / `risk` / `needs_review` triage。
- 第 09 步再登记动态测试或未运行限制。

## 审核

- Sign-off：`reviews/05-starry-evidence-mapping-signoff.yaml`
- 请确认证据定位和“已定位但未 triage”的边界是否合理；如认可，再进入第 06 步静态检查/人工审计。
