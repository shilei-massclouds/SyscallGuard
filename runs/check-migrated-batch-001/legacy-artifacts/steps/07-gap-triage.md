# 步骤 07 - Gap Triage

批次：`001-syscall-batch-ioctl-renameat2`
状态：`pending_human_review`

## 目的

对第 05 步证据映射和第 06 步静态人工审计留下的未闭合项做 triage。
本步允许定性 `gap`、`risk`、`unsupported`、`needs_review`，但不运行动态测试，
不修改 Starry/LTP 源码，也不关闭批次。

## 输入

- `manifest.yaml`
- `steps/03-normalization-review.md`
- `steps/04-checkability-classification.md`
- `steps/05-starry-evidence-mapping.md`
- `steps/06-static-check-or-audit.md`

## Triage 总览

| ID | Triage | Affected scope | Closeout impact | Follow-up |
| --- | --- | --- | --- | --- |
| `T07-IOCTL-REQUEST-SPLIT` | `needs_review` | `ioctl` request-specific behavior | blocks full `ioctl` closeout | split request classes or exclusions |
| `T07-DYNAMIC-PERMISSION` | `risk` | permission-sensitive path mutation syscalls | blocks closeout unless validated or accepted | Step 09 permission matrix |
| `T07-DYNAMIC-FS-SIDE-EFFECT` | `risk` | cwd/root updates and filesystem mutations | blocks closeout unless validated or accepted | Step 09 filesystem state checks |
| `T07-DYNAMIC-DIRENT` | `risk` | `getdents64` enumeration semantics | blocks `getdents64` closeout unless validated or accepted | Step 09 directory enumeration checks |
| `T07-FD-TYPE-MATRIX` | `risk` | fd-bearing syscalls and wrong-fd-type errno paths | blocks closeout unless sampled or accepted | Step 09 fd type matrix |
| `T07-PATH-ERRNO-PRIORITY` | `risk` | pathname, dirfd, and `*at` errno ordering | blocks closeout unless sampled or accepted | Step 09 path errno samples |
| `T07-USERPTR-EFAULT` | `risk` | user pointer copy-in/copy-out paths | blocks closeout unless validated or accepted | Step 09 EFAULT samples |
| `T07-MODE-UID-GID` | `risk` | creation mode and ownership behavior | blocks closeout unless validated or accepted | Step 09 creation metadata samples |
| `T07-SOURCE-SPEC-GAP` | `needs_review` | all 20 syscalls | blocks final `closed` status until accepted or refreshed | future extractor/spec refresh |
| `T07-STATIC-CHECKER-GAP` | `needs_review` | static and partial-static rules | blocks automated-checker coverage claims | future checker integration |

本步没有形成 `unsupported` 结论，也没有形成需要立即修改 Starry/LTP 源码的 `gap` 结论。

## Triage 记录

### `T07-IOCTL-REQUEST-SPLIT`

- Triage：`needs_review`
- Affected syscalls：`ioctl`
- Related rules：`FD_TYPE_ERRNO`、`BAD_FD_EBADF`、`FLAG_MASK_REJECTS_UNKNOWN`、`USERPTR_EFAULT`
- Evidence state：第 06 步定位到 generic fd lookup、user pointer copy 和 request dispatch 证据。
- Gap/risk：`ioctl` request 空间比当前 syscall-level rule set 更宽，per-request 参数形状、errno 映射和副作用还没有拆分。
- Blocking decision：阻塞 `ioctl` 的完整 closeout，但不阻塞进入 Step 08/09。
- Follow-up：后续把 `ioctl` 拆成 request classes，或显式排除不支持的 request classes。

### `T07-DYNAMIC-PERMISSION`

- Triage：`risk`
- Affected syscalls：`chroot`、`mkdir`、`mkdirat`、`mknod`、`mknodat`、`link`、`linkat`、`rmdir`、`unlink`、`unlinkat`、`symlink`、`symlinkat`、`rename`、`renameat`、`renameat2`
- Related rule：`VFS_PERMISSION`
- Evidence state：第 06 步定位到 wrapper 和 VFS call paths，但未运行权限场景。
- Gap/risk：权限结果依赖 runtime credentials、目录权限、mount state 和现有 filesystem state。
- Blocking decision：阻塞 batch closeout，直到 Step 09 验证代表性权限样例，或明确接受该 limitation。
- Follow-up：为 create、remove、link、symlink、rename 和 root-changing paths 补动态权限样例。

### `T07-DYNAMIC-FS-SIDE-EFFECT`

- Triage：`risk`
- Affected syscalls：`chdir`、`fchdir`、`chroot`、`mkdir`、`mkdirat`、`mknod`、`mknodat`、`link`、`linkat`、`rmdir`、`unlink`、`unlinkat`、`getcwd`、`symlink`、`symlinkat`、`rename`、`renameat`、`renameat2`
- Related rule：`FS_SIDE_EFFECT`
- Evidence state：第 06 步定位到主要 mutation 或 state-return paths。
- Gap/risk：静态证据不能证明 observable runtime state transitions，例如 cwd 变化、目录项、link count、rename replacement 行为或 getcwd 返回内容。
- Blocking decision：阻塞 batch closeout，直到 Step 09 验证代表性副作用，或明确接受该 limitation。
- Follow-up：用动态检查观察每类 mutation 前后的 filesystem state。

### `T07-DYNAMIC-DIRENT`

