# 协作模型

SyscallGuard 将 harness 流程职责和外部实现工作分开管理。

## 角色

- Harness owner：维护流程、模板、约束、schema 和批次一致性。
- Spec reviewer：检查行为描述是否有来源支撑，是否已归一化到可分类程度。
- Starry evidence reviewer：检查行为到 Starry 代码、测试、日志或人工审计记录的映射。
- Validation owner：记录外部仓库中的构建、静态检查、动态测试或人工验证结果。
- Closeout reviewer：归档前确认可追溯性、triage 决策和未解决风险。

## Review 状态值

- `pending_human_review`：产物已准备好审核，但尚未接受。
- `confirmed`：审核人接受该产物用于本批次。
- `changes_requested`：审核人要求修改，问题解决前不能接受。
- `not_applicable`：该门禁被明确跳过，并写明理由。

## 规则

- 审核人必须检查输入和输出后，才能将步骤标记为 `confirmed`。
- 自动化可以起草步骤产物，但必须更新人工 sign-off 文件后才算接受。
- 外部仓库证据必须记录路径；可用时还要记录 commit 或 branch，以及捕获日期。
- 如果证据缺失，批次必须记录 gap，不能静默省略该行为。
