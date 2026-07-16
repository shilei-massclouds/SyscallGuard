# Syscall 合规性规则提取报告

## 结论

本次分析了 renameat、renameat2、request_key、rmdir、rt_sigaction、rt_sigprocmask、rt_sigqueueinfo、rt_sigsuspend、rt_sigtimedwait、rt_tgsigqueueinfo、sbrk、sched_get_priority_max、sched_get_priority_min、sched_getaffinity、sched_getattr、sched_getparam、sched_getscheduler、sched_rr_get_interval、sched_setaffinity、sched_setattr、sched_setparam、sched_setscheduler、sched_yield、seccomp、select、send、sendfile、sendmmsg、sendmsg、sendto、set_mempolicy、set_robust_list、set_thread_area、set_tid_address、setdomainname、setegid、setfsgid、setfsuid、setgid、setgroups、sethostname、setitimer、setns、setpgid、setpgrp、setpriority、setregid、setresgid、setresuid、setreuid、setrlimit、setsid、setsockopt、settimeofday、setuid、setxattr、sgetmask、shutdown、sigaction、sigaltstack、sighold、signal、signalfd、signalfd4、sigpending、sigprocmask、sigrelse、sigsuspend、sigtimedwait、sigwait、sigwaitinfo、socket、socketcall、socketpair、sockioctl、splice、ssetmask、stat、statfs、statmount，发现 120 条可执行的合规性规则。

## `renameat`

没有形成可发布的合规性规则。

## `renameat2`

没有形成可发布的合规性规则。

## `request_key`

共形成 10 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_06F742EF42AA55BA`](../../library/rules/ltp-06f742ef42aa55ba.yaml) | 无额外前置条件 | 调用 request_key(".type", "description", NULL, KEY_SPEC_PROCESS_KEYRING) | 返回 -1，errno 为 EPERM |
| [`LTP_0A819CDD66F1C6A1`](../../library/rules/ltp-0a819cdd66f1c6a1.yaml) | 无额外前置条件 | 调用 request_key("keyring", "ltp1", NULL, key1) | 返回 -1，errno 为 ENOKEY |
| [`LTP_1BDC4A832DB89410`](../../library/rules/ltp-1bdc4a832db89410.yaml) | 无额外前置条件 | 调用 request_key("user", "desc", "callout_info", 0) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_47651AB878EBD24C`](../../library/rules/ltp-47651ab878ebd24c.yaml) | 文件描述符无效、BAD_USER_ADDRESS | 调用 request_key("type", "description", (char *)(-1), KEY_SPEC_PROCESS_KEYRING) | 返回 -1，errno 为 EFAULT |
| [`LTP_74C566A603515252`](../../library/rules/ltp-74c566a603515252.yaml) | 文件描述符无效、BAD_USER_ADDRESS | 调用 request_key("type", (char *)(-1), NULL, KEY_SPEC_PROCESS_KEYRING) | 返回 -1，errno 为 EFAULT |
| [`LTP_758C3967C160AA8E`](../../library/rules/ltp-758c3967c160aa8e.yaml) | 文件描述符无效、BAD_USER_ADDRESS | 调用 request_key((char *)(-1), "description", NULL, KEY_SPEC_PROCESS_KEYRING) | 返回 -1，errno 为 EFAULT |
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
| [`LTP_03083D6A95333E23`](../../library/rules/ltp-03083d6a95333e23.yaml) | BAD_USER_ADDRESS | 调用 rt_sigprocmask(SIG_BLOCK, &s, (sigset_t *) - 1, SIGSETSIZE) | 返回 0，errno 为 EFAULT |
| [`LTP_423E92D9328C2A39`](../../library/rules/ltp-423e92d9328c2a39.yaml) | 无额外前置条件 | 调用 rt_sigprocmask(SIG_UNBLOCK, &set, &oset, SIGSETSIZE) | {'kind': 'return_value', 'return': '-1'} |
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

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_2CB0A10A3E175A9C`](../../library/rules/ltp-2cb0a10a3e175a9c.yaml) | 无额外前置条件 | 调用 sched_getaffinity(0, len, mask) | 返回 -1，errno 为 EINVAL |
| [`LTP_5145972CC10FF773`](../../library/rules/ltp-5145972cc10ff773.yaml) | 无额外前置条件 | 调用 sched_getaffinity(pid, cpusize, mask) | 返回 -1，errno 为 exp_errno |
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
| [`LTP_585CC852338F38EE`](../../library/rules/ltp-585cc852338f38ee.yaml) | 无额外前置条件 | 调用 sched_setaffinity(self_pid, emask_size, emask) | 返回 -1，errno 为 EINVAL |
| [`LTP_97D64C0E53AA3FA4`](../../library/rules/ltp-97d64c0e53aa3fa4.yaml) | 无额外前置条件 | 调用 sched_setaffinity(free_pid, mask_size, mask) | 返回 -1，errno 为 ESRCH |
| [`LTP_D23BA34DB5624198`](../../library/rules/ltp-d23ba34db5624198.yaml) | 无额外前置条件 | 调用 sched_setaffinity(privileged_pid, mask_size, mask) | 返回 -1，errno 为 EPERM |
| [`LTP_D7C638B9DFF7DBC3`](../../library/rules/ltp-d7c638b9dff7dbc3.yaml) | BAD_USER_ADDRESS | 调用 sched_setaffinity(self_pid, mask_size, fmask) | 返回 -1，errno 为 EFAULT |
## `sched_setattr`

共形成 4 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_4BA2A081C3EB3304`](../../library/rules/ltp-4ba2a081c3eb3304.yaml) | 无额外前置条件 | 调用 sched_setattr(pid, &attr, 1000) | 返回 -1，errno 为 EINVAL |
| [`LTP_A55106AB533523B0`](../../library/rules/ltp-a55106ab533523b0.yaml) | 无额外前置条件 | 调用 sched_setattr(pid, NULL, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_B10A19D425C6416F`](../../library/rules/ltp-b10a19d425c6416f.yaml) | 无额外前置条件 | 调用 sched_setattr(pid, &attr, 0) | 返回 0，errno 为 0 |
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
| [`LTP_A49B95E01ADFC6F8`](../../library/rules/ltp-a49b95e01adfc6f8.yaml) | 无额外前置条件 | 调用 sendfile(out_fd, in_fd, NULL, sb.st_size) | {'kind': 'return_value', 'return': 'st_size'} |
| [`LTP_A54F3585CC70C99F`](../../library/rules/ltp-a54f3585cc70c99f.yaml) | 无额外前置条件 | 调用 sendfile(out_fd, in_fd, &offset, 26) | {'kind': 'return_value', 'return': '26'} |
| [`LTP_C8536F49779345AA`](../../library/rules/ltp-c8536f49779345aa.yaml) | BAD_USER_ADDRESS | 调用 sendfile(out_fd, in_fd, protected_buffer, 1) | 返回 -1，errno 为 EFAULT |
| [`LTP_CB84D44C84EB80BE`](../../library/rules/ltp-cb84d44c84eb80be.yaml) | 无额外前置条件 | 调用 sendfile(out_fd, in_fd, NULL, 1) | 返回 -1，errno 为 EAGAIN |
| [`LTP_D01667E52BF34BFC`](../../library/rules/ltp-d01667e52bf34bfc.yaml) | 无额外前置条件 | 调用 sendfile(in_fd, in_fd, NULL, 1) | 返回 -1，errno 为 EBADF |
| [`LTP_D3E85F64C28BBC4F`](../../library/rules/ltp-d3e85f64c28bbc4f.yaml) | 无额外前置条件 | 调用 sendfile(out_fd, in_fd, &offset, 24) | {'kind': 'return_value', 'return': '26'} |
## `sendmmsg`

没有形成可发布的合规性规则。

## `sendmsg`

共形成 11 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_065F7F29AD356B3E`](../../library/rules/ltp-065f7f29ad356b3e.yaml) | BAD_USER_ADDRESS | 调用 sendmsg(s, &msgdat, 0) | 返回 0，errno 为 EFAULT |
| [`LTP_0E5462C27210C85F`](../../library/rules/ltp-0e5462c27210c85f.yaml) | 无额外前置条件 | 调用 sendmsg(s, &msgdat, MSG_OOB) | 返回 -1，errno 为 EOPNOTSUPP |
| [`LTP_3B0C2A3A034B17ED`](../../library/rules/ltp-3b0c2a3a034b17ed.yaml) | 无额外前置条件 | 调用 sendmsg(s, &msgdat, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_46A3B23FBDECBAD4`](../../library/rules/ltp-46a3b23fbdecbad4.yaml) | 无额外前置条件 | 调用 sendmsg(s, &msgdat, 0) | 返回 -1，errno 为 EMSGSIZE |
| [`LTP_481898C7C2C1FF1D`](../../library/rules/ltp-481898c7c2c1ff1d.yaml) | 无额外前置条件 | 调用 sendmsg(s, &msgdat, 0) | 返回 -1，errno 为 EPIPE |
| [`LTP_7B85651B66F35DBD`](../../library/rules/ltp-7b85651b66f35dbd.yaml) | 无额外前置条件 | 调用 sendmsg(s, &msgdat, 0) | 返回 -1，errno 为 ENOTSOCK |
| [`LTP_A2098D60C40310A2`](../../library/rules/ltp-a2098d60c40310a2.yaml) | BAD_USER_ADDRESS | 调用 sendmsg(s, NULL, 0) | 返回 -1，errno 为 EFAULT |
| [`LTP_A4DD0508E65CC9FB`](../../library/rules/ltp-a4dd0508e65cc9fb.yaml) | 无额外前置条件 | 调用 sendmsg(s, &msgdat, 0) | 返回 0，errno 为 0 |
| [`LTP_A9B80928550B9520`](../../library/rules/ltp-a9b80928550b9520.yaml) | 无额外前置条件 | 调用 sendmsg(s, &msgdat, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_D9561EEACFF72902`](../../library/rules/ltp-d9561eeacff72902.yaml) | 无额外前置条件 | 调用 sendmsg(s, &msgdat, 0) | 返回 0，errno 为 EOPNOTSUPP |
| [`LTP_F2C1952707BEC602`](../../library/rules/ltp-f2c1952707bec602.yaml) | BAD_USER_ADDRESS | 调用 sendmsg(s, &msgdat, 0) | 返回 -1，errno 为 EFAULT |
## `sendto`

