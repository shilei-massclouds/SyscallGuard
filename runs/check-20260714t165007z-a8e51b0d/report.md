# Starry 合规检查报告

## 本轮结论

- 状态：`completed`
- 静态检查：pass 6、fail 0、error 0
- 动态测试：pass 0、fail 0、skipped 0、not_run 0
- confirmed finding：0
- 环境或执行 blocker：0（不视为实现缺口）

## 静态检查

### `STARRY_CLOSE_FD_TABLE`

- 类型：`static`
- 关联 syscall：`close`
- 通用规则：`LTP_09B39E9C9254ECB2`、`LTP_0CD17E662AFD2956`、`LTP_5CB803B873F78BA0`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn close_file_like\(fd: c_int\)[\s\S]*?FD_TABLE\.write\(\)\.remove\(fd as usize\)`：matched=`true`，第 307 行
  - `pub fn close_file_like\(fd: c_int\)[\s\S]*?return Ok\(\(\)\);[\s\S]*?Err\(AxError::BadFileDescriptor\)`：matched=`true`，第 307 行
- finding：—

### `STARRY_CLOSE_SYSCALL`

- 类型：`static`
- 关联 syscall：`close`
- 通用规则：`LTP_09B39E9C9254ECB2`、`LTP_0CD17E662AFD2956`、`LTP_5CB803B873F78BA0`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_close\(fd: c_int\)[\s\S]*?close_file_like\(fd\)\?;`：matched=`true`，第 441 行
  - `pub fn sys_close\(fd: c_int\)[\s\S]*?close_file_like\(fd\)\?;[\s\S]*?Ok\(0\)`：matched=`true`，第 441 行
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

### `STARRY_MMAP_ACCESS`

- 类型：`static`
- 关联 syscall：`mmap`
- 通用规则：`LTP_36C99C10CD38F8DB`、`LTP_45439D8F2BAB0832`、`LTP_52BAFC01DEA6E172`、`LTP_C346EFF1233F7061`、`LTP_F36F8C0CC1A6D840`、`LTP_FD1B65B0BCC88E0D`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `if needs_file_mmap_checks \{[\s\S]*?if !flags\.contains\(FileFlags::READ\) \{[\s\S]*?return Err\(AxError::PermissionDenied\);`：matched=`true`，第 229 行
  - `matches!\(map_type, MmapFlags::SHARED\)[\s\S]*?permission_flags\.contains\(MmapProt::WRITE\)[\s\S]*?if !flags\.contains\(FileFlags::WRITE\) \{[\s\S]*?return Err\(AxError::PermissionDenied\);`：matched=`true`，第 197 行
- finding：—

### `STARRY_MMAP_ARGUMENTS`

