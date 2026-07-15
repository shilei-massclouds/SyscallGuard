# Syscall 合规性规则提取报告

## 结论

本次分析了 abort、accept、accept4、access、acct、add_key、adjtimex、alarm、arch_prctl、bind、bpf、brk、cacheflush、cachestat、capget、capset、chdir、chmod、chown、chroot，发现 318 条可执行的合规性规则。

## `abort`

没有形成可发布的合规性规则。

## `accept`

共形成 7 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_277FD467E5F1BF1C`](../../library/rules/ltp-277fd467e5f1bf1c.yaml) | 无额外前置条件 | 调用 accept(socket_fd, (struct sockaddr *)3, &sizeof(fsin1)) | 返回 -1，errno 为 EINVAL |
| [`LTP_472AAA35C7382B26`](../../library/rules/ltp-472aaa35c7382b26.yaml) | 无额外前置条件 | 调用 accept(socket_fd, (struct sockaddr *)&fsin1, &1) | 返回 -1，errno 为 EINVAL |
| [`LTP_80C6DB0ACB2A5510`](../../library/rules/ltp-80c6db0acb2a5510.yaml) | 无额外前置条件 | 调用 accept(udp_fd, (struct sockaddr *)&fsin1, &sizeof(fsin1)) | 返回 -1，errno 为 EOPNOTSUPP |
| [`LTP_9CA9C6B61C3317A3`](../../library/rules/ltp-9ca9c6b61c3317a3.yaml) | 无额外前置条件 | 调用 accept(socket_fd, (struct sockaddr *)&fsin1, &sizeof(fsin1)) | 返回 -1，errno 为 EINVAL |
| [`LTP_B90CB73F36B70C6F`](../../library/rules/ltp-b90cb73f36b70c6f.yaml) | 无额外前置条件 | 调用 accept(server_sockfd, (struct sockaddr *)client_addr, &addr_len) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_E13B9C2C9645B841`](../../library/rules/ltp-e13b9c2c9645b841.yaml) | 无额外前置条件 | 调用 accept(invalid_socketfd, (struct sockaddr *)&fsin1, &sizeof(fsin1)) | 返回 -1，errno 为 EBADF |
| [`LTP_F1044C71B6626419`](../../library/rules/ltp-f1044c71b6626419.yaml) | 无额外前置条件 | 调用 accept(fd->fd, (void*)&addr, &size) | 返回 -1，errno 为 exp_errno |
## `accept4`

没有形成可发布的合规性规则。

## `access`

