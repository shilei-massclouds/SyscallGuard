# LTP 和测试输入快照

本目录保存 SyscallGuard 批次可用的来源输入。首个快照来自本地 `tgoskits`
checkout，因为工作区中没有单独的 LTP 仓库，也没有 `new_specs/` 目录。

该快照包含：

- 与 baseline 回归批次相关的 Starry 系统测试源码。
- 用于人工审计证据的 Starry 实现文件。
- 针对 baseline 项的手工归一化行为摘要。
- 记录缺失预期材料的来源索引。

如果后续拿到上游 LTP 材料或四层 syscall 规格，应作为复制快照加入本目录，并
更新 `source-index.yaml`。
