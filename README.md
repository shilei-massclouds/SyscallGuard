# SyscallGuard

SyscallGuard 是一个独立的 Starry syscall 合规性 harness。第一版先把流程落稳：
保存规格、证据、审核门禁、批次产物和最终覆盖结论；暂不直接修改 LTP 或
Starry 仓库，也不内置自动化 checker。

## 仓库结构

- `docs/`：项目目标、协作模型、批次流程和人工审核规则。
- `constraints/`：流程、规格、Starry 修复和动态测试约束。
- `schemas/`：manifest、步骤状态、审核记录和 coverage matrix 的 YAML 结构说明。
- `snapshots/ltp/`：批次使用的来源索引、规格摘要、快照缺口记录和必要的最小证据副本。
- `batches/001-syscall-batch-ioctl-renameat2/`：当前 syscall 检查批次。
- `templates/`：后续批次复用的 manifest、步骤、审核、gap 和验证模板。

外部工具接入计划记录在 `docs/tooling-roadmap.md`。

## 运行模型

每个批次都遵循 `docs/batch-process.md` 中固定的十步流程。每一步都要产出
步骤报告和 review sign-off 文件。只有当证据能追溯到来源索引、复制快照或
不可变外部 commit，且所有审核记录都完成后，批次才可以进入关闭状态。

当前 001 批次从 Starry syscall dispatch 顺序中选择 20 个 syscall，按可复用
检查规则推进十步流程。外部 Starry/LTP 证据优先通过 source index 记录，不默认
提交源码副本。