共形成 266 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0180982614AA9F7D`](../../library/rules/ltp-0180982614aa9f7d.yaml) | 无额外前置条件 | 调用 access(FNAME_R, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_0290063892A53510`](../../library/rules/ltp-0290063892a53510.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_X, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_030858A5FFCCEFF4`](../../library/rules/ltp-030858a5ffcceff4.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_R"/"FNAME_W, F_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_035E62E6D1787773`](../../library/rules/ltp-035e62e6d1787773.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_R, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_036EDA2B8D36CF03`](../../library/rules/ltp-036eda2b8d36cf03.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_X, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_037E6F334D0E0D16`](../../library/rules/ltp-037e6f334d0e0d16.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_R, F_OK) | 返回 -1，errno 为 0 |
| [`LTP_0431E3529AA0FEE8`](../../library/rules/ltp-0431e3529aa0fee8.yaml) | 无额外前置条件 | 调用 access(FNAME_RWX, R_OK|X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_044E7C11E6B503BB`](../../library/rules/ltp-044e7c11e6b503bb.yaml) | 无额外前置条件 | 调用 access(SNAME_W, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_060B6037DEF1D43C`](../../library/rules/ltp-060b6037def1d43c.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_R, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_06725D44DFF06F7E`](../../library/rules/ltp-06725d44dff06f7e.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_W, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_06891E2E299CF48E`](../../library/rules/ltp-06891e2e299cf48e.yaml) | 无额外前置条件 | 调用 access(SNAME_X, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_06A0C295D8E7FAFA`](../../library/rules/ltp-06a0c295d8e7fafa.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_W"/"FNAME_W, F_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_06AC9297E35AAE7A`](../../library/rules/ltp-06ac9297e35aae7a.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_R, F_OK) | 返回 -1，errno 为 0 |
| [`LTP_075318C437B76E06`](../../library/rules/ltp-075318c437b76e06.yaml) | BAD_USER_ADDRESS | 调用 access((void *)-1, R_OK) | 返回 -1，errno 为 EFAULT |
| [`LTP_0799FC60BADD2B18`](../../library/rules/ltp-0799fc60badd2b18.yaml) | BAD_USER_ADDRESS | 调用 access((void *)-1, X_OK) | 返回 -1，errno 为 EFAULT |
| [`LTP_0A62800536904C02`](../../library/rules/ltp-0a62800536904c02.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_R, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_0AAFA34BA77A0D25`](../../library/rules/ltp-0aafa34ba77a0d25.yaml) | 无额外前置条件 | 调用 access(FNAME_X, W_OK|X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_0B45FC33068D334C`](../../library/rules/ltp-0b45fc33068d334c.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_X, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_0BB235F712E819CE`](../../library/rules/ltp-0bb235f712e819ce.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_X, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_0D1782EAAC26DEB4`](../../library/rules/ltp-0d1782eaac26deb4.yaml) | 无额外前置条件 | 调用 access(FNAME_W, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_0E9AF2C058AF8126`](../../library/rules/ltp-0e9af2c058af8126.yaml) | 无额外前置条件 | 调用 access(FNAME_X, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_0F901C62092CC7B8`](../../library/rules/ltp-0f901c62092cc7b8.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_R"/"FNAME_X, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_10A684C1C2D2DE0F`](../../library/rules/ltp-10a684c1c2d2de0f.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_W, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_10FE1313FBAB5F92`](../../library/rules/ltp-10fe1313fbab5f92.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_X, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_1402459B5FF9BF23`](../../library/rules/ltp-1402459b5ff9bf23.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_W"/"FNAME_W, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_1465554B09CE14F0`](../../library/rules/ltp-1465554b09ce14f0.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_RW"/"FNAME_R, F_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_148623FDAF4E478D`](../../library/rules/ltp-148623fdaf4e478d.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_W, F_OK) | 返回 -1，errno 为 0 |
| [`LTP_153B296FA599E0CE`](../../library/rules/ltp-153b296fa599e0ce.yaml) | PERMISSION_DENIED_STATE | 调用 access(FNAME_X, R_OK|W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_17ACF3BE969B64EE`](../../library/rules/ltp-17acf3be969b64ee.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_X, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_17CB4ED7A76BD283`](../../library/rules/ltp-17cb4ed7a76bd283.yaml) | 无额外前置条件 | 调用 access(FNAME_W, R_OK|W_OK) | 返回 -1，errno 为 0 |
| [`LTP_1870C0046E9555AF`](../../library/rules/ltp-1870c0046e9555af.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_RW"/"FNAME_X, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_18A450CE49F8867B`](../../library/rules/ltp-18a450ce49f8867b.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_X, F_OK) | 返回 -1，errno 为 0 |
| [`LTP_198D9555A8BED013`](../../library/rules/ltp-198d9555a8bed013.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_X, X_OK) | 返回 -1，errno 为 0 |
| [`LTP_1BD36AE285B4F3E2`](../../library/rules/ltp-1bd36ae285b4f3e2.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_W"/"FNAME_X, F_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_1C462AC54A29FF35`](../../library/rules/ltp-1c462ac54a29ff35.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_W, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_1CDCF5FE9ED1BE5D`](../../library/rules/ltp-1cdcf5fe9ed1be5d.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_W, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_1D39F97D759F0E57`](../../library/rules/ltp-1d39f97d759f0e57.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_R, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_1DF2B28499E4D7B3`](../../library/rules/ltp-1df2b28499e4d7b3.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_X"/"FNAME_X, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_212269CECE600FD8`](../../library/rules/ltp-212269cece600fd8.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_X, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_21A007DF738F1E73`](../../library/rules/ltp-21a007df738f1e73.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_W"/"FNAME_R, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_21C4957F9EFE94D3`](../../library/rules/ltp-21c4957f9efe94d3.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_W, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_220D1227D307AD3C`](../../library/rules/ltp-220d1227d307ad3c.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_R"/"FNAME_W, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_2221F954D01EB2BB`](../../library/rules/ltp-2221f954d01eb2bb.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_RX"/"FNAME_W, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_25639C9C5750C487`](../../library/rules/ltp-25639c9c5750c487.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_W, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_26AC646B9D18C353`](../../library/rules/ltp-26ac646b9d18c353.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_W, F_OK) | 返回 -1，errno 为 0 |
| [`LTP_27C7E91095DB9DF8`](../../library/rules/ltp-27c7e91095db9df8.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_X, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_2900BC64740A3E44`](../../library/rules/ltp-2900bc64740a3e44.yaml) | PERMISSION_DENIED_STATE | 调用 access(FNAME_X, W_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_298AB67F0CFA519C`](../../library/rules/ltp-298ab67f0cfa519c.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_R"/"FNAME_X, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_2B4171DD8FBD982A`](../../library/rules/ltp-2b4171dd8fbd982a.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_X, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_2D0BAECAE4F61432`](../../library/rules/ltp-2d0baecae4f61432.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_R, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_2E5D530A61E60934`](../../library/rules/ltp-2e5d530a61e60934.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_W, F_OK) | 返回 -1，errno 为 0 |
| [`LTP_2F99FA84C445363C`](../../library/rules/ltp-2f99fa84c445363c.yaml) | NON_DIRECTORY_PATH_COMPONENT | 调用 access(fname2, R_OK) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_2FA43CD942AE7AD6`](../../library/rules/ltp-2fa43cd942ae7ad6.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_R, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_2FE8FAD800DE41F6`](../../library/rules/ltp-2fe8fad800de41f6.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_W, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_3472CD1A0F8A2B4A`](../../library/rules/ltp-3472cd1a0f8a2b4a.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_X, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_347761CBCF52D194`](../../library/rules/ltp-347761cbcf52d194.yaml) | 无额外前置条件 | 调用 access(FNAME_RWX, W_OK|X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_34CFEAD03DB6A3CA`](../../library/rules/ltp-34cfead03db6a3ca.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_R, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_35CAEE10A613E109`](../../library/rules/ltp-35caee10a613e109.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_R, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_3636C4768C196B52`](../../library/rules/ltp-3636c4768c196b52.yaml) | 无额外前置条件 | 调用 access(FNAME_X, X_OK) | 返回 -1，errno 为 0 |
| [`LTP_368D8689810796B2`](../../library/rules/ltp-368d8689810796b2.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_W, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_38FB918826669241`](../../library/rules/ltp-38fb918826669241.yaml) | BAD_USER_ADDRESS | 调用 access((void *)-1, W_OK) | 返回 -1，errno 为 EFAULT |
| [`LTP_3900F4E562AE09D1`](../../library/rules/ltp-3900f4e562ae09d1.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_X, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_3916A669595B3568`](../../library/rules/ltp-3916a669595b3568.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_W, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_3AD3865603ADDC8E`](../../library/rules/ltp-3ad3865603addc8e.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_X"/"FNAME_R, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_3C2853617B38EEE7`](../../library/rules/ltp-3c2853617b38eee7.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_R, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_3D4ECD22BC433164`](../../library/rules/ltp-3d4ecd22bc433164.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_R"/"FNAME_R, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_3D8D38C9123CD051`](../../library/rules/ltp-3d8d38c9123cd051.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_RW"/"FNAME_X, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_3DE23AB4FE2FFC67`](../../library/rules/ltp-3de23ab4fe2ffc67.yaml) | PERMISSION_DENIED_STATE | 调用 access(FNAME_X, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_3E526A0A23B5EF6D`](../../library/rules/ltp-3e526a0a23b5ef6d.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_R, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_3F81436312777EF4`](../../library/rules/ltp-3f81436312777ef4.yaml) | 无额外前置条件 | 调用 access(FNAME_W, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_401D471D37C85820`](../../library/rules/ltp-401d471d37c85820.yaml) | 无额外前置条件 | 调用 access(FNAME_R, W_OK|X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_4661BBF1B3CD3A1E`](../../library/rules/ltp-4661bbf1b3cd3a1e.yaml) | NONEXISTENT_PATH | 调用 access(empty_fname, W_OK) | 返回 -1，errno 为 ENOENT |
| [`LTP_46DE8D9AD1674F26`](../../library/rules/ltp-46de8d9ad1674f26.yaml) | 无额外前置条件 | 调用 access(FNAME_RWX, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_479924116854D92B`](../../library/rules/ltp-479924116854d92b.yaml) | 无额外前置条件 | 调用 access(FNAME_RWX, W_OK|X_OK) | 返回 -1，errno 为 0 |
| [`LTP_48753F73ACA755FB`](../../library/rules/ltp-48753f73aca755fb.yaml) | 无额外前置条件 | 调用 access(FNAME_X, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_4881657CFE57C7E9`](../../library/rules/ltp-4881657cfe57c7e9.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_R, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_492D25A0F1055F72`](../../library/rules/ltp-492d25a0f1055f72.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_X, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_4948E12FB8F9FA49`](../../library/rules/ltp-4948e12fb8f9fa49.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_W"/"FNAME_W, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_49700CDA955B66D8`](../../library/rules/ltp-49700cda955b66d8.yaml) | 无额外前置条件 | 调用 access(FNAME_R, R_OK|W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_49A36559B96D24AF`](../../library/rules/ltp-49a36559b96d24af.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_W, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_4B6E9B98E2E5103D`](../../library/rules/ltp-4b6e9b98e2e5103d.yaml) | 无额外前置条件 | 调用 access(FNAME_RWX, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_4CFAFCE7FCA2BF99`](../../library/rules/ltp-4cfafce7fca2bf99.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_R, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_4ECB786BFA071AAC`](../../library/rules/ltp-4ecb786bfa071aac.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_X, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_50A86D4D5411356E`](../../library/rules/ltp-50a86d4d5411356e.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_W, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_52C209105EE62171`](../../library/rules/ltp-52c209105ee62171.yaml) | PERMISSION_DENIED_STATE | 调用 access(FNAME_W, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_5570480E7920BD0E`](../../library/rules/ltp-5570480e7920bd0e.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_WX"/"FNAME_W, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_563FB650864E0DC6`](../../library/rules/ltp-563fb650864e0dc6.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_X"/"FNAME_R, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_58416E6747519699`](../../library/rules/ltp-58416e6747519699.yaml) | BAD_USER_ADDRESS | 调用 access((void *)-1, F_OK) | 返回 -1，errno 为 EFAULT |
| [`LTP_58F1512157A0052D`](../../library/rules/ltp-58f1512157a0052d.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_RW"/"FNAME_W, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_5A315335586D4227`](../../library/rules/ltp-5a315335586d4227.yaml) | 无额外前置条件 | 调用 access(FNAME_X, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_5C5CDC165410C08C`](../../library/rules/ltp-5c5cdc165410c08c.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_X, F_OK) | 返回 -1，errno 为 0 |
| [`LTP_5CC44E5D1A6B6485`](../../library/rules/ltp-5cc44e5d1a6b6485.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_R"/"FNAME_R, F_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_5D7971086B2ABAE5`](../../library/rules/ltp-5d7971086b2abae5.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_W, F_OK) | 返回 -1，errno 为 0 |
| [`LTP_5EC31E34822684C4`](../../library/rules/ltp-5ec31e34822684c4.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_RW"/"FNAME_W, F_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_606B7E40B6BD82EA`](../../library/rules/ltp-606b7e40b6bd82ea.yaml) | 无额外前置条件 | 调用 access(FNAME_W, R_OK|X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_613A5E121B4B6E68`](../../library/rules/ltp-613a5e121b4b6e68.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_W, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_6156A09A2E506F76`](../../library/rules/ltp-6156a09a2e506f76.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_R, F_OK) | 返回 -1，errno 为 0 |
| [`LTP_6169F41023E00C34`](../../library/rules/ltp-6169f41023e00c34.yaml) | 无额外前置条件 | 调用 access(FNAME_R, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_636590E5A017B28D`](../../library/rules/ltp-636590e5a017b28d.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_W, F_OK) | 返回 -1，errno 为 0 |
| [`LTP_64227C746913D03D`](../../library/rules/ltp-64227c746913d03d.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_W, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_64A4E5DC71A633A2`](../../library/rules/ltp-64a4e5dc71a633a2.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_X, F_OK) | 返回 -1，errno 为 0 |
| [`LTP_65281FBEE0BF6103`](../../library/rules/ltp-65281fbee0bf6103.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_X, X_OK) | 返回 -1，errno 为 0 |
| [`LTP_6580B4D3FA1A86F3`](../../library/rules/ltp-6580b4d3fa1a86f3.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_R, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_679436EC7A4E218A`](../../library/rules/ltp-679436ec7a4e218a.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_R, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_67BF94A4ACD303C4`](../../library/rules/ltp-67bf94a4acd303c4.yaml) | 无额外前置条件 | 调用 access(FNAME_F, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_68745D21F4EC2FF5`](../../library/rules/ltp-68745d21f4ec2ff5.yaml) | 无额外前置条件 | 调用 access(FNAME_X, R_OK|W_OK) | 返回 -1，errno 为 0 |
| [`LTP_68E1B26815D97B79`](../../library/rules/ltp-68e1b26815d97b79.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_R, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_69077B093E81B570`](../../library/rules/ltp-69077b093e81b570.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_W, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_690A651C3A60FC1E`](../../library/rules/ltp-690a651c3a60fc1e.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_R, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_69E094D1DBFF3796`](../../library/rules/ltp-69e094d1dbff3796.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_X, F_OK) | 返回 -1，errno 为 0 |
| [`LTP_6A1A431A08A3F450`](../../library/rules/ltp-6a1a431a08a3f450.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_W, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_6B1746F6BB2266CA`](../../library/rules/ltp-6b1746f6bb2266ca.yaml) | 无额外前置条件 | 调用 access(FNAME_RWX, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_6B8B5453E8B4E6DE`](../../library/rules/ltp-6b8b5453e8b4e6de.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_W, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_6C11BBB4AABA6E7C`](../../library/rules/ltp-6c11bbb4aaba6e7c.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_R"/"FNAME_W, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_6C55A3E760DF75DB`](../../library/rules/ltp-6c55a3e760df75db.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_R"/"FNAME_W, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_6CE9FC3BCA164B5D`](../../library/rules/ltp-6ce9fc3bca164b5d.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_X, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_6D584CE6CF9B8A06`](../../library/rules/ltp-6d584ce6cf9b8a06.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_W, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_6EF7ECD2A8470CEA`](../../library/rules/ltp-6ef7ecd2a8470cea.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_R, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_711D5693356A79F2`](../../library/rules/ltp-711d5693356a79f2.yaml) | 无额外前置条件 | 调用 access(SNAME_R, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_73DF50509BCC128B`](../../library/rules/ltp-73df50509bcc128b.yaml) | 无额外前置条件 | 调用 access(SNAME_F, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_74819A9DC2B5CB06`](../../library/rules/ltp-74819a9dc2b5cb06.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_X, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_752C9A802CF96B8B`](../../library/rules/ltp-752c9a802cf96b8b.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_R, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_78EEEBE648781151`](../../library/rules/ltp-78eeebe648781151.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_RW"/"FNAME_R, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_7963C3DF373596FE`](../../library/rules/ltp-7963c3df373596fe.yaml) | 无额外前置条件 | 调用 access(FNAME_W, W_OK|X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_79C7516DECB19092`](../../library/rules/ltp-79c7516decb19092.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_X"/"FNAME_X, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_7A02B34D5FB8BBC3`](../../library/rules/ltp-7a02b34d5fb8bbc3.yaml) | PERMISSION_DENIED_STATE | 调用 access(FNAME_X, R_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_7B539E14354153DC`](../../library/rules/ltp-7b539e14354153dc.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_RW"/"FNAME_W, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_7BE2877017694C52`](../../library/rules/ltp-7be2877017694c52.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_RW"/"FNAME_R, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_7C06A3394E786948`](../../library/rules/ltp-7c06a3394e786948.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_X, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_7CE7876CE69F200F`](../../library/rules/ltp-7ce7876ce69f200f.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_X, X_OK) | 返回 -1，errno 为 0 |
| [`LTP_7DD493976CBC9A31`](../../library/rules/ltp-7dd493976cbc9a31.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_X, X_OK) | 返回 -1，errno 为 0 |
| [`LTP_7F5487EEB79017AD`](../../library/rules/ltp-7f5487eeb79017ad.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_W, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_7F54F9DFF7E0FB61`](../../library/rules/ltp-7f54f9dff7e0fb61.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_X, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_8059D9227293D592`](../../library/rules/ltp-8059d9227293d592.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_R, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_807E2072E5694684`](../../library/rules/ltp-807e2072e5694684.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_R, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_818BA624CA9E4040`](../../library/rules/ltp-818ba624ca9e4040.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_X, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_820495EA1D1F15DA`](../../library/rules/ltp-820495ea1d1f15da.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_WX"/"FNAME_X, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_82ABB8FBFA06D356`](../../library/rules/ltp-82abb8fbfa06d356.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_RX"/"FNAME_X, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_82E0F55AEC3D382F`](../../library/rules/ltp-82e0f55aec3d382f.yaml) | 无额外前置条件 | 调用 access(mnt_point, W_OK) | 返回 -1，errno 为 EROFS |
| [`LTP_830E17210B1FB7AB`](../../library/rules/ltp-830e17210b1fb7ab.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_X, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_833C5D5CF3C32C2A`](../../library/rules/ltp-833c5d5cf3c32c2a.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_RW"/"FNAME_W, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_839EC7BC904E42D5`](../../library/rules/ltp-839ec7bc904e42d5.yaml) | 无额外前置条件 | 调用 access(FNAME_X, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_843BDD20FF921FC3`](../../library/rules/ltp-843bdd20ff921fc3.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_X, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_84E4CC971DD16EC2`](../../library/rules/ltp-84e4cc971dd16ec2.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_R"/"FNAME_X, F_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_853D34D061DDE8F8`](../../library/rules/ltp-853d34d061dde8f8.yaml) | 无额外前置条件 | 调用 access(FNAME_W, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_853F4B8346648EB9`](../../library/rules/ltp-853f4b8346648eb9.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_X"/"FNAME_W, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_857DC6AD01A88D79`](../../library/rules/ltp-857dc6ad01a88d79.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_W, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_87478A6C3AC7DC60`](../../library/rules/ltp-87478a6c3ac7dc60.yaml) | PERMISSION_DENIED_STATE | 调用 access(FNAME_X, R_OK|W_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_884775F9076E54AB`](../../library/rules/ltp-884775f9076e54ab.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_W, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_885F3BA721198C07`](../../library/rules/ltp-885f3ba721198c07.yaml) | 无额外前置条件 | 调用 access(FNAME_X, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_88F6F279E33633DE`](../../library/rules/ltp-88f6f279e33633de.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_W"/"FNAME_X, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_8AC11633EA3D83E0`](../../library/rules/ltp-8ac11633ea3d83e0.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_W"/"FNAME_R, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_8B1A2084BCF096F1`](../../library/rules/ltp-8b1a2084bcf096f1.yaml) | PERMISSION_DENIED_STATE | 调用 access(FNAME_W, R_OK|W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_8B3FBDFD0453EF40`](../../library/rules/ltp-8b3fbdfd0453ef40.yaml) | 无额外前置条件 | 调用 access(FNAME_X, R_OK|X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_8BB576EB2E1E6B23`](../../library/rules/ltp-8bb576eb2e1e6b23.yaml) | SYMLINK_LOOP | 调用 access(sname1, R_OK) | 返回 -1，errno 为 ELOOP |
| [`LTP_8C508A50371B6444`](../../library/rules/ltp-8c508a50371b6444.yaml) | PERMISSION_DENIED_STATE | 调用 access(FNAME_R, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_8CB51F0A9F8FDEA1`](../../library/rules/ltp-8cb51f0a9f8fdea1.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_X, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_8D3BFFA98E2561BA`](../../library/rules/ltp-8d3bffa98e2561ba.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_WX"/"FNAME_X, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_8D54825D4B298C7C`](../../library/rules/ltp-8d54825d4b298c7c.yaml) | PERMISSION_DENIED_STATE | 调用 access(FNAME_R, R_OK|W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_8E7F1BE3D7D7823B`](../../library/rules/ltp-8e7f1be3d7d7823b.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_X, X_OK) | 返回 -1，errno 为 0 |
| [`LTP_8F29388433422812`](../../library/rules/ltp-8f29388433422812.yaml) | 文件描述符无效 | 调用 access(fname1, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_8FF73194288F8473`](../../library/rules/ltp-8ff73194288f8473.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_X, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_906135780505447D`](../../library/rules/ltp-906135780505447d.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_R, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_911B97B972658989`](../../library/rules/ltp-911b97b972658989.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_WX"/"FNAME_W, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_919ABCA2598F53B5`](../../library/rules/ltp-919abca2598f53b5.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_RW"/"FNAME_R, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_921D4802D7690C64`](../../library/rules/ltp-921d4802d7690c64.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_X, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_9260E923CF8AA018`](../../library/rules/ltp-9260e923cf8aa018.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_R, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_929B120944D8F805`](../../library/rules/ltp-929b120944d8f805.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_W, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_93949494FBAD3568`](../../library/rules/ltp-93949494fbad3568.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_RX"/"FNAME_R, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_94E36E221125BFAF`](../../library/rules/ltp-94e36e221125bfaf.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_W, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_955ECE70D81CA226`](../../library/rules/ltp-955ece70d81ca226.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_W"/"FNAME_X, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_96021AFB69E847F9`](../../library/rules/ltp-96021afb69e847f9.yaml) | 无额外前置条件 | 调用 access(FNAME_RWX, X_OK) | 返回 -1，errno 为 0 |
| [`LTP_969C39F409BFD7AA`](../../library/rules/ltp-969c39f409bfd7aa.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_X, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_96D205FACA0DD8DB`](../../library/rules/ltp-96d205faca0dd8db.yaml) | 无额外前置条件 | 调用 access(FNAME_R, R_OK|X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_96F07DC5DDC8E018`](../../library/rules/ltp-96f07dc5ddc8e018.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_R, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_97C442AC56780374`](../../library/rules/ltp-97c442ac56780374.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_RX"/"FNAME_W, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_9866FB6F1F726CA0`](../../library/rules/ltp-9866fb6f1f726ca0.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_W, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_986F211E7D45CAD7`](../../library/rules/ltp-986f211e7d45cad7.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_W, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_9A723EA0B1F0D1BE`](../../library/rules/ltp-9a723ea0b1f0d1be.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_X, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_9C9D222A34799D55`](../../library/rules/ltp-9c9d222a34799d55.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_X, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_9CDCD3C4BA6C2702`](../../library/rules/ltp-9cdcd3c4ba6c2702.yaml) | 无额外前置条件 | 调用 access(FNAME_RWX, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_A17272D4FE0F040B`](../../library/rules/ltp-a17272d4fe0f040b.yaml) | 无额外前置条件 | 调用 access(FNAME_X, R_OK|W_OK|X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_A1DEE046C0A10B18`](../../library/rules/ltp-a1dee046c0a10b18.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_WX"/"FNAME_R, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_A30F7687D403407B`](../../library/rules/ltp-a30f7687d403407b.yaml) | 无额外前置条件 | 调用 access(FNAME_RWX, R_OK|W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_A4060315D2E047EE`](../../library/rules/ltp-a4060315d2e047ee.yaml) | PERMISSION_DENIED_STATE | 调用 access(FNAME_R, R_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_A4733D4B2FEBE9A4`](../../library/rules/ltp-a4733d4b2febe9a4.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_X, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_A500A46C4B998E74`](../../library/rules/ltp-a500a46c4b998e74.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_W"/"FNAME_R, F_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_A6B94E8A2A4D8853`](../../library/rules/ltp-a6b94e8a2a4d8853.yaml) | 无额外前置条件 | 调用 access(FNAME_RWX, R_OK|X_OK) | 返回 -1，errno 为 0 |
| [`LTP_A9544B59EB6712D9`](../../library/rules/ltp-a9544b59eb6712d9.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_W, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_A9596E932167B3EF`](../../library/rules/ltp-a9596e932167b3ef.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_R, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_AB48F262BBB2CC93`](../../library/rules/ltp-ab48f262bbb2cc93.yaml) | PERMISSION_DENIED_STATE | 调用 access(FNAME_X, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_AC0FB73B4EE420EC`](../../library/rules/ltp-ac0fb73b4ee420ec.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_X, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_AD81218450587FA8`](../../library/rules/ltp-ad81218450587fa8.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_W, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_ADD30BEEC40E661F`](../../library/rules/ltp-add30beec40e661f.yaml) | PERMISSION_DENIED_STATE | 调用 access(FNAME_R, W_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_B1D822DF0057B4E0`](../../library/rules/ltp-b1d822df0057b4e0.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_R"/"FNAME_R, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_B200AFD97E91C2CC`](../../library/rules/ltp-b200afd97e91c2cc.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_W, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_B53406D510ED4981`](../../library/rules/ltp-b53406d510ed4981.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_W, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_B6DAF13EF3143EBF`](../../library/rules/ltp-b6daf13ef3143ebf.yaml) | 无额外前置条件 | 调用 access(FNAME_R, R_OK|W_OK|X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_B9908D4015443661`](../../library/rules/ltp-b9908d4015443661.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_R, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_B9CDD41A0DC2AFCC`](../../library/rules/ltp-b9cdd41a0dc2afcc.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_R, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_BA10984A4B0DE2C6`](../../library/rules/ltp-ba10984a4b0de2c6.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_R, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_BC662075E3BAE807`](../../library/rules/ltp-bc662075e3bae807.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_R, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_BE2E778739EF01D5`](../../library/rules/ltp-be2e778739ef01d5.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_X, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_C0577C0D678214DA`](../../library/rules/ltp-c0577c0d678214da.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_W, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_C071A7FFF929A2A5`](../../library/rules/ltp-c071a7fff929a2a5.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_R"/"FNAME_X, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_C0AA45BC29F98A0E`](../../library/rules/ltp-c0aa45bc29f98a0e.yaml) | 无额外前置条件 | 调用 access(FNAME_R, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_C1C67435FC56D878`](../../library/rules/ltp-c1c67435fc56d878.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_R"/"FNAME_R, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_C5FE18F9550B31BA`](../../library/rules/ltp-c5fe18f9550b31ba.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_X, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_C6A719982BDE9CE4`](../../library/rules/ltp-c6a719982bde9ce4.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_WX"/"FNAME_R, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_C6E67CB1FD2B1F64`](../../library/rules/ltp-c6e67cb1fd2b1f64.yaml) | PERMISSION_DENIED_STATE | 调用 access(FNAME_W, W_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_C8DAE34819E335F8`](../../library/rules/ltp-c8dae34819e335f8.yaml) | PATH_TOO_LONG | 调用 access(longpathname, R_OK) | 返回 -1，errno 为 ENAMETOOLONG |
| [`LTP_C994B56A41A71C1A`](../../library/rules/ltp-c994b56a41a71c1a.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_X, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_CA45A33676AD236D`](../../library/rules/ltp-ca45a33676ad236d.yaml) | 无额外前置条件 | 调用 access(FNAME_W, R_OK|W_OK|X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_CA80C3F10B65226D`](../../library/rules/ltp-ca80c3f10b65226d.yaml) | 无额外前置条件 | 调用 access(FNAME_R, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_CB31E19EE807FFDB`](../../library/rules/ltp-cb31e19ee807ffdb.yaml) | PERMISSION_DENIED_STATE | 调用 access(FNAME_R, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_CCDB1776DAA2C318`](../../library/rules/ltp-ccdb1776daa2c318.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_W"/"FNAME_X, W_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_CDCDC1B9E63D58C3`](../../library/rules/ltp-cdcdc1b9e63d58c3.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_R, F_OK) | 返回 -1，errno 为 0 |
| [`LTP_CE45382D3DE75F8F`](../../library/rules/ltp-ce45382d3de75f8f.yaml) | PERMISSION_DENIED_STATE | 调用 access(FNAME_R, R_OK|W_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_CEBAD6AB3C82795E`](../../library/rules/ltp-cebad6ab3c82795e.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_W, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_D1F469715ECC4195`](../../library/rules/ltp-d1f469715ecc4195.yaml) | PERMISSION_DENIED_STATE | 调用 access(FNAME_W, R_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_D2D67AB5E38A7000`](../../library/rules/ltp-d2d67ab5e38a7000.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_R, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_D2F4BCF2263C56F5`](../../library/rules/ltp-d2f4bcf2263c56f5.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_W, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_D412A09DEDC43045`](../../library/rules/ltp-d412a09dedc43045.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_R, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_D4D8A0FEAA2F6B09`](../../library/rules/ltp-d4d8a0feaa2f6b09.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_W"/"FNAME_R, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_D653D15777B77A1F`](../../library/rules/ltp-d653d15777b77a1f.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_W"/"FNAME_W, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_D6A52FD61BF01578`](../../library/rules/ltp-d6a52fd61bf01578.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_X, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_D72526C4E4301D60`](../../library/rules/ltp-d72526c4e4301d60.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_X, F_OK) | 返回 -1，errno 为 0 |
| [`LTP_D76652434EC85091`](../../library/rules/ltp-d76652434ec85091.yaml) | 无额外前置条件 | 调用 access(FNAME_RWX, F_OK) | 返回 -1，errno 为 0 |
| [`LTP_D8B58CA743EBE711`](../../library/rules/ltp-d8b58ca743ebe711.yaml) | 无额外前置条件 | 调用 access(FNAME_R, R_OK|W_OK) | 返回 -1，errno 为 0 |
| [`LTP_DA10E351BC730D85`](../../library/rules/ltp-da10e351bc730d85.yaml) | 无额外前置条件 | 调用 access(FNAME_R, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_DAA03BAD070DB1D6`](../../library/rules/ltp-daa03bad070db1d6.yaml) | 无额外前置条件 | 调用 access(FNAME_W, R_OK|W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_DAA1F16D8A298E83`](../../library/rules/ltp-daa1f16d8a298e83.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_R, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_DCB33BB29D296843`](../../library/rules/ltp-dcb33bb29d296843.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_RX"/"FNAME_R, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_DD9A41090E3D5A17`](../../library/rules/ltp-dd9a41090e3d5a17.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_X, X_OK) | 返回 -1，errno 为 0 |
| [`LTP_DF1C4714B16B760E`](../../library/rules/ltp-df1c4714b16b760e.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_W, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_E0B177A8B6FE4225`](../../library/rules/ltp-e0b177a8b6fe4225.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_R, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_E0ED96B80FC3B6C9`](../../library/rules/ltp-e0ed96b80fc3b6c9.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_W, F_OK) | 返回 -1，errno 为 0 |
| [`LTP_E28B5BB57A450438`](../../library/rules/ltp-e28b5bb57a450438.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_W, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_E2C3B68EDF07A753`](../../library/rules/ltp-e2c3b68edf07a753.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_R, F_OK) | 返回 -1，errno 为 0 |
| [`LTP_E34945E3DE91022F`](../../library/rules/ltp-e34945e3de91022f.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_X"/"FNAME_W, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_E3A3CF8B98E460BC`](../../library/rules/ltp-e3a3cf8b98e460bc.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_X, F_OK) | 返回 -1，errno 为 0 |
| [`LTP_E41DD7230DA067DD`](../../library/rules/ltp-e41dd7230da067dd.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_X, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_E46539F2D47BA5EC`](../../library/rules/ltp-e46539f2d47ba5ec.yaml) | 无额外前置条件 | 调用 access(DNAME_RW"/"FNAME_X, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_E4D1B76D80905462`](../../library/rules/ltp-e4d1b76d80905462.yaml) | 无额外前置条件 | 调用 access(DNAME_WX"/"FNAME_W, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_E560C027210BF20A`](../../library/rules/ltp-e560c027210bf20a.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_W, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_E5791B389C67677E`](../../library/rules/ltp-e5791b389c67677e.yaml) | 无额外前置条件 | 调用 access(DNAME_X"/"FNAME_R, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_E5E50FB7BDD033D9`](../../library/rules/ltp-e5e50fb7bdd033d9.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_RW"/"FNAME_X, X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_EB00EA74B30E438E`](../../library/rules/ltp-eb00ea74b30e438e.yaml) | 无额外前置条件 | 调用 access(FNAME_RWX, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_EB425D988F2F7604`](../../library/rules/ltp-eb425d988f2f7604.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_RW"/"FNAME_X, F_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_EBF0020C32AD44C8`](../../library/rules/ltp-ebf0020c32ad44c8.yaml) | PERMISSION_DENIED_STATE | 调用 access(FNAME_W, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_EC19C6410BBE0467`](../../library/rules/ltp-ec19c6410bbe0467.yaml) | 无额外前置条件 | 调用 access(FNAME_RWX, R_OK|W_OK) | 返回 -1，errno 为 0 |
| [`LTP_ED36488372A175F5`](../../library/rules/ltp-ed36488372a175f5.yaml) | 无额外前置条件 | 调用 access(FNAME_W, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_ED3F2AE7E59E6F12`](../../library/rules/ltp-ed3f2ae7e59e6f12.yaml) | 无额外前置条件 | 调用 access(FNAME_X, R_OK|W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_EE1518958A8F7CC1`](../../library/rules/ltp-ee1518958a8f7cc1.yaml) | 无额外前置条件 | 调用 access(FNAME_W, R_OK) | 调用成功，返回 SUCCESS |
| [`LTP_EF5C1F365208AD31`](../../library/rules/ltp-ef5c1f365208ad31.yaml) | PERMISSION_DENIED_STATE | 调用 access(DNAME_RX"/"FNAME_X, R_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_F202F3C3B02DEA0E`](../../library/rules/ltp-f202f3c3b02dea0e.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_W, X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_F3200B697F38DD16`](../../library/rules/ltp-f3200b697f38dd16.yaml) | 无额外前置条件 | 调用 access(FNAME_RWX, R_OK|W_OK|X_OK) | 调用成功，返回 SUCCESS |
| [`LTP_F3418C5C403B91FC`](../../library/rules/ltp-f3418c5c403b91fc.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_R, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_F43EC0D01CCFD25A`](../../library/rules/ltp-f43ec0d01ccfd25a.yaml) | 无额外前置条件 | 调用 access(FNAME_RWX, R_OK|W_OK|X_OK) | 返回 -1，errno 为 0 |
| [`LTP_F6BB86F5DCC2FAC8`](../../library/rules/ltp-f6bb86f5dcc2fac8.yaml) | 无额外前置条件 | 调用 access(FNAME_RWX, W_OK) | 调用成功，返回 SUCCESS |
| [`LTP_F70FC66A56FBD769`](../../library/rules/ltp-f70fc66a56fbd769.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_R, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_F7998813C90A7A08`](../../library/rules/ltp-f7998813c90a7a08.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_R, W_OK) | 返回 -1，errno 为 0 |
| [`LTP_F8CDD57D76C8FA6C`](../../library/rules/ltp-f8cdd57d76c8fa6c.yaml) | 无额外前置条件 | 调用 access(DNAME_R"/"FNAME_X, F_OK) | 调用成功，返回 SUCCESS |
| [`LTP_F9BF08369A08E5ED`](../../library/rules/ltp-f9bf08369a08e5ed.yaml) | PERMISSION_DENIED_STATE | 调用 access(FNAME_W, R_OK|W_OK|X_OK) | 返回 -1，errno 为 EACCES |
| [`LTP_FC5B16AB3C53A744`](../../library/rules/ltp-fc5b16ab3c53a744.yaml) | 无额外前置条件 | 调用 access(DNAME_RX"/"FNAME_X, R_OK) | 返回 -1，errno 为 0 |
| [`LTP_FCA376B46A9873B0`](../../library/rules/ltp-fca376b46a9873b0.yaml) | 无额外前置条件 | 调用 access(DNAME_W"/"FNAME_R, F_OK) | 返回 -1，errno 为 0 |
## `acct`

