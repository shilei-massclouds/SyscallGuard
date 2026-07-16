# Starry 合规检查报告

## 本轮结论

- 状态：`completed`
- 静态检查：pass 24、fail 4、error 0
- 动态测试：pass 7、fail 0、skipped 0、not_run 0
- confirmed finding：35
- 新增：0、carry forward：30、已重验：6、待重验：30
- 环境或执行 blocker：0（不视为实现缺口）

## 静态检查

### `STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS`

- 类型：`static`
- 关联 syscall：`close_range`
- 通用规则：`LTP_425E5A3502541DE8`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_close_range\(first: u32, last: u32, flags: u32\)`：matched=`true`，第 489 行
  - `pub fn sys_close_range\([\s\S]*?for fd in first\.\.=last\.min\(max_index as u32\)[\s\S]*?Ok\(0\)`：matched=`true`，第 489 行
- finding：—

### `STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO`

- 类型：`static`
- 关联 syscall：`copy_file_range`
- 通用规则：`LTP_74BB3F96CBA52D02`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_copy_file_range\([\s\S]*?if len > isize::MAX as usize \{[\s\S]*?return Err\(AxError::from\(LinuxError::EOVERFLOW\)\);`：matched=`true`，第 773 行
- finding：—

### `STARRY_EPOLL_NESTED_LOOP`

- 类型：`static`
- 关联 syscall：`epoll_ctl`
- 通用规则：`LTP_66C670178B06E9F3`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn add\([\s\S]*?downcast_arc::<Epoll>\(\)[\s\S]*?reaches_epoll\([\s\S]*?AxError::FilesystemLoop`：matched=`true`，第 501 行
- finding：—

### `STARRY_FINAL_ERRNO_TRANSLATION`

- 类型：`static`
- 关联 syscall：`symlink`、`sysinfo`、`syslog`、`timer_delete`、`tkill`、`umount`、`uname`、`unshare`、`waitid`、`waitpid`、`write`
- 通用规则：`LTP_02908A57586A60CF`、`LTP_10B3572DBFA6742B`、`LTP_22F13AFD9925B2AE`、`LTP_25D7B6229831E0EF`、`LTP_287CF10D893735AB`、`LTP_4184881E196F9E5E`、`LTP_498695B75BD43DAD`、`LTP_4FCD61E2EED61335`、`LTP_6B9F97B897EC5C32`、`LTP_6D02D744B460F97E`、`LTP_82A8802A27A3D2BF`、`LTP_89AC9F4AA9032B8D`、`LTP_9FD87A3F7688FEF1`、`LTP_B212BAAA2C2C75CC`、`LTP_C8376BC347F94A98`、`LTP_C8F11074F91F94EF`、`LTP_DB77907DDC5EDFF4`、`LTP_E272B715ECA16E6C`、`LTP_F92CEB15161CB23C`、`LTP_FCC236A4D5926B81`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `BadAddress \\| BadState => EFAULT`：matched=`true`，第 223 行
  - `BadFileDescriptor => EBADF`：matched=`true`，第 224 行
  - `InvalidInput \\| InvalidData => EINVAL`：matched=`true`，第 235 行
  - `OperationNotPermitted => EPERM`：matched=`true`，第 250 行
- finding：—

### `STARRY_FINAL_SYMLINK_USER_POINTERS`

- 类型：`static`
- 关联 syscall：`symlink`
- 通用规则：`LTP_C8F11074F91F94EF`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_symlinkat\([\s\S]*?vm_load_string\(target\)\?;[\s\S]*?vm_load_path_string\(linkpath\)\?;`：matched=`true`，第 440 行
- finding：—

### `STARRY_FINAL_SYSINFO_COPYOUT`

- 类型：`static`
- 关联 syscall：`sysinfo`
- 通用规则：`LTP_A367723236ADA8B4`、`LTP_B212BAAA2C2C75CC`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_sysinfo\([\s\S]*?kinfo\.uptime[\s\S]*?kinfo\.totalram[\s\S]*?kinfo\.freeram[\s\S]*?kinfo\.procs[\s\S]*?info\.vm_write\(kinfo\)\?;\s*Ok\(0\)`：matched=`true`，第 720 行
- finding：—

### `STARRY_FINAL_SYSLOG_CONSOLE_LEVEL`

- 类型：`static`
- 关联 syscall：`syslog`
- 通用规则：`LTP_02908A57586A60CF`、`LTP_18304438A1D5D6C1`、`LTP_4FCD61E2EED61335`、`LTP_C0694665E22D48E8`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `SYSLOG_ACTION_CONSOLE_LEVEL => \{[\s\S]*?if !\(1\.\.=8\)\.contains\(&len\) \{\s*return Err\(AxError::InvalidInput\);`：matched=`true`，第 808 行
  - `let old_level = state\.console_level;\s*state\.console_level = len;\s*Ok\(old_level as isize\)`：matched=`true`，第 814 行
- finding：—

### `STARRY_FINAL_SYSLOG_CONTROL_ACTIONS`

- 类型：`static`
- 关联 syscall：`syslog`
- 通用规则：`LTP_4828EB12592F311C`、`LTP_6D819B66D5B60871`、`LTP_7F4262FC753FC8D9`、`LTP_F38A837D067865DC`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `SYSLOG_ACTION_CLOSE \\| SYSLOG_ACTION_OPEN => Ok\(0\)`：matched=`true`，第 754 行
  - `SYSLOG_ACTION_CONSOLE_OFF => \{[\s\S]*?console_enabled = false;[\s\S]*?SYSLOG_ACTION_CONSOLE_ON => \{[\s\S]*?console_enabled = true;`：matched=`true`，第 796 行
- finding：—

### `STARRY_FINAL_SYSLOG_INVALID_ACTION`

- 类型：`static`
- 关联 syscall：`syslog`
- 通用规则：`LTP_4184881E196F9E5E`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_syslog\([\s\S]*?_ => Err\(AxError::InvalidInput\),\s*\}`：matched=`true`，第 752 行
- finding：—

### `STARRY_FINAL_SYSLOG_PRIVILEGE`

- 类型：`static`
- 关联 syscall：`syslog`
- 通用规则：`LTP_498695B75BD43DAD`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `fn require_syslog_privilege\([\s\S]*?euid == 0[\s\S]*?Err\(AxError::OperationNotPermitted\)`：matched=`true`，第 744 行
  - `SYSLOG_ACTION_READ => \{\s*(?:validate_syslog_read_args\(buf, len\)\?;\s*)?require_syslog_privilege\(\)\?;`：matched=`true`，第 755 行
- finding：—

### `STARRY_FINAL_SYSLOG_READ_ARGUMENTS`

- 类型：`static`
- 关联 syscall：`syslog`
- 通用规则：`LTP_6B9F97B897EC5C32`、`LTP_C8376BC347F94A98`
- 结果：`fail`
- 原因：one or more required patterns did not match
- pattern 证据：

  - `SYSLOG_ACTION_READ => \{\s*validate_syslog_read_args\(buf, len\)\?;`：matched=`false`，未匹配
  - `SYSLOG_ACTION_READ_ALL => \{\s*validate_syslog_read_args\(buf, len\)\?;`：matched=`false`，未匹配
- finding：`finding-syslog-ltp-6b9f97b897ec5c32-444533f79a99`、`finding-syslog-ltp-c8376bc347f94a98-444533f79a99`

### `STARRY_FINAL_TIMER_DELETE`

- 类型：`static`
- 关联 syscall：`timer_delete`
- 通用规则：`LTP_10B3572DBFA6742B`、`LTP_9B36D27A4A2994D0`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_timer_delete\([\s\S]*?posix_timers\.delete\(timerid\) \{\s*Ok\(0\)\s*\} else \{\s*Err\(AxError::InvalidInput\)`：matched=`true`，第 268 行
- finding：—

### `STARRY_FINAL_TKILL_TID_VALIDATION`

- 类型：`static`
- 关联 syscall：`tkill`
- 通用规则：`LTP_FCC236A4D5926B81`
- 结果：`fail`
- 原因：one or more required patterns did not match
- pattern 证据：

  - `pub fn sys_tkill\([\s\S]*?if tid <= 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}`：matched=`false`，未匹配
- finding：`finding-tkill-ltp-fcc236a4d5926b81-444533f79a99`

### `STARRY_FINAL_UMOUNT_MOUNTPOINT`

- 类型：`static`
- 关联 syscall：`umount`
- 通用规则：`LTP_E272B715ECA16E6C`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `if !target\.is_root_of_mount\(\) \{\s*return Err\(AxError::InvalidInput\);`：matched=`true`，第 140 行
- finding：—

### `STARRY_FINAL_UMOUNT_PRIVILEGE`

- 类型：`static`
- 关联 syscall：`umount`
- 通用规则：`LTP_287CF10D893735AB`
- 结果：`fail`
- 原因：one or more required patterns did not match
- pattern 证据：

  - `pub fn sys_umount2\([\s\S]*?has_cap_sys_admin\(\)[\s\S]*?return Err\(AxError::OperationNotPermitted\);`：matched=`false`，未匹配
- finding：`finding-umount-ltp-287cf10d893735ab-444533f79a99`

### `STARRY_FINAL_UMOUNT_USER_PATH`

- 类型：`static`
- 关联 syscall：`umount`
- 通用规则：`LTP_6D02D744B460F97E`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_umount2\([\s\S]*?let target = vm_load_string\(target\)\?;`：matched=`true`，第 297 行
- finding：—

### `STARRY_FINAL_UNAME_COPYOUT`

- 类型：`static`
- 关联 syscall：`uname`
- 通用规则：`LTP_25D7B6229831E0EF`、`LTP_5516B8A938B9C3A5`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_uname\([\s\S]*?build_utsname\(&ns\)[\s\S]*?name\.vm_write\(uts\)\?;\s*Ok\(0\)`：matched=`true`，第 662 行
- finding：—

### `STARRY_FINAL_UNSHARE_FLAG_VALIDATION`

- 类型：`static`
- 关联 syscall：`unshare`
- 通用规则：`LTP_F92CEB15161CB23C`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_unshare\([\s\S]*?flags & !SUPPORTED_NS_FLAGS != 0[\s\S]*?return Err\(AxError::InvalidInput\);`：matched=`true`，第 25 行
- finding：—

### `STARRY_FINAL_UNSHARE_NEWNS_PRIVILEGE`

- 类型：`static`
- 关联 syscall：`unshare`
- 通用规则：`LTP_82A8802A27A3D2BF`
- 结果：`fail`
- 原因：one or more required patterns did not match
- pattern 证据：

  - `flags & CLONE_NEWNS != 0[\s\S]*?![\s\S]*?has_cap_sys_admin\(\)[\s\S]*?return Err\(AxError::OperationNotPermitted\);`：matched=`false`，未匹配
- finding：`finding-unshare-ltp-82a8802a27a3d2bf-444533f79a99`

### `STARRY_FINAL_WAITID_OPTIONS`

- 类型：`static`
- 关联 syscall：`waitid`
- 通用规则：`LTP_9FD87A3F7688FEF1`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `if !options[\s\S]*?intersects\(WaitIdOptions::WEXITED \\| WaitIdOptions::WUNTRACED \\| WaitIdOptions::WCONTINUED\)[\s\S]*?return Err\(AxError::InvalidInput\);`：matched=`true`，第 382 行
- finding：—

### `STARRY_FINAL_WAITPID_OPTIONS`

- 类型：`static`
- 关联 syscall：`waitpid`
- 通用规则：`LTP_DB77907DDC5EDFF4`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_waitpid\([\s\S]*?WaitPidOptions::from_bits\(options\)\.ok_or\(AxError::InvalidInput\)\?;`：matched=`true`，第 234 行
- finding：—

### `STARRY_FINAL_WRITE_BAD_FD`

- 类型：`static`
- 关联 syscall：`write`
- 通用规则：`LTP_22F13AFD9925B2AE`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_write\([\s\S]*?let file_like = get_file_like\(fd\)\?;[\s\S]*?validate_user_read_buf`：matched=`true`，第 138 行
- finding：—

### `STARRY_FINAL_WRITE_USER_BUFFER`

- 类型：`static`
- 关联 syscall：`write`
- 通用规则：`LTP_89AC9F4AA9032B8D`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `validate_user_read_buf\(buf\.cast_const\(\), len\)\?;[\s\S]*?copy_user_read_buf\(buf\.cast_const\(\), len\)\?;`：matched=`true`，第 141 行
- finding：—

### `STARRY_FINIT_MODULE_FLAG_VALIDATION`

- 类型：`static`
- 关联 syscall：`finit_module`
- 通用规则：`LTP_DA65D6C7A0E4ABBC`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_finit_module\(module_fd: i32, param_ptr: \*const u8, flags: u32\)`：matched=`true`，第 46 行
  - `pub fn sys_finit_module\([\s\S]*?if flags != 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}`：matched=`true`，第 46 行
- finding：—

### `STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE`

- 类型：`static`
- 关联 syscall：`gettimeofday`
- 通用规则：`LTP_6C14DE68E3C0CC24`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_gettimeofday\(ts: \*mut timeval, tz: \*mut Timezone\)`：matched=`true`，第 43 行
  - `tz\.nullable\(\)[\s\S]*?tz\.vm_write\(Timezone::default\(\)\)\?;`：matched=`true`，第 47 行
- finding：—

### `STARRY_ROUND3_INIT_MODULE_PERMISSION`

- 类型：`static`
- 关联 syscall：`init_module`
- 通用规则：`LTP_D246498B20D9CB2C`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_init_module\([\s\S]*?if !current\(\)\.as_thread\(\)\.cred\(\)\.has_cap_sys_module\(\)`：matched=`true`，第 22 行
  - `pub fn sys_init_module\([\s\S]*?has_cap_sys_module\(\)[\s\S]*?return Err\(AxError::OperationNotPermitted\);[\s\S]*?VmBytes::new`：matched=`true`，第 22 行
- finding：—

### `STARRY_ROUND5_SETPGID_NEGATIVE`

- 类型：`static`
- 关联 syscall：`setpgid`
- 通用规则：`LTP_4308D71D8BD6519D`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_setpgid\(pid: i32, pgid: i32\) -> AxResult<isize>`：matched=`true`，第 40 行
  - `pub fn sys_setpgid\([\s\S]*?if pid < 0 \\|\\| pgid < 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}`：matched=`true`，第 40 行
- finding：—

### `STARRY_ROUND5_SOCKET_INVALID_TYPE`

- 类型：`static`
- 关联 syscall：`socket`
- 通用规则：`LTP_971DB17D32C51561`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_socket\([\s\S]*?\(AF_INET \\| AF_INET6, _\) \\| \(AF_UNIX, _\) \\| \(AF_NETLINK, _\) \\| \(AF_VSOCK, _\) => \{[\s\S]*?return Err\(AxError::InvalidInput\);[\s\S]*?\n\}\n\npub fn sys_bind`：matched=`true`，第 35 行
- finding：—

## 动态测试

### `STARRY_FINAL_SYSINFO_BEHAVIOR`

- 类型：`dynamic`
- 关联 syscall：`sysinfo`
- 通用规则：`LTP_A367723236ADA8B4`、`LTP_B212BAAA2C2C75CC`
- 结果：`pass`
- 原因：command exited successfully
- 退出码：`0`
- 精简输出证据：

```text
unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//etc/nsswitch.conf
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//etc/modules
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//etc/inittab
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//etc/hosts
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//etc/hostname
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//etc/group
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//etc/fstab
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//etc/resolv.conf
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//etc
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/tmp
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/spool/cron
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/spool
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/opt
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/mail
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/local
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/lib/misc
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/lib
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/empty
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/cache/apk
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/cache/misc
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/cache
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/log/apk.log
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/log
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//guest/linux/linux-qemu
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//guest/linux/manifest.txt
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//guest/linux
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//guest/nimbos/manifest.txt
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//guest/nimbos/nimbos-qemu
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//guest/nimbos/nimbos-qemu-usertests
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//guest/nimbos/nimbos-qemu.img
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//guest/nimbos
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//guest
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root/
cd /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system && /home/cloud/gitWork/qemu-10.2.1/build/qemu-riscv64 -L /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root/bin/busybox sh -eu /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system/prebuild.sh
/usr/bin/cmake -S /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system -B /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/build -G 'Unix Makefiles' -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/ -DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY -DCMAKE_TOOLCHAIN_FILE=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/cmake-toolchain.cmake -DCMAKE_MAKE_PROGRAM=/usr/bin/make -DPKG_CONFIG_EXECUTABLE=/usr/bin/pkg-config -DSTARRY_STAGING_ROOT=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root -DSTARRY_GROUPED_C_SUBCASES=test-sysinfo
CMake Warning:
  Manually-specified variables were not used by the project:

    PKG_CONFIG_EXECUTABLE
    STARRY_STAGING_ROOT


/usr/bin/cmake --build /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/build --parallel
/usr/bin/cmake --install /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/build
debugfs -w /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/case-rootfs.img
debugfs 1.46.5 (30-Dec-2021)
rm: File not found by ext2_lookup while trying to resolve filename
rm: File not found by ext2_lookup while trying to resolve filename
rm: File not found by ext2_lookup while trying to resolve filename
```
- finding：—

### `STARRY_FINAL_SYSLOG_BEHAVIOR`

- 类型：`dynamic`
- 关联 syscall：`syslog`
- 通用规则：`LTP_02908A57586A60CF`、`LTP_18304438A1D5D6C1`、`LTP_330C66A049727F75`、`LTP_4184881E196F9E5E`、`LTP_4828EB12592F311C`、`LTP_498695B75BD43DAD`、`LTP_4FCD61E2EED61335`、`LTP_6D819B66D5B60871`、`LTP_7F4262FC753FC8D9`、`LTP_C0694665E22D48E8`、`LTP_E7CB95EADCE845E9`、`LTP_F38A837D067865DC`
- 结果：`pass`
- 原因：command exited successfully
- 退出码：`0`
- 精简输出证据：

```text
-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//etc/nsswitch.conf
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//etc/modules
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//etc/inittab
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//etc/hosts
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//etc/hostname
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//etc/group
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//etc/fstab
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//etc/resolv.conf
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//etc
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/tmp
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/spool/cron
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/spool
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/opt
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/mail
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/local
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/lib/misc
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/lib
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/empty
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/cache/apk
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/cache/misc
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/cache
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/log/apk.log
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/log
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//guest/linux/linux-qemu
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//guest/linux/manifest.txt
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//guest/linux
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//guest/nimbos/manifest.txt
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//guest/nimbos/nimbos-qemu
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//guest/nimbos/nimbos-qemu-usertests
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//guest/nimbos/nimbos-qemu.img
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//guest/nimbos
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//guest
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root/
cd /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system && /home/cloud/gitWork/qemu-10.2.1/build/qemu-riscv64 -L /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root/bin/busybox sh -eu /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system/prebuild.sh
/usr/bin/cmake -S /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system -B /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/build -G 'Unix Makefiles' -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/ -DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY -DCMAKE_TOOLCHAIN_FILE=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/cmake-toolchain.cmake -DCMAKE_MAKE_PROGRAM=/usr/bin/make -DPKG_CONFIG_EXECUTABLE=/usr/bin/pkg-config -DSTARRY_STAGING_ROOT=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root -DSTARRY_GROUPED_C_SUBCASES=test-syslog
CMake Warning:
  Manually-specified variables were not used by the project:

    PKG_CONFIG_EXECUTABLE
    STARRY_STAGING_ROOT


/usr/bin/cmake --build /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/build --parallel
/usr/bin/cmake --install /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/build
debugfs -w /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/case-rootfs.img
debugfs 1.46.5 (30-Dec-2021)
rm: File not found by ext2_lookup while trying to resolve filename
rm: File not found by ext2_lookup while trying to resolve filename
rm: File not found by ext2_lookup while trying to resolve filename
```
- finding：—

### `STARRY_FINAL_TIMER_DELETE_BEHAVIOR`

- 类型：`dynamic`
- 关联 syscall：`timer_delete`
- 通用规则：`LTP_10B3572DBFA6742B`、`LTP_9B36D27A4A2994D0`
- 结果：`pass`
- 原因：command exited successfully
- 退出码：`0`
- 精简输出证据：

```text
elf/qemu-cases/qemu/system/runs/86919-0/staging-root//etc/nsswitch.conf
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//etc/modules
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//etc/inittab
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//etc/hosts
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//etc/hostname
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//etc/group
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//etc/fstab
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//etc/resolv.conf
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//etc
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/tmp
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/spool/cron
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/spool
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/opt
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/mail
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/local
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/lib/misc
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/lib
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/empty
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/cache/apk
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/cache/misc
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/cache
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/log/apk.log
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/log
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//guest/linux/linux-qemu
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//guest/linux/manifest.txt
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//guest/linux
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//guest/nimbos/manifest.txt
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//guest/nimbos/nimbos-qemu
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//guest/nimbos/nimbos-qemu-usertests
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//guest/nimbos/nimbos-qemu.img
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//guest/nimbos
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//guest
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root/
cd /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system && /home/cloud/gitWork/qemu-10.2.1/build/qemu-riscv64 -L /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root/bin/busybox sh -eu /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system/prebuild.sh
/usr/bin/cmake -S /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system -B /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/build -G 'Unix Makefiles' -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/ -DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY -DCMAKE_TOOLCHAIN_FILE=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/cmake-toolchain.cmake -DCMAKE_MAKE_PROGRAM=/usr/bin/make -DPKG_CONFIG_EXECUTABLE=/usr/bin/pkg-config -DSTARRY_STAGING_ROOT=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root -DSTARRY_GROUPED_C_SUBCASES=syscall-test-timer-family
CMake Warning:
  Manually-specified variables were not used by the project:

    PKG_CONFIG_EXECUTABLE
    STARRY_STAGING_ROOT


/usr/bin/cmake --build /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/build --parallel
/usr/bin/cmake --install /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/build
debugfs -w /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/case-rootfs.img
debugfs 1.46.5 (30-Dec-2021)
rm: File not found by ext2_lookup while trying to resolve filename
rm: File not found by ext2_lookup while trying to resolve filename
rm: File not found by ext2_lookup while trying to resolve filename
```
- finding：—

### `STARRY_FINAL_UNAME_BEHAVIOR`

- 类型：`dynamic`
- 关联 syscall：`uname`
- 通用规则：`LTP_25D7B6229831E0EF`、`LTP_5516B8A938B9C3A5`
- 结果：`pass`
- 原因：command exited successfully
- 退出码：`0`
- 精简输出证据：

```text
c-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//etc/nsswitch.conf
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//etc/modules
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//etc/inittab
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//etc/hosts
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//etc/hostname
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//etc/group
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//etc/fstab
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//etc/resolv.conf
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//etc
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/tmp
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/spool/cron
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/spool
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/opt
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/mail
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/local
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/lib/misc
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/lib
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/empty
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/cache/apk
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/cache/misc
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/cache
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/log/apk.log
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/log
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//guest/linux/linux-qemu
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//guest/linux/manifest.txt
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//guest/linux
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//guest/nimbos/manifest.txt
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//guest/nimbos/nimbos-qemu
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//guest/nimbos/nimbos-qemu-usertests
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//guest/nimbos/nimbos-qemu.img
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//guest/nimbos
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//guest
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root/
cd /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system && /home/cloud/gitWork/qemu-10.2.1/build/qemu-riscv64 -L /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root/bin/busybox sh -eu /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system/prebuild.sh
/usr/bin/cmake -S /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system -B /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/build -G 'Unix Makefiles' -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/ -DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY -DCMAKE_TOOLCHAIN_FILE=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/cmake-toolchain.cmake -DCMAKE_MAKE_PROGRAM=/usr/bin/make -DPKG_CONFIG_EXECUTABLE=/usr/bin/pkg-config -DSTARRY_STAGING_ROOT=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root -DSTARRY_GROUPED_C_SUBCASES=test-uname
CMake Warning:
  Manually-specified variables were not used by the project:

    PKG_CONFIG_EXECUTABLE
    STARRY_STAGING_ROOT


/usr/bin/cmake --build /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/build --parallel
/usr/bin/cmake --install /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/build
debugfs -w /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/case-rootfs.img
debugfs 1.46.5 (30-Dec-2021)
rm: File not found by ext2_lookup while trying to resolve filename
rm: File not found by ext2_lookup while trying to resolve filename
rm: File not found by ext2_lookup while trying to resolve filename
```
- finding：—

### `STARRY_FINAL_WAIT4_BEHAVIOR`

- 类型：`dynamic`
- 关联 syscall：`wait4`、`waitpid`
- 通用规则：`LTP_2AE73292A13647D5`、`LTP_DB77907DDC5EDFF4`
- 结果：`pass`
- 原因：command exited successfully
- 退出码：`0`
- 精简输出证据：

```text
u-cases/qemu/system/runs/87788-0/staging-root//etc/nsswitch.conf
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//etc/modules
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//etc/inittab
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//etc/hosts
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//etc/hostname
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//etc/group
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//etc/fstab
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//etc/resolv.conf
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//etc
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/tmp
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/spool/cron
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/spool
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/opt
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/mail
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/local
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/lib/misc
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/lib
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/empty
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/cache/apk
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/cache/misc
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/cache
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/log/apk.log
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/log
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//guest/linux/linux-qemu
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//guest/linux/manifest.txt
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//guest/linux
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//guest/nimbos/manifest.txt
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//guest/nimbos/nimbos-qemu
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//guest/nimbos/nimbos-qemu-usertests
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//guest/nimbos/nimbos-qemu.img
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//guest/nimbos
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//guest
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root/
cd /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system && /home/cloud/gitWork/qemu-10.2.1/build/qemu-riscv64 -L /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root/bin/busybox sh -eu /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system/prebuild.sh
/usr/bin/cmake -S /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system -B /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/build -G 'Unix Makefiles' -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/ -DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY -DCMAKE_TOOLCHAIN_FILE=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/cmake-toolchain.cmake -DCMAKE_MAKE_PROGRAM=/usr/bin/make -DPKG_CONFIG_EXECUTABLE=/usr/bin/pkg-config -DSTARRY_STAGING_ROOT=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root -DSTARRY_GROUPED_C_SUBCASES=bugfix-bug-wait4-invalid-options
CMake Warning:
  Manually-specified variables were not used by the project:

    PKG_CONFIG_EXECUTABLE
    STARRY_STAGING_ROOT


/usr/bin/cmake --build /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/build --parallel
/usr/bin/cmake --install /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/build
debugfs -w /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/case-rootfs.img
debugfs 1.46.5 (30-Dec-2021)
rm: File not found by ext2_lookup while trying to resolve filename
rm: File not found by ext2_lookup while trying to resolve filename
rm: File not found by ext2_lookup while trying to resolve filename
```
- finding：—

### `STARRY_FINAL_WAITID_BEHAVIOR`

- 类型：`dynamic`
- 关联 syscall：`waitid`
- 通用规则：`LTP_0FE0E20EAC6DE889`、`LTP_53E7B9C40A44F6D0`、`LTP_74C73CBABE325D5D`、`LTP_77C2FB4A0A9E30F2`、`LTP_9FD87A3F7688FEF1`
- 结果：`pass`
- 原因：command exited successfully
- 退出码：`0`
- 精简输出证据：

```text
emu-cases/qemu/system/runs/88223-0/staging-root//etc/nsswitch.conf
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//etc/modules
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//etc/inittab
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//etc/hosts
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//etc/hostname
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//etc/group
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//etc/fstab
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//etc/resolv.conf
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//etc
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/tmp
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/spool/cron
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/spool
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/opt
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/mail
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/local
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/lib/misc
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/lib
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/empty
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/cache/apk
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/cache/misc
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/cache
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/log/apk.log
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/log
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//guest/linux/linux-qemu
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//guest/linux/manifest.txt
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//guest/linux
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//guest/nimbos/manifest.txt
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//guest/nimbos/nimbos-qemu
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//guest/nimbos/nimbos-qemu-usertests
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//guest/nimbos/nimbos-qemu.img
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//guest/nimbos
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//guest
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root/
cd /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system && /home/cloud/gitWork/qemu-10.2.1/build/qemu-riscv64 -L /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root/bin/busybox sh -eu /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system/prebuild.sh
/usr/bin/cmake -S /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system -B /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/build -G 'Unix Makefiles' -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/ -DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY -DCMAKE_TOOLCHAIN_FILE=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/cmake-toolchain.cmake -DCMAKE_MAKE_PROGRAM=/usr/bin/make -DPKG_CONFIG_EXECUTABLE=/usr/bin/pkg-config -DSTARRY_STAGING_ROOT=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root -DSTARRY_GROUPED_C_SUBCASES=zombie-bugfix-bug-waitid-basic
CMake Warning:
  Manually-specified variables were not used by the project:

    PKG_CONFIG_EXECUTABLE
    STARRY_STAGING_ROOT


/usr/bin/cmake --build /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/build --parallel
/usr/bin/cmake --install /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/build
debugfs -w /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/case-rootfs.img
debugfs 1.46.5 (30-Dec-2021)
rm: File not found by ext2_lookup while trying to resolve filename
rm: File not found by ext2_lookup while trying to resolve filename
rm: File not found by ext2_lookup while trying to resolve filename
```
- finding：—

### `STARRY_FINAL_WRITE_FILE_BEHAVIOR`

- 类型：`dynamic`
- 关联 syscall：`write`
- 通用规则：`LTP_1B4A2A1831541F06`、`LTP_22F13AFD9925B2AE`
- 结果：`pass`
- 原因：command exited successfully
- 退出码：`0`
- 精简输出证据：

```text
n-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//etc/nsswitch.conf
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//etc/modules
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//etc/inittab
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//etc/hosts
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//etc/hostname
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//etc/group
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//etc/fstab
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//etc/resolv.conf
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//etc
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/tmp
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/spool/cron
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/spool
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/opt
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/mail
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/local
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/lib/misc
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/lib
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/empty
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/cache/apk
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/cache/misc
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/cache
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/log/apk.log
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/log
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//guest/linux/linux-qemu
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//guest/linux/manifest.txt
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//guest/linux
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//guest/nimbos/manifest.txt
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//guest/nimbos/nimbos-qemu
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//guest/nimbos/nimbos-qemu-usertests
dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//guest/nimbos/nimbos-qemu.img
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//guest/nimbos
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//guest
rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root/
cd /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system && /home/cloud/gitWork/qemu-10.2.1/build/qemu-riscv64 -L /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root/bin/busybox sh -eu /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system/prebuild.sh
/usr/bin/cmake -S /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system -B /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/build -G 'Unix Makefiles' -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/ -DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY -DCMAKE_TOOLCHAIN_FILE=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/cmake-toolchain.cmake -DCMAKE_MAKE_PROGRAM=/usr/bin/make -DPKG_CONFIG_EXECUTABLE=/usr/bin/pkg-config -DSTARRY_STAGING_ROOT=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root -DSTARRY_GROUPED_C_SUBCASES=syscall-test-write
CMake Warning:
  Manually-specified variables were not used by the project:

    PKG_CONFIG_EXECUTABLE
    STARRY_STAGING_ROOT


/usr/bin/cmake --build /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/build --parallel
/usr/bin/cmake --install /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/build
debugfs -w /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/case-rootfs.img
debugfs 1.46.5 (30-Dec-2021)
rm: File not found by ext2_lookup while trying to resolve filename
rm: File not found by ext2_lookup while trying to resolve filename
rm: File not found by ext2_lookup while trying to resolve filename
```
- finding：—

<details>
<summary>机器可读元数据</summary>

<!-- syscallguard-metadata -->
```yaml
schema_version: 1
kind: syscallguard_check_report
report_id: check-20260716t122612z-272bbd3a
status: completed
generated_at_utc: '2026-07-16T12:39:03.254257Z'
mapping_report_id: mapping-20260716t122422z-159bda4d
mapping_report_version:
  id: mapping-20260716t122422z-159bda4d
  generated_at_utc: '2026-07-16T12:25:48.158091Z'
  content_hash: sha256:757e81214d7e1c6841bc9cf4831ade67b5c8c8bfb4730023e016c8c32e9ca42b
target:
  target_id: starry
  repository: /home/cloud/gitLinux/tgoskits
  repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
  branch: dev-syscalls-compliance-1
  descriptor_hash: sha256:6b982bb80e3a0a3cf408d7c696367996422e3dac8376577222e56ee47f111d24
  snapshot_hash: sha256:444533f79a99575b82552aaca4a4a99d006322491b7c1fd8f913dfc2542e0afa
input_hash: sha256:1130447365c06df25f1d555f5a91d790592f666ed786614d6262a1d397154319
entity_hashes:
  rules:
    LTP_02908A57586A60CF: sha256:02908a57586a60cf97975b8f95394e7951ece1af5dc4a2d4f4d0cfd9e88dcbb5
    LTP_0FE0E20EAC6DE889: sha256:0fe0e20eac6de8892477791e90bb41b553ac27e1e89cdf43a46481d27780b7da
    LTP_10B3572DBFA6742B: sha256:10b3572dbfa6742b44e40e6ffb78f797d484d1c0f37cedc5e4bc5c0099e8b498
    LTP_18304438A1D5D6C1: sha256:18304438a1d5d6c182245685a0aefa3fcd6f0d75073af8b21b358cd6fde2ed6d
    LTP_1B4A2A1831541F06: sha256:1b4a2a1831541f06f6b87330ac547677379f43e2522608e2dd8572aab65102c4
    LTP_22F13AFD9925B2AE: sha256:22f13afd9925b2ae8222ce9fc99a57aade463bf877958700a932dc0139dbc888
    LTP_25D7B6229831E0EF: sha256:25d7b6229831e0ef4c751d96db2c6b85b6bcacf424ab6ee9d1edad943b336041
    LTP_287CF10D893735AB: sha256:287cf10d893735aba939172ccbac5cf025dd704d8272d5048fb79e3f211821c3
    LTP_2AE73292A13647D5: sha256:2ae73292a13647d5e6dee08daa890622c416f4fa286b8e519b746de14bd3fbf9
    LTP_330C66A049727F75: sha256:330c66a049727f7518cbc03f78e0a13298797ce579a19a07aba3934bf5a032a9
    LTP_4184881E196F9E5E: sha256:4184881e196f9e5efee9a54f53a2a97047ce89fd7abffd3a654b71541e6e9fd8
    LTP_4828EB12592F311C: sha256:4828eb12592f311c667b808fe126e60537995d13c3c3e654866c252c6d5dbeed
    LTP_498695B75BD43DAD: sha256:498695b75bd43dadefde5707b7bcf6e34235569b786f3cce6145ec6b7368b0c0
    LTP_4FCD61E2EED61335: sha256:4fcd61e2eed61335208db28dbb13c3b597c026dc806ec751fae9d6f7b7f08622
    LTP_53E7B9C40A44F6D0: sha256:53e7b9c40a44f6d0d298b3f10007f7160a468a8ca200a36aa444b9b8463f2415
    LTP_5516B8A938B9C3A5: sha256:5516b8a938b9c3a56502a0790304ef99d9caee848e7faaafcdf2f016f6443230
    LTP_6B9F97B897EC5C32: sha256:6b9f97b897ec5c326f9f68e26e9353a0e9bcb1ca59ce6f15c338328a7d201bda
    LTP_6D02D744B460F97E: sha256:6d02d744b460f97e6af278379decd500845ef81c194877b232e8fb2df13af1ae
    LTP_6D819B66D5B60871: sha256:6d819b66d5b60871ddc5afd507de205a17a9c129acbbe65c3bb4fbea8b88690e
    LTP_74C73CBABE325D5D: sha256:74c73cbabe325d5d86536c56b5a7a034406acaa122b54ff7dbab1fe8ce929c58
    LTP_77C2FB4A0A9E30F2: sha256:77c2fb4a0a9e30f26ee316c385213fb42393c0799db581972a7db5c406767132
    LTP_7F4262FC753FC8D9: sha256:7f4262fc753fc8d9c2839c24cd85c23360614c577015c6e3fabc9dd8fb34cf65
    LTP_82A8802A27A3D2BF: sha256:82a8802a27a3d2bf01cb995752e7667b482979d9e93565f11e732bb2a5a31b28
    LTP_89AC9F4AA9032B8D: sha256:89ac9f4aa9032b8d11bb4ae86cf399214fec330c862ae0acea4b7e8158e7e21b
    LTP_9B36D27A4A2994D0: sha256:9b36d27a4a2994d0fb9becad9ddba6985ba56fddf7db2169f2efef4819243591
    LTP_9FD87A3F7688FEF1: sha256:9fd87a3f7688fef10bea92050ac0661fedef311659e6ffce7573ff015c42b21d
    LTP_A367723236ADA8B4: sha256:a367723236ada8b46a0d6d3a444b7812e36d2f96cc8654bcd32ce5076bb39ed0
    LTP_B212BAAA2C2C75CC: sha256:b212baaa2c2c75ccd7b7f34232754295047699d8e2313fb615060af5bd169373
    LTP_C0694665E22D48E8: sha256:c0694665e22d48e81c31be680d5f2b1a220a2e394e1bcceee63d029d46d390b9
    LTP_C8376BC347F94A98: sha256:c8376bc347f94a984bf5b3e6cf3baa97d7f384dde2c141d2a0a70d0693aa589d
    LTP_C8F11074F91F94EF: sha256:c8f11074f91f94ef5feee5145cbdf4f625f9fc0bde00d6b1679588c733686a2c
    LTP_DB77907DDC5EDFF4: sha256:db77907ddc5edff4d8d968e3c7e9d2951a2203061f9a3b0b44d16f3fb2fad3a4
    LTP_E272B715ECA16E6C: sha256:e272b715eca16e6c203ebd024d4823faa94823321108392ec0eeae3a79e23e82
    LTP_E7CB95EADCE845E9: sha256:e7cb95eadce845e91b76c832c765fc7fdd3e86dba6cc61afbaee7f9e89fc5dc2
    LTP_F38A837D067865DC: sha256:f38a837d067865dc1bb5b53c9ed0d922ffc01ea007b07efcc91639965b34e90e
    LTP_F92CEB15161CB23C: sha256:f92ceb15161cb23cd37673ad2b1e78081eaf5d927174f20812d06cca3cf0c67c
    LTP_FCC236A4D5926B81: sha256:fcc236a4d5926b81662f49a2c62c658e9c87bcf2c7e179151e8658bd9395a42f
    LTP_425E5A3502541DE8: sha256:425e5a3502541de863d8b8e88eafb95db2f8d8e1f9cb88a32d8b3124950395b2
    LTP_74BB3F96CBA52D02: sha256:74bb3f96cba52d02850ad3c5e54c87acf278ce51290c99d5ae29da583be9ba38
    LTP_66C670178B06E9F3: sha256:66c670178b06e9f3eae76490edd09b4a26bb0e1c2ccba3c4cbc2a625d12c39bb
    LTP_DA65D6C7A0E4ABBC: sha256:da65d6c7a0e4abbc12ba61464384db59b2ccc9a4215469858de691a4c6deb562
    LTP_6C14DE68E3C0CC24: sha256:6c14de68e3c0cc24bbb7021cd805e26a73df65653f350d8fa8ed8de5232949e8
    LTP_D246498B20D9CB2C: sha256:d246498b20d9cb2cd6ece54014a50e1c77fa08b6a598251c2dc0e3a3700193e2
    LTP_4308D71D8BD6519D: sha256:4308d71d8bd6519d6d2c15cb0c6d1925eed73874700fd6f1c1cc8a86199632a4
    LTP_971DB17D32C51561: sha256:971db17d32c515614f0af38045463319bd4bfb3a661a4ae9e4486c0404c75ead
  static_checks:
    STARRY_FINAL_ERRNO_TRANSLATION: sha256:a937942b5d3f72022b0fddda5d4931b4cb9e86448aa2ac71c03866be6f4cd5f0
    STARRY_FINAL_SYMLINK_USER_POINTERS: sha256:aeeb18ba82e36482d2b059560b756c253ebf1a470876449eabdb6b6718662969
    STARRY_FINAL_SYSINFO_COPYOUT: sha256:df81078edcf15eb541d550d27af9ed25d5edc37b9747b684dc98fecb35d125d4
    STARRY_FINAL_SYSLOG_CONSOLE_LEVEL: sha256:a93427ca41bcbef272c181018b50797e3be5790ee87dff556c66826b4b537a6c
    STARRY_FINAL_SYSLOG_CONTROL_ACTIONS: sha256:1f8c0e5613315af758596f3f7ca2c8023e0aaac1199679d6eb61338856de8b9f
    STARRY_FINAL_SYSLOG_INVALID_ACTION: sha256:f4f907d86f0f6d55c3e478cd10768cc4ac1d0e1164c5be30a553e1b9077e91aa
    STARRY_FINAL_SYSLOG_PRIVILEGE: sha256:898b366254d72d0be9f227af9616a15c23a51b948891098d7e904f7e058792e0
    STARRY_FINAL_SYSLOG_READ_ARGUMENTS: sha256:947467c63df939000091ce9bbfa725b3dac3bd6d9fdb07cbb606a5ef778825f1
    STARRY_FINAL_TIMER_DELETE: sha256:8ff5c8e888e49a2b398a5635edb5e7178a7a931b329d81d05cca24c16d5992de
    STARRY_FINAL_TKILL_TID_VALIDATION: sha256:bd665d5bbc7713aa296dbacb6ebac30037600a425236d51c92829d3e3decb9d5
    STARRY_FINAL_UMOUNT_MOUNTPOINT: sha256:50e93ea5e1c0901013e4dba236236162c2a52317c0e9e4f00dfa81cdcdec54ac
    STARRY_FINAL_UMOUNT_PRIVILEGE: sha256:9076327bc10ad8f7970328c88a4b62abfe9cbdc3118616d23772096e764afae7
    STARRY_FINAL_UMOUNT_USER_PATH: sha256:64d71501fef4076b21c80d31adfdcee70f218add2987c48bef918bd8be98f022
    STARRY_FINAL_UNAME_COPYOUT: sha256:89ae263a7198228815051b926ad692f619f95235e577d6e34b8b56d8dacf050d
    STARRY_FINAL_UNSHARE_FLAG_VALIDATION: sha256:fe91c68b39d03be67abfca6e51090b2077bc8d781a7bb8c90dc9f8e4238497cd
    STARRY_FINAL_UNSHARE_NEWNS_PRIVILEGE: sha256:647346966f4cd913f5bc3219f181a2d9b7f6865ea1decc8e898b1f28751b9842
    STARRY_FINAL_WAITID_OPTIONS: sha256:eb10af7768c3c3f23a2004fa7c4d35545f2f964f533df148d3878b32deabd46c
    STARRY_FINAL_WAITPID_OPTIONS: sha256:94510ad8995d40bcfdfb2883cbdb545a20bbfd35969ef29736af779ab998ec73
    STARRY_FINAL_WRITE_BAD_FD: sha256:30cb4cd9e1e8745efae7743768569c3df3a3525ac67edbc112783b63a5197906
    STARRY_FINAL_WRITE_USER_BUFFER: sha256:3ebdca5d15aafca2b9ee204ced42be9f44610f9af6d35ce20e911473c69512be
    STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS: sha256:6d8ffe193808bde740053a61419adcf0e7c090388b2f5fea0475696c5b402070
    STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO: sha256:39ebc0849b8fede86d9689ed1dba7fda23315b83937a447b328ffd1a94bdfb34
    STARRY_EPOLL_NESTED_LOOP: sha256:d1db97954ea66c6632d4d74191ef0d91751bbbcfee42883a78137bbdaac22e58
    STARRY_FINIT_MODULE_FLAG_VALIDATION: sha256:81ef9eef26bc66571e89435a216d883211029dd798c2e5ce97752ec71f012cf4
    STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE: sha256:e2e77be33c0c00e8b38780cef8b7b9ff37f7271c1a4f1d1289041b8cf68f4817
    STARRY_ROUND3_INIT_MODULE_PERMISSION: sha256:9df3be22e06572f2b77a0e12c13e9bc9c3a498b4317a288e87e880ee8b23d177
    STARRY_ROUND5_SETPGID_NEGATIVE: sha256:5fa6b80a0abd76e0c19c944876cb5f33d7cff69abf8434b9fca9fe1af9d94ac5
    STARRY_ROUND5_SOCKET_INVALID_TYPE: sha256:af3e1dc26481ee71e25429daac3d3eb199d94dbf93c29dfa57c25f0a77e13c3d
  dynamic_tests:
    STARRY_FINAL_SYSINFO_BEHAVIOR: sha256:fde838482f4ddeb1cecc3363a09dae5854676132012b3dabe3d74f2c0a9e4d26
    STARRY_FINAL_SYSLOG_BEHAVIOR: sha256:13d97721ea96c22432a09a47f5bf81b1a3891f986c933598936f55e92e13a80d
    STARRY_FINAL_TIMER_DELETE_BEHAVIOR: sha256:dd1f8207f2596bcf6496320e2c9808cebbbb254ab58c2b6dcf02e0ae4b14feb5
    STARRY_FINAL_UNAME_BEHAVIOR: sha256:39b6422f5203e6b607c4c6f8523376e2ec657618eb94905793989c82ac40b7c0
    STARRY_FINAL_WAIT4_BEHAVIOR: sha256:a96cc2b1d6f032573454b8526a95ea95060aa35160accfa6dd0daf02e6a46e64
    STARRY_FINAL_WAITID_BEHAVIOR: sha256:91e4458bd02931ac8e9d04554a8e27efd57492d03682a63fb1052cec45a6e2c2
    STARRY_FINAL_WRITE_FILE_BEHAVIOR: sha256:9c80afe9885e53c60565698d75929f8c1187b76f6f6f3120e2d4eaf657082526
entity_versions:
  rules:
    LTP_02908A57586A60CF:
      id: LTP_02908A57586A60CF
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:02908a57586a60cf97975b8f95394e7951ece1af5dc4a2d4f4d0cfd9e88dcbb5
    LTP_0FE0E20EAC6DE889:
      id: LTP_0FE0E20EAC6DE889
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:0fe0e20eac6de8892477791e90bb41b553ac27e1e89cdf43a46481d27780b7da
    LTP_10B3572DBFA6742B:
      id: LTP_10B3572DBFA6742B
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:10b3572dbfa6742b44e40e6ffb78f797d484d1c0f37cedc5e4bc5c0099e8b498
    LTP_18304438A1D5D6C1:
      id: LTP_18304438A1D5D6C1
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:18304438a1d5d6c182245685a0aefa3fcd6f0d75073af8b21b358cd6fde2ed6d
    LTP_1B4A2A1831541F06:
      id: LTP_1B4A2A1831541F06
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:1b4a2a1831541f06f6b87330ac547677379f43e2522608e2dd8572aab65102c4
    LTP_22F13AFD9925B2AE:
      id: LTP_22F13AFD9925B2AE
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:22f13afd9925b2ae8222ce9fc99a57aade463bf877958700a932dc0139dbc888
    LTP_25D7B6229831E0EF:
      id: LTP_25D7B6229831E0EF
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:25d7b6229831e0ef4c751d96db2c6b85b6bcacf424ab6ee9d1edad943b336041
    LTP_287CF10D893735AB:
      id: LTP_287CF10D893735AB
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:287cf10d893735aba939172ccbac5cf025dd704d8272d5048fb79e3f211821c3
    LTP_2AE73292A13647D5:
      id: LTP_2AE73292A13647D5
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:2ae73292a13647d5e6dee08daa890622c416f4fa286b8e519b746de14bd3fbf9
    LTP_330C66A049727F75:
      id: LTP_330C66A049727F75
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:330c66a049727f7518cbc03f78e0a13298797ce579a19a07aba3934bf5a032a9
    LTP_4184881E196F9E5E:
      id: LTP_4184881E196F9E5E
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:4184881e196f9e5efee9a54f53a2a97047ce89fd7abffd3a654b71541e6e9fd8
    LTP_4828EB12592F311C:
      id: LTP_4828EB12592F311C
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:4828eb12592f311c667b808fe126e60537995d13c3c3e654866c252c6d5dbeed
    LTP_498695B75BD43DAD:
      id: LTP_498695B75BD43DAD
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:498695b75bd43dadefde5707b7bcf6e34235569b786f3cce6145ec6b7368b0c0
    LTP_4FCD61E2EED61335:
      id: LTP_4FCD61E2EED61335
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:4fcd61e2eed61335208db28dbb13c3b597c026dc806ec751fae9d6f7b7f08622
    LTP_53E7B9C40A44F6D0:
      id: LTP_53E7B9C40A44F6D0
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:53e7b9c40a44f6d0d298b3f10007f7160a468a8ca200a36aa444b9b8463f2415
    LTP_5516B8A938B9C3A5:
      id: LTP_5516B8A938B9C3A5
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:5516b8a938b9c3a56502a0790304ef99d9caee848e7faaafcdf2f016f6443230
    LTP_6B9F97B897EC5C32:
      id: LTP_6B9F97B897EC5C32
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:6b9f97b897ec5c326f9f68e26e9353a0e9bcb1ca59ce6f15c338328a7d201bda
    LTP_6D02D744B460F97E:
      id: LTP_6D02D744B460F97E
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:6d02d744b460f97e6af278379decd500845ef81c194877b232e8fb2df13af1ae
    LTP_6D819B66D5B60871:
      id: LTP_6D819B66D5B60871
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:6d819b66d5b60871ddc5afd507de205a17a9c129acbbe65c3bb4fbea8b88690e
    LTP_74C73CBABE325D5D:
      id: LTP_74C73CBABE325D5D
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:74c73cbabe325d5d86536c56b5a7a034406acaa122b54ff7dbab1fe8ce929c58
    LTP_77C2FB4A0A9E30F2:
      id: LTP_77C2FB4A0A9E30F2
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:77c2fb4a0a9e30f26ee316c385213fb42393c0799db581972a7db5c406767132
    LTP_7F4262FC753FC8D9:
      id: LTP_7F4262FC753FC8D9
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:7f4262fc753fc8d9c2839c24cd85c23360614c577015c6e3fabc9dd8fb34cf65
    LTP_82A8802A27A3D2BF:
      id: LTP_82A8802A27A3D2BF
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:82a8802a27a3d2bf01cb995752e7667b482979d9e93565f11e732bb2a5a31b28
    LTP_89AC9F4AA9032B8D:
      id: LTP_89AC9F4AA9032B8D
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:89ac9f4aa9032b8d11bb4ae86cf399214fec330c862ae0acea4b7e8158e7e21b
    LTP_9B36D27A4A2994D0:
      id: LTP_9B36D27A4A2994D0
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:9b36d27a4a2994d0fb9becad9ddba6985ba56fddf7db2169f2efef4819243591
    LTP_9FD87A3F7688FEF1:
      id: LTP_9FD87A3F7688FEF1
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:9fd87a3f7688fef10bea92050ac0661fedef311659e6ffce7573ff015c42b21d
    LTP_A367723236ADA8B4:
      id: LTP_A367723236ADA8B4
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:a367723236ada8b46a0d6d3a444b7812e36d2f96cc8654bcd32ce5076bb39ed0
    LTP_B212BAAA2C2C75CC:
      id: LTP_B212BAAA2C2C75CC
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:b212baaa2c2c75ccd7b7f34232754295047699d8e2313fb615060af5bd169373
    LTP_C0694665E22D48E8:
      id: LTP_C0694665E22D48E8
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:c0694665e22d48e81c31be680d5f2b1a220a2e394e1bcceee63d029d46d390b9
    LTP_C8376BC347F94A98:
      id: LTP_C8376BC347F94A98
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:c8376bc347f94a984bf5b3e6cf3baa97d7f384dde2c141d2a0a70d0693aa589d
    LTP_C8F11074F91F94EF:
      id: LTP_C8F11074F91F94EF
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:c8f11074f91f94ef5feee5145cbdf4f625f9fc0bde00d6b1679588c733686a2c
    LTP_DB77907DDC5EDFF4:
      id: LTP_DB77907DDC5EDFF4
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:db77907ddc5edff4d8d968e3c7e9d2951a2203061f9a3b0b44d16f3fb2fad3a4
    LTP_E272B715ECA16E6C:
      id: LTP_E272B715ECA16E6C
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:e272b715eca16e6c203ebd024d4823faa94823321108392ec0eeae3a79e23e82
    LTP_E7CB95EADCE845E9:
      id: LTP_E7CB95EADCE845E9
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:e7cb95eadce845e91b76c832c765fc7fdd3e86dba6cc61afbaee7f9e89fc5dc2
    LTP_F38A837D067865DC:
      id: LTP_F38A837D067865DC
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:f38a837d067865dc1bb5b53c9ed0d922ffc01ea007b07efcc91639965b34e90e
    LTP_F92CEB15161CB23C:
      id: LTP_F92CEB15161CB23C
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:f92ceb15161cb23cd37673ad2b1e78081eaf5d927174f20812d06cca3cf0c67c
    LTP_FCC236A4D5926B81:
      id: LTP_FCC236A4D5926B81
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:fcc236a4d5926b81662f49a2c62c658e9c87bcf2c7e179151e8658bd9395a42f
    LTP_425E5A3502541DE8:
      id: LTP_425E5A3502541DE8
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:425e5a3502541de863d8b8e88eafb95db2f8d8e1f9cb88a32d8b3124950395b2
    LTP_74BB3F96CBA52D02:
      id: LTP_74BB3F96CBA52D02
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:74bb3f96cba52d02850ad3c5e54c87acf278ce51290c99d5ae29da583be9ba38
    LTP_66C670178B06E9F3:
      id: LTP_66C670178B06E9F3
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:66c670178b06e9f3eae76490edd09b4a26bb0e1c2ccba3c4cbc2a625d12c39bb
    LTP_DA65D6C7A0E4ABBC:
      id: LTP_DA65D6C7A0E4ABBC
      generated_at_utc: '2026-07-16T02:52:01.871423Z'
      content_hash: sha256:da65d6c7a0e4abbc12ba61464384db59b2ccc9a4215469858de691a4c6deb562
    LTP_6C14DE68E3C0CC24:
      id: LTP_6C14DE68E3C0CC24
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:6c14de68e3c0cc24bbb7021cd805e26a73df65653f350d8fa8ed8de5232949e8
    LTP_D246498B20D9CB2C:
      id: LTP_D246498B20D9CB2C
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:d246498b20d9cb2cd6ece54014a50e1c77fa08b6a598251c2dc0e3a3700193e2
    LTP_4308D71D8BD6519D:
      id: LTP_4308D71D8BD6519D
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:4308d71d8bd6519d6d2c15cb0c6d1925eed73874700fd6f1c1cc8a86199632a4
    LTP_971DB17D32C51561:
      id: LTP_971DB17D32C51561
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:971db17d32c515614f0af38045463319bd4bfb3a661a4ae9e4486c0404c75ead
  static_checks:
    STARRY_FINAL_ERRNO_TRANSLATION:
      id: STARRY_FINAL_ERRNO_TRANSLATION
      generated_at_utc: '2026-07-16T09:51:50.883998Z'
      content_hash: sha256:a937942b5d3f72022b0fddda5d4931b4cb9e86448aa2ac71c03866be6f4cd5f0
    STARRY_FINAL_SYMLINK_USER_POINTERS:
      id: STARRY_FINAL_SYMLINK_USER_POINTERS
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:aeeb18ba82e36482d2b059560b756c253ebf1a470876449eabdb6b6718662969
    STARRY_FINAL_SYSINFO_COPYOUT:
      id: STARRY_FINAL_SYSINFO_COPYOUT
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:df81078edcf15eb541d550d27af9ed25d5edc37b9747b684dc98fecb35d125d4
    STARRY_FINAL_SYSLOG_CONSOLE_LEVEL:
      id: STARRY_FINAL_SYSLOG_CONSOLE_LEVEL
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:a93427ca41bcbef272c181018b50797e3be5790ee87dff556c66826b4b537a6c
    STARRY_FINAL_SYSLOG_CONTROL_ACTIONS:
      id: STARRY_FINAL_SYSLOG_CONTROL_ACTIONS
      generated_at_utc: '2026-07-16T12:11:32.964664Z'
      content_hash: sha256:1f8c0e5613315af758596f3f7ca2c8023e0aaac1199679d6eb61338856de8b9f
    STARRY_FINAL_SYSLOG_INVALID_ACTION:
      id: STARRY_FINAL_SYSLOG_INVALID_ACTION
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:f4f907d86f0f6d55c3e478cd10768cc4ac1d0e1164c5be30a553e1b9077e91aa
    STARRY_FINAL_SYSLOG_PRIVILEGE:
      id: STARRY_FINAL_SYSLOG_PRIVILEGE
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:898b366254d72d0be9f227af9616a15c23a51b948891098d7e904f7e058792e0
    STARRY_FINAL_SYSLOG_READ_ARGUMENTS:
      id: STARRY_FINAL_SYSLOG_READ_ARGUMENTS
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:947467c63df939000091ce9bbfa725b3dac3bd6d9fdb07cbb606a5ef778825f1
    STARRY_FINAL_TIMER_DELETE:
      id: STARRY_FINAL_TIMER_DELETE
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:8ff5c8e888e49a2b398a5635edb5e7178a7a931b329d81d05cca24c16d5992de
    STARRY_FINAL_TKILL_TID_VALIDATION:
      id: STARRY_FINAL_TKILL_TID_VALIDATION
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:bd665d5bbc7713aa296dbacb6ebac30037600a425236d51c92829d3e3decb9d5
    STARRY_FINAL_UMOUNT_MOUNTPOINT:
      id: STARRY_FINAL_UMOUNT_MOUNTPOINT
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:50e93ea5e1c0901013e4dba236236162c2a52317c0e9e4f00dfa81cdcdec54ac
    STARRY_FINAL_UMOUNT_PRIVILEGE:
      id: STARRY_FINAL_UMOUNT_PRIVILEGE
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:9076327bc10ad8f7970328c88a4b62abfe9cbdc3118616d23772096e764afae7
    STARRY_FINAL_UMOUNT_USER_PATH:
      id: STARRY_FINAL_UMOUNT_USER_PATH
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:64d71501fef4076b21c80d31adfdcee70f218add2987c48bef918bd8be98f022
    STARRY_FINAL_UNAME_COPYOUT:
      id: STARRY_FINAL_UNAME_COPYOUT
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:89ae263a7198228815051b926ad692f619f95235e577d6e34b8b56d8dacf050d
    STARRY_FINAL_UNSHARE_FLAG_VALIDATION:
      id: STARRY_FINAL_UNSHARE_FLAG_VALIDATION
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:fe91c68b39d03be67abfca6e51090b2077bc8d781a7bb8c90dc9f8e4238497cd
    STARRY_FINAL_UNSHARE_NEWNS_PRIVILEGE:
      id: STARRY_FINAL_UNSHARE_NEWNS_PRIVILEGE
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:647346966f4cd913f5bc3219f181a2d9b7f6865ea1decc8e898b1f28751b9842
    STARRY_FINAL_WAITID_OPTIONS:
      id: STARRY_FINAL_WAITID_OPTIONS
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:eb10af7768c3c3f23a2004fa7c4d35545f2f964f533df148d3878b32deabd46c
    STARRY_FINAL_WAITPID_OPTIONS:
      id: STARRY_FINAL_WAITPID_OPTIONS
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:94510ad8995d40bcfdfb2883cbdb545a20bbfd35969ef29736af779ab998ec73
    STARRY_FINAL_WRITE_BAD_FD:
      id: STARRY_FINAL_WRITE_BAD_FD
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:30cb4cd9e1e8745efae7743768569c3df3a3525ac67edbc112783b63a5197906
    STARRY_FINAL_WRITE_USER_BUFFER:
      id: STARRY_FINAL_WRITE_USER_BUFFER
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:3ebdca5d15aafca2b9ee204ced42be9f44610f9af6d35ce20e911473c69512be
    STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS:
      id: STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:6d8ffe193808bde740053a61419adcf0e7c090388b2f5fea0475696c5b402070
    STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO:
      id: STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:39ebc0849b8fede86d9689ed1dba7fda23315b83937a447b328ffd1a94bdfb34
    STARRY_EPOLL_NESTED_LOOP:
      id: STARRY_EPOLL_NESTED_LOOP
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:d1db97954ea66c6632d4d74191ef0d91751bbbcfee42883a78137bbdaac22e58
    STARRY_FINIT_MODULE_FLAG_VALIDATION:
      id: STARRY_FINIT_MODULE_FLAG_VALIDATION
      generated_at_utc: '2026-07-16T04:30:54.819863Z'
      content_hash: sha256:81ef9eef26bc66571e89435a216d883211029dd798c2e5ce97752ec71f012cf4
    STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE:
      id: STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE
      generated_at_utc: '2026-07-16T08:20:59.387945Z'
      content_hash: sha256:e2e77be33c0c00e8b38780cef8b7b9ff37f7271c1a4f1d1289041b8cf68f4817
    STARRY_ROUND3_INIT_MODULE_PERMISSION:
      id: STARRY_ROUND3_INIT_MODULE_PERMISSION
      generated_at_utc: '2026-07-16T08:20:59.387945Z'
      content_hash: sha256:9df3be22e06572f2b77a0e12c13e9bc9c3a498b4317a288e87e880ee8b23d177
    STARRY_ROUND5_SETPGID_NEGATIVE:
      id: STARRY_ROUND5_SETPGID_NEGATIVE
      generated_at_utc: '2026-07-16T08:20:59.387945Z'
      content_hash: sha256:5fa6b80a0abd76e0c19c944876cb5f33d7cff69abf8434b9fca9fe1af9d94ac5
    STARRY_ROUND5_SOCKET_INVALID_TYPE:
      id: STARRY_ROUND5_SOCKET_INVALID_TYPE
      generated_at_utc: '2026-07-16T08:20:59.387945Z'
      content_hash: sha256:af3e1dc26481ee71e25429daac3d3eb199d94dbf93c29dfa57c25f0a77e13c3d
  dynamic_tests:
    STARRY_FINAL_SYSINFO_BEHAVIOR:
      id: STARRY_FINAL_SYSINFO_BEHAVIOR
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:fde838482f4ddeb1cecc3363a09dae5854676132012b3dabe3d74f2c0a9e4d26
    STARRY_FINAL_SYSLOG_BEHAVIOR:
      id: STARRY_FINAL_SYSLOG_BEHAVIOR
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:13d97721ea96c22432a09a47f5bf81b1a3891f986c933598936f55e92e13a80d
    STARRY_FINAL_TIMER_DELETE_BEHAVIOR:
      id: STARRY_FINAL_TIMER_DELETE_BEHAVIOR
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:dd1f8207f2596bcf6496320e2c9808cebbbb254ab58c2b6dcf02e0ae4b14feb5
    STARRY_FINAL_UNAME_BEHAVIOR:
      id: STARRY_FINAL_UNAME_BEHAVIOR
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:39b6422f5203e6b607c4c6f8523376e2ec657618eb94905793989c82ac40b7c0
    STARRY_FINAL_WAIT4_BEHAVIOR:
      id: STARRY_FINAL_WAIT4_BEHAVIOR
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:a96cc2b1d6f032573454b8526a95ea95060aa35160accfa6dd0daf02e6a46e64
    STARRY_FINAL_WAITID_BEHAVIOR:
      id: STARRY_FINAL_WAITID_BEHAVIOR
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:91e4458bd02931ac8e9d04554a8e27efd57492d03682a63fb1052cec45a6e2c2
    STARRY_FINAL_WRITE_FILE_BEHAVIOR:
      id: STARRY_FINAL_WRITE_FILE_BEHAVIOR
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:9c80afe9885e53c60565698d75929f8c1187b76f6f6f3120e2d4eaf657082526
base_execution_scope:
  rules:
  - LTP_02908A57586A60CF
  - LTP_0FE0E20EAC6DE889
  - LTP_10B3572DBFA6742B
  - LTP_18304438A1D5D6C1
  - LTP_1B4A2A1831541F06
  - LTP_22F13AFD9925B2AE
  - LTP_25D7B6229831E0EF
  - LTP_287CF10D893735AB
  - LTP_2AE73292A13647D5
  - LTP_330C66A049727F75
  - LTP_4184881E196F9E5E
  - LTP_4828EB12592F311C
  - LTP_498695B75BD43DAD
  - LTP_4FCD61E2EED61335
  - LTP_53E7B9C40A44F6D0
  - LTP_5516B8A938B9C3A5
  - LTP_6B9F97B897EC5C32
  - LTP_6D02D744B460F97E
  - LTP_6D819B66D5B60871
  - LTP_74C73CBABE325D5D
  - LTP_77C2FB4A0A9E30F2
  - LTP_7F4262FC753FC8D9
  - LTP_82A8802A27A3D2BF
  - LTP_89AC9F4AA9032B8D
  - LTP_9B36D27A4A2994D0
  - LTP_9FD87A3F7688FEF1
  - LTP_A367723236ADA8B4
  - LTP_B212BAAA2C2C75CC
  - LTP_C0694665E22D48E8
  - LTP_C8376BC347F94A98
  - LTP_C8F11074F91F94EF
  - LTP_DB77907DDC5EDFF4
  - LTP_E272B715ECA16E6C
  - LTP_E7CB95EADCE845E9
  - LTP_F38A837D067865DC
  - LTP_F92CEB15161CB23C
  - LTP_FCC236A4D5926B81
  static_checks:
  - STARRY_FINAL_ERRNO_TRANSLATION
  - STARRY_FINAL_SYMLINK_USER_POINTERS
  - STARRY_FINAL_SYSINFO_COPYOUT
  - STARRY_FINAL_SYSLOG_CONSOLE_LEVEL
  - STARRY_FINAL_SYSLOG_CONTROL_ACTIONS
  - STARRY_FINAL_SYSLOG_INVALID_ACTION
  - STARRY_FINAL_SYSLOG_PRIVILEGE
  - STARRY_FINAL_SYSLOG_READ_ARGUMENTS
  - STARRY_FINAL_TIMER_DELETE
  - STARRY_FINAL_TKILL_TID_VALIDATION
  - STARRY_FINAL_UMOUNT_MOUNTPOINT
  - STARRY_FINAL_UMOUNT_PRIVILEGE
  - STARRY_FINAL_UMOUNT_USER_PATH
  - STARRY_FINAL_UNAME_COPYOUT
  - STARRY_FINAL_UNSHARE_FLAG_VALIDATION
  - STARRY_FINAL_UNSHARE_NEWNS_PRIVILEGE
  - STARRY_FINAL_WAITID_OPTIONS
  - STARRY_FINAL_WAITPID_OPTIONS
  - STARRY_FINAL_WRITE_BAD_FD
  - STARRY_FINAL_WRITE_USER_BUFFER
  dynamic_tests:
  - STARRY_FINAL_SYSINFO_BEHAVIOR
  - STARRY_FINAL_SYSLOG_BEHAVIOR
  - STARRY_FINAL_TIMER_DELETE_BEHAVIOR
  - STARRY_FINAL_UNAME_BEHAVIOR
  - STARRY_FINAL_WAIT4_BEHAVIOR
  - STARRY_FINAL_WAITID_BEHAVIOR
  - STARRY_FINAL_WRITE_FILE_BEHAVIOR
revalidation_scope:
  rules: []
  static_checks: []
  dynamic_tests: []
effective_execution_scope: &id001
  rules:
  - LTP_02908A57586A60CF
  - LTP_0FE0E20EAC6DE889
  - LTP_10B3572DBFA6742B
  - LTP_18304438A1D5D6C1
  - LTP_1B4A2A1831541F06
  - LTP_22F13AFD9925B2AE
  - LTP_25D7B6229831E0EF
  - LTP_287CF10D893735AB
  - LTP_2AE73292A13647D5
  - LTP_330C66A049727F75
  - LTP_4184881E196F9E5E
  - LTP_425E5A3502541DE8
  - LTP_4308D71D8BD6519D
  - LTP_4828EB12592F311C
  - LTP_498695B75BD43DAD
  - LTP_4FCD61E2EED61335
  - LTP_53E7B9C40A44F6D0
  - LTP_5516B8A938B9C3A5
  - LTP_66C670178B06E9F3
  - LTP_6B9F97B897EC5C32
  - LTP_6C14DE68E3C0CC24
  - LTP_6D02D744B460F97E
  - LTP_6D819B66D5B60871
  - LTP_74BB3F96CBA52D02
  - LTP_74C73CBABE325D5D
  - LTP_77C2FB4A0A9E30F2
  - LTP_7F4262FC753FC8D9
  - LTP_82A8802A27A3D2BF
  - LTP_89AC9F4AA9032B8D
  - LTP_971DB17D32C51561
  - LTP_9B36D27A4A2994D0
  - LTP_9FD87A3F7688FEF1
  - LTP_A367723236ADA8B4
  - LTP_B212BAAA2C2C75CC
  - LTP_C0694665E22D48E8
  - LTP_C8376BC347F94A98
  - LTP_C8F11074F91F94EF
  - LTP_D246498B20D9CB2C
  - LTP_DA65D6C7A0E4ABBC
  - LTP_DB77907DDC5EDFF4
  - LTP_E272B715ECA16E6C
  - LTP_E7CB95EADCE845E9
  - LTP_F38A837D067865DC
  - LTP_F92CEB15161CB23C
  - LTP_FCC236A4D5926B81
  static_checks:
  - STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS
  - STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO
  - STARRY_EPOLL_NESTED_LOOP
  - STARRY_FINAL_ERRNO_TRANSLATION
  - STARRY_FINAL_SYMLINK_USER_POINTERS
  - STARRY_FINAL_SYSINFO_COPYOUT
  - STARRY_FINAL_SYSLOG_CONSOLE_LEVEL
  - STARRY_FINAL_SYSLOG_CONTROL_ACTIONS
  - STARRY_FINAL_SYSLOG_INVALID_ACTION
  - STARRY_FINAL_SYSLOG_PRIVILEGE
  - STARRY_FINAL_SYSLOG_READ_ARGUMENTS
  - STARRY_FINAL_TIMER_DELETE
  - STARRY_FINAL_TKILL_TID_VALIDATION
  - STARRY_FINAL_UMOUNT_MOUNTPOINT
  - STARRY_FINAL_UMOUNT_PRIVILEGE
  - STARRY_FINAL_UMOUNT_USER_PATH
  - STARRY_FINAL_UNAME_COPYOUT
  - STARRY_FINAL_UNSHARE_FLAG_VALIDATION
  - STARRY_FINAL_UNSHARE_NEWNS_PRIVILEGE
  - STARRY_FINAL_WAITID_OPTIONS
  - STARRY_FINAL_WAITPID_OPTIONS
  - STARRY_FINAL_WRITE_BAD_FD
  - STARRY_FINAL_WRITE_USER_BUFFER
  - STARRY_FINIT_MODULE_FLAG_VALIDATION
  - STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE
  - STARRY_ROUND3_INIT_MODULE_PERMISSION
  - STARRY_ROUND5_SETPGID_NEGATIVE
  - STARRY_ROUND5_SOCKET_INVALID_TYPE
  dynamic_tests:
  - STARRY_FINAL_SYSINFO_BEHAVIOR
  - STARRY_FINAL_SYSLOG_BEHAVIOR
  - STARRY_FINAL_TIMER_DELETE_BEHAVIOR
  - STARRY_FINAL_UNAME_BEHAVIOR
  - STARRY_FINAL_WAIT4_BEHAVIOR
  - STARRY_FINAL_WAITID_BEHAVIOR
  - STARRY_FINAL_WRITE_FILE_BEHAVIOR
execution_scope: *id001
rule_syscalls:
  LTP_004E24807F6067A5:
  - madvise
  LTP_0069B2BDFC11BD6E:
  - sendto
  LTP_0080969B4E1A8F96:
  - init_module
  LTP_0087F445CEB63414:
  - read
  LTP_00F2A9EA8833DA1D:
  - cachestat
  LTP_0134FE6EEF60CBCD:
  - pidfd_getfd
  LTP_0180982614AA9F7D:
  - access
  LTP_018C7E7A08833780:
  - poll
  LTP_01E0E5231C9C3654:
  - mkdirat
  LTP_021CFAE8581109DA:
  - fsconfig
  LTP_023F1DC98CE31416:
  - fchmodat
  LTP_025CF701276457CB:
  - faccessat2
  LTP_026CB4A1CA7CDC6B:
  - openat2
  LTP_0290063892A53510:
  - access
  LTP_02908A57586A60CF:
  - syslog
  LTP_02D0577172D97F4B:
  - ftruncate
  LTP_03083D6A95333E23:
  - rt_sigprocmask
  LTP_030858A5FFCCEFF4:
  - access
  LTP_0311772B70C94C38:
  - pidfd_open
  LTP_0324F0A6601FFECE:
  - rt_sigsuspend
  LTP_033FAA6E22CDE433:
  - msync
  LTP_035E62E6D1787773:
  - access
  LTP_036EDA2B8D36CF03:
  - access
  LTP_03702BF4223F6AA5:
  - epoll_wait
  LTP_037E6F334D0E0D16:
  - access
  LTP_03AF14160F8B59A0:
  - waitpid
  LTP_03FD233DFE92488D:
  - sbrk
  LTP_04236FD5B061DEB9:
  - utime
  LTP_0431E3529AA0FEE8:
  - access
  LTP_043885E3B78D9010:
  - fchdir
  LTP_044E7C11E6B503BB:
  - access
  LTP_048D7BAFDFD264F6:
  - readlinkat
  LTP_04A84187DEC4CF09:
  - flock
  LTP_04FC167B4A1C57FB:
  - mlock
  LTP_05B109981D13ED76:
  - write
  LTP_060B6037DEF1D43C:
  - access
  LTP_065F7F29AD356B3E:
  - sendmsg
  LTP_06725D44DFF06F7E:
  - access
  LTP_06891E2E299CF48E:
  - access
  LTP_06A0C295D8E7FAFA:
  - access
  LTP_06AC9297E35AAE7A:
  - access
  LTP_06EAAEA7DDC8627E:
  - mlockall
  LTP_06F742EF42AA55BA:
  - request_key
  LTP_074981FFB7FA5DB7:
  - mlock2
  LTP_075318C437B76E06:
  - access
  LTP_0799FC60BADD2B18:
  - access
  LTP_07FCC99E3AE43064:
  - signalfd
  LTP_08C4F07A07C4C3F7:
  - pidfd_send_signal
  LTP_08E1FDAFE6D66846:
  - mprotect
  LTP_08F05BA6ED1CEE6A:
  - pidfd_send_signal
  LTP_09370275EF5F3065:
  - copy_file_range
  LTP_09377FE11AF44E16:
  - setpgrp
  LTP_098AFE0E8E10B0EF:
  - dup3
  LTP_09AB8108C3720119:
  - fchmodat2
  LTP_09ADB22B713F6C62:
  - munmap
  LTP_09B39E9C9254ECB2:
  - close
  LTP_09FED6AAC1020069:
  - fpathconf
  LTP_0A2035C9A2A77F66:
  - sched_getattr
  LTP_0A62800536904C02:
  - access
  LTP_0A819CDD66F1C6A1:
  - request_key
  LTP_0AAFA34BA77A0D25:
  - access
  LTP_0AE3E0188FBE5839:
  - pwrite64
  LTP_0B35C54F2F39E4D4:
  - fsconfig
  LTP_0B45FC33068D334C:
  - access
  LTP_0B898E71738ECEB7:
  - open_by_handle_at
  LTP_0B982157D25C1D06:
  - getsockopt
  LTP_0BB235F712E819CE:
  - access
  LTP_0C5623B3D5C7430F:
  - setpgid
  LTP_0CD17E662AFD2956:
  - close
  LTP_0D1782EAAC26DEB4:
  - access
  LTP_0D3B043506A61BD6:
  - init_module
  LTP_0D59D1FBC322425B:
  - mlockall
  LTP_0D9B02C95396CCDC:
  - signalfd
  LTP_0D9BB2CB02786128:
  - fsconfig
  LTP_0DF4BC077C390176:
  - fsconfig
  LTP_0E114DF9B3215650:
  - finit_module
  LTP_0E51A1345D29A74B:
  - madvise
  LTP_0E5462C27210C85F:
  - sendmsg
  LTP_0E9AF2C058AF8126:
  - access
  LTP_0EBD1214FC6BB6D5:
  - dup
  LTP_0EEA999DE0FFD37D:
  - getsockopt
  LTP_0EEADAF9E605632C:
  - pidfd_open
  LTP_0F02943A8FDA4830:
  - getpriority
  LTP_0F35A2F3718D172D:
  - readahead
  LTP_0F5654610A1780B6:
  - openat2
  LTP_0F901C62092CC7B8:
  - access
  LTP_0F9C596BA8184375:
  - tee
  LTP_0F9F906AC57F0B46:
  - pidfd_send_signal
  LTP_0FCE63CBC47F69DA:
  - connect
  LTP_0FE0E20EAC6DE889:
  - waitid
  LTP_0FEC274199CCD0A0:
  - execveat
  LTP_1028A46194A35788:
  - rename
  LTP_106D7242AECD4D33:
  - setpgrp
  LTP_10A684C1C2D2DE0F:
  - access
  LTP_10B3572DBFA6742B:
  - timer_delete
  LTP_10F51B1972AD94ED:
  - timer_getoverrun
  LTP_10FE1313FBAB5F92:
  - access
  LTP_11235D2EF3DC4C5C:
  - fsconfig
  LTP_11385EF43CBDA2E0:
  - mq_notify
  LTP_11852F99424BD7E5:
  - mprotect
  LTP_11CB16D3E88491A4:
  - copy_file_range
  LTP_1264D075DA68BB98:
  - iopl
  LTP_12A1904141AAE2EE:
  - dup2
  LTP_12EAE2F32232CC05:
  - pidfd_getfd
  LTP_1325C077A1CDE514:
  - cachestat
  LTP_132A1A1638D957AF:
  - connect
  LTP_139142311CF01E20:
  - sbrk
  LTP_1402459B5FF9BF23:
  - access
  LTP_14105E9CB6DC44FC:
  - ustat
  LTP_141CBA02709D5489:
  - vhangup
  LTP_1465554B09CE14F0:
  - access
  LTP_148623FDAF4E478D:
  - access
  LTP_1505AAD11D4091B7:
  - readlinkat
  LTP_1507C71C3D1DF6E5:
  - sendto
  LTP_153B296FA599E0CE:
  - access
  LTP_154DEC6769244339:
  - mlockall
  LTP_15EC9351D2422944:
  - pwrite64
  LTP_15FCB1A16CBF7B34:
  - openat2
  LTP_16343E95C1C7EF47:
  - pathconf
  LTP_1661259678F899BC:
  - pathconf
  LTP_1691F6F9712C5546:
  - wait4
  LTP_16B8EA75C5016419:
  - mlock2
  LTP_16DBBB2E96948A9C:
  - ustat
  LTP_1707E748EA729431:
  - pathconf
  LTP_1726C16756E9651C:
  - dup3
  LTP_17ACF3BE969B64EE:
  - access
  LTP_17B7A9460939622A:
  - fchdir
  LTP_17CB4ED7A76BD283:
  - access
  LTP_18304438A1D5D6C1:
  - syslog
  LTP_183B0BD036512FA6:
  - fchmodat
  LTP_1870C0046E9555AF:
  - access
  LTP_1893FF0C4930806E:
  - pathconf
  LTP_18A450CE49F8867B:
  - access
  LTP_18E65E41E98D9E97:
  - pidfd_open
  LTP_18ECD15E5451228D:
  - epoll_wait
  LTP_1918D556CB808466:
  - fsconfig
  LTP_196A6B5A609ADC9A:
  - llistxattr
  LTP_198D9555A8BED013:
  - access
  LTP_1A68979B981D8947:
  - madvise
  LTP_1A9481FAD460FBF7:
  - alarm
  LTP_1AA7F21DA5C55800:
  - eventfd
  LTP_1AACAC53BAF23BA9:
  - preadv2
  LTP_1AD5BF710E8FB247:
  - pathconf
  LTP_1ADEBF230DD2C214:
  - epoll_wait
  LTP_1B2E614CA8847B31:
  - llistxattr
  LTP_1B3AD244C58835E7:
  - madvise
  LTP_1B4A2A1831541F06:
  - write
  LTP_1B65027CA2FD0026:
  - open_by_handle_at
  LTP_1BB76939FF2A40B5:
  - pidfd_open
  LTP_1BD36AE285B4F3E2:
  - access
  LTP_1BDC4A832DB89410:
  - request_key
  LTP_1C1877AB6CAE8906:
  - mlock
  LTP_1C462AC54A29FF35:
  - access
  LTP_1C8100D018645855:
  - fsconfig
  LTP_1CDCF5FE9ED1BE5D:
  - access
  LTP_1D39F97D759F0E57:
  - access
  LTP_1D3F4A6BCBF6BBE5:
  - init_module
  LTP_1D6E9D5C4E09D7F5:
  - madvise
  LTP_1DF2B28499E4D7B3:
  - access
  LTP_1EEDAE05876D0546:
  - fpathconf
  LTP_1F2328B410A3010D:
  - pwritev2
  LTP_1F8223E4EE64B649:
  - listxattr
  LTP_2084284EEECEEAC0:
  - tkill
  LTP_208C833FF12217F5:
  - capget
  LTP_209742037ADD09F1:
  - readlinkat
  LTP_20DA453342D2F4AB:
  - fpathconf
  LTP_212269CECE600FD8:
  - access
  LTP_213EA37A2B59AB99:
  - ftruncate
  LTP_21A007DF738F1E73:
  - access
  LTP_21C4957F9EFE94D3:
  - access
  LTP_21FCBFC328D1815A:
  - symlink
  LTP_220D1227D307AD3C:
  - access
  LTP_2221F954D01EB2BB:
  - access
  LTP_22E98D1569DAB493:
  - epoll_ctl
  LTP_22F13AFD9925B2AE:
  - write
  LTP_2433DF1752AE54B7:
  - fsconfig
  LTP_245110930B22BF5C:
  - flock
  LTP_245CD61DAA19DC98:
  - chroot
  LTP_249EC7CDE9C4682F:
  - pidfd_getfd
  LTP_252DC2EE1F2FC3AC:
  - setpriority
  LTP_254E7D0C8662B3BB:
  - pidfd_getfd
  LTP_2554AC2E46FC6A15:
  - getrlimit
  LTP_25639C9C5750C487:
  - access
  LTP_25D7B6229831E0EF:
  - uname
  LTP_2648B36BD9CF39EE:
  - ftruncate
  LTP_26555A26680524AD:
  - getrlimit
  LTP_2668EE4D34576C49:
  - signalfd
  LTP_26AC646B9D18C353:
  - access
  LTP_26AE3C69D80D35F8:
  - munmap
  LTP_272A188C039BEA2B:
  - finit_module
  LTP_277FD467E5F1BF1C:
  - accept
  LTP_27C7E91095DB9DF8:
  - access
  LTP_28410A5D4088E644:
  - readahead
  LTP_287CF10D893735AB:
  - umount
  LTP_287FBE05D7B30C6F:
  - ulimit
  LTP_2900BC64740A3E44:
  - access
  LTP_296D3DD5B2B27A84:
  - pwritev2
  LTP_29873BE2A9AABFF4:
  - symlink
  LTP_298AB67F0CFA519C:
  - access
  LTP_2A0C51A9F627F9EE:
  - rename
  LTP_2A28494F77E0B173:
  - preadv2
  LTP_2A3276D2B0A31AC9:
  - madvise
  LTP_2ACD165E402BB8AE:
  - copy_file_range
  LTP_2AE73292A13647D5:
  - wait4
  LTP_2B4171DD8FBD982A:
  - access
  LTP_2B9F3F4A853A14C6:
  - recvfrom
  LTP_2BBDFB48EF060066:
  - fsconfig
  LTP_2BDE60C0E64B4DC8:
  - close
  LTP_2C266C6067333086:
  - read
  LTP_2C2A7A0BCB72A2EB:
  - sendto
  LTP_2C37BF2D4F1059A2:
  - msync
  LTP_2C867F470A477D29:
  - signalfd
  LTP_2CB0A10A3E175A9C:
  - sched_getaffinity
  LTP_2D0BAECAE4F61432:
  - access
  LTP_2D1E25BD679B3494:
  - epoll_create
  LTP_2D65D505344282C8:
  - sendto
  LTP_2E4BA3FA59A48F0F:
  - rename
  LTP_2E5D530A61E60934:
  - access
  LTP_2EBC825D5CF7EF0F:
  - rename
  LTP_2F153EBAAD2A779C:
  - connect
  LTP_2F3E34FD672DBF34:
  - waitpid
  LTP_2F99FA84C445363C:
  - access
  LTP_2FA43CD942AE7AD6:
  - access
  LTP_2FAD34B153D5914E:
  - recvfrom
  LTP_2FDCA4DAED71F98B:
  - mlock2
  LTP_2FE8FAD800DE41F6:
  - access
  LTP_3073AC57544A6A6A:
  - fchmodat
  LTP_30AF82AD36872B80:
  - readlinkat
  LTP_311F7A773994720E:
  - dup
  LTP_3152706321BA354E:
  - pwritev2
  LTP_31D9D767D6888DDA:
  - close_range
  LTP_31E977FBCF448AFD:
  - listxattr
  LTP_3249413C9BA64960:
  - setpgid
  LTP_326E9D51F4EF6E39:
  - open_by_handle_at
  LTP_32D132100CDC04ED:
  - lstat
  LTP_330C66A049727F75:
  - syslog
  LTP_336B0AA063AB645E:
  - setpriority
  LTP_33C492F97B790AB8:
  - fpathconf
  LTP_33D0A33AC4655F3E:
  - pathconf
  LTP_33D137B9002503E5:
  - exit_group
  LTP_3471B46784E57E93:
  - mlock2
  LTP_3472CD1A0F8A2B4A:
  - access
  LTP_347761CBCF52D194:
  - access
  LTP_34A03F3861C10C4E:
  - mincore
  LTP_34C12DFEB9C8A62A:
  - finit_module
  LTP_34CFEAD03DB6A3CA:
  - access
  LTP_34EC9FB9C9551214:
  - cachestat
  LTP_34FB3789C7448B4F:
  - fchmodat2
  LTP_350B586A62C42467:
  - preadv2
  LTP_352394AAA6D49339:
  - getpgid
  LTP_35AF6D3F6FC0EA61:
  - move_mount
  LTP_35CAEE10A613E109:
  - access
  LTP_35CB47575F7752A4:
  - epoll_ctl
  LTP_3636C4768C196B52:
  - access
  LTP_368D8689810796B2:
  - access
  LTP_36C99C10CD38F8DB:
  - mmap
  LTP_36E1AD5A78C2A50D:
  - madvise
  LTP_3707B18864CF6352:
  - listen
  LTP_371BDA67CB8813FD:
  - fchmod
  LTP_3741A721C9C463D0:
  - getrlimit
  LTP_3743BC827FB4F981:
  - pidfd_open
  LTP_37C625BD7D7C5F1D:
  - dup3
  LTP_37F2ED2BA3175CC3:
  - epoll_create
  LTP_380714557B4AE9D4:
  - madvise
  LTP_38432B154B641410:
  - utime
  LTP_38B9BA93F16FBAAF:
  - seccomp
  LTP_38EE9A0047529979:
  - sendfile
  LTP_38FB918826669241:
  - access
  LTP_39008564F17DCBDD:
  - getdents64
  LTP_3900F4E562AE09D1:
  - access
  LTP_3916A669595B3568:
  - access
  LTP_39B1E5C574F2D3DC:
  - sendfile
  LTP_3A18518E9A9DDC47:
  - mincore
  LTP_3A7B17AF231D4158:
  - dup3
  LTP_3AD3865603ADDC8E:
  - access
  LTP_3AF9CC563B4BAC1C:
  - flock
  LTP_3B0C2A3A034B17ED:
  - sendmsg
  LTP_3B1458E6E26CBB53:
  - getrlimit
  LTP_3B4D19754C5D1638:
  - ulimit
  LTP_3B77ABEF9EF7D3ED:
  - umount
  LTP_3C1DCCC4E6DCC76B:
  - sendfile
  LTP_3C2853617B38EEE7:
  - access
  LTP_3C2993663039F664:
  - vhangup
  LTP_3C4C8CA4ED44FE57:
  - getdomainname
  LTP_3CA39247E6E3D055:
  - listxattr
  LTP_3D4ECD22BC433164:
  - access
  LTP_3D50FA09D36623FF:
  - fsconfig
  LTP_3D8D38C9123CD051:
  - access
  LTP_3DDCD08519809A17:
  - getsockopt
  LTP_3DE23AB4FE2FFC67:
  - access
  LTP_3E0077ECCDBC2639:
  - fchmodat
  LTP_3E526A0A23B5EF6D:
  - access
  LTP_3E8DA9E014B82702:
  - alarm
  LTP_3EB53CD0B1672EE5:
  - preadv2
  LTP_3EC51D87D4A4C0C2:
  - rename
  LTP_3F60BBC08D86D573:
  - pread64
  LTP_3F7F517D8AA3614C:
  - get_robust_list
  LTP_3F81436312777EF4:
  - access
  LTP_3F8B5B68E9CDC1F9:
  - write
  LTP_3FF54C2EFF286EF7:
  - open_by_handle_at
  LTP_40024D6BE4C6AECC:
  - set_robust_list
  LTP_401D471D37C85820:
  - access
  LTP_4032B15A045CC9CD:
  - mincore
  LTP_403B654FD084895C:
  - poll
  LTP_40621A9DFAF6D232:
  - msync
  LTP_408787CB8F89AAF4:
  - move_mount
  LTP_409C97094F0CED1F:
  - getdents64
  LTP_40A45C5E82D7F4A1:
  - unshare
  LTP_40ABB27673C9DE62:
  - sendto
  LTP_4101795C27681AB4:
  - openat2
  LTP_412173E3E81DC995:
  - unshare
  LTP_4184881E196F9E5E:
  - syslog
  LTP_423E92D9328C2A39:
  - rt_sigprocmask
  LTP_425E5A3502541DE8:
  - close_range
  LTP_4308D71D8BD6519D:
  - setpgid
  LTP_43728156B00FF104:
  - utime
  LTP_437CFCD991A666C9:
  - faccessat2
  LTP_43A681D8FCD1B740:
  - pidfd_getfd
  LTP_43BC8A0B853CD8DB:
  - rename
  LTP_44128D8D82BC1E09:
  - flock
  LTP_4494B70BBA693D42:
  - waitid
  LTP_44B41305EB538966:
  - getdents64
  LTP_44DC5382746D773D:
  - setpriority
  LTP_453DFC908EB0DD9E:
  - init_module
  LTP_45439D8F2BAB0832:
  - mmap
  LTP_461340ED83E7043D:
  - capset
  LTP_462CE9A88054B448:
  - mq_notify
  LTP_46401248F52AD892:
  - fsconfig
  LTP_4661BBF1B3CD3A1E:
  - access
  LTP_46649CE57B3EFB7F:
  - open_by_handle_at
  LTP_466F01834F965621:
  - fstat
  LTP_468FC84DEAB0BCB8:
  - epoll_ctl
  LTP_46A3B23FBDECBAD4:
  - sendmsg
  LTP_46AA49209C30E739:
  - ftruncate
  LTP_46DC592FFC5E5C44:
  - mq_notify
  LTP_46DE8D9AD1674F26:
  - access
  LTP_470C0966080C93EF:
  - fchmod
  LTP_470EA842B2582537:
  - sigaltstack
  LTP_472AAA35C7382B26:
  - accept
  LTP_47651AB878EBD24C:
  - request_key
  LTP_479924116854D92B:
  - access
  LTP_47B47DF38E582CE0:
  - openat2
  LTP_481898C7C2C1FF1D:
  - sendmsg
  LTP_4828EB12592F311C:
  - syslog
  LTP_48753F73ACA755FB:
  - access
  LTP_4881657CFE57C7E9:
  - access
  LTP_4929F8BCC4B9811B:
  - lstat
  LTP_492D25A0F1055F72:
  - access
  LTP_4948E12FB8F9FA49:
  - access
  LTP_4953FAD330ADE150:
  - epoll_ctl
  LTP_49700CDA955B66D8:
  - access
  LTP_4984976D88DF21AE:
  - ulimit
  LTP_498695B75BD43DAD:
  - syslog
  LTP_49A11FBBFB010278:
  - sendto
  LTP_49A36559B96D24AF:
  - access
  LTP_49ABEE42EF290FDC:
  - unshare
  LTP_4A4F50B0E250249A:
  - msync
  LTP_4A5C15DAE55BBD2E:
  - sendfile
  LTP_4AF75A49B2F7AAB5:
  - munlock
  LTP_4B6E9B98E2E5103D:
  - access
  LTP_4BA2A081C3EB3304:
  - sched_setattr
  LTP_4BBF626715445EFC:
  - setpgid
  LTP_4BCFF61005DC2E9A:
  - faccessat2
  LTP_4BDFA76AA51D745B:
  - pread64
  LTP_4C1F446C9C520B36:
  - faccessat2
  LTP_4C3A8A7664F22B7F:
  - connect
  LTP_4CFAFCE7FCA2BF99:
  - access
  LTP_4D51F55F25C6F2A3:
  - faccessat2
  LTP_4D86B6394424B16C:
  - sigaltstack
  LTP_4D9D59CFB785EB0C:
  - munlock
  LTP_4DB863CC12B75471:
  - setpriority
  LTP_4E45B0701D5BD8A7:
  - pwrite64
  LTP_4ECB786BFA071AAC:
  - access
  LTP_4ED7FF29685C11B0:
  - mlock
  LTP_4F02ACC6E2F6B094:
  - dup2
  LTP_4FCD61E2EED61335:
  - syslog
  LTP_503160311D12E629:
  - setpgid
  LTP_505DF8E6B5595F9E:
  - madvise
  LTP_50853944DA25B2E0:
  - setpriority
  LTP_50972E17C52A9EF6:
  - fsconfig
  LTP_50A86D4D5411356E:
  - access
  LTP_50BD66A0A05AFE51:
  - pathconf
  LTP_50F858A3CBF95EED:
  - chroot
  LTP_50FD97B7CD409007:
  - flock
  LTP_5109EDF645F51D7E:
  - faccessat2
  LTP_511185D6DE2A63A0:
  - dup
  LTP_5145972CC10FF773:
  - sched_getaffinity
  LTP_51E295101A9F4411:
  - mmap
  LTP_51E954C969CAFA58:
  - flistxattr
  LTP_51EC2B222D4690DB:
  - poll
  LTP_52BAFC01DEA6E172:
  - mmap
  LTP_52C209105EE62171:
  - access
  LTP_52CE7E6F9B5FF947:
  - getsockname
  LTP_52FC519F20674559:
  - kill
  LTP_5322AC28C2EB6C16:
  - pidfd_getfd
  LTP_532E8E5A98C0A22D:
  - pathconf
  LTP_53B499F623D50A0A:
  - fsconfig
  LTP_53E3454ED6EFD842:
  - getcwd
  LTP_53E7B9C40A44F6D0:
  - waitid
  LTP_53F53970B961AB32:
  - open_by_handle_at
  LTP_54CE18AAE5BDB693:
  - madvise
  LTP_54D221925C324829:
  - rename
  LTP_5516B8A938B9C3A5:
  - uname
  LTP_5560FF1D5C7F4B90:
  - sgetmask
  LTP_5570480E7920BD0E:
  - access
  LTP_55D2492560C39AFD:
  - sigsuspend
  LTP_55D4EF674AFB4ED1:
  - fsconfig
  LTP_55E78705E11C6E2D:
  - readlinkat
  LTP_55EFF664BDCE3E21:
  - fsconfig
  LTP_5622491E8A2227F2:
  - eventfd
  LTP_563FB650864E0DC6:
  - access
  LTP_5667C5A09C3EC10E:
  - finit_module
  LTP_56694FAD66174814:
  - pwritev2
  LTP_57933F1DF2F98C34:
  - openat2
  LTP_57C7DC5E29B5ADF8:
  - getpriority
  LTP_58266C6AA844BBBD:
  - poll
  LTP_582938D6E8E17DB3:
  - fpathconf
  LTP_58416E6747519699:
  - access
  LTP_585CC852338F38EE:
  - sched_setaffinity
  LTP_5883CD050463E9E8:
  - epoll_ctl
  LTP_58C8C307B1FF2510:
  - utime
  LTP_58F1512157A0052D:
  - access
  LTP_5920F12CFE459CB8:
  - getsockname
  LTP_592639F40E0FF63A:
  - mlock2
  LTP_594FA5B54CA204E5:
  - dup
  LTP_595C676EF473E6BD:
  - pidfd_getfd
  LTP_59A85FEDCED7BE77:
  - munlock
  LTP_5A2FE2DE55DC96EB:
  - readlinkat
  LTP_5A315335586D4227:
  - access
  LTP_5A68AEA67C7612A0:
  - sendfile
  LTP_5A7E16725228EB1E:
  - madvise
  LTP_5B244D0A4892F35A:
  - finit_module
  LTP_5B4AA4EE494B37D2:
  - gettimeofday
  LTP_5B5079DEC75B53F5:
  - readlinkat
  LTP_5BC52683943E907D:
  - epoll_ctl
  LTP_5C5CDC165410C08C:
  - access
  LTP_5CC32725A40238D7:
  - get_robust_list
  LTP_5CC44E5D1A6B6485:
  - access
  LTP_5CF4B42A5ABA3D0D:
  - unshare
  LTP_5D7971086B2ABAE5:
  - access
  LTP_5D8D2B3BEDA79604:
  - epoll_create1
  LTP_5DC368435F71390F:
  - fsconfig
  LTP_5E1690FA7F57F981:
  - madvise
  LTP_5E2B9548D2D9F147:
  - mprotect
  LTP_5E6E4D23F79BC9DA:
  - ftruncate
  LTP_5E8446D4A0B40C0E:
  - mount_setattr
  LTP_5EC31E34822684C4:
  - access
  LTP_5F1D35ACCEFD4971:
  - capget
  LTP_5F50BCA4675B4B03:
  - mount_setattr
  LTP_60398013DD319A2E:
  - sigaction
  LTP_606B7E40B6BD82EA:
  - access
  LTP_6090C26F5D5D8E5D:
  - fsconfig
  LTP_609D7178B8A77C1F:
  - flistxattr
  LTP_612BF74E1426528A:
  - sigaltstack
  LTP_613A5E121B4B6E68:
  - access
  LTP_614C018F61C078A0:
  - waitpid
  LTP_6156A09A2E506F76:
  - access
  LTP_6169F41023E00C34:
  - access
  LTP_6174E3690A05F1CA:
  - mkdirat
  LTP_61778C450B602081:
  - epoll_ctl
  LTP_621EC309C3A75722:
  - pathconf
  LTP_6263797E65C75794:
  - mq_notify
  LTP_628FD2848734A58A:
  - fchmodat
  LTP_62FDC6AAFC4F4DE5:
  - getsockname
  LTP_635254F85EA9B1B0:
  - readlinkat
  LTP_636590E5A017B28D:
  - access
  LTP_6366A1114F49C2CF:
  - sigsuspend
  LTP_636EE8AC66A970F6:
  - sbrk
  LTP_63E6527501A08F92:
  - ftruncate
  LTP_64227C746913D03D:
  - access
  LTP_6449E4A1D20C01D3:
  - alarm
  LTP_644B7DB483FF489B:
  - signalfd
  LTP_64668181C4066A0A:
  - madvise
  LTP_64A4E5DC71A633A2:
  - access
  LTP_64B1B6EEEC3F79FC:
  - fstat
  LTP_65281FBEE0BF6103:
  - access
  LTP_652CE911B47794E0:
  - getrlimit
  LTP_6580B4D3FA1A86F3:
  - access
  LTP_65B70356F06E31F8:
  - alarm
  LTP_66303F5A0EB2D470:
  - recv
  LTP_669BB2DCB1D95979:
  - mlock2
  LTP_66AC645038FEFC7A:
  - swapon
  LTP_66C670178B06E9F3:
  - epoll_ctl
  LTP_67180EB1CFAAB816:
  - llistxattr
  LTP_679436EC7A4E218A:
  - access
  LTP_679924706FAFC4A5:
  - preadv2
  LTP_67BF94A4ACD303C4:
  - access
  LTP_6821C2F644329FB4:
  - rename
  LTP_68745D21F4EC2FF5:
  - access
  LTP_6882C814E58F3D3B:
  - madvise
  LTP_6885CE6A54F7716E:
  - faccessat2
  LTP_68E1B26815D97B79:
  - access
  LTP_68EDEECFEA7F3C06:
  - realpath
  LTP_69077B093E81B570:
  - access
  LTP_690A651C3A60FC1E:
  - access
  LTP_69317571BC0A39EC:
  - openat2
  LTP_69DB4FB0496BC7A2:
  - settimeofday
  LTP_69E094D1DBFF3796:
  - access
  LTP_6A1A431A08A3F450:
  - access
  LTP_6A2F1D2BB0EE8C22:
  - copy_file_range
  LTP_6A52E2C16AC64CEC:
  - madvise
  LTP_6A70899352D69A0B:
  - flock
  LTP_6AEB77CEC03D0E6E:
  - connect
  LTP_6B1746F6BB2266CA:
  - access
  LTP_6B29B31CE99466E6:
  - socket
  LTP_6B8B5453E8B4E6DE:
  - access
  LTP_6B9F97B897EC5C32:
  - syslog
  LTP_6C11BBB4AABA6E7C:
  - access
  LTP_6C14DE68E3C0CC24:
  - gettimeofday
  LTP_6C55A3E760DF75DB:
  - access
  LTP_6C5B2B87F34E7887:
  - move_mount
  LTP_6C8CC973DA350505:
  - nanosleep
  LTP_6CE9FC3BCA164B5D:
  - access
  LTP_6D02D744B460F97E:
  - umount
  LTP_6D195DDAB1BE2B57:
  - kill
  LTP_6D584CE6CF9B8A06:
  - access
  LTP_6D819B66D5B60871:
  - syslog
  LTP_6D86AFD541A61388:
  - capset
  LTP_6DD85CE2E5952779:
  - msync
  LTP_6DF55FF20A44572D:
  - getpriority
  LTP_6EF7ECD2A8470CEA:
  - access
  LTP_6F4B3A38B8BF4C7E:
  - utime
  LTP_6F77CAA9FC4423BA:
  - utime
  LTP_6F89F9EF4C3D3857:
  - mlockall
  LTP_6FFB17DB762F3167:
  - epoll_ctl
  LTP_708F721FB3456F82:
  - fsconfig
  LTP_70E5CA8341B80E83:
  - getcontext
  LTP_711D5693356A79F2:
  - access
  LTP_715AAC0BA45C0567:
  - mlock2
  LTP_71C54C624831C7F0:
  - chroot
  LTP_71DD72481EF5740E:
  - utime
  LTP_725BDB092C6D8F74:
  - execveat
  LTP_729222947741DFD6:
  - getcwd
  LTP_73330FC2133223F4:
  - socket
  LTP_738C27178BBCE2B1:
  - set_tid_address
  LTP_73DF50509BCC128B:
  - access
  LTP_74819A9DC2B5CB06:
  - access
  LTP_74BAD566B6A0F272:
  - finit_module
  LTP_74BB3F96CBA52D02:
  - copy_file_range
  LTP_74C13DA111D6D9BD:
  - pwritev2
  LTP_74C566A603515252:
  - request_key
  LTP_74C73CBABE325D5D:
  - waitid
  LTP_74DD0DCF0CE8388F:
  - lgetxattr
  LTP_74E00510F4C1B849:
  - connect
  LTP_752C9A802CF96B8B:
  - access
  LTP_753BDF43E7947404:
  - madvise
  LTP_757778388A97EE03:
  - setpriority
  LTP_758C3967C160AA8E:
  - request_key
  LTP_75D52C5E9C93B6D7:
  - dup2
  LTP_766411248B80C139:
  - recv
  LTP_769389D69FDFA661:
  - tee
  LTP_76A9B6CF388A8609:
  - alarm
  LTP_76BFF56F735A0074:
  - close_range
  LTP_76D3B1710474AAC2:
  - copy_file_range
  LTP_76F002F46086B46C:
  - execveat
  LTP_7786636C200E9E5C:
  - lremovexattr
  LTP_779183F85F2C1278:
  - pathconf
  LTP_77AA3EAF2AD0C07A:
  - faccessat2
  LTP_77C2FB4A0A9E30F2:
  - waitid
  LTP_77C73AE1FE592877:
  - init_module
  LTP_77FED5FE42B62868:
  - pidfd_getfd
  LTP_78A991C666EEFF75:
  - pwritev2
  LTP_78EEEBE648781151:
  - access
  LTP_791DEA825D66980B:
  - mmap
  LTP_7963C3DF373596FE:
  - access
  LTP_79882F9E36FC9878:
  - unshare
  LTP_79C7516DECB19092:
  - access
  LTP_79D2E6DA4FED3FBC:
  - rt_sigprocmask
  LTP_79FCE1367A3A0369:
  - epoll_wait
  LTP_7A02B34D5FB8BBC3:
  - access
  LTP_7A6820B73D1C2059:
  - iopl
  LTP_7A74A699442CEB99:
  - brk
  LTP_7A84C55AF45835C2:
  - pathconf
  LTP_7AF4AAC644090507:
  - finit_module
  LTP_7B0F966046AECA7E:
  - wait
  LTP_7B539E14354153DC:
  - access
  LTP_7B85651B66F35DBD:
  - sendmsg
  LTP_7B9FBEA6E7CF8A70:
  - gethostid
  LTP_7BC885B5878C95B6:
  - sendfile
  LTP_7BE2877017694C52:
  - access
  LTP_7C0112A92527C2A7:
  - fstatfs
  LTP_7C06A3394E786948:
  - access
  LTP_7C0B488884F6689C:
  - pwritev2
  LTP_7C67E10CB5F35EA2:
  - pathconf
  LTP_7C995D43920E57D0:
  - mlock2
  LTP_7CB2C1C8643130AD:
  - copy_file_range
  LTP_7CD01664A3589136:
  - pidfd_open
  LTP_7CE7876CE69F200F:
  - access
  LTP_7D53002758BFC516:
  - connect
  LTP_7DC583D73FC4A726:
  - epoll_wait
  LTP_7DD493976CBC9A31:
  - access
  LTP_7DEDC53AC33C891F:
  - capset
  LTP_7DFAC48A8971CFE3:
  - getrlimit
  LTP_7E14411F2FC9D9CF:
  - move_mount
  LTP_7E1612F09CACE33D:
  - copy_file_range
  LTP_7EAD5A075576B981:
  - flock
  LTP_7EB2D64ACBEF14A7:
  - recv
  LTP_7ECC43C03A3DCB14:
  - fsconfig
  LTP_7F0FE233BE49C811:
  - read
  LTP_7F4262FC753FC8D9:
  - syslog
  LTP_7F43697FAC4213A8:
  - copy_file_range
  LTP_7F4B220485E99184:
  - get_robust_list
  LTP_7F5487EEB79017AD:
  - access
  LTP_7F54F9DFF7E0FB61:
  - access
  LTP_7FCEEF8C37201FC7:
  - fsconfig
  LTP_7FD1D8A10AC952F2:
  - fsconfig
  LTP_7FD6142E0E88CF17:
  - cachestat
  LTP_7FDF0704C50C872E:
  - pathconf
  LTP_7FEB3B276A8133AC:
  - openat2
  LTP_8059D9227293D592:
  - access
  LTP_807E2072E5694684:
  - access
  LTP_809809859ABFE5C1:
  - getsockopt
  LTP_80AFFD1BF1D04F38:
  - init_module
  LTP_80B2CAF4B298BEE6:
  - pwrite64
  LTP_80C6DB0ACB2A5510:
  - accept
  LTP_818BA624CA9E4040:
  - access
  LTP_81F076122348B68A:
  - pathconf
  LTP_820495EA1D1F15DA:
  - access
  LTP_82621B02FCA09F40:
  - alarm
  LTP_827CE5CB448A411B:
  - capget
  LTP_828E39231372A771:
  - mq_notify
  LTP_82907DD83DFD7800:
  - preadv2
  LTP_82A8802A27A3D2BF:
  - unshare
  LTP_82ABB8FBFA06D356:
  - access
  LTP_82E0F55AEC3D382F:
  - access
  LTP_830E17210B1FB7AB:
  - access
  LTP_833C5D5CF3C32C2A:
  - access
  LTP_83709E56D6285F71:
  - epoll_ctl
  LTP_839EC7BC904E42D5:
  - access
  LTP_8405B02758433FBC:
  - openat2
  LTP_843BDD20FF921FC3:
  - access
  LTP_845843CAB40A4F40:
  - openat2
  LTP_84DBE108A850E845:
  - dup
  LTP_84E4CC971DD16EC2:
  - access
  LTP_85106060CC8B99CF:
  - pidfd_getfd
  LTP_853D34D061DDE8F8:
  - access
  LTP_853F4B8346648EB9:
  - access
  LTP_85742F5EC5C0112F:
  - write
  LTP_857DC6AD01A88D79:
  - access
  LTP_86144BF50FB25D3A:
  - utime
  LTP_86E690B05A18AF6A:
  - flock
  LTP_86E98E40777EA3FA:
  - mprotect
  LTP_8703114C595382AB:
  - madvise
  LTP_8710A0CE4DCC217D:
  - lgetxattr
  LTP_8731C07ADFDC57F6:
  - mlock2
  LTP_87478A6C3AC7DC60:
  - access
  LTP_87EDCD6CC0E458CD:
  - symlink
  LTP_882D8F6DFB4B7858:
  - mprotect
  LTP_884775F9076E54AB:
  - access
  LTP_885F3BA721198C07:
  - access
  LTP_886C26D89B15EF6D:
  - swapon
  LTP_88D0821E4776E388:
  - fsconfig
  LTP_88D300A8FB407324:
  - getpriority
  LTP_88F6F279E33633DE:
  - access
  LTP_89745BB32E6D4D02:
  - epoll_create1
  LTP_8988E5015778894A:
  - getrlimit
  LTP_89AC9F4AA9032B8D:
  - write
  LTP_89BB56D579EEF06D:
  - getcwd
  LTP_89C9E8458EC38C11:
  - cachestat
  LTP_8A337DE81B7EE722:
  - madvise
  LTP_8A4C03F737A3CEE6:
  - fchmodat
  LTP_8AC11633EA3D83E0:
  - access
  LTP_8AC9E6F26C2E3CFE:
  - recvfrom
  LTP_8AD8032754BC8842:
  - cacheflush
  LTP_8ADB82F00C61D567:
  - epoll_ctl
  LTP_8B1A2084BCF096F1:
  - access
  LTP_8B3FBDFD0453EF40:
  - access
  LTP_8B80C0CDA587165C:
  - readlinkat
  LTP_8B95C6DD7983D3F3:
  - sched_getattr
  LTP_8BB576EB2E1E6B23:
  - access
  LTP_8BCA62F97A197BC2:
  - getsockopt
  LTP_8BD2C43CB1EC6794:
  - fchmodat2
  LTP_8BFB8BE2E39B38A1:
  - finit_module
  LTP_8C1C2578972FCA1D:
  - getpgid
  LTP_8C508A50371B6444:
  - access
  LTP_8C796FAE0FBF7688:
  - mlock
  LTP_8CA8B0BC6ED845C4:
  - getdents64
  LTP_8CB51F0A9F8FDEA1:
  - access
  LTP_8CFEBBA603A7011A:
  - ssetmask
  LTP_8D3BFFA98E2561BA:
  - access
  LTP_8D3FD114CB0C7420:
  - swapon
  LTP_8D54825D4B298C7C:
  - access
  LTP_8D6B83A8176DB57E:
  - listxattr
  LTP_8D95C734339E42C6:
  - settimeofday
  LTP_8E7F1BE3D7D7823B:
  - access
  LTP_8ED8688C6292FECF:
  - symlink
  LTP_8F29388433422812:
  - access
  LTP_8F30861E18D66625:
  - epoll_wait
  LTP_8F4CA997DDB954AF:
  - readlinkat
  LTP_8F9E255B19623C24:
  - listxattr
  LTP_8FF73194288F8473:
  - access
  LTP_90068DD4526FEFC0:
  - fstatat
  LTP_906135780505447D:
  - access
  LTP_9062D40054E147B9:
  - rename
  LTP_90893935E64240AA:
  - getpagesize
  LTP_90B95E5DF2BD7509:
  - fstatfs
  LTP_90CF6ADF43644434:
  - rename
  LTP_911B97B972658989:
  - access
  LTP_912BE233FAFE6762:
  - getcwd
  LTP_913EC5DF431DC6C2:
  - pathconf
  LTP_914935DA5C379DA1:
  - getrlimit
  LTP_919ABCA2598F53B5:
  - access
  LTP_91ED7E85761CE00F:
  - getrlimit
  LTP_92006BB83B7F5B92:
  - gethostname
  LTP_921D4802D7690C64:
  - access
  LTP_9256D223D5EF4AF0:
  - flock
  LTP_9260E923CF8AA018:
  - access
  LTP_929B120944D8F805:
  - access
  LTP_930417433305D40F:
  - init_module
  LTP_9305FA6D8B835652:
  - getrlimit
  LTP_93949494FBAD3568:
  - access
  LTP_93C53F01B8732C42:
  - move_mount
  LTP_93F2091ECF31C3E0:
  - preadv2
  LTP_9445A602B4F98B83:
  - pathconf
  LTP_9461AA782926BAB4:
  - getpgid
  LTP_94654CBF1E34C32B:
  - pidfd_getfd
  LTP_947B3CCE7DA0998E:
  - mq_notify
  LTP_94E36E221125BFAF:
  - access
  LTP_955ECE70D81CA226:
  - access
  LTP_9586C4C3CAC60BBC:
  - lgetxattr
  LTP_95C156C7EBB823A1:
  - sched_getattr
  LTP_95F0657B8229FF85:
  - umount
  LTP_96021AFB69E847F9:
  - access
  LTP_963957F80E751EE6:
  - getrlimit
  LTP_963EAEB0B41C7934:
  - fpathconf
  LTP_969660F14B0B297A:
  - listxattr
  LTP_969C39F409BFD7AA:
  - access
  LTP_96B2A3E7AC7B2444:
  - fchmod
  LTP_96D205FACA0DD8DB:
  - access
  LTP_96D8C80548B2B4E0:
  - umount
  LTP_96F07DC5DDC8E018:
  - access
  LTP_971DB17D32C51561:
  - socket
  LTP_97C442AC56780374:
  - access
  LTP_97D64C0E53AA3FA4:
  - sched_setaffinity
  LTP_9847441A67CBCED8:
  - madvise
  LTP_9866FB6F1F726CA0:
  - access
  LTP_9869F02C8AF1851D:
  - mlock2
  LTP_986F211E7D45CAD7:
  - access
  LTP_98EC66149EE68933:
  - alarm
  LTP_99C45ECA20496C98:
  - getpriority
  LTP_99D44C1A136DF4B7:
  - swapon
  LTP_99DF5C34778032E1:
  - chroot
  LTP_9A3244C4CEBE8674:
  - pwritev2
  LTP_9A462447EA8872E9:
  - setpriority
  LTP_9A723EA0B1F0D1BE:
  - access
  LTP_9B0BA3ADF46F5FF4:
  - getpriority
  LTP_9B32E51680CE0BEE:
  - readlinkat
  LTP_9B3646398697EA64:
  - dup3
  LTP_9B36D27A4A2994D0:
  - timer_delete
  LTP_9B507ED32C4F4B43:
  - swapon
  LTP_9C2FB7732A0B90B6:
  - waitid
  LTP_9C9D222A34799D55:
  - access
  LTP_9CA9C6B61C3317A3:
  - accept
  LTP_9CDCD3C4BA6C2702:
  - access
  LTP_9CEE24911B622031:
  - pread64
  LTP_9D13DF07435A4B33:
  - rename
  LTP_9D233BC9DED7A8AA:
  - mkdirat
  LTP_9D4E5ED344B5751D:
  - setpriority
  LTP_9E2C65A6408DD9D3:
  - pause
  LTP_9F30FD7002BC2EBA:
  - read
  LTP_9F560A103CB6F910:
  - dup2
  LTP_9FB758C1B4AF2411:
  - lstat
  LTP_9FC19C1455EBA67E:
  - setpgid
  LTP_9FD87A3F7688FEF1:
  - waitid
  LTP_9FE663EAF1F0ABCF:
  - fsconfig
  LTP_A00E343F4A556B3D:
  - capset
  LTP_A030561DFACE8C93:
  - finit_module
  LTP_A0547B601C515355:
  - getrlimit
  LTP_A16555D2419FBCD4:
  - finit_module
  LTP_A17272D4FE0F040B:
  - access
  LTP_A179D109B034EA29:
  - mq_notify
  LTP_A1AECDF3F41769B2:
  - times
  LTP_A1B6FBC6EF800331:
  - fchmod
  LTP_A1D08F4E94B7899A:
  - listen
  LTP_A1DEE046C0A10B18:
  - access
  LTP_A2098D60C40310A2:
  - sendmsg
  LTP_A2934B80997B62C9:
  - waitpid
  LTP_A2A80201A4364230:
  - flock
  LTP_A2AC8B6C7F993351:
  - timer_getoverrun
  LTP_A2E3A27D541DED02:
  - kill
  LTP_A30F7687D403407B:
  - access
  LTP_A363671517C058B1:
  - fstat
  LTP_A367723236ADA8B4:
  - sysinfo
  LTP_A4060315D2E047EE:
  - access
  LTP_A426BD8C5041DE5E:
  - mincore
  LTP_A4733D4B2FEBE9A4:
  - access
  LTP_A48CE326DC781ECE:
  - mount_setattr
  LTP_A49B95E01ADFC6F8:
  - sendfile
  LTP_A4A662687B98D33F:
  - socket
  LTP_A4DD0508E65CC9FB:
  - sendmsg
  LTP_A4E6C06F187B9504:
  - preadv2
  LTP_A500A46C4B998E74:
  - access
  LTP_A54F3585CC70C99F:
  - sendfile
  LTP_A55106AB533523B0:
  - sched_setattr
  LTP_A5BD363654740DDE:
  - read
  LTP_A6B15E4F4EBDDB36:
  - recvfrom
  LTP_A6B94E8A2A4D8853:
  - access
  LTP_A774FC10727E8ED2:
  - dup
  LTP_A82CC878A661AA28:
  - getpgrp
  LTP_A9544B59EB6712D9:
  - access
  LTP_A9596E932167B3EF:
  - access
  LTP_A9B80928550B9520:
  - sendmsg
  LTP_A9BC7EBC1784A722:
  - sched_yield
  LTP_A9DD0D461E032A07:
  - fsconfig
  LTP_AA6F0F0A8A469B13:
  - readahead
  LTP_AA9171FB32FD0C67:
  - getsockname
  LTP_AACDFBA8019E2D25:
  - tee
  LTP_AB48F262BBB2CC93:
  - access
  LTP_ABB01FA7743F966A:
  - listen
  LTP_ABFA54B9CA53F29E:
  - sendto
  LTP_AC0FB73B4EE420EC:
  - access
  LTP_AC5312B5BF09186C:
  - readlinkat
  LTP_AC7D82691053FF4D:
  - fsconfig
  LTP_ACD12B8C0803E654:
  - epoll_wait
  LTP_ACF7A30AF3B10973:
  - execveat
  LTP_AD3A4B98FF201ABE:
  - wait
  LTP_AD81218450587FA8:
  - access
  LTP_AD9C93AEB21E0E7B:
  - init_module
  LTP_ADD30BEEC40E661F:
  - access
  LTP_ADEB5FE2DF97542A:
  - epoll_ctl
  LTP_AE3908C408304451:
  - copy_file_range
  LTP_AE4AAF77935210BC:
  - madvise
  LTP_AE4CE76865CD4D6D:
  - flock
  LTP_AF0FA27496E3610E:
  - preadv2
  LTP_AF52DA4E6DA2BC9B:
  - setpriority
  LTP_AF8D38878ED1A9DA:
  - socket
  LTP_AFD4E9B4327B6D40:
  - sendto
  LTP_AFDAD0AD4FE0E3FF:
  - munlock
  LTP_B0433B78A1641F24:
  - symlink
  LTP_B058D6B9CBBB459D:
  - getrlimit
  LTP_B061BD44067799D7:
  - sigprocmask
  LTP_B06B0397728F35C3:
  - pwritev2
  LTP_B08ED7334608FAA8:
  - preadv2
  LTP_B10A19D425C6416F:
  - sched_setattr
  LTP_B1D822DF0057B4E0:
  - access
  LTP_B200AFD97E91C2CC:
  - access
  LTP_B212BAAA2C2C75CC:
  - sysinfo
  LTP_B25461243478CEF8:
  - getsockname
  LTP_B34188BD305465CA:
  - recv
  LTP_B3F848BCBCBAB559:
  - epoll_wait
  LTP_B4B9F07E1C1A3826:
  - fsconfig
  LTP_B4FD0E2B4B84F458:
  - fchmodat
  LTP_B53406D510ED4981:
  - access
  LTP_B549A3600766CD49:
  - settimeofday
  LTP_B5959FE5199E821F:
  - flock
  LTP_B6DAF13EF3143EBF:
  - access
  LTP_B6DD7EB9951128C1:
  - preadv2
  LTP_B72405976D9F15E6:
  - getsockopt
  LTP_B7606EDCC1F1031F:
  - pidfd_send_signal
  LTP_B7A341967DF2BD69:
  - alarm
  LTP_B7F51635806E7E59:
  - dup2
  LTP_B84B9DEC792BCB34:
  - lgetxattr
  LTP_B86CDF340A27A5B7:
  - fchmod
  LTP_B87A71DE5DE1260E:
  - copy_file_range
  LTP_B8A61982E829826E:
  - munlock
  LTP_B8EA21096E591EBB:
  - flock
  LTP_B90CB73F36B70C6F:
  - accept
  LTP_B917BA457313E93D:
  - mkdirat
  LTP_B984D0FF91909634:
  - openat2
  LTP_B9908D4015443661:
  - access
  LTP_B9CDD41A0DC2AFCC:
  - access
  LTP_BA03F1BD9B5F2BE2:
  - finit_module
  LTP_BA0600CDE607FB7A:
  - sendto
  LTP_BA10984A4B0DE2C6:
  - access
  LTP_BA10B957ACB3FFC3:
  - umount
  LTP_BA9A8FE901467960:
  - cachestat
  LTP_BAE8F852378DD9F4:
  - copy_file_range
  LTP_BB4C88C7C212DAC7:
  - setpriority
  LTP_BBBCFD7524CBB3CD:
  - mkdirat
  LTP_BC4FACB4E14118C5:
  - settimeofday
  LTP_BC662075E3BAE807:
  - access
  LTP_BD3B3CC9032DF4E5:
  - gettid
  LTP_BD5C209F4C6EE910:
  - getrlimit
  LTP_BDA36F61423EEB3E:
  - dup2
  LTP_BE2E778739EF01D5:
  - access
  LTP_BF2428964ADD116F:
  - close
  LTP_BF31641F04151F3C:
  - pathconf
  LTP_BF679B7A7E60BCFD:
  - fpathconf
  LTP_BFCEAB073A576D51:
  - madvise
  LTP_C05360D699C55915:
  - mlock
  LTP_C054C1DCF56C7CDC:
  - mlockall
  LTP_C0577C0D678214DA:
  - access
  LTP_C0694665E22D48E8:
  - syslog
  LTP_C071A7FFF929A2A5:
  - access
  LTP_C09E83BE36885312:
  - gethostname
  LTP_C0AA45BC29F98A0E:
  - access
  LTP_C12A995BA4553344:
  - madvise
  LTP_C13C4F63D58904BC:
  - waitid
  LTP_C1462BACF46A177B:
  - madvise
  LTP_C16D549555A00E55:
  - copy_file_range
  LTP_C1C67435FC56D878:
  - access
  LTP_C218D3CB0AD80D90:
  - cacheflush
  LTP_C24E55F06625D564:
  - wait4
  LTP_C2909AC2ECEDED94:
  - faccessat2
  LTP_C3098F5341F14B0E:
  - socket
  LTP_C3433C582C87D21B:
  - lstat
  LTP_C346EFF1233F7061:
  - mmap
  LTP_C37E693AB7AA5E28:
  - flistxattr
  LTP_C46B746DAC4331D5:
  - get_robust_list
  LTP_C5FE18F9550B31BA:
  - access
  LTP_C678E0C87280F82D:
  - fsconfig
  LTP_C6A719982BDE9CE4:
  - access
  LTP_C6E67CB1FD2B1F64:
  - access
  LTP_C785774773FB7524:
  - alarm
  LTP_C7B73F4D5B87736A:
  - alarm
  LTP_C7D18796DD651AE8:
  - faccessat2
  LTP_C7E8278CFEF81C98:
  - recv
  LTP_C80C019BE3F47901:
  - alarm
  LTP_C8376BC347F94A98:
  - syslog
  LTP_C8536F49779345AA:
  - sendfile
  LTP_C86E220567585ADC:
  - sendto
  LTP_C87041F4B4B5A930:
  - pathconf
  LTP_C8C667C37A069984:
  - read
  LTP_C8DAE34819E335F8:
  - access
  LTP_C8F11074F91F94EF:
  - symlink
  LTP_C93391BCF53E8020:
  - kill
  LTP_C9789067DD7A3D60:
  - llistxattr
  LTP_C994B56A41A71C1A:
  - access
  LTP_C9AF84778DBE8B78:
  - pidfd_getfd
  LTP_C9D2C2E3FC2B9581:
  - llistxattr
  LTP_CA1E4549CF7692F9:
  - rename
  LTP_CA3E9D83D71EEED4:
  - lstat
  LTP_CA45A33676AD236D:
  - access
  LTP_CA80C3F10B65226D:
  - access
  LTP_CB31E19EE807FFDB:
  - access
  LTP_CB42FAF7C1D6D702:
  - sbrk
  LTP_CB84D44C84EB80BE:
  - sendfile
  LTP_CBB1680336D53D2A:
  - epoll_ctl
  LTP_CBB45E0BB83FDEB0:
  - lstat
  LTP_CBF4B6C8A1458A28:
  - close_range
  LTP_CC9037A76978B569:
  - copy_file_range
  LTP_CCC36F43E9463D3E:
  - fchdir
  LTP_CCDB1776DAA2C318:
  - access
  LTP_CD185859D6C012C8:
  - mlockall
  LTP_CD2150BE4FE81F31:
  - alarm
  LTP_CDCDC1B9E63D58C3:
  - access
  LTP_CE12B215EFDE3D4D:
  - copy_file_range
  LTP_CE45382D3DE75F8F:
  - access
  LTP_CEBAD6AB3C82795E:
  - access
  LTP_CED2FCC737A99D40:
  - capget
  LTP_CEE8E7C01B4D8059:
  - madvise
  LTP_CF7B49C4B74D69E7:
  - setpgid
  LTP_D01667E52BF34BFC:
  - sendfile
  LTP_D0800876342DE939:
  - openat2
  LTP_D0A69D14ADE1718C:
  - msync
  LTP_D0BAC1CBF594EDA6:
  - madvise
  LTP_D0E32E5D27E643A9:
  - chroot
  LTP_D12172005842E2A5:
  - epoll_wait
  LTP_D17799C1BB191952:
  - rename
  LTP_D191923C5ACBADC1:
  - mlock2
  LTP_D1A18560E485E146:
  - waitid
  LTP_D1AADFC2F7C6F594:
  - capset
  LTP_D1B6112551D45B31:
  - alarm
  LTP_D1D51B0412DFB097:
  - pwritev2
  LTP_D1DAB36EB37FCA27:
  - fpathconf
  LTP_D1F469715ECC4195:
  - access
  LTP_D23BA34DB5624198:
  - sched_setaffinity
  LTP_D246498B20D9CB2C:
  - init_module
  LTP_D254EE40E8B5957E:
  - utime
  LTP_D296A517F138A0C0:
  - dup2
  LTP_D297A923D4C5FEC7:
  - mq_notify
  LTP_D2D67AB5E38A7000:
  - access
  LTP_D2E2A5F40B2313E5:
  - msync
  LTP_D2E5AAE97E0E50FE:
  - mkdirat
  LTP_D2F4BCF2263C56F5:
  - access
  LTP_D30F83EC0B5B2E08:
  - pathconf
  LTP_D331AAEAED1F6297:
  - pathconf
  LTP_D33B1BBC658C83D4:
  - openat2
  LTP_D3506D1539EC71AB:
  - mount_setattr
  LTP_D3E85F64C28BBC4F:
  - sendfile
  LTP_D3FBF11AA35FDC98:
  - utime
  LTP_D412A09DEDC43045:
  - access
  LTP_D4159BF3AB78E108:
  - llistxattr
  LTP_D4B433A3696803A8:
  - alarm
  LTP_D4D8A0FEAA2F6B09:
  - access
  LTP_D4E6A74BAB2E8722:
  - pwrite64
  LTP_D579FCFC71E6EB6A:
  - cacheflush
  LTP_D58C26D260BBCED5:
  - init_module
  LTP_D5D78F93265A1980:
  - fsconfig
  LTP_D5DAD3494DBAE67F:
  - getpriority
  LTP_D5F414741594F6E3:
  - pwrite64
  LTP_D615E29C0C4C9CCB:
  - fsconfig
  LTP_D63AFAA6729CB519:
  - flock
  LTP_D653D15777B77A1F:
  - access
  LTP_D6A52FD61BF01578:
  - access
  LTP_D72526C4E4301D60:
  - access
  LTP_D744D6C4A0C3E40C:
  - munmap
  LTP_D758596147111328:
  - rename
  LTP_D75F86A534CB6E02:
  - epoll_wait
  LTP_D76652434EC85091:
  - access
  LTP_D77858597BCC1C13:
  - faccessat2
  LTP_D77AD0D4DC9C0C9E:
  - getsockopt
  LTP_D7936678BF685610:
  - rename
  LTP_D7C638B9DFF7DBC3:
  - sched_setaffinity
  LTP_D7FFD8EE209AB524:
  - mlockall
  LTP_D839FF9444196DDB:
  - madvise
  LTP_D87AF1C2D0AF66D2:
  - poll
  LTP_D8B58CA743EBE711:
  - access
  LTP_D8E4FF36A3FE1F41:
  - recvfrom
  LTP_D8F99518FF4E8643:
  - symlink
  LTP_D90C4B47C5FF6BC9:
  - request_key
  LTP_D90E4279570B6A94:
  - madvise
  LTP_D9418F7424E86C28:
  - mlock2
  LTP_D9561EEACFF72902:
  - sendmsg
  LTP_D982FA373261CE5D:
  - swapon
  LTP_D98D789F4EBA6817:
  - rename
  LTP_D9A5AE03D93C5C6D:
  - read
  LTP_DA10E351BC730D85:
  - access
  LTP_DA64FD04E43656E6:
  - waitid
  LTP_DA65D6C7A0E4ABBC:
  - finit_module
  LTP_DA8094714BA3F734:
  - getpgid
  LTP_DAA03BAD070DB1D6:
  - access
  LTP_DAA1F16D8A298E83:
  - access
  LTP_DACAAECF088B0CFE:
  - lstat
  LTP_DB6066C00D231BA4:
  - copy_file_range
  LTP_DB77907DDC5EDFF4:
  - waitpid
  LTP_DBAE060B9CA303DD:
  - pwritev2
  LTP_DBEC3975C5440D23:
  - setpgid
  LTP_DBFBE6A110B3D17B:
  - getsockname
  LTP_DC1ACD3B300AFCC3:
  - getsockopt
  LTP_DC3D9E7D5D1A75DE:
  - preadv2
  LTP_DC7E9134BB7F6F7A:
  - sched_setattr
  LTP_DC9BC72148835FDC:
  - capget
  LTP_DCB33BB29D296843:
  - access
  LTP_DCC88B2C458969EA:
  - symlink
  LTP_DD2E1A555B603C7B:
  - socket
  LTP_DD64353E8E427275:
  - pathconf
  LTP_DD647A49F00FCC45:
  - recvfrom
  LTP_DD9A41090E3D5A17:
  - access
  LTP_DDA854712C50CD6A:
  - symlink
  LTP_DDCD82CA2726175D:
  - nanosleep
  LTP_DE6F80C5EFE44A9D:
  - dup2
  LTP_DF1C4714B16B760E:
  - access
  LTP_DF5B725563FDFB31:
  - waitid
  LTP_DF9A0B3ADAC6AE1D:
  - socket
  LTP_E0470C189C2D1DE3:
  - set_robust_list
  LTP_E06D53042C10C99E:
  - capset
  LTP_E083F071E292B561:
  - gettid
  LTP_E0B177A8B6FE4225:
  - access
  LTP_E0ED96B80FC3B6C9:
  - access
  LTP_E13B9C2C9645B841:
  - accept
  LTP_E1B6C6D1C8603A83:
  - rename
  LTP_E20E7069E7FA34D5:
  - munmap
  LTP_E2196C3F0F58862B:
  - copy_file_range
  LTP_E2360C045F1BCE8E:
  - preadv2
  LTP_E272B715ECA16E6C:
  - umount
  LTP_E28B5BB57A450438:
  - access
  LTP_E2C3B68EDF07A753:
  - access
  LTP_E2D73477ACB0308D:
  - setegid
  LTP_E316C28E36E136DA:
  - socket
  LTP_E34945E3DE91022F:
  - access
  LTP_E3A3CF8B98E460BC:
  - access
  LTP_E3B5C7908A7B12CC:
  - mq_notify
  LTP_E3BA4E4FAEF39F91:
  - getsid
  LTP_E3E59B16A96A60BC:
  - brk
  LTP_E41DD7230DA067DD:
  - access
  LTP_E46539F2D47BA5EC:
  - access
  LTP_E4D1B76D80905462:
  - access
  LTP_E520E500AB3AE851:
  - close
  LTP_E560C027210BF20A:
  - access
  LTP_E56EFFCF50E90E41:
  - openat2
  LTP_E5791B389C67677E:
  - access
  LTP_E5E50FB7BDD033D9:
  - access
  LTP_E5E64FCDA6CACABE:
  - pidfd_open
  LTP_E6750A641272AF1B:
  - fsconfig
  LTP_E6A7D5E5327D8ECC:
  - pidfd_getfd
  LTP_E6C69C9F4AB565BC:
  - getrlimit
  LTP_E7435E0CBCA319E1:
  - epoll_create
  LTP_E7CB95EADCE845E9:
  - syslog
  LTP_E7E64809057630A5:
  - request_key
  LTP_E8CF2AE0EC60602C:
  - epoll_wait
  LTP_E8E97EBE8E041CF0:
  - kill
  LTP_E98952E12501919D:
  - request_key
  LTP_E9D60674E416A5DC:
  - open_by_handle_at
  LTP_EA58792F115B6235:
  - request_key
  LTP_EA5D1572B890F71E:
  - epoll_wait
  LTP_EA7E63D027CD6941:
  - pidfd_getfd
  LTP_EA90C626D9AA6C08:
  - msync
  LTP_EA953D5E5C4B2B1F:
  - getrlimit
  LTP_EB00EA74B30E438E:
  - access
  LTP_EB1B734A0943248E:
  - fstatfs
  LTP_EB214534D857AE95:
  - ftruncate
  LTP_EB40C6ADD4390CB3:
  - munlockall
  LTP_EB425D988F2F7604:
  - access
  LTP_EB7FFB63F4259214:
  - fchmodat
  LTP_EBB107DB7E3EFF2A:
  - madvise
  LTP_EBCE1A2B8CE59ECE:
  - fsconfig
  LTP_EBD54180D0CAB16B:
  - chroot
  LTP_EBF0020C32AD44C8:
  - access
  LTP_EC19279F1BC5A623:
  - pathconf
  LTP_EC19C6410BBE0467:
  - access
  LTP_EC1CA29BE6888A6B:
  - epoll_wait
  LTP_EC23768761E40E9F:
  - capset
  LTP_EC25ABB5C68F5299:
  - ftruncate
  LTP_ECD986F27CF15E1E:
  - waitid
  LTP_ED2BA909DF79625A:
  - dup
  LTP_ED36488372A175F5:
  - access
  LTP_ED3B9CFAEBD0EAB8:
  - mprotect
  LTP_ED3F2AE7E59E6F12:
  - access
  LTP_EE1518958A8F7CC1:
  - access
  LTP_EE540E689227BDBF:
  - mkdirat
  LTP_EE7A979F212D6C0C:
  - chroot
  LTP_EE8E695CF61D6D8A:
  - dup2
  LTP_EEDED564522D8D2D:
  - faccessat2
  LTP_EF4053B74F85E11B:
  - pwritev2
  LTP_EF5C1F365208AD31:
  - access
  LTP_EF9CD83ECACAA86C:
  - tkill
  LTP_F041ABCAF1E2177F:
  - symlink
  LTP_F04C2129F0253CC0:
  - fchmodat
  LTP_F101CC6D9DF71519:
  - recvfrom
  LTP_F1044C71B6626419:
  - accept
  LTP_F10E5286CF6CAC64:
  - flistxattr
  LTP_F1299BC5F92BF26E:
  - fchmod
  LTP_F13024AE4BC5C024:
  - kill
  LTP_F1391DB634702128:
  - move_mount
  LTP_F13B0055458E603F:
  - finit_module
  LTP_F1DC44813DCA6A05:
  - close_range
  LTP_F202F3C3B02DEA0E:
  - access
  LTP_F284E6C48F6B4BF8:
  - move_mount
  LTP_F2C1952707BEC602:
  - sendmsg
  LTP_F318E892720C2991:
  - msync
  LTP_F3200B697F38DD16:
  - access
  LTP_F3418C5C403B91FC:
  - access
  LTP_F36F8C0CC1A6D840:
  - mmap
  LTP_F38A837D067865DC:
  - syslog
  LTP_F3CE94166822B3E3:
  - get_robust_list
  LTP_F421E1E61753B72C:
  - fchmod
  LTP_F43EC0D01CCFD25A:
  - access
  LTP_F4DE81D703447628:
  - close_range
  LTP_F5D2C7B7F0E3D07C:
  - getpgid
  LTP_F61B5384B4A60F55:
  - mlock
  LTP_F6456DE083F145B0:
  - preadv2
  LTP_F65E54AE96F20D41:
  - fchmodat2
  LTP_F66773BC44256D99:
  - lgetxattr
  LTP_F66DDB5A0EBC5C9F:
  - fsconfig
  LTP_F6BB86F5DCC2FAC8:
  - access
  LTP_F6DD03A9DC1C07D4:
  - mkdirat
  LTP_F70FC66A56FBD769:
  - access
  LTP_F75110BE79864CD1:
  - ustat
  LTP_F7998813C90A7A08:
  - access
  LTP_F7AC6006DC3C06BB:
  - mlock2
  LTP_F7B8EDE302D5D08A:
  - faccessat2
  LTP_F8CDD57D76C8FA6C:
  - access
  LTP_F8FD511858BB650D:
  - getsid
  LTP_F92A1A6292F40811:
  - fstatfs
  LTP_F92CEB15161CB23C:
  - unshare
  LTP_F9357233C6D73800:
  - getpgid
  LTP_F99DE159B75F22A2:
  - kill
  LTP_F9BF08369A08E5ED:
  - access
  LTP_FA4A7CD85E7F31FE:
  - mprotect
  LTP_FA750E6088863E30:
  - sched_getattr
  LTP_FADBA4ADECCFBA4E:
  - getrlimit
  LTP_FAECCAD19268C313:
  - pidfd_send_signal
  LTP_FAF274CF431E6421:
  - nanosleep
  LTP_FB047DBB72D78D19:
  - flock
  LTP_FB0ABF26A21EAE3C:
  - getrlimit
  LTP_FB3B521CE41A299A:
  - preadv2
  LTP_FB7C7C6EA4808026:
  - read
  LTP_FBEB6959ED2912C8:
  - iopl
  LTP_FC1E41C3414E7F21:
  - getcwd
  LTP_FC50E16C03A7EED9:
  - mlock
  LTP_FC5B16AB3C53A744:
  - access
  LTP_FC8BA85373EA2D8F:
  - waitpid
  LTP_FCA376B46A9873B0:
  - access
  LTP_FCC236A4D5926B81:
  - tkill
  LTP_FCC82752F512BE72:
  - seccomp
  LTP_FCF5A4835CFCD143:
  - gettimeofday
  LTP_FD1B65B0BCC88E0D:
  - mmap
  LTP_FD400AE357F2EBB3:
  - openat2
  LTP_FDE0B30F1CFCAA4B:
  - fsconfig
  LTP_FE37A7A30B8E2AFB:
  - mprotect
  LTP_FE471F5051750B9C:
  - pidfd_send_signal
  LTP_FE4A57F142065A14:
  - migrate_pages
  LTP_FE4AD44ED28FE386:
  - umask
  LTP_FE51D85F4A425C61:
  - getsockopt
  LTP_FE57D3FF371E3DDC:
  - rt_sigprocmask
  LTP_FE8AA14F6A64DF2D:
  - mkdirat
  LTP_FE9B97F71E485E58:
  - mlock2
  LTP_FEACDC300C3E1DD7:
  - mmap
  LTP_FEDD56BEBCE11F81:
  - rename
  LTP_FEDE14E9D4DE9A9D:
  - pathconf
  LTP_FF1A8A6101CEA37E:
  - fpathconf
  LTP_FF639650AE6F7097:
  - getdents64
  LTP_FF9C0F9669A39525:
  - chroot
static:
- check_id: STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS
  rule_refs:
  - LTP_425E5A3502541DE8
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/fd_ops.rs
  patterns:
  - label: first and last use unsigned 32-bit syscall semantics
    regex: 'pub fn sys_close_range\(first: u32, last: u32, flags: u32\)'
    matched: true
    line: 489
  - label: the maximum unsigned range is accepted and capped to open descriptors
    regex: pub fn sys_close_range\([\s\S]*?for fd in first\.\.=last\.min\(max_index as u32\)[\s\S]*?Ok\(0\)
    matched: true
    line: 489
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO
  rule_refs:
  - LTP_74BB3F96CBA52D02
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/io.rs
  patterns:
  - label: oversized len returns Linux EOVERFLOW rather than EINVAL
    regex: pub fn sys_copy_file_range\([\s\S]*?if len > isize::MAX as usize \{[\s\S]*?return Err\(AxError::from\(LinuxError::EOVERFLOW\)\);
    matched: true
    line: 773
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_EPOLL_NESTED_LOOP
  rule_refs:
  - LTP_66C670178B06E9F3
  result: pass
  path: os/StarryOS/kernel/src/file/epoll.rs
  patterns:
  - label: add detects whether a nested epoll reaches the destination instance
    regex: pub fn add\([\s\S]*?downcast_arc::<Epoll>\(\)[\s\S]*?reaches_epoll\([\s\S]*?AxError::FilesystemLoop
    matched: true
    line: 501
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINAL_ERRNO_TRANSLATION
  rule_refs:
  - LTP_02908A57586A60CF
  - LTP_10B3572DBFA6742B
  - LTP_22F13AFD9925B2AE
  - LTP_25D7B6229831E0EF
  - LTP_287CF10D893735AB
  - LTP_4184881E196F9E5E
  - LTP_498695B75BD43DAD
  - LTP_4FCD61E2EED61335
  - LTP_6B9F97B897EC5C32
  - LTP_6D02D744B460F97E
  - LTP_82A8802A27A3D2BF
  - LTP_89AC9F4AA9032B8D
  - LTP_9FD87A3F7688FEF1
  - LTP_B212BAAA2C2C75CC
  - LTP_C8376BC347F94A98
  - LTP_C8F11074F91F94EF
  - LTP_DB77907DDC5EDFF4
  - LTP_E272B715ECA16E6C
  - LTP_F92CEB15161CB23C
  - LTP_FCC236A4D5926B81
  result: pass
  path: components/axerrno/src/lib.rs
  patterns:
  - label: bad user addresses translate to EFAULT
    regex: BadAddress \| BadState => EFAULT
    matched: true
    line: 223
  - label: bad descriptors translate to EBADF
    regex: BadFileDescriptor => EBADF
    matched: true
    line: 224
  - label: invalid inputs translate to EINVAL
    regex: InvalidInput \| InvalidData => EINVAL
    matched: true
    line: 235
  - label: permission failures translate to EPERM
    regex: OperationNotPermitted => EPERM
    matched: true
    line: 250
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINAL_SYMLINK_USER_POINTERS
  rule_refs:
  - LTP_C8F11074F91F94EF
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/ctl.rs
  patterns:
  - label: symlinkat loads the target and link path before filesystem access
    regex: pub fn sys_symlinkat\([\s\S]*?vm_load_string\(target\)\?;[\s\S]*?vm_load_path_string\(linkpath\)\?;
    matched: true
    line: 440
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINAL_SYSINFO_COPYOUT
  rule_refs:
  - LTP_A367723236ADA8B4
  - LTP_B212BAAA2C2C75CC
  result: pass
  path: os/StarryOS/kernel/src/syscall/sys.rs
  patterns:
  - label: sysinfo populates core fields and copies the structure to userspace
    regex: pub fn sys_sysinfo\([\s\S]*?kinfo\.uptime[\s\S]*?kinfo\.totalram[\s\S]*?kinfo\.freeram[\s\S]*?kinfo\.procs[\s\S]*?info\.vm_write\(kinfo\)\?;\s*Ok\(0\)
    matched: true
    line: 720
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINAL_SYSLOG_CONSOLE_LEVEL
  rule_refs:
  - LTP_02908A57586A60CF
  - LTP_18304438A1D5D6C1
  - LTP_4FCD61E2EED61335
  - LTP_C0694665E22D48E8
  result: pass
  path: os/StarryOS/kernel/src/syscall/sys.rs
  patterns:
  - label: console levels outside one through eight are invalid
    regex: SYSLOG_ACTION_CONSOLE_LEVEL => \{[\s\S]*?if !\(1\.\.=8\)\.contains\(&len\) \{\s*return Err\(AxError::InvalidInput\);
    matched: true
    line: 808
  - label: a valid console level replaces the prior level
    regex: let old_level = state\.console_level;\s*state\.console_level = len;\s*Ok\(old_level as isize\)
    matched: true
    line: 814
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINAL_SYSLOG_CONTROL_ACTIONS
  rule_refs:
  - LTP_4828EB12592F311C
  - LTP_6D819B66D5B60871
  - LTP_7F4262FC753FC8D9
  - LTP_F38A837D067865DC
  result: pass
  path: os/StarryOS/kernel/src/syscall/sys.rs
  patterns:
  - label: open and close actions succeed directly
    regex: SYSLOG_ACTION_CLOSE \| SYSLOG_ACTION_OPEN => Ok\(0\)
    matched: true
    line: 754
  - label: console off and on update the enabled state
    regex: SYSLOG_ACTION_CONSOLE_OFF => \{[\s\S]*?console_enabled = false;[\s\S]*?SYSLOG_ACTION_CONSOLE_ON
      => \{[\s\S]*?console_enabled = true;
    matched: true
    line: 796
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINAL_SYSLOG_INVALID_ACTION
  rule_refs:
  - LTP_4184881E196F9E5E
  result: pass
  path: os/StarryOS/kernel/src/syscall/sys.rs
  patterns:
  - label: unknown syslog actions return InvalidInput
    regex: pub fn sys_syslog\([\s\S]*?_ => Err\(AxError::InvalidInput\),\s*\}
    matched: true
    line: 752
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINAL_SYSLOG_PRIVILEGE
  rule_refs:
  - LTP_498695B75BD43DAD
  result: pass
  path: os/StarryOS/kernel/src/syscall/sys.rs
  patterns:
  - label: unprivileged callers receive OperationNotPermitted
    regex: fn require_syslog_privilege\([\s\S]*?euid == 0[\s\S]*?Err\(AxError::OperationNotPermitted\)
    matched: true
    line: 744
  - label: read actions invoke the privilege check
    regex: SYSLOG_ACTION_READ => \{\s*(?:validate_syslog_read_args\(buf, len\)\?;\s*)?require_syslog_privilege\(\)\?;
    matched: true
    line: 755
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINAL_SYSLOG_READ_ARGUMENTS
  rule_refs:
  - LTP_6B9F97B897EC5C32
  - LTP_C8376BC347F94A98
  result: fail
  path: os/StarryOS/kernel/src/syscall/sys.rs
  patterns:
  - label: destructive reads validate their user buffer and signed length
    regex: SYSLOG_ACTION_READ => \{\s*validate_syslog_read_args\(buf, len\)\?;
    matched: false
    line: null
  - label: read-all validates its user buffer and signed length
    regex: SYSLOG_ACTION_READ_ALL => \{\s*validate_syslog_read_args\(buf, len\)\?;
    matched: false
    line: null
  reason: one or more required patterns did not match
  finding_ids:
  - finding-syslog-ltp-6b9f97b897ec5c32-444533f79a99
  - finding-syslog-ltp-c8376bc347f94a98-444533f79a99
- check_id: STARRY_FINAL_TIMER_DELETE
  rule_refs:
  - LTP_10B3572DBFA6742B
  - LTP_9B36D27A4A2994D0
  result: pass
  path: os/StarryOS/kernel/src/syscall/time.rs
  patterns:
  - label: successful deletion returns zero and an unknown ID is invalid
    regex: pub fn sys_timer_delete\([\s\S]*?posix_timers\.delete\(timerid\) \{\s*Ok\(0\)\s*\} else \{\s*Err\(AxError::InvalidInput\)
    matched: true
    line: 268
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINAL_TKILL_TID_VALIDATION
  rule_refs:
  - LTP_FCC236A4D5926B81
  result: fail
  path: os/StarryOS/kernel/src/syscall/signal.rs
  patterns:
  - label: tkill rejects zero and negative tids with InvalidInput
    regex: pub fn sys_tkill\([\s\S]*?if tid <= 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}
    matched: false
    line: null
  reason: one or more required patterns did not match
  finding_ids:
  - finding-tkill-ltp-fcc236a4d5926b81-444533f79a99
- check_id: STARRY_FINAL_UMOUNT_MOUNTPOINT
  rule_refs:
  - LTP_E272B715ECA16E6C
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/mount.rs
  patterns:
  - label: non-mount targets return InvalidInput
    regex: if !target\.is_root_of_mount\(\) \{\s*return Err\(AxError::InvalidInput\);
    matched: true
    line: 140
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINAL_UMOUNT_PRIVILEGE
  rule_refs:
  - LTP_287CF10D893735AB
  result: fail
  path: os/StarryOS/kernel/src/syscall/fs/mount.rs
  patterns:
  - label: umount rejects callers without CAP_SYS_ADMIN
    regex: pub fn sys_umount2\([\s\S]*?has_cap_sys_admin\(\)[\s\S]*?return Err\(AxError::OperationNotPermitted\);
    matched: false
    line: null
  reason: one or more required patterns did not match
  finding_ids:
  - finding-umount-ltp-287cf10d893735ab-444533f79a99
- check_id: STARRY_FINAL_UMOUNT_USER_PATH
  rule_refs:
  - LTP_6D02D744B460F97E
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/mount.rs
  patterns:
  - label: umount copies the user path before resolving it
    regex: pub fn sys_umount2\([\s\S]*?let target = vm_load_string\(target\)\?;
    matched: true
    line: 297
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINAL_UNAME_COPYOUT
  rule_refs:
  - LTP_25D7B6229831E0EF
  - LTP_5516B8A938B9C3A5
  result: pass
  path: os/StarryOS/kernel/src/syscall/sys.rs
  patterns:
  - label: uname builds utsname and writes it through VmMutPtr
    regex: pub fn sys_uname\([\s\S]*?build_utsname\(&ns\)[\s\S]*?name\.vm_write\(uts\)\?;\s*Ok\(0\)
    matched: true
    line: 662
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINAL_UNSHARE_FLAG_VALIDATION
  rule_refs:
  - LTP_F92CEB15161CB23C
  result: pass
  path: os/StarryOS/kernel/src/syscall/task/namespace.rs
  patterns:
  - label: unsupported unshare flags return InvalidInput
    regex: pub fn sys_unshare\([\s\S]*?flags & !SUPPORTED_NS_FLAGS != 0[\s\S]*?return Err\(AxError::InvalidInput\);
    matched: true
    line: 25
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINAL_UNSHARE_NEWNS_PRIVILEGE
  rule_refs:
  - LTP_82A8802A27A3D2BF
  result: fail
  path: os/StarryOS/kernel/src/syscall/task/namespace.rs
  patterns:
  - label: mount namespace unshare rejects callers without CAP_SYS_ADMIN
    regex: flags & CLONE_NEWNS != 0[\s\S]*?![\s\S]*?has_cap_sys_admin\(\)[\s\S]*?return Err\(AxError::OperationNotPermitted\);
    matched: false
    line: null
  reason: one or more required patterns did not match
  finding_ids:
  - finding-unshare-ltp-82a8802a27a3d2bf-444533f79a99
- check_id: STARRY_FINAL_WAITID_OPTIONS
  rule_refs:
  - LTP_9FD87A3F7688FEF1
  result: pass
  path: os/StarryOS/kernel/src/syscall/task/wait.rs
  patterns:
  - label: waitid rejects calls without exited stopped or continued events
    regex: if !options[\s\S]*?intersects\(WaitIdOptions::WEXITED \| WaitIdOptions::WUNTRACED \| WaitIdOptions::WCONTINUED\)[\s\S]*?return
      Err\(AxError::InvalidInput\);
    matched: true
    line: 382
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINAL_WAITPID_OPTIONS
  rule_refs:
  - LTP_DB77907DDC5EDFF4
  result: pass
  path: os/StarryOS/kernel/src/syscall/task/wait.rs
  patterns:
  - label: invalid wait4 option bits return InvalidInput
    regex: pub fn sys_waitpid\([\s\S]*?WaitPidOptions::from_bits\(options\)\.ok_or\(AxError::InvalidInput\)\?;
    matched: true
    line: 234
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINAL_WRITE_BAD_FD
  rule_refs:
  - LTP_22F13AFD9925B2AE
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/io.rs
  patterns:
  - label: write propagates descriptor lookup errors first
    regex: pub fn sys_write\([\s\S]*?let file_like = get_file_like\(fd\)\?;[\s\S]*?validate_user_read_buf
    matched: true
    line: 138
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINAL_WRITE_USER_BUFFER
  rule_refs:
  - LTP_89AC9F4AA9032B8D
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/io.rs
  patterns:
  - label: write validates and copies readable user memory
    regex: validate_user_read_buf\(buf\.cast_const\(\), len\)\?;[\s\S]*?copy_user_read_buf\(buf\.cast_const\(\),
      len\)\?;
    matched: true
    line: 141
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINIT_MODULE_FLAG_VALIDATION
  rule_refs:
  - LTP_DA65D6C7A0E4ABBC
  result: pass
  path: os/StarryOS/kernel/src/syscall/kmod.rs
  patterns:
  - label: finit_module names and inspects its flags argument
    regex: 'pub fn sys_finit_module\(module_fd: i32, param_ptr: \*const u8, flags: u32\)'
    matched: true
    line: 46
  - label: unsupported nonzero flags return InvalidInput
    regex: pub fn sys_finit_module\([\s\S]*?if flags != 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}
    matched: true
    line: 46
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE
  rule_refs:
  - LTP_6C14DE68E3C0CC24
  result: pass
  path: os/StarryOS/kernel/src/syscall/time.rs
  patterns:
  - label: handler accepts both timeval and timezone pointers
    regex: 'pub fn sys_gettimeofday\(ts: \*mut timeval, tz: \*mut Timezone\)'
    matched: true
    line: 43
  - label: non-null timezone output uses checked VM access
    regex: tz\.nullable\(\)[\s\S]*?tz\.vm_write\(Timezone::default\(\)\)\?;
    matched: true
    line: 47
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND3_INIT_MODULE_PERMISSION
  rule_refs:
  - LTP_D246498B20D9CB2C
  result: pass
  path: os/StarryOS/kernel/src/syscall/kmod.rs
  patterns:
  - label: init_module checks CAP_SYS_MODULE
    regex: pub fn sys_init_module\([\s\S]*?if !current\(\)\.as_thread\(\)\.cred\(\)\.has_cap_sys_module\(\)
    matched: true
    line: 22
  - label: permission failure precedes user-buffer access
    regex: pub fn sys_init_module\([\s\S]*?has_cap_sys_module\(\)[\s\S]*?return Err\(AxError::OperationNotPermitted\);[\s\S]*?VmBytes::new
    matched: true
    line: 22
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND5_SETPGID_NEGATIVE
  rule_refs:
  - LTP_4308D71D8BD6519D
  result: pass
  path: os/StarryOS/kernel/src/syscall/task/job.rs
  patterns:
  - label: setpgid preserves signed syscall arguments
    regex: 'pub fn sys_setpgid\(pid: i32, pgid: i32\) -> AxResult<isize>'
    matched: true
    line: 40
  - label: negative pid or pgid is rejected with invalid input
    regex: pub fn sys_setpgid\([\s\S]*?if pid < 0 \|\| pgid < 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}
    matched: true
    line: 40
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND5_SOCKET_INVALID_TYPE
  rule_refs:
  - LTP_971DB17D32C51561
  result: pass
  path: os/StarryOS/kernel/src/syscall/net/socket.rs
  patterns:
  - label: unsupported type in a supported domain is invalid input
    regex: pub fn sys_socket\([\s\S]*?\(AF_INET \| AF_INET6, _\) \| \(AF_UNIX, _\) \| \(AF_NETLINK, _\)
      \| \(AF_VSOCK, _\) => \{[\s\S]*?return Err\(AxError::InvalidInput\);[\s\S]*?\n\}\n\npub fn sys_bind
    matched: true
    line: 35
  reason: all required patterns matched
  finding_ids: []
dynamic:
- test_id: STARRY_FINAL_SYSINFO_BEHAVIOR
  rule_refs:
  - LTP_A367723236ADA8B4
  - LTP_B212BAAA2C2C75CC
  result: pass
  exit_code: 0
  command:
  - cargo
  - xtask
  - starry
  - test
  - qemu
  - --arch
  - riscv64
  - -c
  - qemu/system/test-sysinfo
  reason: command exited successfully
  output_tail: "unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//etc/nsswitch.conf\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//etc/modules\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//etc/inittab\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//etc/hosts\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//etc/hostname\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//etc/group\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//etc/fstab\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//etc/resolv.conf\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//etc\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/tmp\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/spool/cron\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/spool\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/opt\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/mail\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/local\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/lib/misc\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/lib\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/empty\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/cache/apk\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/cache/misc\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/cache\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/log/apk.log\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var/log\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//var\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//guest/linux/linux-qemu\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//guest/linux/manifest.txt\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//guest/linux\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//guest/nimbos/manifest.txt\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//guest/nimbos/nimbos-qemu\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//guest/nimbos/nimbos-qemu-usertests\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//guest/nimbos/nimbos-qemu.img\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//guest/nimbos\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root//guest\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root/\n\
    cd /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system && /home/cloud/gitWork/qemu-10.2.1/build/qemu-riscv64\
    \ -L /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root\
    \ /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root/bin/busybox\
    \ sh -eu /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system/prebuild.sh\n/usr/bin/cmake\
    \ -S /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system -B /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/build\
    \ -G 'Unix Makefiles' -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/ -DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY\
    \ -DCMAKE_TOOLCHAIN_FILE=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/cmake-toolchain.cmake\
    \ -DCMAKE_MAKE_PROGRAM=/usr/bin/make -DPKG_CONFIG_EXECUTABLE=/usr/bin/pkg-config -DSTARRY_STAGING_ROOT=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/staging-root\
    \ -DSTARRY_GROUPED_C_SUBCASES=test-sysinfo\nCMake Warning:\n  Manually-specified variables were not\
    \ used by the project:\n\n    PKG_CONFIG_EXECUTABLE\n    STARRY_STAGING_ROOT\n\n\n/usr/bin/cmake --build\
    \ /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/build\
    \ --parallel\n/usr/bin/cmake --install /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/build\n\
    debugfs -w /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86054-0/case-rootfs.img\n\
    debugfs 1.46.5 (30-Dec-2021)\nrm: File not found by ext2_lookup while trying to resolve filename\n\
    rm: File not found by ext2_lookup while trying to resolve filename\nrm: File not found by ext2_lookup\
    \ while trying to resolve filename\n"
  output_truncated: true
  finding_ids: []
- test_id: STARRY_FINAL_SYSLOG_BEHAVIOR
  rule_refs:
  - LTP_02908A57586A60CF
  - LTP_18304438A1D5D6C1
  - LTP_330C66A049727F75
  - LTP_4184881E196F9E5E
  - LTP_4828EB12592F311C
  - LTP_498695B75BD43DAD
  - LTP_4FCD61E2EED61335
  - LTP_6D819B66D5B60871
  - LTP_7F4262FC753FC8D9
  - LTP_C0694665E22D48E8
  - LTP_E7CB95EADCE845E9
  - LTP_F38A837D067865DC
  result: pass
  exit_code: 0
  command:
  - cargo
  - xtask
  - starry
  - test
  - qemu
  - --arch
  - riscv64
  - -c
  - qemu/system/test-syslog
  reason: command exited successfully
  output_tail: "-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//etc/nsswitch.conf\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//etc/modules\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//etc/inittab\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//etc/hosts\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//etc/hostname\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//etc/group\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//etc/fstab\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//etc/resolv.conf\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//etc\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/tmp\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/spool/cron\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/spool\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/opt\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/mail\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/local\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/lib/misc\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/lib\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/empty\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/cache/apk\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/cache/misc\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/cache\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/log/apk.log\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var/log\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//var\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//guest/linux/linux-qemu\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//guest/linux/manifest.txt\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//guest/linux\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//guest/nimbos/manifest.txt\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//guest/nimbos/nimbos-qemu\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//guest/nimbos/nimbos-qemu-usertests\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//guest/nimbos/nimbos-qemu.img\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//guest/nimbos\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root//guest\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root/\n\
    cd /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system && /home/cloud/gitWork/qemu-10.2.1/build/qemu-riscv64\
    \ -L /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root\
    \ /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root/bin/busybox\
    \ sh -eu /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system/prebuild.sh\n/usr/bin/cmake\
    \ -S /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system -B /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/build\
    \ -G 'Unix Makefiles' -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/ -DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY\
    \ -DCMAKE_TOOLCHAIN_FILE=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/cmake-toolchain.cmake\
    \ -DCMAKE_MAKE_PROGRAM=/usr/bin/make -DPKG_CONFIG_EXECUTABLE=/usr/bin/pkg-config -DSTARRY_STAGING_ROOT=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/staging-root\
    \ -DSTARRY_GROUPED_C_SUBCASES=test-syslog\nCMake Warning:\n  Manually-specified variables were not\
    \ used by the project:\n\n    PKG_CONFIG_EXECUTABLE\n    STARRY_STAGING_ROOT\n\n\n/usr/bin/cmake --build\
    \ /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/build\
    \ --parallel\n/usr/bin/cmake --install /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/build\n\
    debugfs -w /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86485-0/case-rootfs.img\n\
    debugfs 1.46.5 (30-Dec-2021)\nrm: File not found by ext2_lookup while trying to resolve filename\n\
    rm: File not found by ext2_lookup while trying to resolve filename\nrm: File not found by ext2_lookup\
    \ while trying to resolve filename\n"
  output_truncated: true
  finding_ids: []
- test_id: STARRY_FINAL_TIMER_DELETE_BEHAVIOR
  rule_refs:
  - LTP_10B3572DBFA6742B
  - LTP_9B36D27A4A2994D0
  result: pass
  exit_code: 0
  command:
  - cargo
  - xtask
  - starry
  - test
  - qemu
  - --arch
  - riscv64
  - -c
  - qemu/system/syscall-test-timer-family
  reason: command exited successfully
  output_tail: "elf/qemu-cases/qemu/system/runs/86919-0/staging-root//etc/nsswitch.conf\ndump_file: Operation\
    \ not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//etc/modules\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//etc/inittab\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//etc/hosts\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//etc/hostname\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//etc/group\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//etc/fstab\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//etc/resolv.conf\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//etc\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/tmp\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/spool/cron\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/spool\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/opt\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/mail\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/local\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/lib/misc\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/lib\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/empty\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/cache/apk\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/cache/misc\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/cache\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/log/apk.log\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var/log\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//var\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//guest/linux/linux-qemu\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//guest/linux/manifest.txt\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//guest/linux\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//guest/nimbos/manifest.txt\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//guest/nimbos/nimbos-qemu\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//guest/nimbos/nimbos-qemu-usertests\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//guest/nimbos/nimbos-qemu.img\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//guest/nimbos\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root//guest\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root/\n\
    cd /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system && /home/cloud/gitWork/qemu-10.2.1/build/qemu-riscv64\
    \ -L /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root\
    \ /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root/bin/busybox\
    \ sh -eu /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system/prebuild.sh\n/usr/bin/cmake\
    \ -S /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system -B /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/build\
    \ -G 'Unix Makefiles' -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/ -DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY\
    \ -DCMAKE_TOOLCHAIN_FILE=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/cmake-toolchain.cmake\
    \ -DCMAKE_MAKE_PROGRAM=/usr/bin/make -DPKG_CONFIG_EXECUTABLE=/usr/bin/pkg-config -DSTARRY_STAGING_ROOT=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/staging-root\
    \ -DSTARRY_GROUPED_C_SUBCASES=syscall-test-timer-family\nCMake Warning:\n  Manually-specified variables\
    \ were not used by the project:\n\n    PKG_CONFIG_EXECUTABLE\n    STARRY_STAGING_ROOT\n\n\n/usr/bin/cmake\
    \ --build /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/build\
    \ --parallel\n/usr/bin/cmake --install /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/build\n\
    debugfs -w /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/86919-0/case-rootfs.img\n\
    debugfs 1.46.5 (30-Dec-2021)\nrm: File not found by ext2_lookup while trying to resolve filename\n\
    rm: File not found by ext2_lookup while trying to resolve filename\nrm: File not found by ext2_lookup\
    \ while trying to resolve filename\n"
  output_truncated: true
  finding_ids: []
- test_id: STARRY_FINAL_UNAME_BEHAVIOR
  rule_refs:
  - LTP_25D7B6229831E0EF
  - LTP_5516B8A938B9C3A5
  result: pass
  exit_code: 0
  command:
  - cargo
  - xtask
  - starry
  - test
  - qemu
  - --arch
  - riscv64
  - -c
  - qemu/system/test-uname
  reason: command exited successfully
  output_tail: "c-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//etc/nsswitch.conf\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//etc/modules\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//etc/inittab\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//etc/hosts\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//etc/hostname\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//etc/group\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//etc/fstab\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//etc/resolv.conf\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//etc\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/tmp\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/spool/cron\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/spool\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/opt\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/mail\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/local\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/lib/misc\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/lib\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/empty\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/cache/apk\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/cache/misc\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/cache\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/log/apk.log\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var/log\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//var\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//guest/linux/linux-qemu\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//guest/linux/manifest.txt\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//guest/linux\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//guest/nimbos/manifest.txt\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//guest/nimbos/nimbos-qemu\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//guest/nimbos/nimbos-qemu-usertests\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//guest/nimbos/nimbos-qemu.img\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//guest/nimbos\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root//guest\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root/\n\
    cd /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system && /home/cloud/gitWork/qemu-10.2.1/build/qemu-riscv64\
    \ -L /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root\
    \ /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root/bin/busybox\
    \ sh -eu /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system/prebuild.sh\n/usr/bin/cmake\
    \ -S /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system -B /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/build\
    \ -G 'Unix Makefiles' -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/ -DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY\
    \ -DCMAKE_TOOLCHAIN_FILE=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/cmake-toolchain.cmake\
    \ -DCMAKE_MAKE_PROGRAM=/usr/bin/make -DPKG_CONFIG_EXECUTABLE=/usr/bin/pkg-config -DSTARRY_STAGING_ROOT=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/staging-root\
    \ -DSTARRY_GROUPED_C_SUBCASES=test-uname\nCMake Warning:\n  Manually-specified variables were not\
    \ used by the project:\n\n    PKG_CONFIG_EXECUTABLE\n    STARRY_STAGING_ROOT\n\n\n/usr/bin/cmake --build\
    \ /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/build\
    \ --parallel\n/usr/bin/cmake --install /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/build\n\
    debugfs -w /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87349-0/case-rootfs.img\n\
    debugfs 1.46.5 (30-Dec-2021)\nrm: File not found by ext2_lookup while trying to resolve filename\n\
    rm: File not found by ext2_lookup while trying to resolve filename\nrm: File not found by ext2_lookup\
    \ while trying to resolve filename\n"
  output_truncated: true
  finding_ids: []
- test_id: STARRY_FINAL_WAIT4_BEHAVIOR
  rule_refs:
  - LTP_2AE73292A13647D5
  - LTP_DB77907DDC5EDFF4
  result: pass
  exit_code: 0
  command:
  - cargo
  - xtask
  - starry
  - test
  - qemu
  - --arch
  - riscv64
  - -c
  - qemu/system/bugfix-bug-wait4-invalid-options
  reason: command exited successfully
  output_tail: "u-cases/qemu/system/runs/87788-0/staging-root//etc/nsswitch.conf\ndump_file: Operation\
    \ not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//etc/modules\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//etc/inittab\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//etc/hosts\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//etc/hostname\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//etc/group\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//etc/fstab\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//etc/resolv.conf\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//etc\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/tmp\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/spool/cron\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/spool\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/opt\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/mail\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/local\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/lib/misc\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/lib\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/empty\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/cache/apk\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/cache/misc\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/cache\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/log/apk.log\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var/log\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//var\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//guest/linux/linux-qemu\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//guest/linux/manifest.txt\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//guest/linux\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//guest/nimbos/manifest.txt\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//guest/nimbos/nimbos-qemu\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//guest/nimbos/nimbos-qemu-usertests\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//guest/nimbos/nimbos-qemu.img\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//guest/nimbos\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root//guest\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root/\n\
    cd /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system && /home/cloud/gitWork/qemu-10.2.1/build/qemu-riscv64\
    \ -L /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root\
    \ /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root/bin/busybox\
    \ sh -eu /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system/prebuild.sh\n/usr/bin/cmake\
    \ -S /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system -B /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/build\
    \ -G 'Unix Makefiles' -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/ -DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY\
    \ -DCMAKE_TOOLCHAIN_FILE=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/cmake-toolchain.cmake\
    \ -DCMAKE_MAKE_PROGRAM=/usr/bin/make -DPKG_CONFIG_EXECUTABLE=/usr/bin/pkg-config -DSTARRY_STAGING_ROOT=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/staging-root\
    \ -DSTARRY_GROUPED_C_SUBCASES=bugfix-bug-wait4-invalid-options\nCMake Warning:\n  Manually-specified\
    \ variables were not used by the project:\n\n    PKG_CONFIG_EXECUTABLE\n    STARRY_STAGING_ROOT\n\n\
    \n/usr/bin/cmake --build /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/build\
    \ --parallel\n/usr/bin/cmake --install /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/build\n\
    debugfs -w /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/87788-0/case-rootfs.img\n\
    debugfs 1.46.5 (30-Dec-2021)\nrm: File not found by ext2_lookup while trying to resolve filename\n\
    rm: File not found by ext2_lookup while trying to resolve filename\nrm: File not found by ext2_lookup\
    \ while trying to resolve filename\n"
  output_truncated: true
  finding_ids: []
- test_id: STARRY_FINAL_WAITID_BEHAVIOR
  rule_refs:
  - LTP_0FE0E20EAC6DE889
  - LTP_53E7B9C40A44F6D0
  - LTP_74C73CBABE325D5D
  - LTP_77C2FB4A0A9E30F2
  - LTP_9FD87A3F7688FEF1
  result: pass
  exit_code: 0
  command:
  - cargo
  - xtask
  - starry
  - test
  - qemu
  - --arch
  - riscv64
  - -c
  - qemu/system/zombie-bugfix-bug-waitid-basic
  reason: command exited successfully
  output_tail: "emu-cases/qemu/system/runs/88223-0/staging-root//etc/nsswitch.conf\ndump_file: Operation\
    \ not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//etc/modules\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//etc/inittab\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//etc/hosts\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//etc/hostname\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//etc/group\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//etc/fstab\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//etc/resolv.conf\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//etc\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/tmp\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/spool/cron\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/spool\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/opt\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/mail\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/local\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/lib/misc\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/lib\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/empty\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/cache/apk\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/cache/misc\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/cache\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/log/apk.log\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var/log\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//var\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//guest/linux/linux-qemu\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//guest/linux/manifest.txt\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//guest/linux\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//guest/nimbos/manifest.txt\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//guest/nimbos/nimbos-qemu\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//guest/nimbos/nimbos-qemu-usertests\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//guest/nimbos/nimbos-qemu.img\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//guest/nimbos\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root//guest\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root/\n\
    cd /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system && /home/cloud/gitWork/qemu-10.2.1/build/qemu-riscv64\
    \ -L /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root\
    \ /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root/bin/busybox\
    \ sh -eu /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system/prebuild.sh\n/usr/bin/cmake\
    \ -S /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system -B /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/build\
    \ -G 'Unix Makefiles' -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/ -DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY\
    \ -DCMAKE_TOOLCHAIN_FILE=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/cmake-toolchain.cmake\
    \ -DCMAKE_MAKE_PROGRAM=/usr/bin/make -DPKG_CONFIG_EXECUTABLE=/usr/bin/pkg-config -DSTARRY_STAGING_ROOT=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/staging-root\
    \ -DSTARRY_GROUPED_C_SUBCASES=zombie-bugfix-bug-waitid-basic\nCMake Warning:\n  Manually-specified\
    \ variables were not used by the project:\n\n    PKG_CONFIG_EXECUTABLE\n    STARRY_STAGING_ROOT\n\n\
    \n/usr/bin/cmake --build /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/build\
    \ --parallel\n/usr/bin/cmake --install /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/build\n\
    debugfs -w /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88223-0/case-rootfs.img\n\
    debugfs 1.46.5 (30-Dec-2021)\nrm: File not found by ext2_lookup while trying to resolve filename\n\
    rm: File not found by ext2_lookup while trying to resolve filename\nrm: File not found by ext2_lookup\
    \ while trying to resolve filename\n"
  output_truncated: true
  finding_ids: []
- test_id: STARRY_FINAL_WRITE_FILE_BEHAVIOR
  rule_refs:
  - LTP_1B4A2A1831541F06
  - LTP_22F13AFD9925B2AE
  result: pass
  exit_code: 0
  command:
  - cargo
  - xtask
  - starry
  - test
  - qemu
  - --arch
  - riscv64
  - -c
  - qemu/system/syscall-test-write
  reason: command exited successfully
  output_tail: "n-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//etc/nsswitch.conf\ndump_file:\
    \ Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//etc/modules\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//etc/inittab\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//etc/hosts\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//etc/hostname\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//etc/group\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//etc/fstab\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//etc/resolv.conf\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//etc\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/tmp\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/spool/cron\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/spool\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/opt\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/mail\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/local\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/lib/misc\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/lib\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/empty\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/cache/apk\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/cache/misc\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/cache\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/log/apk.log\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var/log\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//var\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//guest/linux/linux-qemu\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//guest/linux/manifest.txt\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//guest/linux\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//guest/nimbos/manifest.txt\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//guest/nimbos/nimbos-qemu\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//guest/nimbos/nimbos-qemu-usertests\n\
    dump_file: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//guest/nimbos/nimbos-qemu.img\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//guest/nimbos\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root//guest\n\
    rdump: Operation not permitted while changing ownership of /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root/\n\
    cd /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system && /home/cloud/gitWork/qemu-10.2.1/build/qemu-riscv64\
    \ -L /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root\
    \ /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root/bin/busybox\
    \ sh -eu /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system/prebuild.sh\n/usr/bin/cmake\
    \ -S /home/cloud/gitLinux/tgoskits/test-suit/starryos/qemu/system -B /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/build\
    \ -G 'Unix Makefiles' -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/ -DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY\
    \ -DCMAKE_TOOLCHAIN_FILE=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/cmake-toolchain.cmake\
    \ -DCMAKE_MAKE_PROGRAM=/usr/bin/make -DPKG_CONFIG_EXECUTABLE=/usr/bin/pkg-config -DSTARRY_STAGING_ROOT=/home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/staging-root\
    \ -DSTARRY_GROUPED_C_SUBCASES=syscall-test-write\nCMake Warning:\n  Manually-specified variables were\
    \ not used by the project:\n\n    PKG_CONFIG_EXECUTABLE\n    STARRY_STAGING_ROOT\n\n\n/usr/bin/cmake\
    \ --build /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/build\
    \ --parallel\n/usr/bin/cmake --install /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/build\n\
    debugfs -w /home/cloud/gitLinux/tgoskits/target/riscv64gc-unknown-none-elf/qemu-cases/qemu/system/runs/88654-0/case-rootfs.img\n\
    debugfs 1.46.5 (30-Dec-2021)\nrm: File not found by ext2_lookup while trying to resolve filename\n\
    rm: File not found by ext2_lookup while trying to resolve filename\nrm: File not found by ext2_lookup\
    \ while trying to resolve filename\n"
  output_truncated: true
  finding_ids: []
counts:
  static_pass: 24
  static_fail: 4
  static_error: 0
  dynamic_pass: 7
  dynamic_fail: 0
  dynamic_skipped: 0
  dynamic_not_run: 0
  findings: 35
  blockers: 0
  new_findings: 0
  carried_findings: 30
  revalidated_findings: 6
  needs_revalidation: 30
blockers: []
finding_ids:
- finding-symlink-ltp-21fcbfc328d1815a-444533f79a99
- finding-symlink-ltp-b0433b78a1641f24-444533f79a99
- finding-symlink-ltp-dcc88b2c458969ea-444533f79a99
- finding-symlink-ltp-dda854712c50cd6a-444533f79a99
- finding-syslog-ltp-6b9f97b897ec5c32-444533f79a99
- finding-syslog-ltp-c8376bc347f94a98-444533f79a99
- finding-tkill-ltp-fcc236a4d5926b81-444533f79a99
- finding-umount-ltp-287cf10d893735ab-444533f79a99
- finding-unshare-ltp-40a45c5e82d7f4a1-444533f79a99
- finding-unshare-ltp-82a8802a27a3d2bf-444533f79a99
- finding-utime-ltp-04236fd5b061deb9-444533f79a99
- finding-utime-ltp-38432b154b641410-444533f79a99
- finding-utime-ltp-43728156b00ff104-444533f79a99
- finding-utime-ltp-58c8c307b1ff2510-444533f79a99
- finding-utime-ltp-6f4b3a38b8bf4c7e-444533f79a99
- finding-utime-ltp-6f77caa9fc4423ba-444533f79a99
- finding-utime-ltp-71dd72481ef5740e-444533f79a99
- finding-utime-ltp-86144bf50fb25d3a-444533f79a99
- finding-utime-ltp-d254ee40e8b5957e-444533f79a99
- finding-wait-ltp-7b0f966046aeca7e-444533f79a99
- finding-wait-ltp-ad3a4b98ff201abe-444533f79a99
- finding-wait4-ltp-1691f6f9712c5546-444533f79a99
- finding-wait4-ltp-c24e55f06625d564-444533f79a99
- finding-waitid-ltp-4494b70bba693d42-444533f79a99
- finding-waitid-ltp-9c2fb7732a0b90b6-444533f79a99
- finding-waitid-ltp-c13c4f63d58904bc-444533f79a99
- finding-waitid-ltp-d1a18560e485e146-444533f79a99
- finding-waitid-ltp-da64fd04e43656e6-444533f79a99
- finding-waitid-ltp-df5b725563fdfb31-444533f79a99
- finding-waitid-ltp-ecd986f27cf15e1e-444533f79a99
- finding-waitpid-ltp-03af14160f8b59a0-444533f79a99
- finding-waitpid-ltp-2f3e34fd672dbf34-444533f79a99
- finding-waitpid-ltp-614c018f61c078a0-444533f79a99
- finding-waitpid-ltp-a2934b80997b62c9-444533f79a99
- finding-waitpid-ltp-fc8ba85373ea2d8f-444533f79a99
finding_versions:
  finding-syslog-ltp-6b9f97b897ec5c32-444533f79a99:
    id: finding-syslog-ltp-6b9f97b897ec5c32-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:6e3e081833f717594d197308038a0349052b6be391cb407ea73d6a6496711463
  finding-syslog-ltp-c8376bc347f94a98-444533f79a99:
    id: finding-syslog-ltp-c8376bc347f94a98-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:ded313eb76b2aeed3abf80757d0ec757bdb5c98adc2f9f43d7f3b06423a19cfc
  finding-tkill-ltp-fcc236a4d5926b81-444533f79a99:
    id: finding-tkill-ltp-fcc236a4d5926b81-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:01964c626d97f1fd4895de25c676f5e6ae47d5303439d4656e98208b1ef23937
  finding-umount-ltp-287cf10d893735ab-444533f79a99:
    id: finding-umount-ltp-287cf10d893735ab-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:1c1ee7cfcb91eb188fdbadc67a6d6f2cbb76c9cf2929860ab301dd6721e5d5ef
  finding-unshare-ltp-82a8802a27a3d2bf-444533f79a99:
    id: finding-unshare-ltp-82a8802a27a3d2bf-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:97b20614908c0e484594f7749a2812eb70034f2e064b09b7b85b206657ee8c00
  finding-symlink-ltp-21fcbfc328d1815a-444533f79a99:
    id: finding-symlink-ltp-21fcbfc328d1815a-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:00055c572728efebe717fdfd5bd1d81fd91c3d60a1a5db8335a548649c3cd2f4
  finding-symlink-ltp-b0433b78a1641f24-444533f79a99:
    id: finding-symlink-ltp-b0433b78a1641f24-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:0c94c6c60fdba8a76ebf7398bc4714e94092d7b53b5ed91ca83a9357d7d39438
  finding-symlink-ltp-dcc88b2c458969ea-444533f79a99:
    id: finding-symlink-ltp-dcc88b2c458969ea-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:bea522e18a66550001a02bc8a6214d91eedefa34e1f3dd722bc2448b4b492571
  finding-symlink-ltp-dda854712c50cd6a-444533f79a99:
    id: finding-symlink-ltp-dda854712c50cd6a-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:3afbc23416fcd0a054b8f94992cf91d014981c174e2d0277d85611d961f49f55
  finding-unshare-ltp-40a45c5e82d7f4a1-444533f79a99:
    id: finding-unshare-ltp-40a45c5e82d7f4a1-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:94f6279901df9a804ea9a485b0f9f209b02fb8f807644361b9ba812457a0ccaf
  finding-utime-ltp-04236fd5b061deb9-444533f79a99:
    id: finding-utime-ltp-04236fd5b061deb9-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:69f414273f94ddf5722a058f0ffb853df49dab82923ac283c5dbb46eb9e86e48
  finding-utime-ltp-38432b154b641410-444533f79a99:
    id: finding-utime-ltp-38432b154b641410-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:a24cc110f5a868220acd8058b112be05bc742f2e4da12fdbaf3feed3142ff9d9
  finding-utime-ltp-43728156b00ff104-444533f79a99:
    id: finding-utime-ltp-43728156b00ff104-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:3eea503309856fad9494940a59248daf529a4471267a529c4c95852e8e453438
  finding-utime-ltp-58c8c307b1ff2510-444533f79a99:
    id: finding-utime-ltp-58c8c307b1ff2510-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:2e04a3052eb82efaf27339cc56b65b8db665bfefb103a5b33542a2a4d0c5d654
  finding-utime-ltp-6f4b3a38b8bf4c7e-444533f79a99:
    id: finding-utime-ltp-6f4b3a38b8bf4c7e-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:b703aa048d17d1e1bcd219a73e2078fca2eb79f9a4324b5d12477ebfd88a974f
  finding-utime-ltp-6f77caa9fc4423ba-444533f79a99:
    id: finding-utime-ltp-6f77caa9fc4423ba-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:d5529bbca4b9b1b6df60a07fe44ab89010cd3e4aad696758f502cf2a68f820e6
  finding-utime-ltp-71dd72481ef5740e-444533f79a99:
    id: finding-utime-ltp-71dd72481ef5740e-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:6bda041868b2409a336b6ff637fab38806193cca40e9f963ebd4f9ead13ae6cd
  finding-utime-ltp-86144bf50fb25d3a-444533f79a99:
    id: finding-utime-ltp-86144bf50fb25d3a-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:b3c7e021137ced961d36b7b577b47c397988ad025c1aca5c8330cfb5d952c342
  finding-utime-ltp-d254ee40e8b5957e-444533f79a99:
    id: finding-utime-ltp-d254ee40e8b5957e-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:4a72462bf8f7e4e1eab6769582ba239804cc54f70d906248bd3342e72f50d427
  finding-wait-ltp-7b0f966046aeca7e-444533f79a99:
    id: finding-wait-ltp-7b0f966046aeca7e-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:b034b92b8f57428e05d508ac5750c568ff4d5a63fdc90c07499ab8f2d47e37d9
  finding-wait-ltp-ad3a4b98ff201abe-444533f79a99:
    id: finding-wait-ltp-ad3a4b98ff201abe-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:2649845551bdc2aaf62fa7c61a411e905e50348b018b70385b3a9897d4643fc7
  finding-wait4-ltp-1691f6f9712c5546-444533f79a99:
    id: finding-wait4-ltp-1691f6f9712c5546-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:05aea0480c0354c50a573870f32304277fcdce2504d4e04a54f0aad03d99089c
  finding-wait4-ltp-c24e55f06625d564-444533f79a99:
    id: finding-wait4-ltp-c24e55f06625d564-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:f2dfbf511904494ea7378a94460d326f2193522e2b0718593f0bf7e5ae532e39
  finding-waitid-ltp-4494b70bba693d42-444533f79a99:
    id: finding-waitid-ltp-4494b70bba693d42-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:3bd2aeb5893259b5861a0fcd9c6a025406c22680e5ca91be3a80367eec5e3e94
  finding-waitid-ltp-9c2fb7732a0b90b6-444533f79a99:
    id: finding-waitid-ltp-9c2fb7732a0b90b6-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:dc9fdf4e5a10accba9202149329f6a8dce658d6857f64eefc5ef36ed3378da58
  finding-waitid-ltp-c13c4f63d58904bc-444533f79a99:
    id: finding-waitid-ltp-c13c4f63d58904bc-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:d87fadac54390b6d6d59f5acadc6ac1f480225b8f750ffb7d2edc8d6a2a4ad89
  finding-waitid-ltp-d1a18560e485e146-444533f79a99:
    id: finding-waitid-ltp-d1a18560e485e146-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:edfd668fce6d7724b90d24c9b17dd100ff2c30a93a0d6718d5ef8aea541b3a19
  finding-waitid-ltp-da64fd04e43656e6-444533f79a99:
    id: finding-waitid-ltp-da64fd04e43656e6-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:ef66f780e94c364edf6bc23ac1286df38855342b9e35cc0b0b7e566f06e0a0c2
  finding-waitid-ltp-df5b725563fdfb31-444533f79a99:
    id: finding-waitid-ltp-df5b725563fdfb31-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:e113eef68ef3f17a44fcb5adf5353ff519eb2a3a28b3ebb734572d5dfc61246a
  finding-waitid-ltp-ecd986f27cf15e1e-444533f79a99:
    id: finding-waitid-ltp-ecd986f27cf15e1e-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:75cf5e2b76782ceab85ef329f17147cdab59d85f4e5c4b22d14766f74b940b80
  finding-waitpid-ltp-03af14160f8b59a0-444533f79a99:
    id: finding-waitpid-ltp-03af14160f8b59a0-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:7cb8a1b145afb89072fc7d1f80c0f757bb22004b8b9a6bd1381de0a73f78d1b3
  finding-waitpid-ltp-2f3e34fd672dbf34-444533f79a99:
    id: finding-waitpid-ltp-2f3e34fd672dbf34-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:544dd1d5aec570e1ccd8d90d9efa6cd1435574d0a10a6c32ad6f656ca40c6707
  finding-waitpid-ltp-614c018f61c078a0-444533f79a99:
    id: finding-waitpid-ltp-614c018f61c078a0-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:157a23ab84a4f61d869e14f46642d566295000e29fee0458343fd742f67bb227
  finding-waitpid-ltp-a2934b80997b62c9-444533f79a99:
    id: finding-waitpid-ltp-a2934b80997b62c9-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:94601db29d8c3eb35f1e87204944c6bb51370a7dc0320f2ac258b7391dab79ea
  finding-waitpid-ltp-fc8ba85373ea2d8f-444533f79a99:
    id: finding-waitpid-ltp-fc8ba85373ea2d8f-444533f79a99
    generated_at_utc: '2026-07-16T11:06:29.244183Z'
    content_hash: sha256:2ed7c9699152da10f6d875b7d7b9c19d6307640e98b6e37c23f8501b3764700e
new_finding_ids: []
carried_finding_ids:
- finding-symlink-ltp-21fcbfc328d1815a-444533f79a99
- finding-symlink-ltp-b0433b78a1641f24-444533f79a99
- finding-symlink-ltp-dcc88b2c458969ea-444533f79a99
- finding-symlink-ltp-dda854712c50cd6a-444533f79a99
- finding-unshare-ltp-40a45c5e82d7f4a1-444533f79a99
- finding-utime-ltp-04236fd5b061deb9-444533f79a99
- finding-utime-ltp-38432b154b641410-444533f79a99
- finding-utime-ltp-43728156b00ff104-444533f79a99
- finding-utime-ltp-58c8c307b1ff2510-444533f79a99
- finding-utime-ltp-6f4b3a38b8bf4c7e-444533f79a99
- finding-utime-ltp-6f77caa9fc4423ba-444533f79a99
- finding-utime-ltp-71dd72481ef5740e-444533f79a99
- finding-utime-ltp-86144bf50fb25d3a-444533f79a99
- finding-utime-ltp-d254ee40e8b5957e-444533f79a99
- finding-wait-ltp-7b0f966046aeca7e-444533f79a99
- finding-wait-ltp-ad3a4b98ff201abe-444533f79a99
- finding-wait4-ltp-1691f6f9712c5546-444533f79a99
- finding-wait4-ltp-c24e55f06625d564-444533f79a99
- finding-waitid-ltp-4494b70bba693d42-444533f79a99
- finding-waitid-ltp-9c2fb7732a0b90b6-444533f79a99
- finding-waitid-ltp-c13c4f63d58904bc-444533f79a99
- finding-waitid-ltp-d1a18560e485e146-444533f79a99
- finding-waitid-ltp-da64fd04e43656e6-444533f79a99
- finding-waitid-ltp-df5b725563fdfb31-444533f79a99
- finding-waitid-ltp-ecd986f27cf15e1e-444533f79a99
- finding-waitpid-ltp-03af14160f8b59a0-444533f79a99
- finding-waitpid-ltp-2f3e34fd672dbf34-444533f79a99
- finding-waitpid-ltp-614c018f61c078a0-444533f79a99
- finding-waitpid-ltp-a2934b80997b62c9-444533f79a99
- finding-waitpid-ltp-fc8ba85373ea2d8f-444533f79a99
revalidated_finding_ids:
- finding-syslog-ltp-498695b75bd43dad-444533f79a99
- finding-syslog-ltp-6b9f97b897ec5c32-444533f79a99
- finding-syslog-ltp-c8376bc347f94a98-444533f79a99
- finding-tkill-ltp-fcc236a4d5926b81-444533f79a99
- finding-umount-ltp-287cf10d893735ab-444533f79a99
- finding-unshare-ltp-82a8802a27a3d2bf-444533f79a99
needs_revalidation_finding_ids:
- finding-symlink-ltp-21fcbfc328d1815a-444533f79a99
- finding-symlink-ltp-b0433b78a1641f24-444533f79a99
- finding-symlink-ltp-dcc88b2c458969ea-444533f79a99
- finding-symlink-ltp-dda854712c50cd6a-444533f79a99
- finding-unshare-ltp-40a45c5e82d7f4a1-444533f79a99
- finding-utime-ltp-04236fd5b061deb9-444533f79a99
- finding-utime-ltp-38432b154b641410-444533f79a99
- finding-utime-ltp-43728156b00ff104-444533f79a99
- finding-utime-ltp-58c8c307b1ff2510-444533f79a99
- finding-utime-ltp-6f4b3a38b8bf4c7e-444533f79a99
- finding-utime-ltp-6f77caa9fc4423ba-444533f79a99
- finding-utime-ltp-71dd72481ef5740e-444533f79a99
- finding-utime-ltp-86144bf50fb25d3a-444533f79a99
- finding-utime-ltp-d254ee40e8b5957e-444533f79a99
- finding-wait-ltp-7b0f966046aeca7e-444533f79a99
- finding-wait-ltp-ad3a4b98ff201abe-444533f79a99
- finding-wait4-ltp-1691f6f9712c5546-444533f79a99
- finding-wait4-ltp-c24e55f06625d564-444533f79a99
- finding-waitid-ltp-4494b70bba693d42-444533f79a99
- finding-waitid-ltp-9c2fb7732a0b90b6-444533f79a99
- finding-waitid-ltp-c13c4f63d58904bc-444533f79a99
- finding-waitid-ltp-d1a18560e485e146-444533f79a99
- finding-waitid-ltp-da64fd04e43656e6-444533f79a99
- finding-waitid-ltp-df5b725563fdfb31-444533f79a99
- finding-waitid-ltp-ecd986f27cf15e1e-444533f79a99
- finding-waitpid-ltp-03af14160f8b59a0-444533f79a99
- finding-waitpid-ltp-2f3e34fd672dbf34-444533f79a99
- finding-waitpid-ltp-614c018f61c078a0-444533f79a99
- finding-waitpid-ltp-a2934b80997b62c9-444533f79a99
- finding-waitpid-ltp-fc8ba85373ea2d8f-444533f79a99
historical_regression_scope:
  rules:
  - LTP_425E5A3502541DE8
  - LTP_4308D71D8BD6519D
  - LTP_66C670178B06E9F3
  - LTP_6C14DE68E3C0CC24
  - LTP_74BB3F96CBA52D02
  - LTP_971DB17D32C51561
  - LTP_D246498B20D9CB2C
  - LTP_DA65D6C7A0E4ABBC
  static_checks:
  - STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS
  - STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO
  - STARRY_EPOLL_NESTED_LOOP
  - STARRY_FINIT_MODULE_FLAG_VALIDATION
  - STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE
  - STARRY_ROUND3_INIT_MODULE_PERMISSION
  - STARRY_ROUND5_SETPGID_NEGATIVE
  - STARRY_ROUND5_SOCKET_INVALID_TYPE
  dynamic_tests: []
historical_regression_unresolved: {}
content_hash: sha256:3e7418329d0186312400d4a352142622b805d5620900c4c3947d400a8336bdba
```
</details>
