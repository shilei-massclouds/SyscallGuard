# SyscallGuard

SyscallGuard 是面向 Starry 的增量 syscall 合规性工具。仓库提供五个彼此独立的 Codex
skill；它们不会自动编排或触发下一个阶段。

## 命令

```text
$ingest-syscall-specs [source=<alias-or-descriptor>] [count=<N-or-all> | syscalls=<name1,name2,...>]
$映射规则 [syscalls=<name1,name2,...>]
$合规检查 from=<mapping-report-id>
$修复缺口
$reset-syscallguard
python3 tools/audit_ltp.py [--source <source>] [--syscalls <name1,name2,...>]
```

- `ingest-syscall-specs`（中文显示名 `$提取规则`）：默认从 `ltp-local` 按名字典序分析前
  20 个待处理 syscall；`syscalls=` 可显式限定候选名单。稳定调用标识仍为
  `$ingest-syscall-specs`。
- `map-starry-checks`（中文显示名 `$映射规则`）：直接读取通用规则库，按最新 mapping report 增量生成映射；
  `syscalls=` 只限制本轮处理范围，其他 pending 规则保留。
- `check-starry-compliance`（中文显示名 `$合规检查`）：在隔离 worktree 注入测试并执行检查，
  分离 finding 与环境 blocker，汇总当前快照全部 open finding，并在快照变化后自动重验历史 finding；
  稳定调用标识仍可作为兼容别名。
- `fix-starry-compliance`（中文入口 `$修复缺口`）：无参数扫描当前快照全部 open confirmed finding，
  合并其证据报告回归范围并一次修复；成功后只提交到隔离分支。英文名仍是兼容别名，旧 `from=`
  参数已删除。
- `reset-syscallguard`：清空通用规则 YAML 和 ingest report 历史，使导入回到空白状态。
- `audit_ltp.py`：只读运行旧 baseline、候选 extractor 和已发布 LTP 规则的三方全量审计；
  完整 YAML 仅写入 `/tmp/syscallguard-ltp-audit/<audit-id>/report.yaml`。`--syscalls`
  只过滤报告详情，`full_counts` 始终保留全量统计。

## 持久化模型

一次成功 ingest 写三类结果：

```text
runs/spec-*/report.md          中文规则摘要；末尾保存机器可读增量状态
library/syscalls.yaml          syscall 到规则详情的一级索引
library/rules/*.yaml           二级规则详情
```

不生成 ingest manifest、changeset、raw/normalized evidence、syscall spec 或独立
state。失败 ingest 不写 report、不更新规则，下一次调用会自动重试。一个 syscall 只有在所有
authoritative 证据都能解析且至少形成一条规则时才发布候选规则；context 证据不阻塞发布，
真正无法关联断言的预期证据仍使 report 记录 `no_rules`。

`syscalls=` 名单按逗号分割、去除空白、转为小写、去重并按字典序处理。名单与显式 `count`
互斥，空项、空名单或来源中不存在的名称会使整次执行失败。名单模式仍按 fingerprint 跳过未
变化项，report 的 `pending_count` 保持为全局待处理数。

成功 mapping 只写 `runs/mapping-*/report.md`、静态检查两级库和动态测试两级库。报告末尾元数据
保存完整规则状态、`execution_scope`、规则库索引 hash、实体版本、`rule_syscalls` 和目标内容依赖。
成功 check 只写 `runs/check-*/report.md`、finding 一级索引和 finding 二级详情。中文正文逐项
展示静态/动态结果及精简证据，末尾元数据保存基础、重验与实际 scope，以及当前快照全部 open
finding 和 new/carried/revalidated/needs-revalidation 生命周期状态。check 不再生成 manifest、changeset、
`results.yaml` 或成功运行日志；正常完成后删除 `/tmp/syscallguard-check/<id>`，blocker 或失败时保留。
Fix prepare 从 finding 索引自动选取当前快照全部 open finding，并从 occurrences 收集所有证据报告；
组合补丁暂存于 `/tmp/syscallguard-fix/<run-id>/implementation-fix.patch`。无 finding 时不创建正式 run。

Fix run 继续使用 `runs/<run-id>/manifest.yaml`；新 manifest 以 `source_check_report_ids` 记录所有证据
来源，读取器仍兼容历史 `from_run_id`。规则和下游实体使用
`{id, generated_at_utc, content_hash}` 版本；消费者先比较时间戳，再比较 hash，从而发现漏改
时间戳的人工编辑。Rule 的版本 hash 只覆盖 category 与 semantics，来源追溯变化不使下游失效。
规则库与所有中间结果禁止持久化 Git commit ID；来源和 Starry 一致性使用内容快照，逐规则失效
使用目标文件、符号和 helper 内容指纹。

## 数据布局

```text
library/syscalls.yaml          syscall 到规则的一级索引
library/rules/                 目标无关规则详情
runs/spec-*/report.md          ingest 历史和状态
runs/mapping-*/report.md       完整映射状态和本轮 execution_scope
targets/starry/static-checks.yaml 按 syscall 分组的静态检查一级索引
targets/starry/static-checks/  静态检查二级详情
targets/starry/dynamic-tests.yaml 按 syscall 分组的动态测试一级索引
targets/starry/dynamic-tests/  动态测试详情及 assets
targets/starry/findings/       syscall + rule + target content snapshot 实现缺口
targets/starry/fixes/          补丁、commit 和回归结果
runs/check-*/report.md         中文检查结果和完整机器状态
runs/fix-*/                    修复 run 快照、报告和日志
```

来源示例见 [sources/ltp-local.yaml](sources/ltp-local.yaml)，Starry 目标示例见
[targets/starry/target.yaml](targets/starry/target.yaml)，详细模型见
[docs/data-model.md](docs/data-model.md)。

## 验证

```bash
python3 tools/validate_repository.py
python3 -m unittest discover -s tests -v
```
