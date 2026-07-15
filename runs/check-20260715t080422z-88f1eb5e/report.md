# Starry 合规检查报告

## 本轮结论

- 状态：`completed`
- 静态检查：pass 3、fail 0、error 0
- 动态测试：pass 0、fail 0、skipped 0、not_run 0
- confirmed finding：0
- 环境或执行 blocker：0（不视为实现缺口）

## 静态检查

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

  - `pub fn close_file_like\(fd: c_int\)[\s\S]*?FD_TABLE\.write\(\)\.remove\(fd as usize\)`：matched=`true`，第 307 行
  - `pub fn close_file_like\(fd: c_int\)[\s\S]*?return Ok\(\(\)\);[\s\S]*?Err\(AxError::BadFileDescriptor\)`：matched=`true`，第 307 行
- finding：—

### `STARRY_CLOSE_SYSCALL`

- 类型：`static`
- 关联 syscall：`close`
- 通用规则：`LTP_09B39E9C9254ECB2`、`LTP_0CD17E662AFD2956`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_close\(fd: c_int\)[\s\S]*?close_file_like\(fd\)\?;`：matched=`true`，第 441 行
  - `pub fn sys_close\(fd: c_int\)[\s\S]*?close_file_like\(fd\)\?;[\s\S]*?Ok\(0\)`：matched=`true`，第 441 行
- finding：—

## 动态测试

本轮没有动态测试。

<details>
<summary>机器可读元数据</summary>

<!-- syscallguard-metadata -->
```yaml
schema_version: 1
kind: syscallguard_check_report
report_id: check-20260715t080422z-88f1eb5e
status: completed
generated_at_utc: '2026-07-15T08:04:23.538146Z'
mapping_report_id: mapping-20260715t080009z-8e410a89
mapping_report_version:
  id: mapping-20260715t080009z-8e410a89
  generated_at_utc: '2026-07-15T08:01:37.322193Z'
  content_hash: sha256:74b319abdb1076f8dd1b8032def04deed0f4969a1fc38b5e22845954f1b7c430
target:
  target_id: starry
  repository: /home/cloud/gitLinux/tgoskits
  repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
  revision: HEAD
  worktree_root: /tmp/syscallguard-worktrees
  descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
  snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
input_hash: sha256:b69c20e4beabf9a4f0f7ee6c7c1cbf7efc59153b7e363114a4424e54316da3e8
entity_hashes:
  rules:
    LTP_09B39E9C9254ECB2: sha256:09b39e9c9254ecb24ccb5288c3f12281e9adc0b698de5c706a4f071599c3ce60
    LTP_0CD17E662AFD2956: sha256:0cd17e662afd2956c8c1a42d49b46dca16c37c1972fc6d3632c05c317939a996
  static_checks:
    STARRY_CLOSE_BAD_FD_ERRNO: sha256:bf73e932edc3b57d4c464e3e1698d178f616ad411fe048d7350342c1b894b448
    STARRY_CLOSE_FD_TABLE: sha256:111ad7aafb1c93e53b0c9bb8149d6d4f11df1ea0cc0207f676418c055b90f134
    STARRY_CLOSE_SYSCALL: sha256:633c628e7f46b1ead9fddbb4a1bc2b4fbeee509f819340a54cb14cf41e1213ae
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
  static_checks:
    STARRY_CLOSE_BAD_FD_ERRNO:
      id: STARRY_CLOSE_BAD_FD_ERRNO
      generated_at_utc: '2026-07-15T08:01:37.322193Z'
      content_hash: sha256:bf73e932edc3b57d4c464e3e1698d178f616ad411fe048d7350342c1b894b448
    STARRY_CLOSE_FD_TABLE:
      id: STARRY_CLOSE_FD_TABLE
      generated_at_utc: '2026-07-15T08:01:37.322193Z'
      content_hash: sha256:111ad7aafb1c93e53b0c9bb8149d6d4f11df1ea0cc0207f676418c055b90f134
    STARRY_CLOSE_SYSCALL:
      id: STARRY_CLOSE_SYSCALL
      generated_at_utc: '2026-07-15T08:01:37.322193Z'
      content_hash: sha256:633c628e7f46b1ead9fddbb4a1bc2b4fbeee509f819340a54cb14cf41e1213ae
  dynamic_tests: {}
execution_scope:
  rules:
  - LTP_09B39E9C9254ECB2
  - LTP_0CD17E662AFD2956
  static_checks:
  - STARRY_CLOSE_BAD_FD_ERRNO
  - STARRY_CLOSE_FD_TABLE
  - STARRY_CLOSE_SYSCALL
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
dynamic: []
counts:
  static_pass: 3
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
content_hash: sha256:af723dc00b5b99a57a5dd1e7f3be2575455ea33c690319d14780ac6fd0a85955
```
</details>
