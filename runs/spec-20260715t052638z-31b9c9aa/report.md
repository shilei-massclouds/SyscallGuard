# Syscall 合规性规则提取报告

## 结论

本次分析了 clock_adjtime、clock_getres、clock_gettime、clock_nanosleep、clock_settime、clone、clone3、close、close_range、cma、confstr、connect、copy_file_range、creat、delete_module、dup、dup2、dup3、epoll、epoll_create，发现 59 条可执行的合规性规则。

## `clock_adjtime`

没有形成可发布的合规性规则。

## `clock_getres`

没有形成可发布的合规性规则。

## `clock_gettime`

没有形成可发布的合规性规则。

## `clock_nanosleep`

没有形成可发布的合规性规则。

## `clock_settime`

没有形成可发布的合规性规则。

## `clone`

没有形成可发布的合规性规则。

## `clone3`

没有形成可发布的合规性规则。

## `close`

共形成 5 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_09B39E9C9254ECB2`](../../library/rules/ltp-09b39e9c9254ecb2.yaml) | 文件描述符已经关闭 | 调用 close(fd_closed) | 返回 -1，errno 为 EBADF |
| [`LTP_0CD17E662AFD2956`](../../library/rules/ltp-0cd17e662afd2956.yaml) | 文件描述符无效 | 调用 close(fd_invalid) | 返回 -1，errno 为 EBADF |
| [`LTP_2BDE60C0E64B4DC8`](../../library/rules/ltp-2bde60c0e64b4dc8.yaml) | 无额外前置条件 | 调用 close(get_fd_pipe()) | 调用成功，返回 SUCCESS |
| [`LTP_BF2428964ADD116F`](../../library/rules/ltp-bf2428964add116f.yaml) | 无额外前置条件 | 调用 close(get_fd_file()) | 调用成功，返回 SUCCESS |
| [`LTP_E520E500AB3AE851`](../../library/rules/ltp-e520e500ab3ae851.yaml) | 无额外前置条件 | 调用 close(get_fd_socket()) | 调用成功，返回 SUCCESS |
## `close_range`

共形成 6 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_31D9D767D6888DDA`](../../library/rules/ltp-31d9d767d6888dda.yaml) | 无额外前置条件 | 调用 close_range(fd, fd, flags) | 返回 -1，errno 为 EINVAL |
| [`LTP_425E5A3502541DE8`](../../library/rules/ltp-425e5a3502541de8.yaml) | 无额外前置条件 | 调用 close_range(~0U, ~0U, 0) | 调用成功，返回 SUCCESS |
| [`LTP_76BFF56F735A0074`](../../library/rules/ltp-76bff56f735a0074.yaml) | 无额外前置条件 | 调用 close_range(fd, 100, 0) | 调用成功，返回 SUCCESS |
| [`LTP_CBF4B6C8A1458A28`](../../library/rules/ltp-cbf4b6c8a1458a28.yaml) | 无额外前置条件 | 调用 close_range(3, ~0U, ~0U) | 返回 -1，errno 为 EINVAL |
| [`LTP_F1DC44813DCA6A05`](../../library/rules/ltp-f1dc44813dca6a05.yaml) | 无额外前置条件 | 调用 close_range(4, 3, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_F4DE81D703447628`](../../library/rules/ltp-f4de81d703447628.yaml) | 无额外前置条件 | 调用 close_range(fd, fd, 0) | 调用成功，返回 SUCCESS |
## `cma`

没有形成可发布的合规性规则。

## `confstr`

没有形成可发布的合规性规则。

## `connect`

共形成 7 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0FCE63CBC47F69DA`](../../library/rules/ltp-0fce63cbc47f69da.yaml) | 无额外前置条件 | 调用 connect(s, (struct sockaddr *)&sin1, sizeof(struct sockaddr_in)) | 返回 -1，errno 为 EBADF |
| [`LTP_132A1A1638D957AF`](../../library/rules/ltp-132a1a1638d957af.yaml) | 无额外前置条件 | 调用 connect(s, (struct sockaddr *)&sin2, sizeof(sin2)) | 返回 -1，errno 为 ECONNREFUSED |
| [`LTP_2F153EBAAD2A779C`](../../library/rules/ltp-2f153ebaad2a779c.yaml) | 无额外前置条件 | 调用 connect(s, (struct sockaddr *)&sin1, sizeof(sin1)) | 返回 -1，errno 为 ENOTSOCK |
| [`LTP_4C3A8A7664F22B7F`](../../library/rules/ltp-4c3a8a7664f22b7f.yaml) | BAD_USER_ADDRESS | 调用 connect(s, (struct sockaddr *)-1, sizeof(struct sockaddr_in)) | 返回 -1，errno 为 EFAULT |
| [`LTP_6AEB77CEC03D0E6E`](../../library/rules/ltp-6aeb77cec03d0e6e.yaml) | 无额外前置条件 | 调用 connect(s, (struct sockaddr *)&sin4, sizeof(sin4)) | 返回 -1，errno 为 EAFNOSUPPORT |
| [`LTP_74E00510F4C1B849`](../../library/rules/ltp-74e00510f4c1b849.yaml) | 无额外前置条件 | 调用 connect(s, (struct sockaddr *)&sin1, 3) | 返回 -1，errno 为 EINVAL |
| [`LTP_7D53002758BFC516`](../../library/rules/ltp-7d53002758bfc516.yaml) | 无额外前置条件 | 调用 connect(s, (struct sockaddr *)&sin1, sizeof(sin1)) | 返回 -1，errno 为 EISCONN |
## `copy_file_range`

