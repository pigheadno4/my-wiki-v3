# GitHub ingest packet

- Repository: `stripe/stripe-cli`
- Work item: `github-6142e6edfb7b02322f4b`
- Snapshot: `raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a5d9d6/manifest.json`
- Recommended mode: `delta`
- Review priority: `normal`

## `stripe-cli`

- Version: `1.51.1` -> `1.52.0`
- Recommendation: `delta` / `normal`
- Unchanged retained files: `117`

### Required reading

- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.52.0/2026-10-06/manifest.json`
- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.52.0/2026-10-06/release-notes.md`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a5d9d6/files/cmd/stripe/main.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a5d9d6/files/pkg/cmd/root.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a5d9d6/files/pkg/requests/plugin.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a5d9d6/manifest.json`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/manifest.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.51.1--1.52.0/comparison.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.51.1--1.52.0/comparison.md`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.51.1--1.52.0/diff.patch`

### Upstream changes

- `modified` `.github/workflows/autoupgrade-test.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/install-test.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `.github/workflows/notify-developer-products-review.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `cmd/stripe/main.go`: `retained-evidence` (snapshot-file)
- `added` `pkg/agentsetup/grok.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/agentsetup/grok_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/agentsetup/provider.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/autoupdate/checker.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/autoupdate/checker_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/autoupdate/config.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/autoupdate/config_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/autoupdate/reexec_unix.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/autoupdate/reexec_windows.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/autoupdate/replace.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/autoupdate/replace_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/autoupdate/telemetry.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/autoupdate/telemetry_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/autoupdate/updater.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/autoupdate/updater_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/agent.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/agent_env_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/agent_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/plugin/auto_update.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/plugin/auto_update_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/pluginhints/pluginhints.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/pluginhints/pluginhints_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/root.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/plugins/auto_upgrade.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/auto_upgrade_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/plugin.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/plugin_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/utilities.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/utilities_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/reporting/command_bucket.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/reporting/command_bucket_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/reporting/reporting.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/reporting/reporting_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/requests/plugin.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/requests/plugin_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/useragent/useragent.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/useragent/useragent_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `scripts/install.sh`: `intentional-policy-exclusion` (outside-capsule-policy)
