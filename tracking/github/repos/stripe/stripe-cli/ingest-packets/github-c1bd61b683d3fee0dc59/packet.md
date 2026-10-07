# GitHub ingest packet

- Repository: `stripe/stripe-cli`
- Work item: `github-c1bd61b683d3fee0dc59`
- Snapshot: `raw/github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/manifest.json`
- Recommended mode: `delta`
- Review priority: `normal`

## `stripe-cli`

- Version: `1.51.0` -> `1.51.1`
- Recommendation: `delta` / `normal`
- Unchanged retained files: `115`

### Required reading

- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.51.1/2026-10-06/manifest.json`
- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.51.1/2026-10-06/release-notes.md`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/manifest.json`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/files/pkg/config/migrate.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/files/pkg/login/login.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/files/pkg/login/oauth_accounts.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/files/pkg/login/oauth_device.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/files/pkg/login/oauth_pending.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/manifest.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.51.0--1.51.1/comparison.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.51.0--1.51.1/comparison.md`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.51.0--1.51.1/diff.patch`

### Upstream changes

- `modified` `.github/workflows/install-test.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/config_migration.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/config_migration_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/plugin_cmds.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/plugin_cmds_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/config/migrate.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/config/migrate_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/login/login.go`: `retained-evidence` (snapshot-file)
- `added` `pkg/login/login_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/login/oauth_accounts.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/login/oauth_accounts_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/login/oauth_device.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/login/oauth_pending.go`: `retained-evidence` (snapshot-file)
- `added` `pkg/login/oauth_pending_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/plugins/auto_upgrade.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/auto_upgrade_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/core_cli_helper.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/core_cli_helper_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/plugin.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/plugin_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/proto/main.pb.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/proto/main.proto`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/proto/main_grpc.pb.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/plugins/reported_error.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/plugins/reported_error_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/utilities.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/utilities_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
