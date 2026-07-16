# Starry 合规检查报告

## 本轮结论

- 状态：`completed`
- 静态检查：pass 37、fail 1、error 0
- 动态测试：pass 0、fail 0、skipped 0、not_run 0
- confirmed finding：1
- 新增：1、carry forward：0、已重验：0、待重验：0
- 环境或执行 blocker：0（不视为实现缺口）

## 静态检查

### `STARRY_ACCESS_USER_POINTER`

- 类型：`static`
- 关联 syscall：`access`
- 通用规则：`LTP_075318C437B76E06`、`LTP_0799FC60BADD2B18`、`LTP_38FB918826669241`、`LTP_58416E6747519699`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `let path = path\.nullable\(\)\.map\(vm_load_path_string\)\.transpose\(\)\?;[\s\S]*?let file = resolve_at\(dirfd, path\.as_deref\(\), flags\)\?;`：matched=`true`，第 71 行
- finding：—

### `STARRY_CAPGET_ABI`

- 类型：`static`
- 关联 syscall：`capget`
- 通用规则：`LTP_208C833FF12217F5`、`LTP_5F1D35ACCEFD4971`、`LTP_827CE5CB448A411B`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `fn validate_cap_header\([\s\S]*?header_ptr\.vm_read_uninit\(\)\?[\s\S]*?header\.version != CAPABILITY_VERSION_3[\s\S]*?header_ptr\.vm_write\(header\)\?[\s\S]*?Err\(AxError::InvalidInput\)`：matched=`true`，第 69 行
  - `pub fn sys_capget\([\s\S]*?validate_cap_header\(header\)\?[\s\S]*?cred_for_pid\(pid\)\?[\s\S]*?cap_data_from_cred\(&cred\)[\s\S]*?data\.vm_write\(cap_data\[0\]\)\?[\s\S]*?data\.add\(1\)\.vm_write\(cap_data\[1\]\)\?[\s\S]*?Ok\(0\)`：matched=`true`，第 135 行
- finding：—

### `STARRY_CAPSET_ABI`

