# Syscall 合规性规则提取报告

## 结论

本次分析了 epoll_create1、epoll_ctl、epoll_pwait、epoll_wait、eventfd、eventfd2、execl、execle、execlp、execv、execve、execveat、execvp、exit、exit_group、faccessat、faccessat2、fadvise、fallocate、fanotify，发现 48 条可执行的合规性规则。

## `epoll_create1`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_5D8D2B3BEDA79604`](../../library/rules/ltp-5d8d2b3beda79604.yaml) | 无额外前置条件 | 调用 epoll_create1(EPOLL_CLOEXEC + 1) | 返回 -1，errno 为 EINVAL |
| [`LTP_89745BB32E6D4D02`](../../library/rules/ltp-89745bb32e6d4d02.yaml) | 文件描述符无效 | 调用 epoll_create1(-1) | 返回 -1，errno 为 EINVAL |
## `epoll_ctl`

共形成 13 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_22E98D1569DAB493`](../../library/rules/ltp-22e98d1569dab493.yaml) | 文件描述符无效 | 调用 epoll_ctl(epfd, -1, fd[1], &events[1]) | 返回 -1，errno 为 EINVAL |
| [`LTP_35CB47575F7752A4`](../../library/rules/ltp-35cb47575f7752a4.yaml) | BAD_USER_ADDRESS | 调用 epoll_ctl(epfd, EPOLL_CTL_ADD, fd[1], NULL) | 返回 -1，errno 为 EFAULT |
| [`LTP_468FC84DEAB0BCB8`](../../library/rules/ltp-468fc84deab0bcb8.yaml) | NONEXISTENT_PATH | 调用 epoll_ctl(epfd, EPOLL_CTL_MOD, fd[1], &events[1]) | 返回 -1，errno 为 ENOENT |
| [`LTP_4953FAD330ADE150`](../../library/rules/ltp-4953fad330ade150.yaml) | 无额外前置条件 | 调用 epoll_ctl(epfd, EPOLL_CTL_ADD, inv, &events[1]) | 返回 -1，errno 为 EBADF |
| [`LTP_5883CD050463E9E8`](../../library/rules/ltp-5883cd050463e9e8.yaml) | 无额外前置条件 | 调用 epoll_ctl(epfd, opt, fd, epvs) | {'kind': 'return_value', 'return': '-1'} |
| [`LTP_5BC52683943E907D`](../../library/rules/ltp-5bc52683943e907d.yaml) | 无额外前置条件 | 调用 epoll_ctl(new_epfd, EPOLL_CTL_ADD, epfd, &events) | 返回 -1，errno 为 exp_errnos |
| [`LTP_61778C450B602081`](../../library/rules/ltp-61778c450b602081.yaml) | OBJECT_ALREADY_EXISTS | 调用 epoll_ctl(epfd, EPOLL_CTL_ADD, fd[0], &events[0]) | 返回 -1，errno 为 EEXIST |
| [`LTP_66C670178B06E9F3`](../../library/rules/ltp-66c670178b06e9f3.yaml) | SYMLINK_LOOP | 调用 epoll_ctl(origin_epfd, EPOLL_CTL_ADD, epfd, &events) | 返回 -1，errno 为 ELOOP |
| [`LTP_6FFB17DB762F3167`](../../library/rules/ltp-6ffb17db762f3167.yaml) | 无额外前置条件 | 调用 epoll_ctl(inv, EPOLL_CTL_ADD, fd[1], &events[1]) | 返回 -1，errno 为 EBADF |
| [`LTP_83709E56D6285F71`](../../library/rules/ltp-83709e56d6285f71.yaml) | 无额外前置条件 | 调用 epoll_ctl(epfd, EPOLL_CTL_ADD, epfd, &events[1]) | 返回 -1，errno 为 EINVAL |
| [`LTP_8ADB82F00C61D567`](../../library/rules/ltp-8adb82f00c61d567.yaml) | NONEXISTENT_PATH | 调用 epoll_ctl(epfd, EPOLL_CTL_DEL, fd[1], &events[1]) | 返回 -1，errno 为 ENOENT |
| [`LTP_ADEB5FE2DF97542A`](../../library/rules/ltp-adeb5fe2df97542a.yaml) | 无额外前置条件 | 调用 epoll_ctl(epfd, EPOLL_CTL_MOD, fds[0], &events) | 调用成功，返回 SUCCESS |
| [`LTP_CBB1680336D53D2A`](../../library/rules/ltp-cbb1680336d53d2a.yaml) | 无额外前置条件 | 调用 epoll_ctl(epfd, EPOLL_CTL_ADD, unsupported_fd, &events[1]) | 返回 -1，errno 为 EPERM |
## `epoll_pwait`

没有形成可发布的合规性规则。

## `epoll_wait`

共形成 13 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_03702BF4223F6AA5`](../../library/rules/ltp-03702bf4223f6aa5.yaml) | 无额外前置条件 | 调用 epoll_wait(epfd, &evt_receive, 10, 0) | {'kind': 'return_value', 'return': '1'} |
| [`LTP_18ECD15E5451228D`](../../library/rules/ltp-18ecd15e5451228d.yaml) | 文件描述符无效 | 调用 epoll_wait(epfd, ev_rdwr, 0, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_1ADEBF230DD2C214`](../../library/rules/ltp-1adebf230dd2c214.yaml) | 文件描述符无效 | 调用 epoll_wait(epfd, ev_rdwr, -1, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_79FCE1367A3A0369`](../../library/rules/ltp-79fce1367a3a0369.yaml) | 无额外前置条件 | 调用 epoll_wait(epfd, &evt_receive, 1, 0) | {'kind': 'return_value', 'return': '1'} |
| [`LTP_7DC583D73FC4A726`](../../library/rules/ltp-7dc583d73fc4a726.yaml) | 无额外前置条件 | 调用 epoll_wait(epfd, &evt_receive, 10, 0) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_8F30861E18D66625`](../../library/rules/ltp-8f30861e18d66625.yaml) | 文件描述符无效 | 调用 epoll_wait(inv_epfd, ev_rdwr, 1, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_ACD12B8C0803E654`](../../library/rules/ltp-acd12b8c0803e654.yaml) | 文件描述符无效 | 调用 epoll_wait(epfd, &ret_evs, 1, -1) | {'kind': 'return_value', 'return': '1'} |
| [`LTP_B3F848BCBCBAB559`](../../library/rules/ltp-b3f848bcbcbab559.yaml) | 无额外前置条件 | 调用 epoll_wait(epfd, epevs, 1, 0) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_D12172005842E2A5`](../../library/rules/ltp-d12172005842e2a5.yaml) | 无额外前置条件 | 调用 epoll_wait(epfd, &evt_receive, 1, 0) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_D75F86A534CB6E02`](../../library/rules/ltp-d75f86a534cb6e02.yaml) | 无额外前置条件 | 调用 epoll_wait(epfd, epevs, 1, sleep_ms) | {'kind': 'return_value', 'return': '0'} |
| [`LTP_E8CF2AE0EC60602C`](../../library/rules/ltp-e8cf2ae0ec60602c.yaml) | 文件描述符无效 | 调用 epoll_wait(epfd, ret_evs, 2, -1) | {'kind': 'return_value', 'return': 'events_matched'} |
| [`LTP_EA5D1572B890F71E`](../../library/rules/ltp-ea5d1572b890f71e.yaml) | 文件描述符无效、BAD_USER_ADDRESS | 调用 epoll_wait(epfd, ev_rdonly, 1, -1) | 返回 -1，errno 为 EFAULT |
| [`LTP_EC1CA29BE6888A6B`](../../library/rules/ltp-ec1ca29be6888a6b.yaml) | 文件描述符无效 | 调用 epoll_wait(bad_epfd, ev_rdwr, 1, -1) | 返回 -1，errno 为 EBADF |
## `eventfd`

