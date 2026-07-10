# SyscallGuard Overview

SyscallGuard exists to make syscall compliance work auditable. It keeps the
chain from behavior source to normalized spec, checkability classification,
Starry evidence, validation result, human review, and archived coverage.

## Goals

- Preserve syscall behavior inputs as stable snapshots.
- Normalize behavior into reviewable batch-scoped specs.
- Classify every behavior as static, partial static, dynamic, unsupported, or
  needs review.
- Record Starry evidence without changing Starry from this harness.
- Gate every step with a human review record.
- Produce a coverage matrix that can be traced back to specs and evidence.

## Non-Goals For Version 1

- No CLI or automated scheduler.
- No direct modification of LTP or Starry repositories.
- No migration of extractor or checker scripts.
- No automatic judgement without human sign-off.

## Artifact Lifecycle

1. Snapshot source materials under `snapshots/`.
2. Create a batch manifest under `batches/<id>/manifest.yaml`.
3. Produce one step report and one review sign-off per workflow step.
4. Populate the coverage matrix from normalized specs and evidence records.
5. Close the batch only when all review gates are resolved.

