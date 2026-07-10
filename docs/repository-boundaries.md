# 仓库边界

SyscallGuard 是 harness 仓库。它记录流程产物和审核结论，不拥有测试源码或
内核实现。

## SyscallGuard 负责

- 流程文档。
- 约束文件。
- YAML schema 说明。
- 复制的输入快照。
- 批次 manifest、步骤报告、审核记录、coverage matrix 和最终报告。

## LTP 或测试源码仓库负责

- 原始测试源码。
- 上游测试语义。
- 测试构建系统集成。

## tgoskits 和 Starry 负责

- 内核实现。
- Starry 测试接入。
- 构建和 QEMU 运行结果。
- 修复 commit 和 pull request。

## 边界规则

如果需要修改 Starry 或 LTP，SyscallGuard 只记录计划和外部变更链接。实际代码
修改发生在本仓库之外。
