# 工具接入计划

本文记录可复用外部工具的后续接入方向。这里的内容不是任何批次步骤的证据；只有工具
实际运行并把输出登记到批次产物后，才算该批次的输入或验证结果。

## LTP 工具

### `tools/syscall_spec_extract.py`

来源：`~/gitStudy/ltp/tools/syscall_spec_extract.py`

定位：第 02 步 `spec-ingestion` 和第 03 步 `normalization-review` 的候选输入工具。

用途：

- 从 LTP 测试源码抽取 `TST_EXP_*`、旧 `TEST()` 和部分 SAFE helper 调用。
- 生成 raw candidates、normalized specs 和摘要报告。
- 帮助把测试源码中的 syscall 行为提升为可审核规格。

接入前需要处理：

- 参数化输入 manifest，使其能按 SyscallGuard 当前批次的 20 个 syscall 运行。
- 将 normalized specs 映射到 SyscallGuard 的 `syscall -> rule_refs -> target mappings`
  两表/三层模型。
- 在批次 `inputs/source-index.yaml` 中记录 LTP 仓库路径、commit、工具路径和输出文件。
- 保留人工 review；该工具输出不能直接作为 closeout 结论。

### `tools/starry_static_check.py`

来源：`~/gitStudy/ltp/tools/starry_static_check.py`

定位：第 06 步 `static-check-or-audit` 的候选实现基础。

用途：

- 对 Starry 源码执行 pattern-based 静态检查。
- 适合验证已经人工定义清楚的 guard pattern 是否仍存在。

当前限制：

- 现有规则写死在脚本中，覆盖的是旧 pilot 行为，不覆盖当前 001 批次的完整
  `syscall + rule_id` 工作队列。
- 它只能证明 pattern 存在，不能单独证明完整 syscall 语义。

接入前需要处理：

- 将规则输入参数化，改为读取 SyscallGuard reusable rule table 或批次 mapping。
- 输出结构化结果，能写入第 06 步报告或专门的 checker output。
- 通过 source index 读取 external Starry commit，不默认复制 Starry 源码到本仓库。
- 结果状态应保持为 `static_audit_supports`、`missing_pattern`、`needs_review` 等审计
  状态，不能直接写成 `covered`。

## 记录规则

- 工具适配计划放在本文或流程文档中。
- 工具运行结果放在具体批次目录中，并由对应步骤 sign-off 审核。
- 不把“工具是否有用”的讨论写入步骤报告；步骤报告只记录实际输入、执行内容、证据、
  输出和限制。
