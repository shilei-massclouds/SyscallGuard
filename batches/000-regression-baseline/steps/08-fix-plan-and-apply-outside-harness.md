# 步骤 08 - Fix Plan And Apply Outside Harness

批次：`000-regression-baseline`
状态：`ready_for_human_review`

## 目的

记录修复状态，同时保持 SyscallGuard 不修改 Starry 或 LTP 的边界。

## 修复状态

对本 baseline 而言，范围内所有行为都视为已经在引用的本地 `tgoskits` checkout
中修复或实现。

外部来源：

- Repository: `/home/cloud/gitLinux/tgoskits`
- Branch: `dev-ltp-spec-2`
- Commit: `4f30e12d17e4da175233bb3a51889efe747a45f9`

## 输出

- 修复状态反映在 `outputs/coverage-matrix.yaml`。

## 缺口和风险

- 并非每个行为都捕获了 pull request URL 或 release tag。
- 后续批次应为每个修复包含不可变外部链接。
