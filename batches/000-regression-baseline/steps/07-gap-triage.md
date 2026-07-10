# 步骤 07 - Gap Triage

批次：`000-regression-baseline`
状态：`ready_for_human_review`

## 目的

确认范围内行为暴露的是新的 Starry gap，还是流程/来源 gap。

## Triage 决策

- 本批次不声称发现新的 Starry 实现 gap。
- 本地工作区缺少独立 LTP 方法文档、100 syscall 摘要和 `new_specs/` 四层规格。
  这是 source snapshot gap。
- SyscallGuard 第一版未执行动态验证。外部结果审核前，coverage 条目保持
  `covered_pending_human_review`。
- `p2-mincore-guard` 有静态证据，但没有复制到专用动态测试。

## 输出

- Triage 状态记录在 `outputs/coverage-matrix.yaml`。

## 缺口和风险

- Source gap：缺少上游 LTP/new_specs 产物。
- Validation gap：本仓库没有捕获新的 QEMU 运行结果。
