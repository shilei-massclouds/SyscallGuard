# Starry 规则映射报告

## 本轮结论

- 本轮产生静态检查：8
- 本轮产生动态测试：0
- 全局剩余规则：288（pending 0、needs_review 265、unsupported 23）

## 完整规则关系

### `accept`

| rule_id | 静态检查 | 动态测试 | 状态 | 原因 |
| --- | --- | --- | --- | --- |
| `LTP_277FD467E5F1BF1C` | — | — | `needs_review` | 规则依赖 socket 类型、监听或连接队列、地址长度、用户指针以及 exp_errno 等运行时状态；现有静态分支无法唯一确定预期结果。 |
| `LTP_472AAA35C7382B26` | — | — | `needs_review` | 规则依赖 socket 类型、监听或连接队列、地址长度、用户指针以及 exp_errno 等运行时状态；现有静态分支无法唯一确定预期结果。 |
| `LTP_80C6DB0ACB2A5510` | — | — | `needs_review` | 规则依赖 socket 类型、监听或连接队列、地址长度、用户指针以及 exp_errno 等运行时状态；现有静态分支无法唯一确定预期结果。 |
| `LTP_9CA9C6B61C3317A3` | — | — | `needs_review` | 规则依赖 socket 类型、监听或连接队列、地址长度、用户指针以及 exp_errno 等运行时状态；现有静态分支无法唯一确定预期结果。 |
| `LTP_B90CB73F36B70C6F` | — | — | `needs_review` | 规则依赖 socket 类型、监听或连接队列、地址长度、用户指针以及 exp_errno 等运行时状态；现有静态分支无法唯一确定预期结果。 |
| `LTP_E13B9C2C9645B841` | — | — | `needs_review` | 规则依赖 socket 类型、监听或连接队列、地址长度、用户指针以及 exp_errno 等运行时状态；现有静态分支无法唯一确定预期结果。 |
| `LTP_F1044C71B6626419` | — | — | `needs_review` | 规则依赖 socket 类型、监听或连接队列、地址长度、用户指针以及 exp_errno 等运行时状态；现有静态分支无法唯一确定预期结果。 |

### `access`

| rule_id | 静态检查 | 动态测试 | 状态 | 原因 |
| --- | --- | --- | --- | --- |
| `LTP_0180982614AA9F7D` | `STARRY_ACCESS_PERMISSIONS` | — | `covered` | sys_access 委托 sys_faccessat2；F_OK 快速成功，并按 root 及 owner/group/other 有效权限位检查 R_OK、W_OK、X_OK，静态覆盖 access02 权限案例。 |
| `LTP_0290063892A53510` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_030858A5FFCCEFF4` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_035E62E6D1787773` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_036EDA2B8D36CF03` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_037E6F334D0E0D16` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_0431E3529AA0FEE8` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_044E7C11E6B503BB` | `STARRY_ACCESS_PERMISSIONS` | — | `covered` | sys_access 委托 sys_faccessat2；F_OK 快速成功，并按 root 及 owner/group/other 有效权限位检查 R_OK、W_OK、X_OK，静态覆盖 access02 权限案例。 |
| `LTP_060B6037DEF1D43C` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_06725D44DFF06F7E` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_06891E2E299CF48E` | `STARRY_ACCESS_PERMISSIONS` | — | `covered` | sys_access 委托 sys_faccessat2；F_OK 快速成功，并按 root 及 owner/group/other 有效权限位检查 R_OK、W_OK、X_OK，静态覆盖 access02 权限案例。 |
| `LTP_06A0C295D8E7FAFA` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_06AC9297E35AAE7A` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_075318C437B76E06` | `STARRY_ACCESS_USER_POINTER`、`STARRY_BATCH_ERRNO_TRANSLATION` | — | `covered` | sys_faccessat2 在路径解析前通过 vm_load_path_string 读取用户字符串；坏地址传播为 BadAddress，并由 errno 转换为 EFAULT。 |
| `LTP_0799FC60BADD2B18` | `STARRY_ACCESS_USER_POINTER`、`STARRY_BATCH_ERRNO_TRANSLATION` | — | `covered` | sys_faccessat2 在路径解析前通过 vm_load_path_string 读取用户字符串；坏地址传播为 BadAddress，并由 errno 转换为 EFAULT。 |
| `LTP_0A62800536904C02` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_0AAFA34BA77A0D25` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_0B45FC33068D334C` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_0BB235F712E819CE` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_0D1782EAAC26DEB4` | `STARRY_ACCESS_PERMISSIONS` | — | `covered` | sys_access 委托 sys_faccessat2；F_OK 快速成功，并按 root 及 owner/group/other 有效权限位检查 R_OK、W_OK、X_OK，静态覆盖 access02 权限案例。 |
| `LTP_0E9AF2C058AF8126` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_0F901C62092CC7B8` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_10A684C1C2D2DE0F` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_10FE1313FBAB5F92` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_1402459B5FF9BF23` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_1465554B09CE14F0` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_148623FDAF4E478D` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_153B296FA599E0CE` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_17ACF3BE969B64EE` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_17CB4ED7A76BD283` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_1870C0046E9555AF` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_18A450CE49F8867B` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_198D9555A8BED013` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_1BD36AE285B4F3E2` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_1C462AC54A29FF35` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_1CDCF5FE9ED1BE5D` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_1D39F97D759F0E57` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_1DF2B28499E4D7B3` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_212269CECE600FD8` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_21A007DF738F1E73` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_21C4957F9EFE94D3` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_220D1227D307AD3C` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_2221F954D01EB2BB` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_25639C9C5750C487` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_26AC646B9D18C353` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_27C7E91095DB9DF8` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_2900BC64740A3E44` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_298AB67F0CFA519C` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_2B4171DD8FBD982A` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_2D0BAECAE4F61432` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_2E5D530A61E60934` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_2F99FA84C445363C` | `STARRY_ACCESS_PATH_RESOLUTION`、`STARRY_BATCH_ERRNO_TRANSLATION` | — | `covered` | sys_faccessat2 加载路径后调用 resolve_at/FsContext 路径解析；缺失项、非目录组件、符号链接循环和超长路径错误按 Linux errno 传播。 |
| `LTP_2FA43CD942AE7AD6` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_2FE8FAD800DE41F6` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_3472CD1A0F8A2B4A` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_347761CBCF52D194` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_34CFEAD03DB6A3CA` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_35CAEE10A613E109` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_3636C4768C196B52` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_368D8689810796B2` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_38FB918826669241` | `STARRY_ACCESS_USER_POINTER`、`STARRY_BATCH_ERRNO_TRANSLATION` | — | `covered` | sys_faccessat2 在路径解析前通过 vm_load_path_string 读取用户字符串；坏地址传播为 BadAddress，并由 errno 转换为 EFAULT。 |
| `LTP_3900F4E562AE09D1` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_3916A669595B3568` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_3AD3865603ADDC8E` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_3C2853617B38EEE7` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_3D4ECD22BC433164` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_3D8D38C9123CD051` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_3DE23AB4FE2FFC67` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_3E526A0A23B5EF6D` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_3F81436312777EF4` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_401D471D37C85820` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_4661BBF1B3CD3A1E` | `STARRY_ACCESS_PATH_RESOLUTION`、`STARRY_BATCH_ERRNO_TRANSLATION` | — | `covered` | sys_faccessat2 加载路径后调用 resolve_at/FsContext 路径解析；缺失项、非目录组件、符号链接循环和超长路径错误按 Linux errno 传播。 |
| `LTP_46DE8D9AD1674F26` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_479924116854D92B` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_48753F73ACA755FB` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_4881657CFE57C7E9` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_492D25A0F1055F72` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_4948E12FB8F9FA49` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_49700CDA955B66D8` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_49A36559B96D24AF` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_4B6E9B98E2E5103D` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_4CFAFCE7FCA2BF99` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_4ECB786BFA071AAC` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_50A86D4D5411356E` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_52C209105EE62171` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_5570480E7920BD0E` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_563FB650864E0DC6` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_58416E6747519699` | `STARRY_ACCESS_USER_POINTER`、`STARRY_BATCH_ERRNO_TRANSLATION` | — | `covered` | sys_faccessat2 在路径解析前通过 vm_load_path_string 读取用户字符串；坏地址传播为 BadAddress，并由 errno 转换为 EFAULT。 |
| `LTP_58F1512157A0052D` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_5A315335586D4227` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_5C5CDC165410C08C` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_5CC44E5D1A6B6485` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_5D7971086B2ABAE5` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_5EC31E34822684C4` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_606B7E40B6BD82EA` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_613A5E121B4B6E68` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_6156A09A2E506F76` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_6169F41023E00C34` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_636590E5A017B28D` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_64227C746913D03D` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_64A4E5DC71A633A2` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_65281FBEE0BF6103` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_6580B4D3FA1A86F3` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_679436EC7A4E218A` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_67BF94A4ACD303C4` | `STARRY_ACCESS_PERMISSIONS` | — | `covered` | sys_access 委托 sys_faccessat2；F_OK 快速成功，并按 root 及 owner/group/other 有效权限位检查 R_OK、W_OK、X_OK，静态覆盖 access02 权限案例。 |
| `LTP_68745D21F4EC2FF5` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_68E1B26815D97B79` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_69077B093E81B570` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_690A651C3A60FC1E` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_69E094D1DBFF3796` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_6A1A431A08A3F450` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_6B1746F6BB2266CA` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_6B8B5453E8B4E6DE` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_6C11BBB4AABA6E7C` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_6C55A3E760DF75DB` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_6CE9FC3BCA164B5D` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_6D584CE6CF9B8A06` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_6EF7ECD2A8470CEA` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_711D5693356A79F2` | `STARRY_ACCESS_PERMISSIONS` | — | `covered` | sys_access 委托 sys_faccessat2；F_OK 快速成功，并按 root 及 owner/group/other 有效权限位检查 R_OK、W_OK、X_OK，静态覆盖 access02 权限案例。 |
| `LTP_73DF50509BCC128B` | `STARRY_ACCESS_PERMISSIONS` | — | `covered` | sys_access 委托 sys_faccessat2；F_OK 快速成功，并按 root 及 owner/group/other 有效权限位检查 R_OK、W_OK、X_OK，静态覆盖 access02 权限案例。 |
| `LTP_74819A9DC2B5CB06` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_752C9A802CF96B8B` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_78EEEBE648781151` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_7963C3DF373596FE` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_79C7516DECB19092` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_7A02B34D5FB8BBC3` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_7B539E14354153DC` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_7BE2877017694C52` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_7C06A3394E786948` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_7CE7876CE69F200F` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_7DD493976CBC9A31` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_7F5487EEB79017AD` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_7F54F9DFF7E0FB61` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_8059D9227293D592` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_807E2072E5694684` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_818BA624CA9E4040` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_820495EA1D1F15DA` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_82ABB8FBFA06D356` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_82E0F55AEC3D382F` | — | — | `needs_review` | 预期 EROFS 来自上游错误结果反向解析，但规则没有记录只读挂载前置条件；Starry access 路径不足以证明该 errno。 |
| `LTP_830E17210B1FB7AB` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_833C5D5CF3C32C2A` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_839EC7BC904E42D5` | `STARRY_ACCESS_PERMISSIONS` | — | `covered` | sys_access 委托 sys_faccessat2；F_OK 快速成功，并按 root 及 owner/group/other 有效权限位检查 R_OK、W_OK、X_OK，静态覆盖 access02 权限案例。 |
| `LTP_843BDD20FF921FC3` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_84E4CC971DD16EC2` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_853D34D061DDE8F8` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_853F4B8346648EB9` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_857DC6AD01A88D79` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_87478A6C3AC7DC60` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_884775F9076E54AB` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_885F3BA721198C07` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_88F6F279E33633DE` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_8AC11633EA3D83E0` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_8B1A2084BCF096F1` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_8B3FBDFD0453EF40` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_8BB576EB2E1E6B23` | `STARRY_ACCESS_PATH_RESOLUTION`、`STARRY_BATCH_ERRNO_TRANSLATION` | — | `covered` | sys_faccessat2 加载路径后调用 resolve_at/FsContext 路径解析；缺失项、非目录组件、符号链接循环和超长路径错误按 Linux errno 传播。 |
| `LTP_8C508A50371B6444` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_8CB51F0A9F8FDEA1` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_8D3BFFA98E2561BA` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_8D54825D4B298C7C` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_8E7F1BE3D7D7823B` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_8F29388433422812` | — | — | `needs_review` | 动作使用 mode=-1，但上游把前置条件记录为 INVALID_FD；access 没有 fd 参数，语义前置条件不完整，需先复核规则。 |
| `LTP_8FF73194288F8473` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_906135780505447D` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_911B97B972658989` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_919ABCA2598F53B5` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_921D4802D7690C64` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_9260E923CF8AA018` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_929B120944D8F805` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_93949494FBAD3568` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_94E36E221125BFAF` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_955ECE70D81CA226` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_96021AFB69E847F9` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_969C39F409BFD7AA` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_96D205FACA0DD8DB` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_96F07DC5DDC8E018` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_97C442AC56780374` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_9866FB6F1F726CA0` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_986F211E7D45CAD7` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_9A723EA0B1F0D1BE` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_9C9D222A34799D55` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_9CDCD3C4BA6C2702` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_A17272D4FE0F040B` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_A1DEE046C0A10B18` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_A30F7687D403407B` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_A4060315D2E047EE` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_A4733D4B2FEBE9A4` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_A500A46C4B998E74` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_A6B94E8A2A4D8853` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_A9544B59EB6712D9` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_A9596E932167B3EF` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_AB48F262BBB2CC93` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_AC0FB73B4EE420EC` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_AD81218450587FA8` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_ADD30BEEC40E661F` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_B1D822DF0057B4E0` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_B200AFD97E91C2CC` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_B53406D510ED4981` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_B6DAF13EF3143EBF` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_B9908D4015443661` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_B9CDD41A0DC2AFCC` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_BA10984A4B0DE2C6` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_BC662075E3BAE807` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_BE2E778739EF01D5` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_C0577C0D678214DA` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_C071A7FFF929A2A5` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_C0AA45BC29F98A0E` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_C1C67435FC56D878` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_C5FE18F9550B31BA` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_C6A719982BDE9CE4` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_C6E67CB1FD2B1F64` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_C8DAE34819E335F8` | `STARRY_ACCESS_PATH_RESOLUTION`、`STARRY_BATCH_ERRNO_TRANSLATION` | — | `covered` | sys_faccessat2 加载路径后调用 resolve_at/FsContext 路径解析；缺失项、非目录组件、符号链接循环和超长路径错误按 Linux errno 传播。 |
| `LTP_C994B56A41A71C1A` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_CA45A33676AD236D` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_CA80C3F10B65226D` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_CB31E19EE807FFDB` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_CCDB1776DAA2C318` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_CDCDC1B9E63D58C3` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_CE45382D3DE75F8F` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_CEBAD6AB3C82795E` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_D1F469715ECC4195` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_D2D67AB5E38A7000` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_D2F4BCF2263C56F5` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_D412A09DEDC43045` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_D4D8A0FEAA2F6B09` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_D653D15777B77A1F` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_D6A52FD61BF01578` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_D72526C4E4301D60` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_D76652434EC85091` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_D8B58CA743EBE711` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_DA10E351BC730D85` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_DAA03BAD070DB1D6` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_DAA1F16D8A298E83` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_DCB33BB29D296843` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_DD9A41090E3D5A17` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_DF1C4714B16B760E` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_E0B177A8B6FE4225` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_E0ED96B80FC3B6C9` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_E28B5BB57A450438` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_E2C3B68EDF07A753` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_E34945E3DE91022F` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_E3A3CF8B98E460BC` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_E41DD7230DA067DD` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_E46539F2D47BA5EC` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_E4D1B76D80905462` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_E560C027210BF20A` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_E5791B389C67677E` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_E5E50FB7BDD033D9` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_EB00EA74B30E438E` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_EB425D988F2F7604` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_EBF0020C32AD44C8` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_EC19C6410BBE0467` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_ED36488372A175F5` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_ED3F2AE7E59E6F12` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_EE1518958A8F7CC1` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_EF5C1F365208AD31` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_F202F3C3B02DEA0E` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_F3200B697F38DD16` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_F3418C5C403B91FC` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_F43EC0D01CCFD25A` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_F6BB86F5DCC2FAC8` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_F70FC66A56FBD769` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_F7998813C90A7A08` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_F8CDD57D76C8FA6C` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_F9BF08369A08E5ED` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_FC5B16AB3C53A744` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |
| `LTP_FCA376B46A9873B0` | — | — | `needs_review` | access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。 |

### `alarm`

| rule_id | 静态检查 | 动态测试 | 状态 | 原因 |
| --- | --- | --- | --- | --- |
| `LTP_1A9481FAD460FBF7` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有 sys_alarm 入口。 |
| `LTP_3E8DA9E014B82702` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有 sys_alarm 入口。 |
| `LTP_6449E4A1D20C01D3` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有 sys_alarm 入口。 |
| `LTP_65B70356F06E31F8` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有 sys_alarm 入口。 |
| `LTP_76A9B6CF388A8609` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有 sys_alarm 入口。 |
| `LTP_82621B02FCA09F40` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有 sys_alarm 入口。 |
| `LTP_98EC66149EE68933` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有 sys_alarm 入口。 |
| `LTP_B7A341967DF2BD69` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有 sys_alarm 入口。 |
| `LTP_C785774773FB7524` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有 sys_alarm 入口。 |
| `LTP_C7B73F4D5B87736A` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有 sys_alarm 入口。 |
| `LTP_C80C019BE3F47901` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有 sys_alarm 入口。 |
| `LTP_CD2150BE4FE81F31` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有 sys_alarm 入口。 |
| `LTP_D1B6112551D45B31` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有 sys_alarm 入口。 |
| `LTP_D4B433A3696803A8` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有 sys_alarm 入口。 |

### `brk`

| rule_id | 静态检查 | 动态测试 | 状态 | 原因 |
| --- | --- | --- | --- | --- |
| `LTP_7A74A699442CEB99` | `STARRY_BRK_HEAP` | — | `covered` | sys_brk 校验 heap 地址范围和 RLIMIT_DATA，按需映射或解除映射，成功后更新 heap_top 并返回新 break。 |
| `LTP_E3E59B16A96A60BC` | `STARRY_BRK_HEAP` | — | `covered` | sys_brk 校验 heap 地址范围和 RLIMIT_DATA，按需映射或解除映射，成功后更新 heap_top 并返回新 break。 |

### `cacheflush`

| rule_id | 静态检查 | 动态测试 | 状态 | 原因 |
| --- | --- | --- | --- | --- |
| `LTP_8AD8032754BC8842` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::cacheflush 分派分支，syscall 实现目录中也没有 sys_cacheflush 入口。 |
| `LTP_C218D3CB0AD80D90` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::cacheflush 分派分支，syscall 实现目录中也没有 sys_cacheflush 入口。 |
| `LTP_D579FCFC71E6EB6A` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::cacheflush 分派分支，syscall 实现目录中也没有 sys_cacheflush 入口。 |

### `cachestat`

| rule_id | 静态检查 | 动态测试 | 状态 | 原因 |
| --- | --- | --- | --- | --- |
| `LTP_00F2A9EA8833DA1D` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::cachestat 分派分支，syscall 实现目录中也没有 sys_cachestat 入口。 |
| `LTP_1325C077A1CDE514` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::cachestat 分派分支，syscall 实现目录中也没有 sys_cachestat 入口。 |
| `LTP_34EC9FB9C9551214` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::cachestat 分派分支，syscall 实现目录中也没有 sys_cachestat 入口。 |
| `LTP_7FD6142E0E88CF17` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::cachestat 分派分支，syscall 实现目录中也没有 sys_cachestat 入口。 |
| `LTP_89C9E8458EC38C11` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::cachestat 分派分支，syscall 实现目录中也没有 sys_cachestat 入口。 |
| `LTP_BA9A8FE901467960` | — | — | `unsupported` | 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::cachestat 分派分支，syscall 实现目录中也没有 sys_cachestat 入口。 |

### `capget`

| rule_id | 静态检查 | 动态测试 | 状态 | 原因 |
| --- | --- | --- | --- | --- |
| `LTP_208C833FF12217F5` | `STARRY_CAPGET_ABI` | — | `covered` | sys_capget 校验 Linux V3 capability header，读取目标凭据并向用户态写回两个 capability 数据字，成功返回 0。 |
| `LTP_5F1D35ACCEFD4971` | `STARRY_BATCH_ERRNO_TRANSLATION`、`STARRY_CAPGET_ABI` | — | `covered` | capget 的 V3 header/data 用户指针均通过 VmPtr/VmMutPtr 访问；无效 header 或 data 地址传播 BadAddress，并转换为 EFAULT。 |
| `LTP_827CE5CB448A411B` | `STARRY_BATCH_ERRNO_TRANSLATION`、`STARRY_CAPGET_ABI` | — | `covered` | capget 的 V3 header/data 用户指针均通过 VmPtr/VmMutPtr 访问；无效 header 或 data 地址传播 BadAddress，并转换为 EFAULT。 |
| `LTP_CED2FCC737A99D40` | — | — | `needs_review` | 目标 pid 的存在性和条件表达式选择未完整记录；ESRCH 依赖运行时任务表状态，不能仅凭静态实现确认。 |
| `LTP_DC9BC72148835FDC` | — | — | `needs_review` | 同一条件表达式被上游展开出 EINVAL 与 ESRCH 两种冲突结果，且 header 版本分支未被保真记录，需复核上游分支。 |

### `capset`

| rule_id | 静态检查 | 动态测试 | 状态 | 原因 |
| --- | --- | --- | --- | --- |
| `LTP_461340ED83E7043D` | — | — | `needs_review` | 同一条件表达式被上游过度展开为 EINVAL 或 EPERM，且 BAD_USER_ADDRESS 前置条件与实际选择分支不一致，需复核。 |
| `LTP_6D86AFD541A61388` | `STARRY_BATCH_ERRNO_TRANSLATION`、`STARRY_CAPSET_ABI` | — | `covered` | capset 在修改凭据前通过 VmPtr 读取 V3 header/data；无效 header 或 data 地址传播 BadAddress，并转换为 EFAULT。 |
| `LTP_7DEDC53AC33C891F` | — | — | `needs_review` | 同一条件表达式被上游过度展开为 EINVAL 或 EPERM，且 BAD_USER_ADDRESS 前置条件与实际选择分支不一致，需复核。 |
| `LTP_A00E343F4A556B3D` | — | — | `needs_review` | 旧式测试只保留返回 -1，未保留 errno 与 capability 前置状态，无法映射到唯一静态分支。 |
| `LTP_D1AADFC2F7C6F594` | — | — | `needs_review` | EPERM 取决于调用者 permitted、inheritable、bounding 与 CAP_SETPCAP 运行时状态；规则未完整记录这些前置条件。 |
| `LTP_E06D53042C10C99E` | `STARRY_BATCH_ERRNO_TRANSLATION`、`STARRY_CAPSET_ABI` | — | `covered` | capset 在修改凭据前通过 VmPtr 读取 V3 header/data；无效 header 或 data 地址传播 BadAddress，并转换为 EFAULT。 |
| `LTP_EC23768761E40E9F` | `STARRY_CAPSET_ABI` | — | `covered` | sys_capset 校验 V3 ABI、自身线程与 capability 子集约束，更新当前线程凭据并成功返回 0。 |

### `chroot`

| rule_id | 静态检查 | 动态测试 | 状态 | 原因 |
| --- | --- | --- | --- | --- |
| `LTP_245CD61DAA19DC98` | `STARRY_BATCH_ERRNO_TRANSLATION`、`STARRY_CHROOT_PATH` | — | `covered` | sys_chroot 先读取用户路径，再经 FsContext 解析并要求目标为目录；路径读取或解析错误及 ENOTDIR 由 errno 层保真转换。 |
| `LTP_50F858A3CBF95EED` | — | — | `needs_review` | EPERM 依赖调用者权限状态；当前 sys_chroot 静态入口未显示相应 privilege gate，不能保守标为 covered。 |
| `LTP_71C54C624831C7F0` | `STARRY_BATCH_ERRNO_TRANSLATION`、`STARRY_CHROOT_PATH` | — | `covered` | sys_chroot 先读取用户路径，再经 FsContext 解析并要求目标为目录；路径读取或解析错误及 ENOTDIR 由 errno 层保真转换。 |
| `LTP_99DF5C34778032E1` | `STARRY_BATCH_ERRNO_TRANSLATION`、`STARRY_CHROOT_PATH` | — | `covered` | sys_chroot 先读取用户路径，再经 FsContext 解析并要求目标为目录；路径读取或解析错误及 ENOTDIR 由 errno 层保真转换。 |
| `LTP_D0E32E5D27E643A9` | — | — | `needs_review` | EACCES 依赖目录搜索权限和调用者凭据的运行时组合；规则与静态路径解析证据不足以确认该结果。 |
| `LTP_EBD54180D0CAB16B` | `STARRY_BATCH_ERRNO_TRANSLATION`、`STARRY_CHROOT_PATH` | — | `covered` | sys_chroot 先读取用户路径，再经 FsContext 解析并要求目标为目录；路径读取或解析错误及 ENOTDIR 由 errno 层保真转换。 |
| `LTP_EE7A979F212D6C0C` | `STARRY_CHROOT_PATH` | — | `covered` | sys_chroot 解析目录位置后以该位置创建新的 FsContext，并返回 0，静态覆盖成功路径。 |
| `LTP_FF9C0F9669A39525` | `STARRY_BATCH_ERRNO_TRANSLATION`、`STARRY_CHROOT_PATH` | — | `covered` | sys_chroot 先读取用户路径，再经 FsContext 解析并要求目标为目录；路径读取或解析错误及 ENOTDIR 由 errno 层保真转换。 |

### `close`

| rule_id | 静态检查 | 动态测试 | 状态 | 原因 |
| --- | --- | --- | --- | --- |
| `LTP_09B39E9C9254ECB2` | `STARRY_CLOSE_FD_TABLE`、`STARRY_CLOSE_SYSCALL`、`STARRY_ERRNO_TRANSLATION` | — | `covered` | 相关 Starry 内容指纹未变化，已跳过。 |
| `LTP_0CD17E662AFD2956` | `STARRY_CLOSE_FD_TABLE`、`STARRY_CLOSE_SYSCALL`、`STARRY_ERRNO_TRANSLATION` | — | `covered` | 相关 Starry 内容指纹未变化，已跳过。 |
| `LTP_5CB803B873F78BA0` | `STARRY_CLOSE_FD_TABLE`、`STARRY_CLOSE_SYSCALL` | — | `covered` | 相关 Starry 内容指纹未变化，已跳过。 |

### `mmap`

| rule_id | 静态检查 | 动态测试 | 状态 | 原因 |
| --- | --- | --- | --- | --- |
| `LTP_36C99C10CD38F8DB` | `STARRY_ERRNO_TRANSLATION`、`STARRY_MMAP_ACCESS` | — | `covered` | 相关 Starry 内容指纹未变化，已跳过。 |
| `LTP_45439D8F2BAB0832` | `STARRY_ERRNO_TRANSLATION`、`STARRY_MMAP_ACCESS` | — | `covered` | 相关 Starry 内容指纹未变化，已跳过。 |
| `LTP_51E295101A9F4411` | `STARRY_ERRNO_TRANSLATION`、`STARRY_MMAP_ARGUMENTS` | — | `covered` | 相关 Starry 内容指纹未变化，已跳过。 |
| `LTP_52BAFC01DEA6E172` | `STARRY_ERRNO_TRANSLATION`、`STARRY_MMAP_ACCESS` | — | `covered` | 相关 Starry 内容指纹未变化，已跳过。 |
| `LTP_791DEA825D66980B` | `STARRY_ERRNO_TRANSLATION`、`STARRY_MMAP_FD` | — | `covered` | 相关 Starry 内容指纹未变化，已跳过。 |
| `LTP_C346EFF1233F7061` | `STARRY_ERRNO_TRANSLATION`、`STARRY_MMAP_ACCESS` | — | `covered` | 相关 Starry 内容指纹未变化，已跳过。 |
| `LTP_F36F8C0CC1A6D840` | `STARRY_ERRNO_TRANSLATION`、`STARRY_MMAP_ACCESS` | — | `covered` | 相关 Starry 内容指纹未变化，已跳过。 |
| `LTP_FD1B65B0BCC88E0D` | `STARRY_ERRNO_TRANSLATION`、`STARRY_MMAP_ACCESS` | — | `covered` | 相关 Starry 内容指纹未变化，已跳过。 |
| `LTP_FEACDC300C3E1DD7` | `STARRY_ERRNO_TRANSLATION`、`STARRY_MMAP_ARGUMENTS` | — | `covered` | 相关 Starry 内容指纹未变化，已跳过。 |

<details>
<summary>机器可读元数据</summary>

