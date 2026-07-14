# Starry 增量映射契约

公开接口只有：

```text
$映射规则
$映射规则 syscalls=mmap,close
```

规则库索引提供 rule ID、详情路径和 syscall 归属。最新成功
`runs/mapping-*/report.md` 是唯一增量状态；没有历史报告的规则视为新增。报告元数据必须携带
当前规则库全部规则，状态只能是 `covered`、`needs_review`、`unsupported` 或 `pending`。
`covered` 通过 `static_check_refs` 和 `dynamic_test_refs` 的组合表达静态、动态或共同覆盖。

以下情况重新处理：规则版本变化；引用检查/测试变化或消失；相关 Starry 文件、符号或 helper
变化/消失；目标仓库身份或描述符变化；`needs_review`/`unsupported` 遇到新的目标内容快照。
无关目标内容变化保持跳过。`syscalls=` 只限制本轮处理范围，报告仍保留其他规则；全局剩余分别
列出 pending、needs_review 和 unsupported。

准备、目标只读分析和暂存只使用 `/tmp/syscallguard-map/<run-id>`。每条 selected rule 必须有一个
暂存 rule result。`covered` 必须引用至少一个可执行静态检查或动态测试，并保存非空目标位置；
`needs_review`/`unsupported` 不得引用编造的可执行项，且必须说明原因。

静态一级索引是 `targets/starry/static-checks.yaml`，动态一级索引是
`targets/starry/dynamic-tests.yaml`，都按 syscall 分组并引用同名目录内的二级详情。动态测试独立源码
或 patch 只能放在 `dynamic-tests/assets/`。Finalizer 必须验证全部 ID、规则引用、目标路径/符号、
动态 asset、规则版本和并发状态，再原子发布两个索引、详情、assets 与报告。报告的
`execution_scope` 只列本轮产出的检查和测试。成功删除暂存区；失败保留暂存区且不得改动正式结果。

所有依赖由稳定业务 ID、实体版本和内容 hash 构成；禁止把 Git commit ID 写入规则、报告、检查、
测试或下游 run。
