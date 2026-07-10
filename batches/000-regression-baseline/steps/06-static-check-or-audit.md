# Step 06 - Static Check Or Audit

Batch: `000-regression-baseline`
Status: `ready_for_human_review`

## Purpose

Record version 1 manual static audit results. No automated checker is included
in this harness revision.

## Manual Audit Summary

- `path-max-enametoolong`: `vm_load_path_string` rejects paths with
  `path.len() >= PATH_MAX` and maps to `NameTooLong`.
- `pipe2-copyout-fd-rollback`: `sys_pipe2` closes both allocated fds if
  `fds.vm_write([read_fd, write_fd])` fails.
- `x86-creat-alias`: x86_64 `Sysno::creat` dispatches to `sys_creat`, which
  calls `sys_openat(AT_FDCWD, path, O_CREAT|O_WRONLY|O_TRUNC, mode)`.
- `x86-eventfd-alias`: x86_64 `sys_eventfd(initval)` returns
  `sys_eventfd2(initval, 0)`.
- `mmap04-visible-prot`: `mmap.rs` stores reported flags and `proc.rs` renders
  `area.reported_flags()` into `/proc/self/maps`.
- `p2-iov-guard`: `validate_user_iov_buf_regions` checks `iovcnt`, negative
  segment length, user access, and total length overflow.
- `p2-offset-guard`: offset paths use negative checks, `try_into`, alignment
  checks, and `checked_add`/`checked_sub` before range use.
- `p2-mremap-guard`: `sys_mremap` rejects zero new size, unknown flags,
  fixed/dontunmap without maymove, size mismatch, alignment, overlap, unmapped
  source, and out-of-range sizes.
- `p2-mincore-guard`: `sys_mincore` rejects unaligned addr, null vec, unmapped
  or non-user mappings, and accepts zero length.
- `p2-madvise-guard`: behavior is covered by copied regression test and
  mapped to `sys_madvise` in `mmap.rs`.

## Outputs

- Audit summary included in `outputs/coverage-matrix.yaml`.

## Gaps And Risks

- Static audit was manual. Automated AST or semantic checks are future work.