共形成 17 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_09370275EF5F3065`](../../library/rules/ltp-09370275ef5f3065.yaml) | 无额外前置条件 | 调用 copy_file_range(fd_src, 0, fd_dup, &dst, CONTSIZE/2, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_11CB16D3E88491A4`](../../library/rules/ltp-11cb16d3e88491a4.yaml) | 无额外前置条件 | 调用 copy_file_range(fd_src, 0, fd_rdonly, &dst, CONTSIZE, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_2ACD165E402BB8AE`](../../library/rules/ltp-2acd165e402bb8ae.yaml) | 无额外前置条件 | 调用 copy_file_range(fd_src, 0, fd_swapfile, &dst, CONTSIZE, 0) | 返回 -1，errno 为 ETXTBSY |
| [`LTP_6A2F1D2BB0EE8C22`](../../library/rules/ltp-6a2f1d2bb0ee8c22.yaml) | 无额外前置条件 | 调用 copy_file_range(fd_src, 0, fd_append, &dst, CONTSIZE, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_74BB3F96CBA52D02`](../../library/rules/ltp-74bb3f96cba52d02.yaml) | 无额外前置条件 | 调用 copy_file_range(fd_src, 0, fd_copy, &dst, ULLONG_MAX, 0) | 返回 -1，errno 为 EOVERFLOW |
| [`LTP_76D3B1710474AAC2`](../../library/rules/ltp-76d3b1710474aac2.yaml) | 无额外前置条件 | 调用 copy_file_range(fd_in, off_new_in, fd_out, off_new_out, to_copy, 0) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_7CB2C1C8643130AD`](../../library/rules/ltp-7cb2c1c8643130ad.yaml) | 无额外前置条件 | 调用 copy_file_range(fd_src, 0, fd_copy, &dst, ULLONG_MAX, 0) | 返回 -1，errno 为 EFBIG |
| [`LTP_7E1612F09CACE33D`](../../library/rules/ltp-7e1612f09cace33d.yaml) | 文件描述符无效 | 调用 copy_file_range(fd_src, 0, fd_dest, &dst, CONTSIZE, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_7F43697FAC4213A8`](../../library/rules/ltp-7f43697fac4213a8.yaml) | 无额外前置条件 | 调用 copy_file_range(fd_src, 0, fd_copy, &dst, MIN_OFF, 0) | 返回 -1，errno 为 EFBIG |
| [`LTP_AE3908C408304451`](../../library/rules/ltp-ae3908c408304451.yaml) | 无额外前置条件 | 调用 copy_file_range(fd_src, 0, fd_fifo, &dst, CONTSIZE, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_B87A71DE5DE1260E`](../../library/rules/ltp-b87a71de5de1260e.yaml) | 无额外前置条件 | 调用 copy_file_range(fd_src, 0, fd_dir, &dst, CONTSIZE, 0) | 返回 -1，errno 为 EISDIR |
| [`LTP_BAE8F852378DD9F4`](../../library/rules/ltp-bae8f852378dd9f4.yaml) | 无额外前置条件 | 调用 copy_file_range(fd_src, 0, fd_pipe[0], &dst, CONTSIZE, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_C16D549555A00E55`](../../library/rules/ltp-c16d549555a00e55.yaml) | 文件描述符已经关闭 | 调用 copy_file_range(fd_src, 0, fd_closed, &dst, CONTSIZE, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_CC9037A76978B569`](../../library/rules/ltp-cc9037a76978b569.yaml) | 无额外前置条件 | 调用 copy_file_range(fd_src, 0, fd_chrdev, &dst, CONTSIZE, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_CE12B215EFDE3D4D`](../../library/rules/ltp-ce12b215efde3d4d.yaml) | 无额外前置条件 | 调用 copy_file_range(fd_src, 0, fd_immutable, &dst, CONTSIZE, 0) | 返回 -1，errno 为 EPERM |
| [`LTP_DB6066C00D231BA4`](../../library/rules/ltp-db6066c00d231ba4.yaml) | 无额外前置条件 | 调用 copy_file_range(fd_src, &offset, fd_dest, 0, CONTSIZE, 0) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_E2196C3F0F58862B`](../../library/rules/ltp-e2196c3f0f58862b.yaml) | 无额外前置条件 | 调用 copy_file_range(fd_src, 0, fd_blkdev, &dst, CONTSIZE, 0) | 返回 -1，errno 为 EINVAL |
## `creat`

没有形成可发布的合规性规则。

## `delete_module`

没有形成可发布的合规性规则。

## `dup`

共形成 7 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0EBD1214FC6BB6D5`](../../library/rules/ltp-0ebd1214fc6bb6d5.yaml) | 无额外前置条件 | 调用 dup(fd[0]) | 返回 -1，errno 为 EMFILE |
| [`LTP_311F7A773994720E`](../../library/rules/ltp-311f7a773994720e.yaml) | 文件描述符无效 | 调用 dup(-1) | 返回 -1，errno 为 EBADF |
| [`LTP_511185D6DE2A63A0`](../../library/rules/ltp-511185d6de2a63a0.yaml) | 无额外前置条件 | 调用 dup(1500) | 返回 -1，errno 为 EBADF |
| [`LTP_594FA5B54CA204E5`](../../library/rules/ltp-594fa5b54ca204e5.yaml) | 无额外前置条件 | 调用 dup(fd[0]) | {'kind': 'return_fd', 'return': 'FD'} |
| [`LTP_84DBE108A850E845`](../../library/rules/ltp-84dbe108a850e845.yaml) | 无额外前置条件 | 调用 dup(fd[1]) | {'kind': 'return_fd', 'return': 'FD'} |
| [`LTP_A774FC10727E8ED2`](../../library/rules/ltp-a774fc10727e8ed2.yaml) | 无额外前置条件 | 调用 dup(oldfd) | {'kind': 'return_fd', 'return': 'FD'} |
| [`LTP_ED2BA909DF79625A`](../../library/rules/ltp-ed2ba909df79625a.yaml) | 无额外前置条件 | 调用 dup(fd) | {'kind': 'return_fd', 'return': 'FD'} |
## `dup2`

