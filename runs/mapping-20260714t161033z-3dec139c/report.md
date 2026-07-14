# Starry 规则映射报告

## 本轮结论

- 本轮产生静态检查：6
- 本轮产生动态测试：0
- 全局剩余规则：0（pending 0、needs_review 0、unsupported 0）

## 完整规则关系

### `close`

| rule_id | 静态检查 | 动态测试 | 状态 | 原因 |
| --- | --- | --- | --- | --- |
| `LTP_09B39E9C9254ECB2` | `STARRY_CLOSE_FD_TABLE`、`STARRY_CLOSE_SYSCALL`、`STARRY_ERRNO_TRANSLATION` | — | `covered` | sys_close 传播 fd 表删除结果；已关闭 fd 不在表中，映射为 EBADF。 |
| `LTP_0CD17E662AFD2956` | `STARRY_CLOSE_FD_TABLE`、`STARRY_CLOSE_SYSCALL`、`STARRY_ERRNO_TRANSLATION` | — | `covered` | sys_close 传播 fd 表删除结果；无效 fd 不在表中，映射为 EBADF。 |
| `LTP_5CB803B873F78BA0` | `STARRY_CLOSE_FD_TABLE`、`STARRY_CLOSE_SYSCALL` | — | `covered` | fd 表成功移除文件、管道或 socket 后，sys_close 统一返回 0。 |

### `mmap`

| rule_id | 静态检查 | 动态测试 | 状态 | 原因 |
| --- | --- | --- | --- | --- |
| `LTP_36C99C10CD38F8DB` | `STARRY_ERRNO_TRANSLATION`、`STARRY_MMAP_ACCESS` | — | `covered` | O_WRONLY 文件不含 READ 权限，file-backed MAP_PRIVATE 映射返回 EACCES。 |
| `LTP_45439D8F2BAB0832` | `STARRY_ERRNO_TRANSLATION`、`STARRY_MMAP_ACCESS` | — | `covered` | O_WRONLY 文件不含 READ 权限；shared writable 映射还要求 WRITE，失败映射为 EACCES。 |
| `LTP_51E295101A9F4411` | `STARRY_ERRNO_TRANSLATION`、`STARRY_MMAP_ARGUMENTS` | — | `covered` | sys_mmap 在任何后续处理前拒绝 length=0，并将 InvalidInput 映射为 EINVAL。 |
| `LTP_52BAFC01DEA6E172` | `STARRY_ERRNO_TRANSLATION`、`STARRY_MMAP_ACCESS` | — | `covered` | O_WRONLY 文件不含 READ 权限，file-backed MAP_SHARED 映射返回 EACCES。 |
| `LTP_791DEA825D66980B` | `STARRY_ERRNO_TRANSLATION`、`STARRY_MMAP_FD` | — | `covered` | file-backed mmap 必须解析 fd；已关闭 fd 经 get_file_like 返回 EBADF。 |
| `LTP_C346EFF1233F7061` | `STARRY_ERRNO_TRANSLATION`、`STARRY_MMAP_ACCESS` | — | `covered` | O_WRONLY 文件不含 READ 权限，file-backed MAP_PRIVATE 映射返回 EACCES。 |
| `LTP_F36F8C0CC1A6D840` | `STARRY_ERRNO_TRANSLATION`、`STARRY_MMAP_ACCESS` | — | `covered` | O_WRONLY 文件不含 READ 权限，file-backed MAP_PRIVATE 映射返回 EACCES。 |
| `LTP_FD1B65B0BCC88E0D` | `STARRY_ERRNO_TRANSLATION`、`STARRY_MMAP_ACCESS` | — | `covered` | O_WRONLY 文件不含 READ 权限；shared writable 映射还要求 WRITE，失败映射为 EACCES。 |
| `LTP_FEACDC300C3E1DD7` | `STARRY_ERRNO_TRANSLATION`、`STARRY_MMAP_ARGUMENTS` | — | `covered` | 未包含 MAP_PRIVATE、MAP_SHARED 或 MAP_SHARED_VALIDATE 的映射类型返回 EINVAL。 |

<details>
<summary>机器可读元数据</summary>

