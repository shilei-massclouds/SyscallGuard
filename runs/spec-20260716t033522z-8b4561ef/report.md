# Syscall 合规性规则提取报告

## 结论

本次分析了 fspick、fstat、fstatat、fstatfs、fsync、ftruncate、futex、futimesat、get_mempolicy、get_robust_list、getcontext、getcpu、getcwd、getdents64、getdomainname、getegid、geteuid、getgid、getgroups、gethostbyname_r、gethostid、gethostname、getitimer、getpagesize、getpeername、getpgid、getpgrp、getpid、getppid、getpriority、getrandom、getresgid、getresuid、getrlimit、getrusage、getsid、getsockname、getsockopt、gettid、gettimeofday、getuid、getxattr、init_module、inotify、inotify_init、io_cancel、io_destroy、io_getevents、io_pgetevents、io_setup、io_submit、io_uring、ioctl、ioperm、iopl、ioprio、ipc、kcmp、keyctl、kill、landlock、lgetxattr、link、linkat、listen、listmount、listxattr、llistxattr、llseek、lremovexattr、lseek、lsm、lstat、madvise、mallinfo、mallinfo2、mallopt、mbind、membarrier、memcmp，发现 167 条可执行的合规性规则。

## `fspick`

没有形成可发布的合规性规则。

## `fstat`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_466F01834F965621`](../../library/rules/ltp-466f01834f965621.yaml) | USER_BUFFER | 调用 fstat(fd_ebadf, &stat_buf) | 返回 -1，errno 为 EBADF |
| [`LTP_64B1B6EEEC3F79FC`](../../library/rules/ltp-64b1b6eeec3f79fc.yaml) | BAD_USER_ADDRESS | 调用 fstat(fd_ok, NULL) | 返回 -1，errno 为 EFAULT |
| [`LTP_A363671517C058B1`](../../library/rules/ltp-a363671517c058b1.yaml) | USER_BUFFER | 调用 fstat(fildes, &stat_buf) | 调用成功，返回 SUCCESS |
## `fstatat`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_90068DD4526FEFC0`](../../library/rules/ltp-90068dd4526fefc0.yaml) | 无额外前置条件 | 调用 fstatat(fds[i], filenames[i], &statbuf, flags[i]) | 返回 -1，errno 为 expected_errn |
## `fstatfs`

共形成 4 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_7C0112A92527C2A7`](../../library/rules/ltp-7c0112a92527c2a7.yaml) | USER_BUFFER | 调用 fstatfs(file_fd, &buf) | 调用成功，返回 SUCCESS |
| [`LTP_90B95E5DF2BD7509`](../../library/rules/ltp-90b95e5df2bd7509.yaml) | USER_BUFFER | 调用 fstatfs(pipe_fd, &buf) | 调用成功，返回 SUCCESS |
| [`LTP_EB1B734A0943248E`](../../library/rules/ltp-eb1b734a0943248e.yaml) | BAD_USER_ADDRESS | 调用 fstatfs(fd, (void *)-1) | 返回 -1，errno 为 EFAULT |
| [`LTP_F92A1A6292F40811`](../../library/rules/ltp-f92a1a6292f40811.yaml) | USER_BUFFER | 调用 fstatfs(bad_fd, &buf) | 返回 -1，errno 为 EBADF |
## `fsync`

没有形成可发布的合规性规则。

## `ftruncate`

共形成 8 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_02D0577172D97F4B`](../../library/rules/ltp-02d0577172d97f4b.yaml) | 无额外前置条件 | 调用 ftruncate(fd, TRUNC_LEN2) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_213EA37A2B59AB99`](../../library/rules/ltp-213ea37a2b59ab99.yaml) | 无额外前置条件 | 调用 ftruncate(fd, TRUNC_LEN1) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_2648B36BD9CF39EE`](../../library/rules/ltp-2648b36bd9cf39ee.yaml) | 文件描述符无效 | 调用 ftruncate(fd, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_46AA49209C30E739`](../../library/rules/ltp-46aa49209c30e739.yaml) | 无额外前置条件 | 调用 ftruncate(sock_fd, 4) | 返回 -1，errno 为 EINVAL |
| [`LTP_5E6E4D23F79BC9DA`](../../library/rules/ltp-5e6e4d23f79bc9da.yaml) | 无额外前置条件 | 调用 ftruncate(fd, offset) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_63E6527501A08F92`](../../library/rules/ltp-63e6527501a08f92.yaml) | 无额外前置条件 | 调用 ftruncate(read_fd, 4) | 返回 -1，errno 为 EINVAL |
| [`LTP_EB214534D857AE95`](../../library/rules/ltp-eb214534d857ae95.yaml) | 无额外前置条件 | 调用 ftruncate(bad_fd, 4) | 返回 -1，errno 为 EBADF |
| [`LTP_EC25ABB5C68F5299`](../../library/rules/ltp-ec25abb5c68f5299.yaml) | 无额外前置条件 | 调用 ftruncate(fd, offset) | 返回 0，errno 为 EAGAIN |
## `futex`

没有形成可发布的合规性规则。

## `futimesat`

没有形成可发布的合规性规则。

## `get_mempolicy`

没有形成可发布的合规性规则。

## `get_robust_list`

共形成 5 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_3F7F517D8AA3614C`](../../library/rules/ltp-3f7f517d8aa3614c.yaml) | 无额外前置条件 | 调用 get_robust_list(1, (struct robust_list_head *)&head, &len_ptr) | 返回 -1，errno 为 EPERM |
| [`LTP_5CC32725A40238D7`](../../library/rules/ltp-5cc32725a40238d7.yaml) | 无额外前置条件 | 调用 get_robust_list(0, (struct robust_list_head **)&head, &len_ptr) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_7F4B220485E99184`](../../library/rules/ltp-7f4b220485e99184.yaml) | BAD_USER_ADDRESS | 调用 get_robust_list(0, NULL, &len_ptr) | 返回 -1，errno 为 EFAULT |
| [`LTP_C46B746DAC4331D5`](../../library/rules/ltp-c46b746dac4331d5.yaml) | BAD_USER_ADDRESS | 调用 get_robust_list(0, (struct robust_list_head *)&head, NULL) | 返回 -1，errno 为 EFAULT |
| [`LTP_F3CE94166822B3E3`](../../library/rules/ltp-f3ce94166822b3e3.yaml) | 无额外前置条件 | 调用 get_robust_list(unused_pid, (struct robust_list_head *)&head, &len_ptr) | 返回 -1，errno 为 ESRCH |
## `getcontext`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_70E5CA8341B80E83`](../../library/rules/ltp-70e5ca8341b80e83.yaml) | 无额外前置条件 | 调用 getcontext(&ptr) | 调用成功，返回 SUCCESS |
## `getcpu`

没有形成可发布的合规性规则。

## `getcwd`

共形成 5 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_53E3454ED6EFD842`](../../library/rules/ltp-53e3454ed6efd842.yaml) | 无额外前置条件 | 调用 getcwd(buffer, 1) | 返回 -1，errno 为 ERANGE |
| [`LTP_729222947741DFD6`](../../library/rules/ltp-729222947741dfd6.yaml) | 无额外前置条件 | 调用 getcwd(buffer, 0) | 返回 -1，errno 为 ERANGE |
| [`LTP_89BB56D579EEF06D`](../../library/rules/ltp-89bb56d579eef06d.yaml) | BAD_USER_ADDRESS | 调用 getcwd(NULL, (size_t)-1) | 返回 -1，errno 为 EFAULT |
| [`LTP_912BE233FAFE6762`](../../library/rules/ltp-912be233fafe6762.yaml) | BAD_USER_ADDRESS | 调用 getcwd((void *)-1, PATH_MAX) | 返回 -1，errno 为 EFAULT |
| [`LTP_FC1E41C3414E7F21`](../../library/rules/ltp-fc1e41c3414e7f21.yaml) | 无额外前置条件 | 调用 getcwd(NULL, 1) | 返回 -1，errno 为 ERANGE |
## `getdents64`

共形成 5 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_39008564F17DCBDD`](../../library/rules/ltp-39008564f17dcbdd.yaml) | USER_BUFFER | 调用 getdents64(fd_inv, dirp, size) | 返回 -1，errno 为 EBADF |
| [`LTP_409C97094F0CED1F`](../../library/rules/ltp-409c97094f0ced1f.yaml) | NONEXISTENT_PATH、USER_BUFFER | 调用 getdents64(fd_unlinked, dirp, size) | 返回 -1，errno 为 ENOENT |
| [`LTP_44B41305EB538966`](../../library/rules/ltp-44b41305eb538966.yaml) | NON_DIRECTORY_PATH_COMPONENT、USER_BUFFER | 调用 getdents64(fd_file, dirp, size) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_8CA8B0BC6ED845C4`](../../library/rules/ltp-8ca8b0bc6ed845c4.yaml) | USER_BUFFER | 调用 getdents64(fd, dirp1, size1) | 返回 -1，errno 为 EINVAL |
| [`LTP_FF639650AE6F7097`](../../library/rules/ltp-ff639650ae6f7097.yaml) | BAD_USER_ADDRESS、USER_BUFFER | 调用 getdents64(fd, dirp_bad, size) | 返回 -1，errno 为 EFAULT |
## `getdomainname`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_3C4C8CA4ED44FE57`](../../library/rules/ltp-3c4c8ca4ed44fe57.yaml) | 无额外前置条件 | 调用 getdomainname(domain_name, sizeof(domain_name)) | 调用成功，返回 SUCCESS |
## `getegid`

没有形成可发布的合规性规则。

## `geteuid`

没有形成可发布的合规性规则。

## `getgid`

没有形成可发布的合规性规则。

## `getgroups`

没有形成可发布的合规性规则。

## `gethostbyname_r`

没有形成可发布的合规性规则。

## `gethostid`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_7B9FBEA6E7CF8A70`](../../library/rules/ltp-7b9fbea6e7cf8a70.yaml) | 无额外前置条件 | 调用 gethostid() | {'kind': 'return_value', 'return': '-1'} |
## `gethostname`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_92006BB83B7F5B92`](../../library/rules/ltp-92006bb83b7f5b92.yaml) | PATH_TOO_LONG | 调用 gethostname(hostname, real_length - 1) | 返回 -1，errno 为 ENAMETOOLONG |
| [`LTP_C09E83BE36885312`](../../library/rules/ltp-c09e83be36885312.yaml) | 无额外前置条件 | 调用 gethostname(hname, sizeof(hname)) | 调用成功，返回 SUCCESS |
## `getitimer`

没有形成可发布的合规性规则。

## `getpagesize`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_90893935E64240AA`](../../library/rules/ltp-90893935e64240aa.yaml) | 无额外前置条件 | 调用 getpagesize() | {'kind': 'return_value', 'return': 'pagesize_sysconf'} |
## `getpeername`

没有形成可发布的合规性规则。

## `getpgid`

共形成 6 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_352394AAA6D49339`](../../library/rules/ltp-352394aaa6d49339.yaml) | 无额外前置条件 | 调用 getpgid(child_pid) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_8C1C2578972FCA1D`](../../library/rules/ltp-8c1c2578972fca1d.yaml) | 无额外前置条件 | 调用 getpgid(neg_pid) | 返回 -1，errno 为 ESRCH |
| [`LTP_9461AA782926BAB4`](../../library/rules/ltp-9461aa782926bab4.yaml) | 无额外前置条件 | 调用 getpgid(unused_pid) | 返回 -1，errno 为 ESRCH |
| [`LTP_DA8094714BA3F734`](../../library/rules/ltp-da8094714ba3f734.yaml) | 无额外前置条件 | 调用 getpgid(pgid) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_F5D2C7B7F0E3D07C`](../../library/rules/ltp-f5d2c7b7f0e3d07c.yaml) | 无额外前置条件 | 调用 getpgid(1) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_F9357233C6D73800`](../../library/rules/ltp-f9357233c6d73800.yaml) | 无额外前置条件 | 调用 getpgid(0) | {'kind': 'positive_return', 'return': '>0'} |
## `getpgrp`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_A82CC878A661AA28`](../../library/rules/ltp-a82cc878a661aa28.yaml) | 无额外前置条件 | 调用 getpgrp() | {'kind': 'positive_return', 'return': '>0'} |
## `getpid`

没有形成可发布的合规性规则。

## `getppid`

没有形成可发布的合规性规则。

## `getpriority`

