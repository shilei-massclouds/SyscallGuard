# 步骤 02 - Spec Ingestion

批次：`000-regression-baseline`
状态：`ready_for_human_review`

## 目的

从本地可用快照导入行为规格，并记录来源版本。

## 输入

- `snapshots/ltp/source-index.yaml`
- `snapshots/ltp/specs/regression-behavior-specs.yaml`
- `snapshots/ltp/test-sources/`
- `snapshots/ltp/starry-sources/`

## 执行内容

- 捕获本地 `tgoskits` 分支 `dev-ltp-spec-2`。
- 捕获本地 `tgoskits` commit
  `4f30e12d17e4da175233bb3a51889efe747a45f9`.
- 将相关测试和 Starry 源码复制到 `snapshots/ltp/`。
- 将不可用的 LTP 方法文档、100 syscall 摘要和 `new_specs/` 材料记录为
  snapshot gap。

## 输出

- `inputs/source-index.yaml`
- `snapshots/ltp/source-index.yaml`
- `snapshots/ltp/specs/regression-behavior-specs.yaml`

## 缺口和风险

- 本批次行为规格由复制的测试和 Starry 证据手工归一化。后续批次拿到上游 LTP
  四层规格后，应替换或补充这些记录。
