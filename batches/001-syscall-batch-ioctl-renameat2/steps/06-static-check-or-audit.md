# 步骤 06 - Static Check Or Audit

批次：`001-syscall-batch-ioctl-renameat2`
状态：`pending_human_review`

## 目的

对第 04 步标记为 `static` 和 `partial_static` 的 `syscall + rule_id` 项做静态人工审计。
本步只记录静态证据是否支持继续推进，不运行动态测试，不定性 `gap`、`risk` 或
`covered`。

## 输入

- `manifest.yaml`
- `inputs/source-index.yaml`
- `steps/04-checkability-classification.md`
- `steps/05-starry-evidence-mapping.md`
- 外部 Starry source ref：`tgoskits-local`，branch `dev-ltp-spec-2`，commit
  `4f30e12d17e4da175233bb3a51889efe747a45f9`

## 审计方法

- 未发现可直接运行的仓库内 static checker；本步执行人工静态审计。
- 审计范围限定为 source index 登记的 external commit 文件，不复制 Starry 源码到本仓库。
- 主要审计文件：
  - `os/StarryOS/kernel/src/syscall/mod.rs`
  - `os/StarryOS/kernel/src/syscall/fs/ctl.rs`
  - `os/StarryOS/kernel/src/mm/access.rs`
  - `os/StarryOS/kernel/src/file/fs.rs`
  - `os/StarryOS/kernel/src/file/mod.rs`

## Source Refs

| Ref | Evidence |
| --- | --- |
| `syscall_dispatch` | `syscall/mod.rs`; sha256 `0abe6a7c907f27e4be5013cad243cbf159edddd851d801530b60710103af344f` |
| `syscall_fs_ctl` | `syscall/fs/ctl.rs`; sha256 `17bad888fff91bad602afbfae77ae880a1ee6d1b4cba12d1b560f00e0d02904e` |
| `mm_access` | `mm/access.rs`; sha256 `f8f26299218dc2c2a97329f426c2574ce4c218a771bee8fae4cb71d4ce6982b7` |
| `file_fs` | `file/fs.rs`; sha256 `868e194dee5abd23e083fbc0d981c31b0763778770a3a485191a3836a20087cf` |
| `file_mod` | `file/mod.rs`; sha256 `947f33b7804d97e7634818f94d78b594966c8884d7abd548a6ddf6dda2fe1dd4` |

## 静态审计结果

