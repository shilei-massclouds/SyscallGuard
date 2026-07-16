# Syscall 合规性规则提取报告

## 结论

本次分析了 fchdir、fchmod、fchmodat、fchmodat2、fchown、fcntl、fdatasync、fgetxattr、file_attr、finit_module、flistxattr、flock、fmtmsg、fork、fpathconf、fremovexattr、fsconfig、fsetxattr、fsmount、fsopen，发现 97 条可执行的合规性规则。

## `fchdir`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_043885E3B78D9010`](../../library/rules/ltp-043885e3b78d9010.yaml) | PERMISSION_DENIED_STATE | 调用 fchdir(fd) | 返回 -1，errno 为 EACCES |
| [`LTP_17B7A9460939622A`](../../library/rules/ltp-17b7a9460939622a.yaml) | 无额外前置条件 | 调用 fchdir(fd) | 调用成功，返回 SUCCESS |
| [`LTP_CCC36F43E9463D3E`](../../library/rules/ltp-ccc36f43e9463d3e.yaml) | 无额外前置条件 | 调用 fchdir(bad_fd) | 返回 -1，errno 为 EBADF |
## `fchmod`

共形成 7 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_371BDA67CB8813FD`](../../library/rules/ltp-371bda67cb8813fd.yaml) | 无额外前置条件 | 调用 fchmod(fd2, 0644) | 返回 -1，errno 为 EBADF |
| [`LTP_470C0966080C93EF`](../../library/rules/ltp-470c0966080c93ef.yaml) | 无额外前置条件 | 调用 fchmod(fd, mode) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_96B2A3E7AC7B2444`](../../library/rules/ltp-96b2a3e7ac7b2444.yaml) | 无额外前置条件 | 调用 fchmod(fd, PERMS) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_A1B6FBC6EF800331`](../../library/rules/ltp-a1b6fbc6ef800331.yaml) | 无额外前置条件 | 调用 fchmod(fd, PERMS_DIR) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_B86CDF340A27A5B7`](../../library/rules/ltp-b86cdf340a27a5b7.yaml) | 无额外前置条件 | 调用 fchmod(fd, PERMS) | 调用成功，返回 SUCCESS |
| [`LTP_F1299BC5F92BF26E`](../../library/rules/ltp-f1299bc5f92bf26e.yaml) | 无额外前置条件 | 调用 fchmod(fd3, 0644) | 返回 -1，errno 为 EROFS |
| [`LTP_F421E1E61753B72C`](../../library/rules/ltp-f421e1e61753b72c.yaml) | 无额外前置条件 | 调用 fchmod(fd1, 0644) | 返回 -1，errno 为 EPERM |
## `fchmodat`

共形成 9 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_023F1DC98CE31416`](../../library/rules/ltp-023f1dc98ce31416.yaml) | NONEXISTENT_PATH | 调用 fchmodat(file_fd, empty_path, 0600, 0) | 返回 -1，errno 为 ENOENT |
| [`LTP_183B0BD036512FA6`](../../library/rules/ltp-183b0bd036512fa6.yaml) | BAD_USER_ADDRESS | 调用 fchmodat(file_fd, bad_path, 0600, 0) | 返回 -1，errno 为 EFAULT |
| [`LTP_3073AC57544A6A6A`](../../library/rules/ltp-3073ac57544a6a6a.yaml) | 无额外前置条件 | 调用 fchmodat(bad_fd, test_path, 0600, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_3E0077ECCDBC2639`](../../library/rules/ltp-3e0077eccdbc2639.yaml) | NON_DIRECTORY_PATH_COMPONENT | 调用 fchmodat(file_fd, test_path, 0600, 0) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_628FD2848734A58A`](../../library/rules/ltp-628fd2848734a58a.yaml) | 文件描述符无效 | 调用 fchmodat(fd_atcwd, test_path, 0600, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_8A4C03F737A3CEE6`](../../library/rules/ltp-8a4c03f737a3cee6.yaml) | 无额外前置条件 | 调用 fchmodat(atcwd_fd, file_path, 0600, 0) | 调用成功，返回 SUCCESS |
| [`LTP_B4FD0E2B4B84F458`](../../library/rules/ltp-b4fd0e2b4b84f458.yaml) | 无额外前置条件 | 调用 fchmodat(file_fd, abs_path, 0600, 0) | 调用成功，返回 SUCCESS |
| [`LTP_EB7FFB63F4259214`](../../library/rules/ltp-eb7ffb63f4259214.yaml) | PATH_TOO_LONG | 调用 fchmodat(file_fd, long_path, 0600, 0) | 返回 -1，errno 为 ENAMETOOLONG |
| [`LTP_F04C2129F0253CC0`](../../library/rules/ltp-f04c2129f0253cc0.yaml) | 无额外前置条件 | 调用 fchmodat(dir_fd, test_file, 0600, 0) | 调用成功，返回 SUCCESS |
## `fchmodat2`