共形成 10 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0069B2BDFC11BD6E`](../../library/rules/ltp-0069b2bdfc11bd6e.yaml) | BAD_USER_ADDRESS | 调用 sendto(sockfd, NULL, 1, 0, (struct sockaddr *) &sa, sizeof(sa)) | 返回 -1，errno 为 EFAULT |
| [`LTP_1507C71C3D1DF6E5`](../../library/rules/ltp-1507c71c3d1df6e5.yaml) | BAD_USER_ADDRESS、USER_BUFFER | 调用 sendto(s, (void *)-1, sizeof(buf), 0, (const struct sockaddr *)&sin1, sizeof(sin1)) | 返回 -1，errno 为 EFAULT |
| [`LTP_2C2A7A0BCB72A2EB`](../../library/rules/ltp-2c2a7a0bcb72a2eb.yaml) | BAD_USER_ADDRESS、USER_BUFFER | 调用 sendto(s, buf, sizeof(buf), 0, (const struct sockaddr *)&sin2, sizeof(sin2)) | 返回 0，errno 为 EFAULT |
| [`LTP_2D65D505344282C8`](../../library/rules/ltp-2d65d505344282c8.yaml) | USER_BUFFER | 调用 sendto(s, buf, sizeof(buf), 0, (const struct sockaddr *)&sin1, sizeof(sin1)) | 返回 -1，errno 为 ENOTSOCK |
| [`LTP_40ABB27673C9DE62`](../../library/rules/ltp-40abb27673c9de62.yaml) | 无额外前置条件 | 调用 sendto(s, bigbuf, sizeof(bigbuf), 0, (const struct sockaddr *)&sin1, sizeof(sin1)) | 返回 -1，errno 为 EMSGSIZE |
| [`LTP_49A11FBBFB010278`](../../library/rules/ltp-49a11fbbfb010278.yaml) | USER_BUFFER | 调用 sendto(s, buf, sizeof(buf), MSG_OOB, (const struct sockaddr *)&sin1, sizeof(sin1)) | 返回 -1，errno 为 EOPNOTSUPP |
| [`LTP_ABFA54B9CA53F29E`](../../library/rules/ltp-abfa54b9ca53f29e.yaml) | USER_BUFFER | 调用 sendto(s, buf, sizeof(buf), 0, (const struct sockaddr *)&sin1, sizeof(sin1)) | 返回 -1，errno 为 EPIPE |
| [`LTP_AFD4E9B4327B6D40`](../../library/rules/ltp-afd4e9b4327b6d40.yaml) | USER_BUFFER | 调用 sendto(s, buf, sizeof(buf), 0, (const struct sockaddr *)&sin1, sizeof(sin1)) | 返回 -1，errno 为 EBADF |
| [`LTP_BA0600CDE607FB7A`](../../library/rules/ltp-ba0600cde607fb7a.yaml) | 文件描述符无效、USER_BUFFER | 调用 sendto(s, buf, sizeof(buf), 0, (const struct sockaddr *)&sin1, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_C86E220567585ADC`](../../library/rules/ltp-c86e220567585adc.yaml) | BAD_USER_ADDRESS、USER_BUFFER | 调用 sendto(s, buf, sizeof(buf), 0, (const struct sockaddr *)(struct sockaddr_in *)-1, sizeof(sin1)) | 返回 -1，errno 为 EFAULT |
## `set_mempolicy`

没有形成可发布的合规性规则。

