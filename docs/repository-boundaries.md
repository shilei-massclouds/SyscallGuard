# Repository Boundaries

SyscallGuard is a harness repository. It records process artifacts and review
conclusions. It does not own the test source or the kernel implementation.

## SyscallGuard Owns

- Workflow documentation.
- Constraint files.
- YAML schema descriptions.
- Copied input snapshots.
- Batch manifests, step reports, review records, coverage matrices, and final
  reports.

## LTP Or Test Source Repository Owns

- Original test source.
- Upstream test semantics.
- Test build-system integration.

## tgoskits And Starry Own

- Kernel implementation.
- Starry test integration.
- Build and QEMU execution results.
- Fix commits and pull requests.

## Boundary Rule

If a Starry or LTP change is required, SyscallGuard records the plan and links
to the external change. The actual code change happens outside this repository.

