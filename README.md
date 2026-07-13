# SyscallGuard

SyscallGuard 是面向 Starry 的增量 syscall 合规性工具。仓库只提供四个彼此独立的
Codex skill；每次调用都立即生成 run 快照并更新共享实体库，不存在流水线编排、人工审核
门禁或发布步骤。

## 四个技能

```text
$ingest-syscall-specs source=<source-descriptor> count=<N>
$map-starry-checks from=<spec-run-id> target=<starry-descriptor>
$check-starry-compliance from=<mapping-run-id>
$fix-starry-compliance from=<check-run-id>
```

- `ingest-syscall-specs`：选择来源中前 `N` 个新增或内容变化的 syscall，保存规格与目标无关规则。
- `map-starry-checks`：固定 Starry commit，生成目标映射、静态检查和动态测试定义，不修改 Starry。
- `check-starry-compliance`：在隔离 worktree 注入测试并执行检查，分离实现 finding 与环境 blocker。
- `fix-starry-compliance`：只修复 confirmed implementation findings；回归成功后提交到
  `syscallguard/<run-id>`，不合并用户分支。

每个技能完成后都会打印 `runs/<run-id>/` 和相关共享 index 路径。用户可以重新调用同一
技能，也可以直接修改共享 YAML 后调用下游技能；下游会按上游实体 ID 读取当前文件并重新
计算 hash。

## 数据布局

```text
library/specs/                 syscall 当前规格
library/rules/                 目标无关规则
targets/starry/mappings/       Starry 文件、符号和 helper 映射
targets/starry/static-checks/  可执行静态规则
targets/starry/dynamic-tests/  测试定义、源码/补丁、构建和执行绑定
targets/starry/findings/       syscall + rule + target revision 实现缺口
targets/starry/fixes/          补丁、commit 和回归结果
runs/<run-id>/                 manifest、changeset、报告、日志和输入输出快照
```

每个共享目录都有 `index.yaml`，实体按文件分片。`batches/syscall-check-history.yaml` 只记录
实体输入 hash、处理 run 和 finding/fix 状态，不按 syscall 名整体排除后续工作。

## 描述符

- LTP 来源示例：[sources/ltp-local.yaml](sources/ltp-local.yaml)
- Starry 目标示例：[targets/starry/target.yaml](targets/starry/target.yaml)
- 字段契约：[docs/data-model.md](docs/data-model.md)

## 迁移状态

旧 batch 001 已转换为四个关联 run：

- `spec-migrated-batch-001`
- `mapping-migrated-batch-001`
- `check-migrated-batch-001`
- `fix-migrated-batch-001`

共享库保留 20 个 syscall、289 条 normalized spec、12 条通用规则、9 条静态检查和 7 个
动态测试。原审核文件只保存在各 run 的 `legacy-artifacts/` 中作为 provenance，不参与运行。

## 验证

```bash
python3 tools/validate_repository.py
python3 -m unittest discover -s tests -v
```
