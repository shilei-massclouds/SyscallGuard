# Syscall 合规性规则提取报告

## 结论

本次分析了 memcpy、memfd_create、memset、migrate_pages、mincore、mkdir、mkdirat、mknod、mknodat、mlock、mlock2、mlockall、mmap、modify_ldt、mount、mount_setattr、move_mount、move_pages、mprotect、mq_notify、mq_open、mq_timedreceive、mq_timedsend、mq_unlink、mremap、mseal、msync、munlock、munlockall、munmap、name_to_handle_at、nanosleep、newuname、nftw、nice、open、open_by_handle_at、open_tree、openat、openat2、pathconf、pause、perf_event_open、personality、pidfd_getfd、pidfd_open、pidfd_send_signal、pipe、pipe2、pivot_root、pkeys、poll、ppoll、prctl、pread64、preadv、preadv2、process_madvise、profil、pselect、ptrace、pwrite64、pwritev、pwritev2、quotactl、read、readahead、readdir、readlink、readlinkat、readv、realpath、reboot、recv、recvfrom、recvmmsg、recvmsg、remap_file_pages、removexattr、rename，发现 268 条可执行的合规性规则。

## `memcpy`

没有形成可发布的合规性规则。

## `memfd_create`

没有形成可发布的合规性规则。

## `memset`

没有形成可发布的合规性规则。

## `migrate_pages`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_FE4A57F142065A14`](../../library/rules/ltp-fe4a57f142065a14.yaml) | 无额外前置条件 | 调用 migrate_pages(pid, max_node, old_nodes, new_nodes) | {'kind': 'return_value', 'return': '0'} |
## `mincore`

共形成 4 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_34A03F3861C10C4E`](../../library/rules/ltp-34a03f3861c10c4e.yaml) | BAD_USER_ADDRESS | 调用 mincore(NULL, 0, NULL) | 返回 -1，errno 为 EFAULT |
| [`LTP_3A18518E9A9DDC47`](../../library/rules/ltp-3a18518e9a9ddc47.yaml) | 无额外前置条件 | 调用 mincore(addr, size, vec) | 调用成功，返回 SUCCESS |
| [`LTP_4032B15A045CC9CD`](../../library/rules/ltp-4032b15a045cc9cd.yaml) | 无额外前置条件 | 调用 mincore(NULL, 0, NULL) | 返回 -1，errno 为 EINVAL |
| [`LTP_A426BD8C5041DE5E`](../../library/rules/ltp-a426bd8c5041de5e.yaml) | 无额外前置条件 | 调用 mincore(NULL, 0, NULL) | 返回 -1，errno 为 ENOMEM |
## `mkdir`

没有形成可发布的合规性规则。

## `mkdirat`

共形成 9 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_01E0E5231C9C3654`](../../library/rules/ltp-01e0e5231c9c3654.yaml) | 无额外前置条件 | 调用 mkdirat(dir_fd, abspath, 0600) | 返回 0，errno 为 0 |
| [`LTP_6174E3690A05F1CA`](../../library/rules/ltp-6174e3690a05f1ca.yaml) | 无额外前置条件 | 调用 mkdirat(dir_fd, TEST_DIR, 0777) | 返回 -1，errno 为 EROFS |
| [`LTP_9D233BC9DED7A8AA`](../../library/rules/ltp-9d233bc9ded7a8aa.yaml) | NON_DIRECTORY_PATH_COMPONENT | 调用 mkdirat(fd, relpath, 0600) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_B917BA457313E93D`](../../library/rules/ltp-b917ba457313e93d.yaml) | SYMLINK_LOOP | 调用 mkdirat(cur_fd, test_dir, 0777) | 返回 -1，errno 为 ELOOP |
| [`LTP_BBBCFD7524CBB3CD`](../../library/rules/ltp-bbbcfd7524cbb3cd.yaml) | 无额外前置条件 | 调用 mkdirat(dir_fd, relpath, 0600) | 返回 0，errno 为 0 |
| [`LTP_D2E5AAE97E0E50FE`](../../library/rules/ltp-d2e5aae97e0e50fe.yaml) | 无额外前置条件 | 调用 mkdirat(fd_atcwd, relpath, 0600) | 返回 0，errno 为 0 |
| [`LTP_EE540E689227BDBF`](../../library/rules/ltp-ee540e689227bdbf.yaml) | SYMLINK_LOOP | 调用 mkdirat(dir_fd, test_dir, 0777) | 返回 -1，errno 为 ELOOP |
| [`LTP_F6DD03A9DC1C07D4`](../../library/rules/ltp-f6dd03a9dc1c07d4.yaml) | 无额外前置条件 | 调用 mkdirat(cur_fd, TEST_DIR, 0777) | 返回 -1，errno 为 EROFS |
| [`LTP_FE8AA14F6A64DF2D`](../../library/rules/ltp-fe8aa14f6a64df2d.yaml) | 文件描述符无效 | 调用 mkdirat(fd_invalid, relpath, 0600) | 返回 -1，errno 为 EBADF |
## `mknod`

没有形成可发布的合规性规则。

## `mknodat`

没有形成可发布的合规性规则。

## `mlock`

共形成 7 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_04FC167B4A1C57FB`](../../library/rules/ltp-04fc167b4a1c57fb.yaml) | 无额外前置条件 | 调用 mlock(addr, len) | 返回 -1，errno 为 ENOMEM |
| [`LTP_1C1877AB6CAE8906`](../../library/rules/ltp-1c1877ab6cae8906.yaml) | 无额外前置条件 | 调用 mlock(addr, 1024) | 调用成功，返回 SUCCESS |
| [`LTP_4ED7FF29685C11B0`](../../library/rules/ltp-4ed7ff29685c11b0.yaml) | USER_BUFFER | 调用 mlock(buf, file_len) | 调用成功，返回 SUCCESS |
| [`LTP_8C796FAE0FBF7688`](../../library/rules/ltp-8c796fae0fbf7688.yaml) | 无额外前置条件 | 调用 mlock(addr, len) | 返回 -1，errno 为 EPERM |
| [`LTP_C05360D699C55915`](../../library/rules/ltp-c05360d699c55915.yaml) | 无额外前置条件 | 调用 mlock(addr, 1024 * 1024) | 调用成功，返回 SUCCESS |
| [`LTP_F61B5384B4A60F55`](../../library/rules/ltp-f61b5384b4a60f55.yaml) | 无额外前置条件 | 调用 mlock(addr, 1) | 调用成功，返回 SUCCESS |
| [`LTP_FC50E16C03A7EED9`](../../library/rules/ltp-fc50e16c03a7eed9.yaml) | 无额外前置条件 | 调用 mlock(addr, 1024 * 1024 * 10) | 调用成功，返回 SUCCESS |
## `mlock2`

共形成 14 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_074981FFB7FA5DB7`](../../library/rules/ltp-074981ffb7fa5db7.yaml) | 无额外前置条件 | 调用 mlock2(addr, 2 * pgsz + 1, 0) | 返回 0，errno 为 EINVAL |
| [`LTP_16B8EA75C5016419`](../../library/rules/ltp-16b8ea75c5016419.yaml) | 无额外前置条件 | 调用 mlock2(unmapped_addr, pgsz, 0) | 返回 -1，errno 为 ENOMEM |
| [`LTP_2FDCA4DAED71F98B`](../../library/rules/ltp-2fdca4daed71f98b.yaml) | 无额外前置条件 | 调用 mlock2(addr, pgsz, 0) | 返回 -1，errno 为 EPERM |
| [`LTP_3471B46784E57E93`](../../library/rules/ltp-3471b46784e57e93.yaml) | 无额外前置条件 | 调用 mlock2(addr, PAGES * pgsz + 0, 0) | 返回 0，errno 为 EINVAL |
| [`LTP_592639F40E0FF63A`](../../library/rules/ltp-592639f40e0ff63a.yaml) | 无额外前置条件 | 调用 mlock2(addr, 1 * pgsz + 0, 0) | 返回 0，errno 为 EINVAL |
| [`LTP_669BB2DCB1D95979`](../../library/rules/ltp-669bb2dcb1d95979.yaml) | 无额外前置条件 | 调用 mlock2(addr, pgsz, 0) | 返回 -1，errno 为 ENOMEM |
| [`LTP_715AAC0BA45C0567`](../../library/rules/ltp-715aac0ba45c0567.yaml) | 文件描述符无效 | 调用 mlock2(addr, 2 * pgsz + -1, 0) | 返回 0，errno 为 EINVAL |
| [`LTP_7C995D43920E57D0`](../../library/rules/ltp-7c995d43920e57d0.yaml) | 无额外前置条件 | 调用 mlock2(addr, HPAGES * pgsz + 1, MLOCK_ONFAULT) | 返回 0，errno 为 EINVAL |
| [`LTP_8731C07ADFDC57F6`](../../library/rules/ltp-8731c07adfdc57f6.yaml) | 无额外前置条件 | 调用 mlock2(addr, pgsz, MLOCK_ONFAULT) | 返回 0，errno 为 EINVAL |
| [`LTP_9869F02C8AF1851D`](../../library/rules/ltp-9869f02c8af1851d.yaml) | 文件描述符无效 | 调用 mlock2(addr, HPAGES * pgsz + -1, MLOCK_ONFAULT) | 返回 0，errno 为 EINVAL |
| [`LTP_D191923C5ACBADC1`](../../library/rules/ltp-d191923c5acbadc1.yaml) | 无额外前置条件 | 调用 mlock2(addr, pgsz, 0) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_D9418F7424E86C28`](../../library/rules/ltp-d9418f7424e86c28.yaml) | 文件描述符无效 | 调用 mlock2(addr, pgsz, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_F7AC6006DC3C06BB`](../../library/rules/ltp-f7ac6006dc3c06bb.yaml) | 无额外前置条件 | 调用 mlock2(addr, PAGES * pgsz + 0, MLOCK_ONFAULT) | 返回 0，errno 为 EINVAL |
| [`LTP_FE9B97F71E485E58`](../../library/rules/ltp-fe9b97f71e485e58.yaml) | 无额外前置条件 | 调用 mlock2(addr, 1 * pgsz + 0, MLOCK_ONFAULT) | 返回 0，errno 为 EINVAL |
## `mlockall`

共形成 7 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_06EAAEA7DDC8627E`](../../library/rules/ltp-06eaaea7ddc8627e.yaml) | 无额外前置条件 | 调用 mlockall(MCL_CURRENT | MCL_FUTURE) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_0D59D1FBC322425B`](../../library/rules/ltp-0d59d1fbc322425b.yaml) | 无额外前置条件 | 调用 mlockall(MCL_CURRENT) | 返回 -1，errno 为 EPERM |
| [`LTP_154DEC6769244339`](../../library/rules/ltp-154dec6769244339.yaml) | 无额外前置条件 | 调用 mlockall(~(MCL_CURRENT | MCL_FUTURE)) | 返回 -1，errno 为 EINVAL |
| [`LTP_6F89F9EF4C3D3857`](../../library/rules/ltp-6f89f9ef4c3d3857.yaml) | 无额外前置条件 | 调用 mlockall(MCL_CURRENT) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_C054C1DCF56C7CDC`](../../library/rules/ltp-c054c1dcf56c7cdc.yaml) | 无额外前置条件 | 调用 mlockall(MCL_CURRENT) | 返回 -1，errno 为 ENOMEM |
| [`LTP_CD185859D6C012C8`](../../library/rules/ltp-cd185859d6c012c8.yaml) | 无额外前置条件 | 调用 mlockall(0) | 返回 -1，errno 为 EINVAL |
| [`LTP_D7FFD8EE209AB524`](../../library/rules/ltp-d7ffd8ee209ab524.yaml) | 无额外前置条件 | 调用 mlockall(MCL_FUTURE) | {'kind': 'return_value', 'return': '-1'} |
## `mmap`

共形成 9 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_36C99C10CD38F8DB`](../../library/rules/ltp-36c99c10cd38f8db.yaml) | PERMISSION_DENIED_STATE | 调用 mmap(NULL, MMAPSIZE, PROT_READ | PROT_WRITE, MAP_FILE | MAP_PRIVATE, fd, 0) | 返回 -1，errno 为 EACCES |
| [`LTP_45439D8F2BAB0832`](../../library/rules/ltp-45439d8f2bab0832.yaml) | PERMISSION_DENIED_STATE | 调用 mmap(NULL, MMAPSIZE, PROT_WRITE, MAP_FILE | MAP_SHARED, fd, 0) | 返回 -1，errno 为 EACCES |
| [`LTP_51E295101A9F4411`](../../library/rules/ltp-51e295101a9f4411.yaml) | 无额外前置条件 | 调用 mmap(NULL, 0, PROT_READ | PROT_WRITE, MAP_FILE | MAP_SHARED, fd, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_52BAFC01DEA6E172`](../../library/rules/ltp-52bafc01dea6e172.yaml) | PERMISSION_DENIED_STATE | 调用 mmap(NULL, MMAPSIZE, PROT_READ, MAP_FILE | MAP_SHARED, fd, 0) | 返回 -1，errno 为 EACCES |
| [`LTP_791DEA825D66980B`](../../library/rules/ltp-791dea825d66980b.yaml) | 无额外前置条件 | 调用 mmap(NULL, page_sz, PROT_WRITE, MAP_FILE | MAP_SHARED, fd, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_C346EFF1233F7061`](../../library/rules/ltp-c346eff1233f7061.yaml) | PERMISSION_DENIED_STATE | 调用 mmap(NULL, MMAPSIZE, PROT_WRITE, MAP_FILE | MAP_PRIVATE, fd, 0) | 返回 -1，errno 为 EACCES |
| [`LTP_F36F8C0CC1A6D840`](../../library/rules/ltp-f36f8c0cc1a6d840.yaml) | PERMISSION_DENIED_STATE | 调用 mmap(NULL, MMAPSIZE, PROT_READ, MAP_FILE | MAP_PRIVATE, fd, 0) | 返回 -1，errno 为 EACCES |
| [`LTP_FD1B65B0BCC88E0D`](../../library/rules/ltp-fd1b65b0bcc88e0d.yaml) | PERMISSION_DENIED_STATE | 调用 mmap(NULL, MMAPSIZE, PROT_READ | PROT_WRITE, MAP_FILE | MAP_SHARED, fd, 0) | 返回 -1，errno 为 EACCES |
| [`LTP_FEACDC300C3E1DD7`](../../library/rules/ltp-feacdc300c3e1dd7.yaml) | 无额外前置条件 | 调用 mmap(NULL, MMAPSIZE, PROT_READ | PROT_WRITE, MAP_FILE, fd, 0) | 返回 -1，errno 为 EINVAL |
## `modify_ldt`

没有形成可发布的合规性规则。

## `mount`

没有形成可发布的合规性规则。

## `mount_setattr`

共形成 4 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_5E8446D4A0B40C0E`](../../library/rules/ltp-5e8446d4a0b40c0e.yaml) | 文件描述符无效 | 调用 mount_setattr(-1, tmpdir, 0, &attr, sizeof(attr)) | 返回 -1，errno 为 EINVAL |
| [`LTP_5F50BCA4675B4B03`](../../library/rules/ltp-5f50bca4675b4b03.yaml) | 无额外前置条件 | 调用 mount_setattr(otfd, "", AT_EMPTY_PATH, attr, sizeof(*attr)) | 调用成功，返回 SUCCESS |
| [`LTP_A48CE326DC781ECE`](../../library/rules/ltp-a48ce326dc781ece.yaml) | 文件描述符无效 | 调用 mount_setattr(-1, slavedir, 0, &attr, sizeof(attr)) | 调用成功，返回 SUCCESS |
| [`LTP_D3506D1539EC71AB`](../../library/rules/ltp-d3506d1539ec71ab.yaml) | 文件描述符无效 | 调用 mount_setattr(-1, tmpdir, 0, &attr, sizeof(attr)) | 调用成功，返回 SUCCESS |
## `move_mount`

共形成 7 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_35AF6D3F6FC0EA61`](../../library/rules/ltp-35af6d3f6fc0ea61.yaml) | 无额外前置条件 | 调用 move_mount(fsmfd, "", AT_FDCWD, MNTPOINT, 0x08) | 返回 -1，errno 为 EINVAL |
| [`LTP_408787CB8F89AAF4`](../../library/rules/ltp-408787cb8f89aaf4.yaml) | 无额外前置条件 | 调用 move_mount(fsmfd, "", AT_FDCWD, MNTPOINT, tc->flags | MOVE_MOUNT_F_EMPTY_PATH) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_6C5B2B87F34E7887`](../../library/rules/ltp-6c5b2b87f34e7887.yaml) | NONEXISTENT_PATH | 调用 move_mount(fsmfd, "invalid", AT_FDCWD, MNTPOINT, MOVE_MOUNT_F_EMPTY_PATH) | 返回 -1，errno 为 ENOENT |
| [`LTP_7E14411F2FC9D9CF`](../../library/rules/ltp-7e14411f2fc9d9cf.yaml) | 无额外前置条件 | 调用 move_mount(fda, "", fdb, "", MOVE_MOUNT_BENEATH | MOVE_MOUNT_F_EMPTY_PATH | MOVE_MOUNT_T_EMPTY_PATH) | 调用成功，返回 SUCCESS |
| [`LTP_93C53F01B8732C42`](../../library/rules/ltp-93c53f01b8732c42.yaml) | NONEXISTENT_PATH | 调用 move_mount(fsmfd, "", AT_FDCWD, "invalid", MOVE_MOUNT_F_EMPTY_PATH) | 返回 -1，errno 为 ENOENT |
| [`LTP_F1391DB634702128`](../../library/rules/ltp-f1391db634702128.yaml) | 文件描述符无效 | 调用 move_mount(fsmfd, "", -1, MNTPOINT, MOVE_MOUNT_F_EMPTY_PATH) | 返回 -1，errno 为 EBADF |
| [`LTP_F284E6C48F6B4BF8`](../../library/rules/ltp-f284e6c48f6b4bf8.yaml) | 无额外前置条件 | 调用 move_mount(invalid_fd, "", AT_FDCWD, MNTPOINT, MOVE_MOUNT_F_EMPTY_PATH) | 返回 -1，errno 为 EBADF |
## `move_pages`

