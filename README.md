# SyscallGuard

SyscallGuard 是一个独立的 Starry syscall 合规性 harness。第一版先把流程落稳：
保存规格、证据、审核门禁、批次产物和最终覆盖结论；暂不直接修改 LTP 或
Starry 仓库，也不内置自动化 checker。

## 仓库结构

- `docs/`：项目目标、协作模型、批次流程和人工审核规则。
- `constraints/`：流程、规格、Starry 修复和动态测试约束。
- `schemas/`：manifest、步骤状态、审核记录和 coverage matrix 的 YAML 结构说明。
- `snapshots/ltp/`：批次使用的输入快照、来源索引和快照缺口记录。
- `batches/000-regression-baseline/`：首个已修复回归项示范批次。
- `templates/`：后续批次复用的 manifest、步骤、审核、gap 和验证模板。

## 运行模型

每个批次都遵循 `docs/batch-process.md` 中固定的十步流程。每一步都要产出
步骤报告和 review sign-off 文件。只有当证据能追溯到快照、所有审核记录都
完成后，批次才可以进入关闭状态。

当前 baseline 批次刻意保持保守：它记录已知已修复回归项，并映射到 Starry
证据和本地可用测试源码。它用于跑通 harness 闭环，不声称发现了新的 Starry
缺口。
