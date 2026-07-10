# syscall normalized specs 摘要

本报告由 `tools/syscall_spec_extract.py` 生成，统计从 raw candidates 提升后的保守规格。

- normalized spec 总数：289
- status：dynamic_required=72, needs_review=102, normalized=115
- checkability：dynamic_required=72, needs_review=24, static_direct=58, static_interprocedural=135
- confidence：A=23, C=164, D=102

| syscall | total | normalized | dynamic_required | needs_review |
| --- | ---: | ---: | ---: | ---: |
| `chdir` | 18 | 2 | 0 | 16 |
| `chroot` | 8 | 8 | 0 | 0 |
| `fchdir` | 3 | 2 | 0 | 1 |
| `getcwd` | 5 | 5 | 0 | 0 |
| `getdents64` | 5 | 5 | 0 | 0 |
| `ioctl` | 112 | 50 | 52 | 10 |
| `link` | 20 | 2 | 0 | 18 |
| `linkat` | 1 | 0 | 0 | 1 |
| `mkdir` | 14 | 2 | 0 | 12 |
| `mkdirat` | 2 | 0 | 0 | 2 |
| `mknod` | 18 | 10 | 8 | 0 |
| `mknodat` | 10 | 0 | 0 | 10 |
| `rename` | 30 | 13 | 12 | 5 |
| `renameat` | 8 | 0 | 0 | 8 |
| `renameat2` | 2 | 0 | 0 | 2 |
| `rmdir` | 12 | 0 | 0 | 12 |
| `symlink` | 4 | 3 | 0 | 1 |
| `symlinkat` | 1 | 0 | 0 | 1 |
| `unlink` | 14 | 13 | 0 | 1 |
| `unlinkat` | 2 | 0 | 0 | 2 |

## 说明

- `normalized`：可以进入 Starry 静态检查输入。
- `dynamic_required`：规格可表达，但主要依赖运行时行为确认。
- `needs_review`：旧 API、复杂分支或 helper 语义还需要人工/定向规则提升。
- `checkability=static_direct` 的行优先用于 Starry errno/flag/fd/path 静态扫描。
