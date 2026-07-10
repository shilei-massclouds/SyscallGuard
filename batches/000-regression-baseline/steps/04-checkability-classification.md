# 步骤 04 - Checkability Classification

批次：`000-regression-baseline`
状态：`ready_for_human_review`

## 目的

按 SyscallGuard 第一版可检查方式，为每个行为分类。

## 分类

| 行为 | Checkability | 理由 |
| --- | --- | --- |
| `path-max-enametoolong` | `partial_static` | 有静态路径长度 guard，也有复制的动态回归测试。 |
| `pipe2-copyout-fd-rollback` | `partial_static` | 代码审计能看到 rollback；fd leak 仍适合动态验证。 |
| `x86-creat-alias` | `partial_static` | dispatch 和 helper 可静态审计；测试检查 mode 和 fd 行为。 |
| `x86-eventfd-alias` | `partial_static` | dispatch 和 helper 可静态审计；eventfd2 行为需要动态验证。 |
| `mmap04-visible-prot` | `dynamic` | 需要观察 `/proc/self/maps`。 |
| `p2-iov-guard` | `static` | guard 逻辑本地可读。 |
| `p2-offset-guard` | `static` | guard 逻辑本地可读。 |
| `p2-mremap-guard` | `partial_static` | 静态 guard 加较完整回归测试。 |
| `p2-mincore-guard` | `static` | guard 逻辑本地可读。 |
| `p2-madvise-guard` | `partial_static` | 静态 guard 加复制的回归测试。 |

## 输出

- Checkability 值记录在 `outputs/coverage-matrix.yaml`。

## 缺口和风险

- 本 harness 版本未执行动态命令。