共形成 9 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_12A1904141AAE2EE`](../../library/rules/ltp-12a1904141aae2ee.yaml) | 无额外前置条件 | 调用 dup2(fd0, fd1) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_4F02ACC6E2F6B094`](../../library/rules/ltp-4f02acc6e2f6b094.yaml) | 无额外前置条件 | 调用 dup2(fildes[ifile - 1], ifile) | 返回 -1，errno 为 EBADF |
| [`LTP_75D52C5E9C93B6D7`](../../library/rules/ltp-75d52c5e9c93b6d7.yaml) | 无额外前置条件 | 调用 dup2(mystdout, badfd) | 返回 -1，errno 为 EBADF |
| [`LTP_9F560A103CB6F910`](../../library/rules/ltp-9f560a103cb6f910.yaml) | 无额外前置条件 | 调用 dup2(mystdout, maxfd) | 返回 -1，errno 为 EBADF |
| [`LTP_B7F51635806E7E59`](../../library/rules/ltp-b7f51635806e7e59.yaml) | 无额外前置条件 | 调用 dup2(fd[i], nfd[i]) | {'kind': 'return_value', 'return': 'nfd[i]'} |
| [`LTP_BDA36F61423EEB3E`](../../library/rules/ltp-bda36f61423eeb3e.yaml) | 无额外前置条件 | 调用 dup2(maxfd, goodfd) | 返回 -1，errno 为 EBADF |
| [`LTP_D296A517F138A0C0`](../../library/rules/ltp-d296a517f138a0c0.yaml) | 无额外前置条件 | 调用 dup2(badfd, goodfd) | 返回 -1，errno 为 EBADF |
| [`LTP_DE6F80C5EFE44A9D`](../../library/rules/ltp-de6f80c5efe44a9d.yaml) | 无额外前置条件 | 调用 dup2(ofd, nfd) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_EE8E695CF61D6D8A`](../../library/rules/ltp-ee8e695cf61d6d8a.yaml) | 无额外前置条件 | 调用 dup2(fd, fd) | {'kind': 'return_fd', 'return': 'FD'} |
## `dup3`

共形成 5 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_098AFE0E8E10B0EF`](../../library/rules/ltp-098afe0e8e10b0ef.yaml) | 无额外前置条件 | 调用 dup3(old_fd, old_fd, O_CLOEXEC) | 返回 -1，errno 为 EINVAL |
| [`LTP_1726C16756E9651C`](../../library/rules/ltp-1726c16756e9651c.yaml) | 无额外前置条件 | 调用 dup3(1, 4, O_CLOEXEC) | {'kind': 'return_fd', 'return': 'FD'} |
| [`LTP_37C625BD7D7C5F1D`](../../library/rules/ltp-37c625bd7d7c5f1d.yaml) | 无额外前置条件 | 调用 dup3(old_fd, old_fd, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_3A7B17AF231D4158`](../../library/rules/ltp-3a7b17af231d4158.yaml) | 无额外前置条件 | 调用 dup3(1, 4, 0) | {'kind': 'return_fd', 'return': 'FD'} |
| [`LTP_9B3646398697EA64`](../../library/rules/ltp-9b3646398697ea64.yaml) | 无额外前置条件 | 调用 dup3(old_fd, new_fd, INVALID_FLAG) | 返回 -1，errno 为 EINVAL |
## `epoll`

没有形成可发布的合规性规则。

## `epoll_create`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_2D1E25BD679B3494`](../../library/rules/ltp-2d1e25bd679b3494.yaml) | 无额外前置条件 | 调用 epoll_create(0) | 返回 -1，errno 为 EINVAL |
| [`LTP_37F2ED2BA3175CC3`](../../library/rules/ltp-37f2ed2ba3175cc3.yaml) | 文件描述符无效 | 调用 epoll_create(-1) | 返回 -1，errno 为 EINVAL |
| [`LTP_E7435E0CBCA319E1`](../../library/rules/ltp-e7435e0cbca319e1.yaml) | 无额外前置条件 | 调用 epoll_create(tc[n]) | {'kind': 'return_fd', 'return': 'FD'} |