共形成 7 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0F02943A8FDA4830`](../../library/rules/ltp-0f02943a8fda4830.yaml) | 无额外前置条件 | 调用 getpriority(PRIO_USER, 0) | 返回 -1，errno 为 0 |
| [`LTP_57C7DC5E29B5ADF8`](../../library/rules/ltp-57c7dc5e29b5adf8.yaml) | 无额外前置条件 | 调用 getpriority(PRIO_PROCESS, 0) | 返回 -1，errno 为 0 |
| [`LTP_6DF55FF20A44572D`](../../library/rules/ltp-6df55ff20a44572d.yaml) | 无额外前置条件 | 调用 getpriority(PRIO_PGRP, INVAL_ID) | 返回 -1，errno 为 ESRCH |
| [`LTP_88D300A8FB407324`](../../library/rules/ltp-88d300a8fb407324.yaml) | 无额外前置条件 | 调用 getpriority(INVAL_FLAG, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_99C45ECA20496C98`](../../library/rules/ltp-99c45eca20496c98.yaml) | 无额外前置条件 | 调用 getpriority(PRIO_PROCESS, INVAL_ID) | 返回 -1，errno 为 ESRCH |
| [`LTP_9B0BA3ADF46F5FF4`](../../library/rules/ltp-9b0ba3adf46f5ff4.yaml) | 无额外前置条件 | 调用 getpriority(PRIO_USER, INVAL_ID) | 返回 -1，errno 为 ESRCH |
| [`LTP_D5DAD3494DBAE67F`](../../library/rules/ltp-d5dad3494dbae67f.yaml) | 无额外前置条件 | 调用 getpriority(PRIO_PGRP, 0) | 返回 -1，errno 为 0 |
## `getrandom`

没有形成可发布的合规性规则。

## `getresgid`

没有形成可发布的合规性规则。

## `getresuid`

没有形成可发布的合规性规则。

## `getrlimit`

共形成 18 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_2554AC2E46FC6A15`](../../library/rules/ltp-2554ac2e46fc6a15.yaml) | 无额外前置条件 | 调用 getrlimit(RES(RLIMIT_NOFILE), &rlim) | 调用成功，返回 SUCCESS |
| [`LTP_26555A26680524AD`](../../library/rules/ltp-26555a26680524ad.yaml) | 无额外前置条件 | 调用 getrlimit(RES(RLIMIT_CORE), &rlim) | 调用成功，返回 SUCCESS |
| [`LTP_3741A721C9C463D0`](../../library/rules/ltp-3741a721c9c463d0.yaml) | 无额外前置条件 | 调用 getrlimit(RES(RLIMIT_AS), &rlim) | 调用成功，返回 SUCCESS |
| [`LTP_3B1458E6E26CBB53`](../../library/rules/ltp-3b1458e6e26cbb53.yaml) | 无额外前置条件 | 调用 getrlimit(RES(RLIMIT_STACK), &rlim) | 调用成功，返回 SUCCESS |
| [`LTP_652CE911B47794E0`](../../library/rules/ltp-652ce911b47794e0.yaml) | 无额外前置条件 | 调用 getrlimit(RES(RLIMIT_MSGQUEUE), &rlim) | 调用成功，返回 SUCCESS |
| [`LTP_7DFAC48A8971CFE3`](../../library/rules/ltp-7dfac48a8971cfe3.yaml) | 无额外前置条件 | 调用 getrlimit(RES(RLIMIT_RTPRIO), &rlim) | 调用成功，返回 SUCCESS |
| [`LTP_8988E5015778894A`](../../library/rules/ltp-8988e5015778894a.yaml) | 无额外前置条件 | 调用 getrlimit(RES(RLIMIT_RTTIME), &rlim) | 调用成功，返回 SUCCESS |
| [`LTP_914935DA5C379DA1`](../../library/rules/ltp-914935da5c379da1.yaml) | 无额外前置条件 | 调用 getrlimit(RES(RLIMIT_CPU), &rlim) | 调用成功，返回 SUCCESS |
| [`LTP_91ED7E85761CE00F`](../../library/rules/ltp-91ed7e85761ce00f.yaml) | 无额外前置条件 | 调用 getrlimit(RES(RLIMIT_LOCKS), &rlim) | 调用成功，返回 SUCCESS |
| [`LTP_9305FA6D8B835652`](../../library/rules/ltp-9305fa6d8b835652.yaml) | 无额外前置条件 | 调用 getrlimit(RES(RLIMIT_FSIZE), &rlim) | 调用成功，返回 SUCCESS |
| [`LTP_963957F80E751EE6`](../../library/rules/ltp-963957f80e751ee6.yaml) | BAD_USER_ADDRESS | 调用 getrlimit(RLIMIT_CORE, (void *)-1) | 返回 -1，errno 为 EFAULT |
| [`LTP_A0547B601C515355`](../../library/rules/ltp-a0547b601c515355.yaml) | 无额外前置条件 | 调用 getrlimit(RES(RLIMIT_SIGPENDING), &rlim) | 调用成功，返回 SUCCESS |
| [`LTP_B058D6B9CBBB459D`](../../library/rules/ltp-b058d6b9cbbb459d.yaml) | 无额外前置条件 | 调用 getrlimit(INVALID_RES_TYPE, &rlim) | 返回 -1，errno 为 EINVAL |
| [`LTP_BD5C209F4C6EE910`](../../library/rules/ltp-bd5c209f4c6ee910.yaml) | 无额外前置条件 | 调用 getrlimit(RES(RLIMIT_MEMLOCK), &rlim) | 调用成功，返回 SUCCESS |
| [`LTP_E6C69C9F4AB565BC`](../../library/rules/ltp-e6c69c9f4ab565bc.yaml) | 无额外前置条件 | 调用 getrlimit(RES(RLIMIT_NICE), &rlim) | 调用成功，返回 SUCCESS |
| [`LTP_EA953D5E5C4B2B1F`](../../library/rules/ltp-ea953d5e5c4b2b1f.yaml) | 无额外前置条件 | 调用 getrlimit(RES(RLIMIT_NPROC), &rlim) | 调用成功，返回 SUCCESS |
| [`LTP_FADBA4ADECCFBA4E`](../../library/rules/ltp-fadba4adeccfba4e.yaml) | 无额外前置条件 | 调用 getrlimit(RES(RLIMIT_DATA), &rlim) | 调用成功，返回 SUCCESS |
| [`LTP_FB0ABF26A21EAE3C`](../../library/rules/ltp-fb0abf26a21eae3c.yaml) | 无额外前置条件 | 调用 getrlimit(RES(RLIMIT_RSS), &rlim) | 调用成功，返回 SUCCESS |
## `getrusage`

没有形成可发布的合规性规则。

## `getsid`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_E3BA4E4FAEF39F91`](../../library/rules/ltp-e3ba4e4faef39f91.yaml) | 无额外前置条件 | 调用 getsid(0) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_F8FD511858BB650D`](../../library/rules/ltp-f8fd511858bb650d.yaml) | 无额外前置条件 | 调用 getsid(unused_pid) | 返回 -1，errno 为 ESRCH |
## `getsockname`

共形成 6 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_52CE7E6F9B5FF947`](../../library/rules/ltp-52ce7e6f9b5ff947.yaml) | 无额外前置条件 | 调用 getsockname(sock_null, (struct sockaddr *) &fsin1, &sinlen) | 返回 -1，errno 为 ENOTSOCK |
| [`LTP_5920F12CFE459CB8`](../../library/rules/ltp-5920f12cfe459cb8.yaml) | BAD_USER_ADDRESS | 调用 getsockname(sock_bind, (struct sockaddr *) NULL, &sinlen) | 返回 -1，errno 为 EFAULT |
| [`LTP_62FDC6AAFC4F4DE5`](../../library/rules/ltp-62fdc6aafc4f4de5.yaml) | BAD_USER_ADDRESS | 调用 getsockname(sock_bind, (struct sockaddr *) &fsin1, (socklen_t *) 1) | 返回 -1，errno 为 EFAULT |
| [`LTP_AA9171FB32FD0C67`](../../library/rules/ltp-aa9171fb32fd0c67.yaml) | 无额外前置条件 | 调用 getsockname(sock_fake, (struct sockaddr *) &fsin1, &sinlen) | 返回 -1，errno 为 EBADF |
| [`LTP_B25461243478CEF8`](../../library/rules/ltp-b25461243478cef8.yaml) | BAD_USER_ADDRESS | 调用 getsockname(sock_bind, (struct sockaddr *) &fsin1, NULL) | 返回 -1，errno 为 EFAULT |
| [`LTP_DBFBE6A110B3D17B`](../../library/rules/ltp-dbfbe6a110b3d17b.yaml) | 无额外前置条件 | 调用 getsockname(sock_bind, (struct sockaddr *) &fsin1, &sininval) | 返回 -1，errno 为 EINVAL |
## `getsockopt`

共形成 9 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0B982157D25C1D06`](../../library/rules/ltp-0b982157d25c1d06.yaml) | 文件描述符无效 | 调用 getsockopt(sock_bind, IPPROTO_TCP, -1, &optval, &optlen) | 返回 -1，errno 为 ENOPROTOOPT |
| [`LTP_0EEA999DE0FFD37D`](../../library/rules/ltp-0eea999de0ffd37d.yaml) | BAD_USER_ADDRESS | 调用 getsockopt(sock_bind, SOL_SOCKET, SO_OOBINLINE, &optval, 0) | 返回 -1，errno 为 EFAULT |
| [`LTP_3DDCD08519809A17`](../../library/rules/ltp-3ddcd08519809a17.yaml) | 无额外前置条件 | 调用 getsockopt(sock_bind, IPPROTO_UDP, SO_OOBINLINE, &optval, &optlen) | 返回 -1，errno 为 EOPNOTSUPP |
| [`LTP_809809859ABFE5C1`](../../library/rules/ltp-809809859abfe5c1.yaml) | BAD_USER_ADDRESS | 调用 getsockopt(sock_bind, SOL_SOCKET, SO_OOBINLINE, 0, &optlen) | 返回 -1，errno 为 EFAULT |
| [`LTP_8BCA62F97A197BC2`](../../library/rules/ltp-8bca62f97a197bc2.yaml) | 无额外前置条件 | 调用 getsockopt(sock_bind, 500, SO_OOBINLINE, &optval, &optlen) | 返回 -1，errno 为 EOPNOTSUPP |
| [`LTP_B72405976D9F15E6`](../../library/rules/ltp-b72405976d9f15e6.yaml) | 无额外前置条件 | 调用 getsockopt(sock_fake, SOL_SOCKET, SO_OOBINLINE, &optval, &optlen) | 返回 -1，errno 为 EBADF |
| [`LTP_D77AD0D4DC9C0C9E`](../../library/rules/ltp-d77ad0d4dc9c0c9e.yaml) | 无额外前置条件 | 调用 getsockopt(sock_null, SOL_SOCKET, SO_OOBINLINE, &optval, &optlen) | 返回 -1，errno 为 ENOTSOCK |
| [`LTP_DC1ACD3B300AFCC3`](../../library/rules/ltp-dc1acd3b300afcc3.yaml) | 文件描述符无效 | 调用 getsockopt(sock_bind, IPPROTO_IP, -1, &optval, &optlen) | 返回 -1，errno 为 ENOPROTOOPT |
| [`LTP_FE51D85F4A425C61`](../../library/rules/ltp-fe51d85f4a425c61.yaml) | 无额外前置条件 | 调用 getsockopt(sock_bind, SOL_SOCKET, SO_OOBINLINE, &optval, &optleninval) | 返回 -1，errno 为 EINVAL |
## `gettid`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_BD3B3CC9032DF4E5`](../../library/rules/ltp-bd3b3cc9032df4e5.yaml) | 无额外前置条件 | 调用 gettid() | {'kind': 'return_value', 'return': 'pid'} |
| [`LTP_E083F071E292B561`](../../library/rules/ltp-e083f071e292b561.yaml) | 无额外前置条件 | 调用 gettid() | {'kind': 'return_value', 'return': 'tst_syscall(__NR_getpid)'} |
## `gettimeofday`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_5B4AA4EE494B37D2`](../../library/rules/ltp-5b4aa4ee494b37d2.yaml) | BAD_USER_ADDRESS | 调用 gettimeofday((void *)-1, NULL) | 返回 -1，errno 为 EFAULT |
| [`LTP_6C14DE68E3C0CC24`](../../library/rules/ltp-6c14de68e3c0cc24.yaml) | BAD_USER_ADDRESS | 调用 gettimeofday(&tv1, (void *)-1) | 返回 -1，errno 为 EFAULT |
| [`LTP_FCF5A4835CFCD143`](../../library/rules/ltp-fcf5a4835cfcd143.yaml) | BAD_USER_ADDRESS | 调用 gettimeofday((void *)-1, (void *)-1) | 返回 -1，errno 为 EFAULT |
## `getuid`

没有形成可发布的合规性规则。

## `getxattr`

没有形成可发布的合规性规则。

## `init_module`

