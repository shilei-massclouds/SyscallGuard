# 步骤 01 - Scope Selection

批次：`001-syscall-batch-ioctl-renameat2`
状态：`pending_human_review`

## 目的

确定本批要检查的 syscall 范围。默认每批 20 个 syscall，并从
`batches/syscall-check-history.yaml` 排除已完成检查的 syscall。

## 输入

- `manifest.yaml`
- `inputs/source-index.yaml`
- `snapshots/ltp/starry-sources/syscall/mod.rs`
- `batches/syscall-check-history.yaml`

## 执行内容

- 运行 `python3 skills/syscallguard-flow/scripts/next_syscalls.py list --limit 20 --format text`。
- 未发现 `batches/syscall-check-history.yaml`，因此没有可排除的已检查 syscall。
- 从 Starry syscall dispatch 快照中识别到 280 个候选 syscall。
- 选取 dispatch 顺序中的前 20 个 syscall 作为本批范围。

## 待检查 syscall

1. `ioctl`
2. `chdir`
3. `fchdir`
4. `chroot`
5. `mkdir`
6. `mkdirat`
7. `mknod`
8. `mknodat`
9. `getdents64`
10. `link`
11. `linkat`
12. `rmdir`
13. `unlink`
14. `unlinkat`
15. `getcwd`
16. `symlink`
17. `symlinkat`
18. `rename`
19. `renameat`
20. `renameat2`

## 输出

- 范围写入 `manifest.yaml` 的 `scope.included_syscalls`。
- 输入来源写入 `inputs/source-index.yaml`。
- 审核门禁：`reviews/01-scope-selection-signoff.yaml`。

## 缺口和风险

- 当前没有历史文件 `batches/syscall-check-history.yaml`，因此无法排除更早人工检查但未记录的 syscall。
- 本步只确定检查范围，不判断 syscall 语义正确性。

## 审核

- Sign-off：`reviews/01-scope-selection-signoff.yaml`
- 请确认本批 20 个 syscall 是否合理；如需调整，请直接修改本文件和 `manifest.yaml` 的 `scope.included_syscalls`。