## 技术参考

- 报告 ID：`spec-20260715t052638z-31b9c9aa`
- 来源：`ltp-local`，内容快照 `sha256:d789747f0c0bf1697f538bc5166073fd8449dec3beac7b12ac0be0b1b716dcb4`
- 全局待处理 syscall：353
- 提取数量：`20`（来源：`command`）
- `clock_adjtime`：证据 1 条，未解析 1 条
- `clock_getres`：证据 0 条，未解析 0 条
- `clock_gettime`：证据 6 条，未解析 1 条
- `clock_nanosleep`：证据 4 条，未解析 2 条
- `clock_settime`：证据 2 条，未解析 1 条
- `clone`：证据 9 条，未解析 1 条
- `clone3`：证据 5 条，未解析 1 条
- `close`：证据 4 条，未解析 0 条
- `close_range`：证据 8 条，未解析 0 条
- `cma`：证据 4 条，未解析 0 条
- `confstr`：证据 3 条，未解析 1 条
- `connect`：证据 1 条，未解析 0 条
- `copy_file_range`：证据 3 条，未解析 0 条
- `creat`：证据 12 条，未解析 1 条
- `delete_module`：证据 4 条，未解析 1 条
- `dup`：证据 14 条，未解析 0 条
- `dup2`：证据 14 条，未解析 0 条
- `dup3`：证据 4 条，未解析 0 条
- `epoll`：证据 0 条，未解析 0 条
- `epoll_create`：证据 4 条，未解析 0 条