没有形成可发布的合规性规则。

## `mprotect`

共形成 8 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_08E1FDAFE6D66846`](../../library/rules/ltp-08e1fdafe6d66846.yaml) | USER_BUFFER | 调用 mprotect(addr, strlen(buf), PROT_READ) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_11852F99424BD7E5`](../../library/rules/ltp-11852f99424bd7e5.yaml) | 无额外前置条件 | 调用 mprotect(page_to_copy, page_sz, PROT_READ | PROT_EXEC) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_5E2B9548D2D9F147`](../../library/rules/ltp-5e2b9548d2d9f147.yaml) | 无额外前置条件 | 调用 mprotect(p, page_sz, PROT_EXEC) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_86E98E40777EA3FA`](../../library/rules/ltp-86e98e40777ea3fa.yaml) | 无额外前置条件 | 调用 mprotect(addr, page_sz, PROT_NONE) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_882D8F6DFB4B7858`](../../library/rules/ltp-882d8f6dfb4b7858.yaml) | PERMISSION_DENIED_STATE | 调用 mprotect(NULL, 0, PROT_WRITE) | 返回 -1，errno 为 EACCES |
| [`LTP_ED3B9CFAEBD0EAB8`](../../library/rules/ltp-ed3b9cfaebd0eab8.yaml) | USER_BUFFER | 调用 mprotect(addr, sizeof(buf), PROT_WRITE) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_FA4A7CD85E7F31FE`](../../library/rules/ltp-fa4a7cd85e7f31fe.yaml) | 无额外前置条件 | 调用 mprotect(NULL, 0, PROT_READ) | 返回 -1，errno 为 ENOMEM |
| [`LTP_FE37A7A30B8E2AFB`](../../library/rules/ltp-fe37a7a30b8e2afb.yaml) | 无额外前置条件 | 调用 mprotect(NULL, 1024, PROT_READ) | 返回 -1，errno 为 EINVAL |
## `mq_notify`

共形成 9 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_11385EF43CBDA2E0`](../../library/rules/ltp-11385ef43cbda2e0.yaml) | 无额外前置条件 | 调用 mq_notify(fd, &ev) | 返回 -1，errno 为 EBUSY |
| [`LTP_462CE9A88054B448`](../../library/rules/ltp-462ce9a88054b448.yaml) | 无额外前置条件 | 调用 mq_notify(0, &({.sigev_notify = SIGEV_SIGNAL, .sigev_signo = _NSIG + 1})) | 返回 -1，errno 为 EINVAL |
| [`LTP_46DC592FFC5E5C44`](../../library/rules/ltp-46dc592ffc5e5c44.yaml) | 无额外前置条件 | 调用 mq_notify(m, NULL) | 调用成功，返回 SUCCESS |
| [`LTP_6263797E65C75794`](../../library/rules/ltp-6263797e65c75794.yaml) | 文件描述符无效 | 调用 mq_notify(fd_invalid, &ev) | 返回 -1，errno 为 EBADF |
| [`LTP_828E39231372A771`](../../library/rules/ltp-828e39231372a771.yaml) | 无额外前置条件 | 调用 mq_notify(0, &({.sigev_notify = -1})) | 返回 -1，errno 为 EINVAL |
| [`LTP_947B3CCE7DA0998E`](../../library/rules/ltp-947b3cce7da0998e.yaml) | 无额外前置条件 | 调用 mq_notify(fd_maxint, &ev) | 返回 -1，errno 为 EBADF |
| [`LTP_A179D109B034EA29`](../../library/rules/ltp-a179d109b034ea29.yaml) | 无额外前置条件 | 调用 mq_notify(fd, &ev) | 返回 -1，errno 为 0 |
| [`LTP_D297A923D4C5FEC7`](../../library/rules/ltp-d297a923d4c5fec7.yaml) | 无额外前置条件 | 调用 mq_notify(m, &sev) | 调用成功，返回 SUCCESS |
| [`LTP_E3B5C7908A7B12CC`](../../library/rules/ltp-e3b5c7908a7b12cc.yaml) | 无额外前置条件 | 调用 mq_notify(fd_root, &ev) | 返回 -1，errno 为 EBADF |
## `mq_open`

没有形成可发布的合规性规则。

## `mq_timedreceive`

没有形成可发布的合规性规则。

## `mq_timedsend`

没有形成可发布的合规性规则。

## `mq_unlink`

没有形成可发布的合规性规则。

## `mremap`

没有形成可发布的合规性规则。

## `mseal`

没有形成可发布的合规性规则。

## `msync`

共形成 9 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_033FAA6E22CDE433`](../../library/rules/ltp-033faa6e22cde433.yaml) | 无额外前置条件 | 调用 msync(mmaped_area, pagesize, MS_SYNC) | 调用成功，返回 SUCCESS |
| [`LTP_2C37BF2D4F1059A2`](../../library/rules/ltp-2c37bf2d4f1059a2.yaml) | 无额外前置条件 | 调用 msync(addr, page_sz, MS_ASYNC) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_40621A9DFAF6D232`](../../library/rules/ltp-40621a9dfaf6d232.yaml) | 无额外前置条件 | 调用 msync(addr, page_sz, MS_INVALIDATE) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_4A4F50B0E250249A`](../../library/rules/ltp-4a4f50b0e250249a.yaml) | 无额外前置条件 | 调用 msync(addr4, page_sz, MS_SYNC) | 返回 -1，errno 为 ENOMEM |
| [`LTP_6DD85CE2E5952779`](../../library/rules/ltp-6dd85ce2e5952779.yaml) | 无额外前置条件 | 调用 msync(addr3, page_sz, MS_SYNC) | 返回 -1，errno 为 EINVAL |
| [`LTP_D0A69D14ADE1718C`](../../library/rules/ltp-d0a69d14ade1718c.yaml) | 无额外前置条件 | 调用 msync(addr1, page_sz, MS_INVALIDATE) | 返回 -1，errno 为 EBUSY |
| [`LTP_D2E2A5F40B2313E5`](../../library/rules/ltp-d2e2a5f40b2313e5.yaml) | 无额外前置条件 | 调用 msync(addr1, page_sz, MS_ASYNC | MS_SYNC) | 返回 -1，errno 为 EINVAL |
| [`LTP_EA90C626D9AA6C08`](../../library/rules/ltp-ea90c626d9aa6c08.yaml) | 无额外前置条件 | 调用 msync(addr1, page_sz, INV_SYNC) | 返回 -1，errno 为 EINVAL |
| [`LTP_F318E892720C2991`](../../library/rules/ltp-f318e892720c2991.yaml) | 无额外前置条件 | 调用 msync(addr2, page_sz, MS_SYNC) | 返回 -1，errno 为 EINVAL |
## `munlock`

共形成 5 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_4AF75A49B2F7AAB5`](../../library/rules/ltp-4af75a49b2f7aab5.yaml) | 无额外前置条件 | 调用 munlock(addr, len) | 返回 -1，errno 为 ENOMEM |
| [`LTP_4D9D59CFB785EB0C`](../../library/rules/ltp-4d9d59cfb785eb0c.yaml) | 无额外前置条件 | 调用 munlock(addr, 1024 * 1024) | 调用成功，返回 SUCCESS |
| [`LTP_59A85FEDCED7BE77`](../../library/rules/ltp-59a85fedced7be77.yaml) | 无额外前置条件 | 调用 munlock(addr, 1024 * 1024 * 10) | 调用成功，返回 SUCCESS |
| [`LTP_AFDAD0AD4FE0E3FF`](../../library/rules/ltp-afdad0ad4fe0e3ff.yaml) | 无额外前置条件 | 调用 munlock(addr, 1024) | 调用成功，返回 SUCCESS |
| [`LTP_B8A61982E829826E`](../../library/rules/ltp-b8a61982e829826e.yaml) | 无额外前置条件 | 调用 munlock(addr, 1) | 调用成功，返回 SUCCESS |
## `munlockall`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_EB40C6ADD4390CB3`](../../library/rules/ltp-eb40c6add4390cb3.yaml) | 无额外前置条件 | 调用 munlockall() | 调用成功，返回 SUCCESS |
## `munmap`

共形成 4 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_09ADB22B713F6C62`](../../library/rules/ltp-09adb22b713f6c62.yaml) | 无额外前置条件 | 调用 munmap(maps[2] + page_sz, page_sz) | 返回 -1，errno 为 ENOMEM |
| [`LTP_26AE3C69D80D35F8`](../../library/rules/ltp-26ae3c69d80d35f8.yaml) | 无额外前置条件 | 调用 munmap(&map_addr, map_len_zero) | 返回 -1，errno 为 EINVAL |
| [`LTP_D744D6C4A0C3E40C`](../../library/rules/ltp-d744d6c4a0c3e40c.yaml) | 无额外前置条件 | 调用 munmap(&map_addr_out, map_len) | 返回 -1，errno 为 EINVAL |
| [`LTP_E20E7069E7FA34D5`](../../library/rules/ltp-e20e7069e7fa34d5.yaml) | 无额外前置条件 | 调用 munmap(&map_addr + 1, map_len) | 返回 -1，errno 为 EINVAL |
## `name_to_handle_at`

没有形成可发布的合规性规则。

## `nanosleep`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_6C8CC973DA350505`](../../library/rules/ltp-6c8cc973da350505.yaml) | 无额外前置条件 | 调用 nanosleep(&tcases[n], NULL) | 返回 -1，errno 为 EINVAL |
| [`LTP_DDCD82CA2726175D`](../../library/rules/ltp-ddcd82ca2726175d.yaml) | 无额外前置条件 | 调用 nanosleep(&timereq, &timerem) | 返回 -1，errno 为 EINTR |
| [`LTP_FAF274CF431E6421`](../../library/rules/ltp-faf274cf431e6421.yaml) | 无额外前置条件 | 调用 nanosleep(&t, NULL) | {'kind': 'return_value', 'return': '0'} |
## `newuname`

没有形成可发布的合规性规则。

## `nftw`

没有形成可发布的合规性规则。

## `nice`

没有形成可发布的合规性规则。

## `open`

没有形成可发布的合规性规则。

## `open_by_handle_at`

共形成 7 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0B898E71738ECEB7`](../../library/rules/ltp-0b898e71738eceb7.yaml) | BAD_USER_ADDRESS | 调用 open_by_handle_at(AT_FDCWD, invalid_fhp, O_RDWR) | 返回 -1，errno 为 EFAULT |
| [`LTP_1B65027CA2FD0026`](../../library/rules/ltp-1b65027ca2fd0026.yaml) | 无额外前置条件 | 调用 open_by_handle_at(AT_FDCWD, valid_fhp, O_RDWR) | 返回 -1，errno 为 EPERM |
| [`LTP_326E9D51F4EF6E39`](../../library/rules/ltp-326e9d51f4ef6e39.yaml) | 文件描述符无效 | 调用 open_by_handle_at(-1, valid_fhp, O_RDWR) | 返回 -1，errno 为 EBADF |
| [`LTP_3FF54C2EFF286EF7`](../../library/rules/ltp-3ff54c2eff286ef7.yaml) | 无额外前置条件 | 调用 open_by_handle_at(AT_FDCWD, zero_fhp, O_RDWR) | 返回 -1，errno 为 EINVAL |
| [`LTP_46649CE57B3EFB7F`](../../library/rules/ltp-46649ce57b3efb7f.yaml) | SYMLINK_LOOP | 调用 open_by_handle_at(AT_FDCWD, link_fhp, O_RDWR) | 返回 -1，errno 为 ELOOP |
| [`LTP_53F53970B961AB32`](../../library/rules/ltp-53f53970b961ab32.yaml) | 无额外前置条件 | 调用 open_by_handle_at(0, valid_fhp, O_RDWR) | 返回 -1，errno 为 ESTALE |
| [`LTP_E9D60674E416A5DC`](../../library/rules/ltp-e9d60674e416a5dc.yaml) | 无额外前置条件 | 调用 open_by_handle_at(AT_FDCWD, high_fhp, O_RDWR) | 返回 -1，errno 为 EINVAL |
## `open_tree`

没有形成可发布的合规性规则。

## `openat`

没有形成可发布的合规性规则。

## `openat2`

共形成 15 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_026CB4A1CA7CDC6B`](../../library/rules/ltp-026cb4a1ca7cdc6b.yaml) | 无额外前置条件 | 调用 openat2(AT_FDCWD, TEST_FILE, myhow, sizeof(*how) - 1) | 返回 -1，errno 为 EINVAL |
| [`LTP_0F5654610A1780B6`](../../library/rules/ltp-0f5654610a1780b6.yaml) | SYMLINK_LOOP | 调用 openat2(AT_FDCWD, "/proc/self/exe", how, sizeof(*how)) | 返回 -1，errno 为 ELOOP |
| [`LTP_15FCB1A16CBF7B34`](../../library/rules/ltp-15fcb1a16cbf7b34.yaml) | 无额外前置条件 | 调用 openat2(AT_FDCWD, FOO_SYMLINK, how, sizeof(*how)) | 返回 -1，errno 为 0 |
| [`LTP_4101795C27681AB4`](../../library/rules/ltp-4101795c27681ab4.yaml) | 无额外前置条件 | 调用 openat2(AT_FDCWD, TEST_FILE, myhow, sizeof(*how) + 8) | 返回 -1，errno 为 E2BIG |
| [`LTP_47B47DF38E582CE0`](../../library/rules/ltp-47b47df38e582ce0.yaml) | SYMLINK_LOOP | 调用 openat2(AT_FDCWD, FOO_SYMLINK, how, sizeof(*how)) | 返回 -1，errno 为 ELOOP |
| [`LTP_57933F1DF2F98C34`](../../library/rules/ltp-57933f1df2f98c34.yaml) | 无额外前置条件 | 调用 openat2(AT_FDCWD, TEST_FILE, myhow, sizeof(*how)) | 返回 -1，errno 为 EINVAL |
| [`LTP_69317571BC0A39EC`](../../library/rules/ltp-69317571bc0a39ec.yaml) | NONEXISTENT_PATH | 调用 openat2(AT_FDCWD, "/proc/version", how, sizeof(*how)) | 返回 -1，errno 为 ENOENT |
| [`LTP_7FEB3B276A8133AC`](../../library/rules/ltp-7feb3b276a8133ac.yaml) | 无额外前置条件 | 调用 openat2(AT_FDCWD, "/proc/version", how, sizeof(*how)) | 返回 -1，errno 为 EXDEV |
| [`LTP_8405B02758433FBC`](../../library/rules/ltp-8405b02758433fbc.yaml) | 无额外前置条件 | 调用 openat2(AT_FDCWD, "../foo", how, sizeof(*how)) | 返回 -1，errno 为 EXDEV |
| [`LTP_845843CAB40A4F40`](../../library/rules/ltp-845843cab40a4f40.yaml) | 无额外前置条件 | 调用 openat2(AT_FDCWD, "/proc/self/exe", how, sizeof(*how)) | 返回 -1，errno 为 0 |
| [`LTP_B984D0FF91909634`](../../library/rules/ltp-b984d0ff91909634.yaml) | BAD_USER_ADDRESS | 调用 openat2(AT_FDCWD, TEST_FILE, myhow, sizeof(*how) + 1) | 返回 -1，errno 为 EFAULT |
| [`LTP_D0800876342DE939`](../../library/rules/ltp-d0800876342de939.yaml) | 无额外前置条件 | 调用 openat2(AT_FDCWD, TEST_FILE, myhow, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_D33B1BBC658C83D4`](../../library/rules/ltp-d33b1bbc658c83d4.yaml) | 文件描述符无效 | 调用 openat2(-1, TEST_FILE, myhow, sizeof(*how)) | 返回 -1，errno 为 EBADF |
| [`LTP_E56EFFCF50E90E41`](../../library/rules/ltp-e56effcf50e90e41.yaml) | 无额外前置条件 | 调用 openat2(AT_FDCWD, "/proc/version", how, sizeof(*how)) | 返回 -1，errno 为 0 |
| [`LTP_FD400AE357F2EBB3`](../../library/rules/ltp-fd400ae357f2ebb3.yaml) | BAD_USER_ADDRESS | 调用 openat2(AT_FDCWD, NULL, myhow, sizeof(*how)) | 返回 -1，errno 为 EFAULT |
## `pathconf`

共形成 23 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_16343E95C1C7EF47`](../../library/rules/ltp-16343e95c1c7ef47.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_REC_INCR_XFER_SIZE)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_1661259678F899BC`](../../library/rules/ltp-1661259678f899bc.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_PRIO_IO)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_1707E748EA729431`](../../library/rules/ltp-1707e748ea729431.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_MAX_INPUT)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_1893FF0C4930806E`](../../library/rules/ltp-1893ff0c4930806e.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_MAX_CANON)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_1AD5BF710E8FB247`](../../library/rules/ltp-1ad5bf710e8fb247.yaml) | NON_DIRECTORY_PATH_COMPONENT | 调用 pathconf(fpath, 0) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_33D0A33AC4655F3E`](../../library/rules/ltp-33d0a33ac4655f3e.yaml) | NONEXISTENT_PATH | 调用 pathconf(emptypath, 0) | 返回 -1，errno 为 ENOENT |
| [`LTP_50BD66A0A05AFE51`](../../library/rules/ltp-50bd66a0a05afe51.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_ASYNC_IO)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_532E8E5A98C0A22D`](../../library/rules/ltp-532e8e5a98c0a22d.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_REC_MIN_XFER_SIZE)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_621EC309C3A75722`](../../library/rules/ltp-621ec309c3a75722.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_NAME_MAX)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_779183F85F2C1278`](../../library/rules/ltp-779183f85f2c1278.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_FILESIZEBITS)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_7A84C55AF45835C2`](../../library/rules/ltp-7a84c55af45835c2.yaml) | PATH_TOO_LONG | 调用 pathconf(long_path, 0) | 返回 -1，errno 为 ENAMETOOLONG |
| [`LTP_7C67E10CB5F35EA2`](../../library/rules/ltp-7c67e10cb5f35ea2.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_REC_XFER_ALIGN)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_7FDF0704C50C872E`](../../library/rules/ltp-7fdf0704c50c872e.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_PIPE_BUF)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_81F076122348B68A`](../../library/rules/ltp-81f076122348b68a.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_SYNC_IO)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_913EC5DF431DC6C2`](../../library/rules/ltp-913ec5df431dc6c2.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_NO_TRUNC)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_9445A602B4F98B83`](../../library/rules/ltp-9445a602b4f98b83.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_REC_MAX_XFER_SIZE)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_BF31641F04151F3C`](../../library/rules/ltp-bf31641f04151f3c.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_VDISABLE)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_C87041F4B4B5A930`](../../library/rules/ltp-c87041f4b4b5a930.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_PATH_MAX)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_D30F83EC0B5B2E08`](../../library/rules/ltp-d30f83ec0b5b2e08.yaml) | PERMISSION_DENIED_STATE | 调用 pathconf(abs_path, 0) | 返回 -1，errno 为 EACCES |
| [`LTP_D331AAEAED1F6297`](../../library/rules/ltp-d331aaeaed1f6297.yaml) | 文件描述符无效 | 调用 pathconf(abs_path, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_DD64353E8E427275`](../../library/rules/ltp-dd64353e8e427275.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_LINK_MAX)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_EC19279F1BC5A623`](../../library/rules/ltp-ec19279f1bc5a623.yaml) | SYMLINK_LOOP | 调用 pathconf(testeloop, 0) | 返回 -1，errno 为 ELOOP |
| [`LTP_FEDE14E9D4DE9A9D`](../../library/rules/ltp-fede14e9d4de9a9d.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_CHOWN_RESTRICTED)) | {'kind': 'return_value', 'return': '-1'} |
## `pause`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_9E2C65A6408DD9D3`](../../library/rules/ltp-9e2c65a6408dd9d3.yaml) | 无额外前置条件 | 调用 pause() | 返回 -1，errno 为 EINTR |
## `perf_event_open`

