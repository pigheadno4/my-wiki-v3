# GitHub ingest packet

- Repository: `stripe/stripe-cli`
- Work item: `github-6f28a665749d03e55161`
- Snapshot: `raw/github/stripe/stripe-cli/snapshots/2026-10-06-ba4ee1f/manifest.json`
- Recommended mode: `delta`
- Review priority: `normal`

## `stripe-cli`

- Version: `1.50.5` -> `1.50.6`
- Recommendation: `delta` / `normal`
- Unchanged retained files: `114`

### Required reading

- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.6/2026-10-06/manifest.json`
- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.6/2026-10-06/release-notes.md`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-ba4ee1f/files/pkg/cmd/root.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-ba4ee1f/files/pkg/cmd/whoami.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-ba4ee1f/files/pkg/login/oauth_refresh.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-ba4ee1f/files/pkg/requests/plugin.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-ba4ee1f/manifest.json`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-f5f390b/manifest.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.5--1.50.6/comparison.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.5--1.50.6/comparison.md`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.5--1.50.6/diff.patch`

### Upstream changes

- `modified` `canary/README.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `canary/data_reporting_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/cmd/analytics_help_examples_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/data.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/data_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/cmd/metric_query_error.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/cmd/metric_query_error_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/cmd/nested_flags.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/cmd/nested_flags_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/plugin_cmds.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/plugin_cmds_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/pluginhints/pluginhints.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/pluginhints/pluginhints_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/reporting.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/reporting_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/cmd/resource/nested_flags.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/resource/operation.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/resource/operation_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/root.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/cmd/templates.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/templates_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/whoami.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/cmd/whoami_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmdutil/cmdutil.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmdutil/cmdutil_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/login/oauth_refresh.go`: `retained-evidence` (snapshot-file)
- `added` `pkg/login/oauth_refresh_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/plugins/plugin.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/plugin_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/test_utils.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/utilities.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/utilities_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/requests/plugin.go`: `retained-evidence` (snapshot-file)