<details>
<summary>机器可读元数据</summary>

<!-- syscallguard-metadata -->
```yaml
schema_version: 1
kind: syscallguard_ingest_report
report_id: spec-20260715t052638z-31b9c9aa
generated_at_utc: '2026-07-15T05:26:39.098440Z'
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
pending_count: 353
selected_syscalls:
- clock_adjtime
- clock_getres
- clock_gettime
- clock_nanosleep
- clock_settime
- clone
- clone3
- close
- close_range
- cma
- confstr
- connect
- copy_file_range
- creat
- delete_module
- dup
- dup2
- dup3
- epoll
- epoll_create
syscalls:
- syscall: clock_adjtime
  source_fingerprint: sha256:69ddad99dde068306c21dc007b8cb8b2fc6e306e901086c515fbbadb4b124619
  recognition_fingerprint: sha256:6675ac145478812e0be36f0f9d4233dfcd72f5f74fc6eef68a9315253434985e
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 1
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: clock_getres
  source_fingerprint: sha256:0b9da6671694d48980d2fad4fe98a57e68a96afdfed17f11e886c0c51d5d32a6
  recognition_fingerprint: sha256:1b73239a28f9c4aaf53047c3a854b1d1ea1bd32261a3ecaab78c5d53c87e40ba
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: clock_gettime
  source_fingerprint: sha256:316613f4c65a18374ce1a97c1f5f507263ec18197dfce2ec882ae58c875d74cd
  recognition_fingerprint: sha256:8a2b82ecdb5256506b82e9e12d51663e765f3bbeda8e7a390b11c34805946665
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 6
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: clock_nanosleep
  source_fingerprint: sha256:ca8926cc5807281a0625cc6cbd69409fbca673b1b744e4900ee0006e125bcb9f
  recognition_fingerprint: sha256:10d6b463cbd7e6a083a4fed8ccd211e981ea41f94b4ada83f2db48c50d230596
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 2
  reason: unresolved_evidence
- syscall: clock_settime
  source_fingerprint: sha256:e3f446caac41c3a61e96a33b8fa1926b2867c272f97cc09ae6bc6912d8e3cceb
  recognition_fingerprint: sha256:dc8f8e042a9480873542a0db4657fdb6f2f86d777cb22738bd0e0a6e3ab7b5e3
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 2
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: clone
  source_fingerprint: sha256:458a6618ec68b77336a65a488db7bf5595aaaada275374772fe678deead9bd57
  recognition_fingerprint: sha256:ad2a4f0bf11618a7e4a7313ac949dee207a4aa8f5ac0e05b0078e8a97ecc2253
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 9
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: clone3
  source_fingerprint: sha256:8a826a3bcd92cc86db6b98a2fb78ad6882ed9647021d05acbc010caad6952b43
  recognition_fingerprint: sha256:42a33fb451479a969c9bcad3f94983e437b3d59f339684910cea4e483cda38c8
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: close
  source_fingerprint: sha256:775c18f20fd580008f1dfc93ff3b9ebdad2ea3e9b7445a3d222f7c2adcc57f68
  recognition_fingerprint: sha256:b2209213bce85d7ad6ef662cf3ba0b8b56491759cf6188bcc8e89c100953895b
  selection_reason: recognition_changed
  result: formed_rules
  rules:
  - id: LTP_09B39E9C9254ECB2
    generated_at_utc: '2026-07-14T13:35:02.567816Z'
    content_hash: sha256:09b39e9c9254ecb24ccb5288c3f12281e9adc0b698de5c706a4f071599c3ce60
  - id: LTP_0CD17E662AFD2956
    generated_at_utc: '2026-07-14T13:35:02.567816Z'
    content_hash: sha256:0cd17e662afd2956c8c1a42d49b46dca16c37c1972fc6d3632c05c317939a996
  - id: LTP_2BDE60C0E64B4DC8
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:2bde60c0e64b4dc8fc4b1e23c70973364d891d517c1f8020f709fabec59e6d0f
  - id: LTP_BF2428964ADD116F
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:bf2428964add116f793723626820cf1b363a819d6e38ba6d31d9832e4ab1b2c0
  - id: LTP_E520E500AB3AE851
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:e520e500ab3ae8512756eb4a69fdef5de2701520040c400ce896ec773f4ab472
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: close_range
  source_fingerprint: sha256:87c3a9633957b00a8b27f889d0495aeab0e5ffaefbcd742cdc8d1c7c8f8c3cbc
  recognition_fingerprint: sha256:2d2a75d79156d8b1913f699e78ce9a46192ebff91f3dd90b0140d7c8ea27ddf8
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_31D9D767D6888DDA
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:31d9d767d6888ddaf3c03f24abe0bc874e9932a546e4cdd283ecad199e6bcc1a
  - id: LTP_425E5A3502541DE8
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:425e5a3502541de863d8b8e88eafb95db2f8d8e1f9cb88a32d8b3124950395b2
  - id: LTP_76BFF56F735A0074
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:76bff56f735a0074d725ee7dab337c42b7daf23d2ca44135affba4b983676aa8
  - id: LTP_CBF4B6C8A1458A28
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:cbf4b6c8a1458a2885c6c847b47ca93098a06580fc5fdfc3a1e483b9dab01ac4
  - id: LTP_F1DC44813DCA6A05
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:f1dc44813dca6a05d2fb0697718f8ed1da8d8b033d2c49bd0124284321f6ffd4
  - id: LTP_F4DE81D703447628
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:f4de81d70344762893139769a2724588ddb7213c4667529ce501948b3b6b43c5
  evidence_count: 8
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: cma
  source_fingerprint: sha256:07d649de4675a193dbc1f986227505f69fe1c4d4e014188e3a0612373f10caf0
  recognition_fingerprint: sha256:adb36774a3258063b087383db42416c53e822b62db3efd7f3795306377fb3eb2
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: confstr
  source_fingerprint: sha256:10cf8ed6019dfe96ef1008bbc1ca09204fa7a329ad703708481fb13c390e7ed3
  recognition_fingerprint: sha256:dcf06032ba4da5f776872c8bf78f0fb48bae5fb5e2631e55808b9fc44de6efe7
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 3
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: connect
  source_fingerprint: sha256:a06582a3386eb0d4e92f2791535b97d23950b88031311de142270b0c2632b82d
  recognition_fingerprint: sha256:341ace9489af0c8b49ba8d586a1af8a1ee47432d5005caa56b2c62cb51ba84d5
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_0FCE63CBC47F69DA
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:0fce63cbc47f69da5e2da3272c04cf9386103a75c442cf8614d29166e37f3fbb
  - id: LTP_132A1A1638D957AF
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:132a1a1638d957af179480d8ff00129ed60f76772d5c6c6715b2aa4d0707dce4
  - id: LTP_2F153EBAAD2A779C
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:2f153ebaad2a779c607faa895cdd3493a982348174a10df8a80375ab6dd5e426
  - id: LTP_4C3A8A7664F22B7F
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:4c3a8a7664f22b7f2983c449e5c15d82b53d634db19f0a87e67849d4feb2fb77
  - id: LTP_6AEB77CEC03D0E6E
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:6aeb77cec03d0e6eaa956bea440fe8e71843fa521eafcf9611595dee8394b4bb
  - id: LTP_74E00510F4C1B849
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:74e00510f4c1b849cf8495790f1acd5cf1dc690a2ffcef67fc897e0c910fed22
  - id: LTP_7D53002758BFC516
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:7d53002758bfc516d066ece35835e1d8fba92650df06739913ed9b96cb0b9fca
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: copy_file_range
  source_fingerprint: sha256:aad40b5c1bdb6eb2c8db3f08435599ae7bf6269435e49d3f25edbc9dc2ccb8ea
  recognition_fingerprint: sha256:7c0c7a4d601e75d24999f24ace60a35b7cd9f4b8988c664a5568c9fa61873f63
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_09370275EF5F3065
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:09370275ef5f3065d6f3ea10b7288a1ce0668fd80cc67a7d32a6f3b3069149f6
  - id: LTP_11CB16D3E88491A4
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:11cb16d3e88491a45e81d5b0e293f72489bca18cf692ce74215e2ea9a12818da
  - id: LTP_2ACD165E402BB8AE
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:2acd165e402bb8ae893e6740d7e16f0de16ebd3f204944989f8b12cfc1146a2d
  - id: LTP_6A2F1D2BB0EE8C22
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:6a2f1d2bb0ee8c22d0970af42c645ba4f74a3cfe1a4748f4c47934666e135cfc
  - id: LTP_74BB3F96CBA52D02
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:74bb3f96cba52d02850ad3c5e54c87acf278ce51290c99d5ae29da583be9ba38
  - id: LTP_76D3B1710474AAC2
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:76d3b1710474aac2ab3ab05c3535e1d9d7ce9b51219e0b3dece91a57ff8e9ca8
  - id: LTP_7CB2C1C8643130AD
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:7cb2c1c8643130adeccb3e5edc54e1dee2e15b81aebe28002656dca1c395cb40
  - id: LTP_7E1612F09CACE33D
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:7e1612f09cace33d1e08ea245c28317ff95a538558b1d15dc9cd9e6c8dd2eb09
  - id: LTP_7F43697FAC4213A8
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:7f43697fac4213a888a04ab0db787f9579d492101bd363c9674656d420593f80
  - id: LTP_AE3908C408304451
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:ae3908c40830445120c2543a341389434b0eb8a4703f9666a62f96c38d9265e6
  - id: LTP_B87A71DE5DE1260E
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:b87a71de5de1260eeff71a5a683d9dea4fdc6e019dc8875ec98549865ba352ad
  - id: LTP_BAE8F852378DD9F4
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:bae8f852378dd9f45a95e9fa5f5d957ef4f6efa3a462803119cc93500569bac0
  - id: LTP_C16D549555A00E55
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:c16d549555a00e55b3199db30fcc866aeac70c8911afbcc47053c09ffa2a5b85
  - id: LTP_CC9037A76978B569
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:cc9037a76978b569fcf3e91e91771dc63c6a8cf1479d9f5c6e079b8ef0e91e4f
  - id: LTP_CE12B215EFDE3D4D
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:ce12b215efde3d4d62dda72b7a038267b23a8e4347d224d292925db6db534bc5
  - id: LTP_DB6066C00D231BA4
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:db6066c00d231ba4e40e5c33d75b9b778b61a27e92417a8cbf224d48862d8e6b
  - id: LTP_E2196C3F0F58862B
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:e2196c3f0f58862b9dfeb182337b8bdf6ab3964ad73867128bb0853431dc7dbe
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: creat
  source_fingerprint: sha256:2b9c8808a80a99b17b14cc52110d9587c34df34efd59c7e7b794ca975ec67634
  recognition_fingerprint: sha256:eaac8a38ee71bc788d82192692245d5a278bd97d5037ff37b50755614ca06404
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 12
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: delete_module
  source_fingerprint: sha256:36de1e9b3c4df3689c4ebda1d71f45588c3450eca5698989ff4340e579ceac9b
  recognition_fingerprint: sha256:79d96d6881103472ef96a8d4dc56e319c93eed1539dcb7dde3df8c89b64dddcd
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: dup
  source_fingerprint: sha256:9db64fbbc90db4af18b27314f16cea69b28584ec8eac1f6f37ecc29da08d7280
  recognition_fingerprint: sha256:9e7effbbe599b7d58ef6da8ce02e738905293a78b572ea741801f17690357d13
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_0EBD1214FC6BB6D5
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:0ebd1214fc6bb6d5e224e50177509f565c7be9ba6ad0d4842779e564b71dedbb
  - id: LTP_311F7A773994720E
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:311f7a773994720e7cac8cd3d2b12c6938f7c13b7a4eff6dbcfe843e466448ac
  - id: LTP_511185D6DE2A63A0
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:511185d6de2a63a045d2f5f65babdf4c25b4066ece863b9f121419045563d4c9
  - id: LTP_594FA5B54CA204E5
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:594fa5b54ca204e5062358a745af4921e86e002d54071b19f1650a69d2d468f7
  - id: LTP_84DBE108A850E845
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:84dbe108a850e845bf4a3cfc65c984525f06a85bcf44e616283b5ef4e16bb451
  - id: LTP_A774FC10727E8ED2
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:a774fc10727e8ed282a01bc787e12bd54a0d81a756fc45037304c5906dadb2ff
  - id: LTP_ED2BA909DF79625A
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:ed2ba909df79625a7857c363efc0303c51fef469ee87970e6b322004f28779a5
  evidence_count: 14
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: dup2
  source_fingerprint: sha256:b1211d2479e53660fdd5c81f8a3f8d17d043a983d6afb9b9027200a818319723
  recognition_fingerprint: sha256:05901be9485e59299718047de0a27adf7603a7d28a509b7ababb5f3f95373e71
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_12A1904141AAE2EE
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:12a1904141aae2eec702c330f293e0672a34cc4240c6b0ae35b481a3244fa4e5
  - id: LTP_4F02ACC6E2F6B094
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:4f02acc6e2f6b094f06413684c004106e4c18d8f654cbb8b231de56e60aba90c
  - id: LTP_75D52C5E9C93B6D7
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:75d52c5e9c93b6d7989e3392a132ca3a319f4419c2f678533dc80d000c4891cd
  - id: LTP_9F560A103CB6F910
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:9f560a103cb6f910cc2b8fb141c7de076accd6a913e920715328e9facdfb18db
  - id: LTP_B7F51635806E7E59
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:b7f51635806e7e596b7f6a1baf152d74ca1d365a9bdfc6d3f34984ac1908632d
  - id: LTP_BDA36F61423EEB3E
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:bda36f61423eeb3e616d764edd458663817800e2f3db3adfae687bd17f6c2764
  - id: LTP_D296A517F138A0C0
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:d296a517f138a0c09a3c71729b93607cfff1709b21125573bc2ad30b48302584
  - id: LTP_DE6F80C5EFE44A9D
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:de6f80c5efe44a9d734af297a70d5597f890b2b038ec752e159caefc2425e0fc
  - id: LTP_EE8E695CF61D6D8A
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:ee8e695cf61d6d8aa981eb6e30bf3a8a53c8e8a4ad435ff362bbd78971d17088
  evidence_count: 14
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: dup3
  source_fingerprint: sha256:c4bf8028e446a97268ec49a7845dfb33d372b918a9035a2dcb791e3834ae97da
  recognition_fingerprint: sha256:91e09da2dc19aecb00c274b78fd2bb36f24dd634e00c42d43545f12d892b3862
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_098AFE0E8E10B0EF
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:098afe0e8e10b0efa6872ee3d2ece3674b519943b59189a2758d8ab31b06ab26
  - id: LTP_1726C16756E9651C
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:1726c16756e9651c8be282bf1cdf5c30a283e32aa200934084e3c42a2aee9ff9
  - id: LTP_37C625BD7D7C5F1D
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:37c625bd7d7c5f1db42b7cacc49b4964844f0c2f977ad1a74c3960da0d662932
  - id: LTP_3A7B17AF231D4158
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:3a7b17af231d4158b2c4508e92a25435b89a569164e6dfdabc216b48e1afec9f
  - id: LTP_9B3646398697EA64
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:9b3646398697ea6481b4201006e677123cd226bb81910f45b6fa558aaa810832
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: epoll
  source_fingerprint: sha256:347af9b53085360fbe11b686a7e43c7264b4fd1bc5563b2a82e2c18d3c62d837
  recognition_fingerprint: sha256:7f8022dc186ed2f36644d6d8cf76f98dc2085aac046c4f983fb50987698d9b2f
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: epoll_create
  source_fingerprint: sha256:2ea9590211c36ef191ee7a9cc1309be4c5e71b1cabf8689866e7a86b7c519faa
  recognition_fingerprint: sha256:162dfb9e5d82db72e918fb56b3bde63ee296d050654cd2ea536795561a5e48cb
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_2D1E25BD679B3494
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:2d1e25bd679b349425ebcfa9dd820bb8bc4de40949cd671adc32204c68864bbc
  - id: LTP_37F2ED2BA3175CC3
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:37f2ed2ba3175cc394b1338888db3f207e809f7e36f789587873dc7921e85edd
  - id: LTP_E7435E0CBCA319E1
    generated_at_utc: '2026-07-15T05:26:39.098440Z'
    content_hash: sha256:e7435e0cbca319e18c1459e2f9187003681d326f400fc6d00b47df912010faef
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
```
</details>
