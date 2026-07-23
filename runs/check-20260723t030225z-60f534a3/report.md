# Starry 合规检查报告

## 本轮结论

- 状态：`completed_with_blockers`
- 静态检查：pass 89、fail 10、error 0
- 动态测试：pass 0、fail 0、skipped 0、not_run 2
- confirmed finding：14
- 新增：14、carry forward：0、已重验：0、待重验：0
- 环境或执行 blocker：3（不视为实现缺口）

## 静态检查

### `STARRY_CHROOT_PATH`

- 类型：`static`
- 关联 syscall：`chroot`
- 通用规则：`MAN_F6CB9D32040E99BA`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_chroot\(path: \*const c_char\)[\s\S]*?vm_load_(?:path_)?string\(path\)\?[\s\S]*?fs\.resolve\(path\)\?`：matched=`true`，第 121 行
  - `if loc\.node_type\(\) != NodeType::Directory \{[\s\S]*?return Err\(AxError::NotADirectory\);`：matched=`true`，第 128 行
  - `\*fs = FsContext::new\(loc\);[\s\S]*?Ok\(0\)`：matched=`true`，第 131 行
- finding：—

### `STARRY_CLOSE_BAD_FD_ERRNO`

- 类型：`static`
- 关联 syscall：`close`
- 通用规则：`LTP_09B39E9C9254ECB2`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `BadFileDescriptor => EBADF`：matched=`true`，第 224 行
- finding：—

### `STARRY_CLOSE_FD_TABLE`

- 类型：`static`
- 关联 syscall：`close`
- 通用规则：`LTP_09B39E9C9254ECB2`、`MAN_23E25F7C4136339F`
- 结果：`fail`
- 原因：one or more required patterns did not match
- pattern 证据：

  - `pub fn close_file_like\(fd: c_int\)[\s\S]*?FD_TABLE\.write\(\)\.remove\(fd as usize\)`：matched=`false`，未匹配
  - `pub fn close_file_like\(fd: c_int\)[\s\S]*?return Ok\(\(\)\);[\s\S]*?Err\(AxError::BadFileDescriptor\)`：matched=`true`，第 337 行
- finding：`finding-close-ltp-09b39e9c9254ecb2-07800f218f34`、`finding-close-man-23e25f7c4136339f-07800f218f34`

### `STARRY_CLOSE_RANGE_SWEEP`

- 类型：`static`
- 关联 syscall：`close_range`
- 通用规则：`LTP_76BFF56F735A0074`、`LTP_F4DE81D703447628`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_close_range\([\s\S]*?for fd in first\.\.=last\.min\(max_index as (?:i32\|u32)\)`：matched=`true`，第 541 行
  - `for fd in first\.\.=last\.min\(max_index as (?:i32\|u32)\)[\s\S]*?if let Some\(f\) = fd_table\.remove\(fd as _\)[\s\S]*?Ok\(0\)`：matched=`true`，第 568 行
- finding：—

### `STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS`

- 类型：`static`
- 关联 syscall：`close_range`
- 通用规则：`LTP_425E5A3502541DE8`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_close_range\(first: u32, last: u32, flags: u32\)`：matched=`true`，第 541 行
  - `pub fn sys_close_range\([\s\S]*?for fd in first\.\.=last\.min\(max_index as u32\)[\s\S]*?Ok\(0\)`：matched=`true`，第 541 行
- finding：—

### `STARRY_CLOSE_RANGE_VALIDATION`

- 类型：`static`
- 关联 syscall：`close_range`
- 通用规则：`LTP_31D9D767D6888DDA`、`LTP_CBF4B6C8A1458A28`、`LTP_F1DC44813DCA6A05`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_close_range\([\s\S]*?if (?:first < 0 \\|\\| )?last < first \{[\s\S]*?return Err\(AxError::InvalidInput\);`：matched=`true`，第 541 行
  - `pub fn sys_close_range\([\s\S]*?CloseRangeFlags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?`：matched=`true`，第 541 行
- finding：—

### `STARRY_CLOSE_SYSCALL`

- 类型：`static`
- 关联 syscall：`close`
- 通用规则：`LTP_09B39E9C9254ECB2`、`MAN_494CD34A8C11734B`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_close\(fd: c_int\)[\s\S]*?close_file_like\(fd\)\?;`：matched=`true`，第 527 行
  - `pub fn sys_close\(fd: c_int\)[\s\S]*?close_file_like\(fd\)\?;[\s\S]*?Ok\(0\)`：matched=`true`，第 527 行
- finding：—

### `STARRY_CONNECT_ADDRESS_VALIDATION`

- 类型：`static`
- 关联 syscall：`connect`
- 通用规则：`MAN_392816F25BD330A2`、`MAN_524B615D8F9A7E12`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `fn read_family\([\s\S]*?size_of::<__kernel_sa_family_t>\(\) > addrlen as usize[\s\S]*?Err\(AxError::InvalidInput\)[\s\S]*?addr\.cast::<__kernel_sa_family_t>\(\)\.get_as_ref\(\)\?`：matched=`true`，第 83 行
  - `impl SocketAddrExt for SocketAddrEx[\s\S]*?fn read_from_user\([\s\S]*?_ => Err\(AxError::from\(LinuxError::EAFNOSUPPORT\)\)`：matched=`true`，第 320 行
  - `impl SocketAddrExt for SocketAddrV4[\s\S]*?if addrlen < size_of::<sockaddr_in>\(\) as socklen_t \{[\s\S]*?Err\(AxError::InvalidInput\)`：matched=`true`，第 152 行
- finding：—

### `STARRY_CONNECT_ENTRY`

- 类型：`static`
- 关联 syscall：`connect`
- 通用规则：`MAN_CDD044CBEEED1A80`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_connect\([\s\S]*?Socket::from_fd\(fd\)\?;[\s\S]*?SocketAddrEx::read_from_user\(addr, addrlen\)\?;`：matched=`true`，第 173 行
  - `pub fn sys_connect\([\s\S]*?socket\.connect\(addr\)\.map_err\([\s\S]*?AxError::WouldBlock[\s\S]*?AxError::InProgress[\s\S]*?\?;[\s\S]*?Ok\(0\)`：matched=`true`，第 173 行
- finding：—

### `STARRY_COPY_FILE_RANGE_CORE`

- 类型：`static`
- 关联 syscall：`copy_file_range`
- 通用规则：`MAN_BC425C37C792DDEE`、`MAN_D405972253EA086F`、`MAN_DBD043A36C2E4926`、`MAN_FDD174E970AC7930`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_copy_file_range\([\s\S]*?if flags != 0 \{[\s\S]*?Err\(AxError::InvalidInput\)`：matched=`true`，第 773 行
  - `pub fn sys_copy_file_range\([\s\S]*?let remap = \\|e\\| match e \{[\s\S]*?AxError::BadFileDescriptor \\| AxError::IsADirectory => e,[\s\S]*?_ => AxError::InvalidInput[\s\S]*?File::from_fd\(fd_in\)\.map_err\(remap\)\?;[\s\S]*?File::from_fd\(fd_out\)\.map_err\(remap\)\?;`：matched=`true`，第 773 行
  - `meta_in\.node_type == NodeType::Directory \\|\\| meta_out\.node_type == NodeType::Directory[\s\S]*?Err\(AxError::IsADirectory\)[\s\S]*?meta_in\.node_type != NodeType::RegularFile \\|\\| meta_out\.node_type != NodeType::RegularFile[\s\S]*?Err\(AxError::InvalidInput\)`：matched=`true`，第 810 行
  - `file_out\.inner\(\)\.access\(FileFlags::APPEND\)\.is_ok\(\)[\s\S]*?Err\(AxError::BadFileDescriptor\)`：matched=`true`，第 818 行
  - `meta_in\.device == meta_out\.device && meta_in\.inode == meta_out\.inode[\s\S]*?if in_end >= pos_out && pos_in <= out_end \{[\s\S]*?Err\(AxError::InvalidInput\)`：matched=`true`，第 834 行
- finding：—

### `STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO`

- 类型：`static`
- 关联 syscall：—
- 通用规则：`LTP_74BB3F96CBA52D02`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_copy_file_range\([\s\S]*?if len > isize::MAX as usize \{[\s\S]*?return Err\(AxError::from\(LinuxError::EOVERFLOW\)\);`：matched=`true`，第 773 行
- finding：—

### `STARRY_DUP2_DUP3_BEHAVIOR`

- 类型：`static`
- 关联 syscall：`dup2`、`dup3`
- 通用规则：`LTP_098AFE0E8E10B0EF`、`LTP_1726C16756E9651C`、`LTP_37C625BD7D7C5F1D`、`LTP_3A7B17AF231D4158`、`LTP_4F02ACC6E2F6B094`、`LTP_75D52C5E9C93B6D7`、`LTP_9B3646398697EA64`、`LTP_9F560A103CB6F910`、`LTP_B7F51635806E7E59`、`LTP_BDA36F61423EEB3E`、`LTP_D296A517F138A0C0`、`LTP_EE8E695CF61D6D8A`、`MAN_794294DBD03CA974`、`MAN_9BC94E6BD25C05E1`、`MAN_E99D067CF243EEE8`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_dup2\(old_fd: c_int, new_fd: c_int\)[\s\S]*?if old_fd == new_fd \{[\s\S]*?get_file_like\(new_fd\)\?;[\s\S]*?return Ok\(new_fd as _\);[\s\S]*?sys_dup3\(old_fd, new_fd, 0\)`：matched=`true`，第 618 行
  - `pub fn sys_dup3\([\s\S]*?Dup3Flags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?;[\s\S]*?if old_fd == new_fd \{[\s\S]*?Err\(AxError::InvalidInput\)`：matched=`true`，第 633 行
  - `pub fn sys_dup3\([\s\S]*?\.get\(old_fd as _\)[\s\S]*?\.ok_or\(AxError::BadFileDescriptor\)\?;[\s\S]*?fd_table\.remove\(new_fd as _\)[\s\S]*?\.add_at\(new_fd as _, f\)[\s\S]*?Ok\(new_fd as _\)`：matched=`true`，第 633 行
- finding：—

### `STARRY_DUP_BEHAVIOR`

- 类型：`static`
- 关联 syscall：`dup`
- 通用规则：`LTP_511185D6DE2A63A0`、`LTP_84DBE108A850E845`、`LTP_A774FC10727E8ED2`、`LTP_ED2BA909DF79625A`、`MAN_794294DBD03CA974--794294dbd03c`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `fn dup_fd\(old_fd: c_int, cloexec: bool\)[\s\S]*?get_file_like\(old_fd\)\?;[\s\S]*?add_file_like\(f, cloexec\)\?;[\s\S]*?Ok\(new_fd as _\)`：matched=`true`，第 586 行
  - `pub fn sys_dup\(old_fd: c_int\)[\s\S]*?dup_fd\(old_fd, false\)`：matched=`true`，第 612 行
- finding：—

### `STARRY_EPOLL_CREATE1_FLAGS`

- 类型：`static`
- 关联 syscall：`epoll_create1`
- 通用规则：`LTP_5D8D2B3BEDA79604`、`MAN_6B7EED8E43FDD1BA`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_epoll_create1\(flags: u32\)[\s\S]*?EpollCreateFlags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?`：matched=`true`，第 104 行
  - `pub fn sys_epoll_create1\(flags: u32\)[\s\S]*?Epoll::new\(\)[\s\S]*?\.add_to_fd_table\(flags\.contains\(EpollCreateFlags::CLOEXEC\)\)`：matched=`true`，第 104 行
- finding：—

### `STARRY_EPOLL_CTL_ENTRY`

- 类型：`static`
- 关联 syscall：`epoll_ctl`
- 通用规则：`LTP_6FFB17DB762F3167`、`LTP_83709E56D6285F71`、`MAN_DADCFA23F461FBBF`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_epoll_ctl\([\s\S]*?let epoll = Epoll::from_fd\(epfd\)\?;`：matched=`true`，第 121 行
  - `pub fn sys_epoll_ctl\([\s\S]*?if epfd == fd \{[\s\S]*?return Err\(AxError::InvalidInput\);`：matched=`true`，第 121 行
  - `match op \{[\s\S]*?EPOLL_CTL_ADD =>[\s\S]*?EPOLL_CTL_MOD =>[\s\S]*?EPOLL_CTL_DEL =>[\s\S]*?_ => return Err\(AxError::InvalidInput\)`：matched=`true`，第 149 行
- finding：—

### `STARRY_EPOLL_CTL_INTEREST`

- 类型：`static`
- 关联 syscall：`epoll_ctl`
- 通用规则：`LTP_4953FAD330ADE150`
- 结果：`fail`
- 原因：one or more required patterns did not match
- pattern 证据：

  - `fn new\(fd: i32\)[\s\S]*?let file = get_file_like\(fd\)\?;`：matched=`true`，第 135 行
  - `pub fn add\([\s\S]*?guard\.contains_key\(&key\)[\s\S]*?return Err\(AxError::AlreadyExists\);`：matched=`false`，未匹配
  - `pub fn modify\([\s\S]*?guard\.get_mut\(&key\)\.ok_or\(AxError::NotFound\)\?`：matched=`true`，第 599 行
  - `pub fn delete\([\s\S]*?\.remove\(&key\)[\s\S]*?\.ok_or\(AxError::NotFound\)\?`：matched=`false`，未匹配
- finding：`finding-epoll-ctl-ltp-4953fad330ade150-07800f218f34`

### `STARRY_EPOLL_FACCESS_ERRNO`

- 类型：`static`
- 关联 syscall：`epoll_create1`、`epoll_ctl`、`execveat`、`faccessat2`
- 通用规则：`LTP_4953FAD330ADE150`、`LTP_4C1F446C9C520B36`、`LTP_5D8D2B3BEDA79604`、`LTP_6FFB17DB762F3167`、`LTP_83709E56D6285F71`、`LTP_ACF7A30AF3B10973`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `InvalidInput \\| InvalidData => EINVAL`：matched=`true`，第 235 行
  - `BadFileDescriptor => EBADF`：matched=`true`，第 224 行
  - `BadAddress \\| BadState => EFAULT`：matched=`true`，第 223 行
  - `NotFound => ENOENT`：matched=`true`，第 249 行
  - `NotADirectory => ENOTDIR`：matched=`true`，第 243 行
  - `AlreadyExists => EEXIST`：matched=`true`，第 221 行
  - `FilesystemLoop => ELOOP`：matched=`true`，第 230 行
- finding：—

### `STARRY_EPOLL_FD_LOOKUP`

- 类型：`static`
- 关联 syscall：`epoll_ctl`
- 通用规则：`LTP_6FFB17DB762F3167`、`MAN_E32B6349055FCEF9`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn get_file_like\(fd: c_int\)[\s\S]*?\.ok_or\(AxError::BadFileDescriptor\)`：matched=`true`，第 304 行
  - `fn from_fd\(fd: c_int\)[\s\S]*?get_file_like\(fd\)\?[\s\S]*?\.downcast_arc\(\)[\s\S]*?\.map_err\(\\|_\\| AxError::InvalidInput\)`：matched=`true`，第 266 行
- finding：—

### `STARRY_EPOLL_NESTED_LOOP`

- 类型：`static`
- 关联 syscall：`epoll_ctl`
- 通用规则：`MAN_CDD195853C6DFE14`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `prepare_nested_link\([\s\S]*?scan_epoll_topology\(target,[\s\S]*?Some\(source\)\)\?[\s\S]*?downstream\.reached_target[\s\S]*?AxError::FilesystemLoop`：matched=`true`，第 48 行
  - `upstream\.max_depth \+ 1 \+ downstream\.max_depth > MAX_NESTED_EPOLL_EDGES[\s\S]*?AxError::FilesystemLoop`：matched=`true`，第 61 行
- finding：—

### `STARRY_ERRNO_TRANSLATION`

- 类型：`static`
- 关联 syscall：`close`、`mmap`
- 通用规则：`LTP_09B39E9C9254ECB2`、`LTP_51E295101A9F4411`、`LTP_791DEA825D66980B`、`LTP_FEACDC300C3E1DD7`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `BadFileDescriptor => EBADF`：matched=`true`，第 224 行
  - `InvalidInput \\| InvalidData => EINVAL`：matched=`true`，第 235 行
  - `PermissionDenied => EACCES`：matched=`true`，第 253 行
- finding：—

### `STARRY_EXECVEAT_FACCESSAT_RESOLVE`

- 类型：`static`
- 关联 syscall：`execveat`、`faccessat2`
- 通用规则：`LTP_4C1F446C9C520B36`、`LTP_ACF7A30AF3B10973`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `Some\(""\) \\| None =>[\s\S]*?flags & AT_EMPTY_PATH == 0[\s\S]*?get_file_like\(dirfd\)\?`：matched=`true`，第 62 行
  - `Some\(path\) =>[\s\S]*?if path\.starts_with\('/'\) \{[\s\S]*?AT_FDCWD[\s\S]*?with_fs\(dirfd,`：matched=`true`，第 80 行
  - `impl FileLike for Directory[\s\S]*?fn from_fd\(fd: c_int\)[\s\S]*?get_file_like\(fd\)\?[\s\S]*?AxError::NotADirectory`：matched=`true`，第 313 行
- finding：—

### `STARRY_EXECVEAT_VALIDATION`

- 类型：`static`
- 关联 syscall：`execveat`
- 通用规则：`LTP_ACF7A30AF3B10973`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_execveat\([\s\S]*?if flags & !\(AT_EMPTY_PATH \\| AT_SYMLINK_NOFOLLOW\) != 0 \{[\s\S]*?Err\(AxError::InvalidInput\)`：matched=`true`，第 45 行
  - `pub fn sys_execveat\([\s\S]*?vm_load_string\(path\)\?;[\s\S]*?resolve_at\(dirfd, Some\(path\.as_str\(\)\), flags\)\?`：matched=`true`，第 45 行
- finding：—

### `STARRY_FACCESSAT2_VALIDATION`

- 类型：`static`
- 关联 syscall：`faccessat2`
- 通用规则：`MAN_147EECDC5DAB119D`、`MAN_A58EA189B1C9E326`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `const FACCESSAT2_VALID_FLAGS:[\s\S]*?const FACCESSAT2_VALID_MODE:[\s\S]*?mode & !FACCESSAT2_VALID_MODE != 0 \\|\\| flags & !FACCESSAT2_VALID_FLAGS != 0[\s\S]*?Err\(AxError::InvalidInput\)`：matched=`true`，第 150 行
  - `pub fn sys_faccessat2\([\s\S]*?path\.nullable\(\)\.map\(vm_load_path_string\)\.transpose\(\)\?;[\s\S]*?resolve_at\(dirfd, path\.as_deref\(\), flags\)\?`：matched=`true`，第 146 行
- finding：—

### `STARRY_FCHDIR_CORE`

- 类型：`static`
- 关联 syscall：`fchdir`
- 通用规则：`LTP_17B7A9460939622A`、`LTP_CCC36F43E9463D3E`、`MAN_5B2667DFDCB4EB31`、`MAN_E116073D3FDB5C1F`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_fchdir\(dirfd: i32\)[\s\S]*?with_fs\(dirfd,[\s\S]*?current_dir\(\)\.clone\(\)`：matched=`true`，第 99 行
  - `pub fn sys_fchdir\(dirfd: i32\)[\s\S]*?set_current_dir\(entry\)\?;`：matched=`true`，第 99 行
  - `pub fn sys_fchdir\(dirfd: i32\)[\s\S]*?set_current_dir\(entry\)\?;[\s\S]*?Ok\(0\)`：matched=`true`，第 99 行
- finding：—

### `STARRY_FCHDIR_ERRNO_TRANSLATION`

- 类型：`static`
- 关联 syscall：`fchdir`
- 通用规则：`LTP_CCC36F43E9463D3E`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `BadFileDescriptor\s*=>\s*EBADF`：matched=`true`，第 224 行
- finding：—

### `STARRY_FCHDIR_FD_VALIDATION`

- 类型：`static`
- 关联 syscall：`fchdir`
- 通用规则：`LTP_CCC36F43E9463D3E`、`MAN_5B2667DFDCB4EB31`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn with_fs<[\s\S]*?if dirfd == AT_FDCWD[\s\S]*?Directory::from_fd\(dirfd\)\?`：matched=`true`，第 28 行
  - `impl FileLike for Directory[\s\S]*?fn from_fd\(fd: c_int\)[\s\S]*?get_file_like\(fd\)\?`：matched=`true`，第 313 行
- finding：—

### `STARRY_FCHMODAT_FLAG_VALIDATION`

- 类型：`static`
- 关联 syscall：`fchmodat`
- 通用规则：`MAN_9A17C8A141B47D41`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `const FCHMODAT_VALID_FLAGS: u32 = AT_EMPTY_PATH \\| AT_SYMLINK_NOFOLLOW;`：matched=`true`，第 620 行
  - `if flags & !FCHMODAT_VALID_FLAGS != 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}`：matched=`true`，第 621 行
- finding：—

### `STARRY_FD_TABLE_LOOKUP_ALLOCATION`

- 类型：`static`
- 关联 syscall：`dup`
- 通用规则：`LTP_511185D6DE2A63A0`、`LTP_84DBE108A850E845`、`LTP_A774FC10727E8ED2`、`LTP_ED2BA909DF79625A`
- 结果：`fail`
- 原因：one or more required patterns did not match
- pattern 证据：

  - `pub fn get_file_like\(fd: c_int\)[\s\S]*?FD_TABLE[\s\S]*?\.get\(fd as usize\)[\s\S]*?\.ok_or\(AxError::BadFileDescriptor\)`：matched=`false`，未匹配
  - `pub fn add_file_like\([\s\S]*?RLIMIT_NOFILE[\s\S]*?if table\.count\(\) as u64 >= max_nofile \{[\s\S]*?Err\(AxError::TooManyOpenFiles\)`：matched=`true`，第 325 行
  - `pub fn add_file_like\([\s\S]*?Ok\(table\.add\(fd\)\.map_err\(\\|_\\| AxError::TooManyOpenFiles\)\? as c_int\)`：matched=`true`，第 325 行
- finding：`finding-dup-ltp-511185d6de2a63a0-07800f218f34`、`finding-dup-ltp-84dbe108a850e845-07800f218f34`、`finding-dup-ltp-a774fc10727e8ed2-07800f218f34`、`finding-dup-ltp-ed2ba909df79625a-07800f218f34`

### `STARRY_FINAL_ERRNO_TRANSLATION`

- 类型：`static`
- 关联 syscall：`timer_delete`、`tkill`、`waitid`
- 通用规则：`LTP_10B3572DBFA6742B`、`LTP_9FD87A3F7688FEF1`、`LTP_FCC236A4D5926B81`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `BadAddress \\| BadState => EFAULT`：matched=`true`，第 223 行
  - `BadFileDescriptor => EBADF`：matched=`true`，第 224 行
  - `InvalidInput \\| InvalidData => EINVAL`：matched=`true`，第 235 行
  - `OperationNotPermitted => EPERM`：matched=`true`，第 250 行
- finding：—

### `STARRY_FINAL_SYSINFO_COPYOUT`

- 类型：`static`
- 关联 syscall：`sysinfo`
- 通用规则：`LTP_A367723236ADA8B4`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_sysinfo\([\s\S]*?kinfo\.uptime[\s\S]*?kinfo\.totalram[\s\S]*?kinfo\.freeram[\s\S]*?kinfo\.procs[\s\S]*?info\.vm_write\(kinfo\)\?;\s*Ok\(0\)`：matched=`true`，第 719 行
- finding：—

### `STARRY_FINAL_SYSLOG_READ_ARGUMENTS`

- 类型：`static`
- 关联 syscall：—
- 通用规则：`LTP_6B9F97B897EC5C32`、`LTP_C8376BC347F94A98`
- 结果：`fail`
- 原因：one or more required patterns did not match
- pattern 证据：

  - `SYSLOG_ACTION_READ => \{\s*validate_syslog_read_args\(buf, len\)\?;`：matched=`false`，未匹配
  - `SYSLOG_ACTION_READ_ALL => \{\s*validate_syslog_read_args\(buf, len\)\?;`：matched=`false`，未匹配
- finding：—

### `STARRY_FINAL_TIMER_DELETE`

- 类型：`static`
- 关联 syscall：`timer_delete`
- 通用规则：`LTP_10B3572DBFA6742B`、`LTP_9B36D27A4A2994D0`、`MAN_95930C2D369C878D`、`MAN_AF1D093225F75E82`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_timer_delete\([\s\S]*?posix_timers\.delete\(timerid\) \{\s*Ok\(0\)\s*\} else \{\s*Err\(AxError::InvalidInput\)`：matched=`true`，第 268 行
- finding：—

### `STARRY_FINAL_TKILL_TID_VALIDATION`

- 类型：`static`
- 关联 syscall：`tkill`
- 通用规则：`LTP_FCC236A4D5926B81`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_tkill\([\s\S]*?if tid <= 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}`：matched=`true`，第 214 行
- finding：—

### `STARRY_FINAL_UMOUNT_PRIVILEGE`

- 类型：`static`
- 关联 syscall：—
- 通用规则：`LTP_287CF10D893735AB`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_umount2\([\s\S]*?has_cap_sys_admin\(\)[\s\S]*?return Err\(AxError::OperationNotPermitted\);`：matched=`true`，第 302 行
- finding：—

### `STARRY_FINAL_UNAME_COPYOUT`

- 类型：`static`
- 关联 syscall：`uname`
- 通用规则：`LTP_5516B8A938B9C3A5`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_uname\([\s\S]*?build_utsname\(&ns\)[\s\S]*?name\.vm_write\(uts\)\?;\s*Ok\(0\)`：matched=`true`，第 661 行
- finding：—

### `STARRY_FINAL_UNSHARE_FILES`

- 类型：`static`
- 关联 syscall：`unshare`
- 通用规则：`LTP_40A45C5E82D7F4A1`
- 结果：`fail`
- 原因：one or more required patterns did not match
- pattern 证据：

  - `const SUPPORTED_NS_FLAGS: u32 =[\s\S]*?CLONE_FILES`：matched=`true`，第 24 行
  - `if flags & CLONE_FILES != 0 \{[\s\S]*?FD_TABLE\.read\(\)\.clone\(\)[\s\S]*?FD_TABLE\.scope_mut\(scope\)`：matched=`false`，未匹配
- finding：`finding-unshare-ltp-40a45c5e82d7f4a1-07800f218f34`

### `STARRY_FINAL_UNSHARE_FLAG_VALIDATION`

- 类型：`static`
- 关联 syscall：`unshare`
- 通用规则：`MAN_B4DD5B60F33FC5E3`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_unshare\([\s\S]*?flags & !SUPPORTED_NS_FLAGS != 0[\s\S]*?return Err\(AxError::InvalidInput\);`：matched=`true`，第 109 行
- finding：—

### `STARRY_FINAL_UNSHARE_NEWNS_PRIVILEGE`

- 类型：`static`
- 关联 syscall：—
- 通用规则：`LTP_82A8802A27A3D2BF`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `flags & CLONE_NEWNS != 0[\s\S]*?![\s\S]*?has_cap_sys_admin\(\)[\s\S]*?return Err\(AxError::OperationNotPermitted\);`：matched=`true`，第 64 行
- finding：—

### `STARRY_FINAL_WAITID_OPTIONS`

- 类型：`static`
- 关联 syscall：`waitid`
- 通用规则：`LTP_9FD87A3F7688FEF1`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `if !options[\s\S]*?intersects\(WaitIdOptions::WEXITED \\| WaitIdOptions::WUNTRACED \\| WaitIdOptions::WCONTINUED\)[\s\S]*?return Err\(AxError::InvalidInput\);`：matched=`true`，第 385 行
- finding：—

### `STARRY_FINAL_WAITPID_INT_MIN`

- 类型：`static`
- 关联 syscall：`wait4`、`waitpid`
- 通用规则：`LTP_03AF14160F8B59A0`、`LTP_1691F6F9712C5546`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_waitpid\([\s\S]*?if pid == i32::MIN \{\s*return Err\(AxError::from\(LinuxError::ESRCH\)\);\s*\}`：matched=`true`，第 234 行
- finding：—

### `STARRY_FINIT_MODULE_FLAG_VALIDATION`

- 类型：`static`
- 关联 syscall：`finit_module`
- 通用规则：`MAN_2421026C912D8F9E--2421026c912d`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_finit_module\(module_fd: i32, param_ptr: \*const u8, flags: u32\)`：matched=`true`，第 52 行
  - `pub fn sys_finit_module\([\s\S]*?if flags != 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}`：matched=`true`，第 52 行
- finding：—

### `STARRY_MAN_CLOCK_GETRES_VALIDATION`

- 类型：`static`
- 关联 syscall：`clock_getres`
- 通用规则：`MAN_6D665164162723C5--6d6651641627`、`MAN_DA93975DA79D34AD--da93975da79d`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_clock_getres[\s\S]*?_ => return Err\(AxError::InvalidInput\)`：matched=`true`，第 62 行
  - `pub fn sys_clock_getres[\s\S]*?res\.nullable\(\)[\s\S]*?res\.vm_write\(timespec::from_time_value\(resolution\)\)\?`：matched=`true`，第 62 行
- finding：—

### `STARRY_MAN_CLOCK_GETTIME_VALIDATION`

- 类型：`static`
- 关联 syscall：`clock_gettime`
- 通用规则：`MAN_A67DCE77030808A6`、`MAN_D84D77F1C6E463F4`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_clock_gettime[\s\S]*?_ => \{[\s\S]*?return Err\(AxError::InvalidInput\)`：matched=`true`，第 18 行
  - `pub fn sys_clock_gettime[\s\S]*?ts\.vm_write\(timespec::from_time_value\(now\)\)\?`：matched=`true`，第 18 行
- finding：—

### `STARRY_MAN_EVENTFD2_VALIDATION`

- 类型：`static`
- 关联 syscall：`eventfd2`
- 通用规则：`MAN_A5F4BA2371332A4E`、`MAN_BE929AB9651E5E66`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_eventfd2[\s\S]*?EventFdFlags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?`：matched=`true`，第 26 行
  - `pub fn sys_eventfd2[\s\S]*?add_file_like\(event_fd[\s\S]*?\.map\(\\|fd\\| fd as _\)\?[\s\S]*?Ok\(fd\)`：matched=`true`，第 26 行
- finding：—

### `STARRY_MAN_GETRANDOM_ARGUMENTS`

- 类型：`static`
- 关联 syscall：`getrandom`
- 通用规则：`MAN_39C5F1849EB3A736`、`MAN_CEC45E0E1446E3DF`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_getrandom[\s\S]*?GetRandomFlags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?[\s\S]*?INSECURE[\s\S]*?RANDOM[\s\S]*?AxError::InvalidInput`：matched=`true`，第 850 行
  - `pub fn sys_getrandom[\s\S]*?vm_write_slice\(buf, &kbuf\)\?`：matched=`true`，第 850 行
- finding：—

### `STARRY_MAN_INOTIFY_ADD_WATCH_INPUTS`

- 类型：`static`
- 关联 syscall：`inotify_add_watch`
- 通用规则：`MAN_1EFA395D2832F95E`、`MAN_EFBA9CA2760DA6B8`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_inotify_add_watch[\s\S]*?vm_load_path_string\(path\)\?`：matched=`true`，第 25 行
  - `pub fn sys_inotify_add_watch[\s\S]*?get_file_like\(fd\)\?[\s\S]*?downcast_arc::<Inotify>\(\)`：matched=`true`，第 25 行
- finding：—

### `STARRY_MAN_INOTIFY_INIT1_VALIDATION`

- 类型：`static`
- 关联 syscall：`inotify_init1`
- 通用规则：`MAN_330C0628475E2900`、`MAN_C467D6702AB64674`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_inotify_init1[\s\S]*?valid_flags = IN_CLOEXEC \\| IN_NONBLOCK[\s\S]*?flags & !valid_flags != 0[\s\S]*?AxError::InvalidInput`：matched=`true`，第 12 行
  - `pub fn sys_inotify_init1[\s\S]*?add_file_like\(inotify as _, flags & IN_CLOEXEC != 0\)\.map\(\\|fd\\| fd as _\)`：matched=`true`，第 12 行
- finding：—

### `STARRY_MAN_INOTIFY_RM_WATCH_ID`

- 类型：`static`
- 关联 syscall：`inotify_rm_watch`
- 通用规则：`MAN_EA69373DAD6B5B01`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn rm_watch[\s\S]*?watches\.remove\(&wd\)\.is_none\(\)[\s\S]*?AxError::InvalidInput`：matched=`true`，第 90 行
- finding：—

### `STARRY_MAN_INOTIFY_RM_WATCH_INPUTS`

- 类型：`static`
- 关联 syscall：`inotify_rm_watch`
- 通用规则：`MAN_C04F44BFF720877B`、`MAN_EA69373DAD6B5B01`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_inotify_rm_watch[\s\S]*?get_file_like\(fd\)\?[\s\S]*?downcast_arc::<Inotify>\(\)[\s\S]*?AxError::InvalidInput`：matched=`true`，第 40 行
  - `pub fn sys_inotify_rm_watch[\s\S]*?inotify\.rm_watch\(wd\)\.map\(\\|\(\)\\| 0\)`：matched=`true`，第 40 行
- finding：—

### `STARRY_MAN_LISTEN_ENTRY`

- 类型：`static`
- 关联 syscall：`listen`
- 通用规则：`MAN_6038BC183A1CE6BF`、`MAN_7C3C0347FD37CEB9`、`MAN_AE7C62637F29A4C9`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_listen[\s\S]*?Socket::from_fd\(fd\)\?\.listen\(backlog as usize\)\?`：matched=`true`，第 192 行
  - `pub fn sys_listen[\s\S]*?Ok\(0\)`：matched=`true`，第 192 行
- finding：—

### `STARRY_MAN_MEMFD_CREATE_VALIDATION`

- 类型：`static`
- 关联 syscall：`memfd_create`
- 通用规则：`MAN_4C50AA2793AB7713`、`MAN_67ECA3FB50D80BAF`、`MAN_6FA8F2D41D1B7062`、`MAN_9E0C30E4205FB415`、`MAN_DD8A18DB0BF6E8A9`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_memfd_create[\s\S]*?flags & !valid_flags != 0 \\|\\| flags & MFD_HUGETLB != 0[\s\S]*?AxError::InvalidInput`：matched=`true`，第 45 行
  - `let name_str: String = vm_load_string\(name\)\?`：matched=`true`，第 55 行
  - `const MEMFD_NAME_MAX: usize = 249;[\s\S]*?name_str\.len\(\) > MEMFD_NAME_MAX[\s\S]*?AxError::InvalidInput`：matched=`true`，第 43 行
  - `pub fn sys_memfd_create[\s\S]*?add_file_like\(memfd, cloexec\)\.map\(\\|fd\\| fd as _\)`：matched=`true`，第 45 行
- finding：—

### `STARRY_MAN_PIPE2_VALIDATION`

- 类型：`static`
- 关联 syscall：`pipe2`
- 通用规则：`MAN_1115E878B4F50CF3`、`MAN_DD6D48EB9B80CB6B`、`MAN_EDB775C51FCEA404`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_pipe2[\s\S]*?PipeFlags::from_bits\(flags\)[\s\S]*?AxError::InvalidInput`：matched=`true`，第 21 行
  - `if let Err\(err\) = fds\.vm_write\(\[read_fd, write_fd\]\)[\s\S]*?close_file_like\(read_fd\)[\s\S]*?close_file_like\(write_fd\)[\s\S]*?return Err\(err\.into\(\)\)`：matched=`true`，第 38 行
  - `pub fn sys_pipe2[\s\S]*?Ok\(0\)`：matched=`true`，第 21 行
- finding：—

### `STARRY_MAN_REBOOT_VALIDATION`

- 类型：`static`
- 关联 syscall：`reboot`
- 通用规则：`MAN_03E8B237E962C1D2`、`MAN_F84F01B63ABC178D`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_reboot[\s\S]*?has_cap_sys_boot\(\)[\s\S]*?LinuxError::EPERM`：matched=`true`，第 128 行
  - `magic != LINUX_REBOOT_MAGIC1[\s\S]*?LINUX_REBOOT_MAGIC2C[\s\S]*?LinuxError::EINVAL`：matched=`true`，第 133 行
  - `match cmd \{[\s\S]*?_ => Err\(AxError::from\(LinuxError::EINVAL\)\)`：matched=`true`，第 145 行
- finding：—

### `STARRY_MAN_SECCOMP_OPERATION_FLAGS`

- 类型：`static`
- 关联 syscall：`seccomp`
- 通用规则：`MAN_B9EE0F176B92F526`
- 结果：`fail`
- 原因：one or more required patterns did not match
- pattern 证据：

  - `SECCOMP_SET_MODE_STRICT => \{[\s\S]*?if flags != 0[\s\S]*?AxError::InvalidInput`：matched=`true`，第 939 行
  - `SECCOMP_GET_ACTION_AVAIL => \{[\s\S]*?if flags != 0[\s\S]*?AxError::InvalidInput`：matched=`false`，未匹配
- finding：`finding-seccomp-man-b9ee0f176b92f526-07800f218f34`

### `STARRY_MAN_SECCOMP_VALIDATION`

- 类型：`static`
- 关联 syscall：`seccomp`
- 通用规则：`MAN_02D976F1ED01493F`、`MAN_20A10178D28B400B`、`MAN_73E054548B324267`、`MAN_8609DB2EE85AF88E`、`MAN_BE74B0D21973DAEC`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `fn check_seccomp_install_permission[\s\S]*?no_new_privs\(\)[\s\S]*?has_cap_sys_admin\(\)[\s\S]*?AxError::OperationNotPermitted`：matched=`true`，第 876 行
  - `fn read_seccomp_filter[\s\S]*?args\.is_null\(\)[\s\S]*?AxError::BadAddress[\s\S]*?prog\.len == 0 \\|\\| prog\.filter\.is_null\(\)[\s\S]*?AxError::InvalidInput`：matched=`true`，第 886 行
  - `fn seccomp_action_available[\s\S]*?_ => Err\(AxError::OperationNotSupported\)`：matched=`true`，第 902 行
  - `pub fn sys_seccomp[\s\S]*?flags & !SECCOMP_ALLOWED_FLAGS != 0[\s\S]*?match op[\s\S]*?_ => return Err\(AxError::InvalidInput\)[\s\S]*?Ok\(0\)`：matched=`true`，第 933 行
- finding：—

### `STARRY_MAN_SETDOMAINNAME_ARGUMENTS`

- 类型：`static`
- 关联 syscall：`setdomainname`
- 通用规则：`MAN_027D17C587997F75`、`MAN_083368964C7623C0`、`MAN_968D07C7039689E5`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_setdomainname[\s\S]*?if len > 64[\s\S]*?AxError::InvalidInput`：matched=`true`，第 695 行
  - `pub fn sys_setdomainname[\s\S]*?vm_read_slice\(name\.cast::<u8>\(\), &mut buf\)\?`：matched=`true`，第 695 行
  - `pub fn sys_setdomainname[\s\S]*?domainname = domainname;[\s\S]*?Ok\(0\)`：matched=`true`，第 695 行
- finding：—

### `STARRY_MAN_SETGROUPS_VALIDATION`

- 类型：`static`
- 关联 syscall：`setgroups`
- 通用规则：`MAN_0F2C1ABA8AF5C15E`、`MAN_8D160F5D77EC235B`、`MAN_FD5BF4CD3984BECF`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_setgroups[\s\S]*?!old\.has_cap_setgid\(\)[\s\S]*?AxError::OperationNotPermitted`：matched=`true`，第 627 行
  - `thread\.setgroups_deny\(\)[\s\S]*?AxError::OperationNotPermitted`：matched=`true`，第 637 行
  - `const NGROUPS_MAX: usize = 65536;[\s\S]*?if size > NGROUPS_MAX[\s\S]*?AxError::InvalidInput`：matched=`true`，第 625 行
- finding：—

### `STARRY_MAN_SETHOSTNAME_ARGUMENTS`

- 类型：`static`
- 关联 syscall：`sethostname`
- 通用规则：`MAN_6998D4E70F807B13`、`MAN_9E12AA9A59F1BBE9`、`MAN_DA06B43ED3D9DBBC`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_sethostname[\s\S]*?if len > 64[\s\S]*?AxError::InvalidInput`：matched=`true`，第 675 行
  - `pub fn sys_sethostname[\s\S]*?vm_read_slice\(name\.cast::<u8>\(\), &mut buf\)\?`：matched=`true`，第 675 行
  - `pub fn sys_sethostname[\s\S]*?nodename = nodename;[\s\S]*?Ok\(0\)`：matched=`true`，第 675 行
- finding：—

### `STARRY_MAN_SHUTDOWN_VALIDATION`

- 类型：`static`
- 关联 syscall：`shutdown`
- 通用规则：`MAN_5B4118BF4C21F770`、`MAN_5F5865EF1A8D5904`、`MAN_8812ADE8E360DB8F`、`MAN_CAA0FFEFF7C64A82`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_shutdown[\s\S]*?Socket::from_fd\(fd\)\?`：matched=`true`，第 239 行
  - `let how = match how \{[\s\S]*?SHUT_RD[\s\S]*?SHUT_WR[\s\S]*?SHUT_RDWR[\s\S]*?_ => return Err\(AxError::InvalidInput\)`：matched=`true`，第 243 行
  - `socket\.shutdown\(how\)\.map\(\\|_\\| 0\)`：matched=`true`，第 249 行
- finding：—

### `STARRY_MAN_SOCKETPAIR_VALIDATION`

- 类型：`static`
- 关联 syscall：`socketpair`
- 通用规则：`MAN_43BBCE48C452BDDD`、`MAN_9452D425539B8023`、`MAN_B121E5340A1BEFEE`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_socketpair[\s\S]*?if domain != AF_UNIX[\s\S]*?LinuxError::EAFNOSUPPORT`：matched=`true`，第 252 行
  - `pub fn sys_socketpair[\s\S]*?\*fds\.get_as_mut\(\)\? = \[`：matched=`true`，第 252 行
  - `pub fn sys_socketpair[\s\S]*?Ok\(0\)`：matched=`true`，第 252 行
- finding：—

### `STARRY_MMAP_ACCESS`

- 类型：`static`
- 关联 syscall：`mmap`
- 通用规则：`MAN_18C5488E8D09D6D2--18c5488e8d09`
- 结果：`fail`
- 原因：one or more required patterns did not match
- pattern 证据：

  - `file_mmap\(\)\.map_err\(\\|_\\| AxError::PermissionDenied\)\?`：matched=`false`，未匹配
  - `if needs_file_mmap_checks[\s\S]*?!flags\.contains\(FileFlags::READ\)[\s\S]*?AxError::PermissionDenied`：matched=`true`，第 246 行
  - `MmapFlags::SHARED[\s\S]*?MmapProt::WRITE[\s\S]*?!flags\.contains\(FileFlags::WRITE\)[\s\S]*?AxError::PermissionDenied`：matched=`true`，第 150 行
- finding：`finding-mmap-man-18c5488e8d09d6d2-18c5488e8d09-07800f218f34`

### `STARRY_MMAP_ARGUMENTS`

- 类型：`static`
- 关联 syscall：`mmap`
- 通用规则：`LTP_51E295101A9F4411`、`LTP_FEACDC300C3E1DD7`、`MAN_8DB0AB4E3B90CB50--8db0ab4e3b90`、`MAN_DE03A6A5B1731AF7--de03a6a5b173`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_mmap\([\s\S]*?if length == 0 \{[\s\S]*?return Err\(AxError::InvalidInput\);`：matched=`true`，第 128 行
  - `let map_type = match flags & MmapFlags::TYPE\.bits\(\)[\s\S]*?_ => return Err\(AxError::InvalidInput\)`：matched=`true`，第 160 行
- finding：—

### `STARRY_MMAP_FD`

- 类型：`static`
- 关联 syscall：`mmap`
- 通用规则：`LTP_791DEA825D66980B`、`MAN_35AF4698AC57ED3F--35af4698ac57`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `if !anonymous && fd < 0 \{[\s\S]*?return Err\(AxError::BadFileDescriptor\);`：matched=`true`，第 170 行
  - `let file = if anonymous \{[\s\S]*?None[\s\S]*?\} else \{[\s\S]*?Some\(get_file_like\(fd\)\?\)`：matched=`true`，第 203 行
- finding：—

### `STARRY_ROUND2_CLOSE_FD_TABLE`

- 类型：`static`
- 关联 syscall：`close`
- 通用规则：`LTP_2BDE60C0E64B4DC8`、`LTP_BF2428964ADD116F`、`LTP_E520E500AB3AE851`
- 结果：`fail`
- 原因：one or more required patterns did not match
- pattern 证据：

  - `pub fn close_file_like\(fd: c_int\)[\s\S]*?FD_TABLE\.write\(\)\.remove\(fd as usize\)[\s\S]*?if let Some\(f\) = removed[\s\S]*?return Ok\(\(\)\);`：matched=`false`，未匹配
  - `pub fn close_file_like\(fd: c_int\)[\s\S]*?Err\(AxError::BadFileDescriptor\)`：matched=`true`，第 337 行
- finding：`finding-close-ltp-2bde60c0e64b4dc8-07800f218f34`、`finding-close-ltp-bf2428964add116f-07800f218f34`、`finding-close-ltp-e520e500ab3ae851-07800f218f34`

### `STARRY_ROUND2_CLOSE_SYSCALL`

- 类型：`static`
- 关联 syscall：`close`
- 通用规则：`LTP_2BDE60C0E64B4DC8`、`LTP_BF2428964ADD116F`、`LTP_E520E500AB3AE851`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_close\(fd: c_int\)[\s\S]*?close_file_like\(fd\)\?;[\s\S]*?Ok\(0\)`：matched=`true`，第 527 行
- finding：—

### `STARRY_ROUND2_ERRNO_TRANSLATION`

- 类型：`static`
- 关联 syscall：`close_range`、`dup2`、`dup3`
- 通用规则：`LTP_098AFE0E8E10B0EF`、`LTP_31D9D767D6888DDA`、`LTP_37C625BD7D7C5F1D`、`LTP_4F02ACC6E2F6B094`、`LTP_75D52C5E9C93B6D7`、`LTP_9B3646398697EA64`、`LTP_9F560A103CB6F910`、`LTP_BDA36F61423EEB3E`、`LTP_CBF4B6C8A1458A28`、`LTP_D296A517F138A0C0`、`LTP_F1DC44813DCA6A05`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `InvalidInput \\| InvalidData => EINVAL`：matched=`true`，第 235 行
  - `BadFileDescriptor => EBADF`：matched=`true`，第 224 行
  - `TooManyOpenFiles => EMFILE`：matched=`true`，第 258 行
  - `BadAddress \\| BadState => EFAULT`：matched=`true`，第 223 行
  - `NotASocket => ENOTSOCK`：matched=`true`，第 244 行
  - `IsADirectory => EISDIR`：matched=`true`，第 237 行
- finding：—

### `STARRY_ROUND3_ERRNO_TRANSLATION`

- 类型：`static`
- 关联 syscall：`getcwd`、`getpgid`、`getpriority`、`getsid`
- 通用规则：`LTP_53E3454ED6EFD842`、`LTP_729222947741DFD6`、`LTP_88D300A8FB407324`、`LTP_8C1C2578972FCA1D`、`LTP_9461AA782926BAB4`、`LTP_F8FD511858BB650D`、`LTP_FC1E41C3414E7F21`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `BadAddress \\| BadState => EFAULT`：matched=`true`，第 223 行
  - `BadFileDescriptor => EBADF`：matched=`true`，第 224 行
  - `InvalidInput \\| InvalidData => EINVAL`：matched=`true`，第 235 行
  - `NoSuchProcess => ESRCH`：matched=`true`，第 242 行
  - `OperationNotPermitted => EPERM`：matched=`true`，第 250 行
  - `OutOfRange => ERANGE`：matched=`true`，第 252 行
- finding：—

### `STARRY_ROUND3_FSTATFS_ERRORS`

- 类型：`static`
- 关联 syscall：`fstatfs`
- 通用规则：`MAN_48B52042FE3DEA4C--48b52042fe3d`、`MAN_5378890AE3F832EE--5378890ae3f8`、`MAN_8153E21BD727F6A0`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_fstatfs\(fd: i32, buf: \*mut statfs\)[\s\S]*?File::from_fd\(fd\)\?`：matched=`true`，第 244 行
  - `buf\.vm_write\(statfs\([\s\S]*?\)\?\)\?;`：matched=`true`，第 234 行
- finding：—

### `STARRY_ROUND3_FSTAT_CORE`

- 类型：`static`
- 关联 syscall：`fstat`
- 通用规则：`MAN_37A8B25C745F91BB--37a8b25c745f`、`MAN_AA8C115068BD5D76--aa8c115068bd`、`MAN_DFDB86CEA63B78D3--dfdb86cea63b`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_fstat\(fd: i32, statbuf: \*mut stat\)[\s\S]*?sys_fstatat\(fd, core::ptr::null\(\), statbuf, AT_EMPTY_PATH\)`：matched=`true`，第 43 行
  - `pub fn sys_fstatat\([\s\S]*?let loc = resolve_at\(dirfd, path\.as_deref\(\), flags\)\?;`：matched=`true`，第 57 行
  - `statbuf\.vm_write\(loc\.stat\(\)\?\.into\(\)\)\?;`：matched=`true`，第 75 行
- finding：—

### `STARRY_ROUND3_GETCWD`

- 类型：`static`
- 关联 syscall：`getcwd`
- 通用规则：`LTP_53E3454ED6EFD842`、`LTP_729222947741DFD6`、`LTP_FC1E41C3414E7F21`、`MAN_0D9E79AEB44B7510`、`MAN_45A2B6F5ADF14C3F`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_getcwd\([\s\S]*?let size: usize = size\.try_into\(\)\.map_err\(\\|_\\| AxError::BadAddress\)\?;`：matched=`true`，第 431 行
  - `let cwd = cwd\.as_bytes_with_nul\(\);`：matched=`true`，第 441 行
  - `if cwd\.len\(\) <= size \{[\s\S]*?vm_write_slice\(buf, cwd\)\?;[\s\S]*?\} else \{\s*Err\(AxError::OutOfRange\)`：matched=`true`，第 443 行
- finding：—

### `STARRY_ROUND3_GETPRIORITY_SELECTOR`

- 类型：`static`
- 关联 syscall：`getpriority`
- 通用规则：`LTP_88D300A8FB407324`、`MAN_B1A8365C419E3164--b1a8365c419e`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_getpriority\([\s\S]*?match which \{[\s\S]*?_ => Err\(AxError::InvalidInput\),\s*\}`：matched=`true`，第 237 行
- finding：—

### `STARRY_ROUND3_GETRLIMIT_CORE`

- 类型：`static`
- 关联 syscall：`getrlimit`
- 通用规则：`LTP_2554AC2E46FC6A15`、`LTP_26555A26680524AD`、`LTP_3741A721C9C463D0`、`LTP_3B1458E6E26CBB53`、`LTP_652CE911B47794E0`、`LTP_7DFAC48A8971CFE3`、`LTP_8988E5015778894A`、`LTP_914935DA5C379DA1`、`LTP_91ED7E85761CE00F`、`LTP_9305FA6D8B835652`、`LTP_A0547B601C515355`、`LTP_B058D6B9CBBB459D`、`LTP_BD5C209F4C6EE910`、`LTP_E6C69C9F4AB565BC`、`LTP_EA953D5E5C4B2B1F`、`LTP_FADBA4ADECCFBA4E`、`LTP_FB0ABF26A21EAE3C`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `if resource >= RLIM_NLIMITS \{\s*return Err\(AxError::InvalidInput\);\s*\}`：matched=`true`，第 23 行
  - `let limit = &proc_data\.rlim\.read\(\)\[resource\];`：matched=`true`，第 28 行
  - `old_limit\.vm_write\(rlimit64 \{\s*rlim_cur: limit\.current,\s*rlim_max: limit\.max,\s*\}\)\?;`：matched=`true`，第 29 行
- finding：—

### `STARRY_ROUND3_GETRLIMIT_DISPATCH`

- 类型：`static`
- 关联 syscall：`getrlimit`
- 通用规则：`LTP_2554AC2E46FC6A15`、`LTP_26555A26680524AD`、`LTP_3741A721C9C463D0`、`LTP_3B1458E6E26CBB53`、`LTP_652CE911B47794E0`、`LTP_7DFAC48A8971CFE3`、`LTP_8988E5015778894A`、`LTP_914935DA5C379DA1`、`LTP_91ED7E85761CE00F`、`LTP_9305FA6D8B835652`、`LTP_A0547B601C515355`、`LTP_B058D6B9CBBB459D`、`LTP_BD5C209F4C6EE910`、`LTP_E6C69C9F4AB565BC`、`LTP_EA953D5E5C4B2B1F`、`LTP_FADBA4ADECCFBA4E`、`LTP_FB0ABF26A21EAE3C`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `Sysno::getrlimit => sys_prlimit64\(0, uctx\.arg0\(\) as _, core::ptr::null\(\), uctx\.arg1\(\) as _\)`：matched=`true`，第 650 行
- finding：—

### `STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE`

- 类型：`static`
- 关联 syscall：—
- 通用规则：`LTP_6C14DE68E3C0CC24`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_gettimeofday\(ts: \*mut timeval, tz: \*mut Timezone\)`：matched=`true`，第 43 行
  - `tz\.nullable\(\)[\s\S]*?tz\.vm_write\(Timezone::default\(\)\)\?;`：matched=`true`，第 47 行
- finding：—

### `STARRY_ROUND3_INIT_MODULE_PERMISSION`

- 类型：`static`
- 关联 syscall：—
- 通用规则：`LTP_D246498B20D9CB2C`
- 结果：`fail`
- 原因：one or more required patterns did not match
- pattern 证据：

  - `pub fn sys_init_module\([\s\S]*?if !current\(\)\.as_thread\(\)\.cred\(\)\.has_cap_sys_module\(\)`：matched=`false`，未匹配
  - `pub fn sys_init_module\([\s\S]*?has_cap_sys_module\(\)[\s\S]*?return Err\(AxError::OperationNotPermitted\);[\s\S]*?VmBytes::new`：matched=`false`，未匹配
- finding：—

### `STARRY_ROUND3_JOB_ID_LOOKUP`

- 类型：`static`
- 关联 syscall：`getpgid`、`getsid`
- 通用规则：`LTP_8C1C2578972FCA1D`、`LTP_9461AA782926BAB4`、`LTP_F8FD511858BB650D`、`MAN_045719AC8992819E--045719ac8992`、`MAN_81F4F1C3AD4F3217`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_getsid\(pid: Pid\)[\s\S]*?get_process\(pid\)\?\.group\(\)\.session\(\)\.sid\(\)`：matched=`true`，第 10 行
  - `pub fn sys_getpgid\(pid: Pid\)[\s\S]*?get_process\(pid\)\?\.group\(\)\.pgid\(\)`：matched=`true`，第 30 行
- finding：—

### `STARRY_ROUND3_PROCESS_LOOKUP`

- 类型：`static`
- 关联 syscall：`getpgid`、`getsid`
- 通用规则：`LTP_8C1C2578972FCA1D`、`LTP_9461AA782926BAB4`、`LTP_F8FD511858BB650D`、`MAN_045719AC8992819E--045719ac8992`、`MAN_81F4F1C3AD4F3217`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn get_process\(pid: Pid\)[\s\S]*?if pid == 0 \{\s*return Ok\(current\(\)\.as_thread\(\)\.proc_data\.proc\.clone\(\)\);`：matched=`true`，第 255 行
  - `get_zombie_process\(pid\)\.ok_or\(AxError::NoSuchProcess\)`：matched=`true`，第 262 行
- finding：—

### `STARRY_ROUND4_ERRNO_TRANSLATION`

- 类型：`static`
- 关联 syscall：`msync`、`munmap`、`openat2`、`pidfd_open`、`pidfd_send_signal`、`preadv2`、`read`
- 通用规则：`LTP_0087F445CEB63414`、`LTP_026CB4A1CA7CDC6B`、`LTP_08F05BA6ED1CEE6A`、`LTP_1AACAC53BAF23BA9`、`LTP_1BB76939FF2A40B5`、`LTP_26AE3C69D80D35F8`、`LTP_3743BC827FB4F981`、`LTP_D0800876342DE939`、`LTP_D2E2A5F40B2313E5`、`LTP_EA90C626D9AA6C08`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `BadAddress \\| BadState => EFAULT`：matched=`true`，第 223 行
  - `BadFileDescriptor => EBADF`：matched=`true`，第 224 行
  - `InvalidInput \\| InvalidData => EINVAL`：matched=`true`，第 235 行
  - `NoMemory => ENOMEM`：matched=`true`，第 239 行
  - `OperationNotSupported => EOPNOTSUPP`：matched=`true`，第 251 行
- finding：—

### `STARRY_ROUND4_MLOCK2_FLAGS`

- 类型：`static`
- 关联 syscall：`mlock2`
- 通用规则：`MAN_362BD9184BA2B5C7`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_mlock2\([\s\S]*?if flags & !MLOCK_ONFAULT != 0 \{\s*return Err\(AxError::InvalidInput\);`：matched=`true`，第 1081 行
- finding：—

### `STARRY_ROUND4_MSYNC_EXCLUSIVE_MODES`

- 类型：`static`
- 关联 syscall：`msync`
- 通用规则：`LTP_D2E2A5F40B2313E5`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `if flags & MS_SYNC != 0 && flags & MS_ASYNC != 0 \{\s*return Err\(AxError::InvalidInput\);`：matched=`true`，第 1035 行
- finding：—

### `STARRY_ROUND4_MSYNC_UNKNOWN_FLAGS`

- 类型：`static`
- 关联 syscall：`msync`
- 通用规则：`LTP_EA90C626D9AA6C08`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `let valid_flags = MS_SYNC \\| MS_ASYNC \\| MS_INVALIDATE;\s*if flags & !valid_flags != 0 \{\s*return Err\(AxError::InvalidInput\);`：matched=`true`，第 1031 行
- finding：—

### `STARRY_ROUND4_MUNMAP_ZERO_LENGTH`

- 类型：`static`
- 关联 syscall：`munmap`
- 通用规则：`LTP_26AE3C69D80D35F8`、`MAN_8DB0AB4E3B90CB50`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_munmap\([\s\S]*?if length == 0 \{\s*return Err\(AxError::InvalidInput\);`：matched=`true`，第 592 行
- finding：—

### `STARRY_ROUND4_OPENAT2_SIZE`

- 类型：`static`
- 关联 syscall：`openat2`
- 通用规则：`LTP_026CB4A1CA7CDC6B`、`LTP_D0800876342DE939`、`MAN_25CD94348F7360E1`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_openat2\([\s\S]*?let base_size = size_of::<OpenHow>\(\);\s*if size < base_size \{\s*return Err\(AxError::InvalidInput\);`：matched=`true`，第 428 行
- finding：—

### `STARRY_ROUND4_PIDFD_GETFD_FLAGS`

- 类型：`static`
- 关联 syscall：`pidfd_getfd`
- 通用规则：`MAN_58936D050A8879DE`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_pidfd_getfd\([\s\S]*?if flags != 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}[\s\S]*?PidFd::from_fd`：matched=`true`，第 86 行
- finding：—

### `STARRY_ROUND4_PIDFD_OPEN_INPUTS`

- 类型：`static`
- 关联 syscall：`pidfd_open`
- 通用规则：`LTP_1BB76939FF2A40B5`、`LTP_3743BC827FB4F981`、`MAN_0BA66331CB4B2091`、`MAN_DC37B979EC91203E`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `let flags = PidFdFlags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?;`：matched=`true`，第 61 行
  - `if \(pid as i32\) <= 0 \{\s*return Err\(AxError::InvalidInput\);`：matched=`true`，第 64 行
- finding：—

### `STARRY_ROUND4_PIDFD_SIGNAL_FLAGS`

- 类型：`static`
- 关联 syscall：`pidfd_send_signal`
- 通用规则：`LTP_08F05BA6ED1CEE6A`、`MAN_6D77B363EA967C8F`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_pidfd_send_signal\([\s\S]*?PidFdSignalFlags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?;`：matched=`true`，第 123 行
- finding：—

### `STARRY_ROUND4_READ_BAD_FD`

- 类型：`static`
- 关联 syscall：`read`
- 通用规则：`LTP_0087F445CEB63414`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_read\([\s\S]*?get_file_like\(fd\)\?\.read`：matched=`true`，第 123 行
- finding：—

### `STARRY_ROUND4_VECTOR_IO_FLAGS`

- 类型：`static`
- 关联 syscall：`preadv2`、`pwritev2`
- 通用规则：`LTP_1AACAC53BAF23BA9`、`MAN_B5E18528035F6F87`、`MAN_F12635B7646C0E9B`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `fn validate_rwf_flags\(flags: u32\)[\s\S]*?if flags != 0 \{\s*return Err\(AxError::OperationNotSupported\);`：matched=`true`，第 505 行
  - `pub fn sys_preadv2\([\s\S]*?validate_rwf_flags\(flags\)\?;[\s\S]*?pub fn sys_pwritev2\([\s\S]*?validate_rwf_flags\(flags\)\?;`：matched=`true`，第 512 行
- finding：—

### `STARRY_ROUND5_ERRNO_TRANSLATION`

- 类型：`static`
- 关联 syscall：`sched_setaffinity`、`sendfile`、`setpgid`、`setpriority`、`socket`
- 通用规则：`LTP_39B1E5C574F2D3DC`、`LTP_4308D71D8BD6519D`、`LTP_44DC5382746D773D`、`LTP_585CC852338F38EE`、`LTP_7BC885B5878C95B6`、`LTP_971DB17D32C51561`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `BadAddress \\| BadState => EFAULT`：matched=`true`，第 223 行
  - `BadFileDescriptor => EBADF`：matched=`true`，第 224 行
  - `InvalidInput \\| InvalidData => EINVAL`：matched=`true`，第 235 行
- finding：—

### `STARRY_ROUND5_SCHED_SETAFFINITY_EMPTY_MASK`

- 类型：`static`
- 关联 syscall：`sched_setaffinity`
- 通用规则：`LTP_585CC852338F38EE`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_sched_setaffinity\([\s\S]*?if cpu_mask\.is_empty\(\) \{\s*return Err\(AxError::InvalidInput\);`：matched=`true`，第 141 行
- finding：—

### `STARRY_ROUND5_SCHED_YIELD`

- 类型：`static`
- 关联 syscall：`sched_yield`
- 通用规则：`LTP_A9BC7EBC1784A722`、`MAN_254F60FBFDA7A2BB`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_sched_yield\(\) -> AxResult<isize> \{\s*ax_task::yield_now\(\);\s*Ok\(0\)\s*\}`：matched=`true`，第 30 行
- finding：—

### `STARRY_ROUND5_SENDFILE_IN_FD`

- 类型：`static`
- 关联 syscall：`sendfile`
- 通用规则：`LTP_39B1E5C574F2D3DC`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_sendfile\([\s\S]*?let _in_file = File::from_fd\(in_fd\)\?;`：matched=`true`，第 741 行
- finding：—

### `STARRY_ROUND5_SENDFILE_OUT_FD`

- 类型：`static`
- 关联 syscall：`sendfile`
- 通用规则：`LTP_7BC885B5878C95B6`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_sendfile\([\s\S]*?let out_file = get_file_like\(out_fd\)\?;`：matched=`true`，第 741 行
- finding：—

### `STARRY_ROUND5_SENDMSG_MESSAGE_POINTER`

- 类型：`static`
- 关联 syscall：`sendmsg`
- 通用规则：`MAN_AE68C41A115C80FC--ae68c41a115c`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_sendmsg[\s\S]*?msg\.get_as_ref\(\)\?`：matched=`true`，第 137 行
  - `fn parse_send_cmsgs[\s\S]*?UserConstPtr::<cmsghdr>::from\(ptr\)\.get_as_ref\(\)\?`：matched=`true`，第 41 行
  - `pub fn sys_sendmsg[\s\S]*?IoVectorBuf::new\(msg\.msg_iov as \*const IoVec, msg\.msg_iovlen\)\?`：matched=`true`，第 137 行
  - `fn send_impl[\s\S]*?SocketAddrEx::read_from_user\(addr, addrlen\)\?`：matched=`true`，第 73 行
- finding：—

### `STARRY_ROUND5_SETPGID_NEGATIVE`

- 类型：`static`
- 关联 syscall：`setpgid`
- 通用规则：`LTP_4308D71D8BD6519D`、`MAN_44D6BD8077F837B5`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_setpgid\(pid: i32, pgid: i32\) -> AxResult<isize>`：matched=`true`，第 40 行
  - `pub fn sys_setpgid\([\s\S]*?if pid < 0 \\|\\| pgid < 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}`：matched=`true`，第 40 行
- finding：—

### `STARRY_ROUND5_SETPRIORITY_SELECTOR`

- 类型：`static`
- 关联 syscall：`setpriority`
- 通用规则：`LTP_44DC5382746D773D`、`MAN_B1A8365C419E3164`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_setpriority\([\s\S]*?match which \{[\s\S]*?_ => Err\(AxError::InvalidInput\),\s*\}`：matched=`true`，第 270 行
- finding：—

### `STARRY_ROUND5_SOCKET_INVALID_TYPE`

- 类型：`static`
- 关联 syscall：`socket`
- 通用规则：`LTP_971DB17D32C51561`
- 结果：`fail`
- 原因：one or more required patterns did not match
- pattern 证据：

  - `pub fn sys_socket\([\s\S]*?\(AF_INET \\| AF_INET6, _\) \\| \(AF_UNIX, _\) \\| \(AF_NETLINK, _\) \\| \(AF_VSOCK, _\) => \{[\s\S]*?return Err\(AxError::InvalidInput\);[\s\S]*?\n\}\n\npub fn sys_bind`：matched=`false`，未匹配
- finding：`finding-socket-ltp-971db17d32c51561-07800f218f34`

### `STARRY_ROUND5_SOCKET_PROTOCOL_ERRORS`

- 类型：`static`
- 关联 syscall：`socket`
- 通用规则：`LTP_6B29B31CE99466E6`、`LTP_A4A662687B98D33F`、`LTP_AF8D38878ED1A9DA`、`LTP_DD2E1A555B603C7B`、`LTP_E316C28E36E136DA`、`MAN_732160952277CD16`、`MAN_A1CD98CE32C423E4`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `\(AF_INET \\| AF_INET6, SOCK_STREAM\) => \{[\s\S]*?proto != 0 && proto != IPPROTO_TCP as _[\s\S]*?LinuxError::EPROTONOSUPPORT`：matched=`true`，第 62 行
  - `\(AF_INET \\| AF_INET6, SOCK_DGRAM\) => \{[\s\S]*?proto != 0 && proto != IPPROTO_UDP as _[\s\S]*?LinuxError::EPROTONOSUPPORT`：matched=`true`，第 68 行
  - `\(AF_INET, SOCK_RAW\) => \{[\s\S]*?proto != IPPROTO_ICMP as u32[\s\S]*?LinuxError::EPROTONOSUPPORT`：matched=`true`，第 93 行
  - `_ => \{\s*return Err\(AxError::from\(LinuxError::EAFNOSUPPORT\)\);\s*\}`：matched=`true`，第 106 行
- finding：—

### `STARRY_SOCKET_FD_VALIDATION`

- 类型：`static`
- 关联 syscall：`connect`、`listen`、`shutdown`
- 通用规则：`MAN_5B4118BF4C21F770`、`MAN_5F5865EF1A8D5904`、`MAN_6038BC183A1CE6BF`、`MAN_AE7C62637F29A4C9`、`MAN_CDD044CBEEED1A80`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `fn from_fd\(fd: c_int\)[\s\S]*?get_file_like\(fd\)\?[\s\S]*?\.downcast_arc\(\)[\s\S]*?\.map_err\(\\|_\\| AxError::NotASocket\)`：matched=`true`，第 391 行
- finding：—

## 动态测试

### `STARRY_FINAL_FS_RUNTIME`

- 类型：`dynamic`
- 关联 syscall：—
- 通用规则：`LTP_04236FD5B061DEB9`、`LTP_21FCBFC328D1815A`、`LTP_38432B154B641410`、`LTP_43728156B00FF104`、`LTP_58C8C307B1FF2510`、`LTP_6F4B3A38B8BF4C7E`、`LTP_6F77CAA9FC4423BA`、`LTP_71DD72481EF5740E`、`LTP_86144BF50FB25D3A`、`LTP_B0433B78A1641F24`、`LTP_D254EE40E8B5957E`、`LTP_DCC88B2C458969EA`、`LTP_DDA854712C50CD6A`
- 结果：`not_run`
- 原因：test patch was not applied
- finding：—

### `STARRY_FINAL_WAIT_RUNTIME`

- 类型：`dynamic`
- 关联 syscall：`wait`、`wait4`、`waitid`、`waitpid`
- 通用规则：`LTP_2F3E34FD672DBF34`、`LTP_4494B70BBA693D42`、`LTP_614C018F61C078A0`、`LTP_7B0F966046AECA7E`、`LTP_9C2FB7732A0B90B6`、`LTP_A2934B80997B62C9`、`LTP_AD3A4B98FF201ABE`、`LTP_C13C4F63D58904BC`、`LTP_C24E55F06625D564`、`LTP_D1A18560E485E146`、`LTP_DA64FD04E43656E6`、`LTP_DF5B725563FDFB31`、`LTP_ECD986F27CF15E1E`、`LTP_FC8BA85373EA2D8F`
- 结果：`not_run`
- 原因：test patch was not applied
- finding：—

## Blockers（非实现缺口）

- `test_injection` `STARRY_FINAL_FS_RUNTIME`、`STARRY_FINAL_WAIT_RUNTIME`：git apply failed for dynamic test patch
- `test_injection` `STARRY_FINAL_FS_RUNTIME`：test patch was not applied
- `test_injection` `STARRY_FINAL_WAIT_RUNTIME`：test patch was not applied

<details>
<summary>机器可读元数据</summary>

<!-- syscallguard-metadata -->
```yaml
schema_version: 1
kind: syscallguard_check_report
report_id: check-20260723t030225z-60f534a3
status: completed_with_blockers
generated_at_utc: '2026-07-23T03:02:33.663221Z'
mapping_report_id: mapping-static-man-20260723-current-pre-fix
mapping_report_version:
  id: mapping-static-man-20260723-current-pre-fix
  generated_at_utc: '2026-07-23T03:01:49.216844Z'
  content_hash: sha256:3affd8d691bca2964488178a2639f682170acd6a1fa2d37697641c6e6da0695c
target:
  target_id: starry
  repository: /home/cloud/gitLinux/tgoskits
  repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
  branch: dev-syscalls-compliance-2
  descriptor_hash: sha256:6b982bb80e3a0a3cf408d7c696367996422e3dac8376577222e56ee47f111d24
  snapshot_hash: sha256:07800f218f3431ae837e9c825fa3b384a0c18d0c8d83dd8ff01c728add06c9e7
input_hash: sha256:9c054f4e85fdb1fc51d9a056231ab9825a8ed596b57eb9759c6f31e90c3ea4b3
entity_hashes:
  rules:
    LTP_0087F445CEB63414: sha256:0087f445ceb63414b632c05b271af9fee6f2b3c7167fbc43e208a7b0a485ca33
    LTP_026CB4A1CA7CDC6B: sha256:026cb4a1ca7cdc6bf1b2e94352fa72c86bda5fc328c6ed9ae8983b4696a2c0f8
    LTP_03AF14160F8B59A0: sha256:03af14160f8b59a0b546095a476facf6e3504937dd6f387971839bd21441739b
    LTP_08F05BA6ED1CEE6A: sha256:08f05ba6ed1cee6adc06e52236156d77d5c6dd5d4592642bd443aa47f5e425b7
    LTP_098AFE0E8E10B0EF: sha256:098afe0e8e10b0efa6872ee3d2ece3674b519943b59189a2758d8ab31b06ab26
    LTP_09B39E9C9254ECB2: sha256:09b39e9c9254ecb24ccb5288c3f12281e9adc0b698de5c706a4f071599c3ce60
    LTP_10B3572DBFA6742B: sha256:10b3572dbfa6742b44e40e6ffb78f797d484d1c0f37cedc5e4bc5c0099e8b498
    LTP_1691F6F9712C5546: sha256:1691f6f9712c5546d1b81c76cc385ed8b961683e209c8d54e9543a02a199aac5
    LTP_1726C16756E9651C: sha256:1726c16756e9651c8be282bf1cdf5c30a283e32aa200934084e3c42a2aee9ff9
    LTP_17B7A9460939622A: sha256:17b7a9460939622a41226aa0c0191c618d2a9b74c6e2321e127b1ba067b85bff
    LTP_1AACAC53BAF23BA9: sha256:1aacac53baf23ba9aec716bf031354593948226151154448887698bf2a5dde0d
    LTP_1BB76939FF2A40B5: sha256:1bb76939ff2a40b56089c39f1e2e8db30af944a15e86e47a4e98a572bd8319ea
    LTP_2554AC2E46FC6A15: sha256:2554ac2e46fc6a15932bc27db324eb7b2b1265b2270c61b345af14c0b79e241d
    LTP_26555A26680524AD: sha256:26555a26680524ad18ca9e9f1082b5f71c9edbd627be17b015751aadffc79033
    LTP_26AE3C69D80D35F8: sha256:26ae3c69d80d35f8cde32c3371db6ddce43877024723415f2c15a30f19a02756
    LTP_2BDE60C0E64B4DC8: sha256:2bde60c0e64b4dc8fc4b1e23c70973364d891d517c1f8020f709fabec59e6d0f
    LTP_31D9D767D6888DDA: sha256:31d9d767d6888ddaf3c03f24abe0bc874e9932a546e4cdd283ecad199e6bcc1a
    LTP_3741A721C9C463D0: sha256:3741a721c9c463d0d65d94387111a493a2a48a2a5f1975fc7d455144d3321154
    LTP_3743BC827FB4F981: sha256:3743bc827fb4f9819137ea970af9f8219bfff5989b4fa99ce035c18fa3ca4937
    LTP_37C625BD7D7C5F1D: sha256:37c625bd7d7c5f1db42b7cacc49b4964844f0c2f977ad1a74c3960da0d662932
    LTP_39B1E5C574F2D3DC: sha256:39b1e5c574f2d3dc16cd61efcb95f2cb9bffc5d5a5f86c1e52b9fac3ef82d569
    LTP_3A7B17AF231D4158: sha256:3a7b17af231d4158b2c4508e92a25435b89a569164e6dfdabc216b48e1afec9f
    LTP_3B1458E6E26CBB53: sha256:3b1458e6e26cbb5398ae5221e8cb8d70b475e8e7fa008f9752270403cd9e3e38
    LTP_40A45C5E82D7F4A1: sha256:40a45c5e82d7f4a1748fc7b7d74b4700d4498c801e0fdbad387797d941bb7a7b
    LTP_425E5A3502541DE8: sha256:425e5a3502541de863d8b8e88eafb95db2f8d8e1f9cb88a32d8b3124950395b2
    LTP_4308D71D8BD6519D: sha256:4308d71d8bd6519d6d2c15cb0c6d1925eed73874700fd6f1c1cc8a86199632a4
    LTP_44DC5382746D773D: sha256:44dc5382746d773d253ddf7ccb3ede2e242b978ebfb3e0756367ceb4d839956d
    LTP_4953FAD330ADE150: sha256:4953fad330ade1503bf7a6d4d6bf2c353a337844f58042ceb3214149d1025945
    LTP_4C1F446C9C520B36: sha256:4c1f446c9c520b36b7f3b5a39c42fea74e7befa2adf95e4a919a1bb760184320
    LTP_4F02ACC6E2F6B094: sha256:4f02acc6e2f6b094f06413684c004106e4c18d8f654cbb8b231de56e60aba90c
    LTP_511185D6DE2A63A0: sha256:511185d6de2a63a045d2f5f65babdf4c25b4066ece863b9f121419045563d4c9
    LTP_51E295101A9F4411: sha256:51e295101a9f4411b8c43521d430e85bd27ac1d7a96127b66675d7dc024ba9d2
    LTP_53E3454ED6EFD842: sha256:53e3454ed6efd842d4456341bdaf29e25ad49ab8f5a55c170a4e23c3355fe2f9
    LTP_5516B8A938B9C3A5: sha256:5516b8a938b9c3a56502a0790304ef99d9caee848e7faaafcdf2f016f6443230
    LTP_585CC852338F38EE: sha256:585cc852338f38eedc86755b62d33a8eb443200486dd86bb3f79a4a4df80981c
    LTP_5D8D2B3BEDA79604: sha256:5d8d2b3beda79604301b79695ead77bb1cca6ec4c1e6b679aabacb702befdccf
    LTP_652CE911B47794E0: sha256:652ce911b47794e00cd84120507ce0a4b8fe539ae38dff3f3c047d91cab6d2e1
    LTP_6B29B31CE99466E6: sha256:6b29b31ce99466e6682913919c0fad006475b094d59fadcc43c1ec6f4e9d1630
    LTP_6FFB17DB762F3167: sha256:6ffb17db762f3167790a052bae0fa49f44b1075991c29dcec06f56509e9ae743
    LTP_729222947741DFD6: sha256:729222947741dfd63a81e9c93572baf5c789acbffca84a2edd5dce13fe1fb2a3
    LTP_75D52C5E9C93B6D7: sha256:75d52c5e9c93b6d7989e3392a132ca3a319f4419c2f678533dc80d000c4891cd
    LTP_76BFF56F735A0074: sha256:76bff56f735a0074d725ee7dab337c42b7daf23d2ca44135affba4b983676aa8
    LTP_791DEA825D66980B: sha256:791dea825d66980bfded73936e4745cf7b914f20652b9489e65a7a59509b897b
    LTP_7BC885B5878C95B6: sha256:7bc885b5878c95b621d9876c970257da2de585ab5e9771c1542ceed3b28f8ad0
    LTP_7DFAC48A8971CFE3: sha256:7dfac48a8971cfe3c53af5bdc67246aedc28a76f25fe9bb7d59bb5481e0d4295
    LTP_83709E56D6285F71: sha256:83709e56d6285f71dce5dcd5f54aa0ba99d44ddef002f1e6cc53f2fce6075678
    LTP_84DBE108A850E845: sha256:84dbe108a850e845bf4a3cfc65c984525f06a85bcf44e616283b5ef4e16bb451
    LTP_88D300A8FB407324: sha256:88d300a8fb407324aefbe09d1b569b46d87628a1639509250755357a2c634c1a
    LTP_8988E5015778894A: sha256:8988e5015778894a14a0b54cc6fe1a0f1f2917fb41a0c6dfd0152069d07c8d56
    LTP_8C1C2578972FCA1D: sha256:8c1c2578972fca1d655df720a137f88882824f681ac3cbfa59052c4a1f8ef64a
    LTP_914935DA5C379DA1: sha256:914935da5c379da10358ba568cfe5b8c7a31f6c57db6f6446451375aa973c46a
    LTP_91ED7E85761CE00F: sha256:91ed7e85761ce00fb0a63c61b421b825e76cf8577e07d172597be6451388fa31
    LTP_9305FA6D8B835652: sha256:9305fa6d8b8356529faec8a8a060de73350f98dc7a1db1af07a5e45a6f6e11ae
    LTP_9461AA782926BAB4: sha256:9461aa782926bab4cb006db18510ae154420b8c023b3b2f9cc0308d205ca9cf7
    LTP_971DB17D32C51561: sha256:971db17d32c515614f0af38045463319bd4bfb3a661a4ae9e4486c0404c75ead
    LTP_9B3646398697EA64: sha256:9b3646398697ea6481b4201006e677123cd226bb81910f45b6fa558aaa810832
    LTP_9B36D27A4A2994D0: sha256:9b36d27a4a2994d0fb9becad9ddba6985ba56fddf7db2169f2efef4819243591
    LTP_9F560A103CB6F910: sha256:9f560a103cb6f910cc2b8fb141c7de076accd6a913e920715328e9facdfb18db
    LTP_9FD87A3F7688FEF1: sha256:9fd87a3f7688fef10bea92050ac0661fedef311659e6ffce7573ff015c42b21d
    LTP_A0547B601C515355: sha256:a0547b601c51535524cdadea7c3abcbc2fcd16157591cc2322cd1def6a08cc56
    LTP_A367723236ADA8B4: sha256:a367723236ada8b46a0d6d3a444b7812e36d2f96cc8654bcd32ce5076bb39ed0
    LTP_A4A662687B98D33F: sha256:a4a662687b98d33f933b37774536af580d8b9e44d1bc317c426dd2c4a68a7a1e
    LTP_A774FC10727E8ED2: sha256:a774fc10727e8ed282a01bc787e12bd54a0d81a756fc45037304c5906dadb2ff
    LTP_A9BC7EBC1784A722: sha256:a9bc7ebc1784a72263646142685fb7ed3bb7aec45b58cfc208bd762f44d7c8fe
    LTP_ACF7A30AF3B10973: sha256:acf7a30af3b10973088f22334a5e2b35a00bbc3ff6530b1fb644856f637f06e4
    LTP_AF8D38878ED1A9DA: sha256:af8d38878ed1a9da8bcca89799d36f633a0776307b92fe435d004f9b6cb1b444
    LTP_B058D6B9CBBB459D: sha256:b058d6b9cbbb459d2d0e155285c19e2e49762cc25177b335dab254142809eb74
    LTP_B7F51635806E7E59: sha256:b7f51635806e7e596b7f6a1baf152d74ca1d365a9bdfc6d3f34984ac1908632d
    LTP_BD5C209F4C6EE910: sha256:bd5c209f4c6ee910a13539baa6f55f3f3d2654a60e583b67fa26724405421ad3
    LTP_BDA36F61423EEB3E: sha256:bda36f61423eeb3e616d764edd458663817800e2f3db3adfae687bd17f6c2764
    LTP_BF2428964ADD116F: sha256:bf2428964add116f793723626820cf1b363a819d6e38ba6d31d9832e4ab1b2c0
    LTP_CBF4B6C8A1458A28: sha256:cbf4b6c8a1458a2885c6c847b47ca93098a06580fc5fdfc3a1e483b9dab01ac4
    LTP_CCC36F43E9463D3E: sha256:ccc36f43e9463d3e65e732efa9e9d62af421e5d01bac07a5d343fc88f368505c
    LTP_D0800876342DE939: sha256:d0800876342de9392e43300d2797ff5244107ca4127ddb02ed0ec08832b03e82
    LTP_D296A517F138A0C0: sha256:d296a517f138a0c09a3c71729b93607cfff1709b21125573bc2ad30b48302584
    LTP_D2E2A5F40B2313E5: sha256:d2e2a5f40b2313e5b9a3aa39a6922727d92fff4034821cbe122951d7c12aecce
    LTP_DD2E1A555B603C7B: sha256:dd2e1a555b603c7b2ea7b60867a7cbf5b07e84f866b5a4cd8d83f27a24028065
    LTP_E316C28E36E136DA: sha256:e316c28e36e136da592847ed1389e06538d4842d55259bc0bd80dbb61b78d10e
    LTP_E520E500AB3AE851: sha256:e520e500ab3ae8512756eb4a69fdef5de2701520040c400ce896ec773f4ab472
    LTP_E6C69C9F4AB565BC: sha256:e6c69c9f4ab565bc9a0aedb983bb975a15e4e8da818e58248848705f1fd4b2e5
    LTP_EA90C626D9AA6C08: sha256:ea90c626d9aa6c082a3af19e015cee7a37eb943ced00e4fe6af33ec4f266ba04
    LTP_EA953D5E5C4B2B1F: sha256:ea953d5e5c4b2b1f5d7e50d2191215d70c30b76cda9d1c29b51ec06d41f13bcd
    LTP_ED2BA909DF79625A: sha256:ed2ba909df79625a7857c363efc0303c51fef469ee87970e6b322004f28779a5
    LTP_EE8E695CF61D6D8A: sha256:ee8e695cf61d6d8aa981eb6e30bf3a8a53c8e8a4ad435ff362bbd78971d17088
    LTP_F1DC44813DCA6A05: sha256:f1dc44813dca6a05d2fb0697718f8ed1da8d8b033d2c49bd0124284321f6ffd4
    LTP_F4DE81D703447628: sha256:f4de81d70344762893139769a2724588ddb7213c4667529ce501948b3b6b43c5
    LTP_F8FD511858BB650D: sha256:f8fd511858bb650d732732911dd9b8f3b5680d09787b4b47438a5bb603dc1aff
    LTP_FADBA4ADECCFBA4E: sha256:fadba4adeccfba4e42423348aa44d9b192be1bcb3f9c3fa8b14a06dcdb243a3e
    LTP_FB0ABF26A21EAE3C: sha256:fb0abf26a21eae3c87515646892b72f4321684e5869b1af86bd8b799c5043180
    LTP_FC1E41C3414E7F21: sha256:fc1e41c3414e7f214284f077070cc39320ebd294786eda043234fca8d9f5da6d
    LTP_FCC236A4D5926B81: sha256:fcc236a4d5926b81662f49a2c62c658e9c87bcf2c7e179151e8658bd9395a42f
    LTP_FEACDC300C3E1DD7: sha256:feacdc300c3e1dd754c7925df645b95995a6f17fd0ebcb6a50578071e2f9636f
    MAN_027D17C587997F75: sha256:027d17c587997f75256e072b071c3a273ff5d10188d90df72df4c83f01dfba17
    MAN_02D976F1ED01493F: sha256:02d976f1ed01493f72fb104c4224a2317b6a211ea5d88d288550abb85fe93611
    MAN_03E8B237E962C1D2: sha256:03e8b237e962c1d2ded1178a8a856c9a8f05fa2f554080f72e5640a75e8bf73e
    MAN_045719AC8992819E--045719ac8992: sha256:045719ac8992819ee4aa2c0cf45f413f6505672b5cb8cf8c76683dfdab0c8492
    MAN_083368964C7623C0: sha256:083368964c7623c00bfaf93f1479ca2edacd56be42c734756ec078cd57dee064
    MAN_0BA66331CB4B2091: sha256:0ba66331cb4b20918d9576169959f9a3895937a70db3ead9651af998f7e47cc9
    MAN_0D9E79AEB44B7510: sha256:0d9e79aeb44b7510ce5ee4e104044aeede91e05c93347751fa947026b35c616a
    MAN_0F2C1ABA8AF5C15E: sha256:8e637ce17c0ce4dad505a8ee948a1df3424d2623d4b863c685520a3f58cd3ff2
    MAN_1115E878B4F50CF3: sha256:1115e878b4f50cf36f15d4ead1bd50ea131bde28efdf9a461c7e207a8984bd76
    MAN_147EECDC5DAB119D: sha256:30f13451355242b47168727a5b17e53ed0bc18240446ac065f3b8ba4b75ef811
    MAN_18C5488E8D09D6D2--18c5488e8d09: sha256:18c5488e8d09d6d235e2eeaec354ae6f3da3e3da0adcb25df2a54de4d79ed752
    MAN_1EFA395D2832F95E: sha256:1efa395d2832f95e4f5fcbcffe3d54ff5c2f016f77f317ffbb582b6f0f42aaa2
    MAN_20A10178D28B400B: sha256:20a10178d28b400be0dea7081db5fc3fb17a2fba31e8b7e593c977436359511e
    MAN_23E25F7C4136339F: sha256:23e25f7c4136339fc233a376594c3e51adbc670feb4e07f06388abcb1a9fbe72
    MAN_2421026C912D8F9E--2421026c912d: sha256:2421026c912d8f9ec305c5e9751f0d1163b29ca9fe10d9174b6eee31c9ffceb9
    MAN_254F60FBFDA7A2BB: sha256:254f60fbfda7a2bb6fc59f9a7e57c7bc0e2156bdb128297d07e503c9ed2ec6af
    MAN_25CD94348F7360E1: sha256:25cd94348f7360e150dc548a260da0605fcd58b66138e98b2c44ff75e6a1f7c6
    MAN_330C0628475E2900: sha256:330c0628475e2900e27001852e2e2d51f47e6f6667c807d5f1a6e80b28d0151a
    MAN_35AF4698AC57ED3F--35af4698ac57: sha256:35af4698ac57ed3fbd4027d53da28632f649d4584832089f17a1313728568044
    MAN_362BD9184BA2B5C7: sha256:362bd9184ba2b5c77e3102308a1858a8648220941282fef709ab2610e4490bdb
    MAN_37A8B25C745F91BB--37a8b25c745f: sha256:37a8b25c745f91bb349251c3710ce01ee8039de65c5ab602e13188c8f1d5d1df
    MAN_392816F25BD330A2: sha256:392816f25bd330a2b56467326a64e62e3fac1facf59a1a5b96c34a73901b9e82
    MAN_39C5F1849EB3A736: sha256:39c5f1849eb3a736f911044c97e17681db8edb9ecd3a8e363ecdaa8d8c5cf788
    MAN_43BBCE48C452BDDD: sha256:43bbce48c452bddd06147e2192897e4fc4a09fa385581fb17623e8ebffabded5
    MAN_44D6BD8077F837B5: sha256:44d6bd8077f837b59f4b7446204b778b7317b21c8005c20d9ac23e0747df9c40
    MAN_45A2B6F5ADF14C3F: sha256:45a2b6f5adf14c3f7b93136e2c9e0ed6dbd68a1be6c97d8f268a59cec40e51d1
    MAN_48B52042FE3DEA4C--48b52042fe3d: sha256:48b52042fe3dea4c79cdb23586ab2f4ba57bdd843a4d6ce78e97b56d366a929a
    MAN_494CD34A8C11734B: sha256:494cd34a8c11734bc9db34798547df8cc2c5b29ece8550029b5748c09ada116a
    MAN_4C50AA2793AB7713: sha256:4c50aa2793ab77139ef13b2b4a4f37b26f6d5834f8f175d9bf2af1c1a6222d67
    MAN_524B615D8F9A7E12: sha256:524b615d8f9a7e1244839aa157afec4239cedd15f1b943f88820252fdf625eb1
    MAN_5378890AE3F832EE--5378890ae3f8: sha256:5378890ae3f832eead485266d95bb504a616b5ba643e14ecaf3b4ff2d78a677c
    MAN_58936D050A8879DE: sha256:58936d050a8879deb833d1f0c26fd82f6c34633567c82a71e42be27d416f55ce
    MAN_5B2667DFDCB4EB31: sha256:61cb0a48e7b670defc81b89b80d5581ec43033a0f92fbaf3d5455e52694ec5f1
    MAN_5B4118BF4C21F770: sha256:5b4118bf4c21f7706bc594975201f277d04ee8ddcd6b25776ae13c9441ab5d10
    MAN_5F5865EF1A8D5904: sha256:5f5865ef1a8d5904288de6b5062ee6d1e7fb74125ddf77ba8807847569a6d951
    MAN_6038BC183A1CE6BF: sha256:6038bc183a1ce6bf1f011017b47094e84ad9e4c0bfc10e39d8976a6d72800493
    MAN_67ECA3FB50D80BAF: sha256:67eca3fb50d80bafa77df16282f3438f9c9c4920b7fd07decae94b227fe61da6
    MAN_6998D4E70F807B13: sha256:6998d4e70f807b1346ca12410e36102afece3730fa03bdccb9dd4be8b2b6259e
    MAN_6B7EED8E43FDD1BA: sha256:6b7eed8e43fdd1baacff9af9940105f4955ac0d16ac86e722e3c31fce38962d3
    MAN_6D665164162723C5--6d6651641627: sha256:6d665164162723c5927f1e69624afc5e14e7a2f8dba1118fc63496a505136b1d
    MAN_6D77B363EA967C8F: sha256:6d77b363ea967c8f1ea1bde45c4f2da6a4e19c2305d3f82baf8852f485a3a55a
    MAN_6FA8F2D41D1B7062: sha256:6fa8f2d41d1b7062512f7ef14612d6d6594e7f36cb6ef236fbebd35f0c135f4b
    MAN_732160952277CD16: sha256:732160952277cd1606608f4af9b0045a9446a37910b8072a6cd154c5d3afdf4f
    MAN_73E054548B324267: sha256:73e054548b32426705dd168ebed070bc65b8221d91db2f3cd7c07cdc97c6b7ec
    MAN_794294DBD03CA974: sha256:d902d1f5fea87f82fb55ca1f8cde202501fd23595ec05f804e4b48f30a3c046b
    MAN_794294DBD03CA974--794294dbd03c: sha256:794294dbd03ca974251a37571bebb81f309c66afce642709f6645806303fb1b3
    MAN_7C3C0347FD37CEB9: sha256:7c3c0347fd37ceb9c395aff447dca175e0ddb28fa6a8e4512ac456368e82130c
    MAN_8153E21BD727F6A0: sha256:8153e21bd727f6a08db324d60087d4e20d9872dfda7291879cd173ef3099205a
    MAN_81F4F1C3AD4F3217: sha256:81f4f1c3ad4f3217c876f96830d561edd132adfab97364419ef02c323122ce9b
    MAN_8609DB2EE85AF88E: sha256:8609db2ee85af88e75f0e70480a79070e6b311fae426664f6100a0b5c83248c4
    MAN_8812ADE8E360DB8F: sha256:8812ade8e360db8f8860c3534585321d58461d8a1b01b3614f8e6d175e7d1ebf
    MAN_8D160F5D77EC235B: sha256:54210d6fff8e0fa3f43acdedb25432b12ed74ba277b19e28044dbcc7eab2fd73
    MAN_8DB0AB4E3B90CB50: sha256:99f05e99e18ffad35d1d63c465b8a287c3b1b72137aa0cea75a07abcaa19a942
    MAN_8DB0AB4E3B90CB50--8db0ab4e3b90: sha256:8db0ab4e3b90cb5034fa16053963c87b696afd01c42ca53f05b3f82f4a75bf18
    MAN_9452D425539B8023: sha256:9452d425539b802321ed45714ff13d6c1fd7bedd7ab201adab57f734dcbf8d04
    MAN_95930C2D369C878D: sha256:95930c2d369c878df9727170ea77dede88f30b28d88f4134d230836b09c56ffd
    MAN_968D07C7039689E5: sha256:968d07c7039689e56f444d642d58d2627cf5570c9fb49d87d6174715532b082e
    MAN_9A17C8A141B47D41: sha256:9a17c8a141b47d41e255a725817feeef040f31bb4ee23a66a0388f3ddc3e29fe
    MAN_9BC94E6BD25C05E1: sha256:9bc94e6bd25c05e12b4495102575eb27a9d617116c52c0fe32bc96ccf6993130
    MAN_9E0C30E4205FB415: sha256:9e0c30e4205fb415e37882ebeeb276505c96311a3f6ea5e043d380fa4e7ffcce
    MAN_9E12AA9A59F1BBE9: sha256:9e12aa9a59f1bbe932067a7bea2f5fc6bb12af2006617ce2eead4b1f96df9d5e
    MAN_A1CD98CE32C423E4: sha256:a1cd98ce32c423e4e842945e6b013cb6636ddeeb0d6d9c0c7a031027bdd1c896
    MAN_A58EA189B1C9E326: sha256:04b63d7158635ccef5d77f952c96a3da5f484a2709f71a077e6cb70248c668e0
    MAN_A5F4BA2371332A4E: sha256:a5f4ba2371332a4e5ad6c94bd808ca1e5d12b3f4ebba27c6a38bce0993ea1676
    MAN_A67DCE77030808A6: sha256:a67dce77030808a6cdedab3615677b094ce676615691e2de52a6fb4b0db926a7
    MAN_AA8C115068BD5D76--aa8c115068bd: sha256:aa8c115068bd5d7652899e73145909343274a585413c093b42f7f32189eaf090
    MAN_AE68C41A115C80FC--ae68c41a115c: sha256:ae68c41a115c80fc4017a217740267206206c6d203d671fee845b58442a6e922
    MAN_AE7C62637F29A4C9: sha256:ae7c62637f29a4c902964bd59c569bbe3d477b2d56c84520b8c8c2b95efcbd36
    MAN_AF1D093225F75E82: sha256:af1d093225f75e82ca0aa65cd8a7665ef9c04e7e9e605b0ba70a468bd1912a09
    MAN_B121E5340A1BEFEE: sha256:b121e5340a1befee27d9cf92690b4f7e0255b871a8235f4fa5739aa1411a566f
    MAN_B1A8365C419E3164: sha256:0f82bcd2e050e382f7d68a136dda8b3b92679a71cb1e05533aa8674c7a4edf6f
    MAN_B1A8365C419E3164--b1a8365c419e: sha256:b1a8365c419e3164dc03060e2b7dc24203874a70076a8529e21fdbd338b522b1
    MAN_B4DD5B60F33FC5E3: sha256:b4dd5b60f33fc5e3c397b06c861b0fa7ecd88690346a18883d63a901c71a3e7e
    MAN_B5E18528035F6F87: sha256:b5e18528035f6f870e341e70298511e7345c4884bd66257f3c095ba8b605ca69
    MAN_B9EE0F176B92F526: sha256:b9ee0f176b92f5264517943ccc498c1e148bbcd1f29beb393b4c55bb51dfffd9
    MAN_BC425C37C792DDEE: sha256:bc425c37c792ddeed419770e9b57b33fa41a0def670c961a7c66a8c0140561a4
    MAN_BE74B0D21973DAEC: sha256:be74b0d21973daecfa7f765d37067b4f38de4207b0a1063e18f9cff01b73aa93
    MAN_BE929AB9651E5E66: sha256:be929ab9651e5e66a59780b20d2a800f62ea7b43b007b17615da59afb2cdd5b3
    MAN_C04F44BFF720877B: sha256:c04f44bff720877baad3f8810d2814dd0fda9aef6ee6b15acc5f29f21bd3162f
    MAN_C467D6702AB64674: sha256:c467d6702ab646745acbc033419c24bcf3adba7e9de7c3bd5daab671fe46446e
    MAN_CAA0FFEFF7C64A82: sha256:caa0ffeff7c64a82bf218a9fb6d7c5dde87bcb41e8fb0795fc7bd39adf6f36ca
    MAN_CDD044CBEEED1A80: sha256:cdd044cbeeed1a801200766b35b6ebaf72f44e1f281329942dbc71242f2525e5
    MAN_CDD195853C6DFE14: sha256:cdd195853c6dfe14718620f8892fbace0a9e23ca40f5e2ea0f799870b96b6b6d
    MAN_CEC45E0E1446E3DF: sha256:cec45e0e1446e3df175d83de317b062067cc1252be8ac188e2685182a8f20608
    MAN_D405972253EA086F: sha256:d405972253ea086f3ed41a70328bf8f5f2b5a09a52c24d2a641223dcc95011e0
    MAN_D84D77F1C6E463F4: sha256:d84d77f1c6e463f4f4c3d85ef5c089b81c00e7507cda07eeb705c75bee97da05
    MAN_DA06B43ED3D9DBBC: sha256:da06b43ed3d9dbbc3baa4d137c27c73d6d10ff2ca57f477db761b7b388b41eef
    MAN_DA93975DA79D34AD--da93975da79d: sha256:da93975da79d34add410b3d856d570f7ed0b241558c683ba8f06e3511488bbae
    MAN_DADCFA23F461FBBF: sha256:dadcfa23f461fbbf9a88ff1f9b10e85b6e1e7dac4e37ca8986fc8e414a12fa89
    MAN_DBD043A36C2E4926: sha256:dbd043a36c2e49265a5f003845c9cba0735aecd507d79dc7f57a70407e8d70da
    MAN_DC37B979EC91203E: sha256:dc37b979ec91203e49046191ce1118b342990dd607cfaae4e6498dd222fb4869
    MAN_DD6D48EB9B80CB6B: sha256:dd6d48eb9b80cb6b2d5fe9d47fc4810243c093bd9b8659332800977b9a134923
    MAN_DD8A18DB0BF6E8A9: sha256:dd8a18db0bf6e8a9df4e19403f6d40f6d4028bb331dc3c61bc496ea26ddacf38
    MAN_DE03A6A5B1731AF7--de03a6a5b173: sha256:de03a6a5b1731af7337b6fe64330f8a02f628f42dd87260aa00bf3c01e843fb6
    MAN_DFDB86CEA63B78D3--dfdb86cea63b: sha256:dfdb86cea63b78d3cb728258ccdd4e501fa440f02735ef246d17fdbc5044d250
    MAN_E116073D3FDB5C1F: sha256:5df89d10ec7725763781bc99e8b4d943a9e940b617f483ab009dffdc01a15907
    MAN_E32B6349055FCEF9: sha256:e32b6349055fcef9e6437dc8e1eaf495d3d56f10b316987a403c37553056a544
    MAN_E99D067CF243EEE8: sha256:e99d067cf243eee89be17d52596c12b3fc5286b1f5d8c8481a26cafeeff1a239
    MAN_EA69373DAD6B5B01: sha256:ea69373dad6b5b01efa066131eae0c26137143575cc80c1f62c733bb373d255c
    MAN_EDB775C51FCEA404: sha256:edb775c51fcea404016cb3f6da328eef236bf5d00a21db4c724aeb77a38e9509
    MAN_EFBA9CA2760DA6B8: sha256:efba9ca2760da6b8da59e494c821bf6f038bb5c311b7214f2f4e492ffd37d106
    MAN_F12635B7646C0E9B: sha256:f12635b7646c0e9b485e01b3c148fcd3945e9b6b1478945f19d54cfea262d9a6
    MAN_F6CB9D32040E99BA: sha256:f6cb9d32040e99ba94bc763eb811bd6525692b756fc3d04af406dcbe6c69a122
    MAN_F84F01B63ABC178D: sha256:f84f01b63abc178d1fe5bc1fa49113ceabd5237e70e1ce2ad10aa7debb586f7a
    MAN_FD5BF4CD3984BECF: sha256:fd5bf4cd3984becf55d9ca41296368832467ab7133e075ca462dc2f7053f0e61
    MAN_FDD174E970AC7930: sha256:fdd174e970ac79301953bdd92e44970778a716c86428b4b554bcd57d2a2c4f6a
    LTP_74BB3F96CBA52D02: sha256:74bb3f96cba52d02850ad3c5e54c87acf278ce51290c99d5ae29da583be9ba38
    LTP_6C14DE68E3C0CC24: sha256:6c14de68e3c0cc24bbb7021cd805e26a73df65653f350d8fa8ed8de5232949e8
    LTP_D246498B20D9CB2C: sha256:d246498b20d9cb2cd6ece54014a50e1c77fa08b6a598251c2dc0e3a3700193e2
    LTP_04236FD5B061DEB9: sha256:04236fd5b061deb91a99cc5990d76abb4d0305312af10adf6221c7cdbcf28567
    LTP_21FCBFC328D1815A: sha256:21fcbfc328d1815aad1c1fd20c4797e91d64cad63f8c4dd02b3340c29fc06412
    LTP_38432B154B641410: sha256:38432b154b641410365b7f4a7ad2ca324c3c356bf93948d3c948552a39f1f368
    LTP_43728156B00FF104: sha256:43728156b00ff104889586e9f9c3c97e3681823265c64387f32a84c300f8aebb
    LTP_58C8C307B1FF2510: sha256:58c8c307b1ff25100a989b73841bba45b1dcf61406863df2f8b8bfce4c294f2e
    LTP_6F4B3A38B8BF4C7E: sha256:6f4b3a38b8bf4c7e714c705e096b38742f0d55e11af069efd85a780cbd567c0f
    LTP_6F77CAA9FC4423BA: sha256:6f77caa9fc4423ba48f8bccdc757c34ac19acb29a8df9d9089f395904ee88d54
    LTP_71DD72481EF5740E: sha256:71dd72481ef5740e84d8f583e4c75aa6d22288a996d96ab3f4c50bef33fc2b5b
    LTP_86144BF50FB25D3A: sha256:86144bf50fb25d3a419e3c011f5c2334e4885d5643718a54ea7d6d0d3e8b4bab
    LTP_B0433B78A1641F24: sha256:b0433b78a1641f2478404ccbec3a8cad14d0a94ee86936a6d26460330ce10de8
    LTP_D254EE40E8B5957E: sha256:d254ee40e8b5957eb45b944d458cd22c2b8bd611d8da6326448e10c63c65ed36
    LTP_DCC88B2C458969EA: sha256:dcc88b2c458969ead361273a98cbb21fb0bf32a05c20068c76ebabffd55bf579
    LTP_DDA854712C50CD6A: sha256:dda854712c50cd6a2ea2a11371b97c4eee905e31d70b389262238b10091fa2c9
    LTP_6B9F97B897EC5C32: sha256:6b9f97b897ec5c326f9f68e26e9353a0e9bcb1ca59ce6f15c338328a7d201bda
    LTP_C8376BC347F94A98: sha256:c8376bc347f94a984bf5b3e6cf3baa97d7f384dde2c141d2a0a70d0693aa589d
    LTP_287CF10D893735AB: sha256:287cf10d893735aba939172ccbac5cf025dd704d8272d5048fb79e3f211821c3
    LTP_82A8802A27A3D2BF: sha256:82a8802a27a3d2bf01cb995752e7667b482979d9e93565f11e732bb2a5a31b28
    LTP_2F3E34FD672DBF34: sha256:2f3e34fd672dbf34b28611337f295a687ae0db9f5a34edb98b0cb1a9b82235f2
    LTP_4494B70BBA693D42: sha256:4494b70bba693d42cda9d0a59c88ea7d9d8bd0fcb3276d8a3fc52fa386e7ef78
    LTP_614C018F61C078A0: sha256:614c018f61c078a0c1629bf12f259ab3108460b39da9611587eb8ab0f96a9017
    LTP_7B0F966046AECA7E: sha256:7b0f966046aeca7e7a0ddc40b2774c29247dbabb79174568412a4d08596db153
    LTP_9C2FB7732A0B90B6: sha256:9c2fb7732a0b90b68e056c2337aa1e81e2e609b6ad6c60d53dadf2893b11554b
    LTP_A2934B80997B62C9: sha256:a2934b80997b62c96c7d18d8295c04e7ce45893f9122cfdb44bdfeb8070674ff
    LTP_AD3A4B98FF201ABE: sha256:ad3a4b98ff201abe4bafe39d5fede2f4d497cf03a7d50837c4c7441c515b34fa
    LTP_C13C4F63D58904BC: sha256:c13c4f63d58904bcee6e68546c3fda582209001fe4c9e4e9a46eaf6a25719cfd
    LTP_C24E55F06625D564: sha256:c24e55f06625d564c76dd85c6f1bb8c94b1270cb6e0d83790b02371b7f8fc397
    LTP_D1A18560E485E146: sha256:d1a18560e485e146f23212528bc3caba854e266e4bd431c7605891935860d811
    LTP_DA64FD04E43656E6: sha256:da64fd04e43656e65129d77e5bf6b393319bb248852a3a6db4431783ebad5bcd
    LTP_DF5B725563FDFB31: sha256:df5b725563fdfb318278bc71aa9ae5ffd772ac4f05dbd9b4f118bd9df7339f3c
    LTP_ECD986F27CF15E1E: sha256:ecd986f27cf15e1e145501e0755a1420d46a42ce091e57d23884318e37849a39
    LTP_FC8BA85373EA2D8F: sha256:fc8ba85373ea2d8f73d801b46060fd0ce0d4e78ef2f1ce6a5923118389112ce8
  static_checks:
    STARRY_CHROOT_PATH: sha256:d817cdc66b7277273694b7530ca5444e592ae6dde4fe282e9706dab3bdb7a88b
    STARRY_CLOSE_BAD_FD_ERRNO: sha256:3688bede607dda3b8566d02b28e631d99e656c165ca17f247810585f6e6e9d20
    STARRY_CLOSE_FD_TABLE: sha256:22b2aabe82905f32747892948a313452c321a5bd727a48114ab60cd9f4a7d6e0
    STARRY_CLOSE_RANGE_SWEEP: sha256:b68d84ae1e356355d2ed2f947873f1661d2acef90e75d240829ff1dc62e95ee1
    STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS: sha256:270f978e69107ec932a985c1cda9d40c23fba71e749ab30fb936feed963a9796
    STARRY_CLOSE_RANGE_VALIDATION: sha256:647d3cf0fdb66dd12325ecc9b2512573246e8b70f4d3e76fc3825008fdc13954
    STARRY_CLOSE_SYSCALL: sha256:098456e0db6f88a9696e9be3f748f7fc3466e747ab9c3fad713e7832f944dec5
    STARRY_CONNECT_ADDRESS_VALIDATION: sha256:d1a6e8339cfa112a4c240e163ec01b885aeed46f5ed1e6de3c715e6445ab0c97
    STARRY_CONNECT_ENTRY: sha256:a483667d4879cf3e66ee135e8a55e72ce34396420812383649fd6fed8fead5d1
    STARRY_COPY_FILE_RANGE_CORE: sha256:d3fbeb11a1f0facf48e7447c38ff2b0dcf2c0cbee77889fe5c05cf30698792ca
    STARRY_DUP2_DUP3_BEHAVIOR: sha256:1814d475d47e2ee693e7440a774842a99ea7bf197f5d0f5a5f38fdf65c455971
    STARRY_DUP_BEHAVIOR: sha256:10d750a4976d0be8353dcbddf7c80e88682a6c8012c7df7aad87423595f1a3f5
    STARRY_EPOLL_CREATE1_FLAGS: sha256:f2163883a6167eb0dfabb0b48c02cb981e4bb14c6730811e0b3348a4de8ead23
    STARRY_EPOLL_CTL_ENTRY: sha256:5e9c5d89216a0956603db791f7735b1ba18813e00b42e81c3a16292fbd905162
    STARRY_EPOLL_CTL_INTEREST: sha256:432cd717a72ab0632dad3d1b2702aa43469400853a917d4562a935466ea2fb7a
    STARRY_EPOLL_FACCESS_ERRNO: sha256:e22921f6310fd12312f5a9094c1b2a7fbfa561ff1c45b5d2578d6e4736cb6a79
    STARRY_EPOLL_FD_LOOKUP: sha256:189e42bb88fc505c6fe33c7531efb1b30f99aa83aeba33ae39f4362fefc41f46
    STARRY_EPOLL_NESTED_LOOP: sha256:a051a74deeaa59fdca6eed7d45ab359ade23a502ffa8d19b6f3de98cb94765ce
    STARRY_ERRNO_TRANSLATION: sha256:8d9a60adf231f913f00d0778fd209ab68edadef24ab77fdf68d527374a9163c5
    STARRY_EXECVEAT_FACCESSAT_RESOLVE: sha256:b23f34dc7191754d8e39d5c6a62dd40508f1a505de85e96ecbbf63673c9616dc
    STARRY_EXECVEAT_VALIDATION: sha256:c76c2cd9e97731a525b77e7c46779eb948ec5d57a2e685f43d66d575e8f35b50
    STARRY_FACCESSAT2_VALIDATION: sha256:2a7c3ad920d88352ba2c16849143d93f64f6da0d95a67ce6f1a8d260c6080d0c
    STARRY_FCHDIR_CORE: sha256:6efabd8ab5037dfcabf4998c5ca0727afbfe837cf43acd4bcc0b0eefafd806eb
    STARRY_FCHDIR_ERRNO_TRANSLATION: sha256:fd177e9b3e1499c807d22c42b2ae346718855fa428f5302aa43ecb67b1bd2997
    STARRY_FCHDIR_FD_VALIDATION: sha256:17cf5cd7e876370fda3b89a496c7c087f3827da61a2ee056193ef8401fa1f628
    STARRY_FCHMODAT_FLAG_VALIDATION: sha256:2759b18590554a478af9dd86da5c27e91a163b2987208be937592264c83cfc0f
    STARRY_FD_TABLE_LOOKUP_ALLOCATION: sha256:4bd01e5c33cabcf5458b72c9f3e8863f6e7ce37a1db5127e622bcec36267a2f4
    STARRY_FINAL_ERRNO_TRANSLATION: sha256:7335ab25a23d7920d554be244a3f02fe0be4dfd16f61ffbf3a9de5993cadf0c2
    STARRY_FINAL_SYSINFO_COPYOUT: sha256:fabeb1b90d63733c74800db189e3cf309f7823290add2421d37f2965f13ad0d1
    STARRY_FINAL_TIMER_DELETE: sha256:e300264bee85147a9a5d2ec81a6280444803b96d858336c30600080c40ee820c
    STARRY_FINAL_TKILL_TID_VALIDATION: sha256:1355e02217d5f3bd03fbb329a928015dcd367ceea991d8e160b1f501c50ad7f7
    STARRY_FINAL_UNAME_COPYOUT: sha256:22d2b44a9c168414e9c99d02e3f91db41a61f6023a3a8bb46c64b03e039630e4
    STARRY_FINAL_UNSHARE_FILES: sha256:59906058d6dd4abe0669d7409fb79dc5e2851be551e778dc1d477000e21000fa
    STARRY_FINAL_UNSHARE_FLAG_VALIDATION: sha256:c7ffaed34db719fbbb9d362ab17ab42a6a7b58f629b2073e8ff81c9f7a0676b3
    STARRY_FINAL_WAITID_OPTIONS: sha256:eaa39e7dda1d0fd8b5bf474137b06c8d05da3caa7736e3fc4521731d28b8802f
    STARRY_FINAL_WAITPID_INT_MIN: sha256:6439677bbe44b634d0b03458f4f3d5a766778eb4c754fede279254e996de77a8
    STARRY_FINIT_MODULE_FLAG_VALIDATION: sha256:02b5ac507da07f65ee1eb468d782446b05ce6455a8e57c5e7132becd2c08cd07
    STARRY_MAN_CLOCK_GETRES_VALIDATION: sha256:39c59823deb4fa50619416109c4e60818a95fd08b7e778004ad4dad25a46b1f5
    STARRY_MAN_CLOCK_GETTIME_VALIDATION: sha256:2227be48f5b4c7498f1f70ee087020f5f3633478d37994e1ce95be353b554be3
    STARRY_MAN_EVENTFD2_VALIDATION: sha256:13648156878333adeb78204595c0199fd5930f1b57a0d9dfdbcad2b1a6d2ca3e
    STARRY_MAN_GETRANDOM_ARGUMENTS: sha256:c89ce496ae2155da99e328b9ec02e93addb69b9a9502d311b71f8a9541cee940
    STARRY_MAN_INOTIFY_ADD_WATCH_INPUTS: sha256:e5babd6cb6f55f3c084963bd21bb306a9a5fa7223fac9726e0c46f44d93f0b9b
    STARRY_MAN_INOTIFY_INIT1_VALIDATION: sha256:9b3a7ef6d751aaa85559093ba95e658d18f1fdd232b1fdbc1f2d84250f0ba95a
    STARRY_MAN_INOTIFY_RM_WATCH_ID: sha256:eac5c811986b666a85919e0302a8e6bc2ea53016811b0c0c768a0d2ab99766eb
    STARRY_MAN_INOTIFY_RM_WATCH_INPUTS: sha256:939271cdff41f8344d41706444ac2a4e8c48062080fa87d555f25e4881586e43
    STARRY_MAN_LISTEN_ENTRY: sha256:d03fc9ce42dbb6f8111aaeed4ff4d3090bce65717c6af1899ee061d117b99fe8
    STARRY_MAN_MEMFD_CREATE_VALIDATION: sha256:c843b6e0726c72d7600bc65a6579dd95147bd9b64076f3f52b63ce54ea4657e3
    STARRY_MAN_PIPE2_VALIDATION: sha256:2fc1688a6ae9ee7d6731e73add9ed7573d7b415b42590e62f79528c408203b55
    STARRY_MAN_REBOOT_VALIDATION: sha256:9c70a80c009a123b465beea168b4d650d2c9682e7e0ab8ed3ea5d14bcc0aec21
    STARRY_MAN_SECCOMP_OPERATION_FLAGS: sha256:cc9f481eda67f62b6c703372757260c6ff47317ecc46e7c673b798e07782450a
    STARRY_MAN_SECCOMP_VALIDATION: sha256:b30946bfc14afca77aa8e610940bc9b4d739d445bf7544888fc20ccf984b876d
    STARRY_MAN_SETDOMAINNAME_ARGUMENTS: sha256:52bc1e1519f29f80288fb07e135041049fc219b2dcf53f005b0863d9ef17274b
    STARRY_MAN_SETGROUPS_VALIDATION: sha256:8b357dc37a9d23de00b426bc321759a943306e872ec60c3b97b8aa23056d0da2
    STARRY_MAN_SETHOSTNAME_ARGUMENTS: sha256:63ebc4b591412322c7889cc69d118adda45f6e88d266c2033b70cd8073dc2491
    STARRY_MAN_SHUTDOWN_VALIDATION: sha256:5aeedd7b1f0f02eb2e287c818f73ac61c922daf53a3010d1e56b650a16a21727
    STARRY_MAN_SOCKETPAIR_VALIDATION: sha256:98095b1d4f8be3ca5cce69a464e5708fa401b465c44ab29f31bc172d2f331130
    STARRY_MMAP_ACCESS: sha256:de1c0d707169e1e81d3b24bdfbb470fc9fc179213b603ca9e2e5010423b67af5
    STARRY_MMAP_ARGUMENTS: sha256:e83e60fea871601e0384c76e576ddbeee45210d9ff13fd84c816d7ad7dc8a560
    STARRY_MMAP_FD: sha256:399a5e6488d63e6e7906840fb0cbf3a7b57b7e4cb22564bd069ee535cd09c703
    STARRY_ROUND2_CLOSE_FD_TABLE: sha256:f66aba3c652105df45d6cf102d1672da083636ee12d2d3ff019789aacca6bcc1
    STARRY_ROUND2_CLOSE_SYSCALL: sha256:d6e7f46d631f54cfbf8c53286c0eff767bfe8fbf9a94d0cecb16ecbbaadd539e
    STARRY_ROUND2_ERRNO_TRANSLATION: sha256:44ca1b0e564fb100d4d632b7265d3c7eef30d29f4eead5c61bbb4cab45769537
    STARRY_ROUND3_ERRNO_TRANSLATION: sha256:092633b5bbc1d879cf72a97b889f5a99fa41814409197e21307f7c2e928a7b89
    STARRY_ROUND3_FSTATFS_ERRORS: sha256:543941f48be5bbb202d5f8e9e9d82b8243f945d28ac9db8d55d317c0d34dc66e
    STARRY_ROUND3_FSTAT_CORE: sha256:4a7bba46fd86955a89f0f4e4bc2555c1da47362aa295e98efb19f48da45f9049
    STARRY_ROUND3_GETCWD: sha256:73775de9aebd8a606e4826ecba2a252ab16e507cae2ee06832613491104e3c46
    STARRY_ROUND3_GETPRIORITY_SELECTOR: sha256:21ca3db01eeb28f97c55cb10fa2109985843f45791eb95f17a7c1c6b1eb93986
    STARRY_ROUND3_GETRLIMIT_CORE: sha256:a566f3a65de9d400117cb9415d11a5efb0790d2aa508fcdecb94405c6c95b860
    STARRY_ROUND3_GETRLIMIT_DISPATCH: sha256:2f1fc31793fe71bef62add5e3c56982d46bddf280f64357a7d67c57b61428047
    STARRY_ROUND3_JOB_ID_LOOKUP: sha256:ac335083b4908572a3e23dd3e8a0f990d3a62ecbfc7cee0895a57893c140fa9e
    STARRY_ROUND3_PROCESS_LOOKUP: sha256:da4344fb0b2e8ee152e5d502fd04eb765733baedfbd263f5c95984051c740142
    STARRY_ROUND4_ERRNO_TRANSLATION: sha256:9fc9e5adffd48e65065cfd90d7901d1df41a02fc010a735e3d354055346f85dd
    STARRY_ROUND4_MLOCK2_FLAGS: sha256:451a3c92dd203c594502317904dcedea1b74620e1a9db5c2781345b07c969248
    STARRY_ROUND4_MSYNC_EXCLUSIVE_MODES: sha256:0578df5fcb3eef561e0d51077bf4724c55f01d277361849b03e0516478f3a30a
    STARRY_ROUND4_MSYNC_UNKNOWN_FLAGS: sha256:48ef4ae8f5622bf555efb372cbc0025bdf4ab5eb9bc9470b622c68467836e765
    STARRY_ROUND4_MUNMAP_ZERO_LENGTH: sha256:179cf3a1ea372121ce5d29a1eff7cfc0861ea7bf93a78a20c0c280a972aecec3
    STARRY_ROUND4_OPENAT2_SIZE: sha256:90f4395e66b3445c53574857329bfff21977ce31e516f2429b262fd66af5b056
    STARRY_ROUND4_PIDFD_GETFD_FLAGS: sha256:92a764693b05210a48253bfc6a2737474f011b2b54aa329d8becd879a60494a5
    STARRY_ROUND4_PIDFD_OPEN_INPUTS: sha256:70ec2374f1dcd688c4fcbdc8ffafcc93af19190f7a10a8fb960c5339837f1c37
    STARRY_ROUND4_PIDFD_SIGNAL_FLAGS: sha256:c4a2f69143da820bc683c34f4d511374d5362c6d6f37c0d56dc44f198944d398
    STARRY_ROUND4_READ_BAD_FD: sha256:06f24f5a120841e298f8a157ff0169342c935908ee1379dc8975d4b61ce55706
    STARRY_ROUND4_VECTOR_IO_FLAGS: sha256:2d911dc6bd53e6fc8a77a5209ebdc9e8f5bddfff56fde3f3715b7cc3832043a7
    STARRY_ROUND5_ERRNO_TRANSLATION: sha256:546b5bc4454aed59688b0b8a987f0207e6499398dd3e25065eb5d44e34c6cf8c
    STARRY_ROUND5_SCHED_SETAFFINITY_EMPTY_MASK: sha256:1f586167c13a6afbf5a37390f718844077bb1db86b5af03a6727eb05b024a0b7
    STARRY_ROUND5_SCHED_YIELD: sha256:4b993294f76b39f4d5ea5c02b1ec87ae2fb7bf8602b797cb04f368280bfb66f2
    STARRY_ROUND5_SENDFILE_IN_FD: sha256:c75e772fd1599ff88cc107d1feb67f0646652623adf759665fd42bb6d3cd5aa8
    STARRY_ROUND5_SENDFILE_OUT_FD: sha256:a6310ca6f51ea5b7f2476cb6c791befea85389f449edf7910cb9e737c76dcb8d
    STARRY_ROUND5_SENDMSG_MESSAGE_POINTER: sha256:d98fdcf1f705c6c89ed155d2cedd172ab10c0edfcdd47e440804cfced1dcf47a
    STARRY_ROUND5_SETPGID_NEGATIVE: sha256:e923f0a95c9d3ed1126bc7a86b0ca6c8193477f0035d3cbd51dd1c9b323546c1
    STARRY_ROUND5_SETPRIORITY_SELECTOR: sha256:9cbac9cb08c0446ec8cb0e62deab0da59b922b095489fb8dd540b8f0de3c93d3
    STARRY_ROUND5_SOCKET_INVALID_TYPE: sha256:d2d8afede60aa68d453d70afcadbef69e726ab083280b704d2897d9d62bf31d1
    STARRY_ROUND5_SOCKET_PROTOCOL_ERRORS: sha256:c356539030c60bac476550a7a7eaef646d065dfbb22b00c2d1e365071f077092
    STARRY_SOCKET_FD_VALIDATION: sha256:4b6bc51f2d193cfb1a8f8ffa1097da5c55ba6a184d9206e76efb55240294733e
    STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO: sha256:39ebc0849b8fede86d9689ed1dba7fda23315b83937a447b328ffd1a94bdfb34
    STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE: sha256:e2e77be33c0c00e8b38780cef8b7b9ff37f7271c1a4f1d1289041b8cf68f4817
    STARRY_ROUND3_INIT_MODULE_PERMISSION: sha256:9df3be22e06572f2b77a0e12c13e9bc9c3a498b4317a288e87e880ee8b23d177
    STARRY_FINAL_SYSLOG_READ_ARGUMENTS: sha256:947467c63df939000091ce9bbfa725b3dac3bd6d9fdb07cbb606a5ef778825f1
    STARRY_FINAL_UMOUNT_PRIVILEGE: sha256:9076327bc10ad8f7970328c88a4b62abfe9cbdc3118616d23772096e764afae7
    STARRY_FINAL_UNSHARE_NEWNS_PRIVILEGE: sha256:647346966f4cd913f5bc3219f181a2d9b7f6865ea1decc8e898b1f28751b9842
  dynamic_tests:
    STARRY_FINAL_FS_RUNTIME: sha256:74f19339cd0cbf3cbe5563a79ce90d92665484515dc3bb2e184412d28073f9dd
    STARRY_FINAL_WAIT_RUNTIME: sha256:097f4cbfe7a71eeb6388c56404f67f407d9dc62ce2e19c3d4bad524dd750358a
entity_versions:
  rules:
    LTP_0087F445CEB63414:
      id: LTP_0087F445CEB63414
      generated_at_utc: '2026-07-16T04:20:06.737209Z'
      content_hash: sha256:0087f445ceb63414b632c05b271af9fee6f2b3c7167fbc43e208a7b0a485ca33
    LTP_026CB4A1CA7CDC6B:
      id: LTP_026CB4A1CA7CDC6B
      generated_at_utc: '2026-07-16T04:20:06.737209Z'
      content_hash: sha256:026cb4a1ca7cdc6bf1b2e94352fa72c86bda5fc328c6ed9ae8983b4696a2c0f8
    LTP_03AF14160F8B59A0:
      id: LTP_03AF14160F8B59A0
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:03af14160f8b59a0b546095a476facf6e3504937dd6f387971839bd21441739b
    LTP_08F05BA6ED1CEE6A:
      id: LTP_08F05BA6ED1CEE6A
      generated_at_utc: '2026-07-16T04:20:06.737209Z'
      content_hash: sha256:08f05ba6ed1cee6adc06e52236156d77d5c6dd5d4592642bd443aa47f5e425b7
    LTP_098AFE0E8E10B0EF:
      id: LTP_098AFE0E8E10B0EF
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:098afe0e8e10b0efa6872ee3d2ece3674b519943b59189a2758d8ab31b06ab26
    LTP_09B39E9C9254ECB2:
      id: LTP_09B39E9C9254ECB2
      generated_at_utc: '2026-07-14T13:35:02.567816Z'
      content_hash: sha256:09b39e9c9254ecb24ccb5288c3f12281e9adc0b698de5c706a4f071599c3ce60
    LTP_10B3572DBFA6742B:
      id: LTP_10B3572DBFA6742B
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:10b3572dbfa6742b44e40e6ffb78f797d484d1c0f37cedc5e4bc5c0099e8b498
    LTP_1691F6F9712C5546:
      id: LTP_1691F6F9712C5546
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:1691f6f9712c5546d1b81c76cc385ed8b961683e209c8d54e9543a02a199aac5
    LTP_1726C16756E9651C:
      id: LTP_1726C16756E9651C
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:1726c16756e9651c8be282bf1cdf5c30a283e32aa200934084e3c42a2aee9ff9
    LTP_17B7A9460939622A:
      id: LTP_17B7A9460939622A
      generated_at_utc: '2026-07-16T02:52:01.871423Z'
      content_hash: sha256:17b7a9460939622a41226aa0c0191c618d2a9b74c6e2321e127b1ba067b85bff
    LTP_1AACAC53BAF23BA9:
      id: LTP_1AACAC53BAF23BA9
      generated_at_utc: '2026-07-16T04:20:06.737209Z'
      content_hash: sha256:1aacac53baf23ba9aec716bf031354593948226151154448887698bf2a5dde0d
    LTP_1BB76939FF2A40B5:
      id: LTP_1BB76939FF2A40B5
      generated_at_utc: '2026-07-16T04:20:06.737209Z'
      content_hash: sha256:1bb76939ff2a40b56089c39f1e2e8db30af944a15e86e47a4e98a572bd8319ea
    LTP_2554AC2E46FC6A15:
      id: LTP_2554AC2E46FC6A15
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:2554ac2e46fc6a15932bc27db324eb7b2b1265b2270c61b345af14c0b79e241d
    LTP_26555A26680524AD:
      id: LTP_26555A26680524AD
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:26555a26680524ad18ca9e9f1082b5f71c9edbd627be17b015751aadffc79033
    LTP_26AE3C69D80D35F8:
      id: LTP_26AE3C69D80D35F8
      generated_at_utc: '2026-07-16T04:20:06.737209Z'
      content_hash: sha256:26ae3c69d80d35f8cde32c3371db6ddce43877024723415f2c15a30f19a02756
    LTP_2BDE60C0E64B4DC8:
      id: LTP_2BDE60C0E64B4DC8
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:2bde60c0e64b4dc8fc4b1e23c70973364d891d517c1f8020f709fabec59e6d0f
    LTP_31D9D767D6888DDA:
      id: LTP_31D9D767D6888DDA
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:31d9d767d6888ddaf3c03f24abe0bc874e9932a546e4cdd283ecad199e6bcc1a
    LTP_3741A721C9C463D0:
      id: LTP_3741A721C9C463D0
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:3741a721c9c463d0d65d94387111a493a2a48a2a5f1975fc7d455144d3321154
    LTP_3743BC827FB4F981:
      id: LTP_3743BC827FB4F981
      generated_at_utc: '2026-07-16T04:20:06.737209Z'
      content_hash: sha256:3743bc827fb4f9819137ea970af9f8219bfff5989b4fa99ce035c18fa3ca4937
    LTP_37C625BD7D7C5F1D:
      id: LTP_37C625BD7D7C5F1D
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:37c625bd7d7c5f1db42b7cacc49b4964844f0c2f977ad1a74c3960da0d662932
    LTP_39B1E5C574F2D3DC:
      id: LTP_39B1E5C574F2D3DC
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:39b1e5c574f2d3dc16cd61efcb95f2cb9bffc5d5a5f86c1e52b9fac3ef82d569
    LTP_3A7B17AF231D4158:
      id: LTP_3A7B17AF231D4158
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:3a7b17af231d4158b2c4508e92a25435b89a569164e6dfdabc216b48e1afec9f
    LTP_3B1458E6E26CBB53:
      id: LTP_3B1458E6E26CBB53
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:3b1458e6e26cbb5398ae5221e8cb8d70b475e8e7fa008f9752270403cd9e3e38
    LTP_40A45C5E82D7F4A1:
      id: LTP_40A45C5E82D7F4A1
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:40a45c5e82d7f4a1748fc7b7d74b4700d4498c801e0fdbad387797d941bb7a7b
    LTP_425E5A3502541DE8:
      id: LTP_425E5A3502541DE8
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:425e5a3502541de863d8b8e88eafb95db2f8d8e1f9cb88a32d8b3124950395b2
    LTP_4308D71D8BD6519D:
      id: LTP_4308D71D8BD6519D
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:4308d71d8bd6519d6d2c15cb0c6d1925eed73874700fd6f1c1cc8a86199632a4
    LTP_44DC5382746D773D:
      id: LTP_44DC5382746D773D
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:44dc5382746d773d253ddf7ccb3ede2e242b978ebfb3e0756367ceb4d839956d
    LTP_4953FAD330ADE150:
      id: LTP_4953FAD330ADE150
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:4953fad330ade1503bf7a6d4d6bf2c353a337844f58042ceb3214149d1025945
    LTP_4C1F446C9C520B36:
      id: LTP_4C1F446C9C520B36
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:4c1f446c9c520b36b7f3b5a39c42fea74e7befa2adf95e4a919a1bb760184320
    LTP_4F02ACC6E2F6B094:
      id: LTP_4F02ACC6E2F6B094
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:4f02acc6e2f6b094f06413684c004106e4c18d8f654cbb8b231de56e60aba90c
    LTP_511185D6DE2A63A0:
      id: LTP_511185D6DE2A63A0
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:511185d6de2a63a045d2f5f65babdf4c25b4066ece863b9f121419045563d4c9
    LTP_51E295101A9F4411:
      id: LTP_51E295101A9F4411
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:51e295101a9f4411b8c43521d430e85bd27ac1d7a96127b66675d7dc024ba9d2
    LTP_53E3454ED6EFD842:
      id: LTP_53E3454ED6EFD842
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:53e3454ed6efd842d4456341bdaf29e25ad49ab8f5a55c170a4e23c3355fe2f9
    LTP_5516B8A938B9C3A5:
      id: LTP_5516B8A938B9C3A5
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:5516b8a938b9c3a56502a0790304ef99d9caee848e7faaafcdf2f016f6443230
    LTP_585CC852338F38EE:
      id: LTP_585CC852338F38EE
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:585cc852338f38eedc86755b62d33a8eb443200486dd86bb3f79a4a4df80981c
    LTP_5D8D2B3BEDA79604:
      id: LTP_5D8D2B3BEDA79604
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:5d8d2b3beda79604301b79695ead77bb1cca6ec4c1e6b679aabacb702befdccf
    LTP_652CE911B47794E0:
      id: LTP_652CE911B47794E0
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:652ce911b47794e00cd84120507ce0a4b8fe539ae38dff3f3c047d91cab6d2e1
    LTP_6B29B31CE99466E6:
      id: LTP_6B29B31CE99466E6
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:6b29b31ce99466e6682913919c0fad006475b094d59fadcc43c1ec6f4e9d1630
    LTP_6FFB17DB762F3167:
      id: LTP_6FFB17DB762F3167
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:6ffb17db762f3167790a052bae0fa49f44b1075991c29dcec06f56509e9ae743
    LTP_729222947741DFD6:
      id: LTP_729222947741DFD6
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:729222947741dfd63a81e9c93572baf5c789acbffca84a2edd5dce13fe1fb2a3
    LTP_75D52C5E9C93B6D7:
      id: LTP_75D52C5E9C93B6D7
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:75d52c5e9c93b6d7989e3392a132ca3a319f4419c2f678533dc80d000c4891cd
    LTP_76BFF56F735A0074:
      id: LTP_76BFF56F735A0074
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:76bff56f735a0074d725ee7dab337c42b7daf23d2ca44135affba4b983676aa8
    LTP_791DEA825D66980B:
      id: LTP_791DEA825D66980B
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:791dea825d66980bfded73936e4745cf7b914f20652b9489e65a7a59509b897b
    LTP_7BC885B5878C95B6:
      id: LTP_7BC885B5878C95B6
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:7bc885b5878c95b621d9876c970257da2de585ab5e9771c1542ceed3b28f8ad0
    LTP_7DFAC48A8971CFE3:
      id: LTP_7DFAC48A8971CFE3
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:7dfac48a8971cfe3c53af5bdc67246aedc28a76f25fe9bb7d59bb5481e0d4295
    LTP_83709E56D6285F71:
      id: LTP_83709E56D6285F71
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:83709e56d6285f71dce5dcd5f54aa0ba99d44ddef002f1e6cc53f2fce6075678
    LTP_84DBE108A850E845:
      id: LTP_84DBE108A850E845
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:84dbe108a850e845bf4a3cfc65c984525f06a85bcf44e616283b5ef4e16bb451
    LTP_88D300A8FB407324:
      id: LTP_88D300A8FB407324
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:88d300a8fb407324aefbe09d1b569b46d87628a1639509250755357a2c634c1a
    LTP_8988E5015778894A:
      id: LTP_8988E5015778894A
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:8988e5015778894a14a0b54cc6fe1a0f1f2917fb41a0c6dfd0152069d07c8d56
    LTP_8C1C2578972FCA1D:
      id: LTP_8C1C2578972FCA1D
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:8c1c2578972fca1d655df720a137f88882824f681ac3cbfa59052c4a1f8ef64a
    LTP_914935DA5C379DA1:
      id: LTP_914935DA5C379DA1
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:914935da5c379da10358ba568cfe5b8c7a31f6c57db6f6446451375aa973c46a
    LTP_91ED7E85761CE00F:
      id: LTP_91ED7E85761CE00F
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:91ed7e85761ce00fb0a63c61b421b825e76cf8577e07d172597be6451388fa31
    LTP_9305FA6D8B835652:
      id: LTP_9305FA6D8B835652
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:9305fa6d8b8356529faec8a8a060de73350f98dc7a1db1af07a5e45a6f6e11ae
    LTP_9461AA782926BAB4:
      id: LTP_9461AA782926BAB4
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:9461aa782926bab4cb006db18510ae154420b8c023b3b2f9cc0308d205ca9cf7
    LTP_971DB17D32C51561:
      id: LTP_971DB17D32C51561
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:971db17d32c515614f0af38045463319bd4bfb3a661a4ae9e4486c0404c75ead
    LTP_9B3646398697EA64:
      id: LTP_9B3646398697EA64
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:9b3646398697ea6481b4201006e677123cd226bb81910f45b6fa558aaa810832
    LTP_9B36D27A4A2994D0:
      id: LTP_9B36D27A4A2994D0
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:9b36d27a4a2994d0fb9becad9ddba6985ba56fddf7db2169f2efef4819243591
    LTP_9F560A103CB6F910:
      id: LTP_9F560A103CB6F910
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:9f560a103cb6f910cc2b8fb141c7de076accd6a913e920715328e9facdfb18db
    LTP_9FD87A3F7688FEF1:
      id: LTP_9FD87A3F7688FEF1
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:9fd87a3f7688fef10bea92050ac0661fedef311659e6ffce7573ff015c42b21d
    LTP_A0547B601C515355:
      id: LTP_A0547B601C515355
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:a0547b601c51535524cdadea7c3abcbc2fcd16157591cc2322cd1def6a08cc56
    LTP_A367723236ADA8B4:
      id: LTP_A367723236ADA8B4
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:a367723236ada8b46a0d6d3a444b7812e36d2f96cc8654bcd32ce5076bb39ed0
    LTP_A4A662687B98D33F:
      id: LTP_A4A662687B98D33F
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:a4a662687b98d33f933b37774536af580d8b9e44d1bc317c426dd2c4a68a7a1e
    LTP_A774FC10727E8ED2:
      id: LTP_A774FC10727E8ED2
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:a774fc10727e8ed282a01bc787e12bd54a0d81a756fc45037304c5906dadb2ff
    LTP_A9BC7EBC1784A722:
      id: LTP_A9BC7EBC1784A722
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:a9bc7ebc1784a72263646142685fb7ed3bb7aec45b58cfc208bd762f44d7c8fe
    LTP_ACF7A30AF3B10973:
      id: LTP_ACF7A30AF3B10973
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:acf7a30af3b10973088f22334a5e2b35a00bbc3ff6530b1fb644856f637f06e4
    LTP_AF8D38878ED1A9DA:
      id: LTP_AF8D38878ED1A9DA
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:af8d38878ed1a9da8bcca89799d36f633a0776307b92fe435d004f9b6cb1b444
    LTP_B058D6B9CBBB459D:
      id: LTP_B058D6B9CBBB459D
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:b058d6b9cbbb459d2d0e155285c19e2e49762cc25177b335dab254142809eb74
    LTP_B7F51635806E7E59:
      id: LTP_B7F51635806E7E59
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:b7f51635806e7e596b7f6a1baf152d74ca1d365a9bdfc6d3f34984ac1908632d
    LTP_BD5C209F4C6EE910:
      id: LTP_BD5C209F4C6EE910
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:bd5c209f4c6ee910a13539baa6f55f3f3d2654a60e583b67fa26724405421ad3
    LTP_BDA36F61423EEB3E:
      id: LTP_BDA36F61423EEB3E
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:bda36f61423eeb3e616d764edd458663817800e2f3db3adfae687bd17f6c2764
    LTP_BF2428964ADD116F:
      id: LTP_BF2428964ADD116F
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:bf2428964add116f793723626820cf1b363a819d6e38ba6d31d9832e4ab1b2c0
    LTP_CBF4B6C8A1458A28:
      id: LTP_CBF4B6C8A1458A28
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:cbf4b6c8a1458a2885c6c847b47ca93098a06580fc5fdfc3a1e483b9dab01ac4
    LTP_CCC36F43E9463D3E:
      id: LTP_CCC36F43E9463D3E
      generated_at_utc: '2026-07-16T02:52:01.871423Z'
      content_hash: sha256:ccc36f43e9463d3e65e732efa9e9d62af421e5d01bac07a5d343fc88f368505c
    LTP_D0800876342DE939:
      id: LTP_D0800876342DE939
      generated_at_utc: '2026-07-16T04:20:06.737209Z'
      content_hash: sha256:d0800876342de9392e43300d2797ff5244107ca4127ddb02ed0ec08832b03e82
    LTP_D296A517F138A0C0:
      id: LTP_D296A517F138A0C0
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:d296a517f138a0c09a3c71729b93607cfff1709b21125573bc2ad30b48302584
    LTP_D2E2A5F40B2313E5:
      id: LTP_D2E2A5F40B2313E5
      generated_at_utc: '2026-07-16T04:20:06.737209Z'
      content_hash: sha256:d2e2a5f40b2313e5b9a3aa39a6922727d92fff4034821cbe122951d7c12aecce
    LTP_DD2E1A555B603C7B:
      id: LTP_DD2E1A555B603C7B
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:dd2e1a555b603c7b2ea7b60867a7cbf5b07e84f866b5a4cd8d83f27a24028065
    LTP_E316C28E36E136DA:
      id: LTP_E316C28E36E136DA
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:e316c28e36e136da592847ed1389e06538d4842d55259bc0bd80dbb61b78d10e
    LTP_E520E500AB3AE851:
      id: LTP_E520E500AB3AE851
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:e520e500ab3ae8512756eb4a69fdef5de2701520040c400ce896ec773f4ab472
    LTP_E6C69C9F4AB565BC:
      id: LTP_E6C69C9F4AB565BC
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:e6c69c9f4ab565bc9a0aedb983bb975a15e4e8da818e58248848705f1fd4b2e5
    LTP_EA90C626D9AA6C08:
      id: LTP_EA90C626D9AA6C08
      generated_at_utc: '2026-07-16T04:20:06.737209Z'
      content_hash: sha256:ea90c626d9aa6c082a3af19e015cee7a37eb943ced00e4fe6af33ec4f266ba04
    LTP_EA953D5E5C4B2B1F:
      id: LTP_EA953D5E5C4B2B1F
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:ea953d5e5c4b2b1f5d7e50d2191215d70c30b76cda9d1c29b51ec06d41f13bcd
    LTP_ED2BA909DF79625A:
      id: LTP_ED2BA909DF79625A
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:ed2ba909df79625a7857c363efc0303c51fef469ee87970e6b322004f28779a5
    LTP_EE8E695CF61D6D8A:
      id: LTP_EE8E695CF61D6D8A
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:ee8e695cf61d6d8aa981eb6e30bf3a8a53c8e8a4ad435ff362bbd78971d17088
    LTP_F1DC44813DCA6A05:
      id: LTP_F1DC44813DCA6A05
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:f1dc44813dca6a05d2fb0697718f8ed1da8d8b033d2c49bd0124284321f6ffd4
    LTP_F4DE81D703447628:
      id: LTP_F4DE81D703447628
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:f4de81d70344762893139769a2724588ddb7213c4667529ce501948b3b6b43c5
    LTP_F8FD511858BB650D:
      id: LTP_F8FD511858BB650D
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:f8fd511858bb650d732732911dd9b8f3b5680d09787b4b47438a5bb603dc1aff
    LTP_FADBA4ADECCFBA4E:
      id: LTP_FADBA4ADECCFBA4E
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:fadba4adeccfba4e42423348aa44d9b192be1bcb3f9c3fa8b14a06dcdb243a3e
    LTP_FB0ABF26A21EAE3C:
      id: LTP_FB0ABF26A21EAE3C
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:fb0abf26a21eae3c87515646892b72f4321684e5869b1af86bd8b799c5043180
    LTP_FC1E41C3414E7F21:
      id: LTP_FC1E41C3414E7F21
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:fc1e41c3414e7f214284f077070cc39320ebd294786eda043234fca8d9f5da6d
    LTP_FCC236A4D5926B81:
      id: LTP_FCC236A4D5926B81
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:fcc236a4d5926b81662f49a2c62c658e9c87bcf2c7e179151e8658bd9395a42f
    LTP_FEACDC300C3E1DD7:
      id: LTP_FEACDC300C3E1DD7
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:feacdc300c3e1dd754c7925df645b95995a6f17fd0ebcb6a50578071e2f9636f
    MAN_027D17C587997F75:
      id: MAN_027D17C587997F75
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:027d17c587997f75256e072b071c3a273ff5d10188d90df72df4c83f01dfba17
    MAN_02D976F1ED01493F:
      id: MAN_02D976F1ED01493F
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:02d976f1ed01493f72fb104c4224a2317b6a211ea5d88d288550abb85fe93611
    MAN_03E8B237E962C1D2:
      id: MAN_03E8B237E962C1D2
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:03e8b237e962c1d2ded1178a8a856c9a8f05fa2f554080f72e5640a75e8bf73e
    MAN_045719AC8992819E--045719ac8992:
      id: MAN_045719AC8992819E--045719ac8992
      generated_at_utc: '2026-07-17T05:51:19.977994Z'
      content_hash: sha256:045719ac8992819ee4aa2c0cf45f413f6505672b5cb8cf8c76683dfdab0c8492
    MAN_083368964C7623C0:
      id: MAN_083368964C7623C0
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:083368964c7623c00bfaf93f1479ca2edacd56be42c734756ec078cd57dee064
    MAN_0BA66331CB4B2091:
      id: MAN_0BA66331CB4B2091
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:0ba66331cb4b20918d9576169959f9a3895937a70db3ead9651af998f7e47cc9
    MAN_0D9E79AEB44B7510:
      id: MAN_0D9E79AEB44B7510
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:0d9e79aeb44b7510ce5ee4e104044aeede91e05c93347751fa947026b35c616a
    MAN_0F2C1ABA8AF5C15E:
      id: MAN_0F2C1ABA8AF5C15E
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:8e637ce17c0ce4dad505a8ee948a1df3424d2623d4b863c685520a3f58cd3ff2
    MAN_1115E878B4F50CF3:
      id: MAN_1115E878B4F50CF3
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:1115e878b4f50cf36f15d4ead1bd50ea131bde28efdf9a461c7e207a8984bd76
    MAN_147EECDC5DAB119D:
      id: MAN_147EECDC5DAB119D
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:30f13451355242b47168727a5b17e53ed0bc18240446ac065f3b8ba4b75ef811
    MAN_18C5488E8D09D6D2--18c5488e8d09:
      id: MAN_18C5488E8D09D6D2--18c5488e8d09
      generated_at_utc: '2026-07-17T05:51:19.977994Z'
      content_hash: sha256:18c5488e8d09d6d235e2eeaec354ae6f3da3e3da0adcb25df2a54de4d79ed752
    MAN_1EFA395D2832F95E:
      id: MAN_1EFA395D2832F95E
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:1efa395d2832f95e4f5fcbcffe3d54ff5c2f016f77f317ffbb582b6f0f42aaa2
    MAN_20A10178D28B400B:
      id: MAN_20A10178D28B400B
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:20a10178d28b400be0dea7081db5fc3fb17a2fba31e8b7e593c977436359511e
    MAN_23E25F7C4136339F:
      id: MAN_23E25F7C4136339F
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:23e25f7c4136339fc233a376594c3e51adbc670feb4e07f06388abcb1a9fbe72
    MAN_2421026C912D8F9E--2421026c912d:
      id: MAN_2421026C912D8F9E--2421026c912d
      generated_at_utc: '2026-07-17T05:51:19.977994Z'
      content_hash: sha256:2421026c912d8f9ec305c5e9751f0d1163b29ca9fe10d9174b6eee31c9ffceb9
    MAN_254F60FBFDA7A2BB:
      id: MAN_254F60FBFDA7A2BB
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:254f60fbfda7a2bb6fc59f9a7e57c7bc0e2156bdb128297d07e503c9ed2ec6af
    MAN_25CD94348F7360E1:
      id: MAN_25CD94348F7360E1
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:25cd94348f7360e150dc548a260da0605fcd58b66138e98b2c44ff75e6a1f7c6
    MAN_330C0628475E2900:
      id: MAN_330C0628475E2900
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:330c0628475e2900e27001852e2e2d51f47e6f6667c807d5f1a6e80b28d0151a
    MAN_35AF4698AC57ED3F--35af4698ac57:
      id: MAN_35AF4698AC57ED3F--35af4698ac57
      generated_at_utc: '2026-07-17T05:51:19.977994Z'
      content_hash: sha256:35af4698ac57ed3fbd4027d53da28632f649d4584832089f17a1313728568044
    MAN_362BD9184BA2B5C7:
      id: MAN_362BD9184BA2B5C7
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:362bd9184ba2b5c77e3102308a1858a8648220941282fef709ab2610e4490bdb
    MAN_37A8B25C745F91BB--37a8b25c745f:
      id: MAN_37A8B25C745F91BB--37a8b25c745f
      generated_at_utc: '2026-07-17T05:51:19.977994Z'
      content_hash: sha256:37a8b25c745f91bb349251c3710ce01ee8039de65c5ab602e13188c8f1d5d1df
    MAN_392816F25BD330A2:
      id: MAN_392816F25BD330A2
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:392816f25bd330a2b56467326a64e62e3fac1facf59a1a5b96c34a73901b9e82
    MAN_39C5F1849EB3A736:
      id: MAN_39C5F1849EB3A736
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:39c5f1849eb3a736f911044c97e17681db8edb9ecd3a8e363ecdaa8d8c5cf788
    MAN_43BBCE48C452BDDD:
      id: MAN_43BBCE48C452BDDD
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:43bbce48c452bddd06147e2192897e4fc4a09fa385581fb17623e8ebffabded5
    MAN_44D6BD8077F837B5:
      id: MAN_44D6BD8077F837B5
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:44d6bd8077f837b59f4b7446204b778b7317b21c8005c20d9ac23e0747df9c40
    MAN_45A2B6F5ADF14C3F:
      id: MAN_45A2B6F5ADF14C3F
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:45a2b6f5adf14c3f7b93136e2c9e0ed6dbd68a1be6c97d8f268a59cec40e51d1
    MAN_48B52042FE3DEA4C--48b52042fe3d:
      id: MAN_48B52042FE3DEA4C--48b52042fe3d
      generated_at_utc: '2026-07-17T05:51:19.977994Z'
      content_hash: sha256:48b52042fe3dea4c79cdb23586ab2f4ba57bdd843a4d6ce78e97b56d366a929a
    MAN_494CD34A8C11734B:
      id: MAN_494CD34A8C11734B
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:494cd34a8c11734bc9db34798547df8cc2c5b29ece8550029b5748c09ada116a
    MAN_4C50AA2793AB7713:
      id: MAN_4C50AA2793AB7713
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:4c50aa2793ab77139ef13b2b4a4f37b26f6d5834f8f175d9bf2af1c1a6222d67
    MAN_524B615D8F9A7E12:
      id: MAN_524B615D8F9A7E12
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:524b615d8f9a7e1244839aa157afec4239cedd15f1b943f88820252fdf625eb1
    MAN_5378890AE3F832EE--5378890ae3f8:
      id: MAN_5378890AE3F832EE--5378890ae3f8
      generated_at_utc: '2026-07-17T05:51:19.977994Z'
      content_hash: sha256:5378890ae3f832eead485266d95bb504a616b5ba643e14ecaf3b4ff2d78a677c
    MAN_58936D050A8879DE:
      id: MAN_58936D050A8879DE
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:58936d050a8879deb833d1f0c26fd82f6c34633567c82a71e42be27d416f55ce
    MAN_5B2667DFDCB4EB31:
      id: MAN_5B2667DFDCB4EB31
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:61cb0a48e7b670defc81b89b80d5581ec43033a0f92fbaf3d5455e52694ec5f1
    MAN_5B4118BF4C21F770:
      id: MAN_5B4118BF4C21F770
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:5b4118bf4c21f7706bc594975201f277d04ee8ddcd6b25776ae13c9441ab5d10
    MAN_5F5865EF1A8D5904:
      id: MAN_5F5865EF1A8D5904
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:5f5865ef1a8d5904288de6b5062ee6d1e7fb74125ddf77ba8807847569a6d951
    MAN_6038BC183A1CE6BF:
      id: MAN_6038BC183A1CE6BF
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:6038bc183a1ce6bf1f011017b47094e84ad9e4c0bfc10e39d8976a6d72800493
    MAN_67ECA3FB50D80BAF:
      id: MAN_67ECA3FB50D80BAF
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:67eca3fb50d80bafa77df16282f3438f9c9c4920b7fd07decae94b227fe61da6
    MAN_6998D4E70F807B13:
      id: MAN_6998D4E70F807B13
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:6998d4e70f807b1346ca12410e36102afece3730fa03bdccb9dd4be8b2b6259e
    MAN_6B7EED8E43FDD1BA:
      id: MAN_6B7EED8E43FDD1BA
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:6b7eed8e43fdd1baacff9af9940105f4955ac0d16ac86e722e3c31fce38962d3
    MAN_6D665164162723C5--6d6651641627:
      id: MAN_6D665164162723C5--6d6651641627
      generated_at_utc: '2026-07-17T05:51:19.977994Z'
      content_hash: sha256:6d665164162723c5927f1e69624afc5e14e7a2f8dba1118fc63496a505136b1d
    MAN_6D77B363EA967C8F:
      id: MAN_6D77B363EA967C8F
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:6d77b363ea967c8f1ea1bde45c4f2da6a4e19c2305d3f82baf8852f485a3a55a
    MAN_6FA8F2D41D1B7062:
      id: MAN_6FA8F2D41D1B7062
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:6fa8f2d41d1b7062512f7ef14612d6d6594e7f36cb6ef236fbebd35f0c135f4b
    MAN_732160952277CD16:
      id: MAN_732160952277CD16
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:732160952277cd1606608f4af9b0045a9446a37910b8072a6cd154c5d3afdf4f
    MAN_73E054548B324267:
      id: MAN_73E054548B324267
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:73e054548b32426705dd168ebed070bc65b8221d91db2f3cd7c07cdc97c6b7ec
    MAN_794294DBD03CA974:
      id: MAN_794294DBD03CA974
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:d902d1f5fea87f82fb55ca1f8cde202501fd23595ec05f804e4b48f30a3c046b
    MAN_794294DBD03CA974--794294dbd03c:
      id: MAN_794294DBD03CA974--794294dbd03c
      generated_at_utc: '2026-07-17T05:51:19.977994Z'
      content_hash: sha256:794294dbd03ca974251a37571bebb81f309c66afce642709f6645806303fb1b3
    MAN_7C3C0347FD37CEB9:
      id: MAN_7C3C0347FD37CEB9
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:7c3c0347fd37ceb9c395aff447dca175e0ddb28fa6a8e4512ac456368e82130c
    MAN_8153E21BD727F6A0:
      id: MAN_8153E21BD727F6A0
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:8153e21bd727f6a08db324d60087d4e20d9872dfda7291879cd173ef3099205a
    MAN_81F4F1C3AD4F3217:
      id: MAN_81F4F1C3AD4F3217
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:81f4f1c3ad4f3217c876f96830d561edd132adfab97364419ef02c323122ce9b
    MAN_8609DB2EE85AF88E:
      id: MAN_8609DB2EE85AF88E
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:8609db2ee85af88e75f0e70480a79070e6b311fae426664f6100a0b5c83248c4
    MAN_8812ADE8E360DB8F:
      id: MAN_8812ADE8E360DB8F
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:8812ade8e360db8f8860c3534585321d58461d8a1b01b3614f8e6d175e7d1ebf
    MAN_8D160F5D77EC235B:
      id: MAN_8D160F5D77EC235B
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:54210d6fff8e0fa3f43acdedb25432b12ed74ba277b19e28044dbcc7eab2fd73
    MAN_8DB0AB4E3B90CB50:
      id: MAN_8DB0AB4E3B90CB50
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:99f05e99e18ffad35d1d63c465b8a287c3b1b72137aa0cea75a07abcaa19a942
    MAN_8DB0AB4E3B90CB50--8db0ab4e3b90:
      id: MAN_8DB0AB4E3B90CB50--8db0ab4e3b90
      generated_at_utc: '2026-07-17T05:51:19.977994Z'
      content_hash: sha256:8db0ab4e3b90cb5034fa16053963c87b696afd01c42ca53f05b3f82f4a75bf18
    MAN_9452D425539B8023:
      id: MAN_9452D425539B8023
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:9452d425539b802321ed45714ff13d6c1fd7bedd7ab201adab57f734dcbf8d04
    MAN_95930C2D369C878D:
      id: MAN_95930C2D369C878D
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:95930c2d369c878df9727170ea77dede88f30b28d88f4134d230836b09c56ffd
    MAN_968D07C7039689E5:
      id: MAN_968D07C7039689E5
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:968d07c7039689e56f444d642d58d2627cf5570c9fb49d87d6174715532b082e
    MAN_9A17C8A141B47D41:
      id: MAN_9A17C8A141B47D41
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:9a17c8a141b47d41e255a725817feeef040f31bb4ee23a66a0388f3ddc3e29fe
    MAN_9BC94E6BD25C05E1:
      id: MAN_9BC94E6BD25C05E1
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:9bc94e6bd25c05e12b4495102575eb27a9d617116c52c0fe32bc96ccf6993130
    MAN_9E0C30E4205FB415:
      id: MAN_9E0C30E4205FB415
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:9e0c30e4205fb415e37882ebeeb276505c96311a3f6ea5e043d380fa4e7ffcce
    MAN_9E12AA9A59F1BBE9:
      id: MAN_9E12AA9A59F1BBE9
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:9e12aa9a59f1bbe932067a7bea2f5fc6bb12af2006617ce2eead4b1f96df9d5e
    MAN_A1CD98CE32C423E4:
      id: MAN_A1CD98CE32C423E4
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:a1cd98ce32c423e4e842945e6b013cb6636ddeeb0d6d9c0c7a031027bdd1c896
    MAN_A58EA189B1C9E326:
      id: MAN_A58EA189B1C9E326
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:04b63d7158635ccef5d77f952c96a3da5f484a2709f71a077e6cb70248c668e0
    MAN_A5F4BA2371332A4E:
      id: MAN_A5F4BA2371332A4E
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:a5f4ba2371332a4e5ad6c94bd808ca1e5d12b3f4ebba27c6a38bce0993ea1676
    MAN_A67DCE77030808A6:
      id: MAN_A67DCE77030808A6
      generated_at_utc: '2026-07-17T05:51:19.977994Z'
      content_hash: sha256:a67dce77030808a6cdedab3615677b094ce676615691e2de52a6fb4b0db926a7
    MAN_AA8C115068BD5D76--aa8c115068bd:
      id: MAN_AA8C115068BD5D76--aa8c115068bd
      generated_at_utc: '2026-07-17T05:51:19.977994Z'
      content_hash: sha256:aa8c115068bd5d7652899e73145909343274a585413c093b42f7f32189eaf090
    MAN_AE68C41A115C80FC--ae68c41a115c:
      id: MAN_AE68C41A115C80FC--ae68c41a115c
      generated_at_utc: '2026-07-17T05:51:19.977994Z'
      content_hash: sha256:ae68c41a115c80fc4017a217740267206206c6d203d671fee845b58442a6e922
    MAN_AE7C62637F29A4C9:
      id: MAN_AE7C62637F29A4C9
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:ae7c62637f29a4c902964bd59c569bbe3d477b2d56c84520b8c8c2b95efcbd36
    MAN_AF1D093225F75E82:
      id: MAN_AF1D093225F75E82
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:af1d093225f75e82ca0aa65cd8a7665ef9c04e7e9e605b0ba70a468bd1912a09
    MAN_B121E5340A1BEFEE:
      id: MAN_B121E5340A1BEFEE
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:b121e5340a1befee27d9cf92690b4f7e0255b871a8235f4fa5739aa1411a566f
    MAN_B1A8365C419E3164:
      id: MAN_B1A8365C419E3164
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:0f82bcd2e050e382f7d68a136dda8b3b92679a71cb1e05533aa8674c7a4edf6f
    MAN_B1A8365C419E3164--b1a8365c419e:
      id: MAN_B1A8365C419E3164--b1a8365c419e
      generated_at_utc: '2026-07-17T05:51:19.977994Z'
      content_hash: sha256:b1a8365c419e3164dc03060e2b7dc24203874a70076a8529e21fdbd338b522b1
    MAN_B4DD5B60F33FC5E3:
      id: MAN_B4DD5B60F33FC5E3
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:b4dd5b60f33fc5e3c397b06c861b0fa7ecd88690346a18883d63a901c71a3e7e
    MAN_B5E18528035F6F87:
      id: MAN_B5E18528035F6F87
      generated_at_utc: '2026-07-17T05:51:19.977994Z'
      content_hash: sha256:b5e18528035f6f870e341e70298511e7345c4884bd66257f3c095ba8b605ca69
    MAN_B9EE0F176B92F526:
      id: MAN_B9EE0F176B92F526
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:b9ee0f176b92f5264517943ccc498c1e148bbcd1f29beb393b4c55bb51dfffd9
    MAN_BC425C37C792DDEE:
      id: MAN_BC425C37C792DDEE
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:bc425c37c792ddeed419770e9b57b33fa41a0def670c961a7c66a8c0140561a4
    MAN_BE74B0D21973DAEC:
      id: MAN_BE74B0D21973DAEC
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:be74b0d21973daecfa7f765d37067b4f38de4207b0a1063e18f9cff01b73aa93
    MAN_BE929AB9651E5E66:
      id: MAN_BE929AB9651E5E66
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:be929ab9651e5e66a59780b20d2a800f62ea7b43b007b17615da59afb2cdd5b3
    MAN_C04F44BFF720877B:
      id: MAN_C04F44BFF720877B
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:c04f44bff720877baad3f8810d2814dd0fda9aef6ee6b15acc5f29f21bd3162f
    MAN_C467D6702AB64674:
      id: MAN_C467D6702AB64674
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:c467d6702ab646745acbc033419c24bcf3adba7e9de7c3bd5daab671fe46446e
    MAN_CAA0FFEFF7C64A82:
      id: MAN_CAA0FFEFF7C64A82
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:caa0ffeff7c64a82bf218a9fb6d7c5dde87bcb41e8fb0795fc7bd39adf6f36ca
    MAN_CDD044CBEEED1A80:
      id: MAN_CDD044CBEEED1A80
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:cdd044cbeeed1a801200766b35b6ebaf72f44e1f281329942dbc71242f2525e5
    MAN_CDD195853C6DFE14:
      id: MAN_CDD195853C6DFE14
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:cdd195853c6dfe14718620f8892fbace0a9e23ca40f5e2ea0f799870b96b6b6d
    MAN_CEC45E0E1446E3DF:
      id: MAN_CEC45E0E1446E3DF
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:cec45e0e1446e3df175d83de317b062067cc1252be8ac188e2685182a8f20608
    MAN_D405972253EA086F:
      id: MAN_D405972253EA086F
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:d405972253ea086f3ed41a70328bf8f5f2b5a09a52c24d2a641223dcc95011e0
    MAN_D84D77F1C6E463F4:
      id: MAN_D84D77F1C6E463F4
      generated_at_utc: '2026-07-17T05:51:19.977994Z'
      content_hash: sha256:d84d77f1c6e463f4f4c3d85ef5c089b81c00e7507cda07eeb705c75bee97da05
    MAN_DA06B43ED3D9DBBC:
      id: MAN_DA06B43ED3D9DBBC
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:da06b43ed3d9dbbc3baa4d137c27c73d6d10ff2ca57f477db761b7b388b41eef
    MAN_DA93975DA79D34AD--da93975da79d:
      id: MAN_DA93975DA79D34AD--da93975da79d
      generated_at_utc: '2026-07-17T05:51:19.977994Z'
      content_hash: sha256:da93975da79d34add410b3d856d570f7ed0b241558c683ba8f06e3511488bbae
    MAN_DADCFA23F461FBBF:
      id: MAN_DADCFA23F461FBBF
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:dadcfa23f461fbbf9a88ff1f9b10e85b6e1e7dac4e37ca8986fc8e414a12fa89
    MAN_DBD043A36C2E4926:
      id: MAN_DBD043A36C2E4926
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:dbd043a36c2e49265a5f003845c9cba0735aecd507d79dc7f57a70407e8d70da
    MAN_DC37B979EC91203E:
      id: MAN_DC37B979EC91203E
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:dc37b979ec91203e49046191ce1118b342990dd607cfaae4e6498dd222fb4869
    MAN_DD6D48EB9B80CB6B:
      id: MAN_DD6D48EB9B80CB6B
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:dd6d48eb9b80cb6b2d5fe9d47fc4810243c093bd9b8659332800977b9a134923
    MAN_DD8A18DB0BF6E8A9:
      id: MAN_DD8A18DB0BF6E8A9
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:dd8a18db0bf6e8a9df4e19403f6d40f6d4028bb331dc3c61bc496ea26ddacf38
    MAN_DE03A6A5B1731AF7--de03a6a5b173:
      id: MAN_DE03A6A5B1731AF7--de03a6a5b173
      generated_at_utc: '2026-07-17T05:51:19.977994Z'
      content_hash: sha256:de03a6a5b1731af7337b6fe64330f8a02f628f42dd87260aa00bf3c01e843fb6
    MAN_DFDB86CEA63B78D3--dfdb86cea63b:
      id: MAN_DFDB86CEA63B78D3--dfdb86cea63b
      generated_at_utc: '2026-07-17T05:51:19.977994Z'
      content_hash: sha256:dfdb86cea63b78d3cb728258ccdd4e501fa440f02735ef246d17fdbc5044d250
    MAN_E116073D3FDB5C1F:
      id: MAN_E116073D3FDB5C1F
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:5df89d10ec7725763781bc99e8b4d943a9e940b617f483ab009dffdc01a15907
    MAN_E32B6349055FCEF9:
      id: MAN_E32B6349055FCEF9
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:e32b6349055fcef9e6437dc8e1eaf495d3d56f10b316987a403c37553056a544
    MAN_E99D067CF243EEE8:
      id: MAN_E99D067CF243EEE8
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:e99d067cf243eee89be17d52596c12b3fc5286b1f5d8c8481a26cafeeff1a239
    MAN_EA69373DAD6B5B01:
      id: MAN_EA69373DAD6B5B01
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:ea69373dad6b5b01efa066131eae0c26137143575cc80c1f62c733bb373d255c
    MAN_EDB775C51FCEA404:
      id: MAN_EDB775C51FCEA404
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:edb775c51fcea404016cb3f6da328eef236bf5d00a21db4c724aeb77a38e9509
    MAN_EFBA9CA2760DA6B8:
      id: MAN_EFBA9CA2760DA6B8
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:efba9ca2760da6b8da59e494c821bf6f038bb5c311b7214f2f4e492ffd37d106
    MAN_F12635B7646C0E9B:
      id: MAN_F12635B7646C0E9B
      generated_at_utc: '2026-07-17T05:51:19.977994Z'
      content_hash: sha256:f12635b7646c0e9b485e01b3c148fcd3945e9b6b1478945f19d54cfea262d9a6
    MAN_F6CB9D32040E99BA:
      id: MAN_F6CB9D32040E99BA
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:f6cb9d32040e99ba94bc763eb811bd6525692b756fc3d04af406dcbe6c69a122
    MAN_F84F01B63ABC178D:
      id: MAN_F84F01B63ABC178D
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:f84f01b63abc178d1fe5bc1fa49113ceabd5237e70e1ce2ad10aa7debb586f7a
    MAN_FD5BF4CD3984BECF:
      id: MAN_FD5BF4CD3984BECF
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:fd5bf4cd3984becf55d9ca41296368832467ab7133e075ca462dc2f7053f0e61
    MAN_FDD174E970AC7930:
      id: MAN_FDD174E970AC7930
      generated_at_utc: '2026-07-17T05:18:12.210893Z'
      content_hash: sha256:fdd174e970ac79301953bdd92e44970778a716c86428b4b554bcd57d2a2c4f6a
    LTP_74BB3F96CBA52D02:
      id: LTP_74BB3F96CBA52D02
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:74bb3f96cba52d02850ad3c5e54c87acf278ce51290c99d5ae29da583be9ba38
    LTP_6C14DE68E3C0CC24:
      id: LTP_6C14DE68E3C0CC24
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:6c14de68e3c0cc24bbb7021cd805e26a73df65653f350d8fa8ed8de5232949e8
    LTP_D246498B20D9CB2C:
      id: LTP_D246498B20D9CB2C
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:d246498b20d9cb2cd6ece54014a50e1c77fa08b6a598251c2dc0e3a3700193e2
    LTP_04236FD5B061DEB9:
      id: LTP_04236FD5B061DEB9
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:04236fd5b061deb91a99cc5990d76abb4d0305312af10adf6221c7cdbcf28567
    LTP_21FCBFC328D1815A:
      id: LTP_21FCBFC328D1815A
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:21fcbfc328d1815aad1c1fd20c4797e91d64cad63f8c4dd02b3340c29fc06412
    LTP_38432B154B641410:
      id: LTP_38432B154B641410
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:38432b154b641410365b7f4a7ad2ca324c3c356bf93948d3c948552a39f1f368
    LTP_43728156B00FF104:
      id: LTP_43728156B00FF104
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:43728156b00ff104889586e9f9c3c97e3681823265c64387f32a84c300f8aebb
    LTP_58C8C307B1FF2510:
      id: LTP_58C8C307B1FF2510
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:58c8c307b1ff25100a989b73841bba45b1dcf61406863df2f8b8bfce4c294f2e
    LTP_6F4B3A38B8BF4C7E:
      id: LTP_6F4B3A38B8BF4C7E
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:6f4b3a38b8bf4c7e714c705e096b38742f0d55e11af069efd85a780cbd567c0f
    LTP_6F77CAA9FC4423BA:
      id: LTP_6F77CAA9FC4423BA
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:6f77caa9fc4423ba48f8bccdc757c34ac19acb29a8df9d9089f395904ee88d54
    LTP_71DD72481EF5740E:
      id: LTP_71DD72481EF5740E
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:71dd72481ef5740e84d8f583e4c75aa6d22288a996d96ab3f4c50bef33fc2b5b
    LTP_86144BF50FB25D3A:
      id: LTP_86144BF50FB25D3A
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:86144bf50fb25d3a419e3c011f5c2334e4885d5643718a54ea7d6d0d3e8b4bab
    LTP_B0433B78A1641F24:
      id: LTP_B0433B78A1641F24
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:b0433b78a1641f2478404ccbec3a8cad14d0a94ee86936a6d26460330ce10de8
    LTP_D254EE40E8B5957E:
      id: LTP_D254EE40E8B5957E
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:d254ee40e8b5957eb45b944d458cd22c2b8bd611d8da6326448e10c63c65ed36
    LTP_DCC88B2C458969EA:
      id: LTP_DCC88B2C458969EA
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:dcc88b2c458969ead361273a98cbb21fb0bf32a05c20068c76ebabffd55bf579
    LTP_DDA854712C50CD6A:
      id: LTP_DDA854712C50CD6A
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:dda854712c50cd6a2ea2a11371b97c4eee905e31d70b389262238b10091fa2c9
    LTP_6B9F97B897EC5C32:
      id: LTP_6B9F97B897EC5C32
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:6b9f97b897ec5c326f9f68e26e9353a0e9bcb1ca59ce6f15c338328a7d201bda
    LTP_C8376BC347F94A98:
      id: LTP_C8376BC347F94A98
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:c8376bc347f94a984bf5b3e6cf3baa97d7f384dde2c141d2a0a70d0693aa589d
    LTP_287CF10D893735AB:
      id: LTP_287CF10D893735AB
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:287cf10d893735aba939172ccbac5cf025dd704d8272d5048fb79e3f211821c3
    LTP_82A8802A27A3D2BF:
      id: LTP_82A8802A27A3D2BF
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:82a8802a27a3d2bf01cb995752e7667b482979d9e93565f11e732bb2a5a31b28
    LTP_2F3E34FD672DBF34:
      id: LTP_2F3E34FD672DBF34
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:2f3e34fd672dbf34b28611337f295a687ae0db9f5a34edb98b0cb1a9b82235f2
    LTP_4494B70BBA693D42:
      id: LTP_4494B70BBA693D42
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:4494b70bba693d42cda9d0a59c88ea7d9d8bd0fcb3276d8a3fc52fa386e7ef78
    LTP_614C018F61C078A0:
      id: LTP_614C018F61C078A0
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:614c018f61c078a0c1629bf12f259ab3108460b39da9611587eb8ab0f96a9017
    LTP_7B0F966046AECA7E:
      id: LTP_7B0F966046AECA7E
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:7b0f966046aeca7e7a0ddc40b2774c29247dbabb79174568412a4d08596db153
    LTP_9C2FB7732A0B90B6:
      id: LTP_9C2FB7732A0B90B6
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:9c2fb7732a0b90b68e056c2337aa1e81e2e609b6ad6c60d53dadf2893b11554b
    LTP_A2934B80997B62C9:
      id: LTP_A2934B80997B62C9
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:a2934b80997b62c96c7d18d8295c04e7ce45893f9122cfdb44bdfeb8070674ff
    LTP_AD3A4B98FF201ABE:
      id: LTP_AD3A4B98FF201ABE
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:ad3a4b98ff201abe4bafe39d5fede2f4d497cf03a7d50837c4c7441c515b34fa
    LTP_C13C4F63D58904BC:
      id: LTP_C13C4F63D58904BC
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:c13c4f63d58904bcee6e68546c3fda582209001fe4c9e4e9a46eaf6a25719cfd
    LTP_C24E55F06625D564:
      id: LTP_C24E55F06625D564
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:c24e55f06625d564c76dd85c6f1bb8c94b1270cb6e0d83790b02371b7f8fc397
    LTP_D1A18560E485E146:
      id: LTP_D1A18560E485E146
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:d1a18560e485e146f23212528bc3caba854e266e4bd431c7605891935860d811
    LTP_DA64FD04E43656E6:
      id: LTP_DA64FD04E43656E6
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:da64fd04e43656e65129d77e5bf6b393319bb248852a3a6db4431783ebad5bcd
    LTP_DF5B725563FDFB31:
      id: LTP_DF5B725563FDFB31
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:df5b725563fdfb318278bc71aa9ae5ffd772ac4f05dbd9b4f118bd9df7339f3c
    LTP_ECD986F27CF15E1E:
      id: LTP_ECD986F27CF15E1E
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:ecd986f27cf15e1e145501e0755a1420d46a42ce091e57d23884318e37849a39
    LTP_FC8BA85373EA2D8F:
      id: LTP_FC8BA85373EA2D8F
      generated_at_utc: '2026-07-16T07:55:00.843723Z'
      content_hash: sha256:fc8ba85373ea2d8f73d801b46060fd0ce0d4e78ef2f1ce6a5923118389112ce8
  static_checks:
    STARRY_CHROOT_PATH:
      id: STARRY_CHROOT_PATH
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:d817cdc66b7277273694b7530ca5444e592ae6dde4fe282e9706dab3bdb7a88b
    STARRY_CLOSE_BAD_FD_ERRNO:
      id: STARRY_CLOSE_BAD_FD_ERRNO
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:3688bede607dda3b8566d02b28e631d99e656c165ca17f247810585f6e6e9d20
    STARRY_CLOSE_FD_TABLE:
      id: STARRY_CLOSE_FD_TABLE
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:22b2aabe82905f32747892948a313452c321a5bd727a48114ab60cd9f4a7d6e0
    STARRY_CLOSE_RANGE_SWEEP:
      id: STARRY_CLOSE_RANGE_SWEEP
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:b68d84ae1e356355d2ed2f947873f1661d2acef90e75d240829ff1dc62e95ee1
    STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS:
      id: STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:270f978e69107ec932a985c1cda9d40c23fba71e749ab30fb936feed963a9796
    STARRY_CLOSE_RANGE_VALIDATION:
      id: STARRY_CLOSE_RANGE_VALIDATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:647d3cf0fdb66dd12325ecc9b2512573246e8b70f4d3e76fc3825008fdc13954
    STARRY_CLOSE_SYSCALL:
      id: STARRY_CLOSE_SYSCALL
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:098456e0db6f88a9696e9be3f748f7fc3466e747ab9c3fad713e7832f944dec5
    STARRY_CONNECT_ADDRESS_VALIDATION:
      id: STARRY_CONNECT_ADDRESS_VALIDATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:d1a6e8339cfa112a4c240e163ec01b885aeed46f5ed1e6de3c715e6445ab0c97
    STARRY_CONNECT_ENTRY:
      id: STARRY_CONNECT_ENTRY
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:a483667d4879cf3e66ee135e8a55e72ce34396420812383649fd6fed8fead5d1
    STARRY_COPY_FILE_RANGE_CORE:
      id: STARRY_COPY_FILE_RANGE_CORE
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:d3fbeb11a1f0facf48e7447c38ff2b0dcf2c0cbee77889fe5c05cf30698792ca
    STARRY_DUP2_DUP3_BEHAVIOR:
      id: STARRY_DUP2_DUP3_BEHAVIOR
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:1814d475d47e2ee693e7440a774842a99ea7bf197f5d0f5a5f38fdf65c455971
    STARRY_DUP_BEHAVIOR:
      id: STARRY_DUP_BEHAVIOR
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:10d750a4976d0be8353dcbddf7c80e88682a6c8012c7df7aad87423595f1a3f5
    STARRY_EPOLL_CREATE1_FLAGS:
      id: STARRY_EPOLL_CREATE1_FLAGS
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:f2163883a6167eb0dfabb0b48c02cb981e4bb14c6730811e0b3348a4de8ead23
    STARRY_EPOLL_CTL_ENTRY:
      id: STARRY_EPOLL_CTL_ENTRY
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:5e9c5d89216a0956603db791f7735b1ba18813e00b42e81c3a16292fbd905162
    STARRY_EPOLL_CTL_INTEREST:
      id: STARRY_EPOLL_CTL_INTEREST
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:432cd717a72ab0632dad3d1b2702aa43469400853a917d4562a935466ea2fb7a
    STARRY_EPOLL_FACCESS_ERRNO:
      id: STARRY_EPOLL_FACCESS_ERRNO
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:e22921f6310fd12312f5a9094c1b2a7fbfa561ff1c45b5d2578d6e4736cb6a79
    STARRY_EPOLL_FD_LOOKUP:
      id: STARRY_EPOLL_FD_LOOKUP
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:189e42bb88fc505c6fe33c7531efb1b30f99aa83aeba33ae39f4362fefc41f46
    STARRY_EPOLL_NESTED_LOOP:
      id: STARRY_EPOLL_NESTED_LOOP
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:a051a74deeaa59fdca6eed7d45ab359ade23a502ffa8d19b6f3de98cb94765ce
    STARRY_ERRNO_TRANSLATION:
      id: STARRY_ERRNO_TRANSLATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:8d9a60adf231f913f00d0778fd209ab68edadef24ab77fdf68d527374a9163c5
    STARRY_EXECVEAT_FACCESSAT_RESOLVE:
      id: STARRY_EXECVEAT_FACCESSAT_RESOLVE
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:b23f34dc7191754d8e39d5c6a62dd40508f1a505de85e96ecbbf63673c9616dc
    STARRY_EXECVEAT_VALIDATION:
      id: STARRY_EXECVEAT_VALIDATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:c76c2cd9e97731a525b77e7c46779eb948ec5d57a2e685f43d66d575e8f35b50
    STARRY_FACCESSAT2_VALIDATION:
      id: STARRY_FACCESSAT2_VALIDATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:2a7c3ad920d88352ba2c16849143d93f64f6da0d95a67ce6f1a8d260c6080d0c
    STARRY_FCHDIR_CORE:
      id: STARRY_FCHDIR_CORE
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:6efabd8ab5037dfcabf4998c5ca0727afbfe837cf43acd4bcc0b0eefafd806eb
    STARRY_FCHDIR_ERRNO_TRANSLATION:
      id: STARRY_FCHDIR_ERRNO_TRANSLATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:fd177e9b3e1499c807d22c42b2ae346718855fa428f5302aa43ecb67b1bd2997
    STARRY_FCHDIR_FD_VALIDATION:
      id: STARRY_FCHDIR_FD_VALIDATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:17cf5cd7e876370fda3b89a496c7c087f3827da61a2ee056193ef8401fa1f628
    STARRY_FCHMODAT_FLAG_VALIDATION:
      id: STARRY_FCHMODAT_FLAG_VALIDATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:2759b18590554a478af9dd86da5c27e91a163b2987208be937592264c83cfc0f
    STARRY_FD_TABLE_LOOKUP_ALLOCATION:
      id: STARRY_FD_TABLE_LOOKUP_ALLOCATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:4bd01e5c33cabcf5458b72c9f3e8863f6e7ce37a1db5127e622bcec36267a2f4
    STARRY_FINAL_ERRNO_TRANSLATION:
      id: STARRY_FINAL_ERRNO_TRANSLATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:7335ab25a23d7920d554be244a3f02fe0be4dfd16f61ffbf3a9de5993cadf0c2
    STARRY_FINAL_SYSINFO_COPYOUT:
      id: STARRY_FINAL_SYSINFO_COPYOUT
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:fabeb1b90d63733c74800db189e3cf309f7823290add2421d37f2965f13ad0d1
    STARRY_FINAL_TIMER_DELETE:
      id: STARRY_FINAL_TIMER_DELETE
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:e300264bee85147a9a5d2ec81a6280444803b96d858336c30600080c40ee820c
    STARRY_FINAL_TKILL_TID_VALIDATION:
      id: STARRY_FINAL_TKILL_TID_VALIDATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:1355e02217d5f3bd03fbb329a928015dcd367ceea991d8e160b1f501c50ad7f7
    STARRY_FINAL_UNAME_COPYOUT:
      id: STARRY_FINAL_UNAME_COPYOUT
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:22d2b44a9c168414e9c99d02e3f91db41a61f6023a3a8bb46c64b03e039630e4
    STARRY_FINAL_UNSHARE_FILES:
      id: STARRY_FINAL_UNSHARE_FILES
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:59906058d6dd4abe0669d7409fb79dc5e2851be551e778dc1d477000e21000fa
    STARRY_FINAL_UNSHARE_FLAG_VALIDATION:
      id: STARRY_FINAL_UNSHARE_FLAG_VALIDATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:c7ffaed34db719fbbb9d362ab17ab42a6a7b58f629b2073e8ff81c9f7a0676b3
    STARRY_FINAL_WAITID_OPTIONS:
      id: STARRY_FINAL_WAITID_OPTIONS
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:eaa39e7dda1d0fd8b5bf474137b06c8d05da3caa7736e3fc4521731d28b8802f
    STARRY_FINAL_WAITPID_INT_MIN:
      id: STARRY_FINAL_WAITPID_INT_MIN
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:6439677bbe44b634d0b03458f4f3d5a766778eb4c754fede279254e996de77a8
    STARRY_FINIT_MODULE_FLAG_VALIDATION:
      id: STARRY_FINIT_MODULE_FLAG_VALIDATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:02b5ac507da07f65ee1eb468d782446b05ce6455a8e57c5e7132becd2c08cd07
    STARRY_MAN_CLOCK_GETRES_VALIDATION:
      id: STARRY_MAN_CLOCK_GETRES_VALIDATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:39c59823deb4fa50619416109c4e60818a95fd08b7e778004ad4dad25a46b1f5
    STARRY_MAN_CLOCK_GETTIME_VALIDATION:
      id: STARRY_MAN_CLOCK_GETTIME_VALIDATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:2227be48f5b4c7498f1f70ee087020f5f3633478d37994e1ce95be353b554be3
    STARRY_MAN_EVENTFD2_VALIDATION:
      id: STARRY_MAN_EVENTFD2_VALIDATION
      generated_at_utc: '2026-07-17T07:32:33.916128Z'
      content_hash: sha256:13648156878333adeb78204595c0199fd5930f1b57a0d9dfdbcad2b1a6d2ca3e
    STARRY_MAN_GETRANDOM_ARGUMENTS:
      id: STARRY_MAN_GETRANDOM_ARGUMENTS
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:c89ce496ae2155da99e328b9ec02e93addb69b9a9502d311b71f8a9541cee940
    STARRY_MAN_INOTIFY_ADD_WATCH_INPUTS:
      id: STARRY_MAN_INOTIFY_ADD_WATCH_INPUTS
      generated_at_utc: '2026-07-17T07:32:33.916128Z'
      content_hash: sha256:e5babd6cb6f55f3c084963bd21bb306a9a5fa7223fac9726e0c46f44d93f0b9b
    STARRY_MAN_INOTIFY_INIT1_VALIDATION:
      id: STARRY_MAN_INOTIFY_INIT1_VALIDATION
      generated_at_utc: '2026-07-17T07:32:33.916128Z'
      content_hash: sha256:9b3a7ef6d751aaa85559093ba95e658d18f1fdd232b1fdbc1f2d84250f0ba95a
    STARRY_MAN_INOTIFY_RM_WATCH_ID:
      id: STARRY_MAN_INOTIFY_RM_WATCH_ID
      generated_at_utc: '2026-07-17T08:16:17.470765Z'
      content_hash: sha256:eac5c811986b666a85919e0302a8e6bc2ea53016811b0c0c768a0d2ab99766eb
    STARRY_MAN_INOTIFY_RM_WATCH_INPUTS:
      id: STARRY_MAN_INOTIFY_RM_WATCH_INPUTS
      generated_at_utc: '2026-07-17T08:16:17.470765Z'
      content_hash: sha256:939271cdff41f8344d41706444ac2a4e8c48062080fa87d555f25e4881586e43
    STARRY_MAN_LISTEN_ENTRY:
      id: STARRY_MAN_LISTEN_ENTRY
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:d03fc9ce42dbb6f8111aaeed4ff4d3090bce65717c6af1899ee061d117b99fe8
    STARRY_MAN_MEMFD_CREATE_VALIDATION:
      id: STARRY_MAN_MEMFD_CREATE_VALIDATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:c843b6e0726c72d7600bc65a6579dd95147bd9b64076f3f52b63ce54ea4657e3
    STARRY_MAN_PIPE2_VALIDATION:
      id: STARRY_MAN_PIPE2_VALIDATION
      generated_at_utc: '2026-07-17T07:32:33.916128Z'
      content_hash: sha256:2fc1688a6ae9ee7d6731e73add9ed7573d7b415b42590e62f79528c408203b55
    STARRY_MAN_REBOOT_VALIDATION:
      id: STARRY_MAN_REBOOT_VALIDATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:9c70a80c009a123b465beea168b4d650d2c9682e7e0ab8ed3ea5d14bcc0aec21
    STARRY_MAN_SECCOMP_OPERATION_FLAGS:
      id: STARRY_MAN_SECCOMP_OPERATION_FLAGS
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:cc9f481eda67f62b6c703372757260c6ff47317ecc46e7c673b798e07782450a
    STARRY_MAN_SECCOMP_VALIDATION:
      id: STARRY_MAN_SECCOMP_VALIDATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:b30946bfc14afca77aa8e610940bc9b4d739d445bf7544888fc20ccf984b876d
    STARRY_MAN_SETDOMAINNAME_ARGUMENTS:
      id: STARRY_MAN_SETDOMAINNAME_ARGUMENTS
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:52bc1e1519f29f80288fb07e135041049fc219b2dcf53f005b0863d9ef17274b
    STARRY_MAN_SETGROUPS_VALIDATION:
      id: STARRY_MAN_SETGROUPS_VALIDATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:8b357dc37a9d23de00b426bc321759a943306e872ec60c3b97b8aa23056d0da2
    STARRY_MAN_SETHOSTNAME_ARGUMENTS:
      id: STARRY_MAN_SETHOSTNAME_ARGUMENTS
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:63ebc4b591412322c7889cc69d118adda45f6e88d266c2033b70cd8073dc2491
    STARRY_MAN_SHUTDOWN_VALIDATION:
      id: STARRY_MAN_SHUTDOWN_VALIDATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:5aeedd7b1f0f02eb2e287c818f73ac61c922daf53a3010d1e56b650a16a21727
    STARRY_MAN_SOCKETPAIR_VALIDATION:
      id: STARRY_MAN_SOCKETPAIR_VALIDATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:98095b1d4f8be3ca5cce69a464e5708fa401b465c44ab29f31bc172d2f331130
    STARRY_MMAP_ACCESS:
      id: STARRY_MMAP_ACCESS
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:de1c0d707169e1e81d3b24bdfbb470fc9fc179213b603ca9e2e5010423b67af5
    STARRY_MMAP_ARGUMENTS:
      id: STARRY_MMAP_ARGUMENTS
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:e83e60fea871601e0384c76e576ddbeee45210d9ff13fd84c816d7ad7dc8a560
    STARRY_MMAP_FD:
      id: STARRY_MMAP_FD
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:399a5e6488d63e6e7906840fb0cbf3a7b57b7e4cb22564bd069ee535cd09c703
    STARRY_ROUND2_CLOSE_FD_TABLE:
      id: STARRY_ROUND2_CLOSE_FD_TABLE
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:f66aba3c652105df45d6cf102d1672da083636ee12d2d3ff019789aacca6bcc1
    STARRY_ROUND2_CLOSE_SYSCALL:
      id: STARRY_ROUND2_CLOSE_SYSCALL
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:d6e7f46d631f54cfbf8c53286c0eff767bfe8fbf9a94d0cecb16ecbbaadd539e
    STARRY_ROUND2_ERRNO_TRANSLATION:
      id: STARRY_ROUND2_ERRNO_TRANSLATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:44ca1b0e564fb100d4d632b7265d3c7eef30d29f4eead5c61bbb4cab45769537
    STARRY_ROUND3_ERRNO_TRANSLATION:
      id: STARRY_ROUND3_ERRNO_TRANSLATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:092633b5bbc1d879cf72a97b889f5a99fa41814409197e21307f7c2e928a7b89
    STARRY_ROUND3_FSTATFS_ERRORS:
      id: STARRY_ROUND3_FSTATFS_ERRORS
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:543941f48be5bbb202d5f8e9e9d82b8243f945d28ac9db8d55d317c0d34dc66e
    STARRY_ROUND3_FSTAT_CORE:
      id: STARRY_ROUND3_FSTAT_CORE
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:4a7bba46fd86955a89f0f4e4bc2555c1da47362aa295e98efb19f48da45f9049
    STARRY_ROUND3_GETCWD:
      id: STARRY_ROUND3_GETCWD
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:73775de9aebd8a606e4826ecba2a252ab16e507cae2ee06832613491104e3c46
    STARRY_ROUND3_GETPRIORITY_SELECTOR:
      id: STARRY_ROUND3_GETPRIORITY_SELECTOR
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:21ca3db01eeb28f97c55cb10fa2109985843f45791eb95f17a7c1c6b1eb93986
    STARRY_ROUND3_GETRLIMIT_CORE:
      id: STARRY_ROUND3_GETRLIMIT_CORE
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:a566f3a65de9d400117cb9415d11a5efb0790d2aa508fcdecb94405c6c95b860
    STARRY_ROUND3_GETRLIMIT_DISPATCH:
      id: STARRY_ROUND3_GETRLIMIT_DISPATCH
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:2f1fc31793fe71bef62add5e3c56982d46bddf280f64357a7d67c57b61428047
    STARRY_ROUND3_JOB_ID_LOOKUP:
      id: STARRY_ROUND3_JOB_ID_LOOKUP
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:ac335083b4908572a3e23dd3e8a0f990d3a62ecbfc7cee0895a57893c140fa9e
    STARRY_ROUND3_PROCESS_LOOKUP:
      id: STARRY_ROUND3_PROCESS_LOOKUP
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:da4344fb0b2e8ee152e5d502fd04eb765733baedfbd263f5c95984051c740142
    STARRY_ROUND4_ERRNO_TRANSLATION:
      id: STARRY_ROUND4_ERRNO_TRANSLATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:9fc9e5adffd48e65065cfd90d7901d1df41a02fc010a735e3d354055346f85dd
    STARRY_ROUND4_MLOCK2_FLAGS:
      id: STARRY_ROUND4_MLOCK2_FLAGS
      generated_at_utc: '2026-07-17T07:32:33.916128Z'
      content_hash: sha256:451a3c92dd203c594502317904dcedea1b74620e1a9db5c2781345b07c969248
    STARRY_ROUND4_MSYNC_EXCLUSIVE_MODES:
      id: STARRY_ROUND4_MSYNC_EXCLUSIVE_MODES
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:0578df5fcb3eef561e0d51077bf4724c55f01d277361849b03e0516478f3a30a
    STARRY_ROUND4_MSYNC_UNKNOWN_FLAGS:
      id: STARRY_ROUND4_MSYNC_UNKNOWN_FLAGS
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:48ef4ae8f5622bf555efb372cbc0025bdf4ab5eb9bc9470b622c68467836e765
    STARRY_ROUND4_MUNMAP_ZERO_LENGTH:
      id: STARRY_ROUND4_MUNMAP_ZERO_LENGTH
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:179cf3a1ea372121ce5d29a1eff7cfc0861ea7bf93a78a20c0c280a972aecec3
    STARRY_ROUND4_OPENAT2_SIZE:
      id: STARRY_ROUND4_OPENAT2_SIZE
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:90f4395e66b3445c53574857329bfff21977ce31e516f2429b262fd66af5b056
    STARRY_ROUND4_PIDFD_GETFD_FLAGS:
      id: STARRY_ROUND4_PIDFD_GETFD_FLAGS
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:92a764693b05210a48253bfc6a2737474f011b2b54aa329d8becd879a60494a5
    STARRY_ROUND4_PIDFD_OPEN_INPUTS:
      id: STARRY_ROUND4_PIDFD_OPEN_INPUTS
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:70ec2374f1dcd688c4fcbdc8ffafcc93af19190f7a10a8fb960c5339837f1c37
    STARRY_ROUND4_PIDFD_SIGNAL_FLAGS:
      id: STARRY_ROUND4_PIDFD_SIGNAL_FLAGS
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:c4a2f69143da820bc683c34f4d511374d5362c6d6f37c0d56dc44f198944d398
    STARRY_ROUND4_READ_BAD_FD:
      id: STARRY_ROUND4_READ_BAD_FD
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:06f24f5a120841e298f8a157ff0169342c935908ee1379dc8975d4b61ce55706
    STARRY_ROUND4_VECTOR_IO_FLAGS:
      id: STARRY_ROUND4_VECTOR_IO_FLAGS
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:2d911dc6bd53e6fc8a77a5209ebdc9e8f5bddfff56fde3f3715b7cc3832043a7
    STARRY_ROUND5_ERRNO_TRANSLATION:
      id: STARRY_ROUND5_ERRNO_TRANSLATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:546b5bc4454aed59688b0b8a987f0207e6499398dd3e25065eb5d44e34c6cf8c
    STARRY_ROUND5_SCHED_SETAFFINITY_EMPTY_MASK:
      id: STARRY_ROUND5_SCHED_SETAFFINITY_EMPTY_MASK
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:1f586167c13a6afbf5a37390f718844077bb1db86b5af03a6727eb05b024a0b7
    STARRY_ROUND5_SCHED_YIELD:
      id: STARRY_ROUND5_SCHED_YIELD
      generated_at_utc: '2026-07-17T07:32:33.916128Z'
      content_hash: sha256:4b993294f76b39f4d5ea5c02b1ec87ae2fb7bf8602b797cb04f368280bfb66f2
    STARRY_ROUND5_SENDFILE_IN_FD:
      id: STARRY_ROUND5_SENDFILE_IN_FD
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:c75e772fd1599ff88cc107d1feb67f0646652623adf759665fd42bb6d3cd5aa8
    STARRY_ROUND5_SENDFILE_OUT_FD:
      id: STARRY_ROUND5_SENDFILE_OUT_FD
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:a6310ca6f51ea5b7f2476cb6c791befea85389f449edf7910cb9e737c76dcb8d
    STARRY_ROUND5_SENDMSG_MESSAGE_POINTER:
      id: STARRY_ROUND5_SENDMSG_MESSAGE_POINTER
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:d98fdcf1f705c6c89ed155d2cedd172ab10c0edfcdd47e440804cfced1dcf47a
    STARRY_ROUND5_SETPGID_NEGATIVE:
      id: STARRY_ROUND5_SETPGID_NEGATIVE
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:e923f0a95c9d3ed1126bc7a86b0ca6c8193477f0035d3cbd51dd1c9b323546c1
    STARRY_ROUND5_SETPRIORITY_SELECTOR:
      id: STARRY_ROUND5_SETPRIORITY_SELECTOR
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:9cbac9cb08c0446ec8cb0e62deab0da59b922b095489fb8dd540b8f0de3c93d3
    STARRY_ROUND5_SOCKET_INVALID_TYPE:
      id: STARRY_ROUND5_SOCKET_INVALID_TYPE
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:d2d8afede60aa68d453d70afcadbef69e726ab083280b704d2897d9d62bf31d1
    STARRY_ROUND5_SOCKET_PROTOCOL_ERRORS:
      id: STARRY_ROUND5_SOCKET_PROTOCOL_ERRORS
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:c356539030c60bac476550a7a7eaef646d065dfbb22b00c2d1e365071f077092
    STARRY_SOCKET_FD_VALIDATION:
      id: STARRY_SOCKET_FD_VALIDATION
      generated_at_utc: '2026-07-23T03:01:49.216844Z'
      content_hash: sha256:4b6bc51f2d193cfb1a8f8ffa1097da5c55ba6a184d9206e76efb55240294733e
    STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO:
      id: STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:39ebc0849b8fede86d9689ed1dba7fda23315b83937a447b328ffd1a94bdfb34
    STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE:
      id: STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE
      generated_at_utc: '2026-07-16T08:20:59.387945Z'
      content_hash: sha256:e2e77be33c0c00e8b38780cef8b7b9ff37f7271c1a4f1d1289041b8cf68f4817
    STARRY_ROUND3_INIT_MODULE_PERMISSION:
      id: STARRY_ROUND3_INIT_MODULE_PERMISSION
      generated_at_utc: '2026-07-16T08:20:59.387945Z'
      content_hash: sha256:9df3be22e06572f2b77a0e12c13e9bc9c3a498b4317a288e87e880ee8b23d177
    STARRY_FINAL_SYSLOG_READ_ARGUMENTS:
      id: STARRY_FINAL_SYSLOG_READ_ARGUMENTS
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:947467c63df939000091ce9bbfa725b3dac3bd6d9fdb07cbb606a5ef778825f1
    STARRY_FINAL_UMOUNT_PRIVILEGE:
      id: STARRY_FINAL_UMOUNT_PRIVILEGE
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:9076327bc10ad8f7970328c88a4b62abfe9cbdc3118616d23772096e764afae7
    STARRY_FINAL_UNSHARE_NEWNS_PRIVILEGE:
      id: STARRY_FINAL_UNSHARE_NEWNS_PRIVILEGE
      generated_at_utc: '2026-07-16T10:53:32.721870Z'
      content_hash: sha256:647346966f4cd913f5bc3219f181a2d9b7f6865ea1decc8e898b1f28751b9842
  dynamic_tests:
    STARRY_FINAL_FS_RUNTIME:
      id: STARRY_FINAL_FS_RUNTIME
      generated_at_utc: '2026-07-16T08:20:59.387945Z'
      content_hash: sha256:74f19339cd0cbf3cbe5563a79ce90d92665484515dc3bb2e184412d28073f9dd
    STARRY_FINAL_WAIT_RUNTIME:
      id: STARRY_FINAL_WAIT_RUNTIME
      generated_at_utc: '2026-07-16T08:20:59.387945Z'
      content_hash: sha256:097f4cbfe7a71eeb6388c56404f67f407d9dc62ce2e19c3d4bad524dd750358a
base_execution_scope:
  rules:
  - LTP_0087F445CEB63414
  - LTP_026CB4A1CA7CDC6B
  - LTP_03AF14160F8B59A0
  - LTP_08F05BA6ED1CEE6A
  - LTP_098AFE0E8E10B0EF
  - LTP_09B39E9C9254ECB2
  - LTP_10B3572DBFA6742B
  - LTP_1691F6F9712C5546
  - LTP_1726C16756E9651C
  - LTP_17B7A9460939622A
  - LTP_1AACAC53BAF23BA9
  - LTP_1BB76939FF2A40B5
  - LTP_2554AC2E46FC6A15
  - LTP_26555A26680524AD
  - LTP_26AE3C69D80D35F8
  - LTP_2BDE60C0E64B4DC8
  - LTP_31D9D767D6888DDA
  - LTP_3741A721C9C463D0
  - LTP_3743BC827FB4F981
  - LTP_37C625BD7D7C5F1D
  - LTP_39B1E5C574F2D3DC
  - LTP_3A7B17AF231D4158
  - LTP_3B1458E6E26CBB53
  - LTP_40A45C5E82D7F4A1
  - LTP_425E5A3502541DE8
  - LTP_4308D71D8BD6519D
  - LTP_44DC5382746D773D
  - LTP_4953FAD330ADE150
  - LTP_4C1F446C9C520B36
  - LTP_4F02ACC6E2F6B094
  - LTP_511185D6DE2A63A0
  - LTP_51E295101A9F4411
  - LTP_53E3454ED6EFD842
  - LTP_5516B8A938B9C3A5
  - LTP_585CC852338F38EE
  - LTP_5D8D2B3BEDA79604
  - LTP_652CE911B47794E0
  - LTP_6B29B31CE99466E6
  - LTP_6FFB17DB762F3167
  - LTP_729222947741DFD6
  - LTP_75D52C5E9C93B6D7
  - LTP_76BFF56F735A0074
  - LTP_791DEA825D66980B
  - LTP_7BC885B5878C95B6
  - LTP_7DFAC48A8971CFE3
  - LTP_83709E56D6285F71
  - LTP_84DBE108A850E845
  - LTP_88D300A8FB407324
  - LTP_8988E5015778894A
  - LTP_8C1C2578972FCA1D
  - LTP_914935DA5C379DA1
  - LTP_91ED7E85761CE00F
  - LTP_9305FA6D8B835652
  - LTP_9461AA782926BAB4
  - LTP_971DB17D32C51561
  - LTP_9B3646398697EA64
  - LTP_9B36D27A4A2994D0
  - LTP_9F560A103CB6F910
  - LTP_9FD87A3F7688FEF1
  - LTP_A0547B601C515355
  - LTP_A367723236ADA8B4
  - LTP_A4A662687B98D33F
  - LTP_A774FC10727E8ED2
  - LTP_A9BC7EBC1784A722
  - LTP_ACF7A30AF3B10973
  - LTP_AF8D38878ED1A9DA
  - LTP_B058D6B9CBBB459D
  - LTP_B7F51635806E7E59
  - LTP_BD5C209F4C6EE910
  - LTP_BDA36F61423EEB3E
  - LTP_BF2428964ADD116F
  - LTP_CBF4B6C8A1458A28
  - LTP_CCC36F43E9463D3E
  - LTP_D0800876342DE939
  - LTP_D296A517F138A0C0
  - LTP_D2E2A5F40B2313E5
  - LTP_DD2E1A555B603C7B
  - LTP_E316C28E36E136DA
  - LTP_E520E500AB3AE851
  - LTP_E6C69C9F4AB565BC
  - LTP_EA90C626D9AA6C08
  - LTP_EA953D5E5C4B2B1F
  - LTP_ED2BA909DF79625A
  - LTP_EE8E695CF61D6D8A
  - LTP_F1DC44813DCA6A05
  - LTP_F4DE81D703447628
  - LTP_F8FD511858BB650D
  - LTP_FADBA4ADECCFBA4E
  - LTP_FB0ABF26A21EAE3C
  - LTP_FC1E41C3414E7F21
  - LTP_FCC236A4D5926B81
  - LTP_FEACDC300C3E1DD7
  - MAN_027D17C587997F75
  - MAN_02D976F1ED01493F
  - MAN_03E8B237E962C1D2
  - MAN_045719AC8992819E--045719ac8992
  - MAN_083368964C7623C0
  - MAN_0BA66331CB4B2091
  - MAN_0D9E79AEB44B7510
  - MAN_0F2C1ABA8AF5C15E
  - MAN_1115E878B4F50CF3
  - MAN_147EECDC5DAB119D
  - MAN_18C5488E8D09D6D2--18c5488e8d09
  - MAN_1EFA395D2832F95E
  - MAN_20A10178D28B400B
  - MAN_23E25F7C4136339F
  - MAN_2421026C912D8F9E--2421026c912d
  - MAN_254F60FBFDA7A2BB
  - MAN_25CD94348F7360E1
  - MAN_330C0628475E2900
  - MAN_35AF4698AC57ED3F--35af4698ac57
  - MAN_362BD9184BA2B5C7
  - MAN_37A8B25C745F91BB--37a8b25c745f
  - MAN_392816F25BD330A2
  - MAN_39C5F1849EB3A736
  - MAN_43BBCE48C452BDDD
  - MAN_44D6BD8077F837B5
  - MAN_45A2B6F5ADF14C3F
  - MAN_48B52042FE3DEA4C--48b52042fe3d
  - MAN_494CD34A8C11734B
  - MAN_4C50AA2793AB7713
  - MAN_524B615D8F9A7E12
  - MAN_5378890AE3F832EE--5378890ae3f8
  - MAN_58936D050A8879DE
  - MAN_5B2667DFDCB4EB31
  - MAN_5B4118BF4C21F770
  - MAN_5F5865EF1A8D5904
  - MAN_6038BC183A1CE6BF
  - MAN_67ECA3FB50D80BAF
  - MAN_6998D4E70F807B13
  - MAN_6B7EED8E43FDD1BA
  - MAN_6D665164162723C5--6d6651641627
  - MAN_6D77B363EA967C8F
  - MAN_6FA8F2D41D1B7062
  - MAN_732160952277CD16
  - MAN_73E054548B324267
  - MAN_794294DBD03CA974
  - MAN_794294DBD03CA974--794294dbd03c
  - MAN_7C3C0347FD37CEB9
  - MAN_8153E21BD727F6A0
  - MAN_81F4F1C3AD4F3217
  - MAN_8609DB2EE85AF88E
  - MAN_8812ADE8E360DB8F
  - MAN_8D160F5D77EC235B
  - MAN_8DB0AB4E3B90CB50
  - MAN_8DB0AB4E3B90CB50--8db0ab4e3b90
  - MAN_9452D425539B8023
  - MAN_95930C2D369C878D
  - MAN_968D07C7039689E5
  - MAN_9A17C8A141B47D41
  - MAN_9BC94E6BD25C05E1
  - MAN_9E0C30E4205FB415
  - MAN_9E12AA9A59F1BBE9
  - MAN_A1CD98CE32C423E4
  - MAN_A58EA189B1C9E326
  - MAN_A5F4BA2371332A4E
  - MAN_A67DCE77030808A6
  - MAN_AA8C115068BD5D76--aa8c115068bd
  - MAN_AE68C41A115C80FC--ae68c41a115c
  - MAN_AE7C62637F29A4C9
  - MAN_AF1D093225F75E82
  - MAN_B121E5340A1BEFEE
  - MAN_B1A8365C419E3164
  - MAN_B1A8365C419E3164--b1a8365c419e
  - MAN_B4DD5B60F33FC5E3
  - MAN_B5E18528035F6F87
  - MAN_B9EE0F176B92F526
  - MAN_BC425C37C792DDEE
  - MAN_BE74B0D21973DAEC
  - MAN_BE929AB9651E5E66
  - MAN_C04F44BFF720877B
  - MAN_C467D6702AB64674
  - MAN_CAA0FFEFF7C64A82
  - MAN_CDD044CBEEED1A80
  - MAN_CDD195853C6DFE14
  - MAN_CEC45E0E1446E3DF
  - MAN_D405972253EA086F
  - MAN_D84D77F1C6E463F4
  - MAN_DA06B43ED3D9DBBC
  - MAN_DA93975DA79D34AD--da93975da79d
  - MAN_DADCFA23F461FBBF
  - MAN_DBD043A36C2E4926
  - MAN_DC37B979EC91203E
  - MAN_DD6D48EB9B80CB6B
  - MAN_DD8A18DB0BF6E8A9
  - MAN_DE03A6A5B1731AF7--de03a6a5b173
  - MAN_DFDB86CEA63B78D3--dfdb86cea63b
  - MAN_E116073D3FDB5C1F
  - MAN_E32B6349055FCEF9
  - MAN_E99D067CF243EEE8
  - MAN_EA69373DAD6B5B01
  - MAN_EDB775C51FCEA404
  - MAN_EFBA9CA2760DA6B8
  - MAN_F12635B7646C0E9B
  - MAN_F6CB9D32040E99BA
  - MAN_F84F01B63ABC178D
  - MAN_FD5BF4CD3984BECF
  - MAN_FDD174E970AC7930
  static_checks:
  - STARRY_CHROOT_PATH
  - STARRY_CLOSE_BAD_FD_ERRNO
  - STARRY_CLOSE_FD_TABLE
  - STARRY_CLOSE_RANGE_SWEEP
  - STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS
  - STARRY_CLOSE_RANGE_VALIDATION
  - STARRY_CLOSE_SYSCALL
  - STARRY_CONNECT_ADDRESS_VALIDATION
  - STARRY_CONNECT_ENTRY
  - STARRY_COPY_FILE_RANGE_CORE
  - STARRY_DUP2_DUP3_BEHAVIOR
  - STARRY_DUP_BEHAVIOR
  - STARRY_EPOLL_CREATE1_FLAGS
  - STARRY_EPOLL_CTL_ENTRY
  - STARRY_EPOLL_CTL_INTEREST
  - STARRY_EPOLL_FACCESS_ERRNO
  - STARRY_EPOLL_FD_LOOKUP
  - STARRY_EPOLL_NESTED_LOOP
  - STARRY_ERRNO_TRANSLATION
  - STARRY_EXECVEAT_FACCESSAT_RESOLVE
  - STARRY_EXECVEAT_VALIDATION
  - STARRY_FACCESSAT2_VALIDATION
  - STARRY_FCHDIR_CORE
  - STARRY_FCHDIR_ERRNO_TRANSLATION
  - STARRY_FCHDIR_FD_VALIDATION
  - STARRY_FCHMODAT_FLAG_VALIDATION
  - STARRY_FD_TABLE_LOOKUP_ALLOCATION
  - STARRY_FINAL_ERRNO_TRANSLATION
  - STARRY_FINAL_SYSINFO_COPYOUT
  - STARRY_FINAL_TIMER_DELETE
  - STARRY_FINAL_TKILL_TID_VALIDATION
  - STARRY_FINAL_UNAME_COPYOUT
  - STARRY_FINAL_UNSHARE_FILES
  - STARRY_FINAL_UNSHARE_FLAG_VALIDATION
  - STARRY_FINAL_WAITID_OPTIONS
  - STARRY_FINAL_WAITPID_INT_MIN
  - STARRY_FINIT_MODULE_FLAG_VALIDATION
  - STARRY_MAN_CLOCK_GETRES_VALIDATION
  - STARRY_MAN_CLOCK_GETTIME_VALIDATION
  - STARRY_MAN_EVENTFD2_VALIDATION
  - STARRY_MAN_GETRANDOM_ARGUMENTS
  - STARRY_MAN_INOTIFY_ADD_WATCH_INPUTS
  - STARRY_MAN_INOTIFY_INIT1_VALIDATION
  - STARRY_MAN_INOTIFY_RM_WATCH_ID
  - STARRY_MAN_INOTIFY_RM_WATCH_INPUTS
  - STARRY_MAN_LISTEN_ENTRY
  - STARRY_MAN_MEMFD_CREATE_VALIDATION
  - STARRY_MAN_PIPE2_VALIDATION
  - STARRY_MAN_REBOOT_VALIDATION
  - STARRY_MAN_SECCOMP_OPERATION_FLAGS
  - STARRY_MAN_SECCOMP_VALIDATION
  - STARRY_MAN_SETDOMAINNAME_ARGUMENTS
  - STARRY_MAN_SETGROUPS_VALIDATION
  - STARRY_MAN_SETHOSTNAME_ARGUMENTS
  - STARRY_MAN_SHUTDOWN_VALIDATION
  - STARRY_MAN_SOCKETPAIR_VALIDATION
  - STARRY_MMAP_ACCESS
  - STARRY_MMAP_ARGUMENTS
  - STARRY_MMAP_FD
  - STARRY_ROUND2_CLOSE_FD_TABLE
  - STARRY_ROUND2_CLOSE_SYSCALL
  - STARRY_ROUND2_ERRNO_TRANSLATION
  - STARRY_ROUND3_ERRNO_TRANSLATION
  - STARRY_ROUND3_FSTATFS_ERRORS
  - STARRY_ROUND3_FSTAT_CORE
  - STARRY_ROUND3_GETCWD
  - STARRY_ROUND3_GETPRIORITY_SELECTOR
  - STARRY_ROUND3_GETRLIMIT_CORE
  - STARRY_ROUND3_GETRLIMIT_DISPATCH
  - STARRY_ROUND3_JOB_ID_LOOKUP
  - STARRY_ROUND3_PROCESS_LOOKUP
  - STARRY_ROUND4_ERRNO_TRANSLATION
  - STARRY_ROUND4_MLOCK2_FLAGS
  - STARRY_ROUND4_MSYNC_EXCLUSIVE_MODES
  - STARRY_ROUND4_MSYNC_UNKNOWN_FLAGS
  - STARRY_ROUND4_MUNMAP_ZERO_LENGTH
  - STARRY_ROUND4_OPENAT2_SIZE
  - STARRY_ROUND4_PIDFD_GETFD_FLAGS
  - STARRY_ROUND4_PIDFD_OPEN_INPUTS
  - STARRY_ROUND4_PIDFD_SIGNAL_FLAGS
  - STARRY_ROUND4_READ_BAD_FD
  - STARRY_ROUND4_VECTOR_IO_FLAGS
  - STARRY_ROUND5_ERRNO_TRANSLATION
  - STARRY_ROUND5_SCHED_SETAFFINITY_EMPTY_MASK
  - STARRY_ROUND5_SCHED_YIELD
  - STARRY_ROUND5_SENDFILE_IN_FD
  - STARRY_ROUND5_SENDFILE_OUT_FD
  - STARRY_ROUND5_SENDMSG_MESSAGE_POINTER
  - STARRY_ROUND5_SETPGID_NEGATIVE
  - STARRY_ROUND5_SETPRIORITY_SELECTOR
  - STARRY_ROUND5_SOCKET_INVALID_TYPE
  - STARRY_ROUND5_SOCKET_PROTOCOL_ERRORS
  - STARRY_SOCKET_FD_VALIDATION
  dynamic_tests: []
revalidation_scope:
  rules: []
  static_checks: []
  dynamic_tests: []
effective_execution_scope: &id001
  rules:
  - LTP_0087F445CEB63414
  - LTP_026CB4A1CA7CDC6B
  - LTP_03AF14160F8B59A0
  - LTP_04236FD5B061DEB9
  - LTP_08F05BA6ED1CEE6A
  - LTP_098AFE0E8E10B0EF
  - LTP_09B39E9C9254ECB2
  - LTP_10B3572DBFA6742B
  - LTP_1691F6F9712C5546
  - LTP_1726C16756E9651C
  - LTP_17B7A9460939622A
  - LTP_1AACAC53BAF23BA9
  - LTP_1BB76939FF2A40B5
  - LTP_21FCBFC328D1815A
  - LTP_2554AC2E46FC6A15
  - LTP_26555A26680524AD
  - LTP_26AE3C69D80D35F8
  - LTP_287CF10D893735AB
  - LTP_2BDE60C0E64B4DC8
  - LTP_2F3E34FD672DBF34
  - LTP_31D9D767D6888DDA
  - LTP_3741A721C9C463D0
  - LTP_3743BC827FB4F981
  - LTP_37C625BD7D7C5F1D
  - LTP_38432B154B641410
  - LTP_39B1E5C574F2D3DC
  - LTP_3A7B17AF231D4158
  - LTP_3B1458E6E26CBB53
  - LTP_40A45C5E82D7F4A1
  - LTP_425E5A3502541DE8
  - LTP_4308D71D8BD6519D
  - LTP_43728156B00FF104
  - LTP_4494B70BBA693D42
  - LTP_44DC5382746D773D
  - LTP_4953FAD330ADE150
  - LTP_4C1F446C9C520B36
  - LTP_4F02ACC6E2F6B094
  - LTP_511185D6DE2A63A0
  - LTP_51E295101A9F4411
  - LTP_53E3454ED6EFD842
  - LTP_5516B8A938B9C3A5
  - LTP_585CC852338F38EE
  - LTP_58C8C307B1FF2510
  - LTP_5D8D2B3BEDA79604
  - LTP_614C018F61C078A0
  - LTP_652CE911B47794E0
  - LTP_6B29B31CE99466E6
  - LTP_6B9F97B897EC5C32
  - LTP_6C14DE68E3C0CC24
  - LTP_6F4B3A38B8BF4C7E
  - LTP_6F77CAA9FC4423BA
  - LTP_6FFB17DB762F3167
  - LTP_71DD72481EF5740E
  - LTP_729222947741DFD6
  - LTP_74BB3F96CBA52D02
  - LTP_75D52C5E9C93B6D7
  - LTP_76BFF56F735A0074
  - LTP_791DEA825D66980B
  - LTP_7B0F966046AECA7E
  - LTP_7BC885B5878C95B6
  - LTP_7DFAC48A8971CFE3
  - LTP_82A8802A27A3D2BF
  - LTP_83709E56D6285F71
  - LTP_84DBE108A850E845
  - LTP_86144BF50FB25D3A
  - LTP_88D300A8FB407324
  - LTP_8988E5015778894A
  - LTP_8C1C2578972FCA1D
  - LTP_914935DA5C379DA1
  - LTP_91ED7E85761CE00F
  - LTP_9305FA6D8B835652
  - LTP_9461AA782926BAB4
  - LTP_971DB17D32C51561
  - LTP_9B3646398697EA64
  - LTP_9B36D27A4A2994D0
  - LTP_9C2FB7732A0B90B6
  - LTP_9F560A103CB6F910
  - LTP_9FD87A3F7688FEF1
  - LTP_A0547B601C515355
  - LTP_A2934B80997B62C9
  - LTP_A367723236ADA8B4
  - LTP_A4A662687B98D33F
  - LTP_A774FC10727E8ED2
  - LTP_A9BC7EBC1784A722
  - LTP_ACF7A30AF3B10973
  - LTP_AD3A4B98FF201ABE
  - LTP_AF8D38878ED1A9DA
  - LTP_B0433B78A1641F24
  - LTP_B058D6B9CBBB459D
  - LTP_B7F51635806E7E59
  - LTP_BD5C209F4C6EE910
  - LTP_BDA36F61423EEB3E
  - LTP_BF2428964ADD116F
  - LTP_C13C4F63D58904BC
  - LTP_C24E55F06625D564
  - LTP_C8376BC347F94A98
  - LTP_CBF4B6C8A1458A28
  - LTP_CCC36F43E9463D3E
  - LTP_D0800876342DE939
  - LTP_D1A18560E485E146
  - LTP_D246498B20D9CB2C
  - LTP_D254EE40E8B5957E
  - LTP_D296A517F138A0C0
  - LTP_D2E2A5F40B2313E5
  - LTP_DA64FD04E43656E6
  - LTP_DCC88B2C458969EA
  - LTP_DD2E1A555B603C7B
  - LTP_DDA854712C50CD6A
  - LTP_DF5B725563FDFB31
  - LTP_E316C28E36E136DA
  - LTP_E520E500AB3AE851
  - LTP_E6C69C9F4AB565BC
  - LTP_EA90C626D9AA6C08
  - LTP_EA953D5E5C4B2B1F
  - LTP_ECD986F27CF15E1E
  - LTP_ED2BA909DF79625A
  - LTP_EE8E695CF61D6D8A
  - LTP_F1DC44813DCA6A05
  - LTP_F4DE81D703447628
  - LTP_F8FD511858BB650D
  - LTP_FADBA4ADECCFBA4E
  - LTP_FB0ABF26A21EAE3C
  - LTP_FC1E41C3414E7F21
  - LTP_FC8BA85373EA2D8F
  - LTP_FCC236A4D5926B81
  - LTP_FEACDC300C3E1DD7
  - MAN_027D17C587997F75
  - MAN_02D976F1ED01493F
  - MAN_03E8B237E962C1D2
  - MAN_045719AC8992819E--045719ac8992
  - MAN_083368964C7623C0
  - MAN_0BA66331CB4B2091
  - MAN_0D9E79AEB44B7510
  - MAN_0F2C1ABA8AF5C15E
  - MAN_1115E878B4F50CF3
  - MAN_147EECDC5DAB119D
  - MAN_18C5488E8D09D6D2--18c5488e8d09
  - MAN_1EFA395D2832F95E
  - MAN_20A10178D28B400B
  - MAN_23E25F7C4136339F
  - MAN_2421026C912D8F9E--2421026c912d
  - MAN_254F60FBFDA7A2BB
  - MAN_25CD94348F7360E1
  - MAN_330C0628475E2900
  - MAN_35AF4698AC57ED3F--35af4698ac57
  - MAN_362BD9184BA2B5C7
  - MAN_37A8B25C745F91BB--37a8b25c745f
  - MAN_392816F25BD330A2
  - MAN_39C5F1849EB3A736
  - MAN_43BBCE48C452BDDD
  - MAN_44D6BD8077F837B5
  - MAN_45A2B6F5ADF14C3F
  - MAN_48B52042FE3DEA4C--48b52042fe3d
  - MAN_494CD34A8C11734B
  - MAN_4C50AA2793AB7713
  - MAN_524B615D8F9A7E12
  - MAN_5378890AE3F832EE--5378890ae3f8
  - MAN_58936D050A8879DE
  - MAN_5B2667DFDCB4EB31
  - MAN_5B4118BF4C21F770
  - MAN_5F5865EF1A8D5904
  - MAN_6038BC183A1CE6BF
  - MAN_67ECA3FB50D80BAF
  - MAN_6998D4E70F807B13
  - MAN_6B7EED8E43FDD1BA
  - MAN_6D665164162723C5--6d6651641627
  - MAN_6D77B363EA967C8F
  - MAN_6FA8F2D41D1B7062
  - MAN_732160952277CD16
  - MAN_73E054548B324267
  - MAN_794294DBD03CA974
  - MAN_794294DBD03CA974--794294dbd03c
  - MAN_7C3C0347FD37CEB9
  - MAN_8153E21BD727F6A0
  - MAN_81F4F1C3AD4F3217
  - MAN_8609DB2EE85AF88E
  - MAN_8812ADE8E360DB8F
  - MAN_8D160F5D77EC235B
  - MAN_8DB0AB4E3B90CB50
  - MAN_8DB0AB4E3B90CB50--8db0ab4e3b90
  - MAN_9452D425539B8023
  - MAN_95930C2D369C878D
  - MAN_968D07C7039689E5
  - MAN_9A17C8A141B47D41
  - MAN_9BC94E6BD25C05E1
  - MAN_9E0C30E4205FB415
  - MAN_9E12AA9A59F1BBE9
  - MAN_A1CD98CE32C423E4
  - MAN_A58EA189B1C9E326
  - MAN_A5F4BA2371332A4E
  - MAN_A67DCE77030808A6
  - MAN_AA8C115068BD5D76--aa8c115068bd
  - MAN_AE68C41A115C80FC--ae68c41a115c
  - MAN_AE7C62637F29A4C9
  - MAN_AF1D093225F75E82
  - MAN_B121E5340A1BEFEE
  - MAN_B1A8365C419E3164
  - MAN_B1A8365C419E3164--b1a8365c419e
  - MAN_B4DD5B60F33FC5E3
  - MAN_B5E18528035F6F87
  - MAN_B9EE0F176B92F526
  - MAN_BC425C37C792DDEE
  - MAN_BE74B0D21973DAEC
  - MAN_BE929AB9651E5E66
  - MAN_C04F44BFF720877B
  - MAN_C467D6702AB64674
  - MAN_CAA0FFEFF7C64A82
  - MAN_CDD044CBEEED1A80
  - MAN_CDD195853C6DFE14
  - MAN_CEC45E0E1446E3DF
  - MAN_D405972253EA086F
  - MAN_D84D77F1C6E463F4
  - MAN_DA06B43ED3D9DBBC
  - MAN_DA93975DA79D34AD--da93975da79d
  - MAN_DADCFA23F461FBBF
  - MAN_DBD043A36C2E4926
  - MAN_DC37B979EC91203E
  - MAN_DD6D48EB9B80CB6B
  - MAN_DD8A18DB0BF6E8A9
  - MAN_DE03A6A5B1731AF7--de03a6a5b173
  - MAN_DFDB86CEA63B78D3--dfdb86cea63b
  - MAN_E116073D3FDB5C1F
  - MAN_E32B6349055FCEF9
  - MAN_E99D067CF243EEE8
  - MAN_EA69373DAD6B5B01
  - MAN_EDB775C51FCEA404
  - MAN_EFBA9CA2760DA6B8
  - MAN_F12635B7646C0E9B
  - MAN_F6CB9D32040E99BA
  - MAN_F84F01B63ABC178D
  - MAN_FD5BF4CD3984BECF
  - MAN_FDD174E970AC7930
  static_checks:
  - STARRY_CHROOT_PATH
  - STARRY_CLOSE_BAD_FD_ERRNO
  - STARRY_CLOSE_FD_TABLE
  - STARRY_CLOSE_RANGE_SWEEP
  - STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS
  - STARRY_CLOSE_RANGE_VALIDATION
  - STARRY_CLOSE_SYSCALL
  - STARRY_CONNECT_ADDRESS_VALIDATION
  - STARRY_CONNECT_ENTRY
  - STARRY_COPY_FILE_RANGE_CORE
  - STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO
  - STARRY_DUP2_DUP3_BEHAVIOR
  - STARRY_DUP_BEHAVIOR
  - STARRY_EPOLL_CREATE1_FLAGS
  - STARRY_EPOLL_CTL_ENTRY
  - STARRY_EPOLL_CTL_INTEREST
  - STARRY_EPOLL_FACCESS_ERRNO
  - STARRY_EPOLL_FD_LOOKUP
  - STARRY_EPOLL_NESTED_LOOP
  - STARRY_ERRNO_TRANSLATION
  - STARRY_EXECVEAT_FACCESSAT_RESOLVE
  - STARRY_EXECVEAT_VALIDATION
  - STARRY_FACCESSAT2_VALIDATION
  - STARRY_FCHDIR_CORE
  - STARRY_FCHDIR_ERRNO_TRANSLATION
  - STARRY_FCHDIR_FD_VALIDATION
  - STARRY_FCHMODAT_FLAG_VALIDATION
  - STARRY_FD_TABLE_LOOKUP_ALLOCATION
  - STARRY_FINAL_ERRNO_TRANSLATION
  - STARRY_FINAL_SYSINFO_COPYOUT
  - STARRY_FINAL_SYSLOG_READ_ARGUMENTS
  - STARRY_FINAL_TIMER_DELETE
  - STARRY_FINAL_TKILL_TID_VALIDATION
  - STARRY_FINAL_UMOUNT_PRIVILEGE
  - STARRY_FINAL_UNAME_COPYOUT
  - STARRY_FINAL_UNSHARE_FILES
  - STARRY_FINAL_UNSHARE_FLAG_VALIDATION
  - STARRY_FINAL_UNSHARE_NEWNS_PRIVILEGE
  - STARRY_FINAL_WAITID_OPTIONS
  - STARRY_FINAL_WAITPID_INT_MIN
  - STARRY_FINIT_MODULE_FLAG_VALIDATION
  - STARRY_MAN_CLOCK_GETRES_VALIDATION
  - STARRY_MAN_CLOCK_GETTIME_VALIDATION
  - STARRY_MAN_EVENTFD2_VALIDATION
  - STARRY_MAN_GETRANDOM_ARGUMENTS
  - STARRY_MAN_INOTIFY_ADD_WATCH_INPUTS
  - STARRY_MAN_INOTIFY_INIT1_VALIDATION
  - STARRY_MAN_INOTIFY_RM_WATCH_ID
  - STARRY_MAN_INOTIFY_RM_WATCH_INPUTS
  - STARRY_MAN_LISTEN_ENTRY
  - STARRY_MAN_MEMFD_CREATE_VALIDATION
  - STARRY_MAN_PIPE2_VALIDATION
  - STARRY_MAN_REBOOT_VALIDATION
  - STARRY_MAN_SECCOMP_OPERATION_FLAGS
  - STARRY_MAN_SECCOMP_VALIDATION
  - STARRY_MAN_SETDOMAINNAME_ARGUMENTS
  - STARRY_MAN_SETGROUPS_VALIDATION
  - STARRY_MAN_SETHOSTNAME_ARGUMENTS
  - STARRY_MAN_SHUTDOWN_VALIDATION
  - STARRY_MAN_SOCKETPAIR_VALIDATION
  - STARRY_MMAP_ACCESS
  - STARRY_MMAP_ARGUMENTS
  - STARRY_MMAP_FD
  - STARRY_ROUND2_CLOSE_FD_TABLE
  - STARRY_ROUND2_CLOSE_SYSCALL
  - STARRY_ROUND2_ERRNO_TRANSLATION
  - STARRY_ROUND3_ERRNO_TRANSLATION
  - STARRY_ROUND3_FSTATFS_ERRORS
  - STARRY_ROUND3_FSTAT_CORE
  - STARRY_ROUND3_GETCWD
  - STARRY_ROUND3_GETPRIORITY_SELECTOR
  - STARRY_ROUND3_GETRLIMIT_CORE
  - STARRY_ROUND3_GETRLIMIT_DISPATCH
  - STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE
  - STARRY_ROUND3_INIT_MODULE_PERMISSION
  - STARRY_ROUND3_JOB_ID_LOOKUP
  - STARRY_ROUND3_PROCESS_LOOKUP
  - STARRY_ROUND4_ERRNO_TRANSLATION
  - STARRY_ROUND4_MLOCK2_FLAGS
  - STARRY_ROUND4_MSYNC_EXCLUSIVE_MODES
  - STARRY_ROUND4_MSYNC_UNKNOWN_FLAGS
  - STARRY_ROUND4_MUNMAP_ZERO_LENGTH
  - STARRY_ROUND4_OPENAT2_SIZE
  - STARRY_ROUND4_PIDFD_GETFD_FLAGS
  - STARRY_ROUND4_PIDFD_OPEN_INPUTS
  - STARRY_ROUND4_PIDFD_SIGNAL_FLAGS
  - STARRY_ROUND4_READ_BAD_FD
  - STARRY_ROUND4_VECTOR_IO_FLAGS
  - STARRY_ROUND5_ERRNO_TRANSLATION
  - STARRY_ROUND5_SCHED_SETAFFINITY_EMPTY_MASK
  - STARRY_ROUND5_SCHED_YIELD
  - STARRY_ROUND5_SENDFILE_IN_FD
  - STARRY_ROUND5_SENDFILE_OUT_FD
  - STARRY_ROUND5_SENDMSG_MESSAGE_POINTER
  - STARRY_ROUND5_SETPGID_NEGATIVE
  - STARRY_ROUND5_SETPRIORITY_SELECTOR
  - STARRY_ROUND5_SOCKET_INVALID_TYPE
  - STARRY_ROUND5_SOCKET_PROTOCOL_ERRORS
  - STARRY_SOCKET_FD_VALIDATION
  dynamic_tests:
  - STARRY_FINAL_FS_RUNTIME
  - STARRY_FINAL_WAIT_RUNTIME
execution_scope: *id001
rule_syscalls:
  LTP_004E24807F6067A5:
  - madvise
  LTP_0087F445CEB63414:
  - read
  LTP_018C7E7A08833780:
  - poll
  LTP_018E81B4859D535F:
  - access
  LTP_01F98F68E029F1A9:
  - access
  LTP_021CFAE8581109DA:
  - fsconfig
  LTP_025CF701276457CB:
  - faccessat2
  LTP_026CB4A1CA7CDC6B:
  - openat2
  LTP_02D0577172D97F4B:
  - ftruncate
  LTP_030901665B56CA4C:
  - getsockname
  LTP_0311772B70C94C38:
  - pidfd_open
  LTP_0324F0A6601FFECE:
  - rt_sigsuspend
  LTP_033FAA6E22CDE433:
  - msync
  LTP_03AF14160F8B59A0:
  - waitpid
  LTP_03E15C829583D726:
  - epoll_ctl
  LTP_03FD233DFE92488D:
  - sbrk
  LTP_0433C0FC2D4AD1EE:
  - utime
  LTP_04799921082E0315:
  - access
  LTP_04A84187DEC4CF09:
  - flock
  LTP_056DB4870D82DDC3:
  - openat2
  LTP_05A4E0F4E4D24683:
  - access
  LTP_05B109981D13ED76:
  - write
  LTP_06F742EF42AA55BA:
  - request_key
  LTP_07267357D988E0D3:
  - access
  LTP_074981FFB7FA5DB7:
  - mlock2
  LTP_078A6E34EE607719:
  - request_key
  LTP_07CB582EDCDF46C6:
  - chroot
  LTP_07CE577381BD5611:
  - readlinkat
  LTP_07D1AC926F3B00CA:
  - access
  LTP_07FCC99E3AE43064:
  - signalfd
  LTP_08AD094BD7C5CF64:
  - access
  LTP_08C4F07A07C4C3F7:
  - pidfd_send_signal
  LTP_08E6F527B4F8150F:
  - move_mount
  LTP_08F05BA6ED1CEE6A:
  - pidfd_send_signal
  LTP_092C2A39F54E4F90:
  - access
  LTP_094580B59455EBF1:
  - access
  LTP_0973D484DB2E7E2D:
  - access
  LTP_098AFE0E8E10B0EF:
  - dup3
  LTP_09ADB22B713F6C62:
  - munmap
  LTP_09B39E9C9254ECB2:
  - close
  LTP_09DDAC16EAB70A23:
  - access
  LTP_09FE3EF67718087A:
  - access
  LTP_09FED6AAC1020069:
  - fpathconf
  LTP_0A2035C9A2A77F66:
  - sched_getattr
  LTP_0A7162BAB3AA89BD:
  - access
  LTP_0A819CDD66F1C6A1:
  - request_key
  LTP_0A9DA3A2803EEF70:
  - access
  LTP_0B35C54F2F39E4D4:
  - fsconfig
  LTP_0B6757A74359BB1E:
  - access
  LTP_0B9F382D21CF8997:
  - access
  LTP_0C01151E99096244:
  - pwrite64
  LTP_0C4BDB0FD7A306D8:
  - rename
  LTP_0C5623B3D5C7430F:
  - setpgid
  LTP_0D9B02C95396CCDC:
  - signalfd
  LTP_0D9BB2CB02786128:
  - fsconfig
  LTP_0DAD2B9BF983B90F:
  - access
  LTP_0DF4BC077C390176:
  - fsconfig
  LTP_0E49032B253C732D:
  - access
  LTP_0E51A1345D29A74B:
  - madvise
  LTP_0E9124C6B17214C9:
  - access
  LTP_0EB6FB88C2CC23AE:
  - access
  LTP_0EEADAF9E605632C:
  - pidfd_open
  LTP_0EFD831C4B5C2D95:
  - access
  LTP_0F3BABDCCC428DF4:
  - access
  LTP_0F9C596BA8184375:
  - tee
  LTP_0F9F906AC57F0B46:
  - pidfd_send_signal
  LTP_0FE0E20EAC6DE889:
  - waitid
  LTP_100C7EAA3620A220:
  - utime
  LTP_1028A46194A35788:
  - rename
  LTP_10455AB2DFB23127:
  - access
  LTP_10B3572DBFA6742B:
  - timer_delete
  LTP_11235D2EF3DC4C5C:
  - fsconfig
  LTP_11385EF43CBDA2E0:
  - mq_notify
  LTP_11852F99424BD7E5:
  - mprotect
  LTP_11C0431607FD5753:
  - epoll_create1
  LTP_11C0673F2CC64D66:
  - mkdirat
  LTP_122500959CDABFC9:
  - faccessat2
  LTP_1238FDE5F55AC037:
  - access
  LTP_1264D075DA68BB98:
  - iopl
  LTP_12A1904141AAE2EE:
  - dup2
  LTP_12FEE545B9A2556F:
  - getcwd
  LTP_1325C077A1CDE514:
  - cachestat
  LTP_137CD2E37BF545BF:
  - execveat
  LTP_139142311CF01E20:
  - sbrk
  LTP_14072975543D9890:
  - fstatfs
  LTP_14105E9CB6DC44FC:
  - ustat
  LTP_144706EDC721819A:
  - faccessat2
  LTP_148C73A2C00EBA17:
  - mq_notify
  LTP_149BE2ED84AB5AAC:
  - access
  LTP_1551C6F53CF6865A:
  - symlink
  LTP_15F112E8B77975DD:
  - preadv2
  LTP_15F83338278C3CFE:
  - access
  LTP_1617908ACCAE8499:
  - access
  LTP_16343E95C1C7EF47:
  - pathconf
  LTP_16449F1C9EC8C71F:
  - access
  LTP_1661259678F899BC:
  - pathconf
  LTP_1691F6F9712C5546:
  - wait4
  LTP_1707E748EA729431:
  - pathconf
  LTP_1726C16756E9651C:
  - dup3
  LTP_17B7A9460939622A:
  - fchdir
  LTP_181653F77A7325D4:
  - rename
  LTP_1893FF0C4930806E:
  - pathconf
  LTP_18A80CB437A03D1F:
  - access
  LTP_18E65E41E98D9E97:
  - pidfd_open
  LTP_1918D556CB808466:
  - fsconfig
  LTP_1A1038DA1B735AB6:
  - access
  LTP_1A2B889BBD9A1444:
  - fchmodat
  LTP_1A68979B981D8947:
  - madvise
  LTP_1AA7F21DA5C55800:
  - eventfd
  LTP_1AACAC53BAF23BA9:
  - preadv2
  LTP_1B2E614CA8847B31:
  - llistxattr
  LTP_1B63533FE8D3FAF0:
  - write
  LTP_1B65027CA2FD0026:
  - open_by_handle_at
  LTP_1BB76939FF2A40B5:
  - pidfd_open
  LTP_1BDC4A832DB89410:
  - request_key
  LTP_1C1877AB6CAE8906:
  - mlock
  LTP_1C8100D018645855:
  - fsconfig
  LTP_1CD2E41D7D4A4B9D:
  - access
  LTP_1D4684A49237E045:
  - access
  LTP_1D6E9D5C4E09D7F5:
  - madvise
  LTP_1E3617B704005CFB:
  - pread64
  LTP_1EEDAE05876D0546:
  - fpathconf
  LTP_1F2328B410A3010D:
  - pwritev2
  LTP_1F61FDFDC752BFE1:
  - mmap
  LTP_1FC16C0CDAE55FD5:
  - access
  LTP_1FF6EB837BDD04F1:
  - pathconf
  LTP_207043BA148C0097:
  - mmap
  LTP_2084284EEECEEAC0:
  - tkill
  LTP_208C833FF12217F5:
  - capget
  LTP_20CE8BA111311B3B:
  - access
  LTP_20DA453342D2F4AB:
  - fpathconf
  LTP_213EA37A2B59AB99:
  - ftruncate
  LTP_21E1D9035D6DF74B:
  - getsockopt
  LTP_225DA846BF111CDF:
  - epoll_wait
  LTP_23017C8E93EEED5E:
  - access
  LTP_2316B5E43A8809B0:
  - access
  LTP_239441432F72CF6C:
  - access
  LTP_23FC431E5AACA295:
  - mmap
  LTP_2433DF1752AE54B7:
  - fsconfig
  LTP_245110930B22BF5C:
  - flock
  LTP_248EACE09AACC5AD:
  - lgetxattr
  LTP_252DC2EE1F2FC3AC:
  - setpriority
  LTP_252F2FFC943C6CCB:
  - open_by_handle_at
  LTP_254CA9053175601F:
  - access
  LTP_2553A6069EE908FB:
  - dup
  LTP_2554AC2E46FC6A15:
  - getrlimit
  LTP_2591489AC5619A2C:
  - access
  LTP_26555A26680524AD:
  - getrlimit
  LTP_2668EE4D34576C49:
  - signalfd
  LTP_26AE3C69D80D35F8:
  - munmap
  LTP_2722827BC58E04CD:
  - cachestat
  LTP_273F672499C6852D:
  - access
  LTP_277FD467E5F1BF1C:
  - accept
  LTP_27BB10D3A420BC7D:
  - access
  LTP_287FBE05D7B30C6F:
  - ulimit
  LTP_296D3DD5B2B27A84:
  - pwritev2
  LTP_29873BE2A9AABFF4:
  - symlink
  LTP_29BB55727C5A5616:
  - read
  LTP_2A28494F77E0B173:
  - preadv2
  LTP_2A3276D2B0A31AC9:
  - madvise
  LTP_2AE73292A13647D5:
  - wait4
  LTP_2AEF04E122ED7DC9:
  - pathconf
  LTP_2AF2BC8B94FE2134:
  - access
  LTP_2AF5913113A326EF:
  - waitpid
  LTP_2B8471E586CDE6D7:
  - access
  LTP_2BB228E4FB7C7BEB:
  - access
  LTP_2BBDFB48EF060066:
  - fsconfig
  LTP_2BDE60C0E64B4DC8:
  - close
  LTP_2C266C6067333086:
  - read
  LTP_2C37BF2D4F1059A2:
  - msync
  LTP_2CB0A10A3E175A9C:
  - sched_getaffinity
  LTP_2D0446746669D31E:
  - cachestat
  LTP_2D0CADDE36D70080:
  - access
  LTP_2D13A66AD1AB0813:
  - mlock2
  LTP_2D1E25BD679B3494:
  - epoll_create
  LTP_2DC2EBC740EB7D7C:
  - access
  LTP_2E135F7478A355E8:
  - access
  LTP_2EF9C7EBEC450E9D:
  - symlink
  LTP_2F3E34FD672DBF34:
  - waitpid
  LTP_2F8A8DCF7F3AEB62:
  - access
  LTP_2FA1F12DE62C6A0F:
  - access
  LTP_2FD53CE9C8CF6CE7:
  - access
  LTP_3073AC57544A6A6A:
  - fchmodat
  LTP_30A4B4C40696905E:
  - lstat
  LTP_3152706321BA354E:
  - pwritev2
  LTP_317FC70FE2A58775:
  - access
  LTP_31D9D767D6888DDA:
  - close_range
  LTP_31F03C781DAB0AD2:
  - access
  LTP_326165BAA61906DB:
  - readlinkat
  LTP_32F2B22133BB52DD:
  - access
  LTP_332E6D2186F55A6F:
  - access
  LTP_336B0AA063AB645E:
  - setpriority
  LTP_337F129FE78A007D:
  - epoll_wait
  LTP_33C492F97B790AB8:
  - fpathconf
  LTP_33D137B9002503E5:
  - exit_group
  LTP_342F7EADB5D10802:
  - access
  LTP_3471B46784E57E93:
  - mlock2
  LTP_34A1F75164462203:
  - symlink
  LTP_34EC9FB9C9551214:
  - cachestat
  LTP_352394AAA6D49339:
  - getpgid
  LTP_35AF6D3F6FC0EA61:
  - move_mount
  LTP_3662829F538B7D97:
  - access
  LTP_3670635A7A7D4496:
  - access
  LTP_367A286E9FC81496:
  - getdents64
  LTP_3692C449569215B8:
  - access
  LTP_36E1AD5A78C2A50D:
  - madvise
  LTP_371BDA67CB8813FD:
  - fchmod
  LTP_3741A721C9C463D0:
  - getrlimit
  LTP_3743BC827FB4F981:
  - pidfd_open
  LTP_37C625BD7D7C5F1D:
  - dup3
  LTP_37CFADAF53B6AC9D:
  - poll
  LTP_37F4EFF424BB79B9:
  - setpgid
  LTP_380714557B4AE9D4:
  - madvise
  LTP_3839B158DA52269B:
  - access
  LTP_38B9BA93F16FBAAF:
  - seccomp
  LTP_38EE9A0047529979:
  - sendfile
  LTP_39715C70E797C1B1:
  - faccessat2
  LTP_39B1E5C574F2D3DC:
  - sendfile
  LTP_39B7A82AB3626707:
  - access
  LTP_3A0AAE966297CCA7:
  - access
  LTP_3A18518E9A9DDC47:
  - mincore
  LTP_3A7B17AF231D4158:
  - dup3
  LTP_3AD21C6E4A19DB15:
  - ulimit
  LTP_3B07E4E263BECEDE:
  - readlinkat
  LTP_3B1458E6E26CBB53:
  - getrlimit
  LTP_3B48FBCC62838D3A:
  - access
  LTP_3B4D19754C5D1638:
  - ulimit
  LTP_3BA6F828CDE1E2E6:
  - access
  LTP_3C1DCCC4E6DCC76B:
  - sendfile
  LTP_3C4C8CA4ED44FE57:
  - getdomainname
  LTP_3C8D01B8140DB122:
  - faccessat2
  LTP_3D50FA09D36623FF:
  - fsconfig
  LTP_3D8EEC7BCE259B85:
  - access
  LTP_3DDCD08519809A17:
  - getsockopt
  LTP_3E0472B66C2C5AB3:
  - access
  LTP_3E8DA9E014B82702:
  - alarm
  LTP_3E9AD2C1B3BE9041:
  - execveat
  LTP_3EB53CD0B1672EE5:
  - preadv2
  LTP_3F00E13306997358:
  - getdents64
  LTP_3F7F517D8AA3614C:
  - get_robust_list
  LTP_3F80E012EF9B4D7E:
  - access
  LTP_3FF54C2EFF286EF7:
  - open_by_handle_at
  LTP_403B654FD084895C:
  - poll
  LTP_40621A9DFAF6D232:
  - msync
  LTP_408787CB8F89AAF4:
  - move_mount
  LTP_40A45C5E82D7F4A1:
  - unshare
  LTP_40E02D5F6A601BC5:
  - preadv2
  LTP_4101795C27681AB4:
  - openat2
  LTP_412173E3E81DC995:
  - unshare
  LTP_4171AFC9C3FEC6E7:
  - access
  LTP_41AB796031F8E171:
  - access
  LTP_423E92D9328C2A39:
  - rt_sigprocmask
  LTP_425E5A3502541DE8:
  - close_range
  LTP_428573F9D490F227:
  - access
  LTP_428A6CFF573F0942:
  - utime
  LTP_4308D71D8BD6519D:
  - setpgid
  LTP_4321E1483FC39110:
  - access
  LTP_4323000B7A8D2E5D:
  - lstat
  LTP_437CFCD991A666C9:
  - faccessat2
  LTP_43D6C007093E3B31:
  - access
  LTP_43F303BEA895DBE0:
  - access
  LTP_4405BEE7215E1BBC:
  - pathconf
  LTP_44313BAA17BEB1AE:
  - access
  LTP_4494B70BBA693D42:
  - waitid
  LTP_44983CDE7F1A5F08:
  - access
  LTP_449986F83296A5CF:
  - access
  LTP_44DC5382746D773D:
  - setpriority
  LTP_45D731F7321AFF41:
  - readlinkat
  LTP_462CE9A88054B448:
  - mq_notify
  LTP_46401248F52AD892:
  - fsconfig
  LTP_46AA49209C30E739:
  - ftruncate
  LTP_46DC592FFC5E5C44:
  - mq_notify
  LTP_470C0966080C93EF:
  - fchmod
  LTP_472AAA35C7382B26:
  - accept
  LTP_47DFC97559CA29F8:
  - access
  LTP_4839FA2FBA6C97F5:
  - preadv2
  LTP_485A86C9CB172FBF:
  - rt_sigprocmask
  LTP_4883FC77EC1F2BB9:
  - epoll_wait
  LTP_4953FAD330ADE150:
  - epoll_ctl
  LTP_499A726F0D1EAB38:
  - access
  LTP_49A80712984D44C6:
  - epoll_create
  LTP_49ABEE42EF290FDC:
  - unshare
  LTP_49D5637777352E9B:
  - getsockname
  LTP_4A4F50B0E250249A:
  - msync
  LTP_4A5C15DAE55BBD2E:
  - sendfile
  LTP_4AF75A49B2F7AAB5:
  - munlock
  LTP_4B27C893C8E9111F:
  - access
  LTP_4B7BD75A450AC789:
  - access
  LTP_4BA2A081C3EB3304:
  - sched_setattr
  LTP_4BBF626715445EFC:
  - setpgid
  LTP_4BE43BC3E131100B:
  - access
  LTP_4C1F446C9C520B36:
  - faccessat2
  LTP_4C4EE05D029C81F3:
  - sendto
  LTP_4CA2527DAE947BFC:
  - access
  LTP_4CAA10F04475843A:
  - access
  LTP_4D5D0A94700C0B71:
  - readlinkat
  LTP_4D70641BCBFF1FC9:
  - access
  LTP_4D9D59CFB785EB0C:
  - munlock
  LTP_4E3E972D7735BC63:
  - open_by_handle_at
  LTP_4E45B0701D5BD8A7:
  - pwrite64
  LTP_4E728F2B93D7AF55:
  - access
  LTP_4F02ACC6E2F6B094:
  - dup2
  LTP_4F41926D0ED26FBA:
  - request_key
  LTP_4FAABB99B8EB0CE9:
  - fchmodat
  LTP_503160311D12E629:
  - setpgid
  LTP_505DF8E6B5595F9E:
  - madvise
  LTP_50634C72AABCB02C:
  - access
  LTP_50853944DA25B2E0:
  - setpriority
  LTP_50972E17C52A9EF6:
  - fsconfig
  LTP_50BD66A0A05AFE51:
  - pathconf
  LTP_511185D6DE2A63A0:
  - dup
  LTP_51E295101A9F4411:
  - mmap
  LTP_52CE7E6F9B5FF947:
  - getsockname
  LTP_52FC519F20674559:
  - kill
  LTP_532669DC3463015A:
  - access
  LTP_532E8E5A98C0A22D:
  - pathconf
  LTP_5350E2FAFAB0B884:
  - epoll_ctl
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
  LTP_54E5F3DA585FF826:
  - access
  LTP_5514C74D5CAA93A2:
  - mount_setattr
  LTP_5516B8A938B9C3A5:
  - uname
  LTP_5560FF1D5C7F4B90:
  - sgetmask
  LTP_557771AFA7D3CBA3:
  - access
  LTP_55D2492560C39AFD:
  - sigsuspend
  LTP_55D4EF674AFB4ED1:
  - fsconfig
  LTP_55EFF664BDCE3E21:
  - fsconfig
  LTP_5622491E8A2227F2:
  - eventfd
  LTP_56EB350905546953:
  - access
  LTP_57933F1DF2F98C34:
  - openat2
  LTP_579F2F9BF68FC287:
  - access
  LTP_5818495120E9862A:
  - sched_setaffinity
  LTP_582938D6E8E17DB3:
  - fpathconf
  LTP_585CC852338F38EE:
  - sched_setaffinity
  LTP_5883CD050463E9E8:
  - epoll_ctl
  LTP_58F749C9A4ACFFD3:
  - pwritev2
  LTP_592639F40E0FF63A:
  - mlock2
  LTP_59A85FEDCED7BE77:
  - munlock
  LTP_5A2ECF299444C403:
  - lgetxattr
  LTP_5A68AEA67C7612A0:
  - sendfile
  LTP_5A7E16725228EB1E:
  - madvise
  LTP_5AEA06C99B2F5E9A:
  - epoll_wait
  LTP_5B429657B5297267:
  - access
  LTP_5CC32725A40238D7:
  - get_robust_list
  LTP_5D7B8CB342508B94:
  - read
  LTP_5D8D2B3BEDA79604:
  - epoll_create1
  LTP_5DC368435F71390F:
  - fsconfig
  LTP_5DCAB1EE343F650B:
  - access
  LTP_5DCE40F2EE0477DD:
  - access
  LTP_5DD94B8446C50071:
  - mprotect
  LTP_5E1690FA7F57F981:
  - madvise
  LTP_5E2B9548D2D9F147:
  - mprotect
  LTP_5EE8091D4EA8F7AF:
  - preadv2
  LTP_5F1E8876185AED7D:
  - access
  LTP_5F2B89F71FACBDF3:
  - fchmodat2
  LTP_5F50BCA4675B4B03:
  - mount_setattr
  LTP_5FB40D053220B092:
  - openat2
  LTP_5FC4B14EE38910DA:
  - access
  LTP_60398013DD319A2E:
  - sigaction
  LTP_6090C26F5D5D8E5D:
  - fsconfig
  LTP_609D7178B8A77C1F:
  - flistxattr
  LTP_60B98F9136CDCB0B:
  - mprotect
  LTP_612BF74E1426528A:
  - sigaltstack
  LTP_614C018F61C078A0:
  - waitpid
  LTP_6174E3690A05F1CA:
  - mkdirat
  LTP_619E7A5A0D656A90:
  - poll
  LTP_621EC309C3A75722:
  - pathconf
  LTP_62CC9D9E2E3D7880:
  - access
  LTP_636EE8AC66A970F6:
  - sbrk
  LTP_639CB00D5B06579C:
  - access
  LTP_63E6527501A08F92:
  - ftruncate
  LTP_644B7DB483FF489B:
  - signalfd
  LTP_64668181C4066A0A:
  - madvise
  LTP_647D857E6AB3D942:
  - access
  LTP_650C93999DB128D6:
  - access
  LTP_652CE911B47794E0:
  - getrlimit
  LTP_6534585EC08425D6:
  - access
  LTP_658F21F428A67438:
  - lstat
  LTP_65B70356F06E31F8:
  - alarm
  LTP_661F97F83268E2F4:
  - fchmodat
  LTP_66AC645038FEFC7A:
  - swapon
  LTP_679924706FAFC4A5:
  - preadv2
  LTP_67D824D6D01AC3C8:
  - pathconf
  LTP_6882C814E58F3D3B:
  - madvise
  LTP_68933230FCEAA7D5:
  - access
  LTP_69919B72D9A02D03:
  - gettimeofday
  LTP_69DB4FB0496BC7A2:
  - settimeofday
  LTP_6A52E2C16AC64CEC:
  - madvise
  LTP_6A70899352D69A0B:
  - flock
  LTP_6AAFFF4DD70E39E2:
  - access
  LTP_6B29B31CE99466E6:
  - socket
  LTP_6BBDEE6D1B9C6D94:
  - access
  LTP_6C1DF45A5C274B15:
  - sigsuspend
  LTP_6C89FDE5BFD98590:
  - access
  LTP_6C8CC973DA350505:
  - nanosleep
  LTP_6D034F85A89B1FCF:
  - access
  LTP_6D195DDAB1BE2B57:
  - kill
  LTP_6D2D8585448FB760:
  - access
  LTP_6D74624C7ACACFFC:
  - access
  LTP_6DD85CE2E5952779:
  - msync
  LTP_6DF55FF20A44572D:
  - getpriority
  LTP_6E631BC61A5CEE12:
  - write
  LTP_6FFB17DB762F3167:
  - epoll_ctl
  LTP_701679DC8AD1E4FE:
  - chroot
  LTP_7061ECC5236C3D49:
  - pwrite64
  LTP_708F721FB3456F82:
  - fsconfig
  LTP_70A24E1D78959E54:
  - access
  LTP_70E5CA8341B80E83:
  - getcontext
  LTP_71C59FD029BDE7EC:
  - access
  LTP_71DD675C657FC49A:
  - rename
  LTP_724D6E370813285F:
  - epoll_wait
  LTP_726A6A667C79F568:
  - chroot
  LTP_729222947741DFD6:
  - getcwd
  LTP_72CB51010EB5642E:
  - access
  LTP_72CE32EF22E0AD18:
  - access
  LTP_738C27178BBCE2B1:
  - set_tid_address
  LTP_74C73CBABE325D5D:
  - waitid
  LTP_74D863031FEC1500:
  - mmap
  LTP_7516A82707F421A8:
  - access
  LTP_75354A42F83E3CAC:
  - pathconf
  LTP_753BDF43E7947404:
  - madvise
  LTP_757778388A97EE03:
  - setpriority
  LTP_75D52C5E9C93B6D7:
  - dup2
  LTP_762DED3BB55C0120:
  - access
  LTP_765C6BC355EC57B9:
  - access
  LTP_769389D69FDFA661:
  - tee
  LTP_76A9B6CF388A8609:
  - alarm
  LTP_76BFF56F735A0074:
  - close_range
  LTP_76D3B1710474AAC2:
  - copy_file_range
  LTP_7786636C200E9E5C:
  - lremovexattr
  LTP_779183F85F2C1278:
  - pathconf
  LTP_77C2FB4A0A9E30F2:
  - waitid
  LTP_7886070B1C145E5B:
  - access
  LTP_78A991C666EEFF75:
  - pwritev2
  LTP_78B9E649A9D3C278:
  - access
  LTP_791DEA825D66980B:
  - mmap
  LTP_79882F9E36FC9878:
  - unshare
  LTP_79D2E6DA4FED3FBC:
  - rt_sigprocmask
  LTP_7A6820B73D1C2059:
  - iopl
  LTP_7A74A699442CEB99:
  - brk
  LTP_7AF560F7F0432A01:
  - flistxattr
  LTP_7B0F966046AECA7E:
  - wait
  LTP_7B9FBEA6E7CF8A70:
  - gethostid
  LTP_7BB1BB36E9CF4892:
  - openat2
  LTP_7BC885B5878C95B6:
  - sendfile
  LTP_7C0B488884F6689C:
  - pwritev2
  LTP_7C67E10CB5F35EA2:
  - pathconf
  LTP_7C8CA0FD5D141A05:
  - epoll_wait
  LTP_7C995D43920E57D0:
  - mlock2
  LTP_7CA8BC18271AA973:
  - lstat
  LTP_7CD01664A3589136:
  - pidfd_open
  LTP_7D48AE1036A3CBE7:
  - uname
  LTP_7DDD8970DD3DE57B:
  - access
  LTP_7DFAC48A8971CFE3:
  - getrlimit
  LTP_7E14411F2FC9D9CF:
  - move_mount
  LTP_7E3E96A4962D78D4:
  - close
  LTP_7EB2F82BA2DF09A2:
  - poll
  LTP_7ECC43C03A3DCB14:
  - fsconfig
  LTP_7ED6923454F08CDA:
  - rename
  LTP_7F0FE233BE49C811:
  - read
  LTP_7FC732FCCE410925:
  - rename
  LTP_7FCEEF8C37201FC7:
  - fsconfig
  LTP_7FD1D8A10AC952F2:
  - fsconfig
  LTP_7FDF0704C50C872E:
  - pathconf
  LTP_7FEB3B276A8133AC:
  - openat2
  LTP_804841A817CAA56C:
  - access
  LTP_80C28F63B3DFD8B1:
  - symlink
  LTP_80C6DB0ACB2A5510:
  - accept
  LTP_81F076122348B68A:
  - pathconf
  LTP_82479A4A2E248995:
  - epoll_ctl
  LTP_82677662F036B4D3:
  - access
  LTP_828E39231372A771:
  - mq_notify
  LTP_82907DD83DFD7800:
  - preadv2
  LTP_82D99A9CBFB63C68:
  - execveat
  LTP_82E0F55AEC3D382F:
  - access
  LTP_832A284618144115:
  - access
  LTP_835C2BD8D8081213:
  - readlinkat
  LTP_83709E56D6285F71:
  - epoll_ctl
  LTP_83A8BCF4DE700304:
  - access
  LTP_83B1DE66214C655F:
  - rename
  LTP_83EECC6B473A4EE0:
  - access
  LTP_8405B02758433FBC:
  - openat2
  LTP_84DBE108A850E845:
  - dup
  LTP_85742F5EC5C0112F:
  - write
  LTP_85A46F77356C5F87:
  - access
  LTP_85C6DC212C979199:
  - access
  LTP_85DC9A2EA2A956D8:
  - access
  LTP_86E98E40777EA3FA:
  - mprotect
  LTP_86F208D4521003A5:
  - access
  LTP_8703114C595382AB:
  - madvise
  LTP_8731C07ADFDC57F6:
  - mlock2
  LTP_875F17F6F720BEC2:
  - fstat
  LTP_88D0821E4776E388:
  - fsconfig
  LTP_88D300A8FB407324:
  - getpriority
  LTP_88E657C0C8F3084A:
  - access
  LTP_896519C6DE4DC296:
  - access
  LTP_8988E5015778894A:
  - getrlimit
  LTP_8A337DE81B7EE722:
  - madvise
  LTP_8A4C03F737A3CEE6:
  - fchmodat
  LTP_8AD8032754BC8842:
  - cacheflush
  LTP_8B95C6DD7983D3F3:
  - sched_getattr
  LTP_8BCA62F97A197BC2:
  - getsockopt
  LTP_8BDD5A2DD306EFC4:
  - signalfd
  LTP_8C1C2578972FCA1D:
  - getpgid
  LTP_8C2F2999FBFE056D:
  - lstat
  LTP_8C5755D366EB8CD2:
  - utime
  LTP_8CCE8FA5BFCCA106:
  - access
  LTP_8CF830DB0473B27D:
  - get_robust_list
  LTP_8CFEBBA603A7011A:
  - ssetmask
  LTP_8D2608F53A58B89C:
  - readlinkat
  LTP_8D75172B4EFCA5AB:
  - access
  LTP_8D95C734339E42C6:
  - settimeofday
  LTP_8E4283FE2952D57B:
  - access
  LTP_8E8D0AAC302EAE64:
  - access
  LTP_8EBCB5DB4F08A9DD:
  - access
  LTP_8ED8688C6292FECF:
  - symlink
  LTP_8EEF6B34A8A62DDA:
  - access
  LTP_8F0EEAFC8315D3BC:
  - access
  LTP_90893935E64240AA:
  - getpagesize
  LTP_90AA1F0CFA6C6A5C:
  - sendfile
  LTP_90D9067DABAD1253:
  - gettimeofday
  LTP_910B0D26D7722DBE:
  - access
  LTP_9116D4EE494E16DA:
  - access
  LTP_913EC5DF431DC6C2:
  - pathconf
  LTP_914935DA5C379DA1:
  - getrlimit
  LTP_91664E8E6FF0FCE1:
  - symlink
  LTP_91ED7E85761CE00F:
  - getrlimit
  LTP_91FBCF218DE6C917:
  - access
  LTP_922E84FFC658D432:
  - access
  LTP_9244F92CE966130C:
  - epoll_wait
  LTP_9256D223D5EF4AF0:
  - flock
  LTP_92652DA4B873A330:
  - access
  LTP_9305FA6D8B835652:
  - getrlimit
  LTP_933D919373F0F77C:
  - setpriority
  LTP_938E8BF5D2E7106E:
  - chroot
  LTP_93F2091ECF31C3E0:
  - preadv2
  LTP_9403699F671CF95F:
  - access
  LTP_9445A602B4F98B83:
  - pathconf
  LTP_9461AA782926BAB4:
  - getpgid
  LTP_947B3CCE7DA0998E:
  - mq_notify
  LTP_9495272A3179B794:
  - mmap
  LTP_95C156C7EBB823A1:
  - sched_getattr
  LTP_95C3A1596DE75C5C:
  - rename
  LTP_963EAEB0B41C7934:
  - fpathconf
  LTP_9672C6DE0FC3E7D0:
  - epoll_ctl
  LTP_969660F14B0B297A:
  - listxattr
  LTP_96B52F0F7B6F6E00:
  - access
  LTP_96B67F0F28B0192F:
  - access
  LTP_96C057F70BA4F5B9:
  - getdents64
  LTP_96E9B8F051D51566:
  - access
  LTP_971DB17D32C51561:
  - socket
  LTP_97C6508AAB3F5CF3:
  - access
  LTP_97D64C0E53AA3FA4:
  - sched_setaffinity
  LTP_9847441A67CBCED8:
  - madvise
  LTP_989BADB4E671AAC2:
  - access
  LTP_98A871A86ACC8672:
  - faccessat2
  LTP_98EC66149EE68933:
  - alarm
  LTP_9951A69B869BED04:
  - access
  LTP_998F62DFD40943B2:
  - mlock2
  LTP_99C45ECA20496C98:
  - getpriority
  LTP_99C641DE1B23D6C1:
  - access
  LTP_9AA9FA96C34FAB9E:
  - access
  LTP_9B0BA3ADF46F5FF4:
  - getpriority
  LTP_9B3646398697EA64:
  - dup3
  LTP_9B36D27A4A2994D0:
  - timer_delete
  LTP_9BA35A8C11698D49:
  - access
  LTP_9BFDDF855EC51FDA:
  - lgetxattr
  LTP_9C2FB7732A0B90B6:
  - waitid
  LTP_9CA9C6B61C3317A3:
  - accept
  LTP_9D4E5ED344B5751D:
  - setpriority
  LTP_9E1134B051A31DAD:
  - lstat
  LTP_9E17BDBD53A1AC97:
  - pread64
  LTP_9E2C65A6408DD9D3:
  - pause
  LTP_9E5F965A018077D2:
  - fchdir
  LTP_9F30FD7002BC2EBA:
  - read
  LTP_9F4ADF825E143585:
  - access
  LTP_9F51EEE16C61FFB8:
  - chroot
  LTP_9F560A103CB6F910:
  - dup2
  LTP_9F5D09B41AC183E5:
  - access
  LTP_9FAB1B9A02F7CAF0:
  - getcwd
  LTP_9FC19C1455EBA67E:
  - setpgid
  LTP_9FC3886A5E9A0CDF:
  - access
  LTP_9FD87A3F7688FEF1:
  - waitid
  LTP_9FE663EAF1F0ABCF:
  - fsconfig
  LTP_A0547B601C515355:
  - getrlimit
  LTP_A0CEB16379D94371:
  - access
  LTP_A1024CD742C433A3:
  - access
  LTP_A1AECDF3F41769B2:
  - times
  LTP_A1B6FBC6EF800331:
  - fchmod
  LTP_A2A80201A4364230:
  - flock
  LTP_A2E3A27D541DED02:
  - kill
  LTP_A3187FBB07FD0E35:
  - symlink
  LTP_A367723236ADA8B4:
  - sysinfo
  LTP_A38793D253A9BE8C:
  - readlinkat
  LTP_A448981C368F9EBB:
  - waitpid
  LTP_A48010DFDC346FDE:
  - open_by_handle_at
  LTP_A49B95E01ADFC6F8:
  - sendfile
  LTP_A49D802FF404EADA:
  - access
  LTP_A4A662687B98D33F:
  - socket
  LTP_A54F3585CC70C99F:
  - sendfile
  LTP_A55106AB533523B0:
  - sched_setattr
  LTP_A5952E2BE90138F8:
  - get_robust_list
  LTP_A5BD16DDF641E0B7:
  - getsockname
  LTP_A5BD363654740DDE:
  - read
  LTP_A684365768862744:
  - access
  LTP_A774FC10727E8ED2:
  - dup
  LTP_A7D8EAF1CE0F1A9B:
  - access
  LTP_A8161E50B040AFC9:
  - rename
  LTP_A82CC878A661AA28:
  - getpgrp
  LTP_A86F28C4D1358669:
  - request_key
  LTP_A89D10D41C3C2A1C:
  - set_robust_list
  LTP_A8C7B3D7AF1FA55E:
  - lgetxattr
  LTP_A94C8185C529647D:
  - getsockopt
  LTP_A9833E2E2860A6B7:
  - access
  LTP_A9A7BAA6186D57BD:
  - access
  LTP_A9BC7EBC1784A722:
  - sched_yield
  LTP_A9DD0D461E032A07:
  - fsconfig
  LTP_AA6F0F0A8A469B13:
  - readahead
  LTP_AA8CF336E764C8A7:
  - access
  LTP_AA8D903F4610FB06:
  - access
  LTP_AA8EF9120C0B6329:
  - fchmodat2
  LTP_AA9171FB32FD0C67:
  - getsockname
  LTP_AACDFBA8019E2D25:
  - tee
  LTP_AADEDDF7D9C31F91:
  - lgetxattr
  LTP_AB8173921096C9EE:
  - access
  LTP_ABCBF7DF0ADCB22A:
  - access
  LTP_AC02B3D548635386:
  - access
  LTP_AC7D82691053FF4D:
  - fsconfig
  LTP_AC9BF5A9B41CD255:
  - pwrite64
  LTP_ACF7A30AF3B10973:
  - execveat
  LTP_AD3A4B98FF201ABE:
  - wait
  LTP_ADEB5FE2DF97542A:
  - epoll_ctl
  LTP_AE4AAF77935210BC:
  - madvise
  LTP_AE4CE76865CD4D6D:
  - flock
  LTP_AE66ABEA9F76F42F:
  - access
  LTP_AF0FA27496E3610E:
  - preadv2
  LTP_AF528A39B115F13D:
  - access
  LTP_AF52DA4E6DA2BC9B:
  - setpriority
  LTP_AF8D38878ED1A9DA:
  - socket
  LTP_AFDAD0AD4FE0E3FF:
  - munlock
  LTP_B058D6B9CBBB459D:
  - getrlimit
  LTP_B061BD44067799D7:
  - sigprocmask
  LTP_B06B0397728F35C3:
  - pwritev2
  LTP_B09A317822F38991:
  - rename
  LTP_B0C8B999421C6345:
  - fstat
  LTP_B1E03AECF1FB1196:
  - access
  LTP_B35AB626F46D66FB:
  - access
  LTP_B39DB8E167298745:
  - access
  LTP_B3F848BCBCBAB559:
  - epoll_wait
  LTP_B41BE95567D414C7:
  - epoll_ctl
  LTP_B4AADBA5EA4C395B:
  - fstat
  LTP_B4B9F07E1C1A3826:
  - fsconfig
  LTP_B4FD0E2B4B84F458:
  - fchmodat
  LTP_B549A3600766CD49:
  - settimeofday
  LTP_B54A4B6E6A4ABDD5:
  - access
  LTP_B5959FE5199E821F:
  - flock
  LTP_B5BC41E30C9E37B0:
  - access
  LTP_B5F7BCB7225002FC:
  - mmap
  LTP_B6D4B61FC2494298:
  - setpriority
  LTP_B6FE6370B024CFB8:
  - access
  LTP_B72405976D9F15E6:
  - getsockopt
  LTP_B7606EDCC1F1031F:
  - pidfd_send_signal
  LTP_B7A341967DF2BD69:
  - alarm
  LTP_B7B7B035608D3637:
  - openat2
  LTP_B7F51635806E7E59:
  - dup2
  LTP_B87A5B8BC5B062AA:
  - access
  LTP_B8A61982E829826E:
  - munlock
  LTP_B8EA21096E591EBB:
  - flock
  LTP_B90CB73F36B70C6F:
  - accept
  LTP_BA9A8FE901467960:
  - cachestat
  LTP_BAA1410033A7464D:
  - utime
  LTP_BADA0A131C4F383E:
  - pwritev2
  LTP_BB1FF3530CCDDBB3:
  - access
  LTP_BB4C88C7C212DAC7:
  - setpriority
  LTP_BBDCACF4AE2FEB1D:
  - access
  LTP_BC4FACB4E14118C5:
  - settimeofday
  LTP_BCC58FBC10C684E2:
  - access
  LTP_BCF478535204545E:
  - access
  LTP_BD5C209F4C6EE910:
  - getrlimit
  LTP_BDA36F61423EEB3E:
  - dup2
  LTP_BDA884D4BEFE09C9:
  - pwritev2
  LTP_BDB9250DD17C3225:
  - preadv2
  LTP_BF183AB6911D1BAF:
  - fstatfs
  LTP_BF2428964ADD116F:
  - close
  LTP_BF31641F04151F3C:
  - pathconf
  LTP_BF3532E2FF5C89A0:
  - access
  LTP_BF679B7A7E60BCFD:
  - fpathconf
  LTP_BF696EFB140C9DAF:
  - access
  LTP_BF8A721AF501F7AD:
  - readlinkat
  LTP_BFCEAB073A576D51:
  - madvise
  LTP_BFFEED9C08C13250:
  - gethostname
  LTP_C04292C48EC89063:
  - fstatfs
  LTP_C05360D699C55915:
  - mlock
  LTP_C05A62F05F2C22E1:
  - pwritev2
  LTP_C09E83BE36885312:
  - gethostname
  LTP_C12A995BA4553344:
  - madvise
  LTP_C13C4F63D58904BC:
  - waitid
  LTP_C1462BACF46A177B:
  - madvise
  LTP_C1C97EB1E917FD3D:
  - fchmodat2
  LTP_C1D8DC20331CC18C:
  - access
  LTP_C218D3CB0AD80D90:
  - cacheflush
  LTP_C24E55F06625D564:
  - wait4
  LTP_C2909AC2ECEDED94:
  - faccessat2
  LTP_C3FF5FE7F694FFE6:
  - access
  LTP_C477F05C84F3C00D:
  - access
  LTP_C5088C2E9DB5306A:
  - access
  LTP_C532732193F3A009:
  - rename
  LTP_C544BF068942E8F7:
  - pathconf
  LTP_C58F92F1259E1474:
  - mkdirat
  LTP_C622170DA67BA6E3:
  - access
  LTP_C678E0C87280F82D:
  - fsconfig
  LTP_C6B4E04E7671DF4C:
  - getsockopt
  LTP_C785774773FB7524:
  - alarm
  LTP_C7C0FBBB9024C112:
  - access
  LTP_C87041F4B4B5A930:
  - pathconf
  LTP_C894288BC38DB82C:
  - getdents64
  LTP_C8C667C37A069984:
  - read
  LTP_C92D3BC9579570DA:
  - getrlimit
  LTP_C93391BCF53E8020:
  - kill
  LTP_CB0D3A27CA90726B:
  - write
  LTP_CB319D75C5C1E14F:
  - utime
  LTP_CB42FAF7C1D6D702:
  - sbrk
  LTP_CB84D44C84EB80BE:
  - sendfile
  LTP_CBB1680336D53D2A:
  - epoll_ctl
  LTP_CBD286AFB66B79D0:
  - epoll_ctl
  LTP_CBF4B6C8A1458A28:
  - close_range
  LTP_CC32503F19BF5D53:
  - pwrite64
  LTP_CC6A74384D72A70D:
  - access
  LTP_CCC36F43E9463D3E:
  - fchdir
  LTP_CD06BB76866E1C4F:
  - access
  LTP_CD3A79551F6773E4:
  - mkdirat
  LTP_CDDBF220A7C01FEA:
  - access
  LTP_CEE8E7C01B4D8059:
  - madvise
  LTP_CF4E59775301DA7C:
  - openat2
  LTP_CF7B49C4B74D69E7:
  - setpgid
  LTP_D01667E52BF34BFC:
  - sendfile
  LTP_D0578B9D5D177037:
  - access
  LTP_D071740A6BE2DE31:
  - access
  LTP_D0800876342DE939:
  - openat2
  LTP_D0A69D14ADE1718C:
  - msync
  LTP_D0BAC1CBF594EDA6:
  - madvise
  LTP_D0E55E3A04E47FFC:
  - faccessat2
  LTP_D17799C1BB191952:
  - rename
  LTP_D1A18560E485E146:
  - waitid
  LTP_D1DAB36EB37FCA27:
  - fpathconf
  LTP_D1DE0D497F2B612D:
  - access
  LTP_D23BA34DB5624198:
  - sched_setaffinity
  LTP_D296A517F138A0C0:
  - dup2
  LTP_D297A923D4C5FEC7:
  - mq_notify
  LTP_D2E2A5F40B2313E5:
  - msync
  LTP_D339D6D98B843BEA:
  - mkdirat
  LTP_D3B68F2DFB1C45D5:
  - access
  LTP_D3E85F64C28BBC4F:
  - sendfile
  LTP_D579FCFC71E6EB6A:
  - cacheflush
  LTP_D5BD925DC43E7564:
  - readlinkat
  LTP_D5D78F93265A1980:
  - fsconfig
  LTP_D615E29C0C4C9CCB:
  - fsconfig
  LTP_D63AFAA6729CB519:
  - flock
  LTP_D696A4996FBE61CF:
  - access
  LTP_D744D6C4A0C3E40C:
  - munmap
  LTP_D74B8D7A215A601E:
  - move_mount
  LTP_D75F86A534CB6E02:
  - epoll_wait
  LTP_D77858597BCC1C13:
  - faccessat2
  LTP_D77AD0D4DC9C0C9E:
  - getsockopt
  LTP_D7B9E8F8F713AADA:
  - rename
  LTP_D839FF9444196DDB:
  - madvise
  LTP_D8BB97A8EDA10C0B:
  - chroot
  LTP_D8D1EEF145FEB5EA:
  - access
  LTP_D8F99518FF4E8643:
  - symlink
  LTP_D90C4B47C5FF6BC9:
  - request_key
  LTP_D90E4279570B6A94:
  - madvise
  LTP_D95376E3B0469608:
  - pread64
  LTP_D98D789F4EBA6817:
  - rename
  LTP_D9B6B53AB6CA3BE3:
  - readahead
  LTP_D9ED751DFFC3CC63:
  - fchmodat
  LTP_DA61AB6388EB2D13:
  - rename
  LTP_DA64FD04E43656E6:
  - waitid
  LTP_DA8094714BA3F734:
  - getpgid
  LTP_DB6066C00D231BA4:
  - copy_file_range
  LTP_DBAE060B9CA303DD:
  - pwritev2
  LTP_DBEC3975C5440D23:
  - setpgid
  LTP_DBFBE6A110B3D17B:
  - getsockname
  LTP_DC01A8115E3EC579:
  - fstatfs
  LTP_DC3D9E7D5D1A75DE:
  - preadv2
  LTP_DC7E9134BB7F6F7A:
  - sched_setattr
  LTP_DC994CB22DEE5DE8:
  - access
  LTP_DCAED55A4DA05C29:
  - access
  LTP_DD227DB33548452D:
  - openat2
  LTP_DD2E1A555B603C7B:
  - socket
  LTP_DD64353E8E427275:
  - pathconf
  LTP_DD70936BEB737A0F:
  - access
  LTP_DDC2A75ACE241003:
  - rename
  LTP_DDCD82CA2726175D:
  - nanosleep
  LTP_DE6F80C5EFE44A9D:
  - dup2
  LTP_DEB4A4BEB59AD7A4:
  - getdents64
  LTP_DEF59E8529DC9CD8:
  - access
  LTP_DF5B725563FDFB31:
  - waitid
  LTP_E00D911A632EB8C8:
  - mlock
  LTP_E0470C189C2D1DE3:
  - set_robust_list
  LTP_E0F28EAB0253204C:
  - access
  LTP_E13B9C2C9645B841:
  - accept
  LTP_E20E7069E7FA34D5:
  - munmap
  LTP_E2360C045F1BCE8E:
  - preadv2
  LTP_E2AC7688287A2F9C:
  - realpath
  LTP_E2D73477ACB0308D:
  - setegid
  LTP_E2D7E49A9D6EDA47:
  - access
  LTP_E2EEBD0885B0F3EC:
  - getsockopt
  LTP_E316C28E36E136DA:
  - socket
  LTP_E3B5C7908A7B12CC:
  - mq_notify
  LTP_E3BA4E4FAEF39F91:
  - getsid
  LTP_E3E59B16A96A60BC:
  - brk
  LTP_E520E500AB3AE851:
  - close
  LTP_E564AACFFDAA71E1:
  - gettimeofday
  LTP_E5E64FCDA6CACABE:
  - pidfd_open
  LTP_E61711880DE479B0:
  - pwrite64
  LTP_E6750A641272AF1B:
  - fsconfig
  LTP_E6A7D5E5327D8ECC:
  - pidfd_getfd
  LTP_E6C69C9F4AB565BC:
  - getrlimit
  LTP_E733F750B1F4008F:
  - readlinkat
  LTP_E7435E0CBCA319E1:
  - epoll_create
  LTP_E7761F889A77DB75:
  - flistxattr
  LTP_E7E64809057630A5:
  - request_key
  LTP_E81373866A3C5AB3:
  - faccessat2
  LTP_E86DBD8C9AA9E82B:
  - access
  LTP_E8BA54C78A3F671D:
  - write
  LTP_E8D2C5525DC42DD1:
  - access
  LTP_E8E97EBE8E041CF0:
  - kill
  LTP_E9690AB9682FCE47:
  - lstat
  LTP_E98952E12501919D:
  - request_key
  LTP_E9D60674E416A5DC:
  - open_by_handle_at
  LTP_E9EC00862545876A:
  - access
  LTP_EA51441DF7A43596:
  - access
  LTP_EA58792F115B6235:
  - request_key
  LTP_EA90C626D9AA6C08:
  - msync
  LTP_EA953D5E5C4B2B1F:
  - getrlimit
  LTP_EAAD13B42BE1ED54:
  - fchmodat
  LTP_EB214534D857AE95:
  - ftruncate
  LTP_EB40C6ADD4390CB3:
  - munlockall
  LTP_EB646AEB1D23725B:
  - cachestat
  LTP_EBB107DB7E3EFF2A:
  - madvise
  LTP_EBCE1A2B8CE59ECE:
  - fsconfig
  LTP_ECD986F27CF15E1E:
  - waitid
  LTP_ED2BA909DF79625A:
  - dup
  LTP_ED8240DD1329BBA1:
  - ustat
  LTP_EDE65A5D9B99F21F:
  - access
  LTP_EE8E695CF61D6D8A:
  - dup2
  LTP_EECDB5C492A4B4BD:
  - access
  LTP_EF32B2CC0F6F3848:
  - utime
  LTP_EF9CD83ECACAA86C:
  - tkill
  LTP_EFF3EDE1EC749DE9:
  - access
  LTP_F02D3365DCF08927:
  - access
  LTP_F04C2129F0253CC0:
  - fchmodat
  LTP_F0BF53984C9E5C92:
  - sysinfo
  LTP_F122D4A7C853AEBF:
  - move_mount
  LTP_F1299BC5F92BF26E:
  - fchmod
  LTP_F13024AE4BC5C024:
  - kill
  LTP_F1DC44813DCA6A05:
  - close_range
  LTP_F21B2458879EFBAB:
  - ftruncate
  LTP_F26D09CAE258516C:
  - access
  LTP_F284E6C48F6B4BF8:
  - move_mount
  LTP_F2F310F9646CBB33:
  - mprotect
  LTP_F318E892720C2991:
  - msync
  LTP_F3CE94166822B3E3:
  - get_robust_list
  LTP_F421E1E61753B72C:
  - fchmod
  LTP_F4AE08B0C5A16088:
  - access
  LTP_F4DE81D703447628:
  - close_range
  LTP_F4FEC29E9271B119:
  - access
  LTP_F508E2594C0F3DC9:
  - access
  LTP_F5D2C7B7F0E3D07C:
  - getpgid
  LTP_F61B5384B4A60F55:
  - mlock
  LTP_F65E54AE96F20D41:
  - fchmodat2
  LTP_F66DDB5A0EBC5C9F:
  - fsconfig
  LTP_F6DD03A9DC1C07D4:
  - mkdirat
  LTP_F75110BE79864CD1:
  - ustat
  LTP_F7AC6006DC3C06BB:
  - mlock2
  LTP_F7B8EDE302D5D08A:
  - faccessat2
  LTP_F7EAB2DB74BE5612:
  - flistxattr
  LTP_F8FD511858BB650D:
  - getsid
  LTP_F9357233C6D73800:
  - getpgid
  LTP_F99DE159B75F22A2:
  - kill
  LTP_FA4A7CD85E7F31FE:
  - mprotect
  LTP_FA750E6088863E30:
  - sched_getattr
  LTP_FAB12DCB20BF08A2:
  - access
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
  LTP_FB7250E0E0E98949:
  - access
  LTP_FBEB6959ED2912C8:
  - iopl
  LTP_FC1E41C3414E7F21:
  - getcwd
  LTP_FC50E16C03A7EED9:
  - mlock
  LTP_FC5D8C19ECDBC380:
  - access
  LTP_FC8BA85373EA2D8F:
  - waitpid
  LTP_FCC236A4D5926B81:
  - tkill
  LTP_FCC82752F512BE72:
  - seccomp
  LTP_FCD03068DB9BC256:
  - pwritev2
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
  LTP_FE9B97F71E485E58:
  - mlock2
  LTP_FEACDC300C3E1DD7:
  - mmap
  LTP_FEDE14E9D4DE9A9D:
  - pathconf
  LTP_FF1A8A6101CEA37E:
  - fpathconf
  LTP_FF3F568195A91237:
  - readlinkat
  MAN_00103B28A6F5E08D:
  - bpf
  MAN_001A54DF9FC31CE8:
  - sched_get_priority_min
  MAN_001A54DF9FC31CE8--001a54df9fc3:
  - sched_get_priority_max
  MAN_003CD3763A978D04:
  - timerfd_gettime
  MAN_004335DB8973F3B4:
  - copy_file_range
  MAN_007841377EBEE116:
  - munlockall
  MAN_007841377EBEE116--007841377ebe:
  - mlock
  MAN_00948C3E86F6D71A:
  - socket
  MAN_0114490BA1B01D16:
  - setrlimit
  MAN_0119730CE00C10B5:
  - flock
  MAN_01387ECF64F15BAA:
  - move_mount
  MAN_015E54306EC1E211:
  - clock_adjtime
  MAN_015E54306EC1E211--015e54306ec1:
  - adjtimex
  MAN_016AFBB64F425E24:
  - fanotify_mark
  MAN_0170239FF6930B4E:
  - fchmodat
  MAN_0170239FF6930B4E--0170239ff693:
  - fchmod
  MAN_01C5D96796AD018A:
  - open_tree
  MAN_01CA9DE78E411292:
  - personality
  MAN_0209C28D93D8F5F5:
  - sched_setaffinity
  MAN_0209C28D93D8F5F5--0209c28d93d8:
  - sched_getaffinity
  MAN_0214648CC92CE254:
  - fchownat
  MAN_02308C659518B681:
  - setresuid
  MAN_02308C659518B681--02308c659518:
  - setresgid
  MAN_0236084E65503DBE:
  - mount_setattr
  MAN_023A091A450869AB:
  - statx
  MAN_025048B2C8FABCB8:
  - acct
  MAN_025E20A22A4414CE:
  - openat
  MAN_027D17C587997F75:
  - setdomainname
  MAN_02841D256D8D8D75:
  - add_key
  MAN_0285048F3B9BB9F5:
  - seccomp
  MAN_02D94DE028E9D2AA:
  - sched_rr_get_interval
  MAN_02D976F1ED01493F:
  - seccomp
  MAN_02DBDB23A5B5EB06:
  - munlockall
  MAN_02DBDB23A5B5EB06--02dbdb23a5b5:
  - mlock
  MAN_030D3A5D9EC1271B:
  - move_pages
  MAN_032D5B34C1754A1A:
  - mq_open
  MAN_0341B3D90B22FCCC:
  - unshare
  MAN_034417B2380A057E:
  - readlinkat
  MAN_0394E66422CE04BA:
  - delete_module
  MAN_03973C9BB4FFF9D2:
  - linkat
  MAN_03A1619903E49673:
  - fchmodat
  MAN_03AB8AFA730972F9:
  - perf_event_open
  MAN_03E8B237E962C1D2:
  - reboot
  MAN_04107E81740E9ACA:
  - openat
  MAN_04130DE97E2698FF:
  - fanotify_init
  MAN_045719AC8992819E:
  - setpgid
  MAN_045719AC8992819E--045719ac8992:
  - getpgid
  MAN_049E980341F23FEB:
  - fallocate
  MAN_0576653A58701CC6:
  - syslog
  MAN_05B0FC46D68F4F6D:
  - swapoff
  MAN_05BDBAF2B17488EC:
  - recvmsg
  MAN_05C23E092147A21E:
  - fchdir
  MAN_05C23E092147A21E--05c23e092147:
  - chdir
  MAN_05C898B72CED937B:
  - execve
  MAN_05C8C3529909FA84:
  - getrandom
  MAN_05DE168D7DB0802B:
  - landlock_add_rule
  MAN_060281D47FA8D7BC:
  - linkat
  MAN_060C6C9300CD33C3:
  - landlock_restrict_self
  MAN_060E5AEB84CE74A5:
  - renameat2
  MAN_061B988A427EE9B5:
  - copy_file_range
  MAN_062878027C124D38:
  - io_setup
  MAN_0660C9FF6807093E:
  - execveat
  MAN_0688D8D326509E18:
  - sync_file_range
  MAN_06BCAA4A9250F3F9:
  - fanotify_mark
  MAN_06DC94E90357CD37:
  - umount2
  MAN_06EB3DF49B85FDDB:
  - mount_setattr
  MAN_06EF9821B3C4C6BA:
  - splice
  MAN_071F158EABFC6786:
  - mkdirat
  MAN_073953AAA1410D13:
  - mq_open
  MAN_0752801C163AD8EF:
  - io_getevents
  MAN_076563B373453FBB:
  - linkat
  MAN_07C18A1F5C6914D1:
  - accept4
  MAN_07C18A1F5C6914D1--07c18a1f5c69:
  - accept
  MAN_07CED4F4ACE46242:
  - fchownat
  MAN_07CED4F4ACE46242--07ced4f4ace4:
  - fchown
  MAN_07DF43D0B2066386:
  - execve
  MAN_07ECD8D557265C44:
  - openat
  MAN_07FC0F0D29626BD3:
  - mknodat
  MAN_08038D4021D9C0AA:
  - openat2
  MAN_080B5B5A8F037D7E:
  - kexec_load
  MAN_080B5B5A8F037D7E--080b5b5a8f03:
  - kexec_file_load
  MAN_081D5A08DD9F1477:
  - futex_waitv
  MAN_083368964C7623C0:
  - setdomainname
  MAN_0848356E88B0CF90:
  - signalfd4
  MAN_0848BBF3B84EC796:
  - clone3
  MAN_08490603D39D1972:
  - move_pages
  MAN_084C1EB2D48076CC:
  - statmount
  MAN_08AB3279C1E9108A:
  - splice
  MAN_08B9AC95AA0F1872:
  - readlinkat
  MAN_08ED6E381FEA31E4:
  - openat2
  MAN_08FD6D3E2365FC1C:
  - process_vm_writev
  MAN_08FD6D3E2365FC1C--08fd6d3e2365:
  - process_vm_readv
  MAN_090A017448A1D26E:
  - renameat2
  MAN_091DF0CC098B42B6:
  - acct
  MAN_094BE7407163CD3C:
  - socketpair
  MAN_0951CFFF722E97A8:
  - lookup_dcookie
  MAN_0985C968EEE2B273:
  - msgsnd
  MAN_0985C968EEE2B273--0985c968eee2:
  - msgrcv
  MAN_09A35C27731E7D6C:
  - dup3
  MAN_09D1510C81523F39:
  - sched_setparam
  MAN_09E77998CF96F0B2:
  - mkdirat
  MAN_09FBBE5A1DA918C2:
  - perf_event_open
  MAN_0A219C36086EFF79:
  - connect
  MAN_0A958131FE158000:
  - epoll_create1
  MAN_0AA82EE1C8565C78:
  - bind
  MAN_0AAF2419366FC25E:
  - fanotify_mark
  MAN_0AD66E58A6BF8BB3:
  - quotactl_fd
  MAN_0AD66E58A6BF8BB3--0ad66e58a6bf:
  - quotactl
  MAN_0AD8DB8161C0C75B:
  - landlock_restrict_self
  MAN_0AE9F6A19729C7D2:
  - accept4
  MAN_0AE9F6A19729C7D2--0ae9f6a19729:
  - accept
  MAN_0B1567EB33F0D067:
  - fanotify_mark
  MAN_0B167B276CAE7738:
  - futex_waitv
  MAN_0B5705FDF2C002BE:
  - perf_event_open
  MAN_0B67057F4DF5AD34:
  - openat2
  MAN_0B80140A5428B618:
  - write
  MAN_0B8B602E47C474DE:
  - listxattr
  MAN_0BA66331CB4B2091:
  - pidfd_open
  MAN_0BA7A1835677B5EB:
  - mlockall
  MAN_0BB78F87CD6FB8CD:
  - getsockname
  MAN_0BCFD228C40FCB63:
  - cachestat
  MAN_0C00158F30B4ACC1:
  - openat2
  MAN_0C1233CB7F118FAB:
  - openat
  MAN_0C135305A1B0B069:
  - symlinkat
  MAN_0C54653F18526D07:
  - writev
  MAN_0C54653F18526D07--0c54653f1852:
  - preadv
  MAN_0C8B272D1F7D5D96:
  - clock_settime
  MAN_0C8B272D1F7D5D96--0c8b272d1f7d:
  - clock_getres
  MAN_0C972F0DECC46757:
  - fanotify_mark
  MAN_0CAF71ABB038A13B:
  - connect
  MAN_0CB3AC538D6FF417:
  - perf_event_open
  MAN_0CE22931C51803E9:
  - fchmod
  MAN_0CF0F09EAB24DE1F:
  - tee
  MAN_0D338B630FBDA7E4:
  - open_by_handle_at
  MAN_0D338B630FBDA7E4--0d338b630fbd:
  - name_to_handle_at
  MAN_0D6118B4E3D721DC:
  - fchdir
  MAN_0D6118B4E3D721DC--0d6118b4e3d7:
  - chdir
  MAN_0D73DC6A7D1F8DED:
  - clone3
  MAN_0D73DC6A7D1F8DED--0d73dc6a7d1f:
  - clone
  MAN_0D95EDCC005BD935:
  - timer_create
  MAN_0D9E79AEB44B7510:
  - getcwd
  MAN_0E1E00FAC83DFEEA:
  - statmount
  MAN_0E9ACF30258A85E0:
  - open_tree
  MAN_0ECA28836E826421:
  - setpgid
  MAN_0EEE801F78C405AB:
  - open_by_handle_at
  MAN_0EEE801F78C405AB--0eee801f78c4:
  - name_to_handle_at
  MAN_0F286F1FE274A8E9:
  - msgsnd
  MAN_0F286F1FE274A8E9--0f286f1fe274:
  - msgrcv
  MAN_0F2C1ABA8AF5C15E:
  - setgroups
  MAN_0F2C1ABA8AF5C15E--0f2c1aba8af5:
  - getgroups
  MAN_0F9C19C106091F39:
  - fspick
  MAN_0FAD3468E26A75AA:
  - futex
  MAN_0FB46032412499A3:
  - open_by_handle_at
  MAN_0FB46032412499A3--0fb460324124:
  - name_to_handle_at
  MAN_0FB5B0A9E82D9C13:
  - tkill
  MAN_0FB5B0A9E82D9C13--0fb5b0a9e82d:
  - tgkill
  MAN_0FBFE027E29A7E90:
  - set_robust_list
  MAN_0FBFE027E29A7E90--0fbfe027e29a:
  - get_robust_list
  MAN_100237405024E5A8:
  - mq_unlink
  MAN_1010805F115C44E5:
  - symlinkat
  MAN_1013DB4ACEFF4120:
  - truncate
  MAN_1013DB4ACEFF4120--1013db4aceff:
  - ftruncate
  MAN_102306359DF71F2C:
  - fsconfig
  MAN_102F68125A825DE1:
  - sendto
  MAN_102F68125A825DE1--102f68125a82:
  - sendmsg
  MAN_1034AB80AF5590DD:
  - waitid
  MAN_108BE6B48C92E932:
  - mq_timedsend
  MAN_10C26765AA1ECF4D:
  - setxattr
  MAN_10C26765AA1ECF4D--10c26765aa1e:
  - fsetxattr
  MAN_10C3B8960C949F2E:
  - lseek
  MAN_10D913684986FD75:
  - process_vm_writev
  MAN_10D913684986FD75--10d913684986:
  - process_vm_readv
  MAN_1115E878B4F50CF3:
  - pipe2
  MAN_115E9A54ED8D67E1:
  - shmget
  MAN_117B1556465C7385:
  - openat
  MAN_117E8090B608AC24:
  - shutdown
  MAN_11D5B32238CD0471:
  - unshare
  MAN_1235204A56E78403:
  - fsconfig
  MAN_123B801F86215725:
  - clone
  MAN_1276F0CF91F8B2F4:
  - open_tree
  MAN_1306E9D30B932F05:
  - lgetxattr
  MAN_1306E9D30B932F05--1306e9d30b93:
  - fgetxattr
  MAN_1322BFB37B59679D:
  - request_key
  MAN_1346212782BF61C7:
  - setresuid
  MAN_137F47D445A31EC5:
  - io_getevents
  MAN_13B2203B3F3BB50A:
  - io_cancel
  MAN_13BEDBE5212B0601:
  - init_module
  MAN_13BEDBE5212B0601--13bedbe5212b:
  - finit_module
  MAN_13D3364A18069FCD:
  - statfs
  MAN_13E06375AFCB0967:
  - sched_setattr
  MAN_13E06375AFCB0967--13e06375afcb:
  - sched_getattr
  MAN_13EBCA9DECC049A9:
  - request_key
  MAN_140158F63072686C:
  - linkat
  MAN_140DB23EF5E23D56:
  - writev
  MAN_140DB23EF5E23D56--140db23ef5e2:
  - preadv
  MAN_141E34FD3B450827:
  - setrlimit
  MAN_141E34FD3B450827--141e34fd3b45:
  - getrlimit
  MAN_142A30F5EBF7CCE1:
  - accept4
  MAN_142A30F5EBF7CCE1--142a30f5ebf7:
  - accept
  MAN_145244EB383CB5F4:
  - futex_waitv
  MAN_146A8F5C379A64E2:
  - seccomp
  MAN_147EECDC5DAB119D:
  - faccessat2
  MAN_147EECDC5DAB119D--147eecdc5dab:
  - faccessat
  MAN_1491EC5355086E4E:
  - quotactl_fd
  MAN_1491EC5355086E4E--1491ec535508:
  - quotactl
  MAN_14A8EDF7140CC212:
  - msgsnd
  MAN_14A8EDF7140CC212--14a8edf7140c:
  - msgrcv
  MAN_14F98525705E7767:
  - init_module
  MAN_14F98525705E7767--14f98525705e:
  - finit_module
  MAN_1509E2071E4926B2:
  - read
  MAN_151A6D255AC246A1:
  - fchmodat
  MAN_151A6D255AC246A1--151a6d255ac2:
  - fchmod
  MAN_152CE1AA8F27494F:
  - clock_adjtime
  MAN_15530E372E989131:
  - fallocate
  MAN_158FD05242CE8351:
  - pidfd_getfd
  MAN_15AA32F3DACE7E1C:
  - inotify_init1
  MAN_15BA3F968F2743FD:
  - statx
  MAN_15F4B6F35A48841A:
  - prlimit64
  MAN_1607CAAD75C2A07D:
  - eventfd2
  MAN_161E4EF12C551F0F:
  - init_module
  MAN_161E4EF12C551F0F--161e4ef12c55:
  - finit_module
  MAN_168FD474472CC9B5:
  - open_tree
  MAN_16A397025AF31165:
  - chroot
  MAN_16BFBD0A7DC6F82C:
  - write
  MAN_16DF34CB3DEC5CD7:
  - fchownat
  MAN_16DF34CB3DEC5CD7--16df34cb3dec:
  - fchown
  MAN_17068E46E2A61A83:
  - clock_adjtime
  MAN_17068E46E2A61A83--17068e46e2a6:
  - adjtimex
  MAN_1752878977526B41:
  - setns
  MAN_17C538C135575FCE:
  - munlock
  MAN_17E3CD2547123D42:
  - sched_setattr
  MAN_17E3CD2547123D42--17e3cd254712:
  - sched_getattr
  MAN_17E5F8CE91A31E4A:
  - getrusage
  MAN_182A6A8E148341F1:
  - openat
  MAN_184542E313743E82:
  - process_madvise
  MAN_186BA8EB037F385B:
  - listmount
  MAN_18B3C82EAA89C160:
  - connect
  MAN_18C5488E8D09D6D2:
  - munmap
  MAN_18C5488E8D09D6D2--18c5488e8d09:
  - mmap
  MAN_18D7BFF5ED1AAF47:
  - dup3
  MAN_18D7BFF5ED1AAF47--18d7bff5ed1a:
  - dup
  MAN_194BF662957E49E3:
  - sendto
  MAN_194BF662957E49E3--194bf662957e:
  - sendmsg
  MAN_196CF33DE907C1A4:
  - open_tree
  MAN_19B4AA1EE4A6319C:
  - munmap
  MAN_19B4AA1EE4A6319C--19b4aa1ee4a6:
  - mmap
  MAN_1A4D408E72E87885:
  - semctl
  MAN_1A5EA44F4379EA91:
  - signalfd4
  MAN_1A7DF9D4B4186AB1:
  - truncate
  MAN_1A7DF9D4B4186AB1--1a7df9d4b418:
  - ftruncate
  MAN_1A81417216B4FB48:
  - futex
  MAN_1A99E033062CEF0C:
  - close_range
  MAN_1AA5473D7CB211E7:
  - getdents64
  MAN_1AB755AF85E81162:
  - lseek
  MAN_1AD15208BC1205CD:
  - mount
  MAN_1B09107973DFD85E:
  - delete_module
  MAN_1B94F364679B8706:
  - landlock_restrict_self
  MAN_1C0B0B2E7F7C934D:
  - mount_setattr
  MAN_1C0DA43350202758:
  - getdents64
  MAN_1C47588949214574:
  - readlinkat
  MAN_1C62C19FF51AA2AA:
  - mount
  MAN_1C8833834002BF0D:
  - sendto
  MAN_1C8833834002BF0D--1c8833834002:
  - sendmsg
  MAN_1CB51F6212BFE63E:
  - fsmount
  MAN_1D3BA7CB60EB5557:
  - getresuid
  MAN_1D3BA7CB60EB5557--1d3ba7cb60eb:
  - getresgid
  MAN_1D7057F3EF0B65DF:
  - shmctl
  MAN_1D92F98E3C8E6862:
  - pivot_root
  MAN_1D94CC28DA4FE0E2:
  - epoll_ctl
  MAN_1DBDA8BA316CDCFD:
  - bpf
  MAN_1DD4B4D3FE378ECB:
  - mount
  MAN_1DFD955F6DB12C96:
  - lookup_dcookie
  MAN_1E23EC8F003315AD:
  - kexec_load
  MAN_1E23EC8F003315AD--1e23ec8f0033:
  - kexec_file_load
  MAN_1E681BC36EB3A525:
  - move_mount
  MAN_1E7A18D70D0A3428:
  - fadvise64
  MAN_1E7D6152B61A65E7:
  - clone3
  MAN_1E7D6152B61A65E7--1e7d6152b61a:
  - clone
  MAN_1EAD062EE91686D0:
  - readlinkat
  MAN_1EDDC18B3A6DD197:
  - sync_file_range
  MAN_1EE163900A6A00FE:
  - kexec_load
  MAN_1EE163900A6A00FE--1ee163900a6a:
  - kexec_file_load
  MAN_1EE2F3F643D23CEA:
  - inotify_add_watch
  MAN_1EF42B309ED8194E:
  - utimensat
  MAN_1EFA395D2832F95E:
  - inotify_add_watch
  MAN_1F0BF9A93F70610A:
  - landlock_add_rule
  MAN_1F73471046165D23:
  - semget
  MAN_1F749FCEE6C9B402:
  - fanotify_init
  MAN_1F8638F0BD38CCDA:
  - recvmmsg
  MAN_1FFA45858B50B191:
  - clock_settime
  MAN_200B5022E9194258:
  - fchdir
  MAN_200B5022E9194258--200b5022e919:
  - chdir
  MAN_2022CD25472DA05E:
  - clock_settime
  MAN_202EF9D1C280FD44:
  - msgsnd
  MAN_202EF9D1C280FD44--202ef9d1c280:
  - msgrcv
  MAN_202FE92E9610C89C:
  - timer_create
  MAN_20340C4477D5D719:
  - shmdt
  MAN_20340C4477D5D719--20340c4477d5:
  - shmat
  MAN_2078363C7921ADFB:
  - sendfile
  MAN_208F2B7E2A37BB6A:
  - sync_file_range
  MAN_20929AB9853C5BA0:
  - kill
  MAN_20A10178D28B400B:
  - seccomp
  MAN_20D48FF8D6F2FB93:
  - faccessat2
  MAN_20D48FF8D6F2FB93--20d48ff8d6f2:
  - faccessat
  MAN_20D644B5C57002F8:
  - openat2
  MAN_20DC7720C2DC9974:
  - bpf
  MAN_20E72B974AE0878B:
  - fcntl
  MAN_210B5A9910A7CEA9:
  - msgsnd
  MAN_210B5A9910A7CEA9--210b5a9910a7:
  - msgrcv
  MAN_212564FB71548004:
  - madvise
  MAN_212E61F50AFDF2FB:
  - openat2
  MAN_21341086A8BADA52:
  - pidfd_send_signal
  MAN_2138716686607D9D:
  - msgget
  MAN_21390B5A5477ECE6:
  - mlockall
  MAN_217283AFA7CAA025:
  - symlinkat
  MAN_2178BF34327B5121:
  - move_pages
  MAN_21AFE5F1DBEB0A0A:
  - mlock2
  MAN_21B60AD7C0F6FC76:
  - faccessat2
  MAN_21B60AD7C0F6FC76--21b60ad7c0f6:
  - faccessat
  MAN_220E6A40224963FF:
  - memfd_create
  MAN_224A8C99E6712138:
  - io_submit
  MAN_226975689DE8D34B:
  - process_vm_writev
  MAN_226975689DE8D34B--226975689de8:
  - process_vm_readv
  MAN_22B16FF99BAA88E5:
  - openat2
  MAN_22BF3E97D1478C4C:
  - lremovexattr
  MAN_22C0858FE24A32E2:
  - fchmodat
  MAN_22C0858FE24A32E2--22c0858fe24a:
  - fchmod
  MAN_23180C38C934A465:
  - newfstatat
  MAN_23180C38C934A465--23180c38c934:
  - fstat
  MAN_233050BC56FBB8DE:
  - getpeername
  MAN_235B2706D4B18CF4:
  - fanotify_mark
  MAN_2368B965D46B34D3:
  - chroot
  MAN_236FC0F4338CB201:
  - munmap
  MAN_2380F711600B6721:
  - set_mempolicy
  MAN_23E25F7C4136339F:
  - close
  MAN_23EFF177A5F2D7A1:
  - statmount
  MAN_2402EF21BE061702:
  - setns
  MAN_2409D9E11538D19C:
  - socket
  MAN_2421026C912D8F9E:
  - init_module
  MAN_2421026C912D8F9E--2421026c912d:
  - finit_module
  MAN_2421E4A1763DDD3C:
  - init_module
  MAN_2421E4A1763DDD3C--2421e4a1763d:
  - finit_module
  MAN_24313BF02489F14D:
  - pidfd_getfd
  MAN_2446B3A5E6B944DB:
  - dup3
  MAN_24754DEDA59528A6:
  - fsmount
  MAN_247817CBE3E20431:
  - mkdirat
  MAN_2482F6894B14F49D:
  - execve
  MAN_24CCF625F638F587:
  - clone3
  MAN_24CCF625F638F587--24ccf625f638:
  - clone
  MAN_25356B76779B1451:
  - pivot_root
  MAN_254F60FBFDA7A2BB:
  - sched_yield
  MAN_25CD94348F7360E1:
  - openat2
  MAN_2606D5149C419BDB:
  - copy_file_range
  MAN_26179D59334DA9A7:
  - perf_event_open
  MAN_2630118F3E221335:
  - mq_open
  MAN_263B6B5871524237:
  - readlinkat
  MAN_263D1CC9E3181478:
  - memfd_create
  MAN_2649C98097933D3E:
  - mkdirat
  MAN_264ED3A90F7DCCDF:
  - getxattr
  MAN_265789F462D6BD8A:
  - mount
  MAN_2678BD4CB1C0D2BE:
  - fchmodat
  MAN_2678BD4CB1C0D2BE--2678bd4cb1c0:
  - fchmod
  MAN_26A01FBC336D2116:
  - move_mount
  MAN_26AA0D7BE44FBCDD:
  - msgsnd
  MAN_26AA0D7BE44FBCDD--26aa0d7be44f:
  - msgrcv
  MAN_26AC18BFE2DCA6FF:
  - shmget
  MAN_26C619C18154DE81:
  - openat
  MAN_26D2EF1E86A41A65:
  - madvise
  MAN_26E6F2EB17CEE086:
  - setrlimit
  MAN_26E6F2EB17CEE086--26e6f2eb17ce:
  - getrlimit
  MAN_26E9E7401804792E:
  - linkat
  MAN_26FB9A2F5350CCFC:
  - timer_create
  MAN_272928C5A15DAF8C:
  - perf_event_open
  MAN_272F42596817190F:
  - fallocate
  MAN_2735D4C274FD8ACB:
  - clock_adjtime
  MAN_2735D4C274FD8ACB--2735d4c274fd:
  - adjtimex
  MAN_27805A275D6AAF08:
  - truncate
  MAN_27805A275D6AAF08--27805a275d6a:
  - ftruncate
  MAN_27E55F887C671CDB:
  - io_setup
  MAN_2806B68B6EAD9BCE:
  - futex_waitv
  MAN_2883CA6859B011D4:
  - bind
  MAN_289A48EC5F86B59B:
  - open_by_handle_at
  MAN_289A48EC5F86B59B--289a48ec5f86:
  - name_to_handle_at
  MAN_28F7CBBC6CF8B3DB:
  - clone3
  MAN_28F7CBBC6CF8B3DB--28f7cbbc6cf8:
  - clone
  MAN_28F9F6A703D7EFDD:
  - mount
  MAN_29018D1605BB68EE:
  - socketpair
  MAN_291F8B6BACE5B57A:
  - io_destroy
  MAN_2934B962DD728396:
  - read
  MAN_299A0347BFD65B11:
  - io_destroy
  MAN_29D5D1F7FC85EB60:
  - execve
  MAN_2A19562071A63C4E:
  - linkat
  MAN_2A2C54D173BC044A:
  - read
  MAN_2A2EBD9E8475D935:
  - openat
  MAN_2A33EE6CC9BA82AC:
  - quotactl_fd
  MAN_2A33EE6CC9BA82AC--2a33ee6cc9ba:
  - quotactl
  MAN_2A34A09D80EA6D8E:
  - pidfd_getfd
  MAN_2A5407BCF324A398:
  - sendto
  MAN_2A5407BCF324A398--2a5407bcf324:
  - sendmsg
  MAN_2A61F58E0C932730:
  - add_key
  MAN_2AA482D50920B9BC:
  - memfd_secret
  MAN_2AC4772264DFD22E:
  - mknodat
  MAN_2ADDCC201D443910:
  - quotactl_fd
  MAN_2ADDCC201D443910--2addcc201d44:
  - quotactl
  MAN_2AFF520C77289514:
  - delete_module
  MAN_2B5A35D041B6CDCB:
  - accept4
  MAN_2B5A35D041B6CDCB--2b5a35d041b6:
  - accept
  MAN_2B70E028F83A3FA2:
  - fsconfig
  MAN_2B891ECEED28A712:
  - move_pages
  MAN_2B8F8E6880518700:
  - fanotify_mark
  MAN_2BA50C0DF3547FCF:
  - chroot
  MAN_2BAADC3893215031:
  - openat
  MAN_2BCAD8270951AF76:
  - fchmodat
  MAN_2BCAD8270951AF76--2bcad8270951:
  - fchmod
  MAN_2C07BF803558EA0E:
  - shmget
  MAN_2C230ACE590DB7ED:
  - fchownat
  MAN_2C230ACE590DB7ED--2c230ace590d:
  - fchown
  MAN_2C32AF09A7E61D5D:
  - mount_setattr
  MAN_2C3633EA13C85053:
  - open_by_handle_at
  MAN_2C3633EA13C85053--2c3633ea13c8:
  - name_to_handle_at
  MAN_2C63464DD1422CF5:
  - linkat
  MAN_2C6CC1D1C5B14D4E:
  - setsockopt
  MAN_2C6CC1D1C5B14D4E--2c6cc1d1c5b1:
  - getsockopt
  MAN_2CA114792327E0E9:
  - tkill
  MAN_2CA114792327E0E9--2ca114792327:
  - tgkill
  MAN_2CA8EAC0B30FA577:
  - linkat
  MAN_2CAF91F7A677785D:
  - lseek
  MAN_2D23AD634FA028EB:
  - inotify_add_watch
  MAN_2D25F3BCC51E9E86:
  - close_range
  MAN_2D46DA35A65200EC:
  - mq_timedsend
  MAN_2D58D7D0BFEEFB1B:
  - move_mount
  MAN_2D7347B452D236BC:
  - mkdirat
  MAN_2DA415FEE25CE4FC:
  - renameat2
  MAN_2DAAEF7ED0C396ED:
  - mount_setattr
  MAN_2DD651B77E7D10AC:
  - rt_sigaction
  MAN_2DDCADB7169BBA71:
  - landlock_restrict_self
  MAN_2E495CFEF7DBA7F3:
  - mlock2
  MAN_2EA2BBBA14B84FDD:
  - memfd_secret
  MAN_2EF91B98B0EB3C01:
  - sendto
  MAN_2EF91B98B0EB3C01--2ef91b98b0eb:
  - sendmsg
  MAN_2F46A4167B50A3E0:
  - prlimit64
  MAN_2F5C450F3A5521B6:
  - write
  MAN_2F625C55BE32E5FD:
  - clone3
  MAN_2F625C55BE32E5FD--2f625c55be32:
  - clone
  MAN_2F6CA39A2256BC4F:
  - linkat
  MAN_2F9873D60115A72F:
  - msgsnd
  MAN_2F9873D60115A72F--2f9873d60115:
  - msgrcv
  MAN_2FB2D9D518231198:
  - splice
  MAN_301D9E6109729551:
  - unshare
  MAN_3023CCD668F0A732:
  - read
  MAN_302BC17780790C33:
  - unlinkat
  MAN_3042E7EC4145A8B8:
  - futex_waitv
  MAN_3046C7DF6AB6850B:
  - mkdirat
  MAN_3064AB8BEF01084B:
  - landlock_create_ruleset
  MAN_309050E378DADFF9:
  - fsmount
  MAN_30905429C2E54ECD:
  - msgsnd
  MAN_30A1650A2C9C389D:
  - flock
  MAN_30AB61AADC0EE587:
  - futex_waitv
  MAN_30BADC2366B3AF1C:
  - process_vm_writev
  MAN_30BADC2366B3AF1C--30badc2366b3:
  - process_vm_readv
  MAN_30C49C668E57A773:
  - getpeername
  MAN_310E681A2310DBE4:
  - landlock_restrict_self
  MAN_318C5D4D6EC09023:
  - linkat
  MAN_31916425CFBE6C54:
  - renameat2
  MAN_31BEAACE7AC84003:
  - sendto
  MAN_31BEAACE7AC84003--31beaace7ac8:
  - sendmsg
  MAN_31D07EC9847501EF:
  - umount2
  MAN_31E9F7D6B2A129AA:
  - write
  MAN_31ED344F814036E1:
  - unlinkat
  MAN_31F2245D0EF787F6:
  - kexec_load
  MAN_31F2245D0EF787F6--31f2245d0ef7:
  - kexec_file_load
  MAN_327D891ACDF2F86D:
  - statfs
  MAN_327D891ACDF2F86D--327d891acdf2:
  - fstatfs
  MAN_32FCD5FCDCED0AB8:
  - semctl
  MAN_3307BC1B30AC131D:
  - mount
  MAN_330C0628475E2900:
  - inotify_init1
  MAN_3369325F81DF4552:
  - lookup_dcookie
  MAN_3371E7FA4452F339:
  - pwritev2
  MAN_339334472278802F:
  - fanotify_init
  MAN_33A119ACDE32A174:
  - fsconfig
  MAN_33AFD2637D6F2143:
  - shmctl
  MAN_33C1D82A6838B634:
  - unshare
  MAN_33DEB3C81B7F76BB:
  - statx
  MAN_33EAE4FC4C68DD9C:
  - vhangup
  MAN_33F71F2361B0FAAC:
  - setreuid
  MAN_33F71F2361B0FAAC--33f71f2361b0:
  - setregid
  MAN_33FEF73F809FE6CF:
  - madvise
  MAN_341CC8E025A1D5F7:
  - mincore
  MAN_34267E560D90B4A9:
  - msgget
  MAN_345E0906F8242D6E:
  - setitimer
  MAN_345E0906F8242D6E--345e0906f824:
  - getitimer
  MAN_347E554BA8FC364F:
  - pselect6
  MAN_349DBF40ADAB8EE5:
  - get_robust_list
  MAN_34D46B3AA947FA44:
  - openat2
  MAN_34ECC98B0B7BFD53:
  - msgctl
  MAN_35216B3DD165D44D:
  - fsync
  MAN_35216B3DD165D44D--35216b3dd165:
  - fdatasync
  MAN_354E308920573A4B:
  - renameat2
  MAN_356DB6479B5066CD:
  - swapon
  MAN_359DC9FC6F5747EC:
  - fcntl
  MAN_35AA936C6E80C4F9:
  - mlock2
  MAN_35AF4698AC57ED3F:
  - munmap
  MAN_35AF4698AC57ED3F--35af4698ac57:
  - mmap
  MAN_35D31F1448242454:
  - fallocate
  MAN_35EBB612CF0B3882:
  - openat
  MAN_362BD9184BA2B5C7:
  - mlock2
  MAN_3639B6DEF16764C3:
  - io_submit
  MAN_368FAB2C80DB889C:
  - acct
  MAN_36A2F0E4A3C04C2F:
  - timerfd_settime
  MAN_36A2F0E4A3C04C2F--36a2f0e4a3c0:
  - timerfd_create
  MAN_36B673524E8BDA38:
  - statfs
  MAN_36E0856D3BABB7C2:
  - bind
  MAN_371735C00AEE6562:
  - fadvise64
  MAN_373E0E6AA30B0096:
  - io_submit
  MAN_37468ED79BB61645:
  - mkdirat
  MAN_374E3BEE42444A1D:
  - pivot_root
  MAN_375FDFA41BD9112B:
  - mq_open
  MAN_37738108542F547D:
  - clock_gettime
  MAN_378558E7B426F613:
  - setns
  MAN_3794F5E144A84CC8:
  - renameat2
  MAN_37A8B25C745F91BB:
  - newfstatat
  MAN_37A8B25C745F91BB--37a8b25c745f:
  - fstat
  MAN_37AEEE0A6595940B:
  - mount_setattr
  MAN_37BD7D77B6421637:
  - mount_setattr
  MAN_37C226253263D4A3:
  - settimeofday
  MAN_37DB36BD0A08152C:
  - linkat
  MAN_384A6B8D64AE99B3:
  - timerfd_gettime
  MAN_385A1F88874013A7:
  - truncate
  MAN_385A1F88874013A7--385a1f888740:
  - ftruncate
  MAN_389160BC66285314:
  - mount
  MAN_38D154A7885FCDD0:
  - openat
  MAN_38E06C951F346CD5:
  - sync_file_range
  MAN_392816F25BD330A2:
  - connect
  MAN_39288A7967511F5F:
  - fchownat
  MAN_39288A7967511F5F--39288a796751:
  - fchown
  MAN_3933C2EE51F23FE6:
  - mount
  MAN_393CA866FF9D6CED:
  - pidfd_getfd
  MAN_39443E26E24B6F4B:
  - epoll_ctl
  MAN_394A4683286EC00D:
  - fspick
  MAN_3974B6275AF8E0AB:
  - mount_setattr
  MAN_39C5F1849EB3A736:
  - getrandom
  MAN_3A03324AA84DA5FC:
  - io_setup
  MAN_3A0D7F45C9ADC371:
  - unlinkat
  MAN_3A5A01A3837AC81D:
  - openat
  MAN_3A7851DC11A6C3A7:
  - lsetxattr
  MAN_3A8EC8020DF100AA:
  - fanotify_mark
  MAN_3A9DFB01308FCA76:
  - munlock
  MAN_3A9DFB01308FCA76--3a9dfb01308f:
  - mlock
  MAN_3AA278D668C39AE5:
  - futex_waitv
  MAN_3B0E429D6A498259:
  - statx
  MAN_3B9CEFF1884953AF:
  - keyctl
  MAN_3BA310149156EEEB:
  - umount2
  MAN_3BD96D0B3B4FD223:
  - sched_setattr
  MAN_3BD96D0B3B4FD223--3bd96d0b3b4f:
  - sched_getattr
  MAN_3BDD5D5E243B177B:
  - migrate_pages
  MAN_3BDE665AACAD4856:
  - inotify_add_watch
  MAN_3BF6BE1B805173A3:
  - request_key
  MAN_3C065C38444E3DD3:
  - setreuid
  MAN_3C065C38444E3DD3--3c065c38444e:
  - setregid
  MAN_3C2D9697959EE004:
  - openat
  MAN_3C8672E880FFEE65:
  - userfaultfd
  MAN_3C8DF737F5522AFF:
  - setsockopt
  MAN_3C8DF737F5522AFF--3c8df737f552:
  - getsockopt
  MAN_3CAD391B0E062A55:
  - mknodat
  MAN_3CCE187F10CE9D52:
  - rt_tgsigqueueinfo
  MAN_3CCE187F10CE9D52--3cce187f10ce:
  - rt_sigqueueinfo
  MAN_3D62C6D101C35837:
  - mount
  MAN_3D64FB7ADE71FD41:
  - symlinkat
  MAN_3D7E29C9D2B37AE7:
  - kexec_load
  MAN_3D7E29C9D2B37AE7--3d7e29c9d2b3:
  - kexec_file_load
  MAN_3D85A861F4BCCD36:
  - mincore
  MAN_3D9FFC664D02AC73:
  - mkdirat
  MAN_3DB32671BC6E30D0:
  - io_setup
  MAN_3DB41ED8FB708A59:
  - swapon
  MAN_3DB41ED8FB708A59--3db41ed8fb70:
  - swapoff
  MAN_3E366D9575E87972:
  - mount_setattr
  MAN_3E4DC087F32D56FF:
  - statmount
  MAN_3E73A66430354EA0:
  - keyctl
  MAN_3ECE4137AFA2C958:
  - listxattr
  MAN_3F0982EBF65B854A:
  - tee
  MAN_3F1968CF7CA69481:
  - munmap
  MAN_3F1968CF7CA69481--3f1968cf7ca6:
  - mmap
  MAN_3F3AF210F0AD54A3:
  - acct
  MAN_3F4EBB7230E505C1:
  - futex
  MAN_3F7E04D796AED484:
  - umount2
  MAN_3F8A15CD5ADF2271:
  - mlock2
  MAN_40086D67A0D0AA3E:
  - truncate
  MAN_40086D67A0D0AA3E--40086d67a0d0:
  - ftruncate
  MAN_40103DA4BE596962:
  - clone3
  MAN_40103DA4BE596962--40103da4be59:
  - clone
  MAN_40E49256297343DC:
  - setpriority
  MAN_40E49256297343DC--40e492562973:
  - getpriority
  MAN_41153D2F0FF296A9:
  - tee
  MAN_41242F466A0DCCD5:
  - ptrace
  MAN_416740BC35B12738:
  - keyctl
  MAN_416BAD24203FEA52:
  - write
  MAN_41809A68A4EFFB86:
  - msync
  MAN_41C9898038029FC7:
  - msgsnd
  MAN_41C9898038029FC7--41c989803802:
  - msgrcv
  MAN_421A2E0126F81592:
  - fsmount
  MAN_4240B1E17543DC8D:
  - connect
  MAN_4262141A575FE0AE:
  - removexattr
  MAN_4262141A575FE0AE--4262141a575f:
  - fremovexattr
  MAN_42C9F55F25054133:
  - io_cancel
  MAN_42DE8D0A55A8985E:
  - userfaultfd
  MAN_42E8FCF0CE3F296D:
  - sched_rr_get_interval
  MAN_43051F186B6C7CF3:
  - unlinkat
  MAN_430829E10B00706B:
  - fchownat
  MAN_430829E10B00706B--430829e10b00:
  - fchown
  MAN_4315C3FDBABDEA28:
  - setresuid
  MAN_4315C3FDBABDEA28--4315c3fdbabd:
  - setresgid
  MAN_4335EFED67589228:
  - linkat
  MAN_43483A57D3CDBCCF:
  - clock_nanosleep
  MAN_43722D93EE0871D1:
  - pwritev2
  MAN_4374CCAAC9BF3B44:
  - copy_file_range
  MAN_43BBCE48C452BDDD:
  - socketpair
  MAN_43D1507418FAB6CD:
  - lsetxattr
  MAN_43EA24335323D198:
  - statmount
  MAN_448BB400D4638E08:
  - futex_waitv
  MAN_44914E69BBFD6982:
  - fchmodat
  MAN_44914E69BBFD6982--44914e69bbfd:
  - fchmod
  MAN_44A850FE06CDA3BF:
  - pidfd_send_signal
  MAN_44D6BD8077F837B5:
  - setpgid
  MAN_44FBD9E9752D427D:
  - msgget
  MAN_44FEABE68B0A0F90:
  - mount
  MAN_450048CA06DCF2CF:
  - timerfd_gettime
  MAN_458625F613B8F37B:
  - fspick
  MAN_45A2B6F5ADF14C3F:
  - getcwd
  MAN_45D40BE238F9D474:
  - fchmodat
  MAN_45F8CDD0A55C26B3:
  - io_getevents
  MAN_4624C925BDE67731:
  - linkat
  MAN_463AA50F45210CB8:
  - epoll_ctl
  MAN_469FA19AC7564E1F:
  - move_mount
  MAN_46B226272F228F10:
  - fsconfig
  MAN_471C192D830F9E34:
  - pkey_mprotect
  MAN_471C192D830F9E34--471c192d830f:
  - mprotect
  MAN_47529796A11EB196:
  - mlock2
  MAN_480CA6DAA0DFDD14:
  - unlinkat
  MAN_489CEE9D73DF8A28:
  - writev
  MAN_489CEE9D73DF8A28--489cee9d73df:
  - preadv
  MAN_48A101A62E09F6DE:
  - getdents64
  MAN_48B52042FE3DEA4C:
  - statfs
  MAN_48B52042FE3DEA4C--48b52042fe3d:
  - fstatfs
  MAN_48E91FAE2714E3EA:
  - io_submit
  MAN_48F51962E131940C:
  - process_vm_writev
  MAN_48F51962E131940C--48f51962e131:
  - process_vm_readv
  MAN_491AC2F819A7FC02:
  - vmsplice
  MAN_4925450FB5B52C68:
  - ioprio_set
  MAN_4925450FB5B52C68--4925450fb5b5:
  - ioprio_get
  MAN_494CD34A8C11734B:
  - close
  MAN_494FCD586E2D5DC3:
  - add_key
  MAN_498F75E57971ACE2:
  - execve
  MAN_49961344A6B4428A:
  - write
  MAN_49B7040911675302:
  - mkdirat
  MAN_49C1DB44E2DAB242:
  - seccomp
  MAN_49D00E0CA953344D:
  - futex
  MAN_4A06F3D62F31AFB4:
  - epoll_pwait2
  MAN_4A06F3D62F31AFB4--4a06f3d62f31:
  - epoll_pwait
  MAN_4A604EE4077A40EA:
  - nfsservctl
  MAN_4A8D1318D9FC0351:
  - nanosleep
  MAN_4A99E178A6F5AE66:
  - process_madvise
  MAN_4A9B42B78370FA8A:
  - sched_setattr
  MAN_4A9B42B78370FA8A--4a9b42b78370:
  - sched_getattr
  MAN_4ACDAFA5048EFBA2:
  - truncate
  MAN_4ACDAFA5048EFBA2--4acdafa5048e:
  - ftruncate
  MAN_4AE13EE9521C82E8:
  - fallocate
  MAN_4B1DDC20BEF0A957:
  - openat
  MAN_4B90189C8E50476F:
  - move_mount
  MAN_4B9C90FCF8BB2CCF:
  - move_mount
  MAN_4BA444095AE224CD:
  - fchownat
  MAN_4BB468C8659221AB:
  - linkat
  MAN_4BC9B841AF8A465A:
  - openat
  MAN_4BDABB3297C3A5EF:
  - migrate_pages
  MAN_4C50AA2793AB7713:
  - memfd_create
  MAN_4C7F584C3157F6A1:
  - mount_setattr
  MAN_4CB8B3AC227094CE:
  - memfd_create
  MAN_4CD019E3963C300F:
  - copy_file_range
  MAN_4CDE6B174CC9717C:
  - faccessat
  MAN_4CE7E1C5CF2C0E44:
  - symlinkat
  MAN_4CF2EE50643C6D9A:
  - signalfd4
  MAN_4CF3810093BB6432:
  - add_key
  MAN_4CFAEFA87DFAA555:
  - landlock_restrict_self
  MAN_4D632B3F0E812432:
  - fsconfig
  MAN_4D7C60390E4FAA79:
  - fsconfig
  MAN_4DA1BBD6BBC55961:
  - openat
  MAN_4DC6ADA54B408E80:
  - move_mount
  MAN_4DDC3CFBD2ED9E46:
  - truncate
  MAN_4DDC3CFBD2ED9E46--4ddc3cfbd2ed:
  - ftruncate
  MAN_4DF31C310F43FF85:
  - userfaultfd
  MAN_4DFD8732F88C4CAC:
  - accept4
  MAN_4DFD8732F88C4CAC--4dfd8732f88c:
  - accept
  MAN_4DFF3DB3C6CC395E:
  - sendto
  MAN_4DFF3DB3C6CC395E--4dff3db3c6cc:
  - sendmsg
  MAN_4E1633A41FC2D219:
  - fsopen
  MAN_4E5C3D2A76ED6918:
  - openat
  MAN_4E646428E07087C5:
  - mkdirat
  MAN_4E6BB251F5BA204D:
  - ioprio_set
  MAN_4E75F47CB7B5A138:
  - swapon
  MAN_4E75F47CB7B5A138--4e75f47cb7b5:
  - swapoff
  MAN_4E7A132667618EE8:
  - fchmodat
  MAN_4E7A132667618EE8--4e7a13266761:
  - fchmod
  MAN_4E9ED3890C989D54:
  - sched_setaffinity
  MAN_4E9ED3890C989D54--4e9ed3890c98:
  - sched_getaffinity
  MAN_4EC4209E61942204:
  - mount
  MAN_4F1974600A9BD598:
  - clone3
  MAN_4F1974600A9BD598--4f1974600a9b:
  - clone
  MAN_4F4C945946FDBEEB:
  - io_submit
  MAN_4F90C077A864B302:
  - mbind
  MAN_4FC7F1499578A5CB:
  - mount
  MAN_5021496DD469733E:
  - clone3
  MAN_5021496DD469733E--5021496dd469:
  - clone
  MAN_502A1AD0A1EF3B11:
  - pkey_mprotect
  MAN_502A1AD0A1EF3B11--502a1ad0a1ef:
  - mprotect
  MAN_5045CFB93D8D8044:
  - renameat2
  MAN_509C682D77B312D0:
  - open_tree
  MAN_509E7404D69FD1DF:
  - mount
  MAN_50B1E337E8E12322:
  - bind
  MAN_50EBA3650B39131A:
  - sched_setattr
  MAN_50EBA3650B39131A--50eba3650b39:
  - sched_getattr
  MAN_51133E60F6CD5764:
  - futex_waitv
  MAN_5126172582E0CF35:
  - kcmp
  MAN_513DD0F86F3C8432:
  - mount_setattr
  MAN_51680AEE1B98DFEC:
  - epoll_ctl
  MAN_51691ABE0D8D3A3E:
  - inotify_init1
  MAN_5175E67C45874C49:
  - munlock
  MAN_5175E67C45874C49--5175e67c4587:
  - mlock
  MAN_51804F262D65C7D9:
  - fallocate
  MAN_5182EE044E596F56:
  - syncfs
  MAN_5182EE044E596F56--5182ee044e59:
  - sync
  MAN_51BD21474DEBFE8C:
  - listmount
  MAN_51F3503CC0FAA455:
  - mknodat
  MAN_52099F4FAACD68B6:
  - swapon
  MAN_52099F4FAACD68B6--52099f4faacd:
  - swapoff
  MAN_52224A9438F2741E:
  - fchown
  MAN_524B615D8F9A7E12:
  - connect
  MAN_5250547EA07DA0AA:
  - syslog
  MAN_526494CEC56EDFE6:
  - statx
  MAN_527A0D84E9FF86AB:
  - msgsnd
  MAN_527A0D84E9FF86AB--527a0d84e9ff:
  - msgrcv
  MAN_52ACF4580A4EED48:
  - fallocate
  MAN_52F94A738B523EF8:
  - madvise
  MAN_52FFE1646BF9AB4C:
  - move_pages
  MAN_5336B175AEDE2287:
  - lremovexattr
  MAN_533C289CECDF6E1B:
  - clone3
  MAN_533C289CECDF6E1B--533c289cecdf:
  - clone
  MAN_5351B902D09A2DFE:
  - syncfs
  MAN_5351B902D09A2DFE--5351b902d09a:
  - sync
  MAN_535FF69FBDF6D1BA:
  - execve
  MAN_536F20D217F16896:
  - setxattr
  MAN_536F20D217F16896--536f20d217f1:
  - fsetxattr
  MAN_5377D1E23AC59611:
  - readlinkat
  MAN_5378890AE3F832EE:
  - statfs
  MAN_5378890AE3F832EE--5378890ae3f8:
  - fstatfs
  MAN_5389F693EFBD0128:
  - linkat
  MAN_5397EC477504E285:
  - mknodat
  MAN_53D0AE4697874D68:
  - semctl
  MAN_54012F233360E9A9:
  - setns
  MAN_5401750B0A88DB94:
  - openat
  MAN_542E9C9EE5D8C648:
  - landlock_create_ruleset
  MAN_5437002A2CC2FDDF:
  - clock_gettime
  MAN_5437E540CEE5B02D:
  - pidfd_getfd
  MAN_54494C742FBC3DA2:
  - nanosleep
  MAN_544F18291CF51AFA:
  - rt_tgsigqueueinfo
  MAN_544F18291CF51AFA--544f18291cf5:
  - rt_sigqueueinfo
  MAN_54578E38BA248574:
  - unlinkat
  MAN_54EF07FEBCBD8BEE:
  - rt_tgsigqueueinfo
  MAN_54EF07FEBCBD8BEE--54ef07febcbd:
  - rt_sigqueueinfo
  MAN_5508CCE68A3412AF:
  - sendto
  MAN_5508CCE68A3412AF--5508cce68a34:
  - sendmsg
  MAN_553DD6E647E4133C:
  - execveat
  MAN_5554D99AF09A9C5E:
  - symlinkat
  MAN_55E902CF6CBC5A2D:
  - inotify_add_watch
  MAN_5619D752C456B96A:
  - mount_setattr
  MAN_5639DF08C3AD9674:
  - keyctl
  MAN_567C0F00C4833C62:
  - mount
  MAN_569B6B3D3F59F7ED:
  - pipe2
  MAN_56E378DC4A4562E7:
  - getsockname
  MAN_5705D79E2B694D9C:
  - open_by_handle_at
  MAN_5705D79E2B694D9C--5705d79e2b69:
  - name_to_handle_at
  MAN_5731488A6334C44A:
  - landlock_add_rule
  MAN_5735FF0B88004C71:
  - pivot_root
  MAN_577A4D985F19C482:
  - write
  MAN_5806C241417815C0:
  - futex_waitv
  MAN_58411D10001C0C47:
  - close
  MAN_584FB17A96BB2519:
  - execve
  MAN_587AC616B1BC5054:
  - prctl
  MAN_58936D050A8879DE:
  - pidfd_getfd
  MAN_58AE02A36A0151D5:
  - prctl
  MAN_58BCE2C7ADBC8EC3:
  - sendfile
  MAN_58F03BE7E74BDC3F:
  - readlinkat
  MAN_5940E59001AE8790:
  - clock_adjtime
  MAN_5940E59001AE8790--5940e59001ae:
  - adjtimex
  MAN_595FC7CE5C433E51:
  - bpf
  MAN_597B9FB0CD1E8C89:
  - keyctl
  MAN_5983BA1855B7DD2A:
  - clock_nanosleep
  MAN_59855F72BABB2E05:
  - eventfd2
  MAN_5987730F6E24729A:
  - faccessat2
  MAN_5987730F6E24729A--5987730f6e24:
  - faccessat
  MAN_599F8DFF8D2037EA:
  - semctl
  MAN_59B67A4969C83F19:
  - fsconfig
  MAN_5A2D8C100254E068:
  - truncate
  MAN_5A2D8C100254E068--5a2d8c100254:
  - ftruncate
  MAN_5A3490878AA77E0E:
  - setgid
  MAN_5A74077EE86F077B:
  - execve
  MAN_5A9551B19AED7826:
  - llistxattr
  MAN_5A9551B19AED7826--5a9551b19aed:
  - flistxattr
  MAN_5AAC845A10A05BF3:
  - shmctl
  MAN_5AC1E4DF3AC54412:
  - splice
  MAN_5AD398FDE5FDF82C:
  - fchownat
  MAN_5AD398FDE5FDF82C--5ad398fde5fd:
  - fchown
  MAN_5B03C417C69F2BCD:
  - utimensat
  MAN_5B12F375E4D54731:
  - read
  MAN_5B2667DFDCB4EB31:
  - fchdir
  MAN_5B2667DFDCB4EB31--5b2667dfdcb4:
  - chdir
  MAN_5B4118BF4C21F770:
  - shutdown
  MAN_5B5730F8A05AEA1D:
  - fspick
  MAN_5B7786EEFCC29842:
  - setitimer
  MAN_5B7786EEFCC29842--5b7786eefcc2:
  - getitimer
  MAN_5BAD6B4060421C26:
  - timerfd_settime
  MAN_5BAD6B4060421C26--5bad6b406042:
  - timerfd_create
  MAN_5BCB50E041999E98:
  - clone3
  MAN_5BCB50E041999E98--5bcb50e04199:
  - clone
  MAN_5C1BB76989C74037:
  - sendfile
  MAN_5C21EA890885A138:
  - setgroups
  MAN_5C21EA890885A138--5c21ea890885:
  - getgroups
  MAN_5C4059CF30633E55:
  - openat
  MAN_5C52DBC7100B1A0C:
  - truncate
  MAN_5C52DBC7100B1A0C--5c52dbc7100b:
  - ftruncate
  MAN_5C9F9CF8E5FCECF8:
  - landlock_add_rule
  MAN_5CA77109D8B63C2E:
  - statfs
  MAN_5CA77109D8B63C2E--5ca77109d8b6:
  - fstatfs
  MAN_5CBF63A239A782AE:
  - msgctl
  MAN_5D182F7654922DE8:
  - acct
  MAN_5D19D1B86EC99D53:
  - mount
  MAN_5D32B043AFC47F35:
  - mbind
  MAN_5D407C771BF97999:
  - ptrace
  MAN_5D77D3DF0D183A77:
  - mount_setattr
  MAN_5D7D3D5FA2803685:
  - open_tree
  MAN_5DA5389EECD6E4CF:
  - kexec_load
  MAN_5DA5389EECD6E4CF--5da5389eecd6:
  - kexec_file_load
  MAN_5DAA4B025B7A454F:
  - mkdirat
  MAN_5DB99587335B243D:
  - msgsnd
  MAN_5DB99587335B243D--5db99587335b:
  - msgrcv
  MAN_5E3458C21B3BFCC2:
  - openat
  MAN_5E774C21A4FDD14D:
  - umount2
  MAN_5E8EB174F59A8F62:
  - msgctl
  MAN_5EBACD1F54CFF47E:
  - clock_adjtime
  MAN_5EBACD1F54CFF47E--5ebacd1f54cf:
  - adjtimex
  MAN_5EC557E98E13F4B3:
  - mq_timedsend
  MAN_5EC9C226089F0B36:
  - futex_waitv
  MAN_5ED210431E5E5D7B:
  - fanotify_mark
  MAN_5EED236379EBC595:
  - unlinkat
  MAN_5EF2B85535DA2137:
  - io_setup
  MAN_5F088ADFCCCA98C5:
  - msgctl
  MAN_5F1E1E101D590298:
  - landlock_create_ruleset
  MAN_5F4A835D7FF36724:
  - lsetxattr
  MAN_5F5865EF1A8D5904:
  - shutdown
  MAN_5FA75C29B55D8310:
  - madvise
  MAN_5FB806AF95E69B54:
  - signalfd4
  MAN_5FBA7D222FF2515B:
  - socketpair
  MAN_5FE9A9C52175DA4B:
  - sendfile
  MAN_6010B5E3B46557A8:
  - fspick
  MAN_601A6EC24E728D4A:
  - mkdirat
  MAN_60276E83E8DF5B7B:
  - clone
  MAN_6038BC183A1CE6BF:
  - listen
  MAN_603F4AB2BE3C6F35:
  - sched_setattr
  MAN_603F4AB2BE3C6F35--603f4ab2be3c:
  - sched_getattr
  MAN_60451D11EA174E68:
  - munlockall
  MAN_60451D11EA174E68--60451d11ea17:
  - mlock
  MAN_607DD2BFC7254305:
  - connect
  MAN_60A919B520D2A680:
  - connect
  MAN_60E1D07E34DA6CB1:
  - move_mount
  MAN_611DBAEAF25BEBA0:
  - execve
  MAN_614136932ED0DC9D:
  - signalfd4
  MAN_6150CE201F892BEF:
  - munmap
  MAN_6150CE201F892BEF--6150ce201f89:
  - mmap
  MAN_61993E86D424F5A7:
  - pivot_root
  MAN_61B106C06D65F9D3:
  - umount2
  MAN_61EBE054E176BE82:
  - rt_sigaction
  MAN_61F11BAA4671A70F:
  - msgctl
  MAN_61FED48E04D44F34:
  - socketpair
  MAN_6242DAB50F5E2ADB:
  - settimeofday
  MAN_6242DAB50F5E2ADB--6242dab50f5e:
  - gettimeofday
  MAN_63064D0C5A9838DC:
  - mq_timedreceive
  MAN_631222516EE8AD45:
  - unlinkat
  MAN_632B6884B60A89A0:
  - pivot_root
  MAN_6373791A7F233D7F:
  - truncate
  MAN_6373791A7F233D7F--6373791a7f23:
  - ftruncate
  MAN_63C74740BD037122:
  - io_submit
  MAN_63EE305E2C8EF74E:
  - move_pages
  MAN_64206AC9FE2BAE72:
  - close
  MAN_6426642A757EA481:
  - openat
  MAN_643316829BCBA523:
  - sendto
  MAN_643316829BCBA523--643316829bcb:
  - sendmsg
  MAN_647CCF3ED2CB7E7D:
  - statx
  MAN_64F9D5C22E1530BB:
  - symlinkat
  MAN_650E80CEA3AEC805:
  - lsetxattr
  MAN_652667C0CDB7490F:
  - openat
  MAN_65282EDD82F38BE5:
  - openat
  MAN_65600F460F34E22D:
  - write
  MAN_65E857B82D8265B3:
  - pidfd_open
  MAN_65F2620A4C47AD08:
  - madvise
  MAN_663B3C3EEB98245D:
  - accept4
  MAN_663B3C3EEB98245D--663b3c3eeb98:
  - accept
  MAN_664AD1B99F9964FB:
  - timerfd_settime
  MAN_664AD1B99F9964FB--664ad1b99f99:
  - timerfd_create
  MAN_665CA24BA241A1F8:
  - memfd_secret
  MAN_667D4B2CC64A44F2:
  - execve
  MAN_66B86283526DC70D:
  - request_key
  MAN_66BB89ABDF90CFD2:
  - process_vm_writev
  MAN_66BB89ABDF90CFD2--66bb89abdf90:
  - process_vm_readv
  MAN_66D864DABC0A2276:
  - mkdirat
  MAN_66E2E3D4F6EC9D11:
  - perf_event_open
  MAN_66F897762987387A:
  - timer_getoverrun
  MAN_678D8AD64978C2CA:
  - futex_waitv
  MAN_67B1D531AF6767B5:
  - statmount
  MAN_67D17B7E7A297D1E:
  - memfd_secret
  MAN_67ECA3FB50D80BAF:
  - memfd_create
  MAN_682663184D6AEB4C:
  - open_by_handle_at
  MAN_682663184D6AEB4C--682663184d6a:
  - name_to_handle_at
  MAN_68607EC1ED7502E1:
  - clone3
  MAN_68607EC1ED7502E1--68607ec1ed75:
  - clone
  MAN_688ED52BAD89AD79:
  - unlinkat
  MAN_689DC7C70D1966CC:
  - statx
  MAN_68A4E189EBBF5B19:
  - pwritev
  MAN_68A744027E9CC265:
  - sched_rr_get_interval
  MAN_68ACED6EB62282D8:
  - kexec_load
  MAN_68ACED6EB62282D8--68aced6eb622:
  - kexec_file_load
  MAN_68AF4FBD1DFAA4A4:
  - perf_event_open
  MAN_68B1C3935C4667C3:
  - truncate
  MAN_68B1C3935C4667C3--68b1c3935c46:
  - ftruncate
  MAN_68F79A17A91CCFEA:
  - copy_file_range
  MAN_69276B34762F8A4C:
  - listmount
  MAN_698F89C51955A75D:
  - setgid
  MAN_6991AB4713E8137F:
  - llistxattr
  MAN_6991AB4713E8137F--6991ab4713e8:
  - flistxattr
  MAN_6998D4E70F807B13:
  - sethostname
  MAN_699CBBEA743E20C9:
  - ppoll
  MAN_69B9B9B89FEEE610:
  - mount_setattr
  MAN_69D118FF22E28374:
  - kexec_load
  MAN_69D118FF22E28374--69d118ff22e2:
  - kexec_file_load
  MAN_69DEF392CDC333CB:
  - connect
  MAN_69F44A6E6B819927:
  - timerfd_settime
  MAN_69F44A6E6B819927--69f44a6e6b81:
  - timerfd_create
  MAN_6A21CC2AA8FA9EDD:
  - unlinkat
  MAN_6A70D70E01FD03CF:
  - quotactl_fd
  MAN_6A70D70E01FD03CF--6a70d70e01fd:
  - quotactl
  MAN_6A789985BDC500A9:
  - semtimedop
  MAN_6A789985BDC500A9--6a789985bdc5:
  - semop
  MAN_6A89B7937BC73BAC:
  - clone3
  MAN_6A89B7937BC73BAC--6a89b7937bc7:
  - clone
  MAN_6ACE70C9E2A3E819:
  - clone3
  MAN_6AD26E12F4B51375:
  - mkdirat
  MAN_6B07B6E4CA20325F:
  - msgsnd
  MAN_6B07B6E4CA20325F--6b07b6e4ca20:
  - msgrcv
  MAN_6B279B9EE4AC31BB:
  - read
  MAN_6B7EED8E43FDD1BA:
  - epoll_create1
  MAN_6BACB1D8B8272512:
  - settimeofday
  MAN_6BBD26053C82AFAA:
  - fchdir
  MAN_6BBD26053C82AFAA--6bbd26053c82:
  - chdir
  MAN_6BC3B59B02168621:
  - newfstatat
  MAN_6BC3B59B02168621--6bc3b59b0216:
  - fstat
  MAN_6BC7A806A28089C8:
  - move_mount
  MAN_6BEAAED04206F36C:
  - sched_rr_get_interval
  MAN_6C1FC28AD41EA688:
  - timerfd_gettime
  MAN_6C49366F5848720B:
  - semctl
  MAN_6C55D2511544FB9D:
  - mount_setattr
  MAN_6C93411C3BFF79FE:
  - sendto
  MAN_6C93411C3BFF79FE--6c93411c3bff:
  - sendmsg
  MAN_6CA5256A4C7A3366:
  - landlock_add_rule
  MAN_6CC437DD7D6B2500:
  - munlock
  MAN_6CE109381C3C161B:
  - semtimedop
  MAN_6CE109381C3C161B--6ce109381c3c:
  - semop
  MAN_6D2CC2D69B0E02EF:
  - symlinkat
  MAN_6D571232E41C718D:
  - fsopen
  MAN_6D665164162723C5:
  - clock_settime
  MAN_6D665164162723C5--6d6651641627:
  - clock_getres
  MAN_6D67821E17875717:
  - fsconfig
  MAN_6D77B363EA967C8F:
  - pidfd_send_signal
  MAN_6D92BC0478903471:
  - add_key
  MAN_6DA0C690DD696848:
  - timer_create
  MAN_6DCBB46C48EC79F8:
  - delete_module
  MAN_6DD22946F924AE87:
  - unshare
  MAN_6DED785691EF1985:
  - fallocate
  MAN_6E1B78D7DB21D5CF:
  - connect
  MAN_6E537F0391C47B3C:
  - clone3
  MAN_6E537F0391C47B3C--6e537f0391c4:
  - clone
  MAN_6E72A4C6A8F2BDA3:
  - semget
  MAN_6E94A46DD3E9F446:
  - add_key
  MAN_6ECFFEBB8B171061:
  - cachestat
  MAN_6F0974404A3C6CDE:
  - signalfd4
  MAN_6F3DE0D8F0C45D11:
  - request_key
  MAN_6FA2BF0FF24F7A18:
  - fchmodat
  MAN_6FA2BF0FF24F7A18--6fa2bf0ff24f:
  - fchmod
  MAN_6FA8F2D41D1B7062:
  - memfd_create
  MAN_6FE4E78E13C3DA4F:
  - msync
  MAN_6FFF3E54966CBB24:
  - setns
  MAN_7011B01F7BF45FCE:
  - swapon
  MAN_7011B01F7BF45FCE--7011b01f7bf4:
  - swapoff
  MAN_7055A4E8C4DE46A4:
  - execveat
  MAN_706094938C4326CA:
  - shmget
  MAN_70DFAE36C6B37CD3:
  - setuid
  MAN_70EB0BC9C9ACF1B1:
  - io_setup
  MAN_710B13DF5F84CD08:
  - fsmount
  MAN_7143DFCF0730EE0C:
  - landlock_add_rule
  MAN_7154A5BC5C11D7BF:
  - acct
  MAN_71DA9C510F1A6FF0:
  - shmdt
  MAN_71DA9C510F1A6FF0--71da9c510f1a:
  - shmat
  MAN_71F8AE4C3FDA1956:
  - statmount
  MAN_720AB86172D80E8C:
  - ptrace
  MAN_721AB2110F048B53:
  - sched_setscheduler
  MAN_721AB2110F048B53--721ab2110f04:
  - sched_getscheduler
  MAN_722416AFCA40E68F:
  - process_madvise
  MAN_724A43ACDB2EC1B5:
  - mount
  MAN_7251C701BB057437:
  - close
  MAN_7261FB5B9216890D:
  - io_destroy
  MAN_7264A19C5EA0AD3B:
  - sched_rr_get_interval
  MAN_726D48DBA6410F84:
  - bind
  MAN_7277495AFCCD0F3D:
  - mount
  MAN_7282051237363625:
  - ftruncate
  MAN_72BC35B6D1A7488F:
  - syncfs
  MAN_72BC35B6D1A7488F--72bc35b6d1a7:
  - sync
  MAN_730B8378FA7368D1:
  - add_key
  MAN_732160952277CD16:
  - socket
  MAN_73314E96AB480881:
  - pidfd_open
  MAN_734E3A3ACB36A0FF:
  - pivot_root
  MAN_73878C0ED3F6B7C5:
  - execve
  MAN_739471D1D8BB4BC6:
  - statx
  MAN_7399227B1922C638:
  - flock
  MAN_73A689AC99A1E643:
  - symlinkat
  MAN_73B7CA51A7522BEF:
  - io_setup
  MAN_73BF7257C99A2E8B:
  - setsockopt
  MAN_73BF7257C99A2E8B--73bf7257c99a:
  - getsockopt
  MAN_73E054548B324267:
  - seccomp
  MAN_74476925933868E7:
  - setxattr
  MAN_74476925933868E7--744769259338:
  - fsetxattr
  MAN_745D5AB5A8DA3C1F:
  - faccessat2
  MAN_745D5AB5A8DA3C1F--745d5ab5a8da:
  - faccessat
  MAN_74CD25CD6357CEA3:
  - munlock
  MAN_74CD25CD6357CEA3--74cd25cd6357:
  - mlock
  MAN_74D6975FADF35CB3:
  - getrusage
  MAN_74F3A325C42F5CE5:
  - lookup_dcookie
  MAN_74F539ED43B7344F:
  - recvmsg
  MAN_74F539ED43B7344F--74f539ed43b7:
  - recvfrom
  MAN_74FA94E5100439BF:
  - keyctl
  MAN_751212F796DF34F9:
  - mq_timedreceive
  MAN_7538B0E509D6632E:
  - unshare
  MAN_75435AE77CB1DCC6:
  - writev
  MAN_75435AE77CB1DCC6--75435ae77cb1:
  - preadv
  MAN_7581E30F4F3FD7F6:
  - shmdt
  MAN_7581E30F4F3FD7F6--7581e30f4f3f:
  - shmat
  MAN_7600A01AED50A03F:
  - openat
  MAN_76075BEF778F7A0A:
  - open_tree
  MAN_76253CFAA463D995:
  - readv
  MAN_7637DAFBABD96CB0:
  - clock_settime
  MAN_7637DAFBABD96CB0--7637dafbabd9:
  - clock_getres
  MAN_7659F99685012E59:
  - syncfs
  MAN_7659F99685012E59--7659f9968501:
  - sync
  MAN_76CE8AC1292D503C:
  - mknodat
  MAN_76F8870DE4AE9CDF:
  - mq_unlink
  MAN_770F1F20B1133F72:
  - connect
  MAN_772C247721B404FC:
  - open_by_handle_at
  MAN_772C247721B404FC--772c247721b4:
  - name_to_handle_at
  MAN_775954941C8D8008:
  - unshare
  MAN_77CDB499A8FAC96D:
  - semtimedop
  MAN_77CDB499A8FAC96D--77cdb499a8fa:
  - semop
  MAN_783663C239851918:
  - semtimedop
  MAN_783663C239851918--783663c23985:
  - semop
  MAN_786CA8EC2F2460BE:
  - pidfd_open
  MAN_78CCB41312A72C06:
  - timerfd_settime
  MAN_78CCB41312A72C06--78ccb41312a7:
  - timerfd_create
  MAN_78D036D4D4C36A01:
  - openat
  MAN_79011BFB7A04965D:
  - madvise
  MAN_7939BA9D8C46E111:
  - fsopen
  MAN_794294DBD03CA974:
  - dup3
  MAN_794294DBD03CA974--794294dbd03c:
  - dup
  MAN_797F5DF4C87DFEAD:
  - msgctl
  MAN_79F70A4C5B5A2BB1:
  - tkill
  MAN_79F70A4C5B5A2BB1--79f70a4c5b5a:
  - tgkill
  MAN_7A0588957618E854:
  - timer_create
  MAN_7A0ABC88DA482603:
  - mount_setattr
  MAN_7A41CF99723D3017:
  - recvmsg
  MAN_7A41CF99723D3017--7a41cf99723d:
  - recvfrom
  MAN_7A48D8239BDA60B4:
  - mq_open
  MAN_7A57F53C94A83F72:
  - openat
  MAN_7ACB89EB7B7E25FD:
  - linkat
  MAN_7ACC5E244B308101:
  - setuid
  MAN_7AD2ED6AD70C6CEB:
  - timerfd_gettime
  MAN_7ADE73AC47B06160:
  - truncate
  MAN_7ADE73AC47B06160--7ade73ac47b0:
  - ftruncate
  MAN_7B1346E6F2525BCE:
  - mount
  MAN_7B51488F99889D7D:
  - sched_setparam
  MAN_7B51488F99889D7D--7b51488f9988:
  - sched_getparam
  MAN_7B54B1DFDAFB7E1C:
  - setgroups
  MAN_7B6A4FB3DB08583D:
  - mq_open
  MAN_7BB011FC81656C5C:
  - faccessat
  MAN_7BBBEBDDC278A80F:
  - getrandom
  MAN_7BCF7728F4DF44F4:
  - dup3
  MAN_7BCF7728F4DF44F4--7bcf7728f4df:
  - dup
  MAN_7BF8FD107BE8972F:
  - getcwd
  MAN_7C027ABED9E00F8B:
  - io_submit
  MAN_7C2064F7C94D121C:
  - getpeername
  MAN_7C21AB9FAEA9571D:
  - futex_waitv
  MAN_7C3C0347FD37CEB9:
  - listen
  MAN_7C5C13EDDD337B2E:
  - write
  MAN_7C61C57E7130781C:
  - sendto
  MAN_7C61C57E7130781C--7c61c57e7130:
  - sendmsg
  MAN_7C8BA7357083E4F2:
  - lgetxattr
  MAN_7C8BA7357083E4F2--7c8ba7357083:
  - fgetxattr
  MAN_7C8E482EC3D243A1:
  - move_mount
  MAN_7C9D4B4F49A0C203:
  - inotify_init1
  MAN_7C9E366DB0981954:
  - kexec_load
  MAN_7C9E366DB0981954--7c9e366db098:
  - kexec_file_load
  MAN_7CE4DE0A9892B51D:
  - utimensat
  MAN_7D0590EE27937CF0:
  - openat
  MAN_7D15CB4C3AA1628B:
  - mount_setattr
  MAN_7D2EE362B3084F84:
  - sched_setattr
  MAN_7D2EE362B3084F84--7d2ee362b308:
  - sched_getattr
  MAN_7D35E0844882307D:
  - linkat
  MAN_7D3F52F3AD07AF5B:
  - umount2
  MAN_7D42E8E12B8572B4:
  - munmap
  MAN_7D42E8E12B8572B4--7d42e8e12b85:
  - mmap
  MAN_7D6A0A0D5C10A5F7:
  - timerfd_gettime
  MAN_7D7A6F112E3F4A42:
  - chroot
  MAN_7D8E51DBADDA49E2:
  - fspick
  MAN_7E38D24865D1CC35:
  - renameat2
  MAN_7E74B16F55EB156E:
  - getsockname
  MAN_7E786906C55D638F:
  - fanotify_init
  MAN_7E81F27BE1709331:
  - fsync
  MAN_7E81F27BE1709331--7e81f27be170:
  - fdatasync
  MAN_7E994FDBD031F856:
  - msgget
  MAN_7EAA5B771761F1C5:
  - setreuid
  MAN_7EAA5B771761F1C5--7eaa5b771761:
  - setregid
  MAN_7EF435B7693EFFC7:
  - init_module
  MAN_7EF435B7693EFFC7--7ef435b7693e:
  - finit_module
  MAN_7F34A257DE64CAFE:
  - dup3
  MAN_7F34A257DE64CAFE--7f34a257de64:
  - dup
  MAN_7F3B62C7919A5946:
  - symlinkat
  MAN_7F3C070C0F27DDE3:
  - move_mount
  MAN_7F5A23E7DBAB3F28:
  - epoll_pwait2
  MAN_7F5A23E7DBAB3F28--7f5a23e7dbab:
  - epoll_pwait
  MAN_7F87676A24B63A5C:
  - futex_waitv
  MAN_7FD97F61EA3E0F1F:
  - kill
  MAN_80267EC83AF63772:
  - fchmodat
  MAN_80267EC83AF63772--80267ec83af6:
  - fchmod
  MAN_802C2D137CB40CE8:
  - pkey_alloc
  MAN_803D25361A437299:
  - faccessat2
  MAN_803D25361A437299--803d25361a43:
  - faccessat
  MAN_805AD5EFEEBF0C34:
  - mknodat
  MAN_8089CCB3310B7306:
  - epoll_ctl
  MAN_80D85D82B47F304D:
  - fadvise64
  MAN_811EAE9B5FC80CCA:
  - openat
  MAN_812E503676DD9D23:
  - semget
  MAN_812F8EA9DA017E2A:
  - mount_setattr
  MAN_814CC91689180A8C:
  - mknodat
  MAN_8153E21BD727F6A0:
  - fstatfs
  MAN_8198C90B56B82E87:
  - pipe2
  MAN_81CB42F2B68275AD:
  - fspick
  MAN_81DEEDED0ED29039:
  - setxattr
  MAN_81DEEDED0ED29039--81deeded0ed2:
  - fsetxattr
  MAN_81F4F1C3AD4F3217:
  - getsid
  MAN_821DDF83576C8051:
  - readlinkat
  MAN_8221C3E439E89B62:
  - setgid
  MAN_8246E881A05B6ABC:
  - fallocate
  MAN_8251328BCEF43D9E:
  - open_tree
  MAN_82592148B6764875:
  - bind
  MAN_8267DBA7430B2DCB:
  - clock_settime
  MAN_828CD9CBC91671F3:
  - connect
  MAN_829272B1DEE9A08E:
  - inotify_add_watch
  MAN_82A5A1B0B6919D81:
  - sched_setattr
  MAN_82A5A1B0B6919D81--82a5a1b0b691:
  - sched_getattr
  MAN_82EE41F04229EE7F:
  - rt_sigsuspend
  MAN_82F9B08F30A3FEE4:
  - mremap
  MAN_831FA4218199D0D4:
  - tkill
  MAN_831FA4218199D0D4--831fa4218199:
  - tgkill
  MAN_835E50EF3C99648C:
  - mount_setattr
  MAN_837C792282DF9AD0:
  - init_module
  MAN_837C792282DF9AD0--837c792282df:
  - finit_module
  MAN_838355DDB1BE708E:
  - epoll_ctl
  MAN_83A334327C6E8D25:
  - llistxattr
  MAN_83A334327C6E8D25--83a334327c6e:
  - flistxattr
  MAN_83C42EA54C4F01DB:
  - madvise
  MAN_83E0304A4D485967:
  - setns
  MAN_83FDA2A1B7EF185C:
  - rt_sigsuspend
  MAN_8425F17E513FC8FA:
  - cachestat
  MAN_845BEFF99463578F:
  - fchownat
  MAN_845BEFF99463578F--845beff99463:
  - fchown
  MAN_846B9B763732424F:
  - openat
  MAN_84706FE26532D57F:
  - pkey_mprotect
  MAN_84706FE26532D57F--84706fe26532:
  - mprotect
  MAN_84AFF3A4A1AE1FFD:
  - swapon
  MAN_84AFF3A4A1AE1FFD--84aff3a4a1ae:
  - swapoff
  MAN_851836A4A52C54C4:
  - mkdirat
  MAN_851C55E19663FC3F:
  - syncfs
  MAN_851C55E19663FC3F--851c55e19663:
  - sync
  MAN_85292F3B5D5E6D81:
  - sendfile
  MAN_8582371E66C66488:
  - clone3
  MAN_8582371E66C66488--8582371e66c6:
  - clone
  MAN_858379EE26708EF4:
  - vmsplice
  MAN_85893C92714AFA8C:
  - setns
  MAN_858C80BFA969F710:
  - perf_event_open
  MAN_8609DB2EE85AF88E:
  - seccomp
  MAN_864218B9B08F7337:
  - symlinkat
  MAN_869D25DD5A735F5D:
  - msgsnd
  MAN_869D25DD5A735F5D--869d25dd5a73:
  - msgrcv
  MAN_86F55F465483D85E:
  - execve
  MAN_8708D0B9241DF0D1:
  - sendfile
  MAN_8711CFFA529772CC:
  - readv
  MAN_87330F75C40E095C:
  - mount_setattr
  MAN_8737280B3EFAA24B:
  - fchmodat
  MAN_873728C9D1BA408C:
  - openat
  MAN_874EC668B942F052:
  - symlinkat
  MAN_87702F6D032D14E7:
  - ioctl
  MAN_87A54598F831FF80:
  - perf_event_open
  MAN_88007F0FB13468A5:
  - readahead
  MAN_8812ADE8E360DB8F:
  - shutdown
  MAN_881E980687FFBD0A:
  - setns
  MAN_881F5DA24E112BB1:
  - clone3
  MAN_881F5DA24E112BB1--881f5da24e11:
  - clone
  MAN_8853FCE83FBE1DF6:
  - fsmount
  MAN_8858939ED981F762:
  - getsockopt
  MAN_889ECFD531C4AA95:
  - chroot
  MAN_88A70718E5AB4943:
  - getcwd
  MAN_88AA1B8D587246C5:
  - linkat
  MAN_88C413D737D75B48:
  - setns
  MAN_88CEA369D8FB4020:
  - recvmsg
  MAN_88CEA369D8FB4020--88cea369d8fb:
  - recvfrom
  MAN_8931B36733AA3FCD:
  - mq_timedreceive
  MAN_896A525A8FEEC85C:
  - fallocate
  MAN_896E769EA1469E0D:
  - setxattr
  MAN_896E769EA1469E0D--896e769ea146:
  - fsetxattr
  MAN_898010CF460EB43C:
  - process_madvise
  MAN_89D33AB929D9531F:
  - execve
  MAN_89E33C13364E12DD:
  - getpeername
  MAN_89E3C30B0523F613:
  - fchdir
  MAN_89E3C30B0523F613--89e3c30b0523:
  - chdir
  MAN_8A1D7EAFA0E22D7F:
  - lsetxattr
  MAN_8A7D8855CC5F6AF8:
  - getrandom
  MAN_8AA6A5D0F506569F:
  - mount
  MAN_8AB5CA1BFA7C8E65:
  - sendto
  MAN_8AB5CA1BFA7C8E65--8ab5ca1bfa7c:
  - sendmsg
  MAN_8AEECADC51B07B46:
  - setxattr
  MAN_8AEECADC51B07B46--8aeecadc51b0:
  - fsetxattr
  MAN_8B18C50F6D60DA10:
  - newfstatat
  MAN_8B18C50F6D60DA10--8b18c50f6d60:
  - fstat
  MAN_8B28C4656CECAFDA:
  - truncate
  MAN_8B28C4656CECAFDA--8b28c4656cec:
  - ftruncate
  MAN_8B44353A560CAC65:
  - init_module
  MAN_8B44353A560CAC65--8b44353a560c:
  - finit_module
  MAN_8B9E7EB9BDAD45CF:
  - membarrier
  MAN_8BAB63F189D5F352:
  - kexec_load
  MAN_8BAB63F189D5F352--8bab63f189d5:
  - kexec_file_load
  MAN_8C544CC609884175:
  - faccessat2
  MAN_8C544CC609884175--8c544cc60988:
  - faccessat
  MAN_8C63A41969A0352B:
  - readv
  MAN_8C6E18A34BED8073:
  - renameat2
  MAN_8CEC520B690B55F8:
  - fchdir
  MAN_8CFD0BE9CC831F8F:
  - openat
  MAN_8D160F5D77EC235B:
  - setgroups
  MAN_8D160F5D77EC235B--8d160f5d77ec:
  - getgroups
  MAN_8D43E194EA5A4EA4:
  - kexec_load
  MAN_8D43E194EA5A4EA4--8d43e194ea5a:
  - kexec_file_load
  MAN_8D44C3E0FA81DC95:
  - ioctl
  MAN_8D5685E6EF9F9E48:
  - openat
  MAN_8D6CC9127F1C081F:
  - inotify_add_watch
  MAN_8D7222D703F93461:
  - nanosleep
  MAN_8D7C242C09ADC94C:
  - timerfd_settime
  MAN_8D7C242C09ADC94C--8d7c242c09ad:
  - timerfd_create
  MAN_8D8F7FBF6D6DC598:
  - semctl
  MAN_8DA0B273933CFFA0:
  - getgroups
  MAN_8DA7BF60E6D5385A:
  - write
  MAN_8DB0AB4E3B90CB50:
  - munmap
  MAN_8DB0AB4E3B90CB50--8db0ab4e3b90:
  - mmap
  MAN_8DBB20D706FD804F:
  - madvise
  MAN_8DDE21A60384015C:
  - fchdir
  MAN_8DDE21A60384015C--8dde21a60384:
  - chdir
  MAN_8DF0925852832A7B:
  - open_by_handle_at
  MAN_8DF0925852832A7B--8df092585283:
  - name_to_handle_at
  MAN_8DF108DD14D05A4E:
  - renameat2
  MAN_8E0C833FE24F3D98:
  - bind
  MAN_8E228CEF94A89B00:
  - fanotify_mark
  MAN_8E5A1197355FE232:
  - rt_sigtimedwait
  MAN_8E78EB82EBFE1E18:
  - openat
  MAN_8EB5DAC98CC4E560:
  - openat
  MAN_8EBE30A859B792C3:
  - clock_nanosleep
  MAN_8EDE243F1CC1990E:
  - timerfd_settime
  MAN_8EDE243F1CC1990E--8ede243f1cc1:
  - timerfd_create
  MAN_8EE6A82F777B19BA:
  - msync
  MAN_8F289CB281281804:
  - pidfd_send_signal
  MAN_8F57FC9DB76DC9F7:
  - shmget
  MAN_8F8AE50242F2C31D:
  - symlinkat
  MAN_8FA4B2BD0621C33E:
  - bind
  MAN_8FB4E1D60F608E5C:
  - mkdirat
  MAN_8FC8E163410C47D3:
  - setxattr
  MAN_8FC8E163410C47D3--8fc8e163410c:
  - fsetxattr
  MAN_9021A0739A34E0FF:
  - mknodat
  MAN_902FE9C05B65909D:
  - lgetxattr
  MAN_902FE9C05B65909D--902fe9c05b65:
  - fgetxattr
  MAN_907D4A348A8AA89E:
  - timerfd_settime
  MAN_907D4A348A8AA89E--907d4a348a8a:
  - timerfd_create
  MAN_90C3670105A9BF3A:
  - mq_notify
  MAN_91422D4DBF7854C3:
  - accept4
  MAN_91422D4DBF7854C3--91422d4dbf78:
  - accept
  MAN_915DDBF0C801C17D:
  - unshare
  MAN_915E5D286EE4EC6B:
  - clone3
  MAN_915E5D286EE4EC6B--915e5d286ee4:
  - clone
  MAN_91672FDAF9FD1269:
  - timerfd_gettime
  MAN_91A99AD8F9260676:
  - msgrcv
  MAN_91B064A60E749B82:
  - clone3
  MAN_91B064A60E749B82--91b064a60e74:
  - clone
  MAN_91D2EF33DBA30D0D:
  - mount
  MAN_91EE775821BB386C:
  - mq_unlink
  MAN_9214C9CAF5FBEAE8:
  - getdents64
  MAN_921EEBD96B62E18A:
  - acct
  MAN_926273F22D577E3A:
  - clock_settime
  MAN_9265198EAC52989E:
  - timerfd_settime
  MAN_9265198EAC52989E--9265198eac52:
  - timerfd_create
  MAN_928C8BCADF71D467:
  - utimensat
  MAN_92D06F825C199161:
  - msgget
  MAN_92DE07CA127E7228:
  - setrlimit
  MAN_92DE07CA127E7228--92de07ca127e:
  - getrlimit
  MAN_932E951D0FBCB63E:
  - renameat2
  MAN_9362B04A1AF76D5C:
  - munlock
  MAN_93C1F96D342A3502:
  - acct
  MAN_93EBFE5E9F1617AF:
  - fallocate
  MAN_94196ADBF12086B2:
  - socket
  MAN_941DDE995AA26AC2:
  - truncate
  MAN_941DDE995AA26AC2--941dde995aa2:
  - ftruncate
  MAN_9452D425539B8023:
  - socketpair
  MAN_945A7C74F6C05E02:
  - mount
  MAN_947DCF45679C83F9:
  - renameat2
  MAN_94911D7DD151668A:
  - remap_file_pages
  MAN_94C6721D75F7461E:
  - msgsnd
  MAN_94C6721D75F7461E--94c6721d75f7:
  - msgrcv
  MAN_94FC6A492861E510:
  - cachestat
  MAN_9507A0BFA121CBD7:
  - request_key
  MAN_9536A31C78C4468C:
  - msgsnd
  MAN_9536A31C78C4468C--9536a31c78c4:
  - msgrcv
  MAN_953F196E7342141E:
  - mount
  MAN_955D6BCEE6FF9CA2:
  - munlockall
  MAN_955D6BCEE6FF9CA2--955d6bcee6ff:
  - mlock
  MAN_9568CF230A4C9233:
  - execveat
  MAN_9579EA0993D2ECDF:
  - chroot
  MAN_957A42849C43B265:
  - move_mount
  MAN_95930C2D369C878D:
  - timer_delete
  MAN_95AE27469C0D0FB0:
  - accept4
  MAN_95AE27469C0D0FB0--95ae27469c0d:
  - accept
  MAN_95E4D0042A8E60AF:
  - acct
  MAN_9634121FAACFB898:
  - setuid
  MAN_968D07C7039689E5:
  - setdomainname
  MAN_96A47A27204EC107:
  - openat
  MAN_96CBA8A60D52BB1A:
  - fsopen
  MAN_972985852EC9A0D4:
  - landlock_add_rule
  MAN_972F2545B7976217:
  - swapon
  MAN_972F2545B7976217--972f2545b797:
  - swapoff
  MAN_97FF66B73DB1E098:
  - vhangup
  MAN_980D102A668B4ABA:
  - capset
  MAN_980D102A668B4ABA--980d102a668b:
  - capget
  MAN_982F9E63713F514A:
  - fsmount
  MAN_986CDFEBF5C51B6F:
  - kexec_load
  MAN_986CDFEBF5C51B6F--986cdfebf5c5:
  - kexec_file_load
  MAN_98854708CB479BB5:
  - sendto
  MAN_98854708CB479BB5--98854708cb47:
  - sendmsg
  MAN_9897C2A7108BFB4A:
  - waitid
  MAN_98A629AF2556600E:
  - accept4
  MAN_98A629AF2556600E--98a629af2556:
  - accept
  MAN_98B0BE7D9A11DFBB:
  - execve
  MAN_98C836EAC7D4691D:
  - clock_gettime
  MAN_98D179221ED73D7D:
  - write
  MAN_992F98DB3460FD4C:
  - mknodat
  MAN_998844B56687D754:
  - get_mempolicy
  MAN_9997FFB8AA0BC13C:
  - munmap
  MAN_9997FFB8AA0BC13C--9997ffb8aa0b:
  - mmap
  MAN_99C67AD88E641D59:
  - epoll_pwait2
  MAN_99C67AD88E641D59--99c67ad88e64:
  - epoll_pwait
  MAN_99D6BE23E27B3A69:
  - landlock_create_ruleset
  MAN_99E511CB0DD6BD8B:
  - mq_notify
  MAN_9A17C8A141B47D41:
  - fchmodat
  MAN_9A1A12604E4AB2D2:
  - fchownat
  MAN_9A1A12604E4AB2D2--9a1a12604e4a:
  - fchown
  MAN_9B27D6FD35CE0515:
  - sched_setattr
  MAN_9B27D6FD35CE0515--9b27d6fd35ce:
  - sched_getattr
  MAN_9B43999C26D767B8:
  - statfs
  MAN_9B6A1BB2706D888E:
  - landlock_add_rule
  MAN_9B7256CF8D182953:
  - pkey_mprotect
  MAN_9B7256CF8D182953--9b7256cf8d18:
  - mprotect
  MAN_9B8A51F07CDB1092:
  - flock
  MAN_9B95D3E42B4918C6:
  - openat2
  MAN_9B9DE9517916476A:
  - setsockopt
  MAN_9BC94E6BD25C05E1:
  - dup3
  MAN_9BDA074CCC8604C4:
  - mremap
  MAN_9BDD1022EAC68DED:
  - mq_open
  MAN_9C167BA5F188F234:
  - add_key
  MAN_9C65752BB2FC3F99:
  - timerfd_settime
  MAN_9C65752BB2FC3F99--9c65752bb2fc:
  - timerfd_create
  MAN_9C82783CCAC8EF0D:
  - io_getevents
  MAN_9C92528E1F8DF9C9:
  - umount2
  MAN_9CC0EE7106975DEB:
  - shmget
  MAN_9CC26FBE27A0B0D1:
  - accept4
  MAN_9CC26FBE27A0B0D1--9cc26fbe27a0:
  - accept
  MAN_9CD8BB8BC1A82C97:
  - waitid
  MAN_9CE623FA91E6B3F5:
  - statmount
  MAN_9CE9FA3B8753B4D9:
  - pipe2
  MAN_9D6B030DFB14753E:
  - set_robust_list
  MAN_9D6B030DFB14753E--9d6b030dfb14:
  - get_robust_list
  MAN_9D919535454487A7:
  - linkat
  MAN_9D927E01D804753D:
  - sched_setattr
  MAN_9D927E01D804753D--9d927e01d804:
  - sched_getattr
  MAN_9DA524ED947C6C91:
  - init_module
  MAN_9DA524ED947C6C91--9da524ed947c:
  - finit_module
  MAN_9DC190C7DAEFA324:
  - landlock_add_rule
  MAN_9DD61ABB88830438:
  - fanotify_mark
  MAN_9DE6F8DEA123E9BE:
  - ioctl
  MAN_9E0C30E4205FB415:
  - memfd_create
  MAN_9E0F46165E1997DC:
  - fsconfig
  MAN_9E12AA9A59F1BBE9:
  - sethostname
  MAN_9E1FA9C956A923BA:
  - fallocate
  MAN_9E2263041F8B8CF7:
  - request_key
  MAN_9E6C8CDC569BD8EB:
  - mq_timedsend
  MAN_9EAF81A361AB87DA:
  - kill
  MAN_9F137E9A314E991F:
  - process_vm_writev
  MAN_9F137E9A314E991F--9f137e9a314e:
  - process_vm_readv
  MAN_9FD0FF5AD8750E16:
  - quotactl_fd
  MAN_9FD0FF5AD8750E16--9fd0ff5ad875:
  - quotactl
  MAN_9FD2A586602BFF5C:
  - faccessat2
  MAN_9FD2A586602BFF5C--9fd2a586602b:
  - faccessat
  MAN_9FD391343E0DB6C0:
  - execve
  MAN_9FD6C6C82F2667E8:
  - timer_create
  MAN_9FF10B506400747E:
  - pidfd_send_signal
  MAN_A055049575FB6E47:
  - seccomp
  MAN_A09ACAFDEC1F22CD:
  - bind
  MAN_A0A4C98B164C92C3:
  - sched_getattr
  MAN_A0ACFECCA081DE2D:
  - getpeername
  MAN_A0E2616F3C9DAC4B:
  - timerfd_settime
  MAN_A102E2A8F5431678:
  - epoll_create1
  MAN_A11FFFA10819A17D:
  - renameat2
  MAN_A13A15172625B56C:
  - chroot
  MAN_A1576844286DE3E1:
  - sendfile
  MAN_A16A4CAD298D4C96:
  - write
  MAN_A18F05DC5097AB99:
  - sched_setattr
  MAN_A18F05DC5097AB99--a18f05dc5097:
  - sched_getattr
  MAN_A1980EA9E5FF0FBE:
  - fsconfig
  MAN_A1A5EBA2742E6366:
  - move_pages
  MAN_A1CD98CE32C423E4:
  - socket
  MAN_A1CDFA609E31D6DB:
  - unlinkat
  MAN_A1DD124B05A5DBAD:
  - read
  MAN_A1E1A71D9BC8837D:
  - nanosleep
  MAN_A1F3E03B6CED61C7:
  - pwritev
  MAN_A1FE4D52AB81BEEB:
  - setrlimit
  MAN_A1FE4D52AB81BEEB--a1fe4d52ab81:
  - getrlimit
  MAN_A2141F553DF3DB38:
  - ioctl
  MAN_A250385139EBE1CD:
  - process_madvise
  MAN_A255AC65EABEF838:
  - socket
  MAN_A255EF68F9FD4BC8:
  - open_by_handle_at
  MAN_A255EF68F9FD4BC8--a255ef68f9fd:
  - name_to_handle_at
  MAN_A2A0AA9FF144AE43:
  - lookup_dcookie
  MAN_A2BE90247949F31E:
  - preadv2
  MAN_A2E87AB73AB47803:
  - unshare
  MAN_A31A9CCB700DE939:
  - shmctl
  MAN_A3E9866D3AB15A34:
  - clone3
  MAN_A3F5F031E1166D3E:
  - landlock_create_ruleset
  MAN_A449F3FE48E6AF41:
  - fanotify_mark
  MAN_A46653313E932AE4:
  - sched_setparam
  MAN_A46653313E932AE4--a46653313e93:
  - sched_getparam
  MAN_A4B144E424AFA7F1:
  - bpf
  MAN_A4B87004CF6845EB:
  - shmctl
  MAN_A4D22E8455997722:
  - statmount
  MAN_A4EA63A863940B27:
  - statfs
  MAN_A5040F825A88BCD6:
  - listmount
  MAN_A58EA189B1C9E326:
  - faccessat2
  MAN_A58EA189B1C9E326--a58ea189b1c9:
  - faccessat
  MAN_A5C000C82107F300:
  - mount
  MAN_A5D9BE5EC5050F2D:
  - move_mount
  MAN_A5DF7E1179E6ED23:
  - open_by_handle_at
  MAN_A5DF7E1179E6ED23--a5df7e1179e6:
  - name_to_handle_at
  MAN_A5E61A889FE6459A:
  - pkey_free
  MAN_A5E61A889FE6459A--a5e61a889fe6:
  - pkey_alloc
  MAN_A5F4BA2371332A4E:
  - eventfd2
  MAN_A61FDA2E6CA66366:
  - statfs
  MAN_A61FDA2E6CA66366--a61fda2e6ca6:
  - fstatfs
  MAN_A62F2B2A440B901E:
  - sync_file_range
  MAN_A6341851FD5B840C:
  - ptrace
  MAN_A637DDA9F34883F7:
  - munmap
  MAN_A637DDA9F34883F7--a637dda9f348:
  - mmap
  MAN_A650A050193AE2D3:
  - fallocate
  MAN_A67DCE77030808A6:
  - clock_gettime
  MAN_A68CC55C5764955D:
  - openat2
  MAN_A6DCF38727C07D85:
  - rt_tgsigqueueinfo
  MAN_A6DCF38727C07D85--a6dcf38727c0:
  - rt_sigqueueinfo
  MAN_A6FE87EBBFDE4983:
  - fchmodat
  MAN_A6FE87EBBFDE4983--a6fe87ebbfde:
  - fchmod
  MAN_A72109DBCD03580F:
  - utimensat
  MAN_A764576C2376AFC1:
  - migrate_pages
  MAN_A773383194DAD007:
  - symlinkat
  MAN_A7944CED184DE54B:
  - pidfd_open
  MAN_A7F5466F6F1B9169:
  - fanotify_init
  MAN_A7FB1A674D256169:
  - readahead
  MAN_A806B183ABD7937F:
  - swapon
  MAN_A816B03D718279E1:
  - getcwd
  MAN_A832C347A254AB7F:
  - preadv2
  MAN_A8722C6BD1B498C5:
  - mkdirat
  MAN_A882E273B1BFA83C:
  - renameat2
  MAN_A89B57ABD09FA4DD:
  - mount
  MAN_A89DCFB25B2DA7A6:
  - faccessat2
  MAN_A89DCFB25B2DA7A6--a89dcfb25b2d:
  - faccessat
  MAN_A912AD870D7ADEEA:
  - setresuid
  MAN_A912AD870D7ADEEA--a912ad870d7a:
  - setresgid
  MAN_A914DC7A9C01FF37:
  - fchmodat
  MAN_A914DC7A9C01FF37--a914dc7a9c01:
  - fchmod
  MAN_A941E98A7CBC5E96:
  - semget
  MAN_A94BF61B92A283CE:
  - settimeofday
  MAN_A94EF971BED4AA30:
  - sigaltstack
  MAN_A953E8990237D494:
  - setxattr
  MAN_A953E8990237D494--a953e8990237:
  - fsetxattr
  MAN_A95D8DE641D5242B:
  - acct
  MAN_A97621B251F86EF2:
  - mq_timedreceive
  MAN_A9B55CF3F83DE90B:
  - renameat2
  MAN_A9BEB19AB03CA0AD:
  - symlinkat
  MAN_A9D96AD1D8F35A36:
  - fchdir
  MAN_A9D96AD1D8F35A36--a9d96ad1d8f3:
  - chdir
  MAN_AA342D41284C8043:
  - sysinfo
  MAN_AA8C115068BD5D76:
  - newfstatat
  MAN_AA8C115068BD5D76--aa8c115068bd:
  - fstat
  MAN_AAA2AB163B724C66:
  - getcwd
  MAN_AAC48B97DF41D5C9:
  - semtimedop
  MAN_AAC48B97DF41D5C9--aac48b97df41:
  - semop
  MAN_AAE473B32F377E07:
  - madvise
  MAN_AAEC2B0A6F00223E:
  - rt_tgsigqueueinfo
  MAN_AAEC2B0A6F00223E--aaec2b0a6f00:
  - rt_sigqueueinfo
  MAN_AB29953502749E9B:
  - pselect6
  MAN_AB7BF6BD963B9581:
  - utimensat
  MAN_AB84286FEBD5DA77:
  - seccomp
  MAN_AB92E268E38379C8:
  - fspick
  MAN_ABF2BDBD0DE18170:
  - statfs
  MAN_ABF2BDBD0DE18170--abf2bdbd0de1:
  - fstatfs
  MAN_AC01308A7DFD4FF6:
  - renameat2
  MAN_AC10C09BF76080EA:
  - mlockall
  MAN_AC29B19E10FB71E2:
  - acct
  MAN_AC65964463FBA3CE:
  - semtimedop
  MAN_AC65964463FBA3CE--ac65964463fb:
  - semop
  MAN_AC9D2A4AE994EB59:
  - mount_setattr
  MAN_AC9D72E0631EDF66:
  - process_madvise
  MAN_ACC58504C141BC9E:
  - madvise
  MAN_ACCEC8B73BD102B8:
  - clone3
  MAN_ACD89E42FD5F6797:
  - setresuid
  MAN_ACD89E42FD5F6797--acd89e42fd5f:
  - setresgid
  MAN_AD1A050636B2B976:
  - open_by_handle_at
  MAN_AD1A050636B2B976--ad1a050636b2:
  - name_to_handle_at
  MAN_AD44624A5F6D7CF5:
  - setns
  MAN_AD466FE1EF1E51A4:
  - renameat2
  MAN_AD4D4A5F416F9F5A:
  - mq_open
  MAN_AD5E816980269EC5:
  - pwritev
  MAN_AD651DC28E22F8A2:
  - accept4
  MAN_AD651DC28E22F8A2--ad651dc28e22:
  - accept
  MAN_AD66BC96095868B7:
  - clock_nanosleep
  MAN_AD6806531390142E:
  - setns
  MAN_AD8AA7D30E236578:
  - truncate
  MAN_AD8AA7D30E236578--ad8aa7d30e23:
  - ftruncate
  MAN_AD9A71FB720F3F16:
  - renameat2
  MAN_ADCC2407A0C9100B:
  - execve
  MAN_AE06BA421FC93637:
  - mount_setattr
  MAN_AE37AAAE949CCFB1:
  - setitimer
  MAN_AE37AAAE949CCFB1--ae37aaae949c:
  - getitimer
  MAN_AE46DE0C8B9366F0:
  - io_submit
  MAN_AE68C41A115C80FC:
  - sendto
  MAN_AE68C41A115C80FC--ae68c41a115c:
  - sendmsg
  MAN_AE759265E8EFB39C:
  - renameat2
  MAN_AE7C62637F29A4C9:
  - listen
  MAN_AE9B7D3358ABF2B1:
  - add_key
  MAN_AEA35FE35AC29F86:
  - quotactl_fd
  MAN_AEA35FE35AC29F86--aea35fe35ac2:
  - quotactl
  MAN_AF1D093225F75E82:
  - timer_delete
  MAN_AF6B7627EDF8880A:
  - munmap
  MAN_AF6B7627EDF8880A--af6b7627edf8:
  - mmap
  MAN_AF87083AF942513B:
  - renameat2
  MAN_AFA998EF36C95F83:
  - recvmsg
  MAN_AFA998EF36C95F83--afa998ef36c9:
  - recvfrom
  MAN_AFE95DD67806690E:
  - pkey_mprotect
  MAN_B05C5A299862E91C:
  - init_module
  MAN_B05C5A299862E91C--b05c5a299862:
  - finit_module
  MAN_B0C5FA353BC03C32:
  - fchownat
  MAN_B0C5FA353BC03C32--b0c5fa353bc0:
  - fchown
  MAN_B0CC9593D166E4F1:
  - perf_event_open
  MAN_B0CDDE4BB5732341:
  - shmget
  MAN_B0EBC4F02BF1D777:
  - mq_timedreceive
  MAN_B11F8E4A790E5EC1:
  - mq_timedsend
  MAN_B121E5340A1BEFEE:
  - socketpair
  MAN_B15C5F28E800B98D:
  - getsockname
  MAN_B183F712297ADDB0:
  - semget
  MAN_B1A8365C419E3164:
  - setpriority
  MAN_B1A8365C419E3164--b1a8365c419e:
  - getpriority
  MAN_B1C40D0A6429611D:
  - ioctl
  MAN_B1C70DEFAF919FA0:
  - move_mount
  MAN_B218FCEF9CD238BC:
  - unlinkat
  MAN_B2775D86DE47E6DF:
  - clone3
  MAN_B2775D86DE47E6DF--b2775d86de47:
  - clone
  MAN_B27964BE47C0BFAF:
  - fanotify_mark
  MAN_B2E7AF7C7993204D:
  - landlock_create_ruleset
  MAN_B2FA2520FCDBEF6E:
  - socket
  MAN_B32F28EABF8E5C58:
  - bpf
  MAN_B35DF8C645BF0365:
  - clock_settime
  MAN_B35DF8C645BF0365--b35df8c645bf:
  - clock_getres
  MAN_B3ADDA02AC4782A5:
  - delete_module
  MAN_B3B13791F0D4F8B6:
  - pidfd_send_signal
  MAN_B3F5DA727757964E:
  - munmap
  MAN_B3F5DA727757964E--b3f5da727757:
  - mmap
  MAN_B40E9995A7563644:
  - kill
  MAN_B433B3C8DACC5EB4:
  - connect
  MAN_B44100F9E5A75D06:
  - unshare
  MAN_B4A1F34DFF24820E:
  - renameat2
  MAN_B4D23D7C4AF42D3C:
  - landlock_create_ruleset
  MAN_B4DD5B60F33FC5E3:
  - unshare
  MAN_B4E8714DE8F1D8BC:
  - times
  MAN_B4E9426B661E238A:
  - fsync
  MAN_B4E9426B661E238A--b4e9426b661e:
  - fdatasync
  MAN_B4EB3CCA939EC706:
  - inotify_add_watch
  MAN_B52C9E05680C92E3:
  - ppoll
  MAN_B5426A9A136480B8:
  - fsconfig
  MAN_B57710221C3BD405:
  - close_range
  MAN_B579CA52E8AA4E73:
  - umount2
  MAN_B58395BCFB66624C:
  - bind
  MAN_B5B4336BB8725601:
  - newfstatat
  MAN_B5E18528035F6F87:
  - preadv2
  MAN_B623C916A0D0C52B:
  - recvmsg
  MAN_B623C916A0D0C52B--b623c916a0d0:
  - recvfrom
  MAN_B625679ADE8C1D29:
  - truncate
  MAN_B625679ADE8C1D29--b625679ade8c:
  - ftruncate
  MAN_B6312970F8FECF39:
  - mlock2
  MAN_B68320435E94E3AB:
  - mknodat
  MAN_B6A8CADA204B8089:
  - fallocate
  MAN_B6D195DF26E5FDE3:
  - clone3
  MAN_B6D195DF26E5FDE3--b6d195df26e5:
  - clone
  MAN_B6D39593C5B87DB5:
  - bind
  MAN_B7505628CCA74CC9:
  - accept4
  MAN_B7505628CCA74CC9--b7505628cca7:
  - accept
  MAN_B75BC21DDFF7D484:
  - read
  MAN_B7636B4F22A1320E:
  - perf_event_open
  MAN_B776E385902BFBDD:
  - umount2
  MAN_B7819B40D95FBD97:
  - lsetxattr
  MAN_B78223A10681416D:
  - socket
  MAN_B7A23D1397B57043:
  - timerfd_gettime
  MAN_B7A51FEC15E193EF:
  - pivot_root
  MAN_B7EACF5BB0567B6D:
  - getresuid
  MAN_B7EACF5BB0567B6D--b7eacf5bb056:
  - getresgid
  MAN_B7FE0F4D79FB1B07:
  - setsid
  MAN_B8030FC30CABD8CE:
  - clone3
  MAN_B8030FC30CABD8CE--b8030fc30cab:
  - clone
  MAN_B821196BEABAEB30:
  - msgsnd
  MAN_B821196BEABAEB30--b821196beaba:
  - msgrcv
  MAN_B8AAF34D422EFA92:
  - rt_sigprocmask
  MAN_B8B203E8CD1E3391:
  - bind
  MAN_B8C50B33ADC409A0:
  - open_tree
  MAN_B928D3AB5842791C:
  - sched_setaffinity
  MAN_B9BCD17233CD51DC:
  - lookup_dcookie
  MAN_B9EE0F176B92F526:
  - seccomp
  MAN_BA0DEE128FDEC28D:
  - munlock
  MAN_BA0DEE128FDEC28D--ba0dee128fde:
  - mlock
  MAN_BA170A0867842086:
  - clone3
  MAN_BA170A0867842086--ba170a086784:
  - clone
  MAN_BA258B6237A7C6F7:
  - readlinkat
  MAN_BA2A01C792497916:
  - openat
  MAN_BA4FBB07831E338E:
  - waitid
  MAN_BB3D8A84A281D347:
  - io_cancel
  MAN_BB48213DAFA22DC1:
  - clone3
  MAN_BB48213DAFA22DC1--bb48213dafa2:
  - clone
  MAN_BBAD44E149174DDA:
  - madvise
  MAN_BBBDBFFF3302C2C9:
  - fsync
  MAN_BBBDBFFF3302C2C9--bbbdbfff3302:
  - fdatasync
  MAN_BBC1439D735A48EB:
  - utimensat
  MAN_BC03B820E6800CAE:
  - setxattr
  MAN_BC03B820E6800CAE--bc03b820e680:
  - fsetxattr
  MAN_BC0A333DCC491744:
  - pwritev2
  MAN_BC15177D0740DECA:
  - fanotify_mark
  MAN_BC425C37C792DDEE:
  - copy_file_range
  MAN_BC4618DC029BD6C3:
  - clone3
  MAN_BC71D974F2E7DC73:
  - renameat2
  MAN_BC766A7E60DD5054:
  - remap_file_pages
  MAN_BC8EA96177E7784D:
  - munlock
  MAN_BCB77DDA6E2D5CCD:
  - kcmp
  MAN_BCC6BC6BC77904EA:
  - read
  MAN_BCD9474510C6AD2C:
  - mq_unlink
  MAN_BCDFA2381F449DD2:
  - io_cancel
  MAN_BD0D19DE76F2E8C5:
  - utimensat
  MAN_BD2F8B276CA6BF2C:
  - semtimedop
  MAN_BD2F8B276CA6BF2C--bd2f8b276ca6:
  - semop
  MAN_BD547767C2C7DD9A:
  - fsconfig
  MAN_BD5ACF7CBE854872:
  - syslog
  MAN_BD984637492BE042:
  - fsconfig
  MAN_BD995790062ADA93:
  - setreuid
  MAN_BDD54C63170F37A9:
  - setpgid
  MAN_BDD752F0E4415444:
  - mbind
  MAN_BDE63EEF419087CB:
  - openat2
  MAN_BE4A1F7A2F5140EB:
  - mq_open
  MAN_BE74B0D21973DAEC:
  - seccomp
  MAN_BE8EB8AAFBB857CE:
  - copy_file_range
  MAN_BE929AB9651E5E66:
  - eventfd2
  MAN_BE9A7AEBFB53C64A:
  - epoll_ctl
  MAN_BEEA719C40330D95:
  - kexec_load
  MAN_BEEA719C40330D95--beea719c4033:
  - kexec_file_load
  MAN_BF0AE6B4EE7A8148:
  - set_mempolicy
  MAN_BF11094B09637BF2:
  - timer_settime
  MAN_BF11094B09637BF2--bf11094b0963:
  - timer_gettime
  MAN_BF90BB5511FA5EC2:
  - fsopen
  MAN_BFA07FE3DAEE776B:
  - kcmp
  MAN_BFA5EEEE4632F929:
  - fsconfig
  MAN_BFC49E23D6364C40:
  - mq_timedreceive
  MAN_BFF81F70E3770EAB:
  - connect
  MAN_C02EC2F844CFD6EC:
  - kcmp
  MAN_C04F44BFF720877B:
  - inotify_rm_watch
  MAN_C06EFBBC3DC7A962:
  - truncate
  MAN_C06EFBBC3DC7A962--c06efbbc3dc7:
  - ftruncate
  MAN_C0BAAAF74F931836:
  - listxattr
  MAN_C0BDF986D38C2D1E:
  - timerfd_gettime
  MAN_C0E9558A65575B4D:
  - mount
  MAN_C0EBB91F1057DA24:
  - semget
  MAN_C0F0A4D831B3F82B:
  - clone3
  MAN_C1B7540CF853BA57:
  - request_key
  MAN_C1C3070AC65749FA:
  - statfs
  MAN_C1C3070AC65749FA--c1c3070ac657:
  - fstatfs
  MAN_C1EE9766212D328D:
  - setpriority
  MAN_C1EE9766212D328D--c1ee9766212d:
  - getpriority
  MAN_C22AC7C03A3848CE:
  - copy_file_range
  MAN_C24A59A79D89B0CC:
  - epoll_create1
  MAN_C24BA0B8438C9710:
  - execve
  MAN_C2B19612BA400EB6:
  - linkat
  MAN_C390B2BC8654AAA9:
  - futex
  MAN_C3AAE9EA7D50D806:
  - landlock_add_rule
  MAN_C3C4A64CC1B204E2:
  - perf_event_open
  MAN_C3C9D5492817EF26:
  - msgrcv
  MAN_C3CDB84B3F8A1908:
  - lsetxattr
  MAN_C3D2D67DC211C4BB:
  - pivot_root
  MAN_C4337A8B73D63333:
  - linkat
  MAN_C454845A9E055091:
  - madvise
  MAN_C45E594DAEB3C860:
  - setsockopt
  MAN_C45E594DAEB3C860--c45e594daeb3:
  - getsockopt
  MAN_C464BFCB9D6569D5:
  - splice
  MAN_C467D6702AB64674:
  - inotify_init1
  MAN_C480BD0B4E985931:
  - clock_adjtime
  MAN_C480BD0B4E985931--c480bd0b4e98:
  - adjtimex
  MAN_C4B7ABC56F0A1F0B:
  - getxattr
  MAN_C4CC47C200BD0A5B:
  - fsconfig
  MAN_C5359ECB0F177D68:
  - getxattr
  MAN_C55125E9A8ACA961:
  - munlock
  MAN_C55E90828803FC17:
  - fallocate
  MAN_C58A86C162E52514:
  - flock
  MAN_C5AE4F98736C4704:
  - openat
  MAN_C5BDC80761FC531B:
  - get_mempolicy
  MAN_C6190FF4FC99FFA8:
  - chroot
  MAN_C6595E2EB3E6BDB1:
  - listmount
  MAN_C67B732A15F02906:
  - unlinkat
  MAN_C698BC922C135E4E:
  - mlock2
  MAN_C6BB917B58F9645A:
  - utimensat
  MAN_C6C82F1E2B947764:
  - inotify_add_watch
  MAN_C6E3253794915E40:
  - statmount
  MAN_C72E4E80234A34D4:
  - getcpu
  MAN_C73955E76383C54B:
  - inotify_init1
  MAN_C746175F0756F9CB:
  - fanotify_mark
  MAN_C7ED6A7D31815946:
  - semtimedop
  MAN_C7ED6A7D31815946--c7ed6a7d3181:
  - semop
  MAN_C7F2D1ED6833880A:
  - pkey_mprotect
  MAN_C7F2D1ED6833880A--c7f2d1ed6833:
  - mprotect
  MAN_C80AE70AD06ECEDB:
  - faccessat
  MAN_C80C1CF2F5242D7B:
  - timer_settime
  MAN_C80C1CF2F5242D7B--c80c1cf2f524:
  - timer_gettime
  MAN_C81567E2F17B77F1:
  - capset
  MAN_C81567E2F17B77F1--c81567e2f17b:
  - capget
  MAN_C81F46F598B15888:
  - accept4
  MAN_C81F46F598B15888--c81f46f598b1:
  - accept
  MAN_C82CCE9E0EAD8323:
  - symlinkat
  MAN_C87D13932F9035C5:
  - recvmsg
  MAN_C87D13932F9035C5--c87d13932f90:
  - recvfrom
  MAN_C8819A3B768226EC:
  - capset
  MAN_C8819A3B768226EC--c8819a3b7682:
  - capget
  MAN_C8D13C5ADE5FF682:
  - mount
  MAN_C9501D283014E29F:
  - unshare
  MAN_C950B2EE136181EA:
  - mount
  MAN_C969AD34F49996B0:
  - sched_setaffinity
  MAN_C969AD34F49996B0--c969ad34f499:
  - sched_getaffinity
  MAN_C96C83697AEDFB5C:
  - sendfile
  MAN_C99BC5B9688A84D8:
  - fallocate
  MAN_C9A1723E41A5C912:
  - clock_adjtime
  MAN_C9A1723E41A5C912--c9a1723e41a5:
  - adjtimex
  MAN_C9A71FB430C608F4:
  - bpf
  MAN_C9B95BE858EE810B:
  - sendto
  MAN_C9B95BE858EE810B--c9b95be858ee:
  - sendmsg
  MAN_CA0FAFD80C404E1E:
  - ptrace
  MAN_CA36811F7F21408F:
  - madvise
  MAN_CA6F515A86EFABB7:
  - init_module
  MAN_CA6F515A86EFABB7--ca6f515a86ef:
  - finit_module
  MAN_CA71A1FCF0AEBA8C:
  - getpeername
  MAN_CA78A8C72D82663C:
  - landlock_add_rule
  MAN_CAA0FFEFF7C64A82:
  - shutdown
  MAN_CAFB63DDBE2E718F:
  - linkat
  MAN_CB4B434020B46692:
  - rt_sigqueueinfo
  MAN_CB6B2E38FE5D519F:
  - socket
  MAN_CBA3D40918F39277:
  - timerfd_settime
  MAN_CBA3D40918F39277--cba3d40918f3:
  - timerfd_create
  MAN_CBB20D6569C9F207:
  - keyctl
  MAN_CBC626796845BCDD:
  - memfd_secret
  MAN_CBCECA39A48FAB37:
  - execve
  MAN_CBF0C2E0A971180A:
  - mount_setattr
  MAN_CC05E8D45DA351BD:
  - seccomp
  MAN_CC49DE83F3AA9ACF:
  - signalfd4
  MAN_CC4C0FE683280E7B:
  - truncate
  MAN_CC4C0FE683280E7B--cc4c0fe68328:
  - ftruncate
  MAN_CC5D515827EB9E71:
  - fanotify_mark
  MAN_CC73B1B6B2EFAC08:
  - fallocate
  MAN_CC7FC32E9F343B62:
  - mbind
  MAN_CC8A3CE3EBA6AE65:
  - fanotify_mark
  MAN_CD270898CA52F79A:
  - userfaultfd
  MAN_CD32ED6371DC7BD8:
  - connect
  MAN_CD40B0BE68BF389E:
  - futex
  MAN_CD4C08208441CD4D:
  - io_destroy
  MAN_CD82C633B5326E19:
  - open_tree
  MAN_CDC34AFA606D9D64:
  - mq_notify
  MAN_CDD044CBEEED1A80:
  - connect
  MAN_CDD195853C6DFE14:
  - epoll_ctl
  MAN_CE0BCF8762F46A62:
  - epoll_create1
  MAN_CE5EEE412846E8FB:
  - clone3
  MAN_CE5EEE412846E8FB--ce5eee412846:
  - clone
  MAN_CE8E29EE54F86C15:
  - dup3
  MAN_CE8E29EE54F86C15--ce8e29ee54f8:
  - dup
  MAN_CE90DC5D9462A736:
  - mount
  MAN_CEC45E0E1446E3DF:
  - getrandom
  MAN_CEED8CA1867EE4D5:
  - move_mount
  MAN_CF1C83BB9BEB9F17:
  - fsync
  MAN_CF1C83BB9BEB9F17--cf1c83bb9beb:
  - fdatasync
  MAN_CF5613665D9E86B3:
  - bpf
  MAN_CF87E19722FCA735:
  - newfstatat
  MAN_CFA25F5D32CDF0BE:
  - membarrier
  MAN_CFA5EB567B7081CD:
  - mq_notify
  MAN_CFCAF51B4A9782F5:
  - copy_file_range
  MAN_CFF425C920956F88:
  - madvise
  MAN_CFFCD69DBABD472E:
  - acct
  MAN_D025E1D680FE45ED:
  - fsconfig
  MAN_D0277486665C41EB:
  - getdents64
  MAN_D0689B5C0F73071D:
  - kcmp
  MAN_D11BD564A83001EC:
  - signalfd4
  MAN_D11D29899977AEDB:
  - fspick
  MAN_D13F343CBB4650FB:
  - fspick
  MAN_D16701D2ACF7E529:
  - keyctl
  MAN_D172930A07E8B354:
  - getpeername
  MAN_D1849DD3C3EB9602:
  - bpf
  MAN_D1D31517305B224C:
  - madvise
  MAN_D1DD48D16A207E82:
  - preadv2
  MAN_D21E477DD4F6E245:
  - newfstatat
  MAN_D21E477DD4F6E245--d21e477dd4f6:
  - fstat
  MAN_D21E6EC36D70EABC:
  - mount
  MAN_D24B6269E613A2B5:
  - remap_file_pages
  MAN_D2767B9CC3FE596B:
  - mlockall
  MAN_D2BFACFBB0F4563B:
  - memfd_secret
  MAN_D2D79B836C3BCDD5:
  - preadv2
  MAN_D2DA079C0264DF87:
  - clone3
  MAN_D2DA079C0264DF87--d2da079c0264:
  - clone
  MAN_D30152CF0B357E95:
  - io_submit
  MAN_D3083A7F3E863257:
  - unshare
  MAN_D3111E273EAB1465:
  - openat
  MAN_D32E1BC2C09723BA:
  - mbind
  MAN_D345FDC972306DD2:
  - semtimedop
  MAN_D345FDC972306DD2--d345fdc97230:
  - semop
  MAN_D34B7315A88B27CD:
  - clone3
  MAN_D34B7315A88B27CD--d34b7315a88b:
  - clone
  MAN_D375B8E2579C0112:
  - pivot_root
  MAN_D39B258B209CF2E8:
  - splice
  MAN_D39B6DA9C98E2900:
  - fsopen
  MAN_D3A432F08BC25D98:
  - statx
  MAN_D3C3BDCCDA77E8A4:
  - open_by_handle_at
  MAN_D3C3BDCCDA77E8A4--d3c3bdccda77:
  - name_to_handle_at
  MAN_D3CBC683E098A708:
  - statmount
  MAN_D3D27ED470AE00BD:
  - syslog
  MAN_D3EBBEF25F746557:
  - mknodat
  MAN_D405972253EA086F:
  - copy_file_range
  MAN_D43D0F97C08DC1E8:
  - utimensat
  MAN_D459BEAB6F19CAD6:
  - recvmsg
  MAN_D459BEAB6F19CAD6--d459beab6f19:
  - recvfrom
  MAN_D46842A7AA40AC40:
  - getxattr
  MAN_D468436403120505:
  - sched_setaffinity
  MAN_D468436403120505--d46843640312:
  - sched_getaffinity
  MAN_D4EA50CFD38BBDA9:
  - fanotify_mark
  MAN_D52BB21217EFD80E:
  - renameat2
  MAN_D5A08008FF070591:
  - fanotify_mark
  MAN_D5C5CC30462614A3:
  - openat
  MAN_D5CA1153B000D5E0:
  - setuid
  MAN_D5DE8FFAECD9D187:
  - sched_setattr
  MAN_D5DE8FFAECD9D187--d5de8ffaecd9:
  - sched_getattr
  MAN_D6067E26ABCBBF1A:
  - clock_nanosleep
  MAN_D61333A8FF3612C6:
  - init_module
  MAN_D61333A8FF3612C6--d61333a8ff36:
  - finit_module
  MAN_D6150F4C438930BC:
  - fchdir
  MAN_D6150F4C438930BC--d6150f4c4389:
  - chdir
  MAN_D630FA19E1123B77:
  - clone3
  MAN_D66228B4B29734E5:
  - linkat
  MAN_D69AA1715418F1C3:
  - init_module
  MAN_D69AA1715418F1C3--d69aa1715418:
  - finit_module
  MAN_D6D0F5D75DB16A8E:
  - move_mount
  MAN_D6D101C13E36B87E:
  - keyctl
  MAN_D6E10C490BC8A032:
  - fanotify_mark
  MAN_D6FA62852543E52E:
  - listen
  MAN_D709CB4A234A438D:
  - fanotify_init
  MAN_D72A3E318D01D054:
  - clone3
  MAN_D74E2B88CD3854A8:
  - newfstatat
  MAN_D74E2B88CD3854A8--d74e2b88cd38:
  - fstat
  MAN_D75FF16A62863CCC:
  - fsync
  MAN_D75FF16A62863CCC--d75ff16a6286:
  - fdatasync
  MAN_D78039402D1BA184:
  - landlock_restrict_self
  MAN_D78102E703E7449A:
  - utimensat
  MAN_D7A534631D3375E3:
  - init_module
  MAN_D7A534631D3375E3--d7a534631d33:
  - finit_module
  MAN_D7B4CA35F32CC274:
  - io_cancel
  MAN_D7C065933C13D75E:
  - fsopen
  MAN_D80F9C97CCA73F17:
  - cachestat
  MAN_D823C708ADDBDDFC:
  - timerfd_settime
  MAN_D823C708ADDBDDFC--d823c708addb:
  - timerfd_create
  MAN_D8374736030C5DFC:
  - lremovexattr
  MAN_D839675AA549EA73:
  - lseek
  MAN_D84D77F1C6E463F4:
  - clock_gettime
  MAN_D8614FE82771E138:
  - futex_waitv
  MAN_D861A7478C6B0AE1:
  - capset
  MAN_D861A7478C6B0AE1--d861a7478c6b:
  - capget
  MAN_D886C7F9FEEB36D9:
  - init_module
  MAN_D886C7F9FEEB36D9--d886c7f9feeb:
  - finit_module
  MAN_D906B0BC75089225:
  - clock_adjtime
  MAN_D906B0BC75089225--d906b0bc7508:
  - adjtimex
  MAN_D913B6C6A8F45EE6:
  - newfstatat
  MAN_D913B6C6A8F45EE6--d913b6c6a8f4:
  - fstat
  MAN_D92412EE0F393450:
  - readv
  MAN_D93380A5BCC99CFA:
  - shmdt
  MAN_D93380A5BCC99CFA--d93380a5bcc9:
  - shmat
  MAN_D9398A627C44FD69:
  - statmount
  MAN_D9403506773737A0:
  - mq_timedsend
  MAN_D9455E9E9636D4C6:
  - splice
  MAN_D9499271E245B542:
  - set_mempolicy
  MAN_D96BEFFD9E8D80F6:
  - mprotect
  MAN_D97ACD78345B797A:
  - bpf
  MAN_D98A753342D1A76A:
  - connect
  MAN_D9942B91A0EA62B4:
  - madvise
  MAN_D9AD1FA5307C06CC:
  - request_key
  MAN_D9B93A8C37EF88D2:
  - ioprio_set
  MAN_D9B93A8C37EF88D2--d9b93a8c37ef:
  - ioprio_get
  MAN_D9FAA0B9CB1559E4:
  - pwritev2
  MAN_DA06B43ED3D9DBBC:
  - sethostname
  MAN_DA07F10011AB1531:
  - prlimit64
  MAN_DA34EB9987996A2D:
  - execve
  MAN_DA4424044A50393C:
  - seccomp
  MAN_DA4B1EEF45C908DE:
  - semget
  MAN_DA8E6AA5717504D8:
  - unlinkat
  MAN_DA93975DA79D34AD:
  - clock_settime
  MAN_DA93975DA79D34AD--da93975da79d:
  - clock_getres
  MAN_DA953F7047B0040B:
  - bind
  MAN_DAA310AC644BE032:
  - linkat
  MAN_DAB4A58BBA4CA08A:
  - umount2
  MAN_DAD84DA962750B35:
  - fanotify_mark
  MAN_DADCFA23F461FBBF:
  - epoll_ctl
  MAN_DAE2D4DCA95CC6B7:
  - pkey_mprotect
  MAN_DAE2D4DCA95CC6B7--dae2d4dca95c:
  - mprotect
  MAN_DAECFD4F32FD4418:
  - truncate
  MAN_DAECFD4F32FD4418--daecfd4f32fd:
  - ftruncate
  MAN_DAF7EBA5444C7763:
  - msync
  MAN_DAFD5BBDE8A57BCE:
  - semtimedop
  MAN_DAFD5BBDE8A57BCE--dafd5bbde8a5:
  - semop
  MAN_DB0706309C6A7B74:
  - openat
  MAN_DB3DCD854E01E3D4:
  - settimeofday
  MAN_DB49E539DD5F962B:
  - uname
  MAN_DBB19B385BA18829:
  - capset
  MAN_DBB19B385BA18829--dbb19b385ba1:
  - capget
  MAN_DBC3995E6ADEDD4D:
  - pidfd_open
  MAN_DBCF419F762F0AD2:
  - execve
  MAN_DBD043A36C2E4926:
  - copy_file_range
  MAN_DBDBE6B60DA2FFE8:
  - accept4
  MAN_DBEF8C21687D5021:
  - eventfd2
  MAN_DC136E9371B1F879:
  - lsetxattr
  MAN_DC31B3AD6FAFF8DB:
  - process_madvise
  MAN_DC37B979EC91203E:
  - pidfd_open
  MAN_DC75F5C60AE3D1CB:
  - copy_file_range
  MAN_DC7F71A57922E283:
  - execve
  MAN_DC9D6A494C2A2785:
  - bind
  MAN_DC9DC2AF19F995E1:
  - copy_file_range
  MAN_DC9EDE463A887923:
  - lseek
  MAN_DCD266C6F6F1F4C9:
  - mq_open
  MAN_DD1463272A56805B:
  - timerfd_gettime
  MAN_DD35836D94E4B623:
  - newfstatat
  MAN_DD35836D94E4B623--dd35836d94e4:
  - fstat
  MAN_DD6D48EB9B80CB6B:
  - pipe2
  MAN_DD8A18DB0BF6E8A9:
  - memfd_create
  MAN_DD8D475C7F17A478:
  - bind
  MAN_DD9CA389EB41CFD8:
  - setpgid
  MAN_DDCED1DF31BF00F9:
  - fsconfig
  MAN_DDF6041420426380:
  - perf_event_open
  MAN_DE03A6A5B1731AF7:
  - munmap
  MAN_DE03A6A5B1731AF7--de03a6a5b173:
  - mmap
  MAN_DE203EA1663BA227:
  - munlockall
  MAN_DE203EA1663BA227--de203ea1663b:
  - mlock
  MAN_DE214BBDF6500D66:
  - fcntl
  MAN_DE447C82E8D9463B:
  - splice
  MAN_DF0D9E6D3EAA3029:
  - perf_event_open
  MAN_DF102B5594343613:
  - symlinkat
  MAN_DF7F8413F9C29ACE:
  - faccessat2
  MAN_DF7F8413F9C29ACE--df7f8413f9c2:
  - faccessat
  MAN_DF9A47CE544C9A61:
  - fspick
  MAN_DFDA95DD08B133CB:
  - open_tree
  MAN_DFDB86CEA63B78D3:
  - newfstatat
  MAN_DFDB86CEA63B78D3--dfdb86cea63b:
  - fstat
  MAN_DFE30F511AD57632:
  - mount_setattr
  MAN_DFE42730FCD2612D:
  - writev
  MAN_DFE42730FCD2612D--dfe42730fcd2:
  - preadv
  MAN_E0084285A6FB22E7:
  - pselect6
  MAN_E0402378E4A5C8A3:
  - ioctl
  MAN_E0617C1CEDD245DF:
  - perf_event_open
  MAN_E095018DA2554C6D:
  - pidfd_open
  MAN_E0ADDDBCD1DD1FDC:
  - chroot
  MAN_E0BB73518C6E78D5:
  - fallocate
  MAN_E0E71527F649F940:
  - timerfd_gettime
  MAN_E0EA24901A5FC880:
  - open_tree
  MAN_E0FA975BC7359BF8:
  - fallocate
  MAN_E107BAB8F5012718:
  - bpf
  MAN_E110E8D2BC3B4653:
  - sched_setparam
  MAN_E116073D3FDB5C1F:
  - fchdir
  MAN_E116073D3FDB5C1F--e116073d3fdb:
  - chdir
  MAN_E1269EE6A9794ECF:
  - linkat
  MAN_E13CE4DD7419ECC9:
  - fsync
  MAN_E13CE4DD7419ECC9--e13ce4dd7419:
  - fdatasync
  MAN_E1406C89F0FE5EA3:
  - get_mempolicy
  MAN_E197A924533D7848:
  - munmap
  MAN_E197A924533D7848--e197a924533d:
  - mmap
  MAN_E1E951578D046183:
  - pidfd_getfd
  MAN_E1F0BCCEDC6F5513:
  - rt_sigtimedwait
  MAN_E1F2B55F5D48C7B1:
  - memfd_create
  MAN_E270FD5C740C19CF:
  - setreuid
  MAN_E270FD5C740C19CF--e270fd5c740c:
  - setregid
  MAN_E2B541F24026EF59:
  - unlinkat
  MAN_E2C5701A4F2BD7FE:
  - timer_settime
  MAN_E2DD21DCC3524B83:
  - write
  MAN_E31C74C54288401E:
  - pidfd_getfd
  MAN_E32B6349055FCEF9:
  - epoll_ctl
  MAN_E340D16D3735FEAA:
  - open_tree
  MAN_E35105F4A5A6E12D:
  - timer_settime
  MAN_E35105F4A5A6E12D--e35105f4a5a6:
  - timer_gettime
  MAN_E368E68DC18E2BDA:
  - fanotify_init
  MAN_E36D0C88FF32C0FC:
  - open_by_handle_at
  MAN_E36D0C88FF32C0FC--e36d0c88ff32:
  - name_to_handle_at
  MAN_E37FD6E035976DB1:
  - sched_setattr
  MAN_E37FD6E035976DB1--e37fd6e03597:
  - sched_getattr
  MAN_E3993BD58D128E81:
  - fsconfig
  MAN_E420BC3DD1FDF5D1:
  - delete_module
  MAN_E42FB5C7D2882230:
  - copy_file_range
  MAN_E433131871615492:
  - timerfd_settime
  MAN_E433131871615492--e43313187161:
  - timerfd_create
  MAN_E434ABA15111C15A:
  - clone3
  MAN_E4872956AB411B60:
  - sched_setscheduler
  MAN_E497CF592FF38726:
  - mount_setattr
  MAN_E4C0ADD9E49F196F:
  - membarrier
  MAN_E4DBF180B5081307:
  - pipe2
  MAN_E54016783724646E:
  - acct
  MAN_E5AADDE1523DE0B9:
  - sync_file_range
  MAN_E5D9BEF1312E2965:
  - mlock2
  MAN_E5F3CF8AD505B08F:
  - accept4
  MAN_E5F3CF8AD505B08F--e5f3cf8ad505:
  - accept
  MAN_E600CE1E1D196DFF:
  - openat
  MAN_E619B3D21855BAD1:
  - umount2
  MAN_E63289CEF5022A65:
  - eventfd2
  MAN_E6410AAE89E74298:
  - execve
  MAN_E66B035F26F9A88A:
  - removexattr
  MAN_E66B035F26F9A88A--e66b035f26f9:
  - fremovexattr
  MAN_E6708C93C846BFBB:
  - readv
  MAN_E681781B7AEB92F3:
  - sched_setscheduler
  MAN_E681781B7AEB92F3--e681781b7aeb:
  - sched_getscheduler
  MAN_E686ADFB7B643BFF:
  - epoll_create1
  MAN_E6982D508BC5A276:
  - pidfd_send_signal
  MAN_E6C372012351EB4F:
  - userfaultfd
  MAN_E6D70733E8D3CFB2:
  - vmsplice
  MAN_E6E542A8B19F142C:
  - init_module
  MAN_E6E542A8B19F142C--e6e542a8b19f:
  - finit_module
  MAN_E709A8443F71E3F8:
  - shmdt
  MAN_E72ED462D13F9D26:
  - accept4
  MAN_E72ED462D13F9D26--e72ed462d13f:
  - accept
  MAN_E742D8F4E25B2876:
  - io_submit
  MAN_E746A35445D2FFB4:
  - listen
  MAN_E748D19C091C7491:
  - fsconfig
  MAN_E7610DA751EEA18D:
  - fsconfig
  MAN_E770DAFD189C2AA6:
  - uname
  MAN_E795E15ED6FEB891:
  - mremap
  MAN_E7C8A6A2E17934DA:
  - getsid
  MAN_E7D5DCDB1298A068:
  - kexec_load
  MAN_E7D5DCDB1298A068--e7d5dcdb1298:
  - kexec_file_load
  MAN_E7D9A40A6BED7721:
  - truncate
  MAN_E7D9A40A6BED7721--e7d9a40a6bed:
  - ftruncate
  MAN_E8215AC92BB9474D:
  - unlinkat
  MAN_E8412359F61FBABC:
  - open_tree
  MAN_E842151AFA0BF2BD:
  - openat
  MAN_E85BFBF1EB653041:
  - madvise
  MAN_E8705C1E6A8A698D:
  - sigaltstack
  MAN_E8832D2340C65CEF:
  - msgctl
  MAN_E88777B03615ACD8:
  - epoll_pwait2
  MAN_E88777B03615ACD8--e88777b03615:
  - epoll_pwait
  MAN_E8A200A9C5CACE85:
  - munlockall
  MAN_E8A5B768E5CF883B:
  - newfstatat
  MAN_E8C956115049B663:
  - capset
  MAN_E9162190ADD21E2E:
  - mkdirat
  MAN_E953BDB32BA9BC27:
  - bpf
  MAN_E972526DC2F677AF:
  - close
  MAN_E99D067CF243EEE8:
  - dup3
  MAN_E9B0EB62F08112DF:
  - tkill
  MAN_E9B0EB62F08112DF--e9b0eb62f081:
  - tgkill
  MAN_E9CF7CD8699CB8D7:
  - pwritev
  MAN_E9E317DD853949A4:
  - fchmodat
  MAN_E9E317DD853949A4--e9e317dd8539:
  - fchmod
  MAN_E9F079A1D7478DB3:
  - fadvise64
  MAN_EA46692D397289B5:
  - clock_nanosleep
  MAN_EA48F07CE657127F:
  - kcmp
  MAN_EA4A4C5EBDD0FCB1:
  - rt_sigpending
  MAN_EA69373DAD6B5B01:
  - inotify_rm_watch
  MAN_EA7409F3B348F3BE:
  - listmount
  MAN_EAB1501AA183C211:
  - fsconfig
  MAN_EAF8A727CC0094F8:
  - set_robust_list
  MAN_EAF8A727CC0094F8--eaf8a727cc00:
  - get_robust_list
  MAN_EB188262974850B3:
  - unshare
  MAN_EB28F1D95C7DE30B:
  - readahead
  MAN_EB2E1873B06CFC38:
  - removexattr
  MAN_EB2E1873B06CFC38--eb2e1873b06c:
  - fremovexattr
  MAN_EB9E751639BF9272:
  - vmsplice
  MAN_EBD87FCA2D351456:
  - bind
  MAN_EBE7AF4E472D91CC:
  - acct
  MAN_EBF39F7EF83E90BC:
  - madvise
  MAN_EC12D1A6FD24AF6F:
  - request_key
  MAN_EC3BA27562609F21:
  - pselect6
  MAN_EC8D847C182E5431:
  - ptrace
  MAN_EC934DB31C08321C:
  - fchdir
  MAN_EC934DB31C08321C--ec934db31c08:
  - chdir
  MAN_ECC4567FF2E48872:
  - munmap
  MAN_ECC4567FF2E48872--ecc4567ff2e4:
  - mmap
  MAN_ECDB44F1A6E7CCDF:
  - lgetxattr
  MAN_ECDB44F1A6E7CCDF--ecdb44f1a6e7:
  - fgetxattr
  MAN_ECE5AAC8F01E446F:
  - ppoll
  MAN_ECF9786765D6F213:
  - setuid
  MAN_ED0BB543F95CC312:
  - mount
  MAN_ED21BC3F902A78CD:
  - clone3
  MAN_ED21BC3F902A78CD--ed21bc3f902a:
  - clone
  MAN_ED275A56443D1C45:
  - newfstatat
  MAN_ED275A56443D1C45--ed275a56443d:
  - fstat
  MAN_ED76A5F89A22FE98:
  - sendto
  MAN_ED76A5F89A22FE98--ed76a5f89a22:
  - sendmsg
  MAN_ED7D373BBEA8B379:
  - shmget
  MAN_ED8DFFBCDDB66B38:
  - sched_setparam
  MAN_ED8DFFBCDDB66B38--ed8dffbcddb6:
  - sched_getparam
  MAN_EDB775C51FCEA404:
  - pipe2
  MAN_EDC99BF259AB196D:
  - sync_file_range
  MAN_EDD9FFA1EECA3B6B:
  - clone3
  MAN_EDD9FFA1EECA3B6B--edd9ffa1eeca:
  - clone
  MAN_EE618629A4B85EB0:
  - acct
  MAN_EEBEB943F50F772F:
  - futex_waitv
  MAN_EEED9DE5B4E9A1DF:
  - mount_setattr
  MAN_EEF5626873AA6B76:
  - pidfd_send_signal
  MAN_EF463F5807298006:
  - rt_sigprocmask
  MAN_EF4B69DF86EFA0C3:
  - execve
  MAN_EF7244A0D55E1334:
  - linkat
  MAN_EFB3D4CAADB7B785:
  - fchownat
  MAN_EFB3D4CAADB7B785--efb3d4caadb7:
  - fchown
  MAN_EFBA9CA2760DA6B8:
  - inotify_add_watch
  MAN_EFC36EBFC019B943:
  - mq_notify
  MAN_EFCD4E2987D78390:
  - pselect6
  MAN_EFD05ADD9D003336:
  - mlockall
  MAN_F00524DADEC6CE8E:
  - mlockall
  MAN_F02261D5F2501D56:
  - epoll_ctl
  MAN_F023EDF1DAC5BD54:
  - userfaultfd
  MAN_F04C43AC1468F447:
  - timerfd_gettime
  MAN_F0A09B89CC3A3A9D:
  - mount
  MAN_F0DEA31617D8B4BD:
  - unshare
  MAN_F0F7E31A43D3D703:
  - mknodat
  MAN_F101B1F166BED529:
  - epoll_ctl
  MAN_F10EAAC7D96DB347:
  - sched_setaffinity
  MAN_F10EAAC7D96DB347--f10eaac7d96d:
  - sched_getaffinity
  MAN_F11483CF295E52A4:
  - renameat2
  MAN_F12635B7646C0E9B:
  - pwritev2
  MAN_F127E1A1ED64AD5E:
  - setns
  MAN_F1428AAC39E2127D:
  - futex_waitv
  MAN_F14A4FE3E5111DF9:
  - sigaltstack
  MAN_F161B9902C3F53E6:
  - syncfs
  MAN_F161B9902C3F53E6--f161b9902c3f:
  - sync
  MAN_F1E58D8D1B6E95A6:
  - utimensat
  MAN_F21984AE85B3BABA:
  - mremap
  MAN_F21C8A2B969A6E31:
  - request_key
  MAN_F22AF2753D3EF507:
  - fspick
  MAN_F239ABCA41109C09:
  - readlinkat
  MAN_F2B410276719C5DD:
  - mq_open
  MAN_F2F62EBCDA82729C:
  - tkill
  MAN_F2F62EBCDA82729C--f2f62ebcda82:
  - tgkill
  MAN_F33BEC5B79C322F4:
  - recvmsg
  MAN_F33BEC5B79C322F4--f33bec5b79c3:
  - recvfrom
  MAN_F350D4F80E8650CB:
  - openat
  MAN_F35208C92774E887:
  - unlinkat
  MAN_F36403F294AF1A0B:
  - fsopen
  MAN_F3795B652E18D108:
  - set_mempolicy
  MAN_F3A4D21CCA9032B1:
  - ppoll
  MAN_F3AE80946B3A4936:
  - ppoll
  MAN_F3D996C7350329FC:
  - fchownat
  MAN_F3D996C7350329FC--f3d996c73503:
  - fchown
  MAN_F3E8CCCFECEE96C3:
  - reboot
  MAN_F419926A4FC0EE50:
  - sched_setscheduler
  MAN_F419926A4FC0EE50--f419926a4fc0:
  - sched_getscheduler
  MAN_F41AB10FF34633A3:
  - fspick
  MAN_F458E07FA7150299:
  - fsmount
  MAN_F4721319ED57B1F1:
  - utimensat
  MAN_F49214850C6EC4F5:
  - unlinkat
  MAN_F4932B8D711D713C:
  - pkey_mprotect
  MAN_F4932B8D711D713C--f4932b8d711d:
  - mprotect
  MAN_F54A38164475BA9B:
  - migrate_pages
  MAN_F556B5D121DA3A9F:
  - mbind
  MAN_F58C7E6A7D589B53:
  - fallocate
  MAN_F5BC4836CD9E73F2:
  - move_mount
  MAN_F5E80593B76ED05F:
  - rt_sigtimedwait
  MAN_F60DBFEDFB3F5EDB:
  - mlock2
  MAN_F630CB686BBBFC09:
  - munmap
  MAN_F630CB686BBBFC09--f630cb686bbb:
  - mmap
  MAN_F635310FCEFBE474:
  - fsconfig
  MAN_F637DBB67E32D6EB:
  - getsockname
  MAN_F642D589D83821BF:
  - statx
  MAN_F66662B26012AD7D:
  - faccessat2
  MAN_F66662B26012AD7D--f66662b26012:
  - faccessat
  MAN_F6725ACD1FA99F07:
  - statx
  MAN_F67A66FC38FEB053:
  - unlinkat
  MAN_F67F70C6CC37B637:
  - init_module
  MAN_F67F70C6CC37B637--f67f70c6cc37:
  - finit_module
  MAN_F696D40CB02AF56B:
  - swapon
  MAN_F69BB7D3FEA1E6C0:
  - lsetxattr
  MAN_F69F6987AD4215C0:
  - clock_settime
  MAN_F69FBCA0F4DD28C3:
  - add_key
  MAN_F6B8A3EAB6906025:
  - copy_file_range
  MAN_F6CB9D32040E99BA:
  - chroot
  MAN_F6CC937051236B8B:
  - setrlimit
  MAN_F6CC937051236B8B--f6cc93705123:
  - getrlimit
  MAN_F6D0725D21560A32:
  - fcntl
  MAN_F6DF482A3E9DD764:
  - execve
  MAN_F6E614AB08B3CD3E:
  - fchownat
  MAN_F6FF77CC7A102363:
  - sethostname
  MAN_F721C542DC63BD62:
  - madvise
  MAN_F725D76DED4B72E1:
  - landlock_add_rule
  MAN_F759FA01CCD924D3:
  - renameat2
  MAN_F78F49354EA2C4DD:
  - unshare
  MAN_F7A0EA90AF901E6B:
  - clone3
  MAN_F7A0EA90AF901E6B--f7a0ea90af90:
  - clone
  MAN_F7B3D28D1D7E3798:
  - sched_setattr
  MAN_F7B3D28D1D7E3798--f7b3d28d1d7e:
  - sched_getattr
  MAN_F8323B367F0166E0:
  - openat
  MAN_F839FD72E465E97B:
  - connect
  MAN_F83B0A4E5E26AC60:
  - shmctl
  MAN_F843131CCA96612C:
  - shmget
  MAN_F84F01B63ABC178D:
  - reboot
  MAN_F8602CA6388E2480:
  - process_madvise
  MAN_F87099158C84F948:
  - mincore
  MAN_F8728AC49092DB4E:
  - listmount
  MAN_F88CAC488E125E7E:
  - add_key
  MAN_F8B1F23FB65B6777:
  - pkey_free
  MAN_F8B1F23FB65B6777--f8b1f23fb65b:
  - pkey_alloc
  MAN_F8BEDB972F9EFC81:
  - connect
  MAN_F8CBF99945AD8863:
  - sigaltstack
  MAN_F8D4CD991E75520E:
  - perf_event_open
  MAN_F90518591C595B36:
  - semtimedop
  MAN_F90518591C595B36--f90518591c59:
  - semop
  MAN_F90EC9931B98DCBF:
  - msgsnd
  MAN_F90EC9931B98DCBF--f90ec9931b98:
  - msgrcv
  MAN_F950D39156CA90DD:
  - copy_file_range
  MAN_F995353DC7284138:
  - fsync
  MAN_F995353DC7284138--f995353dc728:
  - fdatasync
  MAN_FA0245FC8CA41633:
  - process_vm_writev
  MAN_FA0245FC8CA41633--fa0245fc8ca4:
  - process_vm_readv
  MAN_FA1DE79F217BEAB5:
  - mincore
  MAN_FA2FFED6AEA5058B:
  - faccessat2
  MAN_FA2FFED6AEA5058B--fa2ffed6aea5:
  - faccessat
  MAN_FA5253C2E58AB81B:
  - listen
  MAN_FA5A8CD06B8D499C:
  - fspick
  MAN_FABB3EE353CAB564:
  - readlinkat
  MAN_FAF27F6BDAA7436F:
  - fanotify_mark
  MAN_FB0572E736316463:
  - setpriority
  MAN_FB0572E736316463--fb0572e73631:
  - getpriority
  MAN_FB0A6B453C2E3A58:
  - sendfile
  MAN_FB16EA9B1F946269:
  - io_getevents
  MAN_FB2AAE15BE87AA16:
  - close_range
  MAN_FB64C1EFF713C2DF:
  - copy_file_range
  MAN_FB7C10EB67834424:
  - munmap
  MAN_FB7C10EB67834424--fb7c10eb6783:
  - mmap
  MAN_FB991CA668E0D904:
  - prlimit64
  MAN_FBA6C02764B1D697:
  - clone3
  MAN_FBB235142BCAC411:
  - clone3
  MAN_FBC8A59AEBFE9691:
  - mknodat
  MAN_FBD57CA95B5D3FC4:
  - madvise
  MAN_FBEFADE147C502AF:
  - pwritev
  MAN_FBFD397D4E9E3926:
  - capset
  MAN_FBFD397D4E9E3926--fbfd397d4e9e:
  - capget
  MAN_FC5C3EC55A0B7777:
  - flock
  MAN_FC5FA989550135DA:
  - add_key
  MAN_FC692F54195D28BB:
  - sendto
  MAN_FC692F54195D28BB--fc692f54195d:
  - sendmsg
  MAN_FCC7BBE7021EDB39:
  - timerfd_gettime
  MAN_FCDB282A3F163957:
  - mknodat
  MAN_FCE5926029B8D7A0:
  - request_key
  MAN_FCF73BE35CA648BA:
  - statfs
  MAN_FD1C66A20F3D8232:
  - munmap
  MAN_FD1C66A20F3D8232--fd1c66a20f3d:
  - mmap
  MAN_FD320818C991D990:
  - bind
  MAN_FD364C9DA3606DD0:
  - clone3
  MAN_FD364C9DA3606DD0--fd364c9da360:
  - clone
  MAN_FD4FB17C743C353C:
  - getrusage
  MAN_FD5BF4CD3984BECF:
  - setgroups
  MAN_FD83C3A37800C7FA:
  - fsmount
  MAN_FD88DE1E43B594DC:
  - sched_setscheduler
  MAN_FD9A6B75BB36A1EC:
  - utimensat
  MAN_FDC0817D43BF0BD8:
  - unshare
  MAN_FDD174E970AC7930:
  - copy_file_range
  MAN_FDDB2B5934441468:
  - mq_open
  MAN_FE11B37FAD24331A:
  - fchown
  MAN_FE482B8C9DC914AF:
  - open_by_handle_at
  MAN_FE482B8C9DC914AF--fe482b8c9dc9:
  - name_to_handle_at
  MAN_FEA2767E6D25968F:
  - readlinkat
  MAN_FEF731D4F49A2C00:
  - shmctl
  MAN_FF210C718F7A1685:
  - prlimit64
  MAN_FF5F239810FD7704:
  - getsockname
  MAN_FF7AC002AD46509D:
  - sendto
  MAN_FF7AC002AD46509D--ff7ac002ad46:
  - sendmsg
  MAN_FFEB999FCEC8AAA4:
  - splice
  MAN_FFF96CB16310BF3A:
  - renameat2
static:
- check_id: STARRY_CHROOT_PATH
  rule_refs:
  - MAN_F6CB9D32040E99BA
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/ctl.rs
  patterns:
  - label: user pathname is loaded and resolved
    regex: 'pub fn sys_chroot\(path: \*const c_char\)[\s\S]*?vm_load_(?:path_)?string\(path\)\?[\s\S]*?fs\.resolve\(path\)\?'
    matched: true
    line: 121
  - label: non directories are rejected
    regex: if loc\.node_type\(\) != NodeType::Directory \{[\s\S]*?return Err\(AxError::NotADirectory\);
    matched: true
    line: 128
  - label: valid directory becomes the new filesystem context
    regex: \*fs = FsContext::new\(loc\);[\s\S]*?Ok\(0\)
    matched: true
    line: 131
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_CLOSE_BAD_FD_ERRNO
  rule_refs:
  - LTP_09B39E9C9254ECB2
  result: pass
  path: components/axerrno/src/lib.rs
  patterns:
  - label: BadFileDescriptor maps to EBADF
    regex: BadFileDescriptor => EBADF
    matched: true
    line: 224
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_CLOSE_FD_TABLE
  rule_refs:
  - LTP_09B39E9C9254ECB2
  - MAN_23E25F7C4136339F
  result: fail
  path: os/StarryOS/kernel/src/file/mod.rs
  patterns:
  - label: close removes the descriptor from the current fd table
    regex: 'pub fn close_file_like\(fd: c_int\)[\s\S]*?FD_TABLE\.write\(\)\.remove\(fd as usize\)'
    matched: false
    line: null
  - label: a removed descriptor succeeds and a missing descriptor is EBADF
    regex: 'pub fn close_file_like\(fd: c_int\)[\s\S]*?return Ok\(\(\)\);[\s\S]*?Err\(AxError::BadFileDescriptor\)'
    matched: true
    line: 337
  reason: one or more required patterns did not match
  finding_ids:
  - finding-close-ltp-09b39e9c9254ecb2-07800f218f34
  - finding-close-man-23e25f7c4136339f-07800f218f34
- check_id: STARRY_CLOSE_RANGE_SWEEP
  rule_refs:
  - LTP_76BFF56F735A0074
  - LTP_F4DE81D703447628
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/fd_ops.rs
  patterns:
  - label: the sweep is capped at the current maximum descriptor
    regex: pub fn sys_close_range\([\s\S]*?for fd in first\.\.=last\.min\(max_index as (?:i32|u32)\)
    matched: true
    line: 541
  - label: missing descriptors are skipped and completion returns zero
    regex: for fd in first\.\.=last\.min\(max_index as (?:i32|u32)\)[\s\S]*?if let Some\(f\) = fd_table\.remove\(fd
      as _\)[\s\S]*?Ok\(0\)
    matched: true
    line: 568
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS
  rule_refs:
  - LTP_425E5A3502541DE8
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/fd_ops.rs
  patterns:
  - label: first and last use unsigned 32-bit syscall semantics
    regex: 'pub fn sys_close_range\(first: u32, last: u32, flags: u32\)'
    matched: true
    line: 541
  - label: the maximum unsigned range is accepted and capped to open descriptors
    regex: pub fn sys_close_range\([\s\S]*?for fd in first\.\.=last\.min\(max_index as u32\)[\s\S]*?Ok\(0\)
    matched: true
    line: 541
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_CLOSE_RANGE_VALIDATION
  rule_refs:
  - LTP_31D9D767D6888DDA
  - LTP_CBF4B6C8A1458A28
  - LTP_F1DC44813DCA6A05
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/fd_ops.rs
  patterns:
  - label: reversed ranges are invalid
    regex: pub fn sys_close_range\([\s\S]*?if (?:first < 0 \|\| )?last < first \{[\s\S]*?return Err\(AxError::InvalidInput\);
    matched: true
    line: 541
  - label: unknown close_range flags are invalid
    regex: pub fn sys_close_range\([\s\S]*?CloseRangeFlags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?
    matched: true
    line: 541
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_CLOSE_SYSCALL
  rule_refs:
  - LTP_09B39E9C9254ECB2
  - MAN_494CD34A8C11734B
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/fd_ops.rs
  patterns:
  - label: sys_close calls close_file_like and propagates errors
    regex: 'pub fn sys_close\(fd: c_int\)[\s\S]*?close_file_like\(fd\)\?;'
    matched: true
    line: 527
  - label: successful close returns zero
    regex: 'pub fn sys_close\(fd: c_int\)[\s\S]*?close_file_like\(fd\)\?;[\s\S]*?Ok\(0\)'
    matched: true
    line: 527
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_CONNECT_ADDRESS_VALIDATION
  rule_refs:
  - MAN_392816F25BD330A2
  - MAN_524B615D8F9A7E12
  result: pass
  path: os/StarryOS/kernel/src/syscall/net/addr.rs
  patterns:
  - label: family reads validate the minimum length and use checked user memory access
    regex: fn read_family\([\s\S]*?size_of::<__kernel_sa_family_t>\(\) > addrlen as usize[\s\S]*?Err\(AxError::InvalidInput\)[\s\S]*?addr\.cast::<__kernel_sa_family_t>\(\)\.get_as_ref\(\)\?
    matched: true
    line: 83
  - label: unsupported top-level address families return EAFNOSUPPORT
    regex: impl SocketAddrExt for SocketAddrEx[\s\S]*?fn read_from_user\([\s\S]*?_ => Err\(AxError::from\(LinuxError::EAFNOSUPPORT\)\)
    matched: true
    line: 320
  - label: short IPv4 addresses return InvalidInput
    regex: impl SocketAddrExt for SocketAddrV4[\s\S]*?if addrlen < size_of::<sockaddr_in>\(\) as socklen_t
      \{[\s\S]*?Err\(AxError::InvalidInput\)
    matched: true
    line: 152
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_CONNECT_ENTRY
  rule_refs:
  - MAN_CDD044CBEEED1A80
  result: pass
  path: os/StarryOS/kernel/src/syscall/net/socket.rs
  patterns:
  - label: connect validates the fd before reading and normalizing the address
    regex: pub fn sys_connect\([\s\S]*?Socket::from_fd\(fd\)\?;[\s\S]*?SocketAddrEx::read_from_user\(addr,
      addrlen\)\?;
    matched: true
    line: 173
  - label: parsed addresses are passed to the socket and errors propagate except nonblocking progress
    regex: pub fn sys_connect\([\s\S]*?socket\.connect\(addr\)\.map_err\([\s\S]*?AxError::WouldBlock[\s\S]*?AxError::InProgress[\s\S]*?\?;[\s\S]*?Ok\(0\)
    matched: true
    line: 173
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_COPY_FILE_RANGE_CORE
  rule_refs:
  - MAN_BC425C37C792DDEE
  - MAN_D405972253EA086F
  - MAN_DBD043A36C2E4926
  - MAN_FDD174E970AC7930
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/io.rs
  patterns:
  - label: nonzero flags are invalid
    regex: pub fn sys_copy_file_range\([\s\S]*?if flags != 0 \{[\s\S]*?Err\(AxError::InvalidInput\)
    matched: true
    line: 773
  - label: fd conversion preserves EBADF and EISDIR while rejecting other non-files
    regex: pub fn sys_copy_file_range\([\s\S]*?let remap = \|e\| match e \{[\s\S]*?AxError::BadFileDescriptor
      \| AxError::IsADirectory => e,[\s\S]*?_ => AxError::InvalidInput[\s\S]*?File::from_fd\(fd_in\)\.map_err\(remap\)\?;[\s\S]*?File::from_fd\(fd_out\)\.map_err\(remap\)\?;
    matched: true
    line: 773
  - label: directories and other non-regular nodes receive the required errors
    regex: meta_in\.node_type == NodeType::Directory \|\| meta_out\.node_type == NodeType::Directory[\s\S]*?Err\(AxError::IsADirectory\)[\s\S]*?meta_in\.node_type
      != NodeType::RegularFile \|\| meta_out\.node_type != NodeType::RegularFile[\s\S]*?Err\(AxError::InvalidInput\)
    matched: true
    line: 810
  - label: append-mode output is rejected as EBADF
    regex: file_out\.inner\(\)\.access\(FileFlags::APPEND\)\.is_ok\(\)[\s\S]*?Err\(AxError::BadFileDescriptor\)
    matched: true
    line: 818
  - label: overlapping ranges in one inode are rejected as EINVAL
    regex: meta_in\.device == meta_out\.device && meta_in\.inode == meta_out\.inode[\s\S]*?if in_end >=
      pos_out && pos_in <= out_end \{[\s\S]*?Err\(AxError::InvalidInput\)
    matched: true
    line: 834
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
- check_id: STARRY_DUP2_DUP3_BEHAVIOR
  rule_refs:
  - LTP_098AFE0E8E10B0EF
  - LTP_1726C16756E9651C
  - LTP_37C625BD7D7C5F1D
  - LTP_3A7B17AF231D4158
  - LTP_4F02ACC6E2F6B094
  - LTP_75D52C5E9C93B6D7
  - LTP_9B3646398697EA64
  - LTP_9F560A103CB6F910
  - LTP_B7F51635806E7E59
  - LTP_BDA36F61423EEB3E
  - LTP_D296A517F138A0C0
  - LTP_EE8E695CF61D6D8A
  - MAN_794294DBD03CA974
  - MAN_9BC94E6BD25C05E1
  - MAN_E99D067CF243EEE8
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/fd_ops.rs
  patterns:
  - label: dup2 same-fd validates the descriptor and otherwise delegates to dup3
    regex: 'pub fn sys_dup2\(old_fd: c_int, new_fd: c_int\)[\s\S]*?if old_fd == new_fd \{[\s\S]*?get_file_like\(new_fd\)\?;[\s\S]*?return
      Ok\(new_fd as _\);[\s\S]*?sys_dup3\(old_fd, new_fd, 0\)'
    matched: true
    line: 618
  - label: dup3 rejects unknown flags and equal descriptors
    regex: pub fn sys_dup3\([\s\S]*?Dup3Flags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?;[\s\S]*?if
      old_fd == new_fd \{[\s\S]*?Err\(AxError::InvalidInput\)
    matched: true
    line: 633
  - label: dup3 validates the old fd, replaces the target, and returns it
    regex: pub fn sys_dup3\([\s\S]*?\.get\(old_fd as _\)[\s\S]*?\.ok_or\(AxError::BadFileDescriptor\)\?;[\s\S]*?fd_table\.remove\(new_fd
      as _\)[\s\S]*?\.add_at\(new_fd as _, f\)[\s\S]*?Ok\(new_fd as _\)
    matched: true
    line: 633
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_DUP_BEHAVIOR
  rule_refs:
  - LTP_511185D6DE2A63A0
  - LTP_84DBE108A850E845
  - LTP_A774FC10727E8ED2
  - LTP_ED2BA909DF79625A
  - MAN_794294DBD03CA974--794294dbd03c
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/fd_ops.rs
  patterns:
  - label: dup_fd looks up the old descriptor and returns a newly allocated descriptor
    regex: 'fn dup_fd\(old_fd: c_int, cloexec: bool\)[\s\S]*?get_file_like\(old_fd\)\?;[\s\S]*?add_file_like\(f,
      cloexec\)\?;[\s\S]*?Ok\(new_fd as _\)'
    matched: true
    line: 586
  - label: sys_dup requests a non-CLOEXEC duplicate
    regex: 'pub fn sys_dup\(old_fd: c_int\)[\s\S]*?dup_fd\(old_fd, false\)'
    matched: true
    line: 612
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_EPOLL_CREATE1_FLAGS
  rule_refs:
  - LTP_5D8D2B3BEDA79604
  - MAN_6B7EED8E43FDD1BA
  result: pass
  path: os/StarryOS/kernel/src/syscall/io_mpx/epoll.rs
  patterns:
  - label: unknown create flags are rejected as invalid input
    regex: 'pub fn sys_epoll_create1\(flags: u32\)[\s\S]*?EpollCreateFlags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?'
    matched: true
    line: 104
  - label: a valid request creates and installs an epoll descriptor
    regex: 'pub fn sys_epoll_create1\(flags: u32\)[\s\S]*?Epoll::new\(\)[\s\S]*?\.add_to_fd_table\(flags\.contains\(EpollCreateFlags::CLOEXEC\)\)'
    matched: true
    line: 104
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_EPOLL_CTL_ENTRY
  rule_refs:
  - LTP_6FFB17DB762F3167
  - LTP_83709E56D6285F71
  - MAN_DADCFA23F461FBBF
  result: pass
  path: os/StarryOS/kernel/src/syscall/io_mpx/epoll.rs
  patterns:
  - label: the epoll descriptor is resolved before the operation
    regex: pub fn sys_epoll_ctl\([\s\S]*?let epoll = Epoll::from_fd\(epfd\)\?;
    matched: true
    line: 121
  - label: adding the epoll descriptor to itself is invalid
    regex: pub fn sys_epoll_ctl\([\s\S]*?if epfd == fd \{[\s\S]*?return Err\(AxError::InvalidInput\);
    matched: true
    line: 121
  - label: only ADD MOD and DEL operations are accepted
    regex: match op \{[\s\S]*?EPOLL_CTL_ADD =>[\s\S]*?EPOLL_CTL_MOD =>[\s\S]*?EPOLL_CTL_DEL =>[\s\S]*?_
      => return Err\(AxError::InvalidInput\)
    matched: true
    line: 149
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_EPOLL_CTL_INTEREST
  rule_refs:
  - LTP_4953FAD330ADE150
  result: fail
  path: os/StarryOS/kernel/src/file/epoll.rs
  patterns:
  - label: monitored descriptors are resolved through the fd table
    regex: 'fn new\(fd: i32\)[\s\S]*?let file = get_file_like\(fd\)\?;'
    matched: true
    line: 135
  - label: duplicate registrations return AlreadyExists
    regex: pub fn add\([\s\S]*?guard\.contains_key\(&key\)[\s\S]*?return Err\(AxError::AlreadyExists\);
    matched: false
    line: null
  - label: modifying a missing interest returns NotFound
    regex: pub fn modify\([\s\S]*?guard\.get_mut\(&key\)\.ok_or\(AxError::NotFound\)\?
    matched: true
    line: 599
  - label: deleting a missing interest returns NotFound
    regex: pub fn delete\([\s\S]*?\.remove\(&key\)[\s\S]*?\.ok_or\(AxError::NotFound\)\?
    matched: false
    line: null
  reason: one or more required patterns did not match
  finding_ids:
  - finding-epoll-ctl-ltp-4953fad330ade150-07800f218f34
- check_id: STARRY_EPOLL_FACCESS_ERRNO
  rule_refs:
  - LTP_4953FAD330ADE150
  - LTP_4C1F446C9C520B36
  - LTP_5D8D2B3BEDA79604
  - LTP_6FFB17DB762F3167
  - LTP_83709E56D6285F71
  - LTP_ACF7A30AF3B10973
  result: pass
  path: components/axerrno/src/lib.rs
  patterns:
  - label: invalid input maps to EINVAL
    regex: InvalidInput \| InvalidData => EINVAL
    matched: true
    line: 235
  - label: bad descriptors map to EBADF
    regex: BadFileDescriptor => EBADF
    matched: true
    line: 224
  - label: bad user addresses map to EFAULT
    regex: BadAddress \| BadState => EFAULT
    matched: true
    line: 223
  - label: missing interests map to ENOENT
    regex: NotFound => ENOENT
    matched: true
    line: 249
  - label: non-directory descriptors map to ENOTDIR
    regex: NotADirectory => ENOTDIR
    matched: true
    line: 243
  - label: duplicate interests map to EEXIST
    regex: AlreadyExists => EEXIST
    matched: true
    line: 221
  - label: nested filesystem-style loops map to ELOOP
    regex: FilesystemLoop => ELOOP
    matched: true
    line: 230
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_EPOLL_FD_LOOKUP
  rule_refs:
  - LTP_6FFB17DB762F3167
  - MAN_E32B6349055FCEF9
  result: pass
  path: os/StarryOS/kernel/src/file/mod.rs
  patterns:
  - label: absent descriptors return BadFileDescriptor
    regex: 'pub fn get_file_like\(fd: c_int\)[\s\S]*?\.ok_or\(AxError::BadFileDescriptor\)'
    matched: true
    line: 304
  - label: a descriptor of the wrong concrete type returns InvalidInput
    regex: 'fn from_fd\(fd: c_int\)[\s\S]*?get_file_like\(fd\)\?[\s\S]*?\.downcast_arc\(\)[\s\S]*?\.map_err\(\|_\|
      AxError::InvalidInput\)'
    matched: true
    line: 266
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_EPOLL_NESTED_LOOP
  rule_refs:
  - MAN_CDD195853C6DFE14
  result: pass
  path: os/StarryOS/kernel/src/file/epoll_topology.rs
  patterns:
  - label: nested topology scan rejects cycles
    regex: prepare_nested_link\([\s\S]*?scan_epoll_topology\(target,[\s\S]*?Some\(source\)\)\?[\s\S]*?downstream\.reached_target[\s\S]*?AxError::FilesystemLoop
    matched: true
    line: 48
  - label: nested topology scan enforces the maximum depth
    regex: upstream\.max_depth \+ 1 \+ downstream\.max_depth > MAX_NESTED_EPOLL_EDGES[\s\S]*?AxError::FilesystemLoop
    matched: true
    line: 61
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ERRNO_TRANSLATION
  rule_refs:
  - LTP_09B39E9C9254ECB2
  - LTP_51E295101A9F4411
  - LTP_791DEA825D66980B
  - LTP_FEACDC300C3E1DD7
  result: pass
  path: components/axerrno/src/lib.rs
  patterns:
  - label: BadFileDescriptor maps to EBADF
    regex: BadFileDescriptor => EBADF
    matched: true
    line: 224
  - label: InvalidInput maps to EINVAL
    regex: InvalidInput \| InvalidData => EINVAL
    matched: true
    line: 235
  - label: PermissionDenied maps to EACCES
    regex: PermissionDenied => EACCES
    matched: true
    line: 253
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_EXECVEAT_FACCESSAT_RESOLVE
  rule_refs:
  - LTP_4C1F446C9C520B36
  - LTP_ACF7A30AF3B10973
  result: pass
  path: os/StarryOS/kernel/src/file/fs.rs
  patterns:
  - label: empty paths require AT_EMPTY_PATH and resolve the supplied descriptor
    regex: Some\(""\) \| None =>[\s\S]*?flags & AT_EMPTY_PATH == 0[\s\S]*?get_file_like\(dirfd\)\?
    matched: true
    line: 62
  - label: absolute paths ignore dirfd while relative paths resolve through it
    regex: Some\(path\) =>[\s\S]*?if path\.starts_with\('/'\) \{[\s\S]*?AT_FDCWD[\s\S]*?with_fs\(dirfd,
    matched: true
    line: 80
  - label: relative non-directory descriptors return NotADirectory
    regex: 'impl FileLike for Directory[\s\S]*?fn from_fd\(fd: c_int\)[\s\S]*?get_file_like\(fd\)\?[\s\S]*?AxError::NotADirectory'
    matched: true
    line: 313
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_EXECVEAT_VALIDATION
  rule_refs:
  - LTP_ACF7A30AF3B10973
  result: pass
  path: os/StarryOS/kernel/src/syscall/task/execve.rs
  patterns:
  - label: unknown execveat flags are invalid
    regex: pub fn sys_execveat\([\s\S]*?if flags & !\(AT_EMPTY_PATH \| AT_SYMLINK_NOFOLLOW\) != 0 \{[\s\S]*?Err\(AxError::InvalidInput\)
    matched: true
    line: 45
  - label: the pathname is loaded and resolved through resolve_at
    regex: pub fn sys_execveat\([\s\S]*?vm_load_string\(path\)\?;[\s\S]*?resolve_at\(dirfd, Some\(path\.as_str\(\)\),
      flags\)\?
    matched: true
    line: 45
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FACCESSAT2_VALIDATION
  rule_refs:
  - MAN_147EECDC5DAB119D
  - MAN_A58EA189B1C9E326
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/stat.rs
  patterns:
  - label: only Linux access mode and faccessat2 flag bits are accepted
    regex: const FACCESSAT2_VALID_FLAGS:[\s\S]*?const FACCESSAT2_VALID_MODE:[\s\S]*?mode & !FACCESSAT2_VALID_MODE
      != 0 \|\| flags & !FACCESSAT2_VALID_FLAGS != 0[\s\S]*?Err\(AxError::InvalidInput\)
    matched: true
    line: 150
  - label: the optional user path is copied before resolve_at
    regex: pub fn sys_faccessat2\([\s\S]*?path\.nullable\(\)\.map\(vm_load_path_string\)\.transpose\(\)\?;[\s\S]*?resolve_at\(dirfd,
      path\.as_deref\(\), flags\)\?
    matched: true
    line: 146
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FCHDIR_CORE
  rule_refs:
  - LTP_17B7A9460939622A
  - LTP_CCC36F43E9463D3E
  - MAN_5B2667DFDCB4EB31
  - MAN_E116073D3FDB5C1F
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/ctl.rs
  patterns:
  - label: fchdir resolves the descriptor through with_fs
    regex: 'pub fn sys_fchdir\(dirfd: i32\)[\s\S]*?with_fs\(dirfd,[\s\S]*?current_dir\(\)\.clone\(\)'
    matched: true
    line: 99
  - label: fchdir propagates cwd update errors
    regex: 'pub fn sys_fchdir\(dirfd: i32\)[\s\S]*?set_current_dir\(entry\)\?;'
    matched: true
    line: 99
  - label: successful fchdir returns zero
    regex: 'pub fn sys_fchdir\(dirfd: i32\)[\s\S]*?set_current_dir\(entry\)\?;[\s\S]*?Ok\(0\)'
    matched: true
    line: 99
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FCHDIR_ERRNO_TRANSLATION
  rule_refs:
  - LTP_CCC36F43E9463D3E
  result: pass
  path: components/axerrno/src/lib.rs
  patterns:
  - label: BadFileDescriptor maps to EBADF
    regex: BadFileDescriptor\s*=>\s*EBADF
    matched: true
    line: 224
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FCHDIR_FD_VALIDATION
  rule_refs:
  - LTP_CCC36F43E9463D3E
  - MAN_5B2667DFDCB4EB31
  result: pass
  path: os/StarryOS/kernel/src/file/fs.rs
  patterns:
  - label: non-AT_FDCWD uses Directory::from_fd with error propagation
    regex: pub fn with_fs<[\s\S]*?if dirfd == AT_FDCWD[\s\S]*?Directory::from_fd\(dirfd\)\?
    matched: true
    line: 28
  - label: Directory::from_fd propagates fd lookup failure
    regex: 'impl FileLike for Directory[\s\S]*?fn from_fd\(fd: c_int\)[\s\S]*?get_file_like\(fd\)\?'
    matched: true
    line: 313
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FCHMODAT_FLAG_VALIDATION
  rule_refs:
  - MAN_9A17C8A141B47D41
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/ctl.rs
  patterns:
  - label: supported fchmodat flags are explicitly bounded
    regex: 'const FCHMODAT_VALID_FLAGS: u32 = AT_EMPTY_PATH \| AT_SYMLINK_NOFOLLOW;'
    matched: true
    line: 620
  - label: unknown fchmodat flags return InvalidInput
    regex: if flags & !FCHMODAT_VALID_FLAGS != 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}
    matched: true
    line: 621
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FD_TABLE_LOOKUP_ALLOCATION
  rule_refs:
  - LTP_511185D6DE2A63A0
  - LTP_84DBE108A850E845
  - LTP_A774FC10727E8ED2
  - LTP_ED2BA909DF79625A
  result: fail
  path: os/StarryOS/kernel/src/file/mod.rs
  patterns:
  - label: missing descriptors produce BadFileDescriptor
    regex: 'pub fn get_file_like\(fd: c_int\)[\s\S]*?FD_TABLE[\s\S]*?\.get\(fd as usize\)[\s\S]*?\.ok_or\(AxError::BadFileDescriptor\)'
    matched: false
    line: null
  - label: allocation enforces the current nofile limit as TooManyOpenFiles
    regex: pub fn add_file_like\([\s\S]*?RLIMIT_NOFILE[\s\S]*?if table\.count\(\) as u64 >= max_nofile
      \{[\s\S]*?Err\(AxError::TooManyOpenFiles\)
    matched: true
    line: 325
  - label: successful allocation returns the new descriptor
    regex: pub fn add_file_like\([\s\S]*?Ok\(table\.add\(fd\)\.map_err\(\|_\| AxError::TooManyOpenFiles\)\?
      as c_int\)
    matched: true
    line: 325
  reason: one or more required patterns did not match
  finding_ids:
  - finding-dup-ltp-511185d6de2a63a0-07800f218f34
  - finding-dup-ltp-84dbe108a850e845-07800f218f34
  - finding-dup-ltp-a774fc10727e8ed2-07800f218f34
  - finding-dup-ltp-ed2ba909df79625a-07800f218f34
- check_id: STARRY_FINAL_ERRNO_TRANSLATION
  rule_refs:
  - LTP_10B3572DBFA6742B
  - LTP_9FD87A3F7688FEF1
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
- check_id: STARRY_FINAL_SYSINFO_COPYOUT
  rule_refs:
  - LTP_A367723236ADA8B4
  result: pass
  path: os/StarryOS/kernel/src/syscall/sys.rs
  patterns:
  - label: sysinfo populates core fields and copies the structure to userspace
    regex: pub fn sys_sysinfo\([\s\S]*?kinfo\.uptime[\s\S]*?kinfo\.totalram[\s\S]*?kinfo\.freeram[\s\S]*?kinfo\.procs[\s\S]*?info\.vm_write\(kinfo\)\?;\s*Ok\(0\)
    matched: true
    line: 719
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
  finding_ids: []
- check_id: STARRY_FINAL_TIMER_DELETE
  rule_refs:
  - LTP_10B3572DBFA6742B
  - LTP_9B36D27A4A2994D0
  - MAN_95930C2D369C878D
  - MAN_AF1D093225F75E82
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
  result: pass
  path: os/StarryOS/kernel/src/syscall/signal.rs
  patterns:
  - label: tkill rejects zero and negative tids with InvalidInput
    regex: pub fn sys_tkill\([\s\S]*?if tid <= 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}
    matched: true
    line: 214
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINAL_UMOUNT_PRIVILEGE
  rule_refs:
  - LTP_287CF10D893735AB
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/mount.rs
  patterns:
  - label: umount rejects callers without CAP_SYS_ADMIN
    regex: pub fn sys_umount2\([\s\S]*?has_cap_sys_admin\(\)[\s\S]*?return Err\(AxError::OperationNotPermitted\);
    matched: true
    line: 302
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINAL_UNAME_COPYOUT
  rule_refs:
  - LTP_5516B8A938B9C3A5
  result: pass
  path: os/StarryOS/kernel/src/syscall/sys.rs
  patterns:
  - label: uname builds utsname and writes it through VmMutPtr
    regex: pub fn sys_uname\([\s\S]*?build_utsname\(&ns\)[\s\S]*?name\.vm_write\(uts\)\?;\s*Ok\(0\)
    matched: true
    line: 661
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINAL_UNSHARE_FILES
  rule_refs:
  - LTP_40A45C5E82D7F4A1
  result: fail
  path: os/StarryOS/kernel/src/syscall/task/namespace.rs
  patterns:
  - label: CLONE_FILES is accepted as a supported unshare flag
    regex: 'const SUPPORTED_NS_FLAGS: u32 =[\s\S]*?CLONE_FILES'
    matched: true
    line: 24
  - label: CLONE_FILES clones and rebinds the descriptor table
    regex: if flags & CLONE_FILES != 0 \{[\s\S]*?FD_TABLE\.read\(\)\.clone\(\)[\s\S]*?FD_TABLE\.scope_mut\(scope\)
    matched: false
    line: null
  reason: one or more required patterns did not match
  finding_ids:
  - finding-unshare-ltp-40a45c5e82d7f4a1-07800f218f34
- check_id: STARRY_FINAL_UNSHARE_FLAG_VALIDATION
  rule_refs:
  - MAN_B4DD5B60F33FC5E3
  result: pass
  path: os/StarryOS/kernel/src/syscall/task/namespace.rs
  patterns:
  - label: unsupported unshare flags return InvalidInput
    regex: pub fn sys_unshare\([\s\S]*?flags & !SUPPORTED_NS_FLAGS != 0[\s\S]*?return Err\(AxError::InvalidInput\);
    matched: true
    line: 109
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINAL_UNSHARE_NEWNS_PRIVILEGE
  rule_refs:
  - LTP_82A8802A27A3D2BF
  result: pass
  path: os/StarryOS/kernel/src/syscall/task/namespace.rs
  patterns:
  - label: mount namespace unshare rejects callers without CAP_SYS_ADMIN
    regex: flags & CLONE_NEWNS != 0[\s\S]*?![\s\S]*?has_cap_sys_admin\(\)[\s\S]*?return Err\(AxError::OperationNotPermitted\);
    matched: true
    line: 64
  reason: all required patterns matched
  finding_ids: []
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
    line: 385
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINAL_WAITPID_INT_MIN
  rule_refs:
  - LTP_03AF14160F8B59A0
  - LTP_1691F6F9712C5546
  result: pass
  path: os/StarryOS/kernel/src/syscall/task/wait.rs
  patterns:
  - label: INT_MIN returns ESRCH before process-group negation
    regex: pub fn sys_waitpid\([\s\S]*?if pid == i32::MIN \{\s*return Err\(AxError::from\(LinuxError::ESRCH\)\);\s*\}
    matched: true
    line: 234
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINIT_MODULE_FLAG_VALIDATION
  rule_refs:
  - MAN_2421026C912D8F9E--2421026c912d
  result: pass
  path: os/StarryOS/kernel/src/syscall/kmod.rs
  patterns:
  - label: finit_module names and inspects its flags argument
    regex: 'pub fn sys_finit_module\(module_fd: i32, param_ptr: \*const u8, flags: u32\)'
    matched: true
    line: 52
  - label: unsupported nonzero flags return InvalidInput
    regex: pub fn sys_finit_module\([\s\S]*?if flags != 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}
    matched: true
    line: 52
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_MAN_CLOCK_GETRES_VALIDATION
  rule_refs:
  - MAN_6D665164162723C5--6d6651641627
  - MAN_DA93975DA79D34AD--da93975da79d
  result: pass
  path: os/StarryOS/kernel/src/syscall/time.rs
  patterns:
  - label: unsupported clock IDs return EINVAL
    regex: pub fn sys_clock_getres[\s\S]*?_ => return Err\(AxError::InvalidInput\)
    matched: true
    line: 62
  - label: a non-null result uses checked user memory
    regex: pub fn sys_clock_getres[\s\S]*?res\.nullable\(\)[\s\S]*?res\.vm_write\(timespec::from_time_value\(resolution\)\)\?
    matched: true
    line: 62
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_MAN_CLOCK_GETTIME_VALIDATION
  rule_refs:
  - MAN_A67DCE77030808A6
  - MAN_D84D77F1C6E463F4
  result: pass
  path: os/StarryOS/kernel/src/syscall/time.rs
  patterns:
  - label: unsupported clock IDs return EINVAL
    regex: pub fn sys_clock_gettime[\s\S]*?_ => \{[\s\S]*?return Err\(AxError::InvalidInput\)
    matched: true
    line: 18
  - label: the timestamp is written through checked user memory
    regex: pub fn sys_clock_gettime[\s\S]*?ts\.vm_write\(timespec::from_time_value\(now\)\)\?
    matched: true
    line: 18
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_MAN_EVENTFD2_VALIDATION
  rule_refs:
  - MAN_A5F4BA2371332A4E
  - MAN_BE929AB9651E5E66
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/event.rs
  patterns:
  - label: unsupported flags return EINVAL
    regex: pub fn sys_eventfd2[\s\S]*?EventFdFlags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?
    matched: true
    line: 26
  - label: the new object is installed and its fd returned
    regex: pub fn sys_eventfd2[\s\S]*?add_file_like\(event_fd[\s\S]*?\.map\(\|fd\| fd as _\)\?[\s\S]*?Ok\(fd\)
    matched: true
    line: 26
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_MAN_GETRANDOM_ARGUMENTS
  rule_refs:
  - MAN_39C5F1849EB3A736
  - MAN_CEC45E0E1446E3DF
  result: pass
  path: os/StarryOS/kernel/src/syscall/sys.rs
  patterns:
  - label: unknown and incompatible flags return EINVAL
    regex: pub fn sys_getrandom[\s\S]*?GetRandomFlags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?[\s\S]*?INSECURE[\s\S]*?RANDOM[\s\S]*?AxError::InvalidInput
    matched: true
    line: 850
  - label: output uses checked user memory
    regex: pub fn sys_getrandom[\s\S]*?vm_write_slice\(buf, &kbuf\)\?
    matched: true
    line: 850
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_MAN_INOTIFY_ADD_WATCH_INPUTS
  rule_refs:
  - MAN_1EFA395D2832F95E
  - MAN_EFBA9CA2760DA6B8
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/inotify.rs
  patterns:
  - label: path loading uses checked user memory
    regex: pub fn sys_inotify_add_watch[\s\S]*?vm_load_path_string\(path\)\?
    matched: true
    line: 25
  - label: fd lookup precedes type validation
    regex: pub fn sys_inotify_add_watch[\s\S]*?get_file_like\(fd\)\?[\s\S]*?downcast_arc::<Inotify>\(\)
    matched: true
    line: 25
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_MAN_INOTIFY_INIT1_VALIDATION
  rule_refs:
  - MAN_330C0628475E2900
  - MAN_C467D6702AB64674
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/inotify.rs
  patterns:
  - label: only CLOEXEC and NONBLOCK are accepted
    regex: pub fn sys_inotify_init1[\s\S]*?valid_flags = IN_CLOEXEC \| IN_NONBLOCK[\s\S]*?flags & !valid_flags
      != 0[\s\S]*?AxError::InvalidInput
    matched: true
    line: 12
  - label: the inotify object is installed and its fd returned
    regex: pub fn sys_inotify_init1[\s\S]*?add_file_like\(inotify as _, flags & IN_CLOEXEC != 0\)\.map\(\|fd\|
      fd as _\)
    matched: true
    line: 12
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_MAN_INOTIFY_RM_WATCH_ID
  rule_refs:
  - MAN_EA69373DAD6B5B01
  result: pass
  path: os/StarryOS/kernel/src/file/inotify.rs
  patterns:
  - label: a missing watch descriptor returns EINVAL
    regex: pub fn rm_watch[\s\S]*?watches\.remove\(&wd\)\.is_none\(\)[\s\S]*?AxError::InvalidInput
    matched: true
    line: 90
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_MAN_INOTIFY_RM_WATCH_INPUTS
  rule_refs:
  - MAN_C04F44BFF720877B
  - MAN_EA69373DAD6B5B01
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/inotify.rs
  patterns:
  - label: fd lookup and inotify type validation are explicit
    regex: pub fn sys_inotify_rm_watch[\s\S]*?get_file_like\(fd\)\?[\s\S]*?downcast_arc::<Inotify>\(\)[\s\S]*?AxError::InvalidInput
    matched: true
    line: 40
  - label: watch removal errors are propagated
    regex: pub fn sys_inotify_rm_watch[\s\S]*?inotify\.rm_watch\(wd\)\.map\(\|\(\)\| 0\)
    matched: true
    line: 40
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_MAN_LISTEN_ENTRY
  rule_refs:
  - MAN_6038BC183A1CE6BF
  - MAN_7C3C0347FD37CEB9
  - MAN_AE7C62637F29A4C9
  result: pass
  path: os/StarryOS/kernel/src/syscall/net/socket.rs
  patterns:
  - label: listen resolves a Socket from the fd
    regex: pub fn sys_listen[\s\S]*?Socket::from_fd\(fd\)\?\.listen\(backlog as usize\)\?
    matched: true
    line: 192
  - label: a successful listen returns zero
    regex: pub fn sys_listen[\s\S]*?Ok\(0\)
    matched: true
    line: 192
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_MAN_MEMFD_CREATE_VALIDATION
  rule_refs:
  - MAN_4C50AA2793AB7713
  - MAN_67ECA3FB50D80BAF
  - MAN_6FA8F2D41D1B7062
  - MAN_9E0C30E4205FB415
  - MAN_DD8A18DB0BF6E8A9
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/memfd.rs
  patterns:
  - label: unknown and hugepage flags return EINVAL
    regex: pub fn sys_memfd_create[\s\S]*?flags & !valid_flags != 0 \|\| flags & MFD_HUGETLB != 0[\s\S]*?AxError::InvalidInput
    matched: true
    line: 45
  - label: name loading uses checked user memory
    regex: 'let name_str: String = vm_load_string\(name\)\?'
    matched: true
    line: 55
  - label: names longer than 249 bytes return EINVAL
    regex: 'const MEMFD_NAME_MAX: usize = 249;[\s\S]*?name_str\.len\(\) > MEMFD_NAME_MAX[\s\S]*?AxError::InvalidInput'
    matched: true
    line: 43
  - label: the memfd is installed and its fd returned
    regex: pub fn sys_memfd_create[\s\S]*?add_file_like\(memfd, cloexec\)\.map\(\|fd\| fd as _\)
    matched: true
    line: 45
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_MAN_PIPE2_VALIDATION
  rule_refs:
  - MAN_1115E878B4F50CF3
  - MAN_DD6D48EB9B80CB6B
  - MAN_EDB775C51FCEA404
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/pipe.rs
  patterns:
  - label: unsupported flags return EINVAL
    regex: pub fn sys_pipe2[\s\S]*?PipeFlags::from_bits\(flags\)[\s\S]*?AxError::InvalidInput
    matched: true
    line: 21
  - label: output uses checked user memory with fd rollback
    regex: if let Err\(err\) = fds\.vm_write\(\[read_fd, write_fd\]\)[\s\S]*?close_file_like\(read_fd\)[\s\S]*?close_file_like\(write_fd\)[\s\S]*?return
      Err\(err\.into\(\)\)
    matched: true
    line: 38
  - label: valid creation returns zero
    regex: pub fn sys_pipe2[\s\S]*?Ok\(0\)
    matched: true
    line: 21
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_MAN_REBOOT_VALIDATION
  rule_refs:
  - MAN_03E8B237E962C1D2
  - MAN_F84F01B63ABC178D
  result: pass
  path: os/StarryOS/kernel/src/syscall/sys.rs
  patterns:
  - label: reboot requires CAP_SYS_BOOT
    regex: pub fn sys_reboot[\s\S]*?has_cap_sys_boot\(\)[\s\S]*?LinuxError::EPERM
    matched: true
    line: 128
  - label: bad magic values return EINVAL
    regex: magic != LINUX_REBOOT_MAGIC1[\s\S]*?LINUX_REBOOT_MAGIC2C[\s\S]*?LinuxError::EINVAL
    matched: true
    line: 133
  - label: unknown commands return EINVAL
    regex: match cmd \{[\s\S]*?_ => Err\(AxError::from\(LinuxError::EINVAL\)\)
    matched: true
    line: 145
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_MAN_SECCOMP_OPERATION_FLAGS
  rule_refs:
  - MAN_B9EE0F176B92F526
  result: fail
  path: os/StarryOS/kernel/src/syscall/sys.rs
  patterns:
  - label: strict mode requires zero flags
    regex: SECCOMP_SET_MODE_STRICT => \{[\s\S]*?if flags != 0[\s\S]*?AxError::InvalidInput
    matched: true
    line: 939
  - label: action availability queries require zero flags
    regex: SECCOMP_GET_ACTION_AVAIL => \{[\s\S]*?if flags != 0[\s\S]*?AxError::InvalidInput
    matched: false
    line: null
  reason: one or more required patterns did not match
  finding_ids:
  - finding-seccomp-man-b9ee0f176b92f526-07800f218f34
- check_id: STARRY_MAN_SECCOMP_VALIDATION
  rule_refs:
  - MAN_02D976F1ED01493F
  - MAN_20A10178D28B400B
  - MAN_73E054548B324267
  - MAN_8609DB2EE85AF88E
  - MAN_BE74B0D21973DAEC
  result: pass
  path: os/StarryOS/kernel/src/syscall/sys.rs
  patterns:
  - label: installation requires no_new_privs or CAP_SYS_ADMIN
    regex: fn check_seccomp_install_permission[\s\S]*?no_new_privs\(\)[\s\S]*?has_cap_sys_admin\(\)[\s\S]*?AxError::OperationNotPermitted
    matched: true
    line: 876
  - label: null and empty filter programs are rejected
    regex: fn read_seccomp_filter[\s\S]*?args\.is_null\(\)[\s\S]*?AxError::BadAddress[\s\S]*?prog\.len
      == 0 \|\| prog\.filter\.is_null\(\)[\s\S]*?AxError::InvalidInput
    matched: true
    line: 886
  - label: unavailable actions return EOPNOTSUPP
    regex: fn seccomp_action_available[\s\S]*?_ => Err\(AxError::OperationNotSupported\)
    matched: true
    line: 902
  - label: flags and operations are bounded and success returns zero
    regex: pub fn sys_seccomp[\s\S]*?flags & !SECCOMP_ALLOWED_FLAGS != 0[\s\S]*?match op[\s\S]*?_ => return
      Err\(AxError::InvalidInput\)[\s\S]*?Ok\(0\)
    matched: true
    line: 933
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_MAN_SETDOMAINNAME_ARGUMENTS
  rule_refs:
  - MAN_027D17C587997F75
  - MAN_083368964C7623C0
  - MAN_968D07C7039689E5
  result: pass
  path: os/StarryOS/kernel/src/syscall/sys.rs
  patterns:
  - label: overlong names return EINVAL
    regex: pub fn sys_setdomainname[\s\S]*?if len > 64[\s\S]*?AxError::InvalidInput
    matched: true
    line: 695
  - label: the name is read through checked user memory
    regex: pub fn sys_setdomainname[\s\S]*?vm_read_slice\(name\.cast::<u8>\(\), &mut buf\)\?
    matched: true
    line: 695
  - label: a valid update returns zero
    regex: pub fn sys_setdomainname[\s\S]*?domainname = domainname;[\s\S]*?Ok\(0\)
    matched: true
    line: 695
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_MAN_SETGROUPS_VALIDATION
  rule_refs:
  - MAN_0F2C1ABA8AF5C15E
  - MAN_8D160F5D77EC235B
  - MAN_FD5BF4CD3984BECF
  result: pass
  path: os/StarryOS/kernel/src/syscall/sys.rs
  patterns:
  - label: CAP_SETGID is required
    regex: pub fn sys_setgroups[\s\S]*?!old\.has_cap_setgid\(\)[\s\S]*?AxError::OperationNotPermitted
    matched: true
    line: 627
  - label: namespace setgroups denial is enforced
    regex: thread\.setgroups_deny\(\)[\s\S]*?AxError::OperationNotPermitted
    matched: true
    line: 637
  - label: oversized group vectors are rejected
    regex: 'const NGROUPS_MAX: usize = 65536;[\s\S]*?if size > NGROUPS_MAX[\s\S]*?AxError::InvalidInput'
    matched: true
    line: 625
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_MAN_SETHOSTNAME_ARGUMENTS
  rule_refs:
  - MAN_6998D4E70F807B13
  - MAN_9E12AA9A59F1BBE9
  - MAN_DA06B43ED3D9DBBC
  result: pass
  path: os/StarryOS/kernel/src/syscall/sys.rs
  patterns:
  - label: overlong names return EINVAL
    regex: pub fn sys_sethostname[\s\S]*?if len > 64[\s\S]*?AxError::InvalidInput
    matched: true
    line: 675
  - label: the name is read through checked user memory
    regex: pub fn sys_sethostname[\s\S]*?vm_read_slice\(name\.cast::<u8>\(\), &mut buf\)\?
    matched: true
    line: 675
  - label: a valid update returns zero
    regex: pub fn sys_sethostname[\s\S]*?nodename = nodename;[\s\S]*?Ok\(0\)
    matched: true
    line: 675
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_MAN_SHUTDOWN_VALIDATION
  rule_refs:
  - MAN_5B4118BF4C21F770
  - MAN_5F5865EF1A8D5904
  - MAN_8812ADE8E360DB8F
  - MAN_CAA0FFEFF7C64A82
  result: pass
  path: os/StarryOS/kernel/src/syscall/net/socket.rs
  patterns:
  - label: shutdown resolves a Socket from the fd
    regex: pub fn sys_shutdown[\s\S]*?Socket::from_fd\(fd\)\?
    matched: true
    line: 239
  - label: only SHUT_RD SHUT_WR and SHUT_RDWR are accepted
    regex: let how = match how \{[\s\S]*?SHUT_RD[\s\S]*?SHUT_WR[\s\S]*?SHUT_RDWR[\s\S]*?_ => return Err\(AxError::InvalidInput\)
    matched: true
    line: 243
  - label: a valid shutdown returns zero
    regex: socket\.shutdown\(how\)\.map\(\|_\| 0\)
    matched: true
    line: 249
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_MAN_SOCKETPAIR_VALIDATION
  rule_refs:
  - MAN_43BBCE48C452BDDD
  - MAN_9452D425539B8023
  - MAN_B121E5340A1BEFEE
  result: pass
  path: os/StarryOS/kernel/src/syscall/net/socket.rs
  patterns:
  - label: unsupported families return EAFNOSUPPORT
    regex: pub fn sys_socketpair[\s\S]*?if domain != AF_UNIX[\s\S]*?LinuxError::EAFNOSUPPORT
    matched: true
    line: 252
  - label: fd output uses checked user memory
    regex: pub fn sys_socketpair[\s\S]*?\*fds\.get_as_mut\(\)\? = \[
    matched: true
    line: 252
  - label: successful pair creation returns zero
    regex: pub fn sys_socketpair[\s\S]*?Ok\(0\)
    matched: true
    line: 252
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_MMAP_ACCESS
  rule_refs:
  - MAN_18C5488E8D09D6D2--18c5488e8d09
  result: fail
  path: os/StarryOS/kernel/src/syscall/mm/mmap.rs
  patterns:
  - label: non-regular file mappings are translated to EACCES
    regex: file_mmap\(\)\.map_err\(\|_\| AxError::PermissionDenied\)\?
    matched: false
    line: null
  - label: all file mappings require read access
    regex: if needs_file_mmap_checks[\s\S]*?!flags\.contains\(FileFlags::READ\)[\s\S]*?AxError::PermissionDenied
    matched: true
    line: 246
  - label: shared writable mappings require write access
    regex: MmapFlags::SHARED[\s\S]*?MmapProt::WRITE[\s\S]*?!flags\.contains\(FileFlags::WRITE\)[\s\S]*?AxError::PermissionDenied
    matched: true
    line: 150
  reason: one or more required patterns did not match
  finding_ids:
  - finding-mmap-man-18c5488e8d09d6d2-18c5488e8d09-07800f218f34
- check_id: STARRY_MMAP_ARGUMENTS
  rule_refs:
  - LTP_51E295101A9F4411
  - LTP_FEACDC300C3E1DD7
  - MAN_8DB0AB4E3B90CB50--8db0ab4e3b90
  - MAN_DE03A6A5B1731AF7--de03a6a5b173
  result: pass
  path: os/StarryOS/kernel/src/syscall/mm/mmap.rs
  patterns:
  - label: zero length is invalid input
    regex: pub fn sys_mmap\([\s\S]*?if length == 0 \{[\s\S]*?return Err\(AxError::InvalidInput\);
    matched: true
    line: 128
  - label: map type must be shared private or shared validate
    regex: let map_type = match flags & MmapFlags::TYPE\.bits\(\)[\s\S]*?_ => return Err\(AxError::InvalidInput\)
    matched: true
    line: 160
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_MMAP_FD
  rule_refs:
  - LTP_791DEA825D66980B
  - MAN_35AF4698AC57ED3F--35af4698ac57
  result: pass
  path: os/StarryOS/kernel/src/syscall/mm/mmap.rs
  patterns:
  - label: negative file descriptor is rejected as EBADF
    regex: if !anonymous && fd < 0 \{[\s\S]*?return Err\(AxError::BadFileDescriptor\);
    matched: true
    line: 170
  - label: non-anonymous mmap resolves the descriptor through get_file_like
    regex: let file = if anonymous \{[\s\S]*?None[\s\S]*?\} else \{[\s\S]*?Some\(get_file_like\(fd\)\?\)
    matched: true
    line: 203
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND2_CLOSE_FD_TABLE
  rule_refs:
  - LTP_2BDE60C0E64B4DC8
  - LTP_BF2428964ADD116F
  - LTP_E520E500AB3AE851
  result: fail
  path: os/StarryOS/kernel/src/file/mod.rs
  patterns:
  - label: close removes the descriptor independently of its file-like type
    regex: 'pub fn close_file_like\(fd: c_int\)[\s\S]*?FD_TABLE\.write\(\)\.remove\(fd as usize\)[\s\S]*?if
      let Some\(f\) = removed[\s\S]*?return Ok\(\(\)\);'
    matched: false
    line: null
  - label: only a missing descriptor is rejected
    regex: 'pub fn close_file_like\(fd: c_int\)[\s\S]*?Err\(AxError::BadFileDescriptor\)'
    matched: true
    line: 337
  reason: one or more required patterns did not match
  finding_ids:
  - finding-close-ltp-2bde60c0e64b4dc8-07800f218f34
  - finding-close-ltp-bf2428964add116f-07800f218f34
  - finding-close-ltp-e520e500ab3ae851-07800f218f34
- check_id: STARRY_ROUND2_CLOSE_SYSCALL
  rule_refs:
  - LTP_2BDE60C0E64B4DC8
  - LTP_BF2428964ADD116F
  - LTP_E520E500AB3AE851
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/fd_ops.rs
  patterns:
  - label: sys_close invokes the fd-table close helper and returns zero
    regex: 'pub fn sys_close\(fd: c_int\)[\s\S]*?close_file_like\(fd\)\?;[\s\S]*?Ok\(0\)'
    matched: true
    line: 527
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND2_ERRNO_TRANSLATION
  rule_refs:
  - LTP_098AFE0E8E10B0EF
  - LTP_31D9D767D6888DDA
  - LTP_37C625BD7D7C5F1D
  - LTP_4F02ACC6E2F6B094
  - LTP_75D52C5E9C93B6D7
  - LTP_9B3646398697EA64
  - LTP_9F560A103CB6F910
  - LTP_BDA36F61423EEB3E
  - LTP_CBF4B6C8A1458A28
  - LTP_D296A517F138A0C0
  - LTP_F1DC44813DCA6A05
  result: pass
  path: components/axerrno/src/lib.rs
  patterns:
  - label: invalid input maps to EINVAL
    regex: InvalidInput \| InvalidData => EINVAL
    matched: true
    line: 235
  - label: bad descriptors map to EBADF
    regex: BadFileDescriptor => EBADF
    matched: true
    line: 224
  - label: exhausted descriptor limits map to EMFILE
    regex: TooManyOpenFiles => EMFILE
    matched: true
    line: 258
  - label: bad user addresses map to EFAULT
    regex: BadAddress \| BadState => EFAULT
    matched: true
    line: 223
  - label: non-sockets map to ENOTSOCK
    regex: NotASocket => ENOTSOCK
    matched: true
    line: 244
  - label: directories map to EISDIR
    regex: IsADirectory => EISDIR
    matched: true
    line: 237
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND3_ERRNO_TRANSLATION
  rule_refs:
  - LTP_53E3454ED6EFD842
  - LTP_729222947741DFD6
  - LTP_88D300A8FB407324
  - LTP_8C1C2578972FCA1D
  - LTP_9461AA782926BAB4
  - LTP_F8FD511858BB650D
  - LTP_FC1E41C3414E7F21
  result: pass
  path: components/axerrno/src/lib.rs
  patterns:
  - label: bad user addresses map to EFAULT
    regex: BadAddress \| BadState => EFAULT
    matched: true
    line: 223
  - label: bad descriptors map to EBADF
    regex: BadFileDescriptor => EBADF
    matched: true
    line: 224
  - label: invalid input maps to EINVAL
    regex: InvalidInput \| InvalidData => EINVAL
    matched: true
    line: 235
  - label: missing processes map to ESRCH
    regex: NoSuchProcess => ESRCH
    matched: true
    line: 242
  - label: permission failure maps to EPERM
    regex: OperationNotPermitted => EPERM
    matched: true
    line: 250
  - label: short output buffers map to ERANGE
    regex: OutOfRange => ERANGE
    matched: true
    line: 252
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND3_FSTATFS_ERRORS
  rule_refs:
  - MAN_48B52042FE3DEA4C--48b52042fe3d
  - MAN_5378890AE3F832EE--5378890ae3f8
  - MAN_8153E21BD727F6A0
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/stat.rs
  patterns:
  - label: fstatfs obtains a real file from the descriptor
    regex: 'pub fn sys_fstatfs\(fd: i32, buf: \*mut statfs\)[\s\S]*?File::from_fd\(fd\)\?'
    matched: true
    line: 244
  - label: fstatfs writes via checked VM access
    regex: buf\.vm_write\(statfs\([\s\S]*?\)\?\)\?;
    matched: true
    line: 234
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND3_FSTAT_CORE
  rule_refs:
  - MAN_37A8B25C745F91BB--37a8b25c745f
  - MAN_AA8C115068BD5D76--aa8c115068bd
  - MAN_DFDB86CEA63B78D3--dfdb86cea63b
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/stat.rs
  patterns:
  - label: fstat uses the descriptor form of fstatat
    regex: 'pub fn sys_fstat\(fd: i32, statbuf: \*mut stat\)[\s\S]*?sys_fstatat\(fd, core::ptr::null\(\),
      statbuf, AT_EMPTY_PATH\)'
    matched: true
    line: 43
  - label: fstatat resolves the supplied descriptor and path
    regex: pub fn sys_fstatat\([\s\S]*?let loc = resolve_at\(dirfd, path\.as_deref\(\), flags\)\?;
    matched: true
    line: 57
  - label: stat output is copied through checked VM access
    regex: statbuf\.vm_write\(loc\.stat\(\)\?\.into\(\)\)\?;
    matched: true
    line: 75
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND3_GETCWD
  rule_refs:
  - LTP_53E3454ED6EFD842
  - LTP_729222947741DFD6
  - LTP_FC1E41C3414E7F21
  - MAN_0D9E79AEB44B7510
  - MAN_45A2B6F5ADF14C3F
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/ctl.rs
  patterns:
  - label: signed size conversion rejects impossible sizes
    regex: 'pub fn sys_getcwd\([\s\S]*?let size: usize = size\.try_into\(\)\.map_err\(\|_\| AxError::BadAddress\)\?;'
    matched: true
    line: 431
  - label: the C string length includes its terminator
    regex: let cwd = cwd\.as_bytes_with_nul\(\);
    matched: true
    line: 441
  - label: short buffers return OutOfRange
    regex: if cwd\.len\(\) <= size \{[\s\S]*?vm_write_slice\(buf, cwd\)\?;[\s\S]*?\} else \{\s*Err\(AxError::OutOfRange\)
    matched: true
    line: 443
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND3_GETPRIORITY_SELECTOR
  rule_refs:
  - LTP_88D300A8FB407324
  - MAN_B1A8365C419E3164--b1a8365c419e
  result: pass
  path: os/StarryOS/kernel/src/syscall/task/schedule.rs
  patterns:
  - label: unknown which values return InvalidInput
    regex: pub fn sys_getpriority\([\s\S]*?match which \{[\s\S]*?_ => Err\(AxError::InvalidInput\),\s*\}
    matched: true
    line: 237
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND3_GETRLIMIT_CORE
  rule_refs:
  - LTP_2554AC2E46FC6A15
  - LTP_26555A26680524AD
  - LTP_3741A721C9C463D0
  - LTP_3B1458E6E26CBB53
  - LTP_652CE911B47794E0
  - LTP_7DFAC48A8971CFE3
  - LTP_8988E5015778894A
  - LTP_914935DA5C379DA1
  - LTP_91ED7E85761CE00F
  - LTP_9305FA6D8B835652
  - LTP_A0547B601C515355
  - LTP_B058D6B9CBBB459D
  - LTP_BD5C209F4C6EE910
  - LTP_E6C69C9F4AB565BC
  - LTP_EA953D5E5C4B2B1F
  - LTP_FADBA4ADECCFBA4E
  - LTP_FB0ABF26A21EAE3C
  result: pass
  path: os/StarryOS/kernel/src/syscall/resources.rs
  patterns:
  - label: resource numbers are bounded by RLIM_NLIMITS
    regex: if resource >= RLIM_NLIMITS \{\s*return Err\(AxError::InvalidInput\);\s*\}
    matched: true
    line: 23
  - label: all valid resource slots are read from the process limit array
    regex: let limit = &proc_data\.rlim\.read\(\)\[resource\];
    matched: true
    line: 28
  - label: the result is copied through checked VM access
    regex: 'old_limit\.vm_write\(rlimit64 \{\s*rlim_cur: limit\.current,\s*rlim_max: limit\.max,\s*\}\)\?;'
    matched: true
    line: 29
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND3_GETRLIMIT_DISPATCH
  rule_refs:
  - LTP_2554AC2E46FC6A15
  - LTP_26555A26680524AD
  - LTP_3741A721C9C463D0
  - LTP_3B1458E6E26CBB53
  - LTP_652CE911B47794E0
  - LTP_7DFAC48A8971CFE3
  - LTP_8988E5015778894A
  - LTP_914935DA5C379DA1
  - LTP_91ED7E85761CE00F
  - LTP_9305FA6D8B835652
  - LTP_A0547B601C515355
  - LTP_B058D6B9CBBB459D
  - LTP_BD5C209F4C6EE910
  - LTP_E6C69C9F4AB565BC
  - LTP_EA953D5E5C4B2B1F
  - LTP_FADBA4ADECCFBA4E
  - LTP_FB0ABF26A21EAE3C
  result: pass
  path: os/StarryOS/kernel/src/syscall/mod.rs
  patterns:
  - label: getrlimit routes current process and output pointer to prlimit64
    regex: Sysno::getrlimit => sys_prlimit64\(0, uctx\.arg0\(\) as _, core::ptr::null\(\), uctx\.arg1\(\)
      as _\)
    matched: true
    line: 650
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
  result: fail
  path: os/StarryOS/kernel/src/syscall/kmod.rs
  patterns:
  - label: init_module checks CAP_SYS_MODULE
    regex: pub fn sys_init_module\([\s\S]*?if !current\(\)\.as_thread\(\)\.cred\(\)\.has_cap_sys_module\(\)
    matched: false
    line: null
  - label: permission failure precedes user-buffer access
    regex: pub fn sys_init_module\([\s\S]*?has_cap_sys_module\(\)[\s\S]*?return Err\(AxError::OperationNotPermitted\);[\s\S]*?VmBytes::new
    matched: false
    line: null
  reason: one or more required patterns did not match
  finding_ids: []
- check_id: STARRY_ROUND3_JOB_ID_LOOKUP
  rule_refs:
  - LTP_8C1C2578972FCA1D
  - LTP_9461AA782926BAB4
  - LTP_F8FD511858BB650D
  - MAN_045719AC8992819E--045719ac8992
  - MAN_81F4F1C3AD4F3217
  result: pass
  path: os/StarryOS/kernel/src/syscall/task/job.rs
  patterns:
  - label: getsid resolves the requested process
    regex: 'pub fn sys_getsid\(pid: Pid\)[\s\S]*?get_process\(pid\)\?\.group\(\)\.session\(\)\.sid\(\)'
    matched: true
    line: 10
  - label: getpgid resolves the requested process
    regex: 'pub fn sys_getpgid\(pid: Pid\)[\s\S]*?get_process\(pid\)\?\.group\(\)\.pgid\(\)'
    matched: true
    line: 30
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND3_PROCESS_LOOKUP
  rule_refs:
  - LTP_8C1C2578972FCA1D
  - LTP_9461AA782926BAB4
  - LTP_F8FD511858BB650D
  - MAN_045719AC8992819E--045719ac8992
  - MAN_81F4F1C3AD4F3217
  result: pass
  path: os/StarryOS/kernel/src/task/ops.rs
  patterns:
  - label: pid zero selects the current process
    regex: 'pub fn get_process\(pid: Pid\)[\s\S]*?if pid == 0 \{\s*return Ok\(current\(\)\.as_thread\(\)\.proc_data\.proc\.clone\(\)\);'
    matched: true
    line: 255
  - label: missing live and zombie processes return NoSuchProcess
    regex: get_zombie_process\(pid\)\.ok_or\(AxError::NoSuchProcess\)
    matched: true
    line: 262
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND4_ERRNO_TRANSLATION
  rule_refs:
  - LTP_0087F445CEB63414
  - LTP_026CB4A1CA7CDC6B
  - LTP_08F05BA6ED1CEE6A
  - LTP_1AACAC53BAF23BA9
  - LTP_1BB76939FF2A40B5
  - LTP_26AE3C69D80D35F8
  - LTP_3743BC827FB4F981
  - LTP_D0800876342DE939
  - LTP_D2E2A5F40B2313E5
  - LTP_EA90C626D9AA6C08
  result: pass
  path: components/axerrno/src/lib.rs
  patterns:
  - label: bad addresses translate to EFAULT
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
  - label: no memory translates to ENOMEM
    regex: NoMemory => ENOMEM
    matched: true
    line: 239
  - label: unsupported operations translate to EOPNOTSUPP
    regex: OperationNotSupported => EOPNOTSUPP
    matched: true
    line: 251
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND4_MLOCK2_FLAGS
  rule_refs:
  - MAN_362BD9184BA2B5C7
  result: pass
  path: os/StarryOS/kernel/src/syscall/mm/mmap.rs
  patterns:
  - label: unknown flags return InvalidInput
    regex: pub fn sys_mlock2\([\s\S]*?if flags & !MLOCK_ONFAULT != 0 \{\s*return Err\(AxError::InvalidInput\);
    matched: true
    line: 1081
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND4_MSYNC_EXCLUSIVE_MODES
  rule_refs:
  - LTP_D2E2A5F40B2313E5
  result: pass
  path: os/StarryOS/kernel/src/syscall/mm/mmap.rs
  patterns:
  - label: MS_SYNC and MS_ASYNC together return InvalidInput
    regex: if flags & MS_SYNC != 0 && flags & MS_ASYNC != 0 \{\s*return Err\(AxError::InvalidInput\);
    matched: true
    line: 1035
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND4_MSYNC_UNKNOWN_FLAGS
  rule_refs:
  - LTP_EA90C626D9AA6C08
  result: pass
  path: os/StarryOS/kernel/src/syscall/mm/mmap.rs
  patterns:
  - label: unknown flag bits return InvalidInput
    regex: let valid_flags = MS_SYNC \| MS_ASYNC \| MS_INVALIDATE;\s*if flags & !valid_flags != 0 \{\s*return
      Err\(AxError::InvalidInput\);
    matched: true
    line: 1031
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND4_MUNMAP_ZERO_LENGTH
  rule_refs:
  - LTP_26AE3C69D80D35F8
  - MAN_8DB0AB4E3B90CB50
  result: pass
  path: os/StarryOS/kernel/src/syscall/mm/mmap.rs
  patterns:
  - label: zero length returns InvalidInput
    regex: pub fn sys_munmap\([\s\S]*?if length == 0 \{\s*return Err\(AxError::InvalidInput\);
    matched: true
    line: 592
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND4_OPENAT2_SIZE
  rule_refs:
  - LTP_026CB4A1CA7CDC6B
  - LTP_D0800876342DE939
  - MAN_25CD94348F7360E1
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/fd_ops.rs
  patterns:
  - label: undersized open_how returns InvalidInput
    regex: pub fn sys_openat2\([\s\S]*?let base_size = size_of::<OpenHow>\(\);\s*if size < base_size \{\s*return
      Err\(AxError::InvalidInput\);
    matched: true
    line: 428
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND4_PIDFD_GETFD_FLAGS
  rule_refs:
  - MAN_58936D050A8879DE
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/pidfd.rs
  patterns:
  - label: nonzero flags return InvalidInput first
    regex: pub fn sys_pidfd_getfd\([\s\S]*?if flags != 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}[\s\S]*?PidFd::from_fd
    matched: true
    line: 86
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND4_PIDFD_OPEN_INPUTS
  rule_refs:
  - LTP_1BB76939FF2A40B5
  - LTP_3743BC827FB4F981
  - MAN_0BA66331CB4B2091
  - MAN_DC37B979EC91203E
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/pidfd.rs
  patterns:
  - label: unknown flags return InvalidInput
    regex: let flags = PidFdFlags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?;
    matched: true
    line: 61
  - label: nonpositive pids return InvalidInput
    regex: if \(pid as i32\) <= 0 \{\s*return Err\(AxError::InvalidInput\);
    matched: true
    line: 64
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND4_PIDFD_SIGNAL_FLAGS
  rule_refs:
  - LTP_08F05BA6ED1CEE6A
  - MAN_6D77B363EA967C8F
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/pidfd.rs
  patterns:
  - label: unknown flags return InvalidInput
    regex: pub fn sys_pidfd_send_signal\([\s\S]*?PidFdSignalFlags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?;
    matched: true
    line: 123
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND4_READ_BAD_FD
  rule_refs:
  - LTP_0087F445CEB63414
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/io.rs
  patterns:
  - label: read propagates descriptor lookup errors
    regex: pub fn sys_read\([\s\S]*?get_file_like\(fd\)\?\.read
    matched: true
    line: 123
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND4_VECTOR_IO_FLAGS
  rule_refs:
  - LTP_1AACAC53BAF23BA9
  - MAN_B5E18528035F6F87
  - MAN_F12635B7646C0E9B
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/io.rs
  patterns:
  - label: nonzero RWF flags return OperationNotSupported
    regex: 'fn validate_rwf_flags\(flags: u32\)[\s\S]*?if flags != 0 \{\s*return Err\(AxError::OperationNotSupported\);'
    matched: true
    line: 505
  - label: both vector I/O paths validate flags before operating
    regex: pub fn sys_preadv2\([\s\S]*?validate_rwf_flags\(flags\)\?;[\s\S]*?pub fn sys_pwritev2\([\s\S]*?validate_rwf_flags\(flags\)\?;
    matched: true
    line: 512
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND5_ERRNO_TRANSLATION
  rule_refs:
  - LTP_39B1E5C574F2D3DC
  - LTP_4308D71D8BD6519D
  - LTP_44DC5382746D773D
  - LTP_585CC852338F38EE
  - LTP_7BC885B5878C95B6
  - LTP_971DB17D32C51561
  result: pass
  path: components/axerrno/src/lib.rs
  patterns:
  - label: bad addresses translate to EFAULT
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
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND5_SCHED_SETAFFINITY_EMPTY_MASK
  rule_refs:
  - LTP_585CC852338F38EE
  result: pass
  path: os/StarryOS/kernel/src/syscall/task/schedule.rs
  patterns:
  - label: empty mask returns invalid input
    regex: pub fn sys_sched_setaffinity\([\s\S]*?if cpu_mask\.is_empty\(\) \{\s*return Err\(AxError::InvalidInput\);
    matched: true
    line: 141
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND5_SCHED_YIELD
  rule_refs:
  - LTP_A9BC7EBC1784A722
  - MAN_254F60FBFDA7A2BB
  result: pass
  path: os/StarryOS/kernel/src/syscall/task/schedule.rs
  patterns:
  - label: sched_yield yields once and returns zero
    regex: pub fn sys_sched_yield\(\) -> AxResult<isize> \{\s*ax_task::yield_now\(\);\s*Ok\(0\)\s*\}
    matched: true
    line: 30
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND5_SENDFILE_IN_FD
  rule_refs:
  - LTP_39B1E5C574F2D3DC
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/io.rs
  patterns:
  - label: direct input descriptor uses File lookup
    regex: pub fn sys_sendfile\([\s\S]*?let _in_file = File::from_fd\(in_fd\)\?;
    matched: true
    line: 741
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND5_SENDFILE_OUT_FD
  rule_refs:
  - LTP_7BC885B5878C95B6
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/io.rs
  patterns:
  - label: output descriptor is looked up first
    regex: pub fn sys_sendfile\([\s\S]*?let out_file = get_file_like\(out_fd\)\?;
    matched: true
    line: 741
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND5_SENDMSG_MESSAGE_POINTER
  rule_refs:
  - MAN_AE68C41A115C80FC--ae68c41a115c
  result: pass
  path: os/StarryOS/kernel/src/syscall/net/io.rs
  patterns:
  - label: the message header uses checked user access
    regex: pub fn sys_sendmsg[\s\S]*?msg\.get_as_ref\(\)\?
    matched: true
    line: 137
  - label: control messages use checked user access
    regex: fn parse_send_cmsgs[\s\S]*?UserConstPtr::<cmsghdr>::from\(ptr\)\.get_as_ref\(\)\?
    matched: true
    line: 41
  - label: the I/O vector is validated before sending
    regex: pub fn sys_sendmsg[\s\S]*?IoVectorBuf::new\(msg\.msg_iov as \*const IoVec, msg\.msg_iovlen\)\?
    matched: true
    line: 137
  - label: a non-null destination address is decoded through checked access
    regex: fn send_impl[\s\S]*?SocketAddrEx::read_from_user\(addr, addrlen\)\?
    matched: true
    line: 73
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND5_SETPGID_NEGATIVE
  rule_refs:
  - LTP_4308D71D8BD6519D
  - MAN_44D6BD8077F837B5
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
- check_id: STARRY_ROUND5_SETPRIORITY_SELECTOR
  rule_refs:
  - LTP_44DC5382746D773D
  - MAN_B1A8365C419E3164
  result: pass
  path: os/StarryOS/kernel/src/syscall/task/schedule.rs
  patterns:
  - label: unknown which value is invalid input
    regex: pub fn sys_setpriority\([\s\S]*?match which \{[\s\S]*?_ => Err\(AxError::InvalidInput\),\s*\}
    matched: true
    line: 270
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND5_SOCKET_INVALID_TYPE
  rule_refs:
  - LTP_971DB17D32C51561
  result: fail
  path: os/StarryOS/kernel/src/syscall/net/socket.rs
  patterns:
  - label: unsupported type in a supported domain is invalid input
    regex: pub fn sys_socket\([\s\S]*?\(AF_INET \| AF_INET6, _\) \| \(AF_UNIX, _\) \| \(AF_NETLINK, _\)
      \| \(AF_VSOCK, _\) => \{[\s\S]*?return Err\(AxError::InvalidInput\);[\s\S]*?\n\}\n\npub fn sys_bind
    matched: false
    line: null
  reason: one or more required patterns did not match
  finding_ids:
  - finding-socket-ltp-971db17d32c51561-07800f218f34
- check_id: STARRY_ROUND5_SOCKET_PROTOCOL_ERRORS
  rule_refs:
  - LTP_6B29B31CE99466E6
  - LTP_A4A662687B98D33F
  - LTP_AF8D38878ED1A9DA
  - LTP_DD2E1A555B603C7B
  - LTP_E316C28E36E136DA
  - MAN_732160952277CD16
  - MAN_A1CD98CE32C423E4
  result: pass
  path: os/StarryOS/kernel/src/syscall/net/socket.rs
  patterns:
  - label: TCP sockets reject non-TCP protocols
    regex: \(AF_INET \| AF_INET6, SOCK_STREAM\) => \{[\s\S]*?proto != 0 && proto != IPPROTO_TCP as _[\s\S]*?LinuxError::EPROTONOSUPPORT
    matched: true
    line: 62
  - label: UDP sockets reject non-UDP protocols
    regex: \(AF_INET \| AF_INET6, SOCK_DGRAM\) => \{[\s\S]*?proto != 0 && proto != IPPROTO_UDP as _[\s\S]*?LinuxError::EPROTONOSUPPORT
    matched: true
    line: 68
  - label: raw IPv4 sockets reject unsupported protocols
    regex: \(AF_INET, SOCK_RAW\) => \{[\s\S]*?proto != IPPROTO_ICMP as u32[\s\S]*?LinuxError::EPROTONOSUPPORT
    matched: true
    line: 93
  - label: unknown domains return EAFNOSUPPORT
    regex: _ => \{\s*return Err\(AxError::from\(LinuxError::EAFNOSUPPORT\)\);\s*\}
    matched: true
    line: 106
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_SOCKET_FD_VALIDATION
  rule_refs:
  - MAN_5B4118BF4C21F770
  - MAN_5F5865EF1A8D5904
  - MAN_6038BC183A1CE6BF
  - MAN_AE7C62637F29A4C9
  - MAN_CDD044CBEEED1A80
  result: pass
  path: os/StarryOS/kernel/src/file/net.rs
  patterns:
  - label: Socket from_fd propagates fd lookup and maps type mismatch to NotASocket
    regex: 'fn from_fd\(fd: c_int\)[\s\S]*?get_file_like\(fd\)\?[\s\S]*?\.downcast_arc\(\)[\s\S]*?\.map_err\(\|_\|
      AxError::NotASocket\)'
    matched: true
    line: 391
  reason: all required patterns matched
  finding_ids: []
dynamic:
- test_id: STARRY_FINAL_FS_RUNTIME
  rule_refs:
  - LTP_04236FD5B061DEB9
  - LTP_21FCBFC328D1815A
  - LTP_38432B154B641410
  - LTP_43728156B00FF104
  - LTP_58C8C307B1FF2510
  - LTP_6F4B3A38B8BF4C7E
  - LTP_6F77CAA9FC4423BA
  - LTP_71DD72481EF5740E
  - LTP_86144BF50FB25D3A
  - LTP_B0433B78A1641F24
  - LTP_D254EE40E8B5957E
  - LTP_DCC88B2C458969EA
  - LTP_DDA854712C50CD6A
  result: not_run
  reason: test patch was not applied
  diagnostic_log: /tmp/syscallguard-check/check-20260723t030225z-60f534a3/logs/dynamic-starry-final-fs-runtime.log
  finding_ids: []
- test_id: STARRY_FINAL_WAIT_RUNTIME
  rule_refs:
  - LTP_2F3E34FD672DBF34
  - LTP_4494B70BBA693D42
  - LTP_614C018F61C078A0
  - LTP_7B0F966046AECA7E
  - LTP_9C2FB7732A0B90B6
  - LTP_A2934B80997B62C9
  - LTP_AD3A4B98FF201ABE
  - LTP_C13C4F63D58904BC
  - LTP_C24E55F06625D564
  - LTP_D1A18560E485E146
  - LTP_DA64FD04E43656E6
  - LTP_DF5B725563FDFB31
  - LTP_ECD986F27CF15E1E
  - LTP_FC8BA85373EA2D8F
  result: not_run
  reason: test patch was not applied
  diagnostic_log: /tmp/syscallguard-check/check-20260723t030225z-60f534a3/logs/dynamic-starry-final-wait-runtime.log
  finding_ids: []
counts:
  static_pass: 89
  static_fail: 10
  static_error: 0
  dynamic_pass: 0
  dynamic_fail: 0
  dynamic_skipped: 0
  dynamic_not_run: 2
  findings: 14
  blockers: 3
  new_findings: 14
  carried_findings: 0
  revalidated_findings: 0
  needs_revalidation: 0
blockers:
- kind: test_injection
  entity_ids:
  - STARRY_FINAL_FS_RUNTIME
  - STARRY_FINAL_WAIT_RUNTIME
  reason: git apply failed for dynamic test patch
  diagnostic_log: /tmp/syscallguard-check/check-20260723t030225z-60f534a3/logs/patch-starry-final-runtime-patch.log
- kind: test_injection
  entity_ids:
  - STARRY_FINAL_FS_RUNTIME
  reason: test patch was not applied
  diagnostic_log: /tmp/syscallguard-check/check-20260723t030225z-60f534a3/logs/dynamic-starry-final-fs-runtime.log
- kind: test_injection
  entity_ids:
  - STARRY_FINAL_WAIT_RUNTIME
  reason: test patch was not applied
  diagnostic_log: /tmp/syscallguard-check/check-20260723t030225z-60f534a3/logs/dynamic-starry-final-wait-runtime.log
finding_ids:
- finding-close-ltp-09b39e9c9254ecb2-07800f218f34
- finding-close-ltp-2bde60c0e64b4dc8-07800f218f34
- finding-close-ltp-bf2428964add116f-07800f218f34
- finding-close-ltp-e520e500ab3ae851-07800f218f34
- finding-close-man-23e25f7c4136339f-07800f218f34
- finding-dup-ltp-511185d6de2a63a0-07800f218f34
- finding-dup-ltp-84dbe108a850e845-07800f218f34
- finding-dup-ltp-a774fc10727e8ed2-07800f218f34
- finding-dup-ltp-ed2ba909df79625a-07800f218f34
- finding-epoll-ctl-ltp-4953fad330ade150-07800f218f34
- finding-mmap-man-18c5488e8d09d6d2-18c5488e8d09-07800f218f34
- finding-seccomp-man-b9ee0f176b92f526-07800f218f34
- finding-socket-ltp-971db17d32c51561-07800f218f34
- finding-unshare-ltp-40a45c5e82d7f4a1-07800f218f34
finding_versions:
  finding-close-ltp-09b39e9c9254ecb2-07800f218f34:
    id: finding-close-ltp-09b39e9c9254ecb2-07800f218f34
    generated_at_utc: '2026-07-23T03:02:33.663221Z'
    content_hash: sha256:fb605adb54592bb13bbd23bf5f909cc1ddec6cb5e9fd4cdba7c31af9631f20f9
  finding-close-man-23e25f7c4136339f-07800f218f34:
    id: finding-close-man-23e25f7c4136339f-07800f218f34
    generated_at_utc: '2026-07-23T03:02:33.663221Z'
    content_hash: sha256:c139f13ac9a04297799be0af2a0f9afc3e2dd6188297d0e26909a013032218a3
  finding-epoll-ctl-ltp-4953fad330ade150-07800f218f34:
    id: finding-epoll-ctl-ltp-4953fad330ade150-07800f218f34
    generated_at_utc: '2026-07-23T03:02:33.663221Z'
    content_hash: sha256:f886eb97fdc60abfd3aed5871696d2e22d896f43069c0de3ef9de3c7f7208e78
  finding-dup-ltp-511185d6de2a63a0-07800f218f34:
    id: finding-dup-ltp-511185d6de2a63a0-07800f218f34
    generated_at_utc: '2026-07-23T03:02:33.663221Z'
    content_hash: sha256:bb17318848c2510bb78bacf635c2455d8ff39d9c540090d6f6f5331a25c1f825
  finding-dup-ltp-84dbe108a850e845-07800f218f34:
    id: finding-dup-ltp-84dbe108a850e845-07800f218f34
    generated_at_utc: '2026-07-23T03:02:33.663221Z'
    content_hash: sha256:c01cffa613d4ba7d475e1c469aae20c6c6db21586642bf8a184ddb174452e2e9
  finding-dup-ltp-a774fc10727e8ed2-07800f218f34:
    id: finding-dup-ltp-a774fc10727e8ed2-07800f218f34
    generated_at_utc: '2026-07-23T03:02:33.663221Z'
    content_hash: sha256:33a1ec3dc733f5412b94b9da3272ddc6a2562b9b5b72c54322d5873baf439b22
  finding-dup-ltp-ed2ba909df79625a-07800f218f34:
    id: finding-dup-ltp-ed2ba909df79625a-07800f218f34
    generated_at_utc: '2026-07-23T03:02:33.663221Z'
    content_hash: sha256:dc8cc10017c6c46601a18ad5cd1b79d1adf9194936e383ecfe77dce79ddf415c
  finding-unshare-ltp-40a45c5e82d7f4a1-07800f218f34:
    id: finding-unshare-ltp-40a45c5e82d7f4a1-07800f218f34
    generated_at_utc: '2026-07-23T03:02:33.663221Z'
    content_hash: sha256:ffd23bb6c1e0eb5ca585d3245123ed1f23fab925d17a6e87eaa33341163c7e9f
  finding-seccomp-man-b9ee0f176b92f526-07800f218f34:
    id: finding-seccomp-man-b9ee0f176b92f526-07800f218f34
    generated_at_utc: '2026-07-23T03:02:33.663221Z'
    content_hash: sha256:4b1ca2dbccbb8e75385cfddb1339dc597384880fa9e092eabbc7301b318b4ca1
  finding-mmap-man-18c5488e8d09d6d2-18c5488e8d09-07800f218f34:
    id: finding-mmap-man-18c5488e8d09d6d2-18c5488e8d09-07800f218f34
    generated_at_utc: '2026-07-23T03:02:33.663221Z'
    content_hash: sha256:b609d022ab0c52ec2d1594b3ad519e796d235c0d41495550a5301f4b3b0b7b78
  finding-close-ltp-2bde60c0e64b4dc8-07800f218f34:
    id: finding-close-ltp-2bde60c0e64b4dc8-07800f218f34
    generated_at_utc: '2026-07-23T03:02:33.663221Z'
    content_hash: sha256:6db351da17ecc2ba5d7aeded579daa8e7cd4a322bb364e57d42d5a0be1db74fa
  finding-close-ltp-bf2428964add116f-07800f218f34:
    id: finding-close-ltp-bf2428964add116f-07800f218f34
    generated_at_utc: '2026-07-23T03:02:33.663221Z'
    content_hash: sha256:c65e487b3468057735c65e70591bdc3d867dc7367c9dbb428c357d5a0f63eec2
  finding-close-ltp-e520e500ab3ae851-07800f218f34:
    id: finding-close-ltp-e520e500ab3ae851-07800f218f34
    generated_at_utc: '2026-07-23T03:02:33.663221Z'
    content_hash: sha256:b57041b3eb192b1d57e36966037b16044ce34083852d820764f4972be758ff8b
  finding-socket-ltp-971db17d32c51561-07800f218f34:
    id: finding-socket-ltp-971db17d32c51561-07800f218f34
    generated_at_utc: '2026-07-23T03:02:33.663221Z'
    content_hash: sha256:4f4d788a73c7338f102cf3a0cd094162e91b82f0de7e8a62f6d350e28d18f339
new_finding_ids:
- finding-close-ltp-09b39e9c9254ecb2-07800f218f34
- finding-close-ltp-2bde60c0e64b4dc8-07800f218f34
- finding-close-ltp-bf2428964add116f-07800f218f34
- finding-close-ltp-e520e500ab3ae851-07800f218f34
- finding-close-man-23e25f7c4136339f-07800f218f34
- finding-dup-ltp-511185d6de2a63a0-07800f218f34
- finding-dup-ltp-84dbe108a850e845-07800f218f34
- finding-dup-ltp-a774fc10727e8ed2-07800f218f34
- finding-dup-ltp-ed2ba909df79625a-07800f218f34
- finding-epoll-ctl-ltp-4953fad330ade150-07800f218f34
- finding-mmap-man-18c5488e8d09d6d2-18c5488e8d09-07800f218f34
- finding-seccomp-man-b9ee0f176b92f526-07800f218f34
- finding-socket-ltp-971db17d32c51561-07800f218f34
- finding-unshare-ltp-40a45c5e82d7f4a1-07800f218f34
carried_finding_ids: []
revalidated_finding_ids: []
needs_revalidation_finding_ids: []
historical_regression_scope:
  rules:
  - LTP_04236FD5B061DEB9
  - LTP_21FCBFC328D1815A
  - LTP_287CF10D893735AB
  - LTP_2F3E34FD672DBF34
  - LTP_38432B154B641410
  - LTP_43728156B00FF104
  - LTP_4494B70BBA693D42
  - LTP_58C8C307B1FF2510
  - LTP_614C018F61C078A0
  - LTP_6B9F97B897EC5C32
  - LTP_6C14DE68E3C0CC24
  - LTP_6F4B3A38B8BF4C7E
  - LTP_6F77CAA9FC4423BA
  - LTP_71DD72481EF5740E
  - LTP_74BB3F96CBA52D02
  - LTP_7B0F966046AECA7E
  - LTP_82A8802A27A3D2BF
  - LTP_86144BF50FB25D3A
  - LTP_9C2FB7732A0B90B6
  - LTP_A2934B80997B62C9
  - LTP_AD3A4B98FF201ABE
  - LTP_B0433B78A1641F24
  - LTP_C13C4F63D58904BC
  - LTP_C24E55F06625D564
  - LTP_C8376BC347F94A98
  - LTP_D1A18560E485E146
  - LTP_D246498B20D9CB2C
  - LTP_D254EE40E8B5957E
  - LTP_DA64FD04E43656E6
  - LTP_DCC88B2C458969EA
  - LTP_DDA854712C50CD6A
  - LTP_DF5B725563FDFB31
  - LTP_ECD986F27CF15E1E
  - LTP_FC8BA85373EA2D8F
  static_checks:
  - STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO
  - STARRY_FINAL_SYSLOG_READ_ARGUMENTS
  - STARRY_FINAL_UMOUNT_PRIVILEGE
  - STARRY_FINAL_UNSHARE_NEWNS_PRIVILEGE
  - STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE
  - STARRY_ROUND3_INIT_MODULE_PERMISSION
  dynamic_tests:
  - STARRY_FINAL_FS_RUNTIME
  - STARRY_FINAL_WAIT_RUNTIME
historical_regression_unresolved: {}
diagnostic_directory: /tmp/syscallguard-check/check-20260723t030225z-60f534a3
content_hash: sha256:96b4fd5a48e827171c5eba14f2a93390c1cc6476e1973e80aa2f84962e6a588e
```
</details>
