# GitHub ingest packet

- Repository: `stripe/stripe-cli`
- Work item: `github-ee134a80def44f62fd7f`
- Snapshot: `raw/github/stripe/stripe-cli/snapshots/2026-10-30-7839c31/manifest.json`
- Recommended mode: `delta`
- Review priority: `normal`

## `stripe-cli`

- Version: `1.53.1` -> `1.54.0`
- Recommendation: `delta` / `normal`
- Unchanged retained files: `113`

### Required reading

- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.54.0/2026-10-30/manifest.json`
- `raw/github/stripe/stripe-cli/releases/stripe-cli/1.54.0/2026-10-30/release-notes.md`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-7839c31/files/pkg/cmd/login.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-7839c31/files/pkg/cmd/root.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-7839c31/files/pkg/login/oauth_accounts.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-7839c31/files/pkg/login/oauth_device.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-7839c31/files/pkg/login/oauth_reauth.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-7839c31/files/pkg/requests/playground_context.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-7839c31/files/pkg/requests/plugin.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-7839c31/files/pkg/requests/workspace_context.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-7839c31/files/pkg/rpcservice/events_resend.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-7839c31/files/pkg/stripe/path.go`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-7839c31/manifest.json`
- `raw/github/stripe/stripe-cli/snapshots/2026-10-30-9725e09/manifest.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.53.1--1.54.0/comparison.json`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.53.1--1.54.0/comparison.md`
- `tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.53.1--1.54.0/diff.patch`

### Upstream changes

- `modified` `.github/workflows/autoupgrade-test.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `CODEOWNERS`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/agentsetup/claude.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/agentsetup/claude_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/agentsetup/codex.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/agentsetup/codex_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/agentsetup/grok.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/agentsetup/grok_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/agentsetup/openclaw.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/agentsetup/openclaw_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/agentsetup/provider.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/agentsetup/provider_helpers.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/agentsetup/scanner.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/agent_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/config_migration.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/login.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/cmd/plugin/install.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/plugin/upgrade.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/pluginhints/pluginhints.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/reporting.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/reporting_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/resource/databases.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/resource/databases_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/resource/operation.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/resource/operation_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/root.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/cmd/root_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/sandbox.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/sandbox_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/templates.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/cmd/templates_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/login/oauth_accounts.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/login/oauth_accounts_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/login/oauth_device.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/login/oauth_device_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/login/oauth_reauth.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/login/oauth_reauth_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/plugins/auto_upgrade.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/auto_upgrade_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/core_cli_helper.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/plugins/dependencies.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/plugins/dependencies_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/min_core_version_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/plugin.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/plugin_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `pkg/plugins/utilities.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/requests/playground_context.go`: `retained-evidence` (snapshot-file)
- `added` `pkg/requests/playground_context_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/requests/plugin.go`: `retained-evidence` (snapshot-file)
- `added` `pkg/requests/workspace_context.go`: `retained-evidence` (snapshot-file)
- `added` `pkg/requests/workspace_context_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `pkg/rpcservice/events_resend.go`: `retained-evidence` (snapshot-file)
- `modified` `pkg/rpcservice/events_resend_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/sandbox/management.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/sandbox/management_test.go`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `pkg/stripe/path.go`: `retained-evidence` (snapshot-file)
- `added` `pkg/stripe/path_test.go`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `scripts/install.ps1`: `intentional-policy-exclusion` (outside-capsule-policy)
