---
title: "Stripe CLI"
type: concept
category: technology
tags: [stripe, developer-tools, cli, webhooks, fixtures, api-testing]
---

## Definition

Stripe CLI is Stripe's command-line developer tool for building, testing, and operating Stripe integrations. At the retained `stripe-cli@1.50.0` baseline, it combines direct Stripe API requests, API-resource commands, fixture execution, synthetic event triggers, webhook listening and local forwarding, request-log streaming, and account/context authentication.

## Checkout-Relevant Workflows

- **Webhook development:** `stripe listen` receives events through Stripe's WebSocket service and can forward standard, thin, and Connect events to local endpoints. It can filter event types, emit JSON, load configured webhook endpoints, and print the local signing secret.
- **Event simulation:** `stripe trigger` runs embedded JSON fixtures that issue API requests needed to produce an event. Unsupported events require a real API or Dashboard action, or a custom fixture.
- **Fixture-driven setup:** `stripe fixtures` executes ordered requests from a JSON file. Steps can reference earlier responses and environment variables and can be skipped, overridden, added to, or stripped of parameters.
- **Direct API access:** generic `get`, `post`, and `delete` commands support Stripe API paths. Request controls include data, expansion, idempotency keys, API version, connected-account/context headers, pagination, and dry-run output.
- **Authentication and contexts:** the CLI supports API keys, browser login, non-interactive/device OAuth, stored profiles, and account or sandbox context switching. Test mode is the default for relevant commands; live behavior requires explicit credentials and mode selection.

## Evidence Boundaries

- Embedded trigger fixtures are executable examples for test setup, not the canonical definition of an API object's lifecycle or merchant eligibility.
- CLI success does not replace webhook signature verification, idempotent fulfillment, or server-side reconciliation.
- The retained source history covers `stripe-cli@1.50.0` through `1.53.0`; later behavior requires its cumulative source and changelog.
- Version `1.50.0` adds agent host and self-reported agent identifiers to telemetry. Users can opt out through `STRIPE_CLI_TELEMETRY_OPTOUT` or `DO_NOT_TRACK`.

## Authentication and Tooling Changes in `1.50.1`

- OAuth access-service destinations accept only the exact production or QA origin. Access-service requests no longer follow redirects, and device/reauthentication browser URLs require HTTPS and a matching trusted host. This is CLI credential protection, not a merchant checkout capability.
- `stripe login --new-session` attempts to revoke the previous OAuth refresh token before starting another login. A revocation failure warns and continues; successful revocation is not guaranteed.
- Mode-tolerant plugin credential resolution becomes a shared profile helper; the plugin metadata/list fallback existed in `1.50.0`. Payment requests and webhook listening still enforce their mode controls.
- Telemetry additionally retains `agent_host_raw`; error origins gain explicit categories. Internal-development WebSocket routing distinguishes Unix-socket dev hosts from public hosts sent through an HTTP CONNECT proxy.
- Release notes announce a feedback command and a credential-resolution plugin RPC, but their implementation is outside the retained capsule. Deep questions need exact-SHA supplemental evidence, not assumptions from the announcements. See [[source-github-stripe-cli]] and [[changelog-github-stripe-cli]].

## Profile and Reauthorization Changes in `1.50.2`

`stripe config --remove-profile <name>` adds confirmation-protected removal, including legacy dotted profile names; non-interactive callers must pass `--confirm`. Reserved machine-wide configuration keys cannot be removed as profiles. Dotted active profiles warn once per process and should be migrated to a non-dotted name.

Reauthorization now polls authorized accounts every three seconds for up to ten minutes and prints an updated context summary when the account ID/name/mode signature changes. This is not a dedicated completion signal: unchanged authorization can time out, and timeout/cancellation return without an error. Display wording changes from test to sandbox, without changing the underlying API `test` value or stable key fields. See [[source-github-stripe-cli]] and [[changelog-github-stripe-cli]].

Version `1.50.3` announces a `ResolveCredentialsForAnyMode` plugin RPC. Its handler and protocol are outside the capsule; this announcement does not establish its detailed contract. See [[source-github-stripe-cli]] and [[changelog-github-stripe-cli]].

## Version `1.50.4`: OAuth Identity Output

OAuth `whoami` fetches authorized accounts and optional user/role information. In this version the OAuth branch bypasses the JSON formatter; account-fetch errors fail, optional identity-fetch errors do not. See [[source-github-stripe-cli]] and [[changelog-github-stripe-cli]].

## Version `1.50.5`: Login Prompt and Agent Announcements

The OAuth login prompt puts the authorization URL before the verification code. The retained change is presentation-only, not a new token flow. See [[source-github-stripe-cli]] and [[changelog-github-stripe-cli]].

## Version `1.50.6`: OAuth JSON and Refresh Metadata

OAuth whoami now supports JSON, using authorized_accounts and optional account/mode/email/role/Unix expiry fields rather than the API-key schema. OAuth refresh preserves existing profile identity metadata. See [[source-github-stripe-cli]] and [[changelog-github-stripe-cli]].

Version `1.50.6` fixes the historical OAuth JSON omission above, but its OAuth JSON omits API-key fields and still makes network requests despite the help wording. The warning is not a claim that JSON remains unsupported.

> [!warning] Contradiction
> In `1.50.4`, whoami help promises no API calls and stable JSON, but its OAuth path fetches accounts/user information and prints text even with `--format json`. The API-key branch remains separate. See [[source-github-stripe-cli]].

## Version `1.50.7`: config v2 migration and base-URL hardening

This release adds a config-v2 migration library and dual-layout profile reads/writes, preserves flat OS-keyring identities, rejects new empty/dotted profile names, and validates parsed base-URL hosts. OAuth context selection now returns an explicit result. Automatic migration/plugin compatibility are outside the capsule; consult version-specific evidence rather than assuming every command migrates the file. See [[source-github-stripe-cli]] and [[changelog-github-stripe-cli]].

