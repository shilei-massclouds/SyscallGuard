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
