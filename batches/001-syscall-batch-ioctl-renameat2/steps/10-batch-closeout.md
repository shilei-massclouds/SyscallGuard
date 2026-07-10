# 步骤 10 - Batch Closeout

批次：`001-syscall-batch-ioctl-renameat2`
状态：`pending_human_review`

## 目的

根据第 09 步确认的验证结果和 Starry patch 候选，执行第 10 步收尾：应用已确认 patch、
执行静态/动态回归、生成 coverage matrix 和 batch report，并判断能否关闭批次。

## 输入

- `steps/06-static-check-or-audit.md`
- `steps/07-gap-triage.md`
- `steps/08-fix-plan-and-apply-outside-harness.md`
- `steps/09-validation.md`
- `outputs/validation-results.yaml`
- `outputs/starry-patch-candidates.yaml`

## 执行内容

- 第 09 步 sign-off 已确认。
- 第 09 步 patch candidates 数量为 `0`。
- 本步没有可应用到 Starry 的 patch。
- 因没有 patch，本步没有执行 patch 后静态回归。
- 因动态测试命令/环境仍缺失，本步没有执行动态回归。
- 生成 coverage matrix：`outputs/coverage-matrix.yaml`。
- 生成 batch report：`outputs/batch-report.md`。
- 批次不标记为 `closed`。

## Closeout gate result

| Gate | Result | Reason |
| --- | --- | --- |
| All scoped syscalls in coverage matrix | pass | 20 个 scoped syscalls 均写入 `outputs/coverage-matrix.yaml`。 |
| Starry patch application | not_applicable | 第 09 步没有生成 Starry patch 候选。 |
| Static regression after patch | not_run | 没有 patch 可回归，且本仓库没有已接入的 automated static checker。 |
| Dynamic regression after patch | blocked | 7 个动态用例仍缺少可运行命令/环境。 |
| Runtime risks resolved | fail | 第 07 步的 7 个 runtime risks 均未验证。 |
| Needs-review items resolved | fail | `ioctl` request split、source/spec basis、static checker coverage 仍为 `needs_review`。 |
| Batch status can become `closed` | fail | 仍存在 unresolved risk / needs_review / execution blocker。 |

## Resolved items

- 第 09 步结果已确认。
- 第 10 步已生成 coverage matrix。
- 第 10 步已生成 batch report。
- Starry patch application 决策已记录为 `not_applicable`，因为没有 patch candidate。

## Unresolved items

| Item | Status | Next action |
| --- | --- | --- |
| `T07-DYNAMIC-PERMISSION` | `execution_blocked` | 回到第 08 步补充可运行 permission matrix 命令/环境。 |
| `T07-DYNAMIC-FS-SIDE-EFFECT` | `execution_blocked` | 回到第 08 步补充 filesystem side-effect 命令/环境。 |
| `T07-DYNAMIC-DIRENT` | `execution_blocked` | 回到第 08 步补充 getdents64 enumeration 命令/环境。 |
| `T07-FD-TYPE-MATRIX` | `execution_blocked` | 回到第 08 步补充 fd type matrix 命令/环境。 |
| `T07-PATH-ERRNO-PRIORITY` | `execution_blocked` | 回到第 08 步补充 path errno priority 命令/环境。 |
| `T07-USERPTR-EFAULT` | `execution_blocked` | 回到第 08 步补充 EFAULT 命令/环境。 |
| `T07-MODE-UID-GID` | `execution_blocked` | 回到第 08 步补充 mode/uid/gid 命令/环境。 |
| `T07-IOCTL-REQUEST-SPLIT` | `needs_review` | 拆分 `ioctl` request classes 或显式排除不覆盖范围。 |
| `T07-SOURCE-SPEC-GAP` | `needs_review` | closeout 前接受当前 source basis 或刷新 spec。 |
| `T07-STATIC-CHECKER-GAP` | `needs_review` | 接入 static checker 或明确本批只保留人工审计。 |

## Human review checklist

| No. | Question | Current answer |
| --- | --- | --- |
| 1 | 是否接受第 10 步没有应用 Starry patch？ | pending human review |
| 2 | 是否接受静态/动态回归未执行的原因？ | pending human review |
| 3 | 是否接受本批不能 closed，只能保留 unresolved blockers？ | pending human review |
| 4 | 是否回到第 08 步补充动态测试命令/环境？ | pending human review |

## 输出

- Coverage matrix：`outputs/coverage-matrix.yaml`
- Batch report：`outputs/batch-report.md`
- 审核门禁：`reviews/10-batch-closeout-signoff.yaml`
