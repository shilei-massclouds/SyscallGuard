# 工具接入计划

本文记录可复用外部工具的后续接入方向。这里的内容不是任何批次步骤的证据；只有工具
实际运行并把输出登记到批次产物后，才算该批次的输入或验证结果。

## LTP 工具

### `tools/syscall_spec_extract.py`

来源：`~/gitStudy/ltp/tools/syscall_spec_extract.py`

定位：第 02 步 `spec-ingestion` 和第 03 步 `normalization-review` 的候选输入工具。

SyscallGuard 适配入口：

```bash
python3 skills/syscallguard-flow/scripts/run_ltp_spec_extract.py batches/<batch-id>
```

用途：

- 从 LTP 测试源码抽取 `TST_EXP_*`、旧 `TEST()` 和部分 SAFE helper 调用。
- 生成 raw candidates、normalized specs 和摘要报告。
- 帮助把测试源码中的 syscall 行为提升为可审核规格。

当前接入状态：

- 已有只读 batch wrapper，会读取 `manifest.yaml` 中的 `scope.included_syscalls`。
- wrapper 会生成 extractor 兼容 manifest，并把 raw candidates、normalized specs 和摘要写入
  批次 `outputs/`。
- wrapper 会在 `inputs/source-index.yaml` 的 `tool_runs.ltp_spec_extract` 中记录 LTP 仓库路径、
  commit、工具路径和输出文件。
- `getdents64` 等 LTP 目录名不完全一致的 syscall 通过 extractor alias 表映射。
- 保留人工 review；该工具输出不能直接作为 closeout 结论。

剩余工作：

- 将 normalized specs 进一步对齐到 SyscallGuard 的 `syscall -> rule_refs -> target mappings`
  两表/三层模型。
- 决定这些输出是在返工第 02/03 步时作为新输入，还是仅作为下一批初始化参考。

### `tools/starry_static_check.py`

来源：`~/gitStudy/ltp/tools/starry_static_check.py`

定位：第 06 步 `static-check-or-audit` 的候选实现基础。

SyscallGuard 适配入口：

```bash
python3 skills/syscallguard-flow/scripts/run_starry_static_check.py batches/<batch-id>
```

用途：

- 对 Starry 源码执行 pattern-based 静态检查。
- 适合验证已经人工定义清楚的 guard pattern 是否仍存在。

当前接入状态：

- 已有 SyscallGuard 侧 wrapper，会从批次 `inputs/source-index.yaml` 推断外部 Starry repo。
- 已新增参数化规则文件 `skills/syscallguard-flow/references/starry-static-rules.yaml`，不再依赖
  LTP 脚本中的旧 pilot 硬编码规则。
- wrapper 输出 `outputs/starry-static-check-results.yaml` 和
  `outputs/starry-static-check-summary.md`，并在 `inputs/source-index.yaml` 的
  `tool_runs.starry_static_check` 中登记。
- 结果状态保持为 `static_audit_supports`、`partial_static_audit_supports`、
  `static_audit_supports_for_bad_fd`、`missing_pattern` 或 `needs_review` 等审计状态，
  不能直接写成 `covered`。

剩余工作：

- 继续把规则文件从当前 001 批次扩展为通用 reusable rule table / batch mapping 输入。
- 若要把 checker 输出替换第 06 步人工审计，需要显式返工第 06 步并重新走 sign-off。
- 它只能证明 pattern 存在，不能单独证明完整 syscall 语义。

## 记录规则

- 工具适配计划放在本文或流程文档中。
- 工具运行结果放在具体批次目录中，并由对应步骤 sign-off 审核。
- 不把“工具是否有用”的讨论写入步骤报告；步骤报告只记录实际输入、执行内容、证据、
  输出和限制。