没有形成可发布的合规性规则。

## `add_key`

没有形成可发布的合规性规则。

## `adjtimex`

没有形成可发布的合规性规则。

## `alarm`

共形成 14 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_1A9481FAD460FBF7`](../../library/rules/ltp-1a9481fad460fbf7.yaml) | 无额外前置条件 | 调用 alarm(1) | 调用成功，返回 SUCCESS |
| [`LTP_3E8DA9E014B82702`](../../library/rules/ltp-3e8da9e014b82702.yaml) | 无额外前置条件 | 调用 alarm(10) | 调用成功，返回 SUCCESS |
| [`LTP_6449E4A1D20C01D3`](../../library/rules/ltp-6449e4a1d20c01d3.yaml) | 无额外前置条件 | 调用 alarm(0) | {'kind': 'return_value', 'return': 'UINT_MAX/4'} |
| [`LTP_65B70356F06E31F8`](../../library/rules/ltp-65b70356f06e31f8.yaml) | 无额外前置条件 | 调用 alarm(UINT_MAX/2) | 调用成功，返回 SUCCESS |
| [`LTP_76A9B6CF388A8609`](../../library/rules/ltp-76a9b6cf388a8609.yaml) | 无额外前置条件 | 调用 alarm(UINT_MAX/4) | 调用成功，返回 SUCCESS |
| [`LTP_82621B02FCA09F40`](../../library/rules/ltp-82621b02fca09f40.yaml) | 无额外前置条件 | 调用 alarm(0) | {'kind': 'return_value', 'return': '1'} |
| [`LTP_98EC66149EE68933`](../../library/rules/ltp-98ec66149ee68933.yaml) | 无额外前置条件 | 调用 alarm(2) | 调用成功，返回 SUCCESS |
| [`LTP_B7A341967DF2BD69`](../../library/rules/ltp-b7a341967df2bd69.yaml) | 无额外前置条件 | 调用 alarm(100) | 调用成功，返回 SUCCESS |
| [`LTP_C785774773FB7524`](../../library/rules/ltp-c785774773fb7524.yaml) | 无额外前置条件 | 调用 alarm(INT_MAX) | 调用成功，返回 SUCCESS |
| [`LTP_C7B73F4D5B87736A`](../../library/rules/ltp-c7b73f4d5b87736a.yaml) | 无额外前置条件 | 调用 alarm(0) | {'kind': 'return_value', 'return': 'INT_MAX'} |
| [`LTP_C80C019BE3F47901`](../../library/rules/ltp-c80c019be3f47901.yaml) | 无额外前置条件 | 调用 alarm(1) | {'kind': 'return_value', 'return': '9'} |
| [`LTP_CD2150BE4FE81F31`](../../library/rules/ltp-cd2150be4fe81f31.yaml) | 无额外前置条件 | 调用 alarm(0) | {'kind': 'return_value', 'return': 'UINT_MAX/2'} |
| [`LTP_D1B6112551D45B31`](../../library/rules/ltp-d1b6112551d45b31.yaml) | 无额外前置条件 | 调用 alarm(0) | {'kind': 'return_value', 'return': '100'} |
| [`LTP_D4B433A3696803A8`](../../library/rules/ltp-d4b433a3696803a8.yaml) | 无额外前置条件 | 调用 alarm(0) | 调用成功，返回 SUCCESS |
## `arch_prctl`

没有形成可发布的合规性规则。

## `bind`

没有形成可发布的合规性规则。

## `bpf`

没有形成可发布的合规性规则。

## `brk`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_7A74A699442CEB99`](../../library/rules/ltp-7a74a699442ceb99.yaml) | 无额外前置条件 | 调用 brk(new_brk) | 调用成功，返回 SUCCESS |
| [`LTP_E3E59B16A96A60BC`](../../library/rules/ltp-e3e59b16a96a60bc.yaml) | 无额外前置条件 | 调用 brk(addr) | 调用成功，返回 SUCCESS |
## `cacheflush`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_8AD8032754BC8842`](../../library/rules/ltp-8ad8032754bc8842.yaml) | 无额外前置条件 | 调用 cacheflush(addr, getpagesize(), CACHE_DESC(ICACHE)) | 调用成功，返回 SUCCESS |
| [`LTP_C218D3CB0AD80D90`](../../library/rules/ltp-c218d3cb0ad80d90.yaml) | 无额外前置条件 | 调用 cacheflush(addr, getpagesize(), CACHE_DESC(BCACHE)) | 调用成功，返回 SUCCESS |
| [`LTP_D579FCFC71E6EB6A`](../../library/rules/ltp-d579fcfc71e6eb6a.yaml) | 无额外前置条件 | 调用 cacheflush(addr, getpagesize(), CACHE_DESC(DCACHE)) | 调用成功，返回 SUCCESS |
## `cachestat`

