# Starry 合规检查报告

## 本轮结论

- 状态：`completed`
- 静态检查：pass 15、fail 2、error 0
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

  - `pub fn sys_finit_module\(module_fd: i32, param_ptr: \*const u8, flags: u32\)`：matched=`true`，第 41 行
  - `pub fn sys_finit_module\([\s\S]*?if flags != 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}`：matched=`true`，第 41 行
- finding：—

### `STARRY_ROUND3_ERRNO_TRANSLATION`

- 类型：`static`
- 关联 syscall：`fstat`、`fstatfs`、`ftruncate`、`getcwd`、`getpgid`、`getpriority`、`getsid`、`gettimeofday`、`init_module`
- 通用规则：`LTP_2648B36BD9CF39EE`、`LTP_466F01834F965621`、`LTP_53E3454ED6EFD842`、`LTP_5B4AA4EE494B37D2`、`LTP_64B1B6EEEC3F79FC`、`LTP_6C14DE68E3C0CC24`、`LTP_729222947741DFD6`、`LTP_88D300A8FB407324`、`LTP_89BB56D579EEF06D`、`LTP_8C1C2578972FCA1D`、`LTP_912BE233FAFE6762`、`LTP_9461AA782926BAB4`、`LTP_D246498B20D9CB2C`、`LTP_EB1B734A0943248E`、`LTP_F8FD511858BB650D`、`LTP_F92A1A6292F40811`、`LTP_FC1E41C3414E7F21`、`LTP_FCF5A4835CFCD143`
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
- 通用规则：`LTP_EB1B734A0943248E`、`LTP_F92A1A6292F40811`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_fstatfs\(fd: i32, buf: \*mut statfs\)[\s\S]*?File::from_fd\(fd\)\?`：matched=`true`，第 245 行
  - `buf\.vm_write\(statfs\([\s\S]*?\)\?\)\?;`：matched=`true`，第 235 行
- finding：—

### `STARRY_ROUND3_FSTAT_CORE`

- 类型：`static`
- 关联 syscall：`fstat`
- 通用规则：`LTP_466F01834F965621`、`LTP_64B1B6EEEC3F79FC`、`LTP_A363671517C058B1`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_fstat\(fd: i32, statbuf: \*mut stat\)[\s\S]*?sys_fstatat\(fd, core::ptr::null\(\), statbuf, AT_EMPTY_PATH\)`：matched=`true`，第 44 行
  - `pub fn sys_fstatat\([\s\S]*?let loc = resolve_at\(dirfd, path\.as_deref\(\), flags\)\?;`：matched=`true`，第 58 行
  - `statbuf\.vm_write\(loc\.stat\(\)\?\.into\(\)\)\?;`：matched=`true`，第 76 行
- finding：—

### `STARRY_ROUND3_FTRUNCATE_NEGATIVE`

- 类型：`static`
- 关联 syscall：`ftruncate`
- 通用规则：`LTP_2648B36BD9CF39EE`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_ftruncate\([\s\S]*?if length < 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}[\s\S]*?File::from_fd\(fd\)`：matched=`true`，第 237 行
- finding：—

### `STARRY_ROUND3_GETCWD`

- 类型：`static`
- 关联 syscall：`getcwd`
- 通用规则：`LTP_53E3454ED6EFD842`、`LTP_729222947741DFD6`、`LTP_89BB56D579EEF06D`、`LTP_912BE233FAFE6762`、`LTP_FC1E41C3414E7F21`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_getcwd\([\s\S]*?let size: usize = size\.try_into\(\)\.map_err\(\\|_\\| AxError::BadAddress\)\?;`：matched=`true`，第 418 行
  - `let cwd = cwd\.as_bytes_with_nul\(\);`：matched=`true`，第 425 行
  - `if cwd\.len\(\) <= size \{[\s\S]*?vm_write_slice\(buf, cwd\)\?;[\s\S]*?\} else \{\s*Err\(AxError::OutOfRange\)`：matched=`true`，第 427 行
- finding：—

### `STARRY_ROUND3_GETPRIORITY_SELECTOR`

