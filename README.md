# SyscallGuard

SyscallGuard 是面向 Starry 的增量 syscall 合规性工具。仓库提供五个彼此独立的 Codex
skill；它们不会自动编排或触发下一个阶段。

## 命令

```text
$ingest-syscall-specs [source=<alias-or-descriptor>] [count=<N-or-all> | syscalls=<name1,name2,...>]
$映射规则 [syscalls=<name1,name2,...>]
$check-starry-compliance from=<mapping-run-id>
$fix-starry-compliance from=<check-run-id>
$reset-syscallguard
```

- `ingest-syscall-specs`（中文显示名 `$提取规则`）：默认从 `ltp-local` 按名字典序分析前
  20 个待处理 syscall；`syscalls=` 可显式限定候选名单。稳定调用标识仍为
  `$ingest-syscall-specs`。
- `map-starry-checks`（中文显示名 `$映射规则`）：直接读取通用规则库，按 coverage 增量生成映射；
  `syscalls=` 只限制本轮处理范围，其他 pending 规则保留。
- `check-starry-compliance`：在隔离 worktree 注入测试并执行检查，分离 finding 与环境 blocker。
- `fix-starry-compliance`：修复 confirmed finding；成功后只提交到隔离分支。
- `reset-syscallguard`：清空通用规则 YAML 和 ingest report 历史，使导入回到空白状态。

## 持久化模型

一次成功 ingest 写三类结果：

```text
runs/spec-*/report.md          中文规则摘要；末尾保存机器可读增量状态
library/syscalls.yaml          syscall 到规则详情的一级索引
library/rules/*.yaml           二级规则详情
```

不生成 ingest manifest、changeset、raw/normalized evidence、syscall spec 或独立
state。失败 ingest 不写 report、不更新规则，下一次调用会自动重试。一个 syscall 只有在所有
证据都能解析且至少形成一条规则时才发布候选规则；否则 report 记录 `no_rules`。

`syscalls=` 名单按逗号分割、去除空白、转为小写、去重并按字典序处理。名单与显式 `count`
互斥，空项、空名单或来源中不存在的名称会使整次执行失败。名单模式仍按 fingerprint 跳过未
变化项，report 的 `pending_count` 保持为全局待处理数。

Mapping/check/fix 使用 `runs/<run-id>/manifest.yaml`。mapping manifest 保存规则库索引 hash、
selected rule versions、`rule_syscalls` 和目标内容快照，不再保存 ingest report ID。规则和下游实体使用
`{id, generated_at_utc, content_hash}` 版本；消费者先比较时间戳，再比较 hash，从而发现漏改
时间戳的人工编辑。Rule 的版本 hash 只覆盖 category 与 semantics，来源追溯变化不使下游失效。
规则库与所有中间结果禁止持久化 Git commit ID；来源和 Starry 一致性使用内容快照，逐规则失效
使用目标文件、符号和 helper 内容指纹。

## 数据布局

```text
library/syscalls.yaml          syscall 到规则的一级索引
library/rules/                 目标无关规则详情
runs/spec-*/report.md          ingest 历史和状态
targets/starry/mappings/       Starry 文件、符号和 helper 映射
targets/starry/rule-coverage.yaml 逐规则增量覆盖状态和目标依赖指纹
targets/starry/static-checks/  可执行静态规则
targets/starry/dynamic-tests/  测试、构建和执行绑定
targets/starry/findings/       syscall + rule + target content snapshot 实现缺口
targets/starry/fixes/          补丁、commit 和回归结果
runs/{mapping,check,fix}-*/    下游 run 快照、报告和日志
```

来源示例见 [sources/ltp-local.yaml](sources/ltp-local.yaml)，Starry 目标示例见
[targets/starry/target.yaml](targets/starry/target.yaml)，详细模型见
[docs/data-model.md](docs/data-model.md)。

## 验证

```bash
python3 tools/validate_repository.py
python3 -m unittest discover -s tests -v
```