## `set_robust_list`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_40024D6BE4C6AECC`](../../library/rules/ltp-40024d6be4c6aecc.yaml) | 文件描述符无效 | 调用 set_robust_list(&head, -1) | 返回 -1，errno 为 EINVAL |
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
| [`LTP_3249413C9BA64960`](../../library/rules/ltp-3249413c9ba64960.yaml) | PERMISSION_DENIED_STATE | 调用 setpgid(child_pid, getppid()) | 返回 -1，errno 为 EACCES |
| [`LTP_4308D71D8BD6519D`](../../library/rules/ltp-4308d71d8bd6519d.yaml) | 无额外前置条件 | 调用 setpgid(pid, negative_pid) | 返回 -1，errno 为 EINVAL |
| [`LTP_4BBF626715445EFC`](../../library/rules/ltp-4bbf626715445efc.yaml) | 无额外前置条件 | 调用 setpgid(ppid, pgid) | 返回 -1，errno 为 ESRCH |
| [`LTP_503160311D12E629`](../../library/rules/ltp-503160311d12e629.yaml) | 无额外前置条件 | 调用 setpgid(pid, pgid) | 调用成功，返回 SUCCESS |
| [`LTP_9FC19C1455EBA67E`](../../library/rules/ltp-9fc19c1455eba67e.yaml) | 无额外前置条件 | 调用 setpgid(0, child_pid) | 返回 -1，errno 为 EPERM |
| [`LTP_CF7B49C4B74D69E7`](../../library/rules/ltp-cf7b49c4b74d69e7.yaml) | 无额外前置条件 | 调用 setpgid(pid, inval_pgid) | 返回 -1，errno 为 EPERM |
| [`LTP_DBEC3975C5440D23`](../../library/rules/ltp-dbec3975c5440d23.yaml) | 无额外前置条件 | 调用 setpgid(child_pid, getppid()) | 返回 -1，errno 为 EPERM |
## `setpgrp`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_09377FE11AF44E16`](../../library/rules/ltp-09377fe11af44e16.yaml) | 无额外前置条件 | 调用 setpgrp() | 调用成功，返回 SUCCESS |
| [`LTP_106D7242AECD4D33`](../../library/rules/ltp-106d7242aecd4d33.yaml) | 无额外前置条件 | 调用 setpgrp() | {'kind': 'return_value', 'return': '0'} |
## `setpriority`

