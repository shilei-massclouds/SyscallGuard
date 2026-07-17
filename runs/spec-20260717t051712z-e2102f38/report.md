# Syscall 合规性规则提取报告

## 结论

本次分析了 abort、accept、accept4、access、acct、add_key、adjtimex、alarm、arch_prctl、bind、bpf、brk、cacheflush、cachestat、capget、capset、chdir、chmod、chown、chroot、clock_adjtime、clock_getres、clock_gettime、clock_nanosleep、clock_settime、clone、clone3、close、close_range、cma、confstr、connect、copy_file_range、creat、delete_module、dup、dup2、dup3、epoll、epoll_create、epoll_create1、epoll_ctl、epoll_pwait、epoll_wait、eventfd、eventfd2、execl、execle、execlp、execv、execve、execveat、execvp、exit、exit_group、faccessat、faccessat2、fadvise、fallocate、fanotify、fchdir、fchmod、fchmodat、fchmodat2、fchown、fcntl、fdatasync、fgetxattr、file_attr、finit_module、flistxattr、flock、fmtmsg、fork、fpathconf、fremovexattr、fsconfig、fsetxattr、fsmount、fsopen、fspick、fstat、fstatat、fstatfs、fsync、ftruncate、futex、futimesat、get_mempolicy、get_robust_list、getcontext、getcpu、getcwd、getdents64、getdomainname、getegid、geteuid、getgid、getgroups、gethostbyname_r、gethostid、gethostname、getitimer、getpagesize、getpeername、getpgid、getpgrp、getpid、getppid、getpriority、getrandom、getresgid、getresuid、getrlimit、getrusage、getsid、getsockname、getsockopt、gettid、gettimeofday、getuid、getxattr、init_module、inotify、inotify_init、io_cancel、io_destroy、io_getevents、io_pgetevents、io_setup、io_submit、io_uring、ioctl、ioperm、iopl、ioprio、ipc、kcmp、keyctl、kill、landlock、lgetxattr、link、linkat、listen、listmount、listxattr、llistxattr、llseek、lremovexattr、lseek、lsm、lstat、madvise、mallinfo、mallinfo2、mallopt、mbind、membarrier、memcmp、memcpy、memfd_create、memset、migrate_pages、mincore、mkdir、mkdirat、mknod、mknodat、mlock、mlock2、mlockall、mmap、modify_ldt、mount、mount_setattr、move_mount、move_pages、mprotect、mq_notify、mq_open、mq_timedreceive、mq_timedsend、mq_unlink、mremap、mseal、msync、munlock、munlockall、munmap、name_to_handle_at、nanosleep、newuname、nftw、nice、open、open_by_handle_at、open_tree、openat、openat2、pathconf、pause、perf_event_open、personality、pidfd_getfd、pidfd_open、pidfd_send_signal、pipe、pipe2、pivot_root、pkeys、poll、ppoll、prctl、pread64、preadv、preadv2、process_madvise、profil、pselect、ptrace、pwrite64、pwritev、pwritev2、quotactl、read、readahead、readdir、readlink、readlinkat、readv、realpath、reboot、recv、recvfrom、recvmmsg、recvmsg、remap_file_pages、removexattr、rename、renameat、renameat2、request_key、rmdir、rt_sigaction、rt_sigprocmask、rt_sigqueueinfo、rt_sigsuspend、rt_sigtimedwait、rt_tgsigqueueinfo、sbrk、sched_get_priority_max、sched_get_priority_min、sched_getaffinity、sched_getattr、sched_getparam、sched_getscheduler、sched_rr_get_interval、sched_setaffinity、sched_setattr、sched_setparam、sched_setscheduler、sched_yield、seccomp、select、send、sendfile、sendmmsg、sendmsg、sendto、set_mempolicy、set_robust_list、set_thread_area、set_tid_address、setdomainname、setegid、setfsgid、setfsuid、setgid、setgroups、sethostname、setitimer、setns、setpgid、setpgrp、setpriority、setregid、setresgid、setresuid、setreuid、setrlimit、setsid、setsockopt、settimeofday、setuid、setxattr、sgetmask、shutdown、sigaction、sigaltstack、sighold、signal、signalfd、signalfd4、sigpending、sigprocmask、sigrelse、sigsuspend、sigtimedwait、sigwait、sigwaitinfo、socket、socketcall、socketpair、sockioctl、splice、ssetmask、stat、statfs、statmount、statvfs、statx、stime、string、swapoff、swapon、switch、symlink、symlinkat、sync、sync_file_range、syncfs、syscall、sysconf、sysctl、sysfs、sysinfo、syslog、tee、tgkill、time、timer_create、timer_delete、timer_getoverrun、timer_gettime、timer_settime、timerfd、times、tkill、truncate、ulimit、umask、umount、umount2、uname、unlink、unlinkat、unshare、userfaultfd、ustat、utils、utime、utimensat、utimes、vfork、vhangup、vmsplice、wait、wait4、waitid、waitpid、write、writev，发现 913 条可执行的合规性规则。

## `abort`

没有形成可发布的合规性规则。

## `accept`

共形成 6 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_277FD467E5F1BF1C`](../../library/rules/ltp-277fd467e5f1bf1c.yaml) | 无额外前置条件 | 调用 accept(socket_fd, (struct sockaddr *)3, &sizeof(fsin1)) | 返回 -1，errno 为 EINVAL |
| [`LTP_472AAA35C7382B26`](../../library/rules/ltp-472aaa35c7382b26.yaml) | 无额外前置条件 | 调用 accept(socket_fd, (struct sockaddr *)&fsin1, &1) | 返回 -1，errno 为 EINVAL |
| [`LTP_80C6DB0ACB2A5510`](../../library/rules/ltp-80c6db0acb2a5510.yaml) | 无额外前置条件 | 调用 accept(udp_fd, (struct sockaddr *)&fsin1, &sizeof(fsin1)) | 返回 -1，errno 为 EOPNOTSUPP |
| [`LTP_9CA9C6B61C3317A3`](../../library/rules/ltp-9ca9c6b61c3317a3.yaml) | 无额外前置条件 | 调用 accept(socket_fd, (struct sockaddr *)&fsin1, &sizeof(fsin1)) | 返回 -1，errno 为 EINVAL |
| [`LTP_B90CB73F36B70C6F`](../../library/rules/ltp-b90cb73f36b70c6f.yaml) | 无额外前置条件 | 调用 accept(server_sockfd, (struct sockaddr *)client_addr, &addr_len) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_E13B9C2C9645B841`](../../library/rules/ltp-e13b9c2c9645b841.yaml) | 无额外前置条件 | 调用 accept(invalid_socketfd, (struct sockaddr *)&fsin1, &sizeof(fsin1)) | 返回 -1，errno 为 EBADF |
## `accept4`

没有形成可发布的合规性规则。

## `access`

共形成 217 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_018E81B4859D535F`](../../library/rules/ltp-018e81b4859d535f.yaml) | The fixture creates DNAME_RX"/"FNAME_R as a regular file.、The fixture sets DNAME_RX"/"FNAME_R mode to 0444.、The test invokes the syscall as root. | 调用 access(DNAME_RX"/"FNAME_R, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_01F98F68E029F1A9`](../../library/rules/ltp-01f98f68e029f1a9.yaml) | The fixture sets FNAME_R mode to 0444.、The caller lacks a permission required by the operation.、The fixture creates FNAME_R as a regular file.、The test invokes the syscall as root. | 调用 access(FNAME_R, R_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_04799921082E0315`](../../library/rules/ltp-04799921082e0315.yaml) | The fixture creates DNAME_RW"/"FNAME_R as a regular file.、The fixture sets DNAME_RW"/"FNAME_R mode to 0444.、The test invokes the syscall as root. | 调用 access(DNAME_RW"/"FNAME_R, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_05A4E0F4E4D24683`](../../library/rules/ltp-05a4e0f4e4d24683.yaml) | The caller lacks a permission required by the operation.、The fixture sets FNAME_X mode to 0111.、The fixture creates FNAME_X as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_X, R_OK|W_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_07267357D988E0D3`](../../library/rules/ltp-07267357d988e0d3.yaml) | The fixture sets FNAME_R mode to 0444.、The caller lacks a permission required by the operation.、The fixture creates FNAME_R as a regular file.、The test invokes the syscall as root. | 调用 access(FNAME_R, R_OK|W_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_07D1AC926F3B00CA`](../../library/rules/ltp-07d1ac926f3b00ca.yaml) | The fixture sets DNAME_X"/"FNAME_X mode to 0111.、The fixture creates DNAME_X"/"FNAME_X as a regular file.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_X"/"FNAME_X, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_08AD094BD7C5CF64`](../../library/rules/ltp-08ad094bd7c5cf64.yaml) | The fixture sets FNAME_X mode to 0111.、The fixture creates FNAME_X as a regular file.、The test invokes the syscall as root. | 调用 access(FNAME_X, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_092C2A39F54E4F90`](../../library/rules/ltp-092c2a39f54e4f90.yaml) | The fixture creates FNAME_RWX as a regular file.、The fixture sets FNAME_RWX mode to 0777.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_RWX, R_OK|X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_094580B59455EBF1`](../../library/rules/ltp-094580b59455ebf1.yaml) | The fixture creates DNAME_RW"/"FNAME_W as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_RW"/"FNAME_W mode to 0222.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RW"/"FNAME_W, F_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_0973D484DB2E7E2D`](../../library/rules/ltp-0973d484db2e7e2d.yaml) | The pathname exceeds the supported limit. | 调用 access(longpathname, R_OK) | 返回 -1，errno 为 ENAMETOOLONG |
| [`LTP_09DDAC16EAB70A23`](../../library/rules/ltp-09ddac16eab70a23.yaml) | The fixture sets FNAME_W mode to 0222.、The fixture creates FNAME_W as a regular file.、The caller lacks a permission required by the operation.、The test invokes the syscall as root. | 调用 access(FNAME_W, R_OK|W_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_09FE3EF67718087A`](../../library/rules/ltp-09fe3ef67718087a.yaml) | The fixture creates DNAME_RW"/"FNAME_X as a regular file.、The fixture sets DNAME_RW"/"FNAME_X mode to 0111.、The test invokes the syscall as root. | 调用 access(DNAME_RW"/"FNAME_X, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_0A7162BAB3AA89BD`](../../library/rules/ltp-0a7162bab3aa89bd.yaml) | The fixture sets FNAME_W mode to 0222.、The fixture creates FNAME_W as a regular file.、The caller lacks a permission required by the operation.、The test invokes the syscall as root. | 调用 access(FNAME_W, R_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_0A9DA3A2803EEF70`](../../library/rules/ltp-0a9da3a2803eef70.yaml) | The fixture creates DNAME_R"/"FNAME_R as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_R"/"FNAME_R mode to 0444.、The test invokes the syscall as root. | 调用 access(DNAME_R"/"FNAME_R, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_0B6757A74359BB1E`](../../library/rules/ltp-0b6757a74359bb1e.yaml) | The fixture sets FNAME_W mode to 0222.、The fixture creates FNAME_W as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_W, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_0B9F382D21CF8997`](../../library/rules/ltp-0b9f382d21cf8997.yaml) | The fixture creates DNAME_W"/"FNAME_R as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_W"/"FNAME_R mode to 0444.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_W"/"FNAME_R, F_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_0DAD2B9BF983B90F`](../../library/rules/ltp-0dad2b9bf983b90f.yaml) | The fixture creates DNAME_W"/"FNAME_R as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_W"/"FNAME_R mode to 0444.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_W"/"FNAME_R, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_0E49032B253C732D`](../../library/rules/ltp-0e49032b253c732d.yaml) | The fixture sets DNAME_W"/"FNAME_X mode to 0111.、The fixture creates DNAME_W"/"FNAME_X as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_W"/"FNAME_X, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_0E9124C6B17214C9`](../../library/rules/ltp-0e9124c6b17214c9.yaml) | The fixture creates DNAME_W"/"FNAME_R as a regular file.、The fixture sets DNAME_W"/"FNAME_R mode to 0444.、The test invokes the syscall as root. | 调用 access(DNAME_W"/"FNAME_R, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_0EB6FB88C2CC23AE`](../../library/rules/ltp-0eb6fb88c2cc23ae.yaml) | The fixture creates DNAME_R"/"FNAME_R as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_R"/"FNAME_R mode to 0444.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_R"/"FNAME_R, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_0EFD831C4B5C2D95`](../../library/rules/ltp-0efd831c4b5c2d95.yaml) | The fixture creates DNAME_RW"/"FNAME_W as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_RW"/"FNAME_W mode to 0222.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RW"/"FNAME_W, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_0F3BABDCCC428DF4`](../../library/rules/ltp-0f3babdccc428df4.yaml) | The caller lacks a permission required by the operation.、The fixture sets FNAME_X mode to 0111.、The fixture creates FNAME_X as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_X, R_OK|W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_10455AB2DFB23127`](../../library/rules/ltp-10455ab2dfb23127.yaml) | The fixture sets FNAME_R mode to 0444.、The caller lacks a permission required by the operation.、The fixture creates FNAME_R as a regular file.、The test invokes the syscall as root. | 调用 access(FNAME_R, W_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_1238FDE5F55AC037`](../../library/rules/ltp-1238fde5f55ac037.yaml) | The fixture creates DNAME_R"/"FNAME_X as a regular file.、The fixture sets DNAME_R"/"FNAME_X mode to 0111.、The test invokes the syscall as root. | 调用 access(DNAME_R"/"FNAME_X, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_149BE2ED84AB5AAC`](../../library/rules/ltp-149be2ed84ab5aac.yaml) | The fixture sets FNAME_R mode to 0444.、The caller lacks a permission required by the operation.、The fixture creates FNAME_R as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_R, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_15F83338278C3CFE`](../../library/rules/ltp-15f83338278c3cfe.yaml) | The fixture creates DNAME_X"/"FNAME_W as a regular file.、The fixture sets DNAME_X"/"FNAME_W mode to 0222.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_X"/"FNAME_W, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_1617908ACCAE8499`](../../library/rules/ltp-1617908accae8499.yaml) | The fixture sets DNAME_WX"/"FNAME_W mode to 0222.、The fixture creates DNAME_WX"/"FNAME_W as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_WX"/"FNAME_W, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_16449F1C9EC8C71F`](../../library/rules/ltp-16449f1c9ec8c71f.yaml) | The fixture creates DNAME_RW"/"FNAME_R as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_RW"/"FNAME_R mode to 0444.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RW"/"FNAME_R, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_18A80CB437A03D1F`](../../library/rules/ltp-18a80cb437a03d1f.yaml) | The fixture creates DNAME_W"/"FNAME_R as a regular file.、The fixture sets DNAME_W"/"FNAME_R mode to 0444.、The test invokes the syscall as root. | 调用 access(DNAME_W"/"FNAME_R, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_1A1038DA1B735AB6`](../../library/rules/ltp-1a1038da1b735ab6.yaml) | The fixture sets DNAME_X"/"FNAME_X mode to 0111.、The fixture creates DNAME_X"/"FNAME_X as a regular file.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_X"/"FNAME_X, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_1CD2E41D7D4A4B9D`](../../library/rules/ltp-1cd2e41d7d4a4b9d.yaml) | The fixture creates DNAME_R"/"FNAME_R as a regular file.、The fixture sets DNAME_R"/"FNAME_R mode to 0444.、The test invokes the syscall as root. | 调用 access(DNAME_R"/"FNAME_R, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_1D4684A49237E045`](../../library/rules/ltp-1d4684a49237e045.yaml) | The fixture sets DNAME_WX"/"FNAME_R mode to 0444.、The fixture creates DNAME_WX"/"FNAME_R as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_WX"/"FNAME_R, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_1FC16C0CDAE55FD5`](../../library/rules/ltp-1fc16c0cdae55fd5.yaml) | The fixture creates DNAME_RW"/"FNAME_R as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_RW"/"FNAME_R mode to 0444.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RW"/"FNAME_R, F_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_20CE8BA111311B3B`](../../library/rules/ltp-20ce8ba111311b3b.yaml) | The fixture creates DNAME_W"/"FNAME_R as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_W"/"FNAME_R mode to 0444.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_W"/"FNAME_R, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_23017C8E93EEED5E`](../../library/rules/ltp-23017c8e93eeed5e.yaml) | The fixture creates DNAME_X"/"FNAME_W as a regular file.、The fixture sets DNAME_X"/"FNAME_W mode to 0222.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_X"/"FNAME_W, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_2316B5E43A8809B0`](../../library/rules/ltp-2316b5e43a8809b0.yaml) | The fixture sets DNAME_W"/"FNAME_X mode to 0111.、The fixture creates DNAME_W"/"FNAME_X as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_W"/"FNAME_X, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_239441432F72CF6C`](../../library/rules/ltp-239441432f72cf6c.yaml) | The fixture creates DNAME_RX"/"FNAME_R as a regular file.、The fixture sets DNAME_RX"/"FNAME_R mode to 0444.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RX"/"FNAME_R, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_254CA9053175601F`](../../library/rules/ltp-254ca9053175601f.yaml) | The fixture sets FNAME_F mode to 0000.、The fixture creates FNAME_F as a regular file. | 调用 access(FNAME_F, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_2591489AC5619A2C`](../../library/rules/ltp-2591489ac5619a2c.yaml) | The fixture creates DNAME_RW"/"FNAME_W as a regular file.、The fixture sets DNAME_RW"/"FNAME_W mode to 0222.、The test invokes the syscall as root. | 调用 access(DNAME_RW"/"FNAME_W, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_273F672499C6852D`](../../library/rules/ltp-273f672499c6852d.yaml) | The fixture sets DNAME_RX"/"FNAME_W mode to 0222.、The fixture creates DNAME_RX"/"FNAME_W as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RX"/"FNAME_W, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_27BB10D3A420BC7D`](../../library/rules/ltp-27bb10d3a420bc7d.yaml) | The fixture creates DNAME_RW"/"FNAME_X as a regular file.、The fixture sets DNAME_RW"/"FNAME_X mode to 0111.、The test invokes the syscall as root. | 调用 access(DNAME_RW"/"FNAME_X, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_2AF2BC8B94FE2134`](../../library/rules/ltp-2af2bc8b94fe2134.yaml) | The fixture creates FNAME_RWX as a regular file.、The fixture sets FNAME_RWX mode to 0777.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_RWX, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_2B8471E586CDE6D7`](../../library/rules/ltp-2b8471e586cde6d7.yaml) | The fixture creates FNAME_RWX as a regular file.、The fixture sets FNAME_RWX mode to 0777.、The test invokes the syscall as root. | 调用 access(FNAME_RWX, R_OK|X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_2BB228E4FB7C7BEB`](../../library/rules/ltp-2bb228e4fb7c7beb.yaml) | The userspace pointer is outside accessible memory. | 调用 access((void *)-1, F_OK) | 返回 -1，errno 为 EFAULT |
| [`LTP_2D0CADDE36D70080`](../../library/rules/ltp-2d0cadde36d70080.yaml) | The fixture sets DNAME_RX"/"FNAME_X mode to 0111.、The fixture creates DNAME_RX"/"FNAME_X as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RX"/"FNAME_X, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_2DC2EBC740EB7D7C`](../../library/rules/ltp-2dc2ebc740eb7d7c.yaml) | The fixture creates DNAME_R"/"FNAME_X as a regular file.、The fixture sets DNAME_R"/"FNAME_X mode to 0111.、The test invokes the syscall as root. | 调用 access(DNAME_R"/"FNAME_X, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_2E135F7478A355E8`](../../library/rules/ltp-2e135f7478a355e8.yaml) | A path component that must be a directory is not a directory. | 调用 access(fname2, R_OK) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_2F8A8DCF7F3AEB62`](../../library/rules/ltp-2f8a8dcf7f3aeb62.yaml) | The fixture creates FNAME_RWX as a regular file.、The fixture sets FNAME_RWX mode to 0777.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_RWX, R_OK|W_OK|X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_2FA1F12DE62C6A0F`](../../library/rules/ltp-2fa1f12de62c6a0f.yaml) | The fixture creates DNAME_X"/"FNAME_W as a regular file.、The fixture sets DNAME_X"/"FNAME_W mode to 0222.、The test invokes the syscall as root. | 调用 access(DNAME_X"/"FNAME_W, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_2FD53CE9C8CF6CE7`](../../library/rules/ltp-2fd53ce9c8cf6ce7.yaml) | The fixture sets DNAME_WX"/"FNAME_W mode to 0222.、The fixture creates DNAME_WX"/"FNAME_W as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_WX"/"FNAME_W, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_317FC70FE2A58775`](../../library/rules/ltp-317fc70fe2a58775.yaml) | The fixture creates FNAME_RWX as a regular file.、The fixture sets FNAME_RWX mode to 0777.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_RWX, W_OK|X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_31F03C781DAB0AD2`](../../library/rules/ltp-31f03c781dab0ad2.yaml) | The fixture creates DNAME_W"/"FNAME_W as a regular file.、The fixture sets DNAME_W"/"FNAME_W mode to 0222.、The test invokes the syscall as root. | 调用 access(DNAME_W"/"FNAME_W, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_32F2B22133BB52DD`](../../library/rules/ltp-32f2b22133bb52dd.yaml) | The fixture creates DNAME_W"/"FNAME_R as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_W"/"FNAME_R mode to 0444.、The test invokes the syscall as root. | 调用 access(DNAME_W"/"FNAME_R, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_332E6D2186F55A6F`](../../library/rules/ltp-332e6d2186f55a6f.yaml) | The fixture sets DNAME_X"/"FNAME_X mode to 0111.、The fixture creates DNAME_X"/"FNAME_X as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_X"/"FNAME_X, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_342F7EADB5D10802`](../../library/rules/ltp-342f7eadb5d10802.yaml) | The fixture creates SNAME_R as a symbolic link. | 调用 access(SNAME_R, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_3662829F538B7D97`](../../library/rules/ltp-3662829f538b7d97.yaml) | The fixture sets DNAME_X"/"FNAME_X mode to 0111.、The fixture creates DNAME_X"/"FNAME_X as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_X"/"FNAME_X, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_3670635A7A7D4496`](../../library/rules/ltp-3670635a7a7d4496.yaml) | The fixture sets DNAME_WX"/"FNAME_W mode to 0222.、The caller lacks a permission required by the operation.、The fixture creates DNAME_WX"/"FNAME_W as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_WX"/"FNAME_W, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_3692C449569215B8`](../../library/rules/ltp-3692c449569215b8.yaml) | The fixture sets FNAME_W mode to 0222.、The fixture creates FNAME_W as a regular file.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_W, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_3839B158DA52269B`](../../library/rules/ltp-3839b158da52269b.yaml) | The fixture sets DNAME_RX"/"FNAME_X mode to 0111.、The fixture creates DNAME_RX"/"FNAME_X as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_RX"/"FNAME_X, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_39B7A82AB3626707`](../../library/rules/ltp-39b7a82ab3626707.yaml) | The caller lacks a permission required by the operation.、The fixture sets DNAME_X"/"FNAME_R mode to 0444.、The fixture creates DNAME_X"/"FNAME_R as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_X"/"FNAME_R, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_3A0AAE966297CCA7`](../../library/rules/ltp-3a0aae966297cca7.yaml) | The caller lacks a permission required by the operation.、The fixture sets FNAME_X mode to 0111.、The fixture creates FNAME_X as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_X, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_3B48FBCC62838D3A`](../../library/rules/ltp-3b48fbcc62838d3a.yaml) | The fixture creates DNAME_RW"/"FNAME_X as a regular file.、The fixture sets DNAME_RW"/"FNAME_X mode to 0111.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RW"/"FNAME_X, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_3BA6F828CDE1E2E6`](../../library/rules/ltp-3ba6f828cde1e2e6.yaml) | The userspace pointer is outside accessible memory. | 调用 access((void *)-1, R_OK) | 返回 -1，errno 为 EFAULT |
| [`LTP_3D8EEC7BCE259B85`](../../library/rules/ltp-3d8eec7bce259b85.yaml) | The fixture creates DNAME_RW"/"FNAME_X as a regular file.、The fixture sets DNAME_RW"/"FNAME_X mode to 0111.、The test invokes the syscall as root. | 调用 access(DNAME_RW"/"FNAME_X, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_3E0472B66C2C5AB3`](../../library/rules/ltp-3e0472b66c2c5ab3.yaml) | The fixture sets DNAME_X"/"FNAME_R mode to 0444.、The fixture creates DNAME_X"/"FNAME_R as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_X"/"FNAME_R, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_3F80E012EF9B4D7E`](../../library/rules/ltp-3f80e012ef9b4d7e.yaml) | The fixture creates DNAME_R"/"FNAME_R as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_R"/"FNAME_R mode to 0444.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_R"/"FNAME_R, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_4171AFC9C3FEC6E7`](../../library/rules/ltp-4171afc9c3fec6e7.yaml) | The fixture creates FNAME_RWX as a regular file.、The fixture sets FNAME_RWX mode to 0777.、The test invokes the syscall as root. | 调用 access(FNAME_RWX, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_41AB796031F8E171`](../../library/rules/ltp-41ab796031f8e171.yaml) | The fixture creates DNAME_RW"/"FNAME_R as a regular file.、The fixture sets DNAME_RW"/"FNAME_R mode to 0444.、The test invokes the syscall as root. | 调用 access(DNAME_RW"/"FNAME_R, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_428573F9D490F227`](../../library/rules/ltp-428573f9d490f227.yaml) | The fixture creates FNAME_RWX as a regular file.、The fixture sets FNAME_RWX mode to 0777.、The test invokes the syscall as root. | 调用 access(FNAME_RWX, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_4321E1483FC39110`](../../library/rules/ltp-4321e1483fc39110.yaml) | The fixture sets DNAME_X"/"FNAME_X mode to 0111.、The fixture creates DNAME_X"/"FNAME_X as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_X"/"FNAME_X, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_43D6C007093E3B31`](../../library/rules/ltp-43d6c007093e3b31.yaml) | The fixture sets FNAME_W mode to 0222.、The fixture creates FNAME_W as a regular file.、The test invokes the syscall as root. | 调用 access(FNAME_W, R_OK|W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_43F303BEA895DBE0`](../../library/rules/ltp-43f303bea895dbe0.yaml) | The fixture creates DNAME_R"/"FNAME_X as a regular file.、The fixture sets DNAME_R"/"FNAME_X mode to 0111.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_R"/"FNAME_X, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_44313BAA17BEB1AE`](../../library/rules/ltp-44313baa17beb1ae.yaml) | The fixture creates DNAME_X"/"FNAME_W as a regular file.、The fixture sets DNAME_X"/"FNAME_W mode to 0222.、The test invokes the syscall as root. | 调用 access(DNAME_X"/"FNAME_W, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_44983CDE7F1A5F08`](../../library/rules/ltp-44983cde7f1a5f08.yaml) | The fixture creates DNAME_R"/"FNAME_R as a regular file.、The fixture sets DNAME_R"/"FNAME_R mode to 0444.、The test invokes the syscall as root. | 调用 access(DNAME_R"/"FNAME_R, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_449986F83296A5CF`](../../library/rules/ltp-449986f83296a5cf.yaml) | The fixture creates DNAME_R"/"FNAME_X as a regular file.、The fixture sets DNAME_R"/"FNAME_X mode to 0111.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_R"/"FNAME_X, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_47DFC97559CA29F8`](../../library/rules/ltp-47dfc97559ca29f8.yaml) | The fixture sets DNAME_RX"/"FNAME_W mode to 0222.、The fixture creates DNAME_RX"/"FNAME_W as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RX"/"FNAME_W, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_499A726F0D1EAB38`](../../library/rules/ltp-499a726f0d1eab38.yaml) | The fixture sets FNAME_X mode to 0111.、The fixture creates FNAME_X as a regular file.、The test invokes the syscall as root. | 调用 access(FNAME_X, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_4B27C893C8E9111F`](../../library/rules/ltp-4b27c893c8e9111f.yaml) | The fixture creates DNAME_RX"/"FNAME_R as a regular file.、The fixture sets DNAME_RX"/"FNAME_R mode to 0444.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RX"/"FNAME_R, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_4B7BD75A450AC789`](../../library/rules/ltp-4b7bd75a450ac789.yaml) | The fixture creates DNAME_RW"/"FNAME_X as a regular file.、The fixture sets DNAME_RW"/"FNAME_X mode to 0111.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RW"/"FNAME_X, F_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_4BE43BC3E131100B`](../../library/rules/ltp-4be43bc3e131100b.yaml) | The fixture sets DNAME_WX"/"FNAME_R mode to 0444.、The fixture creates DNAME_WX"/"FNAME_R as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_WX"/"FNAME_R, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_4CA2527DAE947BFC`](../../library/rules/ltp-4ca2527dae947bfc.yaml) | The fixture creates FNAME_RWX as a regular file.、The fixture sets FNAME_RWX mode to 0777.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_RWX, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_4CAA10F04475843A`](../../library/rules/ltp-4caa10f04475843a.yaml) | The fixture sets FNAME_W mode to 0222.、The fixture creates FNAME_W as a regular file.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_W, R_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_4D70641BCBFF1FC9`](../../library/rules/ltp-4d70641bcbff1fc9.yaml) | The file descriptor is invalid. | 调用 access(fname1, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_4E728F2B93D7AF55`](../../library/rules/ltp-4e728f2b93d7af55.yaml) | The fixture creates DNAME_RW"/"FNAME_R as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_RW"/"FNAME_R mode to 0444.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RW"/"FNAME_R, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_50634C72AABCB02C`](../../library/rules/ltp-50634c72aabcb02c.yaml) | The fixture sets DNAME_RX"/"FNAME_X mode to 0111.、The fixture creates DNAME_RX"/"FNAME_X as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_RX"/"FNAME_X, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_532669DC3463015A`](../../library/rules/ltp-532669dc3463015a.yaml) | The fixture sets FNAME_W mode to 0222.、The fixture creates FNAME_W as a regular file.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_W, R_OK|W_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_54E5F3DA585FF826`](../../library/rules/ltp-54e5f3da585ff826.yaml) | The fixture sets FNAME_R mode to 0444.、The fixture creates FNAME_R as a regular file.、The test invokes the syscall as root. | 调用 access(FNAME_R, R_OK|W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_557771AFA7D3CBA3`](../../library/rules/ltp-557771afa7d3cba3.yaml) | The fixture sets DNAME_RX"/"FNAME_W mode to 0222.、The fixture creates DNAME_RX"/"FNAME_W as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_RX"/"FNAME_W, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_56EB350905546953`](../../library/rules/ltp-56eb350905546953.yaml) | The fixture creates DNAME_X"/"FNAME_W as a regular file.、The fixture sets DNAME_X"/"FNAME_W mode to 0222.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_X"/"FNAME_W, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_579F2F9BF68FC287`](../../library/rules/ltp-579f2f9bf68fc287.yaml) | The fixture sets FNAME_X mode to 0111.、The fixture creates FNAME_X as a regular file.、The test invokes the syscall as root. | 调用 access(FNAME_X, R_OK|W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_5B429657B5297267`](../../library/rules/ltp-5b429657b5297267.yaml) | The fixture creates DNAME_WX"/"FNAME_X as a regular file.、The fixture sets DNAME_WX"/"FNAME_X mode to 0111.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_WX"/"FNAME_X, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_5DCAB1EE343F650B`](../../library/rules/ltp-5dcab1ee343f650b.yaml) | The fixture sets DNAME_RX"/"FNAME_X mode to 0111.、The fixture creates DNAME_RX"/"FNAME_X as a regular file.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RX"/"FNAME_X, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_5DCE40F2EE0477DD`](../../library/rules/ltp-5dce40f2ee0477dd.yaml) | The fixture creates DNAME_W"/"FNAME_W as a regular file.、The fixture sets DNAME_W"/"FNAME_W mode to 0222.、The test invokes the syscall as root. | 调用 access(DNAME_W"/"FNAME_W, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_5F1E8876185AED7D`](../../library/rules/ltp-5f1e8876185aed7d.yaml) | The fixture creates DNAME_RX"/"FNAME_R as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_RX"/"FNAME_R mode to 0444.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RX"/"FNAME_R, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_5FC4B14EE38910DA`](../../library/rules/ltp-5fc4b14ee38910da.yaml) | The fixture sets FNAME_W mode to 0222.、The fixture creates FNAME_W as a regular file.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_W, W_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_62CC9D9E2E3D7880`](../../library/rules/ltp-62cc9d9e2e3d7880.yaml) | The fixture sets DNAME_WX"/"FNAME_R mode to 0444.、The caller lacks a permission required by the operation.、The fixture creates DNAME_WX"/"FNAME_R as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_WX"/"FNAME_R, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_639CB00D5B06579C`](../../library/rules/ltp-639cb00d5b06579c.yaml) | The referenced path does not exist. | 调用 access(empty_fname, W_OK) | 返回 -1，errno 为 ENOENT |
| [`LTP_647D857E6AB3D942`](../../library/rules/ltp-647d857e6ab3d942.yaml) | The fixture creates FNAME_RWX as a regular file.、The fixture sets FNAME_RWX mode to 0777.、The test invokes the syscall as root. | 调用 access(FNAME_RWX, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_650C93999DB128D6`](../../library/rules/ltp-650c93999db128d6.yaml) | The fixture sets DNAME_WX"/"FNAME_R mode to 0444.、The caller lacks a permission required by the operation.、The fixture creates DNAME_WX"/"FNAME_R as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_WX"/"FNAME_R, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_6534585EC08425D6`](../../library/rules/ltp-6534585ec08425d6.yaml) | The fixture sets DNAME_W"/"FNAME_X mode to 0111.、The fixture creates DNAME_W"/"FNAME_X as a regular file.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_W"/"FNAME_X, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_68933230FCEAA7D5`](../../library/rules/ltp-68933230fceaa7d5.yaml) | The fixture creates DNAME_R"/"FNAME_W as a regular file.、The fixture sets DNAME_R"/"FNAME_W mode to 0222.、The test invokes the syscall as root. | 调用 access(DNAME_R"/"FNAME_W, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_6AAFFF4DD70E39E2`](../../library/rules/ltp-6aafff4dd70e39e2.yaml) | The fixture sets DNAME_RX"/"FNAME_W mode to 0222.、The fixture creates DNAME_RX"/"FNAME_W as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_RX"/"FNAME_W, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_6BBDEE6D1B9C6D94`](../../library/rules/ltp-6bbdee6d1b9c6d94.yaml) | The fixture creates DNAME_WX"/"FNAME_X as a regular file.、The fixture sets DNAME_WX"/"FNAME_X mode to 0111.、The test invokes the syscall as root. | 调用 access(DNAME_WX"/"FNAME_X, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_6C89FDE5BFD98590`](../../library/rules/ltp-6c89fde5bfd98590.yaml) | The fixture sets FNAME_W mode to 0222.、The fixture creates FNAME_W as a regular file.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_W, R_OK|W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_6D034F85A89B1FCF`](../../library/rules/ltp-6d034f85a89b1fcf.yaml) | The fixture creates DNAME_RX"/"FNAME_R as a regular file.、The fixture sets DNAME_RX"/"FNAME_R mode to 0444.、The test invokes the syscall as root. | 调用 access(DNAME_RX"/"FNAME_R, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_6D2D8585448FB760`](../../library/rules/ltp-6d2d8585448fb760.yaml) | The fixture sets DNAME_X"/"FNAME_X mode to 0111.、The fixture creates DNAME_X"/"FNAME_X as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_X"/"FNAME_X, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_6D74624C7ACACFFC`](../../library/rules/ltp-6d74624c7acacffc.yaml) | The fixture creates DNAME_WX"/"FNAME_X as a regular file.、The fixture sets DNAME_WX"/"FNAME_X mode to 0111.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_WX"/"FNAME_X, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_70A24E1D78959E54`](../../library/rules/ltp-70a24e1d78959e54.yaml) | The fixture sets DNAME_W"/"FNAME_X mode to 0111.、The fixture creates DNAME_W"/"FNAME_X as a regular file.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_W"/"FNAME_X, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_71C59FD029BDE7EC`](../../library/rules/ltp-71c59fd029bde7ec.yaml) | The fixture sets DNAME_RX"/"FNAME_X mode to 0111.、The fixture creates DNAME_RX"/"FNAME_X as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_RX"/"FNAME_X, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_72CB51010EB5642E`](../../library/rules/ltp-72cb51010eb5642e.yaml) | The fixture creates DNAME_W"/"FNAME_W as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_W"/"FNAME_W mode to 0222.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_W"/"FNAME_W, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_72CE32EF22E0AD18`](../../library/rules/ltp-72ce32ef22e0ad18.yaml) | The caller lacks a permission required by the operation.、The fixture sets DNAME_RX"/"FNAME_W mode to 0222.、The fixture creates DNAME_RX"/"FNAME_W as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_RX"/"FNAME_W, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_7516A82707F421A8`](../../library/rules/ltp-7516a82707f421a8.yaml) | The fixture creates DNAME_R"/"FNAME_R as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_R"/"FNAME_R mode to 0444.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_R"/"FNAME_R, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_762DED3BB55C0120`](../../library/rules/ltp-762ded3bb55c0120.yaml) | The fixture creates DNAME_W"/"FNAME_W as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_W"/"FNAME_W mode to 0222.、The test invokes the syscall as root. | 调用 access(DNAME_W"/"FNAME_W, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_765C6BC355EC57B9`](../../library/rules/ltp-765c6bc355ec57b9.yaml) | The fixture creates FNAME_RWX as a regular file.、The fixture sets FNAME_RWX mode to 0777.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_RWX, R_OK|W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_7886070B1C145E5B`](../../library/rules/ltp-7886070b1c145e5b.yaml) | The fixture creates DNAME_W"/"FNAME_R as a regular file.、The fixture sets DNAME_W"/"FNAME_R mode to 0444.、The test invokes the syscall as root. | 调用 access(DNAME_W"/"FNAME_R, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_78B9E649A9D3C278`](../../library/rules/ltp-78b9e649a9d3c278.yaml) | The fixture sets DNAME_X"/"FNAME_X mode to 0111.、The fixture creates DNAME_X"/"FNAME_X as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_X"/"FNAME_X, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_7DDD8970DD3DE57B`](../../library/rules/ltp-7ddd8970dd3de57b.yaml) | The fixture creates DNAME_RW"/"FNAME_X as a regular file.、The fixture sets DNAME_RW"/"FNAME_X mode to 0111.、The test invokes the syscall as root. | 调用 access(DNAME_RW"/"FNAME_X, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_804841A817CAA56C`](../../library/rules/ltp-804841a817caa56c.yaml) | The fixture sets FNAME_W mode to 0222.、The fixture creates FNAME_W as a regular file. | 调用 access(FNAME_W, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_82677662F036B4D3`](../../library/rules/ltp-82677662f036b4d3.yaml) | The fixture sets FNAME_R mode to 0444.、The fixture creates FNAME_R as a regular file. | 调用 access(FNAME_R, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_82E0F55AEC3D382F`](../../library/rules/ltp-82e0f55aec3d382f.yaml) | 无额外前置条件 | 调用 access(mnt_point, W_OK) | 返回 -1，errno 为 EROFS |
| [`LTP_832A284618144115`](../../library/rules/ltp-832a284618144115.yaml) | The fixture creates DNAME_R"/"FNAME_R as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_R"/"FNAME_R mode to 0444.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_R"/"FNAME_R, F_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_83A8BCF4DE700304`](../../library/rules/ltp-83a8bcf4de700304.yaml) | The fixture creates FNAME_X as a regular file.、The fixture sets FNAME_X mode to 0555. | 调用 access(FNAME_X, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_83EECC6B473A4EE0`](../../library/rules/ltp-83eecc6b473a4ee0.yaml) | The fixture creates DNAME_R"/"FNAME_W as a regular file.、The fixture sets DNAME_R"/"FNAME_W mode to 0222.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_R"/"FNAME_W, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_85A46F77356C5F87`](../../library/rules/ltp-85a46f77356c5f87.yaml) | The fixture sets DNAME_RX"/"FNAME_X mode to 0111.、The fixture creates DNAME_RX"/"FNAME_X as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_RX"/"FNAME_X, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_85C6DC212C979199`](../../library/rules/ltp-85c6dc212c979199.yaml) | The fixture creates FNAME_RWX as a regular file.、The fixture sets FNAME_RWX mode to 0777.、The test invokes the syscall as root. | 调用 access(FNAME_RWX, R_OK|W_OK|X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_85DC9A2EA2A956D8`](../../library/rules/ltp-85dc9a2ea2a956d8.yaml) | The userspace pointer is outside accessible memory. | 调用 access((void *)-1, X_OK) | 返回 -1，errno 为 EFAULT |
| [`LTP_86F208D4521003A5`](../../library/rules/ltp-86f208d4521003a5.yaml) | The fixture creates DNAME_X"/"FNAME_W as a regular file.、The fixture sets DNAME_X"/"FNAME_W mode to 0222.、The caller lacks a permission required by the operation.、The test invokes the syscall as root. | 调用 access(DNAME_X"/"FNAME_W, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_88E657C0C8F3084A`](../../library/rules/ltp-88e657c0c8f3084a.yaml) | The fixture creates DNAME_RX"/"FNAME_R as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_RX"/"FNAME_R mode to 0444.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RX"/"FNAME_R, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_896519C6DE4DC296`](../../library/rules/ltp-896519c6de4dc296.yaml) | The fixture sets DNAME_RX"/"FNAME_X mode to 0111.、The fixture creates DNAME_RX"/"FNAME_X as a regular file.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RX"/"FNAME_X, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_8CCE8FA5BFCCA106`](../../library/rules/ltp-8cce8fa5bfcca106.yaml) | The fixture creates DNAME_RW"/"FNAME_W as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_RW"/"FNAME_W mode to 0222.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RW"/"FNAME_W, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_8D75172B4EFCA5AB`](../../library/rules/ltp-8d75172b4efca5ab.yaml) | The fixture creates DNAME_W"/"FNAME_W as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_W"/"FNAME_W mode to 0222.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_W"/"FNAME_W, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_8E4283FE2952D57B`](../../library/rules/ltp-8e4283fe2952d57b.yaml) | The fixture sets DNAME_W"/"FNAME_X mode to 0111.、The fixture creates DNAME_W"/"FNAME_X as a regular file.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_W"/"FNAME_X, F_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_8E8D0AAC302EAE64`](../../library/rules/ltp-8e8d0aac302eae64.yaml) | The fixture sets DNAME_WX"/"FNAME_W mode to 0222.、The fixture creates DNAME_WX"/"FNAME_W as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_WX"/"FNAME_W, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_8EBCB5DB4F08A9DD`](../../library/rules/ltp-8ebcb5db4f08a9dd.yaml) | The fixture sets FNAME_R mode to 0444.、The caller lacks a permission required by the operation.、The fixture creates FNAME_R as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_R, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_8EEF6B34A8A62DDA`](../../library/rules/ltp-8eef6b34a8a62dda.yaml) | The fixture creates DNAME_W"/"FNAME_W as a regular file.、The fixture sets DNAME_W"/"FNAME_W mode to 0222.、The test invokes the syscall as root. | 调用 access(DNAME_W"/"FNAME_W, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_8F0EEAFC8315D3BC`](../../library/rules/ltp-8f0eeafc8315d3bc.yaml) | The fixture sets DNAME_WX"/"FNAME_W mode to 0222.、The fixture creates DNAME_WX"/"FNAME_W as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_WX"/"FNAME_W, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_910B0D26D7722DBE`](../../library/rules/ltp-910b0d26d7722dbe.yaml) | The caller lacks a permission required by the operation.、The fixture sets FNAME_X mode to 0111.、The fixture creates FNAME_X as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_X, R_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_9116D4EE494E16DA`](../../library/rules/ltp-9116d4ee494e16da.yaml) | The caller lacks a permission required by the operation.、The fixture creates DNAME_WX"/"FNAME_X as a regular file.、The fixture sets DNAME_WX"/"FNAME_X mode to 0111.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_WX"/"FNAME_X, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_91FBCF218DE6C917`](../../library/rules/ltp-91fbcf218de6c917.yaml) | The fixture sets DNAME_W"/"FNAME_X mode to 0111.、The fixture creates DNAME_W"/"FNAME_X as a regular file.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_W"/"FNAME_X, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_922E84FFC658D432`](../../library/rules/ltp-922e84ffc658d432.yaml) | The fixture sets FNAME_X mode to 0111.、The fixture creates FNAME_X as a regular file.、The test invokes the syscall as root. | 调用 access(FNAME_X, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_92652DA4B873A330`](../../library/rules/ltp-92652da4b873a330.yaml) | The fixture sets FNAME_R mode to 0444.、The fixture creates FNAME_R as a regular file.、The test invokes the syscall as root. | 调用 access(FNAME_R, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_9403699F671CF95F`](../../library/rules/ltp-9403699f671cf95f.yaml) | The fixture creates DNAME_R"/"FNAME_W as a regular file.、The fixture sets DNAME_R"/"FNAME_W mode to 0222.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_R"/"FNAME_W, F_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_96B52F0F7B6F6E00`](../../library/rules/ltp-96b52f0f7b6f6e00.yaml) | The fixture sets FNAME_R mode to 0444.、The caller lacks a permission required by the operation.、The fixture creates FNAME_R as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_R, R_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_96B67F0F28B0192F`](../../library/rules/ltp-96b67f0f28b0192f.yaml) | The fixture creates DNAME_RW"/"FNAME_X as a regular file.、The fixture sets DNAME_RW"/"FNAME_X mode to 0111.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RW"/"FNAME_X, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_96E9B8F051D51566`](../../library/rules/ltp-96e9b8f051d51566.yaml) | The fixture creates DNAME_RW"/"FNAME_R as a regular file.、The fixture sets DNAME_RW"/"FNAME_R mode to 0444.、The test invokes the syscall as root. | 调用 access(DNAME_RW"/"FNAME_R, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_97C6508AAB3F5CF3`](../../library/rules/ltp-97c6508aab3f5cf3.yaml) | The caller lacks a permission required by the operation.、The fixture sets FNAME_X mode to 0111.、The fixture creates FNAME_X as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_X, W_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_989BADB4E671AAC2`](../../library/rules/ltp-989badb4e671aac2.yaml) | The fixture sets DNAME_X"/"FNAME_X mode to 0111.、The fixture creates DNAME_X"/"FNAME_X as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_X"/"FNAME_X, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_9951A69B869BED04`](../../library/rules/ltp-9951a69b869bed04.yaml) | The fixture sets DNAME_W"/"FNAME_X mode to 0111.、The fixture creates DNAME_W"/"FNAME_X as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_W"/"FNAME_X, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_99C641DE1B23D6C1`](../../library/rules/ltp-99c641de1b23d6c1.yaml) | The fixture sets DNAME_X"/"FNAME_R mode to 0444.、The fixture creates DNAME_X"/"FNAME_R as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_X"/"FNAME_R, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_9AA9FA96C34FAB9E`](../../library/rules/ltp-9aa9fa96c34fab9e.yaml) | The caller lacks a permission required by the operation.、The fixture sets DNAME_RX"/"FNAME_W mode to 0222.、The fixture creates DNAME_RX"/"FNAME_W as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RX"/"FNAME_W, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_9BA35A8C11698D49`](../../library/rules/ltp-9ba35a8c11698d49.yaml) | The fixture creates DNAME_R"/"FNAME_X as a regular file.、The fixture sets DNAME_R"/"FNAME_X mode to 0111.、The test invokes the syscall as root. | 调用 access(DNAME_R"/"FNAME_X, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_9F4ADF825E143585`](../../library/rules/ltp-9f4adf825e143585.yaml) | The fixture creates SNAME_W as a symbolic link. | 调用 access(SNAME_W, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_9F5D09B41AC183E5`](../../library/rules/ltp-9f5d09b41ac183e5.yaml) | The fixture sets DNAME_WX"/"FNAME_W mode to 0222.、The caller lacks a permission required by the operation.、The fixture creates DNAME_WX"/"FNAME_W as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_WX"/"FNAME_W, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_9FC3886A5E9A0CDF`](../../library/rules/ltp-9fc3886a5e9a0cdf.yaml) | The fixture sets DNAME_X"/"FNAME_R mode to 0444.、The fixture creates DNAME_X"/"FNAME_R as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_X"/"FNAME_R, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_A0CEB16379D94371`](../../library/rules/ltp-a0ceb16379d94371.yaml) | The fixture sets DNAME_WX"/"FNAME_R mode to 0444.、The fixture creates DNAME_WX"/"FNAME_R as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_WX"/"FNAME_R, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_A1024CD742C433A3`](../../library/rules/ltp-a1024cd742c433a3.yaml) | The fixture creates DNAME_WX"/"FNAME_X as a regular file.、The fixture sets DNAME_WX"/"FNAME_X mode to 0111.、The test invokes the syscall as root. | 调用 access(DNAME_WX"/"FNAME_X, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_A49D802FF404EADA`](../../library/rules/ltp-a49d802ff404eada.yaml) | The fixture creates DNAME_R"/"FNAME_W as a regular file.、The fixture sets DNAME_R"/"FNAME_W mode to 0222.、The caller lacks a permission required by the operation.、The test invokes the syscall as root. | 调用 access(DNAME_R"/"FNAME_W, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_A684365768862744`](../../library/rules/ltp-a684365768862744.yaml) | The fixture creates DNAME_R"/"FNAME_X as a regular file.、The fixture sets DNAME_R"/"FNAME_X mode to 0111.、The test invokes the syscall as root. | 调用 access(DNAME_R"/"FNAME_X, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_A7D8EAF1CE0F1A9B`](../../library/rules/ltp-a7d8eaf1ce0f1a9b.yaml) | The fixture sets FNAME_W mode to 0222.、The fixture creates FNAME_W as a regular file.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_W, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_A9833E2E2860A6B7`](../../library/rules/ltp-a9833e2e2860a6b7.yaml) | The fixture creates DNAME_R"/"FNAME_W as a regular file.、The fixture sets DNAME_R"/"FNAME_W mode to 0222.、The test invokes the syscall as root. | 调用 access(DNAME_R"/"FNAME_W, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_A9A7BAA6186D57BD`](../../library/rules/ltp-a9a7baa6186d57bd.yaml) | The fixture sets DNAME_RX"/"FNAME_W mode to 0222.、The fixture creates DNAME_RX"/"FNAME_W as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_RX"/"FNAME_W, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_AA8CF336E764C8A7`](../../library/rules/ltp-aa8cf336e764c8a7.yaml) | The fixture creates FNAME_RWX as a regular file.、The fixture sets FNAME_RWX mode to 0777.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_RWX, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_AA8D903F4610FB06`](../../library/rules/ltp-aa8d903f4610fb06.yaml) | The fixture creates DNAME_R"/"FNAME_W as a regular file.、The fixture sets DNAME_R"/"FNAME_W mode to 0222.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_R"/"FNAME_W, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_AB8173921096C9EE`](../../library/rules/ltp-ab8173921096c9ee.yaml) | The caller lacks a permission required by the operation.、The fixture creates DNAME_WX"/"FNAME_X as a regular file.、The fixture sets DNAME_WX"/"FNAME_X mode to 0111.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_WX"/"FNAME_X, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_ABCBF7DF0ADCB22A`](../../library/rules/ltp-abcbf7df0adcb22a.yaml) | The fixture sets DNAME_WX"/"FNAME_R mode to 0444.、The fixture creates DNAME_WX"/"FNAME_R as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_WX"/"FNAME_R, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_AC02B3D548635386`](../../library/rules/ltp-ac02b3d548635386.yaml) | The fixture sets FNAME_R mode to 0444.、The fixture creates FNAME_R as a regular file.、The test invokes the syscall as root. | 调用 access(FNAME_R, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_AE66ABEA9F76F42F`](../../library/rules/ltp-ae66abea9f76f42f.yaml) | The fixture creates FNAME_RWX as a regular file.、The fixture sets FNAME_RWX mode to 0777.、The test invokes the syscall as root. | 调用 access(FNAME_RWX, W_OK|X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_AF528A39B115F13D`](../../library/rules/ltp-af528a39b115f13d.yaml) | The fixture creates DNAME_W"/"FNAME_W as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_W"/"FNAME_W mode to 0222.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_W"/"FNAME_W, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_B1E03AECF1FB1196`](../../library/rules/ltp-b1e03aecf1fb1196.yaml) | The fixture sets FNAME_X mode to 0111.、The fixture creates FNAME_X as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_X, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_B35AB626F46D66FB`](../../library/rules/ltp-b35ab626f46d66fb.yaml) | The fixture creates DNAME_RW"/"FNAME_R as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_RW"/"FNAME_R mode to 0444.、The test invokes the syscall as root. | 调用 access(DNAME_RW"/"FNAME_R, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_B39DB8E167298745`](../../library/rules/ltp-b39db8e167298745.yaml) | The fixture creates DNAME_RW"/"FNAME_W as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_RW"/"FNAME_W mode to 0222.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RW"/"FNAME_W, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_B54A4B6E6A4ABDD5`](../../library/rules/ltp-b54a4b6e6a4abdd5.yaml) | The fixture sets FNAME_R mode to 0444.、The caller lacks a permission required by the operation.、The fixture creates FNAME_R as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_R, W_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_B5BC41E30C9E37B0`](../../library/rules/ltp-b5bc41e30c9e37b0.yaml) | The fixture creates DNAME_R"/"FNAME_W as a regular file.、The fixture sets DNAME_R"/"FNAME_W mode to 0222.、The test invokes the syscall as root. | 调用 access(DNAME_R"/"FNAME_W, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_B6FE6370B024CFB8`](../../library/rules/ltp-b6fe6370b024cfb8.yaml) | The fixture creates SNAME_F as a symbolic link. | 调用 access(SNAME_F, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_B87A5B8BC5B062AA`](../../library/rules/ltp-b87a5b8bc5b062aa.yaml) | The fixture sets DNAME_WX"/"FNAME_W mode to 0222.、The caller lacks a permission required by the operation.、The fixture creates DNAME_WX"/"FNAME_W as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_WX"/"FNAME_W, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_BB1FF3530CCDDBB3`](../../library/rules/ltp-bb1ff3530ccddbb3.yaml) | The fixture creates DNAME_R"/"FNAME_W as a regular file.、The fixture sets DNAME_R"/"FNAME_W mode to 0222.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_R"/"FNAME_W, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_BBDCACF4AE2FEB1D`](../../library/rules/ltp-bbdcacf4ae2feb1d.yaml) | The fixture creates DNAME_WX"/"FNAME_X as a regular file.、The fixture sets DNAME_WX"/"FNAME_X mode to 0111.、The test invokes the syscall as root. | 调用 access(DNAME_WX"/"FNAME_X, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_BCC58FBC10C684E2`](../../library/rules/ltp-bcc58fbc10c684e2.yaml) | The userspace pointer is outside accessible memory. | 调用 access((void *)-1, W_OK) | 返回 -1，errno 为 EFAULT |
| [`LTP_BCF478535204545E`](../../library/rules/ltp-bcf478535204545e.yaml) | The fixture creates DNAME_RW"/"FNAME_W as a regular file.、The fixture sets DNAME_RW"/"FNAME_W mode to 0222.、The test invokes the syscall as root. | 调用 access(DNAME_RW"/"FNAME_W, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_BF3532E2FF5C89A0`](../../library/rules/ltp-bf3532e2ff5c89a0.yaml) | The fixture creates SNAME_X as a symbolic link. | 调用 access(SNAME_X, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_BF696EFB140C9DAF`](../../library/rules/ltp-bf696efb140c9daf.yaml) | The fixture sets FNAME_R mode to 0444.、The caller lacks a permission required by the operation.、The fixture creates FNAME_R as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_R, R_OK|W_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_C1D8DC20331CC18C`](../../library/rules/ltp-c1d8dc20331cc18c.yaml) | The fixture creates DNAME_W"/"FNAME_W as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_W"/"FNAME_W mode to 0222.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_W"/"FNAME_W, F_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_C3FF5FE7F694FFE6`](../../library/rules/ltp-c3ff5fe7f694ffe6.yaml) | The fixture creates DNAME_X"/"FNAME_W as a regular file.、The fixture sets DNAME_X"/"FNAME_W mode to 0222.、The test invokes the syscall as root. | 调用 access(DNAME_X"/"FNAME_W, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_C477F05C84F3C00D`](../../library/rules/ltp-c477f05c84f3c00d.yaml) | The fixture creates DNAME_X"/"FNAME_W as a regular file.、The fixture sets DNAME_X"/"FNAME_W mode to 0222.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_X"/"FNAME_W, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_C5088C2E9DB5306A`](../../library/rules/ltp-c5088c2e9db5306a.yaml) | The fixture creates FNAME_RWX as a regular file.、The fixture sets FNAME_RWX mode to 0777.、The test invokes the syscall as root. | 调用 access(FNAME_RWX, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_C622170DA67BA6E3`](../../library/rules/ltp-c622170da67ba6e3.yaml) | The fixture sets DNAME_W"/"FNAME_X mode to 0111.、The fixture creates DNAME_W"/"FNAME_X as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_W"/"FNAME_X, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_C7C0FBBB9024C112`](../../library/rules/ltp-c7c0fbbb9024c112.yaml) | The fixture creates DNAME_RW"/"FNAME_W as a regular file.、The fixture sets DNAME_RW"/"FNAME_W mode to 0222.、The test invokes the syscall as root. | 调用 access(DNAME_RW"/"FNAME_W, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_CC6A74384D72A70D`](../../library/rules/ltp-cc6a74384d72a70d.yaml) | The caller lacks a permission required by the operation.、The fixture sets DNAME_X"/"FNAME_R mode to 0444.、The fixture creates DNAME_X"/"FNAME_R as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_X"/"FNAME_R, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_CD06BB76866E1C4F`](../../library/rules/ltp-cd06bb76866e1c4f.yaml) | The fixture creates FNAME_RWX as a regular file.、The fixture sets FNAME_RWX mode to 0777.、The test invokes the syscall as root. | 调用 access(FNAME_RWX, R_OK|W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_CDDBF220A7C01FEA`](../../library/rules/ltp-cddbf220a7c01fea.yaml) | The fixture creates DNAME_R"/"FNAME_X as a regular file.、The fixture sets DNAME_R"/"FNAME_X mode to 0111.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_R"/"FNAME_X, F_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_D0578B9D5D177037`](../../library/rules/ltp-d0578b9d5d177037.yaml) | The fixture sets FNAME_R mode to 0444.、The caller lacks a permission required by the operation.、The fixture creates FNAME_R as a regular file.、The test invokes the syscall as root. | 调用 access(FNAME_R, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_D071740A6BE2DE31`](../../library/rules/ltp-d071740a6be2de31.yaml) | The fixture sets DNAME_X"/"FNAME_R mode to 0444.、The fixture creates DNAME_X"/"FNAME_R as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_X"/"FNAME_R, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_D1DE0D497F2B612D`](../../library/rules/ltp-d1de0d497f2b612d.yaml) | The fixture sets FNAME_W mode to 0222.、The fixture creates FNAME_W as a regular file.、The test invokes the syscall as root. | 调用 access(FNAME_W, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_D3B68F2DFB1C45D5`](../../library/rules/ltp-d3b68f2dfb1c45d5.yaml) | The fixture creates DNAME_R"/"FNAME_X as a regular file.、The fixture sets DNAME_R"/"FNAME_X mode to 0111.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_R"/"FNAME_X, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_D696A4996FBE61CF`](../../library/rules/ltp-d696a4996fbe61cf.yaml) | The fixture sets FNAME_R mode to 0444.、The fixture creates FNAME_R as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_R, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_D8D1EEF145FEB5EA`](../../library/rules/ltp-d8d1eef145feb5ea.yaml) | The caller lacks a permission required by the operation.、The fixture sets FNAME_X mode to 0111.、The fixture creates FNAME_X as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_X, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_DC994CB22DEE5DE8`](../../library/rules/ltp-dc994cb22dee5de8.yaml) | The fixture creates DNAME_RW"/"FNAME_W as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_RW"/"FNAME_W mode to 0222.、The test invokes the syscall as root. | 调用 access(DNAME_RW"/"FNAME_W, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_DCAED55A4DA05C29`](../../library/rules/ltp-dcaed55a4da05c29.yaml) | The fixture creates DNAME_RX"/"FNAME_R as a regular file.、The fixture sets DNAME_RX"/"FNAME_R mode to 0444.、The test invokes the syscall as root. | 调用 access(DNAME_RX"/"FNAME_R, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_DD70936BEB737A0F`](../../library/rules/ltp-dd70936beb737a0f.yaml) | The fixture creates DNAME_WX"/"FNAME_X as a regular file.、The fixture sets DNAME_WX"/"FNAME_X mode to 0111.、The test invokes the syscall as root. | 调用 access(DNAME_WX"/"FNAME_X, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_DEF59E8529DC9CD8`](../../library/rules/ltp-def59e8529dc9cd8.yaml) | The fixture creates DNAME_RX"/"FNAME_R as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_RX"/"FNAME_R mode to 0444.、The test invokes the syscall as root. | 调用 access(DNAME_RX"/"FNAME_R, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_E0F28EAB0253204C`](../../library/rules/ltp-e0f28eab0253204c.yaml) | The fixture sets DNAME_WX"/"FNAME_R mode to 0444.、The caller lacks a permission required by the operation.、The fixture creates DNAME_WX"/"FNAME_R as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_WX"/"FNAME_R, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_E2D7E49A9D6EDA47`](../../library/rules/ltp-e2d7e49a9d6eda47.yaml) | The fixture sets FNAME_W mode to 0222.、The fixture creates FNAME_W as a regular file.、The test invokes the syscall as root. | 调用 access(FNAME_W, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_E86DBD8C9AA9E82B`](../../library/rules/ltp-e86dbd8c9aa9e82b.yaml) | The fixture sets FNAME_R mode to 0444.、The caller lacks a permission required by the operation.、The fixture creates FNAME_R as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_R, R_OK|W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_E8D2C5525DC42DD1`](../../library/rules/ltp-e8d2c5525dc42dd1.yaml) | Path resolution encounters a symlink loop. | 调用 access(sname1, R_OK) | 返回 -1，errno 为 ELOOP |
| [`LTP_E9EC00862545876A`](../../library/rules/ltp-e9ec00862545876a.yaml) | The fixture sets DNAME_WX"/"FNAME_W mode to 0222.、The fixture creates DNAME_WX"/"FNAME_W as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_WX"/"FNAME_W, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_EA51441DF7A43596`](../../library/rules/ltp-ea51441df7a43596.yaml) | The fixture creates DNAME_W"/"FNAME_R as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_W"/"FNAME_R mode to 0444.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_W"/"FNAME_R, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_EDE65A5D9B99F21F`](../../library/rules/ltp-ede65a5d9b99f21f.yaml) | The caller lacks a permission required by the operation.、The fixture sets DNAME_X"/"FNAME_R mode to 0444.、The fixture creates DNAME_X"/"FNAME_R as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_X"/"FNAME_R, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_EECDB5C492A4B4BD`](../../library/rules/ltp-eecdb5c492a4b4bd.yaml) | The caller lacks a permission required by the operation.、The fixture sets DNAME_RX"/"FNAME_W mode to 0222.、The fixture creates DNAME_RX"/"FNAME_W as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RX"/"FNAME_W, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_EFF3EDE1EC749DE9`](../../library/rules/ltp-eff3ede1ec749de9.yaml) | The fixture sets DNAME_WX"/"FNAME_R mode to 0444.、The fixture creates DNAME_WX"/"FNAME_R as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_WX"/"FNAME_R, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_F02D3365DCF08927`](../../library/rules/ltp-f02d3365dcf08927.yaml) | The fixture creates DNAME_RW"/"FNAME_R as a regular file.、The caller lacks a permission required by the operation.、The fixture sets DNAME_RW"/"FNAME_R mode to 0444.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RW"/"FNAME_R, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_F26D09CAE258516C`](../../library/rules/ltp-f26d09cae258516c.yaml) | The fixture creates DNAME_R"/"FNAME_R as a regular file.、The fixture sets DNAME_R"/"FNAME_R mode to 0444.、The test invokes the syscall as root. | 调用 access(DNAME_R"/"FNAME_R, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_F4AE08B0C5A16088`](../../library/rules/ltp-f4ae08b0c5a16088.yaml) | The fixture sets FNAME_W mode to 0222.、The fixture creates FNAME_W as a regular file.、The caller lacks a permission required by the operation.、The test invokes the syscall as root. | 调用 access(FNAME_W, W_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_F4FEC29E9271B119`](../../library/rules/ltp-f4fec29e9271b119.yaml) | The fixture sets FNAME_W mode to 0222.、The fixture creates FNAME_W as a regular file.、The caller lacks a permission required by the operation.、The test invokes the syscall as root. | 调用 access(FNAME_W, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_F508E2594C0F3DC9`](../../library/rules/ltp-f508e2594c0f3dc9.yaml) | The fixture sets DNAME_RX"/"FNAME_X mode to 0111.、The fixture creates DNAME_RX"/"FNAME_X as a regular file.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RX"/"FNAME_X, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_FAB12DCB20BF08A2`](../../library/rules/ltp-fab12dcb20bf08a2.yaml) | The fixture creates FNAME_RWX as a regular file.、The fixture sets FNAME_RWX mode to 0777.、The test drops privileges and invokes the syscall as nobody. | 调用 access(FNAME_RWX, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_FB7250E0E0E98949`](../../library/rules/ltp-fb7250e0e0e98949.yaml) | The fixture sets DNAME_X"/"FNAME_R mode to 0444.、The fixture creates DNAME_X"/"FNAME_R as a regular file.、The test invokes the syscall as root. | 调用 access(DNAME_X"/"FNAME_R, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_FC5D8C19ECDBC380`](../../library/rules/ltp-fc5d8c19ecdbc380.yaml) | The fixture creates DNAME_RW"/"FNAME_X as a regular file.、The fixture sets DNAME_RW"/"FNAME_X mode to 0111.、The caller lacks a permission required by the operation.、The test drops privileges and invokes the syscall as nobody. | 调用 access(DNAME_RW"/"FNAME_X, W_OK) | 返回 -1，errno 为 EACCES |
## `acct`

没有形成可发布的合规性规则。

## `add_key`

没有形成可发布的合规性规则。

## `adjtimex`

没有形成可发布的合规性规则。

## `alarm`

共形成 6 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_3E8DA9E014B82702`](../../library/rules/ltp-3e8da9e014b82702.yaml) | 无额外前置条件 | 调用 alarm(10) | 调用成功，返回 SUCCESS |
| [`LTP_65B70356F06E31F8`](../../library/rules/ltp-65b70356f06e31f8.yaml) | 无额外前置条件 | 调用 alarm(UINT_MAX/2) | 调用成功，返回 SUCCESS |
| [`LTP_76A9B6CF388A8609`](../../library/rules/ltp-76a9b6cf388a8609.yaml) | 无额外前置条件 | 调用 alarm(UINT_MAX/4) | 调用成功，返回 SUCCESS |
| [`LTP_98EC66149EE68933`](../../library/rules/ltp-98ec66149ee68933.yaml) | 无额外前置条件 | 调用 alarm(2) | 调用成功，返回 SUCCESS |
| [`LTP_B7A341967DF2BD69`](../../library/rules/ltp-b7a341967df2bd69.yaml) | 无额外前置条件 | 调用 alarm(100) | 调用成功，返回 SUCCESS |
| [`LTP_C785774773FB7524`](../../library/rules/ltp-c785774773fb7524.yaml) | 无额外前置条件 | 调用 alarm(INT_MAX) | 调用成功，返回 SUCCESS |
## `arch_prctl`

没有形成可发布的合规性规则。

## `bind`

没有形成可发布的合规性规则。

## `bpf`

没有形成可发布的合规性规则。

## `brk`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_7A74A699442CEB99`](../../library/rules/ltp-7a74a699442ceb99.yaml) | 无额外前置条件 | 调用 brk(new_brk) | 调用成功，返回 SUCCESS |
| [`LTP_E3E59B16A96A60BC`](../../library/rules/ltp-e3e59b16a96a60bc.yaml) | 无额外前置条件 | 调用 brk(addr) | 调用成功，返回 SUCCESS |
## `cacheflush`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_8AD8032754BC8842`](../../library/rules/ltp-8ad8032754bc8842.yaml) | 无额外前置条件 | 调用 cacheflush(addr, getpagesize(), CACHE_DESC(ICACHE)) | 调用成功，返回 SUCCESS |
| [`LTP_C218D3CB0AD80D90`](../../library/rules/ltp-c218d3cb0ad80d90.yaml) | 无额外前置条件 | 调用 cacheflush(addr, getpagesize(), CACHE_DESC(BCACHE)) | 调用成功，返回 SUCCESS |
| [`LTP_D579FCFC71E6EB6A`](../../library/rules/ltp-d579fcfc71e6eb6a.yaml) | 无额外前置条件 | 调用 cacheflush(addr, getpagesize(), CACHE_DESC(DCACHE)) | 调用成功，返回 SUCCESS |
## `cachestat`

共形成 6 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_1325C077A1CDE514`](../../library/rules/ltp-1325c077a1cde514.yaml) | 无额外前置条件 | 调用 cachestat(fd, cs_range, cs, 0) | 调用成功，返回 SUCCESS |
| [`LTP_2722827BC58E04CD`](../../library/rules/ltp-2722827bc58e04cd.yaml) | The userspace pointer is outside accessible memory. | 调用 cachestat(fd, cs_range_null, cs, 0) | 返回 -1，errno 为 EFAULT |
| [`LTP_2D0446746669D31E`](../../library/rules/ltp-2d0446746669d31e.yaml) | The userspace pointer is outside accessible memory. | 调用 cachestat(fd, cs_range, cs_null, 0) | 返回 -1，errno 为 EFAULT |
| [`LTP_34EC9FB9C9551214`](../../library/rules/ltp-34ec9fb9c9551214.yaml) | 无额外前置条件 | 调用 cachestat(invalid_fd, cs_range, cs, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_BA9A8FE901467960`](../../library/rules/ltp-ba9a8fe901467960.yaml) | 无额外前置条件 | 调用 cachestat(fd_hugepage, cs_range, cs, 0) | 返回 -1，errno 为 EOPNOTSUPP |
| [`LTP_EB646AEB1D23725B`](../../library/rules/ltp-eb646aeb1d23725b.yaml) | The file descriptor is invalid. | 调用 cachestat(fd, cs_range, cs, -1) | 返回 -1，errno 为 EINVAL |
## `capget`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_208C833FF12217F5`](../../library/rules/ltp-208c833ff12217f5.yaml) | 无额外前置条件 | 调用 capget(hdr, data) | 调用成功，返回 SUCCESS |
## `capset`

没有形成可发布的合规性规则。

## `chdir`

没有形成可发布的合规性规则。

## `chmod`

没有形成可发布的合规性规则。

## `chown`

没有形成可发布的合规性规则。

## `chroot`

共形成 6 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_07CB582EDCDF46C6`](../../library/rules/ltp-07cb582edcdf46c6.yaml) | The fixture sets TEST_TMPDIR mode to 0222.、The fixture creates TEST_TMPDIR as a directory.、The caller lacks a permission required by the operation. | 调用 chroot(TEST_TMPDIR) | 返回 -1，errno 为 EACCES |
| [`LTP_701679DC8AD1E4FE`](../../library/rules/ltp-701679dc8ad1e4fe.yaml) | The referenced path does not exist. | 调用 chroot(nonexistent_dir) | 返回 -1，errno 为 ENOENT |
| [`LTP_726A6A667C79F568`](../../library/rules/ltp-726a6a667c79f568.yaml) | Path resolution encounters a symlink loop. | 调用 chroot(loop_dir) | 返回 -1，errno 为 ELOOP |
| [`LTP_938E8BF5D2E7106E`](../../library/rules/ltp-938e8bf5d2e7106e.yaml) | The userspace pointer is outside accessible memory. | 调用 chroot(bad_ptr) | 返回 -1，errno 为 EFAULT |
| [`LTP_9F51EEE16C61FFB8`](../../library/rules/ltp-9f51eee16c61ffb8.yaml) | The pathname exceeds the supported limit. | 调用 chroot(longname_dir) | 返回 -1，errno 为 ENAMETOOLONG |
| [`LTP_D8BB97A8EDA10C0B`](../../library/rules/ltp-d8bb97a8eda10c0b.yaml) | A path component that must be a directory is not a directory. | 调用 chroot(file_name) | 返回 -1，errno 为 ENOTDIR |
## `clock_adjtime`

没有形成可发布的合规性规则。

## `clock_getres`

没有形成可发布的合规性规则。

## `clock_gettime`

没有形成可发布的合规性规则。

## `clock_nanosleep`

没有形成可发布的合规性规则。

## `clock_settime`

没有形成可发布的合规性规则。

## `clone`

没有形成可发布的合规性规则。

## `clone3`

没有形成可发布的合规性规则。

## `close`

共形成 5 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_09B39E9C9254ECB2`](../../library/rules/ltp-09b39e9c9254ecb2.yaml) | 文件描述符已经关闭 | 调用 close(fd_closed) | 返回 -1，errno 为 EBADF |
| [`LTP_2BDE60C0E64B4DC8`](../../library/rules/ltp-2bde60c0e64b4dc8.yaml) | 无额外前置条件 | 调用 close(get_fd_pipe()) | 调用成功，返回 SUCCESS |
| [`LTP_7E3E96A4962D78D4`](../../library/rules/ltp-7e3e96a4962d78d4.yaml) | The file descriptor is invalid. | 调用 close(fd_invalid) | 返回 -1，errno 为 EBADF |
| [`LTP_BF2428964ADD116F`](../../library/rules/ltp-bf2428964add116f.yaml) | 无额外前置条件 | 调用 close(get_fd_file()) | 调用成功，返回 SUCCESS |
| [`LTP_E520E500AB3AE851`](../../library/rules/ltp-e520e500ab3ae851.yaml) | 无额外前置条件 | 调用 close(get_fd_socket()) | 调用成功，返回 SUCCESS |
## `close_range`

共形成 6 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_31D9D767D6888DDA`](../../library/rules/ltp-31d9d767d6888dda.yaml) | 无额外前置条件 | 调用 close_range(fd, fd, flags) | 返回 -1，errno 为 EINVAL |
| [`LTP_425E5A3502541DE8`](../../library/rules/ltp-425e5a3502541de8.yaml) | 无额外前置条件 | 调用 close_range(~0U, ~0U, 0) | 调用成功，返回 SUCCESS |
| [`LTP_76BFF56F735A0074`](../../library/rules/ltp-76bff56f735a0074.yaml) | 无额外前置条件 | 调用 close_range(fd, 100, 0) | 调用成功，返回 SUCCESS |
| [`LTP_CBF4B6C8A1458A28`](../../library/rules/ltp-cbf4b6c8a1458a28.yaml) | 无额外前置条件 | 调用 close_range(3, ~0U, ~0U) | 返回 -1，errno 为 EINVAL |
| [`LTP_F1DC44813DCA6A05`](../../library/rules/ltp-f1dc44813dca6a05.yaml) | 无额外前置条件 | 调用 close_range(4, 3, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_F4DE81D703447628`](../../library/rules/ltp-f4de81d703447628.yaml) | 无额外前置条件 | 调用 close_range(fd, fd, 0) | 调用成功，返回 SUCCESS |
## `cma`

没有形成可发布的合规性规则。

## `confstr`

没有形成可发布的合规性规则。

## `connect`

没有形成可发布的合规性规则。

## `copy_file_range`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_76D3B1710474AAC2`](../../library/rules/ltp-76d3b1710474aac2.yaml) | 无额外前置条件 | 调用 copy_file_range(fd_in, off_new_in, fd_out, off_new_out, to_copy, 0) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_DB6066C00D231BA4`](../../library/rules/ltp-db6066c00d231ba4.yaml) | 无额外前置条件 | 调用 copy_file_range(fd_src, &offset, fd_dest, 0, CONTSIZE, 0) | {'kind': 'return_value', 'return': '-1'} |
## `creat`

没有形成可发布的合规性规则。

## `delete_module`

没有形成可发布的合规性规则。

## `dup`

共形成 5 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_2553A6069EE908FB`](../../library/rules/ltp-2553a6069ee908fb.yaml) | The file descriptor is invalid. | 调用 dup(-1) | 返回 -1，errno 为 EBADF |
| [`LTP_511185D6DE2A63A0`](../../library/rules/ltp-511185d6de2a63a0.yaml) | 无额外前置条件 | 调用 dup(1500) | 返回 -1，errno 为 EBADF |
| [`LTP_84DBE108A850E845`](../../library/rules/ltp-84dbe108a850e845.yaml) | 无额外前置条件 | 调用 dup(fd[1]) | {'kind': 'return_fd', 'return': 'FD'} |
| [`LTP_A774FC10727E8ED2`](../../library/rules/ltp-a774fc10727e8ed2.yaml) | 无额外前置条件 | 调用 dup(oldfd) | {'kind': 'return_fd', 'return': 'FD'} |
| [`LTP_ED2BA909DF79625A`](../../library/rules/ltp-ed2ba909df79625a.yaml) | 无额外前置条件 | 调用 dup(fd) | {'kind': 'return_fd', 'return': 'FD'} |
## `dup2`

共形成 9 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_12A1904141AAE2EE`](../../library/rules/ltp-12a1904141aae2ee.yaml) | 无额外前置条件 | 调用 dup2(fd0, fd1) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_4F02ACC6E2F6B094`](../../library/rules/ltp-4f02acc6e2f6b094.yaml) | 无额外前置条件 | 调用 dup2(fildes[ifile - 1], ifile) | 返回 -1，errno 为 EBADF |
| [`LTP_75D52C5E9C93B6D7`](../../library/rules/ltp-75d52c5e9c93b6d7.yaml) | 无额外前置条件 | 调用 dup2(mystdout, badfd) | 返回 -1，errno 为 EBADF |
| [`LTP_9F560A103CB6F910`](../../library/rules/ltp-9f560a103cb6f910.yaml) | 无额外前置条件 | 调用 dup2(mystdout, maxfd) | 返回 -1，errno 为 EBADF |
| [`LTP_B7F51635806E7E59`](../../library/rules/ltp-b7f51635806e7e59.yaml) | 无额外前置条件 | 调用 dup2(fd[i], nfd[i]) | {'kind': 'return_value', 'return': 'nfd[i]'} |
| [`LTP_BDA36F61423EEB3E`](../../library/rules/ltp-bda36f61423eeb3e.yaml) | 无额外前置条件 | 调用 dup2(maxfd, goodfd) | 返回 -1，errno 为 EBADF |
| [`LTP_D296A517F138A0C0`](../../library/rules/ltp-d296a517f138a0c0.yaml) | 无额外前置条件 | 调用 dup2(badfd, goodfd) | 返回 -1，errno 为 EBADF |
| [`LTP_DE6F80C5EFE44A9D`](../../library/rules/ltp-de6f80c5efe44a9d.yaml) | 无额外前置条件 | 调用 dup2(ofd, nfd) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_EE8E695CF61D6D8A`](../../library/rules/ltp-ee8e695cf61d6d8a.yaml) | 无额外前置条件 | 调用 dup2(fd, fd) | {'kind': 'return_fd', 'return': 'FD'} |
## `dup3`

共形成 5 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_098AFE0E8E10B0EF`](../../library/rules/ltp-098afe0e8e10b0ef.yaml) | 无额外前置条件 | 调用 dup3(old_fd, old_fd, O_CLOEXEC) | 返回 -1，errno 为 EINVAL |
| [`LTP_1726C16756E9651C`](../../library/rules/ltp-1726c16756e9651c.yaml) | 无额外前置条件 | 调用 dup3(1, 4, O_CLOEXEC) | {'kind': 'return_fd', 'return': 'FD'} |
| [`LTP_37C625BD7D7C5F1D`](../../library/rules/ltp-37c625bd7d7c5f1d.yaml) | 无额外前置条件 | 调用 dup3(old_fd, old_fd, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_3A7B17AF231D4158`](../../library/rules/ltp-3a7b17af231d4158.yaml) | 无额外前置条件 | 调用 dup3(1, 4, 0) | {'kind': 'return_fd', 'return': 'FD'} |
| [`LTP_9B3646398697EA64`](../../library/rules/ltp-9b3646398697ea64.yaml) | 无额外前置条件 | 调用 dup3(old_fd, new_fd, INVALID_FLAG) | 返回 -1，errno 为 EINVAL |
## `epoll`

没有形成可发布的合规性规则。

## `epoll_create`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_2D1E25BD679B3494`](../../library/rules/ltp-2d1e25bd679b3494.yaml) | 无额外前置条件 | 调用 epoll_create(0) | 返回 -1，errno 为 EINVAL |
| [`LTP_49A80712984D44C6`](../../library/rules/ltp-49a80712984d44c6.yaml) | The file descriptor is invalid. | 调用 epoll_create(-1) | 返回 -1，errno 为 EINVAL |
| [`LTP_E7435E0CBCA319E1`](../../library/rules/ltp-e7435e0cbca319e1.yaml) | 无额外前置条件 | 调用 epoll_create(tc[n]) | {'kind': 'return_fd', 'return': 'FD'} |
## `epoll_create1`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_11C0431607FD5753`](../../library/rules/ltp-11c0431607fd5753.yaml) | The file descriptor is invalid. | 调用 epoll_create1(-1) | 返回 -1，errno 为 EINVAL |
| [`LTP_5D8D2B3BEDA79604`](../../library/rules/ltp-5d8d2b3beda79604.yaml) | 无额外前置条件 | 调用 epoll_create1(EPOLL_CLOEXEC + 1) | 返回 -1，errno 为 EINVAL |
## `epoll_ctl`

共形成 12 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_03E15C829583D726`](../../library/rules/ltp-03e15c829583d726.yaml) | The target object already exists. | 调用 epoll_ctl(epfd, EPOLL_CTL_ADD, fd[0], &events[0]) | 返回 -1，errno 为 EEXIST |
| [`LTP_4953FAD330ADE150`](../../library/rules/ltp-4953fad330ade150.yaml) | 无额外前置条件 | 调用 epoll_ctl(epfd, EPOLL_CTL_ADD, inv, &events[1]) | 返回 -1，errno 为 EBADF |
| [`LTP_5350E2FAFAB0B884`](../../library/rules/ltp-5350e2fafab0b884.yaml) | The referenced path does not exist. | 调用 epoll_ctl(epfd, EPOLL_CTL_DEL, fd[1], &events[1]) | 返回 -1，errno 为 ENOENT |
| [`LTP_5883CD050463E9E8`](../../library/rules/ltp-5883cd050463e9e8.yaml) | 无额外前置条件 | 调用 epoll_ctl(epfd, opt, fd, epvs) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_6FFB17DB762F3167`](../../library/rules/ltp-6ffb17db762f3167.yaml) | 无额外前置条件 | 调用 epoll_ctl(inv, EPOLL_CTL_ADD, fd[1], &events[1]) | 返回 -1，errno 为 EBADF |
| [`LTP_82479A4A2E248995`](../../library/rules/ltp-82479a4a2e248995.yaml) | Path resolution encounters a symlink loop. | 调用 epoll_ctl(origin_epfd, EPOLL_CTL_ADD, epfd, &events) | 返回 -1，errno 为 ELOOP |
| [`LTP_83709E56D6285F71`](../../library/rules/ltp-83709e56d6285f71.yaml) | 无额外前置条件 | 调用 epoll_ctl(epfd, EPOLL_CTL_ADD, epfd, &events[1]) | 返回 -1，errno 为 EINVAL |
| [`LTP_9672C6DE0FC3E7D0`](../../library/rules/ltp-9672c6de0fc3e7d0.yaml) | The referenced path does not exist. | 调用 epoll_ctl(epfd, EPOLL_CTL_MOD, fd[1], &events[1]) | 返回 -1，errno 为 ENOENT |
| [`LTP_ADEB5FE2DF97542A`](../../library/rules/ltp-adeb5fe2df97542a.yaml) | 无额外前置条件 | 调用 epoll_ctl(epfd, EPOLL_CTL_MOD, fds[0], &events) | 调用成功，返回 SUCCESS |
| [`LTP_B41BE95567D414C7`](../../library/rules/ltp-b41be95567d414c7.yaml) | The file descriptor is invalid. | 调用 epoll_ctl(epfd, -1, fd[1], &events[1]) | 返回 -1，errno 为 EINVAL |
| [`LTP_CBB1680336D53D2A`](../../library/rules/ltp-cbb1680336d53d2a.yaml) | 无额外前置条件 | 调用 epoll_ctl(epfd, EPOLL_CTL_ADD, unsupported_fd, &events[1]) | 返回 -1，errno 为 EPERM |
| [`LTP_CBD286AFB66B79D0`](../../library/rules/ltp-cbd286afb66b79d0.yaml) | The userspace pointer is outside accessible memory. | 调用 epoll_ctl(epfd, EPOLL_CTL_ADD, fd[1], NULL) | 返回 -1，errno 为 EFAULT |
## `epoll_pwait`

没有形成可发布的合规性规则。

## `epoll_wait`

共形成 9 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_225DA846BF111CDF`](../../library/rules/ltp-225da846bf111cdf.yaml) | The file descriptor is invalid. | 调用 epoll_wait(epfd, &ret_evs, 1, -1) | {'kind': 'return_value', 'return': '1'} |
| [`LTP_337F129FE78A007D`](../../library/rules/ltp-337f129fe78a007d.yaml) | The file descriptor is invalid. | 调用 epoll_wait(epfd, ret_evs, 2, -1) | {'kind': 'return_value', 'return': 'events_matched'} |
| [`LTP_4883FC77EC1F2BB9`](../../library/rules/ltp-4883fc77ec1f2bb9.yaml) | The file descriptor is invalid. | 调用 epoll_wait(epfd, ev_rdwr, -1, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_5AEA06C99B2F5E9A`](../../library/rules/ltp-5aea06c99b2f5e9a.yaml) | The file descriptor is invalid. | 调用 epoll_wait(bad_epfd, ev_rdwr, 1, -1) | 返回 -1，errno 为 EBADF |
| [`LTP_724D6E370813285F`](../../library/rules/ltp-724d6e370813285f.yaml) | The file descriptor is invalid. | 调用 epoll_wait(inv_epfd, ev_rdwr, 1, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_7C8CA0FD5D141A05`](../../library/rules/ltp-7c8ca0fd5d141a05.yaml) | The userspace pointer is outside accessible memory.、The file descriptor is invalid. | 调用 epoll_wait(epfd, ev_rdonly, 1, -1) | 返回 -1，errno 为 EFAULT |
| [`LTP_9244F92CE966130C`](../../library/rules/ltp-9244f92ce966130c.yaml) | The file descriptor is invalid. | 调用 epoll_wait(epfd, ev_rdwr, 0, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_B3F848BCBCBAB559`](../../library/rules/ltp-b3f848bcbcbab559.yaml) | 无额外前置条件 | 调用 epoll_wait(epfd, epevs, 1, 0) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_D75F86A534CB6E02`](../../library/rules/ltp-d75f86a534cb6e02.yaml) | 无额外前置条件 | 调用 epoll_wait(epfd, epevs, 1, sleep_ms) | {'kind': 'return_value', 'return': '0'} |
## `eventfd`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_1AA7F21DA5C55800`](../../library/rules/ltp-1aa7f21da5c55800.yaml) | 无额外前置条件 | 调用 eventfd(0, EFD_NONBLOCK) | {'kind': 'return_fd', 'return': 'FD'} |
| [`LTP_5622491E8A2227F2`](../../library/rules/ltp-5622491e8a2227f2.yaml) | 无额外前置条件 | 调用 eventfd(EVENT_COUNT, EFD_NONBLOCK) | {'kind': 'return_fd', 'return': 'FD'} |
## `eventfd2`

没有形成可发布的合规性规则。

## `execl`

没有形成可发布的合规性规则。

## `execle`

没有形成可发布的合规性规则。

## `execlp`

没有形成可发布的合规性规则。

## `execv`

没有形成可发布的合规性规则。

## `execve`

没有形成可发布的合规性规则。

## `execveat`

共形成 4 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_137CD2E37BF545BF`](../../library/rules/ltp-137cd2e37bf545bf.yaml) | Path resolution encounters a symlink loop. | 调用 execveat(fd, app_sym_path, argv, environ, AT_SYMLINK_NOFOLLOW) | 返回 -1，errno 为 ELOOP |
| [`LTP_3E9AD2C1B3BE9041`](../../library/rules/ltp-3e9ad2c1b3be9041.yaml) | The file descriptor is invalid. | 调用 execveat(fd, app_abs_path, argv, environ, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_82D99A9CBFB63C68`](../../library/rules/ltp-82d99a9cbfb63c68.yaml) | A path component that must be a directory is not a directory. | 调用 execveat(fd, TEST_REL_APP, argv, environ, 0) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_ACF7A30AF3B10973`](../../library/rules/ltp-acf7a30af3b10973.yaml) | 无额外前置条件 | 调用 execveat(bad_fd, "", argv, environ, AT_EMPTY_PATH) | 返回 -1，errno 为 EBADF |
## `execvp`

没有形成可发布的合规性规则。

## `exit`

没有形成可发布的合规性规则。

## `exit_group`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_33D137B9002503E5`](../../library/rules/ltp-33d137b9002503e5.yaml) | 无额外前置条件 | 调用 exit_group(4) | {'kind': 'return_value', 'return': '-1'} |
## `faccessat`

没有形成可发布的合规性规则。

## `faccessat2`

共形成 13 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_025CF701276457CB`](../../library/rules/ltp-025cf701276457cb.yaml) | 无额外前置条件 | 调用 faccessat2(atcwd_fd, sym_path, R_OK, AT_SYMLINK_NOFOLLOW) | 调用成功，返回 SUCCESS |
| [`LTP_122500959CDABFC9`](../../library/rules/ltp-122500959cdabfc9.yaml) | The fixture sets abs_path mode to 0444.、The fixture creates abs_path as a regular file. | 调用 faccessat2(bad_fd, abs_path, R_OK, 0) | 调用成功，返回 SUCCESS |
| [`LTP_144706EDC721819A`](../../library/rules/ltp-144706edc721819a.yaml) | The file descriptor is invalid. | 调用 faccessat2(atcwd_fd, rel_path, -1, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_39715C70E797C1B1`](../../library/rules/ltp-39715c70e797c1b1.yaml) | The fixture sets abs_path mode to 0444.、The fixture creates abs_path as a regular file. | 调用 faccessat2(bad_fd, abs_path, R_OK, AT_EACCESS) | 调用成功，返回 SUCCESS |
| [`LTP_3C8D01B8140DB122`](../../library/rules/ltp-3c8d01b8140db122.yaml) | The caller lacks a permission required by the operation. | 调用 faccessat2(atcwd_fd, rel_path, R_OK, AT_EACCESS) | 返回 -1，errno 为 EACCES |
| [`LTP_437CFCD991A666C9`](../../library/rules/ltp-437cfcd991a666c9.yaml) | 无额外前置条件 | 调用 faccessat2(atcwd_fd, rel_path, R_OK, 0) | 调用成功，返回 SUCCESS |
| [`LTP_4C1F446C9C520B36`](../../library/rules/ltp-4c1f446c9c520b36.yaml) | 无额外前置条件 | 调用 faccessat2(bad_fd, rel_path, R_OK, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_98A871A86ACC8672`](../../library/rules/ltp-98a871a86acc8672.yaml) | The file descriptor is invalid. | 调用 faccessat2(atcwd_fd, rel_path, R_OK, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_C2909AC2ECEDED94`](../../library/rules/ltp-c2909ac2eceded94.yaml) | 无额外前置条件 | 调用 faccessat2(dir_fd, testfile, R_OK, 0) | 调用成功，返回 SUCCESS |
| [`LTP_D0E55E3A04E47FFC`](../../library/rules/ltp-d0e55e3a04e47ffc.yaml) | A path component that must be a directory is not a directory. | 调用 faccessat2(fd, rel_path, R_OK, 0) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_D77858597BCC1C13`](../../library/rules/ltp-d77858597bcc1c13.yaml) | 无额外前置条件 | 调用 faccessat2(atcwd_fd, rel_path, R_OK, AT_EACCESS) | 调用成功，返回 SUCCESS |
| [`LTP_E81373866A3C5AB3`](../../library/rules/ltp-e81373866a3c5ab3.yaml) | The userspace pointer is outside accessible memory. | 调用 faccessat2(atcwd_fd, bad_path, R_OK, 0) | 返回 -1，errno 为 EFAULT |
| [`LTP_F7B8EDE302D5D08A`](../../library/rules/ltp-f7b8ede302d5d08a.yaml) | 无额外前置条件 | 调用 faccessat2(dir_fd, testfile, R_OK, AT_EACCESS) | 调用成功，返回 SUCCESS |
## `fadvise`

没有形成可发布的合规性规则。

## `fallocate`

没有形成可发布的合规性规则。

## `fanotify`

没有形成可发布的合规性规则。

## `fchdir`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_17B7A9460939622A`](../../library/rules/ltp-17b7a9460939622a.yaml) | 无额外前置条件 | 调用 fchdir(fd) | 调用成功，返回 SUCCESS |
| [`LTP_9E5F965A018077D2`](../../library/rules/ltp-9e5f965a018077d2.yaml) | The caller lacks a permission required by the operation. | 调用 fchdir(fd) | 返回 -1，errno 为 EACCES |
| [`LTP_CCC36F43E9463D3E`](../../library/rules/ltp-ccc36f43e9463d3e.yaml) | 无额外前置条件 | 调用 fchdir(bad_fd) | 返回 -1，errno 为 EBADF |
## `fchmod`

共形成 5 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_371BDA67CB8813FD`](../../library/rules/ltp-371bda67cb8813fd.yaml) | 无额外前置条件 | 调用 fchmod(fd2, 0644) | 返回 -1，errno 为 EBADF |
| [`LTP_470C0966080C93EF`](../../library/rules/ltp-470c0966080c93ef.yaml) | 无额外前置条件 | 调用 fchmod(fd, mode) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_A1B6FBC6EF800331`](../../library/rules/ltp-a1b6fbc6ef800331.yaml) | 无额外前置条件 | 调用 fchmod(fd, PERMS_DIR) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_F1299BC5F92BF26E`](../../library/rules/ltp-f1299bc5f92bf26e.yaml) | 无额外前置条件 | 调用 fchmod(fd3, 0644) | 返回 -1，errno 为 EROFS |
| [`LTP_F421E1E61753B72C`](../../library/rules/ltp-f421e1e61753b72c.yaml) | 无额外前置条件 | 调用 fchmod(fd1, 0644) | 返回 -1，errno 为 EPERM |
## `fchmodat`

共形成 9 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_1A2B889BBD9A1444`](../../library/rules/ltp-1a2b889bbd9a1444.yaml) | The file descriptor is invalid. | 调用 fchmodat(fd_atcwd, test_path, 0600, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_3073AC57544A6A6A`](../../library/rules/ltp-3073ac57544a6a6a.yaml) | 无额外前置条件 | 调用 fchmodat(bad_fd, test_path, 0600, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_4FAABB99B8EB0CE9`](../../library/rules/ltp-4faabb99b8eb0ce9.yaml) | The referenced path does not exist. | 调用 fchmodat(file_fd, empty_path, 0600, 0) | 返回 -1，errno 为 ENOENT |
| [`LTP_661F97F83268E2F4`](../../library/rules/ltp-661f97f83268e2f4.yaml) | The pathname exceeds the supported limit. | 调用 fchmodat(file_fd, long_path, 0600, 0) | 返回 -1，errno 为 ENAMETOOLONG |
| [`LTP_8A4C03F737A3CEE6`](../../library/rules/ltp-8a4c03f737a3cee6.yaml) | 无额外前置条件 | 调用 fchmodat(atcwd_fd, file_path, 0600, 0) | 调用成功，返回 SUCCESS |
| [`LTP_B4FD0E2B4B84F458`](../../library/rules/ltp-b4fd0e2b4b84f458.yaml) | 无额外前置条件 | 调用 fchmodat(file_fd, abs_path, 0600, 0) | 调用成功，返回 SUCCESS |
| [`LTP_D9ED751DFFC3CC63`](../../library/rules/ltp-d9ed751dffc3cc63.yaml) | A path component that must be a directory is not a directory. | 调用 fchmodat(file_fd, test_path, 0600, 0) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_EAAD13B42BE1ED54`](../../library/rules/ltp-eaad13b42be1ed54.yaml) | The userspace pointer is outside accessible memory. | 调用 fchmodat(file_fd, bad_path, 0600, 0) | 返回 -1，errno 为 EFAULT |
| [`LTP_F04C2129F0253CC0`](../../library/rules/ltp-f04c2129f0253cc0.yaml) | 无额外前置条件 | 调用 fchmodat(dir_fd, test_file, 0600, 0) | 调用成功，返回 SUCCESS |
## `fchmodat2`

共形成 4 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_5F2B89F71FACBDF3`](../../library/rules/ltp-5f2b89f71facbdf3.yaml) | The fixture creates FILENAME as a regular file.、The fixture sets FILENAME mode to 0640.、The file descriptor is invalid. | 调用 fchmodat2(fd, FILENAME, 0777, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_AA8EF9120C0B6329`](../../library/rules/ltp-aa8ef9120c0b6329.yaml) | The referenced path does not exist. | 调用 fchmodat2(fd, "doesnt_exist.txt", 0777, 0) | 返回 -1，errno 为 ENOENT |
| [`LTP_C1C97EB1E917FD3D`](../../library/rules/ltp-c1c97eb1e917fd3d.yaml) | The file descriptor is invalid.、The fixture creates FILENAME as a regular file.、The fixture sets FILENAME mode to 0640. | 调用 fchmodat2(fd_invalid, FILENAME, 0777, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_F65E54AE96F20D41`](../../library/rules/ltp-f65e54ae96f20d41.yaml) | 无额外前置条件 | 调用 fchmodat2(fd_dir, SNAME, 0640, AT_SYMLINK_NOFOLLOW) | 返回 -1，errno 为 EOPNOTSUPP |
## `fchown`

没有形成可发布的合规性规则。

## `fcntl`

没有形成可发布的合规性规则。

## `fdatasync`

没有形成可发布的合规性规则。

## `fgetxattr`

没有形成可发布的合规性规则。

## `file_attr`

没有形成可发布的合规性规则。

## `finit_module`

没有形成可发布的合规性规则。

## `flistxattr`

共形成 4 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_609D7178B8A77C1F`](../../library/rules/ltp-609d7178b8a77c1f.yaml) | 无额外前置条件 | 调用 flistxattr(fd[n], NULL, 0) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_7AF560F7F0432A01`](../../library/rules/ltp-7af560f7f0432a01.yaml) | The argument is a userspace buffer. | 调用 flistxattr(fd2, buf, 20) | 返回 -1，errno 为 EBADF |
| [`LTP_E7761F889A77DB75`](../../library/rules/ltp-e7761f889a77db75.yaml) | The argument is a userspace buffer. | 调用 flistxattr(fd1, buf, 1) | 返回 -1，errno 为 ERANGE |
| [`LTP_F7EAB2DB74BE5612`](../../library/rules/ltp-f7eab2db74be5612.yaml) | The argument is a userspace buffer. | 调用 flistxattr(fd, buf, sizeof(buf)) | {'kind': 'return_value', 'return': '-1'} |
## `flock`

共形成 10 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_04A84187DEC4CF09`](../../library/rules/ltp-04a84187dec4cf09.yaml) | 无额外前置条件 | 调用 flock(fd2, LOCK_SH) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_245110930B22BF5C`](../../library/rules/ltp-245110930b22bf5c.yaml) | 无额外前置条件 | 调用 flock(fd1, LOCK_UN) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_6A70899352D69A0B`](../../library/rules/ltp-6a70899352d69a0b.yaml) | 无额外前置条件 | 调用 flock(fd, LOCK_UN) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_9256D223D5EF4AF0`](../../library/rules/ltp-9256d223d5ef4af0.yaml) | 无额外前置条件 | 调用 flock(fd, LOCK_SH | LOCK_EX) | 返回 0，errno 为 EINVAL |
| [`LTP_A2A80201A4364230`](../../library/rules/ltp-a2a80201a4364230.yaml) | 无额外前置条件 | 调用 flock(fd, LOCK_NB) | 返回 0，errno 为 EINVAL |
| [`LTP_AE4CE76865CD4D6D`](../../library/rules/ltp-ae4ce76865cd4d6d.yaml) | 无额外前置条件 | 调用 flock(fd, LOCK_NB | LOCK_EX) | 返回 0，errno 为 EWOULDBLOCK |
| [`LTP_B5959FE5199E821F`](../../library/rules/ltp-b5959fe5199e821f.yaml) | 无额外前置条件 | 调用 flock(badfd, LOCK_SH) | 返回 0，errno 为 EBADF |
| [`LTP_B8EA21096E591EBB`](../../library/rules/ltp-b8ea21096e591ebb.yaml) | 无额外前置条件 | 调用 flock(fd1, LOCK_EX) | 调用成功，返回 SUCCESS |
| [`LTP_D63AFAA6729CB519`](../../library/rules/ltp-d63afaa6729cb519.yaml) | 无额外前置条件 | 调用 flock(fd2, LOCK_EX) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_FB047DBB72D78D19`](../../library/rules/ltp-fb047dbb72d78d19.yaml) | 无额外前置条件 | 调用 flock(fd1, LOCK_EX | LOCK_NB) | {'kind': 'return_value', 'return': '0'} |
## `fmtmsg`

没有形成可发布的合规性规则。

## `fork`

没有形成可发布的合规性规则。

## `fpathconf`

共形成 9 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_09FED6AAC1020069`](../../library/rules/ltp-09fed6aac1020069.yaml) | 无额外前置条件 | 调用 fpathconf(fd, _PC_MAX_INPUT) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_1EEDAE05876D0546`](../../library/rules/ltp-1eedae05876d0546.yaml) | 无额外前置条件 | 调用 fpathconf(fd, _PC_PATH_MAX) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_20DA453342D2F4AB`](../../library/rules/ltp-20da453342d2f4ab.yaml) | 无额外前置条件 | 调用 fpathconf(fd, _PC_NAME_MAX) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_33C492F97B790AB8`](../../library/rules/ltp-33c492f97b790ab8.yaml) | 无额外前置条件 | 调用 fpathconf(fd, _PC_CHOWN_RESTRICTED) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_582938D6E8E17DB3`](../../library/rules/ltp-582938d6e8e17db3.yaml) | 无额外前置条件 | 调用 fpathconf(fd, _PC_NO_TRUNC) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_963EAEB0B41C7934`](../../library/rules/ltp-963eaeb0b41c7934.yaml) | 无额外前置条件 | 调用 fpathconf(fd, _PC_MAX_CANON) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_BF679B7A7E60BCFD`](../../library/rules/ltp-bf679b7a7e60bcfd.yaml) | 无额外前置条件 | 调用 fpathconf(fd, _PC_VDISABLE) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_D1DAB36EB37FCA27`](../../library/rules/ltp-d1dab36eb37fca27.yaml) | 无额外前置条件 | 调用 fpathconf(fd, _PC_PIPE_BUF) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_FF1A8A6101CEA37E`](../../library/rules/ltp-ff1a8a6101cea37e.yaml) | 无额外前置条件 | 调用 fpathconf(fd, _PC_LINK_MAX) | {'kind': 'positive_return', 'return': '>0'} |
## `fremovexattr`

没有形成可发布的合规性规则。

## `fsconfig`

共形成 33 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_021CFAE8581109DA`](../../library/rules/ltp-021cfae8581109da.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_BINARY, NULL, "foo", aux_1) | 返回 -1，errno 为 EINVAL |
| [`LTP_0B35C54F2F39E4D4`](../../library/rules/ltp-0b35c54f2f39e4d4.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_CMD_RECONFIGURE, NULL, "foo", aux_0) | 返回 -1，errno 为 EINVAL |
| [`LTP_0D9BB2CB02786128`](../../library/rules/ltp-0d9bb2cb02786128.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_FD, "sync", "foo", temp_fd) | 返回 -1，errno 为 EINVAL |
| [`LTP_0DF4BC077C390176`](../../library/rules/ltp-0df4bc077c390176.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_FD, NULL, NULL, temp_fd) | 返回 -1，errno 为 EINVAL |
| [`LTP_11235D2EF3DC4C5C`](../../library/rules/ltp-11235d2ef3dc4c5c.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_STRING, "source", NULL, aux_0) | 返回 -1，errno 为 EINVAL |
| [`LTP_1918D556CB808466`](../../library/rules/ltp-1918d556cb808466.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_PATH, "sync", NULL, aux_fdcwd) | 返回 -1，errno 为 EINVAL |
| [`LTP_1C8100D018645855`](../../library/rules/ltp-1c8100d018645855.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_PATH_EMPTY, "sync", "/dev/foo", aux_minus1) | 返回 -1，errno 为 EINVAL |
| [`LTP_2433DF1752AE54B7`](../../library/rules/ltp-2433df1752ae54b7.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_FLAG, "rw", NULL, 0) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_2BBDFB48EF060066`](../../library/rules/ltp-2bbdfb48ef060066.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_STRING, "\x00", val, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_3D50FA09D36623FF`](../../library/rules/ltp-3d50fa09d36623ff.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_FD, "sync", NULL, aux_minus1) | 返回 -1，errno 为 EINVAL |
| [`LTP_46401248F52AD892`](../../library/rules/ltp-46401248f52ad892.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_PATH, "sync", tst_device->dev, 0) | 返回 -1，errno 为 EOPNOTSUPP |
| [`LTP_50972E17C52A9EF6`](../../library/rules/ltp-50972e17c52a9ef6.yaml) | 无额外前置条件 | 调用 fsconfig(invalid_fd, FSCONFIG_SET_FLAG, "user_xattr", NULL, aux_0) | 返回 -1，errno 为 EINVAL |
| [`LTP_53B499F623D50A0A`](../../library/rules/ltp-53b499f623d50a0a.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_BINARY, "sync", NULL, aux_1) | 返回 -1，errno 为 EINVAL |
| [`LTP_55D4EF674AFB4ED1`](../../library/rules/ltp-55d4ef674afb4ed1.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_CMD_CREATE, NULL, NULL, aux_1) | 返回 -1，errno 为 EINVAL |
| [`LTP_55EFF664BDCE3E21`](../../library/rules/ltp-55eff664bdce3e21.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_CMD_RECONFIGURE, "foo", NULL, aux_0) | 返回 -1，errno 为 EINVAL |
| [`LTP_5DC368435F71390F`](../../library/rules/ltp-5dc368435f71390f.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_FLAG, NULL, NULL, aux_0) | 返回 -1，errno 为 EINVAL |
| [`LTP_6090C26F5D5D8E5D`](../../library/rules/ltp-6090c26f5d5d8e5d.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_PATH_EMPTY, NULL, "/dev/foo", aux_fdcwd) | 返回 -1，errno 为 EINVAL |
| [`LTP_708F721FB3456F82`](../../library/rules/ltp-708f721fb3456f82.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_FLAG, "rw", NULL, aux_1) | 返回 -1，errno 为 EINVAL |
| [`LTP_7ECC43C03A3DCB14`](../../library/rules/ltp-7ecc43c03a3dcb14.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_PATH_EMPTY, "sync", NULL, aux_fdcwd) | 返回 -1，errno 为 EINVAL |
| [`LTP_7FCEEF8C37201FC7`](../../library/rules/ltp-7fceef8c37201fc7.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_STRING, "source", "#grand.central.org:root.cell.", aux_1) | 返回 -1，errno 为 EINVAL |
| [`LTP_7FD1D8A10AC952F2`](../../library/rules/ltp-7fd1d8a10ac952f2.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_STRING, "source", tst_device->dev, 0) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_88D0821E4776E388`](../../library/rules/ltp-88d0821e4776e388.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_PATH_EMPTY, "sync", tst_device->dev, 0) | 返回 -1，errno 为 EOPNOTSUPP |
| [`LTP_9FE663EAF1F0ABCF`](../../library/rules/ltp-9fe663eaf1f0abcf.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_BINARY, "sync", "foo", aux_0) | 返回 -1，errno 为 EINVAL |
| [`LTP_A9DD0D461E032A07`](../../library/rules/ltp-a9dd0d461e032a07.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_CMD_CREATE, NULL, NULL, 0) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_AC7D82691053FF4D`](../../library/rules/ltp-ac7d82691053ff4d.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_PATH, "sync", "/dev/foo", aux_minus1) | 返回 -1，errno 为 EINVAL |
| [`LTP_B4B9F07E1C1A3826`](../../library/rules/ltp-b4b9f07e1c1a3826.yaml) | 无额外前置条件 | 调用 fsconfig(fd, 100, "rw", NULL, aux_0) | 返回 -1，errno 为 EOPNOTSUPP |
| [`LTP_C678E0C87280F82D`](../../library/rules/ltp-c678e0c87280f82d.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_CMD_RECONFIGURE, NULL, NULL, aux_1) | 返回 -1，errno 为 EINVAL |
| [`LTP_D5D78F93265A1980`](../../library/rules/ltp-d5d78f93265a1980.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_FD, "sync", NULL, 0) | 返回 -1，errno 为 EOPNOTSUPP |
| [`LTP_D615E29C0C4C9CCB`](../../library/rules/ltp-d615e29c0c4c9ccb.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_CMD_CREATE, "foo", NULL, aux_0) | 返回 -1，errno 为 EINVAL |
| [`LTP_E6750A641272AF1B`](../../library/rules/ltp-e6750a641272af1b.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_FLAG, "rw", "foo", aux_0) | 返回 -1，errno 为 EINVAL |
| [`LTP_EBCE1A2B8CE59ECE`](../../library/rules/ltp-ebce1a2b8ce59ece.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_CMD_CREATE, NULL, "foo", aux_0) | 返回 -1，errno 为 EINVAL |
| [`LTP_F66DDB5A0EBC5C9F`](../../library/rules/ltp-f66ddb5a0ebc5c9f.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_STRING, NULL, "#grand.central.org:root.cell.", aux_0) | 返回 -1，errno 为 EINVAL |
| [`LTP_FDE0B30F1CFCAA4B`](../../library/rules/ltp-fde0b30f1cfcaa4b.yaml) | 无额外前置条件 | 调用 fsconfig(fd, FSCONFIG_SET_PATH, NULL, "/dev/foo", aux_fdcwd) | 返回 -1，errno 为 EINVAL |
## `fsetxattr`

没有形成可发布的合规性规则。

## `fsmount`

没有形成可发布的合规性规则。

## `fsopen`

没有形成可发布的合规性规则。

## `fspick`

没有形成可发布的合规性规则。

## `fstat`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_875F17F6F720BEC2`](../../library/rules/ltp-875f17f6f720bec2.yaml) | The argument is a userspace buffer. | 调用 fstat(fd_ebadf, &stat_buf) | 返回 -1，errno 为 EBADF |
| [`LTP_B0C8B999421C6345`](../../library/rules/ltp-b0c8b999421c6345.yaml) | The userspace pointer is outside accessible memory. | 调用 fstat(fd_ok, NULL) | 返回 -1，errno 为 EFAULT |
| [`LTP_B4AADBA5EA4C395B`](../../library/rules/ltp-b4aadba5ea4c395b.yaml) | The argument is a userspace buffer. | 调用 fstat(fildes, &stat_buf) | 调用成功，返回 SUCCESS |
## `fstatat`

没有形成可发布的合规性规则。

## `fstatfs`

共形成 4 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_14072975543D9890`](../../library/rules/ltp-14072975543d9890.yaml) | The userspace pointer is outside accessible memory. | 调用 fstatfs(fd, (void *)-1) | 返回 -1，errno 为 EFAULT |
| [`LTP_BF183AB6911D1BAF`](../../library/rules/ltp-bf183ab6911d1baf.yaml) | The argument is a userspace buffer. | 调用 fstatfs(pipe_fd, &buf) | 调用成功，返回 SUCCESS |
| [`LTP_C04292C48EC89063`](../../library/rules/ltp-c04292c48ec89063.yaml) | The argument is a userspace buffer. | 调用 fstatfs(bad_fd, &buf) | 返回 -1，errno 为 EBADF |
| [`LTP_DC01A8115E3EC579`](../../library/rules/ltp-dc01a8115e3ec579.yaml) | The argument is a userspace buffer. | 调用 fstatfs(file_fd, &buf) | 调用成功，返回 SUCCESS |
## `fsync`

没有形成可发布的合规性规则。

## `ftruncate`

共形成 6 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_02D0577172D97F4B`](../../library/rules/ltp-02d0577172d97f4b.yaml) | 无额外前置条件 | 调用 ftruncate(fd, TRUNC_LEN2) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_213EA37A2B59AB99`](../../library/rules/ltp-213ea37a2b59ab99.yaml) | 无额外前置条件 | 调用 ftruncate(fd, TRUNC_LEN1) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_46AA49209C30E739`](../../library/rules/ltp-46aa49209c30e739.yaml) | 无额外前置条件 | 调用 ftruncate(sock_fd, 4) | 返回 -1，errno 为 EINVAL |
| [`LTP_63E6527501A08F92`](../../library/rules/ltp-63e6527501a08f92.yaml) | 无额外前置条件 | 调用 ftruncate(read_fd, 4) | 返回 -1，errno 为 EINVAL |
| [`LTP_EB214534D857AE95`](../../library/rules/ltp-eb214534d857ae95.yaml) | 无额外前置条件 | 调用 ftruncate(bad_fd, 4) | 返回 -1，errno 为 EBADF |
| [`LTP_F21B2458879EFBAB`](../../library/rules/ltp-f21b2458879efbab.yaml) | The file descriptor is invalid. | 调用 ftruncate(fd, -1) | 返回 -1，errno 为 EINVAL |
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
| [`LTP_8CF830DB0473B27D`](../../library/rules/ltp-8cf830db0473b27d.yaml) | The userspace pointer is outside accessible memory. | 调用 get_robust_list(0, NULL, &len_ptr) | 返回 -1，errno 为 EFAULT |
| [`LTP_A5952E2BE90138F8`](../../library/rules/ltp-a5952e2be90138f8.yaml) | The userspace pointer is outside accessible memory. | 调用 get_robust_list(0, (struct robust_list_head *)&head, NULL) | 返回 -1，errno 为 EFAULT |
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
| [`LTP_12FEE545B9A2556F`](../../library/rules/ltp-12fee545b9a2556f.yaml) | The userspace pointer is outside accessible memory. | 调用 getcwd((void *)-1, PATH_MAX) | 返回 -1，errno 为 EFAULT |
| [`LTP_53E3454ED6EFD842`](../../library/rules/ltp-53e3454ed6efd842.yaml) | 无额外前置条件 | 调用 getcwd(buffer, 1) | 返回 -1，errno 为 ERANGE |
| [`LTP_729222947741DFD6`](../../library/rules/ltp-729222947741dfd6.yaml) | 无额外前置条件 | 调用 getcwd(buffer, 0) | 返回 -1，errno 为 ERANGE |
| [`LTP_9FAB1B9A02F7CAF0`](../../library/rules/ltp-9fab1b9a02f7caf0.yaml) | The userspace pointer is outside accessible memory. | 调用 getcwd(NULL, (size_t)-1) | 返回 -1，errno 为 EFAULT |
| [`LTP_FC1E41C3414E7F21`](../../library/rules/ltp-fc1e41c3414e7f21.yaml) | 无额外前置条件 | 调用 getcwd(NULL, 1) | 返回 -1，errno 为 ERANGE |
## `getdents64`

共形成 5 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_367A286E9FC81496`](../../library/rules/ltp-367a286e9fc81496.yaml) | A path component that must be a directory is not a directory.、The argument is a userspace buffer. | 调用 getdents64(fd_file, dirp, size) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_3F00E13306997358`](../../library/rules/ltp-3f00e13306997358.yaml) | The argument is a userspace buffer. | 调用 getdents64(fd, dirp1, size1) | 返回 -1，errno 为 EINVAL |
| [`LTP_96C057F70BA4F5B9`](../../library/rules/ltp-96c057f70ba4f5b9.yaml) | The argument is a userspace buffer.、The userspace pointer is outside accessible memory. | 调用 getdents64(fd, dirp_bad, size) | 返回 -1，errno 为 EFAULT |
| [`LTP_C894288BC38DB82C`](../../library/rules/ltp-c894288bc38db82c.yaml) | The referenced path does not exist.、The argument is a userspace buffer. | 调用 getdents64(fd_unlinked, dirp, size) | 返回 -1，errno 为 ENOENT |
| [`LTP_DEB4A4BEB59AD7A4`](../../library/rules/ltp-deb4a4beb59ad7a4.yaml) | The argument is a userspace buffer. | 调用 getdents64(fd_inv, dirp, size) | 返回 -1，errno 为 EBADF |
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
| [`LTP_BFFEED9C08C13250`](../../library/rules/ltp-bffeed9c08c13250.yaml) | The pathname exceeds the supported limit. | 调用 gethostname(hostname, real_length - 1) | 返回 -1，errno 为 ENAMETOOLONG |
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

共形成 4 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_6DF55FF20A44572D`](../../library/rules/ltp-6df55ff20a44572d.yaml) | 无额外前置条件 | 调用 getpriority(PRIO_PGRP, INVAL_ID) | 返回 -1，errno 为 ESRCH |
| [`LTP_88D300A8FB407324`](../../library/rules/ltp-88d300a8fb407324.yaml) | 无额外前置条件 | 调用 getpriority(INVAL_FLAG, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_99C45ECA20496C98`](../../library/rules/ltp-99c45eca20496c98.yaml) | 无额外前置条件 | 调用 getpriority(PRIO_PROCESS, INVAL_ID) | 返回 -1，errno 为 ESRCH |
| [`LTP_9B0BA3ADF46F5FF4`](../../library/rules/ltp-9b0ba3adf46f5ff4.yaml) | 无额外前置条件 | 调用 getpriority(PRIO_USER, INVAL_ID) | 返回 -1，errno 为 ESRCH |
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
| [`LTP_A0547B601C515355`](../../library/rules/ltp-a0547b601c515355.yaml) | 无额外前置条件 | 调用 getrlimit(RES(RLIMIT_SIGPENDING), &rlim) | 调用成功，返回 SUCCESS |
| [`LTP_B058D6B9CBBB459D`](../../library/rules/ltp-b058d6b9cbbb459d.yaml) | 无额外前置条件 | 调用 getrlimit(INVALID_RES_TYPE, &rlim) | 返回 -1，errno 为 EINVAL |
| [`LTP_BD5C209F4C6EE910`](../../library/rules/ltp-bd5c209f4c6ee910.yaml) | 无额外前置条件 | 调用 getrlimit(RES(RLIMIT_MEMLOCK), &rlim) | 调用成功，返回 SUCCESS |
| [`LTP_C92D3BC9579570DA`](../../library/rules/ltp-c92d3bc9579570da.yaml) | The userspace pointer is outside accessible memory. | 调用 getrlimit(RLIMIT_CORE, (void *)-1) | 返回 -1，errno 为 EFAULT |
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
| [`LTP_030901665B56CA4C`](../../library/rules/ltp-030901665b56ca4c.yaml) | The userspace pointer is outside accessible memory. | 调用 getsockname(sock_bind, (struct sockaddr *) NULL, &sinlen) | 返回 -1，errno 为 EFAULT |
| [`LTP_49D5637777352E9B`](../../library/rules/ltp-49d5637777352e9b.yaml) | The userspace pointer is outside accessible memory. | 调用 getsockname(sock_bind, (struct sockaddr *) &fsin1, NULL) | 返回 -1，errno 为 EFAULT |
| [`LTP_52CE7E6F9B5FF947`](../../library/rules/ltp-52ce7e6f9b5ff947.yaml) | 无额外前置条件 | 调用 getsockname(sock_null, (struct sockaddr *) &fsin1, &sinlen) | 返回 -1，errno 为 ENOTSOCK |
| [`LTP_A5BD16DDF641E0B7`](../../library/rules/ltp-a5bd16ddf641e0b7.yaml) | The userspace pointer is outside accessible memory. | 调用 getsockname(sock_bind, (struct sockaddr *) &fsin1, (socklen_t *) 1) | 返回 -1，errno 为 EFAULT |
| [`LTP_AA9171FB32FD0C67`](../../library/rules/ltp-aa9171fb32fd0c67.yaml) | 无额外前置条件 | 调用 getsockname(sock_fake, (struct sockaddr *) &fsin1, &sinlen) | 返回 -1，errno 为 EBADF |
| [`LTP_DBFBE6A110B3D17B`](../../library/rules/ltp-dbfbe6a110b3d17b.yaml) | 无额外前置条件 | 调用 getsockname(sock_bind, (struct sockaddr *) &fsin1, &sininval) | 返回 -1，errno 为 EINVAL |
## `getsockopt`

共形成 9 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_21E1D9035D6DF74B`](../../library/rules/ltp-21e1d9035d6df74b.yaml) | The userspace pointer is outside accessible memory. | 调用 getsockopt(sock_bind, SOL_SOCKET, SO_OOBINLINE, &optval, 0) | 返回 -1，errno 为 EFAULT |
| [`LTP_3DDCD08519809A17`](../../library/rules/ltp-3ddcd08519809a17.yaml) | 无额外前置条件 | 调用 getsockopt(sock_bind, IPPROTO_UDP, SO_OOBINLINE, &optval, &optlen) | 返回 -1，errno 为 EOPNOTSUPP |
| [`LTP_8BCA62F97A197BC2`](../../library/rules/ltp-8bca62f97a197bc2.yaml) | 无额外前置条件 | 调用 getsockopt(sock_bind, 500, SO_OOBINLINE, &optval, &optlen) | 返回 -1，errno 为 EOPNOTSUPP |
| [`LTP_A94C8185C529647D`](../../library/rules/ltp-a94c8185c529647d.yaml) | The userspace pointer is outside accessible memory. | 调用 getsockopt(sock_bind, SOL_SOCKET, SO_OOBINLINE, 0, &optlen) | 返回 -1，errno 为 EFAULT |
| [`LTP_B72405976D9F15E6`](../../library/rules/ltp-b72405976d9f15e6.yaml) | 无额外前置条件 | 调用 getsockopt(sock_fake, SOL_SOCKET, SO_OOBINLINE, &optval, &optlen) | 返回 -1，errno 为 EBADF |
| [`LTP_C6B4E04E7671DF4C`](../../library/rules/ltp-c6b4e04e7671df4c.yaml) | The file descriptor is invalid. | 调用 getsockopt(sock_bind, IPPROTO_TCP, -1, &optval, &optlen) | 返回 -1，errno 为 ENOPROTOOPT |
| [`LTP_D77AD0D4DC9C0C9E`](../../library/rules/ltp-d77ad0d4dc9c0c9e.yaml) | 无额外前置条件 | 调用 getsockopt(sock_null, SOL_SOCKET, SO_OOBINLINE, &optval, &optlen) | 返回 -1，errno 为 ENOTSOCK |
| [`LTP_E2EEBD0885B0F3EC`](../../library/rules/ltp-e2eebd0885b0f3ec.yaml) | The file descriptor is invalid. | 调用 getsockopt(sock_bind, IPPROTO_IP, -1, &optval, &optlen) | 返回 -1，errno 为 ENOPROTOOPT |
| [`LTP_FE51D85F4A425C61`](../../library/rules/ltp-fe51d85f4a425c61.yaml) | 无额外前置条件 | 调用 getsockopt(sock_bind, SOL_SOCKET, SO_OOBINLINE, &optval, &optleninval) | 返回 -1，errno 为 EINVAL |
## `gettid`

没有形成可发布的合规性规则。

## `gettimeofday`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_69919B72D9A02D03`](../../library/rules/ltp-69919b72d9a02d03.yaml) | The userspace pointer is outside accessible memory. | 调用 gettimeofday((void *)-1, NULL) | 返回 -1，errno 为 EFAULT |
| [`LTP_90D9067DABAD1253`](../../library/rules/ltp-90d9067dabad1253.yaml) | The userspace pointer is outside accessible memory. | 调用 gettimeofday(&tv1, (void *)-1) | 返回 -1，errno 为 EFAULT |
| [`LTP_E564AACFFDAA71E1`](../../library/rules/ltp-e564aacffdaa71e1.yaml) | The userspace pointer is outside accessible memory. | 调用 gettimeofday((void *)-1, (void *)-1) | 返回 -1，errno 为 EFAULT |
## `getuid`

没有形成可发布的合规性规则。

## `getxattr`

没有形成可发布的合规性规则。

## `init_module`

没有形成可发布的合规性规则。

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
| [`LTP_248EACE09AACC5AD`](../../library/rules/ltp-248eace09aacc5ad.yaml) | The userspace pointer is outside accessible memory.、The argument is a userspace buffer. | 调用 lgetxattr((char *)-1, SECURITY_KEY, buf, sizeof(buf)) | 返回 -1，errno 为 EFAULT |
| [`LTP_5A2ECF299444C403`](../../library/rules/ltp-5a2ecf299444c403.yaml) | The fixture creates "symlink" as a symbolic link.、The argument is a userspace buffer. | 调用 lgetxattr("symlink", SECURITY_KEY, buf, sizeof(buf)) | 返回 -1，errno 为 ERANGE |
| [`LTP_9BFDDF855EC51FDA`](../../library/rules/ltp-9bfddf855ec51fda.yaml) | The fixture creates "symlink" as a symbolic link.、The argument is a userspace buffer. | 调用 lgetxattr("symlink", SECURITY_KEY2, buf, size) | {'kind': 'return_value', 'return': 'strlen(VALUE2'} |
| [`LTP_A8C7B3D7AF1FA55E`](../../library/rules/ltp-a8c7b3d7af1fa55e.yaml) | The fixture creates "symlink" as a symbolic link.、The argument is a userspace buffer. | 调用 lgetxattr("symlink", SECURITY_KEY1, buf, size) | 返回 -1，errno 为 ENODATA |
| [`LTP_AADEDDF7D9C31F91`](../../library/rules/ltp-aadeddf7d9c31f91.yaml) | The fixture sets "testfile" mode to 0644.、The fixture creates "testfile" as a regular file.、The argument is a userspace buffer. | 调用 lgetxattr("testfile", SECURITY_KEY, buf, sizeof(buf)) | 返回 -1，errno 为 ENODATA |
## `link`

没有形成可发布的合规性规则。

## `linkat`

没有形成可发布的合规性规则。

## `listen`

没有形成可发布的合规性规则。

## `listmount`

没有形成可发布的合规性规则。

## `listxattr`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_969660F14B0B297A`](../../library/rules/ltp-969660f14b0b297a.yaml) | 无额外前置条件 | 调用 listxattr(name, NULL, 0) | {'kind': 'return_value', 'return': '-1'} |
## `llistxattr`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_1B2E614CA8847B31`](../../library/rules/ltp-1b2e614ca8847b31.yaml) | 无额外前置条件 | 调用 llistxattr(name, NULL, 0) | {'kind': 'return_value', 'return': '-1'} |
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
| [`LTP_30A4B4C40696905E`](../../library/rules/ltp-30a4b4c40696905e.yaml) | Path resolution encounters a symlink loop.、The argument is a userspace buffer. | 调用 lstat(elooppathname, &stat_buf) | 返回 -1，errno 为 ELOOP |
| [`LTP_4323000B7A8D2E5D`](../../library/rules/ltp-4323000b7a8d2e5d.yaml) | The userspace pointer is outside accessible memory.、The argument is a userspace buffer. | 调用 lstat(NULL, &stat_buf) | 返回 -1，errno 为 EFAULT |
| [`LTP_658F21F428A67438`](../../library/rules/ltp-658f21f428a67438.yaml) | A path component that must be a directory is not a directory.、The argument is a userspace buffer. | 调用 lstat(TEST_ENOTDIR, &stat_buf) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_7CA8BC18271AA973`](../../library/rules/ltp-7ca8bc18271aa973.yaml) | The pathname exceeds the supported limit.、The argument is a userspace buffer. | 调用 lstat(longpathname, &stat_buf) | 返回 -1，errno 为 ENAMETOOLONG |
| [`LTP_8C2F2999FBFE056D`](../../library/rules/ltp-8c2f2999fbfe056d.yaml) | The referenced path does not exist.、The argument is a userspace buffer. | 调用 lstat(TEST_ENOENT, &stat_buf) | 返回 -1，errno 为 ENOENT |
| [`LTP_9E1134B051A31DAD`](../../library/rules/ltp-9e1134b051a31dad.yaml) | The fixture creates TESTSYML as a symbolic link.、The argument is a userspace buffer. | 调用 lstat(TESTSYML, &stat_buf) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_E9690AB9682FCE47`](../../library/rules/ltp-e9690ab9682fce47.yaml) | The fixture creates TEST_EACCES as a regular file.、The caller lacks a permission required by the operation.、The fixture sets TEST_EACCES mode to MODE_RWX.、The argument is a userspace buffer. | 调用 lstat(TEST_EACCES, &stat_buf) | 返回 -1，errno 为 EACCES |
## `madvise`

共形成 27 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_004E24807F6067A5`](../../library/rules/ltp-004e24807f6067a5.yaml) | 无额外前置条件 | 调用 madvise(sfile, st.st_size, MADV_DOFORK) | 返回 -1，errno 为 EINVAL |
| [`LTP_0E51A1345D29A74B`](../../library/rules/ltp-0e51a1345d29a74b.yaml) | 无额外前置条件 | 调用 madvise(amem, st.st_size, MADV_WIPEONFORK) | 返回 -1，errno 为 EINVAL |
| [`LTP_1A68979B981D8947`](../../library/rules/ltp-1a68979b981d8947.yaml) | 无额外前置条件 | 调用 madvise(target, pg_sz * 3, MADV_WILLNEED) | {'kind': 'return_value', 'return': '-1'} |
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

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_3A18518E9A9DDC47`](../../library/rules/ltp-3a18518e9a9ddc47.yaml) | 无额外前置条件 | 调用 mincore(addr, size, vec) | 调用成功，返回 SUCCESS |
## `mkdir`

没有形成可发布的合规性规则。

## `mkdirat`

共形成 6 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_11C0673F2CC64D66`](../../library/rules/ltp-11c0673f2cc64d66.yaml) | Path resolution encounters a symlink loop. | 调用 mkdirat(cur_fd, test_dir, 0777) | 返回 -1，errno 为 ELOOP |
| [`LTP_6174E3690A05F1CA`](../../library/rules/ltp-6174e3690a05f1ca.yaml) | 无额外前置条件 | 调用 mkdirat(dir_fd, TEST_DIR, 0777) | 返回 -1，errno 为 EROFS |
| [`LTP_C58F92F1259E1474`](../../library/rules/ltp-c58f92f1259e1474.yaml) | Path resolution encounters a symlink loop. | 调用 mkdirat(dir_fd, test_dir, 0777) | 返回 -1，errno 为 ELOOP |
| [`LTP_CD3A79551F6773E4`](../../library/rules/ltp-cd3a79551f6773e4.yaml) | A path component that must be a directory is not a directory. | 调用 mkdirat(fd, relpath, 0600) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_D339D6D98B843BEA`](../../library/rules/ltp-d339d6d98b843bea.yaml) | The file descriptor is invalid. | 调用 mkdirat(fd_invalid, relpath, 0600) | 返回 -1，errno 为 EBADF |
| [`LTP_F6DD03A9DC1C07D4`](../../library/rules/ltp-f6dd03a9dc1c07d4.yaml) | 无额外前置条件 | 调用 mkdirat(cur_fd, TEST_DIR, 0777) | 返回 -1，errno 为 EROFS |
## `mknod`

没有形成可发布的合规性规则。

## `mknodat`

没有形成可发布的合规性规则。

## `mlock`

共形成 5 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_1C1877AB6CAE8906`](../../library/rules/ltp-1c1877ab6cae8906.yaml) | 无额外前置条件 | 调用 mlock(addr, 1024) | 调用成功，返回 SUCCESS |
| [`LTP_C05360D699C55915`](../../library/rules/ltp-c05360d699c55915.yaml) | 无额外前置条件 | 调用 mlock(addr, 1024 * 1024) | 调用成功，返回 SUCCESS |
| [`LTP_E00D911A632EB8C8`](../../library/rules/ltp-e00d911a632eb8c8.yaml) | The argument is a userspace buffer. | 调用 mlock(buf, file_len) | 调用成功，返回 SUCCESS |
| [`LTP_F61B5384B4A60F55`](../../library/rules/ltp-f61b5384b4a60f55.yaml) | 无额外前置条件 | 调用 mlock(addr, 1) | 调用成功，返回 SUCCESS |
| [`LTP_FC50E16C03A7EED9`](../../library/rules/ltp-fc50e16c03a7eed9.yaml) | 无额外前置条件 | 调用 mlock(addr, 1024 * 1024 * 10) | 调用成功，返回 SUCCESS |
## `mlock2`

共形成 9 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_074981FFB7FA5DB7`](../../library/rules/ltp-074981ffb7fa5db7.yaml) | 无额外前置条件 | 调用 mlock2(addr, 2 * pgsz + 1, 0) | 返回 0，errno 为 EINVAL |
| [`LTP_2D13A66AD1AB0813`](../../library/rules/ltp-2d13a66ad1ab0813.yaml) | The file descriptor is invalid. | 调用 mlock2(addr, HPAGES * pgsz + -1, MLOCK_ONFAULT) | 返回 0，errno 为 EINVAL |
| [`LTP_3471B46784E57E93`](../../library/rules/ltp-3471b46784e57e93.yaml) | 无额外前置条件 | 调用 mlock2(addr, PAGES * pgsz + 0, 0) | 返回 0，errno 为 EINVAL |
| [`LTP_592639F40E0FF63A`](../../library/rules/ltp-592639f40e0ff63a.yaml) | 无额外前置条件 | 调用 mlock2(addr, 1 * pgsz + 0, 0) | 返回 0，errno 为 EINVAL |
| [`LTP_7C995D43920E57D0`](../../library/rules/ltp-7c995d43920e57d0.yaml) | 无额外前置条件 | 调用 mlock2(addr, HPAGES * pgsz + 1, MLOCK_ONFAULT) | 返回 0，errno 为 EINVAL |
| [`LTP_8731C07ADFDC57F6`](../../library/rules/ltp-8731c07adfdc57f6.yaml) | 无额外前置条件 | 调用 mlock2(addr, pgsz, MLOCK_ONFAULT) | 返回 0，errno 为 EINVAL |
| [`LTP_998F62DFD40943B2`](../../library/rules/ltp-998f62dfd40943b2.yaml) | The file descriptor is invalid. | 调用 mlock2(addr, 2 * pgsz + -1, 0) | 返回 0，errno 为 EINVAL |
| [`LTP_F7AC6006DC3C06BB`](../../library/rules/ltp-f7ac6006dc3c06bb.yaml) | 无额外前置条件 | 调用 mlock2(addr, PAGES * pgsz + 0, MLOCK_ONFAULT) | 返回 0，errno 为 EINVAL |
| [`LTP_FE9B97F71E485E58`](../../library/rules/ltp-fe9b97f71e485e58.yaml) | 无额外前置条件 | 调用 mlock2(addr, 1 * pgsz + 0, MLOCK_ONFAULT) | 返回 0，errno 为 EINVAL |
## `mlockall`

没有形成可发布的合规性规则。

## `mmap`

共形成 9 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_1F61FDFDC752BFE1`](../../library/rules/ltp-1f61fdfdc752bfe1.yaml) | The caller lacks a permission required by the operation. | 调用 mmap(NULL, MMAPSIZE, PROT_READ | PROT_WRITE, MAP_FILE | MAP_SHARED, fd, 0) | 返回 -1，errno 为 EACCES |
| [`LTP_207043BA148C0097`](../../library/rules/ltp-207043ba148c0097.yaml) | The caller lacks a permission required by the operation. | 调用 mmap(NULL, MMAPSIZE, PROT_WRITE, MAP_FILE | MAP_PRIVATE, fd, 0) | 返回 -1，errno 为 EACCES |
| [`LTP_23FC431E5AACA295`](../../library/rules/ltp-23fc431e5aaca295.yaml) | The caller lacks a permission required by the operation. | 调用 mmap(NULL, MMAPSIZE, PROT_READ, MAP_FILE | MAP_PRIVATE, fd, 0) | 返回 -1，errno 为 EACCES |
| [`LTP_51E295101A9F4411`](../../library/rules/ltp-51e295101a9f4411.yaml) | 无额外前置条件 | 调用 mmap(NULL, 0, PROT_READ | PROT_WRITE, MAP_FILE | MAP_SHARED, fd, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_74D863031FEC1500`](../../library/rules/ltp-74d863031fec1500.yaml) | The caller lacks a permission required by the operation. | 调用 mmap(NULL, MMAPSIZE, PROT_WRITE, MAP_FILE | MAP_SHARED, fd, 0) | 返回 -1，errno 为 EACCES |
| [`LTP_791DEA825D66980B`](../../library/rules/ltp-791dea825d66980b.yaml) | 无额外前置条件 | 调用 mmap(NULL, page_sz, PROT_WRITE, MAP_FILE | MAP_SHARED, fd, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_9495272A3179B794`](../../library/rules/ltp-9495272a3179b794.yaml) | The caller lacks a permission required by the operation. | 调用 mmap(NULL, MMAPSIZE, PROT_READ, MAP_FILE | MAP_SHARED, fd, 0) | 返回 -1，errno 为 EACCES |
| [`LTP_B5F7BCB7225002FC`](../../library/rules/ltp-b5f7bcb7225002fc.yaml) | The caller lacks a permission required by the operation. | 调用 mmap(NULL, MMAPSIZE, PROT_READ | PROT_WRITE, MAP_FILE | MAP_PRIVATE, fd, 0) | 返回 -1，errno 为 EACCES |
| [`LTP_FEACDC300C3E1DD7`](../../library/rules/ltp-feacdc300c3e1dd7.yaml) | 无额外前置条件 | 调用 mmap(NULL, MMAPSIZE, PROT_READ | PROT_WRITE, MAP_FILE, fd, 0) | 返回 -1，errno 为 EINVAL |
## `modify_ldt`

没有形成可发布的合规性规则。

## `mount`

没有形成可发布的合规性规则。

## `mount_setattr`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_5514C74D5CAA93A2`](../../library/rules/ltp-5514c74d5caa93a2.yaml) | The fixture sets slavedir mode to 0777.、The fixture creates slavedir as a directory.、The file descriptor is invalid. | 调用 mount_setattr(-1, slavedir, 0, &attr, sizeof(attr)) | 调用成功，返回 SUCCESS |
| [`LTP_5F50BCA4675B4B03`](../../library/rules/ltp-5f50bca4675b4b03.yaml) | 无额外前置条件 | 调用 mount_setattr(otfd, "", AT_EMPTY_PATH, attr, sizeof(*attr)) | 调用成功，返回 SUCCESS |
## `move_mount`

共形成 7 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_08E6F527B4F8150F`](../../library/rules/ltp-08e6f527b4f8150f.yaml) | The file descriptor is invalid. | 调用 move_mount(fsmfd, "", -1, MNTPOINT, MOVE_MOUNT_F_EMPTY_PATH) | 返回 -1，errno 为 EBADF |
| [`LTP_35AF6D3F6FC0EA61`](../../library/rules/ltp-35af6d3f6fc0ea61.yaml) | 无额外前置条件 | 调用 move_mount(fsmfd, "", AT_FDCWD, MNTPOINT, 0x08) | 返回 -1，errno 为 EINVAL |
| [`LTP_408787CB8F89AAF4`](../../library/rules/ltp-408787cb8f89aaf4.yaml) | 无额外前置条件 | 调用 move_mount(fsmfd, "", AT_FDCWD, MNTPOINT, tc->flags | MOVE_MOUNT_F_EMPTY_PATH) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_7E14411F2FC9D9CF`](../../library/rules/ltp-7e14411f2fc9d9cf.yaml) | 无额外前置条件 | 调用 move_mount(fda, "", fdb, "", MOVE_MOUNT_BENEATH | MOVE_MOUNT_F_EMPTY_PATH | MOVE_MOUNT_T_EMPTY_PATH) | 调用成功，返回 SUCCESS |
| [`LTP_D74B8D7A215A601E`](../../library/rules/ltp-d74b8d7a215a601e.yaml) | The referenced path does not exist. | 调用 move_mount(fsmfd, "", AT_FDCWD, "invalid", MOVE_MOUNT_F_EMPTY_PATH) | 返回 -1，errno 为 ENOENT |
| [`LTP_F122D4A7C853AEBF`](../../library/rules/ltp-f122d4a7c853aebf.yaml) | The referenced path does not exist. | 调用 move_mount(fsmfd, "invalid", AT_FDCWD, MNTPOINT, MOVE_MOUNT_F_EMPTY_PATH) | 返回 -1，errno 为 ENOENT |
| [`LTP_F284E6C48F6B4BF8`](../../library/rules/ltp-f284e6c48f6b4bf8.yaml) | 无额外前置条件 | 调用 move_mount(invalid_fd, "", AT_FDCWD, MNTPOINT, MOVE_MOUNT_F_EMPTY_PATH) | 返回 -1，errno 为 EBADF |
## `move_pages`

没有形成可发布的合规性规则。

## `mprotect`

共形成 8 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_11852F99424BD7E5`](../../library/rules/ltp-11852f99424bd7e5.yaml) | 无额外前置条件 | 调用 mprotect(page_to_copy, page_sz, PROT_READ | PROT_EXEC) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_5DD94B8446C50071`](../../library/rules/ltp-5dd94b8446c50071.yaml) | The argument is a userspace buffer. | 调用 mprotect(addr, sizeof(buf), PROT_WRITE) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_5E2B9548D2D9F147`](../../library/rules/ltp-5e2b9548d2d9f147.yaml) | 无额外前置条件 | 调用 mprotect(p, page_sz, PROT_EXEC) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_60B98F9136CDCB0B`](../../library/rules/ltp-60b98f9136cdcb0b.yaml) | The argument is a userspace buffer. | 调用 mprotect(addr, strlen(buf), PROT_READ) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_86E98E40777EA3FA`](../../library/rules/ltp-86e98e40777ea3fa.yaml) | 无额外前置条件 | 调用 mprotect(addr, page_sz, PROT_NONE) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_F2F310F9646CBB33`](../../library/rules/ltp-f2f310f9646cbb33.yaml) | The caller lacks a permission required by the operation. | 调用 mprotect(NULL, 0, PROT_WRITE) | 返回 -1，errno 为 EACCES |
| [`LTP_FA4A7CD85E7F31FE`](../../library/rules/ltp-fa4a7cd85e7f31fe.yaml) | 无额外前置条件 | 调用 mprotect(NULL, 0, PROT_READ) | 返回 -1，errno 为 ENOMEM |
| [`LTP_FE37A7A30B8E2AFB`](../../library/rules/ltp-fe37a7a30b8e2afb.yaml) | 无额外前置条件 | 调用 mprotect(NULL, 1024, PROT_READ) | 返回 -1，errno 为 EINVAL |
## `mq_notify`

共形成 8 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_11385EF43CBDA2E0`](../../library/rules/ltp-11385ef43cbda2e0.yaml) | 无额外前置条件 | 调用 mq_notify(fd, &ev) | 返回 -1，errno 为 EBUSY |
| [`LTP_148C73A2C00EBA17`](../../library/rules/ltp-148c73a2c00eba17.yaml) | The file descriptor is invalid. | 调用 mq_notify(fd_invalid, &ev) | 返回 -1，errno 为 EBADF |
| [`LTP_462CE9A88054B448`](../../library/rules/ltp-462ce9a88054b448.yaml) | 无额外前置条件 | 调用 mq_notify(0, &({.sigev_notify = SIGEV_SIGNAL, .sigev_signo = _NSIG + 1})) | 返回 -1，errno 为 EINVAL |
| [`LTP_46DC592FFC5E5C44`](../../library/rules/ltp-46dc592ffc5e5c44.yaml) | 无额外前置条件 | 调用 mq_notify(m, NULL) | 调用成功，返回 SUCCESS |
| [`LTP_828E39231372A771`](../../library/rules/ltp-828e39231372a771.yaml) | 无额外前置条件 | 调用 mq_notify(0, &({.sigev_notify = -1})) | 返回 -1，errno 为 EINVAL |
| [`LTP_947B3CCE7DA0998E`](../../library/rules/ltp-947b3cce7da0998e.yaml) | 无额外前置条件 | 调用 mq_notify(fd_maxint, &ev) | 返回 -1，errno 为 EBADF |
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
| [`LTP_1B65027CA2FD0026`](../../library/rules/ltp-1b65027ca2fd0026.yaml) | 无额外前置条件 | 调用 open_by_handle_at(AT_FDCWD, valid_fhp, O_RDWR) | 返回 -1，errno 为 EPERM |
| [`LTP_252F2FFC943C6CCB`](../../library/rules/ltp-252f2ffc943c6ccb.yaml) | Path resolution encounters a symlink loop. | 调用 open_by_handle_at(AT_FDCWD, link_fhp, O_RDWR) | 返回 -1，errno 为 ELOOP |
| [`LTP_3FF54C2EFF286EF7`](../../library/rules/ltp-3ff54c2eff286ef7.yaml) | 无额外前置条件 | 调用 open_by_handle_at(AT_FDCWD, zero_fhp, O_RDWR) | 返回 -1，errno 为 EINVAL |
| [`LTP_4E3E972D7735BC63`](../../library/rules/ltp-4e3e972d7735bc63.yaml) | The file descriptor is invalid. | 调用 open_by_handle_at(-1, valid_fhp, O_RDWR) | 返回 -1，errno 为 EBADF |
| [`LTP_53F53970B961AB32`](../../library/rules/ltp-53f53970b961ab32.yaml) | 无额外前置条件 | 调用 open_by_handle_at(0, valid_fhp, O_RDWR) | 返回 -1，errno 为 ESTALE |
| [`LTP_A48010DFDC346FDE`](../../library/rules/ltp-a48010dfdc346fde.yaml) | The userspace pointer is outside accessible memory. | 调用 open_by_handle_at(AT_FDCWD, invalid_fhp, O_RDWR) | 返回 -1，errno 为 EFAULT |
| [`LTP_E9D60674E416A5DC`](../../library/rules/ltp-e9d60674e416a5dc.yaml) | 无额外前置条件 | 调用 open_by_handle_at(AT_FDCWD, high_fhp, O_RDWR) | 返回 -1，errno 为 EINVAL |
## `open_tree`

没有形成可发布的合规性规则。

## `openat`

没有形成可发布的合规性规则。

## `openat2`

共形成 12 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_026CB4A1CA7CDC6B`](../../library/rules/ltp-026cb4a1ca7cdc6b.yaml) | 无额外前置条件 | 调用 openat2(AT_FDCWD, TEST_FILE, myhow, sizeof(*how) - 1) | 返回 -1，errno 为 EINVAL |
| [`LTP_056DB4870D82DDC3`](../../library/rules/ltp-056db4870d82ddc3.yaml) | Path resolution encounters a symlink loop.、The fixture creates FOO_SYMLINK as a symbolic link. | 调用 openat2(AT_FDCWD, FOO_SYMLINK, how, sizeof(*how)) | 返回 -1，errno 为 ELOOP |
| [`LTP_4101795C27681AB4`](../../library/rules/ltp-4101795c27681ab4.yaml) | 无额外前置条件 | 调用 openat2(AT_FDCWD, TEST_FILE, myhow, sizeof(*how) + 8) | 返回 -1，errno 为 E2BIG |
| [`LTP_57933F1DF2F98C34`](../../library/rules/ltp-57933f1df2f98c34.yaml) | 无额外前置条件 | 调用 openat2(AT_FDCWD, TEST_FILE, myhow, sizeof(*how)) | 返回 -1，errno 为 EINVAL |
| [`LTP_5FB40D053220B092`](../../library/rules/ltp-5fb40d053220b092.yaml) | The userspace pointer is outside accessible memory. | 调用 openat2(AT_FDCWD, TEST_FILE, myhow, sizeof(*how) + 1) | 返回 -1，errno 为 EFAULT |
| [`LTP_7BB1BB36E9CF4892`](../../library/rules/ltp-7bb1bb36e9cf4892.yaml) | The referenced path does not exist. | 调用 openat2(AT_FDCWD, "/proc/version", how, sizeof(*how)) | 返回 -1，errno 为 ENOENT |
| [`LTP_7FEB3B276A8133AC`](../../library/rules/ltp-7feb3b276a8133ac.yaml) | 无额外前置条件 | 调用 openat2(AT_FDCWD, "/proc/version", how, sizeof(*how)) | 返回 -1，errno 为 EXDEV |
| [`LTP_8405B02758433FBC`](../../library/rules/ltp-8405b02758433fbc.yaml) | 无额外前置条件 | 调用 openat2(AT_FDCWD, "../foo", how, sizeof(*how)) | 返回 -1，errno 为 EXDEV |
| [`LTP_B7B7B035608D3637`](../../library/rules/ltp-b7b7b035608d3637.yaml) | The file descriptor is invalid. | 调用 openat2(-1, TEST_FILE, myhow, sizeof(*how)) | 返回 -1，errno 为 EBADF |
| [`LTP_CF4E59775301DA7C`](../../library/rules/ltp-cf4e59775301da7c.yaml) | Path resolution encounters a symlink loop. | 调用 openat2(AT_FDCWD, "/proc/self/exe", how, sizeof(*how)) | 返回 -1，errno 为 ELOOP |
| [`LTP_D0800876342DE939`](../../library/rules/ltp-d0800876342de939.yaml) | 无额外前置条件 | 调用 openat2(AT_FDCWD, TEST_FILE, myhow, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_DD227DB33548452D`](../../library/rules/ltp-dd227db33548452d.yaml) | The userspace pointer is outside accessible memory. | 调用 openat2(AT_FDCWD, NULL, myhow, sizeof(*how)) | 返回 -1，errno 为 EFAULT |
## `pathconf`

共形成 23 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_16343E95C1C7EF47`](../../library/rules/ltp-16343e95c1c7ef47.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_REC_INCR_XFER_SIZE)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_1661259678F899BC`](../../library/rules/ltp-1661259678f899bc.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_PRIO_IO)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_1707E748EA729431`](../../library/rules/ltp-1707e748ea729431.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_MAX_INPUT)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_1893FF0C4930806E`](../../library/rules/ltp-1893ff0c4930806e.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_MAX_CANON)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_1FF6EB837BDD04F1`](../../library/rules/ltp-1ff6eb837bdd04f1.yaml) | Path resolution encounters a symlink loop. | 调用 pathconf(testeloop, 0) | 返回 -1，errno 为 ELOOP |
| [`LTP_2AEF04E122ED7DC9`](../../library/rules/ltp-2aef04e122ed7dc9.yaml) | The file descriptor is invalid. | 调用 pathconf(abs_path, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_4405BEE7215E1BBC`](../../library/rules/ltp-4405bee7215e1bbc.yaml) | The caller lacks a permission required by the operation. | 调用 pathconf(abs_path, 0) | 返回 -1，errno 为 EACCES |
| [`LTP_50BD66A0A05AFE51`](../../library/rules/ltp-50bd66a0a05afe51.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_ASYNC_IO)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_532E8E5A98C0A22D`](../../library/rules/ltp-532e8e5a98c0a22d.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_REC_MIN_XFER_SIZE)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_621EC309C3A75722`](../../library/rules/ltp-621ec309c3a75722.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_NAME_MAX)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_67D824D6D01AC3C8`](../../library/rules/ltp-67d824d6d01ac3c8.yaml) | The pathname exceeds the supported limit. | 调用 pathconf(long_path, 0) | 返回 -1，errno 为 ENAMETOOLONG |
| [`LTP_75354A42F83E3CAC`](../../library/rules/ltp-75354a42f83e3cac.yaml) | The referenced path does not exist. | 调用 pathconf(emptypath, 0) | 返回 -1，errno 为 ENOENT |
| [`LTP_779183F85F2C1278`](../../library/rules/ltp-779183f85f2c1278.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_FILESIZEBITS)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_7C67E10CB5F35EA2`](../../library/rules/ltp-7c67e10cb5f35ea2.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_REC_XFER_ALIGN)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_7FDF0704C50C872E`](../../library/rules/ltp-7fdf0704c50c872e.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_PIPE_BUF)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_81F076122348B68A`](../../library/rules/ltp-81f076122348b68a.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_SYNC_IO)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_913EC5DF431DC6C2`](../../library/rules/ltp-913ec5df431dc6c2.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_NO_TRUNC)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_9445A602B4F98B83`](../../library/rules/ltp-9445a602b4f98b83.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_REC_MAX_XFER_SIZE)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_BF31641F04151F3C`](../../library/rules/ltp-bf31641f04151f3c.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_VDISABLE)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_C544BF068942E8F7`](../../library/rules/ltp-c544bf068942e8f7.yaml) | A path component that must be a directory is not a directory. | 调用 pathconf(fpath, 0) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_C87041F4B4B5A930`](../../library/rules/ltp-c87041f4b4b5a930.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_PATH_MAX)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_DD64353E8E427275`](../../library/rules/ltp-dd64353e8e427275.yaml) | 无额外前置条件 | 调用 pathconf(path, NAME_DESC(_PC_LINK_MAX)) | {'kind': 'return_value', 'return': '-1'} |
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

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_E6A7D5E5327D8ECC`](../../library/rules/ltp-e6a7d5e5327d8ecc.yaml) | 无额外前置条件 | 调用 pidfd_getfd(pidfd, targetfd, 0) | {'kind': 'return_fd', 'return': 'FD'} |
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
| [`LTP_37CFADAF53B6AC9D`](../../library/rules/ltp-37cfadaf53b6ac9d.yaml) | The file descriptor is invalid. | 调用 poll(&pfd, 1, -1) | {'kind': 'return_value', 'return': '1'} |
| [`LTP_403B654FD084895C`](../../library/rules/ltp-403b654fd084895c.yaml) | 无额外前置条件 | 调用 poll(&pfd, 1, 0) | {'kind': 'return_value', 'return': '1'} |
| [`LTP_619E7A5A0D656A90`](../../library/rules/ltp-619e7a5a0d656a90.yaml) | The file descriptor is invalid. | 调用 poll(outfds, 1, -1) | {'kind': 'return_value', 'return': '1'} |
| [`LTP_7EB2F82BA2DF09A2`](../../library/rules/ltp-7eb2f82ba2df09a2.yaml) | The file descriptor is invalid. | 调用 poll(infds, 1, -1) | {'kind': 'return_value', 'return': '1'} |
## `ppoll`

没有形成可发布的合规性规则。

## `prctl`

没有形成可发布的合规性规则。

## `pread64`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_1E3617B704005CFB`](../../library/rules/ltp-1e3617b704005cfb.yaml) | The file descriptor is invalid.、The argument is a userspace buffer. | 调用 pread64(fd, &buf, K1, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_9E17BDBD53A1AC97`](../../library/rules/ltp-9e17bdbd53a1ac97.yaml) | The argument is a userspace buffer. | 调用 pread64(dir_fd, &buf, K1, 0) | 返回 -1，errno 为 EISDIR |
| [`LTP_D95376E3B0469608`](../../library/rules/ltp-d95376e3b0469608.yaml) | The argument is a userspace buffer. | 调用 pread64(pipe_fd[0], &buf, K1, 0) | 返回 -1，errno 为 ESPIPE |
## `preadv`

没有形成可发布的合规性规则。

## `preadv2`

共形成 15 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_15F112E8B77975DD`](../../library/rules/ltp-15f112e8b77975dd.yaml) | The file descriptor is invalid. | 调用 preadv2(fd1, rd_iovec2, 1, 1, -1) | 返回 0，errno 为 EOPNOTSUPP |
| [`LTP_1AACAC53BAF23BA9`](../../library/rules/ltp-1aacac53baf23ba9.yaml) | 无额外前置条件 | 调用 preadv2(fd, iovec, 1, 0, RWF_NOWAIT) | 返回 -1，errno 为 EOPNOTSUPP |
| [`LTP_2A28494F77E0B173`](../../library/rules/ltp-2a28494f77e0b173.yaml) | 无额外前置条件 | 调用 preadv2(fd1, rd_iovec1, 1, 0, 0) | 返回 0，errno 为 EINVAL |
| [`LTP_3EB53CD0B1672EE5`](../../library/rules/ltp-3eb53cd0b1672ee5.yaml) | 无额外前置条件 | 调用 preadv2(fd4, rd_iovec2, 1, 0, 0) | 返回 0，errno 为 EISDIR |
| [`LTP_40E02D5F6A601BC5`](../../library/rules/ltp-40e02d5f6a601bc5.yaml) | The file descriptor is invalid. | 调用 preadv2(fd1, rd_iovec2, -1, 0, 0) | 返回 0，errno 为 EINVAL |
| [`LTP_4839FA2FBA6C97F5`](../../library/rules/ltp-4839fa2fba6c97f5.yaml) | The file descriptor is invalid. | 调用 preadv2(fd, rd_iovec, 2, -1, 0) | {'kind': 'return_value', 'return': 'CHUNK'} |
| [`LTP_5EE8091D4EA8F7AF`](../../library/rules/ltp-5ee8091d4ea8f7af.yaml) | The userspace pointer is outside accessible memory. | 调用 preadv2(fd1, rd_iovec3, 1, 0, 0) | 返回 0，errno 为 EFAULT |
| [`LTP_679924706FAFC4A5`](../../library/rules/ltp-679924706fafc4a5.yaml) | 无额外前置条件 | 调用 preadv2(fd5[0], rd_iovec2, 1, 0, 0) | 返回 0，errno 为 ESPIPE |
| [`LTP_82907DD83DFD7800`](../../library/rules/ltp-82907dd83dfd7800.yaml) | 无额外前置条件 | 调用 preadv2(fd, rd_iovec, 2, off, RWF_NOWAIT) | 返回 CHUNK_SZ + CHUNK_SZ/2，errno 为 EAGAIN |
| [`LTP_93F2091ECF31C3E0`](../../library/rules/ltp-93f2091ecf31c3e0.yaml) | 无额外前置条件 | 调用 preadv2(fd, rd_iovec, 1, CHUNK*3 / 2, 0) | {'kind': 'return_value', 'return': 'CHUNK / 2'} |
| [`LTP_AF0FA27496E3610E`](../../library/rules/ltp-af0fa27496e3610e.yaml) | 无额外前置条件 | 调用 preadv2(fd3, rd_iovec2, 1, 0, 0) | 返回 0，errno 为 EBADF |
| [`LTP_BDB9250DD17C3225`](../../library/rules/ltp-bdb9250dd17c3225.yaml) | The file descriptor is invalid. | 调用 preadv2(fd, rd_iovec, 1, -1, 0) | {'kind': 'return_value', 'return': 'CHUNK'} |
| [`LTP_DC3D9E7D5D1A75DE`](../../library/rules/ltp-dc3d9e7d5d1a75de.yaml) | 无额外前置条件 | 调用 preadv2(fd2, rd_iovec2, 1, 0, 0) | 返回 0，errno 为 EBADF |
| [`LTP_E2360C045F1BCE8E`](../../library/rules/ltp-e2360c045f1bce8e.yaml) | 无额外前置条件 | 调用 preadv2(fd, rd_iovec, 1, 0, 0) | {'kind': 'return_value', 'return': 'CHUNK'} |
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
| [`LTP_0C01151E99096244`](../../library/rules/ltp-0c01151e99096244.yaml) | The file descriptor is invalid.、The argument is a userspace buffer. | 调用 pwrite64(fd, buf, BS, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_4E45B0701D5BD8A7`](../../library/rules/ltp-4e45b0701d5bd8a7.yaml) | 无额外前置条件 | 调用 pwrite64(fd, NULL, 0, 0) | 调用成功，返回 SUCCESS |
| [`LTP_7061ECC5236C3D49`](../../library/rules/ltp-7061ecc5236c3d49.yaml) | The argument is a userspace buffer. | 调用 pwrite64(fd_ro, buf, BS, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_AC9BF5A9B41CD255`](../../library/rules/ltp-ac9bf5a9b41cd255.yaml) | The argument is a userspace buffer. | 调用 pwrite64(inv_fd, buf, BS, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_CC32503F19BF5D53`](../../library/rules/ltp-cc32503f19bf5d53.yaml) | The userspace pointer is outside accessible memory. | 调用 pwrite64(fd, NULL, BS, 0) | 返回 -1，errno 为 EFAULT |
| [`LTP_E61711880DE479B0`](../../library/rules/ltp-e61711880de479b0.yaml) | The argument is a userspace buffer. | 调用 pwrite64(pipe_fds[1], buf, BS, 0) | 返回 -1，errno 为 ESPIPE |
## `pwritev`

没有形成可发布的合规性规则。

## `pwritev2`

共形成 12 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_1F2328B410A3010D`](../../library/rules/ltp-1f2328b410a3010d.yaml) | 无额外前置条件 | 调用 pwritev2(fd1, wr_iovec1, 1, 0, 0) | 返回 0，errno 为 EINVAL |
| [`LTP_296D3DD5B2B27A84`](../../library/rules/ltp-296d3dd5b2b27a84.yaml) | 无额外前置条件 | 调用 pwritev2(fd, wr_iovec, 2, 0, 0) | {'kind': 'return_value', 'return': 'CHUNK'} |
| [`LTP_3152706321BA354E`](../../library/rules/ltp-3152706321ba354e.yaml) | 无额外前置条件 | 调用 pwritev2(fd, wr_iovec, 1, CHUNK / 2, 0) | {'kind': 'return_value', 'return': 'CHUNK'} |
| [`LTP_58F749C9A4ACFFD3`](../../library/rules/ltp-58f749c9a4acffd3.yaml) | The file descriptor is invalid. | 调用 pwritev2(fd1, wr_iovec2, 1, 1, -1) | 返回 0，errno 为 EOPNOTSUPP |
| [`LTP_78A991C666EEFF75`](../../library/rules/ltp-78a991c666eeff75.yaml) | 无额外前置条件 | 调用 pwritev2(fd2, wr_iovec2, 1, 0, 0) | 返回 0，errno 为 EBADF |
| [`LTP_7C0B488884F6689C`](../../library/rules/ltp-7c0b488884f6689c.yaml) | 无额外前置条件 | 调用 pwritev2(fd3, wr_iovec2, 1, 0, 0) | 返回 0，errno 为 EBADF |
| [`LTP_B06B0397728F35C3`](../../library/rules/ltp-b06b0397728f35c3.yaml) | 无额外前置条件 | 调用 pwritev2(fd, wr_iovec, 1, 0, 0) | {'kind': 'return_value', 'return': 'CHUNK'} |
| [`LTP_BADA0A131C4F383E`](../../library/rules/ltp-bada0a131c4f383e.yaml) | The userspace pointer is outside accessible memory. | 调用 pwritev2(fd1, wr_iovec3, 1, 0, 0) | 返回 0，errno 为 EFAULT |
| [`LTP_BDA884D4BEFE09C9`](../../library/rules/ltp-bda884d4befe09c9.yaml) | The file descriptor is invalid. | 调用 pwritev2(fd, wr_iovec, 1, -1, 0) | {'kind': 'return_value', 'return': 'CHUNK'} |
| [`LTP_C05A62F05F2C22E1`](../../library/rules/ltp-c05a62f05f2c22e1.yaml) | The file descriptor is invalid. | 调用 pwritev2(fd, wr_iovec, 2, -1, 0) | {'kind': 'return_value', 'return': 'CHUNK'} |
| [`LTP_DBAE060B9CA303DD`](../../library/rules/ltp-dbae060b9ca303dd.yaml) | 无额外前置条件 | 调用 pwritev2(fd4[0], wr_iovec2, 1, 0, 0) | 返回 0，errno 为 ESPIPE |
| [`LTP_FCD03068DB9BC256`](../../library/rules/ltp-fcd03068db9bc256.yaml) | The file descriptor is invalid. | 调用 pwritev2(fd1, wr_iovec2, -1, 0, 0) | 返回 0，errno 为 EINVAL |
## `quotactl`

没有形成可发布的合规性规则。

## `read`

共形成 8 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0087F445CEB63414`](../../library/rules/ltp-0087f445ceb63414.yaml) | 无额外前置条件 | 调用 read(badfd, bufaddr, 1) | 返回 -1，errno 为 EBADF |
| [`LTP_29BB55727C5A5616`](../../library/rules/ltp-29bb55727c5a5616.yaml) | The argument is a userspace buffer. | 调用 read(fd, buf, SIZE) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_2C266C6067333086`](../../library/rules/ltp-2c266c6067333086.yaml) | 无额外前置条件 | 调用 read(fd, prbuf, BUFSIZ) | {'kind': 'return_value', 'return': 'PALFA_LEN'} |
| [`LTP_5D7B8CB342508B94`](../../library/rules/ltp-5d7b8cb342508b94.yaml) | The userspace pointer is outside accessible memory. | 调用 read(fd3, outside_buf, 1) | 返回 -1，errno 为 EFAULT |
| [`LTP_7F0FE233BE49C811`](../../library/rules/ltp-7f0fe233be49c811.yaml) | 无额外前置条件 | 调用 read(fd2, bufaddr, 1) | 返回 -1，errno 为 EISDIR |
| [`LTP_9F30FD7002BC2EBA`](../../library/rules/ltp-9f30fd7002bc2eba.yaml) | 无额外前置条件 | 调用 read(fd4, addr4, 1) | 返回 -1，errno 为 EINVAL |
| [`LTP_A5BD363654740DDE`](../../library/rules/ltp-a5bd363654740dde.yaml) | 无额外前置条件 | 调用 read(rfd, &c, 1) | 返回 -1，errno 为 EAGAIN |
| [`LTP_C8C667C37A069984`](../../library/rules/ltp-c8c667c37a069984.yaml) | 无额外前置条件 | 调用 read(fd4, addr5, 4096) | 返回 -1，errno 为 EINVAL |
## `readahead`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_AA6F0F0A8A469B13`](../../library/rules/ltp-aa6f0f0a8a469b13.yaml) | 无额外前置条件 | 调用 readahead(fd[0], 0, getpagesize()) | 返回 -1，errno 为 EBADF |
| [`LTP_D9B6B53AB6CA3BE3`](../../library/rules/ltp-d9b6b53ab6ca3be3.yaml) | The file descriptor is invalid. | 调用 readahead(-1, 0, getpagesize()) | 返回 -1，errno 为 EBADF |
## `readdir`

没有形成可发布的合规性规则。

## `readlink`

没有形成可发布的合规性规则。

## `readlinkat`

共形成 12 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_07CE577381BD5611`](../../library/rules/ltp-07ce577381bd5611.yaml) | The file descriptor is invalid.、The fixture creates SYMLINK_FILE as a symbolic link.、The argument is a userspace buffer. | 调用 readlinkat(fd_invalid, SYMLINK_FILE, buf, BUFF_SIZE) | 返回 -1，errno 为 EBADF |
| [`LTP_326165BAA61906DB`](../../library/rules/ltp-326165baa61906db.yaml) | A path component that must be a directory is not a directory.、The argument is a userspace buffer. | 调用 readlinkat(dir_fd, "test_file/test_file", buf, BUFF_SIZE) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_3B07E4E263BECEDE`](../../library/rules/ltp-3b07e4e263becede.yaml) | The argument is a userspace buffer. | 调用 readlinkat(file_fd, abspath, buf, sizeof(buf)) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_45D731F7321AFF41`](../../library/rules/ltp-45d731f7321aff41.yaml) | A path component that must be a directory is not a directory.、The fixture creates SYMLINK_FILE as a symbolic link.、The argument is a userspace buffer. | 调用 readlinkat(file_fd, SYMLINK_FILE, buf, BUFF_SIZE) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_4D5D0A94700C0B71`](../../library/rules/ltp-4d5d0a94700c0b71.yaml) | The referenced path does not exist.、The argument is a userspace buffer. | 调用 readlinkat(dir_fd, "does_not_exists", buf, BUFF_SIZE) | 返回 -1，errno 为 ENOENT |
| [`LTP_835C2BD8D8081213`](../../library/rules/ltp-835c2bd8d8081213.yaml) | The argument is a userspace buffer. | 调用 readlinkat(dir_fd, TEST_FILE, buf, BUFF_SIZE) | 返回 -1，errno 为 EINVAL |
| [`LTP_8D2608F53A58B89C`](../../library/rules/ltp-8d2608f53a58b89c.yaml) | The fixture creates SYMLINK_FILE as a symbolic link.、The argument is a userspace buffer. | 调用 readlinkat(dir_fd, SYMLINK_FILE, buf, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_A38793D253A9BE8C`](../../library/rules/ltp-a38793d253a9be8c.yaml) | The argument is a userspace buffer. | 调用 readlinkat(fd_atcwd, testsymlink, buf, sizeof(buf)) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_BF8A721AF501F7AD`](../../library/rules/ltp-bf8a721af501f7ad.yaml) | The argument is a userspace buffer. | 调用 readlinkat(dir_fd, abspath, buf, sizeof(buf)) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_D5BD925DC43E7564`](../../library/rules/ltp-d5bd925dc43e7564.yaml) | The argument is a userspace buffer. | 调用 readlinkat(fd_atcwd, abspath, buf, sizeof(buf)) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_E733F750B1F4008F`](../../library/rules/ltp-e733f750b1f4008f.yaml) | The argument is a userspace buffer. | 调用 readlinkat(dir_fd, testsymlink, buf, sizeof(buf)) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_FF3F568195A91237`](../../library/rules/ltp-ff3f568195a91237.yaml) | The argument is a userspace buffer. | 调用 readlinkat(dir_fd2, emptypath, buf, sizeof(buf)) | {'kind': 'positive_return', 'return': '>0'} |
## `readv`

没有形成可发布的合规性规则。

## `realpath`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_E2AC7688287A2F9C`](../../library/rules/ltp-e2ac7688287a2f9c.yaml) | The referenced path does not exist. | 调用 realpath(".", NULL) | 返回 -1，errno 为 ENOENT |
## `reboot`

没有形成可发布的合规性规则。

## `recv`

没有形成可发布的合规性规则。

## `recvfrom`

没有形成可发布的合规性规则。

## `recvmmsg`

没有形成可发布的合规性规则。

## `recvmsg`

没有形成可发布的合规性规则。

## `remap_file_pages`

没有形成可发布的合规性规则。

## `removexattr`

没有形成可发布的合规性规则。

## `rename`

共形成 16 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0C4BDB0FD7A306D8`](../../library/rules/ltp-0c4bdb0fd7a306d8.yaml) | The fixture sets TEMP_FILE mode to 0700.、The userspace pointer is outside accessible memory.、The fixture creates TEMP_FILE as a regular file. | 调用 rename(TEMP_FILE, INVALID_PATH) | 返回 -1，errno 为 EFAULT |
| [`LTP_1028A46194A35788`](../../library/rules/ltp-1028a46194a35788.yaml) | 无额外前置条件 | 调用 rename(TEST_EROFS, TEST_NEW_EROFS) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_181653F77A7325D4`](../../library/rules/ltp-181653f77a7325d4.yaml) | The fixture sets TEMP_FILE mode to 0700.、The userspace pointer is outside accessible memory.、The fixture creates TEMP_FILE as a regular file. | 调用 rename(INVALID_PATH, TEMP_FILE) | 返回 -1，errno 为 EFAULT |
| [`LTP_71DD675C657FC49A`](../../library/rules/ltp-71dd675c657fc49a.yaml) | The fixture sets TEMP_FILE mode to 0700.、The fixture creates TEMP_DIR as a directory.、The fixture creates TEMP_FILE as a regular file.、The fixture sets TEMP_DIR mode to 00770. | 调用 rename(TEMP_FILE, TEMP_DIR) | 返回 -1，errno 为 EISDIR |
| [`LTP_7ED6923454F08CDA`](../../library/rules/ltp-7ed6923454f08cda.yaml) | The fixture sets SRCFILE mode to PERMS.、The caller lacks a permission required by the operation.、The fixture sets DESTFILE mode to PERMS.、The fixture creates SRCFILE as a regular file.、The fixture creates DESTFILE as a regular file. | 调用 rename(SRCFILE, DESTFILE) | 返回 -1，errno 为 EACCES |
| [`LTP_7FC732FCCE410925`](../../library/rules/ltp-7fc732fcce410925.yaml) | The pathname exceeds the supported limit.、The fixture sets TEMP_FILE mode to 0700.、The fixture creates TEMP_FILE as a regular file. | 调用 rename(TEMP_FILE, long_path) | 返回 -1，errno 为 ENAMETOOLONG |
| [`LTP_83B1DE66214C655F`](../../library/rules/ltp-83b1de66214c655f.yaml) | The fixture creates TEMP_FILE1 as a regular file.、The fixture sets TEMP_FILE1 mode to 0700. | 调用 rename(TEMP_FILE1, TEMP_FILE2) | 返回 -1，errno 为 EPERM |
| [`LTP_95C3A1596DE75C5C`](../../library/rules/ltp-95c3a1596de75c5c.yaml) | The fixture creates old_dir_name as a directory.、The fixture sets old_dir_name mode to 00770. | 调用 rename(old_dir_name, new_dir_name) | 调用成功，返回 SUCCESS |
| [`LTP_A8161E50B040AFC9`](../../library/rules/ltp-a8161e50b040afc9.yaml) | A path component that must be a directory is not a directory.、The fixture sets TEMP_FILE mode to 0700.、The fixture creates TEMP_DIR as a directory.、The fixture creates TEMP_FILE as a regular file.、The fixture sets TEMP_DIR mode to 00770. | 调用 rename(TEMP_DIR, TEMP_FILE) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_B09A317822F38991`](../../library/rules/ltp-b09a317822f38991.yaml) | The pathname exceeds the supported limit.、The fixture sets TEMP_FILE mode to 0700.、The fixture creates TEMP_FILE as a regular file. | 调用 rename(TEMP_FILE, long_name) | 返回 -1，errno 为 ENAMETOOLONG |
| [`LTP_C532732193F3A009`](../../library/rules/ltp-c532732193f3a009.yaml) | The fixture creates NEW_DIR_NAME as a directory.、The fixture creates OLD_DIR_NAME as a directory.、The fixture sets OLD_DIR_NAME mode to 00770.、The fixture sets NEW_DIR_NAME mode to 00770. | 调用 rename(OLD_DIR_NAME, NEW_DIR_NAME) | 调用成功，返回 SUCCESS |
| [`LTP_D17799C1BB191952`](../../library/rules/ltp-d17799c1bb191952.yaml) | 无额外前置条件 | 调用 rename(TEST_EMLINK, TEST_NEW_EMLINK) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_D7B9E8F8F713AADA`](../../library/rules/ltp-d7b9e8f8f713aada.yaml) | The fixture creates old_file_name as a regular file.、The fixture sets old_file_name mode to 0700. | 调用 rename(old_file_name, new_file_name) | 调用成功，返回 SUCCESS |
| [`LTP_D98D789F4EBA6817`](../../library/rules/ltp-d98d789f4eba6817.yaml) | 无额外前置条件 | 调用 rename(elooppathname, TEST_NEW_ELOOP) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_DA61AB6388EB2D13`](../../library/rules/ltp-da61ab6388eb2d13.yaml) | The fixture creates OLD_FILE_NAME as a regular file.、The fixture creates NEW_FILE_NAME as a regular file.、The fixture sets NEW_FILE_NAME mode to 0700.、The fixture sets OLD_FILE_NAME mode to 0700. | 调用 rename(OLD_FILE_NAME, NEW_FILE_NAME) | 调用成功，返回 SUCCESS |
| [`LTP_DDC2A75ACE241003`](../../library/rules/ltp-ddc2a75ace241003.yaml) | The fixture creates TEMP_FILE1 as a regular file.、The fixture sets TEMP_FILE1 mode to 0700. | 调用 rename(TEMP_FILE1, TEMP_FILE1) | 调用成功，返回 SUCCESS |
## `renameat`

没有形成可发布的合规性规则。

## `renameat2`

没有形成可发布的合规性规则。

## `request_key`

共形成 10 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_06F742EF42AA55BA`](../../library/rules/ltp-06f742ef42aa55ba.yaml) | 无额外前置条件 | 调用 request_key(".type", "description", NULL, KEY_SPEC_PROCESS_KEYRING) | 返回 -1，errno 为 EPERM |
| [`LTP_078A6E34EE607719`](../../library/rules/ltp-078a6e34ee607719.yaml) | The userspace pointer is outside accessible memory.、The file descriptor is invalid. | 调用 request_key((char *)(-1), "description", NULL, KEY_SPEC_PROCESS_KEYRING) | 返回 -1，errno 为 EFAULT |
| [`LTP_0A819CDD66F1C6A1`](../../library/rules/ltp-0a819cdd66f1c6a1.yaml) | 无额外前置条件 | 调用 request_key("keyring", "ltp1", NULL, key1) | 返回 -1，errno 为 ENOKEY |
| [`LTP_1BDC4A832DB89410`](../../library/rules/ltp-1bdc4a832db89410.yaml) | 无额外前置条件 | 调用 request_key("user", "desc", "callout_info", 0) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_4F41926D0ED26FBA`](../../library/rules/ltp-4f41926d0ed26fba.yaml) | The userspace pointer is outside accessible memory.、The file descriptor is invalid. | 调用 request_key("type", (char *)(-1), NULL, KEY_SPEC_PROCESS_KEYRING) | 返回 -1，errno 为 EFAULT |
| [`LTP_A86F28C4D1358669`](../../library/rules/ltp-a86f28c4d1358669.yaml) | The userspace pointer is outside accessible memory.、The file descriptor is invalid. | 调用 request_key("type", "description", (char *)(-1), KEY_SPEC_PROCESS_KEYRING) | 返回 -1，errno 为 EFAULT |
| [`LTP_D90C4B47C5FF6BC9`](../../library/rules/ltp-d90c4b47c5ff6bc9.yaml) | 无额外前置条件 | 调用 request_key("keyring", "ltp2", NULL, key2) | 返回 -1，errno 为 EKEYREVOKED |
| [`LTP_E7E64809057630A5`](../../library/rules/ltp-e7e64809057630a5.yaml) | 无额外前置条件 | 调用 request_key(type, "desc", "callout_info", KEY_SPEC_SESSION_KEYRING) | 返回 -1，errno 为 ENOKEY |
| [`LTP_E98952E12501919D`](../../library/rules/ltp-e98952e12501919d.yaml) | 无额外前置条件 | 调用 request_key("keyring", "ltp3", NULL, key3) | 返回 -1，errno 为 EKEYEXPIRED |
| [`LTP_EA58792F115B6235`](../../library/rules/ltp-ea58792f115b6235.yaml) | 无额外前置条件 | 调用 request_key("keyring", "ltp", NULL, KEY_REQKEY_DEFL_DEFAULT) | {'kind': 'positive_return', 'return': '>0'} |
## `rmdir`

没有形成可发布的合规性规则。

## `rt_sigaction`

没有形成可发布的合规性规则。

## `rt_sigprocmask`

共形成 4 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_423E92D9328C2A39`](../../library/rules/ltp-423e92d9328c2a39.yaml) | 无额外前置条件 | 调用 rt_sigprocmask(SIG_UNBLOCK, &set, &oset, SIGSETSIZE) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_485A86C9CB172FBF`](../../library/rules/ltp-485a86c9cb172fbf.yaml) | The userspace pointer is outside accessible memory. | 调用 rt_sigprocmask(SIG_BLOCK, &s, (sigset_t *) - 1, SIGSETSIZE) | 返回 0，errno 为 EFAULT |
| [`LTP_79D2E6DA4FED3FBC`](../../library/rules/ltp-79d2e6da4fed3fbc.yaml) | 无额外前置条件 | 调用 rt_sigprocmask(SIG_BLOCK, &set, &oset, SIGSETSIZE) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_FE57D3FF371E3DDC`](../../library/rules/ltp-fe57d3ff371e3ddc.yaml) | 无额外前置条件 | 调用 rt_sigprocmask(SIG_BLOCK, &s, &set, 1) | 返回 0，errno 为 EINVAL |
## `rt_sigqueueinfo`

没有形成可发布的合规性规则。

## `rt_sigsuspend`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0324F0A6601FFECE`](../../library/rules/ltp-0324f0a6601ffece.yaml) | 无额外前置条件 | 调用 rt_sigsuspend(&set, SIGSETSIZE) | 返回 -1，errno 为 EINTR |
## `rt_sigtimedwait`

没有形成可发布的合规性规则。

## `rt_tgsigqueueinfo`

没有形成可发布的合规性规则。

## `sbrk`

共形成 4 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_03FD233DFE92488D`](../../library/rules/ltp-03fd233dfe92488d.yaml) | 无额外前置条件 | 调用 sbrk(8192) | 调用成功，返回 SUCCESS |
| [`LTP_139142311CF01E20`](../../library/rules/ltp-139142311cf01e20.yaml) | 无额外前置条件 | 调用 sbrk(-8192) | 调用成功，返回 SUCCESS |
| [`LTP_636EE8AC66A970F6`](../../library/rules/ltp-636ee8ac66a970f6.yaml) | 无额外前置条件 | 调用 sbrk(0) | 调用成功，返回 SUCCESS |
| [`LTP_CB42FAF7C1D6D702`](../../library/rules/ltp-cb42faf7c1d6d702.yaml) | 无额外前置条件 | 调用 sbrk(increment) | 返回 -1，errno 为 ENOMEM |
## `sched_get_priority_max`

没有形成可发布的合规性规则。

## `sched_get_priority_min`

没有形成可发布的合规性规则。

## `sched_getaffinity`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_2CB0A10A3E175A9C`](../../library/rules/ltp-2cb0a10a3e175a9c.yaml) | 无额外前置条件 | 调用 sched_getaffinity(0, len, mask) | 返回 -1，errno 为 EINVAL |
## `sched_getattr`

共形成 4 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0A2035C9A2A77F66`](../../library/rules/ltp-0a2035c9a2a77f66.yaml) | 无额外前置条件 | 调用 sched_getattr(unused_pid, &attr_copy, sizeof(struct sched_attr), 0) | 返回 -1，errno 为 ESRCH |
| [`LTP_8B95C6DD7983D3F3`](../../library/rules/ltp-8b95c6dd7983d3f3.yaml) | 无额外前置条件 | 调用 sched_getattr(pid, &attr_copy, sizeof(struct sched_attr), 1000) | 返回 -1，errno 为 EINVAL |
| [`LTP_95C156C7EBB823A1`](../../library/rules/ltp-95c156c7ebb823a1.yaml) | 无额外前置条件 | 调用 sched_getattr(pid, NULL, sizeof(struct sched_attr), 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_FA750E6088863E30`](../../library/rules/ltp-fa750e6088863e30.yaml) | 无额外前置条件 | 调用 sched_getattr(pid, &attr_copy, SCHED_ATTR_SIZE_VER0 - 1, 0) | 返回 -1，errno 为 EINVAL |
## `sched_getparam`

没有形成可发布的合规性规则。

## `sched_getscheduler`

没有形成可发布的合规性规则。

## `sched_rr_get_interval`

没有形成可发布的合规性规则。

## `sched_setaffinity`

共形成 4 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_5818495120E9862A`](../../library/rules/ltp-5818495120e9862a.yaml) | The userspace pointer is outside accessible memory. | 调用 sched_setaffinity(self_pid, mask_size, fmask) | 返回 -1，errno 为 EFAULT |
| [`LTP_585CC852338F38EE`](../../library/rules/ltp-585cc852338f38ee.yaml) | 无额外前置条件 | 调用 sched_setaffinity(self_pid, emask_size, emask) | 返回 -1，errno 为 EINVAL |
| [`LTP_97D64C0E53AA3FA4`](../../library/rules/ltp-97d64c0e53aa3fa4.yaml) | 无额外前置条件 | 调用 sched_setaffinity(free_pid, mask_size, mask) | 返回 -1，errno 为 ESRCH |
| [`LTP_D23BA34DB5624198`](../../library/rules/ltp-d23ba34db5624198.yaml) | 无额外前置条件 | 调用 sched_setaffinity(privileged_pid, mask_size, mask) | 返回 -1，errno 为 EPERM |
## `sched_setattr`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_4BA2A081C3EB3304`](../../library/rules/ltp-4ba2a081c3eb3304.yaml) | 无额外前置条件 | 调用 sched_setattr(pid, &attr, 1000) | 返回 -1，errno 为 EINVAL |
| [`LTP_A55106AB533523B0`](../../library/rules/ltp-a55106ab533523b0.yaml) | 无额外前置条件 | 调用 sched_setattr(pid, NULL, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_DC7E9134BB7F6F7A`](../../library/rules/ltp-dc7e9134bb7f6f7a.yaml) | 无额外前置条件 | 调用 sched_setattr(unused_pid, &attr, 0) | 返回 -1，errno 为 ESRCH |
## `sched_setparam`

没有形成可发布的合规性规则。

## `sched_setscheduler`

没有形成可发布的合规性规则。

## `sched_yield`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_A9BC7EBC1784A722`](../../library/rules/ltp-a9bc7ebc1784a722.yaml) | 无额外前置条件 | 调用 sched_yield() | {'kind': 'return_value', 'return': '0'} |
## `seccomp`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_38B9BA93F16FBAAF`](../../library/rules/ltp-38b9ba93f16fbaaf.yaml) | 无额外前置条件 | 调用 seccomp(SECCOMP_SET_MODE_FILTER, 0, &strict) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_FCC82752F512BE72`](../../library/rules/ltp-fcc82752f512be72.yaml) | 无额外前置条件 | 调用 seccomp(SECCOMP_SET_MODE_STRICT, 0, NULL) | {'kind': 'return_value', 'return': '-1'} |
## `select`

没有形成可发布的合规性规则。

## `send`

没有形成可发布的合规性规则。

## `sendfile`

共形成 12 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_38EE9A0047529979`](../../library/rules/ltp-38ee9a0047529979.yaml) | 无额外前置条件 | 调用 sendfile(out_fd, in_fd, NULL, strlen(TEST_MSG_IN)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_39B1E5C574F2D3DC`](../../library/rules/ltp-39b1e5c574f2d3dc.yaml) | 无额外前置条件 | 调用 sendfile(out_fd, negative_fd, NULL, 1) | 返回 -1，errno 为 EBADF |
| [`LTP_3C1DCCC4E6DCC76B`](../../library/rules/ltp-3c1dccc4e6dcc76b.yaml) | 无额外前置条件 | 调用 sendfile(out_fd, out_fd, NULL, 1) | 返回 -1，errno 为 EBADF |
| [`LTP_4A5C15DAE55BBD2E`](../../library/rules/ltp-4a5c15dae55bbd2e.yaml) | 无额外前置条件 | 调用 sendfile(out_fd, in_fd, &offset, ONE_GB) | {'kind': 'return_value', 'return': 'ONE_GB'} |
| [`LTP_5A68AEA67C7612A0`](../../library/rules/ltp-5a68aea67c7612a0.yaml) | 无额外前置条件 | 调用 sendfile(out_fd, in_fd, &offset, 1) | 返回 -1，errno 为 EINVAL |
| [`LTP_7BC885B5878C95B6`](../../library/rules/ltp-7bc885b5878c95b6.yaml) | 无额外前置条件 | 调用 sendfile(negative_fd, in_fd, NULL, 1) | 返回 -1，errno 为 EBADF |
| [`LTP_90AA1F0CFA6C6A5C`](../../library/rules/ltp-90aa1f0cfa6c6a5c.yaml) | The userspace pointer is outside accessible memory. | 调用 sendfile(out_fd, in_fd, protected_buffer, 1) | 返回 -1，errno 为 EFAULT |
| [`LTP_A49B95E01ADFC6F8`](../../library/rules/ltp-a49b95e01adfc6f8.yaml) | 无额外前置条件 | 调用 sendfile(out_fd, in_fd, NULL, sb.st_size) | {'kind': 'return_value', 'return': 'st_size'} |
| [`LTP_A54F3585CC70C99F`](../../library/rules/ltp-a54f3585cc70c99f.yaml) | 无额外前置条件 | 调用 sendfile(out_fd, in_fd, &offset, 26) | {'kind': 'return_value', 'return': '26'} |
| [`LTP_CB84D44C84EB80BE`](../../library/rules/ltp-cb84d44c84eb80be.yaml) | 无额外前置条件 | 调用 sendfile(out_fd, in_fd, NULL, 1) | 返回 -1，errno 为 EAGAIN |
| [`LTP_D01667E52BF34BFC`](../../library/rules/ltp-d01667e52bf34bfc.yaml) | 无额外前置条件 | 调用 sendfile(in_fd, in_fd, NULL, 1) | 返回 -1，errno 为 EBADF |
| [`LTP_D3E85F64C28BBC4F`](../../library/rules/ltp-d3e85f64c28bbc4f.yaml) | 无额外前置条件 | 调用 sendfile(out_fd, in_fd, &offset, 24) | {'kind': 'return_value', 'return': '26'} |
## `sendmmsg`

没有形成可发布的合规性规则。

## `sendmsg`

没有形成可发布的合规性规则。

## `sendto`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_4C4EE05D029C81F3`](../../library/rules/ltp-4c4ee05d029c81f3.yaml) | The userspace pointer is outside accessible memory. | 调用 sendto(sockfd, NULL, 1, 0, (struct sockaddr *) &sa, sizeof(sa)) | 返回 -1，errno 为 EFAULT |
## `set_mempolicy`

没有形成可发布的合规性规则。

## `set_robust_list`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_A89D10D41C3C2A1C`](../../library/rules/ltp-a89d10d41c3c2a1c.yaml) | The file descriptor is invalid. | 调用 set_robust_list(&head, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_E0470C189C2D1DE3`](../../library/rules/ltp-e0470c189c2d1de3.yaml) | 无额外前置条件 | 调用 set_robust_list(&head, len) | {'kind': 'return_value', 'return': '0'} |
## `set_thread_area`

没有形成可发布的合规性规则。

## `set_tid_address`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_738C27178BBCE2B1`](../../library/rules/ltp-738c27178bbce2b1.yaml) | 无额外前置条件 | 调用 set_tid_address(&newtid) | {'kind': 'return_value', 'return': 'getpid()'} |
## `setdomainname`

没有形成可发布的合规性规则。

## `setegid`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_E2D73477ACB0308D`](../../library/rules/ltp-e2d73477acb0308d.yaml) | 无额外前置条件 | 调用 setegid(ltpuser->pw_gid) | 返回 -1，errno 为 EPERM |
## `setfsgid`

没有形成可发布的合规性规则。

## `setfsuid`

没有形成可发布的合规性规则。

## `setgid`

没有形成可发布的合规性规则。

## `setgroups`

没有形成可发布的合规性规则。

## `sethostname`

没有形成可发布的合规性规则。

## `setitimer`

没有形成可发布的合规性规则。

## `setns`

没有形成可发布的合规性规则。

## `setpgid`

共形成 8 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0C5623B3D5C7430F`](../../library/rules/ltp-0c5623b3d5c7430f.yaml) | 无额外前置条件 | 调用 setpgid(0, 0) | 调用成功，返回 SUCCESS |
| [`LTP_37F4EFF424BB79B9`](../../library/rules/ltp-37f4eff424bb79b9.yaml) | The caller lacks a permission required by the operation. | 调用 setpgid(child_pid, getppid()) | 返回 -1，errno 为 EACCES |
| [`LTP_4308D71D8BD6519D`](../../library/rules/ltp-4308d71d8bd6519d.yaml) | 无额外前置条件 | 调用 setpgid(pid, negative_pid) | 返回 -1，errno 为 EINVAL |
| [`LTP_4BBF626715445EFC`](../../library/rules/ltp-4bbf626715445efc.yaml) | 无额外前置条件 | 调用 setpgid(ppid, pgid) | 返回 -1，errno 为 ESRCH |
| [`LTP_503160311D12E629`](../../library/rules/ltp-503160311d12e629.yaml) | 无额外前置条件 | 调用 setpgid(pid, pgid) | 调用成功，返回 SUCCESS |
| [`LTP_9FC19C1455EBA67E`](../../library/rules/ltp-9fc19c1455eba67e.yaml) | 无额外前置条件 | 调用 setpgid(0, child_pid) | 返回 -1，errno 为 EPERM |
| [`LTP_CF7B49C4B74D69E7`](../../library/rules/ltp-cf7b49c4b74d69e7.yaml) | 无额外前置条件 | 调用 setpgid(pid, inval_pgid) | 返回 -1，errno 为 EPERM |
| [`LTP_DBEC3975C5440D23`](../../library/rules/ltp-dbec3975c5440d23.yaml) | 无额外前置条件 | 调用 setpgid(child_pid, getppid()) | 返回 -1，errno 为 EPERM |
## `setpgrp`

没有形成可发布的合规性规则。

## `setpriority`

共形成 10 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_252DC2EE1F2FC3AC`](../../library/rules/ltp-252dc2ee1f2fc3ac.yaml) | 无额外前置条件 | 调用 setpriority(PRIO_USER, INVAL_ID, NEW_PRIO) | 返回 -1，errno 为 ESRCH |
| [`LTP_336B0AA063AB645E`](../../library/rules/ltp-336b0aa063ab645e.yaml) | 无额外前置条件 | 调用 setpriority(PRIO_USER, uid, new_prio) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_44DC5382746D773D`](../../library/rules/ltp-44dc5382746d773d.yaml) | 无额外前置条件 | 调用 setpriority(INVAL_FLAG, 0, NEW_PRIO) | 返回 -1，errno 为 EINVAL |
| [`LTP_50853944DA25B2E0`](../../library/rules/ltp-50853944da25b2e0.yaml) | 无额外前置条件 | 调用 setpriority(PRIO_PGRP, INVAL_ID, NEW_PRIO) | 返回 -1，errno 为 ESRCH |
| [`LTP_757778388A97EE03`](../../library/rules/ltp-757778388a97ee03.yaml) | 无额外前置条件 | 调用 setpriority(PRIO_PROCESS, pid, new_prio) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_933D919373F0F77C`](../../library/rules/ltp-933d919373f0f77c.yaml) | The caller lacks a permission required by the operation. | 调用 setpriority(PRIO_PROCESS, 0, NEW_PRIO) | 返回 -1，errno 为 EACCES |
| [`LTP_9D4E5ED344B5751D`](../../library/rules/ltp-9d4e5ed344b5751d.yaml) | 无额外前置条件 | 调用 setpriority(PRIO_PROCESS, INIT_PID, NEW_PRIO) | 返回 -1，errno 为 EPERM |
| [`LTP_AF52DA4E6DA2BC9B`](../../library/rules/ltp-af52da4e6da2bc9b.yaml) | 无额外前置条件 | 调用 setpriority(PRIO_PROCESS, INVAL_ID, NEW_PRIO) | 返回 -1，errno 为 ESRCH |
| [`LTP_B6D4B61FC2494298`](../../library/rules/ltp-b6d4b61fc2494298.yaml) | The caller lacks a permission required by the operation. | 调用 setpriority(PRIO_PGRP, 0, NEW_PRIO) | 返回 -1，errno 为 EACCES |
| [`LTP_BB4C88C7C212DAC7`](../../library/rules/ltp-bb4c88c7c212dac7.yaml) | 无额外前置条件 | 调用 setpriority(PRIO_PGRP, pid, new_prio) | {'kind': 'return_value', 'return': '0'} |
## `setregid`

没有形成可发布的合规性规则。

## `setresgid`

没有形成可发布的合规性规则。

## `setresuid`

没有形成可发布的合规性规则。

## `setreuid`

没有形成可发布的合规性规则。

## `setrlimit`

没有形成可发布的合规性规则。

## `setsid`

没有形成可发布的合规性规则。

## `setsockopt`

没有形成可发布的合规性规则。

## `settimeofday`

共形成 4 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_69DB4FB0496BC7A2`](../../library/rules/ltp-69db4fb0496bc7a2.yaml) | 无额外前置条件 | 调用 settimeofday(&{-1, 0}, NULL) | 返回 -1，errno 为 EINVAL |
| [`LTP_8D95C734339E42C6`](../../library/rules/ltp-8d95c734339e42c6.yaml) | 无额外前置条件 | 调用 settimeofday(&{0, -1}, NULL) | 返回 -1，errno 为 EINVAL |
| [`LTP_B549A3600766CD49`](../../library/rules/ltp-b549a3600766cd49.yaml) | 无额外前置条件 | 调用 settimeofday(&tv1, NULL) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_BC4FACB4E14118C5`](../../library/rules/ltp-bc4facb4e14118c5.yaml) | 无额外前置条件 | 调用 settimeofday(&{100, 100}, NULL) | 返回 -1，errno 为 EPERM |
## `setuid`

没有形成可发布的合规性规则。

## `setxattr`

没有形成可发布的合规性规则。

## `sgetmask`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_5560FF1D5C7F4B90`](../../library/rules/ltp-5560ff1d5c7f4b90.yaml) | 无额外前置条件 | 调用 sgetmask() | {'kind': 'return_value', 'return': 'sig'} |
## `shutdown`

没有形成可发布的合规性规则。

## `sigaction`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_60398013DD319A2E`](../../library/rules/ltp-60398013dd319a2e.yaml) | 无额外前置条件 | 调用 sigaction(SIGUSR1, &sa, NULL) | {'kind': 'return_value', 'return': '0'} |
## `sigaltstack`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_612BF74E1426528A`](../../library/rules/ltp-612bf74e1426528a.yaml) | 无额外前置条件 | 调用 sigaltstack(&sigstk, &osigstk) | {'kind': 'return_value', 'return': '-1'} |
## `sighold`

没有形成可发布的合规性规则。

## `signal`

没有形成可发布的合规性规则。

## `signalfd`

共形成 5 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_07FCC99E3AE43064`](../../library/rules/ltp-07fcc99e3ae43064.yaml) | 无额外前置条件 | 调用 signalfd(fd_ebadf, mask, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_0D9B02C95396CCDC`](../../library/rules/ltp-0d9b02c95396ccdc.yaml) | 无额外前置条件 | 调用 signalfd(fd_einval1, mask, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_2668EE4D34576C49`](../../library/rules/ltp-2668ee4d34576c49.yaml) | 无额外前置条件 | 调用 signalfd(fd_signal, &mask1, 0) | {'kind': 'return_fd', 'return': 'FD'} |
| [`LTP_644B7DB483FF489B`](../../library/rules/ltp-644b7db483ff489b.yaml) | 无额外前置条件 | 调用 signalfd(fd_signal, &mask2, 0) | {'kind': 'return_fd', 'return': 'FD'} |
| [`LTP_8BDD5A2DD306EFC4`](../../library/rules/ltp-8bdd5a2dd306efc4.yaml) | The file descriptor is invalid. | 调用 signalfd(fd_einval2, mask, -1) | 返回 -1，errno 为 EINVAL |
## `signalfd4`

没有形成可发布的合规性规则。

## `sigpending`

没有形成可发布的合规性规则。

## `sigprocmask`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_B061BD44067799D7`](../../library/rules/ltp-b061bd44067799d7.yaml) | 无额外前置条件 | 调用 sigprocmask(SIG_BLOCK, &set, 0) | {'kind': 'return_value', 'return': '-1'} |
## `sigrelse`

没有形成可发布的合规性规则。

## `sigsuspend`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_55D2492560C39AFD`](../../library/rules/ltp-55d2492560c39afd.yaml) | 无额外前置条件 | 调用 sigsuspend(&signalset) | 返回 -1，errno 为 EINTR |
| [`LTP_6C1DF45A5C274B15`](../../library/rules/ltp-6c1df45a5c274b15.yaml) | The userspace pointer is outside accessible memory. | 调用 sigsuspend(invalid_mask) | 返回 -1，errno 为 EFAULT |
## `sigtimedwait`

没有形成可发布的合规性规则。

## `sigwait`

没有形成可发布的合规性规则。

## `sigwaitinfo`

没有形成可发布的合规性规则。

## `socket`

共形成 6 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_6B29B31CE99466E6`](../../library/rules/ltp-6b29b31ce99466e6.yaml) | 无额外前置条件 | 调用 socket(PF_INET, SOCK_DGRAM, 6) | 返回 -1，errno 为 EPROTONOSUPPORT |
| [`LTP_971DB17D32C51561`](../../library/rules/ltp-971db17d32c51561.yaml) | 无额外前置条件 | 调用 socket(PF_INET, 75, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_A4A662687B98D33F`](../../library/rules/ltp-a4a662687b98d33f.yaml) | 无额外前置条件 | 调用 socket(PF_INET, SOCK_STREAM, 1) | 返回 -1，errno 为 EPROTONOSUPPORT |
| [`LTP_AF8D38878ED1A9DA`](../../library/rules/ltp-af8d38878ed1a9da.yaml) | 无额外前置条件 | 调用 socket(0, SOCK_STREAM, 0) | 返回 -1，errno 为 EAFNOSUPPORT |
| [`LTP_DD2E1A555B603C7B`](../../library/rules/ltp-dd2e1a555b603c7b.yaml) | 无额外前置条件 | 调用 socket(PF_INET, SOCK_STREAM, 17) | 返回 -1，errno 为 EPROTONOSUPPORT |
| [`LTP_E316C28E36E136DA`](../../library/rules/ltp-e316c28e36e136da.yaml) | 无额外前置条件 | 调用 socket(PF_INET, SOCK_RAW, 0) | 返回 -1，errno 为 EPROTONOSUPPORT |
## `socketcall`

没有形成可发布的合规性规则。

## `socketpair`

没有形成可发布的合规性规则。

## `sockioctl`

没有形成可发布的合规性规则。

## `splice`

没有形成可发布的合规性规则。

## `ssetmask`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_8CFEBBA603A7011A`](../../library/rules/ltp-8cfebba603a7011a.yaml) | 无额外前置条件 | 调用 ssetmask(SIGUSR1) | {'kind': 'return_value', 'return': 'SIGALRM'} |
## `stat`

没有形成可发布的合规性规则。

## `statfs`

没有形成可发布的合规性规则。

## `statmount`

没有形成可发布的合规性规则。

## `statvfs`

没有形成可发布的合规性规则。

## `statx`

没有形成可发布的合规性规则。

## `stime`

没有形成可发布的合规性规则。

## `string`

没有形成可发布的合规性规则。

## `swapoff`

没有形成可发布的合规性规则。

## `swapon`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_66AC645038FEFC7A`](../../library/rules/ltp-66ac645038fefc7a.yaml) | 无额外前置条件 | 调用 swapon(TEST_FILE, 0) | 返回 -1，errno 为 EPERM |
## `switch`

没有形成可发布的合规性规则。

## `symlink`

共形成 9 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_1551C6F53CF6865A`](../../library/rules/ltp-1551c6f53cf6865a.yaml) | The referenced path does not exist. | 调用 symlink(test_file, sym_file) | 返回 -1，errno 为 ENOENT |
| [`LTP_29873BE2A9AABFF4`](../../library/rules/ltp-29873be2a9aabff4.yaml) | 无额外前置条件 | 调用 symlink(nonfile, SYMFILE) | 调用成功，返回 SUCCESS |
| [`LTP_2EF9C7EBEC450E9D`](../../library/rules/ltp-2ef9c7ebec450e9d.yaml) | The caller lacks a permission required by the operation. | 调用 symlink(test_file, sym_file) | 返回 -1，errno 为 EACCES |
| [`LTP_34A1F75164462203`](../../library/rules/ltp-34a1f75164462203.yaml) | A path component that must be a directory is not a directory. | 调用 symlink(test_file, sym_file) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_80C28F63B3DFD8B1`](../../library/rules/ltp-80c28f63b3dfd8b1.yaml) | The target object already exists. | 调用 symlink(test_file, sym_file) | 返回 -1，errno 为 EEXIST |
| [`LTP_8ED8688C6292FECF`](../../library/rules/ltp-8ed8688c6292fecf.yaml) | 无额外前置条件 | 调用 symlink(testfile, SYMFILE) | 调用成功，返回 SUCCESS |
| [`LTP_91664E8E6FF0FCE1`](../../library/rules/ltp-91664e8e6ff0fce1.yaml) | The userspace pointer is outside accessible memory. | 调用 symlink(test_file, sym_file) | 返回 -1，errno 为 EFAULT |
| [`LTP_A3187FBB07FD0E35`](../../library/rules/ltp-a3187fbb07fd0e35.yaml) | The pathname exceeds the supported limit. | 调用 symlink(test_file, sym_file) | 返回 -1，errno 为 ENAMETOOLONG |
| [`LTP_D8F99518FF4E8643`](../../library/rules/ltp-d8f99518ff4e8643.yaml) | 无额外前置条件 | 调用 symlink(fname, symlnk) | {'kind': 'positive_return', 'return': '>0'} |
## `symlinkat`

没有形成可发布的合规性规则。

## `sync`

没有形成可发布的合规性规则。

## `sync_file_range`

没有形成可发布的合规性规则。

## `syncfs`

没有形成可发布的合规性规则。

## `syscall`

没有形成可发布的合规性规则。

## `sysconf`

没有形成可发布的合规性规则。

## `sysctl`

没有形成可发布的合规性规则。

## `sysfs`

没有形成可发布的合规性规则。

## `sysinfo`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_A367723236ADA8B4`](../../library/rules/ltp-a367723236ada8b4.yaml) | 无额外前置条件 | 调用 sysinfo(sys_buf) | 调用成功，返回 SUCCESS |
| [`LTP_F0BF53984C9E5C92`](../../library/rules/ltp-f0bf53984c9e5c92.yaml) | The userspace pointer is outside accessible memory. | 调用 sysinfo(bad_info) | 返回 -1，errno 为 EFAULT |
## `syslog`

没有形成可发布的合规性规则。

## `tee`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0F9C596BA8184375`](../../library/rules/ltp-0f9c596ba8184375.yaml) | 无额外前置条件 | 调用 tee(pipes[0], pipes[1], TEE_TEST_LEN, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_769389D69FDFA661`](../../library/rules/ltp-769389d69fdfa661.yaml) | 无额外前置条件 | 调用 tee(fd, pipes[1], TEE_TEST_LEN, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_AACDFBA8019E2D25`](../../library/rules/ltp-aacdfba8019e2d25.yaml) | 无额外前置条件 | 调用 tee(pipes[0], fd, TEE_TEST_LEN, 0) | 返回 -1，errno 为 EINVAL |
## `tgkill`

没有形成可发布的合规性规则。

## `time`

没有形成可发布的合规性规则。

## `timer_create`

没有形成可发布的合规性规则。

## `timer_delete`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_10B3572DBFA6742B`](../../library/rules/ltp-10b3572dbfa6742b.yaml) | 无额外前置条件 | 调用 timer_delete(INVALID_ID) | 返回 -1，errno 为 EINVAL |
| [`LTP_9B36D27A4A2994D0`](../../library/rules/ltp-9b36d27a4a2994d0.yaml) | 无额外前置条件 | 调用 timer_delete(timer_id) | {'kind': 'return_value', 'return': '0'} |
## `timer_getoverrun`

没有形成可发布的合规性规则。

## `timer_gettime`

没有形成可发布的合规性规则。

## `timer_settime`

没有形成可发布的合规性规则。

## `timerfd`

没有形成可发布的合规性规则。

## `times`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_A1AECDF3F41769B2`](../../library/rules/ltp-a1aecdf3f41769b2.yaml) | 无额外前置条件 | 调用 times(&mytimes) | {'kind': 'return_value', 'return': '-1'} |
## `tkill`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_2084284EEECEEAC0`](../../library/rules/ltp-2084284eeeceeac0.yaml) | 无额外前置条件 | 调用 tkill(tid, SIGUSR1) | 调用成功，返回 SUCCESS |
| [`LTP_EF9CD83ECACAA86C`](../../library/rules/ltp-ef9cd83ecacaa86c.yaml) | 无额外前置条件 | 调用 tkill(unused_tid, SIGUSR1) | 返回 -1，errno 为 ESRCH |
| [`LTP_FCC236A4D5926B81`](../../library/rules/ltp-fcc236a4d5926b81.yaml) | 无额外前置条件 | 调用 tkill(inval_tid, SIGUSR1) | 返回 -1，errno 为 EINVAL |
## `truncate`

没有形成可发布的合规性规则。

## `ulimit`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_287FBE05D7B30C6F`](../../library/rules/ltp-287fbe05d7b30c6f.yaml) | 无额外前置条件 | 调用 ulimit(UL_SETFSIZE, current_fsize - 1) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_3AD21C6E4A19DB15`](../../library/rules/ltp-3ad21c6e4a19db15.yaml) | The file descriptor is invalid. | 调用 ulimit(UL_GETFSIZE, -1) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_3B4D19754C5D1638`](../../library/rules/ltp-3b4d19754c5d1638.yaml) | 无额外前置条件 | 调用 ulimit(UL_SETFSIZE, current_fsize) | {'kind': 'positive_return', 'return': '>0'} |
## `umask`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_FE4AD44ED28FE386`](../../library/rules/ltp-fe4ad44ed28fe386.yaml) | 无额外前置条件 | 调用 umask(mskval) | {'kind': 'return_value', 'return': 'mskval'} |
## `umount`

没有形成可发布的合规性规则。

## `umount2`

没有形成可发布的合规性规则。

## `uname`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_5516B8A938B9C3A5`](../../library/rules/ltp-5516b8a938b9c3a5.yaml) | 无额外前置条件 | 调用 uname(&un) | 调用成功，返回 SUCCESS |
| [`LTP_7D48AE1036A3CBE7`](../../library/rules/ltp-7d48ae1036a3cbe7.yaml) | The userspace pointer is outside accessible memory. | 调用 uname(bad_addr) | 返回 -1，errno 为 EFAULT |
## `unlink`

没有形成可发布的合规性规则。

## `unlinkat`

没有形成可发布的合规性规则。

## `unshare`

共形成 4 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_40A45C5E82D7F4A1`](../../library/rules/ltp-40a45c5e82d7f4a1.yaml) | 无额外前置条件 | 调用 unshare(FLAG_DESC(CLONE_FILES)) | 调用成功，返回 SUCCESS |
| [`LTP_412173E3E81DC995`](../../library/rules/ltp-412173e3e81dc995.yaml) | 无额外前置条件 | 调用 unshare(FLAG_DESC(CLONE_NEWNS)) | 调用成功，返回 SUCCESS |
| [`LTP_49ABEE42EF290FDC`](../../library/rules/ltp-49abee42ef290fdc.yaml) | 无额外前置条件 | 调用 unshare(FLAG_DESC(CLONE_FS)) | 调用成功，返回 SUCCESS |
| [`LTP_79882F9E36FC9878`](../../library/rules/ltp-79882f9e36fc9878.yaml) | 无额外前置条件 | 调用 unshare(CLONE_FILES) | 返回 -1，errno 为 EMFILE |
## `userfaultfd`

没有形成可发布的合规性规则。

## `ustat`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_14105E9CB6DC44FC`](../../library/rules/ltp-14105e9cb6dc44fc.yaml) | 无额外前置条件 | 调用 ustat((unsigned int)dev_num, &ubuf) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_ED8240DD1329BBA1`](../../library/rules/ltp-ed8240dd1329bba1.yaml) | The userspace pointer is outside accessible memory. | 调用 ustat((unsigned int)root_dev, (void*)-1) | 返回 -1，errno 为 EFAULT |
| [`LTP_F75110BE79864CD1`](../../library/rules/ltp-f75110be79864cd1.yaml) | 无额外前置条件 | 调用 ustat((unsigned int)invalid_dev, &ubuf) | 返回 -1，errno 为 EINVAL |
## `utils`

没有形成可发布的合规性规则。

## `utime`

共形成 7 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0433C0FC2D4AD1EE`](../../library/rules/ltp-0433c0fc2d4ad1ee.yaml) | The fixture creates symname as a symbolic link.、Path resolution encounters a symlink loop. | 调用 utime(symname, &utimes) | 返回 -1，errno 为 ELOOP |
| [`LTP_100C7EAA3620A220`](../../library/rules/ltp-100c7eaa3620a220.yaml) | The fixture creates symname as a symbolic link.、The referenced path does not exist. | 调用 utime(symname, &utimes) | 返回 -1，errno 为 ENOENT |
| [`LTP_428A6CFF573F0942`](../../library/rules/ltp-428a6cff573f0942.yaml) | The fixture sets TEMP_FILE mode to FILE_MODE. | 调用 utime(TEMP_FILE, NULL) | 调用成功，返回 SUCCESS |
| [`LTP_8C5755D366EB8CD2`](../../library/rules/ltp-8c5755d366eb8cd2.yaml) | The fixture creates TEMP_FILE as a regular file.、The fixture sets TEMP_FILE mode to FILE_MODE. | 调用 utime(TEMP_FILE, &utbuf) | 调用成功，返回 SUCCESS |
| [`LTP_BAA1410033A7464D`](../../library/rules/ltp-baa1410033a7464d.yaml) | The fixture creates TEMP_FILE as a regular file.、The fixture sets TEMP_FILE mode to FILE_MODE. | 调用 utime(TEMP_FILE, NULL) | 调用成功，返回 SUCCESS |
| [`LTP_CB319D75C5C1E14F`](../../library/rules/ltp-cb319d75c5c1e14f.yaml) | The fixture creates symname as a symbolic link. | 调用 utime(symname, &utimes) | 调用成功，返回 SUCCESS |
| [`LTP_EF32B2CC0F6F3848`](../../library/rules/ltp-ef32b2cc0f6f3848.yaml) | The fixture sets TEMP_FILE mode to FILE_MODE. | 调用 utime(TEMP_FILE, &utbuf) | 调用成功，返回 SUCCESS |
## `utimensat`

没有形成可发布的合规性规则。

## `utimes`

没有形成可发布的合规性规则。

## `vfork`

没有形成可发布的合规性规则。

## `vhangup`

没有形成可发布的合规性规则。

## `vmsplice`

没有形成可发布的合规性规则。

## `wait`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_7B0F966046AECA7E`](../../library/rules/ltp-7b0f966046aeca7e.yaml) | 无额外前置条件 | 调用 wait(&status) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_AD3A4B98FF201ABE`](../../library/rules/ltp-ad3a4b98ff201abe.yaml) | 无额外前置条件 | 调用 wait(NULL) | 返回 -1，errno 为 ECHILD |
## `wait4`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_1691F6F9712C5546`](../../library/rules/ltp-1691f6f9712c5546.yaml) | 无额外前置条件 | 调用 wait4(INT_MIN, &status, 0, &rusage) | 返回 -1，errno 为 ESRCH |
| [`LTP_2AE73292A13647D5`](../../library/rules/ltp-2ae73292a13647d5.yaml) | 无额外前置条件 | 调用 wait4(pid, &status, 0, &rusage) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_C24E55F06625D564`](../../library/rules/ltp-c24e55f06625d564.yaml) | 无额外前置条件 | 调用 wait4(pid_max + 1, &status, 0, &rusage) | 返回 -1，errno 为 ECHILD |
## `waitid`

共形成 12 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0FE0E20EAC6DE889`](../../library/rules/ltp-0fe0e20eac6de889.yaml) | 无额外前置条件 | 调用 waitid(P_ALL, 0, infop, WEXITED) | 调用成功，返回 SUCCESS |
| [`LTP_4494B70BBA693D42`](../../library/rules/ltp-4494b70bba693d42.yaml) | 无额外前置条件 | 调用 waitid(P_PGID, pid_group+1, infop, WEXITED) | 返回 -1，errno 为 ECHILD |
| [`LTP_53E7B9C40A44F6D0`](../../library/rules/ltp-53e7b9c40a44f6d0.yaml) | 无额外前置条件 | 调用 waitid(P_PID, pid_child, infop, WEXITED) | 调用成功，返回 SUCCESS |
| [`LTP_74C73CBABE325D5D`](../../library/rules/ltp-74c73cbabe325d5d.yaml) | 无额外前置条件 | 调用 waitid(P_PID, 1, infop, WEXITED) | 返回 -1，errno 为 ECHILD |
| [`LTP_77C2FB4A0A9E30F2`](../../library/rules/ltp-77c2fb4a0a9e30f2.yaml) | 无额外前置条件 | 调用 waitid(P_PGID, pid_group, infop, WEXITED) | 调用成功，返回 SUCCESS |
| [`LTP_9C2FB7732A0B90B6`](../../library/rules/ltp-9c2fb7732a0b90b6.yaml) | 无额外前置条件 | 调用 waitid(P_PID, pid_child, infop, WSTOPPED) | 调用成功，返回 SUCCESS |
| [`LTP_9FD87A3F7688FEF1`](../../library/rules/ltp-9fd87a3f7688fef1.yaml) | 无额外前置条件 | 调用 waitid(P_ALL, 0, infop, WNOHANG) | 返回 -1，errno 为 EINVAL |
| [`LTP_C13C4F63D58904BC`](../../library/rules/ltp-c13c4f63d58904bc.yaml) | 无额外前置条件 | 调用 waitid(P_PID, pid_child, infop, WSTOPPED | WNOWAIT) | 调用成功，返回 SUCCESS |
| [`LTP_D1A18560E485E146`](../../library/rules/ltp-d1a18560e485e146.yaml) | 无额外前置条件 | 调用 waitid(P_PID, pid_child, infop, WCONTINUED) | 调用成功，返回 SUCCESS |
| [`LTP_DA64FD04E43656E6`](../../library/rules/ltp-da64fd04e43656e6.yaml) | 无额外前置条件 | 调用 waitid(P_PID, pid_child+1, infop, WEXITED) | 返回 -1，errno 为 ECHILD |
| [`LTP_DF5B725563FDFB31`](../../library/rules/ltp-df5b725563fdfb31.yaml) | 无额外前置条件 | 调用 waitid(P_ALL, pid_child, infop, WNOHANG | WEXITED) | 调用成功，返回 SUCCESS |
| [`LTP_ECD986F27CF15E1E`](../../library/rules/ltp-ecd986f27cf15e1e.yaml) | 无额外前置条件 | 调用 waitid(P_ALL, 0, infop, WNOHANG | WEXITED) | 返回 -1，errno 为 ECHILD |
## `waitpid`

共形成 6 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_03AF14160F8B59A0`](../../library/rules/ltp-03af14160f8b59a0.yaml) | 无额外前置条件 | 调用 waitpid(INT_MIN, NULL, 0) | 返回 -1，errno 为 ESRCH |
| [`LTP_2AF5913113A326EF`](../../library/rules/ltp-2af5913113a326ef.yaml) | The file descriptor is invalid. | 调用 waitpid(-1, NULL, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_2F3E34FD672DBF34`](../../library/rules/ltp-2f3e34fd672dbf34.yaml) | 无额外前置条件 | 调用 waitpid(pid, &status, 0) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_614C018F61C078A0`](../../library/rules/ltp-614c018f61c078a0.yaml) | 无额外前置条件 | 调用 waitpid(pid, NULL, 0) | 返回 -1，errno 为 ECHILD |
| [`LTP_A448981C368F9EBB`](../../library/rules/ltp-a448981c368f9ebb.yaml) | The file descriptor is invalid. | 调用 waitpid(-1, NULL, 0) | 返回 -1，errno 为 ECHILD |
| [`LTP_FC8BA85373EA2D8F`](../../library/rules/ltp-fc8ba85373ea2d8f.yaml) | 无额外前置条件 | 调用 waitpid(1, NULL, 0) | 返回 -1，errno 为 ECHILD |
## `write`

共形成 6 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_05B109981D13ED76`](../../library/rules/ltp-05b109981d13ed76.yaml) | 无额外前置条件 | 调用 write(fd, NULL, 0) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_1B63533FE8D3FAF0`](../../library/rules/ltp-1b63533fe8d3faf0.yaml) | The argument is a userspace buffer. | 调用 write(pipefd[1], buf, sizeof(buf)) | 返回 -1，errno 为 EPIPE |
| [`LTP_6E631BC61A5CEE12`](../../library/rules/ltp-6e631bc61a5cee12.yaml) | The argument is a userspace buffer. | 调用 write(inv_fd, buf, sizeof(buf)) | 返回 -1，errno 为 EBADF |
| [`LTP_85742F5EC5C0112F`](../../library/rules/ltp-85742f5ec5c0112f.yaml) | 无额外前置条件 | 调用 write(wfd, wbuf, sizeof(wbuf)) | 返回 -1，errno 为 EAGAIN |
| [`LTP_CB0D3A27CA90726B`](../../library/rules/ltp-cb0d3a27ca90726b.yaml) | The argument is a userspace buffer. | 调用 write(fd, buf, i) | {'kind': 'return_value', 'return': 'i'} |
| [`LTP_E8BA54C78A3F671D`](../../library/rules/ltp-e8ba54c78a3f671d.yaml) | The userspace pointer is outside accessible memory.、The argument is a userspace buffer. | 调用 write(fd, bad_addr, sizeof(buf)) | 返回 -1，errno 为 EFAULT |
## `writev`

没有形成可发布的合规性规则。


## 技术参考

- 报告 ID：`spec-20260717t051712z-e2102f38`
- 来源：`ltp-local`，内容快照 `sha256:d789747f0c0bf1697f538bc5166073fd8449dec3beac7b12ac0be0b1b716dcb4`
- 全局待处理 syscall：373
- 提取数量：`all`（来源：`command`）
- `abort`：证据 1 条，未解析 0 条
- `accept`：证据 6 条，未解析 0 条
- `accept4`：证据 2 条，未解析 2 条
- `access`：证据 10 条，未解析 0 条
- `acct`：证据 8 条，未解析 1 条
- `add_key`：证据 15 条，未解析 5 条
- `adjtimex`：证据 6 条，未解析 3 条
- `alarm`：证据 15 条，未解析 0 条
- `arch_prctl`：证据 1 条，未解析 0 条
- `bind`：证据 9 条，未解析 1 条
- `bpf`：证据 12 条，未解析 1 条
- `brk`：证据 3 条，未解析 0 条
- `cacheflush`：证据 1 条，未解析 0 条
- `cachestat`：证据 7 条，未解析 0 条
- `capget`：证据 2 条，未解析 0 条
- `capset`：证据 10 条，未解析 0 条
- `chdir`：证据 4 条，未解析 1 条
- `chmod`：证据 15 条，未解析 1 条
- `chown`：证据 22 条，未解析 1 条
- `chroot`：证据 8 条，未解析 0 条
- `clock_adjtime`：证据 1 条，未解析 1 条
- `clock_getres`：证据 0 条，未解析 0 条
- `clock_gettime`：证据 6 条，未解析 1 条
- `clock_nanosleep`：证据 4 条，未解析 2 条
- `clock_settime`：证据 2 条，未解析 1 条
- `clone`：证据 9 条，未解析 1 条
- `clone3`：证据 5 条，未解析 1 条
- `close`：证据 4 条，未解析 0 条
- `close_range`：证据 8 条，未解析 0 条
- `cma`：证据 4 条，未解析 0 条
- `confstr`：证据 3 条，未解析 1 条
- `connect`：证据 1 条，未解析 0 条
- `copy_file_range`：证据 3 条，未解析 0 条
- `creat`：证据 12 条，未解析 1 条
- `delete_module`：证据 4 条，未解析 1 条
- `dup`：证据 14 条，未解析 0 条
- `dup2`：证据 14 条，未解析 0 条
- `dup3`：证据 4 条，未解析 0 条
- `epoll`：证据 0 条，未解析 0 条
- `epoll_create`：证据 4 条，未解析 0 条
- `epoll_create1`：证据 3 条，未解析 0 条
- `epoll_ctl`：证据 10 条，未解析 0 条
- `epoll_pwait`：证据 7 条，未解析 1 条
- `epoll_wait`：证据 19 条，未解析 0 条
- `eventfd`：证据 12 条，未解析 0 条
- `eventfd2`：证据 7 条，未解析 0 条
- `execl`：证据 0 条，未解析 0 条
- `execle`：证据 0 条，未解析 0 条
- `execlp`：证据 0 条，未解析 0 条
- `execv`：证据 0 条，未解析 0 条
- `execve`：证据 8 条，未解析 1 条
- `execveat`：证据 1 条，未解析 0 条
- `execvp`：证据 0 条，未解析 0 条
- `exit`：证据 0 条，未解析 0 条
- `exit_group`：证据 3 条，未解析 0 条
- `faccessat`：证据 5 条，未解析 1 条
- `faccessat2`：证据 4 条，未解析 0 条
- `fadvise`：证据 4 条，未解析 0 条
- `fallocate`：证据 12 条，未解析 1 条
- `fanotify`：证据 27 条，未解析 2 条
- `fchdir`：证据 3 条，未解析 0 条
- `fchmod`：证据 12 条，未解析 0 条
- `fchmodat`：证据 4 条，未解析 0 条
- `fchmodat2`：证据 4 条，未解析 0 条
- `fchown`：证据 10 条，未解析 1 条
- `fcntl`：证据 72 条，未解析 14 条
- `fdatasync`：证据 3 条，未解析 1 条
- `fgetxattr`：证据 7 条，未解析 6 条
- `file_attr`：证据 6 条，未解析 1 条
- `finit_module`：证据 5 条，未解析 0 条
- `flistxattr`：证据 3 条，未解析 0 条
- `flock`：证据 18 条，未解析 0 条
- `fmtmsg`：证据 0 条，未解析 0 条
- `fork`：证据 17 条，未解析 0 条
- `fpathconf`：证据 2 条，未解析 0 条
- `fremovexattr`：证据 4 条，未解析 2 条
- `fsconfig`：证据 9 条，未解析 0 条
- `fsetxattr`：证据 5 条，未解析 4 条
- `fsmount`：证据 2 条，未解析 1 条
- `fsopen`：证据 2 条，未解析 1 条
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
- `renameat`：证据 2 条，未解析 2 条
- `renameat2`：证据 2 条，未解析 2 条
- `request_key`：证据 11 条，未解析 0 条
- `rmdir`：证据 4 条，未解析 2 条
- `rt_sigaction`：证据 2 条，未解析 2 条
- `rt_sigprocmask`：证据 3 条，未解析 0 条
- `rt_sigqueueinfo`：证据 2 条，未解析 1 条
- `rt_sigsuspend`：证据 1 条，未解析 0 条
- `rt_sigtimedwait`：证据 0 条，未解析 0 条
- `rt_tgsigqueueinfo`：证据 4 条，未解析 3 条
- `sbrk`：证据 5 条，未解析 0 条
- `sched_get_priority_max`：证据 4 条，未解析 1 条
- `sched_get_priority_min`：证据 4 条，未解析 1 条
- `sched_getaffinity`：证据 2 条，未解析 0 条
- `sched_getattr`：证据 2 条，未解析 0 条
- `sched_getparam`：证据 3 条，未解析 1 条
- `sched_getscheduler`：证据 2 条，未解析 0 条
- `sched_rr_get_interval`：证据 4 条，未解析 1 条
- `sched_setaffinity`：证据 2 条，未解析 0 条
- `sched_setattr`：证据 1 条，未解析 0 条
- `sched_setparam`：证据 6 条，未解析 1 条
- `sched_setscheduler`：证据 2 条，未解析 0 条
- `sched_yield`：证据 1 条，未解析 0 条
- `seccomp`：证据 3 条，未解析 0 条
- `select`：证据 8 条，未解析 2 条
- `send`：证据 3 条，未解析 1 条
- `sendfile`：证据 16 条，未解析 0 条
- `sendmmsg`：证据 3 条，未解析 1 条
- `sendmsg`：证据 2 条，未解析 0 条
- `sendto`：证据 4 条，未解析 0 条
- `set_mempolicy`：证据 5 条，未解析 4 条
- `set_robust_list`：证据 2 条，未解析 0 条
- `set_thread_area`：证据 5 条，未解析 1 条
- `set_tid_address`：证据 2 条，未解析 0 条
- `setdomainname`：证据 1 条，未解析 1 条
- `setegid`：证据 3 条，未解析 0 条
- `setfsgid`：证据 2 条，未解析 0 条
- `setfsuid`：证据 3 条，未解析 0 条
- `setgid`：证据 3 条，未解析 0 条
- `setgroups`：证据 4 条，未解析 1 条
- `sethostname`：证据 0 条，未解析 0 条
- `setitimer`：证据 2 条，未解析 0 条
- `setns`：证据 2 条，未解析 2 条
- `setpgid`：证据 9 条，未解析 0 条
- `setpgrp`：证据 3 条，未解析 0 条
- `setpriority`：证据 2 条，未解析 0 条
- `setregid`：证据 3 条，未解析 2 条
- `setresgid`：证据 4 条，未解析 0 条
- `setresuid`：证据 6 条，未解析 1 条
- `setreuid`：证据 9 条，未解析 2 条
- `setrlimit`：证据 12 条，未解析 1 条
- `setsid`：证据 0 条，未解析 0 条
- `setsockopt`：证据 19 条，未解析 2 条
- `settimeofday`：证据 4 条，未解析 0 条
- `setuid`：证据 2 条，未解析 0 条
- `setxattr`：证据 8 条，未解析 4 条
- `sgetmask`：证据 1 条，未解析 0 条
- `shutdown`：证据 4 条，未解析 1 条
- `sigaction`：证据 1 条，未解析 0 条
- `sigaltstack`：证据 3 条，未解析 0 条
- `sighold`：证据 1 条，未解析 0 条
- `signal`：证据 5 条，未解析 0 条
- `signalfd`：证据 5 条，未解析 0 条
- `signalfd4`：证据 0 条，未解析 0 条
- `sigpending`：证据 0 条，未解析 0 条
- `sigprocmask`：证据 1 条，未解析 0 条
- `sigrelse`：证据 0 条，未解析 0 条
- `sigsuspend`：证据 4 条，未解析 0 条
- `sigtimedwait`：证据 0 条，未解析 0 条
- `sigwait`：证据 0 条，未解析 0 条
- `sigwaitinfo`：证据 0 条，未解析 0 条
- `socket`：证据 3 条，未解析 0 条
- `socketcall`：证据 5 条，未解析 4 条
- `socketpair`：证据 6 条，未解析 3 条
- `sockioctl`：证据 2 条，未解析 2 条
- `splice`：证据 11 条，未解析 1 条
- `ssetmask`：证据 1 条，未解析 0 条
- `stat`：证据 5 条，未解析 1 条
- `statfs`：证据 6 条，未解析 1 条
- `statmount`：证据 19 条，未解析 1 条
- `statvfs`：证据 4 条，未解析 1 条
- `statx`：证据 31 条，未解析 2 条
- `stime`：证据 0 条，未解析 0 条
- `string`：证据 0 条，未解析 0 条
- `swapoff`：证据 5 条，未解析 2 条
- `swapon`：证据 6 条，未解析 0 条
- `switch`：证据 0 条，未解析 0 条
- `symlink`：证据 5 条，未解析 0 条
- `symlinkat`：证据 2 条，未解析 2 条
- `sync`：证据 0 条，未解析 0 条
- `sync_file_range`：证据 4 条，未解析 1 条
- `syncfs`：证据 1 条，未解析 1 条
- `syscall`：证据 1 条，未解析 0 条
- `sysconf`：证据 0 条，未解析 0 条
- `sysctl`：证据 1 条，未解析 1 条
- `sysfs`：证据 11 条，未解析 1 条
- `sysinfo`：证据 4 条，未解析 0 条
- `syslog`：证据 3 条，未解析 0 条
- `tee`：证据 2 条，未解析 0 条
- `tgkill`：证据 0 条，未解析 0 条
- `time`：证据 1 条，未解析 0 条
- `timer_create`：证据 3 条，未解析 1 条
- `timer_delete`：证据 2 条，未解析 0 条
- `timer_getoverrun`：证据 3 条，未解析 0 条
- `timer_gettime`：证据 0 条，未解析 0 条
- `timer_settime`：证据 0 条，未解析 0 条
- `timerfd`：证据 5 条，未解析 3 条
- `times`：证据 2 条，未解析 0 条
- `tkill`：证据 4 条，未解析 0 条
- `truncate`：证据 4 条，未解析 2 条
- `ulimit`：证据 4 条，未解析 0 条
- `umask`：证据 1 条，未解析 0 条
- `umount`：证据 6 条，未解析 0 条
- `umount2`：证据 3 条，未解析 1 条
- `uname`：证据 2 条，未解析 0 条
- `unlink`：证据 10 条，未解析 1 条
- `unlinkat`：证据 3 条，未解析 2 条
- `unshare`：证据 9 条，未解析 0 条
- `userfaultfd`：证据 7 条，未解析 0 条
- `ustat`：证据 2 条，未解析 0 条
- `utils`：证据 0 条，未解析 0 条
- `utime`：证据 19 条，未解析 0 条
- `utimensat`：证据 2 条，未解析 1 条
- `utimes`：证据 3 条，未解析 2 条
- `vfork`：证据 2 条，未解析 0 条
- `vhangup`：证据 2 条，未解析 0 条
- `vmsplice`：证据 5 条，未解析 2 条
- `wait`：证据 4 条，未解析 0 条
- `wait4`：证据 5 条，未解析 0 条
- `waitid`：证据 25 条，未解析 0 条
- `waitpid`：证据 6 条，未解析 0 条
- `write`：证据 9 条，未解析 0 条
- `writev`：证据 7 条，未解析 1 条

<details>
<summary>机器可读元数据</summary>

<!-- syscallguard-metadata -->
```yaml
schema_version: 1
kind: syscallguard_ingest_report
report_id: spec-20260717t051712z-e2102f38
generated_at_utc: '2026-07-17T05:17:17.636551Z'
source:
  id: ltp-local
  type: ltp
  snapshot_hash: sha256:d789747f0c0bf1697f538bc5166073fd8449dec3beac7b12ac0be0b1b716dcb4
  descriptor_hash: sha256:4315924cd8b9aab9608c225950c81f18ab74f25d63d74ee6ac3c444132131b4d
  recognition_rules_hash: sha256:84d715591e7abe5f2ac2de68c75172b2b2389541f6f8b8f23582b8cff81b057e
  resolution: source_alias
count:
  value: all
  source: command
pending_count: 373
selected_syscalls:
- abort
- accept
- accept4
- access
- acct
- add_key
- adjtimex
- alarm
- arch_prctl
- bind
- bpf
- brk
- cacheflush
- cachestat
- capget
- capset
- chdir
- chmod
- chown
- chroot
- clock_adjtime
- clock_getres
- clock_gettime
- clock_nanosleep
- clock_settime
- clone
- clone3
- close
- close_range
- cma
- confstr
- connect
- copy_file_range
- creat
- delete_module
- dup
- dup2
- dup3
- epoll
- epoll_create
- epoll_create1
- epoll_ctl
- epoll_pwait
- epoll_wait
- eventfd
- eventfd2
- execl
- execle
- execlp
- execv
- execve
- execveat
- execvp
- exit
- exit_group
- faccessat
- faccessat2
- fadvise
- fallocate
- fanotify
- fchdir
- fchmod
- fchmodat
- fchmodat2
- fchown
- fcntl
- fdatasync
- fgetxattr
- file_attr
- finit_module
- flistxattr
- flock
- fmtmsg
- fork
- fpathconf
- fremovexattr
- fsconfig
- fsetxattr
- fsmount
- fsopen
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
- renameat
- renameat2
- request_key
- rmdir
- rt_sigaction
- rt_sigprocmask
- rt_sigqueueinfo
- rt_sigsuspend
- rt_sigtimedwait
- rt_tgsigqueueinfo
- sbrk
- sched_get_priority_max
- sched_get_priority_min
- sched_getaffinity
- sched_getattr
- sched_getparam
- sched_getscheduler
- sched_rr_get_interval
- sched_setaffinity
- sched_setattr
- sched_setparam
- sched_setscheduler
- sched_yield
- seccomp
- select
- send
- sendfile
- sendmmsg
- sendmsg
- sendto
- set_mempolicy
- set_robust_list
- set_thread_area
- set_tid_address
- setdomainname
- setegid
- setfsgid
- setfsuid
- setgid
- setgroups
- sethostname
- setitimer
- setns
- setpgid
- setpgrp
- setpriority
- setregid
- setresgid
- setresuid
- setreuid
- setrlimit
- setsid
- setsockopt
- settimeofday
- setuid
- setxattr
- sgetmask
- shutdown
- sigaction
- sigaltstack
- sighold
- signal
- signalfd
- signalfd4
- sigpending
- sigprocmask
- sigrelse
- sigsuspend
- sigtimedwait
- sigwait
- sigwaitinfo
- socket
- socketcall
- socketpair
- sockioctl
- splice
- ssetmask
- stat
- statfs
- statmount
- statvfs
- statx
- stime
- string
- swapoff
- swapon
- switch
- symlink
- symlinkat
- sync
- sync_file_range
- syncfs
- syscall
- sysconf
- sysctl
- sysfs
- sysinfo
- syslog
- tee
- tgkill
- time
- timer_create
- timer_delete
- timer_getoverrun
- timer_gettime
- timer_settime
- timerfd
- times
- tkill
- truncate
- ulimit
- umask
- umount
- umount2
- uname
- unlink
- unlinkat
- unshare
- userfaultfd
- ustat
- utils
- utime
- utimensat
- utimes
- vfork
- vhangup
- vmsplice
- wait
- wait4
- waitid
- waitpid
- write
- writev
syscalls:
- syscall: abort
  source_fingerprint: sha256:bcfbc8209ef30cdaf386eab7a3c95e88d9380d72c1d8113fd57fd4a140c68ee3
  recognition_fingerprint: sha256:a3665b9ccdf0ef5034232eb9b6638add63b48cb792f2614fa398c00a0e6e8a1b
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: accept
  source_fingerprint: sha256:67de27cb07823cd82fe2cccc4519cba50af7559dd97aade2e66d60ba1be6477c
  recognition_fingerprint: sha256:ea693fdf92b0777d70206e76f224ba30ab2eb9ab658abfa6e921de83bf053685
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_277FD467E5F1BF1C
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:277fd467e5f1bf1c23ee7c1139c3420fd53e3387d46a1441bccd3f763aecc0c1
  - id: LTP_472AAA35C7382B26
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:472aaa35c7382b2636fefb76370c46d334f3c77cb0f9a4d38ae943f787a3b503
  - id: LTP_80C6DB0ACB2A5510
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:80c6db0acb2a5510899328ccf5897d7e8d2a652d48a8013d682918b68813a993
  - id: LTP_9CA9C6B61C3317A3
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:9ca9c6b61c3317a32e26c489d7ae42771eb27df123a4f1488713978280f9bfb7
  - id: LTP_B90CB73F36B70C6F
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:b90cb73f36b70c6f80c9105773e4598523d84a62b8068d6913141437de6ddcb8
  - id: LTP_E13B9C2C9645B841
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:e13b9c2c9645b841740286ed51439b50fbadac9cb52df5b4b60bf4bd5ed5df31
  evidence_count: 6
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: accept4
  source_fingerprint: sha256:ef8169f7868949409125798db26ccd7ebbfedd098b5ae018eca3fe029abf1245
  recognition_fingerprint: sha256:08b14facc08997b874353b9beb41959be787e0e041da11e209bc0b5ba2429205
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: access
  source_fingerprint: sha256:2beb6aef3f53b06cc748b2dfabb7de16e44bc56e67e96528700ac22c91729b1a
  recognition_fingerprint: sha256:08645372a703c9c8639d7d3e8771dc0d65330fff41ef6fc14dd1abd16f530627
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_018E81B4859D535F
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:018e81b4859d535f7986d3454ceeb246c966c9f0c762705ffe539f4f94ad00e8
  - id: LTP_01F98F68E029F1A9
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:01f98f68e029f1a9b2d82ff43028938c19aade8fe4b7523f20e751d02eff721f
  - id: LTP_04799921082E0315
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:04799921082e0315e1748aa0cdcde0213d5d6bc9d73e744e097cdc0061ed61a8
  - id: LTP_05A4E0F4E4D24683
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:05a4e0f4e4d24683f0023e31823390ac57abfe19aafe2806d5fb3a80a72b72ce
  - id: LTP_07267357D988E0D3
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:07267357d988e0d3291cdd5f365960af6e477bc8c725c4a3b3f04004b393b0bd
  - id: LTP_07D1AC926F3B00CA
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:07d1ac926f3b00caffdce17d74a601c4663141670aa9930340bd6149120d88f9
  - id: LTP_08AD094BD7C5CF64
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:08ad094bd7c5cf64654209dafec178555a232f97a039e64354a2b204376554b2
  - id: LTP_092C2A39F54E4F90
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:092c2a39f54e4f9096b7290720fca4bba6f8e2fd2e635f45ffa02a132eaf7f48
  - id: LTP_094580B59455EBF1
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:094580b59455ebf16e870f640b7de3c8e627857e1b0f579fa5c9486297380bff
  - id: LTP_0973D484DB2E7E2D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:0973d484db2e7e2dca4389dbb1cbf116e2fd7df79047fa139d7703fb62e0a653
  - id: LTP_09DDAC16EAB70A23
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:09ddac16eab70a2322efad560edaf366041bbbcebcb64e77c9ecf50e0ec63024
  - id: LTP_09FE3EF67718087A
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:09fe3ef67718087ac266efe8927feab9d7cae6946ba1b608ebcaa205ecaf232b
  - id: LTP_0A7162BAB3AA89BD
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:0a7162bab3aa89bd723adb72e663bf5368dbc2f9b20acedcf5edb5f8bcb9ce2c
  - id: LTP_0A9DA3A2803EEF70
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:0a9da3a2803eef70c1f981a01a3194c7a85629308e54e2e0e9d8a371783620be
  - id: LTP_0B6757A74359BB1E
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:0b6757a74359bb1e164614ffab2618269783e9e94f04daf2d9da1d448863731e
  - id: LTP_0B9F382D21CF8997
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:0b9f382d21cf8997f46c5b22511990645263c76693af26c7ff1410cfda2efe2c
  - id: LTP_0DAD2B9BF983B90F
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:0dad2b9bf983b90f532c65802cf79e81f954cde229a4ff251313f2de0551365d
  - id: LTP_0E49032B253C732D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:0e49032b253c732d02b1849a386a284adcf3f1894302b04dc5eb8dfdaf47f0f1
  - id: LTP_0E9124C6B17214C9
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:0e9124c6b17214c9046b03bf27fc2ff383e6f52abc5c72a4d119cc30e21303e6
  - id: LTP_0EB6FB88C2CC23AE
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:0eb6fb88c2cc23ae6003878c81f0c8271eff9df5e97f73dc0157cbcdd0d06078
  - id: LTP_0EFD831C4B5C2D95
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:0efd831c4b5c2d95e60c98fdcfe73253e68c9835d1566c391b6d6e4e39c77d2e
  - id: LTP_0F3BABDCCC428DF4
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:0f3babdccc428df48e96dd8cdd99ac1ff21080236086c73013035e1cb0358241
  - id: LTP_10455AB2DFB23127
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:10455ab2dfb23127f531078b05b5cfd3b01ca0df7af67fbed29eec403e89a232
  - id: LTP_1238FDE5F55AC037
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:1238fde5f55ac03723f2fe56f216fc7522c6041c03436deeef9a7489241005d5
  - id: LTP_149BE2ED84AB5AAC
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:149be2ed84ab5aac3191ca3bcc724afeb27f6b4334190bf6c0aeb2448c912468
  - id: LTP_15F83338278C3CFE
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:15f83338278c3cfe2736c0b30a0a20a8aa71393375364b160fff2c807734b92b
  - id: LTP_1617908ACCAE8499
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:1617908accae849938d073bcc760d4aa4e254e0a39e6a5cbf7e5f260b157a1c9
  - id: LTP_16449F1C9EC8C71F
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:16449f1c9ec8c71ff7f632303c4c82d5cdc8a0fe3fd588f2d85b66cfe7847f7c
  - id: LTP_18A80CB437A03D1F
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:18a80cb437a03d1f174d53030be862cf013cada5f1c93dd8a5ce97e5a4d385d8
  - id: LTP_1A1038DA1B735AB6
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:1a1038da1b735ab6cc84f2b817d580fcf2d8a516f5d562db8232083cd896d300
  - id: LTP_1CD2E41D7D4A4B9D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:1cd2e41d7d4a4b9d7d19a0a34ae357a8f18304c9804e55ed83b36556fc360d90
  - id: LTP_1D4684A49237E045
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:1d4684a49237e045fa38a4f321147579e61ac3e6c1319f6bf556f52392ebdae8
  - id: LTP_1FC16C0CDAE55FD5
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:1fc16c0cdae55fd52df9d4777511e2d59e3b98bc49d1a5fef6913667e940dbc5
  - id: LTP_20CE8BA111311B3B
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:20ce8ba111311b3b69a452f0dc44e4c8351e4bac9ef1fcd5756b72f53e5021d1
  - id: LTP_23017C8E93EEED5E
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:23017c8e93eeed5e3c19c4787a570422ec2a62aef71b7cc54db58a267ee56a13
  - id: LTP_2316B5E43A8809B0
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:2316b5e43a8809b0e347c200395e1580567bf9e58bd28c4c0b006026d3d5a797
  - id: LTP_239441432F72CF6C
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:239441432f72cf6cb1eb4df74284774852f0b784dfb5cec99e6c1443ec3a112f
  - id: LTP_254CA9053175601F
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:254ca9053175601f421f229369e98bbff012b18c71be180e04ce1892e64db74c
  - id: LTP_2591489AC5619A2C
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:2591489ac5619a2c335f2e3cb77ee0e656fdec1de29a5d0ced415a211028cf62
  - id: LTP_273F672499C6852D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:273f672499c6852dabdfb4ad951892587df0645643a98fd7f2c7354774bc0a54
  - id: LTP_27BB10D3A420BC7D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:27bb10d3a420bc7d059716d36f919c2e278a01369e9d3cd0b96e1afe9b2f149c
  - id: LTP_2AF2BC8B94FE2134
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:2af2bc8b94fe213434f6be30a40fd77384c9ee59d8342ad09a7f6f54751f9bca
  - id: LTP_2B8471E586CDE6D7
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:2b8471e586cde6d7e88603cca6be68ab81536e7443d600a32a5080f79201007c
  - id: LTP_2BB228E4FB7C7BEB
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:2bb228e4fb7c7beb56af75724d1cda06b5dacda4822d60bccb85c27df0fb3089
  - id: LTP_2D0CADDE36D70080
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:2d0cadde36d70080cdef6c0e7f0547f9e6a8f3c9049a4734dbd43ae57542e96f
  - id: LTP_2DC2EBC740EB7D7C
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:2dc2ebc740eb7d7c23fcc0b25cae156ff97f34e1f35a8b21c1bb38db4ea77e3a
  - id: LTP_2E135F7478A355E8
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:2e135f7478a355e838494a99e3a6e0a9dde3f5833ca606267e252c6e3b144260
  - id: LTP_2F8A8DCF7F3AEB62
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:2f8a8dcf7f3aeb62b33d830bf02891dd7328cb454b95b41b20d812a4fa96539c
  - id: LTP_2FA1F12DE62C6A0F
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:2fa1f12de62c6a0f126ce9a264e4cc8f49b8a33bb4dd75a2fc96486c8f5af0c3
  - id: LTP_2FD53CE9C8CF6CE7
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:2fd53ce9c8cf6ce75df5356e8be2ef3c4b25a6b3e5919b45f0ff9dadde8a976b
  - id: LTP_317FC70FE2A58775
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:317fc70fe2a58775abcb9c5b5cef4a81efe2fd3956c989671e252ffdb440443b
  - id: LTP_31F03C781DAB0AD2
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:31f03c781dab0ad2fac19a09f02b9f3986695e56dced3292573f181dde5bc2f3
  - id: LTP_32F2B22133BB52DD
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:32f2b22133bb52dd98e6e89e391f3b039fe52ce91631ac6fc6932e46b601c435
  - id: LTP_332E6D2186F55A6F
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:332e6d2186f55a6f1ad3f503a616563983de52917645e34d97c307f2ab332120
  - id: LTP_342F7EADB5D10802
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:342f7eadb5d1080234e0abc1ff8fed84e03ac78d1e068532c4fdb451534d53b8
  - id: LTP_3662829F538B7D97
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:3662829f538b7d97bbe8d59f6432edc580902610e610c7e8ad2498909ad86938
  - id: LTP_3670635A7A7D4496
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:3670635a7a7d4496de5c0b6912c146815e33398ded89666433322d66ab1dc739
  - id: LTP_3692C449569215B8
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:3692c449569215b831a8489fa3b5dd2b65d1113598f7665a1e7863182a2f5677
  - id: LTP_3839B158DA52269B
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:3839b158da52269b377b9f5b08cbb3049893b3c596328784b36a54ad91b07bd7
  - id: LTP_39B7A82AB3626707
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:39b7a82ab36267078cb9b62c4d90c95452b1d3da0ff3de7e3255b77d7abb23ba
  - id: LTP_3A0AAE966297CCA7
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:3a0aae966297cca710eb283060eb879b0cf64008f4c5fd34f7feb0725c32b11a
  - id: LTP_3B48FBCC62838D3A
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:3b48fbcc62838d3acc05053c5dc6271171e7efd977a63977ed467c172402fb06
  - id: LTP_3BA6F828CDE1E2E6
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:3ba6f828cde1e2e6904136eb3ebbbf41435fa8e510bba85e6a61d93beb525436
  - id: LTP_3D8EEC7BCE259B85
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:3d8eec7bce259b85f18e5b45784123e3fcd7067ef1805e5113971a9b7fdb851d
  - id: LTP_3E0472B66C2C5AB3
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:3e0472b66c2c5ab3576ff97cad4657a82b93e2c9454befc67b197e91acd68f69
  - id: LTP_3F80E012EF9B4D7E
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:3f80e012ef9b4d7eee9e91c0bc978f19c4637421f84291cff62442495279573c
  - id: LTP_4171AFC9C3FEC6E7
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:4171afc9c3fec6e7067f9ffb6ee1d6ff15e8f54550f40aabc3e8bcd75e6b43ca
  - id: LTP_41AB796031F8E171
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:41ab796031f8e171350219b39d5b5f0e43e9e31d734e485834204573877e9aa9
  - id: LTP_428573F9D490F227
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:428573f9d490f227629e77419c3c0f82409b630fb759cdcd55cca6b2a1098aaf
  - id: LTP_4321E1483FC39110
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:4321e1483fc391100d7e1ac8a787e71dee5fda4debd1a78be774944c6776b069
  - id: LTP_43D6C007093E3B31
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:43d6c007093e3b318746f4d022aa9de27bc378a9048c3b3729993cbd7fca7dc3
  - id: LTP_43F303BEA895DBE0
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:43f303bea895dbe04042c57ad0288aeb5e8caa30de6a329571b01df0666d21a7
  - id: LTP_44313BAA17BEB1AE
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:44313baa17beb1ae8c17efc36515e47bf011857c83d5ea944cf81e20f979a1e1
  - id: LTP_44983CDE7F1A5F08
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:44983cde7f1a5f087e87a7f564ce90ce726418880bf0f4a8e9ac2407143e9211
  - id: LTP_449986F83296A5CF
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:449986f83296a5cfa0ea932189b02dbb64431fdedfbca964e7846b5907280536
  - id: LTP_47DFC97559CA29F8
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:47dfc97559ca29f8b2a2a0169419501912073dedd46555daa1acb06883b717e6
  - id: LTP_499A726F0D1EAB38
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:499a726f0d1eab38fff859edc8801e32331aec148d0a079907fd8d8905c632f1
  - id: LTP_4B27C893C8E9111F
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:4b27c893c8e9111f189c20ec2a28dbff0ae9c281d9e734b8539c22c31f478101
  - id: LTP_4B7BD75A450AC789
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:4b7bd75a450ac789cad2a2161b9d395ee9eed1b6ce08884d845ac363e8a0a257
  - id: LTP_4BE43BC3E131100B
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:4be43bc3e131100b9c5d902c71c6566219c995963ded21a5f4cc31d0103cac15
  - id: LTP_4CA2527DAE947BFC
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:4ca2527dae947bfc7d7535b232bf3dc6a09a00150d9e355f0e9bc459b4f03980
  - id: LTP_4CAA10F04475843A
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:4caa10f04475843a60d0cec63f2348f047cb852ce7a47eb5b3947ffc72937b09
  - id: LTP_4D70641BCBFF1FC9
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:4d70641bcbff1fc9703c8e9f0113380c9862e741626fe46cb47e9a98be95f934
  - id: LTP_4E728F2B93D7AF55
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:4e728f2b93d7af55240306a95c13a1452a8c1cad3b10b4058a39dfcd6ac5a50a
  - id: LTP_50634C72AABCB02C
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:50634c72aabcb02c2c8c7331d8fb67c7f56d3f689d8652878d01cfeb2e9e3f5c
  - id: LTP_532669DC3463015A
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:532669dc3463015a190113e9b4f2673bb90ef9f7cca304ec01a1e356d3c3a980
  - id: LTP_54E5F3DA585FF826
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:54e5f3da585ff826d07a2ea33c4838859934fdd31dce04df6ed24e34e7ac9d4a
  - id: LTP_557771AFA7D3CBA3
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:557771afa7d3cba3250a4d512f3314a8d42ae3b9a574fd49d7cfba58d2dcd734
  - id: LTP_56EB350905546953
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:56eb350905546953c86a0fa436912181f570e388d96e81fdc9873fec4ef4ddcd
  - id: LTP_579F2F9BF68FC287
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:579f2f9bf68fc287cc2af84c4b09ca00ca74052452327072e0f0015e315c37fa
  - id: LTP_5B429657B5297267
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:5b429657b5297267aa61639c29d91bac2ceec47005e09ace0be210d012a5733e
  - id: LTP_5DCAB1EE343F650B
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:5dcab1ee343f650bd5702f37b667e997249572a96b84282c2b379a9fbb24ff1a
  - id: LTP_5DCE40F2EE0477DD
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:5dce40f2ee0477dd85329a5c84441ca315a5b0b4a0354e464edb707c156a832a
  - id: LTP_5F1E8876185AED7D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:5f1e8876185aed7d7767f9699fd3625fb1dbaad75697682efef4ff0f1270fed3
  - id: LTP_5FC4B14EE38910DA
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:5fc4b14ee38910dae04fbd6aa53d1d08a0304cc3dcb043d0ffe7432888845b70
  - id: LTP_62CC9D9E2E3D7880
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:62cc9d9e2e3d78802ae06c63707ce21f1d1adb7d9abc96f7c234927332397c0b
  - id: LTP_639CB00D5B06579C
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:639cb00d5b06579ca9d5adc985d73d44d007b59b4c5263724ac94b72c41ba66e
  - id: LTP_647D857E6AB3D942
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:647d857e6ab3d9422a295e2cf1850c78124b24ea6db38b054c9d225a5182bd17
  - id: LTP_650C93999DB128D6
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:650c93999db128d68c35f5ffd281dcc5b22c8f6eb97ea10b10301756d7c7fdb4
  - id: LTP_6534585EC08425D6
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:6534585ec08425d6a481ae9a11085ea4495d8eb7db152cfd27f1064df85be688
  - id: LTP_68933230FCEAA7D5
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:68933230fceaa7d56b6d16a2ac384cb5199352ea234a59d27ea77183fdeec425
  - id: LTP_6AAFFF4DD70E39E2
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:6aafff4dd70e39e2cf76b93882420af0a9244b1d9e4cbb05fef2e122b7a7b13f
  - id: LTP_6BBDEE6D1B9C6D94
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:6bbdee6d1b9c6d9456cc8afe286f6486e947fb44b8aedefffff535c80bcc2aa9
  - id: LTP_6C89FDE5BFD98590
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:6c89fde5bfd985907c0ab4a2238d3605063a01a2ae9fc2e77ad1e82d4d25ced9
  - id: LTP_6D034F85A89B1FCF
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:6d034f85a89b1fcf517f2c44b44cbea4ef3c0b72c0f630fb354e013cbd082bc4
  - id: LTP_6D2D8585448FB760
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:6d2d8585448fb76078fac32b9d75d5698036809293abd512c68fc8f421edaa9a
  - id: LTP_6D74624C7ACACFFC
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:6d74624c7acacffc87405d0adf8ff99e721146aa2cf8ed0ad9bf7b8be43cbb84
  - id: LTP_70A24E1D78959E54
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:70a24e1d78959e542cf6c507f0ebf3052409c4a4b18c480c9c0cf41f055cf1d0
  - id: LTP_71C59FD029BDE7EC
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:71c59fd029bde7ec090543052c9b606430639c537aa7b6922bd56d8366e39636
  - id: LTP_72CB51010EB5642E
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:72cb51010eb5642e74088209f6a5114b42f22accd0a5b7b68bff43e8ec80436d
  - id: LTP_72CE32EF22E0AD18
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:72ce32ef22e0ad18112be11cab795563c150b000291d2209017cd7a9c7fa61fa
  - id: LTP_7516A82707F421A8
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:7516a82707f421a886fcd4b275009253089e72a988456454e9f4cf516fc095c8
  - id: LTP_762DED3BB55C0120
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:762ded3bb55c0120f9a49005064a7195ee12110cc5a81a6475a2bace83bb83dd
  - id: LTP_765C6BC355EC57B9
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:765c6bc355ec57b9fb8d7e41a9e355140e2c13f79c8f0045f1fc9354466912bd
  - id: LTP_7886070B1C145E5B
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:7886070b1c145e5bd6fc8548be7590b7a0b4ce95f0cd37392d4c25d29c0a846f
  - id: LTP_78B9E649A9D3C278
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:78b9e649a9d3c278260c7b0a2fd7b8b46f5d8fa32e254910f2bcc138917a190c
  - id: LTP_7DDD8970DD3DE57B
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:7ddd8970dd3de57b1ce8262a580d9690f66756306c34f7d68d3462e92edbd824
  - id: LTP_804841A817CAA56C
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:804841a817caa56c516aa188abef36874f2a2370b9195ca8116da0026f64d5fa
  - id: LTP_82677662F036B4D3
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:82677662f036b4d321975bff9813c6fcfdae268f4a317c07086bd9b06364c32e
  - id: LTP_82E0F55AEC3D382F
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:82e0f55aec3d382ffc129f4f165173a13c4dcdfd664c20edcdfde08730d35547
  - id: LTP_832A284618144115
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:832a284618144115ad844df9b4c3ccb4ee0c08cf9cd1a14c4bcbed8547f69cab
  - id: LTP_83A8BCF4DE700304
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:83a8bcf4de70030432c9db9be613772206cbecdef7dfebe99b01cb375a9223d5
  - id: LTP_83EECC6B473A4EE0
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:83eecc6b473a4ee07540f845f08873eba715246d6e0a1106b1e95c8db0319511
  - id: LTP_85A46F77356C5F87
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:85a46f77356c5f87a952ddda99c6c03df8aa2e95c9fa2612d232c7f9cfbbe6bb
  - id: LTP_85C6DC212C979199
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:85c6dc212c9791998c6e639cd5b11d5808988ef3762f2e775f906720b8d0a903
  - id: LTP_85DC9A2EA2A956D8
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:85dc9a2ea2a956d80a79c16355b7f712b259e121437b97a44eae5fc41281749a
  - id: LTP_86F208D4521003A5
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:86f208d4521003a5d0451c0c281f3a9b4adb52ffef5a418dc2ba897683328f85
  - id: LTP_88E657C0C8F3084A
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:88e657c0c8f3084aac944b27268fe5845c93252f10adcf826c6bd198922f1858
  - id: LTP_896519C6DE4DC296
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:896519c6de4dc29689456e49608688a4d0f932b125d338613e87515a88be7f35
  - id: LTP_8CCE8FA5BFCCA106
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:8cce8fa5bfcca10604ab1a8ef03fd1157427381e671069fe4622855feb78bcf2
  - id: LTP_8D75172B4EFCA5AB
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:8d75172b4efca5ab9baea8c33fb2d3aa3d1a44a8c45771b11c62e6c96c0e4c13
  - id: LTP_8E4283FE2952D57B
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:8e4283fe2952d57b62626a58f71dd1576c1a7f27a3a55dd156849d38b1d8049f
  - id: LTP_8E8D0AAC302EAE64
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:8e8d0aac302eae64e6d117047688e0ca08495c4b88169290ff951b5992cfc0b7
  - id: LTP_8EBCB5DB4F08A9DD
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:8ebcb5db4f08a9dd75fca60ecfe5d81374ac73a4989b66c69ad0a3a5a2aca1a5
  - id: LTP_8EEF6B34A8A62DDA
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:8eef6b34a8a62ddaa43b2c919b8f1414f0d8b1ffddfcd40eb6be8fa02bc2bcdb
  - id: LTP_8F0EEAFC8315D3BC
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:8f0eeafc8315d3bc9d2aba2bdd1ee25d5d0422cb795247e99410c1010a32b959
  - id: LTP_910B0D26D7722DBE
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:910b0d26d7722dbe621f93555b18b7be1ba5a3ff638ccbd6d47a88efb57b6a9f
  - id: LTP_9116D4EE494E16DA
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:9116d4ee494e16da15484f6dce334822f78d8385b330cc03fc4019b403aa8512
  - id: LTP_91FBCF218DE6C917
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:91fbcf218de6c91786807baab6dae40a87b79da3f1b2ca673d1ce3a8e55c18cf
  - id: LTP_922E84FFC658D432
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:922e84ffc658d432fe7e470d2b0fbd219d93cc979b8ba95330bd27f6eccaab90
  - id: LTP_92652DA4B873A330
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:92652da4b873a3305554c2259e450fc29eb22f8ce4a7a3545ed8e586273703cf
  - id: LTP_9403699F671CF95F
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:9403699f671cf95fd9d64a15af3a1252a82f61d0638e6e8cf744eed583befc43
  - id: LTP_96B52F0F7B6F6E00
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:96b52f0f7b6f6e00ae52055251ac48592888c88c4ac09b19b218b0ee55d75fe3
  - id: LTP_96B67F0F28B0192F
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:96b67f0f28b0192f1c31de69819e2976cb7bd243793a26751414de7b753a8fd6
  - id: LTP_96E9B8F051D51566
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:96e9b8f051d51566a623a96cec586432147f6ba4c50c20af0bdd4ae2a41bc148
  - id: LTP_97C6508AAB3F5CF3
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:97c6508aab3f5cf37f01a1496ebe3046f06117f7fd079a6880544aceb6596cd8
  - id: LTP_989BADB4E671AAC2
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:989badb4e671aac223a508f8064da4721b45106601f7305007113068fbd7d590
  - id: LTP_9951A69B869BED04
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:9951a69b869bed042199d8ed46706c21d63cce053a058f8cf02bd97cc4ca0fcb
  - id: LTP_99C641DE1B23D6C1
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:99c641de1b23d6c13474c286734fd2c804a2f6f0272a042443f0826bcd085184
  - id: LTP_9AA9FA96C34FAB9E
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:9aa9fa96c34fab9e0afb3cb9137a0f2cf3c2c0e271563c7a96f6d724abb30bd8
  - id: LTP_9BA35A8C11698D49
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:9ba35a8c11698d491ea27a8205c69439fa71bb895d3cdab49d41da08eff3133d
  - id: LTP_9F4ADF825E143585
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:9f4adf825e1435850f82324a052a494e42b3f7c04d9a7a5b58440e08fde1e28b
  - id: LTP_9F5D09B41AC183E5
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:9f5d09b41ac183e5d6cbbc70590232fbb9a1ab9d61537803fb7102609d8db313
  - id: LTP_9FC3886A5E9A0CDF
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:9fc3886a5e9a0cdfcf9a18093267c2fd87b18b480d9342f1bfeed5d2e4a6a887
  - id: LTP_A0CEB16379D94371
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:a0ceb16379d94371819e4ad46c8a98dce3b6fb70cba888a977623efeae9b3fda
  - id: LTP_A1024CD742C433A3
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:a1024cd742c433a3158ab7698b0fbbca6f7aa82c530fc787357682e56d63cfa1
  - id: LTP_A49D802FF404EADA
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:a49d802ff404eada2650cb670c195d182a4eee1c9c59f9d1721ba60bd752993e
  - id: LTP_A684365768862744
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:a6843657688627440cff31c487384c921a2c9af272acfc71cc329524956c3c8d
  - id: LTP_A7D8EAF1CE0F1A9B
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:a7d8eaf1ce0f1a9b2579f3b4d1bae09eb42fe450b2920fbabecb8e215a9066fb
  - id: LTP_A9833E2E2860A6B7
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:a9833e2e2860a6b7a60bb481cc2f658d3f4a689be94b61c1e2f455b36153078c
  - id: LTP_A9A7BAA6186D57BD
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:a9a7baa6186d57bdcd325fa09acbd9c13f1beeb79244d4c2fe8dc90eaf186bf0
  - id: LTP_AA8CF336E764C8A7
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:aa8cf336e764c8a726b13b43346a056ff96130ee43ef8016ff54b7c368bf2389
  - id: LTP_AA8D903F4610FB06
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:aa8d903f4610fb06fb048932d0392413953852b7ab86e0358271f80d066fb916
  - id: LTP_AB8173921096C9EE
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:ab8173921096c9ee93a9e6bfd227ff387df0b0de4333eeac386f5872e42fec8b
  - id: LTP_ABCBF7DF0ADCB22A
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:abcbf7df0adcb22aaa1cc5046ea9e823215bfa0e7386f459e6de6c0600ff478e
  - id: LTP_AC02B3D548635386
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:ac02b3d548635386d90f9e2676a9149a897a7748a9edfe681398172c08974238
  - id: LTP_AE66ABEA9F76F42F
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:ae66abea9f76f42f4d2979198131792fd10de9877d5bfd5277a619351e794c57
  - id: LTP_AF528A39B115F13D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:af528a39b115f13dadc7db46cd1240bb4ab8b9f5d5b9fea708c69234385a7095
  - id: LTP_B1E03AECF1FB1196
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:b1e03aecf1fb1196fca4dcc6632a4bfd7b8953c6ea30c888d92322f4d82a5a5d
  - id: LTP_B35AB626F46D66FB
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:b35ab626f46d66fbdc2f371c098f5e1f657427457f6a4fc2373235e71b9861ec
  - id: LTP_B39DB8E167298745
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:b39db8e167298745904d04ba29465903ab9fd839479dd30fa32cf872f1afab78
  - id: LTP_B54A4B6E6A4ABDD5
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:b54a4b6e6a4abdd5c0aba27a083a84331f51b0bfe4b6bc371bb5f198255e0f8c
  - id: LTP_B5BC41E30C9E37B0
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:b5bc41e30c9e37b042f3fb7ba1e5e205c8d2a96932a3703f17455f68ca370b8b
  - id: LTP_B6FE6370B024CFB8
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:b6fe6370b024cfb8cf7e84a0ce5989b610b13bb927504c1a5efd9dafb0545f5f
  - id: LTP_B87A5B8BC5B062AA
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:b87a5b8bc5b062aa3f77ecc6b96c406d048eda59bda8c4da063cc21268300222
  - id: LTP_BB1FF3530CCDDBB3
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:bb1ff3530ccddbb3ac123b8be7640c6088f4570b16cffdb264bd99cfdeba6d72
  - id: LTP_BBDCACF4AE2FEB1D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:bbdcacf4ae2feb1dcf10d4dce30e224926ef374959680991639245d278cd1b6e
  - id: LTP_BCC58FBC10C684E2
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:bcc58fbc10c684e2413e6e55e6ec2dec371850993c9d74ab18c40e40bdc1946b
  - id: LTP_BCF478535204545E
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:bcf478535204545e320587082f807fcba185e53427971ba6e73e4e9c9fde2259
  - id: LTP_BF3532E2FF5C89A0
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:bf3532e2ff5c89a04cabf0ad2373d1ed02e003c2364dab577643686eddda43d6
  - id: LTP_BF696EFB140C9DAF
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:bf696efb140c9dafefe90ed1df961735702e35a5b251c3a5d661ce95051eed74
  - id: LTP_C1D8DC20331CC18C
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:c1d8dc20331cc18ce11b451bb42dc00ce653d958c125cda2f6525446a894df34
  - id: LTP_C3FF5FE7F694FFE6
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:c3ff5fe7f694ffe664e6188e7d060dfc0a1989d7a6e2a29a1ee184aa98346b3e
  - id: LTP_C477F05C84F3C00D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:c477f05c84f3c00d45d2b4583a986c7cf8f215bb5985f5a9e248437091bb11d7
  - id: LTP_C5088C2E9DB5306A
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:c5088c2e9db5306ab36160ecd2304a50b15b4ef31c6ddcd3a9b914a9f468198e
  - id: LTP_C622170DA67BA6E3
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:c622170da67ba6e3daca98519d7726d7dde194367a71ba516bc5e064c5dd87e0
  - id: LTP_C7C0FBBB9024C112
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:c7c0fbbb9024c11278e72937bd0d6012b7ee59656dddccf3cf2d22b96c16c9aa
  - id: LTP_CC6A74384D72A70D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:cc6a74384d72a70de38033043e920e21ec97f2bfc4548f9941c32130e7f1ea28
  - id: LTP_CD06BB76866E1C4F
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:cd06bb76866e1c4fb82810b2a8a9aa800776ae54db60d20f406184b08ac53e12
  - id: LTP_CDDBF220A7C01FEA
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:cddbf220a7c01fea6738b9e1b2058b2e2df749538fb90a5853369ca9d9408b56
  - id: LTP_D0578B9D5D177037
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:d0578b9d5d17703746b29acd88a14995e2e7fd54255e92ad95b588aa282a4538
  - id: LTP_D071740A6BE2DE31
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:d071740a6be2de3126243f6d5ed2341607d7b81398c2b316023cf4c9e48378f0
  - id: LTP_D1DE0D497F2B612D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:d1de0d497f2b612dca4943c2d77b0e3bcc02c641c0535e37dac370166d04ae12
  - id: LTP_D3B68F2DFB1C45D5
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:d3b68f2dfb1c45d5273831e2257f1ba73bb21cade9e941f485cef3be1d67e5ef
  - id: LTP_D696A4996FBE61CF
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:d696a4996fbe61cf109c88de53af292385055b9c19a20c3a912f738cb4c5dbb6
  - id: LTP_D8D1EEF145FEB5EA
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:d8d1eef145feb5ea5f62d883cc38894c77ca496672fb9e7a833f73fab17acde1
  - id: LTP_DC994CB22DEE5DE8
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:dc994cb22dee5de80d16b8c9e03eb7d6d0e76a0aa2659feab4512943cc0aee5f
  - id: LTP_DCAED55A4DA05C29
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:dcaed55a4da05c29525febb8e1259d0ebbde45c2ceb26d4771bdee98e62fab10
  - id: LTP_DD70936BEB737A0F
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:dd70936beb737a0fe554c4975c84142806c18e5b93e8710b8b15b38cdc290623
  - id: LTP_DEF59E8529DC9CD8
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:def59e8529dc9cd82c21ae015b924d9b814a2c97d3a98bae69241ab30d42030d
  - id: LTP_E0F28EAB0253204C
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:e0f28eab0253204c6c5e76c67ef63c51ae52b079bf4711ee5917c263e8b412c9
  - id: LTP_E2D7E49A9D6EDA47
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:e2d7e49a9d6eda47eac9f0345d0077373f029ba3249d025e2aba4ec9b5eb41a8
  - id: LTP_E86DBD8C9AA9E82B
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:e86dbd8c9aa9e82b4523fc661eced84410ab6b6ed45233b70a8b81e53037486d
  - id: LTP_E8D2C5525DC42DD1
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:e8d2c5525dc42dd1ee5b8c011f94425e704c8f059b8ca040f716e54b8105bac5
  - id: LTP_E9EC00862545876A
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:e9ec00862545876a7bd02d677082ef6964eea9c5bc1c491e1b9f6f2bd4dcc174
  - id: LTP_EA51441DF7A43596
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:ea51441df7a43596dc4220b05cb6b17b79e12cef954339f26de7fb90b0c26472
  - id: LTP_EDE65A5D9B99F21F
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:ede65a5d9b99f21fb33ced7e7661ef55d666d04da587bee43aa8b4414811f002
  - id: LTP_EECDB5C492A4B4BD
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:eecdb5c492a4b4bdfd3279cabb8babfa700e991a447726c16cc469709921475b
  - id: LTP_EFF3EDE1EC749DE9
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:eff3ede1ec749de95a33a2eb6b4993dde8d57674b8ab552f3669113aa1fad280
  - id: LTP_F02D3365DCF08927
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:f02d3365dcf089272ad9d88ea452cc30b915a1c93f3187dd27c2d3494a83ee71
  - id: LTP_F26D09CAE258516C
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:f26d09cae258516c4a08f4e6eee766d00ba9050f27f288b8c37e386db8a2c230
  - id: LTP_F4AE08B0C5A16088
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:f4ae08b0c5a16088c1f307aec2795e9f1c55f6bef4d3d8945d81d2a6aa799feb
  - id: LTP_F4FEC29E9271B119
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:f4fec29e9271b119bbe6ee96ce8bb9d503da5101d70397c71b823e2ed1879f7c
  - id: LTP_F508E2594C0F3DC9
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:f508e2594c0f3dc98605d37ceca8cae2f06d126897b601731a1dba52b5e44d26
  - id: LTP_FAB12DCB20BF08A2
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:fab12dcb20bf08a250cc9e4f0395369559ec8c265b1f8173cc111246555560de
  - id: LTP_FB7250E0E0E98949
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:fb7250e0e0e98949ff9a2404eb5520dc098d3623151d04be61a3e245376d65e9
  - id: LTP_FC5D8C19ECDBC380
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:fc5d8c19ecdbc38038f015a115595cf5e94b31db754dfe5fde539098482c479f
  evidence_count: 10
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: acct
  source_fingerprint: sha256:778fab6dd104a47c066d101145ad21b83418b7731b03e1881f4bb4ccd6de761a
  recognition_fingerprint: sha256:1345deb7e6e7b9545e0844c1d6ec70504a3f19954da58471350a17344be51ce4
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 8
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: add_key
  source_fingerprint: sha256:bb9d7d97d5e05a202c79cac249656518d9edefe0cf6ccd2a2cac33c7ad6bd739
  recognition_fingerprint: sha256:e4e2bf6776c6847325b628b18ba169be7ded633cd10d4a650e78bc3b0f42b886
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 15
  unresolved_evidence_count: 5
  reason: unresolved_evidence
- syscall: adjtimex
  source_fingerprint: sha256:c17be8a0f4a471625ee5bf619cb5993cdbd886e108b7ee1cc9cbc362949a9edc
  recognition_fingerprint: sha256:554a40f0ec98ef55680d7b87c8c0de4bfa64feac2938d713f03a40688f64b4e2
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 3
  reason: unresolved_evidence
- syscall: alarm
  source_fingerprint: sha256:5061762caf00b96445d3a6532d0f653e3ad72c3451ff67190cb2dd007b36c6df
  recognition_fingerprint: sha256:9db8b0f4983a50e723aa90a114c3c2c19b4fc624a3252fa1b4649633fb46108c
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_3E8DA9E014B82702
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:3e8da9e014b8270237da29d11e36cb3568c2b222d672973a5503c5d451873729
  - id: LTP_65B70356F06E31F8
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:65b70356f06e31f852315fe3be36507e963aadb6d4dc164a7abe5194b80c9713
  - id: LTP_76A9B6CF388A8609
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:76a9b6cf388a8609eeb2a9e479fa27419ade916ce166ad5c0e8255aa5f4497d5
  - id: LTP_98EC66149EE68933
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:98ec66149ee68933043c3d08d35dea4ea3d8145e3e6e4c72dfd96c786ca3c307
  - id: LTP_B7A341967DF2BD69
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:b7a341967df2bd693bb7f1bd2a9d165ae51ec15aa83ec06f274bc9e6ed7dbd8e
  - id: LTP_C785774773FB7524
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:c785774773fb7524870d7b604061d2af95f33c66253633d4323113134440929d
  evidence_count: 15
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: arch_prctl
  source_fingerprint: sha256:352e7cb11b18f12d0d54956cad6ea6f04c6eb7ea8c286f40acf3fcc0c0c7c99d
  recognition_fingerprint: sha256:cb4c8a6cfe86d906521cdd46092a068796226454fde35dbd3dd9ac2dbe5252ec
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: bind
  source_fingerprint: sha256:6757c120aa38501c98fe10599592fb38b6815bdde448c1ea2972a7ebb3e9fcd9
  recognition_fingerprint: sha256:c141f23a9dd3d1499b5042a35e6da90f2155f94ede188e257f2b4c4abf5db578
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 9
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: bpf
  source_fingerprint: sha256:9a280c7b7b0ca4f39ef98af787831781cd61a8277419a4e182d47168763943e9
  recognition_fingerprint: sha256:5207e6df2d36f8ba077ed5fd45a353505abe948a6f136a113de541daf6d54116
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 12
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: brk
  source_fingerprint: sha256:773ad4a8d0c3ca4bea04dc5191f0c4fae1f3cf4c12aa2b09053d77e6e7cf78f9
  recognition_fingerprint: sha256:4c57daeba7581893770698134f56c32710e2d4304d7178ca5f355f387c86f254
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_7A74A699442CEB99
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:7a74a699442ceb99b8495ac52144744c5a7e995035d4c06a10971ce532e8e954
  - id: LTP_E3E59B16A96A60BC
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:e3e59b16a96a60bce3de89603588b78a310e40b3710e530d67d5c30160121e86
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: cacheflush
  source_fingerprint: sha256:65cbb47cf546e3d52fb1d343cf2f522fb89be0d41088a6ab73007fc40831cb3e
  recognition_fingerprint: sha256:af799f32b648b3d12afc18ee4775defdd924bee39447a61fc811444cb1a70cef
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_8AD8032754BC8842
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:8ad8032754bc8842e1ceffe416a3d559f5423eec53ec7db46ee81a6eeba25869
  - id: LTP_C218D3CB0AD80D90
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:c218d3cb0ad80d90bc2c5db1a2892a964c1bc89369fc4ec66a71fac08ac8f5f6
  - id: LTP_D579FCFC71E6EB6A
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:d579fcfc71e6eb6a79a4aefff0c4df8ba201988162fee4b24255c4c001c1302b
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: cachestat
  source_fingerprint: sha256:8967c456145a32184aadba3911d0b0b52ffcd2e88c5f08d3907631ec64d4d082
  recognition_fingerprint: sha256:33705ad144266317b8862366f296b08ed699a65b6e2bc5c973fe2f453f737a23
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_1325C077A1CDE514
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:1325c077a1cde5141c5f598497a0fd7e10c5adeda759688a6fc3b2f02cc64aab
  - id: LTP_2722827BC58E04CD
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:2722827bc58e04cd95d2e1065331bde64de61eef567af97baf3f31f98a5d0c2d
  - id: LTP_2D0446746669D31E
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:2d0446746669d31ecf47ff7445f765e13ab901c3816a9ff4980fd4dca4f70190
  - id: LTP_34EC9FB9C9551214
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:34ec9fb9c9551214fcca5118b8afb84e93c9e242cbd9c2674d0b9d0ec70c9566
  - id: LTP_BA9A8FE901467960
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:ba9a8fe9014679607013f8aa7b560aec873309bb14116b916767925e8499f776
  - id: LTP_EB646AEB1D23725B
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:eb646aeb1d23725b0a99a9ca649937758cb4f46ea2dee50bcdc4f419022fabac
  evidence_count: 7
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: capget
  source_fingerprint: sha256:a4adf6dfb51d8b7b763f6961c2ba419156d4f5c630b1222eb18661aa0731abd9
  recognition_fingerprint: sha256:7b2c4e6d81ae777ffec3ac706416851cd219188e908dc173a0cf3daacc617a0e
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_208C833FF12217F5
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:208c833ff12217f5ee10c2893ca4aab718793f8504783e4c1e69970fe3fc01dc
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: capset
  source_fingerprint: sha256:76e0ae5def1debb091b7c2611d3e9b29b4fbec6a1e05da1d893f0a5d3fb92fda
  recognition_fingerprint: sha256:e8c2d88d0927bef9db7d8d482d1d001d5f0f03ec341729a952a87e11cdea80f6
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 10
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: chdir
  source_fingerprint: sha256:25fb76905e5cf9ba7725b687859c07f6e6860bc3c6ca3664033dca1e1bd80444
  recognition_fingerprint: sha256:7a2836456846584aa465e6d6e24258f45c5d4cc7f32a8c5a515d61f162a0d179
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: chmod
  source_fingerprint: sha256:715beb994e68f7d92c1075f36cbad9da57dcabfc154f4f3f39aa1c282a8d3970
  recognition_fingerprint: sha256:5516a9dd726b624b25055c31b18a4e7e3564dae061ffaf940fa9811f7daa0fdd
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 15
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: chown
  source_fingerprint: sha256:becc3d2d6527b1b4d7c845031e0ae8d74d3deee859efe6bf2bc64288d94e8c18
  recognition_fingerprint: sha256:57129d8131456f2b1eb15c81fbf8899f7a30cde91b99a16c8bccc13b192e5e87
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 22
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: chroot
  source_fingerprint: sha256:cb75700a0413ef1f98114d8135c65f0fa0983a8affef1a8494c5f7a36636d723
  recognition_fingerprint: sha256:4728f677a980fa129a72d3c2c6e03cb4517c37ae2b3f16fb01b34593cdeb125d
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_07CB582EDCDF46C6
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:07cb582edcdf46c62a1d03d440393d7643aabbb757bb29565a3924c36792f7c1
  - id: LTP_701679DC8AD1E4FE
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:701679dc8ad1e4fe0f4368fb7e95da2a61882fd5681d6f4fabd0c036b789c2b8
  - id: LTP_726A6A667C79F568
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:726a6a667c79f568cc434da728424897320316b5abc4b9bea326853292004266
  - id: LTP_938E8BF5D2E7106E
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:938e8bf5d2e7106ecf408e7b6263922bc530eb892a9300a01f4e689e69d29f01
  - id: LTP_9F51EEE16C61FFB8
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:9f51eee16c61ffb8b566c7bee030e1a98dac8ede78e431bfb410adf94ec43ca7
  - id: LTP_D8BB97A8EDA10C0B
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:d8bb97a8eda10c0b185d7e229b6171562bcbbe71d7a7a496eecd9d521467f3b3
  evidence_count: 8
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: clock_adjtime
  source_fingerprint: sha256:69ddad99dde068306c21dc007b8cb8b2fc6e306e901086c515fbbadb4b124619
  recognition_fingerprint: sha256:99deb32e788f560dc5b391077cd017448bf1988b6cc328c69a75933778ab33f8
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: clock_getres
  source_fingerprint: sha256:0b9da6671694d48980d2fad4fe98a57e68a96afdfed17f11e886c0c51d5d32a6
  recognition_fingerprint: sha256:930e778e86cbefbcde9fe7a47e4e67e9e1aa343b660e509c2645ea62158cf2c9
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: clock_gettime
  source_fingerprint: sha256:316613f4c65a18374ce1a97c1f5f507263ec18197dfce2ec882ae58c875d74cd
  recognition_fingerprint: sha256:ae1c209858e7461ec7f99bfeca0384a6af7676988864efe2479b1347c5e8967d
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: clock_nanosleep
  source_fingerprint: sha256:ca8926cc5807281a0625cc6cbd69409fbca673b1b744e4900ee0006e125bcb9f
  recognition_fingerprint: sha256:3ba430d031ae59977fd91a0b1dc5c383a8ff1361b85e62c7230d0c8cd9c923d1
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: clock_settime
  source_fingerprint: sha256:e3f446caac41c3a61e96a33b8fa1926b2867c272f97cc09ae6bc6912d8e3cceb
  recognition_fingerprint: sha256:fcb3ab0ce9cc0c81e41077f19a423c1663f7dbbd9d7690ba9ff1495e7af86193
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: clone
  source_fingerprint: sha256:458a6618ec68b77336a65a488db7bf5595aaaada275374772fe678deead9bd57
  recognition_fingerprint: sha256:bc1ffacc67353fadd4809cd9883b1e42376744f80af6177ed66b9017b5973a21
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 9
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: clone3
  source_fingerprint: sha256:8a826a3bcd92cc86db6b98a2fb78ad6882ed9647021d05acbc010caad6952b43
  recognition_fingerprint: sha256:6ab33bf0a09542c2a81e8a9f045112a1c046410cda1e38159b2f13c482c9cd30
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: close
  source_fingerprint: sha256:775c18f20fd580008f1dfc93ff3b9ebdad2ea3e9b7445a3d222f7c2adcc57f68
  recognition_fingerprint: sha256:4565a4834eaf3fdc83dc9ca4fecde8b6982ed1e6b1391d2e41b06df2ccd08f3a
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_09B39E9C9254ECB2
    generated_at_utc: '2026-07-14T13:35:02.567816Z'
    content_hash: sha256:09b39e9c9254ecb24ccb5288c3f12281e9adc0b698de5c706a4f071599c3ce60
  - id: LTP_2BDE60C0E64B4DC8
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:2bde60c0e64b4dc8fc4b1e23c70973364d891d517c1f8020f709fabec59e6d0f
  - id: LTP_7E3E96A4962D78D4
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:7e3e96a4962d78d4df7e74b7a5749127317130f148655b111351c2f28839c866
  - id: LTP_BF2428964ADD116F
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:bf2428964add116f793723626820cf1b363a819d6e38ba6d31d9832e4ab1b2c0
  - id: LTP_E520E500AB3AE851
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:e520e500ab3ae8512756eb4a69fdef5de2701520040c400ce896ec773f4ab472
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: close_range
  source_fingerprint: sha256:87c3a9633957b00a8b27f889d0495aeab0e5ffaefbcd742cdc8d1c7c8f8c3cbc
  recognition_fingerprint: sha256:a635f59c2704b8110a9c615c21b9c1236398ea98ffaeca164de578548284ef49
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_31D9D767D6888DDA
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:31d9d767d6888ddaf3c03f24abe0bc874e9932a546e4cdd283ecad199e6bcc1a
  - id: LTP_425E5A3502541DE8
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:425e5a3502541de863d8b8e88eafb95db2f8d8e1f9cb88a32d8b3124950395b2
  - id: LTP_76BFF56F735A0074
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:76bff56f735a0074d725ee7dab337c42b7daf23d2ca44135affba4b983676aa8
  - id: LTP_CBF4B6C8A1458A28
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:cbf4b6c8a1458a2885c6c847b47ca93098a06580fc5fdfc3a1e483b9dab01ac4
  - id: LTP_F1DC44813DCA6A05
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:f1dc44813dca6a05d2fb0697718f8ed1da8d8b033d2c49bd0124284321f6ffd4
  - id: LTP_F4DE81D703447628
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:f4de81d70344762893139769a2724588ddb7213c4667529ce501948b3b6b43c5
  evidence_count: 8
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: cma
  source_fingerprint: sha256:07d649de4675a193dbc1f986227505f69fe1c4d4e014188e3a0612373f10caf0
  recognition_fingerprint: sha256:848660504b89d907d5dfce531fad1a738a5d08ceea1b125428b8593c26b483b9
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: confstr
  source_fingerprint: sha256:10cf8ed6019dfe96ef1008bbc1ca09204fa7a329ad703708481fb13c390e7ed3
  recognition_fingerprint: sha256:0f2e001f30d84169c3b3f5859efd9cc578d7d830189a78b9dba5ff79c403a2d4
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: connect
  source_fingerprint: sha256:a06582a3386eb0d4e92f2791535b97d23950b88031311de142270b0c2632b82d
  recognition_fingerprint: sha256:59e95693d2745b1eebf7414a66c814530575b2610dfa053b796585948531fe00
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: copy_file_range
  source_fingerprint: sha256:aad40b5c1bdb6eb2c8db3f08435599ae7bf6269435e49d3f25edbc9dc2ccb8ea
  recognition_fingerprint: sha256:78e671c9e7cb4c4d72bb105a46c1f0affc5ce6148d25f1bd43e5ef5f65e3df6e
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_76D3B1710474AAC2
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:76d3b1710474aac2ab3ab05c3535e1d9d7ce9b51219e0b3dece91a57ff8e9ca8
  - id: LTP_DB6066C00D231BA4
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:db6066c00d231ba4e40e5c33d75b9b778b61a27e92417a8cbf224d48862d8e6b
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: creat
  source_fingerprint: sha256:2b9c8808a80a99b17b14cc52110d9587c34df34efd59c7e7b794ca975ec67634
  recognition_fingerprint: sha256:a7e1021b3a915af0b7f4ddba9fead7871c9ec2e107335a5a9fd6f311dc003e67
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 12
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: delete_module
  source_fingerprint: sha256:36de1e9b3c4df3689c4ebda1d71f45588c3450eca5698989ff4340e579ceac9b
  recognition_fingerprint: sha256:5bed485aec697829bef874b0cadfe2981ac7107f270fe0fcf45d5d1bc360a71f
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: dup
  source_fingerprint: sha256:9db64fbbc90db4af18b27314f16cea69b28584ec8eac1f6f37ecc29da08d7280
  recognition_fingerprint: sha256:76a31479161a48a93a2bc9bbfb302c1cdb51b033b92e1f3578c515a5223645ac
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_2553A6069EE908FB
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:2553a6069ee908fb6de7add1ca2d92763bbabf890ce22d83d51d4857ff607d6d
  - id: LTP_511185D6DE2A63A0
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:511185d6de2a63a045d2f5f65babdf4c25b4066ece863b9f121419045563d4c9
  - id: LTP_84DBE108A850E845
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:84dbe108a850e845bf4a3cfc65c984525f06a85bcf44e616283b5ef4e16bb451
  - id: LTP_A774FC10727E8ED2
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:a774fc10727e8ed282a01bc787e12bd54a0d81a756fc45037304c5906dadb2ff
  - id: LTP_ED2BA909DF79625A
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:ed2ba909df79625a7857c363efc0303c51fef469ee87970e6b322004f28779a5
  evidence_count: 14
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: dup2
  source_fingerprint: sha256:b1211d2479e53660fdd5c81f8a3f8d17d043a983d6afb9b9027200a818319723
  recognition_fingerprint: sha256:217e9eb846db70089a978005ad83951dfa606b2bed5cce9d2ec0c13f0c245fb9
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_12A1904141AAE2EE
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:12a1904141aae2eec702c330f293e0672a34cc4240c6b0ae35b481a3244fa4e5
  - id: LTP_4F02ACC6E2F6B094
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:4f02acc6e2f6b094f06413684c004106e4c18d8f654cbb8b231de56e60aba90c
  - id: LTP_75D52C5E9C93B6D7
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:75d52c5e9c93b6d7989e3392a132ca3a319f4419c2f678533dc80d000c4891cd
  - id: LTP_9F560A103CB6F910
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:9f560a103cb6f910cc2b8fb141c7de076accd6a913e920715328e9facdfb18db
  - id: LTP_B7F51635806E7E59
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:b7f51635806e7e596b7f6a1baf152d74ca1d365a9bdfc6d3f34984ac1908632d
  - id: LTP_BDA36F61423EEB3E
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:bda36f61423eeb3e616d764edd458663817800e2f3db3adfae687bd17f6c2764
  - id: LTP_D296A517F138A0C0
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:d296a517f138a0c09a3c71729b93607cfff1709b21125573bc2ad30b48302584
  - id: LTP_DE6F80C5EFE44A9D
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:de6f80c5efe44a9d734af297a70d5597f890b2b038ec752e159caefc2425e0fc
  - id: LTP_EE8E695CF61D6D8A
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:ee8e695cf61d6d8aa981eb6e30bf3a8a53c8e8a4ad435ff362bbd78971d17088
  evidence_count: 14
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: dup3
  source_fingerprint: sha256:c4bf8028e446a97268ec49a7845dfb33d372b918a9035a2dcb791e3834ae97da
  recognition_fingerprint: sha256:be68e06ed31faf45d6f31819f7f9667a6c3759a300f6cdf459d750c4f77deb19
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_098AFE0E8E10B0EF
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:098afe0e8e10b0efa6872ee3d2ece3674b519943b59189a2758d8ab31b06ab26
  - id: LTP_1726C16756E9651C
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:1726c16756e9651c8be282bf1cdf5c30a283e32aa200934084e3c42a2aee9ff9
  - id: LTP_37C625BD7D7C5F1D
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:37c625bd7d7c5f1db42b7cacc49b4964844f0c2f977ad1a74c3960da0d662932
  - id: LTP_3A7B17AF231D4158
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:3a7b17af231d4158b2c4508e92a25435b89a569164e6dfdabc216b48e1afec9f
  - id: LTP_9B3646398697EA64
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:9b3646398697ea6481b4201006e677123cd226bb81910f45b6fa558aaa810832
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: epoll
  source_fingerprint: sha256:347af9b53085360fbe11b686a7e43c7264b4fd1bc5563b2a82e2c18d3c62d837
  recognition_fingerprint: sha256:946fa19c9b09c25edc1756461252e602cec6508b50990cb5346870ce2e6c2138
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: epoll_create
  source_fingerprint: sha256:2ea9590211c36ef191ee7a9cc1309be4c5e71b1cabf8689866e7a86b7c519faa
  recognition_fingerprint: sha256:e5d09fed716c9f721ac7ba050a828807d4b7790b49c8feb1f6ac39599c159843
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_2D1E25BD679B3494
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:2d1e25bd679b349425ebcfa9dd820bb8bc4de40949cd671adc32204c68864bbc
  - id: LTP_49A80712984D44C6
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:49a80712984d44c6383f636a8618235a539bc7a6284f32c79694f40a57092679
  - id: LTP_E7435E0CBCA319E1
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:e7435e0cbca319e18c1459e2f9187003681d326f400fc6d00b47df912010faef
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: epoll_create1
  source_fingerprint: sha256:adca31441041b76146329e13f3341f54806994f6886cc309be85ea3759259134
  recognition_fingerprint: sha256:c0ce206d6879396d10ddb988813202e71d74b92af72f9903965293670cd17b28
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_11C0431607FD5753
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:11c0431607fd57533d1c5963042c455cbbde73e3b6692aa38141822fd5cf6e40
  - id: LTP_5D8D2B3BEDA79604
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:5d8d2b3beda79604301b79695ead77bb1cca6ec4c1e6b679aabacb702befdccf
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: epoll_ctl
  source_fingerprint: sha256:15462445432b857f20d64c8de3ac72e00224536e107de176479eb54fd86cd0b6
  recognition_fingerprint: sha256:8525e9b25f544dc49c0c7ff7ae09375dd8112e6b1b4cd4b625229714f3d00c91
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_03E15C829583D726
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:03e15c829583d72607f7819e1f423769ae2fb741011274db3039f5c8c64a0566
  - id: LTP_4953FAD330ADE150
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:4953fad330ade1503bf7a6d4d6bf2c353a337844f58042ceb3214149d1025945
  - id: LTP_5350E2FAFAB0B884
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:5350e2fafab0b8846fbad0818b8aa25a32113a0eeb83194ff3db7fe1a40ebb93
  - id: LTP_5883CD050463E9E8
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:5883cd050463e9e8d7a616eded312d138c7a9d06ee39d3947a818a32e9738f36
  - id: LTP_6FFB17DB762F3167
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:6ffb17db762f3167790a052bae0fa49f44b1075991c29dcec06f56509e9ae743
  - id: LTP_82479A4A2E248995
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:82479a4a2e248995f5895ae35ed4681f3a19a267672d269747f2153c269965cb
  - id: LTP_83709E56D6285F71
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:83709e56d6285f71dce5dcd5f54aa0ba99d44ddef002f1e6cc53f2fce6075678
  - id: LTP_9672C6DE0FC3E7D0
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:9672c6de0fc3e7d025f8da536fe17501f4c7f3121f98411c58506bb5c3bb1acb
  - id: LTP_ADEB5FE2DF97542A
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:adeb5fe2df97542a0ab4a690668fb6ff8bf5dabf6dc571b9f1ad50e9a6cd3c7e
  - id: LTP_B41BE95567D414C7
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:b41be95567d414c705f43179cd8a4bb3315fb1fb54b2f998f6998f9ea1d78991
  - id: LTP_CBB1680336D53D2A
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:cbb1680336d53d2a1eeae3e329d0c4d0144ad9da05ca737d1a9573a537224a39
  - id: LTP_CBD286AFB66B79D0
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:cbd286afb66b79d0a9987a4526390c35ee1a496ec0983095171ee20c4ff5fc76
  evidence_count: 10
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: epoll_pwait
  source_fingerprint: sha256:472ff71fd83fe184338308aea8448cbe0618ac38bbce8f89a98f2f4570a81f25
  recognition_fingerprint: sha256:72cc389343f568a25ae37b16aeb6cd82472abd9095ac3bdd7a663d180b7db5c8
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 7
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: epoll_wait
  source_fingerprint: sha256:a1c8ea8bd0f5c8d6b3ad19754840fed93f92118f11b73947ce40f9821dd7b0b3
  recognition_fingerprint: sha256:b688a5c87513117e483cea62c2e9bb65349fc6d15b347786c4fb65019c08f5e8
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_225DA846BF111CDF
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:225da846bf111cdf019d15ff5353a73eea9ac275f40c47c96f53b174fd78a3bd
  - id: LTP_337F129FE78A007D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:337f129fe78a007d42d70488e45137b429d687efe4f0671d06d4b854e900a581
  - id: LTP_4883FC77EC1F2BB9
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:4883fc77ec1f2bb9401befeff145c568628d39e2083f3a11e96dbf63338f5ab0
  - id: LTP_5AEA06C99B2F5E9A
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:5aea06c99b2f5e9a2811d8c6feab9014b5bdca20a76b7349e5a996e22a5d8ce6
  - id: LTP_724D6E370813285F
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:724d6e370813285f579a476ab7dbb60e57f3cea1b2b8436c902e5235c64b4589
  - id: LTP_7C8CA0FD5D141A05
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:7c8ca0fd5d141a05ae63bdb913dd1baa2ed7c8f3b88cfd7d61e1da0ccf166cab
  - id: LTP_9244F92CE966130C
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:9244f92ce966130c3975fb7d69aabeebbf68039c0341e903ef2044aa5e419100
  - id: LTP_B3F848BCBCBAB559
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:b3f848bcbcbab5597d6e4e2abe10464ca363e060e65589801a91a6bac9a7af58
  - id: LTP_D75F86A534CB6E02
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:d75f86a534cb6e02dbd3de6fb64ef149396db4e63651815433cdec7ec6f9ce05
  evidence_count: 19
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: eventfd
  source_fingerprint: sha256:d2030c0ffbbb1228179acd84082f1a18d48af2a3eaab0724704d4f0f0bb693df
  recognition_fingerprint: sha256:fc17c23305940cb2eb9eddb986244ec3ed851601b74f9f9ffef10463dcda5b27
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_1AA7F21DA5C55800
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:1aa7f21da5c558007d9fd7b2943285112b799046994663336b5a0137eb08fc30
  - id: LTP_5622491E8A2227F2
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:5622491e8a2227f2b5f90dbefb8a45560139a3cfbea5be104cbfca5fe10c4e09
  evidence_count: 12
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: eventfd2
  source_fingerprint: sha256:b8278fa23da737be991e2c2088bc95163bb9b6725ce760c56357be4e14f5914a
  recognition_fingerprint: sha256:83dc241cdfe0351f9dd895d34cfacf1853178c8b1c5a2d6c27e291a2c8c241f5
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 7
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: execl
  source_fingerprint: sha256:a2d3304c4459595d637129f41ad14465223c7f76359c500c29907ee00dc3d872
  recognition_fingerprint: sha256:46fe278af60d60ac95feab258debf1a7d214e1d3096e71807c4b4d3bbac8dcdf
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: execle
  source_fingerprint: sha256:a5fe713402ac6e15d3083828b3e241b1187db906c8646ac45890c5300a4bb4d4
  recognition_fingerprint: sha256:b1bfc7b09327623b6df6a93ed2dadaa19ad9c901c2c8ca9c0a3de9000e43ce22
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: execlp
  source_fingerprint: sha256:f62593d8fcb54a93b671583bd6c320c5d3b006e3b3f9a30e912533fcab5618aa
  recognition_fingerprint: sha256:506b5d6fff203514cc9df740cafd70aa43dedfc371dd4a8c876da1fe4d1a20e4
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: execv
  source_fingerprint: sha256:1084eda95b8d01131e2b61e53b04fccccf687689139d941b1c27923679ad77d4
  recognition_fingerprint: sha256:8320ce5c168c0685b72aec87153c225f1a7c579ce10f2d16fd45c0a30c7b934b
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: execve
  source_fingerprint: sha256:b2330d9faaf12c8cc5e333cf16b1c4da6f9e5c7aebd4c9a2ab4e913e768e0794
  recognition_fingerprint: sha256:7d1d0ef5fe562b7075015f818e7d8473d02fc0c2330c176acedcd631ed8ef971
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 8
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: execveat
  source_fingerprint: sha256:1c0517838680a2f98ef901b32e927617915fe5df0b66079e2d02d3694a133880
  recognition_fingerprint: sha256:8159c81533c0bbd2c6750e6f6f2f09d9059a7403229e60fb5410c88a3932c4f7
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_137CD2E37BF545BF
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:137cd2e37bf545bf278b5e0ebcb6ca710389422a5eecfd8aa175376062576801
  - id: LTP_3E9AD2C1B3BE9041
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:3e9ad2c1b3be9041648fef40e3d374ef184de638884e13d09165f53b701ed8e7
  - id: LTP_82D99A9CBFB63C68
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:82d99a9cbfb63c68833178831833414e9b518a6d6d3f078213e719f42965d630
  - id: LTP_ACF7A30AF3B10973
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:acf7a30af3b10973088f22334a5e2b35a00bbc3ff6530b1fb644856f637f06e4
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: execvp
  source_fingerprint: sha256:41e1227e84255d16acdf361caaea4832da0ec125cd81b6beefeff3c45d631647
  recognition_fingerprint: sha256:ca5a335285650024b2ad3acb07fd663a8b281000885372364cc26dac35ad65f4
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: exit
  source_fingerprint: sha256:ae380540dffbdd23fde843efc604b5ea685c8b930d59a34157a7bbd1d320f948
  recognition_fingerprint: sha256:4361424f38ca0544d6cd9362a2b58b958a4f25340a0ba26a1fb4ad6323146e84
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: exit_group
  source_fingerprint: sha256:ea36f07d63fc4d5ee6abbbf46e2880d653b96fe07c1b467e4c725c9ea18ed16a
  recognition_fingerprint: sha256:d26aa730d8c8299977da11f7b09264d95ef7193cab48c4f0ca883f4191e7fda1
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_33D137B9002503E5
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:33d137b9002503e527752b0d755df2a42b8ee4a5560a746646216385fa7bf49d
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: faccessat
  source_fingerprint: sha256:15e2e0228de9f01217d7f29e60169a88185ae01a2f1233b7c1b71c24ba7495e0
  recognition_fingerprint: sha256:906ead62bfbcd1eb59e9bbff0f7877030b415ecfbcb15d0aed40af151baa1dcf
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: faccessat2
  source_fingerprint: sha256:5dc5e64d7ca321293b91ddbb0b8dc58ae523b9757bfdb97d868e8d42cf169c03
  recognition_fingerprint: sha256:3fd7748f31e63d4b7a52766eb4474678e8042a5cb96597a3dc5aeaf3810eabc6
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_025CF701276457CB
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:025cf701276457cb8418eabce2995b043ccbd239d602beb3b3dcb5addb042fb6
  - id: LTP_122500959CDABFC9
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:122500959cdabfc9d20c8aa9d99107a6125c31bffec0135b65b5973aea5f5be4
  - id: LTP_144706EDC721819A
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:144706edc721819a5d8c2423f2ff01ddae8836248c2350964e3193232e22582a
  - id: LTP_39715C70E797C1B1
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:39715c70e797c1b1b285ec6aff1a8570032a77a7b565cca02e4972f6d8b477f5
  - id: LTP_3C8D01B8140DB122
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:3c8d01b8140db122142b9432d924effc7d761792b1bc511d0fd9f5fd9c4030e4
  - id: LTP_437CFCD991A666C9
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:437cfcd991a666c9360e9024835d7e6a8c5727cae5e72567f944a93ce03239b0
  - id: LTP_4C1F446C9C520B36
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:4c1f446c9c520b36b7f3b5a39c42fea74e7befa2adf95e4a919a1bb760184320
  - id: LTP_98A871A86ACC8672
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:98a871a86acc86728d6c903f341f753372ba05c0b3d185fcef8f1b7ee45edbf9
  - id: LTP_C2909AC2ECEDED94
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:c2909ac2eceded9462052049abaac7e397b9366e68188495ac945f457e9c9ae1
  - id: LTP_D0E55E3A04E47FFC
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:d0e55e3a04e47ffc4f925f5431f40559b5ff8c3f61e7c29d44951d656ac7b52d
  - id: LTP_D77858597BCC1C13
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:d77858597bcc1c13039ec0dd178b90fb23905df40451046331495fe91dc2faf1
  - id: LTP_E81373866A3C5AB3
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:e81373866a3c5ab3a596675ac5683df6313d8307efa82d7ec6b78f61d965cf0c
  - id: LTP_F7B8EDE302D5D08A
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:f7b8ede302d5d08a04e637eea3a051fcb4238d4367e86ea376079213b833dfeb
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: fadvise
  source_fingerprint: sha256:8db88f14dacac570aba10be646c9ebb89e4cba75bbfe114cc3a5608f3d66030c
  recognition_fingerprint: sha256:ddcbcccceb6af697a9fbfae72819e80bdd98a148527219418b293a477e47f609
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: fallocate
  source_fingerprint: sha256:0cff563cf65acccc9e28b6f54bf93e258e282eca099fc61b918d27998af1ac03
  recognition_fingerprint: sha256:a9519d91f0b47a29cf8a383a5386c96ed0e921ff4d775b8496011f8fb34ef960
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 12
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: fanotify
  source_fingerprint: sha256:d6021924fd83f220c44821189fcd67e5810f3a707809a0eb24976729f5292c30
  recognition_fingerprint: sha256:74991146f5e2b17a2701f9443e021a038cc9ce585209ded32c4d9f9b3ce2d198
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 27
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: fchdir
  source_fingerprint: sha256:31c91baafe050edaf7020e951d65d9cf1a76c0db8c1fb9872ffd95376207b99f
  recognition_fingerprint: sha256:6504aca45dc7753642327bf455e9682d487bf27f2ce401584142a8f806b826a8
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_17B7A9460939622A
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:17b7a9460939622a41226aa0c0191c618d2a9b74c6e2321e127b1ba067b85bff
  - id: LTP_9E5F965A018077D2
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:9e5f965a018077d2717e277a62f031c3c0d43765b53fd9a4b5cb5db42fbd3395
  - id: LTP_CCC36F43E9463D3E
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:ccc36f43e9463d3e65e732efa9e9d62af421e5d01bac07a5d343fc88f368505c
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: fchmod
  source_fingerprint: sha256:028ad1a908f72e55840780a02295162d05f3dd4a0b77358288e1b7acdb418ee7
  recognition_fingerprint: sha256:c8be4c05a0cb37c35e73523fbd46470e15c3319642f1377a28feffdfe920981a
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_371BDA67CB8813FD
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:371bda67cb8813fdff6eeb64e8a7d946a578b235b292932c7146d1719b4e6264
  - id: LTP_470C0966080C93EF
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:470c0966080c93efafa4bcea1083f34ab24a3c68263c2f688031a830ea7b0032
  - id: LTP_A1B6FBC6EF800331
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:a1b6fbc6ef80033120dca0f6c08260bcd1a078ef1154f9ed5e9603f3dc71f0b0
  - id: LTP_F1299BC5F92BF26E
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:f1299bc5f92bf26e06b257215fcb3155094ff3ac21791f9b95d31551aff7d4b9
  - id: LTP_F421E1E61753B72C
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:f421e1e61753b72c9f4a639632f6078fd4194f57cff8b8688b962838275ae079
  evidence_count: 12
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: fchmodat
  source_fingerprint: sha256:4d29d9e985f186f87bc1a487c528ba548c4183452847241758917e49a73016d5
  recognition_fingerprint: sha256:5aa7401c0d6060e92fb0e555f0df4b6ba1db777e377e9433d7c2c8d751c9720c
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_1A2B889BBD9A1444
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:1a2b889bbd9a1444ff1e3ab42ab6ff0e8e1eb6931564df4b9910946a4a2fb5b7
  - id: LTP_3073AC57544A6A6A
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:3073ac57544a6a6a181bd3ced49d16a7499f79e9efbe267a323ad7d86356ef48
  - id: LTP_4FAABB99B8EB0CE9
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:4faabb99b8eb0ce9c5ffe8535e0b403b19979de168127949e0eab0df5299aa1b
  - id: LTP_661F97F83268E2F4
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:661f97f83268e2f4d1c417d28f14c1fa766d992999d1ea353fff85961fea2a39
  - id: LTP_8A4C03F737A3CEE6
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:8a4c03f737a3cee6ad7b10bfa667b15524ee46f96a3bfa1532a7b6e5276c0405
  - id: LTP_B4FD0E2B4B84F458
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:b4fd0e2b4b84f458bbdc6637e1f2bce1a9bbd8b0b0f9e69ed34a8bfae2ad8153
  - id: LTP_D9ED751DFFC3CC63
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:d9ed751dffc3cc63fa927cf537f53eabaeb079b6464af1baade433f7f993c513
  - id: LTP_EAAD13B42BE1ED54
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:eaad13b42be1ed54485b14056332e1e243ddd37756f3edea8ec2a673e067c944
  - id: LTP_F04C2129F0253CC0
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:f04c2129f0253cc075ad2c5f51c7af13bc903d57bb74f6876d354698009716e6
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: fchmodat2
  source_fingerprint: sha256:e96e7b6953864f897b8be9a7e3a3a804b2cfa77d6533c5b34720f53aeb2c9f1c
  recognition_fingerprint: sha256:7e55fe1a093c191eda133b26747276d644ef6c1e9736051dacf1284a428cc5ed
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_5F2B89F71FACBDF3
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:5f2b89f71facbdf32bbc8df9c9d9729e5608377c7ec1ba48218d181a8930bef0
  - id: LTP_AA8EF9120C0B6329
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:aa8ef9120c0b6329bafd5fe42fd05966b7edb210ba222cb09afd0d77c7546ed9
  - id: LTP_C1C97EB1E917FD3D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:c1c97eb1e917fd3d56d403eaf0f0b9890b663872f78a31af0487f6a0cf92b5f7
  - id: LTP_F65E54AE96F20D41
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:f65e54ae96f20d41e260ec1e6e4cc47a424d61abebb7f8bb25f00f0033efaa98
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: fchown
  source_fingerprint: sha256:2eb51c1d6396d1986ae77fda30bc81607c5bc29db2df787ab4f1703a417ce120
  recognition_fingerprint: sha256:c0470fb1ebca6d9aff22a1936f4fe94a0187d79bf0b88efd3eaa3087bd44e6e6
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 10
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: fcntl
  source_fingerprint: sha256:5cbdaae6fbaa60becf78488e060da2b184b30ae5416d81430c206f20b1be2c92
  recognition_fingerprint: sha256:43c8d6f7c64b890c2ff600e4c393ce9b3c2b624462b4c86c82ef07a4821c6de5
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 72
  unresolved_evidence_count: 14
  reason: unresolved_evidence
- syscall: fdatasync
  source_fingerprint: sha256:3d40a49b1adbd564fdba1333258d000c6ffe6182432594eecc468c6de28b35fa
  recognition_fingerprint: sha256:f631ed825e571b0745f0b401d503c7e7ab18b931d03ef45836452bb38fd1304d
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: fgetxattr
  source_fingerprint: sha256:09ea1ba24b838f0bb1d84d8763e6ad2754f40508cdccdaf0254a227939ef9b27
  recognition_fingerprint: sha256:b1d6735d3d42e6ec6fe99793f427fde1cda87d57ce290eacf56e27c681548c97
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 7
  unresolved_evidence_count: 6
  reason: unresolved_evidence
- syscall: file_attr
  source_fingerprint: sha256:bf2d8d8b7b62bf7390e7cc240c2168e639fc4152f5cb56d5eb55ca92796436a5
  recognition_fingerprint: sha256:ff9d6ea2165920134bf4d298848c6396822389f6b82ad4e832f379225c58afff
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: finit_module
  source_fingerprint: sha256:468391db12f3577f2aeed0e2d23b8444baa5582661434142ee2dcc16de9da5b0
  recognition_fingerprint: sha256:d33a3bb0bbb400e9c3c11df16b070651c158a886f44473606fc5a6ab927b01a9
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: flistxattr
  source_fingerprint: sha256:1df26fe5b67819ad8f7cf3801f8fd2494aef0efaa875294cbef8edb0fc935bcc
  recognition_fingerprint: sha256:05338e110c79072dc630045bf64f46612431fa379f44cfa09a333dac18164907
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_609D7178B8A77C1F
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:609d7178b8a77c1f760e1613cdd180971f8a52082857ee05dc4e1860d8870c75
  - id: LTP_7AF560F7F0432A01
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:7af560f7f0432a016d6b6511c9b2031073915d795966ee391c87f16f0159ddb7
  - id: LTP_E7761F889A77DB75
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:e7761f889a77db75347da4d1856e611c19ba86e2b0948b1c89addb408639cc50
  - id: LTP_F7EAB2DB74BE5612
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:f7eab2db74be5612fc11d80b971dc7c3a64e07361717e158cf307b48f55bc105
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: flock
  source_fingerprint: sha256:6d04724ae5815e41dbb7838662014447338102d4e5a178acd4a28b48531fef78
  recognition_fingerprint: sha256:00579c4fdf361b38590277aa77c96604e392e9a8bc93d597c2239b5cfc353fe0
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_04A84187DEC4CF09
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:04a84187dec4cf09a39d6ca1c97accea65e020ac8a79b7d541d3d215af9fee07
  - id: LTP_245110930B22BF5C
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:245110930b22bf5c23a7fb0a2858242e8f2667f1edc08b79380bc66f38de4f16
  - id: LTP_6A70899352D69A0B
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:6a70899352d69a0b72a8408a0c9b9fdbfefbf2b4c2020fc413cc7ca20a82e7eb
  - id: LTP_9256D223D5EF4AF0
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:9256d223d5ef4af074c553bc4cafca071fbbaf943e052838f225a07d0f9c735b
  - id: LTP_A2A80201A4364230
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:a2a80201a43642307d66311b722952c97f20a2d1df703bba5e772d1fecb0fc22
  - id: LTP_AE4CE76865CD4D6D
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:ae4ce76865cd4d6d5dbefdd5c543b98c81eb7035f5e93a9b68eff25f70dccd68
  - id: LTP_B5959FE5199E821F
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:b5959fe5199e821fd47d208a69762e899a29254a1871f10cc15dc2c9577af0bf
  - id: LTP_B8EA21096E591EBB
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:b8ea21096e591ebbdda1f1bcca289f1e6caf469521cb5e94737aed073acc3e52
  - id: LTP_D63AFAA6729CB519
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:d63afaa6729cb51946dd986124d1064eca5a07e17cbc879b3d9f5db94f0bbd60
  - id: LTP_FB047DBB72D78D19
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:fb047dbb72d78d19892576b231423c9fb491732f808ead6728e4a8331ebe56b8
  evidence_count: 18
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: fmtmsg
  source_fingerprint: sha256:2eba32d5f7b2943a2cbeef2d100eaeae1770d7258448509b75aa4a2a00f5547d
  recognition_fingerprint: sha256:a8706b2f8550a034e401c6194218b38952acaaac1344e87bb8ea0035938bdb09
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: fork
  source_fingerprint: sha256:cced5d1a1b3d08a3c57b7c29d15fdf132aded15a5dd8eb1fd1ae05b2f5fd4a2d
  recognition_fingerprint: sha256:2d613eb9dfb2d0b07f4da7c723401d65021d6117c30c87d10c493f0211189055
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 17
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: fpathconf
  source_fingerprint: sha256:73901aa0c6a6d05a52445fb7d429158b373e8eb3f2a3d37ca853fd645ccbb3f4
  recognition_fingerprint: sha256:cb3efb4c05cfe380ca7cccb99297fa48c299b5a1f19e29c9d4582bf932d9ac36
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_09FED6AAC1020069
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:09fed6aac10200695fa52504d74d6d33fedcd9161a18712bfd9091b75d2d42cd
  - id: LTP_1EEDAE05876D0546
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:1eedae05876d0546a06229ddefc954ef7ff84b7908ab66194614b36350aabe3a
  - id: LTP_20DA453342D2F4AB
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:20da453342d2f4abaadcd362ef84ddb13bc285d1ea6896b02f0935c6119bcbc1
  - id: LTP_33C492F97B790AB8
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:33c492f97b790ab8db632d4947a4680a5cf40a46cb1352a916db41f7bf498b56
  - id: LTP_582938D6E8E17DB3
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:582938d6e8e17db3cae7f95ec69d1df0477bbb60f9cb7deff3d38d4c4f2e5e5b
  - id: LTP_963EAEB0B41C7934
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:963eaeb0b41c793497fc581a61908ddee66e176676088d00abedf28aee76c396
  - id: LTP_BF679B7A7E60BCFD
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:bf679b7a7e60bcfde914d41ecd3496f023f92f23d56985eb98c01f4f04aa0476
  - id: LTP_D1DAB36EB37FCA27
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:d1dab36eb37fca2734bfed35e244b92636b520cc5b00780b16485ba400a93c9c
  - id: LTP_FF1A8A6101CEA37E
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:ff1a8a6101cea37e68836f7bb0b8be80c2bca18d8fa2c7adc3e6b2f6f56aeed3
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: fremovexattr
  source_fingerprint: sha256:075e1febde829765a7f75e20ca109e0f4fc633bb254f9b17ff76bdb2ad789155
  recognition_fingerprint: sha256:ab3f57256f5865c8b885b3bb915c63204dd23ef2370b8e698099cbfa00c77c7d
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: fsconfig
  source_fingerprint: sha256:5f21700ba19ea2010f3e8cf314d7d5c985eff4fadc9bb314d1cc1e30ee44e5a9
  recognition_fingerprint: sha256:a6bb9ce8cc81117395cff709bf2386f1295da42fd0565ca231de16c067fe3eac
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_021CFAE8581109DA
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:021cfae8581109da3a7d7ae276fb94ad5578ba0ac4127c6200e9ee2a76eaef92
  - id: LTP_0B35C54F2F39E4D4
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:0b35c54f2f39e4d4f1f957c59cab2e6209ed2b831085b94b24bc981b46b85207
  - id: LTP_0D9BB2CB02786128
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:0d9bb2cb02786128d0b6787ef69dfa0ba2304778ae0fdb2cfb30cadca3a24104
  - id: LTP_0DF4BC077C390176
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:0df4bc077c39017611f608059ba712c4d94d03c275566d0bfa2594ead40d2867
  - id: LTP_11235D2EF3DC4C5C
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:11235d2ef3dc4c5c42211f5184557081dbc86a707bec8ea9a609eb3a33dc6fec
  - id: LTP_1918D556CB808466
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:1918d556cb80846648017e6916fd67d043842baf1aa0d6697b4f234582a22ba2
  - id: LTP_1C8100D018645855
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:1c8100d018645855f54fd4024f3db43651a82218bd02a668e10f181123011474
  - id: LTP_2433DF1752AE54B7
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:2433df1752ae54b710f6f0bac484afcb5f66a5f1b57a196a7d0c7d75db6a27e1
  - id: LTP_2BBDFB48EF060066
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:2bbdfb48ef060066789b548a4d5d4b8ac13f7e32c5ea336576bbeb120f025b17
  - id: LTP_3D50FA09D36623FF
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:3d50fa09d36623fffde1fa33fa425aa0a2ab222432f04260a1b09464714ac445
  - id: LTP_46401248F52AD892
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:46401248f52ad8924a3c31e565c25c8a8da4ba07659463875da6667070642fc6
  - id: LTP_50972E17C52A9EF6
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:50972e17c52a9ef653b63496b6a6bd94cd5b8c3e5cb07628c83f8549c4c432c2
  - id: LTP_53B499F623D50A0A
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:53b499f623d50a0a23004b18b9b7ee39d1459be6be11c39caee652c8af08720c
  - id: LTP_55D4EF674AFB4ED1
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:55d4ef674afb4ed18d774d3424a69a5f0a7d12f7b13428bcd3056fabb7fc1dbd
  - id: LTP_55EFF664BDCE3E21
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:55eff664bdce3e210c590804688d0c68df3fb4a1efdd739d03bf2104f0391524
  - id: LTP_5DC368435F71390F
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:5dc368435f71390f43761dbbb462a38647aba92c7995129b5509d22d95321d18
  - id: LTP_6090C26F5D5D8E5D
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:6090c26f5d5d8e5dafdf6638326af98a9a9ce1fc49d99344b912ab0b41152f80
  - id: LTP_708F721FB3456F82
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:708f721fb3456f82efd4d16801e8f83d30905db3aa1095f1373675804ef54437
  - id: LTP_7ECC43C03A3DCB14
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:7ecc43c03a3dcb1493e8e5c4e4442fd875eea9276c74121b858d4aace81ca2b2
  - id: LTP_7FCEEF8C37201FC7
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:7fceef8c37201fc7e07757f6ce4baef28445c2016190a1da358c6e2a69d24b7e
  - id: LTP_7FD1D8A10AC952F2
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:7fd1d8a10ac952f2510d25f1268c905680a9f0ee2267d8623c473d4eaf3acad8
  - id: LTP_88D0821E4776E388
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:88d0821e4776e388c36b0ee5157c9c5e12dc2515836b77323839f5555dfd21f5
  - id: LTP_9FE663EAF1F0ABCF
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:9fe663eaf1f0abcf4e774018036bc5f1bf44371306aa0389921c6c1c74875f55
  - id: LTP_A9DD0D461E032A07
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:a9dd0d461e032a07daed5ebd8416b80a44c0e21234444c6375417d490fe93a7f
  - id: LTP_AC7D82691053FF4D
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:ac7d82691053ff4dfa1c4e766e3fd1865abb31725c097d3da0349dc0a7f0eb77
  - id: LTP_B4B9F07E1C1A3826
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:b4b9f07e1c1a382683d5c7d52e11300fba6492d573b6d2cee1c2f551004f809f
  - id: LTP_C678E0C87280F82D
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:c678e0c87280f82d3fbeb7b859b6c1b878b9de4ef9fcf88ff32c2152dd920888
  - id: LTP_D5D78F93265A1980
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:d5d78f93265a1980dcec0e05378c5e30d8f6c3bb963ad2367697440289a91f38
  - id: LTP_D615E29C0C4C9CCB
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:d615e29c0c4c9ccb58d09cab501a27a798ec509596d1f39f299305ba88302394
  - id: LTP_E6750A641272AF1B
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:e6750a641272af1b21af53bcf9d70198331e29c3a29869c2a9d8198358713340
  - id: LTP_EBCE1A2B8CE59ECE
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:ebce1a2b8ce59eceb37d40bdea3e9510b8bfa5052c53af1cf82a93d8d730b215
  - id: LTP_F66DDB5A0EBC5C9F
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:f66ddb5a0ebc5c9fd511ac1467dd9240fa3749f348e795049df2288dedc3464b
  - id: LTP_FDE0B30F1CFCAA4B
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:fde0b30f1cfcaa4b082e9787098c51e6f110c82f63788257a23fcb450859424b
  evidence_count: 9
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: fsetxattr
  source_fingerprint: sha256:d58c6a125271cb27e0e7af15dee721aa0b38dd05a8f0594af2fb39ca0057c0b8
  recognition_fingerprint: sha256:31f39ef748a339d23db70e0c97c3f525707a80c065c4af2e1db3eb142bcc3ea4
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 4
  reason: unresolved_evidence
- syscall: fsmount
  source_fingerprint: sha256:4cb0a96ad974cf2f8cc60f89bb599509e6b626a7f68d80417dcc6302afc52f12
  recognition_fingerprint: sha256:89c661f9014f2cd91c0747f4b655f6e2370e81197016dbb8519c78fd8a6296e2
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: fsopen
  source_fingerprint: sha256:e68be8a61d079622229c3509eae66a221e1af386915bfbcc08013d946d79c3b6
  recognition_fingerprint: sha256:30961b107b86d202297ebac6d75e972b9030e89b1f657db6df18650b6bafe0cb
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: fspick
  source_fingerprint: sha256:cea6a1c90e6182fb256f5c28128ca1aabf89228e8728cc4788bf1221f64ae5b1
  recognition_fingerprint: sha256:f04fce5a8ede40e34a49e1b5a0d449624ab8a67ae8d6dccda3264061948447a1
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: fstat
  source_fingerprint: sha256:1f83263c89cb8c37140be52e887dd4d27559fa55caac9a9ce5cbefc10bb3e677
  recognition_fingerprint: sha256:77a8219787b5c8311c1391d1c5c05a816319b4cb31e4fc6cdcbc96374e0e969c
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_875F17F6F720BEC2
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:875f17f6f720bec20b8d1e72afaca73a198b1e5ca71ada0dc172c5d24a4b8358
  - id: LTP_B0C8B999421C6345
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:b0c8b999421c634558a17ac8ac624863752493e300f87a7ffcfe070805977b54
  - id: LTP_B4AADBA5EA4C395B
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:b4aadba5ea4c395b6ed2195c452ebb3f4f82718e245ac8f343487dba3a2d5b01
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: fstatat
  source_fingerprint: sha256:50e7c45ff4fc0cdd167f5c60897ca8a80d660ba49ab3bfc751d6995fc9c8ba23
  recognition_fingerprint: sha256:5f57583b2bbfdb0392087381800d522ab3277ca6ae463c1d1ce3d160f732e48e
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: fstatfs
  source_fingerprint: sha256:65ee20b2ce98c8ebf8154ee6ca0db6010faf7792a8e9bcdef002d006356f77cb
  recognition_fingerprint: sha256:6719c52ce6a3e5da098916918f771e0ad47279f313e495c4a16305f9e7cff72e
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_14072975543D9890
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:14072975543d989032ee2c1247c1cb9fca032296f9b07f3e40d9eee84ddd0465
  - id: LTP_BF183AB6911D1BAF
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:bf183ab6911d1baf67d6ae1d479cf44569f093f9d9f0820d1323b7afe6833b44
  - id: LTP_C04292C48EC89063
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:c04292c48ec890631dad7462ac866fdf563ed45287d5de2025bc8babd3c8c2c5
  - id: LTP_DC01A8115E3EC579
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:dc01a8115e3ec5790f9a19d9e67db768236bbc57055c40be1ce68501a85d4254
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: fsync
  source_fingerprint: sha256:752e7996e3f21d7a0e6fd06f19136db25b9c58b8c532fca4a037d98896e63d6f
  recognition_fingerprint: sha256:e30b63e698a6a79753b6848b30b70fcc2fcc213b6482f36d8a79bfa42b73e3c3
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: ftruncate
  source_fingerprint: sha256:3500dd0b2efea4bc021db8f8d1ea57693a7397ba0d356ec4a46df2e1137efc8c
  recognition_fingerprint: sha256:8d4ca718ca9447ef64ec1bc14ee4a11dda7744603ff5ebb2d26de4c140e7edb0
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_02D0577172D97F4B
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:02d0577172d97f4b0c53b13d33076d3efcfec173bbca9004cf800d6afc185499
  - id: LTP_213EA37A2B59AB99
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:213ea37a2b59ab99adf7f686665e25ddbe33d1ab0987a2491350f663626e280c
  - id: LTP_46AA49209C30E739
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:46aa49209c30e739363f6cd984100b84e2a071850a4962d4d4431c6f8305ba46
  - id: LTP_63E6527501A08F92
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:63e6527501a08f92aa43e68124f897c040ee1772af6738c64e18e0d766c0823e
  - id: LTP_EB214534D857AE95
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:eb214534d857ae95cd746cbfc32631b6ce2f8653bb7bcf3b1fe2839727245cf8
  - id: LTP_F21B2458879EFBAB
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:f21b2458879efbab884769d320f035c7cf77ff7769cb05b8898608c5b9e8fa6a
  evidence_count: 7
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: futex
  source_fingerprint: sha256:318382a96dc7560c485e768c451a6890a1e75a6bd3694c1608b73b6719e97c59
  recognition_fingerprint: sha256:e2e1a72a022ab538f73ff54b9927dcf53c5d4a262104fa33e25c7261c1906d58
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 8
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: futimesat
  source_fingerprint: sha256:996c44dc07e9ecef905d2fd6147c84ddc5b11a779e0f4ac0c5bb90df6e073167
  recognition_fingerprint: sha256:0e189f81e0555cc396d6fe255842ab742fe95277d347df3ee152cb53c7aa3e1c
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: get_mempolicy
  source_fingerprint: sha256:df964226987afec32e45dd7dc4762f9f503a082c97640fca4b849dc1527d0dc6
  recognition_fingerprint: sha256:25954214eec432f39fd52bf0bb331e737a6bba4b5d95e1cdf2fd047fa0e840e2
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: get_robust_list
  source_fingerprint: sha256:e5ed08dc9f2350aebd9d71c4a60d400e4be0ada6d3fe38874db3481436920a00
  recognition_fingerprint: sha256:c98df3c00b1270d4116fa9d0b177f3a790c31c80cba3a81c50989f828b431b50
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_3F7F517D8AA3614C
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:3f7f517d8aa3614cc841cafd2fb2ba7f37987628ef7c08acee77b45451f6119d
  - id: LTP_5CC32725A40238D7
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:5cc32725a40238d7b4ae1ade31e98d1d8718054fbce20edba776af1c99aa917a
  - id: LTP_8CF830DB0473B27D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:8cf830db0473b27df2c0983edcb1a34d50686deaa7302150b4dd1e974d0f40a4
  - id: LTP_A5952E2BE90138F8
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:a5952e2be90138f82bb0886b6a050e550376d0bbc9e7ede442642be848334de3
  - id: LTP_F3CE94166822B3E3
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:f3ce94166822b3e3c4ff880c3e67ba89d1790bb492cf4ca052638688942d9a5d
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: getcontext
  source_fingerprint: sha256:3980e8642183ab81d5f98fcb7ef7caad2be2005466099368a36ce9ff0fe6fdb1
  recognition_fingerprint: sha256:87ff543d9f053b80693596fbfea83e8df16a602f15bd79e1ee5a8360a00f0a2b
  selection_reason: recognition_changed
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
  recognition_fingerprint: sha256:04307ea7232a0094fcdda9424022ebefb0987f50d5c4cdd436ee3041bc9e6d0b
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: getcwd
  source_fingerprint: sha256:8b0b23a4dcfbe0d60012953312e48c64c5bd4c8235f30cc3834d0fcecba11d7b
  recognition_fingerprint: sha256:45b45cf0ee894697a6493b8f63f508f495b40322bff3bb5a3892dd7deabb3f3d
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_12FEE545B9A2556F
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:12fee545b9a2556f28dbcd45aa67754cd8cff713a8b383fe4533b04c6a9ada01
  - id: LTP_53E3454ED6EFD842
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:53e3454ed6efd842d4456341bdaf29e25ad49ab8f5a55c170a4e23c3355fe2f9
  - id: LTP_729222947741DFD6
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:729222947741dfd63a81e9c93572baf5c789acbffca84a2edd5dce13fe1fb2a3
  - id: LTP_9FAB1B9A02F7CAF0
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:9fab1b9a02f7caf0f9f96bd9a0b1efb08afa7559b459359619d27241e8c5beaf
  - id: LTP_FC1E41C3414E7F21
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:fc1e41c3414e7f214284f077070cc39320ebd294786eda043234fca8d9f5da6d
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: getdents64
  source_fingerprint: sha256:ff03f95706bf002313b1ebb895516a0d8c2501080598134a49252b9fc609fcf2
  recognition_fingerprint: sha256:e46d73ef72a9eae8c4f62326cd5240ba06a4f3de5e212f3bf97096ca3794c213
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_367A286E9FC81496
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:367a286e9fc814967aaf681650524e204e88ec789ad4e854ca9a76b059850ece
  - id: LTP_3F00E13306997358
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:3f00e13306997358b4db3c0bcffb3561b854eee1572dba6e68e8606fa640b0a4
  - id: LTP_96C057F70BA4F5B9
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:96c057f70ba4f5b96c2e0b592d9ecdd4d0ccd060569e00b656a27a01c38bbdb4
  - id: LTP_C894288BC38DB82C
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:c894288bc38db82c527418a287e317b342ee6b7f6c406455d32b7acd371f9422
  - id: LTP_DEB4A4BEB59AD7A4
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:deb4a4beb59ad7a440f8adebcd0f0ebbc19c2fec0558f883f557452a8f723f5a
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: getdomainname
  source_fingerprint: sha256:05c5f426c00c6c8034528a355d7aa55f9bec06ac573dc3fe94a2648d2170ccbc
  recognition_fingerprint: sha256:263b6c1ac26563b0c69498a12fb3bb4eebe9d90224d0bc9b7a2f75cb4d5b8a03
  selection_reason: recognition_changed
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
  recognition_fingerprint: sha256:424497bc6585451de9d3730aab6ae994f70e397811bf7f50373f2d853cf3f729
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: geteuid
  source_fingerprint: sha256:7ef66bde6030bc3f1065d278c3cb7c7b9e774e46e0379fb0c785ccc15ed6e59a
  recognition_fingerprint: sha256:cf33a303553b3755d821ea663b54f300fa8145c5e9e85a146c656151d72fc99a
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: getgid
  source_fingerprint: sha256:6d048bd2e1e133a66dea5cd57a60d5ad8ca8f816c70faa52d11a10d461881e53
  recognition_fingerprint: sha256:98bb951eaceabb0a8e864898947355d33ca16889422f4a5c555df0432b6c9b84
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: getgroups
  source_fingerprint: sha256:78507ba695ed751444f22a5223f0fc16cb5176b3906813bf214449ef2dd2ffc5
  recognition_fingerprint: sha256:7004ecf96c4553ade4f3564a25b74ad10f2658a17d8d53503445ff97dbf91ce2
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: gethostbyname_r
  source_fingerprint: sha256:5bf970d940a0ee47746016f266621f3bac25f47e85ba16d846df5674436544e2
  recognition_fingerprint: sha256:e8a8d1cd0f6cb9a2c6e8d91b9c2407b4f4b90e44cc7734e56416fb1a371acebf
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: gethostid
  source_fingerprint: sha256:4b291a7f5012d6fd1c33ac499595557f0a324867131c2f5207832452d65ee43a
  recognition_fingerprint: sha256:8b1b53b1c38ebea408db39e964a3bb1c354e6125c02313287f8a6fdd1e989ec5
  selection_reason: recognition_changed
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
  recognition_fingerprint: sha256:e2f59423d7c923523821f75376b20e13c1308d01d37409db2323d7d79ce64e02
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_BFFEED9C08C13250
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:bffeed9c08c1325002ad35c0e697eb1bc2f43ac940fa171495aadd9627aeab4e
  - id: LTP_C09E83BE36885312
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:c09e83be3688531210e2e1d786e85d9e52cc39bd66d7f65a47dcf87f4365c2b8
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: getitimer
  source_fingerprint: sha256:072e2f535640ac1c794a6d4465c583cd19571117227c21c259b7ec53aa22db63
  recognition_fingerprint: sha256:b7cfaf9ba0209b1acdc50774e46c47f025649e1463d9084b3627b405a83a7c92
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: getpagesize
  source_fingerprint: sha256:6f843b6704e3d7c4e5d6df065fc774b3aa1e79f80033da459f22a03c11530943
  recognition_fingerprint: sha256:23d8d91c97d8df12c946ec5a884fba9df658dac8d17a35f6e7011a36ac1695f5
  selection_reason: recognition_changed
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
  recognition_fingerprint: sha256:d0f7d467912e856ed658b48b7fd57191dd1b821fd1d08d0297617208f4515215
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: getpgid
  source_fingerprint: sha256:1bd409c1625f03b29f70c22684fe20c9dc4d46749b95a174985b9a0433c6db8f
  recognition_fingerprint: sha256:da63311094ac1614e28c02504608036ac021b8ff4f58a1fedc1f104ba85155ac
  selection_reason: recognition_changed
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
  recognition_fingerprint: sha256:a885ae199b65b088107ba5f752093e9982bade27baad4224164192b54ea9cdc3
  selection_reason: recognition_changed
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
  recognition_fingerprint: sha256:c556f675d5134e268fd008cff2b7cad70f8494810a58cc3b4ca8a3820b89da32
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: getppid
  source_fingerprint: sha256:b6da5286d433a05c1774155b683b0f2f14ca304a10226b1a7a10fa6a9b2e9b96
  recognition_fingerprint: sha256:bca2ccd22be9ab04cb1f1f63526a05665269187dcbef05087282513556600119
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: getpriority
  source_fingerprint: sha256:0ce73c8e6e64ce6e10f2519e66c69d7315f13f11571f9409f19d155e77aec4ad
  recognition_fingerprint: sha256:18d63341cde522315000ac375dbba589b1268f314860cd6e7ef13b2f172c67e7
  selection_reason: recognition_changed
  result: formed_rules
  rules:
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
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: getrandom
  source_fingerprint: sha256:8334c40ddf351ac7d32f4b4122c9ca12e45ffa8486910d5f7435c0c554b75674
  recognition_fingerprint: sha256:3dd4bae61a66810317a7f08e9002f81d0b586fccfc8ce7c64b172d5b2cb09a12
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: getresgid
  source_fingerprint: sha256:1696b24b856d57c2295632df1f7b0d38b473b8fa28f8d29a512f3d8128380dac
  recognition_fingerprint: sha256:862647c1f16138ac54cf0e3546a19b66a708b851b822964b8dc9f2cc3f37bc5b
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: getresuid
  source_fingerprint: sha256:e279dfd24776fa7d4e84e22964e1186bd2bfcf1bf6c9a58fc7af3733fce5f7a7
  recognition_fingerprint: sha256:ce54c1a6b1df9908a25ca707374fea58ffce829fba65f9faf8a8a1fd3a0435bb
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: getrlimit
  source_fingerprint: sha256:048949c417ab0a30173cd0165c6d66b225341010c5933c74350080280a2d6700
  recognition_fingerprint: sha256:89b5e012fe8203bada838644bdf2a35f064738225e1d68594823c2e6cd9accc4
  selection_reason: recognition_changed
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
  - id: LTP_A0547B601C515355
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:a0547b601c51535524cdadea7c3abcbc2fcd16157591cc2322cd1def6a08cc56
  - id: LTP_B058D6B9CBBB459D
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:b058d6b9cbbb459d2d0e155285c19e2e49762cc25177b335dab254142809eb74
  - id: LTP_BD5C209F4C6EE910
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:bd5c209f4c6ee910a13539baa6f55f3f3d2654a60e583b67fa26724405421ad3
  - id: LTP_C92D3BC9579570DA
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:c92d3bc9579570da198d5b37082112b074dcd5c95e8b42b8be5099297a9978b1
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
  recognition_fingerprint: sha256:95e966b5a672cffea488ade4ee906f8b07404d3e935cc1bb1398c9747af80677
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: getsid
  source_fingerprint: sha256:7fa5716fb0d95440b7e8fda0ec5bd51987a909059879f26798cbfbf15b90e3fb
  recognition_fingerprint: sha256:b5375eabeafcca8bde4d0b70f987ded7020cb4b30d436f08f5d16171ddf923c8
  selection_reason: recognition_changed
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
  recognition_fingerprint: sha256:90bc513ce5ebf6ebe1036537b6a7657df98f78e67a9882d3d8f36429b704e96c
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_030901665B56CA4C
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:030901665b56ca4cd25c96eaeaded751caca10fe95582bd8babc9d7231a59254
  - id: LTP_49D5637777352E9B
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:49d5637777352e9bd0feba4999d9f7b2f0e3ac26965a9b61b2981d641dfa2e62
  - id: LTP_52CE7E6F9B5FF947
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:52ce7e6f9b5ff947f2b92b0845844fa92e2daeaeb7f87b60c8f5436b7ad3450f
  - id: LTP_A5BD16DDF641E0B7
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:a5bd16ddf641e0b711e9d3cca4b4e0665f924066c189770c996ce5f7b1f45e71
  - id: LTP_AA9171FB32FD0C67
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:aa9171fb32fd0c671764cc145bd58abcb119b7ef2c9f2e342fdec7ba261573b7
  - id: LTP_DBFBE6A110B3D17B
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:dbfbe6a110b3d17bac558d2ea9f40b57cb18ad41d2b90f2ef587ede93cff633f
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: getsockopt
  source_fingerprint: sha256:37fd155c01e258396f5af11ddd4e69b1ce829bf9fb7f61e5313d1b6fe9fbccf2
  recognition_fingerprint: sha256:87683f1f37f3d01d2e3e51683ba76471eef885dc9ae83c93dae6ce5e39fef7b6
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_21E1D9035D6DF74B
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:21e1d9035d6df74bc60f9ce3c357f04be507be85e167e039566c514b895906cc
  - id: LTP_3DDCD08519809A17
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:3ddcd08519809a17ca7a96a5ee1cdbdc58690968fdea20e1594ac65cd34a4098
  - id: LTP_8BCA62F97A197BC2
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:8bca62f97a197bc2486638365fd31e2c4fa35bab95eb651113068ba12997e583
  - id: LTP_A94C8185C529647D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:a94c8185c529647d2b15db2c1364e630a000fb5846bca25f4a1c090ca6823165
  - id: LTP_B72405976D9F15E6
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:b72405976d9f15e6653a4c19a55c21b6afeb46487ee550707600903ab0c823d3
  - id: LTP_C6B4E04E7671DF4C
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:c6b4e04e7671df4c9a052fd2d8d0dd0fd7e03dfaecced67f3ebffb99f63b8c85
  - id: LTP_D77AD0D4DC9C0C9E
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:d77ad0d4dc9c0c9edb967f3b45dd2a074cbf7266307be86acafe7d0e5554574d
  - id: LTP_E2EEBD0885B0F3EC
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:e2eebd0885b0f3ec05b60e9c90912342c9e0e03568a92b6ebedda47c0d85f68f
  - id: LTP_FE51D85F4A425C61
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:fe51d85f4a425c61761c446e685c34d147bb094cdb0a31f3af1659b800f137cc
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: gettid
  source_fingerprint: sha256:15a03fa7d68718e6b01c51675b28efdbe255ad84a4c6c3b77ceab0c872c39f1b
  recognition_fingerprint: sha256:1fc2f0a6563963808d9023b5e7eb25e607a3bfc550b06fe17694312caec3f44e
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: gettimeofday
  source_fingerprint: sha256:94c3ceca3966c0bc1abc611535c4d7c637029f779a29a3698266d370e3ff9839
  recognition_fingerprint: sha256:b720787675b51e743cbfad2a1fc41af2b696a2ad0b92c84e2544d2783947fe25
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_69919B72D9A02D03
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:69919b72d9a02d031f23c5989a971aa794c86301d2a4941a95a6f8d6598db9eb
  - id: LTP_90D9067DABAD1253
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:90d9067dabad12531e389256b10bfbe72e199a661cc2939603fc10133e1c694c
  - id: LTP_E564AACFFDAA71E1
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:e564aacffdaa71e1a3c605f541f0ea956c5caaf8f0c786dec29c32dca589ea87
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: getuid
  source_fingerprint: sha256:e1e7939b57424bee58fa4c67bdcae73d2e25249ebfdfb00bc2b1c4a555b5cf59
  recognition_fingerprint: sha256:b2a1bdda8b2819f91294afe8b728cf4d78548c41e2237dc97462bc6753eb8a79
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: getxattr
  source_fingerprint: sha256:05a86817eafa7c9b90b665113031500fb30121baef63b2fa4417341c8c2d6785
  recognition_fingerprint: sha256:e0b4ba5c26d22bcc0d9ed2bc906e803ceae3112768eca25abb67111781fd97e6
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 9
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: init_module
  source_fingerprint: sha256:c8b46b2ca233ba87b36bba9d86cfa0d723e66625a982955f8f755abd26ae61a1
  recognition_fingerprint: sha256:b939092de1bac5e394424020d55b2f1d863e1d201df3b1280b94e91e00eb4ce5
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: inotify
  source_fingerprint: sha256:31ac39d94d64342aa4be6d94d46fe00c088e2e92bbd86c1c65a7897f5b7e7a30
  recognition_fingerprint: sha256:04f48340088bb1882be3f1dd4c172f889cdfcac3a186f7e24fff2e57e46f8575
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 12
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: inotify_init
  source_fingerprint: sha256:6d761404dec561676e4755cf6ae5c7196e5e9f7437c892f1a1e20bd28f4592ea
  recognition_fingerprint: sha256:7ad0b0fda9b76803d3191c31d283f8e7c22188ece5024cb038e12b8b3e88e925
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: io_cancel
  source_fingerprint: sha256:d4b076f3ea49fff46bab9e256719c33959d414cc5482026ebea9f3b60fd3aa0d
  recognition_fingerprint: sha256:cc9c04289fbc854c34bccfe06297f5d7803019222549f6a0db52c7245b3e4512
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: io_destroy
  source_fingerprint: sha256:963a95a1dba968525e1a97e2d01df29386162c5853b675d1c6f1815c69bcd766
  recognition_fingerprint: sha256:224ef79afde686c7358a2d448fa0b77dd3a1881308f2524582794829c77e7fbc
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: io_getevents
  source_fingerprint: sha256:f87426c1199a0fae2595e6876da234440d63b918c100358089ebdeeaec9c9b77
  recognition_fingerprint: sha256:7e1cfa6db614fde6a296bd32d8a293ed66b52a334eea1eada9b4b6f92fef5a3f
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: io_pgetevents
  source_fingerprint: sha256:88eff516c9c3136ac1e6e6eda20ac63c84ea370f16e7e78cd960d262fb47a378
  recognition_fingerprint: sha256:a2f51fd63ee9b05d0cd63c6a7373f2b575fbc65cf59418414bce8ad95f79a20b
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: io_setup
  source_fingerprint: sha256:e5bd0be0d717f9a5327fa2b6e6b988d431ac9e94e3c10e0b66abd17f72fb5817
  recognition_fingerprint: sha256:88928825e5510297c94c33eb4b9a1c0dbbebc4b5f41389724c6ec1ab77866f48
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 9
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: io_submit
  source_fingerprint: sha256:b2732f3241cc1a4b4e5e5dd766ed7cd75817c59446aaf1393ba5903fef027bbc
  recognition_fingerprint: sha256:d211bfa26d565943712566a4f3e9c69daafc1a1924a106d8242cf136a07f7001
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 8
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: io_uring
  source_fingerprint: sha256:cf3158cc3dd0cff095c6e64e43bd83a64c943bfe5f1c3aafb275d3c85ee09158
  recognition_fingerprint: sha256:f2f8f7cca6fd9ea5112c3e46160db22c3da71e8b0333bb8900443c3b414dd3ea
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: ioctl
  source_fingerprint: sha256:e52dc9a731e186a43625b562b85f93069760be7fb189b5244dee363f7aaa45d7
  recognition_fingerprint: sha256:a5ed02f25b75cc37055e7e1ee7f452e7c1e9c3cf63bac1093c3d285acf7e3bf7
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 85
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: ioperm
  source_fingerprint: sha256:9f024a711c4af47b14265732ae70b8a6e7f15c35e64b654f217afcb93ddf45ee
  recognition_fingerprint: sha256:5cfc2ba542a19c7e6023d4bf06ebe66ec366259f1ee0c7074eba65074a48f156
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: iopl
  source_fingerprint: sha256:ceb7f1f5b18b3660d142529d7da94de429a3e5119f6d50421268bc95febda9b6
  recognition_fingerprint: sha256:c38e61e6a3fda288cdb47f0ab3ca041f7f06f4515a15056adb94e5657043123c
  selection_reason: recognition_changed
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
  recognition_fingerprint: sha256:6e07b91366974281cb04d588ce443555dd5e403a1feefe88e5977ab89cf372b1
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: ipc
  source_fingerprint: sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  recognition_fingerprint: sha256:6df5128a90410129ab8c50eca90f00d9ba697762703078690de45a5951f7ea2a
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: kcmp
  source_fingerprint: sha256:24eaf02ba19e5b1c5106f5ecdd7e65e7bbcfcbe45ef5315d8580ce3a98d6490d
  recognition_fingerprint: sha256:6f9e7ddf9f70257ba76a499845f00a7cb89c7c1aecd1fdabd75c97991fcd430a
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: keyctl
  source_fingerprint: sha256:eef3b7c13faf919403ba8b2882dda2f2dea0a715425c0e7d285ae5291e061f05
  recognition_fingerprint: sha256:18db3c54b0bdefd98401661e9d94150918f0819ebe36f6e2a50ae4e21bc9290f
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 25
  unresolved_evidence_count: 4
  reason: unresolved_evidence
- syscall: kill
  source_fingerprint: sha256:ebf0d4d1e21aa62f72d00c4f12f74c484a98e8abb8b088d6d46ede7daaa770cd
  recognition_fingerprint: sha256:1e22bca00e414841775d5ee66274f83e16186ecedb7c5de47e667679e065de8c
  selection_reason: recognition_changed
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
  recognition_fingerprint: sha256:1ac55d4a855f760dcb6086a700f976aa181131897b8f2dd9ddc889b650e0c72b
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 13
  unresolved_evidence_count: 3
  reason: unresolved_evidence
- syscall: lgetxattr
  source_fingerprint: sha256:58c6b26abc4b96e5a2c15ad1f39555457d203e722479369279073f24036acce4
  recognition_fingerprint: sha256:c433511bf2ced9190c1c644fe23fbc3993cb24e1f3316d913f68facab7d64baf
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_248EACE09AACC5AD
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:248eace09aacc5adfec33902124f836b9fabe852d462a5f3ee85537d96690b21
  - id: LTP_5A2ECF299444C403
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:5a2ecf299444c4031ccda9f4693114915f854755d64c86f693a0804550ab5b79
  - id: LTP_9BFDDF855EC51FDA
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:9bfddf855ec51fdaac6fbf088cc441e380917b1a31a56468b04f146eefdbf803
  - id: LTP_A8C7B3D7AF1FA55E
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:a8c7b3d7af1fa55e1453aba6520bebc3625c5fb11368c58ba5a66a7ab339dd38
  - id: LTP_AADEDDF7D9C31F91
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:aadeddf7d9c31f91af58fb354659cbfb2aee52dfced52669ce49a5e07adb53f4
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: link
  source_fingerprint: sha256:d4072ead6d303c8e1a0761967ca8f92f72a9c18849660cc65f2318df071aec19
  recognition_fingerprint: sha256:3b5dc2a4a39f6a03ecbf7dea38b85165422bbd4df4517c83dd6ffce2a6e6783f
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 8
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: linkat
  source_fingerprint: sha256:2f9151731fd8458619c5280b0a092d284c80c3e2a322d557a848d7b91366c4f7
  recognition_fingerprint: sha256:6a119af750bc6a4c0402e304ed4f4c34f950d3f4aa3e0c674efb57b1e9265779
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: listen
  source_fingerprint: sha256:f525de39dff490afc4808e6ea544aeceea44f8c23bd77d672e768703eceeaee8
  recognition_fingerprint: sha256:29a1ae8e3e5e031ad1887eba75ded19921e8f88245b5783a2cbc065d5849558d
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: listmount
  source_fingerprint: sha256:8f7d79c4251882a378ab8df275c57eae13cdc473fa10d2bfaf291f46c4ee47f8
  recognition_fingerprint: sha256:30e89c6afa089eab097196d5c1c8629fcefb54ea200b46807b7c5a1f43f12a7f
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 8
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: listxattr
  source_fingerprint: sha256:3b4336e97f32ae03aa2f7b9d0cf4b19a5b908d809d8940da5702641fd9ec216d
  recognition_fingerprint: sha256:769e660392110822911e737723d9faff0efc5e8411ebcdcc98d7e8a5c651a7e3
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_969660F14B0B297A
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:969660f14b0b297a37808acccbf082c77e31549f7f06db4ef42175ea22ca87f4
  evidence_count: 6
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: llistxattr
  source_fingerprint: sha256:90d2ad2877a63af4fd10787b60fd2c4ac0223e7b165d9c42fe3359a7df46d83d
  recognition_fingerprint: sha256:a1756107a522ab76cb2dec361d4aba930dc6dfd8c0c4a22da97cd257f5125db5
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_1B2E614CA8847B31
    generated_at_utc: '2026-07-16T03:35:24.146836Z'
    content_hash: sha256:1b2e614ca8847b312ed786b393a6a5996cfd3d7d05fce916a891c2a2ae5725ea
  evidence_count: 6
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: llseek
  source_fingerprint: sha256:95e5f5ea96a19b3b852fcf992bee7de308ceb69e24f0d8a4d78d177000bcc9b7
  recognition_fingerprint: sha256:346c2f671d151ffb126a499e17fe6e8d19d6046e2b5c5587b97bd2047578af10
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: lremovexattr
  source_fingerprint: sha256:e9545e08899ece9d79f65b7136611cbcc49557b33417647a0ccb3855a7f06c8f
  recognition_fingerprint: sha256:221ac3d6532d8a48f4c2becba92cd4a5b25ddf59272325825ec3eb6d3387577c
  selection_reason: recognition_changed
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
  recognition_fingerprint: sha256:ff03c29e81abb40748659cd2ab22de61b5389450a6c78caa5695f46d4b8fdb91
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: lsm
  source_fingerprint: sha256:40ff9e9f03f7b4f813e1e20f85972c444f5b2d67cf1e7ed94d7c4b65ac46ad39
  recognition_fingerprint: sha256:885c328688733d6f68dbd0017cc85a7400db6a6ba821c0775a8b3485c1d88b14
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 11
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: lstat
  source_fingerprint: sha256:5e4156c704b1c14b42b96c4d36188f6488e5322ad2983b95c6507ed30006f8b4
  recognition_fingerprint: sha256:0b15c53e6f4581440104203fc9d8ef0f87170855f68b11a15d3915c013261d62
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_30A4B4C40696905E
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:30a4b4c40696905e7034edd29358e2f0e7ec9bf91d59d54cd998da2929272e68
  - id: LTP_4323000B7A8D2E5D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:4323000b7a8d2e5dc9f9d920cff992a51a67180fd6b83ea69dcd29a6e742f371
  - id: LTP_658F21F428A67438
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:658f21f428a674383a722abfb9067076a0e8599e2c24462ffb902c17cc3d89a4
  - id: LTP_7CA8BC18271AA973
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:7ca8bc18271aa973e0603298022c62fdc820a1f0c553fc4cf8d90446d64078b9
  - id: LTP_8C2F2999FBFE056D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:8c2f2999fbfe056d30d1d1855c4830b8bde8271ec666e3bc67c890c0d59b79bb
  - id: LTP_9E1134B051A31DAD
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:9e1134b051a31dadb8e67630d1cdbe007fe4ee16f80db10ce77f08682d717d25
  - id: LTP_E9690AB9682FCE47
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:e9690ab9682fce472e97bb505601d9bb24aadf4bd67cb3fb0770e5f139f6db4d
  evidence_count: 15
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: madvise
  source_fingerprint: sha256:07ea376c5fc34d03276c7b6582b2027f4a7d1d6e9d96a1b16e5a751e53ea91aa
  recognition_fingerprint: sha256:9ea5f6a7d92bad0f71016ff3e710032ed0ba4a2511075f91e93a8c66a6662d00
  selection_reason: recognition_changed
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
  recognition_fingerprint: sha256:3621cf213659f82e48d2d6a092d763d22d196a3363dd31919bc958202ca43f38
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: mallinfo2
  source_fingerprint: sha256:ad6e2083c341d53bd4c31712c908d9a18b2ab4fb3ac4a8236a0a2430cb103a92
  recognition_fingerprint: sha256:d9e065852c05f2663df7582b31a00c93ab87046fb4b9997ad787314374768ce9
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: mallopt
  source_fingerprint: sha256:8d65203cfe8f7d1876808999169eac47f74ccbde67aca0bbc74b7c0e31cc7571
  recognition_fingerprint: sha256:b2c6359c4d395ca2edd666db186d1a62e69e5bef83626a0ac5758d1822599e0c
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: mbind
  source_fingerprint: sha256:d67d8418bc3260eac92b5275ec21f7269a812f21001f67f8e5d0c6ce6545108e
  recognition_fingerprint: sha256:eaf2d9cb50b25c1398112086d63523da054b10e4088ad312706b04b6486cbfa6
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 3
  reason: unresolved_evidence
- syscall: membarrier
  source_fingerprint: sha256:02e217865c928213627e7aa343fda03d3b6bab36997545bf123072e0855bcccd
  recognition_fingerprint: sha256:b2422de58406e50a9d1b77dcdb5eceb3bae91ebde7ea63c9bad89dedc7bec510
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: memcmp
  source_fingerprint: sha256:b3a74d3125b6c83a8d1859215e7a126c783e67e4cc0f562e2102307574f50cac
  recognition_fingerprint: sha256:c9cfc420fe9ed005f143f64a7b92e800af572e769d84a68d45080716917f45c1
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: memcpy
  source_fingerprint: sha256:470795acc045bdb94d306cf37913f9295ff579d08cb7f9afe37b200014085d13
  recognition_fingerprint: sha256:1574a88bc40ec44dd45866ea0011f6c453a3fd635367cacf15d339fd0e43ebe8
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: memfd_create
  source_fingerprint: sha256:c73822e02f78fdbda2e5f75daf7fd7b3894c80c07401ef7970bb5bc34f0d5f1a
  recognition_fingerprint: sha256:549a265bbf8e4bf4bbeca53cff8b4a789a1bf130271e0d46cdb1f7b15d86ded2
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: memset
  source_fingerprint: sha256:ab18dfae9d58d8c3acf47260042f361f3b8e97cd60f6151d83c85c8e4951538f
  recognition_fingerprint: sha256:79b21e1b2baaba1ee8e850254155d1a5bbfb6381f7d1538a0199385e102fb2f4
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: migrate_pages
  source_fingerprint: sha256:1cdc50532b9752eef79c66730260e8de7b1e222f6fc399ec43725549c6a1cd6f
  recognition_fingerprint: sha256:6e6c71e41d04738f284de2404a8e1ce9658c6a892bf0215a34cc86ae985ac236
  selection_reason: recognition_changed
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
  recognition_fingerprint: sha256:10c20dfe267d9ccd6d886f3e588f23d80b7a1419a143920328e58698f7bf2a5f
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_3A18518E9A9DDC47
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:3a18518e9a9ddc476c43becc3aeae2f5eb8dbb66225c2131409280ef0d5ab244
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: mkdir
  source_fingerprint: sha256:2f9cf52bad4c4554a81d3e9a091c4e05fe10109fde0687fa748724b00f166c0d
  recognition_fingerprint: sha256:17659fe27c6ed1d89c1a149824455c12f9f308e8557452a279ede24c2f93db77
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 7
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: mkdirat
  source_fingerprint: sha256:b7d9665f2967f632796a35b5298cc7235fe9e161bb178adf61c44142d685ffd9
  recognition_fingerprint: sha256:c56c529b3c9fe8525ea1c1b62ccbf8bb13592b41a14fe46089eb849ef3f6a1ad
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_11C0673F2CC64D66
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:11c0673f2cc64d6693db898e3b01536c0bad36b20ce2e8c1f18dfcec70a24922
  - id: LTP_6174E3690A05F1CA
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:6174e3690a05f1ca197873252a1e0d7555885e03bd2876ff2761725dd8cda77d
  - id: LTP_C58F92F1259E1474
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:c58f92f1259e147433057201737d1f7b2137b324c60cd40856d924914fc3b3cd
  - id: LTP_CD3A79551F6773E4
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:cd3a79551f6773e41607f9694cfdbfd8a37fb09e6ba93354387053f7aa85c377
  - id: LTP_D339D6D98B843BEA
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:d339d6d98b843bea5e8f72fd45e9f0d779a8d63db958e0e4b0963f71d3ff33f7
  - id: LTP_F6DD03A9DC1C07D4
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:f6dd03a9dc1c07d405b7e2e43241d2a5292df8f1ad9ad5103ab5b3e4d26208a0
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: mknod
  source_fingerprint: sha256:b266caedea786cbd37943930762732f7df22fcf0b39561f9f4d0f8b9509a776d
  recognition_fingerprint: sha256:08e5edaeba9be060144d0cb1f13aab296328dd5d0d165cd7dce9273ca01d4587
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 14
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: mknodat
  source_fingerprint: sha256:c98d401281482e5d3cbb9f64105caf739b243b4d0b978195f4dc9ff441a25ac1
  recognition_fingerprint: sha256:292a5de3efa882e60683df80068b459f0303a1a6a27d08479ececd5167eff41d
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: mlock
  source_fingerprint: sha256:636e1d77a2de77f6d58d05018ec69ef1c660917a6fece9eed86b7438638c61fd
  recognition_fingerprint: sha256:7a9fc838462111641afcb444e4a76bd58f33a181fb5637088cdb761a2b9200f0
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_1C1877AB6CAE8906
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:1c1877ab6cae89065ed8da38b9d563f18547ad4af122f8567052e27558bca3ec
  - id: LTP_C05360D699C55915
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:c05360d699c559150df3c3a42d5d34bc55ba91cd49242655320645bb43ee716d
  - id: LTP_E00D911A632EB8C8
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:e00d911a632eb8c8083bad847eb0ef9617c2994479a3919fb85cf54980a9e7aa
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
  recognition_fingerprint: sha256:36445c74fa43efe66fc519aecdca02af47c0832bdef921916862f74d3aebd074
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_074981FFB7FA5DB7
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:074981ffb7fa5db73615c77a87030dcaaa1986aec18d298378c656a14d6d163a
  - id: LTP_2D13A66AD1AB0813
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:2d13a66ad1ab0813c8c2e6993a9b698f5bf9c8481df5a3a1192609999c367b6d
  - id: LTP_3471B46784E57E93
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:3471b46784e57e93add1f02a00f74afe066095dff50dbb9cf2f7e38ec6e2c75a
  - id: LTP_592639F40E0FF63A
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:592639f40e0ff63a180438e5ee8f78ac33e5716106066f5987588d135bb7cb2b
  - id: LTP_7C995D43920E57D0
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:7c995d43920e57d08bd5e018ea4cb4075068ff370e247a5ddbc5f0225042e2b0
  - id: LTP_8731C07ADFDC57F6
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:8731c07adfdc57f6420d8259f1df5c54376d18a06a0dba1a682c63ed989524da
  - id: LTP_998F62DFD40943B2
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:998f62dfd40943b2ef044e6fa8d63f4c1a914a72458c49f188e41e6e93ff1a50
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
  recognition_fingerprint: sha256:d5fb496887f58ec44c794408d5ac28f79e0991453dfb25c11e5cc6e3c8303097
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: mmap
  source_fingerprint: sha256:42415bb3e243bb4071298a44afbfd9c74353212d3d793de7687920a485a52a71
  recognition_fingerprint: sha256:7e3c2cc1b2661e414408236efa2da5545f9156fb66c905d3c14bb28a5abb9c38
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_1F61FDFDC752BFE1
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:1f61fdfdc752bfe17dc1c66e0f651ee83412c8d743b3cff6d1153656f4c55c48
  - id: LTP_207043BA148C0097
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:207043ba148c0097b5620774e1f050b05d98cf4ca3867f8604af54faba9ebb32
  - id: LTP_23FC431E5AACA295
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:23fc431e5aaca295a48ed4d5f1d603e5b95e13e522ae253cf56701d1796b55a2
  - id: LTP_51E295101A9F4411
    generated_at_utc: '2026-07-14T13:38:13.033184Z'
    content_hash: sha256:51e295101a9f4411b8c43521d430e85bd27ac1d7a96127b66675d7dc024ba9d2
  - id: LTP_74D863031FEC1500
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:74d863031fec1500453b8bf8e42ce638de40979f82e5f2da3faa68d1e8a8c202
  - id: LTP_791DEA825D66980B
    generated_at_utc: '2026-07-14T13:38:13.033184Z'
    content_hash: sha256:791dea825d66980bfded73936e4745cf7b914f20652b9489e65a7a59509b897b
  - id: LTP_9495272A3179B794
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:9495272a3179b79491e78f501d50efd21904eda269fe90670f105d8109cc4287
  - id: LTP_B5F7BCB7225002FC
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:b5f7bcb7225002fc8c5d95ab7e06338f0597f5f9c9a352288e8945010392597f
  - id: LTP_FEACDC300C3E1DD7
    generated_at_utc: '2026-07-14T13:38:13.033184Z'
    content_hash: sha256:feacdc300c3e1dd754c7925df645b95995a6f17fd0ebcb6a50578071e2f9636f
  evidence_count: 22
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: modify_ldt
  source_fingerprint: sha256:fba411cb8712c152c969813d5a88eee8b9287635f22602c072cf8bd03d662ea7
  recognition_fingerprint: sha256:9266e9487cc44fcb3461e997b0134970c2fe910fbd2ee5728f18fdf0dd2641e5
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: mount
  source_fingerprint: sha256:d1c68b66f2ac2308eb5754e50f21dada8986642631d4d3cf498fa4de4fd91458
  recognition_fingerprint: sha256:0291a4e09c9e2e689ed45346866c16a2cc9706850f6450318bd5e6655957a682
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 15
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: mount_setattr
  source_fingerprint: sha256:421e505b156fc5413c9b63ad6ba86dc546d6c74e707756c7ae1cc59bf0bc98a0
  recognition_fingerprint: sha256:30e2a5b5be6378cbedfeebbac3571523158e4e2a9ad3d3866209eca11c28253c
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_5514C74D5CAA93A2
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:5514c74d5caa93a290dd5ca9634c33e6d8f61a930d3961177234b00588cd31d9
  - id: LTP_5F50BCA4675B4B03
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:5f50bca4675b4b03967d3a238eaf7ad5f0142849042f56a4a65253061864f06a
  evidence_count: 9
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: move_mount
  source_fingerprint: sha256:7a04584f3f3cc2771fb1c193f366623b309695178bb64e69fdd0d40696766f2c
  recognition_fingerprint: sha256:98ec6b5cec0f5d09288bc7dd65b14ff0f51b581cc18089b662ab69ce58dcc309
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_08E6F527B4F8150F
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:08e6f527b4f8150f2636c95432f2231716123245a809fb0ca3ec7e87e168e1aa
  - id: LTP_35AF6D3F6FC0EA61
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:35af6d3f6fc0ea61630ccd5cc1be80d490dced0daa0b2a619541838ae6db0f35
  - id: LTP_408787CB8F89AAF4
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:408787cb8f89aaf41e54f38d1c125af832cef3f22ca2583de291ff9aa4fb8254
  - id: LTP_7E14411F2FC9D9CF
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:7e14411f2fc9d9cfd435f6318f90790240113aa270eeb22b17a32c0feaf8095f
  - id: LTP_D74B8D7A215A601E
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:d74b8d7a215a601eabedc58d6a8f0ddbf97b8b53eb37dd47e98c632b00a835c2
  - id: LTP_F122D4A7C853AEBF
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:f122d4a7c853aebf1c679e043ec89b23b5eea5022974daf7c0e0296ed71b8a2c
  - id: LTP_F284E6C48F6B4BF8
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:f284e6c48f6b4bf87c3e8ddb82d9ed93bfd66246c9595dba1befcd8427ff123b
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: move_pages
  source_fingerprint: sha256:eea8d8a50ef8ffc6d9e223810ffbea2aa02e9eb466ba48126d555328d56a55fa
  recognition_fingerprint: sha256:6d6340e53689e175569bdf905715fe1f7660ade2d620bf3a29bd9a85f40f70ab
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: mprotect
  source_fingerprint: sha256:1c51e5e0b90c9d4931c8bc247d3b02bddca038dff01453e300d479c0a1fca592
  recognition_fingerprint: sha256:0666ee52a7f7d21468771b0f9dfc72d1fb1e60516ddd7670efca2944dda167ec
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_11852F99424BD7E5
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:11852f99424bd7e5878fe8d1dacc6815b17493a9cce40cf96abc38449fc82f6f
  - id: LTP_5DD94B8446C50071
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:5dd94b8446c500711c0b0c62a9c4dd47443ab781cfcf13c87da9b84a49bf9120
  - id: LTP_5E2B9548D2D9F147
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:5e2b9548d2d9f147619752d1552f1f7a15ada28d2b0374da04d95b22245d2f49
  - id: LTP_60B98F9136CDCB0B
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:60b98f9136cdcb0b16f892c76633e5b83c3d1835e1a162a8d24c488d4300716b
  - id: LTP_86E98E40777EA3FA
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:86e98e40777ea3fa060f00fc79eb6ef84d99e320bb7dfa43999defb2f4a170dc
  - id: LTP_F2F310F9646CBB33
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:f2f310f9646cbb33375caf2d5ce5539d045055f0346cf9c3078cebc924c5ed73
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
  recognition_fingerprint: sha256:93e94aa50c27e4f4126ec88cc8f9ff501430dc51c58f335b667ffa9b4d674c62
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_11385EF43CBDA2E0
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:11385ef43cbda2e0161b08a04b54efb79405a48d4193203f61aca636e4d77409
  - id: LTP_148C73A2C00EBA17
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:148c73a2c00eba17af0a7cc01a2f4719f68209bd79632e7dbff9599a50460ae6
  - id: LTP_462CE9A88054B448
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:462ce9a88054b4487bcd2143cecf9c86d81a7ea19657672dee1caba8b4f056fd
  - id: LTP_46DC592FFC5E5C44
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:46dc592ffc5e5c443fbb94593eeeddfa22359ea08d7152ab74b4af169993e924
  - id: LTP_828E39231372A771
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:828e39231372a771194fa90c58bcced054d7ab09b07cdcf3cbc1e814af2fb6ae
  - id: LTP_947B3CCE7DA0998E
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:947b3cce7da0998e1e8339fda8d2ffede4b295228350f29e0dd90d9a63fb0f04
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
  recognition_fingerprint: sha256:24767e053e4bac77687d81ee26fdb93de4c85d64f898d125fb9091c269303df1
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: mq_timedreceive
  source_fingerprint: sha256:330881550cea8b3e2443e0dd689e7a112de1d5b9c7c63d6e7e4760a883065765
  recognition_fingerprint: sha256:1080b485e4583467c82b592cff0cb5baeda5990ec6b02d3e5ca691ca94d3d6d5
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: mq_timedsend
  source_fingerprint: sha256:f4b89cbd15aed4d1594fd4d5ba8717264bc1b575e5a6ead3d40b336034485823
  recognition_fingerprint: sha256:263064e50023e5cb47e244ecf5591d0c6a035fff964cfc0a20db1cccfd5496fa
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: mq_unlink
  source_fingerprint: sha256:a842164144065479594d59f9a623ec9b04a4d499a952d689fc427d6f9898245e
  recognition_fingerprint: sha256:55fd2925733ecad29012b87d8dbe8626cdf8b517ec85e950e66fd2ce435da951
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: mremap
  source_fingerprint: sha256:771afc13897e6041a9d7b1568c119bfa42c62c5d7cbe876a0292b3aa8f9cd650
  recognition_fingerprint: sha256:d24c2b404c9773f99b267b88630c545510366ca733378f367d8bdb432c1ddf6e
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: mseal
  source_fingerprint: sha256:403ef52e88331332a7ebff18c00c437efd88615cb03fe6b127bde38c96025e75
  recognition_fingerprint: sha256:4e76fb776c716116c14d9ec1ae39b18839052bdba318368f8400024b6ab45f05
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: msync
  source_fingerprint: sha256:5796104e5843466a7d2850f7d73449428a6a572f47cca62e8c6ac13efeef2aaa
  recognition_fingerprint: sha256:144d17ef774dece182af7cdd03aceafb01682df8121360068c351f6a08eaf9ba
  selection_reason: recognition_changed
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
  recognition_fingerprint: sha256:85e8372b870b794ab5a51d36fc6d2241c27a4873cf1283c44b09668e4f06631b
  selection_reason: recognition_changed
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
  recognition_fingerprint: sha256:9e0fc7eee864d0c4a2e293d9de9492bee14e51774a77a1ebb8ea5f11d3984107
  selection_reason: recognition_changed
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
  recognition_fingerprint: sha256:9c421af8339200f9c3ffa073b04a480ac09d517784038b97de19dae3c951b47a
  selection_reason: recognition_changed
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
  recognition_fingerprint: sha256:4c0bc68a365f90acc5695f1eecf61b655740ad70d454dee8adc38418013edcaa
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: nanosleep
  source_fingerprint: sha256:b048b2b0afc40eba39ec83b0427aee9f251ab945e4c0f24d6c7d256603141207
  recognition_fingerprint: sha256:0c2bc484e7bd174660af391e1318b776e77b2004aeffcd1677113502df665637
  selection_reason: recognition_changed
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
  recognition_fingerprint: sha256:17168ef0ca14f11550f19011008ed8a10c4772322332fc7d637f6426d87fa207
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: nftw
  source_fingerprint: sha256:e615be217ccf2d6a0607c1a4a7e295a2a008e99cf5bf74f0884870e42ae194e8
  recognition_fingerprint: sha256:a97b69da3ee904cf29b910b4cf54383f7a2113141def71df793ecaf4c55bf28c
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: nice
  source_fingerprint: sha256:b16a8f0c654be0f466bc417b6c132aad6762ea14180908ee67da9e4612693608
  recognition_fingerprint: sha256:83529789a446a9935e386e6f4b760f13d36629c214ecb5be116d4649a9033be7
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 12
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: open
  source_fingerprint: sha256:82bbf67772e63a784b0f244f9afdd200e69f28a60fb553022e108ca28fdd79ee
  recognition_fingerprint: sha256:77c47d1e13e0fdf2eb69ef767558fb446557b3b0779682992be8eab42fc374ea
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 31
  unresolved_evidence_count: 3
  reason: unresolved_evidence
- syscall: open_by_handle_at
  source_fingerprint: sha256:bec3e4cae40f441098e84e17f20a92f52d56ac77d28e4a8602310c2eebcca7a3
  recognition_fingerprint: sha256:45f035d1a094f6398a988b00a1353cbb69b9d0aee403e5e561b5463a19936015
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_1B65027CA2FD0026
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:1b65027ca2fd0026fbb6c531676777203594144a36fdedda60265fa0293a1d41
  - id: LTP_252F2FFC943C6CCB
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:252f2ffc943c6ccb2b804f33286006680ef2c1fb49480b90591eeb78e88d4c23
  - id: LTP_3FF54C2EFF286EF7
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:3ff54c2eff286ef70b7ce32a8039aacfc37d8e65cfc9072335b6abc7ff4153dc
  - id: LTP_4E3E972D7735BC63
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:4e3e972d7735bc63898a8664e0624b7b2d7e74c2f64c7bc091474aad8e1dc28f
  - id: LTP_53F53970B961AB32
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:53f53970b961ab328e2ac911f076fd3e137183adbf2f5c0f2df155d740e36539
  - id: LTP_A48010DFDC346FDE
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:a48010dfdc346fdef35e3099c5a8bba7fd4ecb37df306cb1895380dfd4a47ed8
  - id: LTP_E9D60674E416A5DC
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:e9d60674e416a5dca5bb397ae6c8827e9ea438205805c22e3c76af196fc666a3
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: open_tree
  source_fingerprint: sha256:95268b380ce94f8ad2af19ce1d43e526e6ddb5744e2cec6c2886bbe3d6a4427c
  recognition_fingerprint: sha256:a61d5b81f7f5f9e244fc9ce038ce9b3136d19389c256bbbc18726d382e0ac8ff
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: openat
  source_fingerprint: sha256:40d4a302661a60ae38c626ef0c826a6bceaa3dc4f38058428e6b214f8705bd91
  recognition_fingerprint: sha256:d267737a24d6107abb78b5c92d4c60f1fda00d7152f4b51a8a5b35ff2128ee7b
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 15
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: openat2
  source_fingerprint: sha256:0519f9c6c4d0b31124a3bcbc3ca76f450e55bfb8a3a14512bb8578132407dbbe
  recognition_fingerprint: sha256:2de542f261aac6dbcd3e97c5cda540bda17d387d1fa44689354fb417f9ef2b97
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_026CB4A1CA7CDC6B
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:026cb4a1ca7cdc6bf1b2e94352fa72c86bda5fc328c6ed9ae8983b4696a2c0f8
  - id: LTP_056DB4870D82DDC3
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:056db4870d82ddc3ba03295208d4f5908240d4fe7a8b5e1801d47796d080a98a
  - id: LTP_4101795C27681AB4
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:4101795c27681ab4155c6f4693d0d225a8b1bd8861237f9a67aff2e0d2b4c2c6
  - id: LTP_57933F1DF2F98C34
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:57933f1df2f98c341829220b06d7e93f29c68a4bf63978219188544a7d1aade9
  - id: LTP_5FB40D053220B092
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:5fb40d053220b092c105968b807ed753f5e6619fc55fb6f8bb4921f13b78a02e
  - id: LTP_7BB1BB36E9CF4892
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:7bb1bb36e9cf4892f58aec7e67c027d16bebad17744b2f8294fb86d265ab715d
  - id: LTP_7FEB3B276A8133AC
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:7feb3b276a8133ace4d382f6e864cfa9a9403d150aa7926a5fbf647348415230
  - id: LTP_8405B02758433FBC
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:8405b02758433fbcb45171791cb5f4acf2a626b57d9438231dc2a6cc47d0012b
  - id: LTP_B7B7B035608D3637
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:b7b7b035608d36373841aa58d1f26430431b72fe51cd88ba5753894f6444ceca
  - id: LTP_CF4E59775301DA7C
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:cf4e59775301da7c87714ae406a2d7ded16761e701fe533a3c49a728d8c15b85
  - id: LTP_D0800876342DE939
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d0800876342de9392e43300d2797ff5244107ca4127ddb02ed0ec08832b03e82
  - id: LTP_DD227DB33548452D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:dd227db33548452d2f4f576882e3d683d7bb63fa4f821312206d0d7a7b539b3d
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: pathconf
  source_fingerprint: sha256:885fd5f6259fd67809d5f8ba20d51898202c381fa1ba1d4cdc6b2d6e993b7eb2
  recognition_fingerprint: sha256:0baa1f2b489aa4a3f0ec532c7dde905b4894b6bc3379a74ab17aef9d0d9f7b7c
  selection_reason: recognition_changed
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
  - id: LTP_1FF6EB837BDD04F1
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:1ff6eb837bdd04f1194f8f9036c772b7641e718d34b347ce97fd602eeaec5f19
  - id: LTP_2AEF04E122ED7DC9
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:2aef04e122ed7dc906f6edf09aaac0ef4592eef7ac760bf28e0c4dcbf8011b7b
  - id: LTP_4405BEE7215E1BBC
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:4405bee7215e1bbcee738210f0aa7231657bd00d08f3c6fd5541877da97dbbe4
  - id: LTP_50BD66A0A05AFE51
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:50bd66a0a05afe51acc9ddfe13d736361bd2685079416130d7ab91a9ecd81dfe
  - id: LTP_532E8E5A98C0A22D
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:532e8e5a98c0a22d5bc83886e639e747cea3a81f6575a89056445adc02d518a8
  - id: LTP_621EC309C3A75722
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:621ec309c3a7572276fde68dfe01103533fca0ad4c65e320637ba54a3272c721
  - id: LTP_67D824D6D01AC3C8
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:67d824d6d01ac3c8587084088abc6ba6d2afbdbc07e3c226b8ee1631772a7979
  - id: LTP_75354A42F83E3CAC
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:75354a42f83e3cace074274950ab8d2be010cb683186babd97e19349ba50bd28
  - id: LTP_779183F85F2C1278
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:779183f85f2c1278ce96f4480ccfe64e0036c174f940478067ef96b7d580e315
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
  - id: LTP_C544BF068942E8F7
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:c544bf068942e8f79f5757f0e65b2de9b321de82352301e52a86c4588d2a83e8
  - id: LTP_C87041F4B4B5A930
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:c87041f4b4b5a930334107c73250cc29436c01b1d802fe03d206ba9ab5b809ef
  - id: LTP_DD64353E8E427275
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:dd64353e8e4272759f9e403a03aa85d287f7e7771ddb3a7c0db148e18273a7f4
  - id: LTP_FEDE14E9D4DE9A9D
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:fede14e9d4de9a9d30a830614024353c37ca96dff584cd4539f8466b8314e9d1
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: pause
  source_fingerprint: sha256:13071d1a993e570205eab1a8d3ce47b1983a51d890a552304cb85d5344f7fbf9
  recognition_fingerprint: sha256:f8c24c32afcb8d8b2c21ff31f7d4e63407f872da2f476c375ea31fb88d4acbed
  selection_reason: recognition_changed
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
  recognition_fingerprint: sha256:364ee14dd271c506aae295d8e765e321887213e744ec212303a2bbb4cb179c05
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: personality
  source_fingerprint: sha256:6a54c84b9245b9bda914f84a55ef976ee92bb621e09fef2f1f47236eacc8c6ae
  recognition_fingerprint: sha256:8d95c758f684717aa4ebfbdfa9a8699146f1c78ca15bd8d56b8dbefb9f13b3f5
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: pidfd_getfd
  source_fingerprint: sha256:a5571bf56f504c7d43bf9f068325855bbdd536d7efd4301f5b06bfe01d3979b9
  recognition_fingerprint: sha256:d1a904deb0e418ac91ca0d990e48397446ee384a5d0b1d262c81f5358a92874b
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_E6A7D5E5327D8ECC
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:e6a7d5e5327d8ecc3c071c1231bd4ab48a868a18cc19ced52ee1526bbb69b1ac
  evidence_count: 6
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: pidfd_open
  source_fingerprint: sha256:d1f5e6eb062c1b49774940d20b7097704dbfbe26b36a3a1f87a6e75bdc530905
  recognition_fingerprint: sha256:4af58eb9eaef8e6215af96ce5c80069de416eeb5aaa445d6f645c774aa708142
  selection_reason: recognition_changed
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
  recognition_fingerprint: sha256:55f0b638bac322336e3f8434e961b49c3a26174d06247f7dba6a4d6d87be5277
  selection_reason: recognition_changed
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
  recognition_fingerprint: sha256:79783e85753440480d056acf585c77fbef428976bee510df3966f7990f6e90d1
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 13
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: pipe2
  source_fingerprint: sha256:09d31552b7c395e3956cd9eed766734399ac4ab7d492cecef97577ce3b108cf6
  recognition_fingerprint: sha256:b37be4f429a327651a69f617f2daf3163106aa7ed95970c9467b6a6dce8bfd10
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 3
  reason: unresolved_evidence
- syscall: pivot_root
  source_fingerprint: sha256:c466c2481277ebdb072a4628483a3b56de9284dc4929226089fb9e2ce73900e9
  recognition_fingerprint: sha256:478419ffadf0834c0cd948928186adc58d194232dff8065e6ed35dde7b315a25
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: pkeys
  source_fingerprint: sha256:3a0ac31efa18088fcadcf179c5466bc6471abdb4b6e715ffa01d8683ac1bb07f
  recognition_fingerprint: sha256:605970f4cad58b587f93a18ffed265b8c80bf6c2a21ad82936d5fcefd557ea87
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: poll
  source_fingerprint: sha256:5fd7cef5e37f0079cb2f3c5d0ceef5ec217a55cdbdca73d195f97f91751b663d
  recognition_fingerprint: sha256:ddba5f9b6e2ab4fec1b554e474c1cd30398c11209d454ff599f01541c02e570d
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_018C7E7A08833780
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:018c7e7a08833780ea56eb2e109dabf8b177b424cae61d72d84873b6812286d9
  - id: LTP_37CFADAF53B6AC9D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:37cfadaf53b6ac9d9f4eb844a7bbdb7d37e5104c8bada9a12f98df4d1f199795
  - id: LTP_403B654FD084895C
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:403b654fd084895c5395687cdccb4cf2c4e64520fe34862afc30db821c9b8850
  - id: LTP_619E7A5A0D656A90
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:619e7a5a0d656a90fd645364a1b0fc1a033aaef6930c55eb1229201333ed5807
  - id: LTP_7EB2F82BA2DF09A2
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:7eb2f82ba2df09a2bb6896f88712b3f09257b25e8ae635f73db8c21d3a33a72d
  evidence_count: 17
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: ppoll
  source_fingerprint: sha256:2a7c5917b092ea88f1b1152f4643717565dfc715cd0ee3e8487cab7279210c15
  recognition_fingerprint: sha256:b49ce72e7a8b7cf3bf1318ce407a4e175dc360e4e53f130db303f946526356c8
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: prctl
  source_fingerprint: sha256:08df0a52deb8977d45915480d221115255feb5ad769548d29a4cb12d7d89a640
  recognition_fingerprint: sha256:835577f038e09d07158e7c9e64becc74bcf8ea11b8a102f0b25a3b528c9deb58
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 35
  unresolved_evidence_count: 4
  reason: unresolved_evidence
- syscall: pread64
  source_fingerprint: sha256:a0628d75ab6e572e447551877b8d0923b7fab6f96a0bee9b33e60cff03fc9592
  recognition_fingerprint: sha256:9e723d4ea39a20685591a0660dea2076f9984eb5c7cae5e3aead6620183adb37
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_1E3617B704005CFB
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:1e3617b704005cfb56d59376d50659bdd95129c98cd7f3d97306270e2d4af5a5
  - id: LTP_9E17BDBD53A1AC97
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:9e17bdbd53a1ac973d6b4e005d32dad88084fdf555b2ec5f509c6bd8e17506bd
  - id: LTP_D95376E3B0469608
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:d95376e3b04696087b8a55cfe7d6fc6d71225fe62043fc247dd911e05c4dc79f
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: preadv
  source_fingerprint: sha256:c6e7fe1ba727e60645588c3e9513aa14f32df9ef45b188b0fa0be90121bdc924
  recognition_fingerprint: sha256:13532d9f225861c51fc98b3cd5847aa9f58467ed047f9d1df92b27bfd0c12986
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: preadv2
  source_fingerprint: sha256:8f46b49cb74e7b771e36fbbca7310e2c6b90ede077bebd5117cf83730b1fd6b5
  recognition_fingerprint: sha256:30c2b3686f929bbdb0509d1c02b2a93bc1da0e17b33207624812171e610401fe
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_15F112E8B77975DD
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:15f112e8b77975ddc2caaed8f64024d9364337744b56461f08e760c3b903ba3b
  - id: LTP_1AACAC53BAF23BA9
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:1aacac53baf23ba9aec716bf031354593948226151154448887698bf2a5dde0d
  - id: LTP_2A28494F77E0B173
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:2a28494f77e0b173725c00fec9d6dd33a01f558c208eb201a566a85d9e978f26
  - id: LTP_3EB53CD0B1672EE5
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:3eb53cd0b1672ee5bf44b072268216b8bef861d09fd38cad017e17b1e610ec0a
  - id: LTP_40E02D5F6A601BC5
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:40e02d5f6a601bc52a08eee1c7c137b94142e83139ff5f315b906fc0aacd1714
  - id: LTP_4839FA2FBA6C97F5
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:4839fa2fba6c97f58ebdc76008e1580aa1aa646863f8786a588d886a38863a21
  - id: LTP_5EE8091D4EA8F7AF
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:5ee8091d4ea8f7afa48d375e0ecc037bb236661b57bb38b4f00a9969b4b1d2d9
  - id: LTP_679924706FAFC4A5
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:679924706fafc4a58089a9e52433db6f9b7925f149bfcb4e357bac1cb20c3906
  - id: LTP_82907DD83DFD7800
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:82907dd83dfd780037d24929e3f15e6e024e9d57c71ecb132b6120d5db6cad9d
  - id: LTP_93F2091ECF31C3E0
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:93f2091ecf31c3e064c0dbd74696ea7a69ee72a21eafc189c369d4411320d3db
  - id: LTP_AF0FA27496E3610E
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:af0fa27496e3610ec60127057b7278db69fd8af04ffe2699343876b0e7b2429b
  - id: LTP_BDB9250DD17C3225
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:bdb9250dd17c3225ca05fac18ce1cd23618e24aa51d45aaa417898f2724309b6
  - id: LTP_DC3D9E7D5D1A75DE
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:dc3d9e7d5d1a75de583e19ecd659cac07cdf47b781870a8c5d95352ca974da9a
  - id: LTP_E2360C045F1BCE8E
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:e2360c045f1bce8e12d7c7fcee773858239da9852a29232b3fbb9c6135c50c50
  - id: LTP_FB3B521CE41A299A
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:fb3b521ce41a299a77ddf3c90f821324497caea4fed1f7a2feab6e64993a8037
  evidence_count: 6
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: process_madvise
  source_fingerprint: sha256:a98a057bdbdab683ac16c99c9fa99465da36d11a5e71159bd8afa1810e65ecf7
  recognition_fingerprint: sha256:4e6b577f5955fdc66ee9b716e09367e54d428c58bc133292263542de447d16de
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: profil
  source_fingerprint: sha256:1cd18e93512f96ae4edb5bcddecbd319eeffbcad42742346a9796581d73038a4
  recognition_fingerprint: sha256:944fefc564a8aeaadd8701ee96a5220acaca2536edf58a9d57f96883775d5e11
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: pselect
  source_fingerprint: sha256:1eef0fcb1b3d44d3ec3ab02036ba0b0207c4d58a4a1410a19b0acf5ab5d9ad08
  recognition_fingerprint: sha256:5acdacfdc1fbf85c40f726ddce56a86dc263344273089c4fe7c54448d49e85ec
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: ptrace
  source_fingerprint: sha256:7251ab449067fc33f074c1e83041e966498f066aab3312cdc973c0b1ed49b7b7
  recognition_fingerprint: sha256:fc18c374552f18544914143e4c37a91b47ad417dcb5a2da8a16e0773b9725db3
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 14
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: pwrite64
  source_fingerprint: sha256:c3c05677a616f91cde40cd34e95be15af20cc48fbfa5863f8b7a227ce7b000ab
  recognition_fingerprint: sha256:7b4f574a9778bb36bd8460e2cefacd4906b2ecab00e8eaef6da797be7b3c6834
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_0C01151E99096244
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:0c01151e99096244ffb2d2ce3187b4104e413d19ec507b5c02235cf46b5cc4cc
  - id: LTP_4E45B0701D5BD8A7
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:4e45b0701d5bd8a7237ee60c8dd4b9af9c2541ca19e65242d830d549f8a555b3
  - id: LTP_7061ECC5236C3D49
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:7061ecc5236c3d499cfb5d602482e240cd5241149f857b83957417bb8d61eedc
  - id: LTP_AC9BF5A9B41CD255
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:ac9bf5a9b41cd255596d016120338706923fcd7041b9a8cd1a26bf0939d32549
  - id: LTP_CC32503F19BF5D53
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:cc32503f19bf5d531303aaa27e9d973a1c83f75c475bf71e809db18e18e31b90
  - id: LTP_E61711880DE479B0
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:e61711880de479b00de48b032ed349db8c4a2a0b2d7f8ad4044da9c539870892
  evidence_count: 6
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: pwritev
  source_fingerprint: sha256:03b6c10163f0006bc6c0e54d349a631c68a13ff45b3a4765df68695b4b01fa3b
  recognition_fingerprint: sha256:24c1433e8a2fec32003a2034ce1bb522549d334306d11e63b4853911f6887e1b
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: pwritev2
  source_fingerprint: sha256:bb227390e2fa981e3d806b939b058e63bae0f665010870d4eb4d50d2572dfad2
  recognition_fingerprint: sha256:7ae636189ce942775dcbf3a7303c552382defa1eac68eb85f06148be1d5f1cd1
  selection_reason: recognition_changed
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
  - id: LTP_58F749C9A4ACFFD3
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:58f749c9a4acffd3e3448fe1c1f88565100e870c096073776f1c2efe604ae7a9
  - id: LTP_78A991C666EEFF75
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:78a991c666eeff7595c20942bf0891fc0da9b8a24768a34950ad51c2e1be6373
  - id: LTP_7C0B488884F6689C
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:7c0b488884f6689c5adc5b29fdb08f8bb2d2c1e8438761bbc5fe0c3ca7932463
  - id: LTP_B06B0397728F35C3
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:b06b0397728f35c33b5fc8d0b08ce0555e5eef647f623ee21f4b3f9d2fb1892f
  - id: LTP_BADA0A131C4F383E
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:bada0a131c4f383e7b34e29876f9dfaa26c4e38333ea8b230817f3aaed670fc2
  - id: LTP_BDA884D4BEFE09C9
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:bda884d4befe09c95ee33f53a800e8b869a9a19ea187abfdd48e0fef3171b86b
  - id: LTP_C05A62F05F2C22E1
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:c05a62f05f2c22e1f5ace4ba2d55ae5b880ef72d1a15561001a5b6321effbd95
  - id: LTP_DBAE060B9CA303DD
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:dbae060b9ca303dd48f5f810981c7f860cb8d05e67dab04b96d3d30c4dd29aec
  - id: LTP_FCD03068DB9BC256
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:fcd03068db9bc256c5e6f319b729aab08f5943ea4719f56c5bbdc43b10036a47
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: quotactl
  source_fingerprint: sha256:a1c5db38a4263a81478b302e04a6f5ee24a39903c03ef355f3f1f7274c91ce74
  recognition_fingerprint: sha256:82005c02727efbe072998b7b85e92b2cb4201b74c75f4408f245bd080459b2e0
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 17
  unresolved_evidence_count: 5
  reason: unresolved_evidence
- syscall: read
  source_fingerprint: sha256:f109b39aa3a55a23a2e4e2fe4e616e79e35796ac3b66ef570b633fc169972028
  recognition_fingerprint: sha256:2b438346622c8fdb0b4adf38084ba6ad179dcffe3db5938598280d51b84ca7bf
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_0087F445CEB63414
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:0087f445ceb63414b632c05b271af9fee6f2b3c7167fbc43e208a7b0a485ca33
  - id: LTP_29BB55727C5A5616
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:29bb55727c5a5616bc7694e6be6d28d8dc66f2404335114edc2da7a452b231e3
  - id: LTP_2C266C6067333086
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:2c266c606733308616a1344419b7b5e00cbca89aa876e40280e9c63614240a35
  - id: LTP_5D7B8CB342508B94
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:5d7b8cb342508b94fbf75893e54ca0aa74132181b0fb5cabed669e544825b612
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
  evidence_count: 6
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: readahead
  source_fingerprint: sha256:5c6f6af058fd84162757bc23cd7e56763f1ea9ca74a548dcc192bfed9bc5bd99
  recognition_fingerprint: sha256:a01032016b066cb447cf65f3161ca8b90c29f0c5c18071bd59c15145377385f9
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_AA6F0F0A8A469B13
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:aa6f0f0a8a469b136667d815ec6ce470e15005441954ff0c744ff13bdd160eb9
  - id: LTP_D9B6B53AB6CA3BE3
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:d9b6b53ab6ca3be366995aad76b94602f7d9fdf01b996ec51c09ff3664b0f5ec
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: readdir
  source_fingerprint: sha256:261f65cb7e55a5be7919856e4e07d3ce870ef688514f772848f94fe4b7f9436d
  recognition_fingerprint: sha256:5e3acb419256cf6bfe12e5e25ef52a344c72cbe52bb540bd3dea86cab7a63567
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: readlink
  source_fingerprint: sha256:e4b3003dac401cf43daaec283d9b8a201bd9ba30043a1f941c869bde5a2a2d56
  recognition_fingerprint: sha256:b2057c23fb670bb002c73e397dbbdd9d82620410e6bb5aeb4ab600e6d866b89b
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 3
  reason: unresolved_evidence
- syscall: readlinkat
  source_fingerprint: sha256:450bab7abd94001b7470af3949ccb9100ba3e2a7ddbe35e9bd0abc4769c9698d
  recognition_fingerprint: sha256:19690ea24f2be854041611de86e934954314ac53e411b4cc0ba88517e5e10116
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_07CE577381BD5611
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:07ce577381bd56117703dbbcb1b069f3e82ae8366fb59b8449224d9c64c22c84
  - id: LTP_326165BAA61906DB
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:326165baa61906db1dc06bb4b7ec35cc7a435e546dffb9e766d6f52ed8c82c55
  - id: LTP_3B07E4E263BECEDE
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:3b07e4e263becede465632491ce187737a7b34b08acf73dae8921a9f6ee29eaf
  - id: LTP_45D731F7321AFF41
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:45d731f7321aff418f0cf2518857c34618edac66d4beeb7d8d038f7799dabc63
  - id: LTP_4D5D0A94700C0B71
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:4d5d0a94700c0b7166873cd3bc8b0c9ade1048583d27cef9464ad330694da827
  - id: LTP_835C2BD8D8081213
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:835c2bd8d80812139bb8e9980d6dee609760731c95cf6b00b1901d5c02c20642
  - id: LTP_8D2608F53A58B89C
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:8d2608f53a58b89c369eaf78efdd9d4e1ae7080c2b6a6e43184fc6ef348803d0
  - id: LTP_A38793D253A9BE8C
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:a38793d253a9be8c2a59ffdacd6d5d139cab666b071f36b7cff422422c55e56b
  - id: LTP_BF8A721AF501F7AD
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:bf8a721af501f7adafcab123f8f00e6b58809e8e996121c2f9f4bfdb5cc7c5c4
  - id: LTP_D5BD925DC43E7564
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:d5bd925dc43e756486c061bcf85f210b6392fe22074176648a1d35c9e545345e
  - id: LTP_E733F750B1F4008F
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:e733f750b1f4008f9dedf1a40e8fa06d36f42fc4f143d4bab6bc6092187ef842
  - id: LTP_FF3F568195A91237
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:ff3f568195a91237df1792358dc91dd583159fb81a2c840896f8d939d1a9e0f9
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: readv
  source_fingerprint: sha256:d275940f25879cdb27773d14825be221d555ee5ca87ac8819d3e645e957fcca6
  recognition_fingerprint: sha256:9c69b1c4f898e422ba6d1eecb306ffc906b658987277d1ab105ce80ea3bbbb1b
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: realpath
  source_fingerprint: sha256:f6de77becb1f31963b6f3bfc959b02bac49cf498593d64cdb759531a4f66c76b
  recognition_fingerprint: sha256:783ea7c185ba7a62b8fc80d64e63c349988303a95aa95df4c2823593884f3ad0
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_E2AC7688287A2F9C
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:e2ac7688287a2f9c853dec7eae2fbc8f1f0a73a30d57f8566b7f51ce417e31da
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: reboot
  source_fingerprint: sha256:d7977b5f99e8b237ad7b460de208ea575606cbd4c9a96d7a8f731b2efb0eca7c
  recognition_fingerprint: sha256:eef161e013f96d79b9bcd3b6005727547b59706570d94d02ef827cdeb10cde6a
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 3
  reason: unresolved_evidence
- syscall: recv
  source_fingerprint: sha256:6ae8020e60033dfcf6219b1e6418415971ac8bd262b41867151267800b65e5ec
  recognition_fingerprint: sha256:3e95916640deacb6d68c5fd0c087818284a2ae0af33e076c36a8d37697addf92
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: recvfrom
  source_fingerprint: sha256:12694b3133d94558a996303d7069939dc4416344b0ecd7223d5d169708fc1b89
  recognition_fingerprint: sha256:e46650e4de43ce2739d7517f014ae2b41db9986139e53291f5def7a9599bc848
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: recvmmsg
  source_fingerprint: sha256:80b00b21115f012f5714b1abaeda60217bfc64056073bc527e19cb0129af30e9
  recognition_fingerprint: sha256:cfb2d0de002540c982403090f92b6973699ad1a1cc40365bea4a454d3a53fe4f
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: recvmsg
  source_fingerprint: sha256:9218da2a3064baf0724cc254f07bbe68d58221345e03edb70c81e5e982cfd0ca
  recognition_fingerprint: sha256:b20ca27acf46bae52516985ac1d637d24b9749333b27575a80fc8f275111e030
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: remap_file_pages
  source_fingerprint: sha256:00cea002bf0c848dc8749c8dcc327586199d285e8c86f8f10266a4a2de69b97e
  recognition_fingerprint: sha256:615d9654ba9d7f42307bac62956ce6fee6ad53deea768ba362bb0f719cadc204
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: removexattr
  source_fingerprint: sha256:6439af61185c2a7b16f3f2a65f24af01f943a55f832ec93d23ee916a62521451
  recognition_fingerprint: sha256:32002ccab7f1975b7b58c13cad35af7ad55dc6d1d93efa4f1d2cdfaf7d004037
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: rename
  source_fingerprint: sha256:0a105956970132f4f9ae21a36b2581744782849b884d62e6c57b8421c45b45e3
  recognition_fingerprint: sha256:81eef5c6ae4959eec48d564518ec627516b874f5a81e6079bdc80523f05b7973
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_0C4BDB0FD7A306D8
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:0c4bdb0fd7a306d8ecb6e7a70e895b0aca5ba1102913276e30eeae19cd30b489
  - id: LTP_1028A46194A35788
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:1028a46194a357881abb36577857770560405dcd2cd7e491c8754f6cc409591c
  - id: LTP_181653F77A7325D4
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:181653f77a7325d4d6e9be62ec41f76d87ea39f0088c2eb54ed74ce461282256
  - id: LTP_71DD675C657FC49A
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:71dd675c657fc49afa572daa9bab9f9cb3d528a3143fc29cdcc8320b228ab019
  - id: LTP_7ED6923454F08CDA
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:7ed6923454f08cda2b9eb955244f59aee556c7ef830534b7b38d8f3d8498c98a
  - id: LTP_7FC732FCCE410925
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:7fc732fcce410925b179e152badb17d766fc13e192a7c683a3d195ca861c8712
  - id: LTP_83B1DE66214C655F
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:83b1de66214c655fee7057fdbdb01d4a7b745ca7b7900e1d0697a39c5251d416
  - id: LTP_95C3A1596DE75C5C
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:95c3a1596de75c5ca30b0e1b3cf9ae49463776899520921a1df47e7d6ad70a48
  - id: LTP_A8161E50B040AFC9
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:a8161e50b040afc901541fe93f3f64fb35e489237a2d2aa0c6693c9d635473a0
  - id: LTP_B09A317822F38991
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:b09a317822f38991f6ba3289e85b8f0b64e316a460d12752108a41baa255202d
  - id: LTP_C532732193F3A009
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:c532732193f3a009e105e92c5844ee94f1260038652681e2c1d0ff23ddc7921f
  - id: LTP_D17799C1BB191952
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d17799c1bb191952c8f2cc832abef239083c8d2cf1a28be3895cc743df184456
  - id: LTP_D7B9E8F8F713AADA
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:d7b9e8f8f713aadad88fddcb4ee4cd4cc6c58ff451bf164968dbde62d474f6a6
  - id: LTP_D98D789F4EBA6817
    generated_at_utc: '2026-07-16T04:20:06.737209Z'
    content_hash: sha256:d98d789f4eba6817bf51c596411fe28898111d5abc5991f3446fb238394f2e11
  - id: LTP_DA61AB6388EB2D13
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:da61ab6388eb2d13f1f9c41ee6119d751606215f79ad5d27098afa3ddb83fc55
  - id: LTP_DDC2A75ACE241003
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:ddc2a75ace241003888fac61de04e7adc5d2685ecd67ed0c5b15859b38e395e5
  evidence_count: 30
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: renameat
  source_fingerprint: sha256:b484089690ef319dbb36525f1b918fdb6aa65ffbbdde21ec15f189f4ce645634
  recognition_fingerprint: sha256:36f80e7c5b4d7d8c90a9b50c639add20e2027aa53e52aa76a7150404f2a6a233
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: renameat2
  source_fingerprint: sha256:80c20d8d5c7533d80f6bedbc88fadabd566d09bd1c1f4210702e817efd58925e
  recognition_fingerprint: sha256:d75be948287fa1beaa0ae52fea2e92aae4f351555455d16e6464176088a061cd
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: request_key
  source_fingerprint: sha256:423ef46d2ddcb4c7dc376b492da7da381104b81445989fe5f4cc49d9ebc72212
  recognition_fingerprint: sha256:b0207c7b71ef99ee2f9ce2d4c039c37571a20ad4a7240e73e22ed1031d1b32ee
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_06F742EF42AA55BA
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:06f742ef42aa55bab6e782e69edc9803705766d67aa9eab75909bf02683ba29d
  - id: LTP_078A6E34EE607719
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:078a6e34ee607719f2add08802faec894e81b65e83bfdcdfeae4bf206a384f4f
  - id: LTP_0A819CDD66F1C6A1
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:0a819cdd66f1c6a12eb3269542bb8543b1e76e4d0c775c6417886121ff53622d
  - id: LTP_1BDC4A832DB89410
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:1bdc4a832db89410164e6f7da6fcd6ddc57cede4911699439f09a8694f934668
  - id: LTP_4F41926D0ED26FBA
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:4f41926d0ed26fba8b8800522aa9bff32aab67d19a03350b28c3563117a3279d
  - id: LTP_A86F28C4D1358669
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:a86f28c4d1358669ae7ce8d3f3eff265b6c17893ed00a46fdc7eccc5a795332c
  - id: LTP_D90C4B47C5FF6BC9
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:d90c4b47c5ff6bc9336f21630b9a7fe512c50b19eb293af3d78249f059b07624
  - id: LTP_E7E64809057630A5
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:e7e64809057630a5cb2808273353195d84b39053a3820fa0f0052201057061af
  - id: LTP_E98952E12501919D
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:e98952e12501919de4be41fcbcec4cb37baef64243062b971b490f66a58fe29a
  - id: LTP_EA58792F115B6235
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:ea58792f115b62359347439c2865f386f226f8f4963e805fe9a93cb0a866b367
  evidence_count: 11
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: rmdir
  source_fingerprint: sha256:6e7c7f5273aefe5d79911fbd567c2f8184ffda56cfe141d330ba90e8e79ac491
  recognition_fingerprint: sha256:e793a6376e92533402cd0c19670e5767d7481a0b84d906a0f63d7a8ed731091f
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: rt_sigaction
  source_fingerprint: sha256:c50270d79fbd34dafc9956cd3d37c756fc1dfa8b9ba10dc5ddcf9dc71148690e
  recognition_fingerprint: sha256:9b817a7abdadb88d94f1e3f1695d0e0e548d25b3d0ab3bd4964d6663dcb6c937
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: rt_sigprocmask
  source_fingerprint: sha256:b83a8d936051efdb0e621d9b10d698836ba3c3de6464391928411e5e3875decf
  recognition_fingerprint: sha256:fa22e82c60cc25341d0c3be76a3e6239fad1fed9eff22509e8676ebaa681f7a9
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_423E92D9328C2A39
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:423e92d9328c2a39012f36f1101818dcc226c890746fe3e26c17d4cb2ed59755
  - id: LTP_485A86C9CB172FBF
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:485a86c9cb172fbfe0ec856309ece336f626a499d1948105115c076028cd3214
  - id: LTP_79D2E6DA4FED3FBC
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:79d2e6da4fed3fbcd7e9d8842c96334c4e5406b3197aaa902e464658dd4f6e1d
  - id: LTP_FE57D3FF371E3DDC
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:fe57d3ff371e3ddc787f08c7b217aa06e930c2084b9fae14db0bb298c5492326
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: rt_sigqueueinfo
  source_fingerprint: sha256:5371a76a0daf362d764bc44d6463eaf34e3e3fb4beb31261737a43072284cb32
  recognition_fingerprint: sha256:6446c90eec5ce09b47d6b30f9c087698fbdf922b2b91ca9383e9f968cd7596b4
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: rt_sigsuspend
  source_fingerprint: sha256:a339509f05d7a63fdd52c69210e4db823d24f54b13b54dea48f7ebada12afd5e
  recognition_fingerprint: sha256:a9a36f0306dbe4778e8eab09060e7ae1c6cffc2686e8852e04d13e8aafe1b526
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_0324F0A6601FFECE
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:0324f0a6601ffecee447fb77df26275c9b1387a811685caed50d33b39b83d2e4
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: rt_sigtimedwait
  source_fingerprint: sha256:2e3fabd8405d0272841cce71a0ed654b361f63b7569b910f562db52aad48db7d
  recognition_fingerprint: sha256:78b608f69e59c27c5ae4c8345d1447f55a83daa0a543a197307d4ed874a584d0
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: rt_tgsigqueueinfo
  source_fingerprint: sha256:b099f0ad3378f4d43747f19b57dbaaf1a99187ffce03f4d1c76d1ff8acd1256a
  recognition_fingerprint: sha256:c3aaf1bc9fbeda674b26794378f903447e5850ed0f60cf131a36622f02dd491e
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 3
  reason: unresolved_evidence
- syscall: sbrk
  source_fingerprint: sha256:a657a5609d22f7e93b24dab38ecb20d678bca1e08042704fd1b172885f0c4eef
  recognition_fingerprint: sha256:df7ff5a1444502ccb5fa237e9765aa43e819a12ad92640f0ae8262389a430166
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_03FD233DFE92488D
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:03fd233dfe92488d8883a27b3a0ff6f1d58c5031fc546470372a7347dd0efc39
  - id: LTP_139142311CF01E20
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:139142311cf01e2015f85cf9053b6ae29a2ac1c5cacb465baa3804bb7ecc7ef7
  - id: LTP_636EE8AC66A970F6
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:636ee8ac66a970f63629398c3a06d19827417b865c9adcb227c8adfe78462082
  - id: LTP_CB42FAF7C1D6D702
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:cb42faf7c1d6d7021c65f59b52c5daab8beb9e664492373d461c3f12b61e33ce
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: sched_get_priority_max
  source_fingerprint: sha256:268db35bb824e91daa90320658eec8fd0f6bd9ea7d87089ad27b080f131d4ac7
  recognition_fingerprint: sha256:546d349bb78bfc06c9a4fb26aa4bea7dc78f183cfd62786f2a6ba4c0b2ec4827
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sched_get_priority_min
  source_fingerprint: sha256:a01e6acad5a122ae399ccefff2d13ddb3ec659cf667a61066dc859befd1b76c2
  recognition_fingerprint: sha256:6d75dcfedf33dc5f3cb02f9fbc896d99d78056fd314c010dfd74d34c49f8f3cf
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sched_getaffinity
  source_fingerprint: sha256:b96ec72b029dfe9b38cb175c66fdc1cfb98dd63bdcabd5a0fe6e1f775837656e
  recognition_fingerprint: sha256:8fe40360837d8683c45876891858a04f5e76f8cb53382e38f4e05b9d74fb42c8
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_2CB0A10A3E175A9C
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:2cb0a10a3e175a9cf9ff374ed3cc5c0852bfbbf32ac3162a5be800ff85f22431
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: sched_getattr
  source_fingerprint: sha256:67317d0c3d987d58067abb4d64cb8c68387cbf2a6347b4965c1e583344578074
  recognition_fingerprint: sha256:74b05f27aa578efc789c8ad1bd47fa8d87e782659c3ee9cdd0b245b83b5cbbfe
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_0A2035C9A2A77F66
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:0a2035c9a2a77f66d7124809f3aaffc30d96f345435c22111272f078c8a397ff
  - id: LTP_8B95C6DD7983D3F3
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:8b95c6dd7983d3f3fb8a876d6cd499e233fc0a851365ce25e1101a179af79d9f
  - id: LTP_95C156C7EBB823A1
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:95c156c7ebb823a10c3fe81923e23e536edfbbbb7a0e66cf090e81c6a1f36075
  - id: LTP_FA750E6088863E30
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:fa750e6088863e30cae9f0c1960f16472319ad0ce31893dd78e9a7b6110f6da2
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: sched_getparam
  source_fingerprint: sha256:46786d8751654367de02d7a14758f26e0626151b77670037bb3ccc27d4744040
  recognition_fingerprint: sha256:d478265a1eee1090156f4153922ef99f740a00276cbf6f972019b0e9117e8ebf
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sched_getscheduler
  source_fingerprint: sha256:c8254738a8f08e3fd23b2747aafe7b5a00640f906b3a39e65307453c365a3ea9
  recognition_fingerprint: sha256:67c8567e17a2f5e113ff4f5f93ba39d82068c22295bb77595e9afd7f03ba3260
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: sched_rr_get_interval
  source_fingerprint: sha256:48e813078669c86660a656a4d433f98aa33878f3ae859683a2ae1bb38f6ca12e
  recognition_fingerprint: sha256:96ce5e45af07a0cdf06fc8d2865b8ad18ff1c61ad7c99183b35b726c8a6b7488
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sched_setaffinity
  source_fingerprint: sha256:d737035b7fdbedc650f60b52a75be3be2b4fdcf8ad96935e7881cae77d9e7b72
  recognition_fingerprint: sha256:95433e45843314f08b8efd97b16de6b203fd0e5e3fce1250dfd8cec49e32d140
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_5818495120E9862A
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:5818495120e9862a9d6e8e943fe7d0bacb9f252a9f7d78d65e0fda2b5a1d0ef3
  - id: LTP_585CC852338F38EE
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:585cc852338f38eedc86755b62d33a8eb443200486dd86bb3f79a4a4df80981c
  - id: LTP_97D64C0E53AA3FA4
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:97d64c0e53aa3fa43ac9171f931907f3c9649f7e1b1ea369f6bacf092a2a959a
  - id: LTP_D23BA34DB5624198
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:d23ba34db562419826707b44be08745b2172749f85b9825dde0d54eb3487dcc0
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: sched_setattr
  source_fingerprint: sha256:db3edc0354ec5f09f9eaa98d5f481dcea2d5c9a9869c04c0429b337db1b6dc64
  recognition_fingerprint: sha256:b9aec649c9c49db08363116c3f9fee248404ab4232a6e3d2cbe327d7f75f15db
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_4BA2A081C3EB3304
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:4ba2a081c3eb3304d69e4bd78e8f04758f3b4e119a33f827665c905bda26ee79
  - id: LTP_A55106AB533523B0
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:a55106ab533523b02256e2c636ad09c3a0a42d580d1a647f65c5a5ebd97fdb09
  - id: LTP_DC7E9134BB7F6F7A
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:dc7e9134bb7f6f7af3b18b3a23151e111f9ffe9edd6e5e5d94b4c4571c543647
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: sched_setparam
  source_fingerprint: sha256:52e940c0faeeef0e75d1ccbad9eb3aa090c3f07836f162a08270d63bf3f22be9
  recognition_fingerprint: sha256:ed9ae295bad902f1c1a7ce2cf26ffdbcd5244c524a3b942ddfa9d52ce0af5223
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sched_setscheduler
  source_fingerprint: sha256:3455609ffc6fa3aa961382e4885780b95a9e2d003b16a36968eb59f4a4408c3b
  recognition_fingerprint: sha256:b8c014b0b63948042d97861ccbb59607ef5a8e769800b0377f9aabb6333c5456
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: sched_yield
  source_fingerprint: sha256:e21368050e5aa9a67f8ab3907eec08e67a261a4283ebfe3113d35fa0295e355e
  recognition_fingerprint: sha256:892eca29e46c69b61e17d79874f3793a3e1183b8e813a2f34f97c6799fb4b746
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_A9BC7EBC1784A722
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:a9bc7ebc1784a72263646142685fb7ed3bb7aec45b58cfc208bd762f44d7c8fe
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: seccomp
  source_fingerprint: sha256:a08a8cb546bd41b6c2de5f697e8af7262e1eb04e046cb622ab5e3baa09ab2c91
  recognition_fingerprint: sha256:5156afe28ab5c6bd77423d6104c7cc6a3a156515958e4c2e475a61a8dd8fa02e
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_38B9BA93F16FBAAF
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:38b9ba93f16fbaaf7820e4e5581785efea25857debb9432d18f6e51e1276debd
  - id: LTP_FCC82752F512BE72
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:fcc82752f512be723b7c85042700bb2fd3b99fba4807c56a0e9eea151cea35da
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: select
  source_fingerprint: sha256:c120a43990251d5fe362a49b5ed5fc9bdaddbd04133552df885da4a5d0bbb44e
  recognition_fingerprint: sha256:4799b96c075fe8d1ac02bd0f5ce2e2fdde3d92f1fdfc6c242338a8f9ad836b69
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 8
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: send
  source_fingerprint: sha256:8efdc6a6250a706884a935b02fab565cd3f6bc2c3a2171e19514971b57346f69
  recognition_fingerprint: sha256:ee90111750c8905a188e5a2f1851eb355ca4ee913bd29ae305035ddd94277f5d
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sendfile
  source_fingerprint: sha256:3da9f393c15cafd6674bc2e14dbafc2dec733b7f672cecf14487c37badd11c21
  recognition_fingerprint: sha256:8513fa7ebfd70a85e3515d03371c2cf88279eb8ff1fa27910d1f9db3aceaacfc
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_38EE9A0047529979
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:38ee9a0047529979d02f062dd145279eb4070d2dfc0c8b9e1797b7888e2ab631
  - id: LTP_39B1E5C574F2D3DC
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:39b1e5c574f2d3dc16cd61efcb95f2cb9bffc5d5a5f86c1e52b9fac3ef82d569
  - id: LTP_3C1DCCC4E6DCC76B
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:3c1dccc4e6dcc76b11d8fcb57b268cec7dcd10a5a6d9103e731d6d3ae93953d5
  - id: LTP_4A5C15DAE55BBD2E
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:4a5c15dae55bbd2eefee551f4f8a1aeb562814c3948307a6108a17601802ccec
  - id: LTP_5A68AEA67C7612A0
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:5a68aea67c7612a0231bbe2a83dd7772f5c4f5d05a82e9025c971586d4e0c0c4
  - id: LTP_7BC885B5878C95B6
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:7bc885b5878c95b621d9876c970257da2de585ab5e9771c1542ceed3b28f8ad0
  - id: LTP_90AA1F0CFA6C6A5C
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:90aa1f0cfa6c6a5c3c8018fe2e50ad7904be8e7f4dff8464006a49f7e58374a8
  - id: LTP_A49B95E01ADFC6F8
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:a49b95e01adfc6f8a2365988a715f341e4f31172445c6e2e557162d64117bd31
  - id: LTP_A54F3585CC70C99F
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:a54f3585cc70c99f0f720a09c619ee917a07d13b34551316dd85e7595781da0c
  - id: LTP_CB84D44C84EB80BE
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:cb84d44c84eb80be136424feb6740835fa42027615d2c8f3ec0c9280a34df9ba
  - id: LTP_D01667E52BF34BFC
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:d01667e52bf34bfc0cb90c141143b963effdc882e8763d3c841d2c09ae4b129b
  - id: LTP_D3E85F64C28BBC4F
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:d3e85f64c28bbc4f02b8deb565d047299f024721f0c2e4f7b170f41e7e6de456
  evidence_count: 16
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: sendmmsg
  source_fingerprint: sha256:24a6a9743a37e37b67b83e8f8e6a9fca560463750bb44618ad9af197c764c616
  recognition_fingerprint: sha256:7c1bf60063449cb486deea436af6ec879c9aae42287a1e443155df3b7dadcf66
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sendmsg
  source_fingerprint: sha256:1fe9a9f51a1e5aa81e3bd29559b8848e42d4292aa2747f0cdff84ede66da07cc
  recognition_fingerprint: sha256:6cc59dc838c58c44db1526924d24a624ea6e14bb0071c147868a260cadd353f8
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: sendto
  source_fingerprint: sha256:3ca942e4d62a193e12ecd48ee2209df021850bc72dac643ccb9cd01c7b7c31c6
  recognition_fingerprint: sha256:a8cde09e2e822d3108eb2e83e3409f2a80c839376195c446f77603c7c7d72816
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_4C4EE05D029C81F3
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:4c4ee05d029c81f367d321941d0c1b5706ea9b7b846ac0866f16f0fc45b954fa
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: set_mempolicy
  source_fingerprint: sha256:c84a754ba0728ce99fa638d21b484589230d768d9c4df4acb6f2c364bac3335f
  recognition_fingerprint: sha256:0278b032c43064b3cb940467bc3178e02b615ad01cd76f2410c6345009366125
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 4
  reason: unresolved_evidence
- syscall: set_robust_list
  source_fingerprint: sha256:b4323495cd9cd2021458522b01aeaeb838dc5a256c2a8a77aa7d35c0ea4d3d9e
  recognition_fingerprint: sha256:42768ec3edf04ad814e3882f2750239e49c393e167e2cc7fddf2b181a03cc5d2
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_A89D10D41C3C2A1C
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:a89d10d41c3c2a1c92bd38989eac288e9edc99da5946bd272901ba5ce3f26e53
  - id: LTP_E0470C189C2D1DE3
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:e0470c189c2d1de37f10ab6be898fcfa26ff828dc89057c84d3ddaf504ab41bd
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: set_thread_area
  source_fingerprint: sha256:8a89a8930681d133e846f0fada73ed5166734e456d7baedc29b253d0cad22db0
  recognition_fingerprint: sha256:02e2f644387eb0ffceb54f705959b2ca6a340fdcb2373848ba33191725e0da70
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: set_tid_address
  source_fingerprint: sha256:25e1295de2df4bb2b9561a60dd18e424694a6df5434e94891576166450ed965e
  recognition_fingerprint: sha256:fbb461ab92ba6bc255506bb32a78a65139c2cdf1074c230a7f119bac37279f69
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_738C27178BBCE2B1
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:738c27178bbce2b1ddcb5104e95afd1dc31d020e311d844a7a3106165d4567cd
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: setdomainname
  source_fingerprint: sha256:435e9c7293ec40ef1a782a5985912e34d09c7c2447d3c329bcb2b019b347c788
  recognition_fingerprint: sha256:de9395eb502f458fbf38aac9ce2fee0cea965dbda88e2c71cdc6b1b8d5f1f9d9
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: setegid
  source_fingerprint: sha256:7a43d7eea77c2ed5b3093777eb56d56cc816e7f37cce1128cc9d776a4c07aa3a
  recognition_fingerprint: sha256:70f81e13ddb5dbfcb4a7111c0d3d87b676518a2864ca559520176617e737b695
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_E2D73477ACB0308D
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:e2d73477acb0308d9f9cc9c5d2d299a9a73f441fef7801f412caf88c3da755f4
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: setfsgid
  source_fingerprint: sha256:68839fdef604b696f339c4cb107dc343abf98ede5cfe9471ec0fec96b294e3f1
  recognition_fingerprint: sha256:e43f9b82f5aa79cd16ef20bc4b76bb2b75d18830d82678d41327fa8f8e10cb27
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: setfsuid
  source_fingerprint: sha256:0776bbcc2b66f237e85febeeaf742374979e029a16bd9e4bf73afc76cc4b43e9
  recognition_fingerprint: sha256:d67ee02abc1bda3d3336db86d58d9d7a91208d36cca7b5ac6c0fab96e615177e
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: setgid
  source_fingerprint: sha256:29246deb879c1a61fd41b72dfe7d2a5700b29af1a1bed635f7af841dd5440ae5
  recognition_fingerprint: sha256:627efb9f1debce660e2e9d5a6d9a9bef3226bb9a408a7e9f6853d1f14bb7e7e6
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: setgroups
  source_fingerprint: sha256:df25704acdc6afa12e9080045bde58e19898bf62a6eea66b24cd69be01d08f46
  recognition_fingerprint: sha256:beca3d9f3d2b5bc39ce636d73f980d4c4d460b3dc2c0a6676dc73eec28d0fe52
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sethostname
  source_fingerprint: sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  recognition_fingerprint: sha256:6df5128a90410129ab8c50eca90f00d9ba697762703078690de45a5951f7ea2a
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: setitimer
  source_fingerprint: sha256:a3aff4ee98a448c32bc9657bcd6a772fc896f40b3b5b2df63cedcd2469b623bb
  recognition_fingerprint: sha256:08aa6393eca6b0c8a6a3e7632441657fdf223c20df80cd07bcc8809fe7a4a3c1
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: setns
  source_fingerprint: sha256:aa8c9d8ea256d57c99afdf36d57ed6f5503a00085d93ebad6b70ebadacb80fb7
  recognition_fingerprint: sha256:1052a50a1af505964c1b713af55fb73cb26e6c2da66f7ce8161851159e58fd3f
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: setpgid
  source_fingerprint: sha256:748b15defef65b4ee2331eaf50d96bad8ec9b2d073be43202eb193748df2018a
  recognition_fingerprint: sha256:9371db3e668f70ac8df3305ad37806a90d2753db8c23ab0575d5cbb0835777df
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_0C5623B3D5C7430F
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:0c5623b3d5c7430faddca0c6166925cdc085a47fd9534b5346766354814f4715
  - id: LTP_37F4EFF424BB79B9
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:37f4eff424bb79b9fe2f999a6002ad74361f799b1876a12953dd4fccd13aa004
  - id: LTP_4308D71D8BD6519D
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:4308d71d8bd6519d6d2c15cb0c6d1925eed73874700fd6f1c1cc8a86199632a4
  - id: LTP_4BBF626715445EFC
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:4bbf626715445efcff616073a7a973c4f5334e1b2fa90500e8253f4acfb6925d
  - id: LTP_503160311D12E629
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:503160311d12e629f8bf79b1a7c0195e7aa8915d8e202086ab7bbaf632e90c43
  - id: LTP_9FC19C1455EBA67E
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:9fc19c1455eba67eeef13c8d700ab8c89c65990ae431b4f68f25ff75ae62b124
  - id: LTP_CF7B49C4B74D69E7
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:cf7b49c4b74d69e728d050ad0b2aaefdb4f5aab5d3613d758f9cd4474e6545ad
  - id: LTP_DBEC3975C5440D23
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:dbec3975c5440d231088c615db5b4d22bfceecc1f084c5aa3eba17d4421abef7
  evidence_count: 9
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: setpgrp
  source_fingerprint: sha256:3ecca3ffcf2929b9c9ef1f3ee72d0e3717620ad3c8b51e558eebc13e74af9e8c
  recognition_fingerprint: sha256:8a485f8d225a059e6997d0d49156b4dd3ec497d6d4ad551fb048c4ff93e88f2d
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: setpriority
  source_fingerprint: sha256:3a0740e9a4bcba576ae4df21e63c48aab6fdf902d46bc8d5ac51dd63ad023538
  recognition_fingerprint: sha256:995dab83f691ba4f0c744eb1d4714e84f7f0f5d9f28aff6a7ceba5bf89cf1e99
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_252DC2EE1F2FC3AC
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:252dc2ee1f2fc3ac21dcc909c66edbba191a7250ed927f0bff80077215522ff3
  - id: LTP_336B0AA063AB645E
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:336b0aa063ab645ef013dd364a649bdeae25361df4529da13641ca3743479708
  - id: LTP_44DC5382746D773D
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:44dc5382746d773d253ddf7ccb3ede2e242b978ebfb3e0756367ceb4d839956d
  - id: LTP_50853944DA25B2E0
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:50853944da25b2e0f6694eb621028eae0225c7734bee98d7bb6d1fca9a132d6c
  - id: LTP_757778388A97EE03
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:757778388a97ee0352730af9c96cf6344cec57c933fa5567a243080bf37fbfbd
  - id: LTP_933D919373F0F77C
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:933d919373f0f77cd647c8bf57e7f65f728199f28c48c4323d77e42ae5a647a1
  - id: LTP_9D4E5ED344B5751D
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:9d4e5ed344b5751da45ffab840fe6b7986c89e70a797ee811b6456cdd77d90b1
  - id: LTP_AF52DA4E6DA2BC9B
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:af52da4e6da2bc9bc597cc4d8a0a73fc1505f8f9f7cd41f866050ae5be4cf8f0
  - id: LTP_B6D4B61FC2494298
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:b6d4b61fc2494298733686e703fa2dde4a1aea40999211e68a96095c066f3c27
  - id: LTP_BB4C88C7C212DAC7
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:bb4c88c7c212dac73eaf78b975894ac2ef9eff45159afdc865d90d2669e60dbc
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: setregid
  source_fingerprint: sha256:cc23f510e807771dac6b0cc03617ea20df75ab98c44f01b412b42bcecc324fe9
  recognition_fingerprint: sha256:a153344419989fbdf363b78a4e5056b421cac752041b446880662c63d80f1c04
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: setresgid
  source_fingerprint: sha256:a96b99c87953c88c7dd4588b81c256ed004a2348226a0fdc913584870fbd5620
  recognition_fingerprint: sha256:658b0071cda66c8b8f99f21971b8bea90acb5fa91914209c28f76ff0416e64da
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: setresuid
  source_fingerprint: sha256:3e5791352632f2edfe4a5f7a1f38ca5aea27e7215cc0ccab679f0eb9e30997f6
  recognition_fingerprint: sha256:60602b451f2c15b9eadd59c27a400eabec8b3dabe8f9b21fd4c5030e0520c075
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: setreuid
  source_fingerprint: sha256:6b376d89fd8dc10095619325c3bdea6d166716bf1c3d27954c0283ffe8fd5b4e
  recognition_fingerprint: sha256:2cdd8713cfeea92e1fe51b38d1ab40a0a6039210631e7df8122eff2eab05f5b1
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 9
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: setrlimit
  source_fingerprint: sha256:3a72142383369e37b9ec7d25fc6064c023b5de3dcdbbeeab13b5a1ca90d5c06a
  recognition_fingerprint: sha256:e0e996d1bb3c47808d5f08007672dfb5768c58064b1ea228d107a918ce02c632
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 12
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: setsid
  source_fingerprint: sha256:aecc3b4981f0215ea6612fd6454e8bcf2f9299f1b459421d2f8625b03354295d
  recognition_fingerprint: sha256:56b12d73e4ab0ebce77e8013f9783a609de0db146995029fe6017724853de131
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: setsockopt
  source_fingerprint: sha256:9f42d93b03f5250db6608914c47bacc90e79b73f7e7aa0138ed2c77c3c03bf83
  recognition_fingerprint: sha256:f5f3cdefdcf490f1785fe721c196293bd71a77f03020f67f69601624369ddae2
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 19
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: settimeofday
  source_fingerprint: sha256:b6bc5ffa3739661873a5ed83fb07d2a36dca66892e259ae55d5ad58a06603f5f
  recognition_fingerprint: sha256:f708e749ce577a1f6483237edaa3e945c7af3b291e8d6d53630a3439c456533b
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_69DB4FB0496BC7A2
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:69db4fb0496bc7a261782fbdda46838bfb455caf8c08f18d2815d8f654d3ca49
  - id: LTP_8D95C734339E42C6
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:8d95c734339e42c65ba85fe78da08c9953487da889827d64fb4f956599e7f22e
  - id: LTP_B549A3600766CD49
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:b549a3600766cd4976c4bd208acbb6c399c9d99f9180d01bf9f3eb0308101dbb
  - id: LTP_BC4FACB4E14118C5
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:bc4facb4e14118c55af9280e31413271cb601c44d5149346ddbee929115f9234
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: setuid
  source_fingerprint: sha256:2d28a5d7ef5ccbe179626986bd9d49bcd6353036dcb5656b3ebb8cfef3da6ba5
  recognition_fingerprint: sha256:a78c907a49890b60898102ae2c0fcfdf1ce6b550b77f0dae12b12b31d36e0f5f
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: setxattr
  source_fingerprint: sha256:2b3ca06942914fa791e7d3b2c75f7ceaa490c4df668fba2a771e4c0db7457cb0
  recognition_fingerprint: sha256:9a1d4433b9fc1b709555a0c489e0ed135ffa5a49d52303d0344340021136498b
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 8
  unresolved_evidence_count: 4
  reason: unresolved_evidence
- syscall: sgetmask
  source_fingerprint: sha256:7472dab768f3bfd479c204abfd475405c9b0d9d0b9a4a84125082c92bd7c54f8
  recognition_fingerprint: sha256:a757f4767f9ed1bbeac6f7cda9f7576122e5932a0a56459b8c4aa3b8f73cde60
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_5560FF1D5C7F4B90
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:5560ff1d5c7f4b90cb6b9dc6ff446e034fb3abbf9e5ac3543fee5a34d3262e03
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: shutdown
  source_fingerprint: sha256:5f176c88b53f40e9e4d09f1d3cc896f8e84cf0ff546cc18e2fc2dfabab311c51
  recognition_fingerprint: sha256:7eea2ee45fbcf4c9f1db975f43638e4a535d4775d9a06165121586ce58c49d15
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sigaction
  source_fingerprint: sha256:61d9673dc305b0ea3d84e83150b83b5269afeaba5b1fd2277babdd5787f6cf1c
  recognition_fingerprint: sha256:c14566c2fcf8bbc7d84fb8db5b3bfb973c2c349c2db893e051818c3bfb2b8128
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_60398013DD319A2E
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:60398013dd319a2e19bc79bc5f924169a882c6ed66e535c094b0b2033712d693
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: sigaltstack
  source_fingerprint: sha256:bc11238dea2838136b2e822294839080ee40db7f52d011e2ee5bcefa58b4b9b5
  recognition_fingerprint: sha256:fa6cd22cb96212dcb2bbd53fb481ea5c370ccfc09e6ec536dd0b69871feef818
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_612BF74E1426528A
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:612bf74e1426528ac5648670a868c758db08a43a4347f410682648cf830f1251
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: sighold
  source_fingerprint: sha256:4ad49fded412785e4a17bb4add5bb7202a0cc746ea8ed37fcaced839c7c6ecd8
  recognition_fingerprint: sha256:4431cc1d59cd5d689c5f241fc403a47366ec830b21d83fd0d81304973050b595
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: signal
  source_fingerprint: sha256:01ab6c51adcc06a4a31adfa404816290f94f777590f35e82d32a43d9c376262d
  recognition_fingerprint: sha256:c6533f5c3e0c8d6d3cdc2da45ad5855a9ad865eb7dc59471d0e6a0bc36874ba8
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: signalfd
  source_fingerprint: sha256:fa8b8494a9a202da803c5ecda7fb307df401d2044779d412babeae9ec841e118
  recognition_fingerprint: sha256:6fe78f5ba8af3a615be3816a2e8a290c890bdf5c2487556eb82e64dfe908e87c
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_07FCC99E3AE43064
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:07fcc99e3ae430648ae15d04668074fae5efefb39929299daa91c0285f180194
  - id: LTP_0D9B02C95396CCDC
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:0d9b02c95396ccdc10dda4d00d47d1bfddb0dbed344cb46c07b843a583d61c9f
  - id: LTP_2668EE4D34576C49
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:2668ee4d34576c49d1b61d40707241e1d29669328dec31636ce9c9cd985a7758
  - id: LTP_644B7DB483FF489B
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:644b7db483ff489b863663d59320d40d38b083fafafb58b6a025df0621562db1
  - id: LTP_8BDD5A2DD306EFC4
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:8bdd5a2dd306efc48ef27714fd4d9d1a71f9a81316fd6b9225f0a58a4291f7ec
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: signalfd4
  source_fingerprint: sha256:3717445b60556e013073e5b04ab7348211c93f6230d7c603836a1d1d040b62ac
  recognition_fingerprint: sha256:20446a94d7f0c043c63b14480c67a3f92fd5f9996e1687af344767039c1b2cdf
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: sigpending
  source_fingerprint: sha256:a4e1a4fc089feb52730582fad120800cc1cc809bb2531a9ae7ad97e2cf6cea70
  recognition_fingerprint: sha256:df966141063a1162b97c706b1dc9cec78e2875df44f142902f1a259499707a6b
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: sigprocmask
  source_fingerprint: sha256:d70688f183380aa65cf0241a4314d3482172666d826e81a943ab27e277f0ae0e
  recognition_fingerprint: sha256:ed5cbb17ba0a14a18eebf47b05401cdf28b635c1d814b71fefa1db0f6ae666c3
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_B061BD44067799D7
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:b061bd44067799d71504a24b979754fa00cbd92c128b12f837f84c5a15037949
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: sigrelse
  source_fingerprint: sha256:dae50ddc14419a4b527353745091a6759900afcdf22033e8163f548841cb99f9
  recognition_fingerprint: sha256:81aaece8e594bb585190d8ee26ec658c9a1996f00dbe948e740f5141fd5e29b3
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: sigsuspend
  source_fingerprint: sha256:abca2c0631cb1398e2f22555d4d647c3e29f03d17a5bb09c27a6ea15c4797dc3
  recognition_fingerprint: sha256:7130a47695c15272f8a509eae7cf0c70e8f8c6612274285e954292c06d9be229
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_55D2492560C39AFD
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:55d2492560c39afdae0198b58071de3dce1131484ca2d56f9b815ee38a7bb70b
  - id: LTP_6C1DF45A5C274B15
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:6c1df45a5c274b159ebd3446eceea2610ea8628fd7d7a84bea463c83e6513935
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: sigtimedwait
  source_fingerprint: sha256:76475232466a02da15b91c7ca6eabe16eae8a97fa6071e450e7db72e8488f5b2
  recognition_fingerprint: sha256:6ed08c7d03cd26ed2c8c57378d0c5ca652a4c005dec0a5d56b47acd05c958b47
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: sigwait
  source_fingerprint: sha256:deb22e843c39406141db44e7871bb3b4657c5d6981d3c731b3d9e61187c9333b
  recognition_fingerprint: sha256:47c5a5ac03a6645f0c57a5f0f95a2a920b8ecd4b6c1eaa889af6995158d60591
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: sigwaitinfo
  source_fingerprint: sha256:0d9a81c57b46c154fbcc83a87da1a41817db30f5b73144634869dbeb40610bd4
  recognition_fingerprint: sha256:4f8dfeac304a7631a5565872d53e7634d2dd12a6dc467bdf812fa50f288236ae
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: socket
  source_fingerprint: sha256:6e88dee3dee49e7e242bdebe264952d30e2f8a9bd081c9f66e6bdf05a74e4955
  recognition_fingerprint: sha256:74c5f92e15df2b9975bfae96376f05d5edb270815ee6c3dfa120810bd6218a36
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_6B29B31CE99466E6
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:6b29b31ce99466e6682913919c0fad006475b094d59fadcc43c1ec6f4e9d1630
  - id: LTP_971DB17D32C51561
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:971db17d32c515614f0af38045463319bd4bfb3a661a4ae9e4486c0404c75ead
  - id: LTP_A4A662687B98D33F
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:a4a662687b98d33f933b37774536af580d8b9e44d1bc317c426dd2c4a68a7a1e
  - id: LTP_AF8D38878ED1A9DA
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:af8d38878ed1a9da8bcca89799d36f633a0776307b92fe435d004f9b6cb1b444
  - id: LTP_DD2E1A555B603C7B
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:dd2e1a555b603c7b2ea7b60867a7cbf5b07e84f866b5a4cd8d83f27a24028065
  - id: LTP_E316C28E36E136DA
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:e316c28e36e136da592847ed1389e06538d4842d55259bc0bd80dbb61b78d10e
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: socketcall
  source_fingerprint: sha256:ed308e2e4f2aceda0639a0f7b4e6f3f60f463e0c0af254f7fac2715097782e9d
  recognition_fingerprint: sha256:649c655442f4737eaeb2013deab9a2bf438c979f47df878d8c86ecca40e379f6
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 4
  reason: unresolved_evidence
- syscall: socketpair
  source_fingerprint: sha256:d0a6793d2e195de68e11d78ff074bab36fa599bd7671738edbd47dc08de1c23a
  recognition_fingerprint: sha256:fbd4970ccc4ae0bad73af99b76d41c3776d81ccd430f415ea71ec7b687cda40b
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 3
  reason: unresolved_evidence
- syscall: sockioctl
  source_fingerprint: sha256:36d05e1378bcd2d1e52c43dfaa00f6f308d4686c6add690d926e3eb2fc606731
  recognition_fingerprint: sha256:9112a83f023ca4b8cdc18e58b50cfa02b868120414c4815e193571d5bd583ee8
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: splice
  source_fingerprint: sha256:6999e9c329f6fc1d92dc7781ace26322268dbf02867df516a33f05c10bda1a8b
  recognition_fingerprint: sha256:45dba1eff8cc2f4fd494526eac22b507f219e83d679d5488e7c3805eb7a6b85d
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 11
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: ssetmask
  source_fingerprint: sha256:c644f8035edc4d76a50f42b97ddbc4061d795c967633b62032e164c2ff6be3f1
  recognition_fingerprint: sha256:ff5f99d1dd4c78ac49532a60b687e49c0e068248626f84085ca39763164c2bb9
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_8CFEBBA603A7011A
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:8cfebba603a7011a01a3c126347ebc10bd534f655fa7958e0c85220d8c5a21bc
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: stat
  source_fingerprint: sha256:5b94e4a9a3797680158419e8bc1534af3acf00b68a1ded9df55966179d50ad2f
  recognition_fingerprint: sha256:517aa5b58538d0d1b5d6d6ba224d765133cc5d493a78abbdaaca8c55eb27d928
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: statfs
  source_fingerprint: sha256:8eb29f7303da698593485eaf5b364f7b3d95ca08ec5c5811aeb1985ea170f1a6
  recognition_fingerprint: sha256:8a60623a994e450dee4af8e7f9dd926822c84cc9cfcf945a8353e031317dc531
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: statmount
  source_fingerprint: sha256:abd6c9a31b025bfe43b885a1ce7a8ba67ebf487f2ebd7cd2395f53485477a315
  recognition_fingerprint: sha256:4a366af61e4fb3022cd5800f7e2bcfcb0829d4fcd9a4b6045f229616ffbac942
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 19
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: statvfs
  source_fingerprint: sha256:38789906e9660ba3a56673aad9fbf81dd31bb00aaa0008bd1b76347b00dc9e17
  recognition_fingerprint: sha256:1c97e24685c07fe0caa714d7500c48db53c2bee9ef07e99b1c8f815d3757b133
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: statx
  source_fingerprint: sha256:4b92eb3772b36967a473e0f6878f39275e1b1f37148ca6b18b978905c7096e32
  recognition_fingerprint: sha256:510344718b568ae5e84027dbad10191ccf5119a66fb11f00c72f989745edbc9a
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 31
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: stime
  source_fingerprint: sha256:1cca3ba099e9764bd786abb404953a2cbdcfe4f60b8d89008fd7c986a576a8d3
  recognition_fingerprint: sha256:6f5d3b2616fab3e59cae0a76d7394efaff55700cf66932a415b912a19ea507c5
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: string
  source_fingerprint: sha256:c180c2ba42c2db20c03acef1fba349d63befa09e1594262f866b80d26cd0f584
  recognition_fingerprint: sha256:94e602e286368ded13da8273c7fb8f3145a68c5408080ff9aced3735d614c63d
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: swapoff
  source_fingerprint: sha256:0c20f51c6916682dd60d3401a54bdb10eb514ff2d10c1c56c8996338f037328e
  recognition_fingerprint: sha256:7cbd87fa4fa70f3dc29114c8b13338591120a97052991e621fcfa87e53bb4cdc
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: swapon
  source_fingerprint: sha256:b282f4161865f2b6668ee5ece32816b50561c189bb9f9e13490e7d2f01d251fb
  recognition_fingerprint: sha256:23b299609abaaca7896fa886eadc2a47aba1796164e13facc742ac3736f5de8f
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_66AC645038FEFC7A
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:66ac645038fefc7a9123ec598be7a035ae49c84595a5fe8f4b584beab1410fe2
  evidence_count: 6
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: switch
  source_fingerprint: sha256:70106259cc71c2c8a28e372c6076525d433171593b67002c36d4e2ecfd31ccb9
  recognition_fingerprint: sha256:f85bd8499502dc961816160e57245b1e28c4d7d9316b2cd33963c21ef31ca546
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: symlink
  source_fingerprint: sha256:bd4df855da95e55fcb230a4d8631acfcf67a876774a10d6cba2f28766b425a6f
  recognition_fingerprint: sha256:1a722a899211d98c33df20ecc890240f9e073deb7904594a96ba3a8f6d3139dc
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_1551C6F53CF6865A
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:1551c6f53cf6865a76134b85a3bc843a415c1b1f874cc0e33fbd203e771d2061
  - id: LTP_29873BE2A9AABFF4
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:29873be2a9aabff487752e9402604cc9a862ceadac098275cffcd26990304244
  - id: LTP_2EF9C7EBEC450E9D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:2ef9c7ebec450e9d34f8c707c81f3515b1168cfcd705555ad7a67092d3e25662
  - id: LTP_34A1F75164462203
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:34a1f75164462203bdd61756365a433e542d77e60e5db737fd4c977902a8e080
  - id: LTP_80C28F63B3DFD8B1
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:80c28f63b3dfd8b1d7a749b7ee6615d3b4bbc6f648df3ac96c73598c042f9a75
  - id: LTP_8ED8688C6292FECF
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:8ed8688c6292fecf560fc5e28ecbab9d72c1be7828ea2675df118a184abe8b91
  - id: LTP_91664E8E6FF0FCE1
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:91664e8e6ff0fce11712eb5696f22ce4f7837aa5f7b2d872a54a60fa272aeb8e
  - id: LTP_A3187FBB07FD0E35
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:a3187fbb07fd0e355e62a41c8013672d6d4484ea5a4977941ddcd7d930f09283
  - id: LTP_D8F99518FF4E8643
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:d8f99518ff4e8643c8a74b95d327b12985404bc44c965c9e3e23563c81ce4922
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: symlinkat
  source_fingerprint: sha256:7d19a3f68ce9bce0be98fd410bab95dcb4acfe7ce3388965e42a816907aa5077
  recognition_fingerprint: sha256:1256bd849133f1ed175a2143a10072d6866018a8c873108e6e4485eb01de803d
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: sync
  source_fingerprint: sha256:6422428a20c3b718edf0917323037a1f5faff1b0653359e65aa46d565347f9b8
  recognition_fingerprint: sha256:85cfb6101639506f83e77ee25e438aa67843ba069d4af885cc174e2b783d835d
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: sync_file_range
  source_fingerprint: sha256:9549e4b46f60a4e43e0781afeefa4e6544c3d3b047371be9109f55aadb61318b
  recognition_fingerprint: sha256:03973751bfa2d4c540c7441a8b94925217fc344df1d9a4f324a22359301d7703
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: syncfs
  source_fingerprint: sha256:633bc5b862527c690b6f46ddb8ddbae448faefa63185dfc1d02433e2a9ff0047
  recognition_fingerprint: sha256:3bbfa0bc1191a411755ea4324199887ca9347c0927b5cb495fc93143ffdce6a9
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: syscall
  source_fingerprint: sha256:30f4af78d21f1f50fffcf043eb66b2767102edc2ef148e30af2f367ca6c11d5e
  recognition_fingerprint: sha256:2d2b9cb25ac2e744a93610803a9b4b72ef20347cbcb0b33de7723b9c70b96087
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: sysconf
  source_fingerprint: sha256:fbdea403a040a4fdeb953f5b20437c090677a148bb9b5ad06467c2aab8df56d6
  recognition_fingerprint: sha256:d985cf08bc258c88b490aeb642f7f1e15ecabce4192e01d638f078a6d272bd84
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: sysctl
  source_fingerprint: sha256:1262294d7ac974e429bc9b1ac873ae55311c865623eeae569b3b1f428c790fcb
  recognition_fingerprint: sha256:030b835e96823bf160be9c3252f540bec4d2d42b1ec0528e1795f4d0f0040cab
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sysfs
  source_fingerprint: sha256:a1d7280e01310ab19fbe9435cea6845d7d69b288efade7464814c9d8ffcbb4de
  recognition_fingerprint: sha256:b7bd68ccfab66f3c50b363bb0862f2d6ee3cc8de171b15bce04ad3d4b4349cdb
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 11
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sysinfo
  source_fingerprint: sha256:230ce7e6f3a21328efc74bc13b27432b6f8b358aa89f34f007d490866f253dec
  recognition_fingerprint: sha256:d7bd10627d5482c0205adcb00bd71422196937818130ff0752a1023c06c9e169
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_A367723236ADA8B4
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:a367723236ada8b46a0d6d3a444b7812e36d2f96cc8654bcd32ce5076bb39ed0
  - id: LTP_F0BF53984C9E5C92
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:f0bf53984c9e5c92c40b0dd388ec437e290d975748263d80ebb353a51aedae8d
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: syslog
  source_fingerprint: sha256:62c4654d4b12139bbadf9ce8646ede27ce5293c2bfca5a48c2e84aef38ff2bce
  recognition_fingerprint: sha256:f401ce520141873ce8526b6f2d969a880ae70d5038d5180d26e0878b74da0a94
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: tee
  source_fingerprint: sha256:f0f5563b5ded9ccc989355f4f2d95b1de904f7dddb9adf1d54aee34a13099b33
  recognition_fingerprint: sha256:c9f06c2e1037faef08981a86dbaa515944b5e3ed184ab48a97fde2b297f5ae03
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_0F9C596BA8184375
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:0f9c596ba818437541965933af200a848ed51ee0a74554f0d4613e07a3e7c60e
  - id: LTP_769389D69FDFA661
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:769389d69fdfa661d0be3e62950ec334150de44df4379facb2cce7e7a27edac9
  - id: LTP_AACDFBA8019E2D25
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:aacdfba8019e2d25a21fd2c55441f5db819d03707c85e0dbc936a3269a6bfda1
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: tgkill
  source_fingerprint: sha256:b7ebfd867b2a75eb7247a755ed4bab5d7b57caf6308f763fd2e5382bca81cdda
  recognition_fingerprint: sha256:68d8d89451fc76adb37e98979adaf61a46435241113a5cfa52f92e2734ac1c76
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: time
  source_fingerprint: sha256:2edaa199d4fd856ca678a85b80a7f2330ce2e9e7744473a2a693d656848eafaa
  recognition_fingerprint: sha256:e3ad0c4a0319adec423661118e9ee9dba1bbe36cfae9c133b184ca4e220fa6f5
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: timer_create
  source_fingerprint: sha256:3c0ad32c8b4d4d5c6420004eec75aac394c608405f046696b813ffe465b167a0
  recognition_fingerprint: sha256:e50de7260e2b11b1a138b659151c70a9f34a9352134abad3d2e5914068c964d4
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: timer_delete
  source_fingerprint: sha256:f22af16816b16cd335c668240718f3e296df38cba4e85b675fc42ba082288e55
  recognition_fingerprint: sha256:b112fe5f0aaa8372868d936bac928dec8afa264edfd65abc1912d355472db73c
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_10B3572DBFA6742B
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:10b3572dbfa6742b44e40e6ffb78f797d484d1c0f37cedc5e4bc5c0099e8b498
  - id: LTP_9B36D27A4A2994D0
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:9b36d27a4a2994d0fb9becad9ddba6985ba56fddf7db2169f2efef4819243591
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: timer_getoverrun
  source_fingerprint: sha256:f10b490b999555739f799f0c37ba286cb9ba2730d4f9c5d42f41dc3ea24cc839
  recognition_fingerprint: sha256:c4dc6b55f4eae1dbc45aba13cd1940787494fccc67206dbe4d1cd730005eb97a
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: timer_gettime
  source_fingerprint: sha256:65bebaf1198e803f48824374545a02fad7bf0675ab9a53ac463993e6d42cbf4e
  recognition_fingerprint: sha256:a57660d84eb75f83832bda284aed8a45589eb107273d321ea85466f42dd3c11d
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: timer_settime
  source_fingerprint: sha256:6a13214fc81d1cf230e3ad90eb29897963a1e05e5633cad613fbf7048401ba4d
  recognition_fingerprint: sha256:4022fcda25e51aa1c7d631063abe089624a2f588e842da0779d65e2207cbb1d7
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: timerfd
  source_fingerprint: sha256:7e568a6cbf4a8b4e62a928d8222728c26246baf09381f67644467f8cdac7fca7
  recognition_fingerprint: sha256:8516e4ac5901e501037658408f365779e9971531271840b198955af921cb3cf0
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 3
  reason: unresolved_evidence
- syscall: times
  source_fingerprint: sha256:e3d621ee1c7e22cc4df76d30c2a42b837a51aec99adc0450425927b94bec3c67
  recognition_fingerprint: sha256:4b0aebe25f9bf5ae4d4e5df19740930cf7715c3b7763f3aa58ba9bff027fcf10
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_A1AECDF3F41769B2
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:a1aecdf3f41769b2ff10d8e153acb18b6f211cabb8281ffcdf923018d6269550
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: tkill
  source_fingerprint: sha256:3037545b98225d05d5b49168e0d4e46294c30c9242ce3400b3ad32a241cebba0
  recognition_fingerprint: sha256:f1103cca2f5141f6298a7192fd90adeccec5d1a5caf60ee70dfb1695fa8e3f97
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_2084284EEECEEAC0
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:2084284eeeceeac0e6f5c717b5b17232056b355dd77de847c28449311321c9bf
  - id: LTP_EF9CD83ECACAA86C
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:ef9cd83ecacaa86c2d4c93d98b8ca5dd3cdbb29fe71fc87fb7cbd3254e95b616
  - id: LTP_FCC236A4D5926B81
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:fcc236a4d5926b81662f49a2c62c658e9c87bcf2c7e179151e8658bd9395a42f
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: truncate
  source_fingerprint: sha256:662b6c1331558c73db1e6fde76b7a2d70b32b0a30abb6fcc4c7ca429dc4b1318
  recognition_fingerprint: sha256:6b150c76f02f24840f23eef10f8236c36404ce6d353889e9bee0df95c05ddfcf
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: ulimit
  source_fingerprint: sha256:6b5527f2af95ca4470378246dd58a9708c75c667f9f5c69626b1bc90adcf9a94
  recognition_fingerprint: sha256:cc8667e1b9ed2b8606c61aefd20fc8fc8ed695823d0d6d936c182ef258f2870b
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_287FBE05D7B30C6F
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:287fbe05d7b30c6fbe2694789ed8d27dfd69891644ad0a2638b4bef47e6dc257
  - id: LTP_3AD21C6E4A19DB15
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:3ad21c6e4a19db154e7b70d9c4f31cd477c5a278e6bb533c98e426116fa7d4f1
  - id: LTP_3B4D19754C5D1638
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:3b4d19754c5d16380eb8bf1f188d3aad4e6a5ffb3e0ced2e504f9a95ef77309d
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: umask
  source_fingerprint: sha256:47d64ed1c8a0f550e1ba6bcad3f9cc1ff9d9c8bf84585860cd5568cc7ef1c604
  recognition_fingerprint: sha256:1d6f916e9f3228a8aebcb44e2c9d9130c7634d384e63c4893201e594baf124e2
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_FE4AD44ED28FE386
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:fe4ad44ed28fe386c6f454015920a059ba052becc45d76521fb756e0a11bc535
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: umount
  source_fingerprint: sha256:b74821aee29d2b1731f3f7bf4522867440daee39547466bc245781d91140a784
  recognition_fingerprint: sha256:82e11359bb67cce0be0a0b7820bdddc1a5b7cc04eeec148b4924c69aeb060070
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: umount2
  source_fingerprint: sha256:026fdae27c0cf73a47bfb7412efa7440c3ad36d802477aaa29f6bd4a77a5b908
  recognition_fingerprint: sha256:389d30f721d254f4338967abc7cd3de3c6dcb9b23f5c7973db9eab03fc185ae4
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: uname
  source_fingerprint: sha256:809ee6d0c537a8c783c72f21457ae65226012bc42f61e371e4f5380149181f7a
  recognition_fingerprint: sha256:852c8d013fa7cf6c4e555933651754a9bef11a9df865f2cb29f9c726098557b2
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_5516B8A938B9C3A5
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:5516b8a938b9c3a56502a0790304ef99d9caee848e7faaafcdf2f016f6443230
  - id: LTP_7D48AE1036A3CBE7
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:7d48ae1036a3cbe77927da7db841a139a0523e7fa1a8738d4ade7294c55a5510
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: unlink
  source_fingerprint: sha256:c26e8ac44302357877f7d0878b75133085d818f06c24719be90b0d2c95f8875d
  recognition_fingerprint: sha256:59a67fa387c17107638f82f46911456cd22d75987d188c10caa2cf3fbb87772d
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 10
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: unlinkat
  source_fingerprint: sha256:1cb52ca796b06c5790269e888dfe6b9b227c24414e4cae7886e0f7117e06b2f0
  recognition_fingerprint: sha256:6ffb7bf7829f6a8b70c30228d389b241508db7a55a03494e0caf3480fbaff121
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: unshare
  source_fingerprint: sha256:c8c06fd3fb37ee58b2df434755f202a6becd88284141bd430375a4e1ac023730
  recognition_fingerprint: sha256:ad4d09b38f08d0549d5bf49d479139d57772e05b6d3385441822cafecfc9221e
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_40A45C5E82D7F4A1
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:40a45c5e82d7f4a1748fc7b7d74b4700d4498c801e0fdbad387797d941bb7a7b
  - id: LTP_412173E3E81DC995
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:412173e3e81dc9959635f1c34d93d65232ba6f40956db08eb86c6214301565d2
  - id: LTP_49ABEE42EF290FDC
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:49abee42ef290fdccc194857d597df925fac592f976582768e8ae944c3a25482
  - id: LTP_79882F9E36FC9878
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:79882f9e36fc98785b2141a1e7d4ddcb6b29424f7eacb2c5028ef17bcdabb831
  evidence_count: 9
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: userfaultfd
  source_fingerprint: sha256:984775e5d36678185dc7a62fd3d6fef8857585d0bb78b6dc140f0fd8c8990f32
  recognition_fingerprint: sha256:6c0f15bccf4400ede6071639c7adae7278b58cd39b1d65b307d2674b276fca25
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 7
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: ustat
  source_fingerprint: sha256:701bc07cf47f966e21ff5ec22f27541a8a87f25a6c0edffc3f8a04fb3c42a43f
  recognition_fingerprint: sha256:bb8087a43015045e784490322d00a23b7ed6a53551a709a73cd2c82a4de81e16
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_14105E9CB6DC44FC
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:14105e9cb6dc44fc9041096a73f814e989b2fd58998fb3840c19f444656c49ab
  - id: LTP_ED8240DD1329BBA1
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:ed8240dd1329bba125f546f7e24ce2c105f3257a289473186929220b81cafa8b
  - id: LTP_F75110BE79864CD1
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:f75110be79864cd1d4048f6b85616b33cb4d5b1b114f83177fed3a73e2ab395a
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: utils
  source_fingerprint: sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  recognition_fingerprint: sha256:6df5128a90410129ab8c50eca90f00d9ba697762703078690de45a5951f7ea2a
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: utime
  source_fingerprint: sha256:1eabec8784e6ecd5375cc682945366f2305ebb6f79e4f87f5c74802f0490460d
  recognition_fingerprint: sha256:22ed15bd7dc87cac1b3c2f01f210f28f9b552a8326320e2c1d24f7b230f49f11
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_0433C0FC2D4AD1EE
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:0433c0fc2d4ad1ee5e378f4d92a8f423248c70ef1c86427edad8ec47b98d518e
  - id: LTP_100C7EAA3620A220
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:100c7eaa3620a220766d6aa605b004def657eb4bf3692b5bd0be05b130d13986
  - id: LTP_428A6CFF573F0942
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:428a6cff573f0942e02a78b1b3f7f0c410ae4835d02c7dbb84c6f80519dce244
  - id: LTP_8C5755D366EB8CD2
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:8c5755d366eb8cd2b36b06a482907e8233aed897127ab92829b13a920aaac7d7
  - id: LTP_BAA1410033A7464D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:baa1410033a7464d5e7e2d090730f6d0a2415cddda3af9d410e525e02144c09d
  - id: LTP_CB319D75C5C1E14F
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:cb319d75c5c1e14fe949b75f7230e1fc109f3be5d329c733d66ac22a67c34487
  - id: LTP_EF32B2CC0F6F3848
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:ef32b2cc0f6f38488619c4376cd0af633851b9efceedbd6aa9daadae9a887bf6
  evidence_count: 19
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: utimensat
  source_fingerprint: sha256:ff0347d28769b35cad9698b38d130a690e077ecaa0a6c03725a8467e71d071c7
  recognition_fingerprint: sha256:69cae0b781b99f185237353775facabd8d1dd0d115fa422ca28d9bebf157ceab
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: utimes
  source_fingerprint: sha256:c98626ff7a10942ab5bdf99142786f991abe275e46cdf75a254336a56f273aa6
  recognition_fingerprint: sha256:39e713f90d7d8a890900af214d62a1b96df74fb9c8fc8105bcf84a7fd75b22ae
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: vfork
  source_fingerprint: sha256:2d9866995435c96b3ffd7ca10b45ccfaf95c2c65cb2388621fd91257fc5a8f86
  recognition_fingerprint: sha256:85551ee71d6abb46ef84367050bab661185b99d7a9d11cef86f634368685eaec
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: vhangup
  source_fingerprint: sha256:d3fb85c015a3a7d4d8d23f3d1e63aa71760f7640152f835ce3d20eb6b4b1b4ad
  recognition_fingerprint: sha256:9ac9f9a3c00f4a5a59cc216339343e5a927da4a27b31df48c44507d6cb8d728f
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: vmsplice
  source_fingerprint: sha256:e72a1c8ae19356d37d917eafb188699f33a61a7787be53b6bd6d80c638060140
  recognition_fingerprint: sha256:e2c9aaa12026b50a7f281d031754975543978688e986f62779f56c226e1cd691
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: wait
  source_fingerprint: sha256:72acc6555cca05cb5deaa5c954daabcc7fd9bba722c565f2595be5efed60dea8
  recognition_fingerprint: sha256:5ddafe94fce9e620e75eee1b0412193a55ec35279bbfad43ad5c8a9f08512839
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_7B0F966046AECA7E
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:7b0f966046aeca7e7a0ddc40b2774c29247dbabb79174568412a4d08596db153
  - id: LTP_AD3A4B98FF201ABE
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:ad3a4b98ff201abe4bafe39d5fede2f4d497cf03a7d50837c4c7441c515b34fa
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: wait4
  source_fingerprint: sha256:55aaa3aafb82fb4d4aae73d93dff81177109e661414bc79af421b8306cb32b9d
  recognition_fingerprint: sha256:73b54787c8b14588cc8df4f0dc681cf0d90cd31f22c404870d2df27c57e26200
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_1691F6F9712C5546
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:1691f6f9712c5546d1b81c76cc385ed8b961683e209c8d54e9543a02a199aac5
  - id: LTP_2AE73292A13647D5
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:2ae73292a13647d5e6dee08daa890622c416f4fa286b8e519b746de14bd3fbf9
  - id: LTP_C24E55F06625D564
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:c24e55f06625d564c76dd85c6f1bb8c94b1270cb6e0d83790b02371b7f8fc397
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: waitid
  source_fingerprint: sha256:a807a8ba444bb56a02be16251671b3dd4c2b2c8fc1c1d532ee42addf38afadcd
  recognition_fingerprint: sha256:6a79b087746393f451787c2db08d16d2ed2399c73125cef305489ddf43673eae
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_0FE0E20EAC6DE889
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:0fe0e20eac6de8892477791e90bb41b553ac27e1e89cdf43a46481d27780b7da
  - id: LTP_4494B70BBA693D42
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:4494b70bba693d42cda9d0a59c88ea7d9d8bd0fcb3276d8a3fc52fa386e7ef78
  - id: LTP_53E7B9C40A44F6D0
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:53e7b9c40a44f6d0d298b3f10007f7160a468a8ca200a36aa444b9b8463f2415
  - id: LTP_74C73CBABE325D5D
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:74c73cbabe325d5d86536c56b5a7a034406acaa122b54ff7dbab1fe8ce929c58
  - id: LTP_77C2FB4A0A9E30F2
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:77c2fb4a0a9e30f26ee316c385213fb42393c0799db581972a7db5c406767132
  - id: LTP_9C2FB7732A0B90B6
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:9c2fb7732a0b90b68e056c2337aa1e81e2e609b6ad6c60d53dadf2893b11554b
  - id: LTP_9FD87A3F7688FEF1
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:9fd87a3f7688fef10bea92050ac0661fedef311659e6ffce7573ff015c42b21d
  - id: LTP_C13C4F63D58904BC
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:c13c4f63d58904bcee6e68546c3fda582209001fe4c9e4e9a46eaf6a25719cfd
  - id: LTP_D1A18560E485E146
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:d1a18560e485e146f23212528bc3caba854e266e4bd431c7605891935860d811
  - id: LTP_DA64FD04E43656E6
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:da64fd04e43656e65129d77e5bf6b393319bb248852a3a6db4431783ebad5bcd
  - id: LTP_DF5B725563FDFB31
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:df5b725563fdfb318278bc71aa9ae5ffd772ac4f05dbd9b4f118bd9df7339f3c
  - id: LTP_ECD986F27CF15E1E
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:ecd986f27cf15e1e145501e0755a1420d46a42ce091e57d23884318e37849a39
  evidence_count: 25
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: waitpid
  source_fingerprint: sha256:e2656c2e1ebef45d19a5252c824a35d8b85e3f3b7843fe1e21e2e0a9dbd93955
  recognition_fingerprint: sha256:45fcefbcc2950e9d1858d2800b642b18a694d5aff5415b4816f76224a43789b8
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_03AF14160F8B59A0
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:03af14160f8b59a0b546095a476facf6e3504937dd6f387971839bd21441739b
  - id: LTP_2AF5913113A326EF
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:2af5913113a326ef45070947084470a9f0e37043d0537ff0b5487e371ddcae1e
  - id: LTP_2F3E34FD672DBF34
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:2f3e34fd672dbf34b28611337f295a687ae0db9f5a34edb98b0cb1a9b82235f2
  - id: LTP_614C018F61C078A0
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:614c018f61c078a0c1629bf12f259ab3108460b39da9611587eb8ab0f96a9017
  - id: LTP_A448981C368F9EBB
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:a448981c368f9ebb4dbd65e1845afcff09c4c5822526790ab2d8201e258370b4
  - id: LTP_FC8BA85373EA2D8F
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:fc8ba85373ea2d8f73d801b46060fd0ce0d4e78ef2f1ce6a5923118389112ce8
  evidence_count: 6
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: write
  source_fingerprint: sha256:6dda79ad1797a15505bc45e729ac05060fefc4da5f8290d5ffe46a9d9f0af98a
  recognition_fingerprint: sha256:f7cb917d2bd249dd1f1c57182693c9ec204ea539dc8229a5827f9d77897bde68
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_05B109981D13ED76
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:05b109981d13ed76154b1411f6997daf1d254a9c067f513bef268b4d8581477b
  - id: LTP_1B63533FE8D3FAF0
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:1b63533fe8d3faf00899504061a02959b665f81da23e24ada65df7b4399cb0c2
  - id: LTP_6E631BC61A5CEE12
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:6e631bc61a5cee12cba6a6b3566fd41d0363a89284e7548f6853805eeb785574
  - id: LTP_85742F5EC5C0112F
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:85742f5ec5c0112fc5450c1c6c95469726dbd05873c4632fc58a9157f73831e9
  - id: LTP_CB0D3A27CA90726B
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:cb0d3a27ca90726b54114413b3fc4a8be1fbd848398dcd06fbc316842af7a0d1
  - id: LTP_E8BA54C78A3F671D
    generated_at_utc: '2026-07-17T05:17:17.636551Z'
    content_hash: sha256:e8ba54c78a3f671d012f67f096af969315100533c8751c1a7ce4647f29a0f8da
  evidence_count: 9
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: writev
  source_fingerprint: sha256:6ab89a155f1732cadab0c34d356b295b5d00c931a8cba19259e1db42966cae0a
  recognition_fingerprint: sha256:54f64f6fb2acb3a37f5023e71bfcee5b0a775694e60ffc04f5d3d5699191f17b
  selection_reason: recognition_changed
  result: no_rules
  rules: []
  evidence_count: 7
  unresolved_evidence_count: 1
  reason: unresolved_evidence
```
</details>