没有形成可发布的合规性规则。

## `personality`

没有形成可发布的合规性规则。

## `pidfd_getfd`

共形成 13 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0134FE6EEF60CBCD`](../../library/rules/ltp-0134fe6eef60cbcd.yaml) | 无额外前置条件 | 调用 pidfd_getfd(pidfd, 0, 0) | 返回 -1，errno 为 EPERM |
| [`LTP_12EAE2F32232CC05`](../../library/rules/ltp-12eae2f32232cc05.yaml) | 无额外前置条件 | 调用 pidfd_getfd(invalid_pidfd, 0, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_249EC7CDE9C4682F`](../../library/rules/ltp-249ec7cde9c4682f.yaml) | 无额外前置条件 | 调用 pidfd_getfd(valid_pidfd, 0, 0) | 返回 -1，errno 为 EPERM |
| [`LTP_254E7D0C8662B3BB`](../../library/rules/ltp-254e7d0c8662b3bb.yaml) | 无额外前置条件 | 调用 pidfd_getfd(valid_pidfd, 0, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_43A681D8FCD1B740`](../../library/rules/ltp-43a681d8fcd1b740.yaml) | 无额外前置条件 | 调用 pidfd_getfd(valid_pidfd, 0, 0) | 返回 -1，errno 为 ESRCH |
| [`LTP_5322AC28C2EB6C16`](../../library/rules/ltp-5322ac28c2eb6c16.yaml) | 无额外前置条件 | 调用 pidfd_getfd(pidfd, 0, 1) | 返回 -1，errno 为 EINVAL |
| [`LTP_595C676EF473E6BD`](../../library/rules/ltp-595c676ef473e6bd.yaml) | 无额外前置条件 | 调用 pidfd_getfd(pidfd, 0, 0) | 返回 -1，errno 为 ESRCH |
| [`LTP_77FED5FE42B62868`](../../library/rules/ltp-77fed5fe42b62868.yaml) | 无额外前置条件 | 调用 pidfd_getfd(pidfd, 0, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_85106060CC8B99CF`](../../library/rules/ltp-85106060cc8b99cf.yaml) | 无额外前置条件 | 调用 pidfd_getfd(*NULL, 0, 0) | 返回 -1，errno 为 ESRCH |
| [`LTP_94654CBF1E34C32B`](../../library/rules/ltp-94654cbf1e34c32b.yaml) | 文件描述符无效 | 调用 pidfd_getfd(valid_pidfd, -1, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_C9AF84778DBE8B78`](../../library/rules/ltp-c9af84778dbe8b78.yaml) | 文件描述符无效 | 调用 pidfd_getfd(pidfd, -1, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_E6A7D5E5327D8ECC`](../../library/rules/ltp-e6a7d5e5327d8ecc.yaml) | 无额外前置条件 | 调用 pidfd_getfd(pidfd, targetfd, 0) | {'kind': 'return_fd', 'return': 'FD'} |
| [`LTP_EA7E63D027CD6941`](../../library/rules/ltp-ea7e63d027cd6941.yaml) | 无额外前置条件 | 调用 pidfd_getfd(valid_pidfd, 0, 1) | 返回 -1，errno 为 EINVAL |
## `pidfd_open`

共形成 7 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0311772B70C94C38`](../../library/rules/ltp-0311772b70c94c38.yaml) | 无额外前置条件 | 调用 pidfd_open(pid, 0) | {'kind': 'return_fd', 'return': 'FD'} |
| [`LTP_0EEADAF9E605632C`](../../library/rules/ltp-0eeadaf9e605632c.yaml) | 无额外前置条件 | 调用 pidfd_open(getpid(), PIDFD_NONBLOCK) | 返回 -1，errno 为 EINVAL |
| [`LTP_18E65E41E98D9E97`](../../library/rules/ltp-18e65e41e98d9e97.yaml) | 无额外前置条件 | 调用 pidfd_open(expired_pid, 0) | 返回 -1，errno 为 ESRCH |
| [`LTP_1BB76939FF2A40B5`](../../library/rules/ltp-1bb76939ff2a40b5.yaml) | 无额外前置条件 | 调用 pidfd_open(invalid_pid, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_3743BC827FB4F981`](../../library/rules/ltp-3743bc827fb4f981.yaml) | 无额外前置条件 | 调用 pidfd_open(my_pid, 1) | 返回 -1，errno 为 EINVAL |
| [`LTP_7CD01664A3589136`](../../library/rules/ltp-7cd01664a3589136.yaml) | 无额外前置条件 | 调用 pidfd_open(getpid(), 0) | {'kind': 'return_fd', 'return': 'FD'} |
| [`LTP_E5E64FCDA6CACABE`](../../library/rules/ltp-e5e64fcda6cacabe.yaml) | 无额外前置条件 | 调用 pidfd_open(pid, PIDFD_NONBLOCK) | {'kind': 'return_fd', 'return': 'FD'} |
## `pidfd_send_signal`

共形成 6 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_08C4F07A07C4C3F7`](../../library/rules/ltp-08c4f07a07c4c3f7.yaml) | 无额外前置条件 | 调用 pidfd_send_signal(pidfd, SIGUSR1, NULL, 0) | 返回 -1，errno 为 ESRCH |
| [`LTP_08F05BA6ED1CEE6A`](../../library/rules/ltp-08f05ba6ed1cee6a.yaml) | 无额外前置条件 | 调用 pidfd_send_signal(pidfd, CORRECT_SIGNAL, &info, 99999) | 返回 -1，errno 为 EINVAL |
| [`LTP_0F9F906AC57F0B46`](../../library/rules/ltp-0f9f906ac57f0b46.yaml) | 无额外前置条件 | 调用 pidfd_send_signal(pidfd, DIFFERENT_SIGNAL, &info, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_B7606EDCC1F1031F`](../../library/rules/ltp-b7606edcc1f1031f.yaml) | 无额外前置条件 | 调用 pidfd_send_signal(init_pidfd, CORRECT_SIGNAL, &info, 0) | 返回 -1，errno 为 EPERM |
| [`LTP_FAECCAD19268C313`](../../library/rules/ltp-faeccad19268c313.yaml) | 无额外前置条件 | 调用 pidfd_send_signal(pidfd, SIGNAL, uinfo, 0) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_FE471F5051750B9C`](../../library/rules/ltp-fe471f5051750b9c.yaml) | 无额外前置条件 | 调用 pidfd_send_signal(dummyfd, CORRECT_SIGNAL, &info, 0) | 返回 -1，errno 为 EBADF |
## `pipe`

没有形成可发布的合规性规则。

## `pipe2`

没有形成可发布的合规性规则。

## `pivot_root`

没有形成可发布的合规性规则。

## `pkeys`

没有形成可发布的合规性规则。

## `poll`

共形成 5 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_018C7E7A08833780`](../../library/rules/ltp-018c7e7a08833780.yaml) | 无额外前置条件 | 调用 poll(pfds, 1, sleep_ms) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_403B654FD084895C`](../../library/rules/ltp-403b654fd084895c.yaml) | 无额外前置条件 | 调用 poll(&pfd, 1, 0) | {'kind': 'return_value', 'return': '1'} |
| [`LTP_51EC2B222D4690DB`](../../library/rules/ltp-51ec2b222d4690db.yaml) | 文件描述符无效 | 调用 poll(infds, 1, -1) | {'kind': 'return_value', 'return': '1'} |
| [`LTP_58266C6AA844BBBD`](../../library/rules/ltp-58266c6aa844bbbd.yaml) | 文件描述符无效 | 调用 poll(&pfd, 1, -1) | {'kind': 'return_value', 'return': '1'} |
| [`LTP_D87AF1C2D0AF66D2`](../../library/rules/ltp-d87af1c2d0af66d2.yaml) | 文件描述符无效 | 调用 poll(outfds, 1, -1) | {'kind': 'return_value', 'return': '1'} |
## `ppoll`

没有形成可发布的合规性规则。

## `prctl`

没有形成可发布的合规性规则。

## `pread64`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_3F60BBC08D86D573`](../../library/rules/ltp-3f60bbc08d86d573.yaml) | 文件描述符无效、USER_BUFFER | 调用 pread64(fd, &buf, K1, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_4BDFA76AA51D745B`](../../library/rules/ltp-4bdfa76aa51d745b.yaml) | USER_BUFFER | 调用 pread64(pipe_fd[0], &buf, K1, 0) | 返回 -1，errno 为 ESPIPE |
| [`LTP_9CEE24911B622031`](../../library/rules/ltp-9cee24911b622031.yaml) | USER_BUFFER | 调用 pread64(dir_fd, &buf, K1, 0) | 返回 -1，errno 为 EISDIR |
## `preadv`

没有形成可发布的合规性规则。

## `preadv2`

共形成 15 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_1AACAC53BAF23BA9`](../../library/rules/ltp-1aacac53baf23ba9.yaml) | 无额外前置条件 | 调用 preadv2(fd, iovec, 1, 0, RWF_NOWAIT) | 返回 -1，errno 为 EOPNOTSUPP |
| [`LTP_2A28494F77E0B173`](../../library/rules/ltp-2a28494f77e0b173.yaml) | 无额外前置条件 | 调用 preadv2(fd1, rd_iovec1, 1, 0, 0) | 返回 0，errno 为 EINVAL |
| [`LTP_350B586A62C42467`](../../library/rules/ltp-350b586a62c42467.yaml) | 文件描述符无效 | 调用 preadv2(fd1, rd_iovec2, 1, 1, -1) | 返回 0，errno 为 EOPNOTSUPP |
| [`LTP_3EB53CD0B1672EE5`](../../library/rules/ltp-3eb53cd0b1672ee5.yaml) | 无额外前置条件 | 调用 preadv2(fd4, rd_iovec2, 1, 0, 0) | 返回 0，errno 为 EISDIR |
| [`LTP_679924706FAFC4A5`](../../library/rules/ltp-679924706fafc4a5.yaml) | 无额外前置条件 | 调用 preadv2(fd5[0], rd_iovec2, 1, 0, 0) | 返回 0，errno 为 ESPIPE |
| [`LTP_82907DD83DFD7800`](../../library/rules/ltp-82907dd83dfd7800.yaml) | 无额外前置条件 | 调用 preadv2(fd, rd_iovec, 2, off, RWF_NOWAIT) | 返回 CHUNK_SZ + CHUNK_SZ/2，errno 为 EAGAIN |
| [`LTP_93F2091ECF31C3E0`](../../library/rules/ltp-93f2091ecf31c3e0.yaml) | 无额外前置条件 | 调用 preadv2(fd, rd_iovec, 1, CHUNK*3 / 2, 0) | {'kind': 'return_value', 'return': 'CHUNK / 2'} |
| [`LTP_A4E6C06F187B9504`](../../library/rules/ltp-a4e6c06f187b9504.yaml) | 文件描述符无效 | 调用 preadv2(fd1, rd_iovec2, -1, 0, 0) | 返回 0，errno 为 EINVAL |
| [`LTP_AF0FA27496E3610E`](../../library/rules/ltp-af0fa27496e3610e.yaml) | 无额外前置条件 | 调用 preadv2(fd3, rd_iovec2, 1, 0, 0) | 返回 0，errno 为 EBADF |
| [`LTP_B08ED7334608FAA8`](../../library/rules/ltp-b08ed7334608faa8.yaml) | 文件描述符无效 | 调用 preadv2(fd, rd_iovec, 2, -1, 0) | {'kind': 'return_value', 'return': 'CHUNK'} |
| [`LTP_B6DD7EB9951128C1`](../../library/rules/ltp-b6dd7eb9951128c1.yaml) | 文件描述符无效 | 调用 preadv2(fd, rd_iovec, 1, -1, 0) | {'kind': 'return_value', 'return': 'CHUNK'} |
| [`LTP_DC3D9E7D5D1A75DE`](../../library/rules/ltp-dc3d9e7d5d1a75de.yaml) | 无额外前置条件 | 调用 preadv2(fd2, rd_iovec2, 1, 0, 0) | 返回 0，errno 为 EBADF |
| [`LTP_E2360C045F1BCE8E`](../../library/rules/ltp-e2360c045f1bce8e.yaml) | 无额外前置条件 | 调用 preadv2(fd, rd_iovec, 1, 0, 0) | {'kind': 'return_value', 'return': 'CHUNK'} |
| [`LTP_F6456DE083F145B0`](../../library/rules/ltp-f6456de083f145b0.yaml) | BAD_USER_ADDRESS | 调用 preadv2(fd1, rd_iovec3, 1, 0, 0) | 返回 0，errno 为 EFAULT |
| [`LTP_FB3B521CE41A299A`](../../library/rules/ltp-fb3b521ce41a299a.yaml) | 无额外前置条件 | 调用 preadv2(fd, rd_iovec, 2, 0, 0) | {'kind': 'return_value', 'return': 'CHUNK'} |
## `process_madvise`

没有形成可发布的合规性规则。

## `profil`

没有形成可发布的合规性规则。

## `pselect`

没有形成可发布的合规性规则。

## `ptrace`

没有形成可发布的合规性规则。

## `pwrite64`

共形成 6 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0AE3E0188FBE5839`](../../library/rules/ltp-0ae3e0188fbe5839.yaml) | BAD_USER_ADDRESS | 调用 pwrite64(fd, NULL, BS, 0) | 返回 -1，errno 为 EFAULT |
| [`LTP_15EC9351D2422944`](../../library/rules/ltp-15ec9351d2422944.yaml) | 文件描述符无效、USER_BUFFER | 调用 pwrite64(fd, buf, BS, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_4E45B0701D5BD8A7`](../../library/rules/ltp-4e45b0701d5bd8a7.yaml) | 无额外前置条件 | 调用 pwrite64(fd, NULL, 0, 0) | 调用成功，返回 SUCCESS |
| [`LTP_80B2CAF4B298BEE6`](../../library/rules/ltp-80b2caf4b298bee6.yaml) | USER_BUFFER | 调用 pwrite64(inv_fd, buf, BS, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_D4E6A74BAB2E8722`](../../library/rules/ltp-d4e6a74bab2e8722.yaml) | USER_BUFFER | 调用 pwrite64(fd_ro, buf, BS, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_D5F414741594F6E3`](../../library/rules/ltp-d5f414741594f6e3.yaml) | USER_BUFFER | 调用 pwrite64(pipe_fds[1], buf, BS, 0) | 返回 -1，errno 为 ESPIPE |
## `pwritev`

没有形成可发布的合规性规则。

## `pwritev2`