共形成 4 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_09AB8108C3720119`](../../library/rules/ltp-09ab8108c3720119.yaml) | 文件描述符无效 | 调用 fchmodat2(fd_invalid, FILENAME, 0777, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_34FB3789C7448B4F`](../../library/rules/ltp-34fb3789c7448b4f.yaml) | NONEXISTENT_PATH | 调用 fchmodat2(fd, "doesnt_exist.txt", 0777, 0) | 返回 -1，errno 为 ENOENT |
| [`LTP_8BD2C43CB1EC6794`](../../library/rules/ltp-8bd2c43cb1ec6794.yaml) | 文件描述符无效 | 调用 fchmodat2(fd, FILENAME, 0777, -1) | 返回 -1，errno 为 EINVAL |
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

共形成 13 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0E114DF9B3215650`](../../library/rules/ltp-0e114df9b3215650.yaml) | 无额外前置条件 | 调用 finit_module(fd, "status=valid", 0) | 调用成功，返回 SUCCESS |
| [`LTP_272A188C039BEA2B`](../../library/rules/ltp-272a188c039bea2b.yaml) | 无额外前置条件 | 调用 finit_module(fd, "", 0) | 返回 -1，errno 为 EBADF |
| [`LTP_34C12DFEB9C8A62A`](../../library/rules/ltp-34c12dfeb9c8a62a.yaml) | 无额外前置条件 | 调用 finit_module(fd, "status=invalid", 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_5667C5A09C3EC10E`](../../library/rules/ltp-5667c5a09c3ec10e.yaml) | BAD_USER_ADDRESS | 调用 finit_module(fd, NULL, 0) | 返回 -1，errno 为 EFAULT |
| [`LTP_5B244D0A4892F35A`](../../library/rules/ltp-5b244d0a4892f35a.yaml) | OBJECT_ALREADY_EXISTS | 调用 finit_module(fd, "", 0) | 返回 -1，errno 为 EEXIST |
| [`LTP_74BAD566B6A0F272`](../../library/rules/ltp-74bad566b6a0f272.yaml) | 无额外前置条件 | 调用 finit_module(fd, "", 0) | 返回 -1，errno 为 EKEYREJECTED |
| [`LTP_7AF4AAC644090507`](../../library/rules/ltp-7af4aac644090507.yaml) | 无额外前置条件 | 调用 finit_module(fd, "", 0) | 返回 -1，errno 为 EPERM |
| [`LTP_8BFB8BE2E39B38A1`](../../library/rules/ltp-8bfb8be2e39b38a1.yaml) | 无额外前置条件 | 调用 finit_module(fd_dir, "", 0) | 返回 -1，errno 为 0 |
| [`LTP_A030561DFACE8C93`](../../library/rules/ltp-a030561dface8c93.yaml) | 无额外前置条件 | 调用 finit_module(fd_zero, "", 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_A16555D2419FBCD4`](../../library/rules/ltp-a16555d2419fbcd4.yaml) | 无额外前置条件 | 调用 finit_module(fd, "status=valid", 0) | 返回 -1，errno 为 EKEYREJECTED |
| [`LTP_BA03F1BD9B5F2BE2`](../../library/rules/ltp-ba03f1bd9b5f2be2.yaml) | 无额外前置条件 | 调用 finit_module(fd, "", 0) | 返回 -1，errno 为 ETXTBSY |
| [`LTP_DA65D6C7A0E4ABBC`](../../library/rules/ltp-da65d6c7a0e4abbc.yaml) | 文件描述符无效 | 调用 finit_module(fd, "", -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_F13B0055458E603F`](../../library/rules/ltp-f13b0055458e603f.yaml) | 文件描述符无效 | 调用 finit_module(fd_invalid, "", 0) | 返回 -1，errno 为 0 |
## `flistxattr`

