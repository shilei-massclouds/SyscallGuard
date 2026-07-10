# LTP And Test Input Snapshot

This directory stores the source inputs available to SyscallGuard batch work.
The first snapshot was captured from the local `tgoskits` checkout because no
separate LTP repository or `new_specs/` directory was present in the workspace.

The snapshot includes:

- Starry system test sources relevant to the baseline regression batch.
- Starry implementation files used as evidence for manual audit.
- A hand-normalized behavior summary for the baseline items.
- A source index that records unavailable expected materials.

If upstream LTP materials or four-layer syscall specs become available, add
them here as copied snapshots and update `source-index.yaml`.

