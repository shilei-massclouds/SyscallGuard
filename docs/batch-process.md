# 批次流程

每个批次都使用同一套十步流程。步骤报告放在 `batches/<id>/steps/`，sign-off
放在 `batches/<id>/reviews/`。

| Step | Name | 必需输出 |
| --- | --- | --- |
| 01 | `scope-selection` | 范围、来源、优先级、排除项 |
| 02 | `spec-ingestion` | 来源索引、外部 commit、必要快照和导入行为 |
| 03 | `normalization-review` | 归一化行为规格和审核备注 |
| 04 | `checkability-classification` | `static`、`partial_static`、`dynamic`、`unsupported`、`needs_review` |
| 05 | `starry-evidence-mapping` | Starry 代码、测试、日志或人工审计证据 |
| 06 | `static-check-or-audit` | 静态 checker 结果或人工审计记录 |
| 07 | `gap-triage` | gap、risk、unsupported、needs_review 决策 |
| 08 | `fix-plan-and-apply-outside-harness` | 外部 Starry 修复计划和链接 |
| 09 | `validation` | 构建、静态 checker、动态测试或人工验证结果 |
| 10 | `batch-closeout` | coverage matrix、未解决风险和最终报告 |

## 步骤门禁

每个步骤都要求：

- Markdown 步骤报告。
- YAML review sign-off。
- 明确的输入和输出路径。
- 能追溯到来源索引、复制快照、不可变外部 commit 或已记录 gap。

## 关闭门禁

批次必须满足以下条件后才能标记为 closed：

- 范围内每个行为都出现在 coverage matrix 中。
- 每个 coverage 条目都引用来源规格，以及 Starry 证据、不可变外部引用或 gap。
- 每个 gap 或 risk 都有 triage 决策。
- 每个步骤 sign-off 都是 `confirmed`，或明确为 `not_applicable`。
