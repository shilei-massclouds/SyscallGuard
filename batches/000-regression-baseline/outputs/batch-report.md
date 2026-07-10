# 批次报告 - 000 Regression Baseline

状态：`ready_for_human_review`
Generated: `2026-07-10T00:00:00Z`

## 范围

本批次用已知已修复的 Starry syscall 回归项建立第一个 SyscallGuard 流程 baseline：
`PATH_MAX`、pipe/pipe2 fd rollback、x86_64 `creat` 和 `eventfd` alias、
mmap04 风格 visible prot，以及 iov、offset、mremap、mincore、madvise 的 P2 guard。

## 产物

- Manifest: `manifest.yaml`
- Source index: `inputs/source-index.yaml`
- Step reports: `steps/01-*.md` through `steps/10-*.md`
- Review records: `reviews/01-*-signoff.yaml` through
  `reviews/10-*-signoff.yaml`
- Coverage matrix: `outputs/coverage-matrix.yaml`

## 证据

证据复制自本地 `tgoskits` 分支 `dev-ltp-spec-2`，commit
`4f30e12d17e4da175233bb3a51889efe747a45f9`。复制快照包含相关 Starry
系统测试和实现文件。

## 结果

- 范围内所有行为都出现在 coverage matrix 中。
- 每个 coverage 条目都能追溯到行为规格和 Starry 证据。
- 本批次不声称发现新的 Starry gap。
- 缺失上游 LTP/new_specs 材料和缺少新动态运行日志的问题已记录为 risk。

## 审核状态

批次已准备好进入人工审核。所有 sign-off 文件当前都是 `pending_human_review`；
这些记录解决前，批次不能视为 closed。
