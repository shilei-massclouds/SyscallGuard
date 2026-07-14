# Syscall 合规性规则提取报告

## 结论

本次分析了 mmap，发现 9 条可执行的合规性规则。

## `mmap`

共形成 9 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_36C99C10CD38F8DB`](../../library/rules/ltp-36c99c10cd38f8db.yaml) | PERMISSION_DENIED_STATE | 调用 mmap(NULL, MMAPSIZE, PROT_READ | PROT_WRITE, MAP_FILE | MAP_PRIVATE, fd, 0) | 返回 -1，errno 为 EACCES |
| [`LTP_45439D8F2BAB0832`](../../library/rules/ltp-45439d8f2bab0832.yaml) | PERMISSION_DENIED_STATE | 调用 mmap(NULL, MMAPSIZE, PROT_WRITE, MAP_FILE | MAP_SHARED, fd, 0) | 返回 -1，errno 为 EACCES |
| [`LTP_51E295101A9F4411`](../../library/rules/ltp-51e295101a9f4411.yaml) | 无额外前置条件 | 调用 mmap(NULL, 0, PROT_READ | PROT_WRITE, MAP_FILE | MAP_SHARED, fd, 0) | 返回 -1，errno 为 EINVAL |
| [`LTP_52BAFC01DEA6E172`](../../library/rules/ltp-52bafc01dea6e172.yaml) | PERMISSION_DENIED_STATE | 调用 mmap(NULL, MMAPSIZE, PROT_READ, MAP_FILE | MAP_SHARED, fd, 0) | 返回 -1，errno 为 EACCES |
| [`LTP_791DEA825D66980B`](../../library/rules/ltp-791dea825d66980b.yaml) | 无额外前置条件 | 调用 mmap(NULL, page_sz, PROT_WRITE, MAP_FILE | MAP_SHARED, fd, 0) | 返回 -1，errno 为 EBADF |
| [`LTP_C346EFF1233F7061`](../../library/rules/ltp-c346eff1233f7061.yaml) | PERMISSION_DENIED_STATE | 调用 mmap(NULL, MMAPSIZE, PROT_WRITE, MAP_FILE | MAP_PRIVATE, fd, 0) | 返回 -1，errno 为 EACCES |
| [`LTP_F36F8C0CC1A6D840`](../../library/rules/ltp-f36f8c0cc1a6d840.yaml) | PERMISSION_DENIED_STATE | 调用 mmap(NULL, MMAPSIZE, PROT_READ, MAP_FILE | MAP_PRIVATE, fd, 0) | 返回 -1，errno 为 EACCES |
| [`LTP_FD1B65B0BCC88E0D`](../../library/rules/ltp-fd1b65b0bcc88e0d.yaml) | PERMISSION_DENIED_STATE | 调用 mmap(NULL, MMAPSIZE, PROT_READ | PROT_WRITE, MAP_FILE | MAP_SHARED, fd, 0) | 返回 -1，errno 为 EACCES |
| [`LTP_FEACDC300C3E1DD7`](../../library/rules/ltp-feacdc300c3e1dd7.yaml) | 无额外前置条件 | 调用 mmap(NULL, MMAPSIZE, PROT_READ | PROT_WRITE, MAP_FILE, fd, 0) | 返回 -1，errno 为 EINVAL |

## 技术参考

- 报告 ID：`spec-20260714t133812z-6fd5c7a0`
- 来源：`ltp-local`，revision `534222c4f3908e9642f913399e37a66fdd266bbe`
- 全局待处理 syscall：372
- 指定 syscall：`mmap`
- `mmap`：证据 2 条，未解析 0 条

<details>
<summary>机器可读元数据</summary>

<!-- syscallguard-metadata -->
```yaml
schema_version: 1
kind: syscallguard_ingest_report
report_id: spec-20260714t133812z-6fd5c7a0
generated_at_utc: '2026-07-14T13:38:13.033184Z'
source:
  id: ltp-local
  type: ltp
  revision: 534222c4f3908e9642f913399e37a66fdd266bbe
  descriptor_hash: sha256:4315924cd8b9aab9608c225950c81f18ab74f25d63d74ee6ac3c444132131b4d
  recognition_rules_hash: sha256:0484079b460c624205ac589891dd570b4f52980944c1379860903092c2a974f6
  resolution: default_source
count:
  value: null
  source: explicit_syscalls
pending_count: 372
selected_syscalls:
- mmap
syscalls:
- syscall: mmap
  source_fingerprint: sha256:42415bb3e243bb4071298a44afbfd9c74353212d3d793de7687920a485a52a71
  recognition_fingerprint: sha256:12b06f310f5064dbd63216c7c911f8e34f564a898b39e21847db9e5520dca06b
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_36C99C10CD38F8DB
    generated_at_utc: '2026-07-14T13:38:13.033184Z'
    content_hash: sha256:36c99c10cd38f8db26e721ea351430f0ebc4767b9a31257223ad8fd5519c7d0d
  - id: LTP_45439D8F2BAB0832
    generated_at_utc: '2026-07-14T13:38:13.033184Z'
    content_hash: sha256:45439d8f2bab0832027a39e78d024f72cc6449adff9fb823af60ff7c004d7bc5
  - id: LTP_51E295101A9F4411
    generated_at_utc: '2026-07-14T13:38:13.033184Z'
    content_hash: sha256:51e295101a9f4411b8c43521d430e85bd27ac1d7a96127b66675d7dc024ba9d2
  - id: LTP_52BAFC01DEA6E172
    generated_at_utc: '2026-07-14T13:38:13.033184Z'
    content_hash: sha256:52bafc01dea6e1725e71d23e11424031141e37ea07b99e151db6bcfc16116bde
  - id: LTP_791DEA825D66980B
    generated_at_utc: '2026-07-14T13:38:13.033184Z'
    content_hash: sha256:791dea825d66980bfded73936e4745cf7b914f20652b9489e65a7a59509b897b
  - id: LTP_C346EFF1233F7061
    generated_at_utc: '2026-07-14T13:38:13.033184Z'
    content_hash: sha256:c346eff1233f706172a595326e9215b63dd1f455b13880c762f92532db036e2e
  - id: LTP_F36F8C0CC1A6D840
    generated_at_utc: '2026-07-14T13:38:13.033184Z'
    content_hash: sha256:f36f8c0cc1a6d84025a2394e30fa1d7c273ce9c13d8f58d759383c75dbf8c10a
  - id: LTP_FD1B65B0BCC88E0D
    generated_at_utc: '2026-07-14T13:38:13.033184Z'
    content_hash: sha256:fd1b65b0bcc88e0d283d47737c8b9d244de44d7461e8efd5bc6eb699ebaa0d54
  - id: LTP_FEACDC300C3E1DD7
    generated_at_utc: '2026-07-14T13:38:13.033184Z'
    content_hash: sha256:feacdc300c3e1dd754c7925df645b95995a6f17fd0ebcb6a50578071e2f9636f
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
requested_syscalls:
- mmap
```
</details>
