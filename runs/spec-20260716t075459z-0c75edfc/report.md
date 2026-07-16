# Syscall 合规性规则提取报告

## 结论

本次分析了 statvfs、statx、stime、string、swapoff、swapon、switch、symlink、symlinkat、sync、sync_file_range、syncfs、syscall、sysconf、sysctl、sysfs、sysinfo、syslog、tee、tgkill、time、timer_create、timer_delete、timer_getoverrun、timer_gettime、timer_settime、timerfd、times、tkill、truncate、ulimit、umask、umount、umount2、uname、unlink、unlinkat、unshare、userfaultfd、ustat、utils、utime、utimensat、utimes、vfork、vhangup、vmsplice、wait、wait4、waitid、waitpid、write、writev，发现 107 条可执行的合规性规则。

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

共形成 6 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_66AC645038FEFC7A`](../../library/rules/ltp-66ac645038fefc7a.yaml) | 无额外前置条件 | 调用 swapon(TEST_FILE, 0) | 返回 -1，errno 为 EPERM |
| [`LTP_886C26D89B15EF6D`](../../library/rules/ltp-886c26d89b15ef6d.yaml) | 无额外前置条件 | 调用 swapon(USED_FILE, 0) | 返回 -1，errno 为 EBUSY |
| [`LTP_8D3FD114CB0C7420`](../../library/rules/ltp-8d3fd114cb0c7420.yaml) | 无额外前置条件 | 调用 swapon(SWAP_FILE, 0) | 调用成功，返回 SUCCESS |
| [`LTP_99D44C1A136DF4B7`](../../library/rules/ltp-99d44c1a136df4b7.yaml) | 无额外前置条件 | 调用 swapon(NOTSWAP_FILE, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_9B507ED32C4F4B43`](../../library/rules/ltp-9b507ed32c4f4b43.yaml) | NONEXISTENT_PATH | 调用 swapon("./doesnotexist", 0) | 返回 -1，errno 为 ENOENT |
| [`LTP_D982FA373261CE5D`](../../library/rules/ltp-d982fa373261ce5d.yaml) | 无额外前置条件 | 调用 swapon(SWAP_FILE, 0) | 返回 -1，errno 为 EPERM |
## `switch`

没有形成可发布的合规性规则。

## `symlink`

共形成 10 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_21FCBFC328D1815A`](../../library/rules/ltp-21fcbfc328d1815a.yaml) | NONEXISTENT_PATH | 调用 symlink(test_file, sym_file) | 返回 -1，errno 为 ENOENT |
| [`LTP_29873BE2A9AABFF4`](../../library/rules/ltp-29873be2a9aabff4.yaml) | 无额外前置条件 | 调用 symlink(nonfile, SYMFILE) | 调用成功，返回 SUCCESS |
| [`LTP_87EDCD6CC0E458CD`](../../library/rules/ltp-87edcd6cc0e458cd.yaml) | OBJECT_ALREADY_EXISTS | 调用 symlink(test_file, sym_file) | 返回 -1，errno 为 EEXIST |
| [`LTP_8ED8688C6292FECF`](../../library/rules/ltp-8ed8688c6292fecf.yaml) | 无额外前置条件 | 调用 symlink(testfile, SYMFILE) | 调用成功，返回 SUCCESS |
| [`LTP_B0433B78A1641F24`](../../library/rules/ltp-b0433b78a1641f24.yaml) | PERMISSION_DENIED_STATE | 调用 symlink(test_file, sym_file) | 返回 -1，errno 为 EACCES |
| [`LTP_C8F11074F91F94EF`](../../library/rules/ltp-c8f11074f91f94ef.yaml) | BAD_USER_ADDRESS | 调用 symlink(test_file, sym_file) | 返回 -1，errno 为 EFAULT |
| [`LTP_D8F99518FF4E8643`](../../library/rules/ltp-d8f99518ff4e8643.yaml) | 无额外前置条件 | 调用 symlink(fname, symlnk) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_DCC88B2C458969EA`](../../library/rules/ltp-dcc88b2c458969ea.yaml) | PATH_TOO_LONG | 调用 symlink(test_file, sym_file) | 返回 -1，errno 为 ENAMETOOLONG |
| [`LTP_DDA854712C50CD6A`](../../library/rules/ltp-dda854712c50cd6a.yaml) | NON_DIRECTORY_PATH_COMPONENT | 调用 symlink(test_file, sym_file) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_F041ABCAF1E2177F`](../../library/rules/ltp-f041abcaf1e2177f.yaml) | 无额外前置条件 | 调用 symlink(test_file, sym_file) | 返回 -1，errno 为 0 |
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
| [`LTP_B212BAAA2C2C75CC`](../../library/rules/ltp-b212baaa2c2c75cc.yaml) | BAD_USER_ADDRESS | 调用 sysinfo(bad_info) | 返回 -1，errno 为 EFAULT |
## `syslog`

共形成 14 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_02908A57586A60CF`](../../library/rules/ltp-02908a57586a60cf.yaml) | 文件描述符无效、USER_BUFFER | 调用 syslog(8, &buf, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_18304438A1D5D6C1`](../../library/rules/ltp-18304438a1d5d6c1.yaml) | 无额外前置条件 | 调用 syslog(8, NULL, 1) | 调用成功，返回 SUCCESS |
| [`LTP_330C66A049727F75`](../../library/rules/ltp-330c66a049727f75.yaml) | USER_BUFFER | 调用 syslog(2, &buf, 0) | 调用成功，返回 SUCCESS |
| [`LTP_4184881E196F9E5E`](../../library/rules/ltp-4184881e196f9e5e.yaml) | USER_BUFFER | 调用 syslog(100, &buf, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_4828EB12592F311C`](../../library/rules/ltp-4828eb12592f311c.yaml) | USER_BUFFER | 调用 syslog(0, &buf, 0) | 调用成功，返回 SUCCESS |
| [`LTP_498695B75BD43DAD`](../../library/rules/ltp-498695b75bd43dad.yaml) | USER_BUFFER | 调用 syslog(2, &buf, 0) | 返回 -1，errno 为 EPERM |
| [`LTP_4FCD61E2EED61335`](../../library/rules/ltp-4fcd61e2eed61335.yaml) | USER_BUFFER | 调用 syslog(8, &buf, 9) | 返回 -1，errno 为 EINVAL |
| [`LTP_6B9F97B897EC5C32`](../../library/rules/ltp-6b9f97b897ec5c32.yaml) | 文件描述符无效、USER_BUFFER | 调用 syslog(3, &buf, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_6D819B66D5B60871`](../../library/rules/ltp-6d819b66d5b60871.yaml) | 无额外前置条件 | 调用 syslog(7, NULL, 0) | 调用成功，返回 SUCCESS |
| [`LTP_7F4262FC753FC8D9`](../../library/rules/ltp-7f4262fc753fc8d9.yaml) | USER_BUFFER | 调用 syslog(1, &buf, 0) | 调用成功，返回 SUCCESS |
| [`LTP_C0694665E22D48E8`](../../library/rules/ltp-c0694665e22d48e8.yaml) | 无额外前置条件 | 调用 syslog(8, NULL, 7) | 调用成功，返回 SUCCESS |
| [`LTP_C8376BC347F94A98`](../../library/rules/ltp-c8376bc347f94a98.yaml) | 无额外前置条件 | 调用 syslog(2, NULL, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_E7CB95EADCE845E9`](../../library/rules/ltp-e7cb95eadce845e9.yaml) | USER_BUFFER | 调用 syslog(3, &buf, 0) | 调用成功，返回 SUCCESS |
| [`LTP_F38A837D067865DC`](../../library/rules/ltp-f38a837d067865dc.yaml) | 无额外前置条件 | 调用 syslog(6, NULL, 0) | 调用成功，返回 SUCCESS |
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

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_10F51B1972AD94ED`](../../library/rules/ltp-10f51b1972ad94ed.yaml) | 无额外前置条件 | 调用 timer_getoverrun(timer) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_A2AC8B6C7F993351`](../../library/rules/ltp-a2ac8b6c7f993351.yaml) | 无额外前置条件 | 调用 timer_getoverrun(timer) | 返回 -1，errno 为 EINVAL |
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
| [`LTP_3B4D19754C5D1638`](../../library/rules/ltp-3b4d19754c5d1638.yaml) | 无额外前置条件 | 调用 ulimit(UL_SETFSIZE, current_fsize) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_4984976D88DF21AE`](../../library/rules/ltp-4984976d88df21ae.yaml) | 文件描述符无效 | 调用 ulimit(UL_GETFSIZE, -1) | {'kind': 'positive_return', 'return': '>0'} |
## `umask`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_FE4AD44ED28FE386`](../../library/rules/ltp-fe4ad44ed28fe386.yaml) | 无额外前置条件 | 调用 umask(mskval) | {'kind': 'return_value', 'return': 'mskval'} |
## `umount`

