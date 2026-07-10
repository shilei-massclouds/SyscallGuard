# 步骤 06 - Static Check Or Audit

批次：`000-regression-baseline`
状态：`ready_for_human_review`

## 目的

记录第一版人工静态审计结果。本 harness 修订版不包含自动 checker。

## 人工审计摘要

- `path-max-enametoolong`：`vm_load_path_string` 拒绝 `path.len() >= PATH_MAX`
  的路径，并映射为 `NameTooLong`。
- `pipe2-copyout-fd-rollback`：如果 `fds.vm_write([read_fd, write_fd])` 失败，
  `sys_pipe2` 会关闭已经分配的两个 fd。
- `x86-creat-alias`：x86_64 `Sysno::creat` dispatch 到 `sys_creat`，后者调用
  `sys_openat(AT_FDCWD, path, O_CREAT|O_WRONLY|O_TRUNC, mode)`。
- `x86-eventfd-alias`：x86_64 `sys_eventfd(initval)` 返回
  `sys_eventfd2(initval, 0)`.
- `mmap04-visible-prot`：`mmap.rs` 保存 reported flags，`proc.rs` 将
  `area.reported_flags()` 渲染到 `/proc/self/maps`。
- `p2-iov-guard`：`validate_user_iov_buf_regions` 检查 `iovcnt`、负 segment
  length、用户态访问和总长度溢出。
- `p2-offset-guard`：offset 路径在使用范围前执行负值检查、`try_into`、对齐检查和
  `checked_add`/`checked_sub`。
- `p2-mremap-guard`：`sys_mremap` 拒绝 new size 为 0、未知 flags、fixed/dontunmap
  缺少 maymove、size mismatch、未对齐、重叠、未映射 source 和越界 size。
- `p2-mincore-guard`：`sys_mincore` 拒绝未对齐 addr、null vec、未映射或非用户
  mapping，并接受 zero length。
- `p2-madvise-guard`：行为由复制的回归测试覆盖，并映射到 `mmap.rs` 中的
  `sys_madvise`。

## 输出

- 审计摘要写入 `outputs/coverage-matrix.yaml`。

## 缺口和风险

- 静态审计为人工完成。自动 AST 或语义检查属于后续工作。