共形成 10 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0080969B4E1A8F96`](../../library/rules/ltp-0080969b4e1a8f96.yaml) | USER_BUFFER | 调用 init_module(buf, zero_size, "") | 返回 -1，errno 为 ENOEXEC |
| [`LTP_0D3B043506A61BD6`](../../library/rules/ltp-0d3b043506a61bd6.yaml) | USER_BUFFER | 调用 init_module(buf, sb.st_size, "status=valid") | 调用成功，返回 SUCCESS |
| [`LTP_1D3F4A6BCBF6BBE5`](../../library/rules/ltp-1d3f4a6bcbf6bbe5.yaml) | USER_BUFFER | 调用 init_module(buf, size, "") | 返回 -1，errno 为 EKEYREJECTED |
| [`LTP_453DFC908EB0DD9E`](../../library/rules/ltp-453dfc908eb0dd9e.yaml) | BAD_USER_ADDRESS | 调用 init_module(faulty_buf, size, "") | 返回 -1，errno 为 EFAULT |
| [`LTP_77C73AE1FE592877`](../../library/rules/ltp-77c73ae1fe592877.yaml) | USER_BUFFER | 调用 init_module(buf, sb.st_size, "status=valid") | 返回 -1，errno 为 EKEYREJECTED |
| [`LTP_80AFFD1BF1D04F38`](../../library/rules/ltp-80affd1bf1d04f38.yaml) | OBJECT_ALREADY_EXISTS、USER_BUFFER | 调用 init_module(buf, size, "") | 返回 -1，errno 为 EEXIST |
| [`LTP_930417433305D40F`](../../library/rules/ltp-930417433305d40f.yaml) | BAD_USER_ADDRESS、USER_BUFFER | 调用 init_module(buf, size, NULL) | 返回 -1，errno 为 EFAULT |
| [`LTP_AD9C93AEB21E0E7B`](../../library/rules/ltp-ad9c93aeb21e0e7b.yaml) | USER_BUFFER | 调用 init_module(buf, size, "status=invalid") | 返回 -1，errno 为 EINVAL |
| [`LTP_D246498B20D9CB2C`](../../library/rules/ltp-d246498b20d9cb2c.yaml) | USER_BUFFER | 调用 init_module(buf, size, "") | 返回 -1，errno 为 EPERM |
| [`LTP_D58C26D260BBCED5`](../../library/rules/ltp-d58c26d260bbced5.yaml) | BAD_USER_ADDRESS | 调用 init_module(null_buf, size, "") | 返回 -1，errno 为 EFAULT |
## `inotify`

没有形成可发布的合规性规则。

## `inotify_init`

没有形成可发布的合规性规则。

## `io_cancel`

没有形成可发布的合规性规则。

## `io_destroy`

没有形成可发布的合规性规则。

## `io_getevents`

没有形成可发布的合规性规则。

## `io_pgetevents`

没有形成可发布的合规性规则。

## `io_setup`

没有形成可发布的合规性规则。

## `io_submit`

没有形成可发布的合规性规则。

## `io_uring`

没有形成可发布的合规性规则。

## `ioctl`

没有形成可发布的合规性规则。

## `ioperm`

没有形成可发布的合规性规则。

## `iopl`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_1264D075DA68BB98`](../../library/rules/ltp-1264d075da68bb98.yaml) | 无额外前置条件 | 调用 iopl(4) | 返回 -1，errno 为 EINVAL |
| [`LTP_7A6820B73D1C2059`](../../library/rules/ltp-7a6820b73d1c2059.yaml) | 无额外前置条件 | 调用 iopl(1) | 返回 -1，errno 为 EPERM |
| [`LTP_FBEB6959ED2912C8`](../../library/rules/ltp-fbeb6959ed2912c8.yaml) | 无额外前置条件 | 调用 iopl(level) | {'kind': 'return_value', 'return': '-1'} |
## `ioprio`

没有形成可发布的合规性规则。

## `ipc`

没有形成可发布的合规性规则。

## `kcmp`

没有形成可发布的合规性规则。

## `keyctl`

没有形成可发布的合规性规则。

## `kill`

共形成 7 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_52FC519F20674559`](../../library/rules/ltp-52fc519f20674559.yaml) | 无额外前置条件 | 调用 kill(-getpgrp(), SIGKILL) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_6D195DDAB1BE2B57`](../../library/rules/ltp-6d195ddab1be2b57.yaml) | 无额外前置条件 | 调用 kill(0, SIGUSR1) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_A2E3A27D541DED02`](../../library/rules/ltp-a2e3a27d541ded02.yaml) | 无额外前置条件 | 调用 kill(int_min_pid, SIGKILL) | 返回 -1，errno 为 ESRCH |
| [`LTP_C93391BCF53E8020`](../../library/rules/ltp-c93391bcf53e8020.yaml) | 无额外前置条件 | 调用 kill(INT_MIN, 0) | 返回 -1，errno 为 ESRCH |
| [`LTP_E8E97EBE8E041CF0`](../../library/rules/ltp-e8e97ebe8e041cf0.yaml) | 无额外前置条件 | 调用 kill(pid1, SIGKILL) | 返回 0，errno 为 EPERM |
| [`LTP_F13024AE4BC5C024`](../../library/rules/ltp-f13024ae4bc5c024.yaml) | 无额外前置条件 | 调用 kill(real_pid, 2000) | 返回 -1，errno 为 EINVAL |
| [`LTP_F99DE159B75F22A2`](../../library/rules/ltp-f99de159b75f22a2.yaml) | 无额外前置条件 | 调用 kill(fake_pid, SIGKILL) | 返回 -1，errno 为 ESRCH |
## `landlock`

没有形成可发布的合规性规则。

## `lgetxattr`

共形成 5 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_74DD0DCF0CE8388F`](../../library/rules/ltp-74dd0dcf0ce8388f.yaml) | BAD_USER_ADDRESS、USER_BUFFER | 调用 lgetxattr((char *)-1, SECURITY_KEY, buf, sizeof(buf)) | 返回 -1，errno 为 EFAULT |
| [`LTP_8710A0CE4DCC217D`](../../library/rules/ltp-8710a0ce4dcc217d.yaml) | USER_BUFFER | 调用 lgetxattr("symlink", SECURITY_KEY2, buf, size) | {'kind': 'return_value', 'return': 'strlen(VALUE2'} |
| [`LTP_9586C4C3CAC60BBC`](../../library/rules/ltp-9586c4c3cac60bbc.yaml) | USER_BUFFER | 调用 lgetxattr("symlink", SECURITY_KEY, buf, sizeof(buf)) | 返回 -1，errno 为 ERANGE |
| [`LTP_B84B9DEC792BCB34`](../../library/rules/ltp-b84b9dec792bcb34.yaml) | USER_BUFFER | 调用 lgetxattr("testfile", SECURITY_KEY, buf, sizeof(buf)) | 返回 -1，errno 为 ENODATA |
| [`LTP_F66773BC44256D99`](../../library/rules/ltp-f66773bc44256d99.yaml) | USER_BUFFER | 调用 lgetxattr("symlink", SECURITY_KEY1, buf, size) | 返回 -1，errno 为 ENODATA |
## `link`

没有形成可发布的合规性规则。

## `linkat`

没有形成可发布的合规性规则。

## `listen`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_3707B18864CF6352`](../../library/rules/ltp-3707b18864cf6352.yaml) | 无额外前置条件 | 调用 listen(s, 0) | 返回 -1，errno 为 EOPNOTSUPP |
| [`LTP_A1D08F4E94B7899A`](../../library/rules/ltp-a1d08f4e94b7899a.yaml) | 无额外前置条件 | 调用 listen(s, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_ABB01FA7743F966A`](../../library/rules/ltp-abb01fa7743f966a.yaml) | 无额外前置条件 | 调用 listen(s, 0) | 返回 -1，errno 为 ENOTSOCK |
## `listmount`

没有形成可发布的合规性规则。

## `listxattr`

共形成 6 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_1F8223E4EE64B649`](../../library/rules/ltp-1f8223e4ee64b649.yaml) | NONEXISTENT_PATH、USER_BUFFER | 调用 listxattr("", buf, sizeof(buf)) | 返回 -1，errno 为 ENOENT |
| [`LTP_31E977FBCF448AFD`](../../library/rules/ltp-31e977fbcf448afd.yaml) | PATH_TOO_LONG、USER_BUFFER | 调用 listxattr(longpathname, buf, sizeof(buf)) | 返回 -1，errno 为 ENAMETOOLONG |
| [`LTP_3CA39247E6E3D055`](../../library/rules/ltp-3ca39247e6e3d055.yaml) | BAD_USER_ADDRESS、USER_BUFFER | 调用 listxattr((char *)-1, buf, sizeof(buf)) | 返回 -1，errno 为 EFAULT |
| [`LTP_8D6B83A8176DB57E`](../../library/rules/ltp-8d6b83a8176db57e.yaml) | USER_BUFFER | 调用 listxattr(TESTFILE, buf, sizeof(buf)) | 返回 -1，errno 为 ERANGE |
| [`LTP_8F9E255B19623C24`](../../library/rules/ltp-8f9e255b19623c24.yaml) | USER_BUFFER | 调用 listxattr(TESTFILE, buf, sizeof(buf)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_969660F14B0B297A`](../../library/rules/ltp-969660f14b0b297a.yaml) | 无额外前置条件 | 调用 listxattr(name, NULL, 0) | {'kind': 'return_value', 'return': '-1'} |
## `llistxattr`

共形成 6 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_196A6B5A609ADC9A`](../../library/rules/ltp-196a6b5a609adc9a.yaml) | PATH_TOO_LONG、USER_BUFFER | 调用 llistxattr(longpathname, buf, sizeof(buf)) | 返回 -1，errno 为 ENAMETOOLONG |
| [`LTP_1B2E614CA8847B31`](../../library/rules/ltp-1b2e614ca8847b31.yaml) | 无额外前置条件 | 调用 llistxattr(name, NULL, 0) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_67180EB1CFAAB816`](../../library/rules/ltp-67180eb1cfaab816.yaml) | USER_BUFFER | 调用 llistxattr(SYMLINK, buf, sizeof(buf)) | 返回 -1，errno 为 ERANGE |
| [`LTP_C9789067DD7A3D60`](../../library/rules/ltp-c9789067dd7a3d60.yaml) | USER_BUFFER | 调用 llistxattr(SYMLINK, buf, sizeof(buf)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_C9D2C2E3FC2B9581`](../../library/rules/ltp-c9d2c2e3fc2b9581.yaml) | BAD_USER_ADDRESS、USER_BUFFER | 调用 llistxattr((char *)-1, buf, sizeof(buf)) | 返回 -1，errno 为 EFAULT |
| [`LTP_D4159BF3AB78E108`](../../library/rules/ltp-d4159bf3ab78e108.yaml) | NONEXISTENT_PATH、USER_BUFFER | 调用 llistxattr("", buf, sizeof(buf)) | 返回 -1，errno 为 ENOENT |
## `llseek`

没有形成可发布的合规性规则。

## `lremovexattr`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_7786636C200E9E5C`](../../library/rules/ltp-7786636c200e9e5c.yaml) | 无额外前置条件 | 调用 lremovexattr(SYMLINK, XATTR_KEY) | {'kind': 'return_value', 'return': '0'} |
## `lseek`

没有形成可发布的合规性规则。

## `lsm`

没有形成可发布的合规性规则。

## `lstat`

共形成 7 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_32D132100CDC04ED`](../../library/rules/ltp-32d132100cdc04ed.yaml) | NON_DIRECTORY_PATH_COMPONENT、USER_BUFFER | 调用 lstat(TEST_ENOTDIR, &stat_buf) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_4929F8BCC4B9811B`](../../library/rules/ltp-4929f8bcc4b9811b.yaml) | BAD_USER_ADDRESS、USER_BUFFER | 调用 lstat(NULL, &stat_buf) | 返回 -1，errno 为 EFAULT |
| [`LTP_9FB758C1B4AF2411`](../../library/rules/ltp-9fb758c1b4af2411.yaml) | PATH_TOO_LONG、USER_BUFFER | 调用 lstat(longpathname, &stat_buf) | 返回 -1，errno 为 ENAMETOOLONG |
| [`LTP_C3433C582C87D21B`](../../library/rules/ltp-c3433c582c87d21b.yaml) | PERMISSION_DENIED_STATE、USER_BUFFER | 调用 lstat(TEST_EACCES, &stat_buf) | 返回 -1，errno 为 EACCES |
| [`LTP_CA3E9D83D71EEED4`](../../library/rules/ltp-ca3e9d83d71eeed4.yaml) | SYMLINK_LOOP、USER_BUFFER | 调用 lstat(elooppathname, &stat_buf) | 返回 -1，errno 为 ELOOP |
| [`LTP_CBB45E0BB83FDEB0`](../../library/rules/ltp-cbb45e0bb83fdeb0.yaml) | NONEXISTENT_PATH、USER_BUFFER | 调用 lstat(TEST_ENOENT, &stat_buf) | 返回 -1，errno 为 ENOENT |
| [`LTP_DACAAECF088B0CFE`](../../library/rules/ltp-dacaaecf088b0cfe.yaml) | USER_BUFFER | 调用 lstat(TESTSYML, &stat_buf) | {'kind': 'return_value', 'return': '-1'} |
## `madvise`