| Rule ID | Audit result | Evidence | Notes |
| --- | --- | --- | --- |
| `SYSCALL_ENTRY_ALIAS` | `static_audit_supports` | `syscall/mod.rs:84-127`; `ctl.rs:47`, `86`, `96`, `105`, `110`, `114`, `160`, `193`, `294`, `328`, `369`, `378`, `409`, `414`, `418`, `436`, `440`, `758`, `763`, `773` | 20 个 syscall 均有 dispatch 和 handler。Legacy wrappers 可见：`mkdir -> mkdirat`、`mknod -> mknodat`、`link -> linkat`、`rmdir/unlink -> unlinkat`、`symlink -> symlinkat`、`rename -> renameat -> renameat2`。 |
| `BAD_FD_EBADF` | `static_audit_supports_for_bad_fd` | `file/mod.rs:275-280`; `ctl.rs:49`, `64-68`, `99`, `299`; `file/fs.rs:28-35`, `341-345` | `get_file_like` 对 missing fd 返回 `BadFileDescriptor`；`ioctl`、`fchdir`、`getdents64` 的 fd 入口能到达该 helper 或 `Directory::from_fd`。fd 类型错误不在此规则完全关闭。 |
| `FD_TYPE_ERRNO` | `partial_static_audit_supports` | `file/fs.rs:252-272`, `341-345`; `ctl.rs:120-122`, `299`, `355-359` | `Directory::from_fd` 可区分非目录为 `NotADirectory`；`File::from_fd` 可区分目录和其他类型。完整 fd object 类型矩阵仍需要第 09 步动态样例。 |
| `FLAG_MASK_REJECTS_UNKNOWN` | `static_audit_supports` | `ctl.rs:335-337`, `386-387`, `780-782` | `linkat`、`unlinkat`、`renameat2` 对未知 flag bits 有直接拒绝路径。`ioctl` request 空间不是普通 flag mask，仍需后续规则细化。 |
| `PATH_LONG_ENAMETOOLONG` | `partial_static_audit_supports` | `mm/access.rs:296-301`; `ctl.rs:87`, `115`, `163`, `196`, `340-341`, `379`, `446`, `785-786` | path 参数普遍经 `vm_load_path_string`，该 helper 对长度达到 `PATH_MAX` 返回 `NameTooLong`。`symlinkat` 的 `target` 用 `vm_load_string`，这里只审计 `linkpath`。 |
| `PATH_RESOLUTION_ERRNO` | `partial_static_audit_supports` | `ctl.rs:90-92`, `118-121`, `175-184`, `222-224`, `355-362`, `391-397`, `452-454`, `792-807`; `file/fs.rs:59-94` | 路径解析由 `FsContext`、`resolve_at`、`with_fs` 和相关 VFS helper 承担。静态路径可定位，但 errno 优先级仍需动态样例确认。 |
| `DIRFD_AND_AT_FLAGS` | `partial_static_audit_supports` | `file/fs.rs:28-35`, `80-85`; `ctl.rs:160`, `193`, `328-337`, `378-387`, `440-454`, `763-807` | `with_fs` 和 `resolve_at` 处理 `AT_FDCWD`、dirfd 和绝对路径切换；`linkat`、`unlinkat`、`renameat2` 有显式 flag mask。跨 VFS 的绝对路径/dirfd errno 优先级仍需动态样例。 |
| `USERPTR_EFAULT` | `partial_static_audit_supports` | `ctl.rs:51`, `56`, `318`, `427-429`; `mm/access.rs:414-455` | `ioctl` 读用户指针，`getdents64` 和 `getcwd` 写用户 buffer，底层使用 VM read/write helper。具体 bad pointer errno 映射留给后续验证确认。 |
| `MODE_UID_GID_GUARD` | `partial_static_audit_supports` | `ctl.rs:166-170`, `202-227`, `232-237`, `449-454` | `mkdirat` 应用 umask、fsuid、fsgid；`mknodat` 拆分 file type/permission bits 并拒绝 `S_IFDIR` 和未知 type。权限结果仍属于动态矩阵。 |
| `VFS_PERMISSION` | `dynamic_deferred` | `ctl.rs` permission-sensitive handler paths located | 本步不运行 credential/search/readonly fs 场景。 |
| `FS_SIDE_EFFECT` | `dynamic_deferred` | `ctl.rs` create/delete/link/rename/cwd mutation paths located | 本步不验证运行时文件系统状态变化。 |
| `DIRENT_ENUMERATION` | `dynamic_deferred` | `ctl.rs:245-320` | 本步不验证目录项内容、record size 和 offset 语义。 |

## 按 syscall 的审计备注

| Syscall group | Static audit note |
| --- | --- |
| `ioctl` | `BAD_FD_EBADF`、`USERPTR_EFAULT` 和部分 request delegation 已定位；request 空间仍需专项拆分。 |
| `chdir`, `chroot` | pathname load、path resolve 和 cwd/root mutation 路径已定位；权限和副作用需动态验证。 |
| `fchdir` | dirfd 到 `Directory::from_fd` 的静态路径已定位；cwd 副作用需动态验证。 |
| `mkdir`, `mkdirat`, `mknod`, `mknodat` | legacy wrapper、path load、mode/uid/gid、type guard 路径已定位；创建副作用和权限需动态验证。 |
| `getdents64` | fd/type、directory read 和 user buffer write 路径已定位；目录项语义需动态验证。 |
| `link`, `linkat`, `unlink`, `unlinkat`, `rmdir` | legacy wrapper、flag mask、path/dirfd 和 mutation 路径已定位；link count、删除状态和权限需动态验证。 |
| `getcwd` | user buffer write 和 size handling 路径已定位；返回内容与 cwd 状态需动态验证。 |
| `symlink`, `symlinkat` | legacy wrapper、linkpath path load、uid/gid 创建路径已定位；target 字符串语义和副作用需动态验证。 |
| `rename`, `renameat`, `renameat2` | legacy wrapper、flag mask、path/dirfd 和 `RENAME_NOREPLACE` 分支已定位；rename 原子性和状态变化需动态验证。 |

## 输出

- 静态人工审计记录在本文件。
- 审核门禁：`reviews/06-static-check-or-audit-signoff.yaml`。

## 分类备注

- 本步没有运行构建、静态 checker 或动态测试。
- 本步没有修改 Starry/LTP 源码。
- `dynamic_deferred` 不是 gap/risk 结论，只表示该规则按第 04 步分类等待第 09 步运行时验证。
- `partial_static_audit_supports` 不是 closeout 结论；第 07 步再决定是否形成 gap/risk/needs_review。

## 审核

- Sign-off：`reviews/06-static-check-or-audit-signoff.yaml`
- 请确认静态审计范围和“支持/部分支持/动态延后”的边界是否合理；如认可，再进入第 07 步 gap triage。
