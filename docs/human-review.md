# 人工审核

人工审核是第一版的主要质量门禁。自动化可以准备产物，但接受产物必须有明确
的 review 记录。

## 必需字段

每个 sign-off 文件记录：

- `batch_id`
- `step_id`
- `artifact`
- `status`
- `reviewer`
- `reviewed_at`
- `decision_summary`
- `required_changes`
- `follow_up`

## 状态语义

- `pending_human_review`：新产物默认状态。
- `confirmed`：本批次接受该产物。
- `changes_requested`：列出的修改解决前保持阻塞。
- `not_applicable`：按规则跳过，并写明理由。

## 审核清单

- 输入与 batch manifest 和 source index 一致。
- 行为描述足够精确，能够测试或审计。
- 证据路径和 commit 具体明确。
- 不支持或不确定行为已 triage，没有被隐藏。
- coverage matrix 与最终步骤报告一致。

## 屏幕确认格式

每个步骤完成后，助手应在对话中显示一个具体确认块。确认块不写入步骤报告。

确认块顺序：

1. 当前步骤和状态。
2. 需要查看的文件。
3. 本步骤产出或检查的具体列表。
4. 用户需要确认的编号清单。
5. 可回复动作，例如 `批准进入下一步` 或 `修改 <编号>: ...`。

示例：

- 第 01 步先列出选中的 syscall 名称，再询问范围是否正确。
- 第 06 步先列出审计过的 rule ID 和 syscall group，再询问审计范围、证据来源和分级是否可接受。
