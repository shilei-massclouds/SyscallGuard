# 数据模型

## Ingest report

`runs/spec-<id>/report.md` 正文先用中文说明规则的适用条件、检查内容和预期结果，末尾的机器
可读元数据是 ingest 的唯一历史与增量状态；mapping 直接读取通用规则库，不再消费该报告。
固定记录 report ID/时间、来源 ID/type/content snapshot、descriptor 与 recognizer hash、count 及其来源、
待处理数、本轮 syscall 列表，以及每个 syscall 的：

- source/recognition fingerprint；
- `formed_rules` 或 `no_rules`；
- 规则 `{id, generated_at_utc, content_hash}` 版本；
- 原始证据数、未解析证据数和原因。

最新状态按 `(source ID, syscall, generated_at_utc)` 从所有 report 扫描得到。fingerprint 未变化
时，`formed_rules` 与 `no_rules` 都跳过。旧 report 若包含已由新 report 更新的 syscall，不能再
用于 mapping。

显式名单模式额外记录已去重排序的 `requested_syscalls`，并将 count 记录为
`{value: null, source: explicit_syscalls}`。`selected_syscalls` 只包含名单内 fingerprint 首次
出现或发生变化的 syscall，`pending_count` 仍表示来源的全局待处理数。

## Syscall index 与 Rule

`library/syscalls.yaml` 是一级表，以 syscall 为索引引用若干规则 ID 和详情文件。
`library/rules/*.yaml` 目录是二级表，每个 YAML 是一条规则详情。Rule 包含 category、semantics、
`semantic_hash`、`generated_at_utc` 和 sources。`semantic_hash` 只覆盖 category 与 semantics。
新增或更新 sources 时不推进规则时间戳；语义变化同时推进时间戳与 hash。

每个 syscall 只有在所有证据都解析且至少产生一条规则时才记为 `formed_rules` 并发布候选。
任何未解析证据或零规则都会使该 syscall 记为 `no_rules`，候选规则全部丢弃。原始和归一化证据
只存在于执行内存和终端诊断中。

## Mapping report、检查库与下游 run

`runs/mapping-*/report.md` 是 mapping 的唯一增量状态。中文正文列出本轮静态检查数、动态测试数、
全局剩余数和完整 rule—syscall 关系；末尾元数据保存当前规则库全部规则。规则状态只有
`covered`、`needs_review`、`unsupported` 和 `pending`。`covered` 通过静态/动态引用组合表达覆盖方式。
每行同时保存规则版本、引用实体版本、目标文件/符号内容指纹、最后验证快照、最后处理报告和原因。

`targets/starry/static-checks.yaml` 与 `targets/starry/dynamic-tests.yaml` 是按 syscall 分组的一级索引；
同名目录保存一个实体一个 YAML 的二级详情。动态测试的独立源码或 patch 位于其 `assets/` 子目录。
Mapping 的 `execution_scope` 只记录本轮产出的检查和测试；check 只执行该范围，并使用报告的完整
`rule_syscalls` 生成 finding 归属。Check/fix manifest 仍使用 `from_run_id` 串接父结果。

所有依赖先比较 `generated_at_utc`，再比较 `content_hash`；任一不同即 stale。第二次 hash 比较
保证人工编辑即使漏更新时间也会被拒绝。

规则库、报告、共享实体和所有 run/result 不保存或依赖 Git commit ID。来源和目标使用内容型
`snapshot_hash` 保证各阶段观察一致；逐规则 pending 判断只比较其目标文件、符号和 helper 指纹。

## 描述符

LTP 来源：

```yaml
source_id: ltp-local
adapter: ltp
location: /path/to/ltp
revision: HEAD
default_count: 50
```

Starry 目标：

```yaml
target_id: starry
repository: /path/to/tgoskits
revision: HEAD
worktree_root: /tmp/syscallguard-worktrees
```

完整字段约束位于 `schemas/`。

## Reset

`$reset-syscallguard` 只删除 `library/syscalls.yaml`、`library/rules/*.yaml` 和
`runs/spec-*/report.md`。它保留来源配置、
recognizer、Starry 共享实体、mapping report 以及 check/fix 历史；下一次 ingest 因无 report 状态而从首个
字典序 syscall 重新开始。