共形成 4 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_51E954C969CAFA58`](../../library/rules/ltp-51e954c969cafa58.yaml) | USER_BUFFER | 调用 flistxattr(fd, buf, sizeof(buf)) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_609D7178B8A77C1F`](../../library/rules/ltp-609d7178b8a77c1f.yaml) | 无额外前置条件 | 调用 flistxattr(fd[n], NULL, 0) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_C37E693AB7AA5E28`](../../library/rules/ltp-c37e693ab7aa5e28.yaml) | USER_BUFFER | 调用 flistxattr(fd2, buf, 20) | 返回 -1，errno 为 EBADF |
| [`LTP_F10E5286CF6CAC64`](../../library/rules/ltp-f10e5286cf6cac64.yaml) | USER_BUFFER | 调用 flistxattr(fd1, buf, 1) | 返回 -1，errno 为 ERANGE |
## `flock`

共形成 15 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_04A84187DEC4CF09`](../../library/rules/ltp-04a84187dec4cf09.yaml) | 无额外前置条件 | 调用 flock(fd2, LOCK_SH) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_245110930B22BF5C`](../../library/rules/ltp-245110930b22bf5c.yaml) | 无额外前置条件 | 调用 flock(fd1, LOCK_UN) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_3AF9CC563B4BAC1C`](../../library/rules/ltp-3af9cc563b4bac1c.yaml) | 无额外前置条件 | 调用 flock(fd, LOCK_SH) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_44128D8D82BC1E09`](../../library/rules/ltp-44128d8d82bc1e09.yaml) | 无额外前置条件 | 调用 flock(fd, LOCK_EX) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_50FD97B7CD409007`](../../library/rules/ltp-50fd97b7cd409007.yaml) | 无额外前置条件 | 调用 flock(fd, LOCK_EX) | 返回 -1，errno 为 EINTR |
| [`LTP_6A70899352D69A0B`](../../library/rules/ltp-6a70899352d69a0b.yaml) | 无额外前置条件 | 调用 flock(fd, LOCK_UN) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_7EAD5A075576B981`](../../library/rules/ltp-7ead5a075576b981.yaml) | 无额外前置条件 | 调用 flock(fd2, LOCK_EX | LOCK_NB) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_86E690B05A18AF6A`](../../library/rules/ltp-86e690b05a18af6a.yaml) | 无额外前置条件 | 调用 flock(fd2, LOCK_EX | LOCK_NB) | {'kind': 'return_value', 'return': '0'} |
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


## 技术参考

- 报告 ID：`spec-20260716t025200z-8687ae3e`
- 来源：`ltp-local`，内容快照 `sha256:d789747f0c0bf1697f538bc5166073fd8449dec3beac7b12ac0be0b1b716dcb4`
- 全局待处理 syscall：313
- 提取数量：`20`（来源：`global_default`）
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

<details>
<summary>机器可读元数据</summary>

