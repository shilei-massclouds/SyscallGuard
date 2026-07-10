# SyscallGuard 概览

SyscallGuard 的目标是让 syscall 合规性工作可审计。它保留从行为来源、规格
归一化、可检查性分类、Starry 证据、验证结果、人工审核到覆盖归档的完整链路。

## 目标

- 将 syscall 行为输入记录为稳定的来源索引；仅在必要时保存最小证据快照。
- 将行为归一化为批次内可审核的规格。
- 将每个行为分类为 `static`、`partial_static`、`dynamic`、`unsupported`
  或 `needs_review`。
- 在不通过 harness 修改 Starry 的前提下记录 Starry 证据。
- 每个步骤都通过人工审核记录做门禁。
- 产出可追溯到规格和证据的 coverage matrix。

## 第一版非目标

- 不实现 CLI 或自动调度器。
- 不直接修改 LTP 或 Starry 仓库。
- 不迁入 extractor 或 checker 脚本。
- 不在缺少人工 sign-off 的情况下自动下结论。

## 产物流转

1. 在批次 `inputs/source-index.yaml` 中记录来源仓库、commit、路径和必要快照。
2. 在 `batches/<id>/manifest.yaml` 创建批次 manifest。
3. 每个流程步骤产出一个步骤报告和一个 review sign-off。
4. 基于归一化规格和证据记录填充 coverage matrix。
5. 只有所有审核门禁都解决后，才能关闭批次。
