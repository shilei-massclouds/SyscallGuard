# Starry 合规检查报告

## 本轮结论

- 状态：`completed`
- 静态检查：pass 13、fail 2、error 0
- 动态测试：pass 0、fail 0、skipped 0、not_run 0
- confirmed finding：2
- 环境或执行 blocker：0（不视为实现缺口）

## 静态检查

### `STARRY_CLOSE_RANGE_SWEEP`

- 类型：`static`
- 关联 syscall：`close_range`
- 通用规则：`LTP_76BFF56F735A0074`、`LTP_F4DE81D703447628`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_close_range\([\s\S]*?for fd in first\.\.=last\.min\(max_index as i32\)`：matched=`true`，第 455 行
  - `for fd in first\.\.=last\.min\(max_index as i32\)[\s\S]*?if let Some\(f\) = fd_table\.remove\(fd as _\)[\s\S]*?Ok\(0\)`：matched=`true`，第 473 行
- finding：—

### `STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS`

- 类型：`static`
- 关联 syscall：`close_range`
- 通用规则：`LTP_425E5A3502541DE8`
- 结果：`fail`
- 原因：one or more required patterns did not match
- pattern 证据：

  - `pub fn sys_close_range\(first: u32, last: u32, flags: u32\)`：matched=`false`，未匹配
  - `pub fn sys_close_range\([\s\S]*?for fd in first\.\.=last\.min\(max_index as u32\)[\s\S]*?Ok\(0\)`：matched=`false`，未匹配
- finding：`finding-close-range-ltp-425e5a3502541de8-041c7ef6f327`

### `STARRY_CLOSE_RANGE_VALIDATION`

- 类型：`static`
- 关联 syscall：`close_range`
- 通用规则：`LTP_31D9D767D6888DDA`、`LTP_CBF4B6C8A1458A28`、`LTP_F1DC44813DCA6A05`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_close_range\([\s\S]*?if first < 0 \\|\\| last < first \{[\s\S]*?return Err\(AxError::InvalidInput\);`：matched=`true`，第 455 行
  - `pub fn sys_close_range\([\s\S]*?CloseRangeFlags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?`：matched=`true`，第 455 行
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
- 通用规则：`LTP_0FCE63CBC47F69DA`、`LTP_2F153EBAAD2A779C`、`LTP_4C3A8A7664F22B7F`、`LTP_6AEB77CEC03D0E6E`、`LTP_74E00510F4C1B849`
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
- 结果：`fail`
- 原因：one or more required patterns did not match
- pattern 证据：

  - `pub fn sys_copy_file_range\([\s\S]*?if len > isize::MAX as usize \{[\s\S]*?return Err\(AxError::from\(LinuxError::EOVERFLOW\)\);`：matched=`false`，未匹配
- finding：`finding-copy-file-range-ltp-74bb3f96cba52d02-041c7ef6f327`

### `STARRY_DUP2_DUP3_BEHAVIOR`

- 类型：`static`
- 关联 syscall：`dup2`、`dup3`
- 通用规则：`LTP_098AFE0E8E10B0EF`、`LTP_1726C16756E9651C`、`LTP_37C625BD7D7C5F1D`、`LTP_3A7B17AF231D4158`、`LTP_4F02ACC6E2F6B094`、`LTP_75D52C5E9C93B6D7`、`LTP_9B3646398697EA64`、`LTP_9F560A103CB6F910`、`LTP_B7F51635806E7E59`、`LTP_BDA36F61423EEB3E`、`LTP_D296A517F138A0C0`、`LTP_EE8E695CF61D6D8A`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_dup2\(old_fd: c_int, new_fd: c_int\)[\s\S]*?if old_fd == new_fd \{[\s\S]*?get_file_like\(new_fd\)\?;[\s\S]*?return Ok\(new_fd as _\);[\s\S]*?sys_dup3\(old_fd, new_fd, 0\)`：matched=`true`，第 518 行
  - `pub fn sys_dup3\([\s\S]*?Dup3Flags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?;[\s\S]*?if old_fd == new_fd \{[\s\S]*?Err\(AxError::InvalidInput\)`：matched=`true`，第 533 行
  - `pub fn sys_dup3\([\s\S]*?\.get\(old_fd as _\)[\s\S]*?\.ok_or\(AxError::BadFileDescriptor\)\?;[\s\S]*?fd_table\.remove\(new_fd as _\)[\s\S]*?\.add_at\(new_fd as _, f\)[\s\S]*?Ok\(new_fd as _\)`：matched=`true`，第 533 行
- finding：—

### `STARRY_DUP_BEHAVIOR`

- 类型：`static`
- 关联 syscall：`dup`
- 通用规则：`LTP_0EBD1214FC6BB6D5`、`LTP_311F7A773994720E`、`LTP_511185D6DE2A63A0`、`LTP_594FA5B54CA204E5`、`LTP_84DBE108A850E845`、`LTP_A774FC10727E8ED2`、`LTP_ED2BA909DF79625A`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `fn dup_fd\(old_fd: c_int, cloexec: bool\)[\s\S]*?get_file_like\(old_fd\)\?;[\s\S]*?add_file_like\(f, cloexec\)\?;[\s\S]*?Ok\(new_fd as _\)`：matched=`true`，第 487 行
  - `pub fn sys_dup\(old_fd: c_int\)[\s\S]*?dup_fd\(old_fd, false\)`：matched=`true`，第 512 行
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

### `STARRY_FD_TABLE_LOOKUP_ALLOCATION`

- 类型：`static`
- 关联 syscall：`dup`
- 通用规则：`LTP_0EBD1214FC6BB6D5`、`LTP_311F7A773994720E`、`LTP_511185D6DE2A63A0`、`LTP_594FA5B54CA204E5`、`LTP_84DBE108A850E845`、`LTP_A774FC10727E8ED2`、`LTP_ED2BA909DF79625A`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn get_file_like\(fd: c_int\)[\s\S]*?FD_TABLE[\s\S]*?\.get\(fd as usize\)[\s\S]*?\.ok_or\(AxError::BadFileDescriptor\)`：matched=`true`，第 275 行
  - `pub fn add_file_like\([\s\S]*?RLIMIT_NOFILE[\s\S]*?if table\.count\(\) as u64 >= max_nofile \{[\s\S]*?Err\(AxError::TooManyOpenFiles\)`：matched=`true`，第 296 行
  - `pub fn add_file_like\([\s\S]*?Ok\(table\.add\(fd\)\.map_err\(\\|_\\| AxError::TooManyOpenFiles\)\? as c_int\)`：matched=`true`，第 296 行
- finding：—

### `STARRY_ROUND2_CLOSE_FD_TABLE`

- 类型：`static`
- 关联 syscall：`close`
- 通用规则：`LTP_2BDE60C0E64B4DC8`、`LTP_BF2428964ADD116F`、`LTP_E520E500AB3AE851`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn close_file_like\(fd: c_int\)[\s\S]*?FD_TABLE\.write\(\)\.remove\(fd as usize\)[\s\S]*?if let Some\(f\) = removed[\s\S]*?return Ok\(\(\)\);`：matched=`true`，第 307 行
  - `pub fn close_file_like\(fd: c_int\)[\s\S]*?Err\(AxError::BadFileDescriptor\)`：matched=`true`，第 307 行
- finding：—

### `STARRY_ROUND2_CLOSE_SYSCALL`

- 类型：`static`
- 关联 syscall：`close`
- 通用规则：`LTP_2BDE60C0E64B4DC8`、`LTP_BF2428964ADD116F`、`LTP_E520E500AB3AE851`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_close\(fd: c_int\)[\s\S]*?close_file_like\(fd\)\?;[\s\S]*?Ok\(0\)`：matched=`true`，第 441 行
- finding：—

### `STARRY_ROUND2_ERRNO_TRANSLATION`

- 类型：`static`
- 关联 syscall：`close_range`、`connect`、`copy_file_range`、`dup`、`dup2`、`dup3`、`epoll_create`
- 通用规则：`LTP_09370275EF5F3065`、`LTP_098AFE0E8E10B0EF`、`LTP_0EBD1214FC6BB6D5`、`LTP_0FCE63CBC47F69DA`、`LTP_2D1E25BD679B3494`、`LTP_2F153EBAAD2A779C`、`LTP_311F7A773994720E`、`LTP_31D9D767D6888DDA`、`LTP_37C625BD7D7C5F1D`、`LTP_37F2ED2BA3175CC3`、`LTP_4C3A8A7664F22B7F`、`LTP_4F02ACC6E2F6B094`、`LTP_511185D6DE2A63A0`、`LTP_6A2F1D2BB0EE8C22`、`LTP_74E00510F4C1B849`、`LTP_75D52C5E9C93B6D7`、`LTP_7E1612F09CACE33D`、`LTP_9B3646398697EA64`、`LTP_9F560A103CB6F910`、`LTP_AE3908C408304451`、`LTP_B87A71DE5DE1260E`、`LTP_BAE8F852378DD9F4`、`LTP_BDA36F61423EEB3E`、`LTP_C16D549555A00E55`、`LTP_CBF4B6C8A1458A28`、`LTP_CC9037A76978B569`、`LTP_D296A517F138A0C0`、`LTP_E2196C3F0F58862B`、`LTP_F1DC44813DCA6A05`
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

  - `fn from_fd\(fd: c_int\)[\s\S]*?get_file_like\(fd\)\?[\s\S]*?\.downcast_arc\(\)[\s\S]*?\.map_err\(\\|_\\| AxError::NotASocket\)`：matched=`true`，第 358 行
- finding：—

## 动态测试

本轮没有动态测试。

<details>
<summary>机器可读元数据</summary>

<!-- syscallguard-metadata -->
```yaml
schema_version: 1
kind: syscallguard_check_report
report_id: check-20260715t065305z-3b1566ec
status: completed
generated_at_utc: '2026-07-15T06:53:06.785885Z'
mapping_report_id: mapping-20260715t052700z-0fcdb851
mapping_report_version:
  id: mapping-20260715t052700z-0fcdb851
  generated_at_utc: '2026-07-15T05:39:36.212938Z'
  content_hash: sha256:8a5745466c92bd4a246c9e9c85626ea8cd305ba99ca86d929eb6635a403642d0
target:
  target_id: starry
  repository: /home/cloud/gitLinux/tgoskits
  repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
  revision: HEAD
  worktree_root: /tmp/syscallguard-worktrees
  descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
  snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
input_hash: sha256:ac8e2bdfcfc27c6cd435c6ddc9c624cb3725d06ac4ef2c40c49545d1d90a5244
entity_hashes:
  rules:
    LTP_09370275EF5F3065: sha256:09370275ef5f3065d6f3ea10b7288a1ce0668fd80cc67a7d32a6f3b3069149f6
    LTP_098AFE0E8E10B0EF: sha256:098afe0e8e10b0efa6872ee3d2ece3674b519943b59189a2758d8ab31b06ab26
    LTP_0EBD1214FC6BB6D5: sha256:0ebd1214fc6bb6d5e224e50177509f565c7be9ba6ad0d4842779e564b71dedbb
    LTP_0FCE63CBC47F69DA: sha256:0fce63cbc47f69da5e2da3272c04cf9386103a75c442cf8614d29166e37f3fbb
    LTP_1726C16756E9651C: sha256:1726c16756e9651c8be282bf1cdf5c30a283e32aa200934084e3c42a2aee9ff9
    LTP_2BDE60C0E64B4DC8: sha256:2bde60c0e64b4dc8fc4b1e23c70973364d891d517c1f8020f709fabec59e6d0f
    LTP_2D1E25BD679B3494: sha256:2d1e25bd679b349425ebcfa9dd820bb8bc4de40949cd671adc32204c68864bbc
    LTP_2F153EBAAD2A779C: sha256:2f153ebaad2a779c607faa895cdd3493a982348174a10df8a80375ab6dd5e426
    LTP_311F7A773994720E: sha256:311f7a773994720e7cac8cd3d2b12c6938f7c13b7a4eff6dbcfe843e466448ac
    LTP_31D9D767D6888DDA: sha256:31d9d767d6888ddaf3c03f24abe0bc874e9932a546e4cdd283ecad199e6bcc1a
    LTP_37C625BD7D7C5F1D: sha256:37c625bd7d7c5f1db42b7cacc49b4964844f0c2f977ad1a74c3960da0d662932
    LTP_37F2ED2BA3175CC3: sha256:37f2ed2ba3175cc394b1338888db3f207e809f7e36f789587873dc7921e85edd
    LTP_3A7B17AF231D4158: sha256:3a7b17af231d4158b2c4508e92a25435b89a569164e6dfdabc216b48e1afec9f
    LTP_425E5A3502541DE8: sha256:425e5a3502541de863d8b8e88eafb95db2f8d8e1f9cb88a32d8b3124950395b2
    LTP_4C3A8A7664F22B7F: sha256:4c3a8a7664f22b7f2983c449e5c15d82b53d634db19f0a87e67849d4feb2fb77
    LTP_4F02ACC6E2F6B094: sha256:4f02acc6e2f6b094f06413684c004106e4c18d8f654cbb8b231de56e60aba90c
    LTP_511185D6DE2A63A0: sha256:511185d6de2a63a045d2f5f65babdf4c25b4066ece863b9f121419045563d4c9
    LTP_594FA5B54CA204E5: sha256:594fa5b54ca204e5062358a745af4921e86e002d54071b19f1650a69d2d468f7
    LTP_6A2F1D2BB0EE8C22: sha256:6a2f1d2bb0ee8c22d0970af42c645ba4f74a3cfe1a4748f4c47934666e135cfc
    LTP_6AEB77CEC03D0E6E: sha256:6aeb77cec03d0e6eaa956bea440fe8e71843fa521eafcf9611595dee8394b4bb
    LTP_74BB3F96CBA52D02: sha256:74bb3f96cba52d02850ad3c5e54c87acf278ce51290c99d5ae29da583be9ba38
    LTP_74E00510F4C1B849: sha256:74e00510f4c1b849cf8495790f1acd5cf1dc690a2ffcef67fc897e0c910fed22
    LTP_75D52C5E9C93B6D7: sha256:75d52c5e9c93b6d7989e3392a132ca3a319f4419c2f678533dc80d000c4891cd
    LTP_76BFF56F735A0074: sha256:76bff56f735a0074d725ee7dab337c42b7daf23d2ca44135affba4b983676aa8
    LTP_7E1612F09CACE33D: sha256:7e1612f09cace33d1e08ea245c28317ff95a538558b1d15dc9cd9e6c8dd2eb09
    LTP_84DBE108A850E845: sha256:84dbe108a850e845bf4a3cfc65c984525f06a85bcf44e616283b5ef4e16bb451
    LTP_9B3646398697EA64: sha256:9b3646398697ea6481b4201006e677123cd226bb81910f45b6fa558aaa810832
    LTP_9F560A103CB6F910: sha256:9f560a103cb6f910cc2b8fb141c7de076accd6a913e920715328e9facdfb18db
    LTP_A774FC10727E8ED2: sha256:a774fc10727e8ed282a01bc787e12bd54a0d81a756fc45037304c5906dadb2ff
    LTP_AE3908C408304451: sha256:ae3908c40830445120c2543a341389434b0eb8a4703f9666a62f96c38d9265e6
    LTP_B7F51635806E7E59: sha256:b7f51635806e7e596b7f6a1baf152d74ca1d365a9bdfc6d3f34984ac1908632d
    LTP_B87A71DE5DE1260E: sha256:b87a71de5de1260eeff71a5a683d9dea4fdc6e019dc8875ec98549865ba352ad
    LTP_BAE8F852378DD9F4: sha256:bae8f852378dd9f45a95e9fa5f5d957ef4f6efa3a462803119cc93500569bac0
    LTP_BDA36F61423EEB3E: sha256:bda36f61423eeb3e616d764edd458663817800e2f3db3adfae687bd17f6c2764
    LTP_BF2428964ADD116F: sha256:bf2428964add116f793723626820cf1b363a819d6e38ba6d31d9832e4ab1b2c0
    LTP_C16D549555A00E55: sha256:c16d549555a00e55b3199db30fcc866aeac70c8911afbcc47053c09ffa2a5b85
    LTP_CBF4B6C8A1458A28: sha256:cbf4b6c8a1458a2885c6c847b47ca93098a06580fc5fdfc3a1e483b9dab01ac4
    LTP_CC9037A76978B569: sha256:cc9037a76978b569fcf3e91e91771dc63c6a8cf1479d9f5c6e079b8ef0e91e4f
    LTP_D296A517F138A0C0: sha256:d296a517f138a0c09a3c71729b93607cfff1709b21125573bc2ad30b48302584
    LTP_E2196C3F0F58862B: sha256:e2196c3f0f58862b9dfeb182337b8bdf6ab3964ad73867128bb0853431dc7dbe
    LTP_E520E500AB3AE851: sha256:e520e500ab3ae8512756eb4a69fdef5de2701520040c400ce896ec773f4ab472
    LTP_E7435E0CBCA319E1: sha256:e7435e0cbca319e18c1459e2f9187003681d326f400fc6d00b47df912010faef
    LTP_ED2BA909DF79625A: sha256:ed2ba909df79625a7857c363efc0303c51fef469ee87970e6b322004f28779a5
    LTP_EE8E695CF61D6D8A: sha256:ee8e695cf61d6d8aa981eb6e30bf3a8a53c8e8a4ad435ff362bbd78971d17088
    LTP_F1DC44813DCA6A05: sha256:f1dc44813dca6a05d2fb0697718f8ed1da8d8b033d2c49bd0124284321f6ffd4
    LTP_F4DE81D703447628: sha256:f4de81d70344762893139769a2724588ddb7213c4667529ce501948b3b6b43c5
  static_checks:
    STARRY_CLOSE_RANGE_SWEEP: sha256:e930378c3b8c61c971d770a190b93b332ad822cc7a18c4372bd5b28dc24549c8
    STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS: sha256:72f0ccfc42dbced9e73e1f1a0190437ce60275d7bc1e7c187f8c9a5d1c4d2660
    STARRY_CLOSE_RANGE_VALIDATION: sha256:f66999e179d22a424c8a9775b216e494d96009491c1d0cee1c8ae10dd11ab221
    STARRY_CONNECT_ADDRESS_VALIDATION: sha256:f12594e38c23899fa45d721c0c0bdaf7ef6184d8b987093528e94001d952b4ce
    STARRY_CONNECT_ENTRY: sha256:917822d39de2c61608947b6f1489f5ffd3d77c0a02683fef4bf53b8c31c7e249
    STARRY_COPY_FILE_RANGE_CORE: sha256:87bbe450c3fed6eedf4989a90b546915add17c1354c4f74f14c87253ecf97950
    STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO: sha256:6762073d1ceebfed08c172e40495ac3d2d484296c43a114b1477042dc051b87f
    STARRY_DUP2_DUP3_BEHAVIOR: sha256:a150c80f2f30799a8d98957b5f049fe697e2ff990de192a833f37725965929ae
    STARRY_DUP_BEHAVIOR: sha256:57cddc0d3a6603566933f41a1c11f23481660361c88964e7cd33461ff3864e8d
    STARRY_EPOLL_CREATE: sha256:94f880e5cad41b9a599f96fce2042b830d0cf590a4b7ce2774536b1f4b5946f2
    STARRY_FD_TABLE_LOOKUP_ALLOCATION: sha256:a4545e2b6d4f0347d731939456dac417be7c0f81fb889cef52bc44c37a3ebddf
    STARRY_ROUND2_CLOSE_FD_TABLE: sha256:cc983863852848c048954787d9249068d81fa388b577e61aaba4efe1a423dfc4
    STARRY_ROUND2_CLOSE_SYSCALL: sha256:a7d7659602bdc60b7b858d375c84f2e5502ffba0db488c3e00781e7dfffd89a5
    STARRY_ROUND2_ERRNO_TRANSLATION: sha256:66f20cc556c04d12f324a7008941d8c0c71ad160df096cefc5829ae11f83ebd5
    STARRY_SOCKET_FD_VALIDATION: sha256:5ecab6581da9bd0116c28c43d73a9f0f9f56c9f0d61d12a312c1bffd9801e963
  dynamic_tests: {}
entity_versions:
  rules:
    LTP_09370275EF5F3065:
      id: LTP_09370275EF5F3065
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:09370275ef5f3065d6f3ea10b7288a1ce0668fd80cc67a7d32a6f3b3069149f6
    LTP_098AFE0E8E10B0EF:
      id: LTP_098AFE0E8E10B0EF
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:098afe0e8e10b0efa6872ee3d2ece3674b519943b59189a2758d8ab31b06ab26
    LTP_0EBD1214FC6BB6D5:
      id: LTP_0EBD1214FC6BB6D5
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:0ebd1214fc6bb6d5e224e50177509f565c7be9ba6ad0d4842779e564b71dedbb
    LTP_0FCE63CBC47F69DA:
      id: LTP_0FCE63CBC47F69DA
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:0fce63cbc47f69da5e2da3272c04cf9386103a75c442cf8614d29166e37f3fbb
    LTP_1726C16756E9651C:
      id: LTP_1726C16756E9651C
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:1726c16756e9651c8be282bf1cdf5c30a283e32aa200934084e3c42a2aee9ff9
    LTP_2BDE60C0E64B4DC8:
      id: LTP_2BDE60C0E64B4DC8
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:2bde60c0e64b4dc8fc4b1e23c70973364d891d517c1f8020f709fabec59e6d0f
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
    LTP_37C625BD7D7C5F1D:
      id: LTP_37C625BD7D7C5F1D
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:37c625bd7d7c5f1db42b7cacc49b4964844f0c2f977ad1a74c3960da0d662932
    LTP_37F2ED2BA3175CC3:
      id: LTP_37F2ED2BA3175CC3
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:37f2ed2ba3175cc394b1338888db3f207e809f7e36f789587873dc7921e85edd
    LTP_3A7B17AF231D4158:
      id: LTP_3A7B17AF231D4158
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:3a7b17af231d4158b2c4508e92a25435b89a569164e6dfdabc216b48e1afec9f
    LTP_425E5A3502541DE8:
      id: LTP_425E5A3502541DE8
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:425e5a3502541de863d8b8e88eafb95db2f8d8e1f9cb88a32d8b3124950395b2
    LTP_4C3A8A7664F22B7F:
      id: LTP_4C3A8A7664F22B7F
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:4c3a8a7664f22b7f2983c449e5c15d82b53d634db19f0a87e67849d4feb2fb77
    LTP_4F02ACC6E2F6B094:
      id: LTP_4F02ACC6E2F6B094
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:4f02acc6e2f6b094f06413684c004106e4c18d8f654cbb8b231de56e60aba90c
    LTP_511185D6DE2A63A0:
      id: LTP_511185D6DE2A63A0
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:511185d6de2a63a045d2f5f65babdf4c25b4066ece863b9f121419045563d4c9
    LTP_594FA5B54CA204E5:
      id: LTP_594FA5B54CA204E5
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:594fa5b54ca204e5062358a745af4921e86e002d54071b19f1650a69d2d468f7
    LTP_6A2F1D2BB0EE8C22:
      id: LTP_6A2F1D2BB0EE8C22
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:6a2f1d2bb0ee8c22d0970af42c645ba4f74a3cfe1a4748f4c47934666e135cfc
    LTP_6AEB77CEC03D0E6E:
      id: LTP_6AEB77CEC03D0E6E
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:6aeb77cec03d0e6eaa956bea440fe8e71843fa521eafcf9611595dee8394b4bb
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
    LTP_7E1612F09CACE33D:
      id: LTP_7E1612F09CACE33D
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:7e1612f09cace33d1e08ea245c28317ff95a538558b1d15dc9cd9e6c8dd2eb09
    LTP_84DBE108A850E845:
      id: LTP_84DBE108A850E845
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:84dbe108a850e845bf4a3cfc65c984525f06a85bcf44e616283b5ef4e16bb451
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
    LTP_BF2428964ADD116F:
      id: LTP_BF2428964ADD116F
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:bf2428964add116f793723626820cf1b363a819d6e38ba6d31d9832e4ab1b2c0
    LTP_C16D549555A00E55:
      id: LTP_C16D549555A00E55
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:c16d549555a00e55b3199db30fcc866aeac70c8911afbcc47053c09ffa2a5b85
    LTP_CBF4B6C8A1458A28:
      id: LTP_CBF4B6C8A1458A28
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:cbf4b6c8a1458a2885c6c847b47ca93098a06580fc5fdfc3a1e483b9dab01ac4
    LTP_CC9037A76978B569:
      id: LTP_CC9037A76978B569
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:cc9037a76978b569fcf3e91e91771dc63c6a8cf1479d9f5c6e079b8ef0e91e4f
    LTP_D296A517F138A0C0:
      id: LTP_D296A517F138A0C0
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:d296a517f138a0c09a3c71729b93607cfff1709b21125573bc2ad30b48302584
    LTP_E2196C3F0F58862B:
      id: LTP_E2196C3F0F58862B
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:e2196c3f0f58862b9dfeb182337b8bdf6ab3964ad73867128bb0853431dc7dbe
    LTP_E520E500AB3AE851:
      id: LTP_E520E500AB3AE851
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:e520e500ab3ae8512756eb4a69fdef5de2701520040c400ce896ec773f4ab472
    LTP_E7435E0CBCA319E1:
      id: LTP_E7435E0CBCA319E1
      generated_at_utc: '2026-07-15T05:26:39.098440Z'
      content_hash: sha256:e7435e0cbca319e18c1459e2f9187003681d326f400fc6d00b47df912010faef
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
  static_checks:
    STARRY_CLOSE_RANGE_SWEEP:
      id: STARRY_CLOSE_RANGE_SWEEP
      generated_at_utc: '2026-07-15T05:39:36.212938Z'
      content_hash: sha256:e930378c3b8c61c971d770a190b93b332ad822cc7a18c4372bd5b28dc24549c8
    STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS:
      id: STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS
      generated_at_utc: '2026-07-15T05:39:36.212938Z'
      content_hash: sha256:72f0ccfc42dbced9e73e1f1a0190437ce60275d7bc1e7c187f8c9a5d1c4d2660
    STARRY_CLOSE_RANGE_VALIDATION:
      id: STARRY_CLOSE_RANGE_VALIDATION
      generated_at_utc: '2026-07-15T05:39:36.212938Z'
      content_hash: sha256:f66999e179d22a424c8a9775b216e494d96009491c1d0cee1c8ae10dd11ab221
    STARRY_CONNECT_ADDRESS_VALIDATION:
      id: STARRY_CONNECT_ADDRESS_VALIDATION
      generated_at_utc: '2026-07-15T05:39:36.212938Z'
      content_hash: sha256:f12594e38c23899fa45d721c0c0bdaf7ef6184d8b987093528e94001d952b4ce
    STARRY_CONNECT_ENTRY:
      id: STARRY_CONNECT_ENTRY
      generated_at_utc: '2026-07-15T05:39:36.212938Z'
      content_hash: sha256:917822d39de2c61608947b6f1489f5ffd3d77c0a02683fef4bf53b8c31c7e249
    STARRY_COPY_FILE_RANGE_CORE:
      id: STARRY_COPY_FILE_RANGE_CORE
      generated_at_utc: '2026-07-15T05:39:36.212938Z'
      content_hash: sha256:87bbe450c3fed6eedf4989a90b546915add17c1354c4f74f14c87253ecf97950
    STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO:
      id: STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO
      generated_at_utc: '2026-07-15T05:39:36.212938Z'
      content_hash: sha256:6762073d1ceebfed08c172e40495ac3d2d484296c43a114b1477042dc051b87f
    STARRY_DUP2_DUP3_BEHAVIOR:
      id: STARRY_DUP2_DUP3_BEHAVIOR
      generated_at_utc: '2026-07-15T05:39:36.212938Z'
      content_hash: sha256:a150c80f2f30799a8d98957b5f049fe697e2ff990de192a833f37725965929ae
    STARRY_DUP_BEHAVIOR:
      id: STARRY_DUP_BEHAVIOR
      generated_at_utc: '2026-07-15T05:39:36.212938Z'
      content_hash: sha256:57cddc0d3a6603566933f41a1c11f23481660361c88964e7cd33461ff3864e8d
    STARRY_EPOLL_CREATE:
      id: STARRY_EPOLL_CREATE
      generated_at_utc: '2026-07-15T05:39:36.212938Z'
      content_hash: sha256:94f880e5cad41b9a599f96fce2042b830d0cf590a4b7ce2774536b1f4b5946f2
    STARRY_FD_TABLE_LOOKUP_ALLOCATION:
      id: STARRY_FD_TABLE_LOOKUP_ALLOCATION
      generated_at_utc: '2026-07-15T05:39:36.212938Z'
      content_hash: sha256:a4545e2b6d4f0347d731939456dac417be7c0f81fb889cef52bc44c37a3ebddf
    STARRY_ROUND2_CLOSE_FD_TABLE:
      id: STARRY_ROUND2_CLOSE_FD_TABLE
      generated_at_utc: '2026-07-15T05:39:36.212938Z'
      content_hash: sha256:cc983863852848c048954787d9249068d81fa388b577e61aaba4efe1a423dfc4
    STARRY_ROUND2_CLOSE_SYSCALL:
      id: STARRY_ROUND2_CLOSE_SYSCALL
      generated_at_utc: '2026-07-15T05:39:36.212938Z'
      content_hash: sha256:a7d7659602bdc60b7b858d375c84f2e5502ffba0db488c3e00781e7dfffd89a5
    STARRY_ROUND2_ERRNO_TRANSLATION:
      id: STARRY_ROUND2_ERRNO_TRANSLATION
      generated_at_utc: '2026-07-15T05:39:36.212938Z'
      content_hash: sha256:66f20cc556c04d12f324a7008941d8c0c71ad160df096cefc5829ae11f83ebd5
    STARRY_SOCKET_FD_VALIDATION:
      id: STARRY_SOCKET_FD_VALIDATION
      generated_at_utc: '2026-07-15T05:39:36.212938Z'
      content_hash: sha256:5ecab6581da9bd0116c28c43d73a9f0f9f56c9f0d61d12a312c1bffd9801e963
  dynamic_tests: {}
execution_scope:
  rules:
  - LTP_09370275EF5F3065
  - LTP_098AFE0E8E10B0EF
  - LTP_0EBD1214FC6BB6D5
  - LTP_0FCE63CBC47F69DA
  - LTP_1726C16756E9651C
  - LTP_2BDE60C0E64B4DC8
  - LTP_2D1E25BD679B3494
  - LTP_2F153EBAAD2A779C
  - LTP_311F7A773994720E
  - LTP_31D9D767D6888DDA
  - LTP_37C625BD7D7C5F1D
  - LTP_37F2ED2BA3175CC3
  - LTP_3A7B17AF231D4158
  - LTP_425E5A3502541DE8
  - LTP_4C3A8A7664F22B7F
  - LTP_4F02ACC6E2F6B094
  - LTP_511185D6DE2A63A0
  - LTP_594FA5B54CA204E5
  - LTP_6A2F1D2BB0EE8C22
  - LTP_6AEB77CEC03D0E6E
  - LTP_74BB3F96CBA52D02
  - LTP_74E00510F4C1B849
  - LTP_75D52C5E9C93B6D7
  - LTP_76BFF56F735A0074
  - LTP_7E1612F09CACE33D
  - LTP_84DBE108A850E845
  - LTP_9B3646398697EA64
  - LTP_9F560A103CB6F910
  - LTP_A774FC10727E8ED2
  - LTP_AE3908C408304451
  - LTP_B7F51635806E7E59
  - LTP_B87A71DE5DE1260E
  - LTP_BAE8F852378DD9F4
  - LTP_BDA36F61423EEB3E
  - LTP_BF2428964ADD116F
  - LTP_C16D549555A00E55
  - LTP_CBF4B6C8A1458A28
  - LTP_CC9037A76978B569
  - LTP_D296A517F138A0C0
  - LTP_E2196C3F0F58862B
  - LTP_E520E500AB3AE851
  - LTP_E7435E0CBCA319E1
  - LTP_ED2BA909DF79625A
  - LTP_EE8E695CF61D6D8A
  - LTP_F1DC44813DCA6A05
  - LTP_F4DE81D703447628
  static_checks:
  - STARRY_CLOSE_RANGE_SWEEP
  - STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS
  - STARRY_CLOSE_RANGE_VALIDATION
  - STARRY_CONNECT_ADDRESS_VALIDATION
  - STARRY_CONNECT_ENTRY
  - STARRY_COPY_FILE_RANGE_CORE
  - STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO
  - STARRY_DUP2_DUP3_BEHAVIOR
  - STARRY_DUP_BEHAVIOR
  - STARRY_EPOLL_CREATE
  - STARRY_FD_TABLE_LOOKUP_ALLOCATION
  - STARRY_ROUND2_CLOSE_FD_TABLE
  - STARRY_ROUND2_CLOSE_SYSCALL
  - STARRY_ROUND2_ERRNO_TRANSLATION
  - STARRY_SOCKET_FD_VALIDATION
  dynamic_tests: []
rule_syscalls:
  LTP_00F2A9EA8833DA1D:
  - cachestat
  LTP_0180982614AA9F7D:
  - access
  LTP_0290063892A53510:
  - access
  LTP_030858A5FFCCEFF4:
  - access
  LTP_035E62E6D1787773:
  - access
  LTP_036EDA2B8D36CF03:
  - access
  LTP_037E6F334D0E0D16:
  - access
  LTP_0431E3529AA0FEE8:
  - access
  LTP_044E7C11E6B503BB:
  - access
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
  LTP_09B39E9C9254ECB2:
  - close
  LTP_0A62800536904C02:
  - access
  LTP_0AAFA34BA77A0D25:
  - access
  LTP_0B45FC33068D334C:
  - access
  LTP_0BB235F712E819CE:
  - access
  LTP_0CD17E662AFD2956:
  - close
  LTP_0D1782EAAC26DEB4:
  - access
  LTP_0E9AF2C058AF8126:
  - access
  LTP_0EBD1214FC6BB6D5:
  - dup
  LTP_0F901C62092CC7B8:
  - access
  LTP_0FCE63CBC47F69DA:
  - connect
  LTP_10A684C1C2D2DE0F:
  - access
  LTP_10FE1313FBAB5F92:
  - access
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
  LTP_17CB4ED7A76BD283:
  - access
  LTP_1870C0046E9555AF:
  - access
  LTP_18A450CE49F8867B:
  - access
  LTP_198D9555A8BED013:
  - access
  LTP_1A9481FAD460FBF7:
  - alarm
  LTP_1BD36AE285B4F3E2:
  - access
  LTP_1C462AC54A29FF35:
  - access
  LTP_1CDCF5FE9ED1BE5D:
  - access
  LTP_1D39F97D759F0E57:
  - access
  LTP_1DF2B28499E4D7B3:
  - access
  LTP_208C833FF12217F5:
  - capget
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
  LTP_245CD61DAA19DC98:
  - chroot
  LTP_25639C9C5750C487:
  - access
  LTP_26AC646B9D18C353:
  - access
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
  LTP_311F7A773994720E:
  - dup
  LTP_31D9D767D6888DDA:
  - close_range
  LTP_3472CD1A0F8A2B4A:
  - access
  LTP_347761CBCF52D194:
  - access
  LTP_34CFEAD03DB6A3CA:
  - access
  LTP_34EC9FB9C9551214:
  - cachestat
  LTP_35CAEE10A613E109:
  - access
  LTP_3636C4768C196B52:
  - access
  LTP_368D8689810796B2:
  - access
  LTP_36C99C10CD38F8DB:
  - mmap
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
  LTP_3C2853617B38EEE7:
  - access
  LTP_3D4ECD22BC433164:
  - access
  LTP_3D8D38C9123CD051:
  - access
  LTP_3DE23AB4FE2FFC67:
  - access
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
  LTP_45439D8F2BAB0832:
  - mmap
  LTP_461340ED83E7043D:
  - capset
  LTP_4661BBF1B3CD3A1E:
  - access
  LTP_46DE8D9AD1674F26:
  - access
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
  LTP_49700CDA955B66D8:
  - access
  LTP_49A36559B96D24AF:
  - access
  LTP_4B6E9B98E2E5103D:
  - access
  LTP_4C3A8A7664F22B7F:
  - connect
  LTP_4CFAFCE7FCA2BF99:
  - access
  LTP_4ECB786BFA071AAC:
  - access
  LTP_4F02ACC6E2F6B094:
  - dup2
  LTP_50A86D4D5411356E:
  - access
  LTP_50F858A3CBF95EED:
  - chroot
  LTP_511185D6DE2A63A0:
  - dup
  LTP_51E295101A9F4411:
  - mmap
  LTP_52BAFC01DEA6E172:
  - mmap
  LTP_52C209105EE62171:
  - access
  LTP_5570480E7920BD0E:
  - access
  LTP_563FB650864E0DC6:
  - access
  LTP_58416E6747519699:
  - access
  LTP_58F1512157A0052D:
  - access
  LTP_594FA5B54CA204E5:
  - dup
  LTP_5A315335586D4227:
  - access
  LTP_5C5CDC165410C08C:
  - access
  LTP_5CC44E5D1A6B6485:
  - access
  LTP_5D7971086B2ABAE5:
  - access
  LTP_5EC31E34822684C4:
  - access
  LTP_5F1D35ACCEFD4971:
  - capget
  LTP_606B7E40B6BD82EA:
  - access
  LTP_613A5E121B4B6E68:
  - access
  LTP_6156A09A2E506F76:
  - access
  LTP_6169F41023E00C34:
  - access
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
  LTP_679436EC7A4E218A:
  - access
  LTP_67BF94A4ACD303C4:
  - access
  LTP_68745D21F4EC2FF5:
  - access
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
  LTP_711D5693356A79F2:
  - access
  LTP_71C54C624831C7F0:
  - chroot
  LTP_73DF50509BCC128B:
  - access
  LTP_74819A9DC2B5CB06:
  - access
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
  LTP_78EEEBE648781151:
  - access
  LTP_791DEA825D66980B:
  - mmap
  LTP_7963C3DF373596FE:
  - access
  LTP_79C7516DECB19092:
  - access
  LTP_7A02B34D5FB8BBC3:
  - access
  LTP_7A74A699442CEB99:
  - brk
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
  LTP_7DD493976CBC9A31:
  - access
  LTP_7DEDC53AC33C891F:
  - capset
  LTP_7E1612F09CACE33D:
  - copy_file_range
  LTP_7F43697FAC4213A8:
  - copy_file_range
  LTP_7F5487EEB79017AD:
  - access
  LTP_7F54F9DFF7E0FB61:
  - access
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
  LTP_87478A6C3AC7DC60:
  - access
  LTP_884775F9076E54AB:
  - access
  LTP_885F3BA721198C07:
  - access
  LTP_88F6F279E33633DE:
  - access
  LTP_89C9E8458EC38C11:
  - cachestat
  LTP_8AC11633EA3D83E0:
  - access
  LTP_8AD8032754BC8842:
  - cacheflush
  LTP_8B1A2084BCF096F1:
  - access
  LTP_8B3FBDFD0453EF40:
  - access
  LTP_8BB576EB2E1E6B23:
  - access
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
  LTP_969C39F409BFD7AA:
  - access
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
  LTP_A00E343F4A556B3D:
  - capset
  LTP_A17272D4FE0F040B:
  - access
  LTP_A1DEE046C0A10B18:
  - access
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
  LTP_AB48F262BBB2CC93:
  - access
  LTP_AC0FB73B4EE420EC:
  - access
  LTP_AD81218450587FA8:
  - access
  LTP_ADD30BEEC40E661F:
  - access
  LTP_AE3908C408304451:
  - copy_file_range
  LTP_B1D822DF0057B4E0:
  - access
  LTP_B200AFD97E91C2CC:
  - access
  LTP_B53406D510ED4981:
  - access
  LTP_B6DAF13EF3143EBF:
  - access
  LTP_B7A341967DF2BD69:
  - alarm
  LTP_B7F51635806E7E59:
  - dup2
  LTP_B87A71DE5DE1260E:
  - copy_file_range
  LTP_B90CB73F36B70C6F:
  - accept
  LTP_B9908D4015443661:
  - access
  LTP_B9CDD41A0DC2AFCC:
  - access
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
  LTP_C346EFF1233F7061:
  - mmap
  LTP_C5FE18F9550B31BA:
  - access
  LTP_C6A719982BDE9CE4:
  - access
  LTP_C6E67CB1FD2B1F64:
  - access
  LTP_C785774773FB7524:
  - alarm
  LTP_C7B73F4D5B87736A:
  - alarm
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
  LTP_CBF4B6C8A1458A28:
  - close_range
  LTP_CC9037A76978B569:
  - copy_file_range
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
  LTP_D1AADFC2F7C6F594:
  - capset
  LTP_D1B6112551D45B31:
  - alarm
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
  LTP_D653D15777B77A1F:
  - access
  LTP_D6A52FD61BF01578:
  - access
  LTP_D72526C4E4301D60:
  - access
  LTP_D76652434EC85091:
  - access
  LTP_D8B58CA743EBE711:
  - access
  LTP_DA10E351BC730D85:
  - access
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
  LTP_E7435E0CBCA319E1:
  - epoll_create
  LTP_EB00EA74B30E438E:
  - access
  LTP_EB425D988F2F7604:
  - access
  LTP_EBD54180D0CAB16B:
  - chroot
  LTP_EBF0020C32AD44C8:
  - access
  LTP_EC19C6410BBE0467:
  - access
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
  LTP_EF5C1F365208AD31:
  - access
  LTP_F1044C71B6626419:
  - accept
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
  LTP_F43EC0D01CCFD25A:
  - access
  LTP_F4DE81D703447628:
  - close_range
  LTP_F6BB86F5DCC2FAC8:
  - access
  LTP_F70FC66A56FBD769:
  - access
  LTP_F7998813C90A7A08:
  - access
  LTP_F8CDD57D76C8FA6C:
  - access
  LTP_F9BF08369A08E5ED:
  - access
  LTP_FC5B16AB3C53A744:
  - access
  LTP_FCA376B46A9873B0:
  - access
  LTP_FD1B65B0BCC88E0D:
  - mmap
  LTP_FEACDC300C3E1DD7:
  - mmap
  LTP_FF9C0F9669A39525:
  - chroot
static:
- check_id: STARRY_CLOSE_RANGE_SWEEP
  rule_refs:
  - LTP_76BFF56F735A0074
  - LTP_F4DE81D703447628
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/fd_ops.rs
  patterns:
  - label: the sweep is capped at the current maximum descriptor
    regex: pub fn sys_close_range\([\s\S]*?for fd in first\.\.=last\.min\(max_index as i32\)
    matched: true
    line: 455
  - label: missing descriptors are skipped and completion returns zero
    regex: for fd in first\.\.=last\.min\(max_index as i32\)[\s\S]*?if let Some\(f\) = fd_table\.remove\(fd
      as _\)[\s\S]*?Ok\(0\)
    matched: true
    line: 473
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS
  rule_refs:
  - LTP_425E5A3502541DE8
  result: fail
  path: os/StarryOS/kernel/src/syscall/fs/fd_ops.rs
  patterns:
  - label: first and last use unsigned 32-bit syscall semantics
    regex: 'pub fn sys_close_range\(first: u32, last: u32, flags: u32\)'
    matched: false
    line: null
  - label: the maximum unsigned range is accepted and capped to open descriptors
    regex: pub fn sys_close_range\([\s\S]*?for fd in first\.\.=last\.min\(max_index as u32\)[\s\S]*?Ok\(0\)
    matched: false
    line: null
  reason: one or more required patterns did not match
  finding_ids:
  - finding-close-range-ltp-425e5a3502541de8-041c7ef6f327
- check_id: STARRY_CLOSE_RANGE_VALIDATION
  rule_refs:
  - LTP_31D9D767D6888DDA
  - LTP_CBF4B6C8A1458A28
  - LTP_F1DC44813DCA6A05
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/fd_ops.rs
  patterns:
  - label: reversed ranges are invalid
    regex: pub fn sys_close_range\([\s\S]*?if first < 0 \|\| last < first \{[\s\S]*?return Err\(AxError::InvalidInput\);
    matched: true
    line: 455
  - label: unknown close_range flags are invalid
    regex: pub fn sys_close_range\([\s\S]*?CloseRangeFlags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?
    matched: true
    line: 455
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
  - LTP_4C3A8A7664F22B7F
  - LTP_6AEB77CEC03D0E6E
  - LTP_74E00510F4C1B849
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
  result: fail
  path: os/StarryOS/kernel/src/syscall/fs/io.rs
  patterns:
  - label: oversized len returns Linux EOVERFLOW rather than EINVAL
    regex: pub fn sys_copy_file_range\([\s\S]*?if len > isize::MAX as usize \{[\s\S]*?return Err\(AxError::from\(LinuxError::EOVERFLOW\)\);
    matched: false
    line: null
  reason: one or more required patterns did not match
  finding_ids:
  - finding-copy-file-range-ltp-74bb3f96cba52d02-041c7ef6f327
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
    line: 518
  - label: dup3 rejects unknown flags and equal descriptors
    regex: pub fn sys_dup3\([\s\S]*?Dup3Flags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?;[\s\S]*?if
      old_fd == new_fd \{[\s\S]*?Err\(AxError::InvalidInput\)
    matched: true
    line: 533
  - label: dup3 validates the old fd, replaces the target, and returns it
    regex: pub fn sys_dup3\([\s\S]*?\.get\(old_fd as _\)[\s\S]*?\.ok_or\(AxError::BadFileDescriptor\)\?;[\s\S]*?fd_table\.remove\(new_fd
      as _\)[\s\S]*?\.add_at\(new_fd as _, f\)[\s\S]*?Ok\(new_fd as _\)
    matched: true
    line: 533
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
    line: 487
  - label: sys_dup requests a non-CLOEXEC duplicate
    regex: 'pub fn sys_dup\(old_fd: c_int\)[\s\S]*?dup_fd\(old_fd, false\)'
    matched: true
    line: 512
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
    line: 275
  - label: allocation enforces the current nofile limit as TooManyOpenFiles
    regex: pub fn add_file_like\([\s\S]*?RLIMIT_NOFILE[\s\S]*?if table\.count\(\) as u64 >= max_nofile
      \{[\s\S]*?Err\(AxError::TooManyOpenFiles\)
    matched: true
    line: 296
  - label: successful allocation returns the new descriptor
    regex: pub fn add_file_like\([\s\S]*?Ok\(table\.add\(fd\)\.map_err\(\|_\| AxError::TooManyOpenFiles\)\?
      as c_int\)
    matched: true
    line: 296
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND2_CLOSE_FD_TABLE
  rule_refs:
  - LTP_2BDE60C0E64B4DC8
  - LTP_BF2428964ADD116F
  - LTP_E520E500AB3AE851
  result: pass
  path: os/StarryOS/kernel/src/file/mod.rs
  patterns:
  - label: close removes the descriptor independently of its file-like type
    regex: 'pub fn close_file_like\(fd: c_int\)[\s\S]*?FD_TABLE\.write\(\)\.remove\(fd as usize\)[\s\S]*?if
      let Some\(f\) = removed[\s\S]*?return Ok\(\(\)\);'
    matched: true
    line: 307
  - label: only a missing descriptor is rejected
    regex: 'pub fn close_file_like\(fd: c_int\)[\s\S]*?Err\(AxError::BadFileDescriptor\)'
    matched: true
    line: 307
  reason: all required patterns matched
  finding_ids: []
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
    line: 441
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND2_ERRNO_TRANSLATION
  rule_refs:
  - LTP_09370275EF5F3065
  - LTP_098AFE0E8E10B0EF
  - LTP_0EBD1214FC6BB6D5
  - LTP_0FCE63CBC47F69DA
  - LTP_2D1E25BD679B3494
  - LTP_2F153EBAAD2A779C
  - LTP_311F7A773994720E
  - LTP_31D9D767D6888DDA
  - LTP_37C625BD7D7C5F1D
  - LTP_37F2ED2BA3175CC3
  - LTP_4C3A8A7664F22B7F
  - LTP_4F02ACC6E2F6B094
  - LTP_511185D6DE2A63A0
  - LTP_6A2F1D2BB0EE8C22
  - LTP_74E00510F4C1B849
  - LTP_75D52C5E9C93B6D7
  - LTP_7E1612F09CACE33D
  - LTP_9B3646398697EA64
  - LTP_9F560A103CB6F910
  - LTP_AE3908C408304451
  - LTP_B87A71DE5DE1260E
  - LTP_BAE8F852378DD9F4
  - LTP_BDA36F61423EEB3E
  - LTP_C16D549555A00E55
  - LTP_CBF4B6C8A1458A28
  - LTP_CC9037A76978B569
  - LTP_D296A517F138A0C0
  - LTP_E2196C3F0F58862B
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
    line: 358
  reason: all required patterns matched
  finding_ids: []
dynamic: []
counts:
  static_pass: 13
  static_fail: 2
  static_error: 0
  dynamic_pass: 0
  dynamic_fail: 0
  dynamic_skipped: 0
  dynamic_not_run: 0
  findings: 2
  blockers: 0
blockers: []
finding_ids:
- finding-close-range-ltp-425e5a3502541de8-041c7ef6f327
- finding-copy-file-range-ltp-74bb3f96cba52d02-041c7ef6f327
finding_versions:
  finding-close-range-ltp-425e5a3502541de8-041c7ef6f327:
    id: finding-close-range-ltp-425e5a3502541de8-041c7ef6f327
    generated_at_utc: '2026-07-15T06:53:06.785885Z'
    content_hash: sha256:89268da49e1db71aedc695f99d930bd7fd766a4d292084985f5cc9419655c018
  finding-copy-file-range-ltp-74bb3f96cba52d02-041c7ef6f327:
    id: finding-copy-file-range-ltp-74bb3f96cba52d02-041c7ef6f327
    generated_at_utc: '2026-07-15T06:53:06.785885Z'
    content_hash: sha256:5891762040a38bcc1fa6a49f3fac4f8762684e8fc7b2b49156c52f12fe4eb050
content_hash: sha256:0a89f9f112c1cbbb8a149baae1d7369d588f79007884f4c453a2a78034947dc2
```
</details>
