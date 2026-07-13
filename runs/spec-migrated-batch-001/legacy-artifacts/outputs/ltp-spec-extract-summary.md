# syscall 提取摘要

本报告由 `tools/syscall_spec_extract.py` 生成。
当前只统计原始候选：`TST_EXP_*`、部分旧 `TEST()` 用法和少量 SAFE helper。setup 派生语义尚未归一化。

- manifest 中 syscall 数量：20
- manifest 分组：syscallguard_batch=20
- 原始目标候选行：174

- 可做简单 testcase array 展开的候选：20
- 展开后的 raw case 数：135

| syscall | 分组 | C 文件数 | TST_EXP 宏数 | 目标候选数 | 旧 API 标记数 | 候选类型 |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `ioctl` | syscallguard_batch | 39 | 78 | 88 | 14 | fail:17, old_api_errno_check:8, old_api_probe:1, old_api_return_check:1, property_eq:42, property_expr:10, success:9 |
| `chdir` | syscallguard_batch | 3 | 2 | 4 | 3 | fail:1, old_api_probe:2, success:1 |
| `fchdir` | syscallguard_batch | 3 | 2 | 3 | 1 | fail:1, old_api_errno_check:1, success:1 |
| `chroot` | syscallguard_batch | 4 | 5 | 4 | 0 | fail:3, success:1 |
| `mkdir` | syscallguard_batch | 5 | 4 | 4 | 2 | fail:1, old_api_errno_check:1, old_api_probe:1, success:1 |
| `mkdirat` | syscallguard_batch | 2 | 0 | 2 | 9 | old_api_errno_check:2 |
| `mknod` | syscallguard_batch | 9 | 13 | 13 | 0 | fail:3, property_eq:8, success:2 |
| `mknodat` | syscallguard_batch | 2 | 0 | 2 | 17 | old_api_errno_check:2 |
| `getdents64` | syscallguard_batch | 2 | 1 | 1 | 0 | fail:1 |
| `link` | syscallguard_batch | 4 | 2 | 4 | 2 | old_api_errno_check:2, success:2 |
| `linkat` | syscallguard_batch | 2 | 0 | 1 | 19 | old_api_errno_check:1 |
| `rmdir` | syscallguard_batch | 3 | 0 | 3 | 3 | old_api_errno_check:2, old_api_probe:1 |
| `unlink` | syscallguard_batch | 5 | 4 | 5 | 2 | fail:4, old_api_probe:1 |
| `unlinkat` | syscallguard_batch | 1 | 0 | 2 | 2 | old_api_errno_check:2 |
| `getcwd` | syscallguard_batch | 4 | 1 | 1 | 0 | fail:1 |
| `symlink` | syscallguard_batch | 3 | 2 | 3 | 10 | old_api_errno_check:1, positive:1, success:1 |
| `symlinkat` | syscallguard_batch | 1 | 0 | 1 | 12 | old_api_errno_check:1 |
| `rename` | syscallguard_batch | 14 | 42 | 30 | 17 | fail:8, old_api_errno_check:2, old_api_probe:3, property_eq:12, success:5 |
| `renameat` | syscallguard_batch | 1 | 0 | 1 | 14 | old_api_errno_check:1 |
| `renameat2` | syscallguard_batch | 2 | 0 | 2 | 23 | old_api_probe:1, old_api_return_check:1 |

## 直接观察

- `目标候选数` 仍是原始候选，需要 testcase array 展开和 setup 标签后才能提升为规范化规格。
- `old_api_*` 候选来自旧 `TEST()` 风格，需要重建期望返回值和 errno。
- `safe_helper_success` 候选来自 SAFE helper，只能表示该 helper 期望成功，后续要关联属性检查。
- `fcntl` 和 `mmap` 这类大目录应按子命令或行为类别拆分。
- property assertion 需要和前一个 syscall 返回值或对象状态关联。
- `expanded_cases` 只是机械替换 `tc->field`，遇到分支条件时还需要 branch filtering。
