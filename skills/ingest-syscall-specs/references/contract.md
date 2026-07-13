# Ingestion Contract

Use a source descriptor with these fields:

```yaml
source_id: ltp-upstream
adapter: ltp-extractor
location: /path/to/ltp
revision: HEAD
parameters:
  tool: tools/syscall_spec_extract.py
  syscalls: [read, write, openat]
```

`parameters.syscalls` defines stable order. When absent, use sorted directories below
`testcases/kernel/syscalls`. Include adapter version, SyscallGuard version, resolved source commit,
extractor content, adapter parameters, and syscall-related source content in each fingerprint.

Write current entities to `library/specs/<syscall>.yaml` and `library/rules/<rule-id>.yaml`; update
both `index.yaml` files. Keep execution snapshots in `runs/<run-id>/`. Downstream consumers select
entity IDs from the run but hash and read the current shared files.