共形成 6 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_00F2A9EA8833DA1D`](../../library/rules/ltp-00f2a9ea8833da1d.yaml) | 文件描述符无效 | 调用 cachestat(fd, cs_range, cs, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_1325C077A1CDE514`](../../library/rules/ltp-1325c077a1cde514.yaml) | 无额外前置条件 | 调用 cachestat(fd, cs_range, cs, 0) | 调用成功，返回 SUCCESS |
| [`LTP_34EC9FB9C9551214`](../../library/rules/ltp-34ec9fb9c9551214.yaml) | 无额外前置条件 | 调用 cachestat(invalid_fd, cs_range, cs, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_7FD6142E0E88CF17`](../../library/rules/ltp-7fd6142e0e88cf17.yaml) | BAD_USER_ADDRESS | 调用 cachestat(fd, cs_range_null, cs, 0) | 返回 -1，errno 为 EFAULT |
| [`LTP_89C9E8458EC38C11`](../../library/rules/ltp-89c9e8458ec38c11.yaml) | BAD_USER_ADDRESS | 调用 cachestat(fd, cs_range, cs_null, 0) | 返回 -1，errno 为 EFAULT |
| [`LTP_BA9A8FE901467960`](../../library/rules/ltp-ba9a8fe901467960.yaml) | 无额外前置条件 | 调用 cachestat(fd_hugepage, cs_range, cs, 0) | 返回 -1，errno 为 EOPNOTSUPP |
## `capget`

共形成 5 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_208C833FF12217F5`](../../library/rules/ltp-208c833ff12217f5.yaml) | 无额外前置条件 | 调用 capget(hdr, data) | 调用成功，返回 SUCCESS |
| [`LTP_5F1D35ACCEFD4971`](../../library/rules/ltp-5f1d35accefd4971.yaml) | BAD_USER_ADDRESS | 调用 capget(2 - 1 ? header : NULL, 2 - 2 ? data : bad_data) | 返回 -1，errno 为 EFAULT |
| [`LTP_827CE5CB448A411B`](../../library/rules/ltp-827ce5cb448a411b.yaml) | BAD_USER_ADDRESS | 调用 capget(1 - 1 ? header : NULL, 1 - 2 ? data : bad_data) | 返回 -1，errno 为 EFAULT |
| [`LTP_CED2FCC737A99D40`](../../library/rules/ltp-ced2fcc737a99d40.yaml) | 无额外前置条件 | 调用 capget(0 - 1 ? header : NULL, 0 - 2 ? data : bad_data) | 返回 -1，errno 为 ESRCH |
| [`LTP_DC9BC72148835FDC`](../../library/rules/ltp-dc9bc72148835fdc.yaml) | 无额外前置条件 | 调用 capget(0 - 1 ? header : NULL, 0 - 2 ? data : bad_data) | 返回 -1，errno 为 EINVAL |
## `capset`

共形成 7 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_461340ED83E7043D`](../../library/rules/ltp-461340ed83e7043d.yaml) | BAD_USER_ADDRESS | 调用 capset(0 - 1 ? header : bad_addr, 0 - 2 ? data : bad_addr) | 返回 -1，errno 为 EINVAL |
| [`LTP_6D86AFD541A61388`](../../library/rules/ltp-6d86afd541a61388.yaml) | BAD_USER_ADDRESS | 调用 capset(2 - 1 ? header : bad_addr, 2 - 2 ? data : bad_addr) | 返回 -1，errno 为 EFAULT |
| [`LTP_7DEDC53AC33C891F`](../../library/rules/ltp-7dedc53ac33c891f.yaml) | BAD_USER_ADDRESS | 调用 capset(0 - 1 ? header : bad_addr, 0 - 2 ? data : bad_addr) | 返回 -1，errno 为 EPERM |
| [`LTP_A00E343F4A556B3D`](../../library/rules/ltp-a00e343f4a556b3d.yaml) | 无额外前置条件 | 调用 capset(header, data) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_D1AADFC2F7C6F594`](../../library/rules/ltp-d1aadfc2f7c6f594.yaml) | 无额外前置条件 | 调用 capset(header, data) | 返回 -1，errno 为 EPERM |
| [`LTP_E06D53042C10C99E`](../../library/rules/ltp-e06d53042c10c99e.yaml) | BAD_USER_ADDRESS | 调用 capset(1 - 1 ? header : bad_addr, 1 - 2 ? data : bad_addr) | 返回 -1，errno 为 EFAULT |
| [`LTP_EC23768761E40E9F`](../../library/rules/ltp-ec23768761e40e9f.yaml) | 无额外前置条件 | 调用 capset(header, data) | 调用成功，返回 SUCCESS |
## `chdir`

没有形成可发布的合规性规则。

## `chmod`

没有形成可发布的合规性规则。

## `chown`

没有形成可发布的合规性规则。

## `chroot`

共形成 8 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_245CD61DAA19DC98`](../../library/rules/ltp-245cd61daa19dc98.yaml) | NON_DIRECTORY_PATH_COMPONENT | 调用 chroot(file_name) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_50F858A3CBF95EED`](../../library/rules/ltp-50f858a3cbf95eed.yaml) | 无额外前置条件 | 调用 chroot(path) | 返回 -1，errno 为 EPERM |
| [`LTP_71C54C624831C7F0`](../../library/rules/ltp-71c54c624831c7f0.yaml) | PATH_TOO_LONG | 调用 chroot(longname_dir) | 返回 -1，errno 为 ENAMETOOLONG |
| [`LTP_99DF5C34778032E1`](../../library/rules/ltp-99df5c34778032e1.yaml) | SYMLINK_LOOP | 调用 chroot(loop_dir) | 返回 -1，errno 为 ELOOP |
| [`LTP_D0E32E5D27E643A9`](../../library/rules/ltp-d0e32e5d27e643a9.yaml) | PERMISSION_DENIED_STATE | 调用 chroot(TEST_TMPDIR) | 返回 -1，errno 为 EACCES |
| [`LTP_EBD54180D0CAB16B`](../../library/rules/ltp-ebd54180d0cab16b.yaml) | BAD_USER_ADDRESS | 调用 chroot(bad_ptr) | 返回 -1，errno 为 EFAULT |
| [`LTP_EE7A979F212D6C0C`](../../library/rules/ltp-ee7a979f212d6c0c.yaml) | 无额外前置条件 | 调用 chroot(path) | 调用成功，返回 SUCCESS |
| [`LTP_FF9C0F9669A39525`](../../library/rules/ltp-ff9c0f9669a39525.yaml) | NONEXISTENT_PATH | 调用 chroot(nonexistent_dir) | 返回 -1，errno 为 ENOENT |

## 技术参考

- 报告 ID：`spec-20260715t030951z-58714275`
- 来源：`ltp-local`，内容快照 `sha256:d789747f0c0bf1697f538bc5166073fd8449dec3beac7b12ac0be0b1b716dcb4`
- 全局待处理 syscall：373
- 提取数量：`20`（来源：`command`）
- `abort`：证据 1 条，未解析 0 条
- `accept`：证据 6 条，未解析 0 条
- `accept4`：证据 2 条，未解析 2 条
- `access`：证据 10 条，未解析 0 条
- `acct`：证据 8 条，未解析 1 条
- `add_key`：证据 15 条，未解析 5 条
- `adjtimex`：证据 6 条，未解析 3 条
- `alarm`：证据 15 条，未解析 0 条
- `arch_prctl`：证据 1 条，未解析 0 条
- `bind`：证据 9 条，未解析 1 条
- `bpf`：证据 12 条，未解析 1 条
- `brk`：证据 3 条，未解析 0 条
- `cacheflush`：证据 1 条，未解析 0 条
- `cachestat`：证据 7 条，未解析 0 条
- `capget`：证据 2 条，未解析 0 条
- `capset`：证据 10 条，未解析 0 条
- `chdir`：证据 4 条，未解析 1 条
- `chmod`：证据 15 条，未解析 1 条
- `chown`：证据 22 条，未解析 1 条
- `chroot`：证据 8 条，未解析 0 条

<details>
<summary>机器可读元数据</summary>

