# SyscallGuard 概览

SyscallGuard 将合规性工作拆成独立的规则导入、Starry 映射、隔离检查、隔离修复和状态重置。
操作之间只通过 report 或 run 的直接引用连接，不自动调度。

导入阶段刻意保持极简：report 同时承担人类报告、增量状态和 mapping 输入，规则 YAML 是唯一
通用库。成功时先原子替换规则、最后发布 report；失败时两者都不推进。`no_rules` 也是可跳过的
成功状态，但从不发布未完整解析的候选语义。

Mapping 将 report 中的规则版本与 syscall 归属保存到 run。Check 只从该归属生成 finding，
不依赖聚合 syscall spec。所有下游消费者先比较依赖时间戳，再复核内容 hash，并同时固定
Starry commit。

Reset 只清空通用规则和 ingest report 状态。来源配置和 Starry 映射、检查、测试定义保持不变。