共形成 7 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_287CF10D893735AB`](../../library/rules/ltp-287cf10d893735ab.yaml) | 无额外前置条件 | 调用 umount(MNTPOINT) | 返回 -1，errno 为 EPERM |
| [`LTP_3B77ABEF9EF7D3ED`](../../library/rules/ltp-3b77abef9ef7d3ed.yaml) | NONEXISTENT_PATH | 调用 umount("nonexistent") | 返回 -1，errno 为 ENOENT |
| [`LTP_6D02D744B460F97E`](../../library/rules/ltp-6d02d744b460f97e.yaml) | BAD_USER_ADDRESS | 调用 umount(NULL) | 返回 -1，errno 为 EFAULT |
| [`LTP_95F0657B8229FF85`](../../library/rules/ltp-95f0657b8229ff85.yaml) | PATH_TOO_LONG | 调用 umount(long_path) | 返回 -1，errno 为 ENAMETOOLONG |
| [`LTP_96D8C80548B2B4E0`](../../library/rules/ltp-96d8c80548b2b4e0.yaml) | 无额外前置条件 | 调用 umount(MNTPOINT) | 调用成功，返回 SUCCESS |
| [`LTP_BA10B957ACB3FFC3`](../../library/rules/ltp-ba10b957acb3ffc3.yaml) | 无额外前置条件 | 调用 umount(MNTPOINT) | 返回 -1，errno 为 EBUSY |
| [`LTP_E272B715ECA16E6C`](../../library/rules/ltp-e272b715eca16e6c.yaml) | 无额外前置条件 | 调用 umount("./") | 返回 -1，errno 为 EINVAL |
## `umount2`

没有形成可发布的合规性规则。

## `uname`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_25D7B6229831E0EF`](../../library/rules/ltp-25d7b6229831e0ef.yaml) | BAD_USER_ADDRESS | 调用 uname(bad_addr) | 返回 -1，errno 为 EFAULT |
| [`LTP_5516B8A938B9C3A5`](../../library/rules/ltp-5516b8a938b9c3a5.yaml) | 无额外前置条件 | 调用 uname(&un) | 调用成功，返回 SUCCESS |
## `unlink`

没有形成可发布的合规性规则。

## `unlinkat`

没有形成可发布的合规性规则。

## `unshare`