<!-- syscallguard-metadata -->
```yaml
schema_version: 1
kind: syscallguard_mapping_report
report_id: mapping-20260715t035919z-aa4629b5
status: completed
generated_at_utc: '2026-07-15T04:13:20.108411Z'
rule_index_hash: sha256:26e37571153d06519bd25fbdf3ea473082b40e529747c843f89bf6487ec6fb70
requested_syscalls: null
selected_rule_ids:
- LTP_00F2A9EA8833DA1D
- LTP_0180982614AA9F7D
- LTP_0290063892A53510
- LTP_030858A5FFCCEFF4
- LTP_035E62E6D1787773
- LTP_036EDA2B8D36CF03
- LTP_037E6F334D0E0D16
- LTP_0431E3529AA0FEE8
- LTP_044E7C11E6B503BB
- LTP_060B6037DEF1D43C
- LTP_06725D44DFF06F7E
- LTP_06891E2E299CF48E
- LTP_06A0C295D8E7FAFA
- LTP_06AC9297E35AAE7A
- LTP_075318C437B76E06
- LTP_0799FC60BADD2B18
- LTP_0A62800536904C02
- LTP_0AAFA34BA77A0D25
- LTP_0B45FC33068D334C
- LTP_0BB235F712E819CE
- LTP_0D1782EAAC26DEB4
- LTP_0E9AF2C058AF8126
- LTP_0F901C62092CC7B8
- LTP_10A684C1C2D2DE0F
- LTP_10FE1313FBAB5F92
- LTP_1325C077A1CDE514
- LTP_1402459B5FF9BF23
- LTP_1465554B09CE14F0
- LTP_148623FDAF4E478D
- LTP_153B296FA599E0CE
- LTP_17ACF3BE969B64EE
- LTP_17CB4ED7A76BD283
- LTP_1870C0046E9555AF
- LTP_18A450CE49F8867B
- LTP_198D9555A8BED013
- LTP_1A9481FAD460FBF7
- LTP_1BD36AE285B4F3E2
- LTP_1C462AC54A29FF35
- LTP_1CDCF5FE9ED1BE5D
- LTP_1D39F97D759F0E57
- LTP_1DF2B28499E4D7B3
- LTP_208C833FF12217F5
- LTP_212269CECE600FD8
- LTP_21A007DF738F1E73
- LTP_21C4957F9EFE94D3
- LTP_220D1227D307AD3C
- LTP_2221F954D01EB2BB
- LTP_245CD61DAA19DC98
- LTP_25639C9C5750C487
- LTP_26AC646B9D18C353
- LTP_277FD467E5F1BF1C
- LTP_27C7E91095DB9DF8
- LTP_2900BC64740A3E44
- LTP_298AB67F0CFA519C
- LTP_2B4171DD8FBD982A
- LTP_2D0BAECAE4F61432
- LTP_2E5D530A61E60934
- LTP_2F99FA84C445363C
- LTP_2FA43CD942AE7AD6
- LTP_2FE8FAD800DE41F6
- LTP_3472CD1A0F8A2B4A
- LTP_347761CBCF52D194
- LTP_34CFEAD03DB6A3CA
- LTP_34EC9FB9C9551214
- LTP_35CAEE10A613E109
- LTP_3636C4768C196B52
- LTP_368D8689810796B2
- LTP_38FB918826669241
- LTP_3900F4E562AE09D1
- LTP_3916A669595B3568
- LTP_3AD3865603ADDC8E
- LTP_3C2853617B38EEE7
- LTP_3D4ECD22BC433164
- LTP_3D8D38C9123CD051
- LTP_3DE23AB4FE2FFC67
- LTP_3E526A0A23B5EF6D
- LTP_3E8DA9E014B82702
- LTP_3F81436312777EF4
- LTP_401D471D37C85820
- LTP_461340ED83E7043D
- LTP_4661BBF1B3CD3A1E
- LTP_46DE8D9AD1674F26
- LTP_472AAA35C7382B26
- LTP_479924116854D92B
- LTP_48753F73ACA755FB
- LTP_4881657CFE57C7E9
- LTP_492D25A0F1055F72
- LTP_4948E12FB8F9FA49
- LTP_49700CDA955B66D8
- LTP_49A36559B96D24AF
- LTP_4B6E9B98E2E5103D
- LTP_4CFAFCE7FCA2BF99
- LTP_4ECB786BFA071AAC
- LTP_50A86D4D5411356E
- LTP_50F858A3CBF95EED
- LTP_52C209105EE62171
- LTP_5570480E7920BD0E
- LTP_563FB650864E0DC6
- LTP_58416E6747519699
- LTP_58F1512157A0052D
- LTP_5A315335586D4227
- LTP_5C5CDC165410C08C
- LTP_5CC44E5D1A6B6485
- LTP_5D7971086B2ABAE5
- LTP_5EC31E34822684C4
- LTP_5F1D35ACCEFD4971
- LTP_606B7E40B6BD82EA
- LTP_613A5E121B4B6E68
- LTP_6156A09A2E506F76
- LTP_6169F41023E00C34
- LTP_636590E5A017B28D
- LTP_64227C746913D03D
- LTP_6449E4A1D20C01D3
- LTP_64A4E5DC71A633A2
- LTP_65281FBEE0BF6103
- LTP_6580B4D3FA1A86F3
- LTP_65B70356F06E31F8
- LTP_679436EC7A4E218A
- LTP_67BF94A4ACD303C4
- LTP_68745D21F4EC2FF5
- LTP_68E1B26815D97B79
- LTP_69077B093E81B570
- LTP_690A651C3A60FC1E
- LTP_69E094D1DBFF3796
- LTP_6A1A431A08A3F450
- LTP_6B1746F6BB2266CA
- LTP_6B8B5453E8B4E6DE
- LTP_6C11BBB4AABA6E7C
- LTP_6C55A3E760DF75DB
- LTP_6CE9FC3BCA164B5D
- LTP_6D584CE6CF9B8A06
- LTP_6D86AFD541A61388
- LTP_6EF7ECD2A8470CEA
- LTP_711D5693356A79F2
- LTP_71C54C624831C7F0
- LTP_73DF50509BCC128B
- LTP_74819A9DC2B5CB06
- LTP_752C9A802CF96B8B
- LTP_76A9B6CF388A8609
- LTP_78EEEBE648781151
- LTP_7963C3DF373596FE
- LTP_79C7516DECB19092
- LTP_7A02B34D5FB8BBC3
- LTP_7A74A699442CEB99
- LTP_7B539E14354153DC
- LTP_7BE2877017694C52
- LTP_7C06A3394E786948
- LTP_7CE7876CE69F200F
- LTP_7DD493976CBC9A31
- LTP_7DEDC53AC33C891F
- LTP_7F5487EEB79017AD
- LTP_7F54F9DFF7E0FB61
- LTP_7FD6142E0E88CF17
- LTP_8059D9227293D592
- LTP_807E2072E5694684
- LTP_80C6DB0ACB2A5510
- LTP_818BA624CA9E4040
- LTP_820495EA1D1F15DA
- LTP_82621B02FCA09F40
- LTP_827CE5CB448A411B
- LTP_82ABB8FBFA06D356
- LTP_82E0F55AEC3D382F
- LTP_830E17210B1FB7AB
- LTP_833C5D5CF3C32C2A
- LTP_839EC7BC904E42D5
- LTP_843BDD20FF921FC3
- LTP_84E4CC971DD16EC2
- LTP_853D34D061DDE8F8
- LTP_853F4B8346648EB9
- LTP_857DC6AD01A88D79
- LTP_87478A6C3AC7DC60
- LTP_884775F9076E54AB
- LTP_885F3BA721198C07
- LTP_88F6F279E33633DE
- LTP_89C9E8458EC38C11
- LTP_8AC11633EA3D83E0
- LTP_8AD8032754BC8842
- LTP_8B1A2084BCF096F1
- LTP_8B3FBDFD0453EF40
- LTP_8BB576EB2E1E6B23
- LTP_8C508A50371B6444
- LTP_8CB51F0A9F8FDEA1
- LTP_8D3BFFA98E2561BA
- LTP_8D54825D4B298C7C
- LTP_8E7F1BE3D7D7823B
- LTP_8F29388433422812
- LTP_8FF73194288F8473
- LTP_906135780505447D
- LTP_911B97B972658989
- LTP_919ABCA2598F53B5
- LTP_921D4802D7690C64
- LTP_9260E923CF8AA018
- LTP_929B120944D8F805
- LTP_93949494FBAD3568
- LTP_94E36E221125BFAF
- LTP_955ECE70D81CA226
- LTP_96021AFB69E847F9
- LTP_969C39F409BFD7AA
- LTP_96D205FACA0DD8DB
- LTP_96F07DC5DDC8E018
- LTP_97C442AC56780374
- LTP_9866FB6F1F726CA0
- LTP_986F211E7D45CAD7
- LTP_98EC66149EE68933
- LTP_99DF5C34778032E1
- LTP_9A723EA0B1F0D1BE
- LTP_9C9D222A34799D55
- LTP_9CA9C6B61C3317A3
- LTP_9CDCD3C4BA6C2702
- LTP_A00E343F4A556B3D
- LTP_A17272D4FE0F040B
- LTP_A1DEE046C0A10B18
- LTP_A30F7687D403407B
- LTP_A4060315D2E047EE
- LTP_A4733D4B2FEBE9A4
- LTP_A500A46C4B998E74
- LTP_A6B94E8A2A4D8853
- LTP_A9544B59EB6712D9
- LTP_A9596E932167B3EF
- LTP_AB48F262BBB2CC93
- LTP_AC0FB73B4EE420EC
- LTP_AD81218450587FA8
- LTP_ADD30BEEC40E661F
- LTP_B1D822DF0057B4E0
- LTP_B200AFD97E91C2CC
- LTP_B53406D510ED4981
- LTP_B6DAF13EF3143EBF
- LTP_B7A341967DF2BD69
- LTP_B90CB73F36B70C6F
- LTP_B9908D4015443661
- LTP_B9CDD41A0DC2AFCC
- LTP_BA10984A4B0DE2C6
- LTP_BA9A8FE901467960
- LTP_BC662075E3BAE807
- LTP_BE2E778739EF01D5
- LTP_C0577C0D678214DA
- LTP_C071A7FFF929A2A5
- LTP_C0AA45BC29F98A0E
- LTP_C1C67435FC56D878
- LTP_C218D3CB0AD80D90
- LTP_C5FE18F9550B31BA
- LTP_C6A719982BDE9CE4
- LTP_C6E67CB1FD2B1F64
- LTP_C785774773FB7524
- LTP_C7B73F4D5B87736A
- LTP_C80C019BE3F47901
- LTP_C8DAE34819E335F8
- LTP_C994B56A41A71C1A
- LTP_CA45A33676AD236D
- LTP_CA80C3F10B65226D
- LTP_CB31E19EE807FFDB
- LTP_CCDB1776DAA2C318
- LTP_CD2150BE4FE81F31
- LTP_CDCDC1B9E63D58C3
- LTP_CE45382D3DE75F8F
- LTP_CEBAD6AB3C82795E
- LTP_CED2FCC737A99D40
- LTP_D0E32E5D27E643A9
- LTP_D1AADFC2F7C6F594
- LTP_D1B6112551D45B31
- LTP_D1F469715ECC4195
- LTP_D2D67AB5E38A7000
- LTP_D2F4BCF2263C56F5
- LTP_D412A09DEDC43045
- LTP_D4B433A3696803A8
- LTP_D4D8A0FEAA2F6B09
- LTP_D579FCFC71E6EB6A
- LTP_D653D15777B77A1F
- LTP_D6A52FD61BF01578
- LTP_D72526C4E4301D60
- LTP_D76652434EC85091
- LTP_D8B58CA743EBE711
- LTP_DA10E351BC730D85
- LTP_DAA03BAD070DB1D6
- LTP_DAA1F16D8A298E83
- LTP_DC9BC72148835FDC
- LTP_DCB33BB29D296843
- LTP_DD9A41090E3D5A17
- LTP_DF1C4714B16B760E
- LTP_E06D53042C10C99E
- LTP_E0B177A8B6FE4225
- LTP_E0ED96B80FC3B6C9
- LTP_E13B9C2C9645B841
- LTP_E28B5BB57A450438
- LTP_E2C3B68EDF07A753
- LTP_E34945E3DE91022F
- LTP_E3A3CF8B98E460BC
- LTP_E3E59B16A96A60BC
- LTP_E41DD7230DA067DD
- LTP_E46539F2D47BA5EC
- LTP_E4D1B76D80905462
- LTP_E560C027210BF20A
- LTP_E5791B389C67677E
- LTP_E5E50FB7BDD033D9
- LTP_EB00EA74B30E438E
- LTP_EB425D988F2F7604
- LTP_EBD54180D0CAB16B
- LTP_EBF0020C32AD44C8
- LTP_EC19C6410BBE0467
- LTP_EC23768761E40E9F
- LTP_ED36488372A175F5
- LTP_ED3F2AE7E59E6F12
- LTP_EE1518958A8F7CC1
- LTP_EE7A979F212D6C0C
- LTP_EF5C1F365208AD31
- LTP_F1044C71B6626419
- LTP_F202F3C3B02DEA0E
- LTP_F3200B697F38DD16
- LTP_F3418C5C403B91FC
- LTP_F43EC0D01CCFD25A
- LTP_F6BB86F5DCC2FAC8
- LTP_F70FC66A56FBD769
- LTP_F7998813C90A7A08
- LTP_F8CDD57D76C8FA6C
- LTP_F9BF08369A08E5ED
- LTP_FC5B16AB3C53A744
- LTP_FCA376B46A9873B0
- LTP_FF9C0F9669A39525
skipped_rule_ids:
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
target:
  target_id: starry
  repository: /home/cloud/gitLinux/tgoskits
  repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
  revision: HEAD
  worktree_root: /tmp/syscallguard-worktrees
  descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
  snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
counts:
  rules_total: 330
  processed: 318
  added: 318
  updated: 0
  skipped: 12
  covered: 42
  pending: 0
  needs_review: 265
  unsupported: 23
  static_checks: 8
  dynamic_tests: 0
  remaining: 288
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
  LTP_00F2A9EA8833DA1D: &id001
  - cachestat
  LTP_0180982614AA9F7D: &id002
  - access
  LTP_0290063892A53510: &id003
  - access
  LTP_030858A5FFCCEFF4: &id004
  - access
  LTP_035E62E6D1787773: &id005
  - access
  LTP_036EDA2B8D36CF03: &id006
  - access
  LTP_037E6F334D0E0D16: &id007
  - access
  LTP_0431E3529AA0FEE8: &id008
  - access
  LTP_044E7C11E6B503BB: &id009
  - access
  LTP_060B6037DEF1D43C: &id010
  - access
  LTP_06725D44DFF06F7E: &id011
  - access
  LTP_06891E2E299CF48E: &id012
  - access
  LTP_06A0C295D8E7FAFA: &id013
  - access
  LTP_06AC9297E35AAE7A: &id014
  - access
  LTP_075318C437B76E06: &id015
  - access
  LTP_0799FC60BADD2B18: &id016
  - access
  LTP_09B39E9C9254ECB2: &id017
  - close
  LTP_0A62800536904C02: &id018
  - access
  LTP_0AAFA34BA77A0D25: &id019
  - access
  LTP_0B45FC33068D334C: &id020
  - access
  LTP_0BB235F712E819CE: &id021
  - access
  LTP_0CD17E662AFD2956: &id022
  - close
  LTP_0D1782EAAC26DEB4: &id023
  - access
  LTP_0E9AF2C058AF8126: &id024
  - access
  LTP_0F901C62092CC7B8: &id025
  - access
  LTP_10A684C1C2D2DE0F: &id026
  - access
  LTP_10FE1313FBAB5F92: &id027
  - access
  LTP_1325C077A1CDE514: &id028
  - cachestat
  LTP_1402459B5FF9BF23: &id029
  - access
  LTP_1465554B09CE14F0: &id030
  - access
  LTP_148623FDAF4E478D: &id031
  - access
  LTP_153B296FA599E0CE: &id032
  - access
  LTP_17ACF3BE969B64EE: &id033
  - access
  LTP_17CB4ED7A76BD283: &id034
  - access
  LTP_1870C0046E9555AF: &id035
  - access
  LTP_18A450CE49F8867B: &id036
  - access
  LTP_198D9555A8BED013: &id037
  - access
  LTP_1A9481FAD460FBF7: &id038
  - alarm
  LTP_1BD36AE285B4F3E2: &id039
  - access
  LTP_1C462AC54A29FF35: &id040
  - access
  LTP_1CDCF5FE9ED1BE5D: &id041
  - access
  LTP_1D39F97D759F0E57: &id042
  - access
  LTP_1DF2B28499E4D7B3: &id043
  - access
  LTP_208C833FF12217F5: &id044
  - capget
  LTP_212269CECE600FD8: &id045
  - access
  LTP_21A007DF738F1E73: &id046
  - access
  LTP_21C4957F9EFE94D3: &id047
  - access
  LTP_220D1227D307AD3C: &id048
  - access
  LTP_2221F954D01EB2BB: &id049
  - access
  LTP_245CD61DAA19DC98: &id050
  - chroot
  LTP_25639C9C5750C487: &id051
  - access
  LTP_26AC646B9D18C353: &id052
  - access
  LTP_277FD467E5F1BF1C: &id053
  - accept
  LTP_27C7E91095DB9DF8: &id054
  - access
  LTP_2900BC64740A3E44: &id055
  - access
  LTP_298AB67F0CFA519C: &id056
  - access
  LTP_2B4171DD8FBD982A: &id057
  - access
  LTP_2D0BAECAE4F61432: &id058
  - access
  LTP_2E5D530A61E60934: &id059
  - access
  LTP_2F99FA84C445363C: &id060
  - access
  LTP_2FA43CD942AE7AD6: &id061
  - access
  LTP_2FE8FAD800DE41F6: &id062
  - access
  LTP_3472CD1A0F8A2B4A: &id063
  - access
  LTP_347761CBCF52D194: &id064
  - access
  LTP_34CFEAD03DB6A3CA: &id065
  - access
  LTP_34EC9FB9C9551214: &id066
  - cachestat
  LTP_35CAEE10A613E109: &id067
  - access
  LTP_3636C4768C196B52: &id068
  - access
  LTP_368D8689810796B2: &id069
  - access
  LTP_36C99C10CD38F8DB: &id070
  - mmap
  LTP_38FB918826669241: &id071
  - access
  LTP_3900F4E562AE09D1: &id072
  - access
  LTP_3916A669595B3568: &id073
  - access
  LTP_3AD3865603ADDC8E: &id074
  - access
  LTP_3C2853617B38EEE7: &id075
  - access
  LTP_3D4ECD22BC433164: &id076
  - access
  LTP_3D8D38C9123CD051: &id077
  - access
  LTP_3DE23AB4FE2FFC67: &id078
  - access
  LTP_3E526A0A23B5EF6D: &id079
  - access
  LTP_3E8DA9E014B82702: &id080
  - alarm
  LTP_3F81436312777EF4: &id081
  - access
  LTP_401D471D37C85820: &id082
  - access
  LTP_45439D8F2BAB0832: &id083
  - mmap
  LTP_461340ED83E7043D: &id084
  - capset
  LTP_4661BBF1B3CD3A1E: &id085
  - access
  LTP_46DE8D9AD1674F26: &id086
  - access
  LTP_472AAA35C7382B26: &id087
  - accept
  LTP_479924116854D92B: &id088
  - access
  LTP_48753F73ACA755FB: &id089
  - access
  LTP_4881657CFE57C7E9: &id090
  - access
  LTP_492D25A0F1055F72: &id091
  - access
  LTP_4948E12FB8F9FA49: &id092
  - access
  LTP_49700CDA955B66D8: &id093
  - access
  LTP_49A36559B96D24AF: &id094
  - access
  LTP_4B6E9B98E2E5103D: &id095
  - access
  LTP_4CFAFCE7FCA2BF99: &id096
  - access
  LTP_4ECB786BFA071AAC: &id097
  - access
  LTP_50A86D4D5411356E: &id098
  - access
  LTP_50F858A3CBF95EED: &id099
  - chroot
  LTP_51E295101A9F4411: &id100
  - mmap
  LTP_52BAFC01DEA6E172: &id101
  - mmap
  LTP_52C209105EE62171: &id102
  - access
  LTP_5570480E7920BD0E: &id103
  - access
  LTP_563FB650864E0DC6: &id104
  - access
  LTP_58416E6747519699: &id105
  - access
  LTP_58F1512157A0052D: &id106
  - access
  LTP_5A315335586D4227: &id107
  - access
  LTP_5C5CDC165410C08C: &id108
  - access
  LTP_5CB803B873F78BA0: &id109
  - close
  LTP_5CC44E5D1A6B6485: &id110
  - access
  LTP_5D7971086B2ABAE5: &id111
  - access
  LTP_5EC31E34822684C4: &id112
  - access
  LTP_5F1D35ACCEFD4971: &id113
  - capget
  LTP_606B7E40B6BD82EA: &id114
  - access
  LTP_613A5E121B4B6E68: &id115
  - access
  LTP_6156A09A2E506F76: &id116
  - access
  LTP_6169F41023E00C34: &id117
  - access
  LTP_636590E5A017B28D: &id118
  - access
  LTP_64227C746913D03D: &id119
  - access
  LTP_6449E4A1D20C01D3: &id120
  - alarm
  LTP_64A4E5DC71A633A2: &id121
  - access
  LTP_65281FBEE0BF6103: &id122
  - access
  LTP_6580B4D3FA1A86F3: &id123
  - access
  LTP_65B70356F06E31F8: &id124
  - alarm
  LTP_679436EC7A4E218A: &id125
  - access
  LTP_67BF94A4ACD303C4: &id126
  - access
  LTP_68745D21F4EC2FF5: &id127
  - access
  LTP_68E1B26815D97B79: &id128
  - access
  LTP_69077B093E81B570: &id129
  - access
  LTP_690A651C3A60FC1E: &id130
  - access
  LTP_69E094D1DBFF3796: &id131
  - access
  LTP_6A1A431A08A3F450: &id132
  - access
  LTP_6B1746F6BB2266CA: &id133
  - access
  LTP_6B8B5453E8B4E6DE: &id134
  - access
  LTP_6C11BBB4AABA6E7C: &id135
  - access
  LTP_6C55A3E760DF75DB: &id136
  - access
  LTP_6CE9FC3BCA164B5D: &id137
  - access
  LTP_6D584CE6CF9B8A06: &id138
  - access
  LTP_6D86AFD541A61388: &id139
  - capset
  LTP_6EF7ECD2A8470CEA: &id140
  - access
  LTP_711D5693356A79F2: &id141
  - access
  LTP_71C54C624831C7F0: &id142
  - chroot
  LTP_73DF50509BCC128B: &id143
  - access
  LTP_74819A9DC2B5CB06: &id144
  - access
  LTP_752C9A802CF96B8B: &id145
  - access
  LTP_76A9B6CF388A8609: &id146
  - alarm
  LTP_78EEEBE648781151: &id147
  - access
  LTP_791DEA825D66980B: &id148
  - mmap
  LTP_7963C3DF373596FE: &id149
  - access
  LTP_79C7516DECB19092: &id150
  - access
  LTP_7A02B34D5FB8BBC3: &id151
  - access
  LTP_7A74A699442CEB99: &id152
  - brk
  LTP_7B539E14354153DC: &id153
  - access
  LTP_7BE2877017694C52: &id154
  - access
  LTP_7C06A3394E786948: &id155
  - access
  LTP_7CE7876CE69F200F: &id156
  - access
  LTP_7DD493976CBC9A31: &id157
  - access
  LTP_7DEDC53AC33C891F: &id158
  - capset
  LTP_7F5487EEB79017AD: &id159
  - access
  LTP_7F54F9DFF7E0FB61: &id160
  - access
  LTP_7FD6142E0E88CF17: &id161
  - cachestat
  LTP_8059D9227293D592: &id162
  - access
  LTP_807E2072E5694684: &id163
  - access
  LTP_80C6DB0ACB2A5510: &id164
  - accept
  LTP_818BA624CA9E4040: &id165
  - access
  LTP_820495EA1D1F15DA: &id166
  - access
  LTP_82621B02FCA09F40: &id167
  - alarm
  LTP_827CE5CB448A411B: &id168
  - capget
  LTP_82ABB8FBFA06D356: &id169
  - access
  LTP_82E0F55AEC3D382F: &id170
  - access
  LTP_830E17210B1FB7AB: &id171
  - access
  LTP_833C5D5CF3C32C2A: &id172
  - access
  LTP_839EC7BC904E42D5: &id173
  - access
  LTP_843BDD20FF921FC3: &id174
  - access
  LTP_84E4CC971DD16EC2: &id175
  - access
  LTP_853D34D061DDE8F8: &id176
  - access
  LTP_853F4B8346648EB9: &id177
  - access
  LTP_857DC6AD01A88D79: &id178
  - access
  LTP_87478A6C3AC7DC60: &id179
  - access
  LTP_884775F9076E54AB: &id180
  - access
  LTP_885F3BA721198C07: &id181
  - access
  LTP_88F6F279E33633DE: &id182
  - access
  LTP_89C9E8458EC38C11: &id183
  - cachestat
  LTP_8AC11633EA3D83E0: &id184
  - access
  LTP_8AD8032754BC8842: &id185
  - cacheflush
  LTP_8B1A2084BCF096F1: &id186
  - access
  LTP_8B3FBDFD0453EF40: &id187
  - access
  LTP_8BB576EB2E1E6B23: &id188
  - access
  LTP_8C508A50371B6444: &id189
  - access
  LTP_8CB51F0A9F8FDEA1: &id190
  - access
  LTP_8D3BFFA98E2561BA: &id191
  - access
  LTP_8D54825D4B298C7C: &id192
  - access
  LTP_8E7F1BE3D7D7823B: &id193
  - access
  LTP_8F29388433422812: &id194
  - access
  LTP_8FF73194288F8473: &id195
  - access
  LTP_906135780505447D: &id196
  - access
  LTP_911B97B972658989: &id197
  - access
  LTP_919ABCA2598F53B5: &id198
  - access
  LTP_921D4802D7690C64: &id199
  - access
  LTP_9260E923CF8AA018: &id200
  - access
  LTP_929B120944D8F805: &id201
  - access
  LTP_93949494FBAD3568: &id202
  - access
  LTP_94E36E221125BFAF: &id203
  - access
  LTP_955ECE70D81CA226: &id204
  - access
  LTP_96021AFB69E847F9: &id205
  - access
  LTP_969C39F409BFD7AA: &id206
  - access
  LTP_96D205FACA0DD8DB: &id207
  - access
  LTP_96F07DC5DDC8E018: &id208
  - access
  LTP_97C442AC56780374: &id209
  - access
  LTP_9866FB6F1F726CA0: &id210
  - access
  LTP_986F211E7D45CAD7: &id211
  - access
  LTP_98EC66149EE68933: &id212
  - alarm
  LTP_99DF5C34778032E1: &id213
  - chroot
  LTP_9A723EA0B1F0D1BE: &id214
  - access
  LTP_9C9D222A34799D55: &id215
  - access
  LTP_9CA9C6B61C3317A3: &id216
  - accept
  LTP_9CDCD3C4BA6C2702: &id217
  - access
  LTP_A00E343F4A556B3D: &id218
  - capset
  LTP_A17272D4FE0F040B: &id219
  - access
  LTP_A1DEE046C0A10B18: &id220
  - access
  LTP_A30F7687D403407B: &id221
  - access
  LTP_A4060315D2E047EE: &id222
  - access
  LTP_A4733D4B2FEBE9A4: &id223
  - access
  LTP_A500A46C4B998E74: &id224
  - access
  LTP_A6B94E8A2A4D8853: &id225
  - access
  LTP_A9544B59EB6712D9: &id226
  - access
  LTP_A9596E932167B3EF: &id227
  - access
  LTP_AB48F262BBB2CC93: &id228
  - access
  LTP_AC0FB73B4EE420EC: &id229
  - access
  LTP_AD81218450587FA8: &id230
  - access
  LTP_ADD30BEEC40E661F: &id231
  - access
  LTP_B1D822DF0057B4E0: &id232
  - access
  LTP_B200AFD97E91C2CC: &id233
  - access
  LTP_B53406D510ED4981: &id234
  - access
  LTP_B6DAF13EF3143EBF: &id235
  - access
  LTP_B7A341967DF2BD69: &id236
  - alarm
  LTP_B90CB73F36B70C6F: &id237
  - accept
  LTP_B9908D4015443661: &id238
  - access
  LTP_B9CDD41A0DC2AFCC: &id239
  - access
  LTP_BA10984A4B0DE2C6: &id240
  - access
  LTP_BA9A8FE901467960: &id241
  - cachestat
  LTP_BC662075E3BAE807: &id242
  - access
  LTP_BE2E778739EF01D5: &id243
  - access
  LTP_C0577C0D678214DA: &id244
  - access
  LTP_C071A7FFF929A2A5: &id245
  - access
  LTP_C0AA45BC29F98A0E: &id246
  - access
  LTP_C1C67435FC56D878: &id247
  - access
  LTP_C218D3CB0AD80D90: &id248
  - cacheflush
  LTP_C346EFF1233F7061: &id249
  - mmap
  LTP_C5FE18F9550B31BA: &id250
  - access
  LTP_C6A719982BDE9CE4: &id251
  - access
  LTP_C6E67CB1FD2B1F64: &id252
  - access
  LTP_C785774773FB7524: &id253
  - alarm
  LTP_C7B73F4D5B87736A: &id254
  - alarm
  LTP_C80C019BE3F47901: &id255
  - alarm
  LTP_C8DAE34819E335F8: &id256
  - access
  LTP_C994B56A41A71C1A: &id257
  - access
  LTP_CA45A33676AD236D: &id258
  - access
  LTP_CA80C3F10B65226D: &id259
  - access
  LTP_CB31E19EE807FFDB: &id260
  - access
  LTP_CCDB1776DAA2C318: &id261
  - access
  LTP_CD2150BE4FE81F31: &id262
  - alarm
  LTP_CDCDC1B9E63D58C3: &id263
  - access
  LTP_CE45382D3DE75F8F: &id264
  - access
  LTP_CEBAD6AB3C82795E: &id265
  - access
  LTP_CED2FCC737A99D40: &id266
  - capget
  LTP_D0E32E5D27E643A9: &id267
  - chroot
  LTP_D1AADFC2F7C6F594: &id268
  - capset
  LTP_D1B6112551D45B31: &id269
  - alarm
  LTP_D1F469715ECC4195: &id270
  - access
  LTP_D2D67AB5E38A7000: &id271
  - access
  LTP_D2F4BCF2263C56F5: &id272
  - access
  LTP_D412A09DEDC43045: &id273
  - access
  LTP_D4B433A3696803A8: &id274
  - alarm
  LTP_D4D8A0FEAA2F6B09: &id275
  - access
  LTP_D579FCFC71E6EB6A: &id276
  - cacheflush
  LTP_D653D15777B77A1F: &id277
  - access
  LTP_D6A52FD61BF01578: &id278
  - access
  LTP_D72526C4E4301D60: &id279
  - access
  LTP_D76652434EC85091: &id280
  - access
  LTP_D8B58CA743EBE711: &id281
  - access
  LTP_DA10E351BC730D85: &id282
  - access
  LTP_DAA03BAD070DB1D6: &id283
  - access
  LTP_DAA1F16D8A298E83: &id284
  - access
  LTP_DC9BC72148835FDC: &id285
  - capget
  LTP_DCB33BB29D296843: &id286
  - access
  LTP_DD9A41090E3D5A17: &id287
  - access
  LTP_DF1C4714B16B760E: &id288
  - access
  LTP_E06D53042C10C99E: &id289
  - capset
  LTP_E0B177A8B6FE4225: &id290
  - access
  LTP_E0ED96B80FC3B6C9: &id291
  - access
  LTP_E13B9C2C9645B841: &id292
  - accept
  LTP_E28B5BB57A450438: &id293
  - access
  LTP_E2C3B68EDF07A753: &id294
  - access
  LTP_E34945E3DE91022F: &id295
  - access
  LTP_E3A3CF8B98E460BC: &id296
  - access
  LTP_E3E59B16A96A60BC: &id297
  - brk
  LTP_E41DD7230DA067DD: &id298
  - access
  LTP_E46539F2D47BA5EC: &id299
  - access
  LTP_E4D1B76D80905462: &id300
  - access
  LTP_E560C027210BF20A: &id301
  - access
  LTP_E5791B389C67677E: &id302
  - access
  LTP_E5E50FB7BDD033D9: &id303
  - access
  LTP_EB00EA74B30E438E: &id304
  - access
  LTP_EB425D988F2F7604: &id305
  - access
  LTP_EBD54180D0CAB16B: &id306
  - chroot
  LTP_EBF0020C32AD44C8: &id307
  - access
  LTP_EC19C6410BBE0467: &id308
  - access
  LTP_EC23768761E40E9F: &id309
  - capset
  LTP_ED36488372A175F5: &id310
  - access
  LTP_ED3F2AE7E59E6F12: &id311
  - access
  LTP_EE1518958A8F7CC1: &id312
  - access
  LTP_EE7A979F212D6C0C: &id313
  - chroot
  LTP_EF5C1F365208AD31: &id314
  - access
  LTP_F1044C71B6626419: &id315
  - accept
  LTP_F202F3C3B02DEA0E: &id316
  - access
  LTP_F3200B697F38DD16: &id317
  - access
  LTP_F3418C5C403B91FC: &id318
  - access
  LTP_F36F8C0CC1A6D840: &id319
  - mmap
  LTP_F43EC0D01CCFD25A: &id320
  - access
  LTP_F6BB86F5DCC2FAC8: &id321
  - access
  LTP_F70FC66A56FBD769: &id322
  - access
  LTP_F7998813C90A7A08: &id323
  - access
  LTP_F8CDD57D76C8FA6C: &id324
  - access
  LTP_F9BF08369A08E5ED: &id325
  - access
  LTP_FC5B16AB3C53A744: &id326
  - access
  LTP_FCA376B46A9873B0: &id327
  - access
  LTP_FD1B65B0BCC88E0D: &id328
  - mmap
  LTP_FEACDC300C3E1DD7: &id329
  - mmap
  LTP_FF9C0F9669A39525: &id330
  - chroot
rules:
  LTP_00F2A9EA8833DA1D:
    syscalls: *id001
    rule_version:
      id: LTP_00F2A9EA8833DA1D
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:00f2a9ea8833da1da8949ee468fb47004f99f1116ae6cda9ea3ba127e264058a
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::cachestat 分派分支，syscall 实现目录中也没有
      sys_cachestat 入口。
  LTP_0180982614AA9F7D:
    syscalls: *id002
    rule_version: &id331
      id: LTP_0180982614AA9F7D
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:0180982614aa9f7deb01d61e1891fc76f80a5dd2c63dd0b04340bb29d02ed2a5
    status: covered
    static_check_refs:
    - STARRY_ACCESS_PERMISSIONS
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ACCESS_PERMISSIONS:
          id: STARRY_ACCESS_PERMISSIONS
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:9a2f8a7c6a97cb3e0bb0faa21d342b618172c583039ca74535fe0f394fa364bd
      dynamic_tests: {}
    target_dependencies:
    - path: os/StarryOS/kernel/src/file/fs.rs
      symbols:
      - resolve_at
      scope: symbols
      file_hash: sha256:550e894d6abfbc7221d14420c4a3b9ed85ff072e792e108c2f8b7f8a6dceeefd
      symbol_hashes:
        resolve_at: sha256:ec9e7f57add9a1db10191664fd7c77c9236ea7f33e3df9b43ce8fd66ddc0a01f
      missing_symbols: []
      content_hash: sha256:b3dce20309fe9f480c0da78b10b6995550acae12ab1f7f9f348ac78ca0cebbe2
    - path: os/StarryOS/kernel/src/syscall/fs/stat.rs
      symbols:
      - sys_access
      - sys_faccessat2
      scope: symbols
      file_hash: sha256:8c2b95c055a36e86b297489cffb8e9d0b4aee3d82941680f6abb9716f3fb2f8e
      symbol_hashes:
        sys_access: sha256:e53d5b954a3ef9ff58ed71b80472fb3f2b0ccaa44cb3004d725642a4a4689410
        sys_faccessat2: sha256:2b709c3ba051efeb9d68846547ada28d8b8cac5b8611e1be55b6fce8e6cab756
      missing_symbols: []
      content_hash: sha256:a54fce312aa6a1f336b085bc3620f03cb300748c4b561a5eef4e55d55de13ed0
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_access 委托 sys_faccessat2；F_OK 快速成功，并按 root 及 owner/group/other 有效权限位检查 R_OK、W_OK、X_OK，静态覆盖
      access02 权限案例。
  LTP_0290063892A53510:
    syscalls: *id003
    rule_version:
      id: LTP_0290063892A53510
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:0290063892a5351022a2ab7b4cb9849ec40fa29b864a2ddc25704eaefa3e2fc7
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_030858A5FFCCEFF4:
    syscalls: *id004
    rule_version:
      id: LTP_030858A5FFCCEFF4
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:030858a5ffcceff4801d7ba45b78d895d2681e32e7f4ef9f88f30c2caa67a40e
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_035E62E6D1787773:
    syscalls: *id005
    rule_version:
      id: LTP_035E62E6D1787773
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:035e62e6d17877739db6b59f91601ed94cfa7d9904d1176fd2d2f2e9f8791738
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_036EDA2B8D36CF03:
    syscalls: *id006
    rule_version:
      id: LTP_036EDA2B8D36CF03
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:036eda2b8d36cf0300b93ee6a14685f0f6e4f787729cd0eb83fa377979143be6
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_037E6F334D0E0D16:
    syscalls: *id007
    rule_version:
      id: LTP_037E6F334D0E0D16
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:037e6f334d0e0d16d085d2f03c051ebd6062b33c049ebecb4a6f1bc79e401a83
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_0431E3529AA0FEE8:
    syscalls: *id008
    rule_version:
      id: LTP_0431E3529AA0FEE8
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:0431e3529aa0fee804b2f7242cf911e84dc5d046d7785cee532eb968842b1886
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_044E7C11E6B503BB:
    syscalls: *id009
    rule_version: &id332
      id: LTP_044E7C11E6B503BB
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:044e7c11e6b503bb657c1f5d568942154575515e5bd090cfb272ebd5b2953217
    status: covered
    static_check_refs:
    - STARRY_ACCESS_PERMISSIONS
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ACCESS_PERMISSIONS:
          id: STARRY_ACCESS_PERMISSIONS
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:9a2f8a7c6a97cb3e0bb0faa21d342b618172c583039ca74535fe0f394fa364bd
      dynamic_tests: {}
    target_dependencies:
    - path: os/StarryOS/kernel/src/file/fs.rs
      symbols:
      - resolve_at
      scope: symbols
      file_hash: sha256:550e894d6abfbc7221d14420c4a3b9ed85ff072e792e108c2f8b7f8a6dceeefd
      symbol_hashes:
        resolve_at: sha256:ec9e7f57add9a1db10191664fd7c77c9236ea7f33e3df9b43ce8fd66ddc0a01f
      missing_symbols: []
      content_hash: sha256:b3dce20309fe9f480c0da78b10b6995550acae12ab1f7f9f348ac78ca0cebbe2
    - path: os/StarryOS/kernel/src/syscall/fs/stat.rs
      symbols:
      - sys_access
      - sys_faccessat2
      scope: symbols
      file_hash: sha256:8c2b95c055a36e86b297489cffb8e9d0b4aee3d82941680f6abb9716f3fb2f8e
      symbol_hashes:
        sys_access: sha256:e53d5b954a3ef9ff58ed71b80472fb3f2b0ccaa44cb3004d725642a4a4689410
        sys_faccessat2: sha256:2b709c3ba051efeb9d68846547ada28d8b8cac5b8611e1be55b6fce8e6cab756
      missing_symbols: []
      content_hash: sha256:a54fce312aa6a1f336b085bc3620f03cb300748c4b561a5eef4e55d55de13ed0
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_access 委托 sys_faccessat2；F_OK 快速成功，并按 root 及 owner/group/other 有效权限位检查 R_OK、W_OK、X_OK，静态覆盖
      access02 权限案例。
  LTP_060B6037DEF1D43C:
    syscalls: *id010
    rule_version:
      id: LTP_060B6037DEF1D43C
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:060b6037def1d43c9de3ca80ee5aebdb2cf64bbf6b1745c252af35d117049ef7
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_06725D44DFF06F7E:
    syscalls: *id011
    rule_version:
      id: LTP_06725D44DFF06F7E
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:06725d44dff06f7e7b34882d799fa971d2ddf049a360e5bc1fa26eee8a5ded8c
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_06891E2E299CF48E:
    syscalls: *id012
    rule_version: &id333
      id: LTP_06891E2E299CF48E
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:06891e2e299cf48e89e834978cafb8d3f54a5f988367d5ac9c5daf94202c0532
    status: covered
    static_check_refs:
    - STARRY_ACCESS_PERMISSIONS
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ACCESS_PERMISSIONS:
          id: STARRY_ACCESS_PERMISSIONS
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:9a2f8a7c6a97cb3e0bb0faa21d342b618172c583039ca74535fe0f394fa364bd
      dynamic_tests: {}
    target_dependencies:
    - path: os/StarryOS/kernel/src/file/fs.rs
      symbols:
      - resolve_at
      scope: symbols
      file_hash: sha256:550e894d6abfbc7221d14420c4a3b9ed85ff072e792e108c2f8b7f8a6dceeefd
      symbol_hashes:
        resolve_at: sha256:ec9e7f57add9a1db10191664fd7c77c9236ea7f33e3df9b43ce8fd66ddc0a01f
      missing_symbols: []
      content_hash: sha256:b3dce20309fe9f480c0da78b10b6995550acae12ab1f7f9f348ac78ca0cebbe2
    - path: os/StarryOS/kernel/src/syscall/fs/stat.rs
      symbols:
      - sys_access
      - sys_faccessat2
      scope: symbols
      file_hash: sha256:8c2b95c055a36e86b297489cffb8e9d0b4aee3d82941680f6abb9716f3fb2f8e
      symbol_hashes:
        sys_access: sha256:e53d5b954a3ef9ff58ed71b80472fb3f2b0ccaa44cb3004d725642a4a4689410
        sys_faccessat2: sha256:2b709c3ba051efeb9d68846547ada28d8b8cac5b8611e1be55b6fce8e6cab756
      missing_symbols: []
      content_hash: sha256:a54fce312aa6a1f336b085bc3620f03cb300748c4b561a5eef4e55d55de13ed0
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_access 委托 sys_faccessat2；F_OK 快速成功，并按 root 及 owner/group/other 有效权限位检查 R_OK、W_OK、X_OK，静态覆盖
      access02 权限案例。
  LTP_06A0C295D8E7FAFA:
    syscalls: *id013
    rule_version:
      id: LTP_06A0C295D8E7FAFA
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:06a0c295d8e7fafa651946a3613c2e32e4a46c5c733aed891d879dd24b06d14f
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_06AC9297E35AAE7A:
    syscalls: *id014
    rule_version:
      id: LTP_06AC9297E35AAE7A
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:06ac9297e35aae7a524a02e7136a35e29d155f5741903b920ab3d6f8f300ab3e
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_075318C437B76E06:
    syscalls: *id015
    rule_version: &id334
      id: LTP_075318C437B76E06
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:075318c437b76e067682a9c6aab95a64558daf471c20df7205f62a72b1fd82ee
    status: covered
    static_check_refs:
    - STARRY_ACCESS_USER_POINTER
    - STARRY_BATCH_ERRNO_TRANSLATION
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ACCESS_USER_POINTER:
          id: STARRY_ACCESS_USER_POINTER
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:1df5a8a335cbf4e4f9bd77c4078ca8ef9f1a642feba46a2c79cea6aec66df23c
        STARRY_BATCH_ERRNO_TRANSLATION:
          id: STARRY_BATCH_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:e19f574ad1b857afc459fe1d55fbe4e71451eceeeeff1452ff74c6c7fec81a15
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: components/starry-vm/src/alloc.rs
      symbols:
      - vm_load_until_nul
      scope: symbols
      file_hash: sha256:06b13f8c1700e024de6382919ddc0f8c2bf772798654a38d9e7f41c18ab2032e
      symbol_hashes:
        vm_load_until_nul: sha256:f65607e74fce137d86a282539ef80615a63582cf551668aa44115ed3b4e49767
      missing_symbols: []
      content_hash: sha256:8d542c4492f2dfe413baf6453ad0fd2edc7ac82a1ba69e9c16ca0f5a27bd691c
    - path: os/StarryOS/kernel/src/file/fs.rs
      symbols:
      - resolve_at
      scope: symbols
      file_hash: sha256:550e894d6abfbc7221d14420c4a3b9ed85ff072e792e108c2f8b7f8a6dceeefd
      symbol_hashes:
        resolve_at: sha256:ec9e7f57add9a1db10191664fd7c77c9236ea7f33e3df9b43ce8fd66ddc0a01f
      missing_symbols: []
      content_hash: sha256:b3dce20309fe9f480c0da78b10b6995550acae12ab1f7f9f348ac78ca0cebbe2
    - path: os/StarryOS/kernel/src/mm/access.rs
      symbols:
      - vm_load_path_string
      - vm_load_string
      scope: symbols
      file_hash: sha256:4c4fd8a5e5fdf74824fba2666041a10ff4daf9a0214bf6ddeabe8c9e67fc60a6
      symbol_hashes:
        vm_load_path_string: sha256:95f8b4926ce8e625750404ccab6b5faf51ebf398553aac30035185c0d56642f4
        vm_load_string: sha256:cee098cc352143ede741ebb982ba6d15f7eac71b6667871500b4a5ac4d42bb2e
      missing_symbols: []
      content_hash: sha256:f6fdd2214052ea5f56fef51f35d895763600c89e1aba847f54432d0346f2d3d4
    - path: os/StarryOS/kernel/src/syscall/fs/stat.rs
      symbols:
      - sys_access
      - sys_faccessat2
      scope: symbols
      file_hash: sha256:8c2b95c055a36e86b297489cffb8e9d0b4aee3d82941680f6abb9716f3fb2f8e
      symbol_hashes:
        sys_access: sha256:e53d5b954a3ef9ff58ed71b80472fb3f2b0ccaa44cb3004d725642a4a4689410
        sys_faccessat2: sha256:2b709c3ba051efeb9d68846547ada28d8b8cac5b8611e1be55b6fce8e6cab756
      missing_symbols: []
      content_hash: sha256:a54fce312aa6a1f336b085bc3620f03cb300748c4b561a5eef4e55d55de13ed0
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_faccessat2 在路径解析前通过 vm_load_path_string 读取用户字符串；坏地址传播为 BadAddress，并由 errno 转换为 EFAULT。
  LTP_0799FC60BADD2B18:
    syscalls: *id016
    rule_version: &id335
      id: LTP_0799FC60BADD2B18
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:0799fc60badd2b189b242a57ba5740cd832aa2477cbe8497f5b09324880ca7f4
    status: covered
    static_check_refs:
    - STARRY_ACCESS_USER_POINTER
    - STARRY_BATCH_ERRNO_TRANSLATION
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ACCESS_USER_POINTER:
          id: STARRY_ACCESS_USER_POINTER
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:1df5a8a335cbf4e4f9bd77c4078ca8ef9f1a642feba46a2c79cea6aec66df23c
        STARRY_BATCH_ERRNO_TRANSLATION:
          id: STARRY_BATCH_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:e19f574ad1b857afc459fe1d55fbe4e71451eceeeeff1452ff74c6c7fec81a15
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: components/starry-vm/src/alloc.rs
      symbols:
      - vm_load_until_nul
      scope: symbols
      file_hash: sha256:06b13f8c1700e024de6382919ddc0f8c2bf772798654a38d9e7f41c18ab2032e
      symbol_hashes:
        vm_load_until_nul: sha256:f65607e74fce137d86a282539ef80615a63582cf551668aa44115ed3b4e49767
      missing_symbols: []
      content_hash: sha256:8d542c4492f2dfe413baf6453ad0fd2edc7ac82a1ba69e9c16ca0f5a27bd691c
    - path: os/StarryOS/kernel/src/file/fs.rs
      symbols:
      - resolve_at
      scope: symbols
      file_hash: sha256:550e894d6abfbc7221d14420c4a3b9ed85ff072e792e108c2f8b7f8a6dceeefd
      symbol_hashes:
        resolve_at: sha256:ec9e7f57add9a1db10191664fd7c77c9236ea7f33e3df9b43ce8fd66ddc0a01f
      missing_symbols: []
      content_hash: sha256:b3dce20309fe9f480c0da78b10b6995550acae12ab1f7f9f348ac78ca0cebbe2
    - path: os/StarryOS/kernel/src/mm/access.rs
      symbols:
      - vm_load_path_string
      - vm_load_string
      scope: symbols
      file_hash: sha256:4c4fd8a5e5fdf74824fba2666041a10ff4daf9a0214bf6ddeabe8c9e67fc60a6
      symbol_hashes:
        vm_load_path_string: sha256:95f8b4926ce8e625750404ccab6b5faf51ebf398553aac30035185c0d56642f4
        vm_load_string: sha256:cee098cc352143ede741ebb982ba6d15f7eac71b6667871500b4a5ac4d42bb2e
      missing_symbols: []
      content_hash: sha256:f6fdd2214052ea5f56fef51f35d895763600c89e1aba847f54432d0346f2d3d4
    - path: os/StarryOS/kernel/src/syscall/fs/stat.rs
      symbols:
      - sys_access
      - sys_faccessat2
      scope: symbols
      file_hash: sha256:8c2b95c055a36e86b297489cffb8e9d0b4aee3d82941680f6abb9716f3fb2f8e
      symbol_hashes:
        sys_access: sha256:e53d5b954a3ef9ff58ed71b80472fb3f2b0ccaa44cb3004d725642a4a4689410
        sys_faccessat2: sha256:2b709c3ba051efeb9d68846547ada28d8b8cac5b8611e1be55b6fce8e6cab756
      missing_symbols: []
      content_hash: sha256:a54fce312aa6a1f336b085bc3620f03cb300748c4b561a5eef4e55d55de13ed0
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_faccessat2 在路径解析前通过 vm_load_path_string 读取用户字符串；坏地址传播为 BadAddress，并由 errno 转换为 EFAULT。
  LTP_09B39E9C9254ECB2:
    syscalls: *id017
    rule_version:
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
    reason: 相关 Starry 内容指纹未变化，已跳过。
  LTP_0A62800536904C02:
    syscalls: *id018
    rule_version:
      id: LTP_0A62800536904C02
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:0a62800536904c0231dfd538b848b4c23fd261fbe26b6291a46dd1c085dc1ff0
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_0AAFA34BA77A0D25:
    syscalls: *id019
    rule_version:
      id: LTP_0AAFA34BA77A0D25
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:0aafa34ba77a0d25c3bd2632bf23889acf190eb7c15c253cee339354f1110c2b
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_0B45FC33068D334C:
    syscalls: *id020
    rule_version:
      id: LTP_0B45FC33068D334C
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:0b45fc33068d334cf0357b5b3073acdade7252dc401c49826a1462e2af51fa55
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_0BB235F712E819CE:
    syscalls: *id021
    rule_version:
      id: LTP_0BB235F712E819CE
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:0bb235f712e819ce1befaab2d5b66dea761c42c1065a66f2bfb8da4f8f73c7ab
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_0CD17E662AFD2956:
    syscalls: *id022
    rule_version:
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
    reason: 相关 Starry 内容指纹未变化，已跳过。
  LTP_0D1782EAAC26DEB4:
    syscalls: *id023
    rule_version: &id336
      id: LTP_0D1782EAAC26DEB4
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:0d1782eaac26deb423a13b1bef2c3fc0e4647c3d464451e818c877ae67a0c0b9
    status: covered
    static_check_refs:
    - STARRY_ACCESS_PERMISSIONS
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ACCESS_PERMISSIONS:
          id: STARRY_ACCESS_PERMISSIONS
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:9a2f8a7c6a97cb3e0bb0faa21d342b618172c583039ca74535fe0f394fa364bd
      dynamic_tests: {}
    target_dependencies:
    - path: os/StarryOS/kernel/src/file/fs.rs
      symbols:
      - resolve_at
      scope: symbols
      file_hash: sha256:550e894d6abfbc7221d14420c4a3b9ed85ff072e792e108c2f8b7f8a6dceeefd
      symbol_hashes:
        resolve_at: sha256:ec9e7f57add9a1db10191664fd7c77c9236ea7f33e3df9b43ce8fd66ddc0a01f
      missing_symbols: []
      content_hash: sha256:b3dce20309fe9f480c0da78b10b6995550acae12ab1f7f9f348ac78ca0cebbe2
    - path: os/StarryOS/kernel/src/syscall/fs/stat.rs
      symbols:
      - sys_access
      - sys_faccessat2
      scope: symbols
      file_hash: sha256:8c2b95c055a36e86b297489cffb8e9d0b4aee3d82941680f6abb9716f3fb2f8e
      symbol_hashes:
        sys_access: sha256:e53d5b954a3ef9ff58ed71b80472fb3f2b0ccaa44cb3004d725642a4a4689410
        sys_faccessat2: sha256:2b709c3ba051efeb9d68846547ada28d8b8cac5b8611e1be55b6fce8e6cab756
      missing_symbols: []
      content_hash: sha256:a54fce312aa6a1f336b085bc3620f03cb300748c4b561a5eef4e55d55de13ed0
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_access 委托 sys_faccessat2；F_OK 快速成功，并按 root 及 owner/group/other 有效权限位检查 R_OK、W_OK、X_OK，静态覆盖
      access02 权限案例。
  LTP_0E9AF2C058AF8126:
    syscalls: *id024
    rule_version:
      id: LTP_0E9AF2C058AF8126
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:0e9af2c058af8126ab590f4af3482c8cef54975bc433bc4fd72f2e9e995f0b7e
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_0F901C62092CC7B8:
    syscalls: *id025
    rule_version:
      id: LTP_0F901C62092CC7B8
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:0f901c62092cc7b8b0b52da1ecc4765c39b985ba06d0cde2403d83870bb85b5f
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_10A684C1C2D2DE0F:
    syscalls: *id026
    rule_version:
      id: LTP_10A684C1C2D2DE0F
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:10a684c1c2d2de0ffb60286a885a3ca7a2dd3efe1ea7f8b558e414f6600a17a2
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_10FE1313FBAB5F92:
    syscalls: *id027
    rule_version:
      id: LTP_10FE1313FBAB5F92
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:10fe1313fbab5f922177fdab0a0b6689cda7f927eb5c69552253739d55d3d86f
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_1325C077A1CDE514:
    syscalls: *id028
    rule_version:
      id: LTP_1325C077A1CDE514
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:1325c077a1cde5141c5f598497a0fd7e10c5adeda759688a6fc3b2f02cc64aab
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::cachestat 分派分支，syscall 实现目录中也没有
      sys_cachestat 入口。
  LTP_1402459B5FF9BF23:
    syscalls: *id029
    rule_version:
      id: LTP_1402459B5FF9BF23
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:1402459b5ff9bf23e7573fc58e2bd88e7a0e24fe7b709fac9d058701c2419681
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_1465554B09CE14F0:
    syscalls: *id030
    rule_version:
      id: LTP_1465554B09CE14F0
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:1465554b09ce14f0b5a735a4a5e0b72f71a87d0d0e40af031decb029dcb06eaf
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_148623FDAF4E478D:
    syscalls: *id031
    rule_version:
      id: LTP_148623FDAF4E478D
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:148623fdaf4e478d7bc5953483a91b32d18a4a0374aa87efa70ca569b067bc08
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_153B296FA599E0CE:
    syscalls: *id032
    rule_version:
      id: LTP_153B296FA599E0CE
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:153b296fa599e0ce4555e2bb2282ac195f43cdb6c0c7079b4d03f64c21b57bd6
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_17ACF3BE969B64EE:
    syscalls: *id033
    rule_version:
      id: LTP_17ACF3BE969B64EE
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:17acf3be969b64eeacbd0b1e0d7962096022eafafe0daba6fed1e0e668a86609
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_17CB4ED7A76BD283:
    syscalls: *id034
    rule_version:
      id: LTP_17CB4ED7A76BD283
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:17cb4ed7a76bd2837ae4f4604ac37111d7656358256727f2e918e7c166bc98a5
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_1870C0046E9555AF:
    syscalls: *id035
    rule_version:
      id: LTP_1870C0046E9555AF
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:1870c0046e9555af9d7e66141ed6475091b877da1cfbdc00aa87c2634b6e60d2
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_18A450CE49F8867B:
    syscalls: *id036
    rule_version:
      id: LTP_18A450CE49F8867B
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:18a450ce49f8867b0a9250309a99648d981828d27b48aa2a91f513504b505643
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_198D9555A8BED013:
    syscalls: *id037
    rule_version:
      id: LTP_198D9555A8BED013
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:198d9555a8bed013005fa53f75f062528eee407371a00ce59e91b35492135b4b
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_1A9481FAD460FBF7:
    syscalls: *id038
    rule_version:
      id: LTP_1A9481FAD460FBF7
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:1a9481fad460fbf78c35e41fcfc8799bab17d5ea12dca5910fcac0ba464bd776
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有
      sys_alarm 入口。
  LTP_1BD36AE285B4F3E2:
    syscalls: *id039
    rule_version:
      id: LTP_1BD36AE285B4F3E2
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:1bd36ae285b4f3e25c7c437dbf46333126e0ff5fa47eeab6ffec8f981fa0874e
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_1C462AC54A29FF35:
    syscalls: *id040
    rule_version:
      id: LTP_1C462AC54A29FF35
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:1c462ac54a29ff357fc83b28d38fb27f808d5eae31786aeff93269e3daf9911a
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_1CDCF5FE9ED1BE5D:
    syscalls: *id041
    rule_version:
      id: LTP_1CDCF5FE9ED1BE5D
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:1cdcf5fe9ed1be5df8f5722e4428822d616a324d2465d968f642d7fc156571a9
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_1D39F97D759F0E57:
    syscalls: *id042
    rule_version:
      id: LTP_1D39F97D759F0E57
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:1d39f97d759f0e57f0b75f9051337bac3a6d0e132ec3b90d9b3e2a5f2eb6ee51
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_1DF2B28499E4D7B3:
    syscalls: *id043
    rule_version:
      id: LTP_1DF2B28499E4D7B3
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:1df2b28499e4d7b3d66a41c156e6d76091647274b46de23227d0d0d90e7d53f0
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_208C833FF12217F5:
    syscalls: *id044
    rule_version: &id337
      id: LTP_208C833FF12217F5
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:208c833ff12217f5ee10c2893ca4aab718793f8504783e4c1e69970fe3fc01dc
    status: covered
    static_check_refs:
    - STARRY_CAPGET_ABI
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_CAPGET_ABI:
          id: STARRY_CAPGET_ABI
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:9a7cf39c2be08e7a05c61f4ecfdb857e5ec45b702956c945d8c51b07cffde003
      dynamic_tests: {}
    target_dependencies:
    - path: components/starry-vm/src/thin.rs
      symbols:
      - VmMutPtr
      - VmPtr
      scope: symbols
      file_hash: sha256:b787237758b16cc38fc20fa79234f62e2bad5d70235621818f9771c4a0810aa4
      symbol_hashes:
        VmMutPtr: sha256:35ae0c032d454211b5a4d3e0b11bf6bf854bd550d635855677666f26fb1f730a
        VmPtr: sha256:6c0ff10e65451fa76a4eb2caa472c0a96ff53459ae357d86f2dbf389f50e8804
      missing_symbols: []
      content_hash: sha256:1b7ca80cea190deec16a1cec479d83444169c6259f68ca0bf314edc58015fecd
    - path: os/StarryOS/kernel/src/syscall/task/ctl.rs
      symbols:
      - cap_data_from_cred
      - cred_for_pid
      - sys_capget
      - validate_cap_header
      scope: symbols
      file_hash: sha256:901fc111c7b58af132705a41cf8a75d89164f522f89135f794e08b76a1ec05e9
      symbol_hashes:
        cap_data_from_cred: sha256:12056db903d695b783e772fd520dafe507b7315b9a2f2581105a450c9d56884c
        cred_for_pid: sha256:5827d237893e92b1f7ac1cca89ee96df45f8bebd11d31d63dd76159e254674f8
        sys_capget: sha256:2d1bd6599456ea3fe4ff537c67fce4708ca32a841c6199426ddfda7997da1556
        validate_cap_header: sha256:f92b10dad6654ff4b7de228735357465447f4fc6010d9b0eb50afaae686cbf33
      missing_symbols: []
      content_hash: sha256:78191b3ad60afbde9d82f02ab40fc336efecdf1730cd04ce1b1052382fc2b197
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_capget 校验 Linux V3 capability header，读取目标凭据并向用户态写回两个 capability 数据字，成功返回 0。
  LTP_212269CECE600FD8:
    syscalls: *id045
    rule_version:
      id: LTP_212269CECE600FD8
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:212269cece600fd878a851cd77e845c2a59b421728918141ae16a27e0d4c95eb
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_21A007DF738F1E73:
    syscalls: *id046
    rule_version:
      id: LTP_21A007DF738F1E73
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:21a007df738f1e73d4d114588fead88ebbe79ee5fd70f18cd1f7fcdb959e920a
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_21C4957F9EFE94D3:
    syscalls: *id047
    rule_version:
      id: LTP_21C4957F9EFE94D3
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:21c4957f9efe94d3e66d50ae689b746486cda4c816cdeb5886609743f44a7b22
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_220D1227D307AD3C:
    syscalls: *id048
    rule_version:
      id: LTP_220D1227D307AD3C
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:220d1227d307ad3c1622e2899c7258e3e21ae9526597a9364235fd48ef3883dd
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_2221F954D01EB2BB:
    syscalls: *id049
    rule_version:
      id: LTP_2221F954D01EB2BB
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:2221f954d01eb2bb9f9cabda5ec81c84973ac2e69b800bd2192cc74e96aaa97a
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_245CD61DAA19DC98:
    syscalls: *id050
    rule_version: &id338
      id: LTP_245CD61DAA19DC98
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:245cd61daa19dc987195efcf282a428df3dfc7429cd89bcc1fbc741e96407c30
    status: covered
    static_check_refs:
    - STARRY_BATCH_ERRNO_TRANSLATION
    - STARRY_CHROOT_PATH
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_BATCH_ERRNO_TRANSLATION:
          id: STARRY_BATCH_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:e19f574ad1b857afc459fe1d55fbe4e71451eceeeeff1452ff74c6c7fec81a15
        STARRY_CHROOT_PATH:
          id: STARRY_CHROOT_PATH
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:357fbab1f149ef6fb3807966810bffa3366973f2c4f2c854bb821004e4a3753f
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: components/axfs-ng-vfs/src/path.rs
      symbols:
      - verify_entry_name
      scope: symbols
      file_hash: sha256:6e44a62c3142a5ebecb4c5c4c93f2d06c24ff549457c5c8b6787c8e90e46c11e
      symbol_hashes:
        verify_entry_name: sha256:516c7b090800149dc2bf3b7312761813844477a67da496c991099780f62c7ce5
      missing_symbols: []
      content_hash: sha256:2b2482c278ed782ee473d1a44f6611931e19f6b8db3edb22a40b3333d6bf50a0
    - path: components/starry-vm/src/alloc.rs
      symbols:
      - vm_load_until_nul
      scope: symbols
      file_hash: sha256:06b13f8c1700e024de6382919ddc0f8c2bf772798654a38d9e7f41c18ab2032e
      symbol_hashes:
        vm_load_until_nul: sha256:f65607e74fce137d86a282539ef80615a63582cf551668aa44115ed3b4e49767
      missing_symbols: []
      content_hash: sha256:8d542c4492f2dfe413baf6453ad0fd2edc7ac82a1ba69e9c16ca0f5a27bd691c
    - path: os/StarryOS/kernel/src/mm/access.rs
      symbols:
      - vm_load_string
      scope: symbols
      file_hash: sha256:4c4fd8a5e5fdf74824fba2666041a10ff4daf9a0214bf6ddeabe8c9e67fc60a6
      symbol_hashes:
        vm_load_string: sha256:cee098cc352143ede741ebb982ba6d15f7eac71b6667871500b4a5ac4d42bb2e
      missing_symbols: []
      content_hash: sha256:e17a288c5843ae74a5c3e12ef6048c2572a8793b06467613638d615ffc385958
    - path: os/StarryOS/kernel/src/syscall/fs/ctl.rs
      symbols:
      - sys_chroot
      scope: symbols
      file_hash: sha256:a42d57fc2422560978476f017ea2ae3d59e59be8c3f119e45fb5f18529d2e7e5
      symbol_hashes:
        sys_chroot: sha256:2445750c1d3c822f8438f9a1914fe47b5360157364ca20142ad673492d889756
      missing_symbols: []
      content_hash: sha256:928d58e7292bc7e8922d1000e5aabe85e9fdb3f1f6c3f84b52583584b92d0d55
    - path: os/arceos/modules/axfs-ng/src/fs_core/context.rs
      symbols:
      - new
      - resolve
      - resolve_inner
      - try_resolve_symlink
      scope: symbols
      file_hash: sha256:6cd56d9acec5dc2b33d0d931a4e147c7dcd13318fe706800a02503c2220f7204
      symbol_hashes:
        new: sha256:3d17bd68745b169b5dbdd92e4dae5756b1d41e3850eea66a0cf7be91f1c551b2
        resolve: sha256:14a2b52408caa4b091a4b90ec30e6412155884199bbc592741da38777fc3581a
        resolve_inner: sha256:702d76c45f2ff1046f5d437d0e459366482b7ef2e76b1cfb259d536be7b52cc5
        try_resolve_symlink: sha256:2577319f282965c000834bd77c6fd7e1f77f7d44f10b688767d6391bab4169f3
      missing_symbols: []
      content_hash: sha256:955067eb239a31c67297a10606806cadf346d537ebd469118db448e88e52f236
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_chroot 先读取用户路径，再经 FsContext 解析并要求目标为目录；路径读取或解析错误及 ENOTDIR 由 errno 层保真转换。
  LTP_25639C9C5750C487:
    syscalls: *id051
    rule_version:
      id: LTP_25639C9C5750C487
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:25639c9c5750c487fcedf6d0ec8774392cef4e9acd74069166a8a2a8bd1ea90e
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_26AC646B9D18C353:
    syscalls: *id052
    rule_version:
      id: LTP_26AC646B9D18C353
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:26ac646b9d18c353cf98f2ad49a480176e3c37f06acf9c84818255abf755f99c
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_277FD467E5F1BF1C:
    syscalls: *id053
    rule_version:
      id: LTP_277FD467E5F1BF1C
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:277fd467e5f1bf1c23ee7c1139c3420fd53e3387d46a1441bccd3f763aecc0c1
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 规则依赖 socket 类型、监听或连接队列、地址长度、用户指针以及 exp_errno 等运行时状态；现有静态分支无法唯一确定预期结果。
  LTP_27C7E91095DB9DF8:
    syscalls: *id054
    rule_version:
      id: LTP_27C7E91095DB9DF8
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:27c7e91095db9df833b0e7ea1e461c43f3d9fbde5c93ef4a7131cccc48a5df5d
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_2900BC64740A3E44:
    syscalls: *id055
    rule_version:
      id: LTP_2900BC64740A3E44
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:2900bc64740a3e44e3915afb13c01233f03f913b311ddb57b3173b513a3215c2
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_298AB67F0CFA519C:
    syscalls: *id056
    rule_version:
      id: LTP_298AB67F0CFA519C
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:298ab67f0cfa519c0db5140ce8f9ad87d6720b8da357263c84dd9346b732cb2a
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_2B4171DD8FBD982A:
    syscalls: *id057
    rule_version:
      id: LTP_2B4171DD8FBD982A
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:2b4171dd8fbd982a461eb396fb5c1b19585ca852641fe389afeda6644b7a4dd0
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_2D0BAECAE4F61432:
    syscalls: *id058
    rule_version:
      id: LTP_2D0BAECAE4F61432
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:2d0baecae4f614321089041a1a0684b081a6857a5d0e84eedc6e8c1772e3fb8c
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_2E5D530A61E60934:
    syscalls: *id059
    rule_version:
      id: LTP_2E5D530A61E60934
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:2e5d530a61e609346a68ecee5667739da2d8a5b9da2a755ad8e2eb5d4882a340
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_2F99FA84C445363C:
    syscalls: *id060
    rule_version: &id339
      id: LTP_2F99FA84C445363C
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:2f99fa84c445363ccdb31044c1a489fb3da71ffb0efca79bea63770a584e2bde
    status: covered
    static_check_refs:
    - STARRY_ACCESS_PATH_RESOLUTION
    - STARRY_BATCH_ERRNO_TRANSLATION
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ACCESS_PATH_RESOLUTION:
          id: STARRY_ACCESS_PATH_RESOLUTION
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:896f2b8f806c19bafee558addd47df7692321be39551b0da996b9c942907a805
        STARRY_BATCH_ERRNO_TRANSLATION:
          id: STARRY_BATCH_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:e19f574ad1b857afc459fe1d55fbe4e71451eceeeeff1452ff74c6c7fec81a15
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: components/axfs-ng-vfs/src/path.rs
      symbols:
      - verify_entry_name
      scope: symbols
      file_hash: sha256:6e44a62c3142a5ebecb4c5c4c93f2d06c24ff549457c5c8b6787c8e90e46c11e
      symbol_hashes:
        verify_entry_name: sha256:516c7b090800149dc2bf3b7312761813844477a67da496c991099780f62c7ce5
      missing_symbols: []
      content_hash: sha256:2b2482c278ed782ee473d1a44f6611931e19f6b8db3edb22a40b3333d6bf50a0
    - path: components/starry-vm/src/alloc.rs
      symbols:
      - vm_load_until_nul
      scope: symbols
      file_hash: sha256:06b13f8c1700e024de6382919ddc0f8c2bf772798654a38d9e7f41c18ab2032e
      symbol_hashes:
        vm_load_until_nul: sha256:f65607e74fce137d86a282539ef80615a63582cf551668aa44115ed3b4e49767
      missing_symbols: []
      content_hash: sha256:8d542c4492f2dfe413baf6453ad0fd2edc7ac82a1ba69e9c16ca0f5a27bd691c
    - path: os/StarryOS/kernel/src/file/fs.rs
      symbols:
      - resolve_at
      scope: symbols
      file_hash: sha256:550e894d6abfbc7221d14420c4a3b9ed85ff072e792e108c2f8b7f8a6dceeefd
      symbol_hashes:
        resolve_at: sha256:ec9e7f57add9a1db10191664fd7c77c9236ea7f33e3df9b43ce8fd66ddc0a01f
      missing_symbols: []
      content_hash: sha256:b3dce20309fe9f480c0da78b10b6995550acae12ab1f7f9f348ac78ca0cebbe2
    - path: os/StarryOS/kernel/src/mm/access.rs
      symbols:
      - vm_load_path_string
      - vm_load_string
      scope: symbols
      file_hash: sha256:4c4fd8a5e5fdf74824fba2666041a10ff4daf9a0214bf6ddeabe8c9e67fc60a6
      symbol_hashes:
        vm_load_path_string: sha256:95f8b4926ce8e625750404ccab6b5faf51ebf398553aac30035185c0d56642f4
        vm_load_string: sha256:cee098cc352143ede741ebb982ba6d15f7eac71b6667871500b4a5ac4d42bb2e
      missing_symbols: []
      content_hash: sha256:f6fdd2214052ea5f56fef51f35d895763600c89e1aba847f54432d0346f2d3d4
    - path: os/StarryOS/kernel/src/syscall/fs/stat.rs
      symbols:
      - sys_access
      - sys_faccessat2
      scope: symbols
      file_hash: sha256:8c2b95c055a36e86b297489cffb8e9d0b4aee3d82941680f6abb9716f3fb2f8e
      symbol_hashes:
        sys_access: sha256:e53d5b954a3ef9ff58ed71b80472fb3f2b0ccaa44cb3004d725642a4a4689410
        sys_faccessat2: sha256:2b709c3ba051efeb9d68846547ada28d8b8cac5b8611e1be55b6fce8e6cab756
      missing_symbols: []
      content_hash: sha256:a54fce312aa6a1f336b085bc3620f03cb300748c4b561a5eef4e55d55de13ed0
    - path: os/arceos/modules/axfs-ng/src/fs_core/context.rs
      symbols:
      - resolve
      - resolve_inner
      - try_resolve_symlink
      scope: symbols
      file_hash: sha256:6cd56d9acec5dc2b33d0d931a4e147c7dcd13318fe706800a02503c2220f7204
      symbol_hashes:
        resolve: sha256:14a2b52408caa4b091a4b90ec30e6412155884199bbc592741da38777fc3581a
        resolve_inner: sha256:702d76c45f2ff1046f5d437d0e459366482b7ef2e76b1cfb259d536be7b52cc5
        try_resolve_symlink: sha256:2577319f282965c000834bd77c6fd7e1f77f7d44f10b688767d6391bab4169f3
      missing_symbols: []
      content_hash: sha256:0cf7ffc1f42cba981fa89780d918b03c47f71d465064f3e12b024bf39d071734
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_faccessat2 加载路径后调用 resolve_at/FsContext 路径解析；缺失项、非目录组件、符号链接循环和超长路径错误按 Linux errno 传播。
  LTP_2FA43CD942AE7AD6:
    syscalls: *id061
    rule_version:
      id: LTP_2FA43CD942AE7AD6
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:2fa43cd942ae7ad6ccb5075fb30e8dfe102ad171ef4bb0d8f3b53fe0414d4f04
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_2FE8FAD800DE41F6:
    syscalls: *id062
    rule_version:
      id: LTP_2FE8FAD800DE41F6
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:2fe8fad800de41f63ccd36fc268ba471fb2b0e8a976a37d489d680e7730d8e9b
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_3472CD1A0F8A2B4A:
    syscalls: *id063
    rule_version:
      id: LTP_3472CD1A0F8A2B4A
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:3472cd1a0f8a2b4a54ab63d2a1d196f03bcd2aa624cb2a98ea16db372fda08db
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_347761CBCF52D194:
    syscalls: *id064
    rule_version:
      id: LTP_347761CBCF52D194
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:347761cbcf52d194787660bd2fb38371c03cb90d478f053ab9e79d9221b6cf8b
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_34CFEAD03DB6A3CA:
    syscalls: *id065
    rule_version:
      id: LTP_34CFEAD03DB6A3CA
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:34cfead03db6a3ca70d00de281c9408d7d7d61d2e4fe236b08786563a8708e78
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_34EC9FB9C9551214:
    syscalls: *id066
    rule_version:
      id: LTP_34EC9FB9C9551214
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:34ec9fb9c9551214fcca5118b8afb84e93c9e242cbd9c2674d0b9d0ec70c9566
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::cachestat 分派分支，syscall 实现目录中也没有
      sys_cachestat 入口。
  LTP_35CAEE10A613E109:
    syscalls: *id067
    rule_version:
      id: LTP_35CAEE10A613E109
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:35caee10a613e10914e037e7be0dacb0a8989b64d1d9e189aa137fb54b89b664
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_3636C4768C196B52:
    syscalls: *id068
    rule_version:
      id: LTP_3636C4768C196B52
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:3636c4768c196b52badf7a37729528d9190192b4ab768ee346f246182e7e7d79
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_368D8689810796B2:
    syscalls: *id069
    rule_version:
      id: LTP_368D8689810796B2
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:368d8689810796b2a234105c4c4f97f7fee4e238f4bd6f026807c3ef860c21d6
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_36C99C10CD38F8DB:
    syscalls: *id070
    rule_version:
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
    reason: 相关 Starry 内容指纹未变化，已跳过。
  LTP_38FB918826669241:
    syscalls: *id071
    rule_version: &id340
      id: LTP_38FB918826669241
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:38fb918826669241ebbe77827a90f4347f124cf6de78fd4f4b46b3495fb3ab2f
    status: covered
    static_check_refs:
    - STARRY_ACCESS_USER_POINTER
    - STARRY_BATCH_ERRNO_TRANSLATION
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ACCESS_USER_POINTER:
          id: STARRY_ACCESS_USER_POINTER
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:1df5a8a335cbf4e4f9bd77c4078ca8ef9f1a642feba46a2c79cea6aec66df23c
        STARRY_BATCH_ERRNO_TRANSLATION:
          id: STARRY_BATCH_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:e19f574ad1b857afc459fe1d55fbe4e71451eceeeeff1452ff74c6c7fec81a15
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: components/starry-vm/src/alloc.rs
      symbols:
      - vm_load_until_nul
      scope: symbols
      file_hash: sha256:06b13f8c1700e024de6382919ddc0f8c2bf772798654a38d9e7f41c18ab2032e
      symbol_hashes:
        vm_load_until_nul: sha256:f65607e74fce137d86a282539ef80615a63582cf551668aa44115ed3b4e49767
      missing_symbols: []
      content_hash: sha256:8d542c4492f2dfe413baf6453ad0fd2edc7ac82a1ba69e9c16ca0f5a27bd691c
    - path: os/StarryOS/kernel/src/file/fs.rs
      symbols:
      - resolve_at
      scope: symbols
      file_hash: sha256:550e894d6abfbc7221d14420c4a3b9ed85ff072e792e108c2f8b7f8a6dceeefd
      symbol_hashes:
        resolve_at: sha256:ec9e7f57add9a1db10191664fd7c77c9236ea7f33e3df9b43ce8fd66ddc0a01f
      missing_symbols: []
      content_hash: sha256:b3dce20309fe9f480c0da78b10b6995550acae12ab1f7f9f348ac78ca0cebbe2
    - path: os/StarryOS/kernel/src/mm/access.rs
      symbols:
      - vm_load_path_string
      - vm_load_string
      scope: symbols
      file_hash: sha256:4c4fd8a5e5fdf74824fba2666041a10ff4daf9a0214bf6ddeabe8c9e67fc60a6
      symbol_hashes:
        vm_load_path_string: sha256:95f8b4926ce8e625750404ccab6b5faf51ebf398553aac30035185c0d56642f4
        vm_load_string: sha256:cee098cc352143ede741ebb982ba6d15f7eac71b6667871500b4a5ac4d42bb2e
      missing_symbols: []
      content_hash: sha256:f6fdd2214052ea5f56fef51f35d895763600c89e1aba847f54432d0346f2d3d4
    - path: os/StarryOS/kernel/src/syscall/fs/stat.rs
      symbols:
      - sys_access
      - sys_faccessat2
      scope: symbols
      file_hash: sha256:8c2b95c055a36e86b297489cffb8e9d0b4aee3d82941680f6abb9716f3fb2f8e
      symbol_hashes:
        sys_access: sha256:e53d5b954a3ef9ff58ed71b80472fb3f2b0ccaa44cb3004d725642a4a4689410
        sys_faccessat2: sha256:2b709c3ba051efeb9d68846547ada28d8b8cac5b8611e1be55b6fce8e6cab756
      missing_symbols: []
      content_hash: sha256:a54fce312aa6a1f336b085bc3620f03cb300748c4b561a5eef4e55d55de13ed0
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_faccessat2 在路径解析前通过 vm_load_path_string 读取用户字符串；坏地址传播为 BadAddress，并由 errno 转换为 EFAULT。
  LTP_3900F4E562AE09D1:
    syscalls: *id072
    rule_version:
      id: LTP_3900F4E562AE09D1
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:3900f4e562ae09d1b996c7e0d13a4a75221f775687ad7e80caaf10193db1caf3
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_3916A669595B3568:
    syscalls: *id073
    rule_version:
      id: LTP_3916A669595B3568
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:3916a669595b35682ab5539f30613ffc1e634d2c181f1c31fbdf0367fea7f735
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_3AD3865603ADDC8E:
    syscalls: *id074
    rule_version:
      id: LTP_3AD3865603ADDC8E
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:3ad3865603addc8e91936e01b73876e1717a621920dbeb5a9751a731b7a14bc4
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_3C2853617B38EEE7:
    syscalls: *id075
    rule_version:
      id: LTP_3C2853617B38EEE7
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:3c2853617b38eee73d035c8cf8f2f494af2aabd3fed30aedbc94a9edfaf7698d
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_3D4ECD22BC433164:
    syscalls: *id076
    rule_version:
      id: LTP_3D4ECD22BC433164
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:3d4ecd22bc433164ccde4e95b5606bd900aa45dd46f58575b755e0c02f3c9c86
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_3D8D38C9123CD051:
    syscalls: *id077
    rule_version:
      id: LTP_3D8D38C9123CD051
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:3d8d38c9123cd051af9092607d45a62f55164808924a0eb549f9224f1dfcb486
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_3DE23AB4FE2FFC67:
    syscalls: *id078
    rule_version:
      id: LTP_3DE23AB4FE2FFC67
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:3de23ab4fe2ffc675ecd96acd034e98e5c50b8b059d547bd746e35859afcc4ba
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_3E526A0A23B5EF6D:
    syscalls: *id079
    rule_version:
      id: LTP_3E526A0A23B5EF6D
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:3e526a0a23b5ef6d666ef23c6f7fdef709d38709ea4ae271ba2352c150809881
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_3E8DA9E014B82702:
    syscalls: *id080
    rule_version:
      id: LTP_3E8DA9E014B82702
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:3e8da9e014b8270237da29d11e36cb3568c2b222d672973a5503c5d451873729
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有
      sys_alarm 入口。
  LTP_3F81436312777EF4:
    syscalls: *id081
    rule_version:
      id: LTP_3F81436312777EF4
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:3f81436312777ef415faf7797d673dd462cee3f00903f2610d05eb93291b67c4
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_401D471D37C85820:
    syscalls: *id082
    rule_version:
      id: LTP_401D471D37C85820
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:401d471d37c85820189e45519e765d1c0fdf65134cf15d25d8f1ef0009bc3408
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_45439D8F2BAB0832:
    syscalls: *id083
    rule_version:
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
    reason: 相关 Starry 内容指纹未变化，已跳过。
  LTP_461340ED83E7043D:
    syscalls: *id084
    rule_version:
      id: LTP_461340ED83E7043D
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:461340ed83e7043dea9542c2f07e235985dde3b81cc4c09f450b1c1df07be266
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 同一条件表达式被上游过度展开为 EINVAL 或 EPERM，且 BAD_USER_ADDRESS 前置条件与实际选择分支不一致，需复核。
  LTP_4661BBF1B3CD3A1E:
    syscalls: *id085
    rule_version: &id341
      id: LTP_4661BBF1B3CD3A1E
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:4661bbf1b3cd3a1ed9794183dd018046d195e23d06cfc4a8e2fa282fef66c737
    status: covered
    static_check_refs:
    - STARRY_ACCESS_PATH_RESOLUTION
    - STARRY_BATCH_ERRNO_TRANSLATION
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ACCESS_PATH_RESOLUTION:
          id: STARRY_ACCESS_PATH_RESOLUTION
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:896f2b8f806c19bafee558addd47df7692321be39551b0da996b9c942907a805
        STARRY_BATCH_ERRNO_TRANSLATION:
          id: STARRY_BATCH_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:e19f574ad1b857afc459fe1d55fbe4e71451eceeeeff1452ff74c6c7fec81a15
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: components/axfs-ng-vfs/src/path.rs
      symbols:
      - verify_entry_name
      scope: symbols
      file_hash: sha256:6e44a62c3142a5ebecb4c5c4c93f2d06c24ff549457c5c8b6787c8e90e46c11e
      symbol_hashes:
        verify_entry_name: sha256:516c7b090800149dc2bf3b7312761813844477a67da496c991099780f62c7ce5
      missing_symbols: []
      content_hash: sha256:2b2482c278ed782ee473d1a44f6611931e19f6b8db3edb22a40b3333d6bf50a0
    - path: components/starry-vm/src/alloc.rs
      symbols:
      - vm_load_until_nul
      scope: symbols
      file_hash: sha256:06b13f8c1700e024de6382919ddc0f8c2bf772798654a38d9e7f41c18ab2032e
      symbol_hashes:
        vm_load_until_nul: sha256:f65607e74fce137d86a282539ef80615a63582cf551668aa44115ed3b4e49767
      missing_symbols: []
      content_hash: sha256:8d542c4492f2dfe413baf6453ad0fd2edc7ac82a1ba69e9c16ca0f5a27bd691c
    - path: os/StarryOS/kernel/src/file/fs.rs
      symbols:
      - resolve_at
      scope: symbols
      file_hash: sha256:550e894d6abfbc7221d14420c4a3b9ed85ff072e792e108c2f8b7f8a6dceeefd
      symbol_hashes:
        resolve_at: sha256:ec9e7f57add9a1db10191664fd7c77c9236ea7f33e3df9b43ce8fd66ddc0a01f
      missing_symbols: []
      content_hash: sha256:b3dce20309fe9f480c0da78b10b6995550acae12ab1f7f9f348ac78ca0cebbe2
    - path: os/StarryOS/kernel/src/mm/access.rs
      symbols:
      - vm_load_path_string
      - vm_load_string
      scope: symbols
      file_hash: sha256:4c4fd8a5e5fdf74824fba2666041a10ff4daf9a0214bf6ddeabe8c9e67fc60a6
      symbol_hashes:
        vm_load_path_string: sha256:95f8b4926ce8e625750404ccab6b5faf51ebf398553aac30035185c0d56642f4
        vm_load_string: sha256:cee098cc352143ede741ebb982ba6d15f7eac71b6667871500b4a5ac4d42bb2e
      missing_symbols: []
      content_hash: sha256:f6fdd2214052ea5f56fef51f35d895763600c89e1aba847f54432d0346f2d3d4
    - path: os/StarryOS/kernel/src/syscall/fs/stat.rs
      symbols:
      - sys_access
      - sys_faccessat2
      scope: symbols
      file_hash: sha256:8c2b95c055a36e86b297489cffb8e9d0b4aee3d82941680f6abb9716f3fb2f8e
      symbol_hashes:
        sys_access: sha256:e53d5b954a3ef9ff58ed71b80472fb3f2b0ccaa44cb3004d725642a4a4689410
        sys_faccessat2: sha256:2b709c3ba051efeb9d68846547ada28d8b8cac5b8611e1be55b6fce8e6cab756
      missing_symbols: []
      content_hash: sha256:a54fce312aa6a1f336b085bc3620f03cb300748c4b561a5eef4e55d55de13ed0
    - path: os/arceos/modules/axfs-ng/src/fs_core/context.rs
      symbols:
      - resolve
      - resolve_inner
      - try_resolve_symlink
      scope: symbols
      file_hash: sha256:6cd56d9acec5dc2b33d0d931a4e147c7dcd13318fe706800a02503c2220f7204
      symbol_hashes:
        resolve: sha256:14a2b52408caa4b091a4b90ec30e6412155884199bbc592741da38777fc3581a
        resolve_inner: sha256:702d76c45f2ff1046f5d437d0e459366482b7ef2e76b1cfb259d536be7b52cc5
        try_resolve_symlink: sha256:2577319f282965c000834bd77c6fd7e1f77f7d44f10b688767d6391bab4169f3
      missing_symbols: []
      content_hash: sha256:0cf7ffc1f42cba981fa89780d918b03c47f71d465064f3e12b024bf39d071734
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_faccessat2 加载路径后调用 resolve_at/FsContext 路径解析；缺失项、非目录组件、符号链接循环和超长路径错误按 Linux errno 传播。
  LTP_46DE8D9AD1674F26:
    syscalls: *id086
    rule_version:
      id: LTP_46DE8D9AD1674F26
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:46de8d9ad1674f268ec5176d6c6112b3e667c7b9e884a397b395dc4f4202fba1
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_472AAA35C7382B26:
    syscalls: *id087
    rule_version:
      id: LTP_472AAA35C7382B26
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:472aaa35c7382b2636fefb76370c46d334f3c77cb0f9a4d38ae943f787a3b503
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 规则依赖 socket 类型、监听或连接队列、地址长度、用户指针以及 exp_errno 等运行时状态；现有静态分支无法唯一确定预期结果。
  LTP_479924116854D92B:
    syscalls: *id088
    rule_version:
      id: LTP_479924116854D92B
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:479924116854d92bd1d203df358cb1eb87571c84548d95311a60a2e5abc9e62a
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_48753F73ACA755FB:
    syscalls: *id089
    rule_version:
      id: LTP_48753F73ACA755FB
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:48753f73aca755fb980caaec98512bd04fdea8e9fd9793bfbd36d89e8f100a40
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_4881657CFE57C7E9:
    syscalls: *id090
    rule_version:
      id: LTP_4881657CFE57C7E9
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:4881657cfe57c7e9a906daa4e09474f24fe060c0fa11c4f8419f3f3b1d9843b8
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_492D25A0F1055F72:
    syscalls: *id091
    rule_version:
      id: LTP_492D25A0F1055F72
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:492d25a0f1055f7272707dc74d2909d60d3bfdb3bdbb276d8dfecd1ba98b2a61
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_4948E12FB8F9FA49:
    syscalls: *id092
    rule_version:
      id: LTP_4948E12FB8F9FA49
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:4948e12fb8f9fa49c261a472b9a2b88b7af3fee9ae5585b0be2d7735fbd49de8
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_49700CDA955B66D8:
    syscalls: *id093
    rule_version:
      id: LTP_49700CDA955B66D8
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:49700cda955b66d806729411debdf13891a8527551aaaa1af426c2ec7e472e8c
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_49A36559B96D24AF:
    syscalls: *id094
    rule_version:
      id: LTP_49A36559B96D24AF
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:49a36559b96d24af3d3ab1868328be5c985a250582334d715a8f40e00052d8c8
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_4B6E9B98E2E5103D:
    syscalls: *id095
    rule_version:
      id: LTP_4B6E9B98E2E5103D
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:4b6e9b98e2e5103df3d3c7a2359a60f35abd8fca0283c6630c38234ecf018a91
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_4CFAFCE7FCA2BF99:
    syscalls: *id096
    rule_version:
      id: LTP_4CFAFCE7FCA2BF99
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:4cfafce7fca2bf99656750383256c61ae565e76c1d4500ccb00d3d51cfeecf7d
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_4ECB786BFA071AAC:
    syscalls: *id097
    rule_version:
      id: LTP_4ECB786BFA071AAC
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:4ecb786bfa071aace1647cbe14be935db4f23e38eb6171a9ca1178bad37df0f0
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_50A86D4D5411356E:
    syscalls: *id098
    rule_version:
      id: LTP_50A86D4D5411356E
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:50a86d4d5411356ebcf10ffcdde2d209330522115285ebaf0d290c55611b93f1
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_50F858A3CBF95EED:
    syscalls: *id099
    rule_version:
      id: LTP_50F858A3CBF95EED
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:50f858a3cbf95eeddf59e035a757996bbd15f7d42379f5ea72330ceb0f3e6190
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: EPERM 依赖调用者权限状态；当前 sys_chroot 静态入口未显示相应 privilege gate，不能保守标为 covered。
  LTP_51E295101A9F4411:
    syscalls: *id100
    rule_version:
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
    reason: 相关 Starry 内容指纹未变化，已跳过。
  LTP_52BAFC01DEA6E172:
    syscalls: *id101
    rule_version:
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
    reason: 相关 Starry 内容指纹未变化，已跳过。
  LTP_52C209105EE62171:
    syscalls: *id102
    rule_version:
      id: LTP_52C209105EE62171
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:52c209105ee6217120690e4f8e29fb2a2eb681b601393f03d6536e8b14b1631d
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_5570480E7920BD0E:
    syscalls: *id103
    rule_version:
      id: LTP_5570480E7920BD0E
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:5570480e7920bd0ed29ec610cdd62bddf31a0d8c8de53cb937c27b58005abe0a
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_563FB650864E0DC6:
    syscalls: *id104
    rule_version:
      id: LTP_563FB650864E0DC6
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:563fb650864e0dc622844bcadcf468b2e11b289be993156a08b366bc3f4376d9
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_58416E6747519699:
    syscalls: *id105
    rule_version: &id342
      id: LTP_58416E6747519699
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:58416e6747519699e7b507fc0ff7e8c00852ff81eaff2cf425bb2d4a84e4e6f3
    status: covered
    static_check_refs:
    - STARRY_ACCESS_USER_POINTER
    - STARRY_BATCH_ERRNO_TRANSLATION
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ACCESS_USER_POINTER:
          id: STARRY_ACCESS_USER_POINTER
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:1df5a8a335cbf4e4f9bd77c4078ca8ef9f1a642feba46a2c79cea6aec66df23c
        STARRY_BATCH_ERRNO_TRANSLATION:
          id: STARRY_BATCH_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:e19f574ad1b857afc459fe1d55fbe4e71451eceeeeff1452ff74c6c7fec81a15
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: components/starry-vm/src/alloc.rs
      symbols:
      - vm_load_until_nul
      scope: symbols
      file_hash: sha256:06b13f8c1700e024de6382919ddc0f8c2bf772798654a38d9e7f41c18ab2032e
      symbol_hashes:
        vm_load_until_nul: sha256:f65607e74fce137d86a282539ef80615a63582cf551668aa44115ed3b4e49767
      missing_symbols: []
      content_hash: sha256:8d542c4492f2dfe413baf6453ad0fd2edc7ac82a1ba69e9c16ca0f5a27bd691c
    - path: os/StarryOS/kernel/src/file/fs.rs
      symbols:
      - resolve_at
      scope: symbols
      file_hash: sha256:550e894d6abfbc7221d14420c4a3b9ed85ff072e792e108c2f8b7f8a6dceeefd
      symbol_hashes:
        resolve_at: sha256:ec9e7f57add9a1db10191664fd7c77c9236ea7f33e3df9b43ce8fd66ddc0a01f
      missing_symbols: []
      content_hash: sha256:b3dce20309fe9f480c0da78b10b6995550acae12ab1f7f9f348ac78ca0cebbe2
    - path: os/StarryOS/kernel/src/mm/access.rs
      symbols:
      - vm_load_path_string
      - vm_load_string
      scope: symbols
      file_hash: sha256:4c4fd8a5e5fdf74824fba2666041a10ff4daf9a0214bf6ddeabe8c9e67fc60a6
      symbol_hashes:
        vm_load_path_string: sha256:95f8b4926ce8e625750404ccab6b5faf51ebf398553aac30035185c0d56642f4
        vm_load_string: sha256:cee098cc352143ede741ebb982ba6d15f7eac71b6667871500b4a5ac4d42bb2e
      missing_symbols: []
      content_hash: sha256:f6fdd2214052ea5f56fef51f35d895763600c89e1aba847f54432d0346f2d3d4
    - path: os/StarryOS/kernel/src/syscall/fs/stat.rs
      symbols:
      - sys_access
      - sys_faccessat2
      scope: symbols
      file_hash: sha256:8c2b95c055a36e86b297489cffb8e9d0b4aee3d82941680f6abb9716f3fb2f8e
      symbol_hashes:
        sys_access: sha256:e53d5b954a3ef9ff58ed71b80472fb3f2b0ccaa44cb3004d725642a4a4689410
        sys_faccessat2: sha256:2b709c3ba051efeb9d68846547ada28d8b8cac5b8611e1be55b6fce8e6cab756
      missing_symbols: []
      content_hash: sha256:a54fce312aa6a1f336b085bc3620f03cb300748c4b561a5eef4e55d55de13ed0
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_faccessat2 在路径解析前通过 vm_load_path_string 读取用户字符串；坏地址传播为 BadAddress，并由 errno 转换为 EFAULT。
  LTP_58F1512157A0052D:
    syscalls: *id106
    rule_version:
      id: LTP_58F1512157A0052D
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:58f1512157a0052d2af0ab1a834b768a94f0483ea6f6f5c904b75b63abe57a97
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_5A315335586D4227:
    syscalls: *id107
    rule_version:
      id: LTP_5A315335586D4227
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:5a315335586d4227dcb876b158bdf7ed73cd51dd9934c72a7a39852596d1f041
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_5C5CDC165410C08C:
    syscalls: *id108
    rule_version:
      id: LTP_5C5CDC165410C08C
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:5c5cdc165410c08c87ec34958aeb8662f2bd50738c79e7e54a3345227c6f463a
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_5CB803B873F78BA0:
    syscalls: *id109
    rule_version:
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
    reason: 相关 Starry 内容指纹未变化，已跳过。
  LTP_5CC44E5D1A6B6485:
    syscalls: *id110
    rule_version:
      id: LTP_5CC44E5D1A6B6485
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:5cc44e5d1a6b6485d58926a3e9b9aea6814a837393ae7b662a145a4ebbe567b5
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_5D7971086B2ABAE5:
    syscalls: *id111
    rule_version:
      id: LTP_5D7971086B2ABAE5
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:5d7971086b2abae59c5ba32908d196fe1ca3c05a91a71c6542a6b9fdaffb5081
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_5EC31E34822684C4:
    syscalls: *id112
    rule_version:
      id: LTP_5EC31E34822684C4
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:5ec31e34822684c4b7afef497aa177c327ce8cb8f1121ea1537865c2b63aa0e7
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_5F1D35ACCEFD4971:
    syscalls: *id113
    rule_version: &id343
      id: LTP_5F1D35ACCEFD4971
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:5f1d35accefd49711e3b8b82de258ecb2f04bba65083b919659edb660948ef2f
    status: covered
    static_check_refs:
    - STARRY_BATCH_ERRNO_TRANSLATION
    - STARRY_CAPGET_ABI
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_BATCH_ERRNO_TRANSLATION:
          id: STARRY_BATCH_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:e19f574ad1b857afc459fe1d55fbe4e71451eceeeeff1452ff74c6c7fec81a15
        STARRY_CAPGET_ABI:
          id: STARRY_CAPGET_ABI
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:9a7cf39c2be08e7a05c61f4ecfdb857e5ec45b702956c945d8c51b07cffde003
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: components/starry-vm/src/thin.rs
      symbols:
      - VmMutPtr
      - VmPtr
      scope: symbols
      file_hash: sha256:b787237758b16cc38fc20fa79234f62e2bad5d70235621818f9771c4a0810aa4
      symbol_hashes:
        VmMutPtr: sha256:35ae0c032d454211b5a4d3e0b11bf6bf854bd550d635855677666f26fb1f730a
        VmPtr: sha256:6c0ff10e65451fa76a4eb2caa472c0a96ff53459ae357d86f2dbf389f50e8804
      missing_symbols: []
      content_hash: sha256:1b7ca80cea190deec16a1cec479d83444169c6259f68ca0bf314edc58015fecd
    - path: os/StarryOS/kernel/src/syscall/task/ctl.rs
      symbols:
      - cap_data_from_cred
      - cred_for_pid
      - sys_capget
      - validate_cap_header
      scope: symbols
      file_hash: sha256:901fc111c7b58af132705a41cf8a75d89164f522f89135f794e08b76a1ec05e9
      symbol_hashes:
        cap_data_from_cred: sha256:12056db903d695b783e772fd520dafe507b7315b9a2f2581105a450c9d56884c
        cred_for_pid: sha256:5827d237893e92b1f7ac1cca89ee96df45f8bebd11d31d63dd76159e254674f8
        sys_capget: sha256:2d1bd6599456ea3fe4ff537c67fce4708ca32a841c6199426ddfda7997da1556
        validate_cap_header: sha256:f92b10dad6654ff4b7de228735357465447f4fc6010d9b0eb50afaae686cbf33
      missing_symbols: []
      content_hash: sha256:78191b3ad60afbde9d82f02ab40fc336efecdf1730cd04ce1b1052382fc2b197
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: capget 的 V3 header/data 用户指针均通过 VmPtr/VmMutPtr 访问；无效 header 或 data 地址传播 BadAddress，并转换为 EFAULT。
  LTP_606B7E40B6BD82EA:
    syscalls: *id114
    rule_version:
      id: LTP_606B7E40B6BD82EA
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:606b7e40b6bd82ea15aa8dc42049573d2f2e0e39e77a92d0dc58bc80badaeee0
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_613A5E121B4B6E68:
    syscalls: *id115
    rule_version:
      id: LTP_613A5E121B4B6E68
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:613a5e121b4b6e688b260c31b705088dbb0330e1a4d204c7887862f309bd6545
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_6156A09A2E506F76:
    syscalls: *id116
    rule_version:
      id: LTP_6156A09A2E506F76
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:6156a09a2e506f76240ecb425f3b0776cbea6dd2d63de09b41c67358f1f9dedc
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_6169F41023E00C34:
    syscalls: *id117
    rule_version:
      id: LTP_6169F41023E00C34
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:6169f41023e00c34d1fae4ccb616eda658fc6cfe7a778d1a84419931fc4eb99e
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_636590E5A017B28D:
    syscalls: *id118
    rule_version:
      id: LTP_636590E5A017B28D
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:636590e5a017b28de0d5d077ab1d9de84c4c96e13945c3e3d5dff4deca279ad5
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_64227C746913D03D:
    syscalls: *id119
    rule_version:
      id: LTP_64227C746913D03D
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:64227c746913d03d2fefb2a3d2cb8e5f8e7b91253bdf8c7e2d18422fd037d10d
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_6449E4A1D20C01D3:
    syscalls: *id120
    rule_version:
      id: LTP_6449E4A1D20C01D3
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:6449e4a1d20c01d34f2f8847a0e41c28dcb6b6515a24692cc3820005faedf3df
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有
      sys_alarm 入口。
  LTP_64A4E5DC71A633A2:
    syscalls: *id121
    rule_version:
      id: LTP_64A4E5DC71A633A2
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:64a4e5dc71a633a26922f41d72c3940a6ec6c25ac2b15d1ad00e035e51510fa8
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_65281FBEE0BF6103:
    syscalls: *id122
    rule_version:
      id: LTP_65281FBEE0BF6103
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:65281fbee0bf6103adf2a3ded2bfb3a308de839b6e7240c78d0714f21fa3e229
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_6580B4D3FA1A86F3:
    syscalls: *id123
    rule_version:
      id: LTP_6580B4D3FA1A86F3
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:6580b4d3fa1a86f3730217dbb09e8bb2bba0013f04002af419503eb90a22135a
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_65B70356F06E31F8:
    syscalls: *id124
    rule_version:
      id: LTP_65B70356F06E31F8
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:65b70356f06e31f852315fe3be36507e963aadb6d4dc164a7abe5194b80c9713
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有
      sys_alarm 入口。
  LTP_679436EC7A4E218A:
    syscalls: *id125
    rule_version:
      id: LTP_679436EC7A4E218A
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:679436ec7a4e218a139db19a8a9a2025de0bac1cec23502aecca28dbeafcccf9
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_67BF94A4ACD303C4:
    syscalls: *id126
    rule_version: &id344
      id: LTP_67BF94A4ACD303C4
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:67bf94a4acd303c4bf5ee873c38bf51c6656dd4b572784d258639f552e8c49d3
    status: covered
    static_check_refs:
    - STARRY_ACCESS_PERMISSIONS
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ACCESS_PERMISSIONS:
          id: STARRY_ACCESS_PERMISSIONS
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:9a2f8a7c6a97cb3e0bb0faa21d342b618172c583039ca74535fe0f394fa364bd
      dynamic_tests: {}
    target_dependencies:
    - path: os/StarryOS/kernel/src/file/fs.rs
      symbols:
      - resolve_at
      scope: symbols
      file_hash: sha256:550e894d6abfbc7221d14420c4a3b9ed85ff072e792e108c2f8b7f8a6dceeefd
      symbol_hashes:
        resolve_at: sha256:ec9e7f57add9a1db10191664fd7c77c9236ea7f33e3df9b43ce8fd66ddc0a01f
      missing_symbols: []
      content_hash: sha256:b3dce20309fe9f480c0da78b10b6995550acae12ab1f7f9f348ac78ca0cebbe2
    - path: os/StarryOS/kernel/src/syscall/fs/stat.rs
      symbols:
      - sys_access
      - sys_faccessat2
      scope: symbols
      file_hash: sha256:8c2b95c055a36e86b297489cffb8e9d0b4aee3d82941680f6abb9716f3fb2f8e
      symbol_hashes:
        sys_access: sha256:e53d5b954a3ef9ff58ed71b80472fb3f2b0ccaa44cb3004d725642a4a4689410
        sys_faccessat2: sha256:2b709c3ba051efeb9d68846547ada28d8b8cac5b8611e1be55b6fce8e6cab756
      missing_symbols: []
      content_hash: sha256:a54fce312aa6a1f336b085bc3620f03cb300748c4b561a5eef4e55d55de13ed0
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_access 委托 sys_faccessat2；F_OK 快速成功，并按 root 及 owner/group/other 有效权限位检查 R_OK、W_OK、X_OK，静态覆盖
      access02 权限案例。
  LTP_68745D21F4EC2FF5:
    syscalls: *id127
    rule_version:
      id: LTP_68745D21F4EC2FF5
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:68745d21f4ec2ff5b5e387fdccc54505aa949cca086e22d405cad28698ad929e
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_68E1B26815D97B79:
    syscalls: *id128
    rule_version:
      id: LTP_68E1B26815D97B79
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:68e1b26815d97b79837bdf0a750d5092b5453c48ea9fccb5caa09e08ac391d75
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_69077B093E81B570:
    syscalls: *id129
    rule_version:
      id: LTP_69077B093E81B570
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:69077b093e81b570fb4973707d5ca7f472fad9335fd22989875d94b6e3feaccc
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_690A651C3A60FC1E:
    syscalls: *id130
    rule_version:
      id: LTP_690A651C3A60FC1E
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:690a651c3a60fc1e3e0857388a189e20596da1430110654cea3df7d95cc8a8db
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_69E094D1DBFF3796:
    syscalls: *id131
    rule_version:
      id: LTP_69E094D1DBFF3796
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:69e094d1dbff37964143e4f6311f36c13c43cf505a51915529cdf47ea38780c9
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_6A1A431A08A3F450:
    syscalls: *id132
    rule_version:
      id: LTP_6A1A431A08A3F450
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:6a1a431a08a3f45047d6e8fa4396b2005af8a85c4b0a481ccd18de27a227ab17
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_6B1746F6BB2266CA:
    syscalls: *id133
    rule_version:
      id: LTP_6B1746F6BB2266CA
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:6b1746f6bb2266ca403fddd5b01714afb012e6190b76a167ec91965e3b307769
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_6B8B5453E8B4E6DE:
    syscalls: *id134
    rule_version:
      id: LTP_6B8B5453E8B4E6DE
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:6b8b5453e8b4e6de3c130b7bfd88e966870e4f5dd4be63541198db8f77332d12
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_6C11BBB4AABA6E7C:
    syscalls: *id135
    rule_version:
      id: LTP_6C11BBB4AABA6E7C
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:6c11bbb4aaba6e7c1ea9cc0299d3ec8157f958bf5001c8dfc4abe7f638f5b840
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_6C55A3E760DF75DB:
    syscalls: *id136
    rule_version:
      id: LTP_6C55A3E760DF75DB
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:6c55a3e760df75dbda4531dc00263c35e19b5544dd4f09efc00dfda935c00534
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_6CE9FC3BCA164B5D:
    syscalls: *id137
    rule_version:
      id: LTP_6CE9FC3BCA164B5D
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:6ce9fc3bca164b5d6aee07583208840f3f1c17c7d70a8f772b2a2946e1e0de2a
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_6D584CE6CF9B8A06:
    syscalls: *id138
    rule_version:
      id: LTP_6D584CE6CF9B8A06
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:6d584ce6cf9b8a06f26df1fde24935b1a38a763306a158a8ae4a2214fae60090
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_6D86AFD541A61388:
    syscalls: *id139
    rule_version: &id345
      id: LTP_6D86AFD541A61388
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:6d86afd541a613880ff94fbbb7fbfdbbebd5fd32d94544f7cc6e3f2ee850df77
    status: covered
    static_check_refs:
    - STARRY_BATCH_ERRNO_TRANSLATION
    - STARRY_CAPSET_ABI
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_BATCH_ERRNO_TRANSLATION:
          id: STARRY_BATCH_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:e19f574ad1b857afc459fe1d55fbe4e71451eceeeeff1452ff74c6c7fec81a15
        STARRY_CAPSET_ABI:
          id: STARRY_CAPSET_ABI
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:fa04e3f3a184e594c6b2b6f1f9d43027f9104bdc8a675eb3555d76e5cfb0faed
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: components/starry-vm/src/thin.rs
      symbols:
      - VmMutPtr
      - VmPtr
      scope: symbols
      file_hash: sha256:b787237758b16cc38fc20fa79234f62e2bad5d70235621818f9771c4a0810aa4
      symbol_hashes:
        VmMutPtr: sha256:35ae0c032d454211b5a4d3e0b11bf6bf854bd550d635855677666f26fb1f730a
        VmPtr: sha256:6c0ff10e65451fa76a4eb2caa472c0a96ff53459ae357d86f2dbf389f50e8804
      missing_symbols: []
      content_hash: sha256:1b7ca80cea190deec16a1cec479d83444169c6259f68ca0bf314edc58015fecd
    - path: os/StarryOS/kernel/src/syscall/task/ctl.rs
      symbols:
      - data_to_mask
      - sys_capset
      - validate_cap_header
      scope: symbols
      file_hash: sha256:901fc111c7b58af132705a41cf8a75d89164f522f89135f794e08b76a1ec05e9
      symbol_hashes:
        data_to_mask: sha256:83fc2bb0eb44d7806a59c49b19d8600aadfdbe3b4e893514102d99611ad985ff
        sys_capset: sha256:3e17536f5a7319b1ad18a17d39c88b715d8795162ccc1860d59845494d69265c
        validate_cap_header: sha256:f92b10dad6654ff4b7de228735357465447f4fc6010d9b0eb50afaae686cbf33
      missing_symbols: []
      content_hash: sha256:df372a3e9f4e00850aad57aaee664224ee6a290029e828efea476bb40d9b46a5
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: capset 在修改凭据前通过 VmPtr 读取 V3 header/data；无效 header 或 data 地址传播 BadAddress，并转换为 EFAULT。
  LTP_6EF7ECD2A8470CEA:
    syscalls: *id140
    rule_version:
      id: LTP_6EF7ECD2A8470CEA
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:6ef7ecd2a8470cea5b90e0cc9e2b7679b9ee2a73a4810b11d35520dcd1a6ac3c
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_711D5693356A79F2:
    syscalls: *id141
    rule_version: &id346
      id: LTP_711D5693356A79F2
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:711d5693356a79f2f78c29dc066b0de731afab838d59939646e4e7b1b2e98a60
    status: covered
    static_check_refs:
    - STARRY_ACCESS_PERMISSIONS
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ACCESS_PERMISSIONS:
          id: STARRY_ACCESS_PERMISSIONS
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:9a2f8a7c6a97cb3e0bb0faa21d342b618172c583039ca74535fe0f394fa364bd
      dynamic_tests: {}
    target_dependencies:
    - path: os/StarryOS/kernel/src/file/fs.rs
      symbols:
      - resolve_at
      scope: symbols
      file_hash: sha256:550e894d6abfbc7221d14420c4a3b9ed85ff072e792e108c2f8b7f8a6dceeefd
      symbol_hashes:
        resolve_at: sha256:ec9e7f57add9a1db10191664fd7c77c9236ea7f33e3df9b43ce8fd66ddc0a01f
      missing_symbols: []
      content_hash: sha256:b3dce20309fe9f480c0da78b10b6995550acae12ab1f7f9f348ac78ca0cebbe2
    - path: os/StarryOS/kernel/src/syscall/fs/stat.rs
      symbols:
      - sys_access
      - sys_faccessat2
      scope: symbols
      file_hash: sha256:8c2b95c055a36e86b297489cffb8e9d0b4aee3d82941680f6abb9716f3fb2f8e
      symbol_hashes:
        sys_access: sha256:e53d5b954a3ef9ff58ed71b80472fb3f2b0ccaa44cb3004d725642a4a4689410
        sys_faccessat2: sha256:2b709c3ba051efeb9d68846547ada28d8b8cac5b8611e1be55b6fce8e6cab756
      missing_symbols: []
      content_hash: sha256:a54fce312aa6a1f336b085bc3620f03cb300748c4b561a5eef4e55d55de13ed0
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_access 委托 sys_faccessat2；F_OK 快速成功，并按 root 及 owner/group/other 有效权限位检查 R_OK、W_OK、X_OK，静态覆盖
      access02 权限案例。
  LTP_71C54C624831C7F0:
    syscalls: *id142
    rule_version: &id347
      id: LTP_71C54C624831C7F0
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:71c54c624831c7f01c5ac8d48046dc370b784af8dc2099633843d4269593e9f7
    status: covered
    static_check_refs:
    - STARRY_BATCH_ERRNO_TRANSLATION
    - STARRY_CHROOT_PATH
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_BATCH_ERRNO_TRANSLATION:
          id: STARRY_BATCH_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:e19f574ad1b857afc459fe1d55fbe4e71451eceeeeff1452ff74c6c7fec81a15
        STARRY_CHROOT_PATH:
          id: STARRY_CHROOT_PATH
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:357fbab1f149ef6fb3807966810bffa3366973f2c4f2c854bb821004e4a3753f
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: components/axfs-ng-vfs/src/path.rs
      symbols:
      - verify_entry_name
      scope: symbols
      file_hash: sha256:6e44a62c3142a5ebecb4c5c4c93f2d06c24ff549457c5c8b6787c8e90e46c11e
      symbol_hashes:
        verify_entry_name: sha256:516c7b090800149dc2bf3b7312761813844477a67da496c991099780f62c7ce5
      missing_symbols: []
      content_hash: sha256:2b2482c278ed782ee473d1a44f6611931e19f6b8db3edb22a40b3333d6bf50a0
    - path: components/starry-vm/src/alloc.rs
      symbols:
      - vm_load_until_nul
      scope: symbols
      file_hash: sha256:06b13f8c1700e024de6382919ddc0f8c2bf772798654a38d9e7f41c18ab2032e
      symbol_hashes:
        vm_load_until_nul: sha256:f65607e74fce137d86a282539ef80615a63582cf551668aa44115ed3b4e49767
      missing_symbols: []
      content_hash: sha256:8d542c4492f2dfe413baf6453ad0fd2edc7ac82a1ba69e9c16ca0f5a27bd691c
    - path: os/StarryOS/kernel/src/mm/access.rs
      symbols:
      - vm_load_string
      scope: symbols
      file_hash: sha256:4c4fd8a5e5fdf74824fba2666041a10ff4daf9a0214bf6ddeabe8c9e67fc60a6
      symbol_hashes:
        vm_load_string: sha256:cee098cc352143ede741ebb982ba6d15f7eac71b6667871500b4a5ac4d42bb2e
      missing_symbols: []
      content_hash: sha256:e17a288c5843ae74a5c3e12ef6048c2572a8793b06467613638d615ffc385958
    - path: os/StarryOS/kernel/src/syscall/fs/ctl.rs
      symbols:
      - sys_chroot
      scope: symbols
      file_hash: sha256:a42d57fc2422560978476f017ea2ae3d59e59be8c3f119e45fb5f18529d2e7e5
      symbol_hashes:
        sys_chroot: sha256:2445750c1d3c822f8438f9a1914fe47b5360157364ca20142ad673492d889756
      missing_symbols: []
      content_hash: sha256:928d58e7292bc7e8922d1000e5aabe85e9fdb3f1f6c3f84b52583584b92d0d55
    - path: os/arceos/modules/axfs-ng/src/fs_core/context.rs
      symbols:
      - new
      - resolve
      - resolve_inner
      - try_resolve_symlink
      scope: symbols
      file_hash: sha256:6cd56d9acec5dc2b33d0d931a4e147c7dcd13318fe706800a02503c2220f7204
      symbol_hashes:
        new: sha256:3d17bd68745b169b5dbdd92e4dae5756b1d41e3850eea66a0cf7be91f1c551b2
        resolve: sha256:14a2b52408caa4b091a4b90ec30e6412155884199bbc592741da38777fc3581a
        resolve_inner: sha256:702d76c45f2ff1046f5d437d0e459366482b7ef2e76b1cfb259d536be7b52cc5
        try_resolve_symlink: sha256:2577319f282965c000834bd77c6fd7e1f77f7d44f10b688767d6391bab4169f3
      missing_symbols: []
      content_hash: sha256:955067eb239a31c67297a10606806cadf346d537ebd469118db448e88e52f236
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_chroot 先读取用户路径，再经 FsContext 解析并要求目标为目录；路径读取或解析错误及 ENOTDIR 由 errno 层保真转换。
  LTP_73DF50509BCC128B:
    syscalls: *id143
    rule_version: &id348
      id: LTP_73DF50509BCC128B
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:73df50509bcc128b1b669bc1dbf328da4c2eeccbf411699638eea46f6a5ffbe5
    status: covered
    static_check_refs:
    - STARRY_ACCESS_PERMISSIONS
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ACCESS_PERMISSIONS:
          id: STARRY_ACCESS_PERMISSIONS
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:9a2f8a7c6a97cb3e0bb0faa21d342b618172c583039ca74535fe0f394fa364bd
      dynamic_tests: {}
    target_dependencies:
    - path: os/StarryOS/kernel/src/file/fs.rs
      symbols:
      - resolve_at
      scope: symbols
      file_hash: sha256:550e894d6abfbc7221d14420c4a3b9ed85ff072e792e108c2f8b7f8a6dceeefd
      symbol_hashes:
        resolve_at: sha256:ec9e7f57add9a1db10191664fd7c77c9236ea7f33e3df9b43ce8fd66ddc0a01f
      missing_symbols: []
      content_hash: sha256:b3dce20309fe9f480c0da78b10b6995550acae12ab1f7f9f348ac78ca0cebbe2
    - path: os/StarryOS/kernel/src/syscall/fs/stat.rs
      symbols:
      - sys_access
      - sys_faccessat2
      scope: symbols
      file_hash: sha256:8c2b95c055a36e86b297489cffb8e9d0b4aee3d82941680f6abb9716f3fb2f8e
      symbol_hashes:
        sys_access: sha256:e53d5b954a3ef9ff58ed71b80472fb3f2b0ccaa44cb3004d725642a4a4689410
        sys_faccessat2: sha256:2b709c3ba051efeb9d68846547ada28d8b8cac5b8611e1be55b6fce8e6cab756
      missing_symbols: []
      content_hash: sha256:a54fce312aa6a1f336b085bc3620f03cb300748c4b561a5eef4e55d55de13ed0
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_access 委托 sys_faccessat2；F_OK 快速成功，并按 root 及 owner/group/other 有效权限位检查 R_OK、W_OK、X_OK，静态覆盖
      access02 权限案例。
  LTP_74819A9DC2B5CB06:
    syscalls: *id144
    rule_version:
      id: LTP_74819A9DC2B5CB06
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:74819a9dc2b5cb06be87f7b24448f78e14019190b6eafc94c1a59aca379084e1
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_752C9A802CF96B8B:
    syscalls: *id145
    rule_version:
      id: LTP_752C9A802CF96B8B
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:752c9a802cf96b8be139bd7098d3505b2ec3c75804887a275c9d4ebf1ae13455
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_76A9B6CF388A8609:
    syscalls: *id146
    rule_version:
      id: LTP_76A9B6CF388A8609
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:76a9b6cf388a8609eeb2a9e479fa27419ade916ce166ad5c0e8255aa5f4497d5
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有
      sys_alarm 入口。
  LTP_78EEEBE648781151:
    syscalls: *id147
    rule_version:
      id: LTP_78EEEBE648781151
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:78eeebe648781151021a0c09a77d9afad8055cb7b1d1b7b1f683af71e8dcf006
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_791DEA825D66980B:
    syscalls: *id148
    rule_version:
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
    reason: 相关 Starry 内容指纹未变化，已跳过。
  LTP_7963C3DF373596FE:
    syscalls: *id149
    rule_version:
      id: LTP_7963C3DF373596FE
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:7963c3df373596fe8332b3428b9eb575d21649abff2f42a2acedfb92b5974614
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_79C7516DECB19092:
    syscalls: *id150
    rule_version:
      id: LTP_79C7516DECB19092
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:79c7516decb190926a1a2da50f2739a169f2c4324ba156756aaa688f27172579
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_7A02B34D5FB8BBC3:
    syscalls: *id151
    rule_version:
      id: LTP_7A02B34D5FB8BBC3
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:7a02b34d5fb8bbc34f9815aabc5fc09dcedf0e626a1a49ba2adcb9bdab42bf59
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_7A74A699442CEB99:
    syscalls: *id152
    rule_version: &id349
      id: LTP_7A74A699442CEB99
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:7a74a699442ceb99b8495ac52144744c5a7e995035d4c06a10971ce532e8e954
    status: covered
    static_check_refs:
    - STARRY_BRK_HEAP
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_BRK_HEAP:
          id: STARRY_BRK_HEAP
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:08b3a24f292c0c2d933bf711c00c866ab3a74a54f291c4ddee9460d0eb6f43ac
      dynamic_tests: {}
    target_dependencies:
    - path: os/StarryOS/kernel/src/config/aarch64.rs
      symbols:
      - USER_HEAP_BASE
      - USER_HEAP_SIZE
      - USER_HEAP_SIZE_MAX
      scope: symbols
      file_hash: sha256:774155d8f1f08322a6707b4d09bcf2a68f5e882a65a7d72ff85b710d6834f201
      symbol_hashes:
        USER_HEAP_BASE: sha256:3ff8ee7d59885899912f42f724f3ab4aff6b34eda021d151e63c73e755caba3a
        USER_HEAP_SIZE: sha256:e150df3dfceba2739ace567435f441463c73cae24c07bd13311a3028286047c0
        USER_HEAP_SIZE_MAX: sha256:0cb8ac49063245c704178c4fceaa4490ce7d5d0369d2dd4d54a9a6a85d5a76c5
      missing_symbols: []
      content_hash: sha256:27fb22b5143847b13f436852fae29eec4df662361abbed0dcf1c052edf34722d
    - path: os/StarryOS/kernel/src/config/loongarch64.rs
      symbols:
      - USER_HEAP_BASE
      - USER_HEAP_SIZE
      - USER_HEAP_SIZE_MAX
      scope: symbols
      file_hash: sha256:74d8dc131109414b9cf80d5f2c6a0bb225a3a8d45a23c97dd8d31e51352cc694
      symbol_hashes:
        USER_HEAP_BASE: sha256:3ff8ee7d59885899912f42f724f3ab4aff6b34eda021d151e63c73e755caba3a
        USER_HEAP_SIZE: sha256:ffd1ad4365175a3bbcae5439e6ce7f26fbcc5b061b2850249a2287a252a68fda
        USER_HEAP_SIZE_MAX: sha256:fde7d3be05b0a123ec2663c6de2ee373ad6ab79d0f93f381d0140a6c4a493ff3
      missing_symbols: []
      content_hash: sha256:451c35f9f88bab1994e49b6c0870759e07eec1536c4bd75ec6709bb53639e78a
    - path: os/StarryOS/kernel/src/config/riscv64.rs
      symbols:
      - USER_HEAP_BASE
      - USER_HEAP_SIZE
      - USER_HEAP_SIZE_MAX
      scope: symbols
      file_hash: sha256:9b0ab32999b12ab2dbf7446a00545bf2a5c54d32f2c42c8382c0fac880443d58
      symbol_hashes:
        USER_HEAP_BASE: sha256:3ff8ee7d59885899912f42f724f3ab4aff6b34eda021d151e63c73e755caba3a
        USER_HEAP_SIZE: sha256:e150df3dfceba2739ace567435f441463c73cae24c07bd13311a3028286047c0
        USER_HEAP_SIZE_MAX: sha256:0cb8ac49063245c704178c4fceaa4490ce7d5d0369d2dd4d54a9a6a85d5a76c5
      missing_symbols: []
      content_hash: sha256:691d052a0f2d35b9d7b80c716b4f555fd17f01e7699433f163ceddad9623c334
    - path: os/StarryOS/kernel/src/config/x86_64.rs
      symbols:
      - USER_HEAP_BASE
      - USER_HEAP_SIZE
      - USER_HEAP_SIZE_MAX
      scope: symbols
      file_hash: sha256:5d2084f2ec16168c78b7fc3784faafb11a2738e52a4bd258068226ac55f0de88
      symbol_hashes:
        USER_HEAP_BASE: sha256:3ff8ee7d59885899912f42f724f3ab4aff6b34eda021d151e63c73e755caba3a
        USER_HEAP_SIZE: sha256:e150df3dfceba2739ace567435f441463c73cae24c07bd13311a3028286047c0
        USER_HEAP_SIZE_MAX: sha256:0cb8ac49063245c704178c4fceaa4490ce7d5d0369d2dd4d54a9a6a85d5a76c5
      missing_symbols: []
      content_hash: sha256:5520eed745a5d7a3f18da1bfc694111642821921d9476dfb16509b914da2262c
    - path: os/StarryOS/kernel/src/syscall/mm/brk.rs
      symbols:
      - sys_brk
      scope: symbols
      file_hash: sha256:235d73dad5117170ec322a42e0afb92edc703c335955af67ab203be685da070e
      symbol_hashes:
        sys_brk: sha256:65291f8268e25c9a6f2f7a7b6c2e40a97217a6fe0c8973c124db5f97dae6f1de
      missing_symbols: []
      content_hash: sha256:adf14b11828ae345ae531b93973cfee0bd9dbcf652999b84120e0125d27cdd9c
    - path: os/StarryOS/kernel/src/task/mod.rs
      symbols:
      - get_heap_top
      - set_heap_top
      scope: symbols
      file_hash: sha256:270ce7a86e57c31a8018300d905443254ecca9994148a7c5a55d18461b7fb0f7
      symbol_hashes:
        get_heap_top: sha256:fa0326839ec0b84758dfc98aab0ba7190fa38250da9e7e672a767cc64315b497
        set_heap_top: sha256:81791179ed6d16e014cc944d4c3193d1f124392d3a3691bf3aac93fb2423ebd3
      missing_symbols: []
      content_hash: sha256:0d36d97cc64136b5d97afed8b1e0036b0e91fdba3381fafcac8c97ea3f978104
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_brk 校验 heap 地址范围和 RLIMIT_DATA，按需映射或解除映射，成功后更新 heap_top 并返回新 break。
  LTP_7B539E14354153DC:
    syscalls: *id153
    rule_version:
      id: LTP_7B539E14354153DC
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:7b539e14354153dc3ae771f14249d899686d09a8132779a15400fe4c7a359fb5
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_7BE2877017694C52:
    syscalls: *id154
    rule_version:
      id: LTP_7BE2877017694C52
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:7be2877017694c5297ea1899a6340f60f45a0512564dc9b803cbeb7f07fcaa89
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_7C06A3394E786948:
    syscalls: *id155
    rule_version:
      id: LTP_7C06A3394E786948
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:7c06a3394e786948b987283ad4350d0fd11b7db40268400f52981a70f7e06cf2
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_7CE7876CE69F200F:
    syscalls: *id156
    rule_version:
      id: LTP_7CE7876CE69F200F
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:7ce7876ce69f200f75ab85c56b4a20b71739e4f3e623447c863f83810e8dc4bc
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_7DD493976CBC9A31:
    syscalls: *id157
    rule_version:
      id: LTP_7DD493976CBC9A31
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:7dd493976cbc9a31473f659f5104974cd1f19ce54d0dd6847b171a289fcbdb76
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_7DEDC53AC33C891F:
    syscalls: *id158
    rule_version:
      id: LTP_7DEDC53AC33C891F
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:7dedc53ac33c891f5dc26a9f6c36be055e5347807fd55cc59f6800da4424f720
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 同一条件表达式被上游过度展开为 EINVAL 或 EPERM，且 BAD_USER_ADDRESS 前置条件与实际选择分支不一致，需复核。
  LTP_7F5487EEB79017AD:
    syscalls: *id159
    rule_version:
      id: LTP_7F5487EEB79017AD
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:7f5487eeb79017ad484481316be8234c05efc4d1c9a9a69f4b7d0f4be0d60e1d
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_7F54F9DFF7E0FB61:
    syscalls: *id160
    rule_version:
      id: LTP_7F54F9DFF7E0FB61
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:7f54f9dff7e0fb6182a763a2155d163534cba4c20aa5919950393fe49e309c79
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_7FD6142E0E88CF17:
    syscalls: *id161
    rule_version:
      id: LTP_7FD6142E0E88CF17
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:7fd6142e0e88cf177fb735c36d08a2ed91ecc3830a60463895683ff3383da791
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::cachestat 分派分支，syscall 实现目录中也没有
      sys_cachestat 入口。
  LTP_8059D9227293D592:
    syscalls: *id162
    rule_version:
      id: LTP_8059D9227293D592
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:8059d9227293d5924f8d626f9d7208df6934b80434c0edd2d718815624c9c2f9
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_807E2072E5694684:
    syscalls: *id163
    rule_version:
      id: LTP_807E2072E5694684
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:807e2072e56946843ec26008205fe1d23b12d9ed133587a34c433e599d98bd49
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_80C6DB0ACB2A5510:
    syscalls: *id164
    rule_version:
      id: LTP_80C6DB0ACB2A5510
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:80c6db0acb2a5510899328ccf5897d7e8d2a652d48a8013d682918b68813a993
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 规则依赖 socket 类型、监听或连接队列、地址长度、用户指针以及 exp_errno 等运行时状态；现有静态分支无法唯一确定预期结果。
  LTP_818BA624CA9E4040:
    syscalls: *id165
    rule_version:
      id: LTP_818BA624CA9E4040
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:818ba624ca9e40408248bf312cf020f05d886c3623be5fc0719d46a9ac849b1c
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_820495EA1D1F15DA:
    syscalls: *id166
    rule_version:
      id: LTP_820495EA1D1F15DA
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:820495ea1d1f15da0bb46f02de41635a1d1e07db2a82d6be42d7d22bf34b5513
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_82621B02FCA09F40:
    syscalls: *id167
    rule_version:
      id: LTP_82621B02FCA09F40
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:82621b02fca09f40310757b7ff831c290f08ab01be6a5ea4bc4c74ce2db492cd
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有
      sys_alarm 入口。
  LTP_827CE5CB448A411B:
    syscalls: *id168
    rule_version: &id350
      id: LTP_827CE5CB448A411B
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:827ce5cb448a411bcd82f3a89e9c733eb11fa4d44a8f563ff1658dac81bd73a4
    status: covered
    static_check_refs:
    - STARRY_BATCH_ERRNO_TRANSLATION
    - STARRY_CAPGET_ABI
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_BATCH_ERRNO_TRANSLATION:
          id: STARRY_BATCH_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:e19f574ad1b857afc459fe1d55fbe4e71451eceeeeff1452ff74c6c7fec81a15
        STARRY_CAPGET_ABI:
          id: STARRY_CAPGET_ABI
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:9a7cf39c2be08e7a05c61f4ecfdb857e5ec45b702956c945d8c51b07cffde003
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: components/starry-vm/src/thin.rs
      symbols:
      - VmMutPtr
      - VmPtr
      scope: symbols
      file_hash: sha256:b787237758b16cc38fc20fa79234f62e2bad5d70235621818f9771c4a0810aa4
      symbol_hashes:
        VmMutPtr: sha256:35ae0c032d454211b5a4d3e0b11bf6bf854bd550d635855677666f26fb1f730a
        VmPtr: sha256:6c0ff10e65451fa76a4eb2caa472c0a96ff53459ae357d86f2dbf389f50e8804
      missing_symbols: []
      content_hash: sha256:1b7ca80cea190deec16a1cec479d83444169c6259f68ca0bf314edc58015fecd
    - path: os/StarryOS/kernel/src/syscall/task/ctl.rs
      symbols:
      - cap_data_from_cred
      - cred_for_pid
      - sys_capget
      - validate_cap_header
      scope: symbols
      file_hash: sha256:901fc111c7b58af132705a41cf8a75d89164f522f89135f794e08b76a1ec05e9
      symbol_hashes:
        cap_data_from_cred: sha256:12056db903d695b783e772fd520dafe507b7315b9a2f2581105a450c9d56884c
        cred_for_pid: sha256:5827d237893e92b1f7ac1cca89ee96df45f8bebd11d31d63dd76159e254674f8
        sys_capget: sha256:2d1bd6599456ea3fe4ff537c67fce4708ca32a841c6199426ddfda7997da1556
        validate_cap_header: sha256:f92b10dad6654ff4b7de228735357465447f4fc6010d9b0eb50afaae686cbf33
      missing_symbols: []
      content_hash: sha256:78191b3ad60afbde9d82f02ab40fc336efecdf1730cd04ce1b1052382fc2b197
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: capget 的 V3 header/data 用户指针均通过 VmPtr/VmMutPtr 访问；无效 header 或 data 地址传播 BadAddress，并转换为 EFAULT。
  LTP_82ABB8FBFA06D356:
    syscalls: *id169
    rule_version:
      id: LTP_82ABB8FBFA06D356
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:82abb8fbfa06d356d166904600f5775ae65964f9dd69ff871508d0394f0a9135
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_82E0F55AEC3D382F:
    syscalls: *id170
    rule_version:
      id: LTP_82E0F55AEC3D382F
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:82e0f55aec3d382ffc129f4f165173a13c4dcdfd664c20edcdfde08730d35547
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 预期 EROFS 来自上游错误结果反向解析，但规则没有记录只读挂载前置条件；Starry access 路径不足以证明该 errno。
  LTP_830E17210B1FB7AB:
    syscalls: *id171
    rule_version:
      id: LTP_830E17210B1FB7AB
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:830e17210b1fb7ab64b2c08aeb681deb05e66d772e2f30106aedad74766c5a07
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_833C5D5CF3C32C2A:
    syscalls: *id172
    rule_version:
      id: LTP_833C5D5CF3C32C2A
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:833c5d5cf3c32c2ad68b674f024e317ad3f2077e9750dbe97ace078129de90b3
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_839EC7BC904E42D5:
    syscalls: *id173
    rule_version: &id351
      id: LTP_839EC7BC904E42D5
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:839ec7bc904e42d51fd03abcb0ea65b5030acf961067619e228750577be93c2f
    status: covered
    static_check_refs:
    - STARRY_ACCESS_PERMISSIONS
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ACCESS_PERMISSIONS:
          id: STARRY_ACCESS_PERMISSIONS
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:9a2f8a7c6a97cb3e0bb0faa21d342b618172c583039ca74535fe0f394fa364bd
      dynamic_tests: {}
    target_dependencies:
    - path: os/StarryOS/kernel/src/file/fs.rs
      symbols:
      - resolve_at
      scope: symbols
      file_hash: sha256:550e894d6abfbc7221d14420c4a3b9ed85ff072e792e108c2f8b7f8a6dceeefd
      symbol_hashes:
        resolve_at: sha256:ec9e7f57add9a1db10191664fd7c77c9236ea7f33e3df9b43ce8fd66ddc0a01f
      missing_symbols: []
      content_hash: sha256:b3dce20309fe9f480c0da78b10b6995550acae12ab1f7f9f348ac78ca0cebbe2
    - path: os/StarryOS/kernel/src/syscall/fs/stat.rs
      symbols:
      - sys_access
      - sys_faccessat2
      scope: symbols
      file_hash: sha256:8c2b95c055a36e86b297489cffb8e9d0b4aee3d82941680f6abb9716f3fb2f8e
      symbol_hashes:
        sys_access: sha256:e53d5b954a3ef9ff58ed71b80472fb3f2b0ccaa44cb3004d725642a4a4689410
        sys_faccessat2: sha256:2b709c3ba051efeb9d68846547ada28d8b8cac5b8611e1be55b6fce8e6cab756
      missing_symbols: []
      content_hash: sha256:a54fce312aa6a1f336b085bc3620f03cb300748c4b561a5eef4e55d55de13ed0
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_access 委托 sys_faccessat2；F_OK 快速成功，并按 root 及 owner/group/other 有效权限位检查 R_OK、W_OK、X_OK，静态覆盖
      access02 权限案例。
  LTP_843BDD20FF921FC3:
    syscalls: *id174
    rule_version:
      id: LTP_843BDD20FF921FC3
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:843bdd20ff921fc332b61339ab9d496555389281619a41dd01b5fa3075040459
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_84E4CC971DD16EC2:
    syscalls: *id175
    rule_version:
      id: LTP_84E4CC971DD16EC2
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:84e4cc971dd16ec2911aa117be814cd39fd921938b6295e00affa123c89207ed
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_853D34D061DDE8F8:
    syscalls: *id176
    rule_version:
      id: LTP_853D34D061DDE8F8
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:853d34d061dde8f86af4431c77852b00c74651f8900db51dc635601cc3d95627
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_853F4B8346648EB9:
    syscalls: *id177
    rule_version:
      id: LTP_853F4B8346648EB9
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:853f4b8346648eb95326d22c8b7bfcf811114a18d54f8f90a057977525c63035
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_857DC6AD01A88D79:
    syscalls: *id178
    rule_version:
      id: LTP_857DC6AD01A88D79
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:857dc6ad01a88d79902a011999f867680c9330ce6c8e5ad503fdd5e6f6389647
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_87478A6C3AC7DC60:
    syscalls: *id179
    rule_version:
      id: LTP_87478A6C3AC7DC60
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:87478a6c3ac7dc608c2eb8e482206b447ae2b1ca6e6a46d5997786f65d847b5b
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_884775F9076E54AB:
    syscalls: *id180
    rule_version:
      id: LTP_884775F9076E54AB
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:884775f9076e54ab6b97c1e3384fe1d180e81896a267336db0df25740c24b57d
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_885F3BA721198C07:
    syscalls: *id181
    rule_version:
      id: LTP_885F3BA721198C07
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:885f3ba721198c07a6615546d3d5161fb126683dbde6e45cac3e768801969348
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_88F6F279E33633DE:
    syscalls: *id182
    rule_version:
      id: LTP_88F6F279E33633DE
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:88f6f279e33633de3f1ef93d7a2345db4c160c5c4b7b2168cac5bc697d415b00
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_89C9E8458EC38C11:
    syscalls: *id183
    rule_version:
      id: LTP_89C9E8458EC38C11
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:89c9e8458ec38c1192fb6eeb76cdcd58fc7b36e08a155e776975b94da2abf980
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::cachestat 分派分支，syscall 实现目录中也没有
      sys_cachestat 入口。
  LTP_8AC11633EA3D83E0:
    syscalls: *id184
    rule_version:
      id: LTP_8AC11633EA3D83E0
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:8ac11633ea3d83e09f4781cae55d25c2bd9319aa1786100063e7e8a24f836492
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_8AD8032754BC8842:
    syscalls: *id185
    rule_version:
      id: LTP_8AD8032754BC8842
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:8ad8032754bc8842e1ceffe416a3d559f5423eec53ec7db46ee81a6eeba25869
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::cacheflush 分派分支，syscall 实现目录中也没有
      sys_cacheflush 入口。
  LTP_8B1A2084BCF096F1:
    syscalls: *id186
    rule_version:
      id: LTP_8B1A2084BCF096F1
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:8b1a2084bcf096f1404d2038c5488359f3de9a3382f8f36d18f1967ea461aad1
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_8B3FBDFD0453EF40:
    syscalls: *id187
    rule_version:
      id: LTP_8B3FBDFD0453EF40
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:8b3fbdfd0453ef405a15e797169e7cc53f5017abb0ad514ada404741cad4b747
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_8BB576EB2E1E6B23:
    syscalls: *id188
    rule_version: &id352
      id: LTP_8BB576EB2E1E6B23
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:8bb576eb2e1e6b23ecfe5c8b7d2bb21eb7fba161f200ce874a6282e806ee9180
    status: covered
    static_check_refs:
    - STARRY_ACCESS_PATH_RESOLUTION
    - STARRY_BATCH_ERRNO_TRANSLATION
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ACCESS_PATH_RESOLUTION:
          id: STARRY_ACCESS_PATH_RESOLUTION
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:896f2b8f806c19bafee558addd47df7692321be39551b0da996b9c942907a805
        STARRY_BATCH_ERRNO_TRANSLATION:
          id: STARRY_BATCH_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:e19f574ad1b857afc459fe1d55fbe4e71451eceeeeff1452ff74c6c7fec81a15
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: components/axfs-ng-vfs/src/path.rs
      symbols:
      - verify_entry_name
      scope: symbols
      file_hash: sha256:6e44a62c3142a5ebecb4c5c4c93f2d06c24ff549457c5c8b6787c8e90e46c11e
      symbol_hashes:
        verify_entry_name: sha256:516c7b090800149dc2bf3b7312761813844477a67da496c991099780f62c7ce5
      missing_symbols: []
      content_hash: sha256:2b2482c278ed782ee473d1a44f6611931e19f6b8db3edb22a40b3333d6bf50a0
    - path: components/starry-vm/src/alloc.rs
      symbols:
      - vm_load_until_nul
      scope: symbols
      file_hash: sha256:06b13f8c1700e024de6382919ddc0f8c2bf772798654a38d9e7f41c18ab2032e
      symbol_hashes:
        vm_load_until_nul: sha256:f65607e74fce137d86a282539ef80615a63582cf551668aa44115ed3b4e49767
      missing_symbols: []
      content_hash: sha256:8d542c4492f2dfe413baf6453ad0fd2edc7ac82a1ba69e9c16ca0f5a27bd691c
    - path: os/StarryOS/kernel/src/file/fs.rs
      symbols:
      - resolve_at
      scope: symbols
      file_hash: sha256:550e894d6abfbc7221d14420c4a3b9ed85ff072e792e108c2f8b7f8a6dceeefd
      symbol_hashes:
        resolve_at: sha256:ec9e7f57add9a1db10191664fd7c77c9236ea7f33e3df9b43ce8fd66ddc0a01f
      missing_symbols: []
      content_hash: sha256:b3dce20309fe9f480c0da78b10b6995550acae12ab1f7f9f348ac78ca0cebbe2
    - path: os/StarryOS/kernel/src/mm/access.rs
      symbols:
      - vm_load_path_string
      - vm_load_string
      scope: symbols
      file_hash: sha256:4c4fd8a5e5fdf74824fba2666041a10ff4daf9a0214bf6ddeabe8c9e67fc60a6
      symbol_hashes:
        vm_load_path_string: sha256:95f8b4926ce8e625750404ccab6b5faf51ebf398553aac30035185c0d56642f4
        vm_load_string: sha256:cee098cc352143ede741ebb982ba6d15f7eac71b6667871500b4a5ac4d42bb2e
      missing_symbols: []
      content_hash: sha256:f6fdd2214052ea5f56fef51f35d895763600c89e1aba847f54432d0346f2d3d4
    - path: os/StarryOS/kernel/src/syscall/fs/stat.rs
      symbols:
      - sys_access
      - sys_faccessat2
      scope: symbols
      file_hash: sha256:8c2b95c055a36e86b297489cffb8e9d0b4aee3d82941680f6abb9716f3fb2f8e
      symbol_hashes:
        sys_access: sha256:e53d5b954a3ef9ff58ed71b80472fb3f2b0ccaa44cb3004d725642a4a4689410
        sys_faccessat2: sha256:2b709c3ba051efeb9d68846547ada28d8b8cac5b8611e1be55b6fce8e6cab756
      missing_symbols: []
      content_hash: sha256:a54fce312aa6a1f336b085bc3620f03cb300748c4b561a5eef4e55d55de13ed0
    - path: os/arceos/modules/axfs-ng/src/fs_core/context.rs
      symbols:
      - resolve
      - resolve_inner
      - try_resolve_symlink
      scope: symbols
      file_hash: sha256:6cd56d9acec5dc2b33d0d931a4e147c7dcd13318fe706800a02503c2220f7204
      symbol_hashes:
        resolve: sha256:14a2b52408caa4b091a4b90ec30e6412155884199bbc592741da38777fc3581a
        resolve_inner: sha256:702d76c45f2ff1046f5d437d0e459366482b7ef2e76b1cfb259d536be7b52cc5
        try_resolve_symlink: sha256:2577319f282965c000834bd77c6fd7e1f77f7d44f10b688767d6391bab4169f3
      missing_symbols: []
      content_hash: sha256:0cf7ffc1f42cba981fa89780d918b03c47f71d465064f3e12b024bf39d071734
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_faccessat2 加载路径后调用 resolve_at/FsContext 路径解析；缺失项、非目录组件、符号链接循环和超长路径错误按 Linux errno 传播。
  LTP_8C508A50371B6444:
    syscalls: *id189
    rule_version:
      id: LTP_8C508A50371B6444
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:8c508a50371b64446913da00f93812e109d4fd8dd925be4a47715748c400a4e5
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_8CB51F0A9F8FDEA1:
    syscalls: *id190
    rule_version:
      id: LTP_8CB51F0A9F8FDEA1
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:8cb51f0a9f8fdea1aa9265603077bdab7f6a75daa52c05b15830b85b2f4a0ea1
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_8D3BFFA98E2561BA:
    syscalls: *id191
    rule_version:
      id: LTP_8D3BFFA98E2561BA
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:8d3bffa98e2561bafe63fc7bc38802e2d2953e533b9e666d99c654309cec9af3
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_8D54825D4B298C7C:
    syscalls: *id192
    rule_version:
      id: LTP_8D54825D4B298C7C
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:8d54825d4b298c7c9eb6eb7ac7b0a5cf3f68cd369587ab92c3607e2e2cc10830
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_8E7F1BE3D7D7823B:
    syscalls: *id193
    rule_version:
      id: LTP_8E7F1BE3D7D7823B
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:8e7f1be3d7d7823b3dde9ddc3d5b8c29ed22da2d21c0fb4dbe4d5d3afcb0c840
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_8F29388433422812:
    syscalls: *id194
    rule_version:
      id: LTP_8F29388433422812
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:8f29388433422812f34a3bd5135b988bfc543476cdd7c971986173d27aea3a5b
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 动作使用 mode=-1，但上游把前置条件记录为 INVALID_FD；access 没有 fd 参数，语义前置条件不完整，需先复核规则。
  LTP_8FF73194288F8473:
    syscalls: *id195
    rule_version:
      id: LTP_8FF73194288F8473
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:8ff73194288f8473237046126e7c31cfa18b72d4aa9df824d60e7f6375ff1458
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_906135780505447D:
    syscalls: *id196
    rule_version:
      id: LTP_906135780505447D
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:906135780505447df3e13e314003f581efa2d1ee30de2ea30dbab0143fcce9a6
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_911B97B972658989:
    syscalls: *id197
    rule_version:
      id: LTP_911B97B972658989
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:911b97b97265898970041564ec32af260903836d6b1beced9f5ec5c56eec3eb6
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_919ABCA2598F53B5:
    syscalls: *id198
    rule_version:
      id: LTP_919ABCA2598F53B5
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:919abca2598f53b5e99bbe5acec60bec538242577a44344d469f5612aef69a6b
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_921D4802D7690C64:
    syscalls: *id199
    rule_version:
      id: LTP_921D4802D7690C64
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:921d4802d7690c64baa13cef4036a930795dd4b8c1c86da11196a6ab251cff74
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_9260E923CF8AA018:
    syscalls: *id200
    rule_version:
      id: LTP_9260E923CF8AA018
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:9260e923cf8aa0181ff0dc6f6891dd95b28c969e2c31087d648a8189707dcfed
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_929B120944D8F805:
    syscalls: *id201
    rule_version:
      id: LTP_929B120944D8F805
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:929b120944d8f80593edbc399d63daf30147188d1cf373314a057f761df649e2
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_93949494FBAD3568:
    syscalls: *id202
    rule_version:
      id: LTP_93949494FBAD3568
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:93949494fbad356821669ef617a89d87a34da4d9887617ed573781f5ae519106
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_94E36E221125BFAF:
    syscalls: *id203
    rule_version:
      id: LTP_94E36E221125BFAF
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:94e36e221125bfaf16f84bfbaf02a7e3205a99944a0fa27e9cea98ed8642a92c
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_955ECE70D81CA226:
    syscalls: *id204
    rule_version:
      id: LTP_955ECE70D81CA226
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:955ece70d81ca2265720d6c55e260bedc4dd54b36cafd2073a3878f975bd7087
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_96021AFB69E847F9:
    syscalls: *id205
    rule_version:
      id: LTP_96021AFB69E847F9
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:96021afb69e847f97d69047d8752f3a007ac9e37dab787c2aa17cbd86cd4ba43
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_969C39F409BFD7AA:
    syscalls: *id206
    rule_version:
      id: LTP_969C39F409BFD7AA
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:969c39f409bfd7aa54d82173400747fbba4044a6be5c4266dc75d7f6ef1444a6
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_96D205FACA0DD8DB:
    syscalls: *id207
    rule_version:
      id: LTP_96D205FACA0DD8DB
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:96d205faca0dd8dbe6122553b7e15b664912bfab18ee1ab4bf67591c7fb581e3
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_96F07DC5DDC8E018:
    syscalls: *id208
    rule_version:
      id: LTP_96F07DC5DDC8E018
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:96f07dc5ddc8e018a3a3a8044b0bf164f2d608e7ae0b79cced18aa24b0729285
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_97C442AC56780374:
    syscalls: *id209
    rule_version:
      id: LTP_97C442AC56780374
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:97c442ac5678037400d83150dbb28aa04f594bf29de4245f75f1c23d732a08fc
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_9866FB6F1F726CA0:
    syscalls: *id210
    rule_version:
      id: LTP_9866FB6F1F726CA0
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:9866fb6f1f726ca09b77bd655c3a477b9ef2d3857d60561868a8240341b223aa
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_986F211E7D45CAD7:
    syscalls: *id211
    rule_version:
      id: LTP_986F211E7D45CAD7
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:986f211e7d45cad74127bbc87f5e50b69ca7ee71e5aa523e5c87ab76ef11ba93
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_98EC66149EE68933:
    syscalls: *id212
    rule_version:
      id: LTP_98EC66149EE68933
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:98ec66149ee68933043c3d08d35dea4ea3d8145e3e6e4c72dfd96c786ca3c307
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有
      sys_alarm 入口。
  LTP_99DF5C34778032E1:
    syscalls: *id213
    rule_version: &id353
      id: LTP_99DF5C34778032E1
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:99df5c34778032e1483871676a4cbb8fc57a3bbfcd2fd0c74f90f83147e1a5f8
    status: covered
    static_check_refs:
    - STARRY_BATCH_ERRNO_TRANSLATION
    - STARRY_CHROOT_PATH
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_BATCH_ERRNO_TRANSLATION:
          id: STARRY_BATCH_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:e19f574ad1b857afc459fe1d55fbe4e71451eceeeeff1452ff74c6c7fec81a15
        STARRY_CHROOT_PATH:
          id: STARRY_CHROOT_PATH
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:357fbab1f149ef6fb3807966810bffa3366973f2c4f2c854bb821004e4a3753f
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: components/axfs-ng-vfs/src/path.rs
      symbols:
      - verify_entry_name
      scope: symbols
      file_hash: sha256:6e44a62c3142a5ebecb4c5c4c93f2d06c24ff549457c5c8b6787c8e90e46c11e
      symbol_hashes:
        verify_entry_name: sha256:516c7b090800149dc2bf3b7312761813844477a67da496c991099780f62c7ce5
      missing_symbols: []
      content_hash: sha256:2b2482c278ed782ee473d1a44f6611931e19f6b8db3edb22a40b3333d6bf50a0
    - path: components/starry-vm/src/alloc.rs
      symbols:
      - vm_load_until_nul
      scope: symbols
      file_hash: sha256:06b13f8c1700e024de6382919ddc0f8c2bf772798654a38d9e7f41c18ab2032e
      symbol_hashes:
        vm_load_until_nul: sha256:f65607e74fce137d86a282539ef80615a63582cf551668aa44115ed3b4e49767
      missing_symbols: []
      content_hash: sha256:8d542c4492f2dfe413baf6453ad0fd2edc7ac82a1ba69e9c16ca0f5a27bd691c
    - path: os/StarryOS/kernel/src/mm/access.rs
      symbols:
      - vm_load_string
      scope: symbols
      file_hash: sha256:4c4fd8a5e5fdf74824fba2666041a10ff4daf9a0214bf6ddeabe8c9e67fc60a6
      symbol_hashes:
        vm_load_string: sha256:cee098cc352143ede741ebb982ba6d15f7eac71b6667871500b4a5ac4d42bb2e
      missing_symbols: []
      content_hash: sha256:e17a288c5843ae74a5c3e12ef6048c2572a8793b06467613638d615ffc385958
    - path: os/StarryOS/kernel/src/syscall/fs/ctl.rs
      symbols:
      - sys_chroot
      scope: symbols
      file_hash: sha256:a42d57fc2422560978476f017ea2ae3d59e59be8c3f119e45fb5f18529d2e7e5
      symbol_hashes:
        sys_chroot: sha256:2445750c1d3c822f8438f9a1914fe47b5360157364ca20142ad673492d889756
      missing_symbols: []
      content_hash: sha256:928d58e7292bc7e8922d1000e5aabe85e9fdb3f1f6c3f84b52583584b92d0d55
    - path: os/arceos/modules/axfs-ng/src/fs_core/context.rs
      symbols:
      - new
      - resolve
      - resolve_inner
      - try_resolve_symlink
      scope: symbols
      file_hash: sha256:6cd56d9acec5dc2b33d0d931a4e147c7dcd13318fe706800a02503c2220f7204
      symbol_hashes:
        new: sha256:3d17bd68745b169b5dbdd92e4dae5756b1d41e3850eea66a0cf7be91f1c551b2
        resolve: sha256:14a2b52408caa4b091a4b90ec30e6412155884199bbc592741da38777fc3581a
        resolve_inner: sha256:702d76c45f2ff1046f5d437d0e459366482b7ef2e76b1cfb259d536be7b52cc5
        try_resolve_symlink: sha256:2577319f282965c000834bd77c6fd7e1f77f7d44f10b688767d6391bab4169f3
      missing_symbols: []
      content_hash: sha256:955067eb239a31c67297a10606806cadf346d537ebd469118db448e88e52f236
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_chroot 先读取用户路径，再经 FsContext 解析并要求目标为目录；路径读取或解析错误及 ENOTDIR 由 errno 层保真转换。
  LTP_9A723EA0B1F0D1BE:
    syscalls: *id214
    rule_version:
      id: LTP_9A723EA0B1F0D1BE
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:9a723ea0b1f0d1be76bccdcb190d1564f1fc1b71f3ad775b55c9121b1402052f
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_9C9D222A34799D55:
    syscalls: *id215
    rule_version:
      id: LTP_9C9D222A34799D55
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:9c9d222a34799d55b8df29a5ca8c61ca4dd502b6f2a003c5f6b3bea7ffd51fff
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_9CA9C6B61C3317A3:
    syscalls: *id216
    rule_version:
      id: LTP_9CA9C6B61C3317A3
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:9ca9c6b61c3317a32e26c489d7ae42771eb27df123a4f1488713978280f9bfb7
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 规则依赖 socket 类型、监听或连接队列、地址长度、用户指针以及 exp_errno 等运行时状态；现有静态分支无法唯一确定预期结果。
  LTP_9CDCD3C4BA6C2702:
    syscalls: *id217
    rule_version:
      id: LTP_9CDCD3C4BA6C2702
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:9cdcd3c4ba6c2702bcfdc87ff580ae8965d93fd14c816da9e2cb2da5bf7f3a32
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_A00E343F4A556B3D:
    syscalls: *id218
    rule_version:
      id: LTP_A00E343F4A556B3D
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:a00e343f4a556b3d95ff7c9596db5dad52a7bcce09ee6424a48853bc04d5c4af
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 旧式测试只保留返回 -1，未保留 errno 与 capability 前置状态，无法映射到唯一静态分支。
  LTP_A17272D4FE0F040B:
    syscalls: *id219
    rule_version:
      id: LTP_A17272D4FE0F040B
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:a17272d4fe0f040b3551f0c48f7f679eac6329498adc53aa6c28b6db119761c0
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_A1DEE046C0A10B18:
    syscalls: *id220
    rule_version:
      id: LTP_A1DEE046C0A10B18
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:a1dee046c0a10b1867a71cbf9e1fa5cda71eb744c20dcee680c7a1b838ffe8f9
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_A30F7687D403407B:
    syscalls: *id221
    rule_version:
      id: LTP_A30F7687D403407B
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:a30f7687d403407bd6fca8b3e2dae3e7d78a7a44247e4ee6ede6bcb7e5c4be0b
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_A4060315D2E047EE:
    syscalls: *id222
    rule_version:
      id: LTP_A4060315D2E047EE
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:a4060315d2e047ee719f30e5665b983e33cfebf352c8040520b504f3fb57eeb5
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_A4733D4B2FEBE9A4:
    syscalls: *id223
    rule_version:
      id: LTP_A4733D4B2FEBE9A4
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:a4733d4b2febe9a4e637179d892540534842c69fb8d76e018b5dc5c23c66daf4
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_A500A46C4B998E74:
    syscalls: *id224
    rule_version:
      id: LTP_A500A46C4B998E74
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:a500a46c4b998e741de132746e8b0b0af9bdf29d85cac68d7f2acd81814c2c62
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_A6B94E8A2A4D8853:
    syscalls: *id225
    rule_version:
      id: LTP_A6B94E8A2A4D8853
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:a6b94e8a2a4d885377e082223b765961646dbaa4510911162986a491fd28f7dd
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_A9544B59EB6712D9:
    syscalls: *id226
    rule_version:
      id: LTP_A9544B59EB6712D9
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:a9544b59eb6712d94dca462aac20f704d4535396cc91193124901c37b73cbf45
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_A9596E932167B3EF:
    syscalls: *id227
    rule_version:
      id: LTP_A9596E932167B3EF
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:a9596e932167b3ef67bc5be85c77f5f7186b148d1d991e588809c2e0180f3a82
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_AB48F262BBB2CC93:
    syscalls: *id228
    rule_version:
      id: LTP_AB48F262BBB2CC93
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ab48f262bbb2cc9376b9361a581295adf4c119fb72babdbec46a9c3fceb34c36
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_AC0FB73B4EE420EC:
    syscalls: *id229
    rule_version:
      id: LTP_AC0FB73B4EE420EC
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ac0fb73b4ee420ecfea385432c4abfe9c2c3b14391ddd2970259d31c1f078ee8
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_AD81218450587FA8:
    syscalls: *id230
    rule_version:
      id: LTP_AD81218450587FA8
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ad81218450587fa8b2318bd795c03007cebfed4129850ee359cfc4131427079d
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_ADD30BEEC40E661F:
    syscalls: *id231
    rule_version:
      id: LTP_ADD30BEEC40E661F
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:add30beec40e661fc3944ee505b4d769fc54d04f71f942462c6cb43630563870
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_B1D822DF0057B4E0:
    syscalls: *id232
    rule_version:
      id: LTP_B1D822DF0057B4E0
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:b1d822df0057b4e0eac5216fb772e5d0c67dc95c27884035caa5b94c422e5b81
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_B200AFD97E91C2CC:
    syscalls: *id233
    rule_version:
      id: LTP_B200AFD97E91C2CC
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:b200afd97e91c2ccb465d33728cb17a5abb857c8c016b9f250cfdb1d2c759a2c
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_B53406D510ED4981:
    syscalls: *id234
    rule_version:
      id: LTP_B53406D510ED4981
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:b53406d510ed49814b3727cfd8c65d414738713fc20ce0d05e400a015ab9779a
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_B6DAF13EF3143EBF:
    syscalls: *id235
    rule_version:
      id: LTP_B6DAF13EF3143EBF
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:b6daf13ef3143ebfc55e0ec850c878d9500e8473f37a55945927c59c6421e6f9
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_B7A341967DF2BD69:
    syscalls: *id236
    rule_version:
      id: LTP_B7A341967DF2BD69
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:b7a341967df2bd693bb7f1bd2a9d165ae51ec15aa83ec06f274bc9e6ed7dbd8e
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有
      sys_alarm 入口。
  LTP_B90CB73F36B70C6F:
    syscalls: *id237
    rule_version:
      id: LTP_B90CB73F36B70C6F
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:b90cb73f36b70c6f80c9105773e4598523d84a62b8068d6913141437de6ddcb8
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 规则依赖 socket 类型、监听或连接队列、地址长度、用户指针以及 exp_errno 等运行时状态；现有静态分支无法唯一确定预期结果。
  LTP_B9908D4015443661:
    syscalls: *id238
    rule_version:
      id: LTP_B9908D4015443661
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:b9908d4015443661be8818bffa5f28fd1ab370bc37b054db41ada6f87be58e3f
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_B9CDD41A0DC2AFCC:
    syscalls: *id239
    rule_version:
      id: LTP_B9CDD41A0DC2AFCC
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:b9cdd41a0dc2afcc67185697f8300fffda120b752a387b2b4bebce66b8e3556e
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_BA10984A4B0DE2C6:
    syscalls: *id240
    rule_version:
      id: LTP_BA10984A4B0DE2C6
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ba10984a4b0de2c627f9d0f52b2a95d6cefc04c10e7118c64201ddb965ef6912
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_BA9A8FE901467960:
    syscalls: *id241
    rule_version:
      id: LTP_BA9A8FE901467960
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ba9a8fe9014679607013f8aa7b560aec873309bb14116b916767925e8499f776
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::cachestat 分派分支，syscall 实现目录中也没有
      sys_cachestat 入口。
  LTP_BC662075E3BAE807:
    syscalls: *id242
    rule_version:
      id: LTP_BC662075E3BAE807
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:bc662075e3bae80716721d493d2ecb205c425c8d4036a15537b8b67f1d6c41e7
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_BE2E778739EF01D5:
    syscalls: *id243
    rule_version:
      id: LTP_BE2E778739EF01D5
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:be2e778739ef01d53e5c394d3e4f4103b51e2ad54fb2ab15a8e37ce409044314
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_C0577C0D678214DA:
    syscalls: *id244
    rule_version:
      id: LTP_C0577C0D678214DA
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:c0577c0d678214da548753b907d5506a697884d30765112eb0a6df1dee8eb040
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_C071A7FFF929A2A5:
    syscalls: *id245
    rule_version:
      id: LTP_C071A7FFF929A2A5
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:c071a7fff929a2a5776da6862c4f0aaf5902ad0b0bb61779ceadca9f556fceaa
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_C0AA45BC29F98A0E:
    syscalls: *id246
    rule_version:
      id: LTP_C0AA45BC29F98A0E
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:c0aa45bc29f98a0e7e47e5f8289bcbaa8298f2dd9baa2a322f25acc464663544
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_C1C67435FC56D878:
    syscalls: *id247
    rule_version:
      id: LTP_C1C67435FC56D878
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:c1c67435fc56d87840f092f5726c75284aa449ae5aca2a9d076cde8bc341ab4b
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_C218D3CB0AD80D90:
    syscalls: *id248
    rule_version:
      id: LTP_C218D3CB0AD80D90
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:c218d3cb0ad80d90bc2c5db1a2892a964c1bc89369fc4ec66a71fac08ac8f5f6
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::cacheflush 分派分支，syscall 实现目录中也没有
      sys_cacheflush 入口。
  LTP_C346EFF1233F7061:
    syscalls: *id249
    rule_version:
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
    reason: 相关 Starry 内容指纹未变化，已跳过。
  LTP_C5FE18F9550B31BA:
    syscalls: *id250
    rule_version:
      id: LTP_C5FE18F9550B31BA
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:c5fe18f9550b31bacd167f490f815fb96ef18cdfa2d50996ca49c23cbad4bf77
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_C6A719982BDE9CE4:
    syscalls: *id251
    rule_version:
      id: LTP_C6A719982BDE9CE4
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:c6a719982bde9ce4456fee47f9a74e3e085b5e587b7c1f3b1593b6673551c887
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_C6E67CB1FD2B1F64:
    syscalls: *id252
    rule_version:
      id: LTP_C6E67CB1FD2B1F64
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:c6e67cb1fd2b1f645c00f57dd53b305566c4d2f510659da09bc7d47a3e68bfe3
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_C785774773FB7524:
    syscalls: *id253
    rule_version:
      id: LTP_C785774773FB7524
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:c785774773fb7524870d7b604061d2af95f33c66253633d4323113134440929d
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有
      sys_alarm 入口。
  LTP_C7B73F4D5B87736A:
    syscalls: *id254
    rule_version:
      id: LTP_C7B73F4D5B87736A
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:c7b73f4d5b87736afb434f999fc75233df1703e63bf0c31b5b8eb241adef31b2
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有
      sys_alarm 入口。
  LTP_C80C019BE3F47901:
    syscalls: *id255
    rule_version:
      id: LTP_C80C019BE3F47901
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:c80c019be3f47901f55816308f54ee6e895f5df8a818ce4d61e002ce96470fdd
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有
      sys_alarm 入口。
  LTP_C8DAE34819E335F8:
    syscalls: *id256
    rule_version: &id354
      id: LTP_C8DAE34819E335F8
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:c8dae34819e335f88d2bad8650e2067ec51e8a1c6d21ef37198241a9af5a56f2
    status: covered
    static_check_refs:
    - STARRY_ACCESS_PATH_RESOLUTION
    - STARRY_BATCH_ERRNO_TRANSLATION
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_ACCESS_PATH_RESOLUTION:
          id: STARRY_ACCESS_PATH_RESOLUTION
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:896f2b8f806c19bafee558addd47df7692321be39551b0da996b9c942907a805
        STARRY_BATCH_ERRNO_TRANSLATION:
          id: STARRY_BATCH_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:e19f574ad1b857afc459fe1d55fbe4e71451eceeeeff1452ff74c6c7fec81a15
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: components/axfs-ng-vfs/src/path.rs
      symbols:
      - verify_entry_name
      scope: symbols
      file_hash: sha256:6e44a62c3142a5ebecb4c5c4c93f2d06c24ff549457c5c8b6787c8e90e46c11e
      symbol_hashes:
        verify_entry_name: sha256:516c7b090800149dc2bf3b7312761813844477a67da496c991099780f62c7ce5
      missing_symbols: []
      content_hash: sha256:2b2482c278ed782ee473d1a44f6611931e19f6b8db3edb22a40b3333d6bf50a0
    - path: components/starry-vm/src/alloc.rs
      symbols:
      - vm_load_until_nul
      scope: symbols
      file_hash: sha256:06b13f8c1700e024de6382919ddc0f8c2bf772798654a38d9e7f41c18ab2032e
      symbol_hashes:
        vm_load_until_nul: sha256:f65607e74fce137d86a282539ef80615a63582cf551668aa44115ed3b4e49767
      missing_symbols: []
      content_hash: sha256:8d542c4492f2dfe413baf6453ad0fd2edc7ac82a1ba69e9c16ca0f5a27bd691c
    - path: os/StarryOS/kernel/src/file/fs.rs
      symbols:
      - resolve_at
      scope: symbols
      file_hash: sha256:550e894d6abfbc7221d14420c4a3b9ed85ff072e792e108c2f8b7f8a6dceeefd
      symbol_hashes:
        resolve_at: sha256:ec9e7f57add9a1db10191664fd7c77c9236ea7f33e3df9b43ce8fd66ddc0a01f
      missing_symbols: []
      content_hash: sha256:b3dce20309fe9f480c0da78b10b6995550acae12ab1f7f9f348ac78ca0cebbe2
    - path: os/StarryOS/kernel/src/mm/access.rs
      symbols:
      - vm_load_path_string
      - vm_load_string
      scope: symbols
      file_hash: sha256:4c4fd8a5e5fdf74824fba2666041a10ff4daf9a0214bf6ddeabe8c9e67fc60a6
      symbol_hashes:
        vm_load_path_string: sha256:95f8b4926ce8e625750404ccab6b5faf51ebf398553aac30035185c0d56642f4
        vm_load_string: sha256:cee098cc352143ede741ebb982ba6d15f7eac71b6667871500b4a5ac4d42bb2e
      missing_symbols: []
      content_hash: sha256:f6fdd2214052ea5f56fef51f35d895763600c89e1aba847f54432d0346f2d3d4
    - path: os/StarryOS/kernel/src/syscall/fs/stat.rs
      symbols:
      - sys_access
      - sys_faccessat2
      scope: symbols
      file_hash: sha256:8c2b95c055a36e86b297489cffb8e9d0b4aee3d82941680f6abb9716f3fb2f8e
      symbol_hashes:
        sys_access: sha256:e53d5b954a3ef9ff58ed71b80472fb3f2b0ccaa44cb3004d725642a4a4689410
        sys_faccessat2: sha256:2b709c3ba051efeb9d68846547ada28d8b8cac5b8611e1be55b6fce8e6cab756
      missing_symbols: []
      content_hash: sha256:a54fce312aa6a1f336b085bc3620f03cb300748c4b561a5eef4e55d55de13ed0
    - path: os/arceos/modules/axfs-ng/src/fs_core/context.rs
      symbols:
      - resolve
      - resolve_inner
      - try_resolve_symlink
      scope: symbols
      file_hash: sha256:6cd56d9acec5dc2b33d0d931a4e147c7dcd13318fe706800a02503c2220f7204
      symbol_hashes:
        resolve: sha256:14a2b52408caa4b091a4b90ec30e6412155884199bbc592741da38777fc3581a
        resolve_inner: sha256:702d76c45f2ff1046f5d437d0e459366482b7ef2e76b1cfb259d536be7b52cc5
        try_resolve_symlink: sha256:2577319f282965c000834bd77c6fd7e1f77f7d44f10b688767d6391bab4169f3
      missing_symbols: []
      content_hash: sha256:0cf7ffc1f42cba981fa89780d918b03c47f71d465064f3e12b024bf39d071734
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_faccessat2 加载路径后调用 resolve_at/FsContext 路径解析；缺失项、非目录组件、符号链接循环和超长路径错误按 Linux errno 传播。
  LTP_C994B56A41A71C1A:
    syscalls: *id257
    rule_version:
      id: LTP_C994B56A41A71C1A
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:c994b56a41a71c1ae8b34f44da5b8c78d6f0c14ccdc0067d6398cdb48f4c54d6
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_CA45A33676AD236D:
    syscalls: *id258
    rule_version:
      id: LTP_CA45A33676AD236D
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ca45a33676ad236da5a59d05b5ed7f937b678b76b2b427c0416f8ca8966c1e6d
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_CA80C3F10B65226D:
    syscalls: *id259
    rule_version:
      id: LTP_CA80C3F10B65226D
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ca80c3f10b65226de17483b8685372fb4aa133ac10a2a11dca2bb1c33b9b01dc
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_CB31E19EE807FFDB:
    syscalls: *id260
    rule_version:
      id: LTP_CB31E19EE807FFDB
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:cb31e19ee807ffdb5836e24f23c68978f710465f4190b09f63bedd88cad364a2
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_CCDB1776DAA2C318:
    syscalls: *id261
    rule_version:
      id: LTP_CCDB1776DAA2C318
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ccdb1776daa2c318c58907012899ab82a3b26a30cc45002a853928e842f26813
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_CD2150BE4FE81F31:
    syscalls: *id262
    rule_version:
      id: LTP_CD2150BE4FE81F31
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:cd2150be4fe81f31d96048faf2fd894533271cce5b64d7f76119b5d3b31387e4
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有
      sys_alarm 入口。
  LTP_CDCDC1B9E63D58C3:
    syscalls: *id263
    rule_version:
      id: LTP_CDCDC1B9E63D58C3
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:cdcdc1b9e63d58c38e0342f9f6a8d311e1bc7314f7faae3ee2ca47a71d9455f4
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_CE45382D3DE75F8F:
    syscalls: *id264
    rule_version:
      id: LTP_CE45382D3DE75F8F
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ce45382d3de75f8f280054000f338075bda0efb06b7920ed5028dbe2c9762a0d
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_CEBAD6AB3C82795E:
    syscalls: *id265
    rule_version:
      id: LTP_CEBAD6AB3C82795E
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:cebad6ab3c82795ef8bc7e31c4d7f005f68342cf154bfae4d5f232ec2997fd8a
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_CED2FCC737A99D40:
    syscalls: *id266
    rule_version:
      id: LTP_CED2FCC737A99D40
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ced2fcc737a99d40bc85fda1ad7df308a9af646010036252eac3d2cc5d384bb8
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 目标 pid 的存在性和条件表达式选择未完整记录；ESRCH 依赖运行时任务表状态，不能仅凭静态实现确认。
  LTP_D0E32E5D27E643A9:
    syscalls: *id267
    rule_version:
      id: LTP_D0E32E5D27E643A9
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:d0e32e5d27e643a92fca4116aaeefb86ce87cdcc1e5fd0d511ff4dbdc52401cb
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: EACCES 依赖目录搜索权限和调用者凭据的运行时组合；规则与静态路径解析证据不足以确认该结果。
  LTP_D1AADFC2F7C6F594:
    syscalls: *id268
    rule_version:
      id: LTP_D1AADFC2F7C6F594
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:d1aadfc2f7c6f594928cbc9032ee1cc614ab7493537d5f16041f8e5885973b3b
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: EPERM 取决于调用者 permitted、inheritable、bounding 与 CAP_SETPCAP 运行时状态；规则未完整记录这些前置条件。
  LTP_D1B6112551D45B31:
    syscalls: *id269
    rule_version:
      id: LTP_D1B6112551D45B31
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:d1b6112551d45b31a564bdbe96d936daffb4747eabac294fc9969f6dfe1c9850
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有
      sys_alarm 入口。
  LTP_D1F469715ECC4195:
    syscalls: *id270
    rule_version:
      id: LTP_D1F469715ECC4195
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:d1f469715ecc419564dd027615d3da31a0126f706ae147e1191a041e4a2d06ab
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_D2D67AB5E38A7000:
    syscalls: *id271
    rule_version:
      id: LTP_D2D67AB5E38A7000
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:d2d67ab5e38a7000f636bb8ea94430224ae59507a8e362a2e8601c835285925e
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_D2F4BCF2263C56F5:
    syscalls: *id272
    rule_version:
      id: LTP_D2F4BCF2263C56F5
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:d2f4bcf2263c56f511e85ed0974323b7de92a5c313314142b314060cfa3416a8
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_D412A09DEDC43045:
    syscalls: *id273
    rule_version:
      id: LTP_D412A09DEDC43045
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:d412a09dedc430455bcaee23066531008ffc400c39cfec08a2b7c0560f283513
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_D4B433A3696803A8:
    syscalls: *id274
    rule_version:
      id: LTP_D4B433A3696803A8
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:d4b433a3696803a8932f8a59a7d40caabfe8f9b592dc394ed4d920b4832325d3
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::alarm 分派分支，syscall 实现目录中也没有
      sys_alarm 入口。
  LTP_D4D8A0FEAA2F6B09:
    syscalls: *id275
    rule_version:
      id: LTP_D4D8A0FEAA2F6B09
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:d4d8a0feaa2f6b09ee4197bda4acedae9ed3a247bb92e107645b013a2b97a9df
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_D579FCFC71E6EB6A:
    syscalls: *id276
    rule_version:
      id: LTP_D579FCFC71E6EB6A
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:d579fcfc71e6eb6a79a4aefff0c4df8ba201988162fee4b24255c4c001c1302b
    status: unsupported
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 固定 Starry 快照的 os/StarryOS/kernel/src/syscall/mod.rs 中没有 Sysno::cacheflush 分派分支，syscall 实现目录中也没有
      sys_cacheflush 入口。
  LTP_D653D15777B77A1F:
    syscalls: *id277
    rule_version:
      id: LTP_D653D15777B77A1F
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:d653d15777b77a1f2f22b9ad51399e98948cbcfeb7dea90eca3bcc1dc2c72c13
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_D6A52FD61BF01578:
    syscalls: *id278
    rule_version:
      id: LTP_D6A52FD61BF01578
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:d6a52fd61bf01578d57b2137fb8783fa4aa12fbc36528c0fe57c44869f8ae3b9
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_D72526C4E4301D60:
    syscalls: *id279
    rule_version:
      id: LTP_D72526C4E4301D60
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:d72526c4e4301d602772892e7acb7d791190ad295c689edee33935e8a3042142
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_D76652434EC85091:
    syscalls: *id280
    rule_version:
      id: LTP_D76652434EC85091
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:d76652434ec85091cb128b18a9f43cf85789b33a1273659abba33ea994dabbf6
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_D8B58CA743EBE711:
    syscalls: *id281
    rule_version:
      id: LTP_D8B58CA743EBE711
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:d8b58ca743ebe711572368b5326e991fe7d9c9c30c831d41aa6f61099d65190b
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_DA10E351BC730D85:
    syscalls: *id282
    rule_version:
      id: LTP_DA10E351BC730D85
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:da10e351bc730d85ee340c6d45341d502bce7d6d63af45b2e0c8bb9d7fd6c0d7
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_DAA03BAD070DB1D6:
    syscalls: *id283
    rule_version:
      id: LTP_DAA03BAD070DB1D6
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:daa03bad070db1d65d975ed3b9f2ec6be962774a8144dce2900b7ac44b218781
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_DAA1F16D8A298E83:
    syscalls: *id284
    rule_version:
      id: LTP_DAA1F16D8A298E83
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:daa1f16d8a298e831f352e689972a6839bc2efd8aa77712fc9b65fcfd0b01654
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_DC9BC72148835FDC:
    syscalls: *id285
    rule_version:
      id: LTP_DC9BC72148835FDC
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:dc9bc72148835fdcfc9cca3b1db4ce73b4cae94f45535d8bc89f01eb527400b0
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 同一条件表达式被上游展开出 EINVAL 与 ESRCH 两种冲突结果，且 header 版本分支未被保真记录，需复核上游分支。
  LTP_DCB33BB29D296843:
    syscalls: *id286
    rule_version:
      id: LTP_DCB33BB29D296843
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:dcb33bb29d296843e50e422e7bb1475ebffefc2ec76a9abe68e61f2e069ec65a
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_DD9A41090E3D5A17:
    syscalls: *id287
    rule_version:
      id: LTP_DD9A41090E3D5A17
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:dd9a41090e3d5a1757e1766c5d8ba367dcf03e04ead95254afac13d6550f0f6b
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_DF1C4714B16B760E:
    syscalls: *id288
    rule_version:
      id: LTP_DF1C4714B16B760E
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:df1c4714b16b760e1517fab21e4b1587a03f487b2fe3b271a21f7f899eb5eb07
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_E06D53042C10C99E:
    syscalls: *id289
    rule_version: &id355
      id: LTP_E06D53042C10C99E
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:e06d53042c10c99e7bdc61242d4ac56e1aace8c13e3442e875e2574ca74e60d3
    status: covered
    static_check_refs:
    - STARRY_BATCH_ERRNO_TRANSLATION
    - STARRY_CAPSET_ABI
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_BATCH_ERRNO_TRANSLATION:
          id: STARRY_BATCH_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:e19f574ad1b857afc459fe1d55fbe4e71451eceeeeff1452ff74c6c7fec81a15
        STARRY_CAPSET_ABI:
          id: STARRY_CAPSET_ABI
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:fa04e3f3a184e594c6b2b6f1f9d43027f9104bdc8a675eb3555d76e5cfb0faed
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: components/starry-vm/src/thin.rs
      symbols:
      - VmMutPtr
      - VmPtr
      scope: symbols
      file_hash: sha256:b787237758b16cc38fc20fa79234f62e2bad5d70235621818f9771c4a0810aa4
      symbol_hashes:
        VmMutPtr: sha256:35ae0c032d454211b5a4d3e0b11bf6bf854bd550d635855677666f26fb1f730a
        VmPtr: sha256:6c0ff10e65451fa76a4eb2caa472c0a96ff53459ae357d86f2dbf389f50e8804
      missing_symbols: []
      content_hash: sha256:1b7ca80cea190deec16a1cec479d83444169c6259f68ca0bf314edc58015fecd
    - path: os/StarryOS/kernel/src/syscall/task/ctl.rs
      symbols:
      - data_to_mask
      - sys_capset
      - validate_cap_header
      scope: symbols
      file_hash: sha256:901fc111c7b58af132705a41cf8a75d89164f522f89135f794e08b76a1ec05e9
      symbol_hashes:
        data_to_mask: sha256:83fc2bb0eb44d7806a59c49b19d8600aadfdbe3b4e893514102d99611ad985ff
        sys_capset: sha256:3e17536f5a7319b1ad18a17d39c88b715d8795162ccc1860d59845494d69265c
        validate_cap_header: sha256:f92b10dad6654ff4b7de228735357465447f4fc6010d9b0eb50afaae686cbf33
      missing_symbols: []
      content_hash: sha256:df372a3e9f4e00850aad57aaee664224ee6a290029e828efea476bb40d9b46a5
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: capset 在修改凭据前通过 VmPtr 读取 V3 header/data；无效 header 或 data 地址传播 BadAddress，并转换为 EFAULT。
  LTP_E0B177A8B6FE4225:
    syscalls: *id290
    rule_version:
      id: LTP_E0B177A8B6FE4225
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:e0b177a8b6fe4225e1088c7e49e952d5a51527d7a94a71d142baf04be4b83566
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_E0ED96B80FC3B6C9:
    syscalls: *id291
    rule_version:
      id: LTP_E0ED96B80FC3B6C9
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:e0ed96b80fc3b6c96463b988f7e4d1ff0b79e1c58a353675386fc6420ccc5977
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_E13B9C2C9645B841:
    syscalls: *id292
    rule_version:
      id: LTP_E13B9C2C9645B841
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:e13b9c2c9645b841740286ed51439b50fbadac9cb52df5b4b60bf4bd5ed5df31
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 规则依赖 socket 类型、监听或连接队列、地址长度、用户指针以及 exp_errno 等运行时状态；现有静态分支无法唯一确定预期结果。
  LTP_E28B5BB57A450438:
    syscalls: *id293
    rule_version:
      id: LTP_E28B5BB57A450438
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:e28b5bb57a450438b801a06bacaa75df24298a8f5ef516fe12005237e4222539
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_E2C3B68EDF07A753:
    syscalls: *id294
    rule_version:
      id: LTP_E2C3B68EDF07A753
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:e2c3b68edf07a7531dfea80c2aec3daba99b0f2c156c60994d6969b2e2bc6ca4
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_E34945E3DE91022F:
    syscalls: *id295
    rule_version:
      id: LTP_E34945E3DE91022F
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:e34945e3de91022f5bec4e3400409e0b76cc76cfa4fefaa6a605861cab436485
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_E3A3CF8B98E460BC:
    syscalls: *id296
    rule_version:
      id: LTP_E3A3CF8B98E460BC
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:e3a3cf8b98e460bcdc3034c9ebc9119094619ba2a33d775e86736f6ea1c7c9df
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_E3E59B16A96A60BC:
    syscalls: *id297
    rule_version: &id356
      id: LTP_E3E59B16A96A60BC
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:e3e59b16a96a60bce3de89603588b78a310e40b3710e530d67d5c30160121e86
    status: covered
    static_check_refs:
    - STARRY_BRK_HEAP
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_BRK_HEAP:
          id: STARRY_BRK_HEAP
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:08b3a24f292c0c2d933bf711c00c866ab3a74a54f291c4ddee9460d0eb6f43ac
      dynamic_tests: {}
    target_dependencies:
    - path: os/StarryOS/kernel/src/config/aarch64.rs
      symbols:
      - USER_HEAP_BASE
      - USER_HEAP_SIZE
      - USER_HEAP_SIZE_MAX
      scope: symbols
      file_hash: sha256:774155d8f1f08322a6707b4d09bcf2a68f5e882a65a7d72ff85b710d6834f201
      symbol_hashes:
        USER_HEAP_BASE: sha256:3ff8ee7d59885899912f42f724f3ab4aff6b34eda021d151e63c73e755caba3a
        USER_HEAP_SIZE: sha256:e150df3dfceba2739ace567435f441463c73cae24c07bd13311a3028286047c0
        USER_HEAP_SIZE_MAX: sha256:0cb8ac49063245c704178c4fceaa4490ce7d5d0369d2dd4d54a9a6a85d5a76c5
      missing_symbols: []
      content_hash: sha256:27fb22b5143847b13f436852fae29eec4df662361abbed0dcf1c052edf34722d
    - path: os/StarryOS/kernel/src/config/loongarch64.rs
      symbols:
      - USER_HEAP_BASE
      - USER_HEAP_SIZE
      - USER_HEAP_SIZE_MAX
      scope: symbols
      file_hash: sha256:74d8dc131109414b9cf80d5f2c6a0bb225a3a8d45a23c97dd8d31e51352cc694
      symbol_hashes:
        USER_HEAP_BASE: sha256:3ff8ee7d59885899912f42f724f3ab4aff6b34eda021d151e63c73e755caba3a
        USER_HEAP_SIZE: sha256:ffd1ad4365175a3bbcae5439e6ce7f26fbcc5b061b2850249a2287a252a68fda
        USER_HEAP_SIZE_MAX: sha256:fde7d3be05b0a123ec2663c6de2ee373ad6ab79d0f93f381d0140a6c4a493ff3
      missing_symbols: []
      content_hash: sha256:451c35f9f88bab1994e49b6c0870759e07eec1536c4bd75ec6709bb53639e78a
    - path: os/StarryOS/kernel/src/config/riscv64.rs
      symbols:
      - USER_HEAP_BASE
      - USER_HEAP_SIZE
      - USER_HEAP_SIZE_MAX
      scope: symbols
      file_hash: sha256:9b0ab32999b12ab2dbf7446a00545bf2a5c54d32f2c42c8382c0fac880443d58
      symbol_hashes:
        USER_HEAP_BASE: sha256:3ff8ee7d59885899912f42f724f3ab4aff6b34eda021d151e63c73e755caba3a
        USER_HEAP_SIZE: sha256:e150df3dfceba2739ace567435f441463c73cae24c07bd13311a3028286047c0
        USER_HEAP_SIZE_MAX: sha256:0cb8ac49063245c704178c4fceaa4490ce7d5d0369d2dd4d54a9a6a85d5a76c5
      missing_symbols: []
      content_hash: sha256:691d052a0f2d35b9d7b80c716b4f555fd17f01e7699433f163ceddad9623c334
    - path: os/StarryOS/kernel/src/config/x86_64.rs
      symbols:
      - USER_HEAP_BASE
      - USER_HEAP_SIZE
      - USER_HEAP_SIZE_MAX
      scope: symbols
      file_hash: sha256:5d2084f2ec16168c78b7fc3784faafb11a2738e52a4bd258068226ac55f0de88
      symbol_hashes:
        USER_HEAP_BASE: sha256:3ff8ee7d59885899912f42f724f3ab4aff6b34eda021d151e63c73e755caba3a
        USER_HEAP_SIZE: sha256:e150df3dfceba2739ace567435f441463c73cae24c07bd13311a3028286047c0
        USER_HEAP_SIZE_MAX: sha256:0cb8ac49063245c704178c4fceaa4490ce7d5d0369d2dd4d54a9a6a85d5a76c5
      missing_symbols: []
      content_hash: sha256:5520eed745a5d7a3f18da1bfc694111642821921d9476dfb16509b914da2262c
    - path: os/StarryOS/kernel/src/syscall/mm/brk.rs
      symbols:
      - sys_brk
      scope: symbols
      file_hash: sha256:235d73dad5117170ec322a42e0afb92edc703c335955af67ab203be685da070e
      symbol_hashes:
        sys_brk: sha256:65291f8268e25c9a6f2f7a7b6c2e40a97217a6fe0c8973c124db5f97dae6f1de
      missing_symbols: []
      content_hash: sha256:adf14b11828ae345ae531b93973cfee0bd9dbcf652999b84120e0125d27cdd9c
    - path: os/StarryOS/kernel/src/task/mod.rs
      symbols:
      - get_heap_top
      - set_heap_top
      scope: symbols
      file_hash: sha256:270ce7a86e57c31a8018300d905443254ecca9994148a7c5a55d18461b7fb0f7
      symbol_hashes:
        get_heap_top: sha256:fa0326839ec0b84758dfc98aab0ba7190fa38250da9e7e672a767cc64315b497
        set_heap_top: sha256:81791179ed6d16e014cc944d4c3193d1f124392d3a3691bf3aac93fb2423ebd3
      missing_symbols: []
      content_hash: sha256:0d36d97cc64136b5d97afed8b1e0036b0e91fdba3381fafcac8c97ea3f978104
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_brk 校验 heap 地址范围和 RLIMIT_DATA，按需映射或解除映射，成功后更新 heap_top 并返回新 break。
  LTP_E41DD7230DA067DD:
    syscalls: *id298
    rule_version:
      id: LTP_E41DD7230DA067DD
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:e41dd7230da067dd49192e171fa405245c34ff3e23ce95a67114c3fbbf4bb303
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_E46539F2D47BA5EC:
    syscalls: *id299
    rule_version:
      id: LTP_E46539F2D47BA5EC
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:e46539f2d47ba5ecd80e66b6a5705003631d65d3d38e7882c5c59c8c2f39bf6d
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_E4D1B76D80905462:
    syscalls: *id300
    rule_version:
      id: LTP_E4D1B76D80905462
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:e4d1b76d80905462632ab0976fb3a8a26184ee6aa72bb777ecf0d2437c1fd88d
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_E560C027210BF20A:
    syscalls: *id301
    rule_version:
      id: LTP_E560C027210BF20A
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:e560c027210bf20ae0ba8e32c02cb2e43fe1db33a34b5477b45c38b8ecd001a7
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_E5791B389C67677E:
    syscalls: *id302
    rule_version:
      id: LTP_E5791B389C67677E
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:e5791b389c67677e342a600db8a0a3d60536e7627457c447be4dada2a41f5ac7
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_E5E50FB7BDD033D9:
    syscalls: *id303
    rule_version:
      id: LTP_E5E50FB7BDD033D9
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:e5e50fb7bdd033d91ceea657540c90d9a0421e2feba98ad411da85613f9b5eff
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_EB00EA74B30E438E:
    syscalls: *id304
    rule_version:
      id: LTP_EB00EA74B30E438E
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:eb00ea74b30e438e0d9c68d1d22c8fc796810ed865f7a571844bd636958fce93
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_EB425D988F2F7604:
    syscalls: *id305
    rule_version:
      id: LTP_EB425D988F2F7604
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:eb425d988f2f7604459aba4e2fe34d6371def71a7110eac5b39dc26f87bb2f23
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_EBD54180D0CAB16B:
    syscalls: *id306
    rule_version: &id357
      id: LTP_EBD54180D0CAB16B
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ebd54180d0cab16b9271d149769e3e3e522ef97222514360017b81114bcc90e1
    status: covered
    static_check_refs:
    - STARRY_BATCH_ERRNO_TRANSLATION
    - STARRY_CHROOT_PATH
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_BATCH_ERRNO_TRANSLATION:
          id: STARRY_BATCH_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:e19f574ad1b857afc459fe1d55fbe4e71451eceeeeff1452ff74c6c7fec81a15
        STARRY_CHROOT_PATH:
          id: STARRY_CHROOT_PATH
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:357fbab1f149ef6fb3807966810bffa3366973f2c4f2c854bb821004e4a3753f
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: components/axfs-ng-vfs/src/path.rs
      symbols:
      - verify_entry_name
      scope: symbols
      file_hash: sha256:6e44a62c3142a5ebecb4c5c4c93f2d06c24ff549457c5c8b6787c8e90e46c11e
      symbol_hashes:
        verify_entry_name: sha256:516c7b090800149dc2bf3b7312761813844477a67da496c991099780f62c7ce5
      missing_symbols: []
      content_hash: sha256:2b2482c278ed782ee473d1a44f6611931e19f6b8db3edb22a40b3333d6bf50a0
    - path: components/starry-vm/src/alloc.rs
      symbols:
      - vm_load_until_nul
      scope: symbols
      file_hash: sha256:06b13f8c1700e024de6382919ddc0f8c2bf772798654a38d9e7f41c18ab2032e
      symbol_hashes:
        vm_load_until_nul: sha256:f65607e74fce137d86a282539ef80615a63582cf551668aa44115ed3b4e49767
      missing_symbols: []
      content_hash: sha256:8d542c4492f2dfe413baf6453ad0fd2edc7ac82a1ba69e9c16ca0f5a27bd691c
    - path: os/StarryOS/kernel/src/mm/access.rs
      symbols:
      - vm_load_string
      scope: symbols
      file_hash: sha256:4c4fd8a5e5fdf74824fba2666041a10ff4daf9a0214bf6ddeabe8c9e67fc60a6
      symbol_hashes:
        vm_load_string: sha256:cee098cc352143ede741ebb982ba6d15f7eac71b6667871500b4a5ac4d42bb2e
      missing_symbols: []
      content_hash: sha256:e17a288c5843ae74a5c3e12ef6048c2572a8793b06467613638d615ffc385958
    - path: os/StarryOS/kernel/src/syscall/fs/ctl.rs
      symbols:
      - sys_chroot
      scope: symbols
      file_hash: sha256:a42d57fc2422560978476f017ea2ae3d59e59be8c3f119e45fb5f18529d2e7e5
      symbol_hashes:
        sys_chroot: sha256:2445750c1d3c822f8438f9a1914fe47b5360157364ca20142ad673492d889756
      missing_symbols: []
      content_hash: sha256:928d58e7292bc7e8922d1000e5aabe85e9fdb3f1f6c3f84b52583584b92d0d55
    - path: os/arceos/modules/axfs-ng/src/fs_core/context.rs
      symbols:
      - new
      - resolve
      - resolve_inner
      - try_resolve_symlink
      scope: symbols
      file_hash: sha256:6cd56d9acec5dc2b33d0d931a4e147c7dcd13318fe706800a02503c2220f7204
      symbol_hashes:
        new: sha256:3d17bd68745b169b5dbdd92e4dae5756b1d41e3850eea66a0cf7be91f1c551b2
        resolve: sha256:14a2b52408caa4b091a4b90ec30e6412155884199bbc592741da38777fc3581a
        resolve_inner: sha256:702d76c45f2ff1046f5d437d0e459366482b7ef2e76b1cfb259d536be7b52cc5
        try_resolve_symlink: sha256:2577319f282965c000834bd77c6fd7e1f77f7d44f10b688767d6391bab4169f3
      missing_symbols: []
      content_hash: sha256:955067eb239a31c67297a10606806cadf346d537ebd469118db448e88e52f236
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_chroot 先读取用户路径，再经 FsContext 解析并要求目标为目录；路径读取或解析错误及 ENOTDIR 由 errno 层保真转换。
  LTP_EBF0020C32AD44C8:
    syscalls: *id307
    rule_version:
      id: LTP_EBF0020C32AD44C8
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ebf0020c32ad44c8ad58e315c1e1cb903e5ed0c419a287e8244869f99cd010d4
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_EC19C6410BBE0467:
    syscalls: *id308
    rule_version:
      id: LTP_EC19C6410BBE0467
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ec19c6410bbe046794ecd79ea7efcb5440012eeaef0061223f455112ff1abb4f
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_EC23768761E40E9F:
    syscalls: *id309
    rule_version: &id358
      id: LTP_EC23768761E40E9F
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ec23768761e40e9f99140715f9e6147dcc348f9f7bbdc7731948b1afb6d29d51
    status: covered
    static_check_refs:
    - STARRY_CAPSET_ABI
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_CAPSET_ABI:
          id: STARRY_CAPSET_ABI
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:fa04e3f3a184e594c6b2b6f1f9d43027f9104bdc8a675eb3555d76e5cfb0faed
      dynamic_tests: {}
    target_dependencies:
    - path: components/starry-vm/src/thin.rs
      symbols:
      - VmMutPtr
      - VmPtr
      scope: symbols
      file_hash: sha256:b787237758b16cc38fc20fa79234f62e2bad5d70235621818f9771c4a0810aa4
      symbol_hashes:
        VmMutPtr: sha256:35ae0c032d454211b5a4d3e0b11bf6bf854bd550d635855677666f26fb1f730a
        VmPtr: sha256:6c0ff10e65451fa76a4eb2caa472c0a96ff53459ae357d86f2dbf389f50e8804
      missing_symbols: []
      content_hash: sha256:1b7ca80cea190deec16a1cec479d83444169c6259f68ca0bf314edc58015fecd
    - path: os/StarryOS/kernel/src/syscall/task/ctl.rs
      symbols:
      - data_to_mask
      - sys_capset
      - validate_cap_header
      scope: symbols
      file_hash: sha256:901fc111c7b58af132705a41cf8a75d89164f522f89135f794e08b76a1ec05e9
      symbol_hashes:
        data_to_mask: sha256:83fc2bb0eb44d7806a59c49b19d8600aadfdbe3b4e893514102d99611ad985ff
        sys_capset: sha256:3e17536f5a7319b1ad18a17d39c88b715d8795162ccc1860d59845494d69265c
        validate_cap_header: sha256:f92b10dad6654ff4b7de228735357465447f4fc6010d9b0eb50afaae686cbf33
      missing_symbols: []
      content_hash: sha256:df372a3e9f4e00850aad57aaee664224ee6a290029e828efea476bb40d9b46a5
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_capset 校验 V3 ABI、自身线程与 capability 子集约束，更新当前线程凭据并成功返回 0。
  LTP_ED36488372A175F5:
    syscalls: *id310
    rule_version:
      id: LTP_ED36488372A175F5
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ed36488372a175f572327b2a4ffbb7ee1509564d2f52f87cc53af698d7eaf6ad
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_ED3F2AE7E59E6F12:
    syscalls: *id311
    rule_version:
      id: LTP_ED3F2AE7E59E6F12
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ed3f2ae7e59e6f12449fce7c967c0ee394349eeea8de7184501ffbbe24b39bec
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_EE1518958A8F7CC1:
    syscalls: *id312
    rule_version:
      id: LTP_EE1518958A8F7CC1
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ee1518958a8f7cc104b201aea93c7258d1fe238563ecaa79fd379a3f94b86448
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_EE7A979F212D6C0C:
    syscalls: *id313
    rule_version: &id359
      id: LTP_EE7A979F212D6C0C
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ee7a979f212d6c0c9e2e3e7cf8fe3078537cd1d9a5e51d2b9d1800e88e29a363
    status: covered
    static_check_refs:
    - STARRY_CHROOT_PATH
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_CHROOT_PATH:
          id: STARRY_CHROOT_PATH
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:357fbab1f149ef6fb3807966810bffa3366973f2c4f2c854bb821004e4a3753f
      dynamic_tests: {}
    target_dependencies:
    - path: components/axfs-ng-vfs/src/path.rs
      symbols:
      - verify_entry_name
      scope: symbols
      file_hash: sha256:6e44a62c3142a5ebecb4c5c4c93f2d06c24ff549457c5c8b6787c8e90e46c11e
      symbol_hashes:
        verify_entry_name: sha256:516c7b090800149dc2bf3b7312761813844477a67da496c991099780f62c7ce5
      missing_symbols: []
      content_hash: sha256:2b2482c278ed782ee473d1a44f6611931e19f6b8db3edb22a40b3333d6bf50a0
    - path: components/starry-vm/src/alloc.rs
      symbols:
      - vm_load_until_nul
      scope: symbols
      file_hash: sha256:06b13f8c1700e024de6382919ddc0f8c2bf772798654a38d9e7f41c18ab2032e
      symbol_hashes:
        vm_load_until_nul: sha256:f65607e74fce137d86a282539ef80615a63582cf551668aa44115ed3b4e49767
      missing_symbols: []
      content_hash: sha256:8d542c4492f2dfe413baf6453ad0fd2edc7ac82a1ba69e9c16ca0f5a27bd691c
    - path: os/StarryOS/kernel/src/mm/access.rs
      symbols:
      - vm_load_string
      scope: symbols
      file_hash: sha256:4c4fd8a5e5fdf74824fba2666041a10ff4daf9a0214bf6ddeabe8c9e67fc60a6
      symbol_hashes:
        vm_load_string: sha256:cee098cc352143ede741ebb982ba6d15f7eac71b6667871500b4a5ac4d42bb2e
      missing_symbols: []
      content_hash: sha256:e17a288c5843ae74a5c3e12ef6048c2572a8793b06467613638d615ffc385958
    - path: os/StarryOS/kernel/src/syscall/fs/ctl.rs
      symbols:
      - sys_chroot
      scope: symbols
      file_hash: sha256:a42d57fc2422560978476f017ea2ae3d59e59be8c3f119e45fb5f18529d2e7e5
      symbol_hashes:
        sys_chroot: sha256:2445750c1d3c822f8438f9a1914fe47b5360157364ca20142ad673492d889756
      missing_symbols: []
      content_hash: sha256:928d58e7292bc7e8922d1000e5aabe85e9fdb3f1f6c3f84b52583584b92d0d55
    - path: os/arceos/modules/axfs-ng/src/fs_core/context.rs
      symbols:
      - new
      - resolve
      - resolve_inner
      - try_resolve_symlink
      scope: symbols
      file_hash: sha256:6cd56d9acec5dc2b33d0d931a4e147c7dcd13318fe706800a02503c2220f7204
      symbol_hashes:
        new: sha256:3d17bd68745b169b5dbdd92e4dae5756b1d41e3850eea66a0cf7be91f1c551b2
        resolve: sha256:14a2b52408caa4b091a4b90ec30e6412155884199bbc592741da38777fc3581a
        resolve_inner: sha256:702d76c45f2ff1046f5d437d0e459366482b7ef2e76b1cfb259d536be7b52cc5
        try_resolve_symlink: sha256:2577319f282965c000834bd77c6fd7e1f77f7d44f10b688767d6391bab4169f3
      missing_symbols: []
      content_hash: sha256:955067eb239a31c67297a10606806cadf346d537ebd469118db448e88e52f236
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_chroot 解析目录位置后以该位置创建新的 FsContext，并返回 0，静态覆盖成功路径。
  LTP_EF5C1F365208AD31:
    syscalls: *id314
    rule_version:
      id: LTP_EF5C1F365208AD31
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ef5c1f365208ad3151d7a53443d6ed6ff0c0fbeca716601c062432a23043bae7
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_F1044C71B6626419:
    syscalls: *id315
    rule_version:
      id: LTP_F1044C71B6626419
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:f1044c71b66264190afeea58604122162821df88724d0f3a9e5b63ac98a3ea48
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: 规则依赖 socket 类型、监听或连接队列、地址长度、用户指针以及 exp_errno 等运行时状态；现有静态分支无法唯一确定预期结果。
  LTP_F202F3C3B02DEA0E:
    syscalls: *id316
    rule_version:
      id: LTP_F202F3C3B02DEA0E
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:f202f3c3b02dea0e6634d113d533b6a816eafdc78c86c34983862ea92a2bdaa6
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_F3200B697F38DD16:
    syscalls: *id317
    rule_version:
      id: LTP_F3200B697F38DD16
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:f3200b697f38dd16dd728a01f6d8986b402618b4821c5d5a4fe155be69464bc6
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_F3418C5C403B91FC:
    syscalls: *id318
    rule_version:
      id: LTP_F3418C5C403B91FC
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:f3418c5c403b91fc13bbab2d80e1b2c05b310be5bd1e672739a6b95a809c0208
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_F36F8C0CC1A6D840:
    syscalls: *id319
    rule_version:
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
    reason: 相关 Starry 内容指纹未变化，已跳过。
  LTP_F43EC0D01CCFD25A:
    syscalls: *id320
    rule_version:
      id: LTP_F43EC0D01CCFD25A
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:f43ec0d01ccfd25ac4dd3c4082864a81a6865fd2d33a7edd8aca614964fe2616
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_F6BB86F5DCC2FAC8:
    syscalls: *id321
    rule_version:
      id: LTP_F6BB86F5DCC2FAC8
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:f6bb86f5dcc2fac8464bad08ce2e6618eb095e35aeab4e9102598e90d725c1c8
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_F70FC66A56FBD769:
    syscalls: *id322
    rule_version:
      id: LTP_F70FC66A56FBD769
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:f70fc66a56fbd769284bfc5c23ca42e3abc7d54a1de2bac9c0ef3f614707ad91
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_F7998813C90A7A08:
    syscalls: *id323
    rule_version:
      id: LTP_F7998813C90A7A08
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:f7998813c90a7a080b3d06433b1f67f20f57e9a58a6ecd3ee851168e86389f2c
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_F8CDD57D76C8FA6C:
    syscalls: *id324
    rule_version:
      id: LTP_F8CDD57D76C8FA6C
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:f8cdd57d76c8fa6ca80724732e2773c1a4fe6c09ac6bcc0cdd61aba4431f958b
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_F9BF08369A08E5ED:
    syscalls: *id325
    rule_version:
      id: LTP_F9BF08369A08E5ED
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:f9bf08369a08e5ed4d4a0ff15288e2395e0bbe2a5414e7a7fff39799cb12acd7
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_FC5B16AB3C53A744:
    syscalls: *id326
    rule_version:
      id: LTP_FC5B16AB3C53A744
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:fc5b16ab3c53a744edca87ac69737e86b586e7fa8fdb3afc25acf0b3e394f5ef
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_FCA376B46A9873B0:
    syscalls: *id327
    rule_version:
      id: LTP_FCA376B46A9873B0
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:fca376b46a9873b02e521509666d25f9012fe2fafdad6f776326dc146bc0ac6a
    status: needs_review
    static_check_refs: []
    dynamic_test_refs: []
    entity_versions:
      static_checks: {}
      dynamic_tests: {}
    target_dependencies: []
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: access01 单一条件分支被上游过度展开为互相冲突的路径、mode 和结果组合；规则缺少文件模式、目录搜索权限与调用凭据状态，不能静态选定分支。
  LTP_FD1B65B0BCC88E0D:
    syscalls: *id328
    rule_version:
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
    reason: 相关 Starry 内容指纹未变化，已跳过。
  LTP_FEACDC300C3E1DD7:
    syscalls: *id329
    rule_version:
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
    reason: 相关 Starry 内容指纹未变化，已跳过。
  LTP_FF9C0F9669A39525:
    syscalls: *id330
    rule_version: &id360
      id: LTP_FF9C0F9669A39525
      generated_at_utc: '2026-07-15T03:09:52.149069Z'
      content_hash: sha256:ff9c0f9669a39525986267a75a9b66e6249d23f8939029c388c3f8f1c9ec1472
    status: covered
    static_check_refs:
    - STARRY_BATCH_ERRNO_TRANSLATION
    - STARRY_CHROOT_PATH
    dynamic_test_refs: []
    entity_versions:
      static_checks:
        STARRY_BATCH_ERRNO_TRANSLATION:
          id: STARRY_BATCH_ERRNO_TRANSLATION
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:e19f574ad1b857afc459fe1d55fbe4e71451eceeeeff1452ff74c6c7fec81a15
        STARRY_CHROOT_PATH:
          id: STARRY_CHROOT_PATH
          generated_at_utc: '2026-07-15T04:13:20.108411Z'
          content_hash: sha256:357fbab1f149ef6fb3807966810bffa3366973f2c4f2c854bb821004e4a3753f
      dynamic_tests: {}
    target_dependencies:
    - path: components/axerrno/src/lib.rs
      symbols: []
      scope: file
      file_hash: sha256:a94d230d7f4b07c158c929df62ba63188107d6730a15dff8871c128d420b37f7
      symbol_hashes: {}
      missing_symbols: []
      content_hash: sha256:3afe6feb7c29a71ed7166317a7a138c45b37ac9557817d98b565bfeac2408b6d
    - path: components/axfs-ng-vfs/src/path.rs
      symbols:
      - verify_entry_name
      scope: symbols
      file_hash: sha256:6e44a62c3142a5ebecb4c5c4c93f2d06c24ff549457c5c8b6787c8e90e46c11e
      symbol_hashes:
        verify_entry_name: sha256:516c7b090800149dc2bf3b7312761813844477a67da496c991099780f62c7ce5
      missing_symbols: []
      content_hash: sha256:2b2482c278ed782ee473d1a44f6611931e19f6b8db3edb22a40b3333d6bf50a0
    - path: components/starry-vm/src/alloc.rs
      symbols:
      - vm_load_until_nul
      scope: symbols
      file_hash: sha256:06b13f8c1700e024de6382919ddc0f8c2bf772798654a38d9e7f41c18ab2032e
      symbol_hashes:
        vm_load_until_nul: sha256:f65607e74fce137d86a282539ef80615a63582cf551668aa44115ed3b4e49767
      missing_symbols: []
      content_hash: sha256:8d542c4492f2dfe413baf6453ad0fd2edc7ac82a1ba69e9c16ca0f5a27bd691c
    - path: os/StarryOS/kernel/src/mm/access.rs
      symbols:
      - vm_load_string
      scope: symbols
      file_hash: sha256:4c4fd8a5e5fdf74824fba2666041a10ff4daf9a0214bf6ddeabe8c9e67fc60a6
      symbol_hashes:
        vm_load_string: sha256:cee098cc352143ede741ebb982ba6d15f7eac71b6667871500b4a5ac4d42bb2e
      missing_symbols: []
      content_hash: sha256:e17a288c5843ae74a5c3e12ef6048c2572a8793b06467613638d615ffc385958
    - path: os/StarryOS/kernel/src/syscall/fs/ctl.rs
      symbols:
      - sys_chroot
      scope: symbols
      file_hash: sha256:a42d57fc2422560978476f017ea2ae3d59e59be8c3f119e45fb5f18529d2e7e5
      symbol_hashes:
        sys_chroot: sha256:2445750c1d3c822f8438f9a1914fe47b5360157364ca20142ad673492d889756
      missing_symbols: []
      content_hash: sha256:928d58e7292bc7e8922d1000e5aabe85e9fdb3f1f6c3f84b52583584b92d0d55
    - path: os/arceos/modules/axfs-ng/src/fs_core/context.rs
      symbols:
      - new
      - resolve
      - resolve_inner
      - try_resolve_symlink
      scope: symbols
      file_hash: sha256:6cd56d9acec5dc2b33d0d931a4e147c7dcd13318fe706800a02503c2220f7204
      symbol_hashes:
        new: sha256:3d17bd68745b169b5dbdd92e4dae5756b1d41e3850eea66a0cf7be91f1c551b2
        resolve: sha256:14a2b52408caa4b091a4b90ec30e6412155884199bbc592741da38777fc3581a
        resolve_inner: sha256:702d76c45f2ff1046f5d437d0e459366482b7ef2e76b1cfb259d536be7b52cc5
        try_resolve_symlink: sha256:2577319f282965c000834bd77c6fd7e1f77f7d44f10b688767d6391bab4169f3
      missing_symbols: []
      content_hash: sha256:955067eb239a31c67297a10606806cadf346d537ebd469118db448e88e52f236
    repository_identity: sha256:ef2d04968be9b7795da3c8841a4e23c0947c0f004d7340dc4c0cc5c863ba9029
    target_descriptor_hash: sha256:81024595e5b8795d9756c55ed1b619e143db11820f2b10d6462080e617ef4e43
    last_verified_snapshot_hash: sha256:041c7ef6f3270ebaea6287f256ec78436ee9cddfac2d41c116066b2fd890067f
    last_processed_report: mapping-20260715t035919z-aa4629b5
    reason: sys_chroot 先读取用户路径，再经 FsContext 解析并要求目标为目录；路径读取或解析错误及 ENOTDIR 由 errno 层保真转换。
entity_versions:
  rules:
    LTP_0180982614AA9F7D: *id331
    LTP_044E7C11E6B503BB: *id332
    LTP_06891E2E299CF48E: *id333
    LTP_075318C437B76E06: *id334
    LTP_0799FC60BADD2B18: *id335
    LTP_0D1782EAAC26DEB4: *id336
    LTP_208C833FF12217F5: *id337
    LTP_245CD61DAA19DC98: *id338
    LTP_2F99FA84C445363C: *id339
    LTP_38FB918826669241: *id340
    LTP_4661BBF1B3CD3A1E: *id341
    LTP_58416E6747519699: *id342
    LTP_5F1D35ACCEFD4971: *id343
    LTP_67BF94A4ACD303C4: *id344
    LTP_6D86AFD541A61388: *id345
    LTP_711D5693356A79F2: *id346
    LTP_71C54C624831C7F0: *id347
    LTP_73DF50509BCC128B: *id348
    LTP_7A74A699442CEB99: *id349
    LTP_827CE5CB448A411B: *id350
    LTP_839EC7BC904E42D5: *id351
    LTP_8BB576EB2E1E6B23: *id352
    LTP_99DF5C34778032E1: *id353
    LTP_C8DAE34819E335F8: *id354
    LTP_E06D53042C10C99E: *id355
    LTP_E3E59B16A96A60BC: *id356
    LTP_EBD54180D0CAB16B: *id357
    LTP_EC23768761E40E9F: *id358
    LTP_EE7A979F212D6C0C: *id359
    LTP_FF9C0F9669A39525: *id360
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
remaining:
  all:
  - LTP_00F2A9EA8833DA1D
  - LTP_0290063892A53510
  - LTP_030858A5FFCCEFF4
  - LTP_035E62E6D1787773
  - LTP_036EDA2B8D36CF03
  - LTP_037E6F334D0E0D16
  - LTP_0431E3529AA0FEE8
  - LTP_060B6037DEF1D43C
  - LTP_06725D44DFF06F7E
  - LTP_06A0C295D8E7FAFA
  - LTP_06AC9297E35AAE7A
  - LTP_0A62800536904C02
  - LTP_0AAFA34BA77A0D25
  - LTP_0B45FC33068D334C
  - LTP_0BB235F712E819CE
  - LTP_0E9AF2C058AF8126
  - LTP_0F901C62092CC7B8
  - LTP_10A684C1C2D2DE0F
  - LTP_10FE1313FBAB5F92
  - LTP_1325C077A1CDE514
  - LTP_1402459B5FF9BF23
  - LTP_1465554B09CE14F0
  - LTP_148623FDAF4E478D
  - LTP_153B296FA599E0CE
  - LTP_17ACF3BE969B64EE
  - LTP_17CB4ED7A76BD283
  - LTP_1870C0046E9555AF
  - LTP_18A450CE49F8867B
  - LTP_198D9555A8BED013
  - LTP_1A9481FAD460FBF7
  - LTP_1BD36AE285B4F3E2
  - LTP_1C462AC54A29FF35
  - LTP_1CDCF5FE9ED1BE5D
  - LTP_1D39F97D759F0E57
  - LTP_1DF2B28499E4D7B3
  - LTP_212269CECE600FD8
  - LTP_21A007DF738F1E73
  - LTP_21C4957F9EFE94D3
  - LTP_220D1227D307AD3C
  - LTP_2221F954D01EB2BB
  - LTP_25639C9C5750C487
  - LTP_26AC646B9D18C353
  - LTP_277FD467E5F1BF1C
  - LTP_27C7E91095DB9DF8
  - LTP_2900BC64740A3E44
  - LTP_298AB67F0CFA519C
  - LTP_2B4171DD8FBD982A
  - LTP_2D0BAECAE4F61432
  - LTP_2E5D530A61E60934
  - LTP_2FA43CD942AE7AD6
  - LTP_2FE8FAD800DE41F6
  - LTP_3472CD1A0F8A2B4A
  - LTP_347761CBCF52D194
  - LTP_34CFEAD03DB6A3CA
  - LTP_34EC9FB9C9551214
  - LTP_35CAEE10A613E109
  - LTP_3636C4768C196B52
  - LTP_368D8689810796B2
  - LTP_3900F4E562AE09D1
  - LTP_3916A669595B3568
  - LTP_3AD3865603ADDC8E
  - LTP_3C2853617B38EEE7
  - LTP_3D4ECD22BC433164
  - LTP_3D8D38C9123CD051
  - LTP_3DE23AB4FE2FFC67
  - LTP_3E526A0A23B5EF6D
  - LTP_3E8DA9E014B82702
  - LTP_3F81436312777EF4
  - LTP_401D471D37C85820
  - LTP_461340ED83E7043D
  - LTP_46DE8D9AD1674F26
  - LTP_472AAA35C7382B26
  - LTP_479924116854D92B
  - LTP_48753F73ACA755FB
  - LTP_4881657CFE57C7E9
  - LTP_492D25A0F1055F72
  - LTP_4948E12FB8F9FA49
  - LTP_49700CDA955B66D8
  - LTP_49A36559B96D24AF
  - LTP_4B6E9B98E2E5103D
  - LTP_4CFAFCE7FCA2BF99
  - LTP_4ECB786BFA071AAC
  - LTP_50A86D4D5411356E
  - LTP_50F858A3CBF95EED
  - LTP_52C209105EE62171
  - LTP_5570480E7920BD0E
  - LTP_563FB650864E0DC6
  - LTP_58F1512157A0052D
  - LTP_5A315335586D4227
  - LTP_5C5CDC165410C08C
  - LTP_5CC44E5D1A6B6485
  - LTP_5D7971086B2ABAE5
  - LTP_5EC31E34822684C4
  - LTP_606B7E40B6BD82EA
  - LTP_613A5E121B4B6E68
  - LTP_6156A09A2E506F76
  - LTP_6169F41023E00C34
  - LTP_636590E5A017B28D
  - LTP_64227C746913D03D
  - LTP_6449E4A1D20C01D3
  - LTP_64A4E5DC71A633A2
  - LTP_65281FBEE0BF6103
  - LTP_6580B4D3FA1A86F3
  - LTP_65B70356F06E31F8
  - LTP_679436EC7A4E218A
  - LTP_68745D21F4EC2FF5
  - LTP_68E1B26815D97B79
  - LTP_69077B093E81B570
  - LTP_690A651C3A60FC1E
  - LTP_69E094D1DBFF3796
  - LTP_6A1A431A08A3F450
  - LTP_6B1746F6BB2266CA
  - LTP_6B8B5453E8B4E6DE
  - LTP_6C11BBB4AABA6E7C
  - LTP_6C55A3E760DF75DB
  - LTP_6CE9FC3BCA164B5D
  - LTP_6D584CE6CF9B8A06
  - LTP_6EF7ECD2A8470CEA
  - LTP_74819A9DC2B5CB06
  - LTP_752C9A802CF96B8B
  - LTP_76A9B6CF388A8609
  - LTP_78EEEBE648781151
  - LTP_7963C3DF373596FE
  - LTP_79C7516DECB19092
  - LTP_7A02B34D5FB8BBC3
  - LTP_7B539E14354153DC
  - LTP_7BE2877017694C52
  - LTP_7C06A3394E786948
  - LTP_7CE7876CE69F200F
  - LTP_7DD493976CBC9A31
  - LTP_7DEDC53AC33C891F
  - LTP_7F5487EEB79017AD
  - LTP_7F54F9DFF7E0FB61
  - LTP_7FD6142E0E88CF17
  - LTP_8059D9227293D592
  - LTP_807E2072E5694684
  - LTP_80C6DB0ACB2A5510
  - LTP_818BA624CA9E4040
  - LTP_820495EA1D1F15DA
  - LTP_82621B02FCA09F40
  - LTP_82ABB8FBFA06D356
  - LTP_82E0F55AEC3D382F
  - LTP_830E17210B1FB7AB
  - LTP_833C5D5CF3C32C2A
  - LTP_843BDD20FF921FC3
  - LTP_84E4CC971DD16EC2
  - LTP_853D34D061DDE8F8
  - LTP_853F4B8346648EB9
  - LTP_857DC6AD01A88D79
  - LTP_87478A6C3AC7DC60
  - LTP_884775F9076E54AB
  - LTP_885F3BA721198C07
  - LTP_88F6F279E33633DE
  - LTP_89C9E8458EC38C11
  - LTP_8AC11633EA3D83E0
  - LTP_8AD8032754BC8842
  - LTP_8B1A2084BCF096F1
  - LTP_8B3FBDFD0453EF40
  - LTP_8C508A50371B6444
  - LTP_8CB51F0A9F8FDEA1
  - LTP_8D3BFFA98E2561BA
  - LTP_8D54825D4B298C7C
  - LTP_8E7F1BE3D7D7823B
  - LTP_8F29388433422812
  - LTP_8FF73194288F8473
  - LTP_906135780505447D
  - LTP_911B97B972658989
  - LTP_919ABCA2598F53B5
  - LTP_921D4802D7690C64
  - LTP_9260E923CF8AA018
  - LTP_929B120944D8F805
  - LTP_93949494FBAD3568
  - LTP_94E36E221125BFAF
  - LTP_955ECE70D81CA226
  - LTP_96021AFB69E847F9
  - LTP_969C39F409BFD7AA
  - LTP_96D205FACA0DD8DB
  - LTP_96F07DC5DDC8E018
  - LTP_97C442AC56780374
  - LTP_9866FB6F1F726CA0
  - LTP_986F211E7D45CAD7
  - LTP_98EC66149EE68933
  - LTP_9A723EA0B1F0D1BE
  - LTP_9C9D222A34799D55
  - LTP_9CA9C6B61C3317A3
  - LTP_9CDCD3C4BA6C2702
  - LTP_A00E343F4A556B3D
  - LTP_A17272D4FE0F040B
  - LTP_A1DEE046C0A10B18
  - LTP_A30F7687D403407B
  - LTP_A4060315D2E047EE
  - LTP_A4733D4B2FEBE9A4
  - LTP_A500A46C4B998E74
  - LTP_A6B94E8A2A4D8853
  - LTP_A9544B59EB6712D9
  - LTP_A9596E932167B3EF
  - LTP_AB48F262BBB2CC93
  - LTP_AC0FB73B4EE420EC
  - LTP_AD81218450587FA8
  - LTP_ADD30BEEC40E661F
  - LTP_B1D822DF0057B4E0
  - LTP_B200AFD97E91C2CC
  - LTP_B53406D510ED4981
  - LTP_B6DAF13EF3143EBF
  - LTP_B7A341967DF2BD69
  - LTP_B90CB73F36B70C6F
  - LTP_B9908D4015443661
  - LTP_B9CDD41A0DC2AFCC
  - LTP_BA10984A4B0DE2C6
  - LTP_BA9A8FE901467960
  - LTP_BC662075E3BAE807
  - LTP_BE2E778739EF01D5
  - LTP_C0577C0D678214DA
  - LTP_C071A7FFF929A2A5
  - LTP_C0AA45BC29F98A0E
  - LTP_C1C67435FC56D878
  - LTP_C218D3CB0AD80D90
  - LTP_C5FE18F9550B31BA
  - LTP_C6A719982BDE9CE4
  - LTP_C6E67CB1FD2B1F64
  - LTP_C785774773FB7524
  - LTP_C7B73F4D5B87736A
  - LTP_C80C019BE3F47901
  - LTP_C994B56A41A71C1A
  - LTP_CA45A33676AD236D
  - LTP_CA80C3F10B65226D
  - LTP_CB31E19EE807FFDB
  - LTP_CCDB1776DAA2C318
  - LTP_CD2150BE4FE81F31
  - LTP_CDCDC1B9E63D58C3
  - LTP_CE45382D3DE75F8F
  - LTP_CEBAD6AB3C82795E
  - LTP_CED2FCC737A99D40
  - LTP_D0E32E5D27E643A9
  - LTP_D1AADFC2F7C6F594
  - LTP_D1B6112551D45B31
  - LTP_D1F469715ECC4195
  - LTP_D2D67AB5E38A7000
  - LTP_D2F4BCF2263C56F5
  - LTP_D412A09DEDC43045
  - LTP_D4B433A3696803A8
  - LTP_D4D8A0FEAA2F6B09
  - LTP_D579FCFC71E6EB6A
  - LTP_D653D15777B77A1F
  - LTP_D6A52FD61BF01578
  - LTP_D72526C4E4301D60
  - LTP_D76652434EC85091
  - LTP_D8B58CA743EBE711
  - LTP_DA10E351BC730D85
  - LTP_DAA03BAD070DB1D6
  - LTP_DAA1F16D8A298E83
  - LTP_DC9BC72148835FDC
  - LTP_DCB33BB29D296843
  - LTP_DD9A41090E3D5A17
  - LTP_DF1C4714B16B760E
  - LTP_E0B177A8B6FE4225
  - LTP_E0ED96B80FC3B6C9
  - LTP_E13B9C2C9645B841
  - LTP_E28B5BB57A450438
  - LTP_E2C3B68EDF07A753
  - LTP_E34945E3DE91022F
  - LTP_E3A3CF8B98E460BC
  - LTP_E41DD7230DA067DD
  - LTP_E46539F2D47BA5EC
  - LTP_E4D1B76D80905462
  - LTP_E560C027210BF20A
  - LTP_E5791B389C67677E
  - LTP_E5E50FB7BDD033D9
  - LTP_EB00EA74B30E438E
  - LTP_EB425D988F2F7604
  - LTP_EBF0020C32AD44C8
  - LTP_EC19C6410BBE0467
  - LTP_ED36488372A175F5
  - LTP_ED3F2AE7E59E6F12
  - LTP_EE1518958A8F7CC1
  - LTP_EF5C1F365208AD31
  - LTP_F1044C71B6626419
  - LTP_F202F3C3B02DEA0E
  - LTP_F3200B697F38DD16
  - LTP_F3418C5C403B91FC
  - LTP_F43EC0D01CCFD25A
  - LTP_F6BB86F5DCC2FAC8
  - LTP_F70FC66A56FBD769
  - LTP_F7998813C90A7A08
  - LTP_F8CDD57D76C8FA6C
  - LTP_F9BF08369A08E5ED
  - LTP_FC5B16AB3C53A744
  - LTP_FCA376B46A9873B0
  pending: []
  needs_review:
  - LTP_0290063892A53510
  - LTP_030858A5FFCCEFF4
  - LTP_035E62E6D1787773
  - LTP_036EDA2B8D36CF03
  - LTP_037E6F334D0E0D16
  - LTP_0431E3529AA0FEE8
  - LTP_060B6037DEF1D43C
  - LTP_06725D44DFF06F7E
  - LTP_06A0C295D8E7FAFA
  - LTP_06AC9297E35AAE7A
  - LTP_0A62800536904C02
  - LTP_0AAFA34BA77A0D25
  - LTP_0B45FC33068D334C
  - LTP_0BB235F712E819CE
  - LTP_0E9AF2C058AF8126
  - LTP_0F901C62092CC7B8
  - LTP_10A684C1C2D2DE0F
  - LTP_10FE1313FBAB5F92
  - LTP_1402459B5FF9BF23
  - LTP_1465554B09CE14F0
  - LTP_148623FDAF4E478D
  - LTP_153B296FA599E0CE
  - LTP_17ACF3BE969B64EE
  - LTP_17CB4ED7A76BD283
  - LTP_1870C0046E9555AF
  - LTP_18A450CE49F8867B
  - LTP_198D9555A8BED013
  - LTP_1BD36AE285B4F3E2
  - LTP_1C462AC54A29FF35
  - LTP_1CDCF5FE9ED1BE5D
  - LTP_1D39F97D759F0E57
  - LTP_1DF2B28499E4D7B3
  - LTP_212269CECE600FD8
  - LTP_21A007DF738F1E73
  - LTP_21C4957F9EFE94D3
  - LTP_220D1227D307AD3C
  - LTP_2221F954D01EB2BB
  - LTP_25639C9C5750C487
  - LTP_26AC646B9D18C353
  - LTP_277FD467E5F1BF1C
  - LTP_27C7E91095DB9DF8
  - LTP_2900BC64740A3E44
  - LTP_298AB67F0CFA519C
  - LTP_2B4171DD8FBD982A
  - LTP_2D0BAECAE4F61432
  - LTP_2E5D530A61E60934
  - LTP_2FA43CD942AE7AD6
  - LTP_2FE8FAD800DE41F6
  - LTP_3472CD1A0F8A2B4A
  - LTP_347761CBCF52D194
  - LTP_34CFEAD03DB6A3CA
  - LTP_35CAEE10A613E109
  - LTP_3636C4768C196B52
  - LTP_368D8689810796B2
  - LTP_3900F4E562AE09D1
  - LTP_3916A669595B3568
  - LTP_3AD3865603ADDC8E
  - LTP_3C2853617B38EEE7
  - LTP_3D4ECD22BC433164
  - LTP_3D8D38C9123CD051
  - LTP_3DE23AB4FE2FFC67
  - LTP_3E526A0A23B5EF6D
  - LTP_3F81436312777EF4
  - LTP_401D471D37C85820
  - LTP_461340ED83E7043D
  - LTP_46DE8D9AD1674F26
  - LTP_472AAA35C7382B26
  - LTP_479924116854D92B
  - LTP_48753F73ACA755FB
  - LTP_4881657CFE57C7E9
  - LTP_492D25A0F1055F72
  - LTP_4948E12FB8F9FA49
  - LTP_49700CDA955B66D8
  - LTP_49A36559B96D24AF
  - LTP_4B6E9B98E2E5103D
  - LTP_4CFAFCE7FCA2BF99
  - LTP_4ECB786BFA071AAC
  - LTP_50A86D4D5411356E
  - LTP_50F858A3CBF95EED
  - LTP_52C209105EE62171
  - LTP_5570480E7920BD0E
  - LTP_563FB650864E0DC6
  - LTP_58F1512157A0052D
  - LTP_5A315335586D4227
  - LTP_5C5CDC165410C08C
  - LTP_5CC44E5D1A6B6485
  - LTP_5D7971086B2ABAE5
  - LTP_5EC31E34822684C4
  - LTP_606B7E40B6BD82EA
  - LTP_613A5E121B4B6E68
  - LTP_6156A09A2E506F76
  - LTP_6169F41023E00C34
  - LTP_636590E5A017B28D
  - LTP_64227C746913D03D
  - LTP_64A4E5DC71A633A2
  - LTP_65281FBEE0BF6103
  - LTP_6580B4D3FA1A86F3
  - LTP_679436EC7A4E218A
  - LTP_68745D21F4EC2FF5
  - LTP_68E1B26815D97B79
  - LTP_69077B093E81B570
  - LTP_690A651C3A60FC1E
  - LTP_69E094D1DBFF3796
  - LTP_6A1A431A08A3F450
  - LTP_6B1746F6BB2266CA
  - LTP_6B8B5453E8B4E6DE
  - LTP_6C11BBB4AABA6E7C
  - LTP_6C55A3E760DF75DB
  - LTP_6CE9FC3BCA164B5D
  - LTP_6D584CE6CF9B8A06
  - LTP_6EF7ECD2A8470CEA
  - LTP_74819A9DC2B5CB06
  - LTP_752C9A802CF96B8B
  - LTP_78EEEBE648781151
  - LTP_7963C3DF373596FE
  - LTP_79C7516DECB19092
  - LTP_7A02B34D5FB8BBC3
  - LTP_7B539E14354153DC
  - LTP_7BE2877017694C52
  - LTP_7C06A3394E786948
  - LTP_7CE7876CE69F200F
  - LTP_7DD493976CBC9A31
  - LTP_7DEDC53AC33C891F
  - LTP_7F5487EEB79017AD
  - LTP_7F54F9DFF7E0FB61
  - LTP_8059D9227293D592
  - LTP_807E2072E5694684
  - LTP_80C6DB0ACB2A5510
  - LTP_818BA624CA9E4040
  - LTP_820495EA1D1F15DA
  - LTP_82ABB8FBFA06D356
  - LTP_82E0F55AEC3D382F
  - LTP_830E17210B1FB7AB
  - LTP_833C5D5CF3C32C2A
  - LTP_843BDD20FF921FC3
  - LTP_84E4CC971DD16EC2
  - LTP_853D34D061DDE8F8
  - LTP_853F4B8346648EB9
  - LTP_857DC6AD01A88D79
  - LTP_87478A6C3AC7DC60
  - LTP_884775F9076E54AB
  - LTP_885F3BA721198C07
  - LTP_88F6F279E33633DE
  - LTP_8AC11633EA3D83E0
  - LTP_8B1A2084BCF096F1
  - LTP_8B3FBDFD0453EF40
  - LTP_8C508A50371B6444
  - LTP_8CB51F0A9F8FDEA1
  - LTP_8D3BFFA98E2561BA
  - LTP_8D54825D4B298C7C
  - LTP_8E7F1BE3D7D7823B
  - LTP_8F29388433422812
  - LTP_8FF73194288F8473
  - LTP_906135780505447D
  - LTP_911B97B972658989
  - LTP_919ABCA2598F53B5
  - LTP_921D4802D7690C64
  - LTP_9260E923CF8AA018
  - LTP_929B120944D8F805
  - LTP_93949494FBAD3568
  - LTP_94E36E221125BFAF
  - LTP_955ECE70D81CA226
  - LTP_96021AFB69E847F9
  - LTP_969C39F409BFD7AA
  - LTP_96D205FACA0DD8DB
  - LTP_96F07DC5DDC8E018
  - LTP_97C442AC56780374
  - LTP_9866FB6F1F726CA0
  - LTP_986F211E7D45CAD7
  - LTP_9A723EA0B1F0D1BE
  - LTP_9C9D222A34799D55
  - LTP_9CA9C6B61C3317A3
  - LTP_9CDCD3C4BA6C2702
  - LTP_A00E343F4A556B3D
  - LTP_A17272D4FE0F040B
  - LTP_A1DEE046C0A10B18
  - LTP_A30F7687D403407B
  - LTP_A4060315D2E047EE
  - LTP_A4733D4B2FEBE9A4
  - LTP_A500A46C4B998E74
  - LTP_A6B94E8A2A4D8853
  - LTP_A9544B59EB6712D9
  - LTP_A9596E932167B3EF
  - LTP_AB48F262BBB2CC93
  - LTP_AC0FB73B4EE420EC
  - LTP_AD81218450587FA8
  - LTP_ADD30BEEC40E661F
  - LTP_B1D822DF0057B4E0
  - LTP_B200AFD97E91C2CC
  - LTP_B53406D510ED4981
  - LTP_B6DAF13EF3143EBF
  - LTP_B90CB73F36B70C6F
  - LTP_B9908D4015443661
  - LTP_B9CDD41A0DC2AFCC
  - LTP_BA10984A4B0DE2C6
  - LTP_BC662075E3BAE807
  - LTP_BE2E778739EF01D5
  - LTP_C0577C0D678214DA
  - LTP_C071A7FFF929A2A5
  - LTP_C0AA45BC29F98A0E
  - LTP_C1C67435FC56D878
  - LTP_C5FE18F9550B31BA
  - LTP_C6A719982BDE9CE4
  - LTP_C6E67CB1FD2B1F64
  - LTP_C994B56A41A71C1A
  - LTP_CA45A33676AD236D
  - LTP_CA80C3F10B65226D
  - LTP_CB31E19EE807FFDB
  - LTP_CCDB1776DAA2C318
  - LTP_CDCDC1B9E63D58C3
  - LTP_CE45382D3DE75F8F
  - LTP_CEBAD6AB3C82795E
  - LTP_CED2FCC737A99D40
  - LTP_D0E32E5D27E643A9
  - LTP_D1AADFC2F7C6F594
  - LTP_D1F469715ECC4195
  - LTP_D2D67AB5E38A7000
  - LTP_D2F4BCF2263C56F5
  - LTP_D412A09DEDC43045
  - LTP_D4D8A0FEAA2F6B09
  - LTP_D653D15777B77A1F
  - LTP_D6A52FD61BF01578
  - LTP_D72526C4E4301D60
  - LTP_D76652434EC85091
  - LTP_D8B58CA743EBE711
  - LTP_DA10E351BC730D85
  - LTP_DAA03BAD070DB1D6
  - LTP_DAA1F16D8A298E83
  - LTP_DC9BC72148835FDC
  - LTP_DCB33BB29D296843
  - LTP_DD9A41090E3D5A17
  - LTP_DF1C4714B16B760E
  - LTP_E0B177A8B6FE4225
  - LTP_E0ED96B80FC3B6C9
  - LTP_E13B9C2C9645B841
  - LTP_E28B5BB57A450438
  - LTP_E2C3B68EDF07A753
  - LTP_E34945E3DE91022F
  - LTP_E3A3CF8B98E460BC
  - LTP_E41DD7230DA067DD
  - LTP_E46539F2D47BA5EC
  - LTP_E4D1B76D80905462
  - LTP_E560C027210BF20A
  - LTP_E5791B389C67677E
  - LTP_E5E50FB7BDD033D9
  - LTP_EB00EA74B30E438E
  - LTP_EB425D988F2F7604
  - LTP_EBF0020C32AD44C8
  - LTP_EC19C6410BBE0467
  - LTP_ED36488372A175F5
  - LTP_ED3F2AE7E59E6F12
  - LTP_EE1518958A8F7CC1
  - LTP_EF5C1F365208AD31
  - LTP_F1044C71B6626419
  - LTP_F202F3C3B02DEA0E
  - LTP_F3200B697F38DD16
  - LTP_F3418C5C403B91FC
  - LTP_F43EC0D01CCFD25A
  - LTP_F6BB86F5DCC2FAC8
  - LTP_F70FC66A56FBD769
  - LTP_F7998813C90A7A08
  - LTP_F8CDD57D76C8FA6C
  - LTP_F9BF08369A08E5ED
  - LTP_FC5B16AB3C53A744
  - LTP_FCA376B46A9873B0
  unsupported:
  - LTP_00F2A9EA8833DA1D
  - LTP_1325C077A1CDE514
  - LTP_1A9481FAD460FBF7
  - LTP_34EC9FB9C9551214
  - LTP_3E8DA9E014B82702
  - LTP_6449E4A1D20C01D3
  - LTP_65B70356F06E31F8
  - LTP_76A9B6CF388A8609
  - LTP_7FD6142E0E88CF17
  - LTP_82621B02FCA09F40
  - LTP_89C9E8458EC38C11
  - LTP_8AD8032754BC8842
  - LTP_98EC66149EE68933
  - LTP_B7A341967DF2BD69
  - LTP_BA9A8FE901467960
  - LTP_C218D3CB0AD80D90
  - LTP_C785774773FB7524
  - LTP_C7B73F4D5B87736A
  - LTP_C80C019BE3F47901
  - LTP_CD2150BE4FE81F31
  - LTP_D1B6112551D45B31
  - LTP_D4B433A3696803A8
  - LTP_D579FCFC71E6EB6A
```
</details>
