# GitHub ingest packet

- Repository: `stripe/stripe-cli`
- Work item: `github-c88c49cb6c8cce4a9dab`
- Snapshot: `raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/manifest.json`
- Recommended mode: `delta`
- Review priority: `normal`

## `stripe-cli`

- Version: `1.52.0` -> `1.52.1`
- Recommendation: `delta` / `normal`
- Unchanged retained files: `113`

### Required reading

- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.52.1/2026-10-06/manifest.json`
- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.52.1/2026-10-06/release-notes.md`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/files/pkg/config/config.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/files/pkg/config/plugin_configs.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/files/pkg/proxy/events_list.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/files/pkg/requests/base.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/files/pkg/requests/plugin.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/files/pkg/requests/stripe_version_header.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/files/pkg/stripe/verbosetransport.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/manifest.json`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a5d9d6/manifest.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.52.0--1.52.1/comparison.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.52.0--1.52.1/comparison.md`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.52.0--1.52.1/diff.patch`

### Upstream changes

- `modified` `api/openapi-spec/spec3.cli.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `api/openapi-spec/spec3.cli.preview.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/agentsetup/claude.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/agentsetup/claude_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/agentsetup/codex.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/agentsetup/codex_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/agentsetup/cursor.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/agentsetup/cursor_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/agentsetup/grok.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/agentsetup/grok_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/agentsetup/provider.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/agentsetup/provider_helpers.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/agent_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/plugin/auto_update.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/plugin/auto_update_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/resources/resources_gen.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/resources/specs_gen.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/config/config.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/config/config_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/config/plugin_configs.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/config/plugin_configs_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/plugins/auto_upgrade.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/auto_upgrade_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/config_compat.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/plugin.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/plugin_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/utilities.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/utilities_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/proxy/events_list.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/requests/base.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/requests/base_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/requests/plugin.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/requests/stripe_version_header.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/stripe/verbosetransport.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/stripe/verbosetransport_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/version/version.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/version/version_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
