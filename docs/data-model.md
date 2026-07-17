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
其中 `syscalls` 只含 active 规则；`inactive_rules` 保存退役或冲突规则的详情路径、原 syscall
归属、原因和可选替代规则。历史二级规则及其下游引用不删除。
`library/rules/*.yaml` 目录是二级表，每个 YAML 是一条规则详情。Rule 包含 category、semantics、
`semantic_hash`、`generated_at_utc` 和 sources。`semantic_hash` 只覆盖 category 与 semantics。
新增或更新 sources 时不推进规则时间戳；语义变化同时推进时间戳与 hash。

每个 syscall 只有在所有证据都解析且至少产生一条规则时才记为 `formed_rules` 并发布候选。
任何未解析证据或零规则都会使该 syscall 记为 `no_rules`，候选规则全部丢弃。原始和归一化证据
只存在于执行内存和终端诊断中。

## Mapping report、检查库与下游 run

`runs/mapping-*/report.md` 是 mapping 的唯一增量状态。Mapping 开始前由用户在 Starry 自行创建并
checkout 一个干净的专用分支，再将名称明确交给工具；报告 `target.branch` 固定该协商结果。中文正文列出本轮静态检查数、动态测试数、
全局剩余数和完整 rule—syscall 关系；末尾元数据保存当前规则库全部规则。规则状态只有
`covered`、`needs_review`、`unsupported` 和 `pending`。`covered` 通过静态/动态引用组合表达覆盖方式。
每行同时保存规则版本、引用实体版本、目标文件/符号内容指纹、最后验证快照、最后处理报告和原因。
Mapping report 另存 `coverage_mode`。`static-only` 不产生动态 execution scope，需要运行时夹具的
规则以 `deferred: dynamic_test` 留待 `full` 模式重试。

`targets/starry/static-checks.yaml` 与 `targets/starry/dynamic-tests.yaml` 是按 syscall 分组的一级索引；
同名目录保存一个实体一个 YAML 的二级详情。动态测试的独立源码或 patch 位于其 `assets/` 子目录。
Mapping 的 `execution_scope` 只记录本轮产出的检查和测试；check 将其作为 base scope，并使用报告的
完整 `rule_syscalls` 生成 finding 归属。若 finding 索引中有旧 Starry 快照的 open finding，check 自动
将其原始静态/动态来源加入 revalidation scope；其他快照已 fixed 的 finding 将原始来源加入
historical regression scope。历史回归失败只创建当前快照的新 finding，旧实体保持 fixed，不被重开、
supersede 或复用。报告同时记录 base、revalidation、historical regression 和 effective scope。

`runs/check-*/report.md` 是 check 的唯一运行结果。中文正文逐项列出 ID、类型、syscall、通用规则、
`pass`/`fail`/`skipped`/`not_run`/`error`、原因和精简证据；末尾
`syscallguard_check_report` 元数据保存父 mapping report、目标快照、输入实体版本、执行范围、完整
静态/动态结果、计数、blocker，以及检查结束时当前快照全部 open confirmed finding 版本。报告另列
new、carried、revalidated、needs-revalidation ID 和计数。同快照未覆盖 finding 直接 carry；旧快照
重验失败会被当前 finding supersede，全部通过标记 `no_longer_reproduces`，缺失实体或 blocker 保持
open 且进入 needs-revalidation。正常完成目录中只有 `report.md`，执行临时区固定为
`/tmp/syscallguard-check/<id>`。环境 blocker 不生成 finding，并使报告状态为
`completed_with_blockers`、临时区保留。Check 直接在协商分支执行，动态测试 patch 在发布前回滚并
验证原内容快照；无 blocker 时删除临时日志。报告、finding 详情和
一级索引在同一事务中发布，报告最后落盘。

Fix 无参数 prepare 扫描 finding 索引，选择当前 Starry 内容快照下全部 open confirmed finding，并从
occurrences 收集全部 evidence-bearing check report。各报告完整回归 scope 按实体 ID 合并；重复动态
patch 只应用一次。prepare 固定依赖版本并输出
`/tmp/syscallguard-fix/<run-id>/implementation-fix.patch`；finalize 重新校验后才创建正式 fix run，
在同一协商分支应用测试与实现 patch、回归并提交。新 manifest 用 `source_check_report_ids` 记录全部
证据来源，读取器兼容历史 `from_run_id`。当前快照没有 open finding 时成功返回，且不修改分支或
创建正式 run。

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
```

完整字段约束位于 `schemas/`。

## Reset

`$reset-syscallguard` 只删除 `library/syscalls.yaml`、`library/rules/*.yaml` 和
`runs/spec-*/report.md`。它保留来源配置、
recognizer、Starry 共享实体、mapping/check report 以及 fix 历史；下一次 ingest 因无 report 状态而从首个
字典序 syscall 重新开始。
