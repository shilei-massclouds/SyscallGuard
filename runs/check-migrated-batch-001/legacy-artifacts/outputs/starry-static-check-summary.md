# Starry Static Check Summary

Batch: `001-syscall-batch-ioctl-renameat2`
Generated: `2026-07-10T08:22:01Z`
Starry repo: `/home/cloud/gitLinux/tgoskits`
Starry commit: `4f30e12d17e4da175233bb3a51889efe747a45f9`

These results are static audit inputs only. They do not mark behavior as covered.

| Status | Rule | Source | Evidence |
| --- | --- | --- | --- |
| `static_audit_supports` | `SG001_ENTRY_DISPATCH` | `os/StarryOS/kernel/src/syscall/mod.rs` | ioctl dispatch: line 84<br>chdir dispatch: line 85<br>fchdir dispatch: line 86<br>chroot dispatch: line 87<br>mkdir dispatch: line 89<br>mkdirat dispatch: line 90<br>mknod dispatch: line 92<br>mknodat dispatch: line 93<br>getdents64 dispatch: line 99<br>link dispatch: line 101<br>linkat dispatch: line 102<br>rmdir dispatch: line 110<br>unlink dispatch: line 112<br>unlinkat dispatch: line 113<br>getcwd dispatch: line 114<br>symlink dispatch: line 116<br>symlinkat dispatch: line 117<br>rename dispatch: line 119<br>renameat dispatch: line 121<br>renameat2 dispatch: line 127 |
| `static_audit_supports` | `SG001_LEGACY_WRAPPERS` | `os/StarryOS/kernel/src/syscall/fs/ctl.rs` | mkdir delegates to mkdirat: line 105<br>mknod delegates to mknodat: line 110<br>link delegates to linkat: line 328<br>rmdir delegates to unlinkat: line 409<br>unlink delegates to unlinkat: line 378<br>symlink delegates to symlinkat: line 436<br>rename delegates to renameat: line 758<br>renameat delegates to renameat2: line 763 |
| `static_audit_supports_for_bad_fd` | `SG001_BAD_FD_EBADF` | `os/StarryOS/kernel/src/file/mod.rs` | get_file_like maps missing fd to BadFileDescriptor: line 275 |
| `partial_static_audit_supports` | `SG001_FD_TYPE_ERRNO` | `os/StarryOS/kernel/src/file/fs.rs` | File::from_fd distinguishes directory and other types: line 252<br>Directory::from_fd maps non-directory to NotADirectory: line 312 |
| `static_audit_supports` | `SG001_FLAG_MASKS` | `os/StarryOS/kernel/src/syscall/fs/ctl.rs` | linkat valid flags mask: line 335<br>unlinkat rejects unknown flags: line 386<br>renameat2 supported flags mask: line 780 |
| `partial_static_audit_supports` | `SG001_PATHMAX_HELPER` | `os/StarryOS/kernel/src/mm/access.rs` | PATH_MAX constant: line 288<br>vm_load_path_string rejects long paths: line 296 |
| `partial_static_audit_supports` | `SG001_PATH_HANDLER_LOADS` | `os/StarryOS/kernel/src/syscall/fs/ctl.rs` | chdir path loader: line 86<br>chroot path loader: line 114<br>mkdirat path loader: line 160<br>mknodat path loader: line 193<br>linkat old/new path loaders: line 328<br>unlinkat path loader: line 378<br>symlinkat linkpath loader: line 440<br>renameat2 old/new path loaders: line 773 |
| `partial_static_audit_supports` | `SG001_USERPTR_EFAULT` | `os/StarryOS/kernel/src/syscall/fs/ctl.rs` | ioctl reads user integer pointer: line 47<br>getdents64 writes user buffer: line 294<br>getcwd writes user buffer: line 418 |
| `partial_static_audit_supports` | `SG001_MODE_NODE_GUARD` | `os/StarryOS/kernel/src/syscall/fs/ctl.rs` | mkdirat applies umask and fs ids: line 160<br>mknodat rejects directory and unknown node types: line 193 |
