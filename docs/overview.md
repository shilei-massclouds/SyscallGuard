# SyscallGuard 概览

SyscallGuard 将 syscall 合规性拆成四个可独立重跑的增量操作：规格导入、Starry 映射、
隔离检查和隔离修复。操作之间只通过不可变 run 快照中的实体 ID 关联，不自动调度。

共享实体文件是可直接编辑的当前视图，run 是执行时快照。消费者不信任历史内容副本：它
使用上游 run 限定实体集合，再读取共享文件并重算 hash。因此来源变化、人工编辑和 Starry
commit 变化都会自然触发重新处理。

成功运行使用原子文件替换发布共享实体。失败运行保留 manifest、changeset、日志、patch
和 worktree 信息，但不覆盖已完成实体。环境问题可以产生 `completed_with_blockers`，但不能
产生 Starry implementation finding。
