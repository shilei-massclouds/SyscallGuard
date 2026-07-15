# Starry 合规检查报告

## 本轮结论

- 状态：`completed`
- 静态检查：pass 8、fail 0、error 0
- 动态测试：pass 0、fail 0、skipped 0、not_run 0
- confirmed finding：0
- 环境或执行 blocker：0（不视为实现缺口）

## 静态检查

### `STARRY_ACCESS_PATH_RESOLUTION`

- 类型：`static`
- 关联 syscall：`access`
- 通用规则：`LTP_2F99FA84C445363C`、`LTP_4661BBF1B3CD3A1E`、`LTP_8BB576EB2E1E6B23`、`LTP_C8DAE34819E335F8`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `let path = path\.nullable\(\)\.map\(vm_load_path_string\)\.transpose\(\)\?;[\s\S]*?let file = resolve_at\(dirfd, path\.as_deref\(\), flags\)\?;`：matched=`true`，第 71 行
  - `let file = resolve_at\(dirfd, path\.as_deref\(\), flags\)\?;[\s\S]*?if mode == 0 \{[\s\S]*?return Ok\(0\);`：matched=`true`，第 160 行
- finding：—

### `STARRY_ACCESS_PERMISSIONS`

- 类型：`static`
- 关联 syscall：`access`
- 通用规则：`LTP_0180982614AA9F7D`、`LTP_044E7C11E6B503BB`、`LTP_06891E2E299CF48E`、`LTP_0D1782EAAC26DEB4`、`LTP_67BF94A4ACD303C4`、`LTP_711D5693356A79F2`、`LTP_73DF50509BCC128B`、`LTP_839EC7BC904E42D5`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_access\([\s\S]*?sys_faccessat2\(AT_FDCWD, path, mode, 0\)`：matched=`true`，第 138 行
  - `const FACCESSAT2_VALID_MODE: u32 = R_OK \\| W_OK \\| X_OK;[\s\S]*?if mode & !FACCESSAT2_VALID_MODE != 0[\s\S]*?if mode == 0 \{[\s\S]*?return Ok\(0\);`：matched=`true`，第 152 行
  - `if cred\.fsuid == 0 \{[\s\S]*?mode & X_OK[\s\S]*?perm_bits & any_exec == 0[\s\S]*?return Err\(AxError::PermissionDenied\);[\s\S]*?return Ok\(0\);`：matched=`true`，第 170 行
  - `let effective_bits = if cred\.fsuid == file_uid[\s\S]*?cred\.fsgid == file_gid \\|\\| cred\.groups\.contains\(&file_gid\)[\s\S]*?mode & R_OK[\s\S]*?effective_bits & 4 == 0[\s\S]*?mode & W_OK[\s\S]*?effective_bits & 2 == 0[\s\S]*?mode & X_OK[\s\S]*?effective_bits & 1 == 0`：matched=`true`，第 189 行
- finding：—

### `STARRY_ACCESS_USER_POINTER`

- 类型：`static`
- 关联 syscall：`access`
- 通用规则：`LTP_075318C437B76E06`、`LTP_0799FC60BADD2B18`、`LTP_38FB918826669241`、`LTP_58416E6747519699`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `let path = path\.nullable\(\)\.map\(vm_load_path_string\)\.transpose\(\)\?;[\s\S]*?let file = resolve_at\(dirfd, path\.as_deref\(\), flags\)\?;`：matched=`true`，第 71 行
- finding：—

### `STARRY_BATCH_ERRNO_TRANSLATION`

- 类型：`static`
- 关联 syscall：`access`、`capget`、`capset`、`chroot`
- 通用规则：`LTP_075318C437B76E06`、`LTP_0799FC60BADD2B18`、`LTP_245CD61DAA19DC98`、`LTP_2F99FA84C445363C`、`LTP_38FB918826669241`、`LTP_4661BBF1B3CD3A1E`、`LTP_58416E6747519699`、`LTP_5F1D35ACCEFD4971`、`LTP_6D86AFD541A61388`、`LTP_71C54C624831C7F0`、`LTP_827CE5CB448A411B`、`LTP_8BB576EB2E1E6B23`、`LTP_99DF5C34778032E1`、`LTP_C8DAE34819E335F8`、`LTP_E06D53042C10C99E`、`LTP_EBD54180D0CAB16B`、`LTP_FF9C0F9669A39525`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `BadAddress \\| BadState => EFAULT`：matched=`true`，第 223 行
  - `NotFound => ENOENT`：matched=`true`，第 249 行
  - `NotADirectory => ENOTDIR`：matched=`true`，第 243 行
  - `FilesystemLoop => ELOOP`：matched=`true`，第 230 行
  - `NameTooLong => ENAMETOOLONG`：matched=`true`，第 238 行
  - `PermissionDenied => EACCES`：matched=`true`，第 253 行
  - `InvalidInput \\| InvalidData => EINVAL`：matched=`true`，第 235 行
- finding：—

### `STARRY_BRK_HEAP`

- 类型：`static`
- 关联 syscall：`brk`
- 通用规则：`LTP_7A74A699442CEB99`、`LTP_E3E59B16A96A60BC`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `if addr == 0 \{[\s\S]*?return Ok\(current_top as isize\);[\s\S]*?if !\(USER_HEAP_BASE\.\.=USER_HEAP_BASE \+ USER_HEAP_SIZE_MAX\)\.contains\(&addr\) \{[\s\S]*?return Ok\(current_top as isize\);`：matched=`true`，第 19 行
  - `if new_top_aligned > current_top_aligned \{[\s\S]*?\.map\([\s\S]*?\)\s*\.is_err\(\)[\s\S]*?else if new_top_aligned < current_top_aligned \{[\s\S]*?\.unmap\(shrink_start, shrink_size\)[\s\S]*?\.is_err\(\)`：matched=`true`，第 52 行
  - `proc_data\.set_heap_top\(addr\);[\s\S]*?Ok\(addr as isize\)`：matched=`true`，第 89 行
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

### `STARRY_CHROOT_PATH`

- 类型：`static`
- 关联 syscall：`chroot`
- 通用规则：`LTP_245CD61DAA19DC98`、`LTP_71C54C624831C7F0`、`LTP_99DF5C34778032E1`、`LTP_EBD54180D0CAB16B`、`LTP_EE7A979F212D6C0C`、`LTP_FF9C0F9669A39525`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_chroot\(path: \*const c_char\)[\s\S]*?vm_load_string\(path\)\?[\s\S]*?fs\.resolve\(path\)\?`：matched=`true`，第 114 行
  - `if loc\.node_type\(\) != NodeType::Directory \{[\s\S]*?return Err\(AxError::NotADirectory\);`：matched=`true`，第 120 行
  - `\*fs = FsContext::new\(loc\);[\s\S]*?Ok\(0\)`：matched=`true`，第 123 行
- finding：—

## 动态测试

本轮没有动态测试。

<details>
<summary>机器可读元数据</summary>

<!-- syscallguard-metadata -->
```yaml
schema_version: 1
kind: syscallguard_check_report
report_id: check-20260715t051552z-22c78d25
status: completed
generated_at_utc: '2026-07-15T05:15:53.793290Z'
mapping_report_id: mapping-20260715t035919z-aa4629b5
mapping_report_version:
  id: mapping-20260715t035919z-aa4629b5
  generated_at_utc: '2026-07-15T04:13:20.108411Z'
  content_hash: sha256:b506a2cb9eb425981ca227f4820c9642668426c5f1ec619f4669b5d1be33dd40
target:
  target_id: starry
  repository: /home/cloud/gitLinux/tgoskits
  repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
  revision: HEAD
  worktree_root: /tmp/syscallguard-worktrees
  descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
  snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
input_hash: sha256:3892098ee3029a0eff8a5524f23a6d83f1be80dd14de56d69392276e8aa9c898
entity_hashes:
  rules:
    LTP_0180982614AA9F7D: sha256:0180982614aa9f7deb01d61e1891fc76f80a5dd2c63dd0b04340bb29d02ed2a5
    LTP_044E7C11E6B503BB: sha256:044e7c11e6b503bb657c1f5d568942154575515e5bd090cfb272ebd5b2953217
    LTP_06891E2E299CF48E: sha256:06891e2e299cf48e89e834978cafb8d3f54a5f988367d5ac9c5daf94202c0532
    LTP_075318C437B76E06: sha256:075318c437b76e067682a9c6aab95a64558daf471c20df7205f62a72b1fd82ee
    LTP_0799FC60BADD2B18: sha256:0799fc60badd2b189b242a57ba5740cd832aa2477cbe8497f5b09324880ca7f4
    LTP_0D1782EAAC26DEB4: sha256:0d1782eaac26deb423a13b1bef2c3fc0e4647c3d464451e818c877ae67a0c0b9
    LTP_208C833FF12217F5: sha256:208c833ff12217f5ee10c2893ca4aab718793f8504783e4c1e69970fe3fc01dc
    LTP_245CD61DAA19DC98: sha256:245cd61daa19dc987195efcf282a428df3dfc7429cd89bcc1fbc741e96407c30
    LTP_2F99FA84C445363C: sha256:2f99fa84c445363ccdb31044c1a489fb3da71ffb0efca79bea63770a584e2bde
    LTP_38FB918826669241: sha256:38fb918826669241ebbe77827a90f4347f124cf6de78fd4f4b46b3495fb3ab2f
    LTP_4661BBF1B3CD3A1E: sha256:4661bbf1b3cd3a1ed9794183dd018046d195e23d06cfc4a8e2fa282fef66c737
    LTP_58416E6747519699: sha256:58416e6747519699e7b507fc0ff7e8c00852ff81eaff2cf425bb2d4a84e4e6f3
    LTP_5F1D35ACCEFD4971: sha256:5f1d35accefd49711e3b8b82de258ecb2f04bba65083b919659edb660948ef2f
    LTP_67BF94A4ACD303C4: sha256:67bf94a4acd303c4bf5ee873c38bf51c6656dd4b572784d258639f552e8c49d3
    LTP_6D86AFD541A61388: sha256:6d86afd541a613880ff94fbbb7fbfdbbebd5fd32d94544f7cc6e3f2ee850df77
    LTP_711D5693356A79F2: sha256:711d5693356a79f2f78c29dc066b0de731afab838d59939646e4e7b1b2e98a60
    LTP_71C54C624831C7F0: sha256:71c54c624831c7f01c5ac8d48046dc370b784af8dc2099633843d4269593e9f7
    LTP_73DF50509BCC128B: sha256:73df50509bcc128b1b669bc1dbf328da4c2eeccbf411699638eea46f6a5ffbe5
    LTP_7A74A699442CEB99: sha256:7a74a699442ceb99b8495ac52144744c5a7e995035d4c06a10971ce532e8e954
    LTP_827CE5CB448A411B: sha256:827ce5cb448a411bcd82f3a89e9c733eb11fa4d44a8f563ff1658dac81bd73a4
    LTP_839EC7BC904E42D5: sha256:839ec7bc904e42d51fd03abcb0ea65b5030acf961067619e228750577be93c2f
    LTP_8BB576EB2E1E6B23: sha256:8bb576eb2e1e6b23ecfe5c8b7d2bb21eb7fba161f200ce874a6282e806ee9180
    LTP_99DF5C34778032E1: sha256:99df5c34778032e1483871676a4cbb8fc57a3bbfcd2fd0c74f90f83147e1a5f8
    LTP_C8DAE34819E335F8: sha256:c8dae34819e335f88d2bad8650e2067ec51e8a1c6d21ef37198241a9af5a56f2
    LTP_E06D53042C10C99E: sha256:e06d53042c10c99e7bdc61242d4ac56e1aace8c13e3442e875e2574ca74e60d3
    LTP_E3E59B16A96A60BC: sha256:e3e59b16a96a60bce3de89603588b78a310e40b3710e530d67d5c30160121e86
    LTP_EBD54180D0CAB16B: sha256:ebd54180d0cab16b9271d149769e3e3e522ef97222514360017b81114bcc90e1
    LTP_EC23768761E40E9F: sha256:ec23768761e40e9f99140715f9e6147dcc348f9f7bbdc7731948b1afb6d29d51
    LTP_EE7A979F212D6C0C: sha256:ee7a979f212d6c0c9e2e3e7cf8fe3078537cd1d9a5e51d2b9d1800e88e29a363
    LTP_FF9C0F9669A39525: sha256:ff9c0f9669a39525986267a75a9b66e6249d23f8939029c388c3f8f1c9ec1472
  static_checks:
    STARRY_ACCESS_PATH_RESOLUTION: sha256:896f2b8f806c19bafee558addd47df7692321be39551b0da996b9c942907a805
    STARRY_ACCESS_PERMISSIONS: sha256:9a2f8a7c6a97cb3e0bb0faa21d342b618172c583039ca74535fe0f394fa364bd
    STARRY_ACCESS_USER_POINTER: sha256:1df5a8a335cbf4e4f9bd77c4078ca8ef9f1a642feba46a2c79cea6aec66df23c
    STARRY_BATCH_ERRNO_TRANSLATION: sha256:e19f574ad1b857afc459fe1d55fbe4e71451eceeeeff1452ff74c6c7fec81a15
    STARRY_BRK_HEAP: sha256:08b3a24f292c0c2d933bf711c00c866ab3a74a54f291c4ddee9460d0eb6f43ac
    STARRY_CAPGET_ABI: sha256:9a7cf39c2be08e7a05c61f4ecfdb857e5ec45b702956c945d8c51b07cffde003
    STARRY_CAPSET_ABI: sha256:fa04e3f3a184e594c6b2b6f1f9d43027f9104bdc8a675eb3555d76e5cfb0faed
    STARRY_CHROOT_PATH: sha256:357fbab1f149ef6fb3807966810bffa3366973f2c4f2c854bb821004e4a3753f
  dynamic_tests: {}
entity_versions:
  rules:
    LTP_0180982614AA9F7D:
      id: LTP_0180982614AA9F7D
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:0180982614aa9f7deb01d61e1891fc76f80a5dd2c63dd0b04340bb29d02ed2a5
    LTP_044E7C11E6B503BB:
      id: LTP_044E7C11E6B503BB
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:044e7c11e6b503bb657c1f5d568942154575515e5bd090cfb272ebd5b2953217
    LTP_06891E2E299CF48E:
      id: LTP_06891E2E299CF48E
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:06891e2e299cf48e89e834978cafb8d3f54a5f988367d5ac9c5daf94202c0532
    LTP_075318C437B76E06:
      id: LTP_075318C437B76E06
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:075318c437b76e067682a9c6aab95a64558daf471c20df7205f62a72b1fd82ee
    LTP_0799FC60BADD2B18:
      id: LTP_0799FC60BADD2B18
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:0799fc60badd2b189b242a57ba5740cd832aa2477cbe8497f5b09324880ca7f4
    LTP_0D1782EAAC26DEB4:
      id: LTP_0D1782EAAC26DEB4
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:0d1782eaac26deb423a13b1bef2c3fc0e4647c3d464451e818c877ae67a0c0b9
    LTP_208C833FF12217F5:
      id: LTP_208C833FF12217F5
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:208c833ff12217f5ee10c2893ca4aab718793f8504783e4c1e69970fe3fc01dc
    LTP_245CD61DAA19DC98:
      id: LTP_245CD61DAA19DC98
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:245cd61daa19dc987195efcf282a428df3dfc7429cd89bcc1fbc741e96407c30
    LTP_2F99FA84C445363C:
      id: LTP_2F99FA84C445363C
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:2f99fa84c445363ccdb31044c1a489fb3da71ffb0efca79bea63770a584e2bde
    LTP_38FB918826669241:
      id: LTP_38FB918826669241
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:38fb918826669241ebbe77827a90f4347f124cf6de78fd4f4b46b3495fb3ab2f
    LTP_4661BBF1B3CD3A1E:
      id: LTP_4661BBF1B3CD3A1E
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:4661bbf1b3cd3a1ed9794183dd018046d195e23d06cfc4a8e2fa282fef66c737
    LTP_58416E6747519699:
      id: LTP_58416E6747519699
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:58416e6747519699e7b507fc0ff7e8c00852ff81eaff2cf425bb2d4a84e4e6f3
    LTP_5F1D35ACCEFD4971:
      id: LTP_5F1D35ACCEFD4971
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:5f1d35accefd49711e3b8b82de258ecb2f04bba65083b919659edb660948ef2f
    LTP_67BF94A4ACD303C4:
      id: LTP_67BF94A4ACD303C4
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:67bf94a4acd303c4bf5ee873c38bf51c6656dd4b572784d258639f552e8c49d3
    LTP_6D86AFD541A61388:
      id: LTP_6D86AFD541A61388
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:6d86afd541a613880ff94fbbb7fbfdbbebd5fd32d94544f7cc6e3f2ee850df77
    LTP_711D5693356A79F2:
      id: LTP_711D5693356A79F2
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:711d5693356a79f2f78c29dc066b0de731afab838d59939646e4e7b1b2e98a60
    LTP_71C54C624831C7F0:
      id: LTP_71C54C624831C7F0
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:71c54c624831c7f01c5ac8d48046dc370b784af8dc2099633843d4269593e9f7
    LTP_73DF50509BCC128B:
      id: LTP_73DF50509BCC128B
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:73df50509bcc128b1b669bc1dbf328da4c2eeccbf411699638eea46f6a5ffbe5
    LTP_7A74A699442CEB99:
      id: LTP_7A74A699442CEB99
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:7a74a699442ceb99b8495ac52144744c5a7e995035d4c06a10971ce532e8e954
    LTP_827CE5CB448A411B:
      id: LTP_827CE5CB448A411B
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:827ce5cb448a411bcd82f3a89e9c733eb11fa4d44a8f563ff1658dac81bd73a4
    LTP_839EC7BC904E42D5:
      id: LTP_839EC7BC904E42D5
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:839ec7bc904e42d51fd03abcb0ea65b5030acf961067619e228750577be93c2f
    LTP_8BB576EB2E1E6B23:
      id: LTP_8BB576EB2E1E6B23
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:8bb576eb2e1e6b23ecfe5c8b7d2bb21eb7fba161f200ce874a6282e806ee9180
    LTP_99DF5C34778032E1:
      id: LTP_99DF5C34778032E1
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:99df5c34778032e1483871676a4cbb8fc57a3bbfcd2fd0c74f90f83147e1a5f8
    LTP_C8DAE34819E335F8:
      id: LTP_C8DAE34819E335F8
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:c8dae34819e335f88d2bad8650e2067ec51e8a1c6d21ef37198241a9af5a56f2
    LTP_E06D53042C10C99E:
      id: LTP_E06D53042C10C99E
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:e06d53042c10c99e7bdc61242d4ac56e1aace8c13e3442e875e2574ca74e60d3
    LTP_E3E59B16A96A60BC:
      id: LTP_E3E59B16A96A60BC
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:e3e59b16a96a60bce3de89603588b78a310e40b3710e530d67d5c30160121e86
    LTP_EBD54180D0CAB16B:
      id: LTP_EBD54180D0CAB16B
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ebd54180d0cab16b9271d149769e3e3e522ef97222514360017b81114bcc90e1
    LTP_EC23768761E40E9F:
      id: LTP_EC23768761E40E9F
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ec23768761e40e9f99140715f9e6147dcc348f9f7bbdc7731948b1afb6d29d51
    LTP_EE7A979F212D6C0C:
      id: LTP_EE7A979F212D6C0C
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ee7a979f212d6c0c9e2e3e7cf8fe3078537cd1d9a5e51d2b9d1800e88e29a363
    LTP_FF9C0F9669A39525:
      id: LTP_FF9C0F9669A39525
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ff9c0f9669a39525986267a75a9b66e6249d23f8939029c388c3f8f1c9ec1472
  static_checks:
    STARRY_ACCESS_PATH_RESOLUTION:
      id: STARRY_ACCESS_PATH_RESOLUTION
      generated_at_utc: '2026-07-15T04:13:20.108411Z'
      content_hash: sha256:896f2b8f806c19bafee558addd47df7692321be39551b0da996b9c942907a805
    STARRY_ACCESS_PERMISSIONS:
      id: STARRY_ACCESS_PERMISSIONS
      generated_at_utc: '2026-07-15T04:13:20.108411Z'
      content_hash: sha256:9a2f8a7c6a97cb3e0bb0faa21d342b618172c583039ca74535fe0f394fa364bd
    STARRY_ACCESS_USER_POINTER:
      id: STARRY_ACCESS_USER_POINTER
      generated_at_utc: '2026-07-15T04:13:20.108411Z'
      content_hash: sha256:1df5a8a335cbf4e4f9bd77c4078ca8ef9f1a642feba46a2c79cea6aec66df23c
    STARRY_BATCH_ERRNO_TRANSLATION:
      id: STARRY_BATCH_ERRNO_TRANSLATION
      generated_at_utc: '2026-07-15T04:13:20.108411Z'
      content_hash: sha256:e19f574ad1b857afc459fe1d55fbe4e71451eceeeeff1452ff74c6c7fec81a15
    STARRY_BRK_HEAP:
      id: STARRY_BRK_HEAP
      generated_at_utc: '2026-07-15T04:13:20.108411Z'
      content_hash: sha256:08b3a24f292c0c2d933bf711c00c866ab3a74a54f291c4ddee9460d0eb6f43ac
    STARRY_CAPGET_ABI:
      id: STARRY_CAPGET_ABI
      generated_at_utc: '2026-07-15T04:13:20.108411Z'
      content_hash: sha256:9a7cf39c2be08e7a05c61f4ecfdb857e5ec45b702956c945d8c51b07cffde003
    STARRY_CAPSET_ABI:
      id: STARRY_CAPSET_ABI
      generated_at_utc: '2026-07-15T04:13:20.108411Z'
      content_hash: sha256:fa04e3f3a184e594c6b2b6f1f9d43027f9104bdc8a675eb3555d76e5cfb0faed
    STARRY_CHROOT_PATH:
      id: STARRY_CHROOT_PATH
      generated_at_utc: '2026-07-15T04:13:20.108411Z'
      content_hash: sha256:357fbab1f149ef6fb3807966810bffa3366973f2c4f2c854bb821004e4a3753f
  dynamic_tests: {}
execution_scope:
  rules:
  - LTP_0180982614AA9F7D
  - LTP_044E7C11E6B503BB
  - LTP_06891E2E299CF48E
  - LTP_075318C437B76E06
  - LTP_0799FC60BADD2B18
  - LTP_0D1782EAAC26DEB4
  - LTP_208C833FF12217F5
  - LTP_245CD61DAA19DC98
  - LTP_2F99FA84C445363C
  - LTP_38FB918826669241
  - LTP_4661BBF1B3CD3A1E
  - LTP_58416E6747519699
  - LTP_5F1D35ACCEFD4971
  - LTP_67BF94A4ACD303C4
  - LTP_6D86AFD541A61388
  - LTP_711D5693356A79F2
  - LTP_71C54C624831C7F0
  - LTP_73DF50509BCC128B
  - LTP_7A74A699442CEB99
  - LTP_827CE5CB448A411B
  - LTP_839EC7BC904E42D5
  - LTP_8BB576EB2E1E6B23
  - LTP_99DF5C34778032E1
  - LTP_C8DAE34819E335F8
  - LTP_E06D53042C10C99E
  - LTP_E3E59B16A96A60BC
  - LTP_EBD54180D0CAB16B
  - LTP_EC23768761E40E9F
  - LTP_EE7A979F212D6C0C
  - LTP_FF9C0F9669A39525
  static_checks:
  - STARRY_ACCESS_PATH_RESOLUTION
  - STARRY_ACCESS_PERMISSIONS
  - STARRY_ACCESS_USER_POINTER
  - STARRY_BATCH_ERRNO_TRANSLATION
  - STARRY_BRK_HEAP
  - STARRY_CAPGET_ABI
  - STARRY_CAPSET_ABI
  - STARRY_CHROOT_PATH
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
  LTP_0F901C62092CC7B8:
  - access
  LTP_10A684C1C2D2DE0F:
  - access
  LTP_10FE1313FBAB5F92:
  - access
  LTP_1325C077A1CDE514:
  - cachestat
  LTP_1402459B5FF9BF23:
  - access
  LTP_1465554B09CE14F0:
  - access
  LTP_148623FDAF4E478D:
  - access
  LTP_153B296FA599E0CE:
  - access
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
  LTP_2B4171DD8FBD982A:
  - access
  LTP_2D0BAECAE4F61432:
  - access
  LTP_2E5D530A61E60934:
  - access
  LTP_2F99FA84C445363C:
  - access
  LTP_2FA43CD942AE7AD6:
  - access
  LTP_2FE8FAD800DE41F6:
  - access
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
  LTP_38FB918826669241:
  - access
  LTP_3900F4E562AE09D1:
  - access
  LTP_3916A669595B3568:
  - access
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
  LTP_4CFAFCE7FCA2BF99:
  - access
  LTP_4ECB786BFA071AAC:
  - access
  LTP_50A86D4D5411356E:
  - access
  LTP_50F858A3CBF95EED:
  - chroot
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
  LTP_5A315335586D4227:
  - access
  LTP_5C5CDC165410C08C:
  - access
  LTP_5CB803B873F78BA0:
  - close
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
  LTP_752C9A802CF96B8B:
  - access
  LTP_76A9B6CF388A8609:
  - alarm
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
  LTP_7CE7876CE69F200F:
  - access
  LTP_7DD493976CBC9A31:
  - access
  LTP_7DEDC53AC33C891F:
  - capset
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
  LTP_9C9D222A34799D55:
  - access
  LTP_9CA9C6B61C3317A3:
  - accept
  LTP_9CDCD3C4BA6C2702:
  - access
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
  LTP_BC662075E3BAE807:
  - access
  LTP_BE2E778739EF01D5:
  - access
  LTP_C0577C0D678214DA:
  - access
  LTP_C071A7FFF929A2A5:
  - access
  LTP_C0AA45BC29F98A0E:
  - access
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
  LTP_CCDB1776DAA2C318:
  - access
  LTP_CD2150BE4FE81F31:
  - alarm
  LTP_CDCDC1B9E63D58C3:
  - access
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
  LTP_DC9BC72148835FDC:
  - capget
  LTP_DCB33BB29D296843:
  - access
  LTP_DD9A41090E3D5A17:
  - access
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
  LTP_E560C027210BF20A:
  - access
  LTP_E5791B389C67677E:
  - access
  LTP_E5E50FB7BDD033D9:
  - access
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
  LTP_ED36488372A175F5:
  - access
  LTP_ED3F2AE7E59E6F12:
  - access
  LTP_EE1518958A8F7CC1:
  - access
  LTP_EE7A979F212D6C0C:
  - chroot
  LTP_EF5C1F365208AD31:
  - access
  LTP_F1044C71B6626419:
  - accept
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
- check_id: STARRY_ACCESS_PATH_RESOLUTION
  rule_refs:
  - LTP_2F99FA84C445363C
  - LTP_4661BBF1B3CD3A1E
  - LTP_8BB576EB2E1E6B23
  - LTP_C8DAE34819E335F8
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/stat.rs
  patterns:
  - label: checked pathname flows into resolve_at
    regex: let path = path\.nullable\(\)\.map\(vm_load_path_string\)\.transpose\(\)\?;[\s\S]*?let file
      = resolve_at\(dirfd, path\.as_deref\(\), flags\)\?;
    matched: true
    line: 71
  - label: existence mode returns only after successful resolution
    regex: let file = resolve_at\(dirfd, path\.as_deref\(\), flags\)\?;[\s\S]*?if mode == 0 \{[\s\S]*?return
      Ok\(0\);
    matched: true
    line: 160
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ACCESS_PERMISSIONS
  rule_refs:
  - LTP_0180982614AA9F7D
  - LTP_044E7C11E6B503BB
  - LTP_06891E2E299CF48E
  - LTP_0D1782EAAC26DEB4
  - LTP_67BF94A4ACD303C4
  - LTP_711D5693356A79F2
  - LTP_73DF50509BCC128B
  - LTP_839EC7BC904E42D5
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/stat.rs
  patterns:
  - label: access delegates to faccessat2
    regex: pub fn sys_access\([\s\S]*?sys_faccessat2\(AT_FDCWD, path, mode, 0\)
    matched: true
    line: 138
  - label: valid mode mask and F_OK success
    regex: 'const FACCESSAT2_VALID_MODE: u32 = R_OK \| W_OK \| X_OK;[\s\S]*?if mode & !FACCESSAT2_VALID_MODE
      != 0[\s\S]*?if mode == 0 \{[\s\S]*?return Ok\(0\);'
    matched: true
    line: 152
  - label: root permission behavior
    regex: if cred\.fsuid == 0 \{[\s\S]*?mode & X_OK[\s\S]*?perm_bits & any_exec == 0[\s\S]*?return Err\(AxError::PermissionDenied\);[\s\S]*?return
      Ok\(0\);
    matched: true
    line: 170
  - label: owner group other effective bits enforce R W X
    regex: let effective_bits = if cred\.fsuid == file_uid[\s\S]*?cred\.fsgid == file_gid \|\| cred\.groups\.contains\(&file_gid\)[\s\S]*?mode
      & R_OK[\s\S]*?effective_bits & 4 == 0[\s\S]*?mode & W_OK[\s\S]*?effective_bits & 2 == 0[\s\S]*?mode
      & X_OK[\s\S]*?effective_bits & 1 == 0
    matched: true
    line: 189
  reason: all required patterns matched
  finding_ids: []
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
- check_id: STARRY_BATCH_ERRNO_TRANSLATION
  rule_refs:
  - LTP_075318C437B76E06
  - LTP_0799FC60BADD2B18
  - LTP_245CD61DAA19DC98
  - LTP_2F99FA84C445363C
  - LTP_38FB918826669241
  - LTP_4661BBF1B3CD3A1E
  - LTP_58416E6747519699
  - LTP_5F1D35ACCEFD4971
  - LTP_6D86AFD541A61388
  - LTP_71C54C624831C7F0
  - LTP_827CE5CB448A411B
  - LTP_8BB576EB2E1E6B23
  - LTP_99DF5C34778032E1
  - LTP_C8DAE34819E335F8
  - LTP_E06D53042C10C99E
  - LTP_EBD54180D0CAB16B
  - LTP_FF9C0F9669A39525
  result: pass
  path: components/axerrno/src/lib.rs
  patterns:
  - label: bad user memory maps to EFAULT
    regex: BadAddress \| BadState => EFAULT
    matched: true
    line: 223
  - label: missing paths map to ENOENT
    regex: NotFound => ENOENT
    matched: true
    line: 249
  - label: non directory components map to ENOTDIR
    regex: NotADirectory => ENOTDIR
    matched: true
    line: 243
  - label: symlink loops map to ELOOP
    regex: FilesystemLoop => ELOOP
    matched: true
    line: 230
  - label: overlong names map to ENAMETOOLONG
    regex: NameTooLong => ENAMETOOLONG
    matched: true
    line: 238
  - label: permission denial maps to EACCES
    regex: PermissionDenied => EACCES
    matched: true
    line: 253
  - label: invalid input maps to EINVAL
    regex: InvalidInput \| InvalidData => EINVAL
    matched: true
    line: 235
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_BRK_HEAP
  rule_refs:
  - LTP_7A74A699442CEB99
  - LTP_E3E59B16A96A60BC
  result: pass
  path: os/StarryOS/kernel/src/syscall/mm/brk.rs
  patterns:
  - label: zero and out of range requests preserve Linux return semantics
    regex: if addr == 0 \{[\s\S]*?return Ok\(current_top as isize\);[\s\S]*?if !\(USER_HEAP_BASE\.\.=USER_HEAP_BASE
      \+ USER_HEAP_SIZE_MAX\)\.contains\(&addr\) \{[\s\S]*?return Ok\(current_top as isize\);
    matched: true
    line: 19
  - label: expansion and shrink update the address space
    regex: if new_top_aligned > current_top_aligned \{[\s\S]*?\.map\([\s\S]*?\)\s*\.is_err\(\)[\s\S]*?else
      if new_top_aligned < current_top_aligned \{[\s\S]*?\.unmap\(shrink_start, shrink_size\)[\s\S]*?\.is_err\(\)
    matched: true
    line: 52
  - label: successful request records and returns the new break
    regex: proc_data\.set_heap_top\(addr\);[\s\S]*?Ok\(addr as isize\)
    matched: true
    line: 89
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
- check_id: STARRY_CHROOT_PATH
  rule_refs:
  - LTP_245CD61DAA19DC98
  - LTP_71C54C624831C7F0
  - LTP_99DF5C34778032E1
  - LTP_EBD54180D0CAB16B
  - LTP_EE7A979F212D6C0C
  - LTP_FF9C0F9669A39525
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/ctl.rs
  patterns:
  - label: user pathname is loaded and resolved
    regex: 'pub fn sys_chroot\(path: \*const c_char\)[\s\S]*?vm_load_string\(path\)\?[\s\S]*?fs\.resolve\(path\)\?'
    matched: true
    line: 114
  - label: non directories are rejected
    regex: if loc\.node_type\(\) != NodeType::Directory \{[\s\S]*?return Err\(AxError::NotADirectory\);
    matched: true
    line: 120
  - label: valid directory becomes the new filesystem context
    regex: \*fs = FsContext::new\(loc\);[\s\S]*?Ok\(0\)
    matched: true
    line: 123
  reason: all required patterns matched
  finding_ids: []
dynamic: []
counts:
  static_pass: 8
  static_fail: 0
  static_error: 0
  dynamic_pass: 0
  dynamic_fail: 0
  dynamic_skipped: 0
  dynamic_not_run: 0
  findings: 0
  blockers: 0
blockers: []
finding_ids: []
finding_versions: {}
content_hash: sha256:ac8325379016c08eecc4174961751f49c748ea9ad898c494ad0738cad919fcee
```
</details>