- 类型：`static`
- 关联 syscall：`capset`
- 通用规则：`LTP_6D86AFD541A61388`、`LTP_E06D53042C10C99E`、`LTP_EC23768761E40E9F`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_capset\([\s\S]*?validate_cap_header\(header\)\?[\s\S]*?if data\.is_null\(\) \{[\s\S]*?Err\(AxError::BadAddress\)[\s\S]*?data\.vm_read_uninit\(\)\?[\s\S]*?data\.add\(1\)\.vm_read_uninit\(\)\?`：matched=`true`，第 160 行
  - `if effective & !permitted != 0[\s\S]*?adds_permitted[\s\S]*?if adds_permitted != 0[\s\S]*?if may_expand[\s\S]*?adds_inheritable`：matched=`true`，第 187 行
  - `new\.cap_effective = effective;[\s\S]*?new\.cap_permitted = permitted;[\s\S]*?new\.cap_inheritable = inheritable;[\s\S]*?new\.sanitize_capabilities\(\);[\s\S]*?thread\.set_cred\(new\);[\s\S]*?Ok\(0\)`：matched=`true`，第 206 行
- finding：—

### `STARRY_CLOSE_BAD_FD_ERRNO`

- 类型：`static`
- 关联 syscall：`close`
- 通用规则：`LTP_09B39E9C9254ECB2`、`LTP_0CD17E662AFD2956`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `BadFileDescriptor => EBADF`：matched=`true`，第 224 行
- finding：—

### `STARRY_CLOSE_FD_TABLE`

- 类型：`static`
- 关联 syscall：`close`
- 通用规则：`LTP_09B39E9C9254ECB2`、`LTP_0CD17E662AFD2956`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn close_file_like\(fd: c_int\)[\s\S]*?FD_TABLE\.write\(\)\.remove\(fd as usize\)`：matched=`true`，第 312 行
  - `pub fn close_file_like\(fd: c_int\)[\s\S]*?return Ok\(\(\)\);[\s\S]*?Err\(AxError::BadFileDescriptor\)`：matched=`true`，第 312 行
- finding：—

### `STARRY_CLOSE_RANGE_SWEEP`

- 类型：`static`
- 关联 syscall：`close_range`
- 通用规则：`LTP_76BFF56F735A0074`、`LTP_F4DE81D703447628`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_close_range\([\s\S]*?for fd in first\.\.=last\.min\(max_index as (?:i32\|u32)\)`：matched=`true`，第 489 行
  - `for fd in first\.\.=last\.min\(max_index as (?:i32\|u32)\)[\s\S]*?if let Some\(f\) = fd_table\.remove\(fd as _\)[\s\S]*?Ok\(0\)`：matched=`true`，第 514 行
- finding：—

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

### `STARRY_CLOSE_RANGE_VALIDATION`

- 类型：`static`
- 关联 syscall：`close_range`
- 通用规则：`LTP_31D9D767D6888DDA`、`LTP_CBF4B6C8A1458A28`、`LTP_F1DC44813DCA6A05`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_close_range\([\s\S]*?if (?:first < 0 \\|\\| )?last < first \{[\s\S]*?return Err\(AxError::InvalidInput\);`：matched=`true`，第 489 行
  - `pub fn sys_close_range\([\s\S]*?CloseRangeFlags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?`：matched=`true`，第 489 行
- finding：—

### `STARRY_CLOSE_SYSCALL`

- 类型：`static`
- 关联 syscall：`close`
- 通用规则：`LTP_09B39E9C9254ECB2`、`LTP_0CD17E662AFD2956`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_close\(fd: c_int\)[\s\S]*?close_file_like\(fd\)\?;`：matched=`true`，第 475 行
  - `pub fn sys_close\(fd: c_int\)[\s\S]*?close_file_like\(fd\)\?;[\s\S]*?Ok\(0\)`：matched=`true`，第 475 行
- finding：—

### `STARRY_CONNECT_ADDRESS_VALIDATION`

- 类型：`static`
- 关联 syscall：`connect`
- 通用规则：`LTP_4C3A8A7664F22B7F`、`LTP_6AEB77CEC03D0E6E`、`LTP_74E00510F4C1B849`
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
- 通用规则：`LTP_0FCE63CBC47F69DA`、`LTP_2F153EBAAD2A779C`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_connect\([\s\S]*?Socket::from_fd\(fd\)\?;[\s\S]*?SocketAddrEx::read_from_user\(addr, addrlen\)\?;`：matched=`true`，第 174 行
  - `pub fn sys_connect\([\s\S]*?socket\.connect\(addr\)\.map_err\([\s\S]*?AxError::WouldBlock[\s\S]*?AxError::InProgress[\s\S]*?\?;[\s\S]*?Ok\(0\)`：matched=`true`，第 174 行
- finding：—

### `STARRY_COPY_FILE_RANGE_CORE`

- 类型：`static`
- 关联 syscall：`copy_file_range`
- 通用规则：`LTP_09370275EF5F3065`、`LTP_6A2F1D2BB0EE8C22`、`LTP_7E1612F09CACE33D`、`LTP_AE3908C408304451`、`LTP_B87A71DE5DE1260E`、`LTP_BAE8F852378DD9F4`、`LTP_C16D549555A00E55`、`LTP_CC9037A76978B569`、`LTP_E2196C3F0F58862B`
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
- 关联 syscall：`copy_file_range`
- 通用规则：`LTP_74BB3F96CBA52D02`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_copy_file_range\([\s\S]*?if len > isize::MAX as usize \{[\s\S]*?return Err\(AxError::from\(LinuxError::EOVERFLOW\)\);`：matched=`true`，第 773 行
- finding：—

### `STARRY_DUP2_DUP3_BEHAVIOR`

- 类型：`static`
- 关联 syscall：`dup2`、`dup3`
- 通用规则：`LTP_098AFE0E8E10B0EF`、`LTP_1726C16756E9651C`、`LTP_37C625BD7D7C5F1D`、`LTP_3A7B17AF231D4158`、`LTP_4F02ACC6E2F6B094`、`LTP_75D52C5E9C93B6D7`、`LTP_9B3646398697EA64`、`LTP_9F560A103CB6F910`、`LTP_B7F51635806E7E59`、`LTP_BDA36F61423EEB3E`、`LTP_D296A517F138A0C0`、`LTP_EE8E695CF61D6D8A`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_dup2\(old_fd: c_int, new_fd: c_int\)[\s\S]*?if old_fd == new_fd \{[\s\S]*?get_file_like\(new_fd\)\?;[\s\S]*?return Ok\(new_fd as _\);[\s\S]*?sys_dup3\(old_fd, new_fd, 0\)`：matched=`true`，第 563 行
  - `pub fn sys_dup3\([\s\S]*?Dup3Flags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?;[\s\S]*?if old_fd == new_fd \{[\s\S]*?Err\(AxError::InvalidInput\)`：matched=`true`，第 578 行
  - `pub fn sys_dup3\([\s\S]*?\.get\(old_fd as _\)[\s\S]*?\.ok_or\(AxError::BadFileDescriptor\)\?;[\s\S]*?fd_table\.remove\(new_fd as _\)[\s\S]*?\.add_at\(new_fd as _, f\)[\s\S]*?Ok\(new_fd as _\)`：matched=`true`，第 578 行
- finding：—

### `STARRY_DUP_BEHAVIOR`

- 类型：`static`
- 关联 syscall：`dup`
- 通用规则：`LTP_0EBD1214FC6BB6D5`、`LTP_311F7A773994720E`、`LTP_511185D6DE2A63A0`、`LTP_594FA5B54CA204E5`、`LTP_84DBE108A850E845`、`LTP_A774FC10727E8ED2`、`LTP_ED2BA909DF79625A`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `fn dup_fd\(old_fd: c_int, cloexec: bool\)[\s\S]*?get_file_like\(old_fd\)\?;[\s\S]*?add_file_like\(f, cloexec\)\?;[\s\S]*?Ok\(new_fd as _\)`：matched=`true`，第 532 行
  - `pub fn sys_dup\(old_fd: c_int\)[\s\S]*?dup_fd\(old_fd, false\)`：matched=`true`，第 557 行
- finding：—

### `STARRY_EPOLL_CREATE`

- 类型：`static`
- 关联 syscall：`epoll_create`
- 通用规则：`LTP_2D1E25BD679B3494`、`LTP_37F2ED2BA3175CC3`、`LTP_E7435E0CBCA319E1`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_epoll_create\(size: i32\)[\s\S]*?if size <= 0 \{[\s\S]*?Err\(AxError::InvalidInput\)`：matched=`true`，第 114 行
  - `pub fn sys_epoll_create\(size: i32\)[\s\S]*?sys_epoll_create1\(0\)`：matched=`true`，第 114 行
  - `pub fn sys_epoll_create1\([\s\S]*?Epoll::new\(\)[\s\S]*?\.add_to_fd_table\([\s\S]*?\.map\(\\|fd\\| fd as isize\)`：matched=`true`，第 104 行
- finding：—

### `STARRY_EPOLL_CREATE1_FLAGS`

- 类型：`static`
- 关联 syscall：`epoll_create1`
- 通用规则：`LTP_5D8D2B3BEDA79604`、`LTP_89745BB32E6D4D02`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_epoll_create1\(flags: u32\)[\s\S]*?EpollCreateFlags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?`：matched=`true`，第 104 行
  - `pub fn sys_epoll_create1\(flags: u32\)[\s\S]*?Epoll::new\(\)[\s\S]*?\.add_to_fd_table\(flags\.contains\(EpollCreateFlags::CLOEXEC\)\)`：matched=`true`，第 104 行
- finding：—

### `STARRY_EPOLL_CTL_ENTRY`

- 类型：`static`
- 关联 syscall：`epoll_ctl`
- 通用规则：`LTP_22E98D1569DAB493`、`LTP_6FFB17DB762F3167`、`LTP_83709E56D6285F71`
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
- 通用规则：`LTP_468FC84DEAB0BCB8`、`LTP_4953FAD330ADE150`、`LTP_61778C450B602081`、`LTP_8ADB82F00C61D567`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `fn new\(fd: i32\)[\s\S]*?let file = get_file_like\(fd\)\?;`：matched=`true`，第 130 行
  - `pub fn add\([\s\S]*?guard\.contains_key\(&key\)[\s\S]*?return Err\(AxError::AlreadyExists\);`：matched=`true`，第 501 行
  - `pub fn modify\([\s\S]*?guard\.get_mut\(&key\)\.ok_or\(AxError::NotFound\)\?`：matched=`true`，第 537 行
  - `pub fn delete\([\s\S]*?\.remove\(&key\)[\s\S]*?\.ok_or\(AxError::NotFound\)\?`：matched=`true`，第 577 行
- finding：—

### `STARRY_EPOLL_FACCESS_ERRNO`

- 类型：`static`
- 关联 syscall：`epoll_create1`、`epoll_ctl`、`epoll_wait`、`execveat`、`faccessat2`
- 通用规则：`LTP_0FEC274199CCD0A0`、`LTP_18ECD15E5451228D`、`LTP_1ADEBF230DD2C214`、`LTP_22E98D1569DAB493`、`LTP_468FC84DEAB0BCB8`、`LTP_4953FAD330ADE150`、`LTP_4BCFF61005DC2E9A`、`LTP_4C1F446C9C520B36`、`LTP_4D51F55F25C6F2A3`、`LTP_5D8D2B3BEDA79604`、`LTP_61778C450B602081`、`LTP_66C670178B06E9F3`、`LTP_6885CE6A54F7716E`、`LTP_6FFB17DB762F3167`、`LTP_77AA3EAF2AD0C07A`、`LTP_83709E56D6285F71`、`LTP_89745BB32E6D4D02`、`LTP_8ADB82F00C61D567`、`LTP_8F30861E18D66625`、`LTP_ACF7A30AF3B10973`、`LTP_EA5D1572B890F71E`、`LTP_EC1CA29BE6888A6B`
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
- 关联 syscall：`epoll_ctl`、`epoll_wait`
- 通用规则：`LTP_6FFB17DB762F3167`、`LTP_8F30861E18D66625`、`LTP_EC1CA29BE6888A6B`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn get_file_like\(fd: c_int\)[\s\S]*?\.ok_or\(AxError::BadFileDescriptor\)`：matched=`true`，第 280 行
  - `fn from_fd\(fd: c_int\)[\s\S]*?get_file_like\(fd\)\?[\s\S]*?\.downcast_arc\(\)[\s\S]*?\.map_err\(\\|_\\| AxError::InvalidInput\)`：matched=`true`，第 250 行
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

### `STARRY_EPOLL_WAIT_VALIDATION`

- 类型：`static`
- 关联 syscall：`epoll_wait`
- 通用规则：`LTP_18ECD15E5451228D`、`LTP_1ADEBF230DD2C214`、`LTP_EA5D1572B890F71E`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `fn do_epoll_wait\([\s\S]*?if maxevents <= 0 \{[\s\S]*?return Err\(AxError::InvalidInput\);`：matched=`true`，第 176 行
  - `fn do_epoll_wait\([\s\S]*?if events\.is_null\(\) \{[\s\S]*?Err\(AxError::BadAddress\)[\s\S]*?check_epoll_events_access\(events, maxevents\)\?`：matched=`true`，第 176 行
  - `fn check_epoll_events_access\([\s\S]*?checked_mul\(size_of::<epoll_event>\(\)\)[\s\S]*?check_access\(start, len\)\?`：matched=`true`，第 36 行
- finding：—

### `STARRY_ERRNO_TRANSLATION`

- 类型：`static`
- 关联 syscall：`close`、`mmap`
- 通用规则：`LTP_09B39E9C9254ECB2`、`LTP_0CD17E662AFD2956`、`LTP_36C99C10CD38F8DB`、`LTP_45439D8F2BAB0832`、`LTP_51E295101A9F4411`、`LTP_52BAFC01DEA6E172`、`LTP_791DEA825D66980B`、`LTP_C346EFF1233F7061`、`LTP_F36F8C0CC1A6D840`、`LTP_FD1B65B0BCC88E0D`、`LTP_FEACDC300C3E1DD7`
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
- 通用规则：`LTP_4C1F446C9C520B36`、`LTP_5109EDF645F51D7E`、`LTP_77AA3EAF2AD0C07A`、`LTP_ACF7A30AF3B10973`、`LTP_EEDED564522D8D2D`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `Some\(""\) \\| None =>[\s\S]*?flags & AT_EMPTY_PATH == 0[\s\S]*?get_file_like\(dirfd\)\?`：matched=`true`，第 61 行
  - `Some\(path\) =>[\s\S]*?if path\.starts_with\('/'\) \{[\s\S]*?AT_FDCWD[\s\S]*?with_fs\(dirfd,`：matched=`true`，第 79 行
  - `impl FileLike for Directory[\s\S]*?fn from_fd\(fd: c_int\)[\s\S]*?get_file_like\(fd\)\?[\s\S]*?AxError::NotADirectory`：matched=`true`，第 312 行
- finding：—

### `STARRY_EXECVEAT_VALIDATION`

- 类型：`static`
- 关联 syscall：`execveat`
- 通用规则：`LTP_0FEC274199CCD0A0`、`LTP_ACF7A30AF3B10973`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_execveat\([\s\S]*?if flags & !\(AT_EMPTY_PATH \\| AT_SYMLINK_NOFOLLOW\) != 0 \{[\s\S]*?Err\(AxError::InvalidInput\)`：matched=`true`，第 46 行
  - `pub fn sys_execveat\([\s\S]*?vm_load_string\(path\)\?;[\s\S]*?resolve_at\(dirfd, Some\(path\.as_str\(\)\), flags\)\?`：matched=`true`，第 46 行
- finding：—

### `STARRY_FACCESSAT2_VALIDATION`

- 类型：`static`
- 关联 syscall：`faccessat2`
- 通用规则：`LTP_4BCFF61005DC2E9A`、`LTP_4D51F55F25C6F2A3`、`LTP_6885CE6A54F7716E`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `const FACCESSAT2_VALID_FLAGS:[\s\S]*?const FACCESSAT2_VALID_MODE:[\s\S]*?mode & !FACCESSAT2_VALID_MODE != 0 \\|\\| flags & !FACCESSAT2_VALID_FLAGS != 0[\s\S]*?Err\(AxError::InvalidInput\)`：matched=`true`，第 151 行
  - `pub fn sys_faccessat2\([\s\S]*?path\.nullable\(\)\.map\(vm_load_path_string\)\.transpose\(\)\?;[\s\S]*?resolve_at\(dirfd, path\.as_deref\(\), flags\)\?`：matched=`true`，第 147 行
- finding：—

### `STARRY_FCHDIR_CORE`

- 类型：`static`
- 关联 syscall：`fchdir`
- 通用规则：`LTP_17B7A9460939622A`、`LTP_CCC36F43E9463D3E`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_fchdir\(dirfd: i32\)[\s\S]*?with_fs\(dirfd,[\s\S]*?current_dir\(\)\.clone\(\)`：matched=`true`，第 96 行
  - `pub fn sys_fchdir\(dirfd: i32\)[\s\S]*?set_current_dir\(entry\)\?;`：matched=`true`，第 96 行
  - `pub fn sys_fchdir\(dirfd: i32\)[\s\S]*?set_current_dir\(entry\)\?;[\s\S]*?Ok\(0\)`：matched=`true`，第 96 行
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
- 通用规则：`LTP_CCC36F43E9463D3E`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn with_fs<[\s\S]*?if dirfd == AT_FDCWD[\s\S]*?Directory::from_fd\(dirfd\)\?`：matched=`true`，第 28 行
  - `impl FileLike for Directory[\s\S]*?fn from_fd\(fd: c_int\)[\s\S]*?get_file_like\(fd\)\?`：matched=`true`，第 312 行
- finding：—

### `STARRY_FCHMODAT_FLAG_VALIDATION`

- 类型：`static`
- 关联 syscall：`fchmodat`、`fchmodat2`
- 通用规则：`LTP_628FD2848734A58A`、`LTP_8BD2C43CB1EC6794`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `const FCHMODAT_VALID_FLAGS: u32 = AT_EMPTY_PATH \\| AT_SYMLINK_NOFOLLOW;`：matched=`true`，第 582 行
  - `if flags & !FCHMODAT_VALID_FLAGS != 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}`：matched=`true`，第 583 行
- finding：—

### `STARRY_FD_TABLE_LOOKUP_ALLOCATION`

- 类型：`static`
- 关联 syscall：`dup`
- 通用规则：`LTP_0EBD1214FC6BB6D5`、`LTP_311F7A773994720E`、`LTP_511185D6DE2A63A0`、`LTP_594FA5B54CA204E5`、`LTP_84DBE108A850E845`、`LTP_A774FC10727E8ED2`、`LTP_ED2BA909DF79625A`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn get_file_like\(fd: c_int\)[\s\S]*?FD_TABLE[\s\S]*?\.get\(fd as usize\)[\s\S]*?\.ok_or\(AxError::BadFileDescriptor\)`：matched=`true`，第 280 行
  - `pub fn add_file_like\([\s\S]*?RLIMIT_NOFILE[\s\S]*?if table\.count\(\) as u64 >= max_nofile \{[\s\S]*?Err\(AxError::TooManyOpenFiles\)`：matched=`true`，第 301 行
  - `pub fn add_file_like\([\s\S]*?Ok\(table\.add\(fd\)\.map_err\(\\|_\\| AxError::TooManyOpenFiles\)\? as c_int\)`：matched=`true`，第 301 行
- finding：—

### `STARRY_FINIT_MODULE_FLAG_VALIDATION`

- 类型：`static`
- 关联 syscall：`finit_module`
- 通用规则：`LTP_DA65D6C7A0E4ABBC`
- 结果：`fail`
- 原因：one or more required patterns did not match
- pattern 证据：

  - `pub fn sys_finit_module\(module_fd: i32, param_ptr: \*const u8, flags: u32\)`：matched=`false`，未匹配
  - `pub fn sys_finit_module\([\s\S]*?if flags != 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}`：matched=`false`，未匹配
- finding：`finding-finit-module-ltp-da65d6c7a0e4abbc-840b33b63dfd`

### `STARRY_MMAP_ACCESS`

- 类型：`static`
- 关联 syscall：`mmap`
- 通用规则：`LTP_36C99C10CD38F8DB`、`LTP_45439D8F2BAB0832`、`LTP_52BAFC01DEA6E172`、`LTP_C346EFF1233F7061`、`LTP_F36F8C0CC1A6D840`、`LTP_FD1B65B0BCC88E0D`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `if needs_file_mmap_checks \{[\s\S]*?if !flags\.contains\(FileFlags::READ\) \{[\s\S]*?return Err\(AxError::PermissionDenied\);`：matched=`true`，第 246 行
  - `matches!\(map_type, MmapFlags::SHARED\)[\s\S]*?permission_flags\.contains\(MmapProt::WRITE\)[\s\S]*?if !flags\.contains\(FileFlags::WRITE\) \{[\s\S]*?return Err\(AxError::PermissionDenied\);`：matched=`true`，第 214 行
- finding：—

### `STARRY_MMAP_ARGUMENTS`

- 类型：`static`
- 关联 syscall：`mmap`
- 通用规则：`LTP_51E295101A9F4411`、`LTP_FEACDC300C3E1DD7`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_mmap\([\s\S]*?if length == 0 \{[\s\S]*?return Err\(AxError::InvalidInput\);`：matched=`true`，第 128 行
  - `let map_type = match flags & MmapFlags::TYPE\.bits\(\)[\s\S]*?_ => return Err\(AxError::InvalidInput\)`：matched=`true`，第 160 行
- finding：—

### `STARRY_MMAP_FD`

- 类型：`static`
- 关联 syscall：`mmap`
- 通用规则：`LTP_791DEA825D66980B`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `if !anonymous && fd < 0 \{[\s\S]*?return Err\(AxError::BadFileDescriptor\);`：matched=`true`，第 170 行
  - `let file = if anonymous \{[\s\S]*?None[\s\S]*?\} else \{[\s\S]*?Some\(get_file_like\(fd\)\?\)`：matched=`true`，第 203 行
- finding：—

### `STARRY_ROUND2_ERRNO_TRANSLATION`

- 类型：`static`
- 关联 syscall：`close_range`、`connect`、`dup2`、`dup3`
- 通用规则：`LTP_098AFE0E8E10B0EF`、`LTP_0FCE63CBC47F69DA`、`LTP_2F153EBAAD2A779C`、`LTP_31D9D767D6888DDA`、`LTP_37C625BD7D7C5F1D`、`LTP_4F02ACC6E2F6B094`、`LTP_75D52C5E9C93B6D7`、`LTP_9B3646398697EA64`、`LTP_9F560A103CB6F910`、`LTP_BDA36F61423EEB3E`、`LTP_CBF4B6C8A1458A28`、`LTP_D296A517F138A0C0`、`LTP_F1DC44813DCA6A05`
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

### `STARRY_SOCKET_FD_VALIDATION`

- 类型：`static`
- 关联 syscall：`connect`
- 通用规则：`LTP_0FCE63CBC47F69DA`、`LTP_2F153EBAAD2A779C`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `fn from_fd\(fd: c_int\)[\s\S]*?get_file_like\(fd\)\?[\s\S]*?\.downcast_arc\(\)[\s\S]*?\.map_err\(\\|_\\| AxError::NotASocket\)`：matched=`true`，第 374 行
- finding：—

## 动态测试

本轮没有动态测试。

<details>
<summary>机器可读元数据</summary>

<!-- syscallguard-metadata -->
```yaml
schema_version: 1
kind: syscallguard_check_report
report_id: check-20260716t031844z-4ae8ccb5
status: completed
generated_at_utc: '2026-07-16T03:18:47.170987Z'
mapping_report_id: mapping-20260716t031657z-9314cea0
mapping_report_version:
  id: mapping-20260716t031657z-9314cea0
  generated_at_utc: '2026-07-16T03:17:56.282688Z'
  content_hash: sha256:ea02cc0374a2abbf004123efc6b6e4bbb2e242eb06061182b8f77772d10a89a0
target:
  target_id: starry
  repository: /home/cloud/gitLinux/tgoskits
  repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
  branch: dev-syscalls-compliance-1
  descriptor_hash: sha256:6b982bb80e3a0a3cf408d7c696367996422e3dac8376577222e56ee47f111d24
  snapshot_hash: sha256:840b33b63dfd4ed63ff8ec942312d9d8197fafed82d54b9ce5b568351c1312a0
input_hash: sha256:a8c1d9c0045042ae8f8a64a711a00d3cebdde401ed272e32a891a5f2a239d003
entity_hashes:
  rules:
    LTP_075318C437B76E06: sha256:075318c437b76e067682a9c6aab95a64558daf471c20df7205f62a72b1fd82ee
    LTP_0799FC60BADD2B18: sha256:0799fc60badd2b189b242a57ba5740cd832aa2477cbe8497f5b09324880ca7f4
    LTP_09370275EF5F3065: sha256:09370275ef5f3065d6f3ea10b7288a1ce0668fd80cc67a7d32a6f3b3069149f6
    LTP_098AFE0E8E10B0EF: sha256:098afe0e8e10b0efa6872ee3d2ece3674b519943b59189a2758d8ab31b06ab26
    LTP_09B39E9C9254ECB2: sha256:09b39e9c9254ecb24ccb5288c3f12281e9adc0b698de5c706a4f071599c3ce60
    LTP_0CD17E662AFD2956: sha256:0cd17e662afd2956c8c1a42d49b46dca16c37c1972fc6d3632c05c317939a996
    LTP_0EBD1214FC6BB6D5: sha256:0ebd1214fc6bb6d5e224e50177509f565c7be9ba6ad0d4842779e564b71dedbb
    LTP_0FCE63CBC47F69DA: sha256:0fce63cbc47f69da5e2da3272c04cf9386103a75c442cf8614d29166e37f3fbb
    LTP_0FEC274199CCD0A0: sha256:0fec274199ccd0a04984fadd1588ef353a2bcb0400a8e713f1adaa3f3a36c208
    LTP_1726C16756E9651C: sha256:1726c16756e9651c8be282bf1cdf5c30a283e32aa200934084e3c42a2aee9ff9
    LTP_17B7A9460939622A: sha256:17b7a9460939622a41226aa0c0191c618d2a9b74c6e2321e127b1ba067b85bff
    LTP_18ECD15E5451228D: sha256:18ecd15e5451228d55bbb4e06d2aeec746b9af6c9aca8fedd0b387d8e3484b50
    LTP_1ADEBF230DD2C214: sha256:1adebf230dd2c214f844468f75ee44f3ee8a8cec961a0ba26caa9afe58bd6d25
    LTP_208C833FF12217F5: sha256:208c833ff12217f5ee10c2893ca4aab718793f8504783e4c1e69970fe3fc01dc
    LTP_22E98D1569DAB493: sha256:22e98d1569dab4931d447f9ee3157b478dbeb887d9c466a1041be801be711343
    LTP_2D1E25BD679B3494: sha256:2d1e25bd679b349425ebcfa9dd820bb8bc4de40949cd671adc32204c68864bbc
    LTP_2F153EBAAD2A779C: sha256:2f153ebaad2a779c607faa895cdd3493a982348174a10df8a80375ab6dd5e426
    LTP_311F7A773994720E: sha256:311f7a773994720e7cac8cd3d2b12c6938f7c13b7a4eff6dbcfe843e466448ac
    LTP_31D9D767D6888DDA: sha256:31d9d767d6888ddaf3c03f24abe0bc874e9932a546e4cdd283ecad199e6bcc1a
    LTP_36C99C10CD38F8DB: sha256:36c99c10cd38f8db26e721ea351430f0ebc4767b9a31257223ad8fd5519c7d0d
    LTP_37C625BD7D7C5F1D: sha256:37c625bd7d7c5f1db42b7cacc49b4964844f0c2f977ad1a74c3960da0d662932
    LTP_37F2ED2BA3175CC3: sha256:37f2ed2ba3175cc394b1338888db3f207e809f7e36f789587873dc7921e85edd
    LTP_38FB918826669241: sha256:38fb918826669241ebbe77827a90f4347f124cf6de78fd4f4b46b3495fb3ab2f
    LTP_3A7B17AF231D4158: sha256:3a7b17af231d4158b2c4508e92a25435b89a569164e6dfdabc216b48e1afec9f
    LTP_425E5A3502541DE8: sha256:425e5a3502541de863d8b8e88eafb95db2f8d8e1f9cb88a32d8b3124950395b2
    LTP_45439D8F2BAB0832: sha256:45439d8f2bab0832027a39e78d024f72cc6449adff9fb823af60ff7c004d7bc5
    LTP_468FC84DEAB0BCB8: sha256:468fc84deab0bcb8749bee2c8342c88aa3345e7f8d1ff568958918217fc129de
    LTP_4953FAD330ADE150: sha256:4953fad330ade1503bf7a6d4d6bf2c353a337844f58042ceb3214149d1025945
    LTP_4BCFF61005DC2E9A: sha256:4bcff61005dc2e9a8baad1357435ae47571fe775bbdbee71ceb80f709a098f9e
    LTP_4C1F446C9C520B36: sha256:4c1f446c9c520b36b7f3b5a39c42fea74e7befa2adf95e4a919a1bb760184320
    LTP_4C3A8A7664F22B7F: sha256:4c3a8a7664f22b7f2983c449e5c15d82b53d634db19f0a87e67849d4feb2fb77
    LTP_4D51F55F25C6F2A3: sha256:4d51f55f25c6f2a3a51ed2c2be2b507816d6ae2d9ba1dd1adcc28340924b1a89
    LTP_4F02ACC6E2F6B094: sha256:4f02acc6e2f6b094f06413684c004106e4c18d8f654cbb8b231de56e60aba90c
    LTP_5109EDF645F51D7E: sha256:5109edf645f51d7ec6698c72239e0feedbcea9ffb1e4f9150d5e066527c66630
    LTP_511185D6DE2A63A0: sha256:511185d6de2a63a045d2f5f65babdf4c25b4066ece863b9f121419045563d4c9
    LTP_51E295101A9F4411: sha256:51e295101a9f4411b8c43521d430e85bd27ac1d7a96127b66675d7dc024ba9d2
    LTP_52BAFC01DEA6E172: sha256:52bafc01dea6e1725e71d23e11424031141e37ea07b99e151db6bcfc16116bde
    LTP_58416E6747519699: sha256:58416e6747519699e7b507fc0ff7e8c00852ff81eaff2cf425bb2d4a84e4e6f3
    LTP_594FA5B54CA204E5: sha256:594fa5b54ca204e5062358a745af4921e86e002d54071b19f1650a69d2d468f7
    LTP_5D8D2B3BEDA79604: sha256:5d8d2b3beda79604301b79695ead77bb1cca6ec4c1e6b679aabacb702befdccf
    LTP_5F1D35ACCEFD4971: sha256:5f1d35accefd49711e3b8b82de258ecb2f04bba65083b919659edb660948ef2f
    LTP_61778C450B602081: sha256:61778c450b60208142d63a0628d3f3a112b7bbdafa09587ce6e84c7618f736c5
    LTP_628FD2848734A58A: sha256:628fd2848734a58abbf91bdc33d9a0296f8f88586fddb7c71f9030a4423d288d
    LTP_66C670178B06E9F3: sha256:66c670178b06e9f3eae76490edd09b4a26bb0e1c2ccba3c4cbc2a625d12c39bb
    LTP_6885CE6A54F7716E: sha256:6885ce6a54f7716e5b79cac1af65007cb4f63aad6398b472d5a7539824bf4de9
    LTP_6A2F1D2BB0EE8C22: sha256:6a2f1d2bb0ee8c22d0970af42c645ba4f74a3cfe1a4748f4c47934666e135cfc
    LTP_6AEB77CEC03D0E6E: sha256:6aeb77cec03d0e6eaa956bea440fe8e71843fa521eafcf9611595dee8394b4bb
    LTP_6D86AFD541A61388: sha256:6d86afd541a613880ff94fbbb7fbfdbbebd5fd32d94544f7cc6e3f2ee850df77
    LTP_6FFB17DB762F3167: sha256:6ffb17db762f3167790a052bae0fa49f44b1075991c29dcec06f56509e9ae743
    LTP_74BB3F96CBA52D02: sha256:74bb3f96cba52d02850ad3c5e54c87acf278ce51290c99d5ae29da583be9ba38
    LTP_74E00510F4C1B849: sha256:74e00510f4c1b849cf8495790f1acd5cf1dc690a2ffcef67fc897e0c910fed22
    LTP_75D52C5E9C93B6D7: sha256:75d52c5e9c93b6d7989e3392a132ca3a319f4419c2f678533dc80d000c4891cd
    LTP_76BFF56F735A0074: sha256:76bff56f735a0074d725ee7dab337c42b7daf23d2ca44135affba4b983676aa8
    LTP_77AA3EAF2AD0C07A: sha256:77aa3eaf2ad0c07a8c890e541d76ea25203c93ad6fbacc025943afc55a92bc17
    LTP_791DEA825D66980B: sha256:791dea825d66980bfded73936e4745cf7b914f20652b9489e65a7a59509b897b
    LTP_7E1612F09CACE33D: sha256:7e1612f09cace33d1e08ea245c28317ff95a538558b1d15dc9cd9e6c8dd2eb09
    LTP_827CE5CB448A411B: sha256:827ce5cb448a411bcd82f3a89e9c733eb11fa4d44a8f563ff1658dac81bd73a4
    LTP_83709E56D6285F71: sha256:83709e56d6285f71dce5dcd5f54aa0ba99d44ddef002f1e6cc53f2fce6075678
    LTP_84DBE108A850E845: sha256:84dbe108a850e845bf4a3cfc65c984525f06a85bcf44e616283b5ef4e16bb451
    LTP_89745BB32E6D4D02: sha256:89745bb32e6d4d02b6ab504c2a88f1b47d35f128eb07bb1921b1c2adb76977d0
    LTP_8ADB82F00C61D567: sha256:8adb82f00c61d5671840571f67ba2e6ea75175e1b94b6fbe88f37d95f8031e40
    LTP_8BD2C43CB1EC6794: sha256:8bd2c43cb1ec6794ff35892efa1d2a2a3e07efe5ef83e9874cfdb79feae89704
    LTP_8F30861E18D66625: sha256:8f30861e18d666256af3aaaa7bd2a46e35d4fa8cb90ab3960bb318a6b7f25a51
    LTP_9B3646398697EA64: sha256:9b3646398697ea6481b4201006e677123cd226bb81910f45b6fa558aaa810832
    LTP_9F560A103CB6F910: sha256:9f560a103cb6f910cc2b8fb141c7de076accd6a913e920715328e9facdfb18db
    LTP_A774FC10727E8ED2: sha256:a774fc10727e8ed282a01bc787e12bd54a0d81a756fc45037304c5906dadb2ff
    LTP_ACF7A30AF3B10973: sha256:acf7a30af3b10973088f22334a5e2b35a00bbc3ff6530b1fb644856f637f06e4
    LTP_AE3908C408304451: sha256:ae3908c40830445120c2543a341389434b0eb8a4703f9666a62f96c38d9265e6
    LTP_B7F51635806E7E59: sha256:b7f51635806e7e596b7f6a1baf152d74ca1d365a9bdfc6d3f34984ac1908632d
    LTP_B87A71DE5DE1260E: sha256:b87a71de5de1260eeff71a5a683d9dea4fdc6e019dc8875ec98549865ba352ad
    LTP_BAE8F852378DD9F4: sha256:bae8f852378dd9f45a95e9fa5f5d957ef4f6efa3a462803119cc93500569bac0
    LTP_BDA36F61423EEB3E: sha256:bda36f61423eeb3e616d764edd458663817800e2f3db3adfae687bd17f6c2764
    LTP_C16D549555A00E55: sha256:c16d549555a00e55b3199db30fcc866aeac70c8911afbcc47053c09ffa2a5b85
    LTP_C346EFF1233F7061: sha256:c346eff1233f706172a595326e9215b63dd1f455b13880c762f92532db036e2e
    LTP_CBF4B6C8A1458A28: sha256:cbf4b6c8a1458a2885c6c847b47ca93098a06580fc5fdfc3a1e483b9dab01ac4
    LTP_CC9037A76978B569: sha256:cc9037a76978b569fcf3e91e91771dc63c6a8cf1479d9f5c6e079b8ef0e91e4f
    LTP_CCC36F43E9463D3E: sha256:ccc36f43e9463d3e65e732efa9e9d62af421e5d01bac07a5d343fc88f368505c
    LTP_D296A517F138A0C0: sha256:d296a517f138a0c09a3c71729b93607cfff1709b21125573bc2ad30b48302584
    LTP_DA65D6C7A0E4ABBC: sha256:da65d6c7a0e4abbc12ba61464384db59b2ccc9a4215469858de691a4c6deb562
    LTP_E06D53042C10C99E: sha256:e06d53042c10c99e7bdc61242d4ac56e1aace8c13e3442e875e2574ca74e60d3
    LTP_E2196C3F0F58862B: sha256:e2196c3f0f58862b9dfeb182337b8bdf6ab3964ad73867128bb0853431dc7dbe
    LTP_E7435E0CBCA319E1: sha256:e7435e0cbca319e18c1459e2f9187003681d326f400fc6d00b47df912010faef
    LTP_EA5D1572B890F71E: sha256:ea5d1572b890f71ea1a55cdcad2c53e9061edc3234a5c30ab4af4952cba049ad
    LTP_EC1CA29BE6888A6B: sha256:ec1ca29be6888a6b373d18e61642398247eb0d3006feee8826fd7fda26f99ab4
    LTP_EC23768761E40E9F: sha256:ec23768761e40e9f99140715f9e6147dcc348f9f7bbdc7731948b1afb6d29d51
    LTP_ED2BA909DF79625A: sha256:ed2ba909df79625a7857c363efc0303c51fef469ee87970e6b322004f28779a5
    LTP_EE8E695CF61D6D8A: sha256:ee8e695cf61d6d8aa981eb6e30bf3a8a53c8e8a4ad435ff362bbd78971d17088
    LTP_EEDED564522D8D2D: sha256:eeded564522d8d2df106307960b9b399555f31b2f4945dc5e10cff79a9fa1454
    LTP_F1DC44813DCA6A05: sha256:f1dc44813dca6a05d2fb0697718f8ed1da8d8b033d2c49bd0124284321f6ffd4
    LTP_F36F8C0CC1A6D840: sha256:f36f8c0cc1a6d84025a2394e30fa1d7c273ce9c13d8f58d759383c75dbf8c10a
    LTP_F4DE81D703447628: sha256:f4de81d70344762893139769a2724588ddb7213c4667529ce501948b3b6b43c5
    LTP_FD1B65B0BCC88E0D: sha256:fd1b65b0bcc88e0d283d47737c8b9d244de44d7461e8efd5bc6eb699ebaa0d54
    LTP_FEACDC300C3E1DD7: sha256:feacdc300c3e1dd754c7925df645b95995a6f17fd0ebcb6a50578071e2f9636f
  static_checks:
    STARRY_ACCESS_USER_POINTER: sha256:875194edef675fee671a296b54cac127af94497eb06c3d08e387c80fed656099
    STARRY_CAPGET_ABI: sha256:1620053a209fba43b466ec0a9b8eaea44efde42224801ad566b8f9d9c6a4e1fb
    STARRY_CAPSET_ABI: sha256:9e208fe86d54f4d13085a2933b1bc9bbc2ec4472c5fdf28dde3cf4eff6b67b41
    STARRY_CLOSE_BAD_FD_ERRNO: sha256:cd741d790147ea4efb9edc24a943e75a7eb0f3b6497495ca3fcd5dbc98e30eef
    STARRY_CLOSE_FD_TABLE: sha256:b5fddad8db22eb60fbbb67a55da405d70f70207c93744cf87c4d621deaacec37
    STARRY_CLOSE_RANGE_SWEEP: sha256:73b42b23b94b53e2991c70af9e072322a37f121e06c324f4fd33a9b597fa712e
    STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS: sha256:6d8ffe193808bde740053a61419adcf0e7c090388b2f5fea0475696c5b402070
    STARRY_CLOSE_RANGE_VALIDATION: sha256:7b18c7fc6e86e5b62680008a3173340100ff3f844aa5cbbaf8b2dcdae3095441
    STARRY_CLOSE_SYSCALL: sha256:5ef4691ec6b70a5f23bfd0429253461106ad98a8f0b559e7b9ca2590e22f183e
    STARRY_CONNECT_ADDRESS_VALIDATION: sha256:f12594e38c23899fa45d721c0c0bdaf7ef6184d8b987093528e94001d952b4ce
    STARRY_CONNECT_ENTRY: sha256:a9436bc59322ffd541750a10e74f7ed6b0e75cc0eb40427208da8cffbab16d37
    STARRY_COPY_FILE_RANGE_CORE: sha256:cecca7fcc313f9b590f06fcf52f1a0b42827c628ee777a7bb934634d6c26d100
    STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO: sha256:39ebc0849b8fede86d9689ed1dba7fda23315b83937a447b328ffd1a94bdfb34
    STARRY_DUP2_DUP3_BEHAVIOR: sha256:ad75ace8040caef4d7430d50b41a593338a6c088a861994feaef68e6d362c05f
    STARRY_DUP_BEHAVIOR: sha256:e8ac235053223da1e439ebad9e0cb7b2a2a9f11b336eea6f7157d11ed8c67184
    STARRY_EPOLL_CREATE: sha256:1e090e914261a999d33624fd3dc60e4c32d20d69f026e740b0a1d9128294db28
    STARRY_EPOLL_CREATE1_FLAGS: sha256:b9c09fe02c4ec588100e6c7dde83b219a76c89e3c39874599037737905c89d64
    STARRY_EPOLL_CTL_ENTRY: sha256:d9f9e3dadbc2ac04cd1596eb367ca56096d0dca11bb6bb5e16963e5961a45b5a
    STARRY_EPOLL_CTL_INTEREST: sha256:53dbda9fcebeaaf47a3e5bd0097f4a9ece6acb3c22859f1dcb712fadca856050
    STARRY_EPOLL_FACCESS_ERRNO: sha256:a99668dc49b4b2196fc6e42898c07e1aabfee9bb6ddccabfaa447da2e19f504d
    STARRY_EPOLL_FD_LOOKUP: sha256:6c943408bcfd7cbe3f417707adef3df73b1b4baa36ab2784ac38691cfe8c9f98
    STARRY_EPOLL_NESTED_LOOP: sha256:d1db97954ea66c6632d4d74191ef0d91751bbbcfee42883a78137bbdaac22e58
    STARRY_EPOLL_WAIT_VALIDATION: sha256:ab835412007b9a486885564ac76abf958e457cc7157b847d2815b674b67635e4
    STARRY_ERRNO_TRANSLATION: sha256:05a4d7a8d2961626f57c080b9e27de813981664f7b139c9602ac02f085483b67
    STARRY_EXECVEAT_FACCESSAT_RESOLVE: sha256:0d06085e4965d18e6d098b550174ea441c74c9c6084651e7f768841178393f35
    STARRY_EXECVEAT_VALIDATION: sha256:dc84733de108d41568ca0537906a51b7e31d6addfd2a71de7507ea03bc265725
    STARRY_FACCESSAT2_VALIDATION: sha256:c7546705c649d8b9279526e14d30e017ea98b814ef5bc72cbe2bd6904e2dd9a7
    STARRY_FCHDIR_CORE: sha256:5001a17fd4efc6ba8b94a96421849ff090882ce30ccdeecee15f18bc2fabcb12
    STARRY_FCHDIR_ERRNO_TRANSLATION: sha256:407ae3188273892147af1f9f750cbcc300ba6c5eb95c074ced64a221decd0ea3
    STARRY_FCHDIR_FD_VALIDATION: sha256:612b3e2eff9fef9f48d7d048ebb0456a32bfcdb5ac13ddcdd077f6e8c49fccb8
    STARRY_FCHMODAT_FLAG_VALIDATION: sha256:0fbb98a71708e8caf503460df5c31d3e683cc59f488b0e0e4dcf3139307739f6
    STARRY_FD_TABLE_LOOKUP_ALLOCATION: sha256:d8c36d57ee9d1cbdadd008c216897a3b8637a3f5942bb62efef92689f25135ce
    STARRY_FINIT_MODULE_FLAG_VALIDATION: sha256:8dfeecdf89721940c44ced615dcddcaa399751a598c6377e0f1f0b2f1e3a39c1
    STARRY_MMAP_ACCESS: sha256:7d80e14ce9b96ce706aa04e693bec4cd06ce2115b8d8017089bc9539da70581a
    STARRY_MMAP_ARGUMENTS: sha256:1e2b63de97e3c23eba0ae7d5750fa8a89752c8acccdde1ef954ce9f0fcae2963
    STARRY_MMAP_FD: sha256:119566942b56c1207135e08e44b2c8364af3c1255633b7b33c673252a5af254b
    STARRY_ROUND2_ERRNO_TRANSLATION: sha256:25461ffd64c3d1f37dc80f578e9ab5818c3736717b6570564219aea7c7a960f9
    STARRY_SOCKET_FD_VALIDATION: sha256:181dd8a7e6ce7f452e3a8b122e376eef02555e0f2058ffad086dd28fe08ceb0b
  dynamic_tests: {}
entity_versions:
  rules:
    LTP_075318C437B76E06:
      id: LTP_075318C437B76E06
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:075318c437b76e067682a9c6aab95a64558daf471c20df7205f62a72b1fd82ee
    LTP_0799FC60BADD2B18:
      id: LTP_0799FC60BADD2B18
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:0799fc60badd2b189b242a57ba5740cd832aa2477cbe8497f5b09324880ca7f4
    LTP_09370275EF5F3065:
      id: LTP_09370275EF5F3065
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:09370275ef5f3065d6f3ea10b7288a1ce0668fd80cc67a7d32a6f3b3069149f6
    LTP_098AFE0E8E10B0EF:
      id: LTP_098AFE0E8E10B0EF
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:098afe0e8e10b0efa6872ee3d2ece3674b519943b59189a2758d8ab31b06ab26
    LTP_09B39E9C9254ECB2:
      id: LTP_09B39E9C9254ECB2
      generated_at_utc: '2026-07-14T13:35:02.567816Z'
      content_hash: sha256:09b39e9c9254ecb24ccb5288c3f12281e9adc0b698de5c706a4f071599c3ce60
    LTP_0CD17E662AFD2956:
      id: LTP_0CD17E662AFD2956
      generated_at_utc: '2026-07-14T13:35:02.567816Z'
      content_hash: sha256:0cd17e662afd2956c8c1a42d49b46dca16c37c1972fc6d3632c05c317939a996
    LTP_0EBD1214FC6BB6D5:
      id: LTP_0EBD1214FC6BB6D5
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:0ebd1214fc6bb6d5e224e50177509f565c7be9ba6ad0d4842779e564b71dedbb
    LTP_0FCE63CBC47F69DA:
      id: LTP_0FCE63CBC47F69DA
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:0fce63cbc47f69da5e2da3272c04cf9386103a75c442cf8614d29166e37f3fbb
    LTP_0FEC274199CCD0A0:
      id: LTP_0FEC274199CCD0A0
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:0fec274199ccd0a04984fadd1588ef353a2bcb0400a8e713f1adaa3f3a36c208
    LTP_1726C16756E9651C:
      id: LTP_1726C16756E9651C
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:1726c16756e9651c8be282bf1cdf5c30a283e32aa200934084e3c42a2aee9ff9
    LTP_17B7A9460939622A:
      id: LTP_17B7A9460939622A
      generated_at_utc: '2026-07-16T02:52:01.871423Z'
      content_hash: sha256:17b7a9460939622a41226aa0c0191c618d2a9b74c6e2321e127b1ba067b85bff
    LTP_18ECD15E5451228D:
      id: LTP_18ECD15E5451228D
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:18ecd15e5451228d55bbb4e06d2aeec746b9af6c9aca8fedd0b387d8e3484b50
    LTP_1ADEBF230DD2C214:
      id: LTP_1ADEBF230DD2C214
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:1adebf230dd2c214f844468f75ee44f3ee8a8cec961a0ba26caa9afe58bd6d25
    LTP_208C833FF12217F5:
      id: LTP_208C833FF12217F5
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:208c833ff12217f5ee10c2893ca4aab718793f8504783e4c1e69970fe3fc01dc
    LTP_22E98D1569DAB493:
      id: LTP_22E98D1569DAB493
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:22e98d1569dab4931d447f9ee3157b478dbeb887d9c466a1041be801be711343
    LTP_2D1E25BD679B3494:
      id: LTP_2D1E25BD679B3494
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:2d1e25bd679b349425ebcfa9dd820bb8bc4de40949cd671adc32204c68864bbc
    LTP_2F153EBAAD2A779C:
      id: LTP_2F153EBAAD2A779C
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:2f153ebaad2a779c607faa895cdd3493a982348174a10df8a80375ab6dd5e426
    LTP_311F7A773994720E:
      id: LTP_311F7A773994720E
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:311f7a773994720e7cac8cd3d2b12c6938f7c13b7a4eff6dbcfe843e466448ac
    LTP_31D9D767D6888DDA:
      id: LTP_31D9D767D6888DDA
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:31d9d767d6888ddaf3c03f24abe0bc874e9932a546e4cdd283ecad199e6bcc1a
    LTP_36C99C10CD38F8DB:
      id: LTP_36C99C10CD38F8DB
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:36c99c10cd38f8db26e721ea351430f0ebc4767b9a31257223ad8fd5519c7d0d
    LTP_37C625BD7D7C5F1D:
      id: LTP_37C625BD7D7C5F1D
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:37c625bd7d7c5f1db42b7cacc49b4964844f0c2f977ad1a74c3960da0d662932
    LTP_37F2ED2BA3175CC3:
      id: LTP_37F2ED2BA3175CC3
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:37f2ed2ba3175cc394b1338888db3f207e809f7e36f789587873dc7921e85edd
    LTP_38FB918826669241:
      id: LTP_38FB918826669241
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:38fb918826669241ebbe77827a90f4347f124cf6de78fd4f4b46b3495fb3ab2f
    LTP_3A7B17AF231D4158:
      id: LTP_3A7B17AF231D4158
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:3a7b17af231d4158b2c4508e92a25435b89a569164e6dfdabc216b48e1afec9f
    LTP_425E5A3502541DE8:
      id: LTP_425E5A3502541DE8
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:425e5a3502541de863d8b8e88eafb95db2f8d8e1f9cb88a32d8b3124950395b2
    LTP_45439D8F2BAB0832:
      id: LTP_45439D8F2BAB0832
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:45439d8f2bab0832027a39e78d024f72cc6449adff9fb823af60ff7c004d7bc5
    LTP_468FC84DEAB0BCB8:
      id: LTP_468FC84DEAB0BCB8
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:468fc84deab0bcb8749bee2c8342c88aa3345e7f8d1ff568958918217fc129de
    LTP_4953FAD330ADE150:
      id: LTP_4953FAD330ADE150
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:4953fad330ade1503bf7a6d4d6bf2c353a337844f58042ceb3214149d1025945
    LTP_4BCFF61005DC2E9A:
      id: LTP_4BCFF61005DC2E9A
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:4bcff61005dc2e9a8baad1357435ae47571fe775bbdbee71ceb80f709a098f9e
    LTP_4C1F446C9C520B36:
      id: LTP_4C1F446C9C520B36
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:4c1f446c9c520b36b7f3b5a39c42fea74e7befa2adf95e4a919a1bb760184320
    LTP_4C3A8A7664F22B7F:
      id: LTP_4C3A8A7664F22B7F
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:4c3a8a7664f22b7f2983c449e5c15d82b53d634db19f0a87e67849d4feb2fb77
    LTP_4D51F55F25C6F2A3:
      id: LTP_4D51F55F25C6F2A3
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:4d51f55f25c6f2a3a51ed2c2be2b507816d6ae2d9ba1dd1adcc28340924b1a89
    LTP_4F02ACC6E2F6B094:
      id: LTP_4F02ACC6E2F6B094
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:4f02acc6e2f6b094f06413684c004106e4c18d8f654cbb8b231de56e60aba90c
    LTP_5109EDF645F51D7E:
      id: LTP_5109EDF645F51D7E
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:5109edf645f51d7ec6698c72239e0feedbcea9ffb1e4f9150d5e066527c66630
    LTP_511185D6DE2A63A0:
      id: LTP_511185D6DE2A63A0
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:511185d6de2a63a045d2f5f65babdf4c25b4066ece863b9f121419045563d4c9
    LTP_51E295101A9F4411:
      id: LTP_51E295101A9F4411
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:51e295101a9f4411b8c43521d430e85bd27ac1d7a96127b66675d7dc024ba9d2
    LTP_52BAFC01DEA6E172:
      id: LTP_52BAFC01DEA6E172
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:52bafc01dea6e1725e71d23e11424031141e37ea07b99e151db6bcfc16116bde
    LTP_58416E6747519699:
      id: LTP_58416E6747519699
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:58416e6747519699e7b507fc0ff7e8c00852ff81eaff2cf425bb2d4a84e4e6f3
    LTP_594FA5B54CA204E5:
      id: LTP_594FA5B54CA204E5
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:594fa5b54ca204e5062358a745af4921e86e002d54071b19f1650a69d2d468f7
    LTP_5D8D2B3BEDA79604:
      id: LTP_5D8D2B3BEDA79604
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:5d8d2b3beda79604301b79695ead77bb1cca6ec4c1e6b679aabacb702befdccf
    LTP_5F1D35ACCEFD4971:
      id: LTP_5F1D35ACCEFD4971
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:5f1d35accefd49711e3b8b82de258ecb2f04bba65083b919659edb660948ef2f
    LTP_61778C450B602081:
      id: LTP_61778C450B602081
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:61778c450b60208142d63a0628d3f3a112b7bbdafa09587ce6e84c7618f736c5
    LTP_628FD2848734A58A:
      id: LTP_628FD2848734A58A
      generated_at_utc: '2026-07-16T02:52:01.871423Z'
      content_hash: sha256:628fd2848734a58abbf91bdc33d9a0296f8f88586fddb7c71f9030a4423d288d
    LTP_66C670178B06E9F3:
      id: LTP_66C670178B06E9F3
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:66c670178b06e9f3eae76490edd09b4a26bb0e1c2ccba3c4cbc2a625d12c39bb
    LTP_6885CE6A54F7716E:
      id: LTP_6885CE6A54F7716E
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:6885ce6a54f7716e5b79cac1af65007cb4f63aad6398b472d5a7539824bf4de9
    LTP_6A2F1D2BB0EE8C22:
      id: LTP_6A2F1D2BB0EE8C22
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:6a2f1d2bb0ee8c22d0970af42c645ba4f74a3cfe1a4748f4c47934666e135cfc
    LTP_6AEB77CEC03D0E6E:
      id: LTP_6AEB77CEC03D0E6E
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:6aeb77cec03d0e6eaa956bea440fe8e71843fa521eafcf9611595dee8394b4bb
    LTP_6D86AFD541A61388:
      id: LTP_6D86AFD541A61388
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:6d86afd541a613880ff94fbbb7fbfdbbebd5fd32d94544f7cc6e3f2ee850df77
    LTP_6FFB17DB762F3167:
      id: LTP_6FFB17DB762F3167
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:6ffb17db762f3167790a052bae0fa49f44b1075991c29dcec06f56509e9ae743
    LTP_74BB3F96CBA52D02:
      id: LTP_74BB3F96CBA52D02
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:74bb3f96cba52d02850ad3c5e54c87acf278ce51290c99d5ae29da583be9ba38
    LTP_74E00510F4C1B849:
      id: LTP_74E00510F4C1B849
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:74e00510f4c1b849cf8495790f1acd5cf1dc690a2ffcef67fc897e0c910fed22
    LTP_75D52C5E9C93B6D7:
      id: LTP_75D52C5E9C93B6D7
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:75d52c5e9c93b6d7989e3392a132ca3a319f4419c2f678533dc80d000c4891cd
    LTP_76BFF56F735A0074:
      id: LTP_76BFF56F735A0074
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:76bff56f735a0074d725ee7dab337c42b7daf23d2ca44135affba4b983676aa8
    LTP_77AA3EAF2AD0C07A:
      id: LTP_77AA3EAF2AD0C07A
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:77aa3eaf2ad0c07a8c890e541d76ea25203c93ad6fbacc025943afc55a92bc17
    LTP_791DEA825D66980B:
      id: LTP_791DEA825D66980B
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:791dea825d66980bfded73936e4745cf7b914f20652b9489e65a7a59509b897b
    LTP_7E1612F09CACE33D:
      id: LTP_7E1612F09CACE33D
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:7e1612f09cace33d1e08ea245c28317ff95a538558b1d15dc9cd9e6c8dd2eb09
    LTP_827CE5CB448A411B:
      id: LTP_827CE5CB448A411B
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:827ce5cb448a411bcd82f3a89e9c733eb11fa4d44a8f563ff1658dac81bd73a4
    LTP_83709E56D6285F71:
      id: LTP_83709E56D6285F71
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:83709e56d6285f71dce5dcd5f54aa0ba99d44ddef002f1e6cc53f2fce6075678
    LTP_84DBE108A850E845:
      id: LTP_84DBE108A850E845
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:84dbe108a850e845bf4a3cfc65c984525f06a85bcf44e616283b5ef4e16bb451
    LTP_89745BB32E6D4D02:
      id: LTP_89745BB32E6D4D02
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:89745bb32e6d4d02b6ab504c2a88f1b47d35f128eb07bb1921b1c2adb76977d0
    LTP_8ADB82F00C61D567:
      id: LTP_8ADB82F00C61D567
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:8adb82f00c61d5671840571f67ba2e6ea75175e1b94b6fbe88f37d95f8031e40
    LTP_8BD2C43CB1EC6794:
      id: LTP_8BD2C43CB1EC6794
      generated_at_utc: '2026-07-16T02:52:01.871423Z'
      content_hash: sha256:8bd2c43cb1ec6794ff35892efa1d2a2a3e07efe5ef83e9874cfdb79feae89704
    LTP_8F30861E18D66625:
      id: LTP_8F30861E18D66625
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:8f30861e18d666256af3aaaa7bd2a46e35d4fa8cb90ab3960bb318a6b7f25a51
    LTP_9B3646398697EA64:
      id: LTP_9B3646398697EA64
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:9b3646398697ea6481b4201006e677123cd226bb81910f45b6fa558aaa810832
    LTP_9F560A103CB6F910:
      id: LTP_9F560A103CB6F910
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:9f560a103cb6f910cc2b8fb141c7de076accd6a913e920715328e9facdfb18db
    LTP_A774FC10727E8ED2:
      id: LTP_A774FC10727E8ED2
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:a774fc10727e8ed282a01bc787e12bd54a0d81a756fc45037304c5906dadb2ff
    LTP_ACF7A30AF3B10973:
      id: LTP_ACF7A30AF3B10973
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:acf7a30af3b10973088f22334a5e2b35a00bbc3ff6530b1fb644856f637f06e4
    LTP_AE3908C408304451:
      id: LTP_AE3908C408304451
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:ae3908c40830445120c2543a341389434b0eb8a4703f9666a62f96c38d9265e6
    LTP_B7F51635806E7E59:
      id: LTP_B7F51635806E7E59
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:b7f51635806e7e596b7f6a1baf152d74ca1d365a9bdfc6d3f34984ac1908632d
    LTP_B87A71DE5DE1260E:
      id: LTP_B87A71DE5DE1260E
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:b87a71de5de1260eeff71a5a683d9dea4fdc6e019dc8875ec98549865ba352ad
    LTP_BAE8F852378DD9F4:
      id: LTP_BAE8F852378DD9F4
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:bae8f852378dd9f45a95e9fa5f5d957ef4f6efa3a462803119cc93500569bac0
    LTP_BDA36F61423EEB3E:
      id: LTP_BDA36F61423EEB3E
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:bda36f61423eeb3e616d764edd458663817800e2f3db3adfae687bd17f6c2764
    LTP_C16D549555A00E55:
      id: LTP_C16D549555A00E55
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:c16d549555a00e55b3199db30fcc866aeac70c8911afbcc47053c09ffa2a5b85
    LTP_C346EFF1233F7061:
      id: LTP_C346EFF1233F7061
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:c346eff1233f706172a595326e9215b63dd1f455b13880c762f92532db036e2e
    LTP_CBF4B6C8A1458A28:
      id: LTP_CBF4B6C8A1458A28
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:cbf4b6c8a1458a2885c6c847b47ca93098a06580fc5fdfc3a1e483b9dab01ac4
    LTP_CC9037A76978B569:
      id: LTP_CC9037A76978B569
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:cc9037a76978b569fcf3e91e91771dc63c6a8cf1479d9f5c6e079b8ef0e91e4f
    LTP_CCC36F43E9463D3E:
      id: LTP_CCC36F43E9463D3E
      generated_at_utc: '2026-07-16T02:52:01.871423Z'
      content_hash: sha256:ccc36f43e9463d3e65e732efa9e9d62af421e5d01bac07a5d343fc88f368505c
    LTP_D296A517F138A0C0:
      id: LTP_D296A517F138A0C0
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:d296a517f138a0c09a3c71729b93607cfff1709b21125573bc2ad30b48302584
    LTP_DA65D6C7A0E4ABBC:
      id: LTP_DA65D6C7A0E4ABBC
      generated_at_utc: '2026-07-16T02:52:01.871423Z'
      content_hash: sha256:da65d6c7a0e4abbc12ba61464384db59b2ccc9a4215469858de691a4c6deb562
    LTP_E06D53042C10C99E:
      id: LTP_E06D53042C10C99E
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:e06d53042c10c99e7bdc61242d4ac56e1aace8c13e3442e875e2574ca74e60d3
    LTP_E2196C3F0F58862B:
      id: LTP_E2196C3F0F58862B
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:e2196c3f0f58862b9dfeb182337b8bdf6ab3964ad73867128bb0853431dc7dbe
    LTP_E7435E0CBCA319E1:
      id: LTP_E7435E0CBCA319E1
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:e7435e0cbca319e18c1459e2f9187003681d326f400fc6d00b47df912010faef
    LTP_EA5D1572B890F71E:
      id: LTP_EA5D1572B890F71E
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:ea5d1572b890f71ea1a55cdcad2c53e9061edc3234a5c30ab4af4952cba049ad
    LTP_EC1CA29BE6888A6B:
      id: LTP_EC1CA29BE6888A6B
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:ec1ca29be6888a6b373d18e61642398247eb0d3006feee8826fd7fda26f99ab4
    LTP_EC23768761E40E9F:
      id: LTP_EC23768761E40E9F
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ec23768761e40e9f99140715f9e6147dcc348f9f7bbdc7731948b1afb6d29d51
    LTP_ED2BA909DF79625A:
      id: LTP_ED2BA909DF79625A
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:ed2ba909df79625a7857c363efc0303c51fef469ee87970e6b322004f28779a5
    LTP_EE8E695CF61D6D8A:
      id: LTP_EE8E695CF61D6D8A
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:ee8e695cf61d6d8aa981eb6e30bf3a8a53c8e8a4ad435ff362bbd78971d17088
    LTP_EEDED564522D8D2D:
      id: LTP_EEDED564522D8D2D
      generated_at_utc: '2026-07-15T10:14:12.969080Z'
      content_hash: sha256:eeded564522d8d2df106307960b9b399555f31b2f4945dc5e10cff79a9fa1454
    LTP_F1DC44813DCA6A05:
      id: LTP_F1DC44813DCA6A05
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:f1dc44813dca6a05d2fb0697718f8ed1da8d8b033d2c49bd0124284321f6ffd4
    LTP_F36F8C0CC1A6D840:
      id: LTP_F36F8C0CC1A6D840
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:f36f8c0cc1a6d84025a2394e30fa1d7c273ce9c13d8f58d759383c75dbf8c10a
    LTP_F4DE81D703447628:
      id: LTP_F4DE81D703447628
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:f4de81d70344762893139769a2724588ddb7213c4667529ce501948b3b6b43c5
    LTP_FD1B65B0BCC88E0D:
      id: LTP_FD1B65B0BCC88E0D
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:fd1b65b0bcc88e0d283d47737c8b9d244de44d7461e8efd5bc6eb699ebaa0d54
    LTP_FEACDC300C3E1DD7:
      id: LTP_FEACDC300C3E1DD7
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:feacdc300c3e1dd754c7925df645b95995a6f17fd0ebcb6a50578071e2f9636f
  static_checks:
    STARRY_ACCESS_USER_POINTER:
      id: STARRY_ACCESS_USER_POINTER
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:875194edef675fee671a296b54cac127af94497eb06c3d08e387c80fed656099
    STARRY_CAPGET_ABI:
      id: STARRY_CAPGET_ABI
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:1620053a209fba43b466ec0a9b8eaea44efde42224801ad566b8f9d9c6a4e1fb
    STARRY_CAPSET_ABI:
      id: STARRY_CAPSET_ABI
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:9e208fe86d54f4d13085a2933b1bc9bbc2ec4472c5fdf28dde3cf4eff6b67b41
    STARRY_CLOSE_BAD_FD_ERRNO:
      id: STARRY_CLOSE_BAD_FD_ERRNO
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:cd741d790147ea4efb9edc24a943e75a7eb0f3b6497495ca3fcd5dbc98e30eef
    STARRY_CLOSE_FD_TABLE:
      id: STARRY_CLOSE_FD_TABLE
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:b5fddad8db22eb60fbbb67a55da405d70f70207c93744cf87c4d621deaacec37
    STARRY_CLOSE_RANGE_SWEEP:
      id: STARRY_CLOSE_RANGE_SWEEP
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:73b42b23b94b53e2991c70af9e072322a37f121e06c324f4fd33a9b597fa712e
    STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS:
      id: STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:6d8ffe193808bde740053a61419adcf0e7c090388b2f5fea0475696c5b402070
    STARRY_CLOSE_RANGE_VALIDATION:
      id: STARRY_CLOSE_RANGE_VALIDATION
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:7b18c7fc6e86e5b62680008a3173340100ff3f844aa5cbbaf8b2dcdae3095441
    STARRY_CLOSE_SYSCALL:
      id: STARRY_CLOSE_SYSCALL
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:5ef4691ec6b70a5f23bfd0429253461106ad98a8f0b559e7b9ca2590e22f183e
    STARRY_CONNECT_ADDRESS_VALIDATION:
      id: STARRY_CONNECT_ADDRESS_VALIDATION
      generated_at_utc: '2026-07-15T05:39:36.212938Z'
      content_hash: sha256:f12594e38c23899fa45d721c0c0bdaf7ef6184d8b987093528e94001d952b4ce
    STARRY_CONNECT_ENTRY:
      id: STARRY_CONNECT_ENTRY
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:a9436bc59322ffd541750a10e74f7ed6b0e75cc0eb40427208da8cffbab16d37
    STARRY_COPY_FILE_RANGE_CORE:
      id: STARRY_COPY_FILE_RANGE_CORE
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:cecca7fcc313f9b590f06fcf52f1a0b42827c628ee777a7bb934634d6c26d100
    STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO:
      id: STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:39ebc0849b8fede86d9689ed1dba7fda23315b83937a447b328ffd1a94bdfb34
    STARRY_DUP2_DUP3_BEHAVIOR:
      id: STARRY_DUP2_DUP3_BEHAVIOR
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:ad75ace8040caef4d7430d50b41a593338a6c088a861994feaef68e6d362c05f
    STARRY_DUP_BEHAVIOR:
      id: STARRY_DUP_BEHAVIOR
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:e8ac235053223da1e439ebad9e0cb7b2a2a9f11b336eea6f7157d11ed8c67184
    STARRY_EPOLL_CREATE:
      id: STARRY_EPOLL_CREATE
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:1e090e914261a999d33624fd3dc60e4c32d20d69f026e740b0a1d9128294db28
    STARRY_EPOLL_CREATE1_FLAGS:
      id: STARRY_EPOLL_CREATE1_FLAGS
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:b9c09fe02c4ec588100e6c7dde83b219a76c89e3c39874599037737905c89d64
    STARRY_EPOLL_CTL_ENTRY:
      id: STARRY_EPOLL_CTL_ENTRY
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:d9f9e3dadbc2ac04cd1596eb367ca56096d0dca11bb6bb5e16963e5961a45b5a
    STARRY_EPOLL_CTL_INTEREST:
      id: STARRY_EPOLL_CTL_INTEREST
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:53dbda9fcebeaaf47a3e5bd0097f4a9ece6acb3c22859f1dcb712fadca856050
    STARRY_EPOLL_FACCESS_ERRNO:
      id: STARRY_EPOLL_FACCESS_ERRNO
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:a99668dc49b4b2196fc6e42898c07e1aabfee9bb6ddccabfaa447da2e19f504d
    STARRY_EPOLL_FD_LOOKUP:
      id: STARRY_EPOLL_FD_LOOKUP
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:6c943408bcfd7cbe3f417707adef3df73b1b4baa36ab2784ac38691cfe8c9f98
    STARRY_EPOLL_NESTED_LOOP:
      id: STARRY_EPOLL_NESTED_LOOP
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:d1db97954ea66c6632d4d74191ef0d91751bbbcfee42883a78137bbdaac22e58
    STARRY_EPOLL_WAIT_VALIDATION:
      id: STARRY_EPOLL_WAIT_VALIDATION
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:ab835412007b9a486885564ac76abf958e457cc7157b847d2815b674b67635e4
    STARRY_ERRNO_TRANSLATION:
      id: STARRY_ERRNO_TRANSLATION
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:05a4d7a8d2961626f57c080b9e27de813981664f7b139c9602ac02f085483b67
    STARRY_EXECVEAT_FACCESSAT_RESOLVE:
      id: STARRY_EXECVEAT_FACCESSAT_RESOLVE
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:0d06085e4965d18e6d098b550174ea441c74c9c6084651e7f768841178393f35
    STARRY_EXECVEAT_VALIDATION:
      id: STARRY_EXECVEAT_VALIDATION
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:dc84733de108d41568ca0537906a51b7e31d6addfd2a71de7507ea03bc265725
    STARRY_FACCESSAT2_VALIDATION:
      id: STARRY_FACCESSAT2_VALIDATION
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:c7546705c649d8b9279526e14d30e017ea98b814ef5bc72cbe2bd6904e2dd9a7
    STARRY_FCHDIR_CORE:
      id: STARRY_FCHDIR_CORE
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:5001a17fd4efc6ba8b94a96421849ff090882ce30ccdeecee15f18bc2fabcb12
    STARRY_FCHDIR_ERRNO_TRANSLATION:
      id: STARRY_FCHDIR_ERRNO_TRANSLATION
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:407ae3188273892147af1f9f750cbcc300ba6c5eb95c074ced64a221decd0ea3
    STARRY_FCHDIR_FD_VALIDATION:
      id: STARRY_FCHDIR_FD_VALIDATION
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:612b3e2eff9fef9f48d7d048ebb0456a32bfcdb5ac13ddcdd077f6e8c49fccb8
    STARRY_FCHMODAT_FLAG_VALIDATION:
      id: STARRY_FCHMODAT_FLAG_VALIDATION
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:0fbb98a71708e8caf503460df5c31d3e683cc59f488b0e0e4dcf3139307739f6
    STARRY_FD_TABLE_LOOKUP_ALLOCATION:
      id: STARRY_FD_TABLE_LOOKUP_ALLOCATION
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:d8c36d57ee9d1cbdadd008c216897a3b8637a3f5942bb62efef92689f25135ce
    STARRY_FINIT_MODULE_FLAG_VALIDATION:
      id: STARRY_FINIT_MODULE_FLAG_VALIDATION
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:8dfeecdf89721940c44ced615dcddcaa399751a598c6377e0f1f0b2f1e3a39c1
    STARRY_MMAP_ACCESS:
      id: STARRY_MMAP_ACCESS
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:7d80e14ce9b96ce706aa04e693bec4cd06ce2115b8d8017089bc9539da70581a
    STARRY_MMAP_ARGUMENTS:
      id: STARRY_MMAP_ARGUMENTS
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:1e2b63de97e3c23eba0ae7d5750fa8a89752c8acccdde1ef954ce9f0fcae2963
    STARRY_MMAP_FD:
      id: STARRY_MMAP_FD
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:119566942b56c1207135e08e44b2c8364af3c1255633b7b33c673252a5af254b
    STARRY_ROUND2_ERRNO_TRANSLATION:
      id: STARRY_ROUND2_ERRNO_TRANSLATION
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:25461ffd64c3d1f37dc80f578e9ab5818c3736717b6570564219aea7c7a960f9
    STARRY_SOCKET_FD_VALIDATION:
      id: STARRY_SOCKET_FD_VALIDATION
      generated_at_utc: '2026-07-16T03:17:56.282688Z'
      content_hash: sha256:181dd8a7e6ce7f452e3a8b122e376eef02555e0f2058ffad086dd28fe08ceb0b
  dynamic_tests: {}
base_execution_scope:
  rules:
  - LTP_075318C437B76E06
  - LTP_0799FC60BADD2B18
  - LTP_09370275EF5F3065
  - LTP_098AFE0E8E10B0EF
  - LTP_09B39E9C9254ECB2
  - LTP_0CD17E662AFD2956
  - LTP_0EBD1214FC6BB6D5
  - LTP_0FCE63CBC47F69DA
  - LTP_0FEC274199CCD0A0
  - LTP_1726C16756E9651C
  - LTP_17B7A9460939622A
  - LTP_18ECD15E5451228D
  - LTP_1ADEBF230DD2C214
  - LTP_208C833FF12217F5
  - LTP_22E98D1569DAB493
  - LTP_2D1E25BD679B3494
  - LTP_2F153EBAAD2A779C
  - LTP_311F7A773994720E
  - LTP_31D9D767D6888DDA
  - LTP_36C99C10CD38F8DB
  - LTP_37C625BD7D7C5F1D
  - LTP_37F2ED2BA3175CC3
  - LTP_38FB918826669241
  - LTP_3A7B17AF231D4158
  - LTP_425E5A3502541DE8
  - LTP_45439D8F2BAB0832
  - LTP_468FC84DEAB0BCB8
  - LTP_4953FAD330ADE150
  - LTP_4BCFF61005DC2E9A
  - LTP_4C1F446C9C520B36
  - LTP_4C3A8A7664F22B7F
  - LTP_4D51F55F25C6F2A3
  - LTP_4F02ACC6E2F6B094
  - LTP_5109EDF645F51D7E
  - LTP_511185D6DE2A63A0
  - LTP_51E295101A9F4411
  - LTP_52BAFC01DEA6E172
  - LTP_58416E6747519699
  - LTP_594FA5B54CA204E5
  - LTP_5D8D2B3BEDA79604
  - LTP_5F1D35ACCEFD4971
  - LTP_61778C450B602081
  - LTP_628FD2848734A58A
  - LTP_66C670178B06E9F3
  - LTP_6885CE6A54F7716E
  - LTP_6A2F1D2BB0EE8C22
  - LTP_6AEB77CEC03D0E6E
  - LTP_6D86AFD541A61388
  - LTP_6FFB17DB762F3167
  - LTP_74BB3F96CBA52D02
  - LTP_74E00510F4C1B849
  - LTP_75D52C5E9C93B6D7
  - LTP_76BFF56F735A0074
  - LTP_77AA3EAF2AD0C07A
  - LTP_791DEA825D66980B
  - LTP_7E1612F09CACE33D
  - LTP_827CE5CB448A411B
  - LTP_83709E56D6285F71
  - LTP_84DBE108A850E845
  - LTP_89745BB32E6D4D02
  - LTP_8ADB82F00C61D567
  - LTP_8BD2C43CB1EC6794
  - LTP_8F30861E18D66625
  - LTP_9B3646398697EA64
  - LTP_9F560A103CB6F910
  - LTP_A774FC10727E8ED2
  - LTP_ACF7A30AF3B10973
  - LTP_AE3908C408304451
  - LTP_B7F51635806E7E59
  - LTP_B87A71DE5DE1260E
  - LTP_BAE8F852378DD9F4
  - LTP_BDA36F61423EEB3E
  - LTP_C16D549555A00E55
  - LTP_C346EFF1233F7061
  - LTP_CBF4B6C8A1458A28
  - LTP_CC9037A76978B569
  - LTP_CCC36F43E9463D3E
  - LTP_D296A517F138A0C0
  - LTP_DA65D6C7A0E4ABBC
  - LTP_E06D53042C10C99E
  - LTP_E2196C3F0F58862B
  - LTP_E7435E0CBCA319E1
  - LTP_EA5D1572B890F71E
  - LTP_EC1CA29BE6888A6B
  - LTP_EC23768761E40E9F
  - LTP_ED2BA909DF79625A
  - LTP_EE8E695CF61D6D8A
  - LTP_EEDED564522D8D2D
  - LTP_F1DC44813DCA6A05
  - LTP_F36F8C0CC1A6D840
  - LTP_F4DE81D703447628
  - LTP_FD1B65B0BCC88E0D
  - LTP_FEACDC300C3E1DD7
  static_checks:
  - STARRY_ACCESS_USER_POINTER
  - STARRY_CAPGET_ABI
  - STARRY_CAPSET_ABI
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
  - STARRY_EPOLL_CREATE
  - STARRY_EPOLL_CREATE1_FLAGS
  - STARRY_EPOLL_CTL_ENTRY
  - STARRY_EPOLL_CTL_INTEREST
  - STARRY_EPOLL_FACCESS_ERRNO
  - STARRY_EPOLL_FD_LOOKUP
  - STARRY_EPOLL_NESTED_LOOP
  - STARRY_EPOLL_WAIT_VALIDATION
  - STARRY_ERRNO_TRANSLATION
  - STARRY_EXECVEAT_FACCESSAT_RESOLVE
  - STARRY_EXECVEAT_VALIDATION
  - STARRY_FACCESSAT2_VALIDATION
  - STARRY_FCHDIR_CORE
  - STARRY_FCHDIR_ERRNO_TRANSLATION
  - STARRY_FCHDIR_FD_VALIDATION
  - STARRY_FCHMODAT_FLAG_VALIDATION
  - STARRY_FD_TABLE_LOOKUP_ALLOCATION
  - STARRY_FINIT_MODULE_FLAG_VALIDATION
  - STARRY_MMAP_ACCESS
  - STARRY_MMAP_ARGUMENTS
  - STARRY_MMAP_FD
  - STARRY_ROUND2_ERRNO_TRANSLATION
  - STARRY_SOCKET_FD_VALIDATION
  dynamic_tests: []
revalidation_scope:
  rules: []
  static_checks: []
  dynamic_tests: []
effective_execution_scope: &id001
  rules:
  - LTP_075318C437B76E06
  - LTP_0799FC60BADD2B18
  - LTP_09370275EF5F3065
  - LTP_098AFE0E8E10B0EF
  - LTP_09B39E9C9254ECB2
  - LTP_0CD17E662AFD2956
  - LTP_0EBD1214FC6BB6D5
  - LTP_0FCE63CBC47F69DA
  - LTP_0FEC274199CCD0A0
  - LTP_1726C16756E9651C
  - LTP_17B7A9460939622A
  - LTP_18ECD15E5451228D
  - LTP_1ADEBF230DD2C214
  - LTP_208C833FF12217F5
  - LTP_22E98D1569DAB493
  - LTP_2D1E25BD679B3494
  - LTP_2F153EBAAD2A779C
  - LTP_311F7A773994720E
  - LTP_31D9D767D6888DDA
  - LTP_36C99C10CD38F8DB
  - LTP_37C625BD7D7C5F1D
  - LTP_37F2ED2BA3175CC3
  - LTP_38FB918826669241
  - LTP_3A7B17AF231D4158
  - LTP_425E5A3502541DE8
  - LTP_45439D8F2BAB0832
  - LTP_468FC84DEAB0BCB8
  - LTP_4953FAD330ADE150
  - LTP_4BCFF61005DC2E9A
  - LTP_4C1F446C9C520B36
  - LTP_4C3A8A7664F22B7F
  - LTP_4D51F55F25C6F2A3
  - LTP_4F02ACC6E2F6B094
  - LTP_5109EDF645F51D7E
  - LTP_511185D6DE2A63A0
  - LTP_51E295101A9F4411
  - LTP_52BAFC01DEA6E172
  - LTP_58416E6747519699
  - LTP_594FA5B54CA204E5
  - LTP_5D8D2B3BEDA79604
  - LTP_5F1D35ACCEFD4971
  - LTP_61778C450B602081
  - LTP_628FD2848734A58A
  - LTP_66C670178B06E9F3
  - LTP_6885CE6A54F7716E
  - LTP_6A2F1D2BB0EE8C22
  - LTP_6AEB77CEC03D0E6E
  - LTP_6D86AFD541A61388
  - LTP_6FFB17DB762F3167
  - LTP_74BB3F96CBA52D02
  - LTP_74E00510F4C1B849
  - LTP_75D52C5E9C93B6D7
  - LTP_76BFF56F735A0074
  - LTP_77AA3EAF2AD0C07A
  - LTP_791DEA825D66980B
  - LTP_7E1612F09CACE33D
  - LTP_827CE5CB448A411B
  - LTP_83709E56D6285F71
  - LTP_84DBE108A850E845
  - LTP_89745BB32E6D4D02
  - LTP_8ADB82F00C61D567
  - LTP_8BD2C43CB1EC6794
  - LTP_8F30861E18D66625
  - LTP_9B3646398697EA64
  - LTP_9F560A103CB6F910
  - LTP_A774FC10727E8ED2
  - LTP_ACF7A30AF3B10973
  - LTP_AE3908C408304451
  - LTP_B7F51635806E7E59
  - LTP_B87A71DE5DE1260E
  - LTP_BAE8F852378DD9F4
  - LTP_BDA36F61423EEB3E
  - LTP_C16D549555A00E55
  - LTP_C346EFF1233F7061
  - LTP_CBF4B6C8A1458A28
  - LTP_CC9037A76978B569
  - LTP_CCC36F43E9463D3E
  - LTP_D296A517F138A0C0
  - LTP_DA65D6C7A0E4ABBC
  - LTP_E06D53042C10C99E
  - LTP_E2196C3F0F58862B
  - LTP_E7435E0CBCA319E1
  - LTP_EA5D1572B890F71E
  - LTP_EC1CA29BE6888A6B
  - LTP_EC23768761E40E9F
  - LTP_ED2BA909DF79625A
  - LTP_EE8E695CF61D6D8A
  - LTP_EEDED564522D8D2D
  - LTP_F1DC44813DCA6A05
  - LTP_F36F8C0CC1A6D840
  - LTP_F4DE81D703447628
  - LTP_FD1B65B0BCC88E0D
  - LTP_FEACDC300C3E1DD7
  static_checks:
  - STARRY_ACCESS_USER_POINTER
  - STARRY_CAPGET_ABI
  - STARRY_CAPSET_ABI
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
  - STARRY_EPOLL_CREATE
  - STARRY_EPOLL_CREATE1_FLAGS
  - STARRY_EPOLL_CTL_ENTRY
  - STARRY_EPOLL_CTL_INTEREST
  - STARRY_EPOLL_FACCESS_ERRNO
  - STARRY_EPOLL_FD_LOOKUP
  - STARRY_EPOLL_NESTED_LOOP
  - STARRY_EPOLL_WAIT_VALIDATION
  - STARRY_ERRNO_TRANSLATION
  - STARRY_EXECVEAT_FACCESSAT_RESOLVE
  - STARRY_EXECVEAT_VALIDATION
  - STARRY_FACCESSAT2_VALIDATION
  - STARRY_FCHDIR_CORE
  - STARRY_FCHDIR_ERRNO_TRANSLATION
  - STARRY_FCHDIR_FD_VALIDATION
  - STARRY_FCHMODAT_FLAG_VALIDATION
  - STARRY_FD_TABLE_LOOKUP_ALLOCATION
  - STARRY_FINIT_MODULE_FLAG_VALIDATION
  - STARRY_MMAP_ACCESS
  - STARRY_MMAP_ARGUMENTS
  - STARRY_MMAP_FD
  - STARRY_ROUND2_ERRNO_TRANSLATION
  - STARRY_SOCKET_FD_VALIDATION
  dynamic_tests: []
execution_scope: *id001
rule_syscalls:
  LTP_00F2A9EA8833DA1D:
  - cachestat
  LTP_0180982614AA9F7D:
  - access
  LTP_021CFAE8581109DA:
  - fsconfig
  LTP_023F1DC98CE31416:
  - fchmodat
  LTP_025CF701276457CB:
  - faccessat2
  LTP_0290063892A53510:
  - access
  LTP_030858A5FFCCEFF4:
  - access
  LTP_035E62E6D1787773:
  - access
  LTP_036EDA2B8D36CF03:
  - access
  LTP_03702BF4223F6AA5:
  - epoll_wait
  LTP_037E6F334D0E0D16:
  - access
  LTP_0431E3529AA0FEE8:
  - access
  LTP_043885E3B78D9010:
  - fchdir
  LTP_044E7C11E6B503BB:
  - access
  LTP_04A84187DEC4CF09:
  - flock
  LTP_060B6037DEF1D43C:
  - access
  LTP_06725D44DFF06F7E:
  - access
  LTP_06891E2E299CF48E:
  - access
  LTP_06A0C295D8E7FAFA:
  - access
  LTP_06AC9297E35AAE7A:
  - access
  LTP_075318C437B76E06:
  - access
  LTP_0799FC60BADD2B18:
  - access
  LTP_09370275EF5F3065:
  - copy_file_range
  LTP_098AFE0E8E10B0EF:
  - dup3
  LTP_09AB8108C3720119:
  - fchmodat2
  LTP_09B39E9C9254ECB2:
  - close
  LTP_09FED6AAC1020069:
  - fpathconf
  LTP_0A62800536904C02:
  - access
  LTP_0AAFA34BA77A0D25:
  - access
  LTP_0B35C54F2F39E4D4:
  - fsconfig
  LTP_0B45FC33068D334C:
  - access
  LTP_0BB235F712E819CE:
  - access
  LTP_0CD17E662AFD2956:
  - close
  LTP_0D1782EAAC26DEB4:
  - access
  LTP_0D9BB2CB02786128:
  - fsconfig
  LTP_0DF4BC077C390176:
  - fsconfig
  LTP_0E114DF9B3215650:
  - finit_module
  LTP_0E9AF2C058AF8126:
  - access
  LTP_0EBD1214FC6BB6D5:
  - dup
  LTP_0F901C62092CC7B8:
  - access
  LTP_0FCE63CBC47F69DA:
  - connect
  LTP_0FEC274199CCD0A0:
  - execveat
  LTP_10A684C1C2D2DE0F:
  - access
  LTP_10FE1313FBAB5F92:
  - access
  LTP_11235D2EF3DC4C5C:
  - fsconfig
  LTP_11CB16D3E88491A4:
  - copy_file_range
  LTP_12A1904141AAE2EE:
  - dup2
  LTP_1325C077A1CDE514:
  - cachestat
  LTP_132A1A1638D957AF:
  - connect
  LTP_1402459B5FF9BF23:
  - access
  LTP_1465554B09CE14F0:
  - access
  LTP_148623FDAF4E478D:
  - access
  LTP_153B296FA599E0CE:
  - access
  LTP_1726C16756E9651C:
  - dup3
  LTP_17ACF3BE969B64EE:
  - access
  LTP_17B7A9460939622A:
  - fchdir
  LTP_17CB4ED7A76BD283:
  - access
  LTP_183B0BD036512FA6:
  - fchmodat
  LTP_1870C0046E9555AF:
  - access
  LTP_18A450CE49F8867B:
  - access
  LTP_18ECD15E5451228D:
  - epoll_wait
  LTP_1918D556CB808466:
  - fsconfig
  LTP_198D9555A8BED013:
  - access
  LTP_1A9481FAD460FBF7:
  - alarm
  LTP_1AA7F21DA5C55800:
  - eventfd
  LTP_1ADEBF230DD2C214:
  - epoll_wait
  LTP_1BD36AE285B4F3E2:
  - access
  LTP_1C462AC54A29FF35:
  - access
  LTP_1C8100D018645855:
  - fsconfig
  LTP_1CDCF5FE9ED1BE5D:
  - access
  LTP_1D39F97D759F0E57:
  - access
  LTP_1DF2B28499E4D7B3:
  - access
  LTP_1EEDAE05876D0546:
  - fpathconf
  LTP_208C833FF12217F5:
  - capget
  LTP_20DA453342D2F4AB:
  - fpathconf
  LTP_212269CECE600FD8:
  - access
  LTP_21A007DF738F1E73:
  - access
  LTP_21C4957F9EFE94D3:
  - access
  LTP_220D1227D307AD3C:
  - access
  LTP_2221F954D01EB2BB:
  - access
  LTP_22E98D1569DAB493:
  - epoll_ctl
  LTP_2433DF1752AE54B7:
  - fsconfig
  LTP_245110930B22BF5C:
  - flock
  LTP_245CD61DAA19DC98:
  - chroot
  LTP_25639C9C5750C487:
  - access
  LTP_26AC646B9D18C353:
  - access
  LTP_272A188C039BEA2B:
  - finit_module
  LTP_277FD467E5F1BF1C:
  - accept
  LTP_27C7E91095DB9DF8:
  - access
  LTP_2900BC64740A3E44:
  - access
  LTP_298AB67F0CFA519C:
  - access
  LTP_2ACD165E402BB8AE:
  - copy_file_range
  LTP_2B4171DD8FBD982A:
  - access
  LTP_2BBDFB48EF060066:
  - fsconfig
  LTP_2BDE60C0E64B4DC8:
  - close
  LTP_2D0BAECAE4F61432:
  - access
  LTP_2D1E25BD679B3494:
  - epoll_create
  LTP_2E5D530A61E60934:
  - access
  LTP_2F153EBAAD2A779C:
  - connect
  LTP_2F99FA84C445363C:
  - access
  LTP_2FA43CD942AE7AD6:
  - access
  LTP_2FE8FAD800DE41F6:
  - access
  LTP_3073AC57544A6A6A:
  - fchmodat
  LTP_311F7A773994720E:
  - dup
  LTP_31D9D767D6888DDA:
  - close_range
  LTP_33C492F97B790AB8:
  - fpathconf
  LTP_33D137B9002503E5:
  - exit_group
  LTP_3472CD1A0F8A2B4A:
  - access
  LTP_347761CBCF52D194:
  - access
  LTP_34C12DFEB9C8A62A:
  - finit_module
  LTP_34CFEAD03DB6A3CA:
  - access
  LTP_34EC9FB9C9551214:
  - cachestat
  LTP_34FB3789C7448B4F:
  - fchmodat2
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
  LTP_371BDA67CB8813FD:
  - fchmod
  LTP_37C625BD7D7C5F1D:
  - dup3
  LTP_37F2ED2BA3175CC3:
  - epoll_create
  LTP_38FB918826669241:
  - access
  LTP_3900F4E562AE09D1:
  - access
  LTP_3916A669595B3568:
  - access
  LTP_3A7B17AF231D4158:
  - dup3
  LTP_3AD3865603ADDC8E:
  - access
  LTP_3AF9CC563B4BAC1C:
  - flock
  LTP_3C2853617B38EEE7:
  - access
  LTP_3D4ECD22BC433164:
  - access
  LTP_3D50FA09D36623FF:
  - fsconfig
  LTP_3D8D38C9123CD051:
  - access
  LTP_3DE23AB4FE2FFC67:
  - access
  LTP_3E0077ECCDBC2639:
  - fchmodat
  LTP_3E526A0A23B5EF6D:
  - access
  LTP_3E8DA9E014B82702:
  - alarm
  LTP_3F81436312777EF4:
  - access
  LTP_401D471D37C85820:
  - access
  LTP_425E5A3502541DE8:
  - close_range
  LTP_437CFCD991A666C9:
  - faccessat2
  LTP_44128D8D82BC1E09:
  - flock
  LTP_45439D8F2BAB0832:
  - mmap
  LTP_461340ED83E7043D:
  - capset
  LTP_46401248F52AD892:
  - fsconfig
  LTP_4661BBF1B3CD3A1E:
  - access
  LTP_468FC84DEAB0BCB8:
  - epoll_ctl
  LTP_46DE8D9AD1674F26:
  - access
  LTP_470C0966080C93EF:
  - fchmod
  LTP_472AAA35C7382B26:
  - accept
  LTP_479924116854D92B:
  - access
  LTP_48753F73ACA755FB:
  - access
  LTP_4881657CFE57C7E9:
  - access
  LTP_492D25A0F1055F72:
  - access
  LTP_4948E12FB8F9FA49:
  - access
  LTP_4953FAD330ADE150:
  - epoll_ctl
  LTP_49700CDA955B66D8:
  - access
  LTP_49A36559B96D24AF:
  - access
  LTP_4B6E9B98E2E5103D:
  - access
  LTP_4BCFF61005DC2E9A:
  - faccessat2
  LTP_4C1F446C9C520B36:
  - faccessat2
  LTP_4C3A8A7664F22B7F:
  - connect
  LTP_4CFAFCE7FCA2BF99:
  - access
  LTP_4D51F55F25C6F2A3:
  - faccessat2
  LTP_4ECB786BFA071AAC:
  - access
  LTP_4F02ACC6E2F6B094:
  - dup2
  LTP_50972E17C52A9EF6:
  - fsconfig
  LTP_50A86D4D5411356E:
  - access
  LTP_50F858A3CBF95EED:
  - chroot
  LTP_50FD97B7CD409007:
  - flock
  LTP_5109EDF645F51D7E:
  - faccessat2
  LTP_511185D6DE2A63A0:
  - dup
  LTP_51E295101A9F4411:
  - mmap
  LTP_51E954C969CAFA58:
  - flistxattr
  LTP_52BAFC01DEA6E172:
  - mmap
  LTP_52C209105EE62171:
  - access
  LTP_53B499F623D50A0A:
  - fsconfig
  LTP_5570480E7920BD0E:
  - access
  LTP_55D4EF674AFB4ED1:
  - fsconfig
  LTP_55EFF664BDCE3E21:
  - fsconfig
  LTP_5622491E8A2227F2:
  - eventfd
  LTP_563FB650864E0DC6:
  - access
  LTP_5667C5A09C3EC10E:
  - finit_module
  LTP_582938D6E8E17DB3:
  - fpathconf
  LTP_58416E6747519699:
  - access
  LTP_5883CD050463E9E8:
  - epoll_ctl
  LTP_58F1512157A0052D:
  - access
  LTP_594FA5B54CA204E5:
  - dup
  LTP_5A315335586D4227:
  - access
  LTP_5B244D0A4892F35A:
  - finit_module
  LTP_5BC52683943E907D:
  - epoll_ctl
  LTP_5C5CDC165410C08C:
  - access
  LTP_5CC44E5D1A6B6485:
  - access
  LTP_5D7971086B2ABAE5:
  - access
  LTP_5D8D2B3BEDA79604:
  - epoll_create1
  LTP_5DC368435F71390F:
  - fsconfig
  LTP_5EC31E34822684C4:
  - access
  LTP_5F1D35ACCEFD4971:
  - capget
  LTP_606B7E40B6BD82EA:
  - access
  LTP_6090C26F5D5D8E5D:
  - fsconfig
  LTP_609D7178B8A77C1F:
  - flistxattr
  LTP_613A5E121B4B6E68:
  - access
  LTP_6156A09A2E506F76:
  - access
  LTP_6169F41023E00C34:
  - access
  LTP_61778C450B602081:
  - epoll_ctl
  LTP_628FD2848734A58A:
  - fchmodat
  LTP_636590E5A017B28D:
  - access
  LTP_64227C746913D03D:
  - access
  LTP_6449E4A1D20C01D3:
  - alarm
  LTP_64A4E5DC71A633A2:
  - access
  LTP_65281FBEE0BF6103:
  - access
  LTP_6580B4D3FA1A86F3:
  - access
  LTP_65B70356F06E31F8:
  - alarm
  LTP_66C670178B06E9F3:
  - epoll_ctl
  LTP_679436EC7A4E218A:
  - access
  LTP_67BF94A4ACD303C4:
  - access
  LTP_68745D21F4EC2FF5:
  - access
  LTP_6885CE6A54F7716E:
  - faccessat2
  LTP_68E1B26815D97B79:
  - access
  LTP_69077B093E81B570:
  - access
  LTP_690A651C3A60FC1E:
  - access
  LTP_69E094D1DBFF3796:
  - access
  LTP_6A1A431A08A3F450:
  - access
  LTP_6A2F1D2BB0EE8C22:
  - copy_file_range
  LTP_6A70899352D69A0B:
  - flock
  LTP_6AEB77CEC03D0E6E:
  - connect
  LTP_6B1746F6BB2266CA:
  - access
  LTP_6B8B5453E8B4E6DE:
  - access
  LTP_6C11BBB4AABA6E7C:
  - access
  LTP_6C55A3E760DF75DB:
  - access
  LTP_6CE9FC3BCA164B5D:
  - access
  LTP_6D584CE6CF9B8A06:
  - access
  LTP_6D86AFD541A61388:
  - capset
  LTP_6EF7ECD2A8470CEA:
  - access
  LTP_6FFB17DB762F3167:
  - epoll_ctl
  LTP_708F721FB3456F82:
  - fsconfig
  LTP_711D5693356A79F2:
  - access
  LTP_71C54C624831C7F0:
  - chroot
  LTP_725BDB092C6D8F74:
  - execveat
  LTP_73DF50509BCC128B:
  - access
  LTP_74819A9DC2B5CB06:
  - access
  LTP_74BAD566B6A0F272:
  - finit_module
  LTP_74BB3F96CBA52D02:
  - copy_file_range
  LTP_74E00510F4C1B849:
  - connect
  LTP_752C9A802CF96B8B:
  - access
  LTP_75D52C5E9C93B6D7:
  - dup2
  LTP_76A9B6CF388A8609:
  - alarm
  LTP_76BFF56F735A0074:
  - close_range
  LTP_76D3B1710474AAC2:
  - copy_file_range
  LTP_76F002F46086B46C:
  - execveat
  LTP_77AA3EAF2AD0C07A:
  - faccessat2
  LTP_78EEEBE648781151:
  - access
  LTP_791DEA825D66980B:
  - mmap
  LTP_7963C3DF373596FE:
  - access
  LTP_79C7516DECB19092:
  - access
  LTP_79FCE1367A3A0369:
  - epoll_wait
  LTP_7A02B34D5FB8BBC3:
  - access
  LTP_7A74A699442CEB99:
  - brk
  LTP_7AF4AAC644090507:
  - finit_module
  LTP_7B539E14354153DC:
  - access
  LTP_7BE2877017694C52:
  - access
  LTP_7C06A3394E786948:
  - access
  LTP_7CB2C1C8643130AD:
  - copy_file_range
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
  LTP_7E1612F09CACE33D:
  - copy_file_range
  LTP_7EAD5A075576B981:
  - flock
  LTP_7ECC43C03A3DCB14:
  - fsconfig
  LTP_7F43697FAC4213A8:
  - copy_file_range
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
  LTP_8059D9227293D592:
  - access
  LTP_807E2072E5694684:
  - access
  LTP_80C6DB0ACB2A5510:
  - accept
  LTP_818BA624CA9E4040:
  - access
  LTP_820495EA1D1F15DA:
  - access
  LTP_82621B02FCA09F40:
  - alarm
  LTP_827CE5CB448A411B:
  - capget
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
  LTP_843BDD20FF921FC3:
  - access
  LTP_84DBE108A850E845:
  - dup
  LTP_84E4CC971DD16EC2:
  - access
  LTP_853D34D061DDE8F8:
  - access
  LTP_853F4B8346648EB9:
  - access
  LTP_857DC6AD01A88D79:
  - access
  LTP_86E690B05A18AF6A:
  - flock
  LTP_87478A6C3AC7DC60:
  - access
  LTP_884775F9076E54AB:
  - access
  LTP_885F3BA721198C07:
  - access
  LTP_88D0821E4776E388:
  - fsconfig
  LTP_88F6F279E33633DE:
  - access
  LTP_89745BB32E6D4D02:
  - epoll_create1
  LTP_89C9E8458EC38C11:
  - cachestat
  LTP_8A4C03F737A3CEE6:
  - fchmodat
  LTP_8AC11633EA3D83E0:
  - access
  LTP_8AD8032754BC8842:
  - cacheflush
  LTP_8ADB82F00C61D567:
  - epoll_ctl
  LTP_8B1A2084BCF096F1:
  - access
  LTP_8B3FBDFD0453EF40:
  - access
  LTP_8BB576EB2E1E6B23:
  - access
  LTP_8BD2C43CB1EC6794:
  - fchmodat2
  LTP_8BFB8BE2E39B38A1:
  - finit_module
  LTP_8C508A50371B6444:
  - access
  LTP_8CB51F0A9F8FDEA1:
  - access
  LTP_8D3BFFA98E2561BA:
  - access
  LTP_8D54825D4B298C7C:
  - access
  LTP_8E7F1BE3D7D7823B:
  - access
  LTP_8F29388433422812:
  - access
  LTP_8F30861E18D66625:
  - epoll_wait
  LTP_8FF73194288F8473:
  - access
  LTP_906135780505447D:
  - access
  LTP_911B97B972658989:
  - access
  LTP_919ABCA2598F53B5:
  - access
  LTP_921D4802D7690C64:
  - access
  LTP_9256D223D5EF4AF0:
  - flock
  LTP_9260E923CF8AA018:
  - access
  LTP_929B120944D8F805:
  - access
  LTP_93949494FBAD3568:
  - access
  LTP_94E36E221125BFAF:
  - access
  LTP_955ECE70D81CA226:
  - access
  LTP_96021AFB69E847F9:
  - access
  LTP_963EAEB0B41C7934:
  - fpathconf
  LTP_969C39F409BFD7AA:
  - access
  LTP_96B2A3E7AC7B2444:
  - fchmod
  LTP_96D205FACA0DD8DB:
  - access
  LTP_96F07DC5DDC8E018:
  - access
  LTP_97C442AC56780374:
  - access
  LTP_9866FB6F1F726CA0:
  - access
  LTP_986F211E7D45CAD7:
  - access
  LTP_98EC66149EE68933:
  - alarm
  LTP_99DF5C34778032E1:
  - chroot
  LTP_9A723EA0B1F0D1BE:
  - access
  LTP_9B3646398697EA64:
  - dup3
  LTP_9C9D222A34799D55:
  - access
  LTP_9CA9C6B61C3317A3:
  - accept
  LTP_9CDCD3C4BA6C2702:
  - access
  LTP_9F560A103CB6F910:
  - dup2
  LTP_9FE663EAF1F0ABCF:
  - fsconfig
  LTP_A00E343F4A556B3D:
  - capset
  LTP_A030561DFACE8C93:
  - finit_module
  LTP_A16555D2419FBCD4:
  - finit_module
  LTP_A17272D4FE0F040B:
  - access
  LTP_A1B6FBC6EF800331:
  - fchmod
  LTP_A1DEE046C0A10B18:
  - access
  LTP_A2A80201A4364230:
  - flock
  LTP_A30F7687D403407B:
  - access
  LTP_A4060315D2E047EE:
  - access
  LTP_A4733D4B2FEBE9A4:
  - access
  LTP_A500A46C4B998E74:
  - access
  LTP_A6B94E8A2A4D8853:
  - access
  LTP_A774FC10727E8ED2:
  - dup
  LTP_A9544B59EB6712D9:
  - access
  LTP_A9596E932167B3EF:
  - access
  LTP_A9DD0D461E032A07:
  - fsconfig
  LTP_AB48F262BBB2CC93:
  - access
  LTP_AC0FB73B4EE420EC:
  - access
  LTP_AC7D82691053FF4D:
  - fsconfig
  LTP_ACD12B8C0803E654:
  - epoll_wait
  LTP_ACF7A30AF3B10973:
  - execveat
  LTP_AD81218450587FA8:
  - access
  LTP_ADD30BEEC40E661F:
  - access
  LTP_ADEB5FE2DF97542A:
  - epoll_ctl
  LTP_AE3908C408304451:
  - copy_file_range
  LTP_AE4CE76865CD4D6D:
  - flock
  LTP_B1D822DF0057B4E0:
  - access
  LTP_B200AFD97E91C2CC:
  - access
  LTP_B3F848BCBCBAB559:
  - epoll_wait
  LTP_B4B9F07E1C1A3826:
  - fsconfig
  LTP_B4FD0E2B4B84F458:
  - fchmodat
  LTP_B53406D510ED4981:
  - access
  LTP_B5959FE5199E821F:
  - flock
  LTP_B6DAF13EF3143EBF:
  - access
  LTP_B7A341967DF2BD69:
  - alarm
  LTP_B7F51635806E7E59:
  - dup2
  LTP_B86CDF340A27A5B7:
  - fchmod
  LTP_B87A71DE5DE1260E:
  - copy_file_range
  LTP_B8EA21096E591EBB:
  - flock
  LTP_B90CB73F36B70C6F:
  - accept
  LTP_B9908D4015443661:
  - access
  LTP_B9CDD41A0DC2AFCC:
  - access
  LTP_BA03F1BD9B5F2BE2:
  - finit_module
  LTP_BA10984A4B0DE2C6:
  - access
  LTP_BA9A8FE901467960:
  - cachestat
  LTP_BAE8F852378DD9F4:
  - copy_file_range
  LTP_BC662075E3BAE807:
  - access
  LTP_BDA36F61423EEB3E:
  - dup2
  LTP_BE2E778739EF01D5:
  - access
  LTP_BF2428964ADD116F:
  - close
  LTP_BF679B7A7E60BCFD:
  - fpathconf
  LTP_C0577C0D678214DA:
  - access
  LTP_C071A7FFF929A2A5:
  - access
  LTP_C0AA45BC29F98A0E:
  - access
  LTP_C16D549555A00E55:
  - copy_file_range
  LTP_C1C67435FC56D878:
  - access
  LTP_C218D3CB0AD80D90:
  - cacheflush
  LTP_C2909AC2ECEDED94:
  - faccessat2
  LTP_C346EFF1233F7061:
  - mmap
  LTP_C37E693AB7AA5E28:
  - flistxattr
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
  LTP_C80C019BE3F47901:
  - alarm
  LTP_C8DAE34819E335F8:
  - access
  LTP_C994B56A41A71C1A:
  - access
  LTP_CA45A33676AD236D:
  - access
  LTP_CA80C3F10B65226D:
  - access
  LTP_CB31E19EE807FFDB:
  - access
  LTP_CBB1680336D53D2A:
  - epoll_ctl
  LTP_CBF4B6C8A1458A28:
  - close_range
  LTP_CC9037A76978B569:
  - copy_file_range
  LTP_CCC36F43E9463D3E:
  - fchdir
  LTP_CCDB1776DAA2C318:
  - access
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
  LTP_D0E32E5D27E643A9:
  - chroot
  LTP_D12172005842E2A5:
  - epoll_wait
  LTP_D1AADFC2F7C6F594:
  - capset
  LTP_D1B6112551D45B31:
  - alarm
  LTP_D1DAB36EB37FCA27:
  - fpathconf
  LTP_D1F469715ECC4195:
  - access
  LTP_D296A517F138A0C0:
  - dup2
  LTP_D2D67AB5E38A7000:
  - access
  LTP_D2F4BCF2263C56F5:
  - access
  LTP_D412A09DEDC43045:
  - access
  LTP_D4B433A3696803A8:
  - alarm
  LTP_D4D8A0FEAA2F6B09:
  - access
  LTP_D579FCFC71E6EB6A:
  - cacheflush
  LTP_D5D78F93265A1980:
  - fsconfig
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
  LTP_D75F86A534CB6E02:
  - epoll_wait
  LTP_D76652434EC85091:
  - access
  LTP_D77858597BCC1C13:
  - faccessat2
  LTP_D8B58CA743EBE711:
  - access
  LTP_DA10E351BC730D85:
  - access
  LTP_DA65D6C7A0E4ABBC:
  - finit_module
  LTP_DAA03BAD070DB1D6:
  - access
  LTP_DAA1F16D8A298E83:
  - access
  LTP_DB6066C00D231BA4:
  - copy_file_range
  LTP_DC9BC72148835FDC:
  - capget
  LTP_DCB33BB29D296843:
  - access
  LTP_DD9A41090E3D5A17:
  - access
  LTP_DE6F80C5EFE44A9D:
  - dup2
  LTP_DF1C4714B16B760E:
  - access
  LTP_E06D53042C10C99E:
  - capset
  LTP_E0B177A8B6FE4225:
  - access
  LTP_E0ED96B80FC3B6C9:
  - access
  LTP_E13B9C2C9645B841:
  - accept
  LTP_E2196C3F0F58862B:
  - copy_file_range
  LTP_E28B5BB57A450438:
  - access
  LTP_E2C3B68EDF07A753:
  - access
  LTP_E34945E3DE91022F:
  - access
  LTP_E3A3CF8B98E460BC:
  - access
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
  LTP_E5791B389C67677E:
  - access
  LTP_E5E50FB7BDD033D9:
  - access
  LTP_E6750A641272AF1B:
  - fsconfig
  LTP_E7435E0CBCA319E1:
  - epoll_create
  LTP_E8CF2AE0EC60602C:
  - epoll_wait
  LTP_EA5D1572B890F71E:
  - epoll_wait
  LTP_EB00EA74B30E438E:
  - access
  LTP_EB425D988F2F7604:
  - access
  LTP_EB7FFB63F4259214:
  - fchmodat
  LTP_EBCE1A2B8CE59ECE:
  - fsconfig
  LTP_EBD54180D0CAB16B:
  - chroot
  LTP_EBF0020C32AD44C8:
  - access
  LTP_EC19C6410BBE0467:
  - access
  LTP_EC1CA29BE6888A6B:
  - epoll_wait
  LTP_EC23768761E40E9F:
  - capset
  LTP_ED2BA909DF79625A:
  - dup
  LTP_ED36488372A175F5:
  - access
  LTP_ED3F2AE7E59E6F12:
  - access
  LTP_EE1518958A8F7CC1:
  - access
  LTP_EE7A979F212D6C0C:
  - chroot
  LTP_EE8E695CF61D6D8A:
  - dup2
  LTP_EEDED564522D8D2D:
  - faccessat2
  LTP_EF5C1F365208AD31:
  - access
  LTP_F04C2129F0253CC0:
  - fchmodat
  LTP_F1044C71B6626419:
  - accept
  LTP_F10E5286CF6CAC64:
  - flistxattr
  LTP_F1299BC5F92BF26E:
  - fchmod
  LTP_F13B0055458E603F:
  - finit_module
  LTP_F1DC44813DCA6A05:
  - close_range
  LTP_F202F3C3B02DEA0E:
  - access
  LTP_F3200B697F38DD16:
  - access
  LTP_F3418C5C403B91FC:
  - access
  LTP_F36F8C0CC1A6D840:
  - mmap
  LTP_F421E1E61753B72C:
  - fchmod
  LTP_F43EC0D01CCFD25A:
  - access
  LTP_F4DE81D703447628:
  - close_range
  LTP_F65E54AE96F20D41:
  - fchmodat2
  LTP_F66DDB5A0EBC5C9F:
  - fsconfig
  LTP_F6BB86F5DCC2FAC8:
  - access
  LTP_F70FC66A56FBD769:
  - access
  LTP_F7998813C90A7A08:
  - access
  LTP_F7B8EDE302D5D08A:
  - faccessat2
  LTP_F8CDD57D76C8FA6C:
  - access
  LTP_F9BF08369A08E5ED:
  - access
  LTP_FB047DBB72D78D19:
  - flock
  LTP_FC5B16AB3C53A744:
  - access
  LTP_FCA376B46A9873B0:
  - access
  LTP_FD1B65B0BCC88E0D:
  - mmap
  LTP_FDE0B30F1CFCAA4B:
  - fsconfig
  LTP_FEACDC300C3E1DD7:
  - mmap
  LTP_FF1A8A6101CEA37E:
  - fpathconf
  LTP_FF9C0F9669A39525:
  - chroot
static:
- check_id: STARRY_ACCESS_USER_POINTER
  rule_refs:
  - LTP_075318C437B76E06
  - LTP_0799FC60BADD2B18
  - LTP_38FB918826669241
  - LTP_58416E6747519699
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/stat.rs
  patterns:
  - label: pathname is loaded before resolution
    regex: let path = path\.nullable\(\)\.map\(vm_load_path_string\)\.transpose\(\)\?;[\s\S]*?let file
      = resolve_at\(dirfd, path\.as_deref\(\), flags\)\?;
    matched: true
    line: 71
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_CAPGET_ABI
  rule_refs:
  - LTP_208C833FF12217F5
  - LTP_5F1D35ACCEFD4971
  - LTP_827CE5CB448A411B
  result: pass
  path: os/StarryOS/kernel/src/syscall/task/ctl.rs
  patterns:
  - label: header pointer and V3 version are validated
    regex: fn validate_cap_header\([\s\S]*?header_ptr\.vm_read_uninit\(\)\?[\s\S]*?header\.version !=
      CAPABILITY_VERSION_3[\s\S]*?header_ptr\.vm_write\(header\)\?[\s\S]*?Err\(AxError::InvalidInput\)
    matched: true
    line: 69
  - label: capget copies both V3 words to userspace
    regex: pub fn sys_capget\([\s\S]*?validate_cap_header\(header\)\?[\s\S]*?cred_for_pid\(pid\)\?[\s\S]*?cap_data_from_cred\(&cred\)[\s\S]*?data\.vm_write\(cap_data\[0\]\)\?[\s\S]*?data\.add\(1\)\.vm_write\(cap_data\[1\]\)\?[\s\S]*?Ok\(0\)
    matched: true
    line: 135
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_CAPSET_ABI
  rule_refs:
  - LTP_6D86AFD541A61388
  - LTP_E06D53042C10C99E
  - LTP_EC23768761E40E9F
  result: pass
  path: os/StarryOS/kernel/src/syscall/task/ctl.rs
  patterns:
  - label: header and data pointers are validated before use
    regex: pub fn sys_capset\([\s\S]*?validate_cap_header\(header\)\?[\s\S]*?if data\.is_null\(\) \{[\s\S]*?Err\(AxError::BadAddress\)[\s\S]*?data\.vm_read_uninit\(\)\?[\s\S]*?data\.add\(1\)\.vm_read_uninit\(\)\?
    matched: true
    line: 160
  - label: capability subsets are enforced
    regex: if effective & !permitted != 0[\s\S]*?adds_permitted[\s\S]*?if adds_permitted != 0[\s\S]*?if
      may_expand[\s\S]*?adds_inheritable
    matched: true
    line: 187
  - label: validated capability state replaces current credentials
    regex: new\.cap_effective = effective;[\s\S]*?new\.cap_permitted = permitted;[\s\S]*?new\.cap_inheritable
      = inheritable;[\s\S]*?new\.sanitize_capabilities\(\);[\s\S]*?thread\.set_cred\(new\);[\s\S]*?Ok\(0\)
    matched: true
    line: 206
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_CLOSE_BAD_FD_ERRNO
  rule_refs:
  - LTP_09B39E9C9254ECB2
  - LTP_0CD17E662AFD2956
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
  - LTP_0CD17E662AFD2956
  result: pass
  path: os/StarryOS/kernel/src/file/mod.rs
  patterns:
  - label: close removes the descriptor from the current fd table
    regex: 'pub fn close_file_like\(fd: c_int\)[\s\S]*?FD_TABLE\.write\(\)\.remove\(fd as usize\)'
    matched: true
    line: 312
  - label: a removed descriptor succeeds and a missing descriptor is EBADF
    regex: 'pub fn close_file_like\(fd: c_int\)[\s\S]*?return Ok\(\(\)\);[\s\S]*?Err\(AxError::BadFileDescriptor\)'
    matched: true
    line: 312
  reason: all required patterns matched
  finding_ids: []
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
    line: 489
  - label: missing descriptors are skipped and completion returns zero
    regex: for fd in first\.\.=last\.min\(max_index as (?:i32|u32)\)[\s\S]*?if let Some\(f\) = fd_table\.remove\(fd
      as _\)[\s\S]*?Ok\(0\)
    matched: true
    line: 514
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
    line: 489
  - label: the maximum unsigned range is accepted and capped to open descriptors
    regex: pub fn sys_close_range\([\s\S]*?for fd in first\.\.=last\.min\(max_index as u32\)[\s\S]*?Ok\(0\)
    matched: true
    line: 489
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
    line: 489
  - label: unknown close_range flags are invalid
    regex: pub fn sys_close_range\([\s\S]*?CloseRangeFlags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?
    matched: true
    line: 489
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_CLOSE_SYSCALL
  rule_refs:
  - LTP_09B39E9C9254ECB2
  - LTP_0CD17E662AFD2956
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/fd_ops.rs
  patterns:
  - label: sys_close calls close_file_like and propagates errors
    regex: 'pub fn sys_close\(fd: c_int\)[\s\S]*?close_file_like\(fd\)\?;'
    matched: true
    line: 475
  - label: successful close returns zero
    regex: 'pub fn sys_close\(fd: c_int\)[\s\S]*?close_file_like\(fd\)\?;[\s\S]*?Ok\(0\)'
    matched: true
    line: 475
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_CONNECT_ADDRESS_VALIDATION
  rule_refs:
  - LTP_4C3A8A7664F22B7F
  - LTP_6AEB77CEC03D0E6E
  - LTP_74E00510F4C1B849
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
  - LTP_0FCE63CBC47F69DA
  - LTP_2F153EBAAD2A779C
  result: pass
  path: os/StarryOS/kernel/src/syscall/net/socket.rs
  patterns:
  - label: connect validates the fd before reading and normalizing the address
    regex: pub fn sys_connect\([\s\S]*?Socket::from_fd\(fd\)\?;[\s\S]*?SocketAddrEx::read_from_user\(addr,
      addrlen\)\?;
    matched: true
    line: 174
  - label: parsed addresses are passed to the socket and errors propagate except nonblocking progress
    regex: pub fn sys_connect\([\s\S]*?socket\.connect\(addr\)\.map_err\([\s\S]*?AxError::WouldBlock[\s\S]*?AxError::InProgress[\s\S]*?\?;[\s\S]*?Ok\(0\)
    matched: true
    line: 174
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_COPY_FILE_RANGE_CORE
  rule_refs:
  - LTP_09370275EF5F3065
  - LTP_6A2F1D2BB0EE8C22
  - LTP_7E1612F09CACE33D
  - LTP_AE3908C408304451
  - LTP_B87A71DE5DE1260E
  - LTP_BAE8F852378DD9F4
  - LTP_C16D549555A00E55
  - LTP_CC9037A76978B569
  - LTP_E2196C3F0F58862B
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
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/fd_ops.rs
  patterns:
  - label: dup2 same-fd validates the descriptor and otherwise delegates to dup3
    regex: 'pub fn sys_dup2\(old_fd: c_int, new_fd: c_int\)[\s\S]*?if old_fd == new_fd \{[\s\S]*?get_file_like\(new_fd\)\?;[\s\S]*?return
      Ok\(new_fd as _\);[\s\S]*?sys_dup3\(old_fd, new_fd, 0\)'
    matched: true
    line: 563
  - label: dup3 rejects unknown flags and equal descriptors
    regex: pub fn sys_dup3\([\s\S]*?Dup3Flags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?;[\s\S]*?if
      old_fd == new_fd \{[\s\S]*?Err\(AxError::InvalidInput\)
    matched: true
    line: 578
  - label: dup3 validates the old fd, replaces the target, and returns it
    regex: pub fn sys_dup3\([\s\S]*?\.get\(old_fd as _\)[\s\S]*?\.ok_or\(AxError::BadFileDescriptor\)\?;[\s\S]*?fd_table\.remove\(new_fd
      as _\)[\s\S]*?\.add_at\(new_fd as _, f\)[\s\S]*?Ok\(new_fd as _\)
    matched: true
    line: 578
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_DUP_BEHAVIOR
  rule_refs:
  - LTP_0EBD1214FC6BB6D5
  - LTP_311F7A773994720E
  - LTP_511185D6DE2A63A0
  - LTP_594FA5B54CA204E5
  - LTP_84DBE108A850E845
  - LTP_A774FC10727E8ED2
  - LTP_ED2BA909DF79625A
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/fd_ops.rs
  patterns:
  - label: dup_fd looks up the old descriptor and returns a newly allocated descriptor
    regex: 'fn dup_fd\(old_fd: c_int, cloexec: bool\)[\s\S]*?get_file_like\(old_fd\)\?;[\s\S]*?add_file_like\(f,
      cloexec\)\?;[\s\S]*?Ok\(new_fd as _\)'
    matched: true
    line: 532
  - label: sys_dup requests a non-CLOEXEC duplicate
    regex: 'pub fn sys_dup\(old_fd: c_int\)[\s\S]*?dup_fd\(old_fd, false\)'
    matched: true
    line: 557
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_EPOLL_CREATE
  rule_refs:
  - LTP_2D1E25BD679B3494
  - LTP_37F2ED2BA3175CC3
  - LTP_E7435E0CBCA319E1
  result: pass
  path: os/StarryOS/kernel/src/syscall/io_mpx/epoll.rs
  patterns:
  - label: nonpositive legacy sizes are invalid
    regex: 'pub fn sys_epoll_create\(size: i32\)[\s\S]*?if size <= 0 \{[\s\S]*?Err\(AxError::InvalidInput\)'
    matched: true
    line: 114
  - label: positive legacy sizes create an epoll descriptor without flags
    regex: 'pub fn sys_epoll_create\(size: i32\)[\s\S]*?sys_epoll_create1\(0\)'
    matched: true
    line: 114
  - label: epoll_create1 allocates and returns a file descriptor
    regex: pub fn sys_epoll_create1\([\s\S]*?Epoll::new\(\)[\s\S]*?\.add_to_fd_table\([\s\S]*?\.map\(\|fd\|
      fd as isize\)
    matched: true
    line: 104
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_EPOLL_CREATE1_FLAGS
  rule_refs:
  - LTP_5D8D2B3BEDA79604
  - LTP_89745BB32E6D4D02
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
  - LTP_22E98D1569DAB493
  - LTP_6FFB17DB762F3167
  - LTP_83709E56D6285F71
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
  - LTP_468FC84DEAB0BCB8
  - LTP_4953FAD330ADE150
  - LTP_61778C450B602081
  - LTP_8ADB82F00C61D567
  result: pass
  path: os/StarryOS/kernel/src/file/epoll.rs
  patterns:
  - label: monitored descriptors are resolved through the fd table
    regex: 'fn new\(fd: i32\)[\s\S]*?let file = get_file_like\(fd\)\?;'
    matched: true
    line: 130
  - label: duplicate registrations return AlreadyExists
    regex: pub fn add\([\s\S]*?guard\.contains_key\(&key\)[\s\S]*?return Err\(AxError::AlreadyExists\);
    matched: true
    line: 501
  - label: modifying a missing interest returns NotFound
    regex: pub fn modify\([\s\S]*?guard\.get_mut\(&key\)\.ok_or\(AxError::NotFound\)\?
    matched: true
    line: 537
  - label: deleting a missing interest returns NotFound
    regex: pub fn delete\([\s\S]*?\.remove\(&key\)[\s\S]*?\.ok_or\(AxError::NotFound\)\?
    matched: true
    line: 577
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_EPOLL_FACCESS_ERRNO
  rule_refs:
  - LTP_0FEC274199CCD0A0
  - LTP_18ECD15E5451228D
  - LTP_1ADEBF230DD2C214
  - LTP_22E98D1569DAB493
  - LTP_468FC84DEAB0BCB8
  - LTP_4953FAD330ADE150
  - LTP_4BCFF61005DC2E9A
  - LTP_4C1F446C9C520B36
  - LTP_4D51F55F25C6F2A3
  - LTP_5D8D2B3BEDA79604
  - LTP_61778C450B602081
  - LTP_66C670178B06E9F3
  - LTP_6885CE6A54F7716E
  - LTP_6FFB17DB762F3167
  - LTP_77AA3EAF2AD0C07A
  - LTP_83709E56D6285F71
  - LTP_89745BB32E6D4D02
  - LTP_8ADB82F00C61D567
  - LTP_8F30861E18D66625
  - LTP_ACF7A30AF3B10973
  - LTP_EA5D1572B890F71E
  - LTP_EC1CA29BE6888A6B
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
  - LTP_8F30861E18D66625
  - LTP_EC1CA29BE6888A6B
  result: pass
  path: os/StarryOS/kernel/src/file/mod.rs
  patterns:
  - label: absent descriptors return BadFileDescriptor
    regex: 'pub fn get_file_like\(fd: c_int\)[\s\S]*?\.ok_or\(AxError::BadFileDescriptor\)'
    matched: true
    line: 280
  - label: a descriptor of the wrong concrete type returns InvalidInput
    regex: 'fn from_fd\(fd: c_int\)[\s\S]*?get_file_like\(fd\)\?[\s\S]*?\.downcast_arc\(\)[\s\S]*?\.map_err\(\|_\|
      AxError::InvalidInput\)'
    matched: true
    line: 250
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
- check_id: STARRY_EPOLL_WAIT_VALIDATION
  rule_refs:
  - LTP_18ECD15E5451228D
  - LTP_1ADEBF230DD2C214
  - LTP_EA5D1572B890F71E
  result: pass
  path: os/StarryOS/kernel/src/syscall/io_mpx/epoll.rs
  patterns:
  - label: nonpositive maximum event counts are invalid
    regex: fn do_epoll_wait\([\s\S]*?if maxevents <= 0 \{[\s\S]*?return Err\(AxError::InvalidInput\);
    matched: true
    line: 176
  - label: null and inaccessible event buffers are rejected
    regex: fn do_epoll_wait\([\s\S]*?if events\.is_null\(\) \{[\s\S]*?Err\(AxError::BadAddress\)[\s\S]*?check_epoll_events_access\(events,
      maxevents\)\?
    matched: true
    line: 176
  - label: event buffer access is checked for the complete output slice
    regex: fn check_epoll_events_access\([\s\S]*?checked_mul\(size_of::<epoll_event>\(\)\)[\s\S]*?check_access\(start,
      len\)\?
    matched: true
    line: 36
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ERRNO_TRANSLATION
  rule_refs:
  - LTP_09B39E9C9254ECB2
  - LTP_0CD17E662AFD2956
  - LTP_36C99C10CD38F8DB
  - LTP_45439D8F2BAB0832
  - LTP_51E295101A9F4411
  - LTP_52BAFC01DEA6E172
  - LTP_791DEA825D66980B
  - LTP_C346EFF1233F7061
  - LTP_F36F8C0CC1A6D840
  - LTP_FD1B65B0BCC88E0D
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
  - LTP_5109EDF645F51D7E
  - LTP_77AA3EAF2AD0C07A
  - LTP_ACF7A30AF3B10973
  - LTP_EEDED564522D8D2D
  result: pass
  path: os/StarryOS/kernel/src/file/fs.rs
  patterns:
  - label: empty paths require AT_EMPTY_PATH and resolve the supplied descriptor
    regex: Some\(""\) \| None =>[\s\S]*?flags & AT_EMPTY_PATH == 0[\s\S]*?get_file_like\(dirfd\)\?
    matched: true
    line: 61
  - label: absolute paths ignore dirfd while relative paths resolve through it
    regex: Some\(path\) =>[\s\S]*?if path\.starts_with\('/'\) \{[\s\S]*?AT_FDCWD[\s\S]*?with_fs\(dirfd,
    matched: true
    line: 79
  - label: relative non-directory descriptors return NotADirectory
    regex: 'impl FileLike for Directory[\s\S]*?fn from_fd\(fd: c_int\)[\s\S]*?get_file_like\(fd\)\?[\s\S]*?AxError::NotADirectory'
    matched: true
    line: 312
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_EXECVEAT_VALIDATION
  rule_refs:
  - LTP_0FEC274199CCD0A0
  - LTP_ACF7A30AF3B10973
  result: pass
  path: os/StarryOS/kernel/src/syscall/task/execve.rs
  patterns:
  - label: unknown execveat flags are invalid
    regex: pub fn sys_execveat\([\s\S]*?if flags & !\(AT_EMPTY_PATH \| AT_SYMLINK_NOFOLLOW\) != 0 \{[\s\S]*?Err\(AxError::InvalidInput\)
    matched: true
    line: 46
  - label: the pathname is loaded and resolved through resolve_at
    regex: pub fn sys_execveat\([\s\S]*?vm_load_string\(path\)\?;[\s\S]*?resolve_at\(dirfd, Some\(path\.as_str\(\)\),
      flags\)\?
    matched: true
    line: 46
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FACCESSAT2_VALIDATION
  rule_refs:
  - LTP_4BCFF61005DC2E9A
  - LTP_4D51F55F25C6F2A3
  - LTP_6885CE6A54F7716E
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/stat.rs
  patterns:
  - label: only Linux access mode and faccessat2 flag bits are accepted
    regex: const FACCESSAT2_VALID_FLAGS:[\s\S]*?const FACCESSAT2_VALID_MODE:[\s\S]*?mode & !FACCESSAT2_VALID_MODE
      != 0 \|\| flags & !FACCESSAT2_VALID_FLAGS != 0[\s\S]*?Err\(AxError::InvalidInput\)
    matched: true
    line: 151
  - label: the optional user path is copied before resolve_at
    regex: pub fn sys_faccessat2\([\s\S]*?path\.nullable\(\)\.map\(vm_load_path_string\)\.transpose\(\)\?;[\s\S]*?resolve_at\(dirfd,
      path\.as_deref\(\), flags\)\?
    matched: true
    line: 147
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FCHDIR_CORE
  rule_refs:
  - LTP_17B7A9460939622A
  - LTP_CCC36F43E9463D3E
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/ctl.rs
  patterns:
  - label: fchdir resolves the descriptor through with_fs
    regex: 'pub fn sys_fchdir\(dirfd: i32\)[\s\S]*?with_fs\(dirfd,[\s\S]*?current_dir\(\)\.clone\(\)'
    matched: true
    line: 96
  - label: fchdir propagates cwd update errors
    regex: 'pub fn sys_fchdir\(dirfd: i32\)[\s\S]*?set_current_dir\(entry\)\?;'
    matched: true
    line: 96
  - label: successful fchdir returns zero
    regex: 'pub fn sys_fchdir\(dirfd: i32\)[\s\S]*?set_current_dir\(entry\)\?;[\s\S]*?Ok\(0\)'
    matched: true
    line: 96
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
    line: 312
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FCHMODAT_FLAG_VALIDATION
  rule_refs:
  - LTP_628FD2848734A58A
  - LTP_8BD2C43CB1EC6794
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/ctl.rs
  patterns:
  - label: supported fchmodat flags are explicitly bounded
    regex: 'const FCHMODAT_VALID_FLAGS: u32 = AT_EMPTY_PATH \| AT_SYMLINK_NOFOLLOW;'
    matched: true
    line: 582
  - label: unknown fchmodat flags return InvalidInput
    regex: if flags & !FCHMODAT_VALID_FLAGS != 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}
    matched: true
    line: 583
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FD_TABLE_LOOKUP_ALLOCATION
  rule_refs:
  - LTP_0EBD1214FC6BB6D5
  - LTP_311F7A773994720E
  - LTP_511185D6DE2A63A0
  - LTP_594FA5B54CA204E5
  - LTP_84DBE108A850E845
  - LTP_A774FC10727E8ED2
  - LTP_ED2BA909DF79625A
  result: pass
  path: os/StarryOS/kernel/src/file/mod.rs
  patterns:
  - label: missing descriptors produce BadFileDescriptor
    regex: 'pub fn get_file_like\(fd: c_int\)[\s\S]*?FD_TABLE[\s\S]*?\.get\(fd as usize\)[\s\S]*?\.ok_or\(AxError::BadFileDescriptor\)'
    matched: true
    line: 280
  - label: allocation enforces the current nofile limit as TooManyOpenFiles
    regex: pub fn add_file_like\([\s\S]*?RLIMIT_NOFILE[\s\S]*?if table\.count\(\) as u64 >= max_nofile
      \{[\s\S]*?Err\(AxError::TooManyOpenFiles\)
    matched: true
    line: 301
  - label: successful allocation returns the new descriptor
    regex: pub fn add_file_like\([\s\S]*?Ok\(table\.add\(fd\)\.map_err\(\|_\| AxError::TooManyOpenFiles\)\?
      as c_int\)
    matched: true
    line: 301
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_FINIT_MODULE_FLAG_VALIDATION
  rule_refs:
  - LTP_DA65D6C7A0E4ABBC
  result: fail
  path: os/StarryOS/kernel/src/syscall/kmod.rs
  patterns:
  - label: finit_module names and inspects its flags argument
    regex: 'pub fn sys_finit_module\(module_fd: i32, param_ptr: \*const u8, flags: u32\)'
    matched: false
    line: null
  - label: unsupported nonzero flags return InvalidInput
    regex: pub fn sys_finit_module\([\s\S]*?if flags != 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}
    matched: false
    line: null
  reason: one or more required patterns did not match
  finding_ids:
  - finding-finit-module-ltp-da65d6c7a0e4abbc-840b33b63dfd
- check_id: STARRY_MMAP_ACCESS
  rule_refs:
  - LTP_36C99C10CD38F8DB
  - LTP_45439D8F2BAB0832
  - LTP_52BAFC01DEA6E172
  - LTP_C346EFF1233F7061
  - LTP_F36F8C0CC1A6D840
  - LTP_FD1B65B0BCC88E0D
  result: pass
  path: os/StarryOS/kernel/src/syscall/mm/mmap.rs
  patterns:
  - label: all regular file mappings require fd read access
    regex: if needs_file_mmap_checks \{[\s\S]*?if !flags\.contains\(FileFlags::READ\) \{[\s\S]*?return
      Err\(AxError::PermissionDenied\);
    matched: true
    line: 246
  - label: shared writable mappings additionally require fd write access
    regex: matches!\(map_type, MmapFlags::SHARED\)[\s\S]*?permission_flags\.contains\(MmapProt::WRITE\)[\s\S]*?if
      !flags\.contains\(FileFlags::WRITE\) \{[\s\S]*?return Err\(AxError::PermissionDenied\);
    matched: true
    line: 214
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_MMAP_ARGUMENTS
  rule_refs:
  - LTP_51E295101A9F4411
  - LTP_FEACDC300C3E1DD7
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
- check_id: STARRY_ROUND2_ERRNO_TRANSLATION
  rule_refs:
  - LTP_098AFE0E8E10B0EF
  - LTP_0FCE63CBC47F69DA
  - LTP_2F153EBAAD2A779C
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
- check_id: STARRY_SOCKET_FD_VALIDATION
  rule_refs:
  - LTP_0FCE63CBC47F69DA
  - LTP_2F153EBAAD2A779C
  result: pass
  path: os/StarryOS/kernel/src/file/net.rs
  patterns:
  - label: Socket from_fd propagates fd lookup and maps type mismatch to NotASocket
    regex: 'fn from_fd\(fd: c_int\)[\s\S]*?get_file_like\(fd\)\?[\s\S]*?\.downcast_arc\(\)[\s\S]*?\.map_err\(\|_\|
      AxError::NotASocket\)'
    matched: true
    line: 374
  reason: all required patterns matched
  finding_ids: []
dynamic: []
counts:
  static_pass: 37
  static_fail: 1
  static_error: 0
  dynamic_pass: 0
  dynamic_fail: 0
  dynamic_skipped: 0
  dynamic_not_run: 0
  findings: 1
  blockers: 0
  new_findings: 1
  carried_findings: 0
  revalidated_findings: 0
  needs_revalidation: 0
blockers: []
finding_ids:
- finding-finit-module-ltp-da65d6c7a0e4abbc-840b33b63dfd
finding_versions:
  finding-finit-module-ltp-da65d6c7a0e4abbc-840b33b63dfd:
    id: finding-finit-module-ltp-da65d6c7a0e4abbc-840b33b63dfd
    generated_at_utc: '2026-07-16T03:18:47.170987Z'
    content_hash: sha256:0355fb32ae0140317edf868035c399ddafeac7df32fb09ba3c9097de76015473
new_finding_ids:
- finding-finit-module-ltp-da65d6c7a0e4abbc-840b33b63dfd
carried_finding_ids: []
revalidated_finding_ids: []
needs_revalidation_finding_ids: []
historical_regression_scope:
  rules: []
  static_checks: []
  dynamic_tests: []
historical_regression_unresolved: {}
content_hash: sha256:7dd7c1457822fc616b4875b5f7cf831ede4d0d1c8e1394717df1a7b19b71949b
```
</details>