- Triage：`risk`
- Affected syscalls：`getdents64`
- Related rule：`DIRENT_ENUMERATION`
- Evidence state：第 06 步定位到 directory read 和 user buffer write paths。
- Gap/risk：entry ordering、record length、d_type、repeated reads、small-buffer behavior 和 EOF behavior 需要 runtime validation。
- Blocking decision：阻塞 `getdents64` closeout，直到动态目录枚举行为被验证，或明确接受该 limitation。
- Follow-up：为 empty、single-entry、multi-entry 和 undersized-buffer directories 补 Step 09 样例。

### `T07-FD-TYPE-MATRIX`

- Triage：`risk`
- Affected syscalls：`ioctl`、`chdir`、`fchdir`、`getdents64`
- Related rules：`BAD_FD_EBADF`、`FD_TYPE_ERRNO`
- Evidence state：第 06 步定位到 bad-fd 或 fd-type handling paths；fd-type errno 仍是 partial static confidence。
- Gap/risk：regular files、directories、pipes、sockets、closed fds、invalid fds 的精确 errno 行为还没有动态采样。
- Blocking decision：阻塞 closeout，直到动态采样或明确接受该 limitation。
- Follow-up：为每个 fd-bearing syscall 补 Step 09 fd matrix cases。

### `T07-PATH-ERRNO-PRIORITY`

- Triage：`risk`
- Affected syscalls：`chdir`、`chroot`、`mkdir`、`mkdirat`、`mknod`、`mknodat`、`link`、`linkat`、`rmdir`、`unlink`、`unlinkat`、`symlink`、`symlinkat`、`rename`、`renameat`、`renameat2`
- Related rules：`PATH_LONG_ENAMETOOLONG`、`PATH_RESOLUTION_ERRNO`、`DIRFD_AND_AT_FLAGS`
- Evidence state：第 06 步定位到 path wrappers、dirfd handling 和 flag validation paths。
- Gap/risk：runtime errno priority 可能受 path length、missing components、non-directory components、trailing slash、dirfd validity 和 `*at` flag combinations 影响。
- Blocking decision：阻塞 closeout，直到代表性 errno-priority cases 被验证，或明确接受该 limitation。
- Follow-up：为 long paths、missing paths、non-directory parents、invalid dirfd 和 invalid `*at` flags 补 Step 09 样例。

### `T07-USERPTR-EFAULT`

- Triage：`risk`
- Affected syscalls：`ioctl`、`getcwd`、`getdents64`
- Related rule：`USERPTR_EFAULT`
- Evidence state：第 06 步定位到 user pointer copy paths。
- Gap/risk：null pointers、unmapped pointers、read-only output buffers 和 short buffers 的 runtime EFAULT 行为还没有验证。
- Blocking decision：阻塞 closeout，直到 bad-pointer behavior 被验证，或明确接受该 limitation。
- Follow-up：为 copy-in 和 copy-out paths 补 Step 09 EFAULT samples。

### `T07-MODE-UID-GID`

- Triage：`risk`
- Affected syscalls：`mkdir`、`mkdirat`、`mknod`、`mknodat`
- Related rule：`MODE_UID_GID_GUARD`
- Evidence state：第 06 步定位到 creation syscalls 的 mode 和 ownership source paths。
- Gap/risk：实际 mode masking、ownership assignment、special mode bits 和 device node behavior 依赖 runtime credentials 和 filesystem state。
- Blocking decision：阻塞 closeout，直到 creation metadata behavior 被验证，或明确接受该 limitation。
- Follow-up：为 mode、umask-sensitive behavior、uid/gid 和 device node constraints 补 Step 09 metadata samples。

### `T07-SOURCE-SPEC-GAP`

- Triage：`needs_review`
- Affected syscalls：全部 20 个 scoped syscalls
- Related rules：当前 draft rules
- Evidence state：本批次按从头开始处理，使用外部 LTP checkout 作为参考，不继承 `~/gitStudy/ltp/new_specs/` 的既有进度。
- Gap/risk：syscall/rule model 的 source-of-truth 状态还没有最终定稿。
- Blocking decision：阻塞最终 `closed` 状态，直到 reviewer 接受当前 reference basis，或后续 extractor/spec refresh 替换它。
- Follow-up：把 extractor-based workflow 作为未来 tooling，后续决定是否使用 `tools/syscall_spec_extract.py` 刷新 spec。

### `T07-STATIC-CHECKER-GAP`

- Triage：`needs_review`
- Affected syscalls：所有包含 `static` 或 `partial_static` 规则的 syscalls
- Related rules：`SYSCALL_ENTRY_ALIAS`、`BAD_FD_EBADF`、`FD_TYPE_ERRNO`、`FLAG_MASK_REJECTS_UNKNOWN`、`PATH_LONG_ENAMETOOLONG`、`PATH_RESOLUTION_ERRNO`、`DIRFD_AND_AT_FLAGS`、`USERPTR_EFAULT`、`MODE_UID_GID_GUARD`
- Evidence state：第 06 步是人工静态审计，没有运行适配后的 SyscallGuard static checker。
- Gap/risk：本批次目前不能声称 automated static-checker coverage。
- Blocking decision：不阻塞进入 Step 08/09，但阻塞任何“自动静态 checker 已覆盖”的 closeout 表述。
- Follow-up：`tools/starry_static_check.py` 和 `tools/syscall_spec_extract.py` 继续作为未来集成参考，记录在 `docs/tooling-roadmap.md`。

## Closeout gate state

- `gap` items：0
- `risk` items：7
- `needs_review` items：3
- `unsupported` items：0
- Closeout status：not eligible for `closed`
- Continue status：人工确认本步 triage 后可进入 Step 08

## 输出

- Gap/risk/needs_review triage 记录在本文件。
- 审核门禁：`reviews/07-gap-triage-signoff.yaml`。
