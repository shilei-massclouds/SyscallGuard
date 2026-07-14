# Syscall 合规性规则提取报告

## 结论

本次分析了 close，发现 3 条可执行的合规性规则。

## `close`

共形成 3 条规则：

| 规则 | 条件 | 检查内容 | 预期结果 |
| --- | --- | --- | --- |
| [`LTP_09B39E9C9254ECB2`](../../library/rules/ltp-09b39e9c9254ecb2.yaml) | 文件描述符已经关闭 | 调用 close(fd_closed) | 返回 -1，errno 为 EBADF |
| [`LTP_0CD17E662AFD2956`](../../library/rules/ltp-0cd17e662afd2956.yaml) | 文件描述符无效 | 调用 close(fd_invalid) | 返回 -1，errno 为 EBADF |
| [`LTP_5CB803B873F78BA0`](../../library/rules/ltp-5cb803b873f78ba0.yaml) | 文件描述符有效且处于打开状态 | 调用 close(tc[i].get_fd()) | 调用成功，返回 SUCCESS |

## 技术参考

- 报告 ID：`spec-20260714t133502z-772aa222`
- 来源：`ltp-local`，内容快照 `sha256:d789747f0c0bf1697f538bc5166073fd8449dec3beac7b12ac0be0b1b716dcb4`
- 全局待处理 syscall：373
- 指定 syscall：`close`
- `close`：证据 2 条，未解析 0 条

<details>
<summary>机器可读元数据</summary>

<!-- syscallguard-metadata -->
```yaml
schema_version: 1
kind: syscallguard_ingest_report
report_id: spec-20260714t133502z-772aa222
generated_at_utc: '2026-07-14T13:35:02.567816Z'
source:
  id: ltp-local
  type: ltp
  snapshot_hash: sha256:d789747f0c0bf1697f538bc5166073fd8449dec3beac7b12ac0be0b1b716dcb4
  descriptor_hash: sha256:4315924cd8b9aab9608c225950c81f18ab74f25d63d74ee6ac3c444132131b4d
  recognition_rules_hash: sha256:0484079b460c624205ac589891dd570b4f52980944c1379860903092c2a974f6
  resolution: default_source
count:
  value: null
  source: explicit_syscalls
pending_count: 373
selected_syscalls:
- close
syscalls:
- syscall: close
  source_fingerprint: sha256:775c18f20fd580008f1dfc93ff3b9ebdad2ea3e9b7445a3d222f7c2adcc57f68
  recognition_fingerprint: sha256:feaed9c17020b231a505a85489fd9dd8b7f0f9b3fa500ef0eb40b7f1336ced7a
  selection_reason: new
  result: formed_rules
  rules:
  - id: LTP_09B39E9C9254ECB2
    generated_at_utc: '2026-07-14T13:35:02.567816Z'
    content_hash: sha256:09b39e9c9254ecb24ccb5288c3f12281e9adc0b698de5c706a4f071599c3ce60
  - id: LTP_0CD17E662AFD2956
    generated_at_utc: '2026-07-14T13:35:02.567816Z'
    content_hash: sha256:0cd17e662afd2956c8c1a42d49b46dca16c37c1972fc6d3632c05c317939a996
  - id: LTP_5CB803B873F78BA0
    generated_at_utc: '2026-07-14T13:35:02.567816Z'
    content_hash: sha256:5cb803b873f78ba0c0cafe0d4ab7a0e69be0d150de939bbf030e0c66f583d1c6
  evidence_count: 2
  unresolved_evidence_count: 0
  reason: all_evidence_resolved
requested_syscalls:
- close
```
</details>