共形成 7 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_40A45C5E82D7F4A1`](../../library/rules/ltp-40a45c5e82d7f4a1.yaml) | 无额外前置条件 | 调用 unshare(FLAG_DESC(CLONE_FILES)) | 调用成功，返回 SUCCESS |
| [`LTP_412173E3E81DC995`](../../library/rules/ltp-412173e3e81dc995.yaml) | 无额外前置条件 | 调用 unshare(FLAG_DESC(CLONE_NEWNS)) | 调用成功，返回 SUCCESS |
| [`LTP_49ABEE42EF290FDC`](../../library/rules/ltp-49abee42ef290fdc.yaml) | 无额外前置条件 | 调用 unshare(FLAG_DESC(CLONE_FS)) | 调用成功，返回 SUCCESS |
| [`LTP_5CF4B42A5ABA3D0D`](../../library/rules/ltp-5cf4b42a5aba3d0d.yaml) | 无额外前置条件 | 调用 unshare(CLONE_NEWNS) | 调用成功，返回 SUCCESS |
| [`LTP_79882F9E36FC9878`](../../library/rules/ltp-79882f9e36fc9878.yaml) | 无额外前置条件 | 调用 unshare(CLONE_FILES) | 返回 -1，errno 为 EMFILE |
| [`LTP_82A8802A27A3D2BF`](../../library/rules/ltp-82a8802a27a3d2bf.yaml) | 无额外前置条件 | 调用 unshare(CLONE_NEWNS) | 返回 -1，errno 为 EPERM |
| [`LTP_F92CEB15161CB23C`](../../library/rules/ltp-f92ceb15161cb23c.yaml) | 文件描述符无效 | 调用 unshare(-1) | 返回 -1，errno 为 EINVAL |
## `userfaultfd`

没有形成可发布的合规性规则。

## `ustat`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_14105E9CB6DC44FC`](../../library/rules/ltp-14105e9cb6dc44fc.yaml) | 无额外前置条件 | 调用 ustat((unsigned int)dev_num, &ubuf) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_16DBBB2E96948A9C`](../../library/rules/ltp-16dbbb2e96948a9c.yaml) | BAD_USER_ADDRESS | 调用 ustat((unsigned int)root_dev, (void*)-1) | 返回 -1，errno 为 EFAULT |
| [`LTP_F75110BE79864CD1`](../../library/rules/ltp-f75110be79864cd1.yaml) | 无额外前置条件 | 调用 ustat((unsigned int)invalid_dev, &ubuf) | 返回 -1，errno 为 EINVAL |
## `utils`

没有形成可发布的合规性规则。

## `utime`

共形成 10 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_04236FD5B061DEB9`](../../library/rules/ltp-04236fd5b061deb9.yaml) | 无额外前置条件 | 调用 utime(symname, &utimes) | 调用成功，返回 SUCCESS |
| [`LTP_38432B154B641410`](../../library/rules/ltp-38432b154b641410.yaml) | NONEXISTENT_PATH | 调用 utime("", NULL) | 返回 -1，errno 为 ENOENT |
| [`LTP_43728156B00FF104`](../../library/rules/ltp-43728156b00ff104.yaml) | PERMISSION_DENIED_STATE | 调用 utime(TEMP_FILE, NULL) | 返回 -1，errno 为 EACCES |
| [`LTP_58C8C307B1FF2510`](../../library/rules/ltp-58c8c307b1ff2510.yaml) | 无额外前置条件 | 调用 utime(TEMP_FILE, &times) | 返回 -1，errno 为 EPERM |
| [`LTP_6F4B3A38B8BF4C7E`](../../library/rules/ltp-6f4b3a38b8bf4c7e.yaml) | SYMLINK_LOOP | 调用 utime(symname, &utimes) | 返回 -1，errno 为 ELOOP |
| [`LTP_6F77CAA9FC4423BA`](../../library/rules/ltp-6f77caa9fc4423ba.yaml) | 无额外前置条件 | 调用 utime(TEMP_FILE, &times) | 调用成功，返回 SUCCESS |
| [`LTP_71DD72481EF5740E`](../../library/rules/ltp-71dd72481ef5740e.yaml) | NONEXISTENT_PATH | 调用 utime(symname, &utimes) | 返回 -1，errno 为 ENOENT |
| [`LTP_86144BF50FB25D3A`](../../library/rules/ltp-86144bf50fb25d3a.yaml) | 无额外前置条件 | 调用 utime(TEMP_FILE, NULL) | 调用成功，返回 SUCCESS |
| [`LTP_D254EE40E8B5957E`](../../library/rules/ltp-d254ee40e8b5957e.yaml) | 无额外前置条件 | 调用 utime(TEMP_FILE, &utbuf) | 调用成功，返回 SUCCESS |
| [`LTP_D3FBF11AA35FDC98`](../../library/rules/ltp-d3fbf11aa35fdc98.yaml) | 无额外前置条件 | 调用 utime(MNT_POINT, NULL) | 返回 -1，errno 为 EROFS |
## `utimensat`

没有形成可发布的合规性规则。

## `utimes`

没有形成可发布的合规性规则。

## `vfork`

没有形成可发布的合规性规则。

## `vhangup`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_141CBA02709D5489`](../../library/rules/ltp-141cba02709d5489.yaml) | 无额外前置条件 | 调用 vhangup() | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_3C2993663039F664`](../../library/rules/ltp-3c2993663039f664.yaml) | 无额外前置条件 | 调用 vhangup() | 返回 -1，errno 为 EPERM |
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
| [`LTP_2F3E34FD672DBF34`](../../library/rules/ltp-2f3e34fd672dbf34.yaml) | 无额外前置条件 | 调用 waitpid(pid, &status, 0) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_614C018F61C078A0`](../../library/rules/ltp-614c018f61c078a0.yaml) | 无额外前置条件 | 调用 waitpid(pid, NULL, 0) | 返回 -1，errno 为 ECHILD |
| [`LTP_A2934B80997B62C9`](../../library/rules/ltp-a2934b80997b62c9.yaml) | 文件描述符无效 | 调用 waitpid(-1, NULL, 0) | 返回 -1，errno 为 ECHILD |
| [`LTP_DB77907DDC5EDFF4`](../../library/rules/ltp-db77907ddc5edff4.yaml) | 文件描述符无效 | 调用 waitpid(-1, NULL, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_FC8BA85373EA2D8F`](../../library/rules/ltp-fc8ba85373ea2d8f.yaml) | 无额外前置条件 | 调用 waitpid(1, NULL, 0) | 返回 -1，errno 为 ECHILD |
## `write`

