# 仓库边界

SyscallGuard 拥有规则、ingest/mapping report、Starry 检查定义、finding/fix 记录和下游 run
快照。规格来源仓库只读。Ingest 不持久化原始证据或 syscall 聚合规格。

LTP 全量审计也是只读流程：它可读取来源配置、当前 checkout 和已发布规则，但只能把
`report.yaml` 写入 `/tmp/syscallguard-ltp-audit/<audit-id>/`，不得更新 ingest report、规则、
索引或 fingerprint。现代 `/*\` 文档块仅作为上下文和代码冲突诊断，不形成正式规则。

检查和修复允许在独立 Git worktree 中注入测试、构建、运行 QEMU 和修改 Starry。调用对应
skill 即授权这些隔离操作。用户现有 Starry worktree 和分支永不修改；修复成功只创建
`syscallguard/<run-id>` 分支 commit，永不自动 merge。

检查不生成实现修复。检查无 blocker 时清理 `/tmp/syscallguard-check/<id>`；环境 blocker 或意外
失败时保留临时 worktree 和日志，但 blocker 不进入 finding。修复不处理环境 blocker，默认补丁
暂存于 `/tmp/syscallguard-fix/`。回归失败不创建完成 commit，并保留隔离 worktree、patch 和日志供
检查或重跑。

重置命令的删除边界只包括 `library/syscalls.yaml`、`library/rules/*.yaml` 和
`runs/spec-*/report.md`，不会扩大到来源
配置、Starry 共享实体或下游 run。