<!-- syscallguard-metadata -->
```yaml
schema_version: 1
kind: syscallguard_ingest_report
report_id: spec-20260716t025200z-8687ae3e
generated_at_utc: '2026-07-16T02:52:01.871423Z'
source:
  id: ltp-local
  type: ltp
  snapshot_hash: sha256:d789747f0c0bf1697f538bc5166073fd8449dec3beac7b12ac0be0b1b716dcb4
  descriptor_hash: sha256:4315924cd8b9aab9608c225950c81f18ab74f25d63d74ee6ac3c444132131b4d
  recognition_rules_hash: sha256:84d715591e7abe5f2ac2de68c75172b2b2389541f6f8b8f23582b8cff81b057e
  resolution: default_source
count:
  value: '20'
  source: global_default
pending_count: 313
selected_syscalls:
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
syscalls:
- syscall: fchdir
  source_fingerprint: sha256:31c91baafe050edaf7020e951d65d9cf1a76c0db8c1fb9872ffd95376207b99f
  recognition_fingerprint: sha256:7878bbf5ba193ab1b82f189d7197907d96879ccdcdd1d308ac05e41e313add7b
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_043885E3B78D9010
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:043885e3b78d90106faa4a4cb2129667871c12a6e7ac92aa294dfc4ede78a34a
  - id: LTP_17B7A9460939622A
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:17b7a9460939622a41226aa0c0191c618d2a9b74c6e2321e127b1ba067b85bff
  - id: LTP_CCC36F43E9463D3E
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:ccc36f43e9463d3e65e732efa9e9d62af421e5d01bac07a5d343fc88f368505c
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: fchmod
  source_fingerprint: sha256:028ad1a908f72e55840780a02295162d05f3dd4a0b77358288e1b7acdb418ee7
  recognition_fingerprint: sha256:d963de998255ad975a72de6f734a528a1ffe06671cdfb3aa11d5b3a2bc4d025c
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_371BDA67CB8813FD
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:371bda67cb8813fdff6eeb64e8a7d946a578b235b292932c7146d1719b4e6264
  - id: LTP_470C0966080C93EF
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:470c0966080c93efafa4bcea1083f34ab24a3c68263c2f688031a830ea7b0032
  - id: LTP_96B2A3E7AC7B2444
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:96b2a3e7ac7b2444d382341c2a7d4d7b025ae4d3e042455247ec25fd4f8b1010
  - id: LTP_A1B6FBC6EF800331
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:a1b6fbc6ef80033120dca0f6c08260bcd1a078ef1154f9ed5e9603f3dc71f0b0
  - id: LTP_B86CDF340A27A5B7
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:b86cdf340a27a5b75852381d6eac2add8cf670304b1d54a76181f89f5d363e35
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
  recognition_fingerprint: sha256:b1c6670b4d25ef388e7deac8f433d56eb3e9d27136af010f454fac21cffddb30
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_023F1DC98CE31416
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:023f1dc98ce3141678463f59b113829f79e80d000c0b92361d7251dcf5d42b71
  - id: LTP_183B0BD036512FA6
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:183b0bd036512fa6ac5e4e495d4ef620f962c234ba0ef62006c2081693268db9
  - id: LTP_3073AC57544A6A6A
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:3073ac57544a6a6a181bd3ced49d16a7499f79e9efbe267a323ad7d86356ef48
  - id: LTP_3E0077ECCDBC2639
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:3e0077eccdbc26395a1a3827bc17d12750c3e40e3e6839bacd780bc0ee642521
  - id: LTP_628FD2848734A58A
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:628fd2848734a58abbf91bdc33d9a0296f8f88586fddb7c71f9030a4423d288d
  - id: LTP_8A4C03F737A3CEE6
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:8a4c03f737a3cee6ad7b10bfa667b15524ee46f96a3bfa1532a7b6e5276c0405
  - id: LTP_B4FD0E2B4B84F458
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:b4fd0e2b4b84f458bbdc6637e1f2bce1a9bbd8b0b0f9e69ed34a8bfae2ad8153
  - id: LTP_EB7FFB63F4259214
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:eb7ffb63f4259214501407d3dc0fe0cdfb5c3e1ab5e87be029614bbddca993d0
  - id: LTP_F04C2129F0253CC0
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:f04c2129f0253cc075ad2c5f51c7af13bc903d57bb74f6876d354698009716e6
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: fchmodat2
  source_fingerprint: sha256:e96e7b6953864f897b8be9a7e3a3a804b2cfa77d6533c5b34720f53aeb2c9f1c
  recognition_fingerprint: sha256:b4b6e3da701a4a03cc8fe73d20c0d66c783a48fb6dc6aa3572e2f749d36b6edd
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_09AB8108C3720119
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:09ab8108c3720119659120dd2eb6acf3d722fc4b914a1d063ddf8477a4d28816
  - id: LTP_34FB3789C7448B4F
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:34fb3789c7448b4f6842c575aae7014ef1ef45bd2800832e3a63db32be802a90
  - id: LTP_8BD2C43CB1EC6794
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:8bd2c43cb1ec6794ff35892efa1d2a2a3e07efe5ef83e9874cfdb79feae89704
  - id: LTP_F65E54AE96F20D41
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:f65e54ae96f20d41e260ec1e6e4cc47a424d61abebb7f8bb25f00f0033efaa98
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: fchown
  source_fingerprint: sha256:2eb51c1d6396d1986ae77fda30bc81607c5bc29db2df787ab4f1703a417ce120
  recognition_fingerprint: sha256:924559d103d37f38cc6df81ecc0220cf436a653cf830d2caaf9a380a58e847e7
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 10
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: fcntl
  source_fingerprint: sha256:5cbdaae6fbaa60becf78488e060da2b184b30ae5416d81430c206f20b1be2c92
  recognition_fingerprint: sha256:f0416548e4b9a930e89ef39759c76baa60cd3021d5b68ac133f3eff9d2ef66d0
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 72
  unresolved_evidence_count: 14
  reason: unresolved_evidence
- syscall: fdatasync
  source_fingerprint: sha256:3d40a49b1adbd564fdba1333258d000c6ffe6182432594eecc468c6de28b35fa
  recognition_fingerprint: sha256:e7dfc845f64a09ae6cd75e626652e33b8c8173f279d86c8a36c0131d6a09296d
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: fgetxattr
  source_fingerprint: sha256:09ea1ba24b838f0bb1d84d8763e6ad2754f40508cdccdaf0254a227939ef9b27
  recognition_fingerprint: sha256:8b3f4eb9c695cf4a44dcab2e8037f14cded516c8aa966cb88c6c8a7ea7c97102
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 7
  unresolved_evidence_count: 6
  reason: unresolved_evidence
- syscall: file_attr
  source_fingerprint: sha256:bf2d8d8b7b62bf7390e7cc240c2168e639fc4152f5cb56d5eb55ca92796436a5
  recognition_fingerprint: sha256:88f77c524c518195f331e8078a20f6eb16de013ad6e988c3476deb4f6537be26
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: finit_module
  source_fingerprint: sha256:468391db12f3577f2aeed0e2d23b8444baa5582661434142ee2dcc16de9da5b0
  recognition_fingerprint: sha256:c208390815ee88795ab4615d5af63267405500daae3db4c78344512b35cb878f
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_0E114DF9B3215650
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:0e114df9b3215650c6de9cbd51697868ae21db21911564355da386012eef3afe
  - id: LTP_272A188C039BEA2B
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:272a188c039bea2baec774fc1b03165f007184709fb6b2efe803a6739102db1e
  - id: LTP_34C12DFEB9C8A62A
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:34c12dfeb9c8a62a2b62de07b5bb2d6118af1f1980737fbe1ecb217c7107382d
  - id: LTP_5667C5A09C3EC10E
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:5667c5a09c3ec10e1110edd68f9f141863f54079ca6de1268981398eb63ccfdb
  - id: LTP_5B244D0A4892F35A
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:5b244d0a4892f35add627ada0fc5b533097c10c25331b226453c960b2d337873
  - id: LTP_74BAD566B6A0F272
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:74bad566b6a0f27240f593e3a2a233e57cb8927f4baf73a84bf351ea1c049b28
  - id: LTP_7AF4AAC644090507
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:7af4aac644090507113b22b6706063acd3bc9113dd5b624340c7e10ed5d8410e
  - id: LTP_8BFB8BE2E39B38A1
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:8bfb8be2e39b38a18c2e168882cd879ad69551de0b22d39a604276c5800d3335
  - id: LTP_A030561DFACE8C93
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:a030561dface8c93a84e7859ab595997ce720c805d6a863d6815400ebecb4d64
  - id: LTP_A16555D2419FBCD4
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:a16555d2419fbcd4e5983b68f8c9c2c0650cb2f45963ba2b31a89cc4e6f9cab4
  - id: LTP_BA03F1BD9B5F2BE2
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:ba03f1bd9b5f2be2a92785e6a571d00b86f295628e5d3fd1393c71b7b66a18b9
  - id: LTP_DA65D6C7A0E4ABBC
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:da65d6c7a0e4abbc12ba61464384db59b2ccc9a4215469858de691a4c6deb562
  - id: LTP_F13B0055458E603F
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:f13b0055458e603facaeea464691300d04a210e03afab6ac3fe67c85947c4a02
  evidence_count: 5
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: flistxattr
  source_fingerprint: sha256:1df26fe5b67819ad8f7cf3801f8fd2494aef0efaa875294cbef8edb0fc935bcc
  recognition_fingerprint: sha256:a8b5d7ea6d474a92a777e2cebc29cdb91ea9a843dd4246b5d675b55d56337fc0
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_51E954C969CAFA58
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:51e954c969cafa58524d543aab5699c57b0b8fdc2401496ddc4128f667684e8e
  - id: LTP_609D7178B8A77C1F
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:609d7178b8a77c1f760e1613cdd180971f8a52082857ee05dc4e1860d8870c75
  - id: LTP_C37E693AB7AA5E28
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:c37e693ab7aa5e28cf47747b1e55d478f6766dc3acf88af405f1087dd8759f9f
  - id: LTP_F10E5286CF6CAC64
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:f10e5286cf6cac6482348f669c44ca60b5286950b010dbcad6f7e74c201e60a9
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: flock
  source_fingerprint: sha256:6d04724ae5815e41dbb7838662014447338102d4e5a178acd4a28b48531fef78
  recognition_fingerprint: sha256:eed8c4dabf5b55fd79b6575b1f45df1f91512ebded5db8a328d982aacb4f203f
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_04A84187DEC4CF09
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:04a84187dec4cf09a39d6ca1c97accea65e020ac8a79b7d541d3d215af9fee07
  - id: LTP_245110930B22BF5C
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:245110930b22bf5c23a7fb0a2858242e8f2667f1edc08b79380bc66f38de4f16
  - id: LTP_3AF9CC563B4BAC1C
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:3af9cc563b4bac1cd18296d24c2c04bb129a16239fb9a33f3af25d4d20550fb0
  - id: LTP_44128D8D82BC1E09
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:44128d8d82bc1e0933e93cae52dbe9b095dd8cca45b1f59c918e3a39bc1bd910
  - id: LTP_50FD97B7CD409007
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:50fd97b7cd409007415a42a5a18165fdaf2dc32f34e00c33b8c1abd820aa01f5
  - id: LTP_6A70899352D69A0B
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:6a70899352d69a0b72a8408a0c9b9fdbfefbf2b4c2020fc413cc7ca20a82e7eb
  - id: LTP_7EAD5A075576B981
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:7ead5a075576b9813f8c42b9351bdfe2afe4effadc165630af1767f0d8774d67
  - id: LTP_86E690B05A18AF6A
    generated_at_utc: '2026-07-16T02:52:01.871423Z'
    content_hash: sha256:86e690b05a18af6ab66ede06e3f1b5ceeb8296c574a2e674598d2d2a2d7bf744
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
  recognition_fingerprint: sha256:9c6378e0387cf7a54750dc9f405a27ca506d537d6af89cab8db75017775f7a0d
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: fork
  source_fingerprint: sha256:cced5d1a1b3d08a3c57b7c29d15fdf132aded15a5dd8eb1fd1ae05b2f5fd4a2d
  recognition_fingerprint: sha256:975c484634deab6bf9b715035c858c16e96086410685286701f7c6b625675cc5
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 17
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: fpathconf
  source_fingerprint: sha256:73901aa0c6a6d05a52445fb7d429158b373e8eb3f2a3d37ca853fd645ccbb3f4
  recognition_fingerprint: sha256:96f68fbc1049cd74964725d3bd75d386314c7ab449cd5959ba5763e7592fa7cf
  selection_reason: new
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
  recognition_fingerprint: sha256:8681994b8599d604a6486abc90b204af4e41b201c47acfef655ad3eede412c1e
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: fsconfig
  source_fingerprint: sha256:5f21700ba19ea2010f3e8cf314d7d5c985eff4fadc9bb314d1cc1e30ee44e5a9
  recognition_fingerprint: sha256:97f5efcdda898e781908aca72fe6d5b126909990b39142c5f9cd310fc9ad8304
  selection_reason: new
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
  recognition_fingerprint: sha256:3edbd679e31258ae63af8380e0addbdbd88af6d53e40a567b8a368075a1435f3
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 4
  reason: unresolved_evidence
- syscall: fsmount
  source_fingerprint: sha256:4cb0a96ad974cf2f8cc60f89bb599509e6b626a7f68d80417dcc6302afc52f12
  recognition_fingerprint: sha256:f1a25e935ba1a5cf9b6ae9f9ee535a47558935f0395adf2c6d02ab518077918a
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: fsopen
  source_fingerprint: sha256:e68be8a61d079622229c3509eae66a221e1af386915bfbcc08013d946d79c3b6
  recognition_fingerprint: sha256:acbb2922632afe18d4786a6b984c4a968c049d52a58f65a5585d43b7602f241d
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
```
</details>