- 类型：`static`
- 关联 syscall：`getpriority`
- 通用规则：`LTP_88D300A8FB407324`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_getpriority\([\s\S]*?match which \{[\s\S]*?_ => Err\(AxError::InvalidInput\),\s*\}`：matched=`true`，第 237 行
- finding：—

### `STARRY_ROUND3_GETRLIMIT_CORE`

- 类型：`static`
- 关联 syscall：`getrlimit`
- 通用规则：`LTP_2554AC2E46FC6A15`、`LTP_26555A26680524AD`、`LTP_3741A721C9C463D0`、`LTP_3B1458E6E26CBB53`、`LTP_652CE911B47794E0`、`LTP_7DFAC48A8971CFE3`、`LTP_8988E5015778894A`、`LTP_914935DA5C379DA1`、`LTP_91ED7E85761CE00F`、`LTP_9305FA6D8B835652`、`LTP_963957F80E751EE6`、`LTP_A0547B601C515355`、`LTP_B058D6B9CBBB459D`、`LTP_BD5C209F4C6EE910`、`LTP_E6C69C9F4AB565BC`、`LTP_EA953D5E5C4B2B1F`、`LTP_FADBA4ADECCFBA4E`、`LTP_FB0ABF26A21EAE3C`
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
- 通用规则：`LTP_2554AC2E46FC6A15`、`LTP_26555A26680524AD`、`LTP_3741A721C9C463D0`、`LTP_3B1458E6E26CBB53`、`LTP_652CE911B47794E0`、`LTP_7DFAC48A8971CFE3`、`LTP_8988E5015778894A`、`LTP_914935DA5C379DA1`、`LTP_91ED7E85761CE00F`、`LTP_9305FA6D8B835652`、`LTP_963957F80E751EE6`、`LTP_A0547B601C515355`、`LTP_B058D6B9CBBB459D`、`LTP_BD5C209F4C6EE910`、`LTP_E6C69C9F4AB565BC`、`LTP_EA953D5E5C4B2B1F`、`LTP_FADBA4ADECCFBA4E`、`LTP_FB0ABF26A21EAE3C`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `Sysno::getrlimit => sys_prlimit64\(0, uctx\.arg0\(\) as _, core::ptr::null\(\), uctx\.arg1\(\) as _\)`：matched=`true`，第 645 行
- finding：—

### `STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE`

- 类型：`static`
- 关联 syscall：`gettimeofday`
- 通用规则：`LTP_6C14DE68E3C0CC24`
- 结果：`fail`
- 原因：one or more required patterns did not match
- pattern 证据：

  - `pub fn sys_gettimeofday\(ts: \*mut timeval, tz: \*mut Timezone\)`：matched=`false`，未匹配
  - `tz\.nullable\(\)[\s\S]*?tz\.vm_write\(Timezone::default\(\)\)\?;`：matched=`false`，未匹配
- finding：`finding-gettimeofday-ltp-6c14de68e3c0cc24-117b5f149133`

### `STARRY_ROUND3_GETTIMEOFDAY_VALUE`

- 类型：`static`
- 关联 syscall：`gettimeofday`
- 通用规则：`LTP_5B4AA4EE494B37D2`、`LTP_FCF5A4835CFCD143`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_gettimeofday\([\s\S]*?ts\.vm_write\(timeval::from_time_value\(wall_time\(\)\)\)\?;`：matched=`true`，第 36 行
- finding：—

### `STARRY_ROUND3_INIT_MODULE_PERMISSION`

- 类型：`static`
- 关联 syscall：`init_module`
- 通用规则：`LTP_D246498B20D9CB2C`
- 结果：`fail`
- 原因：one or more required patterns did not match
- pattern 证据：

  - `pub fn sys_init_module\([\s\S]*?if !current\(\)\.as_thread\(\)\.cred\(\)\.has_cap_sys_module\(\)`：matched=`false`，未匹配
  - `pub fn sys_init_module\([\s\S]*?has_cap_sys_module\(\)[\s\S]*?return Err\(AxError::OperationNotPermitted\);[\s\S]*?VmBytes::new`：matched=`false`，未匹配
- finding：`finding-init-module-ltp-d246498b20d9cb2c-117b5f149133`

### `STARRY_ROUND3_JOB_ID_LOOKUP`

- 类型：`static`
- 关联 syscall：`getpgid`、`getsid`
- 通用规则：`LTP_8C1C2578972FCA1D`、`LTP_9461AA782926BAB4`、`LTP_F8FD511858BB650D`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn sys_getsid\(pid: Pid\)[\s\S]*?get_process\(pid\)\?\.group\(\)\.session\(\)\.sid\(\)`：matched=`true`，第 10 行
  - `pub fn sys_getpgid\(pid: Pid\)[\s\S]*?get_process\(pid\)\?\.group\(\)\.pgid\(\)`：matched=`true`，第 30 行
- finding：—

### `STARRY_ROUND3_PROCESS_LOOKUP`

- 类型：`static`
- 关联 syscall：`getpgid`、`getsid`
- 通用规则：`LTP_8C1C2578972FCA1D`、`LTP_9461AA782926BAB4`、`LTP_F8FD511858BB650D`
- 结果：`pass`
- 原因：all required patterns matched
- pattern 证据：

  - `pub fn get_process\(pid: Pid\)[\s\S]*?if pid == 0 \{\s*return Ok\(current\(\)\.as_thread\(\)\.proc_data\.proc\.clone\(\)\);`：matched=`true`，第 255 行
  - `get_zombie_process\(pid\)\.ok_or\(AxError::NoSuchProcess\)`：matched=`true`，第 262 行
- finding：—

## 动态测试

本轮没有动态测试。

<details>
<summary>机器可读元数据</summary>

<!-- syscallguard-metadata -->
```yaml
schema_version: 1
kind: syscallguard_check_report
report_id: check-20260716t034600z-819e26b8
status: completed
generated_at_utc: '2026-07-16T03:46:03.609800Z'
mapping_report_id: mapping-20260716t033545z-218dce19
mapping_report_version:
  id: mapping-20260716t033545z-218dce19
  generated_at_utc: '2026-07-16T03:45:25.334454Z'
  content_hash: sha256:a554638847d92da46484047df1747dd8f90cbbb8f902efe5c7120aefa57a9de9
target:
  target_id: starry
  repository: /home/cloud/gitLinux/tgoskits
  repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
  branch: dev-syscalls-compliance-1
  descriptor_hash: sha256:6b982bb80e3a0a3cf408d7c696367996422e3dac8376577222e56ee47f111d24
  snapshot_hash: sha256:117b5f149133d675e2090cbee65583ded74d7f19faf62873843614ca56168abe
input_hash: sha256:44543acc9035d4ff3eaa221082e7b84ecf1f0f604c64024a281672e8d7fa51b2
entity_hashes:
  rules:
    LTP_2554AC2E46FC6A15: sha256:2554ac2e46fc6a15932bc27db324eb7b2b1265b2270c61b345af14c0b79e241d
    LTP_2648B36BD9CF39EE: sha256:2648b36bd9cf39eed20eeccf40f65b34092fefc293cc25e59a3b4d0130b0968f
    LTP_26555A26680524AD: sha256:26555a26680524ad18ca9e9f1082b5f71c9edbd627be17b015751aadffc79033
    LTP_3741A721C9C463D0: sha256:3741a721c9c463d0d65d94387111a493a2a48a2a5f1975fc7d455144d3321154
    LTP_3B1458E6E26CBB53: sha256:3b1458e6e26cbb5398ae5221e8cb8d70b475e8e7fa008f9752270403cd9e3e38
    LTP_466F01834F965621: sha256:466f01834f965621ab012906888aad7acf5ae6e62b290e92e8975f01e19fc7ef
    LTP_53E3454ED6EFD842: sha256:53e3454ed6efd842d4456341bdaf29e25ad49ab8f5a55c170a4e23c3355fe2f9
    LTP_5B4AA4EE494B37D2: sha256:5b4aa4ee494b37d28532bc2342bda381464c5ae3ffeb7fb7f6e14d925a95e2e7
    LTP_64B1B6EEEC3F79FC: sha256:64b1b6eeec3f79fc85edbb4e3e6e6066f854c28d9721e3cbbab7294f2295e473
    LTP_652CE911B47794E0: sha256:652ce911b47794e00cd84120507ce0a4b8fe539ae38dff3f3c047d91cab6d2e1
    LTP_6C14DE68E3C0CC24: sha256:6c14de68e3c0cc24bbb7021cd805e26a73df65653f350d8fa8ed8de5232949e8
    LTP_729222947741DFD6: sha256:729222947741dfd63a81e9c93572baf5c789acbffca84a2edd5dce13fe1fb2a3
    LTP_7DFAC48A8971CFE3: sha256:7dfac48a8971cfe3c53af5bdc67246aedc28a76f25fe9bb7d59bb5481e0d4295
    LTP_88D300A8FB407324: sha256:88d300a8fb407324aefbe09d1b569b46d87628a1639509250755357a2c634c1a
    LTP_8988E5015778894A: sha256:8988e5015778894a14a0b54cc6fe1a0f1f2917fb41a0c6dfd0152069d07c8d56
    LTP_89BB56D579EEF06D: sha256:89bb56d579eef06d47c81ec803de4585a5afecb282c21eb9399b98db46b4e647
    LTP_8C1C2578972FCA1D: sha256:8c1c2578972fca1d655df720a137f88882824f681ac3cbfa59052c4a1f8ef64a
    LTP_912BE233FAFE6762: sha256:912be233fafe67624b7249f0492e0d4ded1fbd11fc3cf20af5bc3bb23dfc0874
    LTP_914935DA5C379DA1: sha256:914935da5c379da10358ba568cfe5b8c7a31f6c57db6f6446451375aa973c46a
    LTP_91ED7E85761CE00F: sha256:91ed7e85761ce00fb0a63c61b421b825e76cf8577e07d172597be6451388fa31
    LTP_9305FA6D8B835652: sha256:9305fa6d8b8356529faec8a8a060de73350f98dc7a1db1af07a5e45a6f6e11ae
    LTP_9461AA782926BAB4: sha256:9461aa782926bab4cb006db18510ae154420b8c023b3b2f9cc0308d205ca9cf7
    LTP_963957F80E751EE6: sha256:963957f80e751ee69ad1bc37cd06dda20a9abc3d44b32496ea0aae263fe7715f
    LTP_A0547B601C515355: sha256:a0547b601c51535524cdadea7c3abcbc2fcd16157591cc2322cd1def6a08cc56
    LTP_A363671517C058B1: sha256:a363671517c058b177b37c8394c48508feb8e3077c9818d779846e05afad7aa3
    LTP_B058D6B9CBBB459D: sha256:b058d6b9cbbb459d2d0e155285c19e2e49762cc25177b335dab254142809eb74
    LTP_BD5C209F4C6EE910: sha256:bd5c209f4c6ee910a13539baa6f55f3f3d2654a60e583b67fa26724405421ad3
    LTP_D246498B20D9CB2C: sha256:d246498b20d9cb2cd6ece54014a50e1c77fa08b6a598251c2dc0e3a3700193e2
    LTP_DA65D6C7A0E4ABBC: sha256:da65d6c7a0e4abbc12ba61464384db59b2ccc9a4215469858de691a4c6deb562
    LTP_E6C69C9F4AB565BC: sha256:e6c69c9f4ab565bc9a0aedb983bb975a15e4e8da818e58248848705f1fd4b2e5
    LTP_EA953D5E5C4B2B1F: sha256:ea953d5e5c4b2b1f5d7e50d2191215d70c30b76cda9d1c29b51ec06d41f13bcd
    LTP_EB1B734A0943248E: sha256:eb1b734a0943248e40e858f9d9547299edda39a8c18852a2c1775fce0d0b0f6e
    LTP_F8FD511858BB650D: sha256:f8fd511858bb650d732732911dd9b8f3b5680d09787b4b47438a5bb603dc1aff
    LTP_F92A1A6292F40811: sha256:f92a1a6292f408112c127494a4bcae4af4bb94ac649b58da52777e46e088a50e
    LTP_FADBA4ADECCFBA4E: sha256:fadba4adeccfba4e42423348aa44d9b192be1bcb3f9c3fa8b14a06dcdb243a3e
    LTP_FB0ABF26A21EAE3C: sha256:fb0abf26a21eae3c87515646892b72f4321684e5869b1af86bd8b799c5043180
    LTP_FC1E41C3414E7F21: sha256:fc1e41c3414e7f214284f077070cc39320ebd294786eda043234fca8d9f5da6d
    LTP_FCF5A4835CFCD143: sha256:fcf5a4835cfcd143bee1e5d04d1a6a86a0a2d3560f5b6abc1a0b388e31f42c86
    LTP_425E5A3502541DE8: sha256:425e5a3502541de863d8b8e88eafb95db2f8d8e1f9cb88a32d8b3124950395b2
    LTP_74BB3F96CBA52D02: sha256:74bb3f96cba52d02850ad3c5e54c87acf278ce51290c99d5ae29da583be9ba38
    LTP_66C670178B06E9F3: sha256:66c670178b06e9f3eae76490edd09b4a26bb0e1c2ccba3c4cbc2a625d12c39bb
  static_checks:
    STARRY_FINIT_MODULE_FLAG_VALIDATION: sha256:dc386f0f1e684798e6c95359648b40bc8b35029e6225ca8f5fe0d1e3c8119e5e
    STARRY_ROUND3_ERRNO_TRANSLATION: sha256:d6230c19c9780e6e7ba4c5d5752b9029e1d6a8575efeb6c4f262c8f3214c1a83
    STARRY_ROUND3_FSTATFS_ERRORS: sha256:a4779e53065976fa564f53fb0b901e87fcd8c95b3eb2d6ad5d8c46acc390b1e1
    STARRY_ROUND3_FSTAT_CORE: sha256:c03fbea34b01ec1891e40a732c263b37429525d389e12235b3a638c227a0d37a
    STARRY_ROUND3_FTRUNCATE_NEGATIVE: sha256:81f1a37871f4ed42e333270b6a6229f87c03bb704e472bd7593437dd70290281
    STARRY_ROUND3_GETCWD: sha256:962560d14712aae8bc75802edf0b76d97b11cccd1748f890789deb252c3cce6e
    STARRY_ROUND3_GETPRIORITY_SELECTOR: sha256:70b7e27926c91c7a973fe2c436229d13946d73e1d03ff19bfcbb129a1046eed6
    STARRY_ROUND3_GETRLIMIT_CORE: sha256:df024c7997b871d665489e8320271b8c35553d83a5b4c33378673f462659be87
    STARRY_ROUND3_GETRLIMIT_DISPATCH: sha256:7e99498a0d93451e421a010b0f7ff54fb309ea498190a17a93f254db4d027bfe
    STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE: sha256:92bc710c6c3f284e3eff2c787941c590b62affb1bc04fcd6bdd64874db819663
    STARRY_ROUND3_GETTIMEOFDAY_VALUE: sha256:92e018dcac5c003b40d4bc2ac920008e8bce2b0cb30b174e3b55a0d79b7402ea
    STARRY_ROUND3_INIT_MODULE_PERMISSION: sha256:bb8b549ce47a786283f4228f35bd1f41b767c396d4abbfe84df1f67fb2f824d8
    STARRY_ROUND3_JOB_ID_LOOKUP: sha256:200d4c22b88ccaa3197ad71f0ac11fabc2563a258bcf1c3b1cf4bc7aa6b2b9c8
    STARRY_ROUND3_PROCESS_LOOKUP: sha256:faf088c7797542a64336a18a1f4b3ee9724ce0a6bce05d6ea7bd8152ffd2a88b
    STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS: sha256:6d8ffe193808bde740053a61419adcf0e7c090388b2f5fea0475696c5b402070
    STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO: sha256:39ebc0849b8fede86d9689ed1dba7fda23315b83937a447b328ffd1a94bdfb34
    STARRY_EPOLL_NESTED_LOOP: sha256:d1db97954ea66c6632d4d74191ef0d91751bbbcfee42883a78137bbdaac22e58
  dynamic_tests: {}
entity_versions:
  rules:
    LTP_2554AC2E46FC6A15:
      id: LTP_2554AC2E46FC6A15
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:2554ac2e46fc6a15932bc27db324eb7b2b1265b2270c61b345af14c0b79e241d
    LTP_2648B36BD9CF39EE:
      id: LTP_2648B36BD9CF39EE
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:2648b36bd9cf39eed20eeccf40f65b34092fefc293cc25e59a3b4d0130b0968f
    LTP_26555A26680524AD:
      id: LTP_26555A26680524AD
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:26555a26680524ad18ca9e9f1082b5f71c9edbd627be17b015751aadffc79033
    LTP_3741A721C9C463D0:
      id: LTP_3741A721C9C463D0
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:3741a721c9c463d0d65d94387111a493a2a48a2a5f1975fc7d455144d3321154
    LTP_3B1458E6E26CBB53:
      id: LTP_3B1458E6E26CBB53
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:3b1458e6e26cbb5398ae5221e8cb8d70b475e8e7fa008f9752270403cd9e3e38
    LTP_466F01834F965621:
      id: LTP_466F01834F965621
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:466f01834f965621ab012906888aad7acf5ae6e62b290e92e8975f01e19fc7ef
    LTP_53E3454ED6EFD842:
      id: LTP_53E3454ED6EFD842
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:53e3454ed6efd842d4456341bdaf29e25ad49ab8f5a55c170a4e23c3355fe2f9
    LTP_5B4AA4EE494B37D2:
      id: LTP_5B4AA4EE494B37D2
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:5b4aa4ee494b37d28532bc2342bda381464c5ae3ffeb7fb7f6e14d925a95e2e7
    LTP_64B1B6EEEC3F79FC:
      id: LTP_64B1B6EEEC3F79FC
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:64b1b6eeec3f79fc85edbb4e3e6e6066f854c28d9721e3cbbab7294f2295e473
    LTP_652CE911B47794E0:
      id: LTP_652CE911B47794E0
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:652ce911b47794e00cd84120507ce0a4b8fe539ae38dff3f3c047d91cab6d2e1
    LTP_6C14DE68E3C0CC24:
      id: LTP_6C14DE68E3C0CC24
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:6c14de68e3c0cc24bbb7021cd805e26a73df65653f350d8fa8ed8de5232949e8
    LTP_729222947741DFD6:
      id: LTP_729222947741DFD6
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:729222947741dfd63a81e9c93572baf5c789acbffca84a2edd5dce13fe1fb2a3
    LTP_7DFAC48A8971CFE3:
      id: LTP_7DFAC48A8971CFE3
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:7dfac48a8971cfe3c53af5bdc67246aedc28a76f25fe9bb7d59bb5481e0d4295
    LTP_88D300A8FB407324:
      id: LTP_88D300A8FB407324
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:88d300a8fb407324aefbe09d1b569b46d87628a1639509250755357a2c634c1a
    LTP_8988E5015778894A:
      id: LTP_8988E5015778894A
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:8988e5015778894a14a0b54cc6fe1a0f1f2917fb41a0c6dfd0152069d07c8d56
    LTP_89BB56D579EEF06D:
      id: LTP_89BB56D579EEF06D
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:89bb56d579eef06d47c81ec803de4585a5afecb282c21eb9399b98db46b4e647
    LTP_8C1C2578972FCA1D:
      id: LTP_8C1C2578972FCA1D
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:8c1c2578972fca1d655df720a137f88882824f681ac3cbfa59052c4a1f8ef64a
    LTP_912BE233FAFE6762:
      id: LTP_912BE233FAFE6762
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:912be233fafe67624b7249f0492e0d4ded1fbd11fc3cf20af5bc3bb23dfc0874
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
    LTP_963957F80E751EE6:
      id: LTP_963957F80E751EE6
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:963957f80e751ee69ad1bc37cd06dda20a9abc3d44b32496ea0aae263fe7715f
    LTP_A0547B601C515355:
      id: LTP_A0547B601C515355
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:a0547b601c51535524cdadea7c3abcbc2fcd16157591cc2322cd1def6a08cc56
    LTP_A363671517C058B1:
      id: LTP_A363671517C058B1
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:a363671517c058b177b37c8394c48508feb8e3077c9818d779846e05afad7aa3
    LTP_B058D6B9CBBB459D:
      id: LTP_B058D6B9CBBB459D
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:b058d6b9cbbb459d2d0e155285c19e2e49762cc25177b335dab254142809eb74
    LTP_BD5C209F4C6EE910:
      id: LTP_BD5C209F4C6EE910
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:bd5c209f4c6ee910a13539baa6f55f3f3d2654a60e583b67fa26724405421ad3
    LTP_D246498B20D9CB2C:
      id: LTP_D246498B20D9CB2C
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:d246498b20d9cb2cd6ece54014a50e1c77fa08b6a598251c2dc0e3a3700193e2
    LTP_DA65D6C7A0E4ABBC:
      id: LTP_DA65D6C7A0E4ABBC
      generated_at_utc: '2026-07-16T02:52:01.871423Z'
      content_hash: sha256:da65d6c7a0e4abbc12ba61464384db59b2ccc9a4215469858de691a4c6deb562
    LTP_E6C69C9F4AB565BC:
      id: LTP_E6C69C9F4AB565BC
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:e6c69c9f4ab565bc9a0aedb983bb975a15e4e8da818e58248848705f1fd4b2e5
    LTP_EA953D5E5C4B2B1F:
      id: LTP_EA953D5E5C4B2B1F
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:ea953d5e5c4b2b1f5d7e50d2191215d70c30b76cda9d1c29b51ec06d41f13bcd
    LTP_EB1B734A0943248E:
      id: LTP_EB1B734A0943248E
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:eb1b734a0943248e40e858f9d9547299edda39a8c18852a2c1775fce0d0b0f6e
    LTP_F8FD511858BB650D:
      id: LTP_F8FD511858BB650D
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:f8fd511858bb650d732732911dd9b8f3b5680d09787b4b47438a5bb603dc1aff
    LTP_F92A1A6292F40811:
      id: LTP_F92A1A6292F40811
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:f92a1a6292f408112c127494a4bcae4af4bb94ac649b58da52777e46e088a50e
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
    LTP_FCF5A4835CFCD143:
      id: LTP_FCF5A4835CFCD143
      generated_at_utc: '2026-07-16T03:35:24.146836Z'
      content_hash: sha256:fcf5a4835cfcd143bee1e5d04d1a6a86a0a2d3560f5b6abc1a0b388e31f42c86
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
  static_checks:
    STARRY_FINIT_MODULE_FLAG_VALIDATION:
      id: STARRY_FINIT_MODULE_FLAG_VALIDATION
      generated_at_utc: '2026-07-16T03:45:25.334454Z'
      content_hash: sha256:dc386f0f1e684798e6c95359648b40bc8b35029e6225ca8f5fe0d1e3c8119e5e
    STARRY_ROUND3_ERRNO_TRANSLATION:
      id: STARRY_ROUND3_ERRNO_TRANSLATION
      generated_at_utc: '2026-07-16T03:45:25.334454Z'
      content_hash: sha256:d6230c19c9780e6e7ba4c5d5752b9029e1d6a8575efeb6c4f262c8f3214c1a83
    STARRY_ROUND3_FSTATFS_ERRORS:
      id: STARRY_ROUND3_FSTATFS_ERRORS
      generated_at_utc: '2026-07-16T03:45:25.334454Z'
      content_hash: sha256:a4779e53065976fa564f53fb0b901e87fcd8c95b3eb2d6ad5d8c46acc390b1e1
    STARRY_ROUND3_FSTAT_CORE:
      id: STARRY_ROUND3_FSTAT_CORE
      generated_at_utc: '2026-07-16T03:45:25.334454Z'
      content_hash: sha256:c03fbea34b01ec1891e40a732c263b37429525d389e12235b3a638c227a0d37a
    STARRY_ROUND3_FTRUNCATE_NEGATIVE:
      id: STARRY_ROUND3_FTRUNCATE_NEGATIVE
      generated_at_utc: '2026-07-16T03:45:25.334454Z'
      content_hash: sha256:81f1a37871f4ed42e333270b6a6229f87c03bb704e472bd7593437dd70290281
    STARRY_ROUND3_GETCWD:
      id: STARRY_ROUND3_GETCWD
      generated_at_utc: '2026-07-16T03:45:25.334454Z'
      content_hash: sha256:962560d14712aae8bc75802edf0b76d97b11cccd1748f890789deb252c3cce6e
    STARRY_ROUND3_GETPRIORITY_SELECTOR:
      id: STARRY_ROUND3_GETPRIORITY_SELECTOR
      generated_at_utc: '2026-07-16T03:45:25.334454Z'
      content_hash: sha256:70b7e27926c91c7a973fe2c436229d13946d73e1d03ff19bfcbb129a1046eed6
    STARRY_ROUND3_GETRLIMIT_CORE:
      id: STARRY_ROUND3_GETRLIMIT_CORE
      generated_at_utc: '2026-07-16T03:45:25.334454Z'
      content_hash: sha256:df024c7997b871d665489e8320271b8c35553d83a5b4c33378673f462659be87
    STARRY_ROUND3_GETRLIMIT_DISPATCH:
      id: STARRY_ROUND3_GETRLIMIT_DISPATCH
      generated_at_utc: '2026-07-16T03:45:25.334454Z'
      content_hash: sha256:7e99498a0d93451e421a010b0f7ff54fb309ea498190a17a93f254db4d027bfe
    STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE:
      id: STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE
      generated_at_utc: '2026-07-16T03:45:25.334454Z'
      content_hash: sha256:92bc710c6c3f284e3eff2c787941c590b62affb1bc04fcd6bdd64874db819663
    STARRY_ROUND3_GETTIMEOFDAY_VALUE:
      id: STARRY_ROUND3_GETTIMEOFDAY_VALUE
      generated_at_utc: '2026-07-16T03:45:25.334454Z'
      content_hash: sha256:92e018dcac5c003b40d4bc2ac920008e8bce2b0cb30b174e3b55a0d79b7402ea
    STARRY_ROUND3_INIT_MODULE_PERMISSION:
      id: STARRY_ROUND3_INIT_MODULE_PERMISSION
      generated_at_utc: '2026-07-16T03:45:25.334454Z'
      content_hash: sha256:bb8b549ce47a786283f4228f35bd1f41b767c396d4abbfe84df1f67fb2f824d8
    STARRY_ROUND3_JOB_ID_LOOKUP:
      id: STARRY_ROUND3_JOB_ID_LOOKUP
      generated_at_utc: '2026-07-16T03:45:25.334454Z'
      content_hash: sha256:200d4c22b88ccaa3197ad71f0ac11fabc2563a258bcf1c3b1cf4bc7aa6b2b9c8
    STARRY_ROUND3_PROCESS_LOOKUP:
      id: STARRY_ROUND3_PROCESS_LOOKUP
      generated_at_utc: '2026-07-16T03:45:25.334454Z'
      content_hash: sha256:faf088c7797542a64336a18a1f4b3ee9724ce0a6bce05d6ea7bd8152ffd2a88b
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
  dynamic_tests: {}
base_execution_scope:
  rules:
  - LTP_2554AC2E46FC6A15
  - LTP_2648B36BD9CF39EE
  - LTP_26555A26680524AD
  - LTP_3741A721C9C463D0
  - LTP_3B1458E6E26CBB53
  - LTP_466F01834F965621
  - LTP_53E3454ED6EFD842
  - LTP_5B4AA4EE494B37D2
  - LTP_64B1B6EEEC3F79FC
  - LTP_652CE911B47794E0
  - LTP_6C14DE68E3C0CC24
  - LTP_729222947741DFD6
  - LTP_7DFAC48A8971CFE3
  - LTP_88D300A8FB407324
  - LTP_8988E5015778894A
  - LTP_89BB56D579EEF06D
  - LTP_8C1C2578972FCA1D
  - LTP_912BE233FAFE6762
  - LTP_914935DA5C379DA1
  - LTP_91ED7E85761CE00F
  - LTP_9305FA6D8B835652
  - LTP_9461AA782926BAB4
  - LTP_963957F80E751EE6
  - LTP_A0547B601C515355
  - LTP_A363671517C058B1
  - LTP_B058D6B9CBBB459D
  - LTP_BD5C209F4C6EE910
  - LTP_D246498B20D9CB2C
  - LTP_DA65D6C7A0E4ABBC
  - LTP_E6C69C9F4AB565BC
  - LTP_EA953D5E5C4B2B1F
  - LTP_EB1B734A0943248E
  - LTP_F8FD511858BB650D
  - LTP_F92A1A6292F40811
  - LTP_FADBA4ADECCFBA4E
  - LTP_FB0ABF26A21EAE3C
  - LTP_FC1E41C3414E7F21
  - LTP_FCF5A4835CFCD143
  static_checks:
  - STARRY_FINIT_MODULE_FLAG_VALIDATION
  - STARRY_ROUND3_ERRNO_TRANSLATION
  - STARRY_ROUND3_FSTATFS_ERRORS
  - STARRY_ROUND3_FSTAT_CORE
  - STARRY_ROUND3_FTRUNCATE_NEGATIVE
  - STARRY_ROUND3_GETCWD
  - STARRY_ROUND3_GETPRIORITY_SELECTOR
  - STARRY_ROUND3_GETRLIMIT_CORE
  - STARRY_ROUND3_GETRLIMIT_DISPATCH
  - STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE
  - STARRY_ROUND3_GETTIMEOFDAY_VALUE
  - STARRY_ROUND3_INIT_MODULE_PERMISSION
  - STARRY_ROUND3_JOB_ID_LOOKUP
  - STARRY_ROUND3_PROCESS_LOOKUP
  dynamic_tests: []
revalidation_scope:
  rules: []
  static_checks: []
  dynamic_tests: []
effective_execution_scope: &id001
  rules:
  - LTP_2554AC2E46FC6A15
  - LTP_2648B36BD9CF39EE
  - LTP_26555A26680524AD
  - LTP_3741A721C9C463D0
  - LTP_3B1458E6E26CBB53
  - LTP_425E5A3502541DE8
  - LTP_466F01834F965621
  - LTP_53E3454ED6EFD842
  - LTP_5B4AA4EE494B37D2
  - LTP_64B1B6EEEC3F79FC
  - LTP_652CE911B47794E0
  - LTP_66C670178B06E9F3
  - LTP_6C14DE68E3C0CC24
  - LTP_729222947741DFD6
  - LTP_74BB3F96CBA52D02
  - LTP_7DFAC48A8971CFE3
  - LTP_88D300A8FB407324
  - LTP_8988E5015778894A
  - LTP_89BB56D579EEF06D
  - LTP_8C1C2578972FCA1D
  - LTP_912BE233FAFE6762
  - LTP_914935DA5C379DA1
  - LTP_91ED7E85761CE00F
  - LTP_9305FA6D8B835652
  - LTP_9461AA782926BAB4
  - LTP_963957F80E751EE6
  - LTP_A0547B601C515355
  - LTP_A363671517C058B1
  - LTP_B058D6B9CBBB459D
  - LTP_BD5C209F4C6EE910
  - LTP_D246498B20D9CB2C
  - LTP_DA65D6C7A0E4ABBC
  - LTP_E6C69C9F4AB565BC
  - LTP_EA953D5E5C4B2B1F
  - LTP_EB1B734A0943248E
  - LTP_F8FD511858BB650D
  - LTP_F92A1A6292F40811
  - LTP_FADBA4ADECCFBA4E
  - LTP_FB0ABF26A21EAE3C
  - LTP_FC1E41C3414E7F21
  - LTP_FCF5A4835CFCD143
  static_checks:
  - STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS
  - STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO
  - STARRY_EPOLL_NESTED_LOOP
  - STARRY_FINIT_MODULE_FLAG_VALIDATION
  - STARRY_ROUND3_ERRNO_TRANSLATION
  - STARRY_ROUND3_FSTATFS_ERRORS
  - STARRY_ROUND3_FSTAT_CORE
  - STARRY_ROUND3_FTRUNCATE_NEGATIVE
  - STARRY_ROUND3_GETCWD
  - STARRY_ROUND3_GETPRIORITY_SELECTOR
  - STARRY_ROUND3_GETRLIMIT_CORE
  - STARRY_ROUND3_GETRLIMIT_DISPATCH
  - STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE
  - STARRY_ROUND3_GETTIMEOFDAY_VALUE
  - STARRY_ROUND3_INIT_MODULE_PERMISSION
  - STARRY_ROUND3_JOB_ID_LOOKUP
  - STARRY_ROUND3_PROCESS_LOOKUP
  dynamic_tests: []
execution_scope: *id001
rule_syscalls:
  LTP_004E24807F6067A5:
  - madvise
  LTP_0080969B4E1A8F96:
  - init_module
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
  LTP_02D0577172D97F4B:
  - ftruncate
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
  LTP_0B982157D25C1D06:
  - getsockopt
  LTP_0BB235F712E819CE:
  - access
  LTP_0CD17E662AFD2956:
  - close
  LTP_0D1782EAAC26DEB4:
  - access
  LTP_0D3B043506A61BD6:
  - init_module
  LTP_0D9BB2CB02786128:
  - fsconfig
  LTP_0DF4BC077C390176:
  - fsconfig
  LTP_0E114DF9B3215650:
  - finit_module
  LTP_0E51A1345D29A74B:
  - madvise
  LTP_0E9AF2C058AF8126:
  - access
  LTP_0EBD1214FC6BB6D5:
  - dup
  LTP_0EEA999DE0FFD37D:
  - getsockopt
  LTP_0F02943A8FDA4830:
  - getpriority
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
  LTP_1264D075DA68BB98:
  - iopl
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
  LTP_1ADEBF230DD2C214:
  - epoll_wait
  LTP_1B2E614CA8847B31:
  - llistxattr
  LTP_1B3AD244C58835E7:
  - madvise
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
  LTP_1D3F4A6BCBF6BBE5:
  - init_module
  LTP_1D6E9D5C4E09D7F5:
  - madvise
  LTP_1DF2B28499E4D7B3:
  - access
  LTP_1EEDAE05876D0546:
  - fpathconf
  LTP_1F8223E4EE64B649:
  - listxattr
  LTP_208C833FF12217F5:
  - capget
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
  LTP_2554AC2E46FC6A15:
  - getrlimit
  LTP_25639C9C5750C487:
  - access
  LTP_2648B36BD9CF39EE:
  - ftruncate
  LTP_26555A26680524AD:
  - getrlimit
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
  LTP_2A3276D2B0A31AC9:
  - madvise
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
  LTP_31E977FBCF448AFD:
  - listxattr
  LTP_32D132100CDC04ED:
  - lstat
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
  LTP_352394AAA6D49339:
  - getpgid
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
  LTP_37C625BD7D7C5F1D:
  - dup3
  LTP_37F2ED2BA3175CC3:
  - epoll_create
  LTP_380714557B4AE9D4:
  - madvise
  LTP_38FB918826669241:
  - access
  LTP_39008564F17DCBDD:
  - getdents64
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
  LTP_3B1458E6E26CBB53:
  - getrlimit
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
  LTP_3F7F517D8AA3614C:
  - get_robust_list
  LTP_3F81436312777EF4:
  - access
  LTP_401D471D37C85820:
  - access
  LTP_409C97094F0CED1F:
  - getdents64
  LTP_425E5A3502541DE8:
  - close_range
  LTP_437CFCD991A666C9:
  - faccessat2
  LTP_44128D8D82BC1E09:
  - flock
  LTP_44B41305EB538966:
  - getdents64
  LTP_453DFC908EB0DD9E:
  - init_module
  LTP_45439D8F2BAB0832:
  - mmap
  LTP_461340ED83E7043D:
  - capset
  LTP_46401248F52AD892:
  - fsconfig
  LTP_4661BBF1B3CD3A1E:
  - access
  LTP_466F01834F965621:
  - fstat
  LTP_468FC84DEAB0BCB8:
  - epoll_ctl
  LTP_46AA49209C30E739:
  - ftruncate
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
  LTP_505DF8E6B5595F9E:
  - madvise
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
  LTP_52CE7E6F9B5FF947:
  - getsockname
  LTP_52FC519F20674559:
  - kill
  LTP_53B499F623D50A0A:
  - fsconfig
  LTP_53E3454ED6EFD842:
  - getcwd
  LTP_54CE18AAE5BDB693:
  - madvise
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
  LTP_57C7DC5E29B5ADF8:
  - getpriority
  LTP_582938D6E8E17DB3:
  - fpathconf
  LTP_58416E6747519699:
  - access
  LTP_5883CD050463E9E8:
  - epoll_ctl
  LTP_58F1512157A0052D:
  - access
  LTP_5920F12CFE459CB8:
  - getsockname
  LTP_594FA5B54CA204E5:
  - dup
  LTP_5A315335586D4227:
  - access
  LTP_5A7E16725228EB1E:
  - madvise
  LTP_5B244D0A4892F35A:
  - finit_module
  LTP_5B4AA4EE494B37D2:
  - gettimeofday
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
  LTP_5E6E4D23F79BC9DA:
  - ftruncate
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
  LTP_62FDC6AAFC4F4DE5:
  - getsockname
  LTP_636590E5A017B28D:
  - access
  LTP_63E6527501A08F92:
  - ftruncate
  LTP_64227C746913D03D:
  - access
  LTP_6449E4A1D20C01D3:
  - alarm
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
  LTP_66C670178B06E9F3:
  - epoll_ctl
  LTP_67180EB1CFAAB816:
  - llistxattr
  LTP_679436EC7A4E218A:
  - access
  LTP_67BF94A4ACD303C4:
  - access
  LTP_68745D21F4EC2FF5:
  - access
  LTP_6882C814E58F3D3B:
  - madvise
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
  LTP_6A52E2C16AC64CEC:
  - madvise
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
  LTP_6C14DE68E3C0CC24:
  - gettimeofday
  LTP_6C55A3E760DF75DB:
  - access
  LTP_6CE9FC3BCA164B5D:
  - access
  LTP_6D195DDAB1BE2B57:
  - kill
  LTP_6D584CE6CF9B8A06:
  - access
  LTP_6D86AFD541A61388:
  - capset
  LTP_6DF55FF20A44572D:
  - getpriority
  LTP_6EF7ECD2A8470CEA:
  - access
  LTP_6FFB17DB762F3167:
  - epoll_ctl
  LTP_708F721FB3456F82:
  - fsconfig
  LTP_70E5CA8341B80E83:
  - getcontext
  LTP_711D5693356A79F2:
  - access
  LTP_71C54C624831C7F0:
  - chroot
  LTP_725BDB092C6D8F74:
  - execveat
  LTP_729222947741DFD6:
  - getcwd
  LTP_73DF50509BCC128B:
  - access
  LTP_74819A9DC2B5CB06:
  - access
  LTP_74BAD566B6A0F272:
  - finit_module
  LTP_74BB3F96CBA52D02:
  - copy_file_range
  LTP_74DD0DCF0CE8388F:
  - lgetxattr
  LTP_74E00510F4C1B849:
  - connect
  LTP_752C9A802CF96B8B:
  - access
  LTP_753BDF43E7947404:
  - madvise
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
  LTP_7786636C200E9E5C:
  - lremovexattr
  LTP_77AA3EAF2AD0C07A:
  - faccessat2
  LTP_77C73AE1FE592877:
  - init_module
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
  LTP_7A6820B73D1C2059:
  - iopl
  LTP_7A74A699442CEB99:
  - brk
  LTP_7AF4AAC644090507:
  - finit_module
  LTP_7B539E14354153DC:
  - access
  LTP_7B9FBEA6E7CF8A70:
  - gethostid
  LTP_7BE2877017694C52:
  - access
  LTP_7C0112A92527C2A7:
  - fstatfs
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
  LTP_7DFAC48A8971CFE3:
  - getrlimit
  LTP_7E1612F09CACE33D:
  - copy_file_range
  LTP_7EAD5A075576B981:
  - flock
  LTP_7ECC43C03A3DCB14:
  - fsconfig
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
  LTP_8059D9227293D592:
  - access
  LTP_807E2072E5694684:
  - access
  LTP_809809859ABFE5C1:
  - getsockopt
  LTP_80AFFD1BF1D04F38:
  - init_module
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
  LTP_8703114C595382AB:
  - madvise
  LTP_8710A0CE4DCC217D:
  - lgetxattr
  LTP_87478A6C3AC7DC60:
  - access
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
  LTP_8CA8B0BC6ED845C4:
  - getdents64
  LTP_8CB51F0A9F8FDEA1:
  - access
  LTP_8D3BFFA98E2561BA:
  - access
  LTP_8D54825D4B298C7C:
  - access
  LTP_8D6B83A8176DB57E:
  - listxattr
  LTP_8E7F1BE3D7D7823B:
  - access
  LTP_8F29388433422812:
  - access
  LTP_8F30861E18D66625:
  - epoll_wait
  LTP_8F9E255B19623C24:
  - listxattr
  LTP_8FF73194288F8473:
  - access
  LTP_90068DD4526FEFC0:
  - fstatat
  LTP_906135780505447D:
  - access
  LTP_90893935E64240AA:
  - getpagesize
  LTP_90B95E5DF2BD7509:
  - fstatfs
  LTP_911B97B972658989:
  - access
  LTP_912BE233FAFE6762:
  - getcwd
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
  LTP_9461AA782926BAB4:
  - getpgid
  LTP_94E36E221125BFAF:
  - access
  LTP_955ECE70D81CA226:
  - access
  LTP_9586C4C3CAC60BBC:
  - lgetxattr
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
  LTP_97C442AC56780374:
  - access
  LTP_9847441A67CBCED8:
  - madvise
  LTP_9866FB6F1F726CA0:
  - access
  LTP_986F211E7D45CAD7:
  - access
  LTP_98EC66149EE68933:
  - alarm
  LTP_99C45ECA20496C98:
  - getpriority
  LTP_99DF5C34778032E1:
  - chroot
  LTP_9A723EA0B1F0D1BE:
  - access
  LTP_9B0BA3ADF46F5FF4:
  - getpriority
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
  LTP_9FB758C1B4AF2411:
  - lstat
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
  LTP_A1B6FBC6EF800331:
  - fchmod
  LTP_A1D08F4E94B7899A:
  - listen
  LTP_A1DEE046C0A10B18:
  - access
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
  LTP_A4733D4B2FEBE9A4:
  - access
  LTP_A500A46C4B998E74:
  - access
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
  LTP_A9DD0D461E032A07:
  - fsconfig
  LTP_AA9171FB32FD0C67:
  - getsockname
  LTP_AB48F262BBB2CC93:
  - access
  LTP_ABB01FA7743F966A:
  - listen
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
  LTP_B058D6B9CBBB459D:
  - getrlimit
  LTP_B1D822DF0057B4E0:
  - access
  LTP_B200AFD97E91C2CC:
  - access
  LTP_B25461243478CEF8:
  - getsockname
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
  LTP_B72405976D9F15E6:
  - getsockopt
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
  LTP_BF679B7A7E60BCFD:
  - fpathconf
  LTP_BFCEAB073A576D51:
  - madvise
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
  LTP_C80C019BE3F47901:
  - alarm
  LTP_C8DAE34819E335F8:
  - access
  LTP_C93391BCF53E8020:
  - kill
  LTP_C9789067DD7A3D60:
  - llistxattr
  LTP_C994B56A41A71C1A:
  - access
  LTP_C9D2C2E3FC2B9581:
  - llistxattr
  LTP_CA3E9D83D71EEED4:
  - lstat
  LTP_CA45A33676AD236D:
  - access
  LTP_CA80C3F10B65226D:
  - access
  LTP_CB31E19EE807FFDB:
  - access
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
  LTP_D0BAC1CBF594EDA6:
  - madvise
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
  LTP_D246498B20D9CB2C:
  - init_module
  LTP_D296A517F138A0C0:
  - dup2
  LTP_D2D67AB5E38A7000:
  - access
  LTP_D2F4BCF2263C56F5:
  - access
  LTP_D412A09DEDC43045:
  - access
  LTP_D4159BF3AB78E108:
  - llistxattr
  LTP_D4B433A3696803A8:
  - alarm
  LTP_D4D8A0FEAA2F6B09:
  - access
  LTP_D579FCFC71E6EB6A:
  - cacheflush
  LTP_D58C26D260BBCED5:
  - init_module
  LTP_D5D78F93265A1980:
  - fsconfig
  LTP_D5DAD3494DBAE67F:
  - getpriority
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
  LTP_D77AD0D4DC9C0C9E:
  - getsockopt
  LTP_D839FF9444196DDB:
  - madvise
  LTP_D8B58CA743EBE711:
  - access
  LTP_D90E4279570B6A94:
  - madvise
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
  LTP_DBFBE6A110B3D17B:
  - getsockname
  LTP_DC1ACD3B300AFCC3:
  - getsockopt
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
  LTP_E083F071E292B561:
  - gettid
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
  LTP_E5791B389C67677E:
  - access
  LTP_E5E50FB7BDD033D9:
  - access
  LTP_E6750A641272AF1B:
  - fsconfig
  LTP_E6C69C9F4AB565BC:
  - getrlimit
  LTP_E7435E0CBCA319E1:
  - epoll_create
  LTP_E8CF2AE0EC60602C:
  - epoll_wait
  LTP_E8E97EBE8E041CF0:
  - kill
  LTP_EA5D1572B890F71E:
  - epoll_wait
  LTP_EA953D5E5C4B2B1F:
  - getrlimit
  LTP_EB00EA74B30E438E:
  - access
  LTP_EB1B734A0943248E:
  - fstatfs
  LTP_EB214534D857AE95:
  - ftruncate
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
  LTP_F13024AE4BC5C024:
  - kill
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
  LTP_F65E54AE96F20D41:
  - fchmodat2
  LTP_F66773BC44256D99:
  - lgetxattr
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
  LTP_FADBA4ADECCFBA4E:
  - getrlimit
  LTP_FB047DBB72D78D19:
  - flock
  LTP_FB0ABF26A21EAE3C:
  - getrlimit
  LTP_FBEB6959ED2912C8:
  - iopl
  LTP_FC1E41C3414E7F21:
  - getcwd
  LTP_FC5B16AB3C53A744:
  - access
  LTP_FCA376B46A9873B0:
  - access
  LTP_FCF5A4835CFCD143:
  - gettimeofday
  LTP_FD1B65B0BCC88E0D:
  - mmap
  LTP_FDE0B30F1CFCAA4B:
  - fsconfig
  LTP_FE51D85F4A425C61:
  - getsockopt
  LTP_FEACDC300C3E1DD7:
  - mmap
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
    line: 41
  - label: unsupported nonzero flags return InvalidInput
    regex: pub fn sys_finit_module\([\s\S]*?if flags != 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}
    matched: true
    line: 41
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND3_ERRNO_TRANSLATION
  rule_refs:
  - LTP_2648B36BD9CF39EE
  - LTP_466F01834F965621
  - LTP_53E3454ED6EFD842
  - LTP_5B4AA4EE494B37D2
  - LTP_64B1B6EEEC3F79FC
  - LTP_6C14DE68E3C0CC24
  - LTP_729222947741DFD6
  - LTP_88D300A8FB407324
  - LTP_89BB56D579EEF06D
  - LTP_8C1C2578972FCA1D
  - LTP_912BE233FAFE6762
  - LTP_9461AA782926BAB4
  - LTP_D246498B20D9CB2C
  - LTP_EB1B734A0943248E
  - LTP_F8FD511858BB650D
  - LTP_F92A1A6292F40811
  - LTP_FC1E41C3414E7F21
  - LTP_FCF5A4835CFCD143
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
  - LTP_EB1B734A0943248E
  - LTP_F92A1A6292F40811
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/stat.rs
  patterns:
  - label: fstatfs obtains a real file from the descriptor
    regex: 'pub fn sys_fstatfs\(fd: i32, buf: \*mut statfs\)[\s\S]*?File::from_fd\(fd\)\?'
    matched: true
    line: 245
  - label: fstatfs writes via checked VM access
    regex: buf\.vm_write\(statfs\([\s\S]*?\)\?\)\?;
    matched: true
    line: 235
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND3_FSTAT_CORE
  rule_refs:
  - LTP_466F01834F965621
  - LTP_64B1B6EEEC3F79FC
  - LTP_A363671517C058B1
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/stat.rs
  patterns:
  - label: fstat uses the descriptor form of fstatat
    regex: 'pub fn sys_fstat\(fd: i32, statbuf: \*mut stat\)[\s\S]*?sys_fstatat\(fd, core::ptr::null\(\),
      statbuf, AT_EMPTY_PATH\)'
    matched: true
    line: 44
  - label: fstatat resolves the supplied descriptor and path
    regex: pub fn sys_fstatat\([\s\S]*?let loc = resolve_at\(dirfd, path\.as_deref\(\), flags\)\?;
    matched: true
    line: 58
  - label: stat output is copied through checked VM access
    regex: statbuf\.vm_write\(loc\.stat\(\)\?\.into\(\)\)\?;
    matched: true
    line: 76
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND3_FTRUNCATE_NEGATIVE
  rule_refs:
  - LTP_2648B36BD9CF39EE
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/io.rs
  patterns:
  - label: negative lengths return InvalidInput first
    regex: pub fn sys_ftruncate\([\s\S]*?if length < 0 \{\s*return Err\(AxError::InvalidInput\);\s*\}[\s\S]*?File::from_fd\(fd\)
    matched: true
    line: 237
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND3_GETCWD
  rule_refs:
  - LTP_53E3454ED6EFD842
  - LTP_729222947741DFD6
  - LTP_89BB56D579EEF06D
  - LTP_912BE233FAFE6762
  - LTP_FC1E41C3414E7F21
  result: pass
  path: os/StarryOS/kernel/src/syscall/fs/ctl.rs
  patterns:
  - label: signed size conversion rejects impossible sizes
    regex: 'pub fn sys_getcwd\([\s\S]*?let size: usize = size\.try_into\(\)\.map_err\(\|_\| AxError::BadAddress\)\?;'
    matched: true
    line: 418
  - label: the C string length includes its terminator
    regex: let cwd = cwd\.as_bytes_with_nul\(\);
    matched: true
    line: 425
  - label: short buffers return OutOfRange
    regex: if cwd\.len\(\) <= size \{[\s\S]*?vm_write_slice\(buf, cwd\)\?;[\s\S]*?\} else \{\s*Err\(AxError::OutOfRange\)
    matched: true
    line: 427
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND3_GETPRIORITY_SELECTOR
  rule_refs:
  - LTP_88D300A8FB407324
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
  - LTP_963957F80E751EE6
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
  - LTP_963957F80E751EE6
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
    line: 645
  reason: all required patterns matched
  finding_ids: []
- check_id: STARRY_ROUND3_GETTIMEOFDAY_TIMEZONE
  rule_refs:
  - LTP_6C14DE68E3C0CC24
  result: fail
  path: os/StarryOS/kernel/src/syscall/time.rs
  patterns:
  - label: handler accepts both timeval and timezone pointers
    regex: 'pub fn sys_gettimeofday\(ts: \*mut timeval, tz: \*mut Timezone\)'
    matched: false
    line: null
  - label: non-null timezone output uses checked VM access
    regex: tz\.nullable\(\)[\s\S]*?tz\.vm_write\(Timezone::default\(\)\)\?;
    matched: false
    line: null
  reason: one or more required patterns did not match
  finding_ids:
  - finding-gettimeofday-ltp-6c14de68e3c0cc24-117b5f149133
- check_id: STARRY_ROUND3_GETTIMEOFDAY_VALUE
  rule_refs:
  - LTP_5B4AA4EE494B37D2
  - LTP_FCF5A4835CFCD143
  result: pass
  path: os/StarryOS/kernel/src/syscall/time.rs
  patterns:
  - label: timeval is written with VM validation
    regex: pub fn sys_gettimeofday\([\s\S]*?ts\.vm_write\(timeval::from_time_value\(wall_time\(\)\)\)\?;
    matched: true
    line: 36
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
  finding_ids:
  - finding-init-module-ltp-d246498b20d9cb2c-117b5f149133
- check_id: STARRY_ROUND3_JOB_ID_LOOKUP
  rule_refs:
  - LTP_8C1C2578972FCA1D
  - LTP_9461AA782926BAB4
  - LTP_F8FD511858BB650D
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
dynamic: []
counts:
  static_pass: 15
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
- finding-gettimeofday-ltp-6c14de68e3c0cc24-117b5f149133
- finding-init-module-ltp-d246498b20d9cb2c-117b5f149133
finding_versions:
  finding-gettimeofday-ltp-6c14de68e3c0cc24-117b5f149133:
    id: finding-gettimeofday-ltp-6c14de68e3c0cc24-117b5f149133
    generated_at_utc: '2026-07-16T03:46:03.609800Z'
    content_hash: sha256:55de5b7079e9de5b84a2d2b10670bf015e1f0c7b0608c050f7f50d3c5503786f
  finding-init-module-ltp-d246498b20d9cb2c-117b5f149133:
    id: finding-init-module-ltp-d246498b20d9cb2c-117b5f149133
    generated_at_utc: '2026-07-16T03:46:03.609800Z'
    content_hash: sha256:5158779bf71318b08cb6011af8990d93f3ea9398d94ef617df2343683a790f4e
new_finding_ids:
- finding-gettimeofday-ltp-6c14de68e3c0cc24-117b5f149133
- finding-init-module-ltp-d246498b20d9cb2c-117b5f149133
carried_finding_ids: []
revalidated_finding_ids: []
needs_revalidation_finding_ids: []
historical_regression_scope:
  rules:
  - LTP_425E5A3502541DE8
  - LTP_66C670178B06E9F3
  - LTP_74BB3F96CBA52D02
  static_checks:
  - STARRY_CLOSE_RANGE_UNSIGNED_BOUNDS
  - STARRY_COPY_FILE_RANGE_OVERFLOW_ERRNO
  - STARRY_EPOLL_NESTED_LOOP
  dynamic_tests: []
historical_regression_unresolved: {}
content_hash: sha256:ef0d046052dd0043e218a416ae15bcff64570d208da309a1607293848c752401
```
</details>
