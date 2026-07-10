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

## 执行内容

- 第 08 步 sign-off 已确认。
- `outputs/validation-cases.yaml` 已标记为 `confirmed`，7 个动态用例进入执行阶段。
- 本步检查每个动态用例的 `execution_binding`。
- 7 个动态用例均没有绑定可运行命令，`command_status` 均为 `missing`。
- 因缺少命令、环境和日志路径，本步没有实际运行动态测试。
- 本步读取第 06 步静态检查/审计结果；第 06 步没有记录直接 implementation gap 或 missing pattern。
- 因没有动态失败证据，也没有静态直接 gap，本步没有生成 Starry patch 候选。

## Dynamic execution results

| Case ID | Command binding | Result | Evidence |
| --- | --- | --- | --- |
| `V09-PERMISSION-MATRIX` | missing | `not_run` / `execution_blocked` | no command, no log |
| `V09-FS-SIDE-EFFECT` | missing | `not_run` / `execution_blocked` | no command, no log |
| `V09-DIRENT-ENUMERATION` | missing | `not_run` / `execution_blocked` | no command, no log |
| `V09-FD-TYPE-MATRIX` | missing | `not_run` / `execution_blocked` | no command, no log |
| `V09-PATH-ERRNO-PRIORITY` | missing | `not_run` / `execution_blocked` | no command, no log |
| `V09-USERPTR-EFAULT` | missing | `not_run` / `execution_blocked` | no command, no log |
| `V09-MODE-UID-GID` | missing | `not_run` / `execution_blocked` | no command, no log |

结构化结果写入：`outputs/validation-results.yaml`。

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
| none | no confirmed static gap and no dynamic failure evidence | no patch generated |

结构化 patch 候选记录：`outputs/starry-patch-candidates.yaml`。

## 缺口和风险

- 所有动态用例均因缺少执行命令而 `not_run`。
- 第 09 步没有产生动态测试日志，因此不能确认 runtime gap，也不能把 runtime risk 标记为 covered。
- 第 06 步静态检查/审计结果没有给出直接 implementation gap，因此本步不能仅凭静态输入生成 Starry patch。
- 当前没有可应用到 Starry 的 patch；若不接受这个结果，需要回到第 08 步补充可运行的动态测试命令或调整用例。

## Human review checklist

| No. | Question | Current answer |
| --- | --- | --- |
| 1 | 是否接受 7 个动态用例本次执行结果均为 `execution_blocked`？ | pending human review |
| 2 | 是否接受本步没有生成 Starry patch 候选？ | pending human review |
| 3 | 如果不接受，是否回到第 08 步补充测试命令/环境或修改测试用例？ | pending human review |
| 4 | 如果接受，是否进入第 10 步记录 no patch applied，并保留未解决的动态执行阻塞项？ | pending human review |

## 输出

- 验证结果：`outputs/validation-results.yaml`
- Starry patch 候选：`outputs/starry-patch-candidates.yaml`
- 审核门禁：`reviews/09-validation-signoff.yaml`