共形成 2 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_1AA7F21DA5C55800`](../../library/rules/ltp-1aa7f21da5c55800.yaml) | 无额外前置条件 | 调用 eventfd(0, EFD_NONBLOCK) | {'kind': 'return_fd', 'return': 'FD'} |
| [`LTP_5622491E8A2227F2`](../../library/rules/ltp-5622491e8a2227f2.yaml) | 无额外前置条件 | 调用 eventfd(EVENT_COUNT, EFD_NONBLOCK) | {'kind': 'return_fd', 'return': 'FD'} |
## `eventfd2`

没有形成可发布的合规性规则。

## `execl`

没有形成可发布的合规性规则。

## `execle`

没有形成可发布的合规性规则。

## `execlp`

没有形成可发布的合规性规则。

## `execv`

没有形成可发布的合规性规则。

## `execve`

没有形成可发布的合规性规则。

## `execveat`

共形成 4 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_0FEC274199CCD0A0`](../../library/rules/ltp-0fec274199ccd0a0.yaml) | 文件描述符无效 | 调用 execveat(fd, app_abs_path, argv, environ, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_725BDB092C6D8F74`](../../library/rules/ltp-725bdb092c6d8f74.yaml) | NON_DIRECTORY_PATH_COMPONENT | 调用 execveat(fd, TEST_REL_APP, argv, environ, 0) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_76F002F46086B46C`](../../library/rules/ltp-76f002f46086b46c.yaml) | SYMLINK_LOOP | 调用 execveat(fd, app_sym_path, argv, environ, AT_SYMLINK_NOFOLLOW) | 返回 -1，errno 为 ELOOP |
| [`LTP_ACF7A30AF3B10973`](../../library/rules/ltp-acf7a30af3b10973.yaml) | 无额外前置条件 | 调用 execveat(bad_fd, "", argv, environ, AT_EMPTY_PATH) | 返回 -1，errno 为 EBADF |
## `execvp`

