# 步骤 09 - Validation

批次：`001-syscall-batch-ioctl-renameat2`
状态：`pending_human_review`

## 目的

执行第 08 步已确认的动态测试用例，结合第 06 步静态检查/审计结果和本步动态测试结果，
生成 Starry patch 候选，并询问是否进入第 10 步应用这些 patch。

## 输入

- `steps/06-static-check-or-audit.md`
- `steps/08-fix-plan-and-apply-outside-harness.md`
- `outputs/validation-cases.yaml`
- `outputs/starry-dynamic-tests.patch`
- `outputs/starry-dynamic-tests.yaml`

## 执行内容

- 用户输入“批准进入下一步”，第 08 步 sign-off 已记录为 `confirmed`。
- `outputs/validation-cases.yaml` 已标记为 `confirmed`，7 个动态用例进入执行阶段。
- 本步将 `outputs/starry-dynamic-tests.patch` 应用到外部 tgoskits 仓库。
- 应用后 tgoskits 工作树新增 7 个未跟踪的 `test-suit/starryos/qemu-smp1/system/syscallguard-b001-*` 测试目录。
- 本步逐个执行 `outputs/starry-dynamic-tests.yaml` 中绑定的 riscv64 命令。
- 7 个命令均启动并完成 Starry 内核构建，但在 QEMU case 加载前的 rootfs 准备阶段失败。
- 统一阻塞原因：`/tmp/.tgos-images/rootfs-riscv64-alpine.img/rootfs-riscv64-alpine.img` 解包失败，底层错误为 `No space left on device (os error 28)`。
- `df -h` 显示 `/tmp`、SyscallGuard workspace 和 tgoskits 所在文件系统使用率为 99%，可用空间约 1.4G。
- 因没有进入 QEMU guest，也没有运行生成的 C 测试二进制，本步没有产生 guest-level syscall 动态失败证据。
- 本步读取第 06 步静态检查/审计结果；第 06 步没有记录直接 implementation gap 或 missing pattern。
- 因没有动态失败证据，也没有静态直接 gap，本步没有生成 Starry 修复 patch 候选。

## Dynamic execution results

结构化结果写入：`outputs/validation-results.yaml`。
日志目录：`outputs/logs/starry-dynamic/`。

| Case ID | Command binding | Result | Evidence |
| --- | --- | --- | --- |
| `V09-PERMISSION-MATRIX` | bound and attempted | `not_run` / `blocked_rootfs_no_space` | `outputs/logs/starry-dynamic/V09-PERMISSION-MATRIX-riscv64.log` |
| `V09-FS-SIDE-EFFECT` | bound and attempted | `not_run` / `blocked_rootfs_no_space` | `outputs/logs/starry-dynamic/V09-FS-SIDE-EFFECT-riscv64.log` |
| `V09-DIRENT-ENUMERATION` | bound and attempted | `not_run` / `blocked_rootfs_no_space` | `outputs/logs/starry-dynamic/V09-DIRENT-ENUMERATION-riscv64.log` |
| `V09-FD-TYPE-MATRIX` | bound and attempted | `not_run` / `blocked_rootfs_no_space` | `outputs/logs/starry-dynamic/V09-FD-TYPE-MATRIX-riscv64.log` |
| `V09-PATH-ERRNO-PRIORITY` | bound and attempted | `not_run` / `blocked_rootfs_no_space` | `outputs/logs/starry-dynamic/V09-PATH-ERRNO-PRIORITY-riscv64.log` |
| `V09-USERPTR-EFAULT` | bound and attempted | `not_run` / `blocked_rootfs_no_space` | `outputs/logs/starry-dynamic/V09-USERPTR-EFAULT-riscv64.log` |
| `V09-MODE-UID-GID` | bound and attempted | `not_run` / `blocked_rootfs_no_space` | `outputs/logs/starry-dynamic/V09-MODE-UID-GID-riscv64.log` |

每条日志都包含相同的阻塞尾部：

```text
failed to unpack `rootfs-riscv64-alpine.img` into `/tmp/.tgos-images/rootfs-riscv64-alpine.img/rootfs-riscv64-alpine.img`
No space left on device (os error 28)
```

## Static result input

| Rule ID | Step 06 result | Patch signal in Step 09 |
| --- | --- | --- |
| `SYSCALL_ENTRY_ALIAS` | `static_audit_supports` | none |
| `BAD_FD_EBADF` | `static_audit_supports_for_bad_fd` | none |
| `FD_TYPE_ERRNO` | `partial_static_audit_supports` | needs dynamic validation |
| `FLAG_MASK_REJECTS_UNKNOWN` | `static_audit_supports` | none |
| `PATH_LONG_ENAMETOOLONG` | `partial_static_audit_supports` | needs dynamic validation |
| `PATH_RESOLUTION_ERRNO` | `partial_static_audit_supports` | needs dynamic validation |
| `DIRFD_AND_AT_FLAGS` | `partial_static_audit_supports` | needs dynamic validation |
| `USERPTR_EFAULT` | `partial_static_audit_supports` | needs dynamic validation |
| `MODE_UID_GID_GUARD` | `partial_static_audit_supports` | needs dynamic validation |
| `VFS_PERMISSION` | `dynamic_deferred` | needs dynamic validation |
| `FS_SIDE_EFFECT` | `dynamic_deferred` | needs dynamic validation |
| `DIRENT_ENUMERATION` | `dynamic_deferred` | needs dynamic validation |

## Starry patch candidates

| Candidate | Source evidence | Status |
| --- | --- | --- |
| none | no confirmed static gap and no guest-level dynamic failure evidence | no patch generated |

结构化 patch 候选记录：`outputs/starry-patch-candidates.yaml`。

## 缺口和风险

- 所有动态命令均已绑定并尝试执行，但均因 host/rootfs 准备空间不足而 `not_run`。
- 第 09 步没有运行到生成的 Starry C 测试二进制，因此不能确认 runtime gap，也不能把 runtime risk 标记为 covered。
- 第 06 步静态检查/审计结果没有给出直接 implementation gap，因此本步不能仅凭静态输入生成 Starry 修复 patch。
- 当前没有可应用到 Starry 的修复 patch；若不接受这个结果，需要释放或迁移 rootfs 准备空间后重跑第 09 步。

## Human review checklist

| No. | Question | Current answer |
| --- | --- | --- |
| 1 | 是否接受 7 个动态命令已尝试执行，但均因 rootfs 解包空间不足而 `not_run`？ | pending human review |
| 2 | 是否接受本步没有 guest-level 动态失败证据？ | pending human review |
| 3 | 是否接受本步没有生成 Starry 修复 patch 候选？ | pending human review |
| 4 | 如果不接受，是否先释放或迁移 rootfs 准备空间后重跑第 09 步？ | pending human review |
| 5 | 如果接受，是否进入第 10 步记录 no Starry repair patch applied，并保留未解决的动态执行阻塞项？ | pending human review |

## 输出

- 验证结果：`outputs/validation-results.yaml`
- Starry patch 候选：`outputs/starry-patch-candidates.yaml`
- 执行日志：`outputs/logs/starry-dynamic/`
- 审核门禁：`reviews/09-validation-signoff.yaml`
