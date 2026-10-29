# GitHub ingest packet

- Repository: `stripe/stripe-cli`
- Work item: `github-541a1da1348b9d86a709`
- Snapshot: `raw/github/stripe/stripe-cli/snapshots/2026-10-30-b93a4f3/manifest.json`
- Recommended mode: `delta`
- Review priority: `normal`

## `stripe-cli`

- Version: `1.55.2` -> `1.55.3`
- Recommendation: `delta` / `normal`
- Unchanged retained files: `113`

### Required reading

- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.55.3/2026-10-30/manifest.json`
- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.55.3/2026-10-30/release-notes.md`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-2713dc4/manifest.json`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-b93a4f3/files/pkg/cmd/login.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-b93a4f3/files/pkg/cmd/root.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-b93a4f3/files/pkg/cmd/switch.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-b93a4f3/files/pkg/cmd/whoami.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-b93a4f3/files/pkg/login/login.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-b93a4f3/files/pkg/login/oauth_accounts.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-b93a4f3/files/pkg/login/oauth_device.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-b93a4f3/files/pkg/login/oauth_reauth.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-b93a4f3/files/pkg/login/oauth_refresh.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-b93a4f3/files/pkg/login/parent_accounts.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-b93a4f3/files/pkg/login/switch_context.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-b93a4f3/files/pkg/requests/context_statuses.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-b93a4f3/manifest.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.55.2--1.55.3/comparison.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.55.2--1.55.3/comparison.md`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.55.2--1.55.3/diff.patch`

### Upstream changes

- `modified` `pkg/cmd/login.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/cmd/login_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/plugin/install.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/pluginhints/pluginhints.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/reauth.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/root.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/cmd/sandbox.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/sandbox_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/switch.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/cmd/whoami.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/cmd/whoami_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/fixtures/triggers/charge.refund.updated.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/fixtures/triggers/charge.refunded.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/fixtures/triggers/charge.updated.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/fixtures/triggers/customer.tax_id.created.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/fixtures/triggers/customer.tax_id.deleted.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/fixtures/triggers/issuing_authorization.created.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/fixtures/triggers/issuing_authorization.updated.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/fixtures/triggers/issuing_card.updated.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/fixtures/triggers/issuing_cardholder.updated.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/login/login.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/login/oauth_accounts.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/login/oauth_accounts_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/login/oauth_device.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/login/oauth_device_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/login/oauth_reauth.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/login/oauth_reauth_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/login/oauth_refresh.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/login/oauth_refresh_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `added` `pkg/login/parent_accounts.go`: `retained-evidence` (snapshot-file)
- `added` `pkg/login/parent_accounts_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `added` `pkg/login/print_authorized_summary_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/login/switch_context.go`: `retained-evidence` (snapshot-file)
- `added` `pkg/login/switch_context_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/plugins/core_cli_helper.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/core_cli_helper_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/requests/context_statuses.go`: `retained-evidence` (snapshot-file)
- `added` `pkg/requests/context_statuses_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
