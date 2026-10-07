# GitHub ingest packet

- Repository: `stripe/stripe-cli`
- Work item: `github-a243b054a19fc4d40e6c`
- Snapshot: `raw/github/stripe/stripe-cli/snapshots/2026-10-06-2f3420a/manifest.json`
- Recommended mode: `delta`
- Review priority: `normal`

## `stripe-cli`

- Version: `1.50.3` -> `1.50.4`
- Recommendation: `delta` / `normal`
- Unchanged retained files: `114`

### Required reading

- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.4/2026-10-06/manifest.json`
- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.4/2026-10-06/release-notes.md`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-2f3420a/files/pkg/cmd/root.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-2f3420a/files/pkg/cmd/whoami.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-2f3420a/files/pkg/login/oauth_accounts.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-2f3420a/files/pkg/requests/user_info.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-2f3420a/manifest.json`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-53f08e9/manifest.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.3--1.50.4/comparison.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.3--1.50.4/comparison.md`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.3--1.50.4/diff.patch`

### Upstream changes

- `modified` `pkg/cmd/docs/search.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/docs/search_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/pluginhints/pluginhints.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/cmd/provision.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/cmd/provision_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/root.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/cmd/sandbox.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/sandbox_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/whoami.go`: `retained-evidence` (snapshot-file)
- `added` `pkg/login/main_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/login/oauth_accounts.go`: `retained-evidence` (snapshot-file)
- `added` `pkg/plugins/main_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/requests/user_info.go`: `retained-evidence` (snapshot-file)
- `added` `pkg/requests/user_info_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
