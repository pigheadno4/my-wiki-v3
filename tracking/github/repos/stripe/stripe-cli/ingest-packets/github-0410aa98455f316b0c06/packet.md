# GitHub ingest packet

- Repository: `stripe/stripe-cli`
- Work item: `github-0410aa98455f316b0c06`
- Snapshot: `raw/github/stripe/stripe-cli/snapshots/2026-10-30-9830249/manifest.json`
- Recommended mode: `delta`
- Review priority: `normal`

## `stripe-cli`

- Version: `1.54.1` -> `1.55.0`
- Recommendation: `delta` / `normal`
- Unchanged retained files: `119`

### Required reading

- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.55.0/2026-10-30/manifest.json`
- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.55.0/2026-10-30/release-notes.md`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-9830249/files/pkg/cmd/root.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-9830249/files/pkg/requests/base.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-9830249/files/pkg/stripe/analytics_telemetry.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-9830249/files/pkg/stripe/client.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-9830249/manifest.json`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-e04aea5/manifest.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.54.1--1.55.0/comparison.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.54.1--1.55.0/comparison.md`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.54.1--1.55.0/diff.patch`

### Upstream changes

- `modified` `.github/workflows/test-snapshot.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `CODEOWNERS`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/docs/api_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/root.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/docs/client.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/docs/client_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/core_cli_helper.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/plugins/core_cli_helper_output_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/interface_grpc_3.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/plugin.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/plugin_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/proto/main.pb.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/proto/main.proto`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/proto/main_grpc.pb.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/plugins/rendering/engine.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/plugins/rendering/engine_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/plugins/rendering/envelope.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/plugins/sdk/sdk.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/plugins/sdk/sdk_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/reporting/reporting.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/reporting/reporting_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/requests/base.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/requests/base_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/stripe/analytics_telemetry.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/stripe/analytics_telemetry_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/stripe/client.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/stripe/client_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
