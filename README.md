# SyscallGuard

SyscallGuard 是一个独立的 Starry syscall 合规性 harness。它负责保存 syscall
检查范围、规格来源、归一化规则、Starry 证据、人工审核门禁、验证结果和最终覆盖结论。

当前仓库默认不直接修改 LTP；也不在未获确认时修改 Starry。Starry 修复补丁只在流程后段
生成候选并等待人工确认，应用补丁属于显式确认后的外部目标操作。

## 快速开始

在 Codex 中输入：

```text
开始检查系统调用
```

期望行为：

1. 立即显示当前步骤和进度，避免用户误以为卡住。
2. 第 01 步先给出待检查 syscall 列表；默认每批 20 个。
3. 已在 `batches/syscall-check-history.yaml` 中记录为完成的 syscall 不再重复选择。
4. 每一步只处理当前步骤，生成或检查对应中间结果文件。
5. 步骤结束时在屏幕上显示本步产物列表和编号确认清单。
6. 用户检查文件后输入 `批准进入下一步`，流程才进入下一步。

如果需要修改中间结果，直接说明：

```text
修改 2: ...
```

Codex 应根据修改意见更新当前步骤产物，并继续停在当前步骤的 review sign-off。

## 十步流程

每个批次遵循 `docs/batch-process.md` 中固定的十步流程：

| Step | Name | 用户主要确认内容 |
| --- | --- | --- |
| 01 | `scope-selection` | 本批 20 个 syscall 是否正确，是否有应排除或补入的项 |
| 02 | `spec-ingestion` | 规格来源、外部 commit、source index 和缺口是否完整 |
| 03 | `normalization-review` | syscall 表、可复用检查规则表和映射关系是否合理 |
| 04 | `checkability-classification` | `static`、`partial_static`、`dynamic`、`unsupported`、`needs_review` 分级是否正确 |
| 05 | `starry-evidence-mapping` | Starry 代码、测试、日志或人工审计证据路径是否充分 |
| 06 | `static-check-or-audit` | 静态检查或人工审计覆盖了哪些规则，结论是否可接受 |
| 07 | `gap-triage` | 每个 gap、risk、needs_review 的定性和后续处理是否正确 |
| 08 | `fix-plan-and-apply-outside-harness` | 动态测试用例清单和执行阻塞项是否正确 |
| 09 | `validation` | 第 08 步确认的动态测试是否执行，结合静态/动态结果生成的 Starry patch 候选是否接受 |
| 10 | `batch-closeout` | 已确认 Starry patch 是否应用，静态/动态回归结果和最终 unresolved 状态是否接受 |

`批准进入下一步` 只表示当前步骤审核通过。上一阶段 sign-off 未确认时，流程必须停止并提示需要先确认哪个 review 文件。

## 产物位置

- `skills/syscallguard-flow/`：SyscallGuard 十步向导 skill 源码。
- `skills/syscallguard-flow/references/ten-step-flow.md`：每一步的输入、输出、检查点和停顿条件。
- `skills/syscallguard-flow/references/artifact-map.md`：批次目录结构、文件命名和 history 记录规则。
- `skills/syscallguard-flow/scripts/next_syscalls.py`：列出下一批待检查 syscall，或在 closeout 后记录检查历史。
- `skills/syscallguard-flow/scripts/check_batch.py`：非破坏性检查批次完整性和关闭门禁。
- `docs/`：项目目标、协作模型、批次流程、工具接入计划和人工审核规则。
- `constraints/`：流程、规格、Starry 修复和动态测试约束。
- `schemas/`：manifest、步骤状态、审核记录和 coverage matrix 的 YAML 结构说明。
- `batches/001-syscall-batch-ioctl-renameat2/`：当前 syscall 检查批次。
- `snapshots/`：必要时保存的最小证据快照；外部 Starry/LTP 来源优先记录在 batch 的 `inputs/source-index.yaml`。
- `templates/`：后续批次复用的 manifest、步骤、审核、gap 和验证模板。

## 当前批次状态

当前批次是 `batches/001-syscall-batch-ioctl-renameat2/`，范围为 20 个 syscall：

```text
ioctl, chdir, fchdir, chroot, mkdir, mkdirat, mknod, mknodat, getdents64, link,
linkat, rmdir, unlink, unlinkat, getcwd, symlink, symlinkat, rename, renameat,
renameat2
```

截至当前产物：

- 第 01 到第 09 步已经有确认记录。
- 第 10 步停在 `pending_human_review`。
- 第 09 步没有生成 Starry patch 候选。
- 动态验证用例已登记，但缺少可执行命令和环境绑定，因此未运行。
- 批次不能标记为 `closed`；需要接受当前 closeout 结果，或回到第 08 步补充可执行动态测试。

## 常用检查命令

列出下一批默认 20 个待检查 syscall：

```bash
python3 skills/syscallguard-flow/scripts/next_syscalls.py list --limit 20
```

检查当前批次是否结构完整、是否满足关闭门禁：

```bash
python3 skills/syscallguard-flow/scripts/check_batch.py batches/001-syscall-batch-ioctl-renameat2
```

在第 10 步人工确认后记录 syscall 检查历史：

```bash
python3 skills/syscallguard-flow/scripts/next_syscalls.py record --batch batches/001-syscall-batch-ioctl-renameat2
```

未解决 review gate 或未关闭批次不应写入完成历史，除非用户明确要求做 dry review 记录。