- 类型：`static`
- 关联 syscall：`mmap`
- 通用规则：`LTP_51E295101A9F4411`、`LTP_FEACDC300C3E1DD7`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_mmap\([\s\S]*?if length == 0 \{[\s\S]*?return Err\(AxError::InvalidInput\);`：matched=`true`，第 111 行
  - `let map_type = match flags & MmapFlags::TYPE\.bits\(\)[\s\S]*?_ => return Err\(AxError::InvalidInput\)`：matched=`true`，第 143 行
- finding：—

### `STARRY_MMAP_FD`

- 类型：`static`
- 关联 syscall：`mmap`
- 通用规则：`LTP_791DEA825D66980B`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `if !anonymous && fd < 0 \{[\s\S]*?return Err\(AxError::BadFileDescriptor\);`：matched=`true`，第 153 行
  - `let file = if anonymous \{[\s\S]*?None[\s\S]*?\} else \{[\s\S]*?Some\(get_file_like\(fd\)\?\)`：matched=`true`，第 186 行
- finding：—

## 动态测试

本轮没有动态测试。

<details>
<summary>机器可读元数据</summary>

<!-- syscallguard-metadata -->
```yaml
schema_version: 1
kind: syscallguard_check_report
report_id: check-20260714t165007z-a8e51b0d
status: completed
generated_at_utc: '2026-07-14T16:50:07.947066Z'
mapping_report_id: mapping-20260714t161033z-3dec139c
mapping_report_version:
  id: mapping-20260714t161033z-3dec139c
  generated_at_utc: '2026-07-14T16:14:51.791596Z'
  content_hash: sha256:de89c940b3cb12144da9a711bcd45c8bdcee82af49e28183aaae7c4594618184
target:
  target_id: starry
  repository: /home/cloud/gitLinux/tgoskits
  repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
  revision: HEAD
  worktree_root: /tmp/syscallguard-worktrees
  descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
  snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
input_hash: sha256:4c7adcbebfcdcc8a91277f12658e19fe7753982e6389266802390a7a0e767638
entity_hashes:
  rules:
    LTP_09B39E9C9254ECB2: sha256:09b39e9c9254ecb24ccb5288c3f12281e9adc0b698de5c706a4f071599c3ce60
    LTP_0CD17E662AFD2956: sha256:0cd17e662afd2956c8c1a42d49b46dca16c37c1972fc6d3632c05c317939a996
    LTP_36C99C10CD38F8DB: sha256:36c99c10cd38f8db26e721ea351430f0ebc4767b9a31257223ad8fd5519c7d0d
    LTP_45439D8F2BAB0832: sha256:45439d8f2bab0832027a39e78d024f72cc6449adff9fb823af60ff7c004d7bc5
    LTP_51E295101A9F4411: sha256:51e295101a9f4411b8c43521d430e85bd27ac1d7a96127b66675d7dc024ba9d2
    LTP_52BAFC01DEA6E172: sha256:52bafc01dea6e1725e71d23e11424031141e37ea07b99e151db6bcfc16116bde
    LTP_5CB803B873F78BA0: sha256:5cb803b873f78ba0c0cafe0d4ab7a0e69be0d150de939bbf030e0c66f583d1c6
    LTP_791DEA825D66980B: sha256:791dea825d66980bfded73936e4745cf7b914f20652b9489e65a7a59509b897b
    LTP_C346EFF1233F7061: sha256:c346eff1233f706172a595326e9215b63dd1f455b13880c762f92532db036e2e
    LTP_F36F8C0CC1A6D840: sha256:f36f8c0cc1a6d84025a2394e30fa1d7c273ce9c13d8f58d759383c75dbf8c10a
    LTP_FD1B65B0BCC88E0D: sha256:fd1b65b0bcc88e0d283d47737c8b9d244de44d7461e8efd5bc6eb699ebaa0d54
    LTP_FEACDC300C3E1DD7: sha256:feacdc300c3e1dd754c7925df645b95995a6f17fd0ebcb6a50578071e2f9636f
  static_checks:
    STARRY_CLOSE_FD_TABLE: sha256:c2a4f66437f46152892f704131da2405e6299203876b5152885f31f7ffeb2d23
    STARRY_CLOSE_SYSCALL: sha256:0c4804a0e1f7b77630d33127c5fbdd34638a9625cac7847821cf654ffe836eaf
    STARRY_ERRNO_TRANSLATION: sha256:5534265415b3a67ee5444497f79a373115fdab59a1a8d88e1faf0f0b387fc053
    STARRY_MMAP_ACCESS: sha256:ed8ff2e5c88f6013bb2dc3555d34922456aa7b8932d0a5fab3372aebfcdfd336
    STARRY_MMAP_ARGUMENTS: sha256:b6441cf0b2e64983d3588d8d6bf3b0875e3141a5477585aafbb8100d28cfe9a1
    STARRY_MMAP_FD: sha256:5e90be2726ddfc1ba2283b97a09d43daeabb55c4240a517ed6e7f3404bbc5241
  dynamic_tests: {}
entity_versions:
  rules:
    LTP_09B39E9C9254ECB2:
      id: LTP_09B39E9C9254ECB2
      generated_at_utc: '2026-07-14T13:35:02.567816Z'
      content_hash: sha256:09b39e9c9254ecb24ccb5288c3f12281e9adc0b698de5c706a4f071599c3ce60
    LTP_0CD17E662AFD2956:
      id: LTP_0CD17E662AFD2956
      generated_at_utc: '2026-07-14T13:35:02.567816Z'
      content_hash: sha256:0cd17e662afd2956c8c1a42d49b46dca16c37c1972fc6d3632c05c317939a996
    LTP_36C99C10CD38F8DB:
      id: LTP_36C99C10CD38F8DB
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:36c99c10cd38f8db26e721ea351430f0ebc4767b9a31257223ad8fd5519c7d0d
    LTP_45439D8F2BAB0832:
      id: LTP_45439D8F2BAB0832
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:45439d8f2bab0832027a39e78d024f72cc6449adff9fb823af60ff7c004d7bc5
    LTP_51E295101A9F4411:
      id: LTP_51E295101A9F4411
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:51e295101a9f4411b8c43521d430e85bd27ac1d7a96127b66675d7dc024ba9d2
    LTP_52BAFC01DEA6E172:
      id: LTP_52BAFC01DEA6E172
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:52bafc01dea6e1725e71d23e11424031141e37ea07b99e151db6bcfc16116bde
    LTP_5CB803B873F78BA0:
      id: LTP_5CB803B873F78BA0
      generated_at_utc: '2026-07-14T13:35:02.567816Z'
      content_hash: sha256:5cb803b873f78ba0c0cafe0d4ab7a0e69be0d150de939bbf030e0c66f583d1c6
    LTP_791DEA825D66980B:
      id: LTP_791DEA825D66980B
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:791dea825d66980bfded73936e4745cf7b914f20652b9489e65a7a59509b897b
    LTP_C346EFF1233F7061:
      id: LTP_C346EFF1233F7061
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:c346eff1233f706172a595326e9215b63dd1f455b13880c762f92532db036e2e
    LTP_F36F8C0CC1A6D840:
      id: LTP_F36F8C0CC1A6D840
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:f36f8c0cc1a6d84025a2394e30fa1d7c273ce9c13d8f58d759383c75dbf8c10a
    LTP_FD1B65B0BCC88E0D:
      id: LTP_FD1B65B0BCC88E0D
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:fd1b65b0bcc88e0d283d47737c8b9d244de44d7461e8efd5bc6eb699ebaa0d54
    LTP_FEACDC300C3E1DD7:
      id: LTP_FEACDC300C3E1DD7
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:feacdc300c3e1dd754c7925df645b95995a6f17fd0ebcb6a50578071e2f9636f
  static_checks:
    STARRY_CLOSE_FD_TABLE:
      id: STARRY_CLOSE_FD_TABLE
      generated_at_utc: '2026-07-14T16:14:51.791596Z'
      content_hash: sha256:c2a4f66437f46152892f704131da2405e6299203876b5152885f31f7ffeb2d23
    STARRY_CLOSE_SYSCALL:
      id: STARRY_CLOSE_SYSCALL
      generated_at_utc: '2026-07-14T16:14:51.791596Z'
      content_hash: sha256:0c4804a0e1f7b77630d33127c5fbdd34638a9625cac7847821cf654ffe836eaf
    STARRY_ERRNO_TRANSLATION:
      id: STARRY_ERRNO_TRANSLATION
      generated_at_utc: '2026-07-14T16:14:51.791596Z'
      content_hash: sha256:5534265415b3a67ee5444497f79a373115fdab59a1a8d88e1faf0f0b387fc053
    STARRY_MMAP_ACCESS:
      id: STARRY_MMAP_ACCESS
      generated_at_utc: '2026-07-14T16:14:51.791596Z'
      content_hash: sha256:ed8ff2e5c88f6013bb2dc3555d34922456aa7b8932d0a5fab3372aebfcdfd336
    STARRY_MMAP_ARGUMENTS:
      id: STARRY_MMAP_ARGUMENTS
      generated_at_utc: '2026-07-14T16:14:51.791596Z'
      content_hash: sha256:b6441cf0b2e64983d3588d8d6bf3b0875e3141a5477585aafbb8100d28cfe9a1
    STARRY_MMAP_FD:
      id: STARRY_MMAP_FD
      generated_at_utc: '2026-07-14T16:14:51.791596Z'
      content_hash: sha256:5e90be2726ddfc1ba2283b97a09d43daeabb55c4240a517ed6e7f3404bbc5241
  dynamic_tests: {}
execution_scope:
  rules:
  - LTP_09B39E9C9254ECB2
  - LTP_0CD17E662AFD2956
  - LTP_36C99C10CD38F8DB
  - LTP_45439D8F2BAB0832
  - LTP_51E295101A9F4411
  - LTP_52BAFC01DEA6E172
  - LTP_5CB803B873F78BA0
  - LTP_791DEA825D66980B
  - LTP_C346EFF1233F7061
  - LTP_F36F8C0CC1A6D840
  - LTP_FD1B65B0BCC88E0D
  - LTP_FEACDC300C3E1DD7
  static_checks:
  - STARRY_CLOSE_FD_TABLE
  - STARRY_CLOSE_SYSCALL
  - STARRY_ERRNO_TRANSLATION
  - STARRY_MMAP_ACCESS
  - STARRY_MMAP_ARGUMENTS
  - STARRY_MMAP_FD
  dynamic_tests: []
rule_syscalls:
  LTP_09B39E9C9254ECB2:
  - close
  LTP_0CD17E662AFD2956:
  - close
  LTP_36C99C10CD38F8DB:
  - mmap
  LTP_45439D8F2BAB0832:
  - mmap
  LTP_51E295101A9F4411:
  - mmap
  LTP_52BAFC01DEA6E172:
  - mmap
  LTP_5CB803B873F78BA0:
  - close
  LTP_791DEA825D66980B:
  - mmap
  LTP_C346EFF1233F7061:
  - mmap
  LTP_F36F8C0CC1A6D840:
  - mmap
  LTP_FD1B65B0BCC88E0D:
  - mmap
  LTP_FEACDC300C3E1DD7:
  - mmap
static:
- check_id: STARRY_CLOSE_FD_TABLE
  rule_refs:
  - LTP_09B39E9C9254ECB2
  - LTP_0CD17E662AFD2956
  - LTP_5CB803B873F78BA0
  result: pass
  path: os/StarryOS/kernel/src/file/mod.rs
  patterns:
  - label: close removes the descriptor from the current fd table
    regex: 'pub fn close_file_like\(fd: c_int\)[\s\S]*?FD_TABLE\.write\(\)\.remove\(fd as usize\)'
    matched: true
    line: 307
  - label: a removed descriptor succeeds and a missing descriptor is EBADF
    regex: 'pub fn close_file_like\(fd: c_int\)[\s\S]*?return Ok\(\(\)\);[\s\S]*?Err\(AxError::BadFileDescriptor\)'
    matched: true
    line: 307
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_CLOSE_SYSCALL
  rule_refs:
  - LTP_09B39E9C9254ECB2
  - LTP_0CD17E662AFD2956
  - LTP_5CB803B873F78BA0
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/fd_ops.rs
  patterns:
  - label: sys_close calls close_file_like and propagates errors
    regex: 'pub fn sys_close\(fd: c_int\)[\s\S]*?close_file_like\(fd\)\?;'
    matched: true
    line: 441
  - label: successful close returns zero
    regex: 'pub fn sys_close\(fd: c_int\)[\s\S]*?close_file_like\(fd\)\?;[\s\S]*?Ok\(0\)'
    matched: true
    line: 441
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
    line: 229
  - label: shared writable mappings additionally require fd write access
    regex: matches!\(map_type, MmapFlags::SHARED\)[\s\S]*?permission_flags\.contains\(MmapProt::WRITE\)[\s\S]*?if
      !flags\.contains\(FileFlags::WRITE\) \{[\s\S]*?return Err\(AxError::PermissionDenied\);
    matched: true
    line: 197
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
    line: 111
  - label: map type must be shared private or shared validate
    regex: let map_type = match flags & MmapFlags::TYPE\.bits\(\)[\s\S]*?_ => return Err\(AxError::InvalidInput\)
    matched: true
    line: 143
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
    line: 153
  - label: non-anonymous mmap resolves the descriptor through get_file_like
    regex: let file = if anonymous \{[\s\S]*?None[\s\S]*?\} else \{[\s\S]*?Some\(get_file_like\(fd\)\?\)
    matched: true
    line: 186
  reason: all required patterns matched
  finding_ids: []
dynamic: []
counts:
  static_pass: 6
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
content_hash: sha256:d61ccf768d6f02c467b5a640981598fd82e1837a0b512e59493c26dc8e021e10
```
</details>
