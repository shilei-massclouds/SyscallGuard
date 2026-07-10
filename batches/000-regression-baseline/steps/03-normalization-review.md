# 步骤 03 - Normalization Review

批次：`000-regression-baseline`
状态：`ready_for_human_review`

## 目的

检查导入的行为描述是否足够精确，可用于分类和证据映射。

## 输入

- `snapshots/ltp/specs/regression-behavior-specs.yaml`

## 归一化决策

- 架构相关 alias 范围限定为 `x86_64`。
- 错误返回行为保留预期 errno 名称。
- `pipe2-copyout-fd-rollback` 同时保留外部可见的 `EFAULT` 和内部 fd rollback 要求。
- `mmap04-visible-prot` 限定为 `/proc/self/maps` 可见权限，而不是硬件页表权限。
- P2 guard 按 iov、offset、mremap、mincore、madvise 拆分。

## 输出

- 归一化行为记录保留在
  `snapshots/ltp/specs/regression-behavior-specs.yaml`.

## 缺口和风险

- 手工归一化记录尚未由上游 spec reviewer 确认。
