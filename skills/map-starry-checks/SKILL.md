---
name: map-starry-checks
description: Negotiate a user-created dedicated Starry branch, then incrementally map new or invalidated general syscall rules to that branch. Use when the user invokes `$映射规则`/`$map-starry-checks`, optionally with `syscalls=<comma-separated-names>`. Never create or switch the branch for the user, and do not modify, build, or execute Starry.
---

# 映射规则

## 执行

1. 只解析可选的 `syscalls=<comma-separated-names>`；不接受 `from` 或 `target`。
2. 阅读 [references/contract.md](references/contract.md)。
3. 告知用户 Starry 仓库路径，请用户自行创建并切换到一个干净的专用分支，然后回复分支名。必须等待用户回复；不得替用户创建、切换或猜测分支。
4. 收到 `<starry-branch>` 后运行准备阶段：

   ```bash
   python3 skills/map-starry-checks/scripts/run.py [--syscalls <names>] --branch <starry-branch> --phase prepare
   ```

5. 读取输出的 `preparation.yaml` 和暂存实体。只读检查协商分支
   `targets/starry/target.yaml` 指向的内容快照，为每条 selected rule 完善实现位置和证据：
   能静态判断时生成静态检查，必须观察行为时生成动态测试，部分可静态覆盖时两者都生成。
   无可靠证据时保留 `needs_review` 及具体原因；明确无法支持时使用 `unsupported`。
6. 只编辑 `/tmp/syscallguard-map/<run-id>/staged/`，然后运行 finalizer：

   ```bash
   python3 skills/map-starry-checks/scripts/run.py --phase finalize --run-id <run-id>
   ```

7. 报告协商分支、新增、更新、跳过、待复核、不支持、静态检查、动态测试和剩余 pending 数量。

## 边界

- 规则输入固定读取 `library/syscalls.yaml` 和 `library/rules/*.yaml`。
- Starry 仓库路径固定读取 `targets/starry/target.yaml`；分支必须由用户本轮明确提供，且当前 checkout 必须与其相同并保持干净。
- 依赖使用规则 ID、实体 ID、语义/内容 hash 和 Starry 文件/符号内容指纹；任何共享结果都不得保存或依赖 Git commit ID。
- `syscalls=` 只限制本轮处理范围，其他 pending rule 必须保留。
- `needs_review`/`unsupported` 在相同内容快照下不重复处理，目标内容变化后自动重试。
- 准备和分析阶段不得写正式结果；finalizer 校验全部引用后原子发布中文报告和静态/动态两级库。
- 成功后删除 `/tmp/syscallguard-map/<run-id>`；失败时保留它供诊断，正式结果不得部分推进。
- 不创建或切换分支，不创建 worktree，不应用补丁，不构建或运行 Starry，不调用其他 SyscallGuard skill。