共形成 10 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_252DC2EE1F2FC3AC`](../../library/rules/ltp-252dc2ee1f2fc3ac.yaml) | 无额外前置条件 | 调用 setpriority(PRIO_USER, INVAL_ID, NEW_PRIO) | 返回 -1，errno 为 ESRCH |
| [`LTP_336B0AA063AB645E`](../../library/rules/ltp-336b0aa063ab645e.yaml) | 无额外前置条件 | 调用 setpriority(PRIO_USER, uid, new_prio) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_44DC5382746D773D`](../../library/rules/ltp-44dc5382746d773d.yaml) | 无额外前置条件 | 调用 setpriority(INVAL_FLAG, 0, NEW_PRIO) | 返回 -1，errno 为 EINVAL |
| [`LTP_4DB863CC12B75471`](../../library/rules/ltp-4db863cc12b75471.yaml) | PERMISSION_DENIED_STATE | 调用 setpriority(PRIO_PROCESS, 0, NEW_PRIO) | 返回 -1，errno 为 EACCES |
| [`LTP_50853944DA25B2E0`](../../library/rules/ltp-50853944da25b2e0.yaml) | 无额外前置条件 | 调用 setpriority(PRIO_PGRP, INVAL_ID, NEW_PRIO) | 返回 -1，errno 为 ESRCH |
| [`LTP_757778388A97EE03`](../../library/rules/ltp-757778388a97ee03.yaml) | 无额外前置条件 | 调用 setpriority(PRIO_PROCESS, pid, new_prio) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_9A462447EA8872E9`](../../library/rules/ltp-9a462447ea8872e9.yaml) | PERMISSION_DENIED_STATE | 调用 setpriority(PRIO_PGRP, 0, NEW_PRIO) | 返回 -1，errno 为 EACCES |
| [`LTP_9D4E5ED344B5751D`](../../library/rules/ltp-9d4e5ed344b5751d.yaml) | 无额外前置条件 | 调用 setpriority(PRIO_PROCESS, INIT_PID, NEW_PRIO) | 返回 -1，errno 为 EPERM |
| [`LTP_AF52DA4E6DA2BC9B`](../../library/rules/ltp-af52da4e6da2bc9b.yaml) | 无额外前置条件 | 调用 setpriority(PRIO_PROCESS, INVAL_ID, NEW_PRIO) | 返回 -1，errno 为 ESRCH |
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

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_470EA842B2582537`](../../library/rules/ltp-470ea842b2582537.yaml) | 无额外前置条件 | 调用 sigaltstack(&sigstk, NULL) | 返回 -1，errno 为 ENOMEM |
| [`LTP_4D86B6394424B16C`](../../library/rules/ltp-4d86b6394424b16c.yaml) | 无额外前置条件 | 调用 sigaltstack(&sigstk, NULL) | 返回 -1，errno 为 EINVAL |
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
| [`LTP_2C867F470A477D29`](../../library/rules/ltp-2c867f470a477d29.yaml) | 文件描述符无效 | 调用 signalfd(fd_einval2, mask, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_644B7DB483FF489B`](../../library/rules/ltp-644b7db483ff489b.yaml) | 无额外前置条件 | 调用 signalfd(fd_signal, &mask2, 0) | {'kind': 'return_fd', 'return': 'FD'} |
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
| [`LTP_6366A1114F49C2CF`](../../library/rules/ltp-6366a1114f49c2cf.yaml) | BAD_USER_ADDRESS | 调用 sigsuspend(invalid_mask) | 返回 -1，errno 为 EFAULT |
## `sigtimedwait`

没有形成可发布的合规性规则。

## `sigwait`

没有形成可发布的合规性规则。

## `sigwaitinfo`

没有形成可发布的合规性规则。

## `socket`

共形成 9 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_6B29B31CE99466E6`](../../library/rules/ltp-6b29b31ce99466e6.yaml) | 无额外前置条件 | 调用 socket(PF_INET, SOCK_DGRAM, 6) | 返回 -1，errno 为 EPROTONOSUPPORT |
| [`LTP_73330FC2133223F4`](../../library/rules/ltp-73330fc2133223f4.yaml) | 无额外前置条件 | 调用 socket(PF_INET, SOCK_STREAM, 6) | 返回 0，errno 为 0 |
| [`LTP_971DB17D32C51561`](../../library/rules/ltp-971db17d32c51561.yaml) | 无额外前置条件 | 调用 socket(PF_INET, 75, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_A4A662687B98D33F`](../../library/rules/ltp-a4a662687b98d33f.yaml) | 无额外前置条件 | 调用 socket(PF_INET, SOCK_STREAM, 1) | 返回 -1，errno 为 EPROTONOSUPPORT |
| [`LTP_AF8D38878ED1A9DA`](../../library/rules/ltp-af8d38878ed1a9da.yaml) | 无额外前置条件 | 调用 socket(0, SOCK_STREAM, 0) | 返回 -1，errno 为 EAFNOSUPPORT |
| [`LTP_C3098F5341F14B0E`](../../library/rules/ltp-c3098f5341f14b0e.yaml) | 无额外前置条件 | 调用 socket(PF_INET, SOCK_DGRAM, 17) | 返回 0，errno 为 0 |
| [`LTP_DD2E1A555B603C7B`](../../library/rules/ltp-dd2e1a555b603c7b.yaml) | 无额外前置条件 | 调用 socket(PF_INET, SOCK_STREAM, 17) | 返回 -1，errno 为 EPROTONOSUPPORT |
| [`LTP_DF9A0B3ADAC6AE1D`](../../library/rules/ltp-df9a0b3adac6ae1d.yaml) | 无额外前置条件 | 调用 socket(PF_UNIX, SOCK_DGRAM, 0) | 返回 0，errno 为 0 |
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


## 技术参考

- 报告 ID：`spec-20260716t051423z-168822db`
- 来源：`ltp-local`，内容快照 `sha256:d789747f0c0bf1697f538bc5166073fd8449dec3beac7b12ac0be0b1b716dcb4`
- 全局待处理 syscall：133
- 提取数量：`80`（来源：`command`）
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

<details>
<summary>机器可读元数据</summary>

<!-- syscallguard-metadata -->
```yaml
schema_version: 1
kind: syscallguard_ingest_report
report_id: spec-20260716t051423z-168822db
generated_at_utc: '2026-07-16T05:14:25.198516Z'
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
pending_count: 133
selected_syscalls:
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
syscalls:
- syscall: renameat
  source_fingerprint: sha256:b484089690ef319dbb36525f1b918fdb6aa65ffbbdde21ec15f189f4ce645634
  recognition_fingerprint: sha256:79a214cde88114b6aca9407af310c60c445ecc8ed8b05288ec9ce87d2743c357
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: renameat2
  source_fingerprint: sha256:80c20d8d5c7533d80f6bedbc88fadabd566d09bd1c1f4210702e817efd58925e
  recognition_fingerprint: sha256:27ef7481e51a6392bd54ab94b2e6de5ed0f46d90e5e111c07565bf48f803569d
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: request_key
  source_fingerprint: sha256:423ef46d2ddcb4c7dc376b492da7da381104b81445989fe5f4cc49d9ebc72212
  recognition_fingerprint: sha256:ee24ee6fd972e21f6bd48533b7b0020979ecda97f3e7895ab4feee11fff3c1e4
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_06F742EF42AA55BA
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:06f742ef42aa55bab6e782e69edc9803705766d67aa9eab75909bf02683ba29d
  - id: LTP_0A819CDD66F1C6A1
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:0a819cdd66f1c6a12eb3269542bb8543b1e76e4d0c775c6417886121ff53622d
  - id: LTP_1BDC4A832DB89410
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:1bdc4a832db89410164e6f7da6fcd6ddc57cede4911699439f09a8694f934668
  - id: LTP_47651AB878EBD24C
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:47651ab878ebd24c60f33fb8af813c0c6107e3b904af9513ae56bdfd7ddcf17a
  - id: LTP_74C566A603515252
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:74c566a60351525232875060cd59060fd5b624fa0320b19fcd33dad62b2e0e15
  - id: LTP_758C3967C160AA8E
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:758c3967c160aa8e30e6bec474c6b3f89144ebd24b535138f4ee71ffc615eda3
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
  recognition_fingerprint: sha256:768f59c03676417f18ac117a89bd677d36ff5e92cd66d64c3b4e3d0503963fe2
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: rt_sigaction
  source_fingerprint: sha256:c50270d79fbd34dafc9956cd3d37c756fc1dfa8b9ba10dc5ddcf9dc71148690e
  recognition_fingerprint: sha256:928b3ae3a83ec335dc08c9c352a5c13837044761197b636da8edab269b53e871
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: rt_sigprocmask
  source_fingerprint: sha256:b83a8d936051efdb0e621d9b10d698836ba3c3de6464391928411e5e3875decf
  recognition_fingerprint: sha256:4452e89acd1bf851dd72385a815c4266823ec16460c90bb36a6f7b7d3357542c
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_03083D6A95333E23
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:03083d6a95333e23dcb3b559e0c43356ab763bf13601397d50fa60fdb63541cb
  - id: LTP_423E92D9328C2A39
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:423e92d9328c2a39012f36f1101818dcc226c890746fe3e26c17d4cb2ed59755
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
  recognition_fingerprint: sha256:9b16c469189fa5806c900c1dd56a5d72d9be1be5817c6722854975a41773a1b3
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: rt_sigsuspend
  source_fingerprint: sha256:a339509f05d7a63fdd52c69210e4db823d24f54b13b54dea48f7ebada12afd5e
  recognition_fingerprint: sha256:7ac75deea737295b431485a5a6826fe92435d0033b6b2694eca38833b7fdd7b4
  selection_reason: new
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
  recognition_fingerprint: sha256:fc67e4eabcc0738402d767bd5d0ba8273b45e67d616e2885edbb1cb45d6d37d9
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: rt_tgsigqueueinfo
  source_fingerprint: sha256:b099f0ad3378f4d43747f19b57dbaaf1a99187ffce03f4d1c76d1ff8acd1256a
  recognition_fingerprint: sha256:5a5dcd190ebb9a099c7d9930177bbef7e78a52b9b264544f3cd39822e9d9f446
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 3
  reason: unresolved_evidence
- syscall: sbrk
  source_fingerprint: sha256:a657a5609d22f7e93b24dab38ecb20d678bca1e08042704fd1b172885f0c4eef
  recognition_fingerprint: sha256:25944f1e06ef8f050bae41e05d8a4f6f6dcf18903c16bc042d7039f3a5b99177
  selection_reason: new
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
  recognition_fingerprint: sha256:f4eeaf2588faaed7d5543d59e88068eb615a5e0a036c90b0172df8ef2f0a3343
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sched_get_priority_min
  source_fingerprint: sha256:a01e6acad5a122ae399ccefff2d13ddb3ec659cf667a61066dc859befd1b76c2
  recognition_fingerprint: sha256:234a30de215fc0c323bdc2521e9adcb2a9a15dee795ff17fcd46a4e32e15310f
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sched_getaffinity
  source_fingerprint: sha256:b96ec72b029dfe9b38cb175c66fdc1cfb98dd63bdcabd5a0fe6e1f775837656e
  recognition_fingerprint: sha256:82c2cb1e9545cb234677989acf21f371b9c550b324aa802e1366ab44a7478574
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_2CB0A10A3E175A9C
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:2cb0a10a3e175a9cf9ff374ed3cc5c0852bfbbf32ac3162a5be800ff85f22431
  - id: LTP_5145972CC10FF773
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:5145972cc10ff7739a0a8a3ff407c7dbc75c53fa0fb9c91bf1acab51dd05254b
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: sched_getattr
  source_fingerprint: sha256:67317d0c3d987d58067abb4d64cb8c68387cbf2a6347b4965c1e583344578074
  recognition_fingerprint: sha256:3c966c32eb2c62c0d0ddeffe5a0584288269bcfa8fecba32ddfe0cdbf51b9031
  selection_reason: new
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
  recognition_fingerprint: sha256:01ae7e00edbfebf4d622495022e4c16d86089b27572b04c064cccf76c8667202
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sched_getscheduler
  source_fingerprint: sha256:c8254738a8f08e3fd23b2747aafe7b5a00640f906b3a39e65307453c365a3ea9
  recognition_fingerprint: sha256:0b5135f2764b0838fb6078372da69711fcdd247416f442ef223ba2f486d1a9f2
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: sched_rr_get_interval
  source_fingerprint: sha256:48e813078669c86660a656a4d433f98aa33878f3ae859683a2ae1bb38f6ca12e
  recognition_fingerprint: sha256:85bf5fe4f49fc599ca4756cf4e2aef72929f93702612c7ded568932f49057539
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sched_setaffinity
  source_fingerprint: sha256:d737035b7fdbedc650f60b52a75be3be2b4fdcf8ad96935e7881cae77d9e7b72
  recognition_fingerprint: sha256:e1ef98e4ac7170242f61150805938f7788d7471494d63e375cc5f6f9b66c6cb3
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_585CC852338F38EE
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:585cc852338f38eedc86755b62d33a8eb443200486dd86bb3f79a4a4df80981c
  - id: LTP_97D64C0E53AA3FA4
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:97d64c0e53aa3fa43ac9171f931907f3c9649f7e1b1ea369f6bacf092a2a959a
  - id: LTP_D23BA34DB5624198
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:d23ba34db562419826707b44be08745b2172749f85b9825dde0d54eb3487dcc0
  - id: LTP_D7C638B9DFF7DBC3
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:d7c638b9dff7dbc39fe5df57a4ae8b6951d7c05218ed89e15d0e3e15710f4a7c
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: sched_setattr
  source_fingerprint: sha256:db3edc0354ec5f09f9eaa98d5f481dcea2d5c9a9869c04c0429b337db1b6dc64
  recognition_fingerprint: sha256:de157c360615a91e981068abee4a9be7a95f5ad8fde04433d08cb6c290bc9d4f
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_4BA2A081C3EB3304
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:4ba2a081c3eb3304d69e4bd78e8f04758f3b4e119a33f827665c905bda26ee79
  - id: LTP_A55106AB533523B0
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:a55106ab533523b02256e2c636ad09c3a0a42d580d1a647f65c5a5ebd97fdb09
  - id: LTP_B10A19D425C6416F
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:b10a19d425c6416f8bdd6cc2e2868bd2c4347d36d6f7a576702c96c6cfd97b02
  - id: LTP_DC7E9134BB7F6F7A
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:dc7e9134bb7f6f7af3b18b3a23151e111f9ffe9edd6e5e5d94b4c4571c543647
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: sched_setparam
  source_fingerprint: sha256:52e940c0faeeef0e75d1ccbad9eb3aa090c3f07836f162a08270d63bf3f22be9
  recognition_fingerprint: sha256:03f157667776b7174a7cf935e07995204f782bbd6c220e1402e25c8d8de737bd
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sched_setscheduler
  source_fingerprint: sha256:3455609ffc6fa3aa961382e4885780b95a9e2d003b16a36968eb59f4a4408c3b
  recognition_fingerprint: sha256:df561dd3d950c5083b9cda09080bd11d390555c75f930cabdb9ec99e55392f21
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: sched_yield
  source_fingerprint: sha256:e21368050e5aa9a67f8ab3907eec08e67a261a4283ebfe3113d35fa0295e355e
  recognition_fingerprint: sha256:37a09663aff6f727ab71ca6a943434a5cc3dc480c80bac5baa976e6f92fefcfa
  selection_reason: new
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
  recognition_fingerprint: sha256:d1e4d8f52b2516017fe8b4a18905f3955f403f67e97f1be8e39f9b50d19d69d8
  selection_reason: new
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
  recognition_fingerprint: sha256:460d18f015bfdd777c6f363bfd6035172e5b8d4bd6febb5cd0f33d1803aed56e
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 8
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: send
  source_fingerprint: sha256:8efdc6a6250a706884a935b02fab565cd3f6bc2c3a2171e19514971b57346f69
  recognition_fingerprint: sha256:2901a92a60414619d66f8c815fa63ac8909421c9839d3770a2295dbbc6cb61f6
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sendfile
  source_fingerprint: sha256:3da9f393c15cafd6674bc2e14dbafc2dec733b7f672cecf14487c37badd11c21
  recognition_fingerprint: sha256:2a92c6f1c21faf7130a9048ffa7b65585813b409f7204f74b632f6fec1691894
  selection_reason: new
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
  - id: LTP_A49B95E01ADFC6F8
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:a49b95e01adfc6f8a2365988a715f341e4f31172445c6e2e557162d64117bd31
  - id: LTP_A54F3585CC70C99F
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:a54f3585cc70c99f0f720a09c619ee917a07d13b34551316dd85e7595781da0c
  - id: LTP_C8536F49779345AA
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:c8536f49779345aaca6b3672cea8de30e836aafaabcd8bfdeb6c149dff8a6810
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
  recognition_fingerprint: sha256:916ac366826c26eb636048293ba214b5e9a9cedc812c9affaac0ed2e2f661494
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sendmsg
  source_fingerprint: sha256:1fe9a9f51a1e5aa81e3bd29559b8848e42d4292aa2747f0cdff84ede66da07cc
  recognition_fingerprint: sha256:b33c0e94073f88840f65daf93d76807b1a6cd656b1c8027a5c9b1f087aa492af
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_065F7F29AD356B3E
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:065f7f29ad356b3e78f74dc65b3a00f92b4ae4ce0f9a3e0877996194054dcbf0
  - id: LTP_0E5462C27210C85F
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:0e5462c27210c85f9377d36f01a2b0992e79f68f388251e25565c8f8e6a81b5a
  - id: LTP_3B0C2A3A034B17ED
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:3b0c2a3a034b17ed88a04cafe8ea71559ef6c3059bcdd1e428246a9e1555f72d
  - id: LTP_46A3B23FBDECBAD4
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:46a3b23fbdecbad41e5b717c9adde3dd4d10c5572a120d8ee58240c9c0f7f459
  - id: LTP_481898C7C2C1FF1D
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:481898c7c2c1ff1d10da1f147e0567d1295776ed171e186602739a371813d4c1
  - id: LTP_7B85651B66F35DBD
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:7b85651b66f35dbd442f5ebec077096e94f8c00e628a61758c597a7606e51347
  - id: LTP_A2098D60C40310A2
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:a2098d60c40310a201cf1ee9258fa49ff832fae788c0f99896d048e0cd323d61
  - id: LTP_A4DD0508E65CC9FB
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:a4dd0508e65cc9fba3e2d49e5500810b604b5f0314ed6ac9e8066478c5d3fcd7
  - id: LTP_A9B80928550B9520
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:a9b80928550b9520608ae089b3d79c19128ba2efe900aa442ebe822b5b00034b
  - id: LTP_D9561EEACFF72902
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:d9561eeacff729029e6227205d2175826cf0d3ac863e7cf26b718be05c3b1d13
  - id: LTP_F2C1952707BEC602
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:f2c1952707bec6025f0985bec64c541d14da594602cd195001a297936870ba96
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: sendto
  source_fingerprint: sha256:3ca942e4d62a193e12ecd48ee2209df021850bc72dac643ccb9cd01c7b7c31c6
  recognition_fingerprint: sha256:1a39db68720a2b5d0ffa87f20dc89bb006c41d86555c581cff87d58d11a979bd
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_0069B2BDFC11BD6E
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:0069b2bdfc11bd6e25b830e73c792acbb1ca4c4d9d9f22e922ab8f29f7983555
  - id: LTP_1507C71C3D1DF6E5
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:1507c71c3d1df6e5c1080edfd42e1b3d72fde977f442adc9977ba43c7c8431da
  - id: LTP_2C2A7A0BCB72A2EB
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:2c2a7a0bcb72a2eb31062477392c15029a5e864eaa3f93750c800d0cde11a1af
  - id: LTP_2D65D505344282C8
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:2d65d505344282c8780f4f8b4c0e0b507c5727dcd97b6539bcb0cf7735f73157
  - id: LTP_40ABB27673C9DE62
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:40abb27673c9de621a649c640044b692934433c3356e8fae6d0eabc87d14de36
  - id: LTP_49A11FBBFB010278
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:49a11fbbfb010278e64e9a4d6583740cbb77708f4951aab2c1f7236c5645bc80
  - id: LTP_ABFA54B9CA53F29E
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:abfa54b9ca53f29e38a947193b20964635b8afd640036b58d81b427a5bfbdbee
  - id: LTP_AFD4E9B4327B6D40
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:afd4e9b4327b6d408fbe3b3f82dba779d5e8ad6364e77dca4a508b6d2e962f22
  - id: LTP_BA0600CDE607FB7A
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:ba0600cde607fb7a42d55f0fa6f546e59cb2e12b86d4112d78a6318aa62029fb
  - id: LTP_C86E220567585ADC
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:c86e220567585adcf877bf5551031ee4fa0025622e221864b8e6fe13e0ad809a
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: set_mempolicy
  source_fingerprint: sha256:c84a754ba0728ce99fa638d21b484589230d768d9c4df4acb6f2c364bac3335f
  recognition_fingerprint: sha256:767ce738fb52d25fe7d6a171257cc563cfcf3afce864a10af4b2d530203e8111
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 4
  reason: unresolved_evidence
- syscall: set_robust_list
  source_fingerprint: sha256:b4323495cd9cd2021458522b01aeaeb838dc5a256c2a8a77aa7d35c0ea4d3d9e
  recognition_fingerprint: sha256:4cdddd7bdaf2ace2f4d705c2838434fd41b042164005707f429a8895508590b1
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_40024D6BE4C6AECC
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:40024d6be4c6aecc25eec2daf4ec64294dfce4200606f41b586028d4ee8360c1
  - id: LTP_E0470C189C2D1DE3
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:e0470c189c2d1de37f10ab6be898fcfa26ff828dc89057c84d3ddaf504ab41bd
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: set_thread_area
  source_fingerprint: sha256:8a89a8930681d133e846f0fada73ed5166734e456d7baedc29b253d0cad22db0
  recognition_fingerprint: sha256:75d32de264a3a12bc2e73f8051d359731087d45cb3eb7ded734d44dc7359e138
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: set_tid_address
  source_fingerprint: sha256:25e1295de2df4bb2b9561a60dd18e424694a6df5434e94891576166450ed965e
  recognition_fingerprint: sha256:c78b1285440a204c68df9b33259a9390b00c445dc4f4b97f88c545b159c8b656
  selection_reason: new
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
  recognition_fingerprint: sha256:ff72f64637bb43a7d6ba4ba47b43206f7bc04a629a86b6826fa39c35e4249e11
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: setegid
  source_fingerprint: sha256:7a43d7eea77c2ed5b3093777eb56d56cc816e7f37cce1128cc9d776a4c07aa3a
  recognition_fingerprint: sha256:726531b542da2d0091e98c1c3702757e53c72f9d2512dccf4726a4fab8b791f1
  selection_reason: new
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
  recognition_fingerprint: sha256:eb2bc431df85d247f656edc1ba36d8432d9bea7e19f95fb60010e9bac11681eb
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: setfsuid
  source_fingerprint: sha256:0776bbcc2b66f237e85febeeaf742374979e029a16bd9e4bf73afc76cc4b43e9
  recognition_fingerprint: sha256:c85755a90872e916c5457662563a7e6210ea35aa3a99fc8008dfbe1187b6d412
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: setgid
  source_fingerprint: sha256:29246deb879c1a61fd41b72dfe7d2a5700b29af1a1bed635f7af841dd5440ae5
  recognition_fingerprint: sha256:9a7d86b87a2e592a6edd6964a8036fee6e67e324701604db55c7b31b92a5a4a7
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: setgroups
  source_fingerprint: sha256:df25704acdc6afa12e9080045bde58e19898bf62a6eea66b24cd69be01d08f46
  recognition_fingerprint: sha256:959a12ded131a748f45714b19fa50523b1b21fa30f68d19df596b7e51503d9ab
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sethostname
  source_fingerprint: sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  recognition_fingerprint: sha256:85822a6d8b1a27d979425ba6f0fd7e43949cbb612bac34a26dbf6e48194096ca
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: setitimer
  source_fingerprint: sha256:a3aff4ee98a448c32bc9657bcd6a772fc896f40b3b5b2df63cedcd2469b623bb
  recognition_fingerprint: sha256:535ab227eed0e4b6dd77c01cd517dc9a8a091815199d8352e80be00f9f78c793
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: setns
  source_fingerprint: sha256:aa8c9d8ea256d57c99afdf36d57ed6f5503a00085d93ebad6b70ebadacb80fb7
  recognition_fingerprint: sha256:54d0ecf19fbe9d075a6a0e1962a16ec813dc4765e8cbb22d644b8a1c6b53c50e
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: setpgid
  source_fingerprint: sha256:748b15defef65b4ee2331eaf50d96bad8ec9b2d073be43202eb193748df2018a
  recognition_fingerprint: sha256:f7f2d9dee706ba457c2fa9b14eda7460bfb4a6de19fefa0a8bfe7fab720d99aa
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_0C5623B3D5C7430F
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:0c5623b3d5c7430faddca0c6166925cdc085a47fd9534b5346766354814f4715
  - id: LTP_3249413C9BA64960
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:3249413c9ba6496026f8d40bc5b1a2770110b32c0938b4e9f01b499445eeb42b
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
  recognition_fingerprint: sha256:d0d7c6a68903b172051fc525743d38dd37869d269289aebf3de7eeceb992d945
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_09377FE11AF44E16
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:09377fe11af44e166b836c58fb7e0dfd64bb41196e28d86b83c00009511a9b1a
  - id: LTP_106D7242AECD4D33
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:106d7242aecd4d330817399d402a2a3d75e2c7483206907303868fb4137c77a0
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: setpriority
  source_fingerprint: sha256:3a0740e9a4bcba576ae4df21e63c48aab6fdf902d46bc8d5ac51dd63ad023538
  recognition_fingerprint: sha256:f1a2a5df6346de38dde6befc03851097a4238f4014559ffe59b88f07deb541f0
  selection_reason: new
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
  - id: LTP_4DB863CC12B75471
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:4db863cc12b754714f471e5c0bc8f9fa89ca5b5caa1a3c82d2f0397c48372684
  - id: LTP_50853944DA25B2E0
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:50853944da25b2e0f6694eb621028eae0225c7734bee98d7bb6d1fca9a132d6c
  - id: LTP_757778388A97EE03
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:757778388a97ee0352730af9c96cf6344cec57c933fa5567a243080bf37fbfbd
  - id: LTP_9A462447EA8872E9
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:9a462447ea8872e9182915808da9971932fb317810137f587f8353a975a4f155
  - id: LTP_9D4E5ED344B5751D
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:9d4e5ed344b5751da45ffab840fe6b7986c89e70a797ee811b6456cdd77d90b1
  - id: LTP_AF52DA4E6DA2BC9B
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:af52da4e6da2bc9bc597cc4d8a0a73fc1505f8f9f7cd41f866050ae5be4cf8f0
  - id: LTP_BB4C88C7C212DAC7
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:bb4c88c7c212dac73eaf78b975894ac2ef9eff45159afdc865d90d2669e60dbc
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: setregid
  source_fingerprint: sha256:cc23f510e807771dac6b0cc03617ea20df75ab98c44f01b412b42bcecc324fe9
  recognition_fingerprint: sha256:a771138fb0ec84d33e901657b2bae0c2b0839f487260de0cbf93f466fc89e06d
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: setresgid
  source_fingerprint: sha256:a96b99c87953c88c7dd4588b81c256ed004a2348226a0fdc913584870fbd5620
  recognition_fingerprint: sha256:a9d1b7fca905dc7174542202a1c67e4bbb1d824602a39c4eccbbd6022e608d0f
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: setresuid
  source_fingerprint: sha256:3e5791352632f2edfe4a5f7a1f38ca5aea27e7215cc0ccab679f0eb9e30997f6
  recognition_fingerprint: sha256:22c2c9cb33c21c2ae7d0b5e36394befc13bfa726638c6f121cd9f2dfd7141373
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: setreuid
  source_fingerprint: sha256:6b376d89fd8dc10095619325c3bdea6d166716bf1c3d27954c0283ffe8fd5b4e
  recognition_fingerprint: sha256:1296883d2739c44a48a53e0130387593fc31e33df9c35a8417645d6d2f12391f
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 9
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: setrlimit
  source_fingerprint: sha256:3a72142383369e37b9ec7d25fc6064c023b5de3dcdbbeeab13b5a1ca90d5c06a
  recognition_fingerprint: sha256:c9fa274a83563b6ec975c5cb6a91d619e22740f61a9273c327e0c4dc470358f7
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 12
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: setsid
  source_fingerprint: sha256:aecc3b4981f0215ea6612fd6454e8bcf2f9299f1b459421d2f8625b03354295d
  recognition_fingerprint: sha256:081bc4a1ac9671166b111d48d25fe82dd5e26edd0cf1de432d790dd7f19651e8
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: setsockopt
  source_fingerprint: sha256:9f42d93b03f5250db6608914c47bacc90e79b73f7e7aa0138ed2c77c3c03bf83
  recognition_fingerprint: sha256:cf536f5b01d33fcf4f0dcec3135b97cb71841072bcec929170b2b615a57283fb
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 19
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: settimeofday
  source_fingerprint: sha256:b6bc5ffa3739661873a5ed83fb07d2a36dca66892e259ae55d5ad58a06603f5f
  recognition_fingerprint: sha256:895de2e6e3036234c4833c376ec33238d705384073682684613a19ada56b8456
  selection_reason: new
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
  recognition_fingerprint: sha256:c8c96a8b79d65a4b847edde71cfa425f5ecef7c4b639124ce7f10dec483880dc
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: setxattr
  source_fingerprint: sha256:2b3ca06942914fa791e7d3b2c75f7ceaa490c4df668fba2a771e4c0db7457cb0
  recognition_fingerprint: sha256:4094acc7e80d34d4cfd45859e703be24d568f913f24f4b29b4b278b012b12cc1
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 8
  unresolved_evidence_count: 4
  reason: unresolved_evidence
- syscall: sgetmask
  source_fingerprint: sha256:7472dab768f3bfd479c204abfd475405c9b0d9d0b9a4a84125082c92bd7c54f8
  recognition_fingerprint: sha256:8fcd9f75443427db44947f0ff451569e696d3d4d29a0a360b2f3add31ac36dcf
  selection_reason: new
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
  recognition_fingerprint: sha256:d09d8b731bc221c5b268495e9c31e3dfbeee74709c473bf1b925c00b8be71554
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sigaction
  source_fingerprint: sha256:61d9673dc305b0ea3d84e83150b83b5269afeaba5b1fd2277babdd5787f6cf1c
  recognition_fingerprint: sha256:a00f62e84421eb5cd1096400422577490c1a24f3f43b359e074fa1e58bcb1289
  selection_reason: new
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
  recognition_fingerprint: sha256:ecdb7af258fb7b9e4a91fc8d4135293b51f5e3378821149d7af8fcc95643621e
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_470EA842B2582537
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:470ea842b2582537a448a45d2fc1e840076d342c0951e5694778d43c616c8b48
  - id: LTP_4D86B6394424B16C
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:4d86b6394424b16c0b19db94d948a5c2159b97bc2926ad97046cc24d0f327c71
  - id: LTP_612BF74E1426528A
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:612bf74e1426528ac5648670a868c758db08a43a4347f410682648cf830f1251
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: sighold
  source_fingerprint: sha256:4ad49fded412785e4a17bb4add5bb7202a0cc746ea8ed37fcaced839c7c6ecd8
  recognition_fingerprint: sha256:93d524a3bcf7926ff054ab2cefeaf20740e642d7e1a4177f6ad4549bc5019738
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: signal
  source_fingerprint: sha256:01ab6c51adcc06a4a31adfa404816290f94f777590f35e82d32a43d9c376262d
  recognition_fingerprint: sha256:cc75f86f751cf457722d5e7db7930cb144a2210669066615a2ee0220306e14af
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: signalfd
  source_fingerprint: sha256:fa8b8494a9a202da803c5ecda7fb307df401d2044779d412babeae9ec841e118
  recognition_fingerprint: sha256:560bf5a7057859f8d48398be9dd872fb2e8b05300f3b304a8f10afe0f5d2ca31
  selection_reason: new
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
  - id: LTP_2C867F470A477D29
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:2c867f470a477d292a4a2d40ee43a337e4f77bb80811d916445beb2036cebbb8
  - id: LTP_644B7DB483FF489B
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:644b7db483ff489b863663d59320d40d38b083fafafb58b6a025df0621562db1
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: signalfd4
  source_fingerprint: sha256:3717445b60556e013073e5b04ab7348211c93f6230d7c603836a1d1d040b62ac
  recognition_fingerprint: sha256:8c45b667ce519cb1a80d58dfe01cb7c5d01f37b78712977b555939c0c37a13b7
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: sigpending
  source_fingerprint: sha256:a4e1a4fc089feb52730582fad120800cc1cc809bb2531a9ae7ad97e2cf6cea70
  recognition_fingerprint: sha256:b282b12a57e3daa0a5178b362398e2261e94f13dfd9f3589be1d7c8c6baed137
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: sigprocmask
  source_fingerprint: sha256:d70688f183380aa65cf0241a4314d3482172666d826e81a943ab27e277f0ae0e
  recognition_fingerprint: sha256:e68375079d12c69bd1cda8a409db4358323bbd58c56fd672c108ae28f10ef2b0
  selection_reason: new
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
  recognition_fingerprint: sha256:82cae111ee9019731860a831f8c18b77d6af921ee2af832b6174f3045a4c9271
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: sigsuspend
  source_fingerprint: sha256:abca2c0631cb1398e2f22555d4d647c3e29f03d17a5bb09c27a6ea15c4797dc3
  recognition_fingerprint: sha256:a1a5e27a8924b13bc867ee60bb309a145310c305a2677ab95046e35c9500e61d
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_55D2492560C39AFD
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:55d2492560c39afdae0198b58071de3dce1131484ca2d56f9b815ee38a7bb70b
  - id: LTP_6366A1114F49C2CF
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:6366a1114f49c2cf8938432f60e282c5e56e90dcc063071b80f7a0e11280647e
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: sigtimedwait
  source_fingerprint: sha256:76475232466a02da15b91c7ca6eabe16eae8a97fa6071e450e7db72e8488f5b2
  recognition_fingerprint: sha256:40e81a68593a8c5963eeabaf3293c48657ca11ec94a89474ca3698d65c9ddddc
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: sigwait
  source_fingerprint: sha256:deb22e843c39406141db44e7871bb3b4657c5d6981d3c731b3d9e61187c9333b
  recognition_fingerprint: sha256:2d34d26879b8bc0ca274f62c16446a5b3883719e30b6a3f1f1c072a43a632fe3
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: sigwaitinfo
  source_fingerprint: sha256:0d9a81c57b46c154fbcc83a87da1a41817db30f5b73144634869dbeb40610bd4
  recognition_fingerprint: sha256:93d77e63baa277bc121f30627bdb8da6272a91431cff99d5701179ab03883941
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: socket
  source_fingerprint: sha256:6e88dee3dee49e7e242bdebe264952d30e2f8a9bd081c9f66e6bdf05a74e4955
  recognition_fingerprint: sha256:7fe9f6cbe59ec41cfcefcfa8193c17a8f0884dff8e2c7e915079b8721c548310
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_6B29B31CE99466E6
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:6b29b31ce99466e6682913919c0fad006475b094d59fadcc43c1ec6f4e9d1630
  - id: LTP_73330FC2133223F4
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:73330fc2133223f4aef27a10967edcd38d24fb276a72897521672217684ecc8e
  - id: LTP_971DB17D32C51561
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:971db17d32c515614f0af38045463319bd4bfb3a661a4ae9e4486c0404c75ead
  - id: LTP_A4A662687B98D33F
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:a4a662687b98d33f933b37774536af580d8b9e44d1bc317c426dd2c4a68a7a1e
  - id: LTP_AF8D38878ED1A9DA
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:af8d38878ed1a9da8bcca89799d36f633a0776307b92fe435d004f9b6cb1b444
  - id: LTP_C3098F5341F14B0E
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:c3098f5341f14b0e7f76b1bf97fff899bcf2a773a005d8c1acaf4a875833bc6e
  - id: LTP_DD2E1A555B603C7B
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:dd2e1a555b603c7b2ea7b60867a7cbf5b07e84f866b5a4cd8d83f27a24028065
  - id: LTP_DF9A0B3ADAC6AE1D
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:df9a0b3adac6ae1d22252c15f7a5d3cf7c96e3996d13b4e11b91819af475bf95
  - id: LTP_E316C28E36E136DA
    generated_at_utc: '2026-07-16T05:14:25.198516Z'
    content_hash: sha256:e316c28e36e136da592847ed1389e06538d4842d55259bc0bd80dbb61b78d10e
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: socketcall
  source_fingerprint: sha256:ed308e2e4f2aceda0639a0f7b4e6f3f60f463e0c0af254f7fac2715097782e9d
  recognition_fingerprint: sha256:4ff7262d7998e1c1c1031e3511309d8d8723b893f5ac0e22ee309b7ac199e7b3
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 4
  reason: unresolved_evidence
- syscall: socketpair
  source_fingerprint: sha256:d0a6793d2e195de68e11d78ff074bab36fa599bd7671738edbd47dc08de1c23a
  recognition_fingerprint: sha256:058e2cd53eb6ff8eedd222176b745a98305bf8abf63c6017851dd2eea5a398ab
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 3
  reason: unresolved_evidence
- syscall: sockioctl
  source_fingerprint: sha256:36d05e1378bcd2d1e52c43dfaa00f6f308d4686c6add690d926e3eb2fc606731
  recognition_fingerprint: sha256:5b6d65fa4a440954e2b3260d19eafa9cf358770400bda7dcda36159d947475b7
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: splice
  source_fingerprint: sha256:6999e9c329f6fc1d92dc7781ace26322268dbf02867df516a33f05c10bda1a8b
  recognition_fingerprint: sha256:bfbbed9a919be0303928fe8decd1996097afddb20d8163e944dfe6b3b3cb89de
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 11
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: ssetmask
  source_fingerprint: sha256:c644f8035edc4d76a50f42b97ddbc4061d795c967633b62032e164c2ff6be3f1
  recognition_fingerprint: sha256:4be268ae2250d7209231594447b2844a434fcc430a32dbe6e88d30f8505fec32
  selection_reason: new
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
  recognition_fingerprint: sha256:4dfdadf1fa5750ee933b1d771e3811047d50b739add6c89524b37e76c52eaa02
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: statfs
  source_fingerprint: sha256:8eb29f7303da698593485eaf5b364f7b3d95ca08ec5c5811aeb1985ea170f1a6
  recognition_fingerprint: sha256:8f6ff5b39f23d87b8d7983adb24c877762e064f77123407b96de4cc1269e4b84
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: statmount
  source_fingerprint: sha256:abd6c9a31b025bfe43b885a1ce7a8ba67ebf487f2ebd7cd2395f53485477a315
  recognition_fingerprint: sha256:3dea4a8158fdf7ba75c757d02c2bd78329b1e7ca443b720ec8d6c721cc8815ff
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 19
  unresolved_evidence_count: 1
  reason: unresolved_evidence
```
</details>
