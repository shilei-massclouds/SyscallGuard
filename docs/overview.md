# SyscallGuard 概览

SyscallGuard 将合规性工作拆成独立的规则导入、Starry 映射、隔离检查、隔离修复和状态重置。
操作之间只通过 report 或 run 的直接引用连接，不自动调度。

导入阶段刻意保持极简：report 正文说明规则结论，末尾元数据承担增量状态和 mapping 输入；
`library/syscalls.yaml` 是一级索引，规则 YAML 是二级详情。成功时先原子替换索引和规则、最后
发布 report；失败时三者都不推进。`no_rules` 也是可跳过的
成功状态，但从不发布未完整解析的候选语义。

Mapping 将完整规则状态写入中文报告尾部元数据，并只把本轮产出的检查与测试写入
`execution_scope`。Check 从该范围执行、从完整归属生成 finding，不依赖聚合 syscall spec。
Check 的中文报告本身承载完整机器状态，finding 与报告在单次事务中发布；成功运行不保留
manifest、results 或日志。Fix 直接消费该报告及 finding 版本。所有下游消费者先比较依赖时间戳，
再复核内容 hash，并固定 Starry 内容快照。

Reset 只清空 syscall 索引、通用规则和 ingest report 状态。来源配置、mapping report、检查和测试定义保持不变。
