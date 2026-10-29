# GitHub ingest packet

- Repository: `stripe/stripe-cli`
- Work item: `github-8eee50d578a32111fa93`
- Snapshot: `raw/github/stripe/stripe-cli/snapshots/2026-10-30-4501fc5/manifest.json`
- Recommended mode: `delta`
- Review priority: `normal`

## `stripe-cli`

- Version: `1.55.0` -> `1.55.1`
- Recommendation: `delta` / `normal`
- Unchanged retained files: `122`

### Required reading

- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.55.1/2026-10-30/manifest.json`
- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.55.1/2026-10-30/release-notes.md`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-4501fc5/files/pkg/requests/base.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-4501fc5/manifest.json`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-9830249/manifest.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.55.0--1.55.1/comparison.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.55.0--1.55.1/comparison.md`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.55.0--1.55.1/diff.patch`

### Upstream changes

- `modified` `pkg/cmd/resource/operation.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/resource/operation_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/resource/spec_data.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/resources/specs_gen.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/templates.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/templates_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/gen/gen_resources_cmds.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/gen/gen_resources_cmds_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/gen/resource_specs.go.tpl`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/requests/base.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/requests/base_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
