# SyscallGuard

SyscallGuard is a standalone Starry syscall compliance harness. The first
version is process-first: it stores specs, evidence, review gates, batch
artifacts, and final coverage conclusions. It does not modify LTP or Starry
repositories and does not run an automated checker yet.

## Repository Layout

- `docs/`: project goals, collaboration model, batch process, and review gates.
- `constraints/`: process, spec, Starry-fix, and dynamic-test constraints.
- `schemas/`: YAML structure descriptions for manifests, step status, reviews,
  and coverage matrices.
- `snapshots/ltp/`: copied inputs used by batches, plus a source index and
  snapshot gaps.
- `batches/000-regression-baseline/`: first demonstration batch for repaired
  regression items.
- `templates/`: reusable batch, step, review, gap, and validation templates.

## Operating Model

Each batch follows the fixed ten-step workflow in
`docs/batch-process.md`. Every step produces a step report and a review
sign-off file. A batch may be marked ready only after all required evidence is
traceable to snapshots and all review records are resolved by a human reviewer.

The current baseline batch is intentionally conservative. It records known
repaired regressions and maps them back to Starry evidence and available local
test sources. It is a harness dry run, not a claim that new Starry gaps were
found.