共形成 12 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_1F2328B410A3010D`](../../library/rules/ltp-1f2328b410a3010d.yaml) | 无额外前置条件 | 调用 pwritev2(fd1, wr_iovec1, 1, 0, 0) | 返回 0，errno 为 EINVAL |
| [`LTP_296D3DD5B2B27A84`](../../library/rules/ltp-296d3dd5b2b27a84.yaml) | 无额外前置条件 | 调用 pwritev2(fd, wr_iovec, 2, 0, 0) | {'kind': 'return_value', 'return': 'CHUNK'} |
| [`LTP_3152706321BA354E`](../../library/rules/ltp-3152706321ba354e.yaml) | 无额外前置条件 | 调用 pwritev2(fd, wr_iovec, 1, CHUNK / 2, 0) | {'kind': 'return_value', 'return': 'CHUNK'} |
| [`LTP_56694FAD66174814`](../../library/rules/ltp-56694fad66174814.yaml) | 文件描述符无效 | 调用 pwritev2(fd, wr_iovec, 1, -1, 0) | {'kind': 'return_value', 'return': 'CHUNK'} |
| [`LTP_74C13DA111D6D9BD`](../../library/rules/ltp-74c13da111d6d9bd.yaml) | 文件描述符无效 | 调用 pwritev2(fd, wr_iovec, 2, -1, 0) | {'kind': 'return_value', 'return': 'CHUNK'} |
| [`LTP_78A991C666EEFF75`](../../library/rules/ltp-78a991c666eeff75.yaml) | 无额外前置条件 | 调用 pwritev2(fd2, wr_iovec2, 1, 0, 0) | 返回 0，errno 为 EBADF |
| [`LTP_7C0B488884F6689C`](../../library/rules/ltp-7c0b488884f6689c.yaml) | 无额外前置条件 | 调用 pwritev2(fd3, wr_iovec2, 1, 0, 0) | 返回 0，errno 为 EBADF |
| [`LTP_9A3244C4CEBE8674`](../../library/rules/ltp-9a3244c4cebe8674.yaml) | BAD_USER_ADDRESS | 调用 pwritev2(fd1, wr_iovec3, 1, 0, 0) | 返回 0，errno 为 EFAULT |
| [`LTP_B06B0397728F35C3`](../../library/rules/ltp-b06b0397728f35c3.yaml) | 无额外前置条件 | 调用 pwritev2(fd, wr_iovec, 1, 0, 0) | {'kind': 'return_value', 'return': 'CHUNK'} |
| [`LTP_D1D51B0412DFB097`](../../library/rules/ltp-d1d51b0412dfb097.yaml) | 文件描述符无效 | 调用 pwritev2(fd1, wr_iovec2, 1, 1, -1) | 返回 0，errno 为 EOPNOTSUPP |
| [`LTP_DBAE060B9CA303DD`](../../library/rules/ltp-dbae060b9ca303dd.yaml) | 无额外前置条件 | 调用 pwritev2(fd4[0], wr_iovec2, 1, 0, 0) | 返回 0，errno 为 ESPIPE |
| [`LTP_EF4053B74F85E11B`](../../library/rules/ltp-ef4053b74f85e11b.yaml) | 文件描述符无效 | 调用 pwritev2(fd1, wr_iovec2, -1, 0, 0) | 返回 0，errno 为 EINVAL |
## `quotactl`

没有形成可发布的合规性规则。

## `read`

共形成 8 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0087F445CEB63414`](../../library/rules/ltp-0087f445ceb63414.yaml) | 无额外前置条件 | 调用 read(badfd, bufaddr, 1) | 返回 -1，errno 为 EBADF |
| [`LTP_2C266C6067333086`](../../library/rules/ltp-2c266c6067333086.yaml) | 无额外前置条件 | 调用 read(fd, prbuf, BUFSIZ) | {'kind': 'return_value', 'return': 'PALFA_LEN'} |
| [`LTP_7F0FE233BE49C811`](../../library/rules/ltp-7f0fe233be49c811.yaml) | 无额外前置条件 | 调用 read(fd2, bufaddr, 1) | 返回 -1，errno 为 EISDIR |
| [`LTP_9F30FD7002BC2EBA`](../../library/rules/ltp-9f30fd7002bc2eba.yaml) | 无额外前置条件 | 调用 read(fd4, addr4, 1) | 返回 -1，errno 为 EINVAL |
| [`LTP_A5BD363654740DDE`](../../library/rules/ltp-a5bd363654740dde.yaml) | 无额外前置条件 | 调用 read(rfd, &c, 1) | 返回 -1，errno 为 EAGAIN |
| [`LTP_C8C667C37A069984`](../../library/rules/ltp-c8c667c37a069984.yaml) | 无额外前置条件 | 调用 read(fd4, addr5, 4096) | 返回 -1，errno 为 EINVAL |
| [`LTP_D9A5AE03D93C5C6D`](../../library/rules/ltp-d9a5ae03d93c5c6d.yaml) | BAD_USER_ADDRESS | 调用 read(fd3, outside_buf, 1) | 返回 -1，errno 为 EFAULT |
| [`LTP_FB7C7C6EA4808026`](../../library/rules/ltp-fb7c7c6ea4808026.yaml) | USER_BUFFER | 调用 read(fd, buf, SIZE) | {'kind': 'return_value', 'return': '-1'} |
## `readahead`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0F35A2F3718D172D`](../../library/rules/ltp-0f35a2f3718d172d.yaml) | 文件描述符无效 | 调用 readahead(-1, 0, getpagesize()) | 返回 -1，errno 为 EBADF |
| [`LTP_28410A5D4088E644`](../../library/rules/ltp-28410a5d4088e644.yaml) | 无额外前置条件 | 调用 readahead(fd->fd, 0, getpagesize()) | 返回 -1，errno 为 exp_errnos |
| [`LTP_AA6F0F0A8A469B13`](../../library/rules/ltp-aa6f0f0a8a469b13.yaml) | 无额外前置条件 | 调用 readahead(fd[0], 0, getpagesize()) | 返回 -1，errno 为 EBADF |
## `readdir`

没有形成可发布的合规性规则。

## `readlink`

没有形成可发布的合规性规则。

## `readlinkat`

共形成 12 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_048D7BAFDFD264F6`](../../library/rules/ltp-048d7bafdfd264f6.yaml) | USER_BUFFER | 调用 readlinkat(dir_fd, TEST_FILE, buf, BUFF_SIZE) | 返回 -1，errno 为 EINVAL |
| [`LTP_1505AAD11D4091B7`](../../library/rules/ltp-1505aad11d4091b7.yaml) | USER_BUFFER | 调用 readlinkat(fd_atcwd, abspath, buf, sizeof(buf)) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_209742037ADD09F1`](../../library/rules/ltp-209742037add09f1.yaml) | USER_BUFFER | 调用 readlinkat(fd_atcwd, testsymlink, buf, sizeof(buf)) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_30AF82AD36872B80`](../../library/rules/ltp-30af82ad36872b80.yaml) | NON_DIRECTORY_PATH_COMPONENT、USER_BUFFER | 调用 readlinkat(file_fd, SYMLINK_FILE, buf, BUFF_SIZE) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_55E78705E11C6E2D`](../../library/rules/ltp-55e78705e11c6e2d.yaml) | USER_BUFFER | 调用 readlinkat(dir_fd, testsymlink, buf, sizeof(buf)) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_5A2FE2DE55DC96EB`](../../library/rules/ltp-5a2fe2de55dc96eb.yaml) | USER_BUFFER | 调用 readlinkat(dir_fd, SYMLINK_FILE, buf, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_5B5079DEC75B53F5`](../../library/rules/ltp-5b5079dec75b53f5.yaml) | 文件描述符无效、USER_BUFFER | 调用 readlinkat(fd_invalid, SYMLINK_FILE, buf, BUFF_SIZE) | 返回 -1，errno 为 EBADF |
| [`LTP_635254F85EA9B1B0`](../../library/rules/ltp-635254f85ea9b1b0.yaml) | NONEXISTENT_PATH、USER_BUFFER | 调用 readlinkat(dir_fd, "does_not_exists", buf, BUFF_SIZE) | 返回 -1，errno 为 ENOENT |
| [`LTP_8B80C0CDA587165C`](../../library/rules/ltp-8b80c0cda587165c.yaml) | USER_BUFFER | 调用 readlinkat(dir_fd, abspath, buf, sizeof(buf)) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_8F4CA997DDB954AF`](../../library/rules/ltp-8f4ca997ddb954af.yaml) | NON_DIRECTORY_PATH_COMPONENT、USER_BUFFER | 调用 readlinkat(dir_fd, "test_file/test_file", buf, BUFF_SIZE) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_9B32E51680CE0BEE`](../../library/rules/ltp-9b32e51680ce0bee.yaml) | USER_BUFFER | 调用 readlinkat(dir_fd2, emptypath, buf, sizeof(buf)) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_AC5312B5BF09186C`](../../library/rules/ltp-ac5312b5bf09186c.yaml) | USER_BUFFER | 调用 readlinkat(file_fd, abspath, buf, sizeof(buf)) | {'kind': 'positive_return', 'return': '>0'} |
## `readv`

没有形成可发布的合规性规则。

## `realpath`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_68EDEECFEA7F3C06`](../../library/rules/ltp-68edeecfea7f3c06.yaml) | NONEXISTENT_PATH | 调用 realpath(".", NULL) | 返回 -1，errno 为 ENOENT |
## `reboot`

没有形成可发布的合规性规则。

## `recv`

共形成 5 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_66303F5A0EB2D470`](../../library/rules/ltp-66303f5a0eb2d470.yaml) | BAD_USER_ADDRESS、USER_BUFFER | 调用 recv(s, (void *)-1, sizeof(buf), 0) | 返回 -1，errno 为 EFAULT |
| [`LTP_766411248B80C139`](../../library/rules/ltp-766411248b80c139.yaml) | USER_BUFFER | 调用 recv(s, buf, sizeof(buf), MSG_ERRQUEUE) | 返回 -1，errno 为 EAGAIN |
| [`LTP_7EB2D64ACBEF14A7`](../../library/rules/ltp-7eb2d64acbef14a7.yaml) | USER_BUFFER | 调用 recv(s, buf, sizeof(buf), 0) | 返回 -1，errno 为 ENOTSOCK |
| [`LTP_B34188BD305465CA`](../../library/rules/ltp-b34188bd305465ca.yaml) | USER_BUFFER | 调用 recv(s, buf, sizeof(buf), 0) | 返回 -1，errno 为 EBADF |
| [`LTP_C7E8278CFEF81C98`](../../library/rules/ltp-c7e8278cfef81c98.yaml) | USER_BUFFER | 调用 recv(s, buf, sizeof(buf), MSG_OOB) | 返回 -1，errno 为 EINVAL |
## `recvfrom`

共形成 7 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_2B9F3F4A853A14C6`](../../library/rules/ltp-2b9f3f4a853a14c6.yaml) | USER_BUFFER | 调用 recvfrom(s, (void *)buf, sizeof(buf), 0, (struct sockaddr *)&from, &fromlen) | 返回 -1，errno 为 EINVAL |
| [`LTP_2FAD34B153D5914E`](../../library/rules/ltp-2fad34b153d5914e.yaml) | USER_BUFFER | 调用 recvfrom(s, buf, sizeof(buf), 0, (struct sockaddr *)&from, &fromlen) | 返回 -1，errno 为 ENOTSOCK |
| [`LTP_8AC9E6F26C2E3CFE`](../../library/rules/ltp-8ac9e6f26c2e3cfe.yaml) | USER_BUFFER | 调用 recvfrom(s, (void *)buf, sizeof(buf), MSG_OOB, (struct sockaddr *)&from, &fromlen) | 返回 -1，errno 为 EINVAL |
| [`LTP_A6B15E4F4EBDDB36`](../../library/rules/ltp-a6b15e4f4ebddb36.yaml) | USER_BUFFER | 调用 recvfrom(s, (void *)buf, sizeof(buf), 0, (struct sockaddr *)-1, &fromlen) | 返回 0，errno 为 ENOTSOCK |
| [`LTP_D8E4FF36A3FE1F41`](../../library/rules/ltp-d8e4ff36a3fe1f41.yaml) | BAD_USER_ADDRESS、USER_BUFFER | 调用 recvfrom(s, (void *)-1, sizeof(buf), 0, (struct sockaddr *)&from, &fromlen) | 返回 -1，errno 为 EFAULT |
| [`LTP_DD647A49F00FCC45`](../../library/rules/ltp-dd647a49f00fcc45.yaml) | USER_BUFFER | 调用 recvfrom(s, (void *)buf, sizeof(buf), MSG_ERRQUEUE, (struct sockaddr *)&from, &fromlen) | 返回 -1，errno 为 EAGAIN |
| [`LTP_F101CC6D9DF71519`](../../library/rules/ltp-f101cc6d9df71519.yaml) | USER_BUFFER | 调用 recvfrom(s, buf, sizeof(buf), 0, (struct sockaddr *)&from, &fromlen) | 返回 -1，errno 为 EBADF |
## `recvmmsg`

没有形成可发布的合规性规则。

## `recvmsg`

没有形成可发布的合规性规则。

## `remap_file_pages`

没有形成可发布的合规性规则。

## `removexattr`

没有形成可发布的合规性规则。

## `rename`

共形成 18 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_1028A46194A35788`](../../library/rules/ltp-1028a46194a35788.yaml) | 无额外前置条件 | 调用 rename(TEST_EROFS, TEST_NEW_EROFS) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_2A0C51A9F627F9EE`](../../library/rules/ltp-2a0c51a9f627f9ee.yaml) | 无额外前置条件 | 调用 rename(old_file_name, new_file_name) | 调用成功，返回 SUCCESS |
| [`LTP_2E4BA3FA59A48F0F`](../../library/rules/ltp-2e4ba3fa59a48f0f.yaml) | 无额外前置条件 | 调用 rename(OLD_DIR_NAME, NEW_DIR_NAME) | 调用成功，返回 SUCCESS |
| [`LTP_2EBC825D5CF7EF0F`](../../library/rules/ltp-2ebc825d5cf7ef0f.yaml) | 无额外前置条件 | 调用 rename(old_dir_name, new_dir_name) | 调用成功，返回 SUCCESS |
| [`LTP_3EC51D87D4A4C0C2`](../../library/rules/ltp-3ec51d87d4a4c0c2.yaml) | 无额外前置条件 | 调用 rename(TEMP_FILE, TEMP_DIR) | 返回 -1，errno 为 EISDIR |
| [`LTP_43BC8A0B853CD8DB`](../../library/rules/ltp-43bc8a0b853cd8db.yaml) | 无额外前置条件 | 调用 rename(TEMP_FILE1, TEMP_FILE1) | 调用成功，返回 SUCCESS |
| [`LTP_54D221925C324829`](../../library/rules/ltp-54d221925c324829.yaml) | 无额外前置条件 | 调用 rename(DIR1, DIR2) | 返回 -1，errno 为 ENOTEMPTY |
| [`LTP_6821C2F644329FB4`](../../library/rules/ltp-6821c2f644329fb4.yaml) | NON_DIRECTORY_PATH_COMPONENT | 调用 rename(TEMP_DIR, TEMP_FILE) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_9062D40054E147B9`](../../library/rules/ltp-9062d40054e147b9.yaml) | 无额外前置条件 | 调用 rename(DIR1, DIR2) | 返回 -1，errno 为 EINVAL |
| [`LTP_90CF6ADF43644434`](../../library/rules/ltp-90cf6adf43644434.yaml) | PATH_TOO_LONG | 调用 rename(TEMP_FILE, long_name) | 返回 -1，errno 为 ENAMETOOLONG |
| [`LTP_9D13DF07435A4B33`](../../library/rules/ltp-9d13df07435a4b33.yaml) | PERMISSION_DENIED_STATE | 调用 rename(SRCFILE, DESTFILE) | 返回 -1，errno 为 EACCES |
| [`LTP_CA1E4549CF7692F9`](../../library/rules/ltp-ca1e4549cf7692f9.yaml) | BAD_USER_ADDRESS | 调用 rename(INVALID_PATH, TEMP_FILE) | 返回 -1，errno 为 EFAULT |
| [`LTP_D17799C1BB191952`](../../library/rules/ltp-d17799c1bb191952.yaml) | 无额外前置条件 | 调用 rename(TEST_EMLINK, TEST_NEW_EMLINK) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_D758596147111328`](../../library/rules/ltp-d758596147111328.yaml) | 无额外前置条件 | 调用 rename(OLD_FILE_NAME, NEW_FILE_NAME) | 调用成功，返回 SUCCESS |
| [`LTP_D7936678BF685610`](../../library/rules/ltp-d7936678bf685610.yaml) | BAD_USER_ADDRESS | 调用 rename(TEMP_FILE, INVALID_PATH) | 返回 -1，errno 为 EFAULT |
| [`LTP_D98D789F4EBA6817`](../../library/rules/ltp-d98d789f4eba6817.yaml) | 无额外前置条件 | 调用 rename(elooppathname, TEST_NEW_ELOOP) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_E1B6C6D1C8603A83`](../../library/rules/ltp-e1b6c6d1c8603a83.yaml) | 无额外前置条件 | 调用 rename(TEMP_FILE1, TEMP_FILE2) | 返回 -1，errno 为 EPERM |
| [`LTP_FEDD56BEBCE11F81`](../../library/rules/ltp-fedd56bebce11f81.yaml) | PATH_TOO_LONG | 调用 rename(TEMP_FILE, long_path) | 返回 -1，errno 为 ENAMETOOLONG |

## 技术参考

- 报告 ID：`spec-20260716t042005z-e81fdaef`
- 来源：`ltp-local`，内容快照 `sha256:d789747f0c0bf1697f538bc5166073fd8449dec3beac7b12ac0be0b1b716dcb4`
- 全局待处理 syscall：213
- 提取数量：`80`（来源：`command`）
- `memcpy`：证据 1 条，未解析 0 条
- `memfd_create`：证据 6 条，未解析 1 条
- `memset`：证据 1 条，未解析 0 条
- `migrate_pages`：证据 1 条，未解析 0 条
- `mincore`：证据 3 条，未解析 0 条
- `mkdir`：证据 7 条，未解析 1 条
- `mkdirat`：证据 2 条，未解析 0 条
- `mknod`：证据 14 条，未解析 2 条
- `mknodat`：证据 3 条，未解析 2 条
- `mlock`：证据 10 条，未解析 0 条
- `mlock2`：证据 4 条，未解析 0 条
- `mlockall`：证据 3 条，未解析 0 条
- `mmap`：证据 22 条，未解析 0 条
- `modify_ldt`：证据 4 条，未解析 2 条
- `mount`：证据 15 条，未解析 1 条
- `mount_setattr`：证据 9 条，未解析 0 条
- `move_mount`：证据 4 条，未解析 0 条
- `move_pages`：证据 2 条，未解析 0 条
- `mprotect`：证据 7 条，未解析 0 条
- `mq_notify`：证据 7 条，未解析 0 条
- `mq_open`：证据 1 条，未解析 1 条
- `mq_timedreceive`：证据 0 条，未解析 0 条
- `mq_timedsend`：证据 0 条，未解析 0 条
- `mq_unlink`：证据 1 条，未解析 1 条
- `mremap`：证据 4 条，未解析 2 条
- `mseal`：证据 4 条，未解析 2 条
- `msync`：证据 5 条，未解析 0 条
- `munlock`：证据 4 条，未解析 0 条
- `munlockall`：证据 2 条，未解析 0 条
- `munmap`：证据 5 条，未解析 0 条
- `name_to_handle_at`：证据 6 条，未解析 1 条
- `nanosleep`：证据 5 条，未解析 0 条
- `newuname`：证据 1 条，未解析 0 条
- `nftw`：证据 0 条，未解析 0 条
- `nice`：证据 12 条，未解析 2 条
- `open`：证据 31 条，未解析 3 条
- `open_by_handle_at`：证据 3 条，未解析 0 条
- `open_tree`：证据 4 条，未解析 1 条
- `openat`：证据 15 条，未解析 2 条
- `openat2`：证据 5 条，未解析 0 条
- `pathconf`：证据 4 条，未解析 0 条
- `pause`：证据 3 条，未解析 0 条
- `perf_event_open`：证据 1 条，未解析 1 条
- `personality`：证据 3 条，未解析 0 条
- `pidfd_getfd`：证据 6 条，未解析 0 条
- `pidfd_open`：证据 9 条，未解析 0 条
- `pidfd_send_signal`：证据 6 条，未解析 0 条
- `pipe`：证据 13 条，未解析 1 条
- `pipe2`：证据 3 条，未解析 3 条
- `pivot_root`：证据 2 条，未解析 1 条
- `pkeys`：证据 1 条，未解析 0 条
- `poll`：证据 17 条，未解析 0 条
- `ppoll`：证据 0 条，未解析 0 条
- `prctl`：证据 35 条，未解析 4 条
- `pread64`：证据 3 条，未解析 0 条
- `preadv`：证据 6 条，未解析 1 条
- `preadv2`：证据 6 条，未解析 0 条
- `process_madvise`：证据 2 条，未解析 0 条
- `profil`：证据 0 条，未解析 0 条
- `pselect`：证据 4 条，未解析 1 条
- `ptrace`：证据 14 条，未解析 2 条
- `pwrite64`：证据 6 条，未解析 0 条
- `pwritev`：证据 6 条，未解析 1 条
- `pwritev2`：证据 4 条，未解析 0 条
- `quotactl`：证据 17 条，未解析 5 条
- `read`：证据 6 条，未解析 0 条
- `readahead`：证据 4 条，未解析 0 条
- `readdir`：证据 3 条，未解析 1 条
- `readlink`：证据 5 条，未解析 3 条
- `readlinkat`：证据 4 条，未解析 0 条
- `readv`：证据 4 条，未解析 2 条
- `realpath`：证据 2 条，未解析 0 条
- `reboot`：证据 5 条，未解析 3 条
- `recv`：证据 1 条，未解析 0 条
- `recvfrom`：证据 1 条，未解析 0 条
- `recvmmsg`：证据 2 条，未解析 1 条
- `recvmsg`：证据 2 条，未解析 1 条
- `remap_file_pages`：证据 1 条，未解析 1 条
- `removexattr`：证据 3 条，未解析 2 条
- `rename`：证据 30 条，未解析 0 条

<details>
<summary>机器可读元数据</summary>

<!-- syscallguard-metadata -->
```yaml
schema_version: 1
kind: syscallguard_ingest_report
report_id: spec-20260716t042005z-e81fdaef
generated_at_utc: '2026-07-16T04:20:06.737209Z'
source:
  id: ltp-local
  type: ltp
  snapshot_hash: sha256:d789747f0c0bf1697f538bc5166073fd8449dec3beac7b12ac0be0b1b716dcb4
  descriptor_hash: sha256:4315924cd8b9aab9608c225950c81f18ab74f25d63d74ee6ac3c444132131b4d
  recognition_rules_hash: sha256:84d715591e7abe5f2ac2de68c75172b2b2389541f6f8b8f23582b8cff81b057e
  resolution: default_source