共形成 6 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_05B109981D13ED76`](../../library/rules/ltp-05b109981d13ed76.yaml) | 无额外前置条件 | 调用 write(fd, NULL, 0) | {'kind': 'positive_return', 'return': '>0'} |
| [`LTP_1B4A2A1831541F06`](../../library/rules/ltp-1b4a2a1831541f06.yaml) | USER_BUFFER | 调用 write(fd, buf, i) | {'kind': 'return_value', 'return': 'i'} |
| [`LTP_22F13AFD9925B2AE`](../../library/rules/ltp-22f13afd9925b2ae.yaml) | USER_BUFFER | 调用 write(inv_fd, buf, sizeof(buf)) | 返回 -1，errno 为 EBADF |
| [`LTP_3F8B5B68E9CDC1F9`](../../library/rules/ltp-3f8b5b68e9cdc1f9.yaml) | USER_BUFFER | 调用 write(pipefd[1], buf, sizeof(buf)) | 返回 -1，errno 为 EPIPE |
| [`LTP_85742F5EC5C0112F`](../../library/rules/ltp-85742f5ec5c0112f.yaml) | 无额外前置条件 | 调用 write(wfd, wbuf, sizeof(wbuf)) | 返回 -1，errno 为 EAGAIN |
| [`LTP_89AC9F4AA9032B8D`](../../library/rules/ltp-89ac9f4aa9032b8d.yaml) | BAD_USER_ADDRESS、USER_BUFFER | 调用 write(fd, bad_addr, sizeof(buf)) | 返回 -1，errno 为 EFAULT |
## `writev`

没有形成可发布的合规性规则。


## 技术参考

- 报告 ID：`spec-20260716t075459z-0c75edfc`
- 来源：`ltp-local`，内容快照 `sha256:d789747f0c0bf1697f538bc5166073fd8449dec3beac7b12ac0be0b1b716dcb4`
- 全局待处理 syscall：53
- 提取数量：`all`（来源：`command`）
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
report_id: spec-20260716t075459z-0c75edfc
generated_at_utc: '2026-07-16T07:55:00.843723Z'
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
pending_count: 53
selected_syscalls:
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
- syscall: statvfs
  source_fingerprint: sha256:38789906e9660ba3a56673aad9fbf81dd31bb00aaa0008bd1b76347b00dc9e17
  recognition_fingerprint: sha256:a6004bac8d1e30a5dede71c9e3c615d4d048427e13aa619c6c542de3a881017a
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: statx
  source_fingerprint: sha256:4b92eb3772b36967a473e0f6878f39275e1b1f37148ca6b18b978905c7096e32
  recognition_fingerprint: sha256:df407be04f88ad75da6d57e75c36fc8e8526d781ef3aeb06716ddb3dd9de238e
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 31
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: stime
  source_fingerprint: sha256:1cca3ba099e9764bd786abb404953a2cbdcfe4f60b8d89008fd7c986a576a8d3
  recognition_fingerprint: sha256:75eca7c0a15f5d434e7b44ce82070470ed26673a258d278c1f93639e4c72dce7
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: string
  source_fingerprint: sha256:c180c2ba42c2db20c03acef1fba349d63befa09e1594262f866b80d26cd0f584
  recognition_fingerprint: sha256:a3777a587a465fe655d1e1bf075492e66e223afa200b9bfdf3d4f68a5034203a
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: swapoff
  source_fingerprint: sha256:0c20f51c6916682dd60d3401a54bdb10eb514ff2d10c1c56c8996338f037328e
  recognition_fingerprint: sha256:2a8c41bcb10bab4350ab958b5d2fda01b8dab502b2cdd539c255b43cffcea86c
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: swapon
  source_fingerprint: sha256:b282f4161865f2b6668ee5ece32816b50561c189bb9f9e13490e7d2f01d251fb
  recognition_fingerprint: sha256:1f263df578361e92653cf01d71834207237920043bbfbf2c6aee5ea05a788657
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_66AC645038FEFC7A
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:66ac645038fefc7a9123ec598be7a035ae49c84595a5fe8f4b584beab1410fe2
  - id: LTP_886C26D89B15EF6D
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:886c26d89b15ef6dc7950b0a54ad52870218a9db23b7599736a893d0e780baa4
  - id: LTP_8D3FD114CB0C7420
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:8d3fd114cb0c74201e48883709b52db162fe5bb4aa93133e8d694931edc73df9
  - id: LTP_99D44C1A136DF4B7
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:99d44c1a136df4b71776cbde598f17ed34b8993146dfceda5db4bc4e0d80748d
  - id: LTP_9B507ED32C4F4B43
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:9b507ed32c4f4b439dd7c8668ebd526fb2aeaa594c5f5d8c21a10f234896d080
  - id: LTP_D982FA373261CE5D
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:d982fa373261ce5df81f0a068b3ab1b07e3900ae875f05ceac0974c382fa14ec
  evidence_count: 6
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: switch
  source_fingerprint: sha256:70106259cc71c2c8a28e372c6076525d433171593b67002c36d4e2ecfd31ccb9
  recognition_fingerprint: sha256:5bc86dbd2988a4b91085a0ab4fce1126c8d64c8b3dae9f314577eb96bc71ad81
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: symlink
  source_fingerprint: sha256:bd4df855da95e55fcb230a4d8631acfcf67a876774a10d6cba2f28766b425a6f
  recognition_fingerprint: sha256:8d45bcc91f9a8a21e26b1a0ac3cc5135c2b6eb2632fb79d27013456a697005d0
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_21FCBFC328D1815A
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:21fcbfc328d1815aad1c1fd20c4797e91d64cad63f8c4dd02b3340c29fc06412
  - id: LTP_29873BE2A9AABFF4
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:29873be2a9aabff487752e9402604cc9a862ceadac098275cffcd26990304244
  - id: LTP_87EDCD6CC0E458CD
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:87edcd6cc0e458cde25e1becd2a341d155e7a4092acc48a70a283db7b4301227
  - id: LTP_8ED8688C6292FECF
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:8ed8688c6292fecf560fc5e28ecbab9d72c1be7828ea2675df118a184abe8b91
  - id: LTP_B0433B78A1641F24
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:b0433b78a1641f2478404ccbec3a8cad14d0a94ee86936a6d26460330ce10de8
  - id: LTP_C8F11074F91F94EF
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:c8f11074f91f94ef5feee5145cbdf4f625f9fc0bde00d6b1679588c733686a2c
  - id: LTP_D8F99518FF4E8643
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:d8f99518ff4e8643c8a74b95d327b12985404bc44c965c9e3e23563c81ce4922
  - id: LTP_DCC88B2C458969EA
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:dcc88b2c458969ead361273a98cbb21fb0bf32a05c20068c76ebabffd55bf579
  - id: LTP_DDA854712C50CD6A
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:dda854712c50cd6a2ea2a11371b97c4eee905e31d70b389262238b10091fa2c9
  - id: LTP_F041ABCAF1E2177F
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:f041abcaf1e2177f1ea24252596f52adac84498c8d5deeae4d5600c9e80529c3
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: symlinkat
  source_fingerprint: sha256:7d19a3f68ce9bce0be98fd410bab95dcb4acfe7ce3388965e42a816907aa5077
  recognition_fingerprint: sha256:7bbbf6e7d57093defbae4d9e5892f1d0451800715b3e186304939736e245e175
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: sync
  source_fingerprint: sha256:6422428a20c3b718edf0917323037a1f5faff1b0653359e65aa46d565347f9b8
  recognition_fingerprint: sha256:9aaf08d3ab5e34392552f21af9d9f70535e69e66dc371d88f31bd86806752190
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: sync_file_range
  source_fingerprint: sha256:9549e4b46f60a4e43e0781afeefa4e6544c3d3b047371be9109f55aadb61318b
  recognition_fingerprint: sha256:b379f651360a47503b148b2adbf5efb84241243edc616be1558be3178a7abb4f
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: syncfs
  source_fingerprint: sha256:633bc5b862527c690b6f46ddb8ddbae448faefa63185dfc1d02433e2a9ff0047
  recognition_fingerprint: sha256:53b8eeb4982beeea9bae2db36815b9788e6ed2c2d8ba93ed30e4b533d2d9bc48
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: syscall
  source_fingerprint: sha256:30f4af78d21f1f50fffcf043eb66b2767102edc2ef148e30af2f367ca6c11d5e
  recognition_fingerprint: sha256:b0f92425ae007677e3c6b58516acce6790a9d43c7c7d071d65fea3ba50056e40
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: sysconf
  source_fingerprint: sha256:fbdea403a040a4fdeb953f5b20437c090677a148bb9b5ad06467c2aab8df56d6
  recognition_fingerprint: sha256:0998cee6df7c6885d259a74630b0f6fda10873bc66e69fd66a054eca550e4aa3
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: sysctl
  source_fingerprint: sha256:1262294d7ac974e429bc9b1ac873ae55311c865623eeae569b3b1f428c790fcb
  recognition_fingerprint: sha256:79e3da2e31bd6b273ff375384bf41a6fd9bdf92dd463c0850eaa29de619cea76
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sysfs
  source_fingerprint: sha256:a1d7280e01310ab19fbe9435cea6845d7d69b288efade7464814c9d8ffcbb4de
  recognition_fingerprint: sha256:599c2d5bdd7a767be7d197087d2f8b895b96877888c528300aafc48aae1fe844
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 11
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: sysinfo
  source_fingerprint: sha256:230ce7e6f3a21328efc74bc13b27432b6f8b358aa89f34f007d490866f253dec
  recognition_fingerprint: sha256:58142ad4ceca302b2186bd83c98dcad3d3c4ebd1f4f3e19cb86ba05fde9cf03f
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_A367723236ADA8B4
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:a367723236ada8b46a0d6d3a444b7812e36d2f96cc8654bcd32ce5076bb39ed0
  - id: LTP_B212BAAA2C2C75CC
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:b212baaa2c2c75ccd7b7f34232754295047699d8e2313fb615060af5bd169373
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: syslog
  source_fingerprint: sha256:62c4654d4b12139bbadf9ce8646ede27ce5293c2bfca5a48c2e84aef38ff2bce
  recognition_fingerprint: sha256:1c4030fa9b58eb3a50af7434cffa7fd6a7a23f8f408b1172580e78c99703304c
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_02908A57586A60CF
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:02908a57586a60cf97975b8f95394e7951ece1af5dc4a2d4f4d0cfd9e88dcbb5
  - id: LTP_18304438A1D5D6C1
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:18304438a1d5d6c182245685a0aefa3fcd6f0d75073af8b21b358cd6fde2ed6d
  - id: LTP_330C66A049727F75
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:330c66a049727f7518cbc03f78e0a13298797ce579a19a07aba3934bf5a032a9
  - id: LTP_4184881E196F9E5E
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:4184881e196f9e5efee9a54f53a2a97047ce89fd7abffd3a654b71541e6e9fd8
  - id: LTP_4828EB12592F311C
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:4828eb12592f311c667b808fe126e60537995d13c3c3e654866c252c6d5dbeed
  - id: LTP_498695B75BD43DAD
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:498695b75bd43dadefde5707b7bcf6e34235569b786f3cce6145ec6b7368b0c0
  - id: LTP_4FCD61E2EED61335
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:4fcd61e2eed61335208db28dbb13c3b597c026dc806ec751fae9d6f7b7f08622
  - id: LTP_6B9F97B897EC5C32
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:6b9f97b897ec5c326f9f68e26e9353a0e9bcb1ca59ce6f15c338328a7d201bda
  - id: LTP_6D819B66D5B60871
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:6d819b66d5b60871ddc5afd507de205a17a9c129acbbe65c3bb4fbea8b88690e
  - id: LTP_7F4262FC753FC8D9
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:7f4262fc753fc8d9c2839c24cd85c23360614c577015c6e3fabc9dd8fb34cf65
  - id: LTP_C0694665E22D48E8
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:c0694665e22d48e81c31be680d5f2b1a220a2e394e1bcceee63d029d46d390b9
  - id: LTP_C8376BC347F94A98
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:c8376bc347f94a984bf5b3e6cf3baa97d7f384dde2c141d2a0a70d0693aa589d
  - id: LTP_E7CB95EADCE845E9
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:e7cb95eadce845e91b76c832c765fc7fdd3e86dba6cc61afbaee7f9e89fc5dc2
  - id: LTP_F38A837D067865DC
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:f38a837d067865dc1bb5b53c9ed0d922ffc01ea007b07efcc91639965b34e90e
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: tee
  source_fingerprint: sha256:f0f5563b5ded9ccc989355f4f2d95b1de904f7dddb9adf1d54aee34a13099b33
  recognition_fingerprint: sha256:0ed3bb0e9f6be55a42ef5f1a98a87d888baa13643b8fc66f28d2abd650223fee
  selection_reason: new
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
  recognition_fingerprint: sha256:035860d8f8434c7c7da8ee80c103308a187edbaa9af4f7fce9ffb31813e17d46
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: time
  source_fingerprint: sha256:2edaa199d4fd856ca678a85b80a7f2330ce2e9e7744473a2a693d656848eafaa
  recognition_fingerprint: sha256:ab21a5e6add580b8ad2d9b368f05eb5d5656e8d8ee917d4939e9f581a937ad4d
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: timer_create
  source_fingerprint: sha256:3c0ad32c8b4d4d5c6420004eec75aac394c608405f046696b813ffe465b167a0
  recognition_fingerprint: sha256:59dc73c3791d1c466b54445578fc85321ad14ab920d71e5fb76f297c2b1277ba
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: timer_delete
  source_fingerprint: sha256:f22af16816b16cd335c668240718f3e296df38cba4e85b675fc42ba082288e55
  recognition_fingerprint: sha256:bd14d2b1d7f2a2de8064fa1b3e0a8d3297c08f7ee0a44589c78be2c79cf41798
  selection_reason: new
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
  recognition_fingerprint: sha256:3596fc0bb8256a6ef0e6489df4423a316d916b6b647e1bd32ff5db1bf77f4f0e
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_10F51B1972AD94ED
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:10f51b1972ad94ed66f8d82dba0507bf1d6e5a169f13d0ee89dae82b431dd523
  - id: LTP_A2AC8B6C7F993351
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:a2ac8b6c7f99335192748f659d49049fb811e0f11dac0bb364e9e3608b702498
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: timer_gettime
  source_fingerprint: sha256:65bebaf1198e803f48824374545a02fad7bf0675ab9a53ac463993e6d42cbf4e
  recognition_fingerprint: sha256:77c281a830fef348e6af8d42234394bea5fd6e1111cb2ddd0021df7e5fb51246
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: timer_settime
  source_fingerprint: sha256:6a13214fc81d1cf230e3ad90eb29897963a1e05e5633cad613fbf7048401ba4d
  recognition_fingerprint: sha256:ca1a79414b267ab24988ae29f757c0171e73d75591e3d829d9301ac210375656
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: timerfd
  source_fingerprint: sha256:7e568a6cbf4a8b4e62a928d8222728c26246baf09381f67644467f8cdac7fca7
  recognition_fingerprint: sha256:575476d1cd35b8c1f961718d2aa4bfdd54ca63326d55b1b8a83e1052c3915c63
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 3
  reason: unresolved_evidence
- syscall: times
  source_fingerprint: sha256:e3d621ee1c7e22cc4df76d30c2a42b837a51aec99adc0450425927b94bec3c67
  recognition_fingerprint: sha256:8e0651c19e67983022eed868a9a31ce7e307894786856fc1966d62aae8863f6b
  selection_reason: new
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
  recognition_fingerprint: sha256:007e87dbc956690a093cde7035c97f08c33c8e9f7d62b59ec2a63775e06ddf0d
  selection_reason: new
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
  recognition_fingerprint: sha256:23076092f8eaa8189af03c25cdbdf15d1a30f773be27627902e854520fb91236
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: ulimit
  source_fingerprint: sha256:6b5527f2af95ca4470378246dd58a9708c75c667f9f5c69626b1bc90adcf9a94
  recognition_fingerprint: sha256:d7c218d222dce099198cff5612ad8af3f06fe59cd77d71cf7ba50d03f61ca855
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_287FBE05D7B30C6F
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:287fbe05d7b30c6fbe2694789ed8d27dfd69891644ad0a2638b4bef47e6dc257
  - id: LTP_3B4D19754C5D1638
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:3b4d19754c5d16380eb8bf1f188d3aad4e6a5ffb3e0ced2e504f9a95ef77309d
  - id: LTP_4984976D88DF21AE
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:4984976d88df21ae2776c5e23c70c552b2fe81a776d404ea395e317f5b568279
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: umask
  source_fingerprint: sha256:47d64ed1c8a0f550e1ba6bcad3f9cc1ff9d9c8bf84585860cd5568cc7ef1c604
  recognition_fingerprint: sha256:44b2e2a765c5b8561a2bb7378caa8e22e3bbd654c6e2316e3311df59b2b6a713
  selection_reason: new
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
  recognition_fingerprint: sha256:955db09737c6e5e4ebcefcfcd8fb3f729a7f116bf70340f244ce851592c7f44f
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_287CF10D893735AB
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:287cf10d893735aba939172ccbac5cf025dd704d8272d5048fb79e3f211821c3
  - id: LTP_3B77ABEF9EF7D3ED
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:3b77abef9ef7d3edf9e2dc1c928c11e4889fa87246788efd39350072d6a71b36
  - id: LTP_6D02D744B460F97E
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:6d02d744b460f97e6af278379decd500845ef81c194877b232e8fb2df13af1ae
  - id: LTP_95F0657B8229FF85
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:95f0657b8229ff85be4707165cfd53f30a4a7be9d8922cff2f0e73f62929b7c4
  - id: LTP_96D8C80548B2B4E0
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:96d8c80548b2b4e0e34fe791102b0afa0a522100507abe2552214a6fc39c5d72
  - id: LTP_BA10B957ACB3FFC3
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:ba10b957acb3ffc3f735e9ac0e7841382981ac5f91af68418b9c4bc64eac1dbf
  - id: LTP_E272B715ECA16E6C
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:e272b715eca16e6c203ebd024d4823faa94823321108392ec0eeae3a79e23e82
  evidence_count: 6
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: umount2
  source_fingerprint: sha256:026fdae27c0cf73a47bfb7412efa7440c3ad36d802477aaa29f6bd4a77a5b908
  recognition_fingerprint: sha256:188bd002cb6ca104fdc9c570eb8a96e17c75f66ae191feaeb97774239d6539f3
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: uname
  source_fingerprint: sha256:809ee6d0c537a8c783c72f21457ae65226012bc42f61e371e4f5380149181f7a
  recognition_fingerprint: sha256:78cdebc7dc4a88ce4c3e9a8d8c5cbf000e6e91cf5fc58eca235427a3e8b7dd5c
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_25D7B6229831E0EF
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:25d7b6229831e0ef4c751d96db2c6b85b6bcacf424ab6ee9d1edad943b336041
  - id: LTP_5516B8A938B9C3A5
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:5516b8a938b9c3a56502a0790304ef99d9caee848e7faaafcdf2f016f6443230
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: unlink
  source_fingerprint: sha256:c26e8ac44302357877f7d0878b75133085d818f06c24719be90b0d2c95f8875d
  recognition_fingerprint: sha256:c9c8107a8dd5432ec82164619c3e5585353dda4234bf5a478de246df63b0fb22
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 10
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: unlinkat
  source_fingerprint: sha256:1cb52ca796b06c5790269e888dfe6b9b227c24414e4cae7886e0f7117e06b2f0
  recognition_fingerprint: sha256:7cf95be0f7ab71d0eddaa96972097175d55658678ede5ef0b97f712ef250adb1
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: unshare
  source_fingerprint: sha256:c8c06fd3fb37ee58b2df434755f202a6becd88284141bd430375a4e1ac023730
  recognition_fingerprint: sha256:4fbc44941782091ee7bb92ceb06941fe233dfcb5e326e1652917e4666df6d2bf
  selection_reason: new
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
  - id: LTP_5CF4B42A5ABA3D0D
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:5cf4b42a5aba3d0d993d4b307856f5ec2234c06d696585bc72260e1a39827cba
  - id: LTP_79882F9E36FC9878
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:79882f9e36fc98785b2141a1e7d4ddcb6b29424f7eacb2c5028ef17bcdabb831
  - id: LTP_82A8802A27A3D2BF
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:82a8802a27a3d2bf01cb995752e7667b482979d9e93565f11e732bb2a5a31b28
  - id: LTP_F92CEB15161CB23C
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:f92ceb15161cb23cd37673ad2b1e78081eaf5d927174f20812d06cca3cf0c67c
  evidence_count: 9
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: userfaultfd
  source_fingerprint: sha256:984775e5d36678185dc7a62fd3d6fef8857585d0bb78b6dc140f0fd8c8990f32
  recognition_fingerprint: sha256:8bd30c395715b730c19b35916ec7130f0dd88d20f55874fb1bca6cd1cb2d7072
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 7
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: ustat
  source_fingerprint: sha256:701bc07cf47f966e21ff5ec22f27541a8a87f25a6c0edffc3f8a04fb3c42a43f
  recognition_fingerprint: sha256:0ffd3ccda6259c290985e39fce68210db3776f55f336d4a41b5f8fc25067e17a
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_14105E9CB6DC44FC
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:14105e9cb6dc44fc9041096a73f814e989b2fd58998fb3840c19f444656c49ab
  - id: LTP_16DBBB2E96948A9C
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:16dbbb2e96948a9c6649079c041ed99e1a7caffecc8e20185d6b5a9191cc06fd
  - id: LTP_F75110BE79864CD1
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:f75110be79864cd1d4048f6b85616b33cb4d5b1b114f83177fed3a73e2ab395a
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: utils
  source_fingerprint: sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  recognition_fingerprint: sha256:85822a6d8b1a27d979425ba6f0fd7e43949cbb612bac34a26dbf6e48194096ca
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: utime
  source_fingerprint: sha256:1eabec8784e6ecd5375cc682945366f2305ebb6f79e4f87f5c74802f0490460d
  recognition_fingerprint: sha256:0f1eefca73450d7170b8d70c3840c09512d68f90b7cc3316c2802622579f45cf
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_04236FD5B061DEB9
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:04236fd5b061deb91a99cc5990d76abb4d0305312af10adf6221c7cdbcf28567
  - id: LTP_38432B154B641410
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:38432b154b641410365b7f4a7ad2ca324c3c356bf93948d3c948552a39f1f368
  - id: LTP_43728156B00FF104
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:43728156b00ff104889586e9f9c3c97e3681823265c64387f32a84c300f8aebb
  - id: LTP_58C8C307B1FF2510
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:58c8c307b1ff25100a989b73841bba45b1dcf61406863df2f8b8bfce4c294f2e
  - id: LTP_6F4B3A38B8BF4C7E
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:6f4b3a38b8bf4c7e714c705e096b38742f0d55e11af069efd85a780cbd567c0f
  - id: LTP_6F77CAA9FC4423BA
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:6f77caa9fc4423ba48f8bccdc757c34ac19acb29a8df9d9089f395904ee88d54
  - id: LTP_71DD72481EF5740E
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:71dd72481ef5740e84d8f583e4c75aa6d22288a996d96ab3f4c50bef33fc2b5b
  - id: LTP_86144BF50FB25D3A
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:86144bf50fb25d3a419e3c011f5c2334e4885d5643718a54ea7d6d0d3e8b4bab
  - id: LTP_D254EE40E8B5957E
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:d254ee40e8b5957eb45b944d458cd22c2b8bd611d8da6326448e10c63c65ed36
  - id: LTP_D3FBF11AA35FDC98
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:d3fbf11aa35fdc9822cf222ab445c4b805e07deeb66e77dbef1f57cb740563ac
  evidence_count: 19
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: utimensat
  source_fingerprint: sha256:ff0347d28769b35cad9698b38d130a690e077ecaa0a6c03725a8467e71d071c7
  recognition_fingerprint: sha256:f4908565c91276f2be7a65cabb8a5ff1f742dac53e9722c5c5d2ed7a1fc69321
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: utimes
  source_fingerprint: sha256:c98626ff7a10942ab5bdf99142786f991abe275e46cdf75a254336a56f273aa6
  recognition_fingerprint: sha256:61e2e7a1c341b43ddb594eed3a2a9cde0b723c6325be4c28570b817f3a5a228d
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: vfork
  source_fingerprint: sha256:2d9866995435c96b3ffd7ca10b45ccfaf95c2c65cb2388621fd91257fc5a8f86
  recognition_fingerprint: sha256:6dcfe6e3215923a9bc0b2e6f3df49a5069c86563d59640875fb2e8524a46cb04
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: vhangup
  source_fingerprint: sha256:d3fb85c015a3a7d4d8d23f3d1e63aa71760f7640152f835ce3d20eb6b4b1b4ad
  recognition_fingerprint: sha256:c4de629d9357f6df56b6b212edc9a53e43dff96ac5f149a11d7ebfe8ab04d6de
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_141CBA02709D5489
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:141cba02709d5489742216adf4aa157d65c364d6f6942354cc665e0282727154
  - id: LTP_3C2993663039F664
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:3c2993663039f66452c93ada6311fb9f02eecf9c4a376f303fe87f536ead8b13
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: vmsplice
  source_fingerprint: sha256:e72a1c8ae19356d37d917eafb188699f33a61a7787be53b6bd6d80c638060140
  recognition_fingerprint: sha256:d00dee3d556078bbf4a5d885aca17c75537a18aaedf77d0ef17b64cdc130b7d3
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: wait
  source_fingerprint: sha256:72acc6555cca05cb5deaa5c954daabcc7fd9bba722c565f2595be5efed60dea8
  recognition_fingerprint: sha256:590e181d96b48ede6e19fc40a2f4b8f66a49d192386ae9a8f96dd73d3f5881f7
  selection_reason: new
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
  recognition_fingerprint: sha256:70b38855bc2bd0aa027cf09bf0488b902c898dc2b8a1a570157fecf1c04d956e
  selection_reason: new
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
  recognition_fingerprint: sha256:6166d470b7004a8bbe592b51d8dbff16df2dc66659c0c484fd2bf2a28af4d3ad
  selection_reason: new
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
  recognition_fingerprint: sha256:7eb497aa77a88179aaa266f8d816d78e821bbb60613299a822870d0acc37be27
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_03AF14160F8B59A0
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:03af14160f8b59a0b546095a476facf6e3504937dd6f387971839bd21441739b
  - id: LTP_2F3E34FD672DBF34
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:2f3e34fd672dbf34b28611337f295a687ae0db9f5a34edb98b0cb1a9b82235f2
  - id: LTP_614C018F61C078A0
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:614c018f61c078a0c1629bf12f259ab3108460b39da9611587eb8ab0f96a9017
  - id: LTP_A2934B80997B62C9
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:a2934b80997b62c96c7d18d8295c04e7ce45893f9122cfdb44bdfeb8070674ff
  - id: LTP_DB77907DDC5EDFF4
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:db77907ddc5edff4d8d968e3c7e9d2951a2203061f9a3b0b44d16f3fb2fad3a4
  - id: LTP_FC8BA85373EA2D8F
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:fc8ba85373ea2d8f73d801b46060fd0ce0d4e78ef2f1ce6a5923118389112ce8
  evidence_count: 6
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: write
  source_fingerprint: sha256:6dda79ad1797a15505bc45e729ac05060fefc4da5f8290d5ffe46a9d9f0af98a
  recognition_fingerprint: sha256:735b575c8466760e1c3b5081fa0a88545619dae3a5c7453cff11bbd71fd43a5a
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_05B109981D13ED76
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:05b109981d13ed76154b1411f6997daf1d254a9c067f513bef268b4d8581477b
  - id: LTP_1B4A2A1831541F06
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:1b4a2a1831541f06f6b87330ac547677379f43e2522608e2dd8572aab65102c4
  - id: LTP_22F13AFD9925B2AE
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:22f13afd9925b2ae8222ce9fc99a57aade463bf877958700a932dc0139dbc888
  - id: LTP_3F8B5B68E9CDC1F9
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:3f8b5b68e9cdc1f980e44691a83d3b5788c86273070e759891e3403e651a742e
  - id: LTP_85742F5EC5C0112F
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:85742f5ec5c0112fc5450c1c6c95469726dbd05873c4632fc58a9157f73831e9
  - id: LTP_89AC9F4AA9032B8D
    generated_at_utc: '2026-07-16T07:55:00.843723Z'
    content_hash: sha256:89ac9f4aa9032b8d11bb4ae86cf399214fec330c862ae0acea4b7e8158e7e21b
  evidence_count: 9
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: writev
  source_fingerprint: sha256:6ab89a155f1732cadab0c34d356b295b5d00c931a8cba19259e1db42966cae0a
  recognition_fingerprint: sha256:fd56a84763dfe2f5030c532f3624a70248fc77f39e22a20eb046a7be28bca4a5
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 7
  unresolved_evidence_count: 1
  reason: unresolved_evidence
```
</details>
