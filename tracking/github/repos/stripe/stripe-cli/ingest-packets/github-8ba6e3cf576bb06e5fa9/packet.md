# GitHub ingest packet

- Repository: `stripe/stripe-cli`
- Work item: `github-8ba6e3cf576bb06e5fa9`
- Snapshot: `raw/github/stripe/stripe-cli/snapshots/2026-10-06-eea8a71/manifest.json`
- Recommended mode: `delta`
- Review priority: `normal`

## `stripe-cli`

- Version: `1.52.1` -> `1.52.2`
- Recommendation: `delta` / `normal`
- Unchanged retained files: `115`

### Required reading

- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.52.2/2026-10-06/manifest.json`
- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.52.2/2026-10-06/release-notes.md`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/manifest.json`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-eea8a71/files/pkg/cmd/root.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-eea8a71/files/pkg/fixtures/fixtures.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-eea8a71/files/pkg/login/login.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-eea8a71/files/pkg/login/oauth_device.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-eea8a71/files/pkg/login/oauth_pending.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-eea8a71/manifest.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.52.1--1.52.2/comparison.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.52.1--1.52.2/comparison.md`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.52.1--1.52.2/diff.patch`

### Upstream changes

- `deleted` `.github/workflows/autoupgrade-test-trigger.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/autoupgrade-test.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `api/openapi-spec/spec3.cli.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `api/openapi-spec/spec3.cli.preview.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/cmd/resource/boolean_args.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/cmd/resource/boolean_args_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/resources/specs_gen.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/root.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/cmd/root_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/templates.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/templates_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/fixtures/fixtures.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/fixtures/fixtures_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/login/login.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/login/oauth_device.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/login/oauth_device_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/login/oauth_pending.go`: `retained-evidence` (snapshot-file)