没有形成可发布的合规性规则。

## `exit`

没有形成可发布的合规性规则。

## `exit_group`

共形成 1 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_33D137B9002503E5`](../../library/rules/ltp-33d137b9002503e5.yaml) | 无额外前置条件 | 调用 exit_group(4) | {'kind': 'return_value', 'return': '-1'} |
## `faccessat`

没有形成可发布的合规性规则。

## `faccessat2`

共形成 13 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_025CF701276457CB`](../../library/rules/ltp-025cf701276457cb.yaml) | 无额外前置条件 | 调用 faccessat2(atcwd_fd, sym_path, R_OK, AT_SYMLINK_NOFOLLOW) | 调用成功，返回 SUCCESS |
| [`LTP_437CFCD991A666C9`](../../library/rules/ltp-437cfcd991a666c9.yaml) | 无额外前置条件 | 调用 faccessat2(atcwd_fd, rel_path, R_OK, 0) | 调用成功，返回 SUCCESS |
| [`LTP_4BCFF61005DC2E9A`](../../library/rules/ltp-4bcff61005dc2e9a.yaml) | 文件描述符无效 | 调用 faccessat2(atcwd_fd, rel_path, -1, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_4C1F446C9C520B36`](../../library/rules/ltp-4c1f446c9c520b36.yaml) | 无额外前置条件 | 调用 faccessat2(bad_fd, rel_path, R_OK, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_4D51F55F25C6F2A3`](../../library/rules/ltp-4d51f55f25c6f2a3.yaml) | BAD_USER_ADDRESS | 调用 faccessat2(atcwd_fd, bad_path, R_OK, 0) | 返回 -1，errno 为 EFAULT |
| [`LTP_5109EDF645F51D7E`](../../library/rules/ltp-5109edf645f51d7e.yaml) | 无额外前置条件 | 调用 faccessat2(bad_fd, abs_path, R_OK, 0) | 调用成功，返回 SUCCESS |
| [`LTP_6885CE6A54F7716E`](../../library/rules/ltp-6885ce6a54f7716e.yaml) | 文件描述符无效 | 调用 faccessat2(atcwd_fd, rel_path, R_OK, -1) | 返回 -1，errno 为 EINVAL |
| [`LTP_77AA3EAF2AD0C07A`](../../library/rules/ltp-77aa3eaf2ad0c07a.yaml) | NON_DIRECTORY_PATH_COMPONENT | 调用 faccessat2(fd, rel_path, R_OK, 0) | 返回 -1，errno 为 ENOTDIR |
| [`LTP_C2909AC2ECEDED94`](../../library/rules/ltp-c2909ac2eceded94.yaml) | 无额外前置条件 | 调用 faccessat2(dir_fd, testfile, R_OK, 0) | 调用成功，返回 SUCCESS |
| [`LTP_C7D18796DD651AE8`](../../library/rules/ltp-c7d18796dd651ae8.yaml) | PERMISSION_DENIED_STATE | 调用 faccessat2(atcwd_fd, rel_path, R_OK, AT_EACCESS) | 返回 -1，errno 为 EACCES |
| [`LTP_D77858597BCC1C13`](../../library/rules/ltp-d77858597bcc1c13.yaml) | 无额外前置条件 | 调用 faccessat2(atcwd_fd, rel_path, R_OK, AT_EACCESS) | 调用成功，返回 SUCCESS |
| [`LTP_EEDED564522D8D2D`](../../library/rules/ltp-eeded564522d8d2d.yaml) | 无额外前置条件 | 调用 faccessat2(bad_fd, abs_path, R_OK, AT_EACCESS) | 调用成功，返回 SUCCESS |
| [`LTP_F7B8EDE302D5D08A`](../../library/rules/ltp-f7b8ede302d5d08a.yaml) | 无额外前置条件 | 调用 faccessat2(dir_fd, testfile, R_OK, AT_EACCESS) | 调用成功，返回 SUCCESS |
## `fadvise`

