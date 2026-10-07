# GitHub ingest packet

- Repository: `stripe/stripe-cli`
- Work item: `github-31650eba29ec951da332`
- Snapshot: `raw/github/stripe/stripe-cli/snapshots/2026-10-06-07050f2/manifest.json`
- Recommended mode: `delta`
- Review priority: `normal`

## `stripe-cli`

- Version: `1.50.7` -> `1.50.8`
- Recommendation: `delta` / `normal`
- Unchanged retained files: `118`

### Required reading

- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.8/2026-10-06/manifest.json`
- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.8/2026-10-06/release-notes.md`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-07050f2/files/pkg/requests/plugin.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-07050f2/manifest.json`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/manifest.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.7--1.50.8/comparison.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.7--1.50.8/comparison.md`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.7--1.50.8/diff.patch`

### Upstream changes

- `modified` `pkg/cmd/plugin/install.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/plugin/install_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/plugin/upgrade.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/pluginhints/pluginhints.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/pluginhints/pluginhints_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/plugins/min_core_version.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/plugins/min_core_version_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/plugin.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/utilities.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/requests/plugin.go`: `retained-evidence` (snapshot-file)
- `added` `pkg/requests/plugin_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
