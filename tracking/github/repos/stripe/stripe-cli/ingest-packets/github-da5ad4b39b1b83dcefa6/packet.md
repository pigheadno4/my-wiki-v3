# GitHub ingest packet

- Repository: `stripe/stripe-cli`
- Work item: `github-da5ad4b39b1b83dcefa6`
- Snapshot: `raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/manifest.json`
- Recommended mode: `delta`
- Review priority: `normal`

## `stripe-cli`

- Version: `1.50.1` -> `1.50.2`
- Recommendation: `delta` / `normal`
- Unchanged retained files: `99`

### Required reading

- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.2/2026-10-06/manifest.json`
- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.2/2026-10-06/release-notes.md`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/manifest.json`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/cmd/config.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/cmd/delete.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/cmd/listen.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/cmd/login.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/cmd/logout.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/cmd/post.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/cmd/root.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/cmd/switch.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/cmd/trigger.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/cmd/whoami.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/config/config.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/config/profile.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/login/login.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/login/oauth_accounts.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/login/oauth_device.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/login/oauth_reauth.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/login/switch_context.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/requests/base.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/manifest.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.1--1.50.2/comparison.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.1--1.50.2/comparison.md`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.1--1.50.2/diff.patch`

### Upstream changes

- `modified` `.github/actions/install-stripe-cli/action.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `.github/dependabot.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/autoupgrade-test-trigger.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/canary-test.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/curl-install-test.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/data-analytics-canary.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/install-test.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/plugin-canary.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/release.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/sync-openapi-artifacts.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/test-snapshot.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/test.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/config.go`: `retained-evidence` (snapshot-file)
- `added` `pkg/cmd/config_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/delete.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/cmd/listen.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/cmd/login.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/cmd/logout.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/cmd/logs/tail.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/pluginhints/pluginhints.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/post.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/cmd/root.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/cmd/switch.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/cmd/templates.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/templates_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/trigger.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/cmd/whoami.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/config/config.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/config/config_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/config/profile.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/config/profile_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/login/login.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/login/oauth_accounts.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/login/oauth_device.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/login/oauth_reauth.go`: `retained-evidence` (snapshot-file)
- `added` `pkg/login/oauth_reauth_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/login/switch_context.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/requests/base.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/validators/validate.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/validators/validate_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