没有形成可发布的合规性规则。

## `fallocate`

没有形成可发布的合规性规则。

## `fanotify`

没有形成可发布的合规性规则。


## 技术参考

- 报告 ID：`spec-20260715t101411z-599ee896`
- 来源：`ltp-local`，内容快照 `sha256:d789747f0c0bf1697f538bc5166073fd8449dec3beac7b12ac0be0b1b716dcb4`
- 全局待处理 syscall：333
- 提取数量：`20`（来源：`global_default`）
- `epoll_create1`：证据 3 条，未解析 0 条
- `epoll_ctl`：证据 10 条，未解析 0 条
- `epoll_pwait`：证据 7 条，未解析 1 条
- `epoll_wait`：证据 19 条，未解析 0 条
- `eventfd`：证据 12 条，未解析 0 条
- `eventfd2`：证据 7 条，未解析 0 条
- `execl`：证据 0 条，未解析 0 条
- `execle`：证据 0 条，未解析 0 条
- `execlp`：证据 0 条，未解析 0 条
- `execv`：证据 0 条，未解析 0 条
- `execve`：证据 8 条，未解析 1 条
- `execveat`：证据 1 条，未解析 0 条
- `execvp`：证据 0 条，未解析 0 条
- `exit`：证据 0 条，未解析 0 条
- `exit_group`：证据 3 条，未解析 0 条
- `faccessat`：证据 5 条，未解析 1 条
- `faccessat2`：证据 4 条，未解析 0 条
- `fadvise`：证据 4 条，未解析 0 条
- `fallocate`：证据 12 条，未解析 1 条
- `fanotify`：证据 27 条，未解析 2 条

<details>
<summary>机器可读元数据</summary>