共形成 28 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_004E24807F6067A5`](../../library/rules/ltp-004e24807f6067a5.yaml) | 无额外前置条件 | 调用 madvise(sfile, st.st_size, MADV_DOFORK) | 返回 -1，errno 为 EINVAL |
| [`LTP_0E51A1345D29A74B`](../../library/rules/ltp-0e51a1345d29a74b.yaml) | 无额外前置条件 | 调用 madvise(amem, st.st_size, MADV_WIPEONFORK) | 返回 -1，errno 为 EINVAL |
| [`LTP_1A68979B981D8947`](../../library/rules/ltp-1a68979b981d8947.yaml) | 无额外前置条件 | 调用 madvise(target, pg_sz * 3, MADV_WILLNEED) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_1B3AD244C58835E7`](../../library/rules/ltp-1b3ad244c58835e7.yaml) | 无额外前置条件 | 调用 madvise(*(tc->addr), st.st_size, tc->advice) | 返回 -1，errno 为 tc->exp_errno |
| [`LTP_1D6E9D5C4E09D7F5`](../../library/rules/ltp-1d6e9d5c4e09d7f5.yaml) | 无额外前置条件 | 调用 madvise(sfile, st.st_size, MADV_NORMAL) | 返回 -1，errno 为 EINVAL |
| [`LTP_2A3276D2B0A31AC9`](../../library/rules/ltp-2a3276d2b0a31ac9.yaml) | 无额外前置条件 | 调用 madvise(sfile, st.st_size, MADV_SEQUENTIAL) | 返回 -1，errno 为 EINVAL |
| [`LTP_36E1AD5A78C2A50D`](../../library/rules/ltp-36e1ad5a78c2a50d.yaml) | 无额外前置条件 | 调用 madvise(sfile, st.st_size, MADV_DONTDUMP) | 返回 -1，errno 为 EINVAL |
| [`LTP_380714557B4AE9D4`](../../library/rules/ltp-380714557b4ae9d4.yaml) | 无额外前置条件 | 调用 madvise(sfile, st.st_size, MADV_RANDOM) | 返回 -1，errno 为 EINVAL |
| [`LTP_505DF8E6B5595F9E`](../../library/rules/ltp-505df8e6b5595f9e.yaml) | 无额外前置条件 | 调用 madvise(sfile, st.st_size, MADV_WILLNEED) | 返回 -1，errno 为 EINVAL |
| [`LTP_54CE18AAE5BDB693`](../../library/rules/ltp-54ce18aae5bdb693.yaml) | 无额外前置条件 | 调用 madvise(addr, MAP_SIZE, MADV_GUARD_REMOVE) | 调用成功，返回 SUCCESS |
| [`LTP_5A7E16725228EB1E`](../../library/rules/ltp-5a7e16725228eb1e.yaml) | 无额外前置条件 | 调用 madvise(sfile, st.st_size, MADV_DONTNEED) | 返回 -1，errno 为 EINVAL |
| [`LTP_5E1690FA7F57F981`](../../library/rules/ltp-5e1690fa7f57f981.yaml) | 无额外前置条件 | 调用 madvise(sfile, st.st_size, MADV_REMOVE) | 返回 -1，errno 为 EINVAL |
| [`LTP_64668181C4066A0A`](../../library/rules/ltp-64668181c4066a0a.yaml) | 无额外前置条件 | 调用 madvise(amem, st.st_size, MADV_NOHUGEPAGE) | 返回 -1，errno 为 EINVAL |
| [`LTP_6882C814E58F3D3B`](../../library/rules/ltp-6882c814e58f3d3b.yaml) | 无额外前置条件 | 调用 madvise(addr, MAP_SIZE, MADV_DONTNEED) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_6A52E2C16AC64CEC`](../../library/rules/ltp-6a52e2c16ac64cec.yaml) | 无额外前置条件 | 调用 madvise(sfile, st.st_size, MADV_HWPOISON) | 返回 -1，errno 为 EINVAL |
| [`LTP_753BDF43E7947404`](../../library/rules/ltp-753bdf43e7947404.yaml) | 无额外前置条件 | 调用 madvise(sfile, st.st_size, MADV_DODUMP) | 返回 -1，errno 为 EINVAL |
| [`LTP_8703114C595382AB`](../../library/rules/ltp-8703114c595382ab.yaml) | 无额外前置条件 | 调用 madvise(p, ALLOC_SIZE, MADV_WILLNEED) | 返回 0，errno 为 EBADF |
| [`LTP_8A337DE81B7EE722`](../../library/rules/ltp-8a337de81b7ee722.yaml) | 无额外前置条件 | 调用 madvise(amem, st.st_size, MADV_FREE) | 返回 -1，errno 为 EINVAL |
| [`LTP_9847441A67CBCED8`](../../library/rules/ltp-9847441a67cbced8.yaml) | 无额外前置条件 | 调用 madvise(amem, st.st_size, MADV_KEEPONFORK) | 返回 -1，errno 为 EINVAL |
| [`LTP_AE4AAF77935210BC`](../../library/rules/ltp-ae4aaf77935210bc.yaml) | 无额外前置条件 | 调用 madvise(sfile, st.st_size, MADV_DONTFORK) | 返回 -1，errno 为 EINVAL |
| [`LTP_BFCEAB073A576D51`](../../library/rules/ltp-bfceab073a576d51.yaml) | 无额外前置条件 | 调用 madvise(addr, MAP_SIZE, MADV_GUARD_INSTALL) | 调用成功，返回 SUCCESS |
| [`LTP_C12A995BA4553344`](../../library/rules/ltp-c12a995ba4553344.yaml) | 无额外前置条件 | 调用 madvise(amem, st.st_size, MADV_COLD) | 返回 -1，errno 为 EINVAL |
| [`LTP_C1462BACF46A177B`](../../library/rules/ltp-c1462bacf46a177b.yaml) | 无额外前置条件 | 调用 madvise(amem, st.st_size, MADV_PAGEOUT) | 返回 -1，errno 为 EINVAL |
| [`LTP_CEE8E7C01B4D8059`](../../library/rules/ltp-cee8e7c01b4d8059.yaml) | 无额外前置条件 | 调用 madvise(amem, st.st_size, MADV_HUGEPAGE) | 返回 -1，errno 为 EINVAL |
| [`LTP_D0BAC1CBF594EDA6`](../../library/rules/ltp-d0bac1cbf594eda6.yaml) | 无额外前置条件 | 调用 madvise(sfile, st.st_size, MADV_UNMERGEABLE) | 返回 -1，errno 为 EINVAL |
| [`LTP_D839FF9444196DDB`](../../library/rules/ltp-d839ff9444196ddb.yaml) | 无额外前置条件 | 调用 madvise(sfile, st.st_size, MADV_MERGEABLE) | 返回 -1，errno 为 EINVAL |
| [`LTP_D90E4279570B6A94`](../../library/rules/ltp-d90e4279570b6a94.yaml) | 无额外前置条件 | 调用 madvise(target, MEM_LIMIT, MADV_WILLNEED) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_EBB107DB7E3EFF2A`](../../library/rules/ltp-ebb107db7e3eff2a.yaml) | 无额外前置条件 | 调用 madvise(addr, size, advise) | 返回 -1，errno 为 EINVAL |
## `mallinfo`

没有形成可发布的合规性规则。

## `mallinfo2`

没有形成可发布的合规性规则。

## `mallopt`

没有形成可发布的合规性规则。

## `mbind`

没有形成可发布的合规性规则。

## `membarrier`

没有形成可发布的合规性规则。

## `memcmp`

没有形成可发布的合规性规则。


## 技术参考

- 报告 ID：`spec-20260716t033522z-8b4561ef`
- 来源：`ltp-local`，内容快照 `sha256:d789747f0c0bf1697f538bc5166073fd8449dec3beac7b12ac0be0b1b716dcb4`
- 全局待处理 syscall：293
- 提取数量：`80`（来源：`command`）
- `fspick`：证据 2 条，未解析 1 条
- `fstat`：证据 3 条，未解析 0 条
- `fstatat`：证据 1 条，未解析 0 条
- `fstatfs`：证据 4 条，未解析 0 条
- `fsync`：证据 5 条，未解析 1 条
- `ftruncate`：证据 7 条，未解析 0 条
- `futex`：证据 8 条，未解析 2 条
- `futimesat`：证据 0 条，未解析 0 条
- `get_mempolicy`：证据 4 条，未解析 2 条
- `get_robust_list`：证据 5 条，未解析 0 条
- `getcontext`：证据 2 条，未解析 0 条
- `getcpu`：证据 4 条，未解析 1 条
- `getcwd`：证据 3 条，未解析 0 条
- `getdents64`：证据 3 条，未解析 0 条
- `getdomainname`：证据 2 条，未解析 0 条
- `getegid`：证据 2 条，未解析 0 条
- `geteuid`：证据 3 条，未解析 0 条
- `getgid`：证据 2 条，未解析 0 条
- `getgroups`：证据 0 条，未解析 0 条
- `gethostbyname_r`：证据 1 条，未解析 0 条
- `gethostid`：证据 3 条，未解析 0 条
- `gethostname`：证据 4 条，未解析 0 条
- `getitimer`：证据 5 条，未解析 1 条
- `getpagesize`：证据 2 条，未解析 0 条
- `getpeername`：证据 2 条，未解析 1 条
- `getpgid`：证据 8 条，未解析 0 条
- `getpgrp`：证据 2 条，未解析 0 条
- `getpid`：证据 2 条，未解析 0 条
- `getppid`：证据 2 条，未解析 0 条
- `getpriority`：证据 2 条，未解析 0 条
- `getrandom`：证据 6 条，未解析 1 条
- `getresgid`：证据 0 条，未解析 0 条
- `getresuid`：证据 0 条，未解析 0 条
- `getrlimit`：证据 4 条，未解析 0 条
- `getrusage`：证据 6 条，未解析 1 条
- `getsid`：证据 5 条，未解析 0 条
- `getsockname`：证据 2 条，未解析 0 条
- `getsockopt`：证据 3 条，未解析 0 条
- `gettid`：证据 5 条，未解析 0 条
- `gettimeofday`：证据 3 条，未解析 0 条
- `getuid`：证据 2 条，未解析 0 条
- `getxattr`：证据 9 条，未解析 2 条
- `init_module`：证据 5 条，未解析 0 条
- `inotify`：证据 12 条，未解析 0 条
- `inotify_init`：证据 2 条，未解析 0 条
- `io_cancel`：证据 4 条，未解析 1 条
- `io_destroy`：证据 4 条，未解析 1 条
- `io_getevents`：证据 4 条，未解析 1 条
- `io_pgetevents`：证据 1 条，未解析 1 条
- `io_setup`：证据 9 条，未解析 1 条
- `io_submit`：证据 8 条，未解析 1 条
- `io_uring`：证据 1 条，未解析 0 条
- `ioctl`：证据 85 条，未解析 2 条
- `ioperm`：证据 2 条，未解析 1 条
- `iopl`：证据 4 条，未解析 0 条
- `ioprio`：证据 4 条，未解析 0 条
- `ipc`：证据 0 条，未解析 0 条
- `kcmp`：证据 6 条，未解析 2 条
- `keyctl`：证据 25 条，未解析 4 条
- `kill`：证据 11 条，未解析 0 条
- `landlock`：证据 13 条，未解析 3 条
- `lgetxattr`：证据 5 条，未解析 0 条
- `link`：证据 8 条，未解析 1 条
- `linkat`：证据 2 条，未解析 1 条
- `listen`：证据 1 条，未解析 0 条
- `listmount`：证据 8 条，未解析 1 条
- `listxattr`：证据 6 条，未解析 0 条
- `llistxattr`：证据 6 条，未解析 0 条
- `llseek`：证据 1 条，未解析 1 条
- `lremovexattr`：证据 2 条，未解析 0 条
- `lseek`：证据 3 条，未解析 2 条
- `lsm`：证据 11 条，未解析 2 条
- `lstat`：证据 15 条，未解析 0 条
- `madvise`：证据 13 条，未解析 0 条
- `mallinfo`：证据 2 条，未解析 0 条
- `mallinfo2`：证据 1 条，未解析 0 条
- `mallopt`：证据 1 条，未解析 0 条
- `mbind`：证据 4 条，未解析 3 条
- `membarrier`：证据 2 条，未解析 2 条
- `memcmp`：证据 1 条，未解析 0 条

<details>
<summary>机器可读元数据</summary>

