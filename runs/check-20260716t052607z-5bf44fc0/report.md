# Starry 合规检查报告

## 本轮结论

- 状态：`completed`
- 静态检查：pass 18、fail 2、error 0
- 动态测试：pass 0、fail 0、skipped 0、not_run 0
- confirmed finding：2
- 新增：2、carry forward：0、已重验：0、待重验：0
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

### `STARRY_ROUND5_ERRNO_TRANSLATION`

- 类型：`static`
- 关联 syscall：`sched_setaffinity`、`sendfile`、`sendmsg`、`set_robust_list`、`setpgid`、`setpriority`、`signalfd`、`socket`
- 通用规则：`LTP_2C867F470A477D29`、`LTP_39B1E5C574F2D3DC`、`LTP_40024D6BE4C6AECC`、`LTP_4308D71D8BD6519D`、`LTP_44DC5382746D773D`、`LTP_585CC852338F38EE`、`LTP_7BC885B5878C95B6`、`LTP_971DB17D32C51561`、`LTP_A2098D60C40310A2`、`LTP_C8536F49779345AA`、`LTP_D7C638B9DFF7DBC3`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `BadAddress \\| BadState => EFAULT`：matched=`true`，第 223 行
  - `BadFileDescriptor => EBADF`：matched=`true`，第 224 行
  - `InvalidInput \\| InvalidData => EINVAL`：matched=`true`，第 235 行
- finding：—

### `STARRY_ROUND5_ROBUST_LIST`

