# 仓库边界

SyscallGuard 拥有规则、ingest/mapping report、Starry 检查定义、finding/fix 记录和下游 run
快照。规格来源仓库只读。Ingest 不持久化原始证据或 syscall 聚合规格。

LTP 全量审计也是只读流程：它可读取来源配置、当前 checkout 和已发布规则，但只能把
`report.yaml` 写入 `/tmp/syscallguard-ltp-audit/<audit-id>/`，不得更新 ingest report、规则、
索引或 fingerprint。现代 `/*\` 文档块仅作为上下文和代码冲突诊断，不形成正式规则。

Mapping 开始前由用户负责在 Starry 创建并 checkout 专用分支，再把分支名交给工具。工具不得创建、
切换、删除或 merge 分支。Check 和 fix 开始前再次请用户确认仍基于 mapping 报告中的分支，并验证
当前 checkout、仓库身份、干净状态和内容快照。

检查允许在该分支临时注入测试、构建和运行 QEMU，但发布报告前必须回滚测试 patch 并恢复原快照。
修复直接在同一分支应用测试与实现 patch；全部回归通过后提交该分支，不创建额外完成分支。

检查不生成实现修复。检查无 blocker 时清理 `/tmp/syscallguard-check/<id>`；环境 blocker 或意外
失败时保留临时日志，但 blocker 不进入 finding。修复不处理环境 blocker，默认补丁暂存于
`/tmp/syscallguard-fix/`。回归失败不创建完成 commit，并保留专用分支上的未提交变化、patch 和日志
供检查或重跑。

重置命令的删除边界只包括 `library/syscalls.yaml`、`library/rules/*.yaml` 和
`runs/spec-*/report.md`，不会扩大到来源
配置、Starry 共享实体或下游 run。
