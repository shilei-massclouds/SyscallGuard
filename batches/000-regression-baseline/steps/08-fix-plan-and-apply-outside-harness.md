# Step 08 - Fix Plan And Apply Outside Harness

Batch: `000-regression-baseline`
Status: `ready_for_human_review`

## Purpose

Record fix status while preserving the boundary that SyscallGuard does not
modify Starry or LTP.

## Fix Status

All scoped behaviors are treated as already repaired or already implemented in
the referenced local `tgoskits` checkout for purposes of this baseline.

External source:

- Repository: `/home/cloud/gitLinux/tgoskits`
- Branch: `dev-ltp-spec-2`
- Commit: `4f30e12d17e4da175233bb3a51889efe747a45f9`

## Outputs

- Fix status reflected in `outputs/coverage-matrix.yaml`.

## Gaps And Risks

- No pull request URLs or release tags were captured for every behavior.
- Future batches should include immutable external links for each fix.

