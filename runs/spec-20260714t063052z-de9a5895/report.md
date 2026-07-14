---
schema_version: 1
kind: syscallguard_ingest_report
report_id: spec-20260714t063052z-de9a5895
generated_at_utc: '2026-07-14T06:30:53.205277Z'
source:
  id: ltp-local
  type: ltp
  revision: 534222c4f3908e9642f913399e37a66fdd266bbe
  descriptor_hash: sha256:4315924cd8b9aab9608c225950c81f18ab74f25d63d74ee6ac3c444132131b4d
  recognition_rules_hash: sha256:0484079b460c624205ac589891dd570b4f52980944c1379860903092c2a974f6
  resolution: default_source
count:
  value: '1'
  source: command
pending_count: 353
selected_syscalls:
- abort
syscalls:
- syscall: abort
  source_fingerprint: sha256:bcfbc8209ef30cdaf386eab7a3c95e88d9380d72c1d8113fd57fd4a140c68ee3
  recognition_fingerprint: sha256:4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
  selection_reason: new
  result: no_rules
  rules: []
  evidence_count: 0
  unresolved_evidence_count: 0
  reason: no_evidence
---

# Syscall rule ingestion

Report: `spec-20260714t063052z-de9a5895`
Source: `ltp-local` (`534222c4f3908e9642f913399e37a66fdd266bbe`)
Count: `1` from `command`
Pending before selection: 353

| Syscall | Result | Evidence | Unresolved | Rules | Reason |
| --- | --- | ---: | ---: | --- | --- |
| `abort` | `no_rules` | 0 | 0 | - | `no_evidence` |