count:
  value: '80'
  source: command
pending_count: 213
selected_syscalls:
- memcpy
- memfd_create
- memset
- migrate_pages
- mincore
- mkdir
- mkdirat
- mknod
- mknodat
- mlock
- mlock2
- mlockall
- mmap
- modify_ldt
- mount
- mount_setattr
- move_mount
- move_pages
- mprotect
- mq_notify
- mq_open
- mq_timedreceive
- mq_timedsend
- mq_unlink
- mremap
- mseal
- msync
- munlock
- munlockall
- munmap
- name_to_handle_at
- nanosleep
- newuname
- nftw
- nice
- open
- open_by_handle_at
- open_tree
- openat
- openat2
- pathconf
- pause
- perf_event_open
- personality
- pidfd_getfd
- pidfd_open
- pidfd_send_signal
- pipe
- pipe2
- pivot_root
- pkeys
- poll
- ppoll
- prctl
- pread64
- preadv
- preadv2
- process_madvise
- profil
- pselect
- ptrace
- pwrite64
- pwritev
- pwritev2
- quotactl
- read
- readahead
- readdir
- readlink
- readlinkat
- readv
- realpath
- reboot
- recv
- recvfrom
- recvmmsg
- recvmsg
- remap_file_pages
- removexattr
- rename
syscalls:
- syscall: memcpy
  source_fingerprint: sha256:470795acc045bdb94d306cf37913f9295ff579d08cb7f9afe37b200014085d13
  recognition_fingerprint: sha256:f7186da1e8b71b79b2be81294af4cbc4ed3e37c11876f313c51107ed03493588
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: memfd_create
  source_fingerprint: sha256:c73822e02f78fdbda2e5f75daf7fd7b3894c80c07401ef7970bb5bc34f0d5f1a
  recognition_fingerprint: sha256:01e0c5a394e995c323cee3b7c90b6026135eda55cf002a243ae94e8db422d57f
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: memset
  source_fingerprint: sha256:ab18dfae9d58d8c3acf47260042f361f3b8e97cd60f6151d83c85c8e4951538f
  recognition_fingerprint: sha256:84fa318c193e3b8bdbe775f0695d8248348f85a55fef2db47d822716faee8677
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: migrate_pages
  source_fingerprint: sha256:1cdc50532b9752eef79c66730260e8de7b1e222f6fc399ec43725549c6a1cd6f
  recognition_fingerprint: sha256:67067e542a6075599954856ad16758258135c87a8c0050cb83e63a02819bae30
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_FE4A57F142065A14
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:fe4a57f142065a14d886e22c222559644c54a37dfe7f971b7fe6ab3b59707f11
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: mincore
  source_fingerprint: sha256:236845a111c281409c3452a36a4c715e01970410e955abc75d0ef3fddddd3ce9
  recognition_fingerprint: sha256:8a1f99f784fad7adbe89f8b8e1efc13249b3d464fde00c9ddf1e95c8e25559e9
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_34A03F3861C10C4E
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:34a03f3861c10c4e51661f2217847ff299153f412994a8fd329ec082652bba7d
  - id: LTP_3A18518E9A9DDC47
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:3a18518e9a9ddc476c43becc3aeae2f5eb8dbb66225c2131409280ef0d5ab244
  - id: LTP_4032B15A045CC9CD
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:4032b15a045cc9cdc2c9ae31e9e94f793be4b38c25dc93667ef610851e26c31d
  - id: LTP_A426BD8C5041DE5E
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:a426bd8c5041de5e7faaefe1a59e2d1cc60184e20d4aed73640adca310fb38df
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: mkdir
  source_fingerprint: sha256:2f9cf52bad4c4554a81d3e9a091c4e05fe10109fde0687fa748724b00f166c0d
  recognition_fingerprint: sha256:aa519bc9452a1a7a96d0f66409df9980ddc895f075dd8ef3af85aa6c838e20b4
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 7
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: mkdirat
  source_fingerprint: sha256:b7d9665f2967f632796a35b5298cc7235fe9e161bb178adf61c44142d685ffd9
  recognition_fingerprint: sha256:ba18accd90165e0ec28e448335c8e66ab34c26dbfb1a435b81f04c33e3b164dc
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_01E0E5231C9C3654
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:01e0e5231c9c36542e08632bef53669e6e944c010e2196ea1549bfd52a6a7b77
  - id: LTP_6174E3690A05F1CA
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:6174e3690a05f1ca197873252a1e0d7555885e03bd2876ff2761725dd8cda77d
  - id: LTP_9D233BC9DED7A8AA
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:9d233bc9ded7a8aa16f6d468fe19fdd31eb7ee27c7cd6479e296b1f46587e416
  - id: LTP_B917BA457313E93D
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:b917ba457313e93d959e7a20a85b83e450053435c394910c399ac668eb46ac5e
  - id: LTP_BBBCFD7524CBB3CD
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:bbbcfd7524cbb3cdd78d1f04ec595fc3679c4188c19f97ce5aec2f5fcf15d00f
  - id: LTP_D2E5AAE97E0E50FE
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d2e5aae97e0e50fe79434f31202187d87b98abed46a1f0496c419718d67fbdcd
  - id: LTP_EE540E689227BDBF
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:ee540e689227bdbf55a518a7fa232132f9e5f953ba268867f1582581f9f6a497
  - id: LTP_F6DD03A9DC1C07D4
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:f6dd03a9dc1c07d405b7e2e43241d2a5292df8f1ad9ad5103ab5b3e4d26208a0
  - id: LTP_FE8AA14F6A64DF2D
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:fe8aa14f6a64df2d1b70243fd62c350166281f91a8854037433e6931d93e99cd
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: mknod
  source_fingerprint: sha256:b266caedea786cbd37943930762732f7df22fcf0b39561f9f4d0f8b9509a776d
  recognition_fingerprint: sha256:838e07d9aab2d81beb24ae9287b530198fe0c2ce164aa1c6e4895a64dee11ac4
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 14
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: mknodat
  source_fingerprint: sha256:c98d401281482e5d3cbb9f64105caf739b243b4d0b978195f4dc9ff441a25ac1
  recognition_fingerprint: sha256:b7cb31bc885d980bbb485b37f85ead3ea28c4d5f10d12487918fdae6008fd0cb
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: mlock
  source_fingerprint: sha256:636e1d77a2de77f6d58d05018ec69ef1c660917a6fece9eed86b7438638c61fd
  recognition_fingerprint: sha256:ca5ea832f056640030358ae980ad8d0c387321163140e16f199c9cb17854c2d2
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_04FC167B4A1C57FB
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:04fc167b4a1c57fb6932d1a7aec66311e943fdab7dcd50d7725c154856922944
  - id: LTP_1C1877AB6CAE8906
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:1c1877ab6cae89065ed8da38b9d563f18547ad4af122f8567052e27558bca3ec
  - id: LTP_4ED7FF29685C11B0
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:4ed7ff29685c11b00854306ad62c06da01ee82de6e9573a207afdad76a1e99a3
  - id: LTP_8C796FAE0FBF7688
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:8c796fae0fbf768850b62a73ca5179b093a50f9594ce30b00b271110688083e4
  - id: LTP_C05360D699C55915
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:c05360d699c559150df3c3a42d5d34bc55ba91cd49242655320645bb43ee716d
  - id: LTP_F61B5384B4A60F55
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:f61b5384b4a60f5592727e2b67e908ef02b250d1cf9623afe062d957392c85ae
  - id: LTP_FC50E16C03A7EED9
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:fc50e16c03a7eed9d559a75a1996717af389421823f601fc37f5b3813703162b
  evidence_count: 10
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: mlock2
  source_fingerprint: sha256:20b927a2f8b3ada20fe0d2f352d4f6360fbd1f29bd92b905da559be8ae0156bc
  recognition_fingerprint: sha256:9b5cbd77a5b85f7754954c23a7525aba15214fbba4a30ddfe09f49cff2d9e5aa
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_074981FFB7FA5DB7
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:074981ffb7fa5db73615c77a87030dcaaa1986aec18d298378c656a14d6d163a
  - id: LTP_16B8EA75C5016419
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:16b8ea75c5016419538d1607b8634924f5c05e5cf30c5e10ba39b0fbeae23626
  - id: LTP_2FDCA4DAED71F98B
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:2fdca4daed71f98b076a5c4b966708011711c6c7c63080bcc1df2f091abbdb82
  - id: LTP_3471B46784E57E93
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:3471b46784e57e93add1f02a00f74afe066095dff50dbb9cf2f7e38ec6e2c75a
  - id: LTP_592639F40E0FF63A
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:592639f40e0ff63a180438e5ee8f78ac33e5716106066f5987588d135bb7cb2b
  - id: LTP_669BB2DCB1D95979
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:669bb2dcb1d9597911edd90cebde9144a1cf89e03d489b5cb8395df002f490c1
  - id: LTP_715AAC0BA45C0567
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:715aac0ba45c05670ea3b3d53cf1e46c4b97b0dbcc989991b839868b38a631d9
  - id: LTP_7C995D43920E57D0
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:7c995d43920e57d08bd5e018ea4cb4075068ff370e247a5ddbc5f0225042e2b0
  - id: LTP_8731C07ADFDC57F6
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:8731c07adfdc57f6420d8259f1df5c54376d18a06a0dba1a682c63ed989524da
  - id: LTP_9869F02C8AF1851D
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:9869f02c8af1851dcd15433890c720d4d1b4a5418dbf2c85d510e55b474bf955
  - id: LTP_D191923C5ACBADC1
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d191923c5acbadc14d84fbe260fc84a0df7e72798b9ac94910aa717912750dea
  - id: LTP_D9418F7424E86C28
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d9418f7424e86c28e525f8bafe039c85a9e938f4e9de0be59a528d86070e5a0e
  - id: LTP_F7AC6006DC3C06BB
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:f7ac6006dc3c06bbcd16e10e9db80270ddabb8380ac327ee805d33e7601b3e35
  - id: LTP_FE9B97F71E485E58
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:fe9b97f71e485e58e58463ef8149e4c813a19ba553ff0306a4e4c949ba87fb18
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: mlockall
  source_fingerprint: sha256:01d6347d35ec4f409b3bf6a46f7e2cfe3497b8981b7d1dd484243ab6821cec3e
  recognition_fingerprint: sha256:e2a22827069695699128ef9815d5908b2dbb401caa5660bb3e648e59697229cf
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_06EAAEA7DDC8627E
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:06eaaea7ddc8627e0dd1ac6aebe40d77853b5205e02dcf6d503f1288e0690e46
  - id: LTP_0D59D1FBC322425B
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:0d59d1fbc322425b979d21c81beabaf9dc6ea82f2c8b62edc90721824d4a34d7
  - id: LTP_154DEC6769244339
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:154dec676924433965912bbaaed76511a95ccb6f69531b768a22256f4e79886e
  - id: LTP_6F89F9EF4C3D3857
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:6f89f9ef4c3d3857f202ed4efc432e63429f54ccdecf01809b988c65d83b0dae
  - id: LTP_C054C1DCF56C7CDC
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:c054c1dcf56c7cdc6e89fd821927ee9b12fdc717c0f342b669d2296a718172aa
  - id: LTP_CD185859D6C012C8
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:cd185859d6c012c832c3b1e14349d28127bea7d2f94d7fb9bf77dcecda43c3a6
  - id: LTP_D7FFD8EE209AB524
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d7ffd8ee209ab524d4563423230af612f4eb606e573f2e54a9a57bb27a656c79
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: mmap
  source_fingerprint: sha256:42415bb3e243bb4071298a44afbfd9c74353212d3d793de7687920a485a52a71
  recognition_fingerprint: sha256:dc3a315c243879b89d0eaa8d9d6eed83b789cbf5eb7481537a4cfc195658ddce
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_36C99C10CD38F8DB
    generated_at_utc: '2026-07-14T13:38:13.033184Z'
    content_hash: sha256:36c99c10cd38f8db26e721ea351430f0ebc4767b9a31257223ad8fd5519c7d0d
  - id: LTP_45439D8F2BAB0832
    generated_at_utc: '2026-07-14T13:38:13.033184Z'
    content_hash: sha256:45439d8f2bab0832027a39e78d024f72cc6449adff9fb823af60ff7c004d7bc5
  - id: LTP_51E295101A9F4411
    generated_at_utc: '2026-07-14T13:38:13.033184Z'
    content_hash: sha256:51e295101a9f4411b8c43521d430e85bd27ac1d7a96127b66675d7dc024ba9d2
  - id: LTP_52BAFC01DEA6E172
    generated_at_utc: '2026-07-14T13:38:13.033184Z'
    content_hash: sha256:52bafc01dea6e1725e71d23e11424031141e37ea07b99e151db6bcfc16116bde
  - id: LTP_791DEA825D66980B
    generated_at_utc: '2026-07-14T13:38:13.033184Z'
    content_hash: sha256:791dea825d66980bfded73936e4745cf7b914f20652b9489e65a7a59509b897b
  - id: LTP_C346EFF1233F7061
    generated_at_utc: '2026-07-14T13:38:13.033184Z'
    content_hash: sha256:c346eff1233f706172a595326e9215b63dd1f455b13880c762f92532db036e2e
  - id: LTP_F36F8C0CC1A6D840
    generated_at_utc: '2026-07-14T13:38:13.033184Z'
    content_hash: sha256:f36f8c0cc1a6d84025a2394e30fa1d7c273ce9c13d8f58d759383c75dbf8c10a
  - id: LTP_FD1B65B0BCC88E0D
    generated_at_utc: '2026-07-14T13:38:13.033184Z'
    content_hash: sha256:fd1b65b0bcc88e0d283d47737c8b9d244de44d7461e8efd5bc6eb699ebaa0d54
  - id: LTP_FEACDC300C3E1DD7
    generated_at_utc: '2026-07-14T13:38:13.033184Z'
    content_hash: sha256:feacdc300c3e1dd754c7925df645b95995a6f17fd0ebcb6a50578071e2f9636f
  evidence_count: 22
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: modify_ldt
  source_fingerprint: sha256:fba411cb8712c152c969813d5a88eee8b9287635f22602c072cf8bd03d662ea7
  recognition_fingerprint: sha256:8b4e5d4955dd347435290f58f69f3649f987e2677b8231df68108235beaf1607
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: mount
  source_fingerprint: sha256:d1c68b66f2ac2308eb5754e50f21dada8986642631d4d3cf498fa4de4fd91458
  recognition_fingerprint: sha256:3aedf8c2439dccb2e4a50aa7e3f495bd65dea8e6346fc7779fb330eb5f230d68
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 15
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: mount_setattr
  source_fingerprint: sha256:421e505b156fc5413c9b63ad6ba86dc546d6c74e707756c7ae1cc59bf0bc98a0
  recognition_fingerprint: sha256:c1fe7796c7a60308bcbcd2a52cd6973122a51f7ce3ef3457d19ef99e631110b9
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_5E8446D4A0B40C0E
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:5e8446d4a0b40c0e79dbca4ae5f68d34176ed978a8a62a1f3ba7e0c503760724
  - id: LTP_5F50BCA4675B4B03
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:5f50bca4675b4b03967d3a238eaf7ad5f0142849042f56a4a65253061864f06a
  - id: LTP_A48CE326DC781ECE
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:a48ce326dc781ece28c3fdbd5e79fa70041eebd0fead9dd29e4fc11f475762d7
  - id: LTP_D3506D1539EC71AB
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d3506d1539ec71abedc6bf48e30ca4d4ab8c3c7970d6d0b5e33dfa724b2ab935
  evidence_count: 9
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: move_mount
  source_fingerprint: sha256:7a04584f3f3cc2771fb1c193f366623b309695178bb64e69fdd0d40696766f2c
  recognition_fingerprint: sha256:6b4b73ca339ae6ea18570836329e585d95e59ea0033946188744ee42571fd356
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_35AF6D3F6FC0EA61
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:35af6d3f6fc0ea61630ccd5cc1be80d490dced0daa0b2a619541838ae6db0f35
  - id: LTP_408787CB8F89AAF4
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:408787cb8f89aaf41e54f38d1c125af832cef3f22ca2583de291ff9aa4fb8254
  - id: LTP_6C5B2B87F34E7887
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:6c5b2b87f34e7887f74e4d5623016571c72f2c5ddae631dacdfc48759b55b555
  - id: LTP_7E14411F2FC9D9CF
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:7e14411f2fc9d9cfd435f6318f90790240113aa270eeb22b17a32c0feaf8095f
  - id: LTP_93C53F01B8732C42
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:93c53f01b8732c4247fddf6bbc96f8a1ea30b655f14e263428706d654b0d63ea
  - id: LTP_F1391DB634702128
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:f1391db63470212837a8a433201c3b16ac0085652d2484eb4517ae6eac0265eb
  - id: LTP_F284E6C48F6B4BF8
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:f284e6c48f6b4bf87c3e8ddb82d9ed93bfd66246c9595dba1befcd8427ff123b
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: move_pages
  source_fingerprint: sha256:eea8d8a50ef8ffc6d9e223810ffbea2aa02e9eb466ba48126d555328d56a55fa
  recognition_fingerprint: sha256:dfe9e27589e181a535f3b809a6fba32dc851a4151502b78d2f7eb736e1ac5c66
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: mprotect
  source_fingerprint: sha256:1c51e5e0b90c9d4931c8bc247d3b02bddca038dff01453e300d479c0a1fca592
  recognition_fingerprint: sha256:e20390ecd5143189fab8fd8b697bfd61855a3fc72d3ddd96cfea485833d1303a
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_08E1FDAFE6D66846
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:08e1fdafe6d668464f584599f7e87094e93736f36464d5707851b161a562ec0f
  - id: LTP_11852F99424BD7E5
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:11852f99424bd7e5878fe8d1dacc6815b17493a9cce40cf96abc38449fc82f6f
  - id: LTP_5E2B9548D2D9F147
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:5e2b9548d2d9f147619752d1552f1f7a15ada28d2b0374da04d95b22245d2f49
  - id: LTP_86E98E40777EA3FA
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:86e98e40777ea3fa060f00fc79eb6ef84d99e320bb7dfa43999defb2f4a170dc
  - id: LTP_882D8F6DFB4B7858
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:882d8f6dfb4b785838015eddcf67bb6ce2f2ec1921788aa8e74bc674f7215107
  - id: LTP_ED3B9CFAEBD0EAB8
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:ed3b9cfaebd0eab8d94ca2f91ad7eb1048b44bc066478b951e5d3ce042a06f27
  - id: LTP_FA4A7CD85E7F31FE
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:fa4a7cd85e7f31fee92eb0ec3515ae69a5a605c7c9d34d021571975e7e4bb290
  - id: LTP_FE37A7A30B8E2AFB
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:fe37a7a30b8e2afb25c4a40bc48724ccd3be8e7536ea5c626362b6e1a5289d18
  evidence_count: 7
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: mq_notify
  source_fingerprint: sha256:dc7e71f88d1ddfb256d674e3940ea5f95a0b26a27f9b1118ddf7784ff4654d8e
  recognition_fingerprint: sha256:7b38f37a84f226ea89ddee599347e4ca8c17c2d2013b9686aa8687169196ff45
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_11385EF43CBDA2E0
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:11385ef43cbda2e0161b08a04b54efb79405a48d4193203f61aca636e4d77409
  - id: LTP_462CE9A88054B448
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:462ce9a88054b4487bcd2143cecf9c86d81a7ea19657672dee1caba8b4f056fd
  - id: LTP_46DC592FFC5E5C44
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:46dc592ffc5e5c443fbb94593eeeddfa22359ea08d7152ab74b4af169993e924
  - id: LTP_6263797E65C75794
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:6263797e65c75794c63d6d6add4215a7f7947c6631298ef42d49c1c32064d691
  - id: LTP_828E39231372A771
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:828e39231372a771194fa90c58bcced054d7ab09b07cdcf3cbc1e814af2fb6ae
  - id: LTP_947B3CCE7DA0998E
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:947b3cce7da0998e1e8339fda8d2ffede4b295228350f29e0dd90d9a63fb0f04
  - id: LTP_A179D109B034EA29
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:a179d109b034ea29229411cca47142910419a96397aa777e2ae4ff04197f381e
  - id: LTP_D297A923D4C5FEC7
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d297a923d4c5fec7e28816290ffe7a5373b354ee7202be677b763d636248cc5e
  - id: LTP_E3B5C7908A7B12CC
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:e3b5c7908a7b12cc11d66c5771ba7070d48d703f8b6c0b1a66bb1e18edc1dcbb
  evidence_count: 7
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: mq_open
  source_fingerprint: sha256:49eede21b0ab9619fd4e3597c609d83f0d0d0153a473a3baff79b0b128351a18
  recognition_fingerprint: sha256:0dabcf4ae82360a68027235a5d566657be5569bdf4eb7e534eb86cf3a47697fe
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: mq_timedreceive
  source_fingerprint: sha256:330881550cea8b3e2443e0dd689e7a112de1d5b9c7c63d6e7e4760a883065765
  recognition_fingerprint: sha256:fd40093d8069f1bb638bd13f96fc97181f7e5778433c9605591dbadd2872a631
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: mq_timedsend
  source_fingerprint: sha256:f4b89cbd15aed4d1594fd4d5ba8717264bc1b575e5a6ead3d40b336034485823
  recognition_fingerprint: sha256:0467b9bbe2e3308d795553d62538401c92a5742bf9f7949faa8a2a7561f50bcd
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: mq_unlink
  source_fingerprint: sha256:a842164144065479594d59f9a623ec9b04a4d499a952d689fc427d6f9898245e
  recognition_fingerprint: sha256:abfc57d26f40d0961a9d6f586c9be69f68131da3c15bb63d0a957981afc86fa8
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: mremap
  source_fingerprint: sha256:771afc13897e6041a9d7b1568c119bfa42c62c5d7cbe876a0292b3aa8f9cd650
  recognition_fingerprint: sha256:c7dc91037ef82f196f6c25cb6888deec5a118ff4a69744f57ba8574de9d8e574
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: mseal
  source_fingerprint: sha256:403ef52e88331332a7ebff18c00c437efd88615cb03fe6b127bde38c96025e75
  recognition_fingerprint: sha256:7230b1bc0817c0ef04f3db8908159f680bd61ab5a1b5f2137530c037dae55715
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: msync
  source_fingerprint: sha256:5796104e5843466a7d2850f7d73449428a6a572f47cca62e8c6ac13efeef2aaa
  recognition_fingerprint: sha256:243409aafc89a08c0c16ff67bf0dec2ba8a1cd598356f4e3ca565ec4e8c3a35e
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_033FAA6E22CDE433
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:033faa6e22cde433c6c746b4db0fd4443ea3a6de3b72f67f5de2d681df59ef4a
  - id: LTP_2C37BF2D4F1059A2
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:2c37bf2d4f1059a2655b5c6b639fe7ce059485cae9589601062e3a4e0f485cc0
  - id: LTP_40621A9DFAF6D232
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:40621a9dfaf6d2327975db4d11396c8a1f47a9dd8e5995af2990554370318a66
  - id: LTP_4A4F50B0E250249A
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:4a4f50b0e250249a8b816ba0f63047e7f3db5c5e6ef96879b76a81f366c2a976
  - id: LTP_6DD85CE2E5952779
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:6dd85ce2e5952779addedb6296032e24e510d8766676ae794027a8303e490d81
  - id: LTP_D0A69D14ADE1718C
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d0a69d14ade1718cf67e498a5aff0182a431cc3b5424ff0cba7d8857dd621293
  - id: LTP_D2E2A5F40B2313E5
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d2e2a5f40b2313e5b9a3aa39a6922727d92fff4034821cbe122951d7c12aecce
  - id: LTP_EA90C626D9AA6C08
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:ea90c626d9aa6c082a3af19e015cee7a37eb943ced00e4fe6af33ec4f266ba04
  - id: LTP_F318E892720C2991
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:f318e892720c2991ec44a5c1f94a456ae72c0f8ab9d08e7d2598bc455808fd92
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: munlock
  source_fingerprint: sha256:bbc90a1cc43e956519cd738a7d89a7cd923c9fb191ab149269ddea8489fdeb55
  recognition_fingerprint: sha256:1ed2a5432f6aa7860477b0bb4a5f4a80c1bcfdd1a88fcaa1f655b6fcad85e690
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_4AF75A49B2F7AAB5
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:4af75a49b2f7aab5c5913fa4d5be036a7ac9113a218680fd7961b39eb6ecf1aa
  - id: LTP_4D9D59CFB785EB0C
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:4d9d59cfb785eb0ca2116744b600929c1e2361794f35e6e09e558ebcf993fd60
  - id: LTP_59A85FEDCED7BE77
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:59a85fedced7be774e7b8e9d780100aa0f9167764a9e75f2c9a9417475fcaa7c
  - id: LTP_AFDAD0AD4FE0E3FF
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:afdad0ad4fe0e3ff55dc8a6aff581876a8690e2289b5aefcf6e7b7ab7b94af61
  - id: LTP_B8A61982E829826E
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:b8a61982e829826ec22cb4e0d792090579e1dedd13bae43cc558ee6a9cb8da92
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: munlockall
  source_fingerprint: sha256:6e58d12736a7fc44ec4228bf5dae7f64bff29bd78dbf6d5d0f90ec8dfa9496c5
  recognition_fingerprint: sha256:9bd1a22ea341185d1e04367f7bbd62d0714d49bd884b33143564d471fecdc08f
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_EB40C6ADD4390CB3
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:eb40c6add4390cb303f9cc17fbcf034bead15a3218d03abf64db5bbf202797aa
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: munmap
  source_fingerprint: sha256:bc8fd6a245418a194f82a1a2d4955c8c01a0d1449e80b84b787f65d23be91445
  recognition_fingerprint: sha256:5ed4d8a682c8b85951cd86a5bbdf4bd27b898e9c5cdd3c6c0919619847436622
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_09ADB22B713F6C62
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:09adb22b713f6c623de9c08591d5c38bec8c26355a4d903d89c0ae680c54026f
  - id: LTP_26AE3C69D80D35F8
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:26ae3c69d80d35f8cde32c3371db6ddce43877024723415f2c15a30f19a02756
  - id: LTP_D744D6C4A0C3E40C
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d744d6c4a0c3e40c09a42998582b85c7cebc93e879005e2ac91dd7eed362ceff
  - id: LTP_E20E7069E7FA34D5
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:e20e7069e7fa34d525c29c0a916c6cecf3cd6aa52bde1c4fe108b0f2597b4a8b
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: name_to_handle_at
  source_fingerprint: sha256:1f5e356f11d7801a3ee731d1f435acd9d33c15ca7dc749e920abc7e60eb8c728
  recognition_fingerprint: sha256:ce62d70c8593fb540b6287644355501670c943e1fa8fe853739699c05ce7b6ea
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: nanosleep
  source_fingerprint: sha256:b048b2b0afc40eba39ec83b0427aee9f251ab945e4c0f24d6c7d256603141207
  recognition_fingerprint: sha256:ef699df5d68459148b1028037a878c2ea7b5e072556d4c51be980122b9b0f60d
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_6C8CC973DA350505
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:6c8cc973da350505d86955f0521e8b75c8308d4a9ed6cebb8b2c9da46e3681e9
  - id: LTP_DDCD82CA2726175D
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:ddcd82ca2726175d640fcb1ea60dd8a89639814178760365a308bd45dc95cd6a
  - id: LTP_FAF274CF431E6421
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:faf274cf431e6421308bcb9892f22171498b921ec7dc3d9e6eb6c3788ba473a8
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: newuname
  source_fingerprint: sha256:a257e357d28ff1d2e45e1ca7cc9c1d68c7b7de37f91a776e2d5fd27bd82ef830
  recognition_fingerprint: sha256:76aea1925da451a0468996d4d9794e846910c268115782565b0d393b2efeffe3
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: nftw
  source_fingerprint: sha256:e615be217ccf2d6a0607c1a4a7e295a2a008e99cf5bf74f0884870e42ae194e8
  recognition_fingerprint: sha256:6cf901e669359e03ae39d257ec15ebf8cc07f3fd2bbd73a92b02135c7b58ce8f
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: nice
  source_fingerprint: sha256:b16a8f0c654be0f466bc417b6c132aad6762ea14180908ee67da9e4612693608
  recognition_fingerprint: sha256:6ef78b5a3e5270be8216b57d145f95a52d019a4c2c3ebee03c793bf737ff2739
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 12
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: open
  source_fingerprint: sha256:82bbf67772e63a784b0f244f9afdd200e69f28a60fb553022e108ca28fdd79ee
  recognition_fingerprint: sha256:bf268a021a2d875116ec33185ddd81d8091960b9082882a78f578717ea52ad17
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 31
  unresolved_evidence_count: 3
  reason: unresolved_evidence