- 类型：`static`
- 关联 syscall：`set_robust_list`
- 通用规则：`LTP_40024D6BE4C6AECC`、`LTP_E0470C189C2D1DE3`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_set_robust_list\([\s\S]*?if size != size_of::<robust_list_head>\(\) \{\s*return Err\(AxError::InvalidInput\);`：matched=`true`，第 324 行
  - `current\(\)\.as_thread\(\)\.set_robust_list_head\(head\.addr\(\)\);\s*Ok\(0\)`：matched=`true`，第 328 行
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

### `STARRY_ROUND5_SCHED_SETAFFINITY_USER_MASK`

- 类型：`static`
- 关联 syscall：`sched_setaffinity`
- 通用规则：`LTP_D7C638B9DFF7DBC3`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_sched_setaffinity\([\s\S]*?let user_mask = vm_load\(user_mask, size\)\?;`：matched=`true`，第 141 行
- finding：—

### `STARRY_ROUND5_SCHED_YIELD`

- 类型：`static`
- 关联 syscall：`sched_yield`
- 通用规则：`LTP_A9BC7EBC1784A722`
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

### `STARRY_ROUND5_SENDFILE_OFFSET_POINTER`

- 类型：`static`
- 关联 syscall：`sendfile`
- 通用规则：`LTP_C8536F49779345AA`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_sendfile\([\s\S]*?if !offset\.is_null\(\) \{\s*let pos = offset\.vm_read\(\)\?;`：matched=`true`，第 741 行
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
- 通用规则：`LTP_A2098D60C40310A2`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_sendmsg\([\s\S]*?let msg = msg\.get_as_ref\(\)\?;`：matched=`true`，第 137 行
- finding：—

### `STARRY_ROUND5_SETPGID_NEGATIVE`

- 类型：`static`
- 关联 syscall：`setpgid`
- 通用规则：`LTP_4308D71D8BD6519D`
- 结果：`fail`
- 原因：one or more required patterns did not match
- pattern 证据：

  - `pub fn sys_setpgid\(pid: i32, pgid: i32\) -> AxResult<isize>`：matched=`false`，未匹配
  - `pub fn sys_setpgid\([\s\S]*?if pid < 0 \\|\\| pgid < 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}`：matched=`false`，未匹配
- finding：`finding-setpgid-ltp-4308d71d8bd6519d-606a4cfde780`

### `STARRY_ROUND5_SETPRIORITY_SELECTOR`

- 类型：`static`
- 关联 syscall：`setpriority`
- 通用规则：`LTP_44DC5382746D773D`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_setpriority\([\s\S]*?match which \{[\s\S]*?_ => Err\(AxError::InvalidInput\),\s*\}`：matched=`true`，第 270 行
- finding：—

### `STARRY_ROUND5_SIGNALFD_FLAGS`

- 类型：`static`
- 关联 syscall：`signalfd`
- 通用规则：`LTP_2C867F470A477D29`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `let flags = SignalfdFlags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?;`：matched=`true`，第 48 行
- finding：—

### `STARRY_ROUND5_SOCKET_INVALID_TYPE`

- 类型：`static`
- 关联 syscall：`socket`
- 通用规则：`LTP_971DB17D32C51561`
- 结果：`fail`
- 原因：one or more required patterns did not match
- pattern 证据：

  - `pub fn sys_socket\([\s\S]*?\(AF_INET \\| AF_INET6, _\) \\| \(AF_UNIX, _\) \\| \(AF_NETLINK, _\) \\| \(AF_VSOCK, _\) => \{[\s\S]*?return Err\(AxError::InvalidInput\);[\s\S]*?\n\}\n\npub fn sys_bind`：matched=`false`，未匹配
- finding：`finding-socket-ltp-971db17d32c51561-606a4cfde780`

### `STARRY_ROUND5_SOCKET_PROTOCOL_ERRORS`

- 类型：`static`
- 关联 syscall：`socket`
- 通用规则：`LTP_6B29B31CE99466E6`、`LTP_A4A662687B98D33F`、`LTP_AF8D38878ED1A9DA`、`LTP_DD2E1A555B603C7B`、`LTP_E316C28E36E136DA`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `\(AF_INET \\| AF_INET6, SOCK_STREAM\) => \{[\s\S]*?proto != 0 && proto != IPPROTO_TCP as _[\s\S]*?LinuxError::EPROTONOSUPPORT`：matched=`true`，第 63 行
  - `\(AF_INET \\| AF_INET6, SOCK_DGRAM\) => \{[\s\S]*?proto != 0 && proto != IPPROTO_UDP as _[\s\S]*?LinuxError::EPROTONOSUPPORT`：matched=`true`，第 69 行
  - `\(AF_INET, SOCK_RAW\) => \{[\s\S]*?proto != IPPROTO_ICMP as u32[\s\S]*?LinuxError::EPROTONOSUPPORT`：matched=`true`，第 94 行
  - `_ => \{\s*return Err\(AxError::from\(LinuxError::EAFNOSUPPORT\)\);\s*\}`：matched=`true`，第 107 行
- finding：—

## 动态测试

本轮没有动态测试。

<details>
<summary>机器可读元数据</summary>

<!-- syscallguard-metadata -->
```yaml
schema_version: 1
kind: syscallguard_check_report
report_id: check-20260716t052607z-5bf44fc0
status: completed
generated_at_utc: '2026-07-16T05:26:11.833939Z'
mapping_report_id: mapping-20260716t051513z-743233c3
mapping_report_version:
  id: mapping-20260716t051513z-743233c3
  generated_at_utc: '2026-07-16T05:25:46.137226Z'
  content_hash: sha256:dc1b4bb7576bbfe6521180ec181b17ec2fe43fa5d0c5ebc5bac3a19b54aded19
target:
  target_id: starry
  repository: /home/cloud/gitLinux/tgoskits
  repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
  branch: dev-syscalls-compliance-1
  descriptor_hash: sha256:6b982bb80e3a0a3cf408d7c696367996422e3dac8376577222e56ee47f111d24
  snapshot_hash: sha256:606a4cfde780311cc5edcdcc833c7cbf520a190360791a132ff9da6d231772b8
input_hash: sha256:b2c58e8270b1e2b6968fe81d9b20fb343ee49454cdd10ed4edcc9582ea8e50a3
entity_hashes:
  rules:
    LTP_2C867F470A477D29: sha256:2c867f470a477d292a4a2d40ee43a337e4f77bb80811d916445beb2036cebbb8
    LTP_39B1E5C574F2D3DC: sha256:39b1e5c574f2d3dc16cd61efcb95f2cb9bffc5d5a5f86c1e52b9fac3ef82d569
    LTP_40024D6BE4C6AECC: sha256:40024d6be4c6aecc25eec2daf4ec64294dfce4200606f41b586028d4ee8360c1
    LTP_4308D71D8BD6519D: sha256:4308d71d8bd6519d6d2c15cb0c6d1925eed73874700fd6f1c1cc8a86199632a4
    LTP_44DC5382746D773D: sha256:44dc5382746d773d253ddf7ccb3ede2e242b978ebfb3e0756367ceb4d839956d
    LTP_585CC852338F38EE: sha256:585cc852338f38eedc86755b62d33a8eb443200486dd86bb3f79a4a4df80981c
    LTP_6B29B31CE99466E6: sha256:6b29b31ce99466e6682913919c0fad006475b094d59fadcc43c1ec6f4e9d1630
    LTP_7BC885B5878C95B6: sha256:7bc885b5878c95b621d9876c970257da2de585ab5e9771c1542ceed3b28f8ad0
    LTP_971DB17D32C51561: sha256:971db17d32c515614f0af38045463319bd4bfb3a661a4ae9e4486c0404c75ead
    LTP_A2098D60C40310A2: sha256:a2098d60c40310a201cf1ee9258fa49ff832fae788c0f99896d048e0cd323d61
    LTP_A4A662687B98D33F: sha256:a4a662687b98d33f933b37774536af580d8b9e44d1bc317c426dd2c4a68a7a1e
    LTP_A9BC7EBC1784A722: sha256:a9bc7ebc1784a72263646142685fb7ed3bb7aec45b58cfc208bd762f44d7c8fe
    LTP_AF8D38878ED1A9DA: sha256:af8d38878ed1a9da8bcca89799d36f633a0776307b92fe435d004f9b6cb1b444
    LTP_C8536F49779345AA: sha256:c8536f49779345aaca6b3672cea8de30e836aafaabcd8bfdeb6c149dff8a6810
    LTP_D7C638B9DFF7DBC3: sha256:d7c638b9dff7dbc39fe5df57a4ae8b6951d7c05218ed89e15d0e3e15710f4a7c
    LTP_DD2E1A555B603C7B: sha256:dd2e1a555b603c7b2ea7b60867a7cbf5b07e84f866b5a4cd8d83f27a24028065
    LTP_E0470C189C2D1DE3: sha256:e0470c189c2d1de37f10ab6be898fcfa26ff828dc89057c84d3ddaf504ab41bd
    LTP_E316C28E36E136DA: sha256:e316c28e36e136da592847ed1389e06538d4842d55259bc0bd80dbb61b78d10e
    LTP_425E5A3502541DE8: sha256:425e5a3502541de863d8b8e88eafb95db2f8d8e1f9cb88a32d8b3124950395b2
    LTP_74BB3F96CBA52D02: sha256:74bb3f96cba52d02850ad3c5e54c87acf278ce51290c99d5ae29da583be9ba38
    LTP_66C670178B06E9F3: sha256:66c670178b06e9f3eae76490edd09b4a26bb0e1c2ccba3c4cbc2a625d12c39bb
    LTP_DA65D6C7A0E4ABBC: sha256:da65d6c7a0e4abbc12ba61464384db59b2ccc9a4215469858de691a4c6deb562
    LTP_6C14DE68E3C0CC24: sha256:6c14de68e3c0cc24bbb7021cd805e26a73df65653f350d8fa8ed8de5232949e8
    LTP_D246498B20D9CB2C: sha256:d246498b20d9cb2cd6ece54014a50e1c77fa08b6a598251c2dc0e3a3700193e2
  static_checks:
    STARRY_ROUND5_ERRNO_TRANSLATION: sha256:da770a5400fe32b31dae3fdc5a48aa221b331983d32fd2b3bb87a450e423aa95
    STARRY_ROUND5_ROBUST_LIST: sha256:49c225ff275ba796295228b813bfbfe761cc508a01a9b971464fcf7affc91426
    STARRY_ROUND5_SCHED_SETAFFINITY_EMPTY_MASK: sha256:1286cf448c7276b238ae0d54ccd93eabfa18ca945139d46a4eb97a11c766d9df
    STARRY_ROUND5_SCHED_SETAFFINITY_USER_MASK: sha256:c8f75a8cb1b1ad6abff2190bf03499956e9f2f2533b82a8435763319939f5659
    STARRY_ROUND5_SCHED_YIELD: sha256:f1d5abc2d7ecb7e7c1cb8a3d6f071fc74d40239a7364a6d9b7f78bdf77eaf6e4
    STARRY_ROUND5_SENDFILE_IN_FD: sha256:b7aac3850568921e4f59c7882d1498dc68d0db6a6efa16737d53f12e56e26938
    STARRY_ROUND5_SENDFILE_OFFSET_POINTER: sha256:cb5f336256c5a1d3e9babebe6f1b2af1e4be40787db147ad64c4047e345dac7a
    STARRY_ROUND5_SENDFILE_OUT_FD: sha256:69c98a26ff6fd6f0534a6eddc1c977a5f60ce20b9c9efaccb4a00b65c48faef6
    STARRY_ROUND5_SENDMSG_MESSAGE_POINTER: sha256:50e22d19350bd1144627e433bc10ea63c290fec1cf9187cadb3e9d874ef596ab
    STARRY_ROUND5_SETPGID_NEGATIVE: sha256:e89391ce26bf073a42d5a1dd59186e745d8579fc6655083d4206d06e7db12831
    STARRY_ROUND5_SETPRIORITY_SELECTOR: sha256:0a117a8add6bdbeef860acccf720e9feb130a9d62257944831d44bc590e383b5
    STARRY_ROUND5_SIGNALFD_FLAGS: sha256:464e7ac32d448e68093c3a53cd0a9d95c5bd76754fab1fa566201454f5210a7d
    STARRY_ROUND5_SOCKET_INVALID_TYPE: sha256:e01440a0647bad98aa25dce14810b77d35d1943ba53d2e0a9cfced0afb63e543
    STARRY_ROUND5_SOCKET_PROTOCOL_ERRORS: sha256:ef888f38f5caad5a56c28b14fd6bf934e317b3ea18fe9b83949eb0126368fad3
    STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS: sha256:6d8ffe193808bde740053a61419adcf0e7c090388b2f5fea0475696c5b402070
    STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO: sha256:39ebc0849b8fede86d9689ed1dba7fda23315b83937a447b328ffd1a94bdfb34
    STARRY_EPOLL_NESTED_LOOP: sha256:d1db97954ea66c6632d4d74191ef0d91751bbbcfee42883a78137bbdaac22e58
    STARRY_FINIT_MODULE_FLAG_VALIDATION: sha256:81ef9eef26bc66571e89435a216d883211029dd798c2e5ce97752ec71f012cf4
    STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE: sha256:2e938148c5bb7288d8d9971f38b67963abae7401d6ccd7d1c25d575321dee90f
    STARRY_ROUND3_INIT_MODULE_PERMISSION: sha256:529b6e4f913c327e42930f608d34b14a971a4d23f7b25f9e82dec7def42e6d27
  dynamic_tests: {}
entity_versions:
  rules:
    LTP_2C867F470A477D29:
      id: LTP_2C867F470A477D29
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:2c867f470a477d292a4a2d40ee43a337e4f77bb80811d916445beb2036cebbb8
    LTP_39B1E5C574F2D3DC:
      id: LTP_39B1E5C574F2D3DC
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:39b1e5c574f2d3dc16cd61efcb95f2cb9bffc5d5a5f86c1e52b9fac3ef82d569
    LTP_40024D6BE4C6AECC:
      id: LTP_40024D6BE4C6AECC
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:40024d6be4c6aecc25eec2daf4ec64294dfce4200606f41b586028d4ee8360c1
    LTP_4308D71D8BD6519D:
      id: LTP_4308D71D8BD6519D
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:4308d71d8bd6519d6d2c15cb0c6d1925eed73874700fd6f1c1cc8a86199632a4
    LTP_44DC5382746D773D:
      id: LTP_44DC5382746D773D
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:44dc5382746d773d253ddf7ccb3ede2e242b978ebfb3e0756367ceb4d839956d
    LTP_585CC852338F38EE:
      id: LTP_585CC852338F38EE
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:585cc852338f38eedc86755b62d33a8eb443200486dd86bb3f79a4a4df80981c
    LTP_6B29B31CE99466E6:
      id: LTP_6B29B31CE99466E6
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:6b29b31ce99466e6682913919c0fad006475b094d59fadcc43c1ec6f4e9d1630
    LTP_7BC885B5878C95B6:
      id: LTP_7BC885B5878C95B6
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:7bc885b5878c95b621d9876c970257da2de585ab5e9771c1542ceed3b28f8ad0
    LTP_971DB17D32C51561:
      id: LTP_971DB17D32C51561
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:971db17d32c515614f0af38045463319bd4bfb3a661a4ae9e4486c0404c75ead
    LTP_A2098D60C40310A2:
      id: LTP_A2098D60C40310A2
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:a2098d60c40310a201cf1ee9258fa49ff832fae788c0f99896d048e0cd323d61
    LTP_A4A662687B98D33F:
      id: LTP_A4A662687B98D33F
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:a4a662687b98d33f933b37774536af580d8b9e44d1bc317c426dd2c4a68a7a1e
    LTP_A9BC7EBC1784A722:
      id: LTP_A9BC7EBC1784A722
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:a9bc7ebc1784a72263646142685fb7ed3bb7aec45b58cfc208bd762f44d7c8fe
    LTP_AF8D38878ED1A9DA:
      id: LTP_AF8D38878ED1A9DA
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:af8d38878ed1a9da8bcca89799d36f633a0776307b92fe435d004f9b6cb1b444
    LTP_C8536F49779345AA:
      id: LTP_C8536F49779345AA
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:c8536f49779345aaca6b3672cea8de30e836aafaabcd8bfdeb6c149dff8a6810
    LTP_D7C638B9DFF7DBC3:
      id: LTP_D7C638B9DFF7DBC3
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:d7c638b9dff7dbc39fe5df57a4ae8b6951d7c05218ed89e15d0e3e15710f4a7c
    LTP_DD2E1A555B603C7B:
      id: LTP_DD2E1A555B603C7B
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:dd2e1a555b603c7b2ea7b60867a7cbf5b07e84f866b5a4cd8d83f27a24028065
    LTP_E0470C189C2D1DE3:
      id: LTP_E0470C189C2D1DE3
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:e0470c189c2d1de37f10ab6be898fcfa26ff828dc89057c84d3ddaf504ab41bd
    LTP_E316C28E36E136DA:
      id: LTP_E316C28E36E136DA
      generated_at_utc: '2026-07-16T05:14:25.198516Z'
      content_hash: sha256:e316c28e36e136da592847ed1389e06538d4842d55259bc0bd80dbb61b78d10e
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
  static_checks:
    STARRY_ROUND5_ERRNO_TRANSLATION:
      id: STARRY_ROUND5_ERRNO_TRANSLATION
      generated_at_utc: '2026-07-16T05:25:46.137226Z'
      content_hash: sha256:da770a5400fe32b31dae3fdc5a48aa221b331983d32fd2b3bb87a450e423aa95
    STARRY_ROUND5_ROBUST_LIST:
      id: STARRY_ROUND5_ROBUST_LIST
      generated_at_utc: '2026-07-16T05:25:46.137226Z'
      content_hash: sha256:49c225ff275ba796295228b813bfbfe761cc508a01a9b971464fcf7affc91426
    STARRY_ROUND5_SCHED_SETAFFINITY_EMPTY_MASK:
      id: STARRY_ROUND5_SCHED_SETAFFINITY_EMPTY_MASK
      generated_at_utc: '2026-07-16T05:25:46.137226Z'
      content_hash: sha256:1286cf448c7276b238ae0d54ccd93eabfa18ca945139d46a4eb97a11c766d9df
    STARRY_ROUND5_SCHED_SETAFFINITY_USER_MASK:
      id: STARRY_ROUND5_SCHED_SETAFFINITY_USER_MASK
      generated_at_utc: '2026-07-16T05:25:46.137226Z'
      content_hash: sha256:c8f75a8cb1b1ad6abff2190bf03499956e9f2f2533b82a8435763319939f5659
    STARRY_ROUND5_SCHED_YIELD:
      id: STARRY_ROUND5_SCHED_YIELD
      generated_at_utc: '2026-07-16T05:25:46.137226Z'
      content_hash: sha256:f1d5abc2d7ecb7e7c1cb8a3d6f071fc74d40239a7364a6d9b7f78bdf77eaf6e4
    STARRY_ROUND5_SENDFILE_IN_FD:
      id: STARRY_ROUND5_SENDFILE_IN_FD
      generated_at_utc: '2026-07-16T05:25:46.137226Z'
      content_hash: sha256:b7aac3850568921e4f59c7882d1498dc68d0db6a6efa16737d53f12e56e26938
    STARRY_ROUND5_SENDFILE_OFFSET_POINTER:
      id: STARRY_ROUND5_SENDFILE_OFFSET_POINTER
      generated_at_utc: '2026-07-16T05:25:46.137226Z'
      content_hash: sha256:cb5f336256c5a1d3e9babebe6f1b2af1e4be40787db147ad64c4047e345dac7a
    STARRY_ROUND5_SENDFILE_OUT_FD:
      id: STARRY_ROUND5_SENDFILE_OUT_FD
      generated_at_utc: '2026-07-16T05:25:46.137226Z'
      content_hash: sha256:69c98a26ff6fd6f0534a6eddc1c977a5f60ce20b9c9efaccb4a00b65c48faef6
    STARRY_ROUND5_SENDMSG_MESSAGE_POINTER:
      id: STARRY_ROUND5_SENDMSG_MESSAGE_POINTER
      generated_at_utc: '2026-07-16T05:25:46.137226Z'
      content_hash: sha256:50e22d19350bd1144627e433bc10ea63c290fec1cf9187cadb3e9d874ef596ab
    STARRY_ROUND5_SETPGID_NEGATIVE:
      id: STARRY_ROUND5_SETPGID_NEGATIVE
      generated_at_utc: '2026-07-16T05:25:46.137226Z'
      content_hash: sha256:e89391ce26bf073a42d5a1dd59186e745d8579fc6655083d4206d06e7db12831
    STARRY_ROUND5_SETPRIORITY_SELECTOR:
      id: STARRY_ROUND5_SETPRIORITY_SELECTOR
      generated_at_utc: '2026-07-16T05:25:46.137226Z'
      content_hash: sha256:0a117a8add6bdbeef860acccf720e9feb130a9d62257944831d44bc590e383b5
    STARRY_ROUND5_SIGNALFD_FLAGS:
      id: STARRY_ROUND5_SIGNALFD_FLAGS
      generated_at_utc: '2026-07-16T05:25:46.137226Z'
      content_hash: sha256:464e7ac32d448e68093c3a53cd0a9d95c5bd76754fab1fa566201454f5210a7d
    STARRY_ROUND5_SOCKET_INVALID_TYPE:
      id: STARRY_ROUND5_SOCKET_INVALID_TYPE
      generated_at_utc: '2026-07-16T05:25:46.137226Z'
      content_hash: sha256:e01440a0647bad98aa25dce14810b77d35d1943ba53d2e0a9cfced0afb63e543
    STARRY_ROUND5_SOCKET_PROTOCOL_ERRORS:
      id: STARRY_ROUND5_SOCKET_PROTOCOL_ERRORS
      generated_at_utc: '2026-07-16T05:25:46.137226Z'
      content_hash: sha256:ef888f38f5caad5a56c28b14fd6bf934e317b3ea18fe9b83949eb0126368fad3
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
      generated_at_utc: '2026-07-16T04:30:54.819863Z'
      content_hash: sha256:2e938148c5bb7288d8d9971f38b67963abae7401d6ccd7d1c25d575321dee90f
    STARRY_ROUND3_INIT_MODULE_PERMISSION:
      id: STARRY_ROUND3_INIT_MODULE_PERMISSION
      generated_at_utc: '2026-07-16T04:30:54.819863Z'
      content_hash: sha256:529b6e4f913c327e42930f608d34b14a971a4d23f7b25f9e82dec7def42e6d27
  dynamic_tests: {}
base_execution_scope:
  rules:
  - LTP_2C867F470A477D29
  - LTP_39B1E5C574F2D3DC
  - LTP_40024D6BE4C6AECC
  - LTP_4308D71D8BD6519D
  - LTP_44DC5382746D773D
  - LTP_585CC852338F38EE
  - LTP_6B29B31CE99466E6
  - LTP_7BC885B5878C95B6
  - LTP_971DB17D32C51561
  - LTP_A2098D60C40310A2
  - LTP_A4A662687B98D33F
  - LTP_A9BC7EBC1784A722
  - LTP_AF8D38878ED1A9DA
  - LTP_C8536F49779345AA
  - LTP_D7C638B9DFF7DBC3
  - LTP_DD2E1A555B603C7B
  - LTP_E0470C189C2D1DE3
  - LTP_E316C28E36E136DA
  static_checks:
  - STARRY_ROUND5_ERRNO_TRANSLATION
  - STARRY_ROUND5_ROBUST_LIST
  - STARRY_ROUND5_SCHED_SETAFFINITY_EMPTY_MASK
  - STARRY_ROUND5_SCHED_SETAFFINITY_USER_MASK
  - STARRY_ROUND5_SCHED_YIELD
  - STARRY_ROUND5_SENDFILE_IN_FD
  - STARRY_ROUND5_SENDFILE_OFFSET_POINTER
  - STARRY_ROUND5_SENDFILE_OUT_FD
  - STARRY_ROUND5_SENDMSG_MESSAGE_POINTER
  - STARRY_ROUND5_SETPGID_NEGATIVE
  - STARRY_ROUND5_SETPRIORITY_SELECTOR
  - STARRY_ROUND5_SIGNALFD_FLAGS
  - STARRY_ROUND5_SOCKET_INVALID_TYPE
  - STARRY_ROUND5_SOCKET_PROTOCOL_ERRORS
  dynamic_tests: []
revalidation_scope:
  rules: []
  static_checks: []
  dynamic_tests: []
effective_execution_scope: &id001
  rules:
  - LTP_2C867F470A477D29
  - LTP_39B1E5C574F2D3DC
  - LTP_40024D6BE4C6AECC
  - LTP_425E5A3502541DE8
  - LTP_4308D71D8BD6519D
  - LTP_44DC5382746D773D
  - LTP_585CC852338F38EE
  - LTP_66C670178B06E9F3
  - LTP_6B29B31CE99466E6
  - LTP_6C14DE68E3C0CC24
  - LTP_74BB3F96CBA52D02
  - LTP_7BC885B5878C95B6
  - LTP_971DB17D32C51561
  - LTP_A2098D60C40310A2
  - LTP_A4A662687B98D33F
  - LTP_A9BC7EBC1784A722
  - LTP_AF8D38878ED1A9DA
  - LTP_C8536F49779345AA
  - LTP_D246498B20D9CB2C
  - LTP_D7C638B9DFF7DBC3
  - LTP_DA65D6C7A0E4ABBC
  - LTP_DD2E1A555B603C7B
  - LTP_E0470C189C2D1DE3
  - LTP_E316C28E36E136DA
  static_checks:
  - STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS
  - STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO
  - STARRY_EPOLL_NESTED_LOOP
  - STARRY_FINIT_MODULE_FLAG_VALIDATION
  - STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE
  - STARRY_ROUND3_INIT_MODULE_PERMISSION
  - STARRY_ROUND5_ERRNO_TRANSLATION
  - STARRY_ROUND5_ROBUST_LIST
  - STARRY_ROUND5_SCHED_SETAFFINITY_EMPTY_MASK
  - STARRY_ROUND5_SCHED_SETAFFINITY_USER_MASK
  - STARRY_ROUND5_SCHED_YIELD
  - STARRY_ROUND5_SENDFILE_IN_FD
  - STARRY_ROUND5_SENDFILE_OFFSET_POINTER
  - STARRY_ROUND5_SENDFILE_OUT_FD
  - STARRY_ROUND5_SENDMSG_MESSAGE_POINTER
  - STARRY_ROUND5_SETPGID_NEGATIVE
  - STARRY_ROUND5_SETPRIORITY_SELECTOR
  - STARRY_ROUND5_SIGNALFD_FLAGS
  - STARRY_ROUND5_SOCKET_INVALID_TYPE
  - STARRY_ROUND5_SOCKET_PROTOCOL_ERRORS
  dynamic_tests: []
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
  LTP_03FD233DFE92488D:
  - sbrk
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
  LTP_0F9F906AC57F0B46:
  - pidfd_send_signal
  LTP_0FCE63CBC47F69DA:
  - connect
  LTP_0FEC274199CCD0A0:
  - execveat
  LTP_1028A46194A35788:
  - rename
  LTP_106D7242AECD4D33:
  - setpgrp
  LTP_10A684C1C2D2DE0F:
  - access
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
  LTP_16B8EA75C5016419:
  - mlock2
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
  LTP_2900BC64740A3E44:
  - access
  LTP_296D3DD5B2B27A84:
  - pwritev2
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
  LTP_3C1DCCC4E6DCC76B:
  - sendfile
  LTP_3C2853617B38EEE7:
  - access
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
  LTP_40ABB27673C9DE62:
  - sendto
  LTP_4101795C27681AB4:
  - openat2
  LTP_423E92D9328C2A39:
  - rt_sigprocmask
  LTP_425E5A3502541DE8:
  - close_range
  LTP_4308D71D8BD6519D:
  - setpgid
  LTP_437CFCD991A666C9:
  - faccessat2
  LTP_43A681D8FCD1B740:
  - pidfd_getfd
  LTP_43BC8A0B853CD8DB:
  - rename
  LTP_44128D8D82BC1E09:
  - flock
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
  LTP_49A11FBBFB010278:
  - sendto
  LTP_49A36559B96D24AF:
  - access
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
  LTP_53F53970B961AB32:
  - open_by_handle_at
  LTP_54CE18AAE5BDB693:
  - madvise
  LTP_54D221925C324829:
  - rename
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
  LTP_6D195DDAB1BE2B57:
  - kill
  LTP_6D584CE6CF9B8A06:
  - access
  LTP_6D86AFD541A61388:
  - capset
  LTP_6DD85CE2E5952779:
  - msync
  LTP_6DF55FF20A44572D:
  - getpriority
  LTP_6EF7ECD2A8470CEA:
  - access
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
  LTP_857DC6AD01A88D79:
  - access
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
  LTP_882D8F6DFB4B7858:
  - mprotect
  LTP_884775F9076E54AB:
  - access
  LTP_885F3BA721198C07:
  - access
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
  LTP_8D54825D4B298C7C:
  - access
  LTP_8D6B83A8176DB57E:
  - listxattr
  LTP_8D95C734339E42C6:
  - settimeofday
  LTP_8E7F1BE3D7D7823B:
  - access
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
  LTP_A1B6FBC6EF800331:
  - fchmod
  LTP_A1D08F4E94B7899A:
  - listen
  LTP_A1DEE046C0A10B18:
  - access
  LTP_A2098D60C40310A2:
  - sendmsg
  LTP_A2A80201A4364230:
  - flock
  LTP_A2E3A27D541DED02:
  - kill
  LTP_A30F7687D403407B:
  - access
  LTP_A363671517C058B1:
  - fstat
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
  LTP_C071A7FFF929A2A5:
  - access
  LTP_C09E83BE36885312:
  - gethostname
  LTP_C0AA45BC29F98A0E:
  - access
  LTP_C12A995BA4553344:
  - madvise
  LTP_C1462BACF46A177B:
  - madvise
  LTP_C16D549555A00E55:
  - copy_file_range
  LTP_C1C67435FC56D878:
  - access
  LTP_C218D3CB0AD80D90:
  - cacheflush
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
  LTP_D90C4B47C5FF6BC9:
  - request_key
  LTP_D90E4279570B6A94:
  - madvise
  LTP_D9418F7424E86C28:
  - mlock2
  LTP_D9561EEACFF72902:
  - sendmsg
  LTP_D98D789F4EBA6817:
  - rename
  LTP_D9A5AE03D93C5C6D:
  - read
  LTP_DA10E351BC730D85:
  - access
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
  LTP_DD2E1A555B603C7B:
  - socket
  LTP_DD64353E8E427275:
  - pathconf
  LTP_DD647A49F00FCC45:
  - recvfrom
  LTP_DD9A41090E3D5A17:
  - access
  LTP_DDCD82CA2726175D:
  - nanosleep
  LTP_DE6F80C5EFE44A9D:
  - dup2
  LTP_DF1C4714B16B760E:
  - access
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
  LTP_FCA376B46A9873B0:
  - access
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
- check_id: STARRY_ROUND5_ERRNO_TRANSLATION
  rule_refs:
  - LTP_2C867F470A477D29
  - LTP_39B1E5C574F2D3DC
  - LTP_40024D6BE4C6AECC
  - LTP_4308D71D8BD6519D
  - LTP_44DC5382746D773D
  - LTP_585CC852338F38EE
  - LTP_7BC885B5878C95B6
  - LTP_971DB17D32C51561
  - LTP_A2098D60C40310A2
  - LTP_C8536F49779345AA
  - LTP_D7C638B9DFF7DBC3
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
- check_id: STARRY_ROUND5_ROBUST_LIST
  rule_refs:
  - LTP_40024D6BE4C6AECC
  - LTP_E0470C189C2D1DE3
  result: pass
  path: os/StarryOS/kernel/src/syscall/sync/futex.rs
  patterns:
  - label: wrong robust-list size is invalid
    regex: pub fn sys_set_robust_list\([\s\S]*?if size != size_of::<robust_list_head>\(\) \{\s*return
      Err\(AxError::InvalidInput\);
    matched: true
    line: 324
  - label: valid robust-list head is stored before success
    regex: current\(\)\.as_thread\(\)\.set_robust_list_head\(head\.addr\(\)\);\s*Ok\(0\)
    matched: true
    line: 328
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
- check_id: STARRY_ROUND5_SCHED_SETAFFINITY_USER_MASK
  rule_refs:
  - LTP_D7C638B9DFF7DBC3
  result: pass
  path: os/StarryOS/kernel/src/syscall/task/schedule.rs
  patterns:
  - label: user mask is loaded through vm_load
    regex: pub fn sys_sched_setaffinity\([\s\S]*?let user_mask = vm_load\(user_mask, size\)\?;
    matched: true
    line: 141
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND5_SCHED_YIELD
  rule_refs:
  - LTP_A9BC7EBC1784A722
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
- check_id: STARRY_ROUND5_SENDFILE_OFFSET_POINTER
  rule_refs:
  - LTP_C8536F49779345AA
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/io.rs
  patterns:
  - label: offset is read with vm_read
    regex: pub fn sys_sendfile\([\s\S]*?if !offset\.is_null\(\) \{\s*let pos = offset\.vm_read\(\)\?;
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
  - LTP_A2098D60C40310A2
  result: pass
  path: os/StarryOS/kernel/src/syscall/net/io.rs
  patterns:
  - label: message header uses checked user access
    regex: pub fn sys_sendmsg\([\s\S]*?let msg = msg\.get_as_ref\(\)\?;
    matched: true
    line: 137
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND5_SETPGID_NEGATIVE
  rule_refs:
  - LTP_4308D71D8BD6519D
  result: fail
  path: os/StarryOS/kernel/src/syscall/task/job.rs
  patterns:
  - label: setpgid preserves signed syscall arguments
    regex: 'pub fn sys_setpgid\(pid: i32, pgid: i32\) -> AxResult<isize>'
    matched: false
    line: null
  - label: negative pid or pgid is rejected with invalid input
    regex: pub fn sys_setpgid\([\s\S]*?if pid < 0 \|\| pgid < 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}
    matched: false
    line: null
  reason: one or more required patterns did not match
  finding_ids:
  - finding-setpgid-ltp-4308d71d8bd6519d-606a4cfde780
- check_id: STARRY_ROUND5_SETPRIORITY_SELECTOR
  rule_refs:
  - LTP_44DC5382746D773D
  result: pass
  path: os/StarryOS/kernel/src/syscall/task/schedule.rs
  patterns:
  - label: unknown which value is invalid input
    regex: pub fn sys_setpriority\([\s\S]*?match which \{[\s\S]*?_ => Err\(AxError::InvalidInput\),\s*\}
    matched: true
    line: 270
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND5_SIGNALFD_FLAGS
  rule_refs:
  - LTP_2C867F470A477D29
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/signalfd.rs
  patterns:
  - label: unknown flag bits are invalid input
    regex: let flags = SignalfdFlags::from_bits\(flags\)\.ok_or\(AxError::InvalidInput\)\?;
    matched: true
    line: 48
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
  - finding-socket-ltp-971db17d32c51561-606a4cfde780
- check_id: STARRY_ROUND5_SOCKET_PROTOCOL_ERRORS
  rule_refs:
  - LTP_6B29B31CE99466E6
  - LTP_A4A662687B98D33F
  - LTP_AF8D38878ED1A9DA
  - LTP_DD2E1A555B603C7B
  - LTP_E316C28E36E136DA
  result: pass
  path: os/StarryOS/kernel/src/syscall/net/socket.rs
  patterns:
  - label: TCP sockets reject non-TCP protocols
    regex: \(AF_INET \| AF_INET6, SOCK_STREAM\) => \{[\s\S]*?proto != 0 && proto != IPPROTO_TCP as _[\s\S]*?LinuxError::EPROTONOSUPPORT
    matched: true
    line: 63
  - label: UDP sockets reject non-UDP protocols
    regex: \(AF_INET \| AF_INET6, SOCK_DGRAM\) => \{[\s\S]*?proto != 0 && proto != IPPROTO_UDP as _[\s\S]*?LinuxError::EPROTONOSUPPORT
    matched: true
    line: 69
  - label: raw IPv4 sockets reject unsupported protocols
    regex: \(AF_INET, SOCK_RAW\) => \{[\s\S]*?proto != IPPROTO_ICMP as u32[\s\S]*?LinuxError::EPROTONOSUPPORT
    matched: true
    line: 94
  - label: unknown domains return EAFNOSUPPORT
    regex: _ => \{\s*return Err\(AxError::from\(LinuxError::EAFNOSUPPORT\)\);\s*\}
    matched: true
    line: 107
  reason: all required patterns matched
  finding_ids: []
dynamic: []
counts:
  static_pass: 18
  static_fail: 2
  static_error: 0
  dynamic_pass: 0
  dynamic_fail: 0
  dynamic_skipped: 0
  dynamic_not_run: 0
  findings: 2
  blockers: 0
  new_findings: 2
  carried_findings: 0
  revalidated_findings: 0
  needs_revalidation: 0
blockers: []
finding_ids:
- finding-setpgid-ltp-4308d71d8bd6519d-606a4cfde780
- finding-socket-ltp-971db17d32c51561-606a4cfde780
finding_versions:
  finding-setpgid-ltp-4308d71d8bd6519d-606a4cfde780:
    id: finding-setpgid-ltp-4308d71d8bd6519d-606a4cfde780
    generated_at_utc: '2026-07-16T05:26:11.833939Z'
    content_hash: sha256:66cf2c49e765b1febaa7df1c71e1edc35fde740837d306d06c2c2859f86f509e
  finding-socket-ltp-971db17d32c51561-606a4cfde780:
    id: finding-socket-ltp-971db17d32c51561-606a4cfde780
    generated_at_utc: '2026-07-16T05:26:11.833939Z'
    content_hash: sha256:04e646e7945fb1e1924f58382b583f39c0e94a080ea0c82f204174c2f6d654d4
new_finding_ids:
- finding-setpgid-ltp-4308d71d8bd6519d-606a4cfde780
- finding-socket-ltp-971db17d32c51561-606a4cfde780
carried_finding_ids: []
revalidated_finding_ids: []
needs_revalidation_finding_ids: []
historical_regression_scope:
  rules:
  - LTP_425E5A3502541DE8
  - LTP_66C670178B06E9F3
  - LTP_6C14DE68E3C0CC24
  - LTP_74BB3F96CBA52D02
  - LTP_D246498B20D9CB2C
  - LTP_DA65D6C7A0E4ABBC
  static_checks:
  - STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS
  - STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO
  - STARRY_EPOLL_NESTED_LOOP
  - STARRY_FINIT_MODULE_FLAG_VALIDATION
  - STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE
  - STARRY_ROUND3_INIT_MODULE_PERMISSION
  dynamic_tests: []
historical_regression_unresolved: {}
content_hash: sha256:8c1364655b031bbb7fedf1013bd2502754b6ef539102e70eae23f9118e897b70
```
</details>