<!-- syscallguard-metadata -->
```yaml
schema_version: 1
kind: syscallguard_ingest_report
report_id: spec-20260716t033522z-8b4561ef
generated_at_utc: '2026-07-16T03:35:24.146836Z'
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
pending_count: 293
selected_syscalls:
- fspick
- fstat
- fstatat
- fstatfs
- fsync
- ftruncate
- futex
- futimesat
- get_mempolicy
- get_robust_list
- getcontext
- getcpu
- getcwd
- getdents64
- getdomainname
- getegid
- geteuid
- getgid
- getgroups
- gethostbyname_r
- gethostid
- gethostname
- getitimer
- getpagesize
- getpeername
- getpgid
- getpgrp
- getpid
- getppid
- getpriority
- getrandom
- getresgid
- getresuid
- getrlimit
- getrusage
- getsid
- getsockname
- getsockopt
- gettid
- gettimeofday
- getuid
- getxattr
- init_module
- inotify
- inotify_init
- io_cancel
- io_destroy
- io_getevents
- io_pgetevents
- io_setup
- io_submit
- io_uring
- ioctl
- ioperm
- iopl
- ioprio
- ipc
- kcmp
- keyctl
- kill
- landlock
- lgetxattr
- link
- linkat
- listen
- listmount
- listxattr
- llistxattr
- llseek
- lremovexattr
- lseek
- lsm
- lstat
- madvise
- mallinfo
- mallinfo2
- mallopt
- mbind
- membarrier
- memcmp
syscalls:
- syscall: fspick
  source_fingerprint: sha256:cea6a1c90e6182fb256f5c28128ca1aabf89228e8728cc4788bf1221f64ae5b1
  recognition_fingerprint: sha256:8d19986ef13f5c483ed7196304f835091a1273ff6b3fcee5e0ff314e5a9150e1
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: fstat
  source_fingerprint: sha256:1f83263c89cb8c37140be52e887dd4d27559fa55caac9a9ce5cbefc10bb3e677
  recognition_fingerprint: sha256:ed6311c038477eb87b65156f569a0bb926917f95f6da7ce43cce39a12da8f77b
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_466F01834F965621
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:466f01834f965621ab012906888aad7acf5ae6e62b290e92e8975f01e19fc7ef
  - id: LTP_64B1B6EEEC3F79FC
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:64b1b6eeec3f79fc85edbb4e3e6e6066f854c28d9721e3cbbab7294f2295e473
  - id: LTP_A363671517C058B1
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:a363671517c058b177b37c8394c48508feb8e3077c9818d779846e05afad7aa3
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: fstatat
  source_fingerprint: sha256:50e7c45ff4fc0cdd167f5c60897ca8a80d660ba49ab3bfc751d6995fc9c8ba23
  recognition_fingerprint: sha256:4385b85387b01b5b5a595cb18d3ccb596240b90a4830b40b75cc65c8f5f6ccae
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_90068DD4526FEFC0
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:90068dd4526fefc01f1d69c833e3bfc26dbeb3d17893baa29a215ca3685e77c4
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: fstatfs
  source_fingerprint: sha256:65ee20b2ce98c8ebf8154ee6ca0db6010faf7792a8e9bcdef002d006356f77cb
  recognition_fingerprint: sha256:938b25593f00195d6f297c41c4353acccda196f802f88c405301b126d329e5e0
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_7C0112A92527C2A7
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:7c0112a92527c2a7ab9f1d97532b9904a23602736586d210189db4eec7b1e2c2
  - id: LTP_90B95E5DF2BD7509
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:90b95e5df2bd7509dcf232f0e78eb3461eb6da29dfa4f6dc8795bff6676b016a
  - id: LTP_EB1B734A0943248E
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:eb1b734a0943248e40e858f9d9547299edda39a8c18852a2c1775fce0d0b0f6e
  - id: LTP_F92A1A6292F40811
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:f92a1a6292f408112c127494a4bcae4af4bb94ac649b58da52777e46e088a50e
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: fsync
  source_fingerprint: sha256:752e7996e3f21d7a0e6fd06f19136db25b9c58b8c532fca4a037d98896e63d6f
  recognition_fingerprint: sha256:78fa0bf9d82f3f722b8490d23de4c8fc7db8eb672b04c6d2e88ffa9fb9289fd4
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: ftruncate
  source_fingerprint: sha256:3500dd0b2efea4bc021db8f8d1ea57693a7397ba0d356ec4a46df2e1137efc8c
  recognition_fingerprint: sha256:60aed23a561524a22674f9d637add73631e3d7cb06d69cc777b933c1364c01eb
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_02D0577172D97F4B
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:02d0577172d97f4b0c53b13d33076d3efcfec173bbca9004cf800d6afc185499
  - id: LTP_213EA37A2B59AB99
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:213ea37a2b59ab99adf7f686665e25ddbe33d1ab0987a2491350f663626e280c
  - id: LTP_2648B36BD9CF39EE
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:2648b36bd9cf39eed20eeccf40f65b34092fefc293cc25e59a3b4d0130b0968f
  - id: LTP_46AA49209C30E739
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:46aa49209c30e739363f6cd984100b84e2a071850a4962d4d4431c6f8305ba46
  - id: LTP_5E6E4D23F79BC9DA
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:5e6e4d23f79bc9da671ad8f01d2701c24c0c3e551f212a49795f70ba908f32e7
  - id: LTP_63E6527501A08F92
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:63e6527501a08f92aa43e68124f897c040ee1772af6738c64e18e0d766c0823e
  - id: LTP_EB214534D857AE95
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:eb214534d857ae95cd746cbfc32631b6ce2f8653bb7bcf3b1fe2839727245cf8
  - id: LTP_EC25ABB5C68F5299
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:ec25abb5c68f52996d646b0c5a0f0325269a0abf4f21aa60f4d285dc17ecad87
  evidence_count: 7
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: futex
  source_fingerprint: sha256:318382a96dc7560c485e768c451a6890a1e75a6bd3694c1608b73b6719e97c59
  recognition_fingerprint: sha256:8c6963f7fc746d0933cc863631f7207e86218e6b7714f6fd76dc5fba1bdf525d
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 8
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: futimesat
  source_fingerprint: sha256:996c44dc07e9ecef905d2fd6147c84ddc5b11a779e0f4ac0c5bb90df6e073167
  recognition_fingerprint: sha256:d06132ba259c6a9321cefbe94c2f5ba936cc02ae59951284d3cd28e1513c77de
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: get_mempolicy
  source_fingerprint: sha256:df964226987afec32e45dd7dc4762f9f503a082c97640fca4b849dc1527d0dc6
  recognition_fingerprint: sha256:7857d0daaa342ad9aff31406d4f820b7ee8744efff04a38241299fd1f8f4ec11
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: get_robust_list
  source_fingerprint: sha256:e5ed08dc9f2350aebd9d71c4a60d400e4be0ada6d3fe38874db3481436920a00
  recognition_fingerprint: sha256:26a55bd92272afefe2e8ecce08b1c1cfeb2fb9e83d0ce0f8dc3d002304eb42cc
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_3F7F517D8AA3614C
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:3f7f517d8aa3614cc841cafd2fb2ba7f37987628ef7c08acee77b45451f6119d
  - id: LTP_5CC32725A40238D7
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:5cc32725a40238d7b4ae1ade31e98d1d8718054fbce20edba776af1c99aa917a
  - id: LTP_7F4B220485E99184
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:7f4b220485e99184e61a7692983c01eff9a4abf0aa67b529ce23dd78af7d2fc7
  - id: LTP_C46B746DAC4331D5
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:c46b746dac4331d56727fcdf00d90f08ce593dc1087d55018d0449db964039ff
  - id: LTP_F3CE94166822B3E3
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:f3ce94166822b3e3c4ff880c3e67ba89d1790bb492cf4ca052638688942d9a5d
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: getcontext
  source_fingerprint: sha256:3980e8642183ab81d5f98fcb7ef7caad2be2005466099368a36ce9ff0fe6fdb1
  recognition_fingerprint: sha256:9c7a8d7f30bdb118caf47278c4787968c9c2d9de82a6e91dc7909491d6042581
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_70E5CA8341B80E83
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:70e5ca8341b80e8352b9c97562fa5463658d7d1287b107416580dec7fa2f79b9
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: getcpu
  source_fingerprint: sha256:24576af7a3e1294b10b126a92990529e4f57904eb35992ac431406cdf6be3441
  recognition_fingerprint: sha256:cb2283357aa8b273a9983c9a949155211f8980b2cdc914aa1890bb00c4ce265f
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: getcwd
  source_fingerprint: sha256:8b0b23a4dcfbe0d60012953312e48c64c5bd4c8235f30cc3834d0fcecba11d7b
  recognition_fingerprint: sha256:8d291a046476e080cd5443387eb65f5a1ced5b1f709a99e5f22e80164d964973
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_53E3454ED6EFD842
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:53e3454ed6efd842d4456341bdaf29e25ad49ab8f5a55c170a4e23c3355fe2f9
  - id: LTP_729222947741DFD6
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:729222947741dfd63a81e9c93572baf5c789acbffca84a2edd5dce13fe1fb2a3
  - id: LTP_89BB56D579EEF06D
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:89bb56d579eef06d47c81ec803de4585a5afecb282c21eb9399b98db46b4e647
  - id: LTP_912BE233FAFE6762
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:912be233fafe67624b7249f0492e0d4ded1fbd11fc3cf20af5bc3bb23dfc0874
  - id: LTP_FC1E41C3414E7F21
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:fc1e41c3414e7f214284f077070cc39320ebd294786eda043234fca8d9f5da6d
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: getdents64
  source_fingerprint: sha256:ff03f95706bf002313b1ebb895516a0d8c2501080598134a49252b9fc609fcf2
  recognition_fingerprint: sha256:84aeb81d227ead16089b41c6ad42d0a20424677f49dd016bafee2c1437eaece9
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_39008564F17DCBDD
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:39008564f17dcbddcb905c58e4ea634b69ee068f66e8005cb6a52a504e9da344
  - id: LTP_409C97094F0CED1F
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:409c97094f0ced1f465e2cdae5bbfb4caf29b11c7062603a1139d46f3d6322be
  - id: LTP_44B41305EB538966
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:44b41305eb538966a0e42523ddfb9c91f77bf9e7f919d0a6b3aec054de05868f
  - id: LTP_8CA8B0BC6ED845C4
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:8ca8b0bc6ed845c4a4faefb0cf21071b83be9fccfee0399b1f44a02aa861046d
  - id: LTP_FF639650AE6F7097
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:ff639650ae6f70979e66371c53d1e1e4f4b214936d1fbfe5cb2be2fb4a1ea9ac
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: getdomainname
  source_fingerprint: sha256:05c5f426c00c6c8034528a355d7aa55f9bec06ac573dc3fe94a2648d2170ccbc
  recognition_fingerprint: sha256:dc5e3f954d4662a67134bc59752d7e27b19c04b52a4489da7a0170cb93ea89a3
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_3C4C8CA4ED44FE57
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:3c4c8ca4ed44fe574b6132e5f1b86df5e014211eda61e0bf3ae1c0ca704dbab6
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: getegid
  source_fingerprint: sha256:15f8ecd293acd6cc611ca7f818b5ca03b986d41cb540ca261268887a9ad2ec20
  recognition_fingerprint: sha256:902cfeb3315b0f000ef92b0db9243e296f1a7af902b5a4d848669a39553967c8
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: geteuid
  source_fingerprint: sha256:7ef66bde6030bc3f1065d278c3cb7c7b9e774e46e0379fb0c785ccc15ed6e59a
  recognition_fingerprint: sha256:a2cbd2ee716380cb1e57e4fe3b4d5579402bedf09fdfbcfaac9ccc51d94e7282
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: getgid
  source_fingerprint: sha256:6d048bd2e1e133a66dea5cd57a60d5ad8ca8f816c70faa52d11a10d461881e53
  recognition_fingerprint: sha256:28eb74cbcdaa6dd10af36df9cb32f453415d56c39acc744f433b6b122789fa80
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: getgroups
  source_fingerprint: sha256:78507ba695ed751444f22a5223f0fc16cb5176b3906813bf214449ef2dd2ffc5
  recognition_fingerprint: sha256:7c976598aced79de7adea79548b7ad746e5ccd7fa826a57f8fb1c8fad2e9bb8a
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: gethostbyname_r
  source_fingerprint: sha256:5bf970d940a0ee47746016f266621f3bac25f47e85ba16d846df5674436544e2
  recognition_fingerprint: sha256:769304309d68e89331062c450de879e2c02dca969649d4c2c288167bf8dd86a5
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: gethostid
  source_fingerprint: sha256:4b291a7f5012d6fd1c33ac499595557f0a324867131c2f5207832452d65ee43a
  recognition_fingerprint: sha256:d68b331849393d5178290dd9c43e177e716115616197c168b98e8f720df7a265
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_7B9FBEA6E7CF8A70
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:7b9fbea6e7cf8a708194477d3d2c32704b481014077bb6c76073db9e2f9c2b65
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: gethostname
  source_fingerprint: sha256:dee36371c5e588b2bd57d8cf4d99c89b7f64b98f832ff14bf663e1f981e15c39
  recognition_fingerprint: sha256:e9df41d251d4c4303645e2fd39ef991b00b1aea3aef1113ff2e1ae63c048375d
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_92006BB83B7F5B92
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:92006bb83b7f5b92d4415dfbd952350b23d8465ff01d67a1b2dabb1052e57141
  - id: LTP_C09E83BE36885312
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:c09e83be3688531210e2e1d786e85d9e52cc39bd66d7f65a47dcf87f4365c2b8
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: getitimer
  source_fingerprint: sha256:072e2f535640ac1c794a6d4465c583cd19571117227c21c259b7ec53aa22db63
  recognition_fingerprint: sha256:c51ee2a2f5ab8fe8b6b0144b25e77c53d397656033359d847a82f2583a1e0f7b
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: getpagesize
  source_fingerprint: sha256:6f843b6704e3d7c4e5d6df065fc774b3aa1e79f80033da459f22a03c11530943
  recognition_fingerprint: sha256:d3d38bf9e2fc7d0405337d7af76be07ab7e42e8d4da87a187af6fb9ec2801048
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_90893935E64240AA
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:90893935e64240aa8fa9dffe15da614494b4acb748ac76733b5d9168d4f5d437
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: getpeername
  source_fingerprint: sha256:2a540b87619fd1fd14cfb366ecff81dca3d065bc0d6c22541c7853c54e3bf166
  recognition_fingerprint: sha256:e1ea0a55042214adba23f3db74744474c56e8dcb5a8dd4133263dc2195630d05
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: getpgid
  source_fingerprint: sha256:1bd409c1625f03b29f70c22684fe20c9dc4d46749b95a174985b9a0433c6db8f
  recognition_fingerprint: sha256:2af0cc81f3d2470a973525451b4940345e9298a9a6c58974d9984f902e8d5413
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_352394AAA6D49339
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:352394aaa6d493392bb743f69c206521e937c1336a1dc66bb12e7b11c63c2c77
  - id: LTP_8C1C2578972FCA1D
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:8c1c2578972fca1d655df720a137f88882824f681ac3cbfa59052c4a1f8ef64a
  - id: LTP_9461AA782926BAB4
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:9461aa782926bab4cb006db18510ae154420b8c023b3b2f9cc0308d205ca9cf7
  - id: LTP_DA8094714BA3F734
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:da8094714ba3f734708cdc2e3c0c2f3c4ebf2b7d376b9a39b45ee03d0909bbc9
  - id: LTP_F5D2C7B7F0E3D07C
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:f5d2c7b7f0e3d07c127c21233c83cc2ce1ed5a1b40375a4c9e77df3cab97d5f8
  - id: LTP_F9357233C6D73800
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:f9357233c6d73800c2cf4dea52dc1935bf1ac03fbe6c0be994610be5e0748070
  evidence_count: 8
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: getpgrp
  source_fingerprint: sha256:42d8f3aac7a44e40d99e35c8659d362dc72ec500e674d6b4277adce8e38e91ef
  recognition_fingerprint: sha256:cb3c929267a8dd5ea9e1e537c700b742a589225677029c8ff10fd6fe02be72a5
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_A82CC878A661AA28
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:a82cc878a661aa289f9978fb4eb6ba9b8717916191a4d0a92b729bbd245c7023
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: getpid
  source_fingerprint: sha256:0954990e7eb6a790786e10d69475345d4290fc7c5c72891a318de5cc0fd5babb
  recognition_fingerprint: sha256:93bacc8feab66c006c054829c0b17b0eacae72bdb688e9f54db69692e4e98f2e
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: getppid
  source_fingerprint: sha256:b6da5286d433a05c1774155b683b0f2f14ca304a10226b1a7a10fa6a9b2e9b96
  recognition_fingerprint: sha256:7f02a9581e9ba868ee69df6099b1134228341bd9c0def57d26515f8b5b958e6e
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: getpriority
  source_fingerprint: sha256:0ce73c8e6e64ce6e10f2519e66c69d7315f13f11571f9409f19d155e77aec4ad
  recognition_fingerprint: sha256:1f04b74f37d5fc9ce5b281f118150330d9cd1c15809527d4b657d1ac330b665c
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_0F02943A8FDA4830
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:0f02943a8fda48308b8b1bf0b3699cd65678254104143bf70caf36004f8b875e
  - id: LTP_57C7DC5E29B5ADF8
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:57c7dc5e29b5adf895024eaf279017a0a88a9e1468ba534d5889b086a5993f6f
  - id: LTP_6DF55FF20A44572D
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:6df55ff20a44572df1c26284f4cf16c249e9e16af1682cc1a8607d1c8c6f2d98
  - id: LTP_88D300A8FB407324
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:88d300a8fb407324aefbe09d1b569b46d87628a1639509250755357a2c634c1a
  - id: LTP_99C45ECA20496C98
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:99c45eca20496c9873400e90273fbe96fdd7d865b057f58ffbf85ee425dda1b9
  - id: LTP_9B0BA3ADF46F5FF4
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:9b0ba3adf46f5ff48bbc73278346b56aa43858110d87ef77f98c2075b09a8938
  - id: LTP_D5DAD3494DBAE67F
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:d5dad3494dbae67f0462ae67da79fa193a1225cbb37836489bcc615a6fc1d4ef
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: getrandom
  source_fingerprint: sha256:8334c40ddf351ac7d32f4b4122c9ca12e45ffa8486910d5f7435c0c554b75674
  recognition_fingerprint: sha256:0497ddcd970100558520baa9b37d1b3992be021daf4f2708ae0fc44c398a0eec
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: getresgid
  source_fingerprint: sha256:1696b24b856d57c2295632df1f7b0d38b473b8fa28f8d29a512f3d8128380dac
  recognition_fingerprint: sha256:6e1a061c5da5f9fdbcb1d6c17add8a35ece8c3a36a057ce9b2eacad83b8b2f40
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: getresuid
  source_fingerprint: sha256:e279dfd24776fa7d4e84e22964e1186bd2bfcf1bf6c9a58fc7af3733fce5f7a7
  recognition_fingerprint: sha256:a69c5b4ccae68034587bdd13d62c996fc343cede4d93285e204e485ce5f1dde0
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: getrlimit
  source_fingerprint: sha256:048949c417ab0a30173cd0165c6d66b225341010c5933c74350080280a2d6700
  recognition_fingerprint: sha256:5d3a45f8f7c31775ebfebdd7e315f17ca2cd632ec2beec58888afd47588fa805
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_2554AC2E46FC6A15
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:2554ac2e46fc6a15932bc27db324eb7b2b1265b2270c61b345af14c0b79e241d
  - id: LTP_26555A26680524AD
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:26555a26680524ad18ca9e9f1082b5f71c9edbd627be17b015751aadffc79033
  - id: LTP_3741A721C9C463D0
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:3741a721c9c463d0d65d94387111a493a2a48a2a5f1975fc7d455144d3321154
  - id: LTP_3B1458E6E26CBB53
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:3b1458e6e26cbb5398ae5221e8cb8d70b475e8e7fa008f9752270403cd9e3e38
  - id: LTP_652CE911B47794E0
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:652ce911b47794e00cd84120507ce0a4b8fe539ae38dff3f3c047d91cab6d2e1
  - id: LTP_7DFAC48A8971CFE3
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:7dfac48a8971cfe3c53af5bdc67246aedc28a76f25fe9bb7d59bb5481e0d4295
  - id: LTP_8988E5015778894A
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:8988e5015778894a14a0b54cc6fe1a0f1f2917fb41a0c6dfd0152069d07c8d56
  - id: LTP_914935DA5C379DA1
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:914935da5c379da10358ba568cfe5b8c7a31f6c57db6f6446451375aa973c46a
  - id: LTP_91ED7E85761CE00F
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:91ed7e85761ce00fb0a63c61b421b825e76cf8577e07d172597be6451388fa31
  - id: LTP_9305FA6D8B835652
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:9305fa6d8b8356529faec8a8a060de73350f98dc7a1db1af07a5e45a6f6e11ae
  - id: LTP_963957F80E751EE6
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:963957f80e751ee69ad1bc37cd06dda20a9abc3d44b32496ea0aae263fe7715f
  - id: LTP_A0547B601C515355
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:a0547b601c51535524cdadea7c3abcbc2fcd16157591cc2322cd1def6a08cc56
  - id: LTP_B058D6B9CBBB459D
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:b058d6b9cbbb459d2d0e155285c19e2e49762cc25177b335dab254142809eb74
  - id: LTP_BD5C209F4C6EE910
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:bd5c209f4c6ee910a13539baa6f55f3f3d2654a60e583b67fa26724405421ad3
  - id: LTP_E6C69C9F4AB565BC
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:e6c69c9f4ab565bc9a0aedb983bb975a15e4e8da818e58248848705f1fd4b2e5
  - id: LTP_EA953D5E5C4B2B1F
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:ea953d5e5c4b2b1f5d7e50d2191215d70c30b76cda9d1c29b51ec06d41f13bcd
  - id: LTP_FADBA4ADECCFBA4E
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:fadba4adeccfba4e42423348aa44d9b192be1bcb3f9c3fa8b14a06dcdb243a3e
  - id: LTP_FB0ABF26A21EAE3C
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:fb0abf26a21eae3c87515646892b72f4321684e5869b1af86bd8b799c5043180
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: getrusage
  source_fingerprint: sha256:e70b1b31b4094f41ee7a058661617810f4071b193850ca52951de29edb2ed2b0
  recognition_fingerprint: sha256:26dc0b09e8df09384f4a3e56b5d98b2fb841b401518ff3cf452fcbe2214f2ee2
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: getsid
  source_fingerprint: sha256:7fa5716fb0d95440b7e8fda0ec5bd51987a909059879f26798cbfbf15b90e3fb
  recognition_fingerprint: sha256:a5791340e9947831dd8eb65e8b1dec3a9160ddab17946e8ec43de445d1300067
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_E3BA4E4FAEF39F91
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:e3ba4e4faef39f91b2e48247b3566347e8f4c0c692c670782846bb445d5d4c87
  - id: LTP_F8FD511858BB650D
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:f8fd511858bb650d732732911dd9b8f3b5680d09787b4b47438a5bb603dc1aff
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: getsockname
  source_fingerprint: sha256:924d9b7cdacd077072b69dd95289ce1ffd71ec573b7aa2d3af65e634b5589ff0
  recognition_fingerprint: sha256:507cee8d24529e892fb7056c9837cb0f86ca7d9e6db9e34fa25f14bbdc8b0387
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_52CE7E6F9B5FF947
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:52ce7e6f9b5ff947f2b92b0845844fa92e2daeaeb7f87b60c8f5436b7ad3450f
  - id: LTP_5920F12CFE459CB8
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:5920f12cfe459cb877731bccb8be3c2da00f049e439c1796b92e3e9a5ac6c9ef
  - id: LTP_62FDC6AAFC4F4DE5
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:62fdc6aafc4f4de5abe2b5f43bc4db32dca0dd6c2b6d1cae16e922df7fcd7313
  - id: LTP_AA9171FB32FD0C67
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:aa9171fb32fd0c671764cc145bd58abcb119b7ef2c9f2e342fdec7ba261573b7
  - id: LTP_B25461243478CEF8
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:b25461243478cef85a752642b4328cc91e8d034447b09444110689f31bc19799
  - id: LTP_DBFBE6A110B3D17B
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:dbfbe6a110b3d17bac558d2ea9f40b57cb18ad41d2b90f2ef587ede93cff633f
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: getsockopt
  source_fingerprint: sha256:37fd155c01e258396f5af11ddd4e69b1ce829bf9fb7f61e5313d1b6fe9fbccf2
  recognition_fingerprint: sha256:949e29188236721532a2b088dc420277734731febd7195974716527a81d301cc
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_0B982157D25C1D06
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:0b982157d25c1d06236980a4a5d2d1c9c8f2d8456c74c7072f2def05ca8a60a5
  - id: LTP_0EEA999DE0FFD37D
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:0eea999de0ffd37deee6ebcc5d90326963d95dcc08c115eb5f1359f119ccfa45
  - id: LTP_3DDCD08519809A17
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:3ddcd08519809a17ca7a96a5ee1cdbdc58690968fdea20e1594ac65cd34a4098
  - id: LTP_809809859ABFE5C1
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:809809859abfe5c19887d5b6d60386c073afa22a1113d13570ca19d0f39d2388
  - id: LTP_8BCA62F97A197BC2
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:8bca62f97a197bc2486638365fd31e2c4fa35bab95eb651113068ba12997e583
  - id: LTP_B72405976D9F15E6
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:b72405976d9f15e6653a4c19a55c21b6afeb46487ee550707600903ab0c823d3
  - id: LTP_D77AD0D4DC9C0C9E
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:d77ad0d4dc9c0c9edb967f3b45dd2a074cbf7266307be86acafe7d0e5554574d
  - id: LTP_DC1ACD3B300AFCC3
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:dc1acd3b300afcc35e5ee15ef5aa4b8726bce8004310036fffa8a8a811ae2160
  - id: LTP_FE51D85F4A425C61
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:fe51d85f4a425c61761c446e685c34d147bb094cdb0a31f3af1659b800f137cc
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: gettid
  source_fingerprint: sha256:15a03fa7d68718e6b01c51675b28efdbe255ad84a4c6c3b77ceab0c872c39f1b
  recognition_fingerprint: sha256:98274316436301f25fbea141e721634b37f672a8a22ed8f0464ff00c293d9ac9
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_BD3B3CC9032DF4E5
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:bd3b3cc9032df4e5ed71324ac3a187fd6b9c5708435812e1f3fa5f2f5d7297ea
  - id: LTP_E083F071E292B561
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:e083f071e292b561bc9b92b57e487f1edc298723ce570c08c2c94f7d85088949
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: gettimeofday
  source_fingerprint: sha256:94c3ceca3966c0bc1abc611535c4d7c637029f779a29a3698266d370e3ff9839
  recognition_fingerprint: sha256:2954a4c73d5bda481f7fd5291f4c001a0a43aac307837685e8c98b21e7bfa459
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_5B4AA4EE494B37D2
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:5b4aa4ee494b37d28532bc2342bda381464c5ae3ffeb7fb7f6e14d925a95e2e7
  - id: LTP_6C14DE68E3C0CC24
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:6c14de68e3c0cc24bbb7021cd805e26a73df65653f350d8fa8ed8de5232949e8
  - id: LTP_FCF5A4835CFCD143
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:fcf5a4835cfcd143bee1e5d04d1a6a86a0a2d3560f5b6abc1a0b388e31f42c86
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: getuid
  source_fingerprint: sha256:e1e7939b57424bee58fa4c67bdcae73d2e25249ebfdfb00bc2b1c4a555b5cf59
  recognition_fingerprint: sha256:a30e284d7c36099ee25f4b5e395eaf1d0ce14703b2eb0c72707931ce485753d5
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: getxattr
  source_fingerprint: sha256:05a86817eafa7c9b90b665113031500fb30121baef63b2fa4417341c8c2d6785
  recognition_fingerprint: sha256:482cd61143e145441ed7139e059a39cfca76edae00d60dc70d918c5c7f230d39
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 9
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: init_module
  source_fingerprint: sha256:c8b46b2ca233ba87b36bba9d86cfa0d723e66625a982955f8f755abd26ae61a1
  recognition_fingerprint: sha256:627b558f8ac50c4571c06081fa96f896f70d8224179b28d610f3767746651578
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_0080969B4E1A8F96
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:0080969b4e1a8f9679d77c60fc72e5e630e7ec64f3d8172ab277651b30639ab3
  - id: LTP_0D3B043506A61BD6
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:0d3b043506a61bd69accde8c08199f4636f7796b6e95193d24adad0ca99ce286
  - id: LTP_1D3F4A6BCBF6BBE5
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:1d3f4a6bcbf6bbe5d957d3e78bfb1aaa3354bc295bfa33bffc7f7124afe30cb0
  - id: LTP_453DFC908EB0DD9E
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:453dfc908eb0dd9e2c0917d52af80520155fe7276760fe9cde183412e5e7bfb1
  - id: LTP_77C73AE1FE592877
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:77c73ae1fe5928779940252f0789b97020f1eb053e7270c368326200db871398
  - id: LTP_80AFFD1BF1D04F38
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:80affd1bf1d04f38304f6fc04212433f9b32e76a16eda4000eb08cec472454fc
  - id: LTP_930417433305D40F
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:930417433305d40ffe25b45bc6d81f5c9224ba6dd0cb9e972ceacf928f88f185
  - id: LTP_AD9C93AEB21E0E7B
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:ad9c93aeb21e0e7b61b88bafd91c7d121c0b7f3ed43afb9e6296533719d988da
  - id: LTP_D246498B20D9CB2C
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:d246498b20d9cb2cd6ece54014a50e1c77fa08b6a598251c2dc0e3a3700193e2
  - id: LTP_D58C26D260BBCED5
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:d58c26d260bbced5c29ac631176f0bd7989e96c72180161894b779c1b699a904
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: inotify
  source_fingerprint: sha256:31ac39d94d64342aa4be6d94d46fe00c088e2e92bbd86c1c65a7897f5b7e7a30
  recognition_fingerprint: sha256:ef1cc1d4c64832f910c0f304182316ef6f6160b93b9f7dc7bc948af0a50bd09b
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 12
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: inotify_init
  source_fingerprint: sha256:6d761404dec561676e4755cf6ae5c7196e5e9f7437c892f1a1e20bd28f4592ea
  recognition_fingerprint: sha256:8aa8d175b260bde79f6a0fef0069f2b67a9aebdbdb0e52b7550fb30df55c7b6f
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: io_cancel
  source_fingerprint: sha256:d4b076f3ea49fff46bab9e256719c33959d414cc5482026ebea9f3b60fd3aa0d
  recognition_fingerprint: sha256:60526a716ac14ec4e907f4b5a3bc1f11cb2d4d0b008b2cdf5488cfbf89818bc4
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: io_destroy
  source_fingerprint: sha256:963a95a1dba968525e1a97e2d01df29386162c5853b675d1c6f1815c69bcd766
  recognition_fingerprint: sha256:9bf591c72ad0053db78fab2dfc2694837a3bef6a799af4ee1b6587080d93f292
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: io_getevents
  source_fingerprint: sha256:f87426c1199a0fae2595e6876da234440d63b918c100358089ebdeeaec9c9b77
  recognition_fingerprint: sha256:8c83e5e704f04f9ae0c5edce1ea19614ee32081933f989630b50f214ad490781
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: io_pgetevents
  source_fingerprint: sha256:88eff516c9c3136ac1e6e6eda20ac63c84ea370f16e7e78cd960d262fb47a378
  recognition_fingerprint: sha256:20727e01a1b1ec7369a7daaaa5be82b2875a5790499b32cbb6c16032c66c55ed
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: io_setup
  source_fingerprint: sha256:e5bd0be0d717f9a5327fa2b6e6b988d431ac9e94e3c10e0b66abd17f72fb5817
  recognition_fingerprint: sha256:ab73756acadeb6b414c189d90fa81ad30160316d0029e24a9428c7ec2cbc9f6d
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 9
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: io_submit
  source_fingerprint: sha256:b2732f3241cc1a4b4e5e5dd766ed7cd75817c59446aaf1393ba5903fef027bbc
  recognition_fingerprint: sha256:55922dcd08ae738487484e0802f3687cdff001dfcdbcbd60336f7250798b7dd4
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 8
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: io_uring
  source_fingerprint: sha256:cf3158cc3dd0cff095c6e64e43bd83a64c943bfe5f1c3aafb275d3c85ee09158
  recognition_fingerprint: sha256:603dcac637b2346dac16ebea3ce9d46c0e43e09c61672e763d144f5c00cecae3
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: ioctl
  source_fingerprint: sha256:e52dc9a731e186a43625b562b85f93069760be7fb189b5244dee363f7aaa45d7
  recognition_fingerprint: sha256:1f9e59b8ba83e391f4553624a83cbc3c31056ea211095989f79734a28e9da7a8
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 85
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: ioperm
  source_fingerprint: sha256:9f024a711c4af47b14265732ae70b8a6e7f15c35e64b654f217afcb93ddf45ee
  recognition_fingerprint: sha256:b34f39a69ee944ac898ca06ed199b7c2bab6706a138daf5e49b9b53b217205f3
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: iopl
  source_fingerprint: sha256:ceb7f1f5b18b3660d142529d7da94de429a3e5119f6d50421268bc95febda9b6
  recognition_fingerprint: sha256:5b6c7c1947f78ce39d1c4294d88d9fd59c0e8834a3d2bfb646c6a5425ba23ac1
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_1264D075DA68BB98
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:1264d075da68bb981d00141fe8bf26e0efa7631a40563b91665a0cc4c84620ad
  - id: LTP_7A6820B73D1C2059
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:7a6820b73d1c2059c5505b61a1f1f9153cf7e5f7a3b5b68602c63af375cfd6e9
  - id: LTP_FBEB6959ED2912C8
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:fbeb6959ed2912c89af854a1f29abd1de11252e5409418a7cc0eb374b7ac3461
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: ioprio
  source_fingerprint: sha256:bf0bbbc689a772d9d2b21842aef36a50893c84750a08c367e6708e9421fa6cc9
  recognition_fingerprint: sha256:71b104b11b198835f6ecb7e07c0ab9d9f9db5bf66ccd9104695aa0ce7192e0e5
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: ipc
  source_fingerprint: sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  recognition_fingerprint: sha256:85822a6d8b1a27d979425ba6f0fd7e43949cbb612bac34a26dbf6e48194096ca
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: kcmp
  source_fingerprint: sha256:24eaf02ba19e5b1c5106f5ecdd7e65e7bbcfcbe45ef5315d8580ce3a98d6490d
  recognition_fingerprint: sha256:b569d7bfb2633d8d8e59751357319edf177a9b50a6d3b7eeaabfb4ed0a43988f
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: keyctl
  source_fingerprint: sha256:eef3b7c13faf919403ba8b2882dda2f2dea0a715425c0e7d285ae5291e061f05
  recognition_fingerprint: sha256:1b313ad54e51f9731a2eaf871234dc1c314edf28195c25bfd9482af205731972
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 25
  unresolved_evidence_count: 4
  reason: unresolved_evidence
- syscall: kill
  source_fingerprint: sha256:ebf0d4d1e21aa62f72d00c4f12f74c484a98e8abb8b088d6d46ede7daaa770cd
  recognition_fingerprint: sha256:883b52ba168be646b76def3e2b40c084bedcb1e6aa2aed5f57f469335c2cd112
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_52FC519F20674559
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:52fc519f20674559343beffa85217a29d10a1d0566b335d584493da0eb9282d6
  - id: LTP_6D195DDAB1BE2B57
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:6d195ddab1be2b57ff112525baae6af1a6055cd12b1a319f25d0415f8a5c20ea
  - id: LTP_A2E3A27D541DED02
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:a2e3a27d541ded02ec7fb18cace3a23a82f65fafdc4837640cd62b790bea612c
  - id: LTP_C93391BCF53E8020
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:c93391bcf53e802000b6aa53d418dd2b999cce908bbc459163f2054f560c2397
  - id: LTP_E8E97EBE8E041CF0
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:e8e97ebe8e041cf0a6bcd84e59759538136d221ad742727373d2eefbd9381380
  - id: LTP_F13024AE4BC5C024
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:f13024ae4bc5c024d9f0e0600334466db68b567bd1a3b68b556d7f9bbd22b823
  - id: LTP_F99DE159B75F22A2
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:f99de159b75f22a255bff5773ddc96023c41a3282476ca2614202bc1ce4f51a3
  evidence_count: 11
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: landlock
  source_fingerprint: sha256:c3483d2527b81d5335df90503a85e1f2d22ac085043404a70b9d1dbaa00006f0
  recognition_fingerprint: sha256:569cc449ffdc404499f8e1e2a7188da928fa3d60a8400187e686e7737f46f798
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 13
  unresolved_evidence_count: 3
  reason: unresolved_evidence
- syscall: lgetxattr
  source_fingerprint: sha256:58c6b26abc4b96e5a2c15ad1f39555457d203e722479369279073f24036acce4
  recognition_fingerprint: sha256:b534cb58cd99931b8c98f840f1c77f18ff44f42fe3c69949f468a8e01e6ebff2
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_74DD0DCF0CE8388F
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:74dd0dcf0ce8388fe8731da3926a5479b0dac285afc7df9a4a9f59a1e41bac59
  - id: LTP_8710A0CE4DCC217D
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:8710a0ce4dcc217d40c455c33bc820340815ba5505c06fe17bac92938bbdec70
  - id: LTP_9586C4C3CAC60BBC
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:9586c4c3cac60bbcda466d4717e8774a514e5a7cc8464e773af27d48ba92e1ea
  - id: LTP_B84B9DEC792BCB34
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:b84b9dec792bcb349092295cfe8942f482764c71e25095538c4d24bff4b57085
  - id: LTP_F66773BC44256D99
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:f66773bc44256d99cabe51efdecff95a87e4094881f276b6c902def452096fd4
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: link
  source_fingerprint: sha256:d4072ead6d303c8e1a0761967ca8f92f72a9c18849660cc65f2318df071aec19
  recognition_fingerprint: sha256:1a3fcb18ffe8f8d22f9ca2e3072766b8e4eb267af665cc7dd35515dbbad0ff9a
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 8
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: linkat
  source_fingerprint: sha256:2f9151731fd8458619c5280b0a092d284c80c3e2a322d557a848d7b91366c4f7
  recognition_fingerprint: sha256:6f3df55db7d19ebdb4cf1861953126e394c0801be4b31b7ad11e40019eb6d25d
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: listen
  source_fingerprint: sha256:f525de39dff490afc4808e6ea544aeceea44f8c23bd77d672e768703eceeaee8
  recognition_fingerprint: sha256:f78ad89e204b5c618df665ab3b0527d4b3547abbd3c9375b662b2527ca1d3829
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_3707B18864CF6352
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:3707b18864cf635299970e15b85fdadf438fe486ee42ed1e84b5aba45d850e98
  - id: LTP_A1D08F4E94B7899A
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:a1d08f4e94b7899ae3ee856410e934a6e2e7d1c5f44ab183d80d579b5ea59277
  - id: LTP_ABB01FA7743F966A
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:abb01fa7743f966a783e35d8cef841c9cf2d35244ec5d52c07c878d0fc16af40
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: listmount
  source_fingerprint: sha256:8f7d79c4251882a378ab8df275c57eae13cdc473fa10d2bfaf291f46c4ee47f8
  recognition_fingerprint: sha256:3bd0b9b8cd8796a9c84609d0f5444f2c3debf5ad453ebb417c462b64bb11c649
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 8
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: listxattr
  source_fingerprint: sha256:3b4336e97f32ae03aa2f7b9d0cf4b19a5b908d809d8940da5702641fd9ec216d
  recognition_fingerprint: sha256:bddd6fbf16a1c19c88c1a21f88ea2b5b17441a8cf177e1fa2084f3b300a96ff6
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_1F8223E4EE64B649
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:1f8223e4ee64b6490a9890a96fcb2f4d1f650cb93a3891bac85401513f3e3f47
  - id: LTP_31E977FBCF448AFD
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:31e977fbcf448afd70274ac44c9fe26bf996bf30ec21a404bdd1c7240ad4393e
  - id: LTP_3CA39247E6E3D055
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:3ca39247e6e3d05562ebdadcd4b8c6b8e3fe45ce7b959b8ec1fa01fda856d07e
  - id: LTP_8D6B83A8176DB57E
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:8d6b83a8176db57ea72511e83a5811fbc4347db725a4d723db54300d9e8b328a
  - id: LTP_8F9E255B19623C24
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:8f9e255b19623c24a8ed6c18591f20ba43fb4dea01ce6c811c47ab4e682eaade
  - id: LTP_969660F14B0B297A
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:969660f14b0b297a37808acccbf082c77e31549f7f06db4ef42175ea22ca87f4
  evidence_count: 6
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: llistxattr
  source_fingerprint: sha256:90d2ad2877a63af4fd10787b60fd2c4ac0223e7b165d9c42fe3359a7df46d83d
  recognition_fingerprint: sha256:cccdc367b3d239254dfbe67359f4795bd4e1aa8cd26a59c60b5ea1fa1375f612
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_196A6B5A609ADC9A
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:196a6b5a609adc9a759b8a8b70c7bfec33b49bfa7b4908d730c4a13bed37fdd4
  - id: LTP_1B2E614CA8847B31
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:1b2e614ca8847b312ed786b393a6a5996cfd3d7d05fce916a891c2a2ae5725ea
  - id: LTP_67180EB1CFAAB816
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:67180eb1cfaab81697a1990dc9a9fe2e6ddeefb107c976d9db1f35d3f5409366
  - id: LTP_C9789067DD7A3D60
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:c9789067dd7a3d600b43d62e8bcff4e7f437ebceb4d2ed2aced2ca5e218656a5
  - id: LTP_C9D2C2E3FC2B9581
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:c9d2c2e3fc2b95818a9380681086fcc9296cb4914b7e4d08df9b27097c9d00a8
  - id: LTP_D4159BF3AB78E108
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:d4159bf3ab78e1089fa7619581769c096275d25a03db3c3e6cf73a8dbb075974
  evidence_count: 6
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: llseek
  source_fingerprint: sha256:95e5f5ea96a19b3b852fcf992bee7de308ceb69e24f0d8a4d78d177000bcc9b7
  recognition_fingerprint: sha256:fa32d2a3d0e03051660766dd9fc4626285e94e358d903920f14e686a23a24deb
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: lremovexattr
  source_fingerprint: sha256:e9545e08899ece9d79f65b7136611cbcc49557b33417647a0ccb3855a7f06c8f
  recognition_fingerprint: sha256:ba61695d6d0f57899d977fe2789872072dce7a753329637598c09ade8940e008
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_7786636C200E9E5C
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:7786636c200e9e5c6ead718b2a4c4fcfac3263e45a8732ee521bb3a6e2f6136b
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: lseek
  source_fingerprint: sha256:81bc10949c45a98215a01dc3fbbbfadd3d95cbb8347c53c5e13cf32f78e35c20
  recognition_fingerprint: sha256:9ef06ac524eb84c71c4d8f76eb3a47d808b76a44357882a0cd38c8eb16199419
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: lsm
  source_fingerprint: sha256:40ff9e9f03f7b4f813e1e20f85972c444f5b2d67cf1e7ed94d7c4b65ac46ad39
  recognition_fingerprint: sha256:c0616df9671bd193a5740bc4cdf94ab11df4218f8b3db4296e21e51e33d7c525
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 11
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: lstat
  source_fingerprint: sha256:5e4156c704b1c14b42b96c4d36188f6488e5322ad2983b95c6507ed30006f8b4
  recognition_fingerprint: sha256:4d677073b6d0fdd71aeb1ef0be9f60c832ee9866203c2f108e9eb78102c7f262
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_32D132100CDC04ED
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:32d132100cdc04ed54a6e9b3929df16914bd750ac1121246e6fa05211e6c6ad7
  - id: LTP_4929F8BCC4B9811B
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:4929f8bcc4b9811bbf406b027d8e7c2e08cf8cb375a6f78e4eb89e5453565938
  - id: LTP_9FB758C1B4AF2411
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:9fb758c1b4af2411c8da67a91fabb69ede90ed52ceed982b409de9eef6bc5a8c
  - id: LTP_C3433C582C87D21B
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:c3433c582c87d21b1fcee1f8665134018647f0c74d65b783f562da4caa1ec97b
  - id: LTP_CA3E9D83D71EEED4
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:ca3e9d83d71eeed4dad6312a2791dd24c2ba4db701f33ea456d44367a2f51f9a
  - id: LTP_CBB45E0BB83FDEB0
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:cbb45e0bb83fdeb009903b985949692574aeb0fd77ebf08a945a3b42bd13b1e7
  - id: LTP_DACAAECF088B0CFE
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:dacaaecf088b0cfe5e5625c1b5115f669f9eff3debf6d0c5c9b445b87b4a910f
  evidence_count: 15
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: madvise
  source_fingerprint: sha256:07ea376c5fc34d03276c7b6582b2027f4a7d1d6e9d96a1b16e5a751e53ea91aa
  recognition_fingerprint: sha256:94244b615a782ad393303601ff0dcb0cb5eacc76cacb8c95b2138c08b7bfac92
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_004E24807F6067A5
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:004e24807f6067a5dc6a098bc1735f0b0c64782704073a54d1882587560ecd5d
  - id: LTP_0E51A1345D29A74B
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:0e51a1345d29a74b7b8326506c4062401ef5a668a018c98c58df18f19bb93c1e
  - id: LTP_1A68979B981D8947
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:1a68979b981d8947fa406b35f6017ae6e5ed07a0f0df6aa68253f616ba812c40
  - id: LTP_1B3AD244C58835E7
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:1b3ad244c58835e70d5fd7720aae6a6d96f8857d549acf0ad8b355a34b65458b
  - id: LTP_1D6E9D5C4E09D7F5
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:1d6e9d5c4e09d7f5fff8620a3865735bf544cfcbe06e0281d66246ce58c5556e
  - id: LTP_2A3276D2B0A31AC9
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:2a3276d2b0a31ac904821374e561c5378ef40cd74701114a32c348acd7bc11be
  - id: LTP_36E1AD5A78C2A50D
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:36e1ad5a78c2a50d30c60d1fd7995696aebc8b1cd9060c68030796c4b543528a
  - id: LTP_380714557B4AE9D4
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:380714557b4ae9d4c33d59d41ddfdeec0d67b9d31332565135934c916b6e93a3
  - id: LTP_505DF8E6B5595F9E
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:505df8e6b5595f9e395720e2417b6970c82fe0db97952d6c5a849f4b80f9d0b8
  - id: LTP_54CE18AAE5BDB693
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:54ce18aae5bdb693dcb34ced1236a2262c9e291dd0a31ae76b92e6c0e943aa5f
  - id: LTP_5A7E16725228EB1E
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:5a7e16725228eb1ee19985d876a9200479a8d1dcebc16fb74778ab4ba4261574
  - id: LTP_5E1690FA7F57F981
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:5e1690fa7f57f9816f3da8a9c90337d1cc33fe374f8c43ac608ab293d6cb7447
  - id: LTP_64668181C4066A0A
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:64668181c4066a0a266cfb479a6772c418a9ef1f09fcce88a08a0338bf19e834
  - id: LTP_6882C814E58F3D3B
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:6882c814e58f3d3bc5b65b2b76e3cef7e5db13b8b78fb6aa3e2b8fb61d61de58
  - id: LTP_6A52E2C16AC64CEC
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:6a52e2c16ac64cecf278be7210409f653ad5c4a882dfde8549490cf4b4563b9b
  - id: LTP_753BDF43E7947404
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:753bdf43e7947404b079d3d9142f1334a216e240b26a456fd4ea3cfe8ae57d39
  - id: LTP_8703114C595382AB
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:8703114c595382ab1bcd18ccaa8f81c8feb084620cba4ac59450575e9d779cd6
  - id: LTP_8A337DE81B7EE722
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:8a337de81b7ee72217ca147c200160ef29e148f430724adf2fa0d23d53ea1404
  - id: LTP_9847441A67CBCED8
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:9847441a67cbced84832c9e333bf95ab80ec3a3652af7b579c6290c9987828ba
  - id: LTP_AE4AAF77935210BC
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:ae4aaf77935210bce08fa100d7b18ace363e084a08f841e3e945eee558780014
  - id: LTP_BFCEAB073A576D51
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:bfceab073a576d5129b9700f03a572fb492d42c6827ee5e84ac0ca8042467411
  - id: LTP_C12A995BA4553344
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:c12a995ba4553344cd62081ffadb0422faa2b60b1428ebbf6e6cdda36affd029
  - id: LTP_C1462BACF46A177B
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:c1462bacf46a177b61a92dd94a50cbcf3231d3f068308375419d28706759d623
  - id: LTP_CEE8E7C01B4D8059
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:cee8e7c01b4d8059324c3f4869c23aae4fef998ada8f1244f4a40b4e61f57991
  - id: LTP_D0BAC1CBF594EDA6
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:d0bac1cbf594eda64d4614371e64131a7093c66ad51527b7514c192ddd2d107e
  - id: LTP_D839FF9444196DDB
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:d839ff9444196ddbe18820892bf72bffc63a13136db8b5a2715b85fe5d0341d9
  - id: LTP_D90E4279570B6A94
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:d90e4279570b6a944cabc5d1f610b1faf35f2b1aff4c67d789b7e403fcd1b247
  - id: LTP_EBB107DB7E3EFF2A
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:ebb107db7e3eff2a30e6da94b1ca8da54beb5c0ac7b982b4aee0be67c474c1d2
  evidence_count: 13
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: mallinfo
  source_fingerprint: sha256:f05e7bbcab198ec34d57e11373b7b504401ada9c3c671bc312ff03fa9cddeaf5
  recognition_fingerprint: sha256:c8a386432806112adf0d9a469c59e80b5bc53b7dc7d9c28964dd82d8f300292d
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: mallinfo2
  source_fingerprint: sha256:ad6e2083c341d53bd4c31712c908d9a18b2ab4fb3ac4a8236a0a2430cb103a92
  recognition_fingerprint: sha256:cf5cf14b5bbfe55594a727d3500ac2451429643ace7ec51da0d3b0bf306ca6bf
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: mallopt
  source_fingerprint: sha256:8d65203cfe8f7d1876808999169eac47f74ccbde67aca0bbc74b7c0e31cc7571
  recognition_fingerprint: sha256:8c6089d6b8cd5fe5c8d599d139cba7af12c70e1ead34e9d57d5ee33f9e975e57
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: mbind
  source_fingerprint: sha256:d67d8418bc3260eac92b5275ec21f7269a812f21001f67f8e5d0c6ce6545108e
  recognition_fingerprint: sha256:99b2a8bd1b40f3d18b716dc0c3444648d8d37e6ad86ec1e5687275d632e3cc1d
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 3
  reason: unresolved_evidence
- syscall: membarrier
  source_fingerprint: sha256:02e217865c928213627e7aa343fda03d3b6bab36997545bf123072e0855bcccd
  recognition_fingerprint: sha256:8da8c5e8ffbfb1864d664d7f92da879fa10e9d9812543004c4ea5db318b67f3d
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: memcmp
  source_fingerprint: sha256:b3a74d3125b6c83a8d1859215e7a126c783e67e4cc0f562e2102307574f50cac
  recognition_fingerprint: sha256:19597b3e1f8864b05d03d58190de0304842da5f6e4f0e6a33b367cfee8bb9569
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
```
</details>