- syscall: open_by_handle_at
  source_fingerprint: sha256:bec3e4cae40f441098e84e17f20a92f52d56ac77d28e4a8602310c2eebcca7a3
  recognition_fingerprint: sha256:b3376ee454f475b86e1fbe34b6890c00c2e5c9fde48342278ece311b18af8bd6
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_0B898E71738ECEB7
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:0b898e71738eceb79aec4a504135bf7526669ed47892279792e1635ea8a46a0f
  - id: LTP_1B65027CA2FD0026
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:1b65027ca2fd0026fbb6c531676777203594144a36fdedda60265fa0293a1d41
  - id: LTP_326E9D51F4EF6E39
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:326e9d51f4ef6e39b1d063ea2f0e2ed34d269d9faee56b8918631fb4f15bc741
  - id: LTP_3FF54C2EFF286EF7
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:3ff54c2eff286ef70b7ce32a8039aacfc37d8e65cfc9072335b6abc7ff4153dc
  - id: LTP_46649CE57B3EFB7F
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:46649ce57b3efb7ff6045e894af6aaf0b5bee743616539aa24dde71adff04aef
  - id: LTP_53F53970B961AB32
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:53f53970b961ab328e2ac911f076fd3e137183adbf2f5c0f2df155d740e36539
  - id: LTP_E9D60674E416A5DC
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:e9d60674e416a5dca5bb397ae6c8827e9ea438205805c22e3c76af196fc666a3
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: open_tree
  source_fingerprint: sha256:95268b380ce94f8ad2af19ce1d43e526e6ddb5744e2cec6c2886bbe3d6a4427c
  recognition_fingerprint: sha256:7c3adeb9bfafde0d6341a7c6e233b94eb10bfd56319898d0205a5abf9775d45d
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: openat
  source_fingerprint: sha256:40d4a302661a60ae38c626ef0c826a6bceaa3dc4f38058428e6b214f8705bd91
  recognition_fingerprint: sha256:e037da20a2f7ac11443727043deba2b912fab185a2205397f3d069ae32555a26
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 15
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: openat2
  source_fingerprint: sha256:0519f9c6c4d0b31124a3bcbc3ca76f450e55bfb8a3a14512bb8578132407dbbe
  recognition_fingerprint: sha256:98a86309f82cf0d0ba6d52220b3919f145735d3f389d55535606520b218c8fe7
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_026CB4A1CA7CDC6B
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:026cb4a1ca7cdc6bf1b2e94352fa72c86bda5fc328c6ed9ae8983b4696a2c0f8
  - id: LTP_0F5654610A1780B6
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:0f5654610a1780b6a8d30727fc660e4d9069ad379a35fe0c1e8f461790db7d68
  - id: LTP_15FCB1A16CBF7B34
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:15fcb1a16cbf7b347720dcedffa25a4e7ee56bdb76f411197d0926e6bad01d56
  - id: LTP_4101795C27681AB4
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:4101795c27681ab4155c6f4693d0d225a8b1bd8861237f9a67aff2e0d2b4c2c6
  - id: LTP_47B47DF38E582CE0
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:47b47df38e582ce027d12ad309cb20ec35b45c18789e59eabb645f60e69bf6dc
  - id: LTP_57933F1DF2F98C34
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:57933f1df2f98c341829220b06d7e93f29c68a4bf63978219188544a7d1aade9
  - id: LTP_69317571BC0A39EC
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:69317571bc0a39ec75c2a9ea3895d0eb5a736226159ae82b09f7819a7b341474
  - id: LTP_7FEB3B276A8133AC
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:7feb3b276a8133ace4d382f6e864cfa9a9403d150aa7926a5fbf647348415230
  - id: LTP_8405B02758433FBC
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:8405b02758433fbcb45171791cb5f4acf2a626b57d9438231dc2a6cc47d0012b
  - id: LTP_845843CAB40A4F40
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:845843cab40a4f40411427b3cd3759e72402fe5de958bdaae1b5c9cd8800d54a
  - id: LTP_B984D0FF91909634
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:b984d0ff9190963405473304947e976fc6ca2529785f69f3b5d0aeedac73a637
  - id: LTP_D0800876342DE939
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d0800876342de9392e43300d2797ff5244107ca4127ddb02ed0ec08832b03e82
  - id: LTP_D33B1BBC658C83D4
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d33b1bbc658c83d40c4ecef3744f84c395f3e1911f394d3d19699a20afefc157
  - id: LTP_E56EFFCF50E90E41
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:e56effcf50e90e414d11cd8a6ba60ffc0df9ad200dfe703543beb1415b30acad
  - id: LTP_FD400AE357F2EBB3
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:fd400ae357f2ebb333557aefe8e1f71b6d1e1075b968972f1c121ab2bd3ac72b
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: pathconf
  source_fingerprint: sha256:885fd5f6259fd67809d5f8ba20d51898202c381fa1ba1d4cdc6b2d6e993b7eb2
  recognition_fingerprint: sha256:424264fef68ff4c5c1c9dc60a71618e5c239496e9d425e48e1b600fb44c97b45
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_16343E95C1C7EF47
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:16343e95c1c7ef4733244fce30322c1d28ee1a5723608a213a339c5e397ef1f0
  - id: LTP_1661259678F899BC
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:1661259678f899bcca16b9b69cb7a56163e634e8c91d6f58f39b13e8e16b9995
  - id: LTP_1707E748EA729431
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:1707e748ea7294315a816bd257a8518e6067cef2e4782fbcf446780c857e2841
  - id: LTP_1893FF0C4930806E
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:1893ff0c4930806e844312141cba38963977d16789cc842b19d51afb558a8393
  - id: LTP_1AD5BF710E8FB247
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:1ad5bf710e8fb24797000382f0a4327cb500ca42e3fe1056f1f4073e20d84590
  - id: LTP_33D0A33AC4655F3E
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:33d0a33ac4655f3eabd72aae27ed76246463c7e37cf2a548d97be97c6228bf17
  - id: LTP_50BD66A0A05AFE51
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:50bd66a0a05afe51acc9ddfe13d736361bd2685079416130d7ab91a9ecd81dfe
  - id: LTP_532E8E5A98C0A22D
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:532e8e5a98c0a22d5bc83886e639e747cea3a81f6575a89056445adc02d518a8
  - id: LTP_621EC309C3A75722
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:621ec309c3a7572276fde68dfe01103533fca0ad4c65e320637ba54a3272c721
  - id: LTP_779183F85F2C1278
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:779183f85f2c1278ce96f4480ccfe64e0036c174f940478067ef96b7d580e315
  - id: LTP_7A84C55AF45835C2
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:7a84c55af45835c23a0ad71d01c4b3afe44abaa00f27c08c30bf780a27cac4e2
  - id: LTP_7C67E10CB5F35EA2
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:7c67e10cb5f35ea253d5e7feee2a81523a0e3111e46dae784d7d513ce176604d
  - id: LTP_7FDF0704C50C872E
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:7fdf0704c50c872e7051a1befb816daf49149f613497ca3b4c9f1f5f5d325751
  - id: LTP_81F076122348B68A
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:81f076122348b68ab2bfe12869bbb5ac8030e0013952f1b7b7a9e46ddf3d313c
  - id: LTP_913EC5DF431DC6C2
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:913ec5df431dc6c2c92bfd6ab7053896f60b810f86a7a5aafed7b1c111a40771
  - id: LTP_9445A602B4F98B83
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:9445a602b4f98b83f280d7a971dd2c8db0099d6023a679b56a55696d0a27e078
  - id: LTP_BF31641F04151F3C
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:bf31641f04151f3cdd75004d611c03e59bc696f12b800746914b6bc6c8c39f9e
  - id: LTP_C87041F4B4B5A930
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:c87041f4b4b5a930334107c73250cc29436c01b1d802fe03d206ba9ab5b809ef
  - id: LTP_D30F83EC0B5B2E08
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d30f83ec0b5b2e08f6ed142483e725a3c143b86f996fdb587bee8fe4006c9e31
  - id: LTP_D331AAEAED1F6297
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d331aaeaed1f62973b4a3aa942661bb58ef4cc3b24e82bf1b2e93ea6aa79d865
  - id: LTP_DD64353E8E427275
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:dd64353e8e4272759f9e403a03aa85d287f7e7771ddb3a7c0db148e18273a7f4
  - id: LTP_EC19279F1BC5A623
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:ec19279f1bc5a6236fb0cbd33023acc9839fe365cce84fb5ac1f5e65265f36bb
  - id: LTP_FEDE14E9D4DE9A9D
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:fede14e9d4de9a9d30a830614024353c37ca96dff584cd4539f8466b8314e9d1
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: pause
  source_fingerprint: sha256:13071d1a993e570205eab1a8d3ce47b1983a51d890a552304cb85d5344f7fbf9
  recognition_fingerprint: sha256:9d58a29e258353a645151fe82653e8ed4c2e7ac6995e5901136a9a110e945351
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_9E2C65A6408DD9D3
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:9e2c65a6408dd9d3648c6177b7180dab2dd050cd61947ce94cb9d5624c71b7c8
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: perf_event_open
  source_fingerprint: sha256:e1e848858fae99154d14d3609a20a4e257653775a4dcb73d16591f485c89ce1a
  recognition_fingerprint: sha256:f903fa2f29bb06b561961507eba6ffbcaaa4ab44f8ddc5970c1da0508252b027
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: personality
  source_fingerprint: sha256:6a54c84b9245b9bda914f84a55ef976ee92bb621e09fef2f1f47236eacc8c6ae
  recognition_fingerprint: sha256:e11e1abd80d4c84658dc38561fd4351b89306829ef3307c6e875d0ae9ca53fc4
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: pidfd_getfd
  source_fingerprint: sha256:a5571bf56f504c7d43bf9f068325855bbdd536d7efd4301f5b06bfe01d3979b9
  recognition_fingerprint: sha256:305555f94838598ee9cb965a84f3599a4cb884bd8e91b75516640ba7378dffd4
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_0134FE6EEF60CBCD
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:0134fe6eef60cbcd4b30a1746723ab881063b6abe8b232821f8c9efd6976cee7
  - id: LTP_12EAE2F32232CC05
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:12eae2f32232cc054513265749d1c8b850ea44632a593b0ff518281906b7b930
  - id: LTP_249EC7CDE9C4682F
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:249ec7cde9c4682ff5fb9f33524da6cf9904d8e85b9447893c83705e85639533
  - id: LTP_254E7D0C8662B3BB
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:254e7d0c8662b3bb8a69de7f1fb9def8357ea30c2b37836ff66fae236ec13a89
  - id: LTP_43A681D8FCD1B740
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:43a681d8fcd1b740d1ffcec8bffb04b7ae654757bc960590d87fda037a945734
  - id: LTP_5322AC28C2EB6C16
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:5322ac28c2eb6c1633ef3aad4c16cc30f0be65c7bd19e5571d85d60bbf93ee8a
  - id: LTP_595C676EF473E6BD
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:595c676ef473e6bd2bce152e1ae5c32c2949f40cd5ec8bc1cd0d49bd1eebfa4c
  - id: LTP_77FED5FE42B62868
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:77fed5fe42b62868ea424673f30fd06afdcb0ed529bea6d6fcf7f98f229747ae
  - id: LTP_85106060CC8B99CF
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:85106060cc8b99cfd6483f1f6a5bc895fba9274adf4d4336df01f22769a6c37a
  - id: LTP_94654CBF1E34C32B
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:94654cbf1e34c32bf1084539d4860be43ac9bf85efc638a9becfd3e3b9f523dd
  - id: LTP_C9AF84778DBE8B78
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:c9af84778dbe8b78ce92292d9ed45fa8c9764d3d99363aa9d54d9766ef823e79
  - id: LTP_E6A7D5E5327D8ECC
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:e6a7d5e5327d8ecc3c071c1231bd4ab48a868a18cc19ced52ee1526bbb69b1ac
  - id: LTP_EA7E63D027CD6941
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:ea7e63d027cd6941db5f635805ab7fcdb3274ef77bf7291058741dd9da669775
  evidence_count: 6
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: pidfd_open
  source_fingerprint: sha256:d1f5e6eb062c1b49774940d20b7097704dbfbe26b36a3a1f87a6e75bdc530905
  recognition_fingerprint: sha256:9838cdd0c48da46fc6f0a135c54d4d8c94d94674bf550659770eb7af93056057
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_0311772B70C94C38
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:0311772b70c94c3843c413fb234d2465d0386aa9d621663ff836089bb0cbb67e
  - id: LTP_0EEADAF9E605632C
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:0eeadaf9e605632c4e99ed136cff1466763ab5fbdb29a2145f8421e2bde5506b
  - id: LTP_18E65E41E98D9E97
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:18e65e41e98d9e9706ec8d5064ed73b758a95fcff958eef12cbb8057734ae7c1
  - id: LTP_1BB76939FF2A40B5
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:1bb76939ff2a40b56089c39f1e2e8db30af944a15e86e47a4e98a572bd8319ea
  - id: LTP_3743BC827FB4F981
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:3743bc827fb4f9819137ea970af9f8219bfff5989b4fa99ce035c18fa3ca4937
  - id: LTP_7CD01664A3589136
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:7cd01664a35891364d75616f7f57532b980ad702dee33bc49c536f8eac95c26f
  - id: LTP_E5E64FCDA6CACABE
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:e5e64fcda6cacabe1fd65c1e34fab6acaeaec7ce8b9d45ffc7f870920cdc4131
  evidence_count: 9
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: pidfd_send_signal
  source_fingerprint: sha256:6bf40ccd638a0ddbf472875db83975bb4a4641d60a5cc4654ee204482b4aaae2
  recognition_fingerprint: sha256:e0245a4282bc44f708d6e72beba879e635e1f929d9edcb4cecdcbf25b63edf49
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_08C4F07A07C4C3F7
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:08c4f07a07c4c3f776844c10d23013377829536ac66aa22e94ab9a1d5237d780
  - id: LTP_08F05BA6ED1CEE6A
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:08f05ba6ed1cee6adc06e52236156d77d5c6dd5d4592642bd443aa47f5e425b7
  - id: LTP_0F9F906AC57F0B46
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:0f9f906ac57f0b46681f278334cb2b01f0fd674591bd10083a709b29ef258b52
  - id: LTP_B7606EDCC1F1031F
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:b7606edcc1f1031f03dcbbee11de9971f507606bf3de54fbdcc7838c4f6feffe
  - id: LTP_FAECCAD19268C313
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:faeccad19268c3134c5d17cf5d0015bfb99b0d899223bb31dbe525d0b5fb8def
  - id: LTP_FE471F5051750B9C
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:fe471f5051750b9c0c8067dda89dd4df0e308e63b1badc876cc73259788797be
  evidence_count: 6
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: pipe
  source_fingerprint: sha256:4ddb3ddd007727590f59ed46bb573e5b1219621bfba3ecee7b1d1709924f31dd
  recognition_fingerprint: sha256:c8838784924c6e88a87d24adb118f470da81fa9a9f38341fd3ca58baaf0788cb
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 13
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: pipe2
  source_fingerprint: sha256:09d31552b7c395e3956cd9eed766734399ac4ab7d492cecef97577ce3b108cf6
  recognition_fingerprint: sha256:2eaef4970afa1b2a8e35b63f82a3413df30d6c45f2f5f8ca31c733d571acde63
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 3
  reason: unresolved_evidence
