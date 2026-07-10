# 步骤 01 - Scope Selection

批次：`000-regression-baseline`
状态：`ready_for_human_review`

## 目的

选择一组已修复 Starry syscall 回归项，作为流程 baseline 范围。本批次不用于发现
新的实现缺口。

## 输入

- `manifest.yaml`
- `inputs/source-index.yaml`
- `snapshots/ltp/specs/regression-behavior-specs.yaml`

## 选定行为

- `path-max-enametoolong`
- `pipe2-copyout-fd-rollback`
- `x86-creat-alias`
- `x86-eventfd-alias`
- `mmap04-visible-prot`
- `p2-iov-guard`
- `p2-offset-guard`
- `p2-mremap-guard`
- `p2-mincore-guard`
- `p2-madvise-guard`

## 排除项

- 新 syscall gap 发现。
- 直接修改 Starry 或 LTP 代码。
- 自动化 CLI/checker 实现。

## 输出

- 范围记录在 `manifest.yaml`。
- 审核门禁：`reviews/01-scope-selection-signoff.yaml`。

## 缺口和风险

- 本地没有独立 LTP 和 `new_specs/` 输入。该问题记录为 snapshot gap，不阻塞本
  流程 baseline。
