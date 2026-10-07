# GitHub ingest packet

- Repository: `stripe/stripe-cli`
- Work item: `github-30e591eb05618f8c9c5e`
- Snapshot: `raw/github/stripe/stripe-cli/snapshots/2026-10-06-f5f390b/manifest.json`
- Recommended mode: `delta`
- Review priority: `normal`

## `stripe-cli`

- Version: `1.50.4` -> `1.50.5`
- Recommendation: `delta` / `normal`
- Unchanged retained files: `117`

### Required reading

- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.5/2026-10-06/manifest.json`
- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.5/2026-10-06/release-notes.md`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-2f3420a/manifest.json`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-f5f390b/files/pkg/login/oauth_device.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-f5f390b/manifest.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.4--1.50.5/comparison.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.4--1.50.5/comparison.md`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.4--1.50.5/diff.patch`

### Upstream changes

- `modified` `pkg/ansi/ansi.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/cmd/agent_env_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/templates_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/unknown_cmd_telemetry_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/docs/markdown/document.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/docs/markdown/document_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/docs/markdown/renderer.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/docs/markdown/renderer_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/docs/tui/model.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/docs/tui/model_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/login/oauth_device.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/stripe/analytics_telemetry_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/useragent/useragent.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/useragent/useragent_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
