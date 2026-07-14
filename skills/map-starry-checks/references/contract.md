# Starry 增量映射契约

公开接口只有：

```text
$映射规则
$映射规则 syscalls=mmap,close
```

规则库索引提供 rule ID、详情路径和 syscall 归属。`targets/starry/rule-coverage.yaml` 按 rule ID
保存规则版本、状态、分类、mapping/check/test 引用、目标文件/符号内容指纹、最后验证内容快照、
处理 run 和原因。

以下情况进入 pending：没有 coverage；规则语义版本变化；相关 Starry 文件、符号或 helper
变化/消失；目标仓库身份或描述符变化；coverage 引用实体变化/消失；`needs_review` 或
`unsupported` 遇到新的目标内容快照。仅无关内容变化时保持跳过并更新最后验证快照。

mapping manifest 保存规则库索引 hash、selected rule versions、`rule_syscalls` 和目标
`snapshot_hash`，不保存 ingest report ID。所有依赖都由稳定业务 ID 与内容 hash 构成；禁止把
Git commit ID 写入规则、coverage、mapping、check、test 或 run。

暂存 mapping 必须覆盖每条 selected rule。`static` 必须只引用静态检查，`dynamic` 必须只引用
动态测试，`partial_static` 必须同时引用两类定义。`needs_review`/`unsupported` 不得引用编造的
可执行检查，并必须给出具体原因。finalizer 必须拒绝缺失引用、目标路径/符号和并发状态变化，
失败时不得推进共享实体或 coverage。
