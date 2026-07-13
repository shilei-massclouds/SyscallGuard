# 数据模型

## Run

`runs/<run-id>/manifest.yaml` 记录 `stage`、`status`、`from_run_id`、实体 ID、实体 hash、目标
hash、输出和 blocker。状态只允许：

- `running`
- `completed`
- `completed_with_blockers`
- `failed`
- `superseded`

阶段链固定为单个直接来源：`spec <- mapping <- check <- fix`。这只是数据引用关系，不是自动
编排；任意 skill 都只在被明确调用时执行。

## 增量语义

规格来源指纹包含 source ID、adapter/version、工具版本、解析后的 revision、adapter 参数、
extractor 内容和 syscall 相关源内容。只选择未见或指纹变化的 syscall，并按 adapter 稳定顺序
截取 `count`。

下游从上游 run 读取实体 ID，但从共享目录读取内容并重算 hash。输入和目标 hash 均相同时
可跳过；规则文件人工变化或 Starry commit 变化时不得复用旧结果。

## 描述符

LTP 来源：

```yaml
source_id: ltp-local
adapter: ltp-extractor
location: /path/to/ltp
revision: HEAD
parameters:
  tool: tools/syscall_spec_extract.py
  syscalls: [read, write]
```

Starry 目标：

```yaml
target_id: starry
repository: /path/to/tgoskits
revision: HEAD
worktree_root: /tmp/syscallguard-worktrees
```

完整字段约束位于 `schemas/`。

## Finding 与 Blocker

finding 必须绑定 `syscall + rule_id + target_revision`，具有可靠的静态缺失或动态失败证据。
磁盘、构建、toolchain、rootfs、QEMU、timeout 和测试注入问题只写入 run blocker。修复阶段
只处理 `status: confirmed` 且 `resolution: open` 的 finding。
