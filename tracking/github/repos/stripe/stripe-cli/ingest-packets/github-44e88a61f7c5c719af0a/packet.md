# GitHub ingest packet

- Repository: `stripe/stripe-cli`
- Work item: `github-44e88a61f7c5c719af0a`
- Snapshot: `raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/manifest.json`
- Recommended mode: `delta`
- Review priority: `normal`

## `stripe-cli`

- Version: `1.50.6` -> `1.50.7`
- Recommendation: `delta` / `normal`
- Unchanged retained files: `109`

### Required reading

- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.7/2026-10-06/manifest.json`
- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.7/2026-10-06/release-notes.md`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/files/pkg/cmd/login.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/files/pkg/cmd/root.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/files/pkg/cmd/switch.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/files/pkg/config/config.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/files/pkg/config/migrate.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/files/pkg/config/plugin_configs.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/files/pkg/config/profile.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/files/pkg/login/switch_context.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/files/pkg/proxy/proxy.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/files/pkg/stripe/url.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/manifest.json`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-ba4ee1f/manifest.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.6--1.50.7/comparison.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.6--1.50.7/comparison.md`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.6--1.50.7/diff.patch`

### Upstream changes

- `modified` `.github/workflows/curl-install-test.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/cmd/config_migration.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/cmd/config_migration_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/docs/prefs.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/login.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/cmd/login_helpers.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/login_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/plugin/install.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/cmd/plugin/lifecycle.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/cmd/plugin/lifecycle_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/plugin/uninstall.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/plugin/upgrade.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/plugin_cmds.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/pluginhints/pluginhints.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/provision.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/root.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/cmd/sandbox.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/sandbox_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/switch.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/config/config.go`: `retained-evidence` (snapshot-file)
- `added` `pkg/config/config_layout_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `added` `pkg/config/migrate.go`: `retained-evidence` (snapshot-file)
- `added` `pkg/config/migrate_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/config/plugin_configs.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/config/profile.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/config/profile_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/errorcategory/category.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/errorcategory/category_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/login/switch_context.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/logtailing/tailer.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/logtailing/tailer_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/plugins/config_compat.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/plugins/config_compat_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/core_cli_helper.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/core_cli_helper_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/interface_grpc_3.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/plugin.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/plugin_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/proto/main.pb.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/proto/main.proto`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/proto/main_grpc.pb.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/proxy/proxy.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/proxy/proxy_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/reporting/classify.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/reporting/classify_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/reporting/reporting.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/reporting/reporting_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/reporting/scrub.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/reporting/scrub_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/stripe/url.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/stripe/url_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `added` `scripts/install.ps1`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `scripts/install.sh`: `intentional-policy-exclusion` (outside-capsule-policy)