## Version `1.50.8`: plugin minimum-core-version errors

The metadata request layer recognizes HTTP 400 with plugin_requires_newer_cli and extracts an optional min_core_version. Release notes announce installation enforcement; installer, upgrade and version-comparison implementations are excluded, so their exact behavior needs supplemental evidence. See [[source-github-stripe-cli]] and [[changelog-github-stripe-cli]].

## Version `1.50.9`: installation telemetry and docs announcements

Telemetry delegates installation-method detection to installmethod.Detect. Notes also announce docs context/mode header forwarding, restored docs pre-run/telemetry and upgrade-command guidance, but those implementations are excluded; exact routing/detection details are not established. See [[source-github-stripe-cli]] and [[changelog-github-stripe-cli]].

## Version `1.50.10`: agent usage-report announcement

This release announces stripe agent report_usage. The retained capsule is hash-identical to 1.50.9; the command implementation is excluded, so its payload, authorization, opt-out and transport behavior are not established. See [[source-github-stripe-cli]] and [[changelog-github-stripe-cli]].

## Version `1.50.11`: login reauthorization and device completion

Existing valid OAuth sessions now make stripe login initiate reauthorization, not merely print existing identity. Non-interactive reauthorization returns browser_url and next_step = stripe login --complete-reauth, with no verification_code. Completion uses account ID/name/mode changes and can return nil on timeout/cancel or print current contexts without a saved baseline, so process success is not confirmation. Device login shares a poll/save helper and detaches cancellation after token issuance. Default generated API headers advance to 2026-08-26.dahlia / .preview; preview event names and uninstall guidance are version-qualified. See [[source-github-stripe-cli]] and [[changelog-github-stripe-cli]].

## Version `1.51.0`: explicit webhook subscriptions and account switching

Webhook forwarding now needs explicit event selection; --events '*' is rejected, while bare listen subscribes to snapshot and thin channels. Unified --events classifies version-prefixed names as thin; snapshot/thin payloads cannot share the corresponding forwarding destination. --events-from filters self/connected accounts. Deprecated thin flags still work. stripe switch supports account_id/display_name/mode JSON and retains switch context as a hidden alias. OAuth whoami refreshes near-expiry tokens and removes historical no-network/universal-schema help claims. These are CLI tooling changes, not new checkout methods. See [[source-github-stripe-cli]] and [[changelog-github-stripe-cli]].

## Version `1.51.1`: resumable device login and config collision fixes

Device-login helpers can discover/resume a valid pending code and check once without a polling loop; CLI non-interactive login still mints fresh. Poll caller cancellation preserves pending state before its persisted deadline, but other failures can clear it. New issued_at makes older pending files expire locally. Config migration recognizes reserved-name profile collisions; new-file stamping is a library capability, not proof of automatic invocation. See [[source-github-stripe-cli]] and [[changelog-github-stripe-cli]].

## Version `1.52.0`: automatic CLI update wiring and plugin rollout metadata

Release notes announce automatic updates for install-script installations and Grok agent setup. Retained main wiring applies pending updates before command execution and defers a check until normal return; command-failure os.Exit bypasses that defer. The updater internals remain excluded. Plugin metadata removes machine_uuid, while auto_install stays present. See [[source-github-stripe-cli]] and [[changelog-github-stripe-cli]].

## Version `1.52.1`: custom request headers and Endive API defaults

Request commands add repeatable --request-header/-H with last-value-wins parsing. Custom headers follow generated auth/context/version/idempotency headers and can override them; verbose output and dry-run JSON can expose custom secrets. Defaults advance to 2026-09-30.endive / .preview. Plugin update decisions now use a backend default only when neither local override is set; this supersedes the earlier default-off behavior for these helpers. See [[source-github-stripe-cli]] and [[changelog-github-stripe-cli]].

## Version `1.52.2`: OAuth Code Prefilling and Fixture Guidance

OAuth login prefers the server-provided verification_uri_complete URL, falling back to verification_uri; fresh interactive and non-interactive URLs are validated before use. Older valid pending sessions without the new field retain their fallback. Accounts v1 fixture creation failures gain guidance, but the message is not a verified diagnosis of account eligibility. Resource boolean normalization is wired at the root; its excluded helper requires supplemental evidence for detailed flag semantics. See [[source-github-stripe-cli]] and [[changelog-github-stripe-cli]].

## Version `1.53.0`: Version Release-Notes Command Announcement

Release 1.53.0 announces `stripe version --notes`. All 120 retained files match 1.52.2; four upstream version-command/library/test paths are intentionally excluded. The announcement is note-backed, not an implementation audit; an empty retained diff does not mean an unchanged upstream repository. See [[source-github-stripe-cli]] and [[changelog-github-stripe-cli]].

## Related
> [!warning] Contradiction
> The earlier source summary bounded OAuth request refresh to one retry. The baseline, prior and `1.51.0` retained request implementation recurses without an explicit one-retry guard for repeated eligible unauthorized responses. This is a corrected evidence interpretation, not a newly introduced release behavior or a safe replay guarantee. The `1.51.0` whoami help separately resolves the historical no-network/universal-schema wording mismatch. See [[source-github-stripe-cli]] and [[changelog-github-stripe-cli]].

> [!warning] Contradiction
> The `1.50.11` reauthorization helper comment refers to scope changes, but its completion signature compares account ID, name and modes only. A scope-only change may not be detected. This is separate from the historical `whoami` help mismatch. See [[source-github-stripe-cli]].


- Company: [[stripe]]
- Source: [[source-github-stripe-cli]]
- History: [[changelog-github-stripe-cli]]