<!-- syscallguard-metadata -->
```yaml
schema_version: 1
kind: syscallguard_mapping_report
report_id: mapping-20260714t161033z-3dec139c
status: completed
generated_at_utc: '2026-07-14T16:14:51.791596Z'
rule_index_hash: sha256:3e5e692515d700b67b7d66b672f4320e8d1a3e57e92b94b4d2be61401de11bf0
requested_syscalls: null
selected_rule_ids:
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
skipped_rule_ids: []
target:
  target_id: starry
  repository: /home/cloud/gitLinux/tgoskits
  repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
  revision: HEAD
  worktree_root: /tmp/syscallguard-worktrees
  descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
  snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
counts:
  rules_total: 12
  processed: 12
  added: 12
  updated: 0
  skipped: 0
  covered: 12
  pending: 0
  needs_review: 0
  unsupported: 0
  static_checks: 6
  dynamic_tests: 0
  remaining: 0
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
  LTP_09B39E9C9254ECB2: &id001
  - close
  LTP_0CD17E662AFD2956: &id002
  - close
  LTP_36C99C10CD38F8DB: &id003
  - mmap
  LTP_45439D8F2BAB0832: &id004
  - mmap
  LTP_51E295101A9F4411: &id005
  - mmap
  LTP_52BAFC01DEA6E172: &id006
  - mmap
  LTP_5CB803B873F78BA0: &id007
  - close
  LTP_791DEA825D66980B: &id008
  - mmap
  LTP_C346EFF1233F7061: &id009
  - mmap
  LTP_F36F8C0CC1A6D840: &id010
  - mmap
  LTP_FD1B65B0BCC88E0D: &id011
  - mmap
  LTP_FEACDC300C3E1DD7: &id012
  - mmap
rules:
  LTP_09B39E9C9254ECB2:
    syscalls: *id001
    rule_version: &id013
      id: LTP_09B39E9C9254ECB2
      generated_at_utc: '2026-07-14T13:35:02.567816Z'
      content_hash: sha256:09b39e9c9254ecb24ccb5288c3f12281e9adc0b698de5c706a4f071599c3ce60
    status: covered
    static_check_refs:
    - STARRY_CLOSE_FD_TABLE
    - STARRY_CLOSE_SYSCALL
    - STARRY_ERRNO_TRANSLATION
    dynamic_test_refs: []
    entity_versions:
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
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: os/StarryOS/kernel/src/file/mod.rs
      symbols:
      - close_file_like
      scope: symbols
      file_hash: sha256:6155028f03d0acfe42f410b0b3e553b6a32411988d08a78e6ee03e09fa80e716
      symbol_hashes:
        close_file_like: sha256:4d1f8d29801b3d463bb4413e8325214d7af8f86f0cae7ada5006dd90e18be8e8
      missing_symbols: []
      content_hash: sha256:58a89ea09d3782630014814fc50f8c47c237503228195d53faf41af2f40d4026
    - path: os/StarryOS/kernel/src/syscall/fs/fd_ops.rs
      symbols:
      - sys_close
      scope: symbols
      file_hash: sha256:e78cf0bf497f11b5dab1dd55689ef3a4f450f55c492ad1703bc748022d61152b
      symbol_hashes:
        sys_close: sha256:e7aca9df1278d812347be922bb2ca7b5be5fff1cf995a42300adc9a77de496ba
      missing_symbols: []
      content_hash: sha256:83f68616aa28981b6d088330cf93b948e1e4c0eb2a3029552811f0b4b8789a12
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260714t161033z-3dec139c
    reason: sys_close 传播 fd 表删除结果；已关闭 fd 不在表中，映射为 EBADF。
  LTP_0CD17E662AFD2956:
    syscalls: *id002
    rule_version: &id014
      id: LTP_0CD17E662AFD2956
      generated_at_utc: '2026-07-14T13:35:02.567816Z'
      content_hash: sha256:0cd17e662afd2956c8c1a42d49b46dca16c37c1972fc6d3632c05c317939a996
    status: covered
    static_check_refs:
    - STARRY_CLOSE_FD_TABLE
    - STARRY_CLOSE_SYSCALL
    - STARRY_ERRNO_TRANSLATION
    dynamic_test_refs: []
    entity_versions:
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
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: os/StarryOS/kernel/src/file/mod.rs
      symbols:
      - close_file_like
      scope: symbols
      file_hash: sha256:6155028f03d0acfe42f410b0b3e553b6a32411988d08a78e6ee03e09fa80e716
      symbol_hashes:
        close_file_like: sha256:4d1f8d29801b3d463bb4413e8325214d7af8f86f0cae7ada5006dd90e18be8e8
      missing_symbols: []
      content_hash: sha256:58a89ea09d3782630014814fc50f8c47c237503228195d53faf41af2f40d4026
    - path: os/StarryOS/kernel/src/syscall/fs/fd_ops.rs
      symbols:
      - sys_close
      scope: symbols
      file_hash: sha256:e78cf0bf497f11b5dab1dd55689ef3a4f450f55c492ad1703bc748022d61152b
      symbol_hashes:
        sys_close: sha256:e7aca9df1278d812347be922bb2ca7b5be5fff1cf995a42300adc9a77de496ba
      missing_symbols: []
      content_hash: sha256:83f68616aa28981b6d088330cf93b948e1e4c0eb2a3029552811f0b4b8789a12
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260714t161033z-3dec139c
    reason: sys_close 传播 fd 表删除结果；无效 fd 不在表中，映射为 EBADF。
  LTP_36C99C10CD38F8DB:
    syscalls: *id003
    rule_version: &id015
      id: LTP_36C99C10CD38F8DB
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:36c99c10cd38f8db26e721ea351430f0ebc4767b9a31257223ad8fd5519c7d0d
    status: covered
    static_check_refs:
    - STARRY_ERRNO_TRANSLATION
    - STARRY_MMAP_ACCESS
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ERRNO_TRANSLATION:
          id: STARRY_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-14T16:14:51.791596Z'
          content_hash: sha256:5534265415b3a67ee5444497f79a373115fdab59a1a8d88e1faf0f0b387fc053
        STARRY_MMAP_ACCESS:
          id: STARRY_MMAP_ACCESS
          generated_at_utc: '2026-07-14T16:14:51.791596Z'
          content_hash: sha256:ed8ff2e5c88f6013bb2dc3555d34922456aa7b8932d0a5fab3372aebfcdfd336
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: os/StarryOS/kernel/src/syscall/mm/mmap.rs
      symbols:
      - sys_mmap
      scope: symbols
      file_hash: sha256:b37bd11c9b637e9b3a2aff1b562e4d1bf4406308c8fbe67ee1c4f75fe3031f01
      symbol_hashes:
        sys_mmap: sha256:95ec5c43c23cb422260c8e31cc2c12f1be122cc188aafb59e68aa86b97346a1d
      missing_symbols: []
      content_hash: sha256:87b0d9d13887c5200143332c90906559b5ba8e298d4c2805c875f159375c6b62
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260714t161033z-3dec139c
    reason: O_WRONLY 文件不含 READ 权限，file-backed MAP_PRIVATE 映射返回 EACCES。
  LTP_45439D8F2BAB0832:
    syscalls: *id004
    rule_version: &id016
      id: LTP_45439D8F2BAB0832
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:45439d8f2bab0832027a39e78d024f72cc6449adff9fb823af60ff7c004d7bc5
    status: covered
    static_check_refs:
    - STARRY_ERRNO_TRANSLATION
    - STARRY_MMAP_ACCESS
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ERRNO_TRANSLATION:
          id: STARRY_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-14T16:14:51.791596Z'
          content_hash: sha256:5534265415b3a67ee5444497f79a373115fdab59a1a8d88e1faf0f0b387fc053
        STARRY_MMAP_ACCESS:
          id: STARRY_MMAP_ACCESS
          generated_at_utc: '2026-07-14T16:14:51.791596Z'
          content_hash: sha256:ed8ff2e5c88f6013bb2dc3555d34922456aa7b8932d0a5fab3372aebfcdfd336
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: os/StarryOS/kernel/src/syscall/mm/mmap.rs
      symbols:
      - sys_mmap
      scope: symbols
      file_hash: sha256:b37bd11c9b637e9b3a2aff1b562e4d1bf4406308c8fbe67ee1c4f75fe3031f01
      symbol_hashes:
        sys_mmap: sha256:95ec5c43c23cb422260c8e31cc2c12f1be122cc188aafb59e68aa86b97346a1d
      missing_symbols: []
      content_hash: sha256:87b0d9d13887c5200143332c90906559b5ba8e298d4c2805c875f159375c6b62
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260714t161033z-3dec139c
    reason: O_WRONLY 文件不含 READ 权限；shared writable 映射还要求 WRITE，失败映射为 EACCES。
  LTP_51E295101A9F4411:
    syscalls: *id005
    rule_version: &id017
      id: LTP_51E295101A9F4411
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:51e295101a9f4411b8c43521d430e85bd27ac1d7a96127b66675d7dc024ba9d2
    status: covered
    static_check_refs:
    - STARRY_ERRNO_TRANSLATION
    - STARRY_MMAP_ARGUMENTS
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ERRNO_TRANSLATION:
          id: STARRY_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-14T16:14:51.791596Z'
          content_hash: sha256:5534265415b3a67ee5444497f79a373115fdab59a1a8d88e1faf0f0b387fc053
        STARRY_MMAP_ARGUMENTS:
          id: STARRY_MMAP_ARGUMENTS
          generated_at_utc: '2026-07-14T16:14:51.791596Z'
          content_hash: sha256:b6441cf0b2e64983d3588d8d6bf3b0875e3141a5477585aafbb8100d28cfe9a1
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: os/StarryOS/kernel/src/syscall/mm/mmap.rs
      symbols:
      - sys_mmap
      scope: symbols
      file_hash: sha256:b37bd11c9b637e9b3a2aff1b562e4d1bf4406308c8fbe67ee1c4f75fe3031f01
      symbol_hashes:
        sys_mmap: sha256:95ec5c43c23cb422260c8e31cc2c12f1be122cc188aafb59e68aa86b97346a1d
      missing_symbols: []
      content_hash: sha256:87b0d9d13887c5200143332c90906559b5ba8e298d4c2805c875f159375c6b62
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260714t161033z-3dec139c
    reason: sys_mmap 在任何后续处理前拒绝 length=0，并将 InvalidInput 映射为 EINVAL。
  LTP_52BAFC01DEA6E172:
    syscalls: *id006
    rule_version: &id018
      id: LTP_52BAFC01DEA6E172
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:52bafc01dea6e1725e71d23e11424031141e37ea07b99e151db6bcfc16116bde
    status: covered
    static_check_refs:
    - STARRY_ERRNO_TRANSLATION
    - STARRY_MMAP_ACCESS
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ERRNO_TRANSLATION:
          id: STARRY_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-14T16:14:51.791596Z'
          content_hash: sha256:5534265415b3a67ee5444497f79a373115fdab59a1a8d88e1faf0f0b387fc053
        STARRY_MMAP_ACCESS:
          id: STARRY_MMAP_ACCESS
          generated_at_utc: '2026-07-14T16:14:51.791596Z'
          content_hash: sha256:ed8ff2e5c88f6013bb2dc3555d34922456aa7b8932d0a5fab3372aebfcdfd336
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: os/StarryOS/kernel/src/syscall/mm/mmap.rs
      symbols:
      - sys_mmap
      scope: symbols
      file_hash: sha256:b37bd11c9b637e9b3a2aff1b562e4d1bf4406308c8fbe67ee1c4f75fe3031f01
      symbol_hashes:
        sys_mmap: sha256:95ec5c43c23cb422260c8e31cc2c12f1be122cc188aafb59e68aa86b97346a1d
      missing_symbols: []
      content_hash: sha256:87b0d9d13887c5200143332c90906559b5ba8e298d4c2805c875f159375c6b62
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260714t161033z-3dec139c
    reason: O_WRONLY 文件不含 READ 权限，file-backed MAP_SHARED 映射返回 EACCES。
  LTP_5CB803B873F78BA0:
    syscalls: *id007
    rule_version: &id019
      id: LTP_5CB803B873F78BA0
      generated_at_utc: '2026-07-14T13:35:02.567816Z'
      content_hash: sha256:5cb803b873f78ba0c0cafe0d4ab7a0e69be0d150de939bbf030e0c66f583d1c6
    status: covered
    static_check_refs:
    - STARRY_CLOSE_FD_TABLE
    - STARRY_CLOSE_SYSCALL
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_CLOSE_FD_TABLE:
          id: STARRY_CLOSE_FD_TABLE
          generated_at_utc: '2026-07-14T16:14:51.791596Z'
          content_hash: sha256:c2a4f66437f46152892f704131da2405e6299203876b5152885f31f7ffeb2d23
        STARRY_CLOSE_SYSCALL:
          id: STARRY_CLOSE_SYSCALL
          generated_at_utc: '2026-07-14T16:14:51.791596Z'
          content_hash: sha256:0c4804a0e1f7b77630d33127c5fbdd34638a9625cac7847821cf654ffe836eaf
      dynamic_tests: {}
    target_dependencies:
    - path: os/StarryOS/kernel/src/file/mod.rs
      symbols:
      - close_file_like
      scope: symbols
      file_hash: sha256:6155028f03d0acfe42f410b0b3e553b6a32411988d08a78e6ee03e09fa80e716
      symbol_hashes:
        close_file_like: sha256:4d1f8d29801b3d463bb4413e8325214d7af8f86f0cae7ada5006dd90e18be8e8
      missing_symbols: []
      content_hash: sha256:58a89ea09d3782630014814fc50f8c47c237503228195d53faf41af2f40d4026
    - path: os/StarryOS/kernel/src/syscall/fs/fd_ops.rs
      symbols:
      - sys_close
      scope: symbols
      file_hash: sha256:e78cf0bf497f11b5dab1dd55689ef3a4f450f55c492ad1703bc748022d61152b
      symbol_hashes:
        sys_close: sha256:e7aca9df1278d812347be922bb2ca7b5be5fff1cf995a42300adc9a77de496ba
      missing_symbols: []
      content_hash: sha256:83f68616aa28981b6d088330cf93b948e1e4c0eb2a3029552811f0b4b8789a12
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260714t161033z-3dec139c
    reason: fd 表成功移除文件、管道或 socket 后，sys_close 统一返回 0。
  LTP_791DEA825D66980B:
    syscalls: *id008
    rule_version: &id020
      id: LTP_791DEA825D66980B
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:791dea825d66980bfded73936e4745cf7b914f20652b9489e65a7a59509b897b
    status: covered
    static_check_refs:
    - STARRY_ERRNO_TRANSLATION
    - STARRY_MMAP_FD
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ERRNO_TRANSLATION:
          id: STARRY_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-14T16:14:51.791596Z'
          content_hash: sha256:5534265415b3a67ee5444497f79a373115fdab59a1a8d88e1faf0f0b387fc053
        STARRY_MMAP_FD:
          id: STARRY_MMAP_FD
          generated_at_utc: '2026-07-14T16:14:51.791596Z'
          content_hash: sha256:5e90be2726ddfc1ba2283b97a09d43daeabb55c4240a517ed6e7f3404bbc5241
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: os/StarryOS/kernel/src/file/mod.rs
      symbols:
      - get_file_like
      scope: symbols
      file_hash: sha256:6155028f03d0acfe42f410b0b3e553b6a32411988d08a78e6ee03e09fa80e716
      symbol_hashes:
        get_file_like: sha256:01d10faef084ccb22e1f2c14980d2539cb091a2af833bd1ed6baa8abe08785b5
      missing_symbols: []
      content_hash: sha256:a0ac4f88598370fae1b30592b26c7f4bc7ec59aaecd3083ab5a806fd86592985
    - path: os/StarryOS/kernel/src/syscall/mm/mmap.rs
      symbols:
      - sys_mmap
      scope: symbols
      file_hash: sha256:b37bd11c9b637e9b3a2aff1b562e4d1bf4406308c8fbe67ee1c4f75fe3031f01
      symbol_hashes:
        sys_mmap: sha256:95ec5c43c23cb422260c8e31cc2c12f1be122cc188aafb59e68aa86b97346a1d
      missing_symbols: []
      content_hash: sha256:87b0d9d13887c5200143332c90906559b5ba8e298d4c2805c875f159375c6b62
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260714t161033z-3dec139c
    reason: file-backed mmap 必须解析 fd；已关闭 fd 经 get_file_like 返回 EBADF。
  LTP_C346EFF1233F7061:
    syscalls: *id009
    rule_version: &id021
      id: LTP_C346EFF1233F7061
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:c346eff1233f706172a595326e9215b63dd1f455b13880c762f92532db036e2e
    status: covered
    static_check_refs:
    - STARRY_ERRNO_TRANSLATION
    - STARRY_MMAP_ACCESS
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ERRNO_TRANSLATION:
          id: STARRY_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-14T16:14:51.791596Z'
          content_hash: sha256:5534265415b3a67ee5444497f79a373115fdab59a1a8d88e1faf0f0b387fc053
        STARRY_MMAP_ACCESS:
          id: STARRY_MMAP_ACCESS
          generated_at_utc: '2026-07-14T16:14:51.791596Z'
          content_hash: sha256:ed8ff2e5c88f6013bb2dc3555d34922456aa7b8932d0a5fab3372aebfcdfd336
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: os/StarryOS/kernel/src/syscall/mm/mmap.rs
      symbols:
      - sys_mmap
      scope: symbols
      file_hash: sha256:b37bd11c9b637e9b3a2aff1b562e4d1bf4406308c8fbe67ee1c4f75fe3031f01
      symbol_hashes:
        sys_mmap: sha256:95ec5c43c23cb422260c8e31cc2c12f1be122cc188aafb59e68aa86b97346a1d
      missing_symbols: []
      content_hash: sha256:87b0d9d13887c5200143332c90906559b5ba8e298d4c2805c875f159375c6b62
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260714t161033z-3dec139c
    reason: O_WRONLY 文件不含 READ 权限，file-backed MAP_PRIVATE 映射返回 EACCES。
  LTP_F36F8C0CC1A6D840:
    syscalls: *id010
    rule_version: &id022
      id: LTP_F36F8C0CC1A6D840
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:f36f8c0cc1a6d84025a2394e30fa1d7c273ce9c13d8f58d759383c75dbf8c10a
    status: covered
    static_check_refs:
    - STARRY_ERRNO_TRANSLATION
    - STARRY_MMAP_ACCESS
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ERRNO_TRANSLATION:
          id: STARRY_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-14T16:14:51.791596Z'
          content_hash: sha256:5534265415b3a67ee5444497f79a373115fdab59a1a8d88e1faf0f0b387fc053
        STARRY_MMAP_ACCESS:
          id: STARRY_MMAP_ACCESS
          generated_at_utc: '2026-07-14T16:14:51.791596Z'
          content_hash: sha256:ed8ff2e5c88f6013bb2dc3555d34922456aa7b8932d0a5fab3372aebfcdfd336
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: os/StarryOS/kernel/src/syscall/mm/mmap.rs
      symbols:
      - sys_mmap
      scope: symbols
      file_hash: sha256:b37bd11c9b637e9b3a2aff1b562e4d1bf4406308c8fbe67ee1c4f75fe3031f01
      symbol_hashes:
        sys_mmap: sha256:95ec5c43c23cb422260c8e31cc2c12f1be122cc188aafb59e68aa86b97346a1d
      missing_symbols: []
      content_hash: sha256:87b0d9d13887c5200143332c90906559b5ba8e298d4c2805c875f159375c6b62
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260714t161033z-3dec139c
    reason: O_WRONLY 文件不含 READ 权限，file-backed MAP_PRIVATE 映射返回 EACCES。
  LTP_FD1B65B0BCC88E0D:
    syscalls: *id011
    rule_version: &id023
      id: LTP_FD1B65B0BCC88E0D
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:fd1b65b0bcc88e0d283d47737c8b9d244de44d7461e8efd5bc6eb699ebaa0d54
    status: covered
    static_check_refs:
    - STARRY_ERRNO_TRANSLATION
    - STARRY_MMAP_ACCESS
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ERRNO_TRANSLATION:
          id: STARRY_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-14T16:14:51.791596Z'
          content_hash: sha256:5534265415b3a67ee5444497f79a373115fdab59a1a8d88e1faf0f0b387fc053
        STARRY_MMAP_ACCESS:
          id: STARRY_MMAP_ACCESS
          generated_at_utc: '2026-07-14T16:14:51.791596Z'
          content_hash: sha256:ed8ff2e5c88f6013bb2dc3555d34922456aa7b8932d0a5fab3372aebfcdfd336
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: os/StarryOS/kernel/src/syscall/mm/mmap.rs
      symbols:
      - sys_mmap
      scope: symbols
      file_hash: sha256:b37bd11c9b637e9b3a2aff1b562e4d1bf4406308c8fbe67ee1c4f75fe3031f01
      symbol_hashes:
        sys_mmap: sha256:95ec5c43c23cb422260c8e31cc2c12f1be122cc188aafb59e68aa86b97346a1d
      missing_symbols: []
      content_hash: sha256:87b0d9d13887c5200143332c90906559b5ba8e298d4c2805c875f159375c6b62
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260714t161033z-3dec139c
    reason: O_WRONLY 文件不含 READ 权限；shared writable 映射还要求 WRITE，失败映射为 EACCES。
  LTP_FEACDC300C3E1DD7:
    syscalls: *id012
    rule_version: &id024
      id: LTP_FEACDC300C3E1DD7
      generated_at_utc: '2026-07-14T13:38:13.033184Z'
      content_hash: sha256:feacdc300c3e1dd754c7925df645b95995a6f17fd0ebcb6a50578071e2f9636f
    status: covered
    static_check_refs:
    - STARRY_ERRNO_TRANSLATION
    - STARRY_MMAP_ARGUMENTS
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ERRNO_TRANSLATION:
          id: STARRY_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-14T16:14:51.791596Z'
          content_hash: sha256:5534265415b3a67ee5444497f79a373115fdab59a1a8d88e1faf0f0b387fc053
        STARRY_MMAP_ARGUMENTS:
          id: STARRY_MMAP_ARGUMENTS
          generated_at_utc: '2026-07-14T16:14:51.791596Z'
          content_hash: sha256:b6441cf0b2e64983d3588d8d6bf3b0875e3141a5477585aafbb8100d28cfe9a1
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: os/StarryOS/kernel/src/syscall/mm/mmap.rs
      symbols:
      - sys_mmap
      scope: symbols
      file_hash: sha256:b37bd11c9b637e9b3a2aff1b562e4d1bf4406308c8fbe67ee1c4f75fe3031f01
      symbol_hashes:
        sys_mmap: sha256:95ec5c43c23cb422260c8e31cc2c12f1be122cc188aafb59e68aa86b97346a1d
      missing_symbols: []
      content_hash: sha256:87b0d9d13887c5200143332c90906559b5ba8e298d4c2805c875f159375c6b62
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260714t161033z-3dec139c
    reason: 未包含 MAP_PRIVATE、MAP_SHARED 或 MAP_SHARED_VALIDATE 的映射类型返回 EINVAL。
entity_versions:
  rules:
    LTP_09B39E9C9254ECB2: *id013
    LTP_0CD17E662AFD2956: *id014
    LTP_36C99C10CD38F8DB: *id015
    LTP_45439D8F2BAB0832: *id016
    LTP_51E295101A9F4411: *id017
    LTP_52BAFC01DEA6E172: *id018
    LTP_5CB803B873F78BA0: *id019
    LTP_791DEA825D66980B: *id020
    LTP_C346EFF1233F7061: *id021
    LTP_F36F8C0CC1A6D840: *id022
    LTP_FD1B65B0BCC88E0D: *id023
    LTP_FEACDC300C3E1DD7: *id024
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
remaining:
  all: []
  pending: []
  needs_review: []
  unsupported: []
```
</details>
