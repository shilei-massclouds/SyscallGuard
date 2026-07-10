# 步骤 09 - Validation

批次：`000-regression-baseline`
状态：`ready_for_human_review`

## 目的

记录 harness 可用的验证证据。

## 可用验证输入

- 已复制测试源码：
  - `bugfix-bug-open-pathmax-no-enametoolong`
  - `syscall-test-pipe-syscalls`
  - `syscall-test-eventfd2`
  - `syscall-test-open-family`
  - `syscall-test-ltp-pilot-min`
  - `syscall-test-mmap-family`
  - `syscall-test-madvise`
  - `c-regression-test-mremap`
- `snapshots/ltp/starry-sources` 下的 Starry 实现源码快照。

## Harness 验证结果

本版本 SyscallGuard 没有执行 Starry build 或 QEMU test run。因此 coverage matrix
按行为记录为 `manual_audit_only` 或 `not_run`。

## 输出

- `outputs/coverage-matrix.yaml`

## 缺口和风险

- 将动态行为标记为完全 confirmed 前，需要新的动态运行日志。