<!-- syscallguard-metadata -->
```yaml
schema_version: 1
kind: syscallguard_ingest_report
report_id: spec-20260715t030951z-58714275
generated_at_utc: '2026-07-15T03:09:52.149069Z'
source:
  id: ltp-local
  type: ltp
  snapshot_hash: sha256:d789747f0c0bf1697f538bc5166073fd8449dec3beac7b12ac0be0b1b716dcb4
  descriptor_hash: sha256:4315924cd8b9aab9608c225950c81f18ab74f25d63d74ee6ac3c444132131b4d
  recognition_rules_hash: sha256:84d715591e7abe5f2ac2de68c75172b2b2389541f6f8b8f23582b8cff81b057e
  resolution: default_source
count:
  value: '20'
  source: command
pending_count: 373
selected_syscalls:
- abort
- accept
- accept4
- access
- acct
- add_key
- adjtimex
- alarm
- arch_prctl
- bind
- bpf
- brk
- cacheflush
- cachestat
- capget
- capset
- chdir
- chmod
- chown
- chroot
syscalls:
- syscall: abort
  source_fingerprint: sha256:bcfbc8209ef30cdaf386eab7a3c95e88d9380d72c1d8113fd57fd4a140c68ee3
  recognition_fingerprint: sha256:46e6817e2278640dfc6209ff21eafc3fb4b490e07a674ea9148aabdb56de3547
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: accept
  source_fingerprint: sha256:67de27cb07823cd82fe2cccc4519cba50af7559dd97aade2e66d60ba1be6477c
  recognition_fingerprint: sha256:f442db18bead0f5b46cf62a47c8661b6f43e682cf2f2f8f0c2e961a7a9c4cabd
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_277FD467E5F1BF1C
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:277fd467e5f1bf1c23ee7c1139c3420fd53e3387d46a1441bccd3f763aecc0c1
  - id: LTP_472AAA35C7382B26
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:472aaa35c7382b2636fefb76370c46d334f3c77cb0f9a4d38ae943f787a3b503
  - id: LTP_80C6DB0ACB2A5510
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:80c6db0acb2a5510899328ccf5897d7e8d2a652d48a8013d682918b68813a993
  - id: LTP_9CA9C6B61C3317A3
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:9ca9c6b61c3317a32e26c489d7ae42771eb27df123a4f1488713978280f9bfb7
  - id: LTP_B90CB73F36B70C6F
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:b90cb73f36b70c6f80c9105773e4598523d84a62b8068d6913141437de6ddcb8
  - id: LTP_E13B9C2C9645B841
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:e13b9c2c9645b841740286ed51439b50fbadac9cb52df5b4b60bf4bd5ed5df31
  - id: LTP_F1044C71B6626419
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:f1044c71b66264190afeea58604122162821df88724d0f3a9e5b63ac98a3ea48
  evidence_count: 6
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: accept4
  source_fingerprint: sha256:ef8169f7868949409125798db26ccd7ebbfedd098b5ae018eca3fe029abf1245
  recognition_fingerprint: sha256:f3b070e1906482ff2aa17bd22e70d31b11680e249dfcdccee6c5a66dd163d711
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: access
  source_fingerprint: sha256:2beb6aef3f53b06cc748b2dfabb7de16e44bc56e67e96528700ac22c91729b1a
  recognition_fingerprint: sha256:7e4b8b5ce1baf384f64930d1ec2c377b8124fd3174dd312f2ae5beb0956f48de
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_0180982614AA9F7D
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:0180982614aa9f7deb01d61e1891fc76f80a5dd2c63dd0b04340bb29d02ed2a5
  - id: LTP_0290063892A53510
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:0290063892a5351022a2ab7b4cb9849ec40fa29b864a2ddc25704eaefa3e2fc7
  - id: LTP_030858A5FFCCEFF4
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:030858a5ffcceff4801d7ba45b78d895d2681e32e7f4ef9f88f30c2caa67a40e
  - id: LTP_035E62E6D1787773
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:035e62e6d17877739db6b59f91601ed94cfa7d9904d1176fd2d2f2e9f8791738
  - id: LTP_036EDA2B8D36CF03
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:036eda2b8d36cf0300b93ee6a14685f0f6e4f787729cd0eb83fa377979143be6
  - id: LTP_037E6F334D0E0D16
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:037e6f334d0e0d16d085d2f03c051ebd6062b33c049ebecb4a6f1bc79e401a83
  - id: LTP_0431E3529AA0FEE8
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:0431e3529aa0fee804b2f7242cf911e84dc5d046d7785cee532eb968842b1886
  - id: LTP_044E7C11E6B503BB
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:044e7c11e6b503bb657c1f5d568942154575515e5bd090cfb272ebd5b2953217
  - id: LTP_060B6037DEF1D43C
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:060b6037def1d43c9de3ca80ee5aebdb2cf64bbf6b1745c252af35d117049ef7
  - id: LTP_06725D44DFF06F7E
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:06725d44dff06f7e7b34882d799fa971d2ddf049a360e5bc1fa26eee8a5ded8c
  - id: LTP_06891E2E299CF48E
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:06891e2e299cf48e89e834978cafb8d3f54a5f988367d5ac9c5daf94202c0532
  - id: LTP_06A0C295D8E7FAFA
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:06a0c295d8e7fafa651946a3613c2e32e4a46c5c733aed891d879dd24b06d14f
  - id: LTP_06AC9297E35AAE7A
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:06ac9297e35aae7a524a02e7136a35e29d155f5741903b920ab3d6f8f300ab3e
  - id: LTP_075318C437B76E06
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:075318c437b76e067682a9c6aab95a64558daf471c20df7205f62a72b1fd82ee
  - id: LTP_0799FC60BADD2B18
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:0799fc60badd2b189b242a57ba5740cd832aa2477cbe8497f5b09324880ca7f4
  - id: LTP_0A62800536904C02
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:0a62800536904c0231dfd538b848b4c23fd261fbe26b6291a46dd1c085dc1ff0
  - id: LTP_0AAFA34BA77A0D25
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:0aafa34ba77a0d25c3bd2632bf23889acf190eb7c15c253cee339354f1110c2b
  - id: LTP_0B45FC33068D334C
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:0b45fc33068d334cf0357b5b3073acdade7252dc401c49826a1462e2af51fa55
  - id: LTP_0BB235F712E819CE
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:0bb235f712e819ce1befaab2d5b66dea761c42c1065a66f2bfb8da4f8f73c7ab
  - id: LTP_0D1782EAAC26DEB4
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:0d1782eaac26deb423a13b1bef2c3fc0e4647c3d464451e818c877ae67a0c0b9
  - id: LTP_0E9AF2C058AF8126
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:0e9af2c058af8126ab590f4af3482c8cef54975bc433bc4fd72f2e9e995f0b7e
  - id: LTP_0F901C62092CC7B8
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:0f901c62092cc7b8b0b52da1ecc4765c39b985ba06d0cde2403d83870bb85b5f
  - id: LTP_10A684C1C2D2DE0F
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:10a684c1c2d2de0ffb60286a885a3ca7a2dd3efe1ea7f8b558e414f6600a17a2
  - id: LTP_10FE1313FBAB5F92
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:10fe1313fbab5f922177fdab0a0b6689cda7f927eb5c69552253739d55d3d86f
  - id: LTP_1402459B5FF9BF23
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:1402459b5ff9bf23e7573fc58e2bd88e7a0e24fe7b709fac9d058701c2419681
  - id: LTP_1465554B09CE14F0
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:1465554b09ce14f0b5a735a4a5e0b72f71a87d0d0e40af031decb029dcb06eaf
  - id: LTP_148623FDAF4E478D
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:148623fdaf4e478d7bc5953483a91b32d18a4a0374aa87efa70ca569b067bc08
  - id: LTP_153B296FA599E0CE
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:153b296fa599e0ce4555e2bb2282ac195f43cdb6c0c7079b4d03f64c21b57bd6
  - id: LTP_17ACF3BE969B64EE
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:17acf3be969b64eeacbd0b1e0d7962096022eafafe0daba6fed1e0e668a86609
  - id: LTP_17CB4ED7A76BD283
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:17cb4ed7a76bd2837ae4f4604ac37111d7656358256727f2e918e7c166bc98a5
  - id: LTP_1870C0046E9555AF
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:1870c0046e9555af9d7e66141ed6475091b877da1cfbdc00aa87c2634b6e60d2
  - id: LTP_18A450CE49F8867B
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:18a450ce49f8867b0a9250309a99648d981828d27b48aa2a91f513504b505643
  - id: LTP_198D9555A8BED013
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:198d9555a8bed013005fa53f75f062528eee407371a00ce59e91b35492135b4b
  - id: LTP_1BD36AE285B4F3E2
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:1bd36ae285b4f3e25c7c437dbf46333126e0ff5fa47eeab6ffec8f981fa0874e
  - id: LTP_1C462AC54A29FF35
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:1c462ac54a29ff357fc83b28d38fb27f808d5eae31786aeff93269e3daf9911a
  - id: LTP_1CDCF5FE9ED1BE5D
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:1cdcf5fe9ed1be5df8f5722e4428822d616a324d2465d968f642d7fc156571a9
  - id: LTP_1D39F97D759F0E57
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:1d39f97d759f0e57f0b75f9051337bac3a6d0e132ec3b90d9b3e2a5f2eb6ee51
  - id: LTP_1DF2B28499E4D7B3
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:1df2b28499e4d7b3d66a41c156e6d76091647274b46de23227d0d0d90e7d53f0
  - id: LTP_212269CECE600FD8
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:212269cece600fd878a851cd77e845c2a59b421728918141ae16a27e0d4c95eb
  - id: LTP_21A007DF738F1E73
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:21a007df738f1e73d4d114588fead88ebbe79ee5fd70f18cd1f7fcdb959e920a
  - id: LTP_21C4957F9EFE94D3
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:21c4957f9efe94d3e66d50ae689b746486cda4c816cdeb5886609743f44a7b22
  - id: LTP_220D1227D307AD3C
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:220d1227d307ad3c1622e2899c7258e3e21ae9526597a9364235fd48ef3883dd
  - id: LTP_2221F954D01EB2BB
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:2221f954d01eb2bb9f9cabda5ec81c84973ac2e69b800bd2192cc74e96aaa97a
  - id: LTP_25639C9C5750C487
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:25639c9c5750c487fcedf6d0ec8774392cef4e9acd74069166a8a2a8bd1ea90e
  - id: LTP_26AC646B9D18C353
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:26ac646b9d18c353cf98f2ad49a480176e3c37f06acf9c84818255abf755f99c
  - id: LTP_27C7E91095DB9DF8
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:27c7e91095db9df833b0e7ea1e461c43f3d9fbde5c93ef4a7131cccc48a5df5d
  - id: LTP_2900BC64740A3E44
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:2900bc64740a3e44e3915afb13c01233f03f913b311ddb57b3173b513a3215c2
  - id: LTP_298AB67F0CFA519C
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:298ab67f0cfa519c0db5140ce8f9ad87d6720b8da357263c84dd9346b732cb2a
  - id: LTP_2B4171DD8FBD982A
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:2b4171dd8fbd982a461eb396fb5c1b19585ca852641fe389afeda6644b7a4dd0
  - id: LTP_2D0BAECAE4F61432
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:2d0baecae4f614321089041a1a0684b081a6857a5d0e84eedc6e8c1772e3fb8c
  - id: LTP_2E5D530A61E60934
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:2e5d530a61e609346a68ecee5667739da2d8a5b9da2a755ad8e2eb5d4882a340
  - id: LTP_2F99FA84C445363C
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:2f99fa84c445363ccdb31044c1a489fb3da71ffb0efca79bea63770a584e2bde
  - id: LTP_2FA43CD942AE7AD6
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:2fa43cd942ae7ad6ccb5075fb30e8dfe102ad171ef4bb0d8f3b53fe0414d4f04
  - id: LTP_2FE8FAD800DE41F6
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:2fe8fad800de41f63ccd36fc268ba471fb2b0e8a976a37d489d680e7730d8e9b
  - id: LTP_3472CD1A0F8A2B4A
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:3472cd1a0f8a2b4a54ab63d2a1d196f03bcd2aa624cb2a98ea16db372fda08db
  - id: LTP_347761CBCF52D194
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:347761cbcf52d194787660bd2fb38371c03cb90d478f053ab9e79d9221b6cf8b
  - id: LTP_34CFEAD03DB6A3CA
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:34cfead03db6a3ca70d00de281c9408d7d7d61d2e4fe236b08786563a8708e78
  - id: LTP_35CAEE10A613E109
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:35caee10a613e10914e037e7be0dacb0a8989b64d1d9e189aa137fb54b89b664
  - id: LTP_3636C4768C196B52
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:3636c4768c196b52badf7a37729528d9190192b4ab768ee346f246182e7e7d79
  - id: LTP_368D8689810796B2
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:368d8689810796b2a234105c4c4f97f7fee4e238f4bd6f026807c3ef860c21d6
  - id: LTP_38FB918826669241
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:38fb918826669241ebbe77827a90f4347f124cf6de78fd4f4b46b3495fb3ab2f
  - id: LTP_3900F4E562AE09D1
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:3900f4e562ae09d1b996c7e0d13a4a75221f775687ad7e80caaf10193db1caf3
  - id: LTP_3916A669595B3568
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:3916a669595b35682ab5539f30613ffc1e634d2c181f1c31fbdf0367fea7f735
  - id: LTP_3AD3865603ADDC8E
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:3ad3865603addc8e91936e01b73876e1717a621920dbeb5a9751a731b7a14bc4
  - id: LTP_3C2853617B38EEE7
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:3c2853617b38eee73d035c8cf8f2f494af2aabd3fed30aedbc94a9edfaf7698d
  - id: LTP_3D4ECD22BC433164
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:3d4ecd22bc433164ccde4e95b5606bd900aa45dd46f58575b755e0c02f3c9c86
  - id: LTP_3D8D38C9123CD051
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:3d8d38c9123cd051af9092607d45a62f55164808924a0eb549f9224f1dfcb486
  - id: LTP_3DE23AB4FE2FFC67
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:3de23ab4fe2ffc675ecd96acd034e98e5c50b8b059d547bd746e35859afcc4ba
  - id: LTP_3E526A0A23B5EF6D
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:3e526a0a23b5ef6d666ef23c6f7fdef709d38709ea4ae271ba2352c150809881
  - id: LTP_3F81436312777EF4
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:3f81436312777ef415faf7797d673dd462cee3f00903f2610d05eb93291b67c4
  - id: LTP_401D471D37C85820
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:401d471d37c85820189e45519e765d1c0fdf65134cf15d25d8f1ef0009bc3408
  - id: LTP_4661BBF1B3CD3A1E
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:4661bbf1b3cd3a1ed9794183dd018046d195e23d06cfc4a8e2fa282fef66c737
  - id: LTP_46DE8D9AD1674F26
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:46de8d9ad1674f268ec5176d6c6112b3e667c7b9e884a397b395dc4f4202fba1
  - id: LTP_479924116854D92B
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:479924116854d92bd1d203df358cb1eb87571c84548d95311a60a2e5abc9e62a
  - id: LTP_48753F73ACA755FB
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:48753f73aca755fb980caaec98512bd04fdea8e9fd9793bfbd36d89e8f100a40
  - id: LTP_4881657CFE57C7E9
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:4881657cfe57c7e9a906daa4e09474f24fe060c0fa11c4f8419f3f3b1d9843b8
  - id: LTP_492D25A0F1055F72
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:492d25a0f1055f7272707dc74d2909d60d3bfdb3bdbb276d8dfecd1ba98b2a61
  - id: LTP_4948E12FB8F9FA49
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:4948e12fb8f9fa49c261a472b9a2b88b7af3fee9ae5585b0be2d7735fbd49de8
  - id: LTP_49700CDA955B66D8
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:49700cda955b66d806729411debdf13891a8527551aaaa1af426c2ec7e472e8c
  - id: LTP_49A36559B96D24AF
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:49a36559b96d24af3d3ab1868328be5c985a250582334d715a8f40e00052d8c8
  - id: LTP_4B6E9B98E2E5103D
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:4b6e9b98e2e5103df3d3c7a2359a60f35abd8fca0283c6630c38234ecf018a91
  - id: LTP_4CFAFCE7FCA2BF99
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:4cfafce7fca2bf99656750383256c61ae565e76c1d4500ccb00d3d51cfeecf7d
  - id: LTP_4ECB786BFA071AAC
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:4ecb786bfa071aace1647cbe14be935db4f23e38eb6171a9ca1178bad37df0f0
  - id: LTP_50A86D4D5411356E
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:50a86d4d5411356ebcf10ffcdde2d209330522115285ebaf0d290c55611b93f1
  - id: LTP_52C209105EE62171
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:52c209105ee6217120690e4f8e29fb2a2eb681b601393f03d6536e8b14b1631d
  - id: LTP_5570480E7920BD0E
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:5570480e7920bd0ed29ec610cdd62bddf31a0d8c8de53cb937c27b58005abe0a
  - id: LTP_563FB650864E0DC6
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:563fb650864e0dc622844bcadcf468b2e11b289be993156a08b366bc3f4376d9
  - id: LTP_58416E6747519699
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:58416e6747519699e7b507fc0ff7e8c00852ff81eaff2cf425bb2d4a84e4e6f3
  - id: LTP_58F1512157A0052D
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:58f1512157a0052d2af0ab1a834b768a94f0483ea6f6f5c904b75b63abe57a97
  - id: LTP_5A315335586D4227
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:5a315335586d4227dcb876b158bdf7ed73cd51dd9934c72a7a39852596d1f041
  - id: LTP_5C5CDC165410C08C
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:5c5cdc165410c08c87ec34958aeb8662f2bd50738c79e7e54a3345227c6f463a
  - id: LTP_5CC44E5D1A6B6485
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:5cc44e5d1a6b6485d58926a3e9b9aea6814a837393ae7b662a145a4ebbe567b5
  - id: LTP_5D7971086B2ABAE5
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:5d7971086b2abae59c5ba32908d196fe1ca3c05a91a71c6542a6b9fdaffb5081
  - id: LTP_5EC31E34822684C4
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:5ec31e34822684c4b7afef497aa177c327ce8cb8f1121ea1537865c2b63aa0e7
  - id: LTP_606B7E40B6BD82EA
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:606b7e40b6bd82ea15aa8dc42049573d2f2e0e39e77a92d0dc58bc80badaeee0
  - id: LTP_613A5E121B4B6E68
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:613a5e121b4b6e688b260c31b705088dbb0330e1a4d204c7887862f309bd6545
  - id: LTP_6156A09A2E506F76
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:6156a09a2e506f76240ecb425f3b0776cbea6dd2d63de09b41c67358f1f9dedc
  - id: LTP_6169F41023E00C34
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:6169f41023e00c34d1fae4ccb616eda658fc6cfe7a778d1a84419931fc4eb99e
  - id: LTP_636590E5A017B28D
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:636590e5a017b28de0d5d077ab1d9de84c4c96e13945c3e3d5dff4deca279ad5
  - id: LTP_64227C746913D03D
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:64227c746913d03d2fefb2a3d2cb8e5f8e7b91253bdf8c7e2d18422fd037d10d
  - id: LTP_64A4E5DC71A633A2
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:64a4e5dc71a633a26922f41d72c3940a6ec6c25ac2b15d1ad00e035e51510fa8
  - id: LTP_65281FBEE0BF6103
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:65281fbee0bf6103adf2a3ded2bfb3a308de839b6e7240c78d0714f21fa3e229
  - id: LTP_6580B4D3FA1A86F3
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:6580b4d3fa1a86f3730217dbb09e8bb2bba0013f04002af419503eb90a22135a
  - id: LTP_679436EC7A4E218A
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:679436ec7a4e218a139db19a8a9a2025de0bac1cec23502aecca28dbeafcccf9
  - id: LTP_67BF94A4ACD303C4
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:67bf94a4acd303c4bf5ee873c38bf51c6656dd4b572784d258639f552e8c49d3
  - id: LTP_68745D21F4EC2FF5
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:68745d21f4ec2ff5b5e387fdccc54505aa949cca086e22d405cad28698ad929e
  - id: LTP_68E1B26815D97B79
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:68e1b26815d97b79837bdf0a750d5092b5453c48ea9fccb5caa09e08ac391d75
  - id: LTP_69077B093E81B570
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:69077b093e81b570fb4973707d5ca7f472fad9335fd22989875d94b6e3feaccc
  - id: LTP_690A651C3A60FC1E
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:690a651c3a60fc1e3e0857388a189e20596da1430110654cea3df7d95cc8a8db
  - id: LTP_69E094D1DBFF3796
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:69e094d1dbff37964143e4f6311f36c13c43cf505a51915529cdf47ea38780c9
  - id: LTP_6A1A431A08A3F450
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:6a1a431a08a3f45047d6e8fa4396b2005af8a85c4b0a481ccd18de27a227ab17
  - id: LTP_6B1746F6BB2266CA
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:6b1746f6bb2266ca403fddd5b01714afb012e6190b76a167ec91965e3b307769
  - id: LTP_6B8B5453E8B4E6DE
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:6b8b5453e8b4e6de3c130b7bfd88e966870e4f5dd4be63541198db8f77332d12
  - id: LTP_6C11BBB4AABA6E7C
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:6c11bbb4aaba6e7c1ea9cc0299d3ec8157f958bf5001c8dfc4abe7f638f5b840
  - id: LTP_6C55A3E760DF75DB
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:6c55a3e760df75dbda4531dc00263c35e19b5544dd4f09efc00dfda935c00534
  - id: LTP_6CE9FC3BCA164B5D
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:6ce9fc3bca164b5d6aee07583208840f3f1c17c7d70a8f772b2a2946e1e0de2a
  - id: LTP_6D584CE6CF9B8A06
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:6d584ce6cf9b8a06f26df1fde24935b1a38a763306a158a8ae4a2214fae60090
  - id: LTP_6EF7ECD2A8470CEA
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:6ef7ecd2a8470cea5b90e0cc9e2b7679b9ee2a73a4810b11d35520dcd1a6ac3c
  - id: LTP_711D5693356A79F2
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:711d5693356a79f2f78c29dc066b0de731afab838d59939646e4e7b1b2e98a60
  - id: LTP_73DF50509BCC128B
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:73df50509bcc128b1b669bc1dbf328da4c2eeccbf411699638eea46f6a5ffbe5
  - id: LTP_74819A9DC2B5CB06
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:74819a9dc2b5cb06be87f7b24448f78e14019190b6eafc94c1a59aca379084e1
  - id: LTP_752C9A802CF96B8B
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:752c9a802cf96b8be139bd7098d3505b2ec3c75804887a275c9d4ebf1ae13455
  - id: LTP_78EEEBE648781151
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:78eeebe648781151021a0c09a77d9afad8055cb7b1d1b7b1f683af71e8dcf006
  - id: LTP_7963C3DF373596FE
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:7963c3df373596fe8332b3428b9eb575d21649abff2f42a2acedfb92b5974614
  - id: LTP_79C7516DECB19092
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:79c7516decb190926a1a2da50f2739a169f2c4324ba156756aaa688f27172579
  - id: LTP_7A02B34D5FB8BBC3
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:7a02b34d5fb8bbc34f9815aabc5fc09dcedf0e626a1a49ba2adcb9bdab42bf59
  - id: LTP_7B539E14354153DC
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:7b539e14354153dc3ae771f14249d899686d09a8132779a15400fe4c7a359fb5
  - id: LTP_7BE2877017694C52
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:7be2877017694c5297ea1899a6340f60f45a0512564dc9b803cbeb7f07fcaa89
  - id: LTP_7C06A3394E786948
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:7c06a3394e786948b987283ad4350d0fd11b7db40268400f52981a70f7e06cf2
  - id: LTP_7CE7876CE69F200F
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:7ce7876ce69f200f75ab85c56b4a20b71739e4f3e623447c863f83810e8dc4bc
  - id: LTP_7DD493976CBC9A31
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:7dd493976cbc9a31473f659f5104974cd1f19ce54d0dd6847b171a289fcbdb76
  - id: LTP_7F5487EEB79017AD
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:7f5487eeb79017ad484481316be8234c05efc4d1c9a9a69f4b7d0f4be0d60e1d
  - id: LTP_7F54F9DFF7E0FB61
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:7f54f9dff7e0fb6182a763a2155d163534cba4c20aa5919950393fe49e309c79
  - id: LTP_8059D9227293D592
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:8059d9227293d5924f8d626f9d7208df6934b80434c0edd2d718815624c9c2f9
  - id: LTP_807E2072E5694684
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:807e2072e56946843ec26008205fe1d23b12d9ed133587a34c433e599d98bd49
  - id: LTP_818BA624CA9E4040
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:818ba624ca9e40408248bf312cf020f05d886c3623be5fc0719d46a9ac849b1c
  - id: LTP_820495EA1D1F15DA
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:820495ea1d1f15da0bb46f02de41635a1d1e07db2a82d6be42d7d22bf34b5513
  - id: LTP_82ABB8FBFA06D356
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:82abb8fbfa06d356d166904600f5775ae65964f9dd69ff871508d0394f0a9135
  - id: LTP_82E0F55AEC3D382F
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:82e0f55aec3d382ffc129f4f165173a13c4dcdfd664c20edcdfde08730d35547
  - id: LTP_830E17210B1FB7AB
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:830e17210b1fb7ab64b2c08aeb681deb05e66d772e2f30106aedad74766c5a07
  - id: LTP_833C5D5CF3C32C2A
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:833c5d5cf3c32c2ad68b674f024e317ad3f2077e9750dbe97ace078129de90b3
  - id: LTP_839EC7BC904E42D5
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:839ec7bc904e42d51fd03abcb0ea65b5030acf961067619e228750577be93c2f
  - id: LTP_843BDD20FF921FC3
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:843bdd20ff921fc332b61339ab9d496555389281619a41dd01b5fa3075040459
  - id: LTP_84E4CC971DD16EC2
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:84e4cc971dd16ec2911aa117be814cd39fd921938b6295e00affa123c89207ed
  - id: LTP_853D34D061DDE8F8
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:853d34d061dde8f86af4431c77852b00c74651f8900db51dc635601cc3d95627
  - id: LTP_853F4B8346648EB9
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:853f4b8346648eb95326d22c8b7bfcf811114a18d54f8f90a057977525c63035
  - id: LTP_857DC6AD01A88D79
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:857dc6ad01a88d79902a011999f867680c9330ce6c8e5ad503fdd5e6f6389647
  - id: LTP_87478A6C3AC7DC60
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:87478a6c3ac7dc608c2eb8e482206b447ae2b1ca6e6a46d5997786f65d847b5b
  - id: LTP_884775F9076E54AB
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:884775f9076e54ab6b97c1e3384fe1d180e81896a267336db0df25740c24b57d
  - id: LTP_885F3BA721198C07
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:885f3ba721198c07a6615546d3d5161fb126683dbde6e45cac3e768801969348
  - id: LTP_88F6F279E33633DE
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:88f6f279e33633de3f1ef93d7a2345db4c160c5c4b7b2168cac5bc697d415b00
  - id: LTP_8AC11633EA3D83E0
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:8ac11633ea3d83e09f4781cae55d25c2bd9319aa1786100063e7e8a24f836492
  - id: LTP_8B1A2084BCF096F1
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:8b1a2084bcf096f1404d2038c5488359f3de9a3382f8f36d18f1967ea461aad1
  - id: LTP_8B3FBDFD0453EF40
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:8b3fbdfd0453ef405a15e797169e7cc53f5017abb0ad514ada404741cad4b747
  - id: LTP_8BB576EB2E1E6B23
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:8bb576eb2e1e6b23ecfe5c8b7d2bb21eb7fba161f200ce874a6282e806ee9180
  - id: LTP_8C508A50371B6444
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:8c508a50371b64446913da00f93812e109d4fd8dd925be4a47715748c400a4e5
  - id: LTP_8CB51F0A9F8FDEA1
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:8cb51f0a9f8fdea1aa9265603077bdab7f6a75daa52c05b15830b85b2f4a0ea1
  - id: LTP_8D3BFFA98E2561BA
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:8d3bffa98e2561bafe63fc7bc38802e2d2953e533b9e666d99c654309cec9af3
  - id: LTP_8D54825D4B298C7C
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:8d54825d4b298c7c9eb6eb7ac7b0a5cf3f68cd369587ab92c3607e2e2cc10830
  - id: LTP_8E7F1BE3D7D7823B
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:8e7f1be3d7d7823b3dde9ddc3d5b8c29ed22da2d21c0fb4dbe4d5d3afcb0c840
  - id: LTP_8F29388433422812
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:8f29388433422812f34a3bd5135b988bfc543476cdd7c971986173d27aea3a5b
  - id: LTP_8FF73194288F8473
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:8ff73194288f8473237046126e7c31cfa18b72d4aa9df824d60e7f6375ff1458
  - id: LTP_906135780505447D
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:906135780505447df3e13e314003f581efa2d1ee30de2ea30dbab0143fcce9a6
  - id: LTP_911B97B972658989
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:911b97b97265898970041564ec32af260903836d6b1beced9f5ec5c56eec3eb6
  - id: LTP_919ABCA2598F53B5
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:919abca2598f53b5e99bbe5acec60bec538242577a44344d469f5612aef69a6b
  - id: LTP_921D4802D7690C64
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:921d4802d7690c64baa13cef4036a930795dd4b8c1c86da11196a6ab251cff74
  - id: LTP_9260E923CF8AA018
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:9260e923cf8aa0181ff0dc6f6891dd95b28c969e2c31087d648a8189707dcfed
  - id: LTP_929B120944D8F805
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:929b120944d8f80593edbc399d63daf30147188d1cf373314a057f761df649e2
  - id: LTP_93949494FBAD3568
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:93949494fbad356821669ef617a89d87a34da4d9887617ed573781f5ae519106
  - id: LTP_94E36E221125BFAF
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:94e36e221125bfaf16f84bfbaf02a7e3205a99944a0fa27e9cea98ed8642a92c
  - id: LTP_955ECE70D81CA226
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:955ece70d81ca2265720d6c55e260bedc4dd54b36cafd2073a3878f975bd7087
  - id: LTP_96021AFB69E847F9
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:96021afb69e847f97d69047d8752f3a007ac9e37dab787c2aa17cbd86cd4ba43
  - id: LTP_969C39F409BFD7AA
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:969c39f409bfd7aa54d82173400747fbba4044a6be5c4266dc75d7f6ef1444a6
  - id: LTP_96D205FACA0DD8DB
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:96d205faca0dd8dbe6122553b7e15b664912bfab18ee1ab4bf67591c7fb581e3
  - id: LTP_96F07DC5DDC8E018
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:96f07dc5ddc8e018a3a3a8044b0bf164f2d608e7ae0b79cced18aa24b0729285
  - id: LTP_97C442AC56780374
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:97c442ac5678037400d83150dbb28aa04f594bf29de4245f75f1c23d732a08fc
  - id: LTP_9866FB6F1F726CA0
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:9866fb6f1f726ca09b77bd655c3a477b9ef2d3857d60561868a8240341b223aa
  - id: LTP_986F211E7D45CAD7
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:986f211e7d45cad74127bbc87f5e50b69ca7ee71e5aa523e5c87ab76ef11ba93
  - id: LTP_9A723EA0B1F0D1BE
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:9a723ea0b1f0d1be76bccdcb190d1564f1fc1b71f3ad775b55c9121b1402052f
  - id: LTP_9C9D222A34799D55
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:9c9d222a34799d55b8df29a5ca8c61ca4dd502b6f2a003c5f6b3bea7ffd51fff
  - id: LTP_9CDCD3C4BA6C2702
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:9cdcd3c4ba6c2702bcfdc87ff580ae8965d93fd14c816da9e2cb2da5bf7f3a32
  - id: LTP_A17272D4FE0F040B
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:a17272d4fe0f040b3551f0c48f7f679eac6329498adc53aa6c28b6db119761c0
  - id: LTP_A1DEE046C0A10B18
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:a1dee046c0a10b1867a71cbf9e1fa5cda71eb744c20dcee680c7a1b838ffe8f9
  - id: LTP_A30F7687D403407B
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:a30f7687d403407bd6fca8b3e2dae3e7d78a7a44247e4ee6ede6bcb7e5c4be0b
  - id: LTP_A4060315D2E047EE
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:a4060315d2e047ee719f30e5665b983e33cfebf352c8040520b504f3fb57eeb5
  - id: LTP_A4733D4B2FEBE9A4
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:a4733d4b2febe9a4e637179d892540534842c69fb8d76e018b5dc5c23c66daf4
  - id: LTP_A500A46C4B998E74
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:a500a46c4b998e741de132746e8b0b0af9bdf29d85cac68d7f2acd81814c2c62
  - id: LTP_A6B94E8A2A4D8853
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:a6b94e8a2a4d885377e082223b765961646dbaa4510911162986a491fd28f7dd
  - id: LTP_A9544B59EB6712D9
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:a9544b59eb6712d94dca462aac20f704d4535396cc91193124901c37b73cbf45
  - id: LTP_A9596E932167B3EF
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:a9596e932167b3ef67bc5be85c77f5f7186b148d1d991e588809c2e0180f3a82
  - id: LTP_AB48F262BBB2CC93
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:ab48f262bbb2cc9376b9361a581295adf4c119fb72babdbec46a9c3fceb34c36
  - id: LTP_AC0FB73B4EE420EC
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:ac0fb73b4ee420ecfea385432c4abfe9c2c3b14391ddd2970259d31c1f078ee8
  - id: LTP_AD81218450587FA8
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:ad81218450587fa8b2318bd795c03007cebfed4129850ee359cfc4131427079d
  - id: LTP_ADD30BEEC40E661F
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:add30beec40e661fc3944ee505b4d769fc54d04f71f942462c6cb43630563870
  - id: LTP_B1D822DF0057B4E0
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:b1d822df0057b4e0eac5216fb772e5d0c67dc95c27884035caa5b94c422e5b81
  - id: LTP_B200AFD97E91C2CC
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:b200afd97e91c2ccb465d33728cb17a5abb857c8c016b9f250cfdb1d2c759a2c
  - id: LTP_B53406D510ED4981
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:b53406d510ed49814b3727cfd8c65d414738713fc20ce0d05e400a015ab9779a
  - id: LTP_B6DAF13EF3143EBF
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:b6daf13ef3143ebfc55e0ec850c878d9500e8473f37a55945927c59c6421e6f9
  - id: LTP_B9908D4015443661
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:b9908d4015443661be8818bffa5f28fd1ab370bc37b054db41ada6f87be58e3f
  - id: LTP_B9CDD41A0DC2AFCC
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:b9cdd41a0dc2afcc67185697f8300fffda120b752a387b2b4bebce66b8e3556e
  - id: LTP_BA10984A4B0DE2C6
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:ba10984a4b0de2c627f9d0f52b2a95d6cefc04c10e7118c64201ddb965ef6912
  - id: LTP_BC662075E3BAE807
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:bc662075e3bae80716721d493d2ecb205c425c8d4036a15537b8b67f1d6c41e7
  - id: LTP_BE2E778739EF01D5
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:be2e778739ef01d53e5c394d3e4f4103b51e2ad54fb2ab15a8e37ce409044314
  - id: LTP_C0577C0D678214DA
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:c0577c0d678214da548753b907d5506a697884d30765112eb0a6df1dee8eb040
  - id: LTP_C071A7FFF929A2A5
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:c071a7fff929a2a5776da6862c4f0aaf5902ad0b0bb61779ceadca9f556fceaa
  - id: LTP_C0AA45BC29F98A0E
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:c0aa45bc29f98a0e7e47e5f8289bcbaa8298f2dd9baa2a322f25acc464663544
  - id: LTP_C1C67435FC56D878
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:c1c67435fc56d87840f092f5726c75284aa449ae5aca2a9d076cde8bc341ab4b
  - id: LTP_C5FE18F9550B31BA
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:c5fe18f9550b31bacd167f490f815fb96ef18cdfa2d50996ca49c23cbad4bf77
  - id: LTP_C6A719982BDE9CE4
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:c6a719982bde9ce4456fee47f9a74e3e085b5e587b7c1f3b1593b6673551c887
  - id: LTP_C6E67CB1FD2B1F64
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:c6e67cb1fd2b1f645c00f57dd53b305566c4d2f510659da09bc7d47a3e68bfe3
  - id: LTP_C8DAE34819E335F8
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:c8dae34819e335f88d2bad8650e2067ec51e8a1c6d21ef37198241a9af5a56f2
  - id: LTP_C994B56A41A71C1A
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:c994b56a41a71c1ae8b34f44da5b8c78d6f0c14ccdc0067d6398cdb48f4c54d6
  - id: LTP_CA45A33676AD236D
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:ca45a33676ad236da5a59d05b5ed7f937b678b76b2b427c0416f8ca8966c1e6d
  - id: LTP_CA80C3F10B65226D
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:ca80c3f10b65226de17483b8685372fb4aa133ac10a2a11dca2bb1c33b9b01dc
  - id: LTP_CB31E19EE807FFDB
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:cb31e19ee807ffdb5836e24f23c68978f710465f4190b09f63bedd88cad364a2
  - id: LTP_CCDB1776DAA2C318
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:ccdb1776daa2c318c58907012899ab82a3b26a30cc45002a853928e842f26813
  - id: LTP_CDCDC1B9E63D58C3
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:cdcdc1b9e63d58c38e0342f9f6a8d311e1bc7314f7faae3ee2ca47a71d9455f4
  - id: LTP_CE45382D3DE75F8F
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:ce45382d3de75f8f280054000f338075bda0efb06b7920ed5028dbe2c9762a0d
  - id: LTP_CEBAD6AB3C82795E
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:cebad6ab3c82795ef8bc7e31c4d7f005f68342cf154bfae4d5f232ec2997fd8a
  - id: LTP_D1F469715ECC4195
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:d1f469715ecc419564dd027615d3da31a0126f706ae147e1191a041e4a2d06ab
  - id: LTP_D2D67AB5E38A7000
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:d2d67ab5e38a7000f636bb8ea94430224ae59507a8e362a2e8601c835285925e
  - id: LTP_D2F4BCF2263C56F5
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:d2f4bcf2263c56f511e85ed0974323b7de92a5c313314142b314060cfa3416a8
  - id: LTP_D412A09DEDC43045
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:d412a09dedc430455bcaee23066531008ffc400c39cfec08a2b7c0560f283513
  - id: LTP_D4D8A0FEAA2F6B09
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:d4d8a0feaa2f6b09ee4197bda4acedae9ed3a247bb92e107645b013a2b97a9df
  - id: LTP_D653D15777B77A1F
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:d653d15777b77a1f2f22b9ad51399e98948cbcfeb7dea90eca3bcc1dc2c72c13
  - id: LTP_D6A52FD61BF01578
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:d6a52fd61bf01578d57b2137fb8783fa4aa12fbc36528c0fe57c44869f8ae3b9
  - id: LTP_D72526C4E4301D60
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:d72526c4e4301d602772892e7acb7d791190ad295c689edee33935e8a3042142
  - id: LTP_D76652434EC85091
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:d76652434ec85091cb128b18a9f43cf85789b33a1273659abba33ea994dabbf6
  - id: LTP_D8B58CA743EBE711
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:d8b58ca743ebe711572368b5326e991fe7d9c9c30c831d41aa6f61099d65190b
  - id: LTP_DA10E351BC730D85
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:da10e351bc730d85ee340c6d45341d502bce7d6d63af45b2e0c8bb9d7fd6c0d7
  - id: LTP_DAA03BAD070DB1D6
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:daa03bad070db1d65d975ed3b9f2ec6be962774a8144dce2900b7ac44b218781
  - id: LTP_DAA1F16D8A298E83
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:daa1f16d8a298e831f352e689972a6839bc2efd8aa77712fc9b65fcfd0b01654
  - id: LTP_DCB33BB29D296843
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:dcb33bb29d296843e50e422e7bb1475ebffefc2ec76a9abe68e61f2e069ec65a
  - id: LTP_DD9A41090E3D5A17
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:dd9a41090e3d5a1757e1766c5d8ba367dcf03e04ead95254afac13d6550f0f6b
  - id: LTP_DF1C4714B16B760E
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:df1c4714b16b760e1517fab21e4b1587a03f487b2fe3b271a21f7f899eb5eb07
  - id: LTP_E0B177A8B6FE4225
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:e0b177a8b6fe4225e1088c7e49e952d5a51527d7a94a71d142baf04be4b83566
  - id: LTP_E0ED96B80FC3B6C9
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:e0ed96b80fc3b6c96463b988f7e4d1ff0b79e1c58a353675386fc6420ccc5977
  - id: LTP_E28B5BB57A450438
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:e28b5bb57a450438b801a06bacaa75df24298a8f5ef516fe12005237e4222539
  - id: LTP_E2C3B68EDF07A753
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:e2c3b68edf07a7531dfea80c2aec3daba99b0f2c156c60994d6969b2e2bc6ca4
  - id: LTP_E34945E3DE91022F
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:e34945e3de91022f5bec4e3400409e0b76cc76cfa4fefaa6a605861cab436485
  - id: LTP_E3A3CF8B98E460BC
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:e3a3cf8b98e460bcdc3034c9ebc9119094619ba2a33d775e86736f6ea1c7c9df
  - id: LTP_E41DD7230DA067DD
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:e41dd7230da067dd49192e171fa405245c34ff3e23ce95a67114c3fbbf4bb303
  - id: LTP_E46539F2D47BA5EC
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:e46539f2d47ba5ecd80e66b6a5705003631d65d3d38e7882c5c59c8c2f39bf6d
  - id: LTP_E4D1B76D80905462
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:e4d1b76d80905462632ab0976fb3a8a26184ee6aa72bb777ecf0d2437c1fd88d
  - id: LTP_E560C027210BF20A
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:e560c027210bf20ae0ba8e32c02cb2e43fe1db33a34b5477b45c38b8ecd001a7
  - id: LTP_E5791B389C67677E
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:e5791b389c67677e342a600db8a0a3d60536e7627457c447be4dada2a41f5ac7
  - id: LTP_E5E50FB7BDD033D9
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:e5e50fb7bdd033d91ceea657540c90d9a0421e2feba98ad411da85613f9b5eff
  - id: LTP_EB00EA74B30E438E
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:eb00ea74b30e438e0d9c68d1d22c8fc796810ed865f7a571844bd636958fce93
  - id: LTP_EB425D988F2F7604
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:eb425d988f2f7604459aba4e2fe34d6371def71a7110eac5b39dc26f87bb2f23
  - id: LTP_EBF0020C32AD44C8
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:ebf0020c32ad44c8ad58e315c1e1cb903e5ed0c419a287e8244869f99cd010d4
  - id: LTP_EC19C6410BBE0467
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:ec19c6410bbe046794ecd79ea7efcb5440012eeaef0061223f455112ff1abb4f
  - id: LTP_ED36488372A175F5
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:ed36488372a175f572327b2a4ffbb7ee1509564d2f52f87cc53af698d7eaf6ad
  - id: LTP_ED3F2AE7E59E6F12
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:ed3f2ae7e59e6f12449fce7c967c0ee394349eeea8de7184501ffbbe24b39bec
  - id: LTP_EE1518958A8F7CC1
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:ee1518958a8f7cc104b201aea93c7258d1fe238563ecaa79fd379a3f94b86448
  - id: LTP_EF5C1F365208AD31
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:ef5c1f365208ad3151d7a53443d6ed6ff0c0fbeca716601c062432a23043bae7
  - id: LTP_F202F3C3B02DEA0E
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:f202f3c3b02dea0e6634d113d533b6a816eafdc78c86c34983862ea92a2bdaa6
  - id: LTP_F3200B697F38DD16
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:f3200b697f38dd16dd728a01f6d8986b402618b4821c5d5a4fe155be69464bc6
  - id: LTP_F3418C5C403B91FC
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:f3418c5c403b91fc13bbab2d80e1b2c05b310be5bd1e672739a6b95a809c0208
  - id: LTP_F43EC0D01CCFD25A
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:f43ec0d01ccfd25ac4dd3c4082864a81a6865fd2d33a7edd8aca614964fe2616
  - id: LTP_F6BB86F5DCC2FAC8
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:f6bb86f5dcc2fac8464bad08ce2e6618eb095e35aeab4e9102598e90d725c1c8
  - id: LTP_F70FC66A56FBD769
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:f70fc66a56fbd769284bfc5c23ca42e3abc7d54a1de2bac9c0ef3f614707ad91
  - id: LTP_F7998813C90A7A08
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:f7998813c90a7a080b3d06433b1f67f20f57e9a58a6ecd3ee851168e86389f2c
  - id: LTP_F8CDD57D76C8FA6C
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:f8cdd57d76c8fa6ca80724732e2773c1a4fe6c09ac6bcc0cdd61aba4431f958b
  - id: LTP_F9BF08369A08E5ED
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:f9bf08369a08e5ed4d4a0ff15288e2395e0bbe2a5414e7a7fff39799cb12acd7
  - id: LTP_FC5B16AB3C53A744
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:fc5b16ab3c53a744edca87ac69737e86b586e7fa8fdb3afc25acf0b3e394f5ef
  - id: LTP_FCA376B46A9873B0
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:fca376b46a9873b02e521509666d25f9012fe2fafdad6f776326dc146bc0ac6a
  evidence_count: 10
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: acct
  source_fingerprint: sha256:778fab6dd104a47c066d101145ad21b83418b7731b03e1881f4bb4ccd6de761a
  recognition_fingerprint: sha256:af12c2c0f6b92d0adbafbe874807f113f8826a93be30232a80727eea92349910
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 8
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: add_key
  source_fingerprint: sha256:bb9d7d97d5e05a202c79cac249656518d9edefe0cf6ccd2a2cac33c7ad6bd739
  recognition_fingerprint: sha256:2cb8d1e4f99d375130ae605a3d452c970bfd887d03daea92ebe3febac32f2808
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 15
  unresolved_evidence_count: 5
  reason: unresolved_evidence
- syscall: adjtimex
  source_fingerprint: sha256:c17be8a0f4a471625ee5bf619cb5993cdbd886e108b7ee1cc9cbc362949a9edc
  recognition_fingerprint: sha256:3d8c89272214bfc21a26ca2cd359b08ff3de1db0619d508a2aff4b69e7559159
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 3
  reason: unresolved_evidence
- syscall: alarm
  source_fingerprint: sha256:5061762caf00b96445d3a6532d0f653e3ad72c3451ff67190cb2dd007b36c6df
  recognition_fingerprint: sha256:75022c75739f0480b4c3a057d03befecdf28560f238d9aa9351d8b582fda2c0a
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_1A9481FAD460FBF7
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:1a9481fad460fbf78c35e41fcfc8799bab17d5ea12dca5910fcac0ba464bd776
  - id: LTP_3E8DA9E014B82702
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:3e8da9e014b8270237da29d11e36cb3568c2b222d672973a5503c5d451873729
  - id: LTP_6449E4A1D20C01D3
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:6449e4a1d20c01d34f2f8847a0e41c28dcb6b6515a24692cc3820005faedf3df
  - id: LTP_65B70356F06E31F8
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:65b70356f06e31f852315fe3be36507e963aadb6d4dc164a7abe5194b80c9713
  - id: LTP_76A9B6CF388A8609
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:76a9b6cf388a8609eeb2a9e479fa27419ade916ce166ad5c0e8255aa5f4497d5
  - id: LTP_82621B02FCA09F40
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:82621b02fca09f40310757b7ff831c290f08ab01be6a5ea4bc4c74ce2db492cd
  - id: LTP_98EC66149EE68933
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:98ec66149ee68933043c3d08d35dea4ea3d8145e3e6e4c72dfd96c786ca3c307
  - id: LTP_B7A341967DF2BD69
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:b7a341967df2bd693bb7f1bd2a9d165ae51ec15aa83ec06f274bc9e6ed7dbd8e
  - id: LTP_C785774773FB7524
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:c785774773fb7524870d7b604061d2af95f33c66253633d4323113134440929d
  - id: LTP_C7B73F4D5B87736A
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:c7b73f4d5b87736afb434f999fc75233df1703e63bf0c31b5b8eb241adef31b2
  - id: LTP_C80C019BE3F47901
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:c80c019be3f47901f55816308f54ee6e895f5df8a818ce4d61e002ce96470fdd
  - id: LTP_CD2150BE4FE81F31
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:cd2150be4fe81f31d96048faf2fd894533271cce5b64d7f76119b5d3b31387e4
  - id: LTP_D1B6112551D45B31
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:d1b6112551d45b31a564bdbe96d936daffb4747eabac294fc9969f6dfe1c9850
  - id: LTP_D4B433A3696803A8
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:d4b433a3696803a8932f8a59a7d40caabfe8f9b592dc394ed4d920b4832325d3
  evidence_count: 15
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: arch_prctl
  source_fingerprint: sha256:352e7cb11b18f12d0d54956cad6ea6f04c6eb7ea8c286f40acf3fcc0c0c7c99d
  recognition_fingerprint: sha256:290591717e1cf2ede1f34092086eaacb0ea966a7f2d0dd60ba87fe9d381feca0
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: bind
  source_fingerprint: sha256:6757c120aa38501c98fe10599592fb38b6815bdde448c1ea2972a7ebb3e9fcd9
  recognition_fingerprint: sha256:dcc6229d1768a7efb39a99c2270a23b4e9924e68a0e8a9aeec5c88aad27be6cd
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 9
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: bpf
  source_fingerprint: sha256:9a280c7b7b0ca4f39ef98af787831781cd61a8277419a4e182d47168763943e9
  recognition_fingerprint: sha256:5b4870a068476ab2bae6496bc46f86bf51b7fb6dce8ea91e821655cf80e64e85
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 12
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: brk
  source_fingerprint: sha256:773ad4a8d0c3ca4bea04dc5191f0c4fae1f3cf4c12aa2b09053d77e6e7cf78f9
  recognition_fingerprint: sha256:9d4ad0a25cc0aa00a47c1852f8bc3b1e040195365b2868cb11e811fdc6e2c920
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_7A74A699442CEB99
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:7a74a699442ceb99b8495ac52144744c5a7e995035d4c06a10971ce532e8e954
  - id: LTP_E3E59B16A96A60BC
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:e3e59b16a96a60bce3de89603588b78a310e40b3710e530d67d5c30160121e86
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: cacheflush
  source_fingerprint: sha256:65cbb47cf546e3d52fb1d343cf2f522fb89be0d41088a6ab73007fc40831cb3e
  recognition_fingerprint: sha256:5518246950ceefa49eb510895091de1511938691cccc0bad2a6426b9c3ab7226
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_8AD8032754BC8842
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:8ad8032754bc8842e1ceffe416a3d559f5423eec53ec7db46ee81a6eeba25869
  - id: LTP_C218D3CB0AD80D90
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:c218d3cb0ad80d90bc2c5db1a2892a964c1bc89369fc4ec66a71fac08ac8f5f6
  - id: LTP_D579FCFC71E6EB6A
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:d579fcfc71e6eb6a79a4aefff0c4df8ba201988162fee4b24255c4c001c1302b
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: cachestat
  source_fingerprint: sha256:8967c456145a32184aadba3911d0b0b52ffcd2e88c5f08d3907631ec64d4d082
  recognition_fingerprint: sha256:f56d30beba1fe72b5892668889efed5fbce37bda6c3ee03372d10251766df7a6
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_00F2A9EA8833DA1D
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:00f2a9ea8833da1da8949ee468fb47004f99f1116ae6cda9ea3ba127e264058a
  - id: LTP_1325C077A1CDE514
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:1325c077a1cde5141c5f598497a0fd7e10c5adeda759688a6fc3b2f02cc64aab
  - id: LTP_34EC9FB9C9551214
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:34ec9fb9c9551214fcca5118b8afb84e93c9e242cbd9c2674d0b9d0ec70c9566
  - id: LTP_7FD6142E0E88CF17
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:7fd6142e0e88cf177fb735c36d08a2ed91ecc3830a60463895683ff3383da791
  - id: LTP_89C9E8458EC38C11
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:89c9e8458ec38c1192fb6eeb76cdcd58fc7b36e08a155e776975b94da2abf980
  - id: LTP_BA9A8FE901467960
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:ba9a8fe9014679607013f8aa7b560aec873309bb14116b916767925e8499f776
  evidence_count: 7
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: capget
  source_fingerprint: sha256:a4adf6dfb51d8b7b763f6961c2ba419156d4f5c630b1222eb18661aa0731abd9
  recognition_fingerprint: sha256:ef2866aec0c0dfb71f9c19336ba0119a22f24dbd5938b7e5f3e476f03015276e
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_208C833FF12217F5
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:208c833ff12217f5ee10c2893ca4aab718793f8504783e4c1e69970fe3fc01dc
  - id: LTP_5F1D35ACCEFD4971
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:5f1d35accefd49711e3b8b82de258ecb2f04bba65083b919659edb660948ef2f
  - id: LTP_827CE5CB448A411B
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:827ce5cb448a411bcd82f3a89e9c733eb11fa4d44a8f563ff1658dac81bd73a4
  - id: LTP_CED2FCC737A99D40
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:ced2fcc737a99d40bc85fda1ad7df308a9af646010036252eac3d2cc5d384bb8
  - id: LTP_DC9BC72148835FDC
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:dc9bc72148835fdcfc9cca3b1db4ce73b4cae94f45535d8bc89f01eb527400b0
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: capset
  source_fingerprint: sha256:76e0ae5def1debb091b7c2611d3e9b29b4fbec6a1e05da1d893f0a5d3fb92fda
  recognition_fingerprint: sha256:edba938d09019bb9d3effd87e839b7ddbc98af062967d829361a53ba5614c3a5
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_461340ED83E7043D
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:461340ed83e7043dea9542c2f07e235985dde3b81cc4c09f450b1c1df07be266
  - id: LTP_6D86AFD541A61388
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:6d86afd541a613880ff94fbbb7fbfdbbebd5fd32d94544f7cc6e3f2ee850df77
  - id: LTP_7DEDC53AC33C891F
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:7dedc53ac33c891f5dc26a9f6c36be055e5347807fd55cc59f6800da4424f720
  - id: LTP_A00E343F4A556B3D
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:a00e343f4a556b3d95ff7c9596db5dad52a7bcce09ee6424a48853bc04d5c4af
  - id: LTP_D1AADFC2F7C6F594
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:d1aadfc2f7c6f594928cbc9032ee1cc614ab7493537d5f16041f8e5885973b3b
  - id: LTP_E06D53042C10C99E
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:e06d53042c10c99e7bdc61242d4ac56e1aace8c13e3442e875e2574ca74e60d3
  - id: LTP_EC23768761E40E9F
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:ec23768761e40e9f99140715f9e6147dcc348f9f7bbdc7731948b1afb6d29d51
  evidence_count: 10
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: chdir
  source_fingerprint: sha256:25fb76905e5cf9ba7725b687859c07f6e6860bc3c6ca3664033dca1e1bd80444
  recognition_fingerprint: sha256:8a7fe3e9bb6f7cde4e867565c9d19e5653423668835501249020770558b244ee
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: chmod
  source_fingerprint: sha256:715beb994e68f7d92c1075f36cbad9da57dcabfc154f4f3f39aa1c282a8d3970
  recognition_fingerprint: sha256:457bb049fecc3b257739e446945ad9821a265f710a02c31d667a815d0229ea66
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 15
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: chown
  source_fingerprint: sha256:becc3d2d6527b1b4d7c845031e0ae8d74d3deee859efe6bf2bc64288d94e8c18
  recognition_fingerprint: sha256:825a6da218b110883db67ee4e2f7b5aedccb1c2fe473366089e11bd28703af5b
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 22
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: chroot
  source_fingerprint: sha256:cb75700a0413ef1f98114d8135c65f0fa0983a8affef1a8494c5f7a36636d723
  recognition_fingerprint: sha256:cacbe2412f7631d855ab5085cd342f675391a3bfe916ba6109596a82f126cec0
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_245CD61DAA19DC98
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:245cd61daa19dc987195efcf282a428df3dfc7429cd89bcc1fbc741e96407c30
  - id: LTP_50F858A3CBF95EED
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:50f858a3cbf95eeddf59e035a757996bbd15f7d42379f5ea72330ceb0f3e6190
  - id: LTP_71C54C624831C7F0
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:71c54c624831c7f01c5ac8d48046dc370b784af8dc2099633843d4269593e9f7
  - id: LTP_99DF5C34778032E1
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:99df5c34778032e1483871676a4cbb8fc57a3bbfcd2fd0c74f90f83147e1a5f8
  - id: LTP_D0E32E5D27E643A9
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:d0e32e5d27e643a92fca4116aaeefb86ce87cdcc1e5fd0d511ff4dbdc52401cb
  - id: LTP_EBD54180D0CAB16B
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:ebd54180d0cab16b9271d149769e3e3e522ef97222514360017b81114bcc90e1
  - id: LTP_EE7A979F212D6C0C
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:ee7a979f212d6c0c9e2e3e7cf8fe3078537cd1d9a5e51d2b9d1800e88e29a363
  - id: LTP_FF9C0F9669A39525
    generated_at_utc: '2026-07-15T03:09:52.149069Z'
    content_hash: sha256:ff9c0f9669a39525986267a75a9b66e6249d23f8939029c388c3f8f1c9ec1472
  evidence_count: 8
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
```
</details>