- syscall: pivot_root
  source_fingerprint: sha256:c466c2481277ebdb072a4628483a3b56de9284dc4929226089fb9e2ce73900e9
  recognition_fingerprint: sha256:8a1f9057af3d0f59fb2687a8dede7960d45e522094756eb874d880149ff039c9
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: pkeys
  source_fingerprint: sha256:3a0ac31efa18088fcadcf179c5466bc6471abdb4b6e715ffa01d8683ac1bb07f
  recognition_fingerprint: sha256:093f298fadf8ba53154763732576e14dbd28af75130e53ff8cbfa6749864e1a5
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: poll
  source_fingerprint: sha256:5fd7cef5e37f0079cb2f3c5d0ceef5ec217a55cdbdca73d195f97f91751b663d
  recognition_fingerprint: sha256:e2f92136e3e583f2f3d993055dfb553d00b6be4564b18ba2e487a89cd1ed6ab1
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_018C7E7A08833780
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:018c7e7a08833780ea56eb2e109dabf8b177b424cae61d72d84873b6812286d9
  - id: LTP_403B654FD084895C
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:403b654fd084895c5395687cdccb4cf2c4e64520fe34862afc30db821c9b8850
  - id: LTP_51EC2B222D4690DB
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:51ec2b222d4690db3a603a7cf06d13e15c576d7e70905c8fa444d2e069374c9e
  - id: LTP_58266C6AA844BBBD
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:58266c6aa844bbbd0336451a2ebf02e3fd9c9a8a4e78416d05d0defbc4cecbf3
  - id: LTP_D87AF1C2D0AF66D2
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d87af1c2d0af66d2dc7d3535db2e8dade464f297fd9db1945c974a10e41f66f6
  evidence_count: 17
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: ppoll
  source_fingerprint: sha256:2a7c5917b092ea88f1b1152f4643717565dfc715cd0ee3e8487cab7279210c15
  recognition_fingerprint: sha256:ecab9ab86238918cfc3aa17a03d0d4b92842cff9f2e2815e4a828abac90c98a4
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: prctl
  source_fingerprint: sha256:08df0a52deb8977d45915480d221115255feb5ad769548d29a4cb12d7d89a640
  recognition_fingerprint: sha256:aea2532364ac30e76fe1fe38717049e86650aa018eef76452f46ce55a8e71a67
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 35
  unresolved_evidence_count: 4
  reason: unresolved_evidence