<!-- syscallguard-metadata -->
```yaml
schema_version: 1
kind: syscallguard_ingest_report
report_id: spec-20260715t101411z-599ee896
generated_at_utc: '2026-07-15T10:14:12.969080Z'
source:
  id: ltp-local
  type: ltp
  snapshot_hash: sha256:d789747f0c0bf1697f538bc5166073fd8449dec3beac7b12ac0be0b1b716dcb4
  descriptor_hash: sha256:4315924cd8b9aab9608c225950c81f18ab74f25d63d74ee6ac3c444132131b4d
  recognition_rules_hash: sha256:84d715591e7abe5f2ac2de68c75172b2b2389541f6f8b8f23582b8cff81b057e
  resolution: default_source
count:
  value: '20'
  source: global_default
pending_count: 333
selected_syscalls:
- epoll_create1
- epoll_ctl
- epoll_pwait
- epoll_wait
- eventfd
- eventfd2
- execl
- execle
- execlp
- execv
- execve
- execveat
- execvp
- exit
- exit_group
- faccessat
- faccessat2
- fadvise
- fallocate
- fanotify
syscalls:
- syscall: epoll_create1
  source_fingerprint: sha256:adca31441041b76146329e13f3341f54806994f6886cc309be85ea3759259134
  recognition_fingerprint: sha256:7f3c0047b4141c775a6e68dba5842c5c9ba77296d43d414b287f5d4b511dc0c7
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_5D8D2B3BEDA79604
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:5d8d2b3beda79604301b79695ead77bb1cca6ec4c1e6b679aabacb702befdccf
  - id: LTP_89745BB32E6D4D02
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:89745bb32e6d4d02b6ab504c2a88f1b47d35f128eb07bb1921b1c2adb76977d0
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: epoll_ctl
  source_fingerprint: sha256:15462445432b857f20d64c8de3ac72e00224536e107de176479eb54fd86cd0b6
  recognition_fingerprint: sha256:22f995349adf1e8f337092cf086e9b00fe8c004cace8340b1e36f3cceb24a358
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_22E98D1569DAB493
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:22e98d1569dab4931d447f9ee3157b478dbeb887d9c466a1041be801be711343
  - id: LTP_35CB47575F7752A4
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:35cb47575f7752a4b4814c5629309fc02f2a6405e2e075ca1945c287a38d1c81
  - id: LTP_468FC84DEAB0BCB8
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:468fc84deab0bcb8749bee2c8342c88aa3345e7f8d1ff568958918217fc129de
  - id: LTP_4953FAD330ADE150
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:4953fad330ade1503bf7a6d4d6bf2c353a337844f58042ceb3214149d1025945
  - id: LTP_5883CD050463E9E8
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:5883cd050463e9e8d7a616eded312d138c7a9d06ee39d3947a818a32e9738f36
  - id: LTP_5BC52683943E907D
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:5bc52683943e907d8c1ee104d1a6f46436beca5f3b6ebd776c52407f65940b5c
  - id: LTP_61778C450B602081
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:61778c450b60208142d63a0628d3f3a112b7bbdafa09587ce6e84c7618f736c5
  - id: LTP_66C670178B06E9F3
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:66c670178b06e9f3eae76490edd09b4a26bb0e1c2ccba3c4cbc2a625d12c39bb
  - id: LTP_6FFB17DB762F3167
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:6ffb17db762f3167790a052bae0fa49f44b1075991c29dcec06f56509e9ae743
  - id: LTP_83709E56D6285F71
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:83709e56d6285f71dce5dcd5f54aa0ba99d44ddef002f1e6cc53f2fce6075678
  - id: LTP_8ADB82F00C61D567
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:8adb82f00c61d5671840571f67ba2e6ea75175e1b94b6fbe88f37d95f8031e40
  - id: LTP_ADEB5FE2DF97542A
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:adeb5fe2df97542a0ab4a690668fb6ff8bf5dabf6dc571b9f1ad50e9a6cd3c7e
  - id: LTP_CBB1680336D53D2A
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:cbb1680336d53d2a1eeae3e329d0c4d0144ad9da05ca737d1a9573a537224a39
  evidence_count: 10
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: epoll_pwait
  source_fingerprint: sha256:472ff71fd83fe184338308aea8448cbe0618ac38bbce8f89a98f2f4570a81f25
  recognition_fingerprint: sha256:3cde5407a1982fa83f10c8702bb584e3a72bc21b1b7cbfef7626a837a860e7ff
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 7
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: epoll_wait
  source_fingerprint: sha256:a1c8ea8bd0f5c8d6b3ad19754840fed93f92118f11b73947ce40f9821dd7b0b3
  recognition_fingerprint: sha256:c29fe820925c0724b5a0f51783f4f0cfcbe0c1970079aa04f28499eefbc24261
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_03702BF4223F6AA5
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:03702bf4223f6aa5d1fb270e6dad20acf5dc0634501ea7f552ee0d38cf2143a0
  - id: LTP_18ECD15E5451228D
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:18ecd15e5451228d55bbb4e06d2aeec746b9af6c9aca8fedd0b387d8e3484b50
  - id: LTP_1ADEBF230DD2C214
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:1adebf230dd2c214f844468f75ee44f3ee8a8cec961a0ba26caa9afe58bd6d25
  - id: LTP_79FCE1367A3A0369
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:79fce1367a3a0369e9893dd52e26564ee3a4b33a48e921740b3e6a1fc36cf892
  - id: LTP_7DC583D73FC4A726
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:7dc583d73fc4a7267709ff0452c11b7a2fc91965670254ab0cce04b64223d1aa
  - id: LTP_8F30861E18D66625
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:8f30861e18d666256af3aaaa7bd2a46e35d4fa8cb90ab3960bb318a6b7f25a51
  - id: LTP_ACD12B8C0803E654
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:acd12b8c0803e654854f1267c8e89786da595fa9788ba431fda06dfd0cbcd5d2
  - id: LTP_B3F848BCBCBAB559
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:b3f848bcbcbab5597d6e4e2abe10464ca363e060e65589801a91a6bac9a7af58
  - id: LTP_D12172005842E2A5
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:d12172005842e2a5c84eabfd9e2ee4a02a5cd9f56457607850d08658f9c7b8a4
  - id: LTP_D75F86A534CB6E02
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:d75f86a534cb6e02dbd3de6fb64ef149396db4e63651815433cdec7ec6f9ce05
  - id: LTP_E8CF2AE0EC60602C
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:e8cf2ae0ec60602cb9843ed946dd3d5351d21e77104f6ac7918b33e760694a8d
  - id: LTP_EA5D1572B890F71E
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:ea5d1572b890f71ea1a55cdcad2c53e9061edc3234a5c30ab4af4952cba049ad
  - id: LTP_EC1CA29BE6888A6B
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:ec1ca29be6888a6b373d18e61642398247eb0d3006feee8826fd7fda26f99ab4
  evidence_count: 19
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: eventfd
  source_fingerprint: sha256:d2030c0ffbbb1228179acd84082f1a18d48af2a3eaab0724704d4f0f0bb693df
  recognition_fingerprint: sha256:d8e22d9ae215a1d4977e54bfc41e404a15869ec93e99df47f08bf2fea5412136
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_1AA7F21DA5C55800
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:1aa7f21da5c558007d9fd7b2943285112b799046994663336b5a0137eb08fc30
  - id: LTP_5622491E8A2227F2
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:5622491e8a2227f2b5f90dbefb8a45560139a3cfbea5be104cbfca5fe10c4e09
  evidence_count: 12
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: eventfd2
  source_fingerprint: sha256:b8278fa23da737be991e2c2088bc95163bb9b6725ce760c56357be4e14f5914a
  recognition_fingerprint: sha256:5e19fa8c028a853237fd339c521cb7f3e58686f384ea889e17d4b57ef8cff288
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 7
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: execl
  source_fingerprint: sha256:a2d3304c4459595d637129f41ad14465223c7f76359c500c29907ee00dc3d872
  recognition_fingerprint: sha256:229446127691798f40521ca2d166873755708769d43b3b5d45a4fe09659145b1
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: execle
  source_fingerprint: sha256:a5fe713402ac6e15d3083828b3e241b1187db906c8646ac45890c5300a4bb4d4
  recognition_fingerprint: sha256:32da35ea1a88efe570d0e6ab80afb9e0ac41419d062959ac7fe14c67ab8da78d
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: execlp
  source_fingerprint: sha256:f62593d8fcb54a93b671583bd6c320c5d3b006e3b3f9a30e912533fcab5618aa
  recognition_fingerprint: sha256:c47e3467d1efa1eb6157676018395730242013d8ca504b1f3cc9ee3f68c30947
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: execv
  source_fingerprint: sha256:1084eda95b8d01131e2b61e53b04fccccf687689139d941b1c27923679ad77d4
  recognition_fingerprint: sha256:a9df9286170b58ac5a83d055f0d0b620e05c64ad693374ff80a2dede19402718
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: execve
  source_fingerprint: sha256:b2330d9faaf12c8cc5e333cf16b1c4da6f9e5c7aebd4c9a2ab4e913e768e0794
  recognition_fingerprint: sha256:6c4c5a47e58da4128900a85da0ad70f0d29496301bb7514ed17669e8b51d04cc
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 8
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: execveat
  source_fingerprint: sha256:1c0517838680a2f98ef901b32e927617915fe5df0b66079e2d02d3694a133880
  recognition_fingerprint: sha256:5c12dd5406a86ac0f8bb9acbb3204d5a7a9636a2b67ca7a03462475b47fca4aa
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_0FEC274199CCD0A0
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:0fec274199ccd0a04984fadd1588ef353a2bcb0400a8e713f1adaa3f3a36c208
  - id: LTP_725BDB092C6D8F74
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:725bdb092c6d8f746ce7afd0c94d6ba70ce5b4695bc692d4d324614f8a697591
  - id: LTP_76F002F46086B46C
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:76f002f46086b46c88bb0abaeda57dc5389da3ecbcf8ede0f2c978824eae391a
  - id: LTP_ACF7A30AF3B10973
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:acf7a30af3b10973088f22334a5e2b35a00bbc3ff6530b1fb644856f637f06e4
  evidence_count: 1
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: execvp
  source_fingerprint: sha256:41e1227e84255d16acdf361caaea4832da0ec125cd81b6beefeff3c45d631647
  recognition_fingerprint: sha256:efab94a55c075ab8c5442fecd6a90d8843b750c52a64c33933fb425e8d9c4aa7
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: exit
  source_fingerprint: sha256:ae380540dffbdd23fde843efc604b5ea685c8b930d59a34157a7bbd1d320f948
  recognition_fingerprint: sha256:b65987246105b6d50d0b7858ed53e741fe23737d0c006352405cdcdd838549fc
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
- syscall: exit_group
  source_fingerprint: sha256:ea36f07d63fc4d5ee6abbbf46e2880d653b96fe07c1b467e4c725c9ea18ed16a
  recognition_fingerprint: sha256:5b629486c36bbad51071112399befebd1eaa3393cadbcc301135627d46c60ac4
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_33D137B9002503E5
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:33d137b9002503e527752b0d755df2a42b8ee4a5560a746646216385fa7bf49d
  evidence_count: 3
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: faccessat
  source_fingerprint: sha256:15e2e0228de9f01217d7f29e60169a88185ae01a2f1233b7c1b71c24ba7495e0
  recognition_fingerprint: sha256:900b081489a6abe779474148595c1b1db6d735caaacb3f9dd96070adcc074923
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 5
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: faccessat2
  source_fingerprint: sha256:5dc5e64d7ca321293b91ddbb0b8dc58ae523b9757bfdb97d868e8d42cf169c03
  recognition_fingerprint: sha256:d952af8b2ea9f1588813df3612fc76f663a93dcaff42524fb7d8523ab90e5e92
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_025CF701276457CB
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:025cf701276457cb8418eabce2995b043ccbd239d602beb3b3dcb5addb042fb6
  - id: LTP_437CFCD991A666C9
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:437cfcd991a666c9360e9024835d7e6a8c5727cae5e72567f944a93ce03239b0
  - id: LTP_4BCFF61005DC2E9A
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:4bcff61005dc2e9a8baad1357435ae47571fe775bbdbee71ceb80f709a098f9e
  - id: LTP_4C1F446C9C520B36
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:4c1f446c9c520b36b7f3b5a39c42fea74e7befa2adf95e4a919a1bb760184320
  - id: LTP_4D51F55F25C6F2A3
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:4d51f55f25c6f2a3a51ed2c2be2b507816d6ae2d9ba1dd1adcc28340924b1a89
  - id: LTP_5109EDF645F51D7E
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:5109edf645f51d7ec6698c72239e0feedbcea9ffb1e4f9150d5e066527c66630
  - id: LTP_6885CE6A54F7716E
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:6885ce6a54f7716e5b79cac1af65007cb4f63aad6398b472d5a7539824bf4de9
  - id: LTP_77AA3EAF2AD0C07A
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:77aa3eaf2ad0c07a8c890e541d76ea25203c93ad6fbacc025943afc55a92bc17
  - id: LTP_C2909AC2ECEDED94
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:c2909ac2eceded9462052049abaac7e397b9366e68188495ac945f457e9c9ae1
  - id: LTP_C7D18796DD651AE8
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:c7d18796dd651ae8914c31a80f64213c1c7e2f240a44865e94191854e058f93f
  - id: LTP_D77858597BCC1C13
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:d77858597bcc1c13039ec0dd178b90fb23905df40451046331495fe91dc2faf1
  - id: LTP_EEDED564522D8D2D
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:eeded564522d8d2df106307960b9b399555f31b2f4945dc5e10cff79a9fa1454
  - id: LTP_F7B8EDE302D5D08A
    generated_at_utc: '2026-07-15T10:14:12.969080Z'
    content_hash: sha256:f7b8ede302d5d08a04e637eea3a051fcb4238d4367e86ea376079213b833dfeb
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
- syscall: fadvise
  source_fingerprint: sha256:8db88f14dacac570aba10be646c9ebb89e4cba75bbfe114cc3a5608f3d66030c
  recognition_fingerprint: sha256:40eea4b9041052dc3fd14dae16b15891e56de7605b327c33d4176b8347313b57
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 4
  unresolved_evidence_count: 0
  reason: zero_rules
- syscall: fallocate
  source_fingerprint: sha256:0cff563cf65acccc9e28b6f54bf93e258e282eca099fc61b918d27998af1ac03
  recognition_fingerprint: sha256:1743cf21ad25747f9c04c1deda99749f16665621fa179d549d26e54af373e72a
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 12
  unresolved_evidence_count: 1
  reason: unresolved_evidence
- syscall: fanotify
  source_fingerprint: sha256:d6021924fd83f220c44821189fcd67e5810f3a707809a0eb24976729f5292c30
  recognition_fingerprint: sha256:9cb465441c56af5b2d91d535aec8ec7b9f3952192f101885633242c53cc5259b
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 27
  unresolved_evidence_count: 2
  reason: unresolved_evidence
```
</details>