- syscall: pread64
  source_fingerprint: sha256:a0628d75ab6e572e447551877b8d0923b7fab6f96a0bee9b33e60cff03fc9592
  recognition_fingerprint: sha256:0a95fca9f841bf2d24be5a5876a2ef69a3db46f61aee95cd744e736c62b71bd9
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_3F60BBC08D86D573
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:3f60bbc08d86d5735c7e66550d7165b77386c0b9de2e3300bb3ccd48d5c0ee16
  - id: LTP_4BDFA76AA51D745B
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:4bdfa76aa51d745bf89870ab1fb7542097ff67029fa982b14a787a64a7306112
  - id: LTP_9CEE24911B622031
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:9cee24911b622031515f5a22737a658e636fbe6449d7504b9105790be8d613e3
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: preadv
  source_fingerprint: sha256:c6e7fe1ba727e60645588c3e9513aa14f32df9ef45b188b0fa0be90121bdc924
  recognition_fingerprint: sha256:ac8b8f5c0dad7676936aa2dace0b2bf55977690d0164b6ed2765c188874bb112
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: preadv2
  source_fingerprint: sha256:8f46b49cb74e7b771e36fbbca7310e2c6b90ede077bebd5117cf83730b1fd6b5
  recognition_fingerprint: sha256:70acae34bf58e5baf36d3fcfc4dda0e339d84a755ed99e7bf2ff41443620e48a
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_1AACAC53BAF23BA9
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:1aacac53baf23ba9aec716bf031354593948226151154448887698bf2a5dde0d
  - id: LTP_2A28494F77E0B173
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:2a28494f77e0b173725c00fec9d6dd33a01f558c208eb201a566a85d9e978f26
  - id: LTP_350B586A62C42467
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:350b586a62c42467b8440fbed04bba2b2852ba65f0984a89ccdaec120364a7b2
  - id: LTP_3EB53CD0B1672EE5
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:3eb53cd0b1672ee5bf44b072268216b8bef861d09fd38cad017e17b1e610ec0a
  - id: LTP_679924706FAFC4A5
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:679924706fafc4a58089a9e52433db6f9b7925f149bfcb4e357bac1cb20c3906
  - id: LTP_82907DD83DFD7800
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:82907dd83dfd780037d24929e3f15e6e024e9d57c71ecb132b6120d5db6cad9d
  - id: LTP_93F2091ECF31C3E0
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:93f2091ecf31c3e064c0dbd74696ea7a69ee72a21eafc189c369d4411320d3db
  - id: LTP_A4E6C06F187B9504
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:a4e6c06f187b950473eb0f50169a90c03253e1e9e9b4cc83bfcc79beb3f13468
  - id: LTP_AF0FA27496E3610E
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:af0fa27496e3610ec60127057b7278db69fd8af04ffe2699343876b0e7b2429b
  - id: LTP_B08ED7334608FAA8
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:b08ed7334608faa8a0a302f3b70aa7a225162cacfce3494a9adbe55199971455
  - id: LTP_B6DD7EB9951128C1
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:b6dd7eb9951128c1133ae31703ce75dc0b0a623cfe20220eaa3729566097ac81
  - id: LTP_DC3D9E7D5D1A75DE
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:dc3d9e7d5d1a75de583e19ecd659cac07cdf47b781870a8c5d95352ca974da9a
  - id: LTP_E2360C045F1BCE8E
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:e2360c045f1bce8e12d7c7fcee773858239da9852a29232b3fbb9c6135c50c50
  - id: LTP_F6456DE083F145B0
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:f6456de083f145b0b67323dd607c175b22926a3ecee6578c7b348d6a69a3bf40
  - id: LTP_FB3B521CE41A299A
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:fb3b521ce41a299a77ddf3c90f821324497caea4fed1f7a2feab6e64993a8037
  evidence_count: 6
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: process_madvise
  source_fingerprint: sha256:a98a057bdbdab683ac16c99c9fa99465da36d11a5e71159bd8afa1810e65ecf7
  recognition_fingerprint: sha256:f4b9617a47b115792fbfc1d391e34a1c3849d9a7796e6c79f295582fc1d5794b
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: profil
  source_fingerprint: sha256:1cd18e93512f96ae4edb5bcddecbd319eeffbcad42742346a9796581d73038a4
  recognition_fingerprint: sha256:0484ca9e0e7ef604145c902cee6a1911a5bd414608fe8ef9d63ead54d8363a5e
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: pselect
  source_fingerprint: sha256:1eef0fcb1b3d44d3ec3ab02036ba0b0207c4d58a4a1410a19b0acf5ab5d9ad08
  recognition_fingerprint: sha256:885e07a1b632ad86933b0ff45c1a08b029bd631e474ee2e8da41651a91ba76ba
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: ptrace
  source_fingerprint: sha256:7251ab449067fc33f074c1e83041e966498f066aab3312cdc973c0b1ed49b7b7
  recognition_fingerprint: sha256:818a1bc022817b3fdc9472c035cffc1b0342ec59e5d8c28836602306d432ab99
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 14
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: pwrite64
  source_fingerprint: sha256:c3c05677a616f91cde40cd34e95be15af20cc48fbfa5863f8b7a227ce7b000ab
  recognition_fingerprint: sha256:819073eca9e0ca5e47abd0f0484ee7fccda733bc788176a36e36e32f12381b15
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_0AE3E0188FBE5839
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:0ae3e0188fbe58395b6d79faeaa07e57ac14d765597f300619a77bda9693c1d5
  - id: LTP_15EC9351D2422944
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:15ec9351d2422944369dc92172ad29f11be0eb44336ba22d88498fcc2032ca7e
  - id: LTP_4E45B0701D5BD8A7
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:4e45b0701d5bd8a7237ee60c8dd4b9af9c2541ca19e65242d830d549f8a555b3
  - id: LTP_80B2CAF4B298BEE6
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:80b2caf4b298bee64fb6a706b6ee51ff7bb3371dc3966ec8691623079197c43c
  - id: LTP_D4E6A74BAB2E8722
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d4e6a74bab2e87222a34369ac51e811301e5af570bbad81040409f330a513eff
  - id: LTP_D5F414741594F6E3
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d5f414741594f6e346742580aef9bee1ebd3b8c7348b6f456c5f497db6780a78
  evidence_count: 6
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: pwritev
  source_fingerprint: sha256:03b6c10163f0006bc6c0e54d349a631c68a13ff45b3a4765df68695b4b01fa3b
  recognition_fingerprint: sha256:48f176473af39d4a1f7f1f77fd5fdca3f6039c33f1c81d8226d71847d13fd4c2
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: pwritev2
  source_fingerprint: sha256:bb227390e2fa981e3d806b939b058e63bae0f665010870d4eb4d50d2572dfad2
  recognition_fingerprint: sha256:51bea62f8d51dcc3cc58164e9b5d231117664fc4cd1a2dc5300bc1e3a67ccef9
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_1F2328B410A3010D
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:1f2328b410a3010d9a107beb059e36d4731444bc16f2826f9611cb5ce1b8217a
  - id: LTP_296D3DD5B2B27A84
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:296d3dd5b2b27a84fc85306c406355ed5cb04d124ae3fa579584919ae60912ef
  - id: LTP_3152706321BA354E
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:3152706321ba354ebe451193e5b49b178eb865d42e7a764ccbcbf58322acb645
  - id: LTP_56694FAD66174814
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:56694fad66174814030c577cb9e6a99a77bf10810b700c426dc551ae28ea66c4
  - id: LTP_74C13DA111D6D9BD
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:74c13da111d6d9bd1c72870349a54b9b4af5748e64b325e0a3cc26062b57e353
  - id: LTP_78A991C666EEFF75
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:78a991c666eeff7595c20942bf0891fc0da9b8a24768a34950ad51c2e1be6373
  - id: LTP_7C0B488884F6689C
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:7c0b488884f6689c5adc5b29fdb08f8bb2d2c1e8438761bbc5fe0c3ca7932463
  - id: LTP_9A3244C4CEBE8674
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:9a3244c4cebe8674abf16a7ecc24315eb1833dfcd6b10314ba84f83ae8b1e539
  - id: LTP_B06B0397728F35C3
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:b06b0397728f35c33b5fc8d0b08ce0555e5eef647f623ee21f4b3f9d2fb1892f
  - id: LTP_D1D51B0412DFB097
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d1d51b0412dfb0975fb7f3bb446e6bc756f86afb371de00a2f2b917b455c2951
  - id: LTP_DBAE060B9CA303DD
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:dbae060b9ca303dd48f5f810981c7f860cb8d05e67dab04b96d3d30c4dd29aec
  - id: LTP_EF4053B74F85E11B
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:ef4053b74f85e11bb6b1ed695e43b2370829ac81591dc1ee030a187a451bde1d
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: quotactl
  source_fingerprint: sha256:a1c5db38a4263a81478b302e04a6f5ee24a39903c03ef355f3f1f7274c91ce74
  recognition_fingerprint: sha256:d99e15072a1c2f6701858e08652504a93ceac1c40c4fcb97e335a9076549a7de
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 17
  unresolved_evidence_count: 5
  reason: unresolved_evidence
- syscall: read
  source_fingerprint: sha256:f109b39aa3a55a23a2e4e2fe4e616e79e35796ac3b66ef570b633fc169972028
  recognition_fingerprint: sha256:c1e527ded48c9e472538abed6fbd8247e1bf1089f986eaf3aa8bbc5098a23e2d
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_0087F445CEB63414
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:0087f445ceb63414b632c05b271af9fee6f2b3c7167fbc43e208a7b0a485ca33
  - id: LTP_2C266C6067333086
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:2c266c606733308616a1344419b7b5e00cbca89aa876e40280e9c63614240a35
  - id: LTP_7F0FE233BE49C811
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:7f0fe233be49c811ec769e845a3852ec2325869a78a25a525a7f4fda5e411907
  - id: LTP_9F30FD7002BC2EBA
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:9f30fd7002bc2ebaa326ab7ba6f3dbbba702f7a2c4f6008e3ade7ab4b84b4b94
  - id: LTP_A5BD363654740DDE
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:a5bd363654740ddec4466dcb7b0109061736d67df44a4fac40e035621e79d026
  - id: LTP_C8C667C37A069984
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:c8c667c37a06998461198d5df32e0481f509c0f12103aa55bb76b7eef34be7ce
  - id: LTP_D9A5AE03D93C5C6D
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d9a5ae03d93c5c6d41318874e7926906a3efc8a2b6384f8435b16250d2a777c4
  - id: LTP_FB7C7C6EA4808026
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:fb7c7c6ea4808026fb4235678c73bebaca4b4e60a2932fa5f90f282b6becf623
  evidence_count: 6
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: readahead
  source_fingerprint: sha256:5c6f6af058fd84162757bc23cd7e56763f1ea9ca74a548dcc192bfed9bc5bd99
  recognition_fingerprint: sha256:568cfd35009ec8129b024c9737987a95f1f485c119a26dbecfa80a7b5e110776
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_0F35A2F3718D172D
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:0f35a2f3718d172dabefe023e7389db8e9aeae66ab2774dfe77fa2b8cc72b2af
  - id: LTP_28410A5D4088E644
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:28410a5d4088e644ca9dadf8ba29badbad1d120a4e198eed790e45406a88b581
  - id: LTP_AA6F0F0A8A469B13
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:aa6f0f0a8a469b136667d815ec6ce470e15005441954ff0c744ff13bdd160eb9
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: readdir
  source_fingerprint: sha256:261f65cb7e55a5be7919856e4e07d3ce870ef688514f772848f94fe4b7f9436d
  recognition_fingerprint: sha256:0340ae488c514a6e15f61a0f9fb69f0612521a30ffd8b14d771f634dc40a5cea
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: readlink
  source_fingerprint: sha256:e4b3003dac401cf43daaec283d9b8a201bd9ba30043a1f941c869bde5a2a2d56
  recognition_fingerprint: sha256:be2063b84448d16d76162aee7d9d082c53290aa1f33933f57be4978e46cd2a1c
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 3
  reason: unresolved_evidence
- syscall: readlinkat
  source_fingerprint: sha256:450bab7abd94001b7470af3949ccb9100ba3e2a7ddbe35e9bd0abc4769c9698d
  recognition_fingerprint: sha256:7ac1be0f6753d1a68a56bfff58048fd951d8e4eee46105dbe71da53c36059855
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_048D7BAFDFD264F6
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:048d7bafdfd264f6112847a5ad9b4ff775bca430be47fb61eabe14fd6b681175
  - id: LTP_1505AAD11D4091B7
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:1505aad11d4091b7f077c711c6c659f63170d8e648c79c025f242504ec6340d1
  - id: LTP_209742037ADD09F1
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:209742037add09f12b1c7913cee022a50f65baabf47064576c959b662f23bb9c
  - id: LTP_30AF82AD36872B80
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:30af82ad36872b800cac405b387073530a85abb06b033be6822f30834d4c2012
  - id: LTP_55E78705E11C6E2D
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:55e78705e11c6e2d05fb5e7538367be1a1a0ec0d52957b873c79e0a9a6da60aa
  - id: LTP_5A2FE2DE55DC96EB
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:5a2fe2de55dc96eb45cebfc1be8e012707df11d5a5feac11d1ac5dac9d94d99a
  - id: LTP_5B5079DEC75B53F5
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:5b5079dec75b53f5b85d6f4580d9be2b8c2590946a88e421b3d8e80018548cc4
  - id: LTP_635254F85EA9B1B0
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:635254f85ea9b1b025c4d03e7c5a0d8f83a73dcc8b38d3e2df7700d967612e72
  - id: LTP_8B80C0CDA587165C
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:8b80c0cda587165c6b1660bc654c12c6fa804d8e1bffb36ef935515065239e72
  - id: LTP_8F4CA997DDB954AF
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:8f4ca997ddb954af54df87b6a587d4fa043e35334f07f9a1ef803e0ab9501f2a
  - id: LTP_9B32E51680CE0BEE
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:9b32e51680ce0beed95e9a27110440fa759b6bf385dc89dc29f6bb277fa18ba6
  - id: LTP_AC5312B5BF09186C
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:ac5312b5bf09186c854855a7ad3f97e96486a355a3f4df57d3e4422f6bb8b364
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: readv
  source_fingerprint: sha256:d275940f25879cdb27773d14825be221d555ee5ca87ac8819d3e645e957fcca6
  recognition_fingerprint: sha256:93ce9f61c10d2da7e3a1927c02a1bb8a37cef7d1964bb80d9bf555054a1a4573
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: realpath
  source_fingerprint: sha256:f6de77becb1f31963b6f3bfc959b02bac49cf498593d64cdb759531a4f66c76b
  recognition_fingerprint: sha256:d3d07ba8192e811d5f6a937a1c28531a18219823f37aaab861db485a2129963a
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_68EDEECFEA7F3C06
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:68edeecfea7f3c068d6a9caad14a0f6796ca59fd1b93364c94c20fa07352f431
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: reboot
  source_fingerprint: sha256:d7977b5f99e8b237ad7b460de208ea575606cbd4c9a96d7a8f731b2efb0eca7c
  recognition_fingerprint: sha256:abf4de404bd3e65feaeb1d9e3a3fb74c3793e73f23a7bb839533a705c02ff1e9
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 3
  reason: unresolved_evidence
- syscall: recv
  source_fingerprint: sha256:6ae8020e60033dfcf6219b1e6418415971ac8bd262b41867151267800b65e5ec
  recognition_fingerprint: sha256:eeb128132fd0e1b9e7ed6fbdc4f24376e78c7ee535d1271a70dcc71f51a16c75
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_66303F5A0EB2D470
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:66303f5a0eb2d470d51bda66db60bf2c17fb12d7ea289890b0ec5f4da51be91d
  - id: LTP_766411248B80C139
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:766411248b80c1392a1f3cfc05f91a3270232dc3c5dfa27efd46c2f916410ee9
  - id: LTP_7EB2D64ACBEF14A7
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:7eb2d64acbef14a7e894cd4f34ae9204d8315099dc3fe639eef510c34df76b76
  - id: LTP_B34188BD305465CA
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:b34188bd305465cacb8aaa777c9f7c2544f0f9c7ac398e375b741262499dcf5b
  - id: LTP_C7E8278CFEF81C98
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:c7e8278cfef81c9817f04be6403dad12326fe6ae73cfa2a4d1e2e8247933b036
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: recvfrom
  source_fingerprint: sha256:12694b3133d94558a996303d7069939dc4416344b0ecd7223d5d169708fc1b89
  recognition_fingerprint: sha256:586ad4e95cc5d2ab3847eaf144c2b3b5cd4533060379ea19809804e78f933915
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_2B9F3F4A853A14C6
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:2b9f3f4a853a14c6f700b3d5fffa9c1b375e23ccad426342a9e92863c660b52b
  - id: LTP_2FAD34B153D5914E
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:2fad34b153d5914e99d42ee2864d68b85fbad09bda04c53019ff67873b9c5727
  - id: LTP_8AC9E6F26C2E3CFE
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:8ac9e6f26c2e3cfe517a34483ea598752d7cef858cb71afe6736d859575ab328
  - id: LTP_A6B15E4F4EBDDB36
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:a6b15e4f4ebddb36563f2472e43d96810b28a928032be03ce425766918f14570
  - id: LTP_D8E4FF36A3FE1F41
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d8e4ff36a3fe1f417be1a7b3b55f6e12af138b0ca37264e12db4093c0e522f5b
  - id: LTP_DD647A49F00FCC45
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:dd647a49f00fcc45a01624b47e1115bccf3327282fb0226079f9fccf3cde24da
  - id: LTP_F101CC6D9DF71519
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:f101cc6d9df71519f9a4d6e43b0202aee2fbdb4d5b6c9cbf8e408c8d051176e6
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: recvmmsg
  source_fingerprint: sha256:80b00b21115f012f5714b1abaeda60217bfc64056073bc527e19cb0129af30e9
  recognition_fingerprint: sha256:c0cd6a80ab7e3c51837a9989dcde6236455e3b27e806796c8d29de0b86ffa438
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: recvmsg
  source_fingerprint: sha256:9218da2a3064baf0724cc254f07bbe68d58221345e03edb70c81e5e982cfd0ca
  recognition_fingerprint: sha256:833a254a1475b7bbf89a8334d0cbd83eae04c2c2dfd5768506515356d3edca80
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: remap_file_pages
  source_fingerprint: sha256:00cea002bf0c848dc8749c8dcc327586199d285e8c86f8f10266a4a2de69b97e
  recognition_fingerprint: sha256:eb980d592fba1e7384276dff92768668b1beda0133409224e2f11258ae44916e
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: removexattr
  source_fingerprint: sha256:6439af61185c2a7b16f3f2a65f24af01f943a55f832ec93d23ee916a62521451
  recognition_fingerprint: sha256:775568cd12f4aaf8c9f7344f61326aa0a890a1eed826191d7b5b551cebe2bbee
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: rename
  source_fingerprint: sha256:0a105956970132f4f9ae21a36b2581744782849b884d62e6c57b8421c45b45e3
  recognition_fingerprint: sha256:52ee156ae64aacfdbce042de6c1e0c703dfd3dd275ce98f613fb496ec76eedd9
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_1028A46194A35788
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:1028a46194a357881abb36577857770560405dcd2cd7e491c8754f6cc409591c
  - id: LTP_2A0C51A9F627F9EE
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:2a0c51a9f627f9ee7ac43f2bacd49a4c3bb1984810cce5d7e5abb2355ad87a6a
  - id: LTP_2E4BA3FA59A48F0F
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:2e4ba3fa59a48f0f0cea61bd78321a2e6ebd6268e549ba4156008daed72a9807
  - id: LTP_2EBC825D5CF7EF0F
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:2ebc825d5cf7ef0fa396ac1a3687c2bf53d8fd932147ca359fe5118dd5b4deb2
  - id: LTP_3EC51D87D4A4C0C2
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:3ec51d87d4a4c0c26a7eed1d9bbc05efea28f9acb70d8a73380f4817bda9206e
  - id: LTP_43BC8A0B853CD8DB
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:43bc8a0b853cd8db659ada2f1c8a70e989efa50f79951339920e1726191ed97c
  - id: LTP_54D221925C324829
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:54d221925c3248296c72ab5bab50eedc83600a21193fb45b57c50cd9847020f5
  - id: LTP_6821C2F644329FB4
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:6821c2f644329fb42db6ed6ee0ff53d1782c810e9b06f51ecb7664986596cf0d
  - id: LTP_9062D40054E147B9
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:9062d40054e147b96a9ce249f51d1e22a94bb1012e0c3d52a72373afec378ae6
  - id: LTP_90CF6ADF43644434
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:90cf6adf4364443443b50c2e471ace344cbf7fb691454f205e9067cd8ae953f0
  - id: LTP_9D13DF07435A4B33
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:9d13df07435a4b331ad7ad736b90d2360ed2a781ab30bb9d9b71b209df3dfe55
  - id: LTP_CA1E4549CF7692F9
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:ca1e4549cf7692f9b70c18cbdd4fda9142e71e6e53c36e657a6580b1aa45aac9
  - id: LTP_D17799C1BB191952
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d17799c1bb191952c8f2cc832abef239083c8d2cf1a28be3895cc743df184456
  - id: LTP_D758596147111328
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d758596147111328ebe3885b920bfc4e4bd8b4c1a41820ae47ef48cceb8d1f5d
  - id: LTP_D7936678BF685610
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d7936678bf685610bb9b7d85dbd99b3021702ffa47abcd925bb8bdd68493904f
  - id: LTP_D98D789F4EBA6817
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d98d789f4eba6817bf51c596411fe28898111d5abc5991f3446fb238394f2e11
  - id: LTP_E1B6C6D1C8603A83
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:e1b6c6d1c8603a83f0afb4734f012a8767e65607f1005299836d382097b0b282
  - id: LTP_FEDD56BEBCE11F81
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:fedd56bebce11f812b73821e227c66019f46df49947458e81965368e2b9def89
  evidence_count: 30
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
```
</details>
