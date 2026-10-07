---
title: "GitHub: stripe/stripe-cli"
type: source
date_ingested: 2026-08-14
date_updated: 2026-10-07
original_format: github-repo
raw_files:
  - "github/stripe/stripe-cli/snapshots/2026-10-06-a915fc6/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-eea8a71/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-1090068/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-4a5d9d6/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-c78e4ab/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-150fa3f/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-6056ace/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-07050f2/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-ba4ee1f/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-f5f390b/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-2f3420a/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-53f08e9/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/manifest.json"
tags: [stripe, stripe-cli, developer-tools, webhooks, fixtures, api-testing, github-repository]
---

## Overview

`stripe/stripe-cli` is Stripe's Go command-line tool for building, testing, and managing integrations. This initial full ingest records package-qualified release `stripe-cli@1.50.0`, exact SHA `a6f40658b99e4142fd63b2e4b560aa9c7ae337b1`, collected on 2026-08-14.

Repository: <https://github.com/stripe/stripe-cli>

An additive full ingest on 2026-10-07 adds `stripe-cli@1.50.1`, SHA `4a89968de966ca1978eb4c8da558367233769b4c`, without replacing the `1.50.0` baseline below. Sequential additive history now reaches `stripe-cli@1.53.0`; this is curated history, not a claim about the latest upstream version.

## Evidence Boundary

- Findings are version-qualified to the retained capsules through `stripe-cli@1.53.0`, not an unqualified latest CLI.
- The capsule focuses on checkout-relevant command, authentication, fixture, request, proxy, RPC, telemetry, and WebSocket code. It does not represent the complete upstream tree.
- This first immutable snapshot retains 28 Go test files as an approved one-time collection superset. The corrected future capsule policy excludes Go tests.
- Embedded trigger fixtures demonstrate how the CLI generates test events. They do not independently establish canonical API lifecycle, production availability, or merchant eligibility.
- The CLI is development and operations tooling. A successful local forward or synthetic trigger does not prove production fulfillment correctness.
- For `1.50.1` only, the user approved focused reading within additive full mode: all 32 added/modified retained files were read fully, with affected prior code, the complete comparison, and cumulative wiki history. Both snapshot inventories and hashes, 85 unchanged paths, and 28 policy-excluded prior tests were checked mechanically. Those test omissions are a collection-policy change, not upstream deletion.

## Grounding Excerpts

> "The Stripe CLI is a developer tool to help you build, test, and manage your integration with Stripe directly from the command line."
>
> `raw/github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/files/ARCHITECTURE.md:3`

> "Securely test webhooks without relying on 3rd party software"
>
> `raw/github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/files/README.md:10`

> "The listen command watches and forwards webhook events from Stripe to your local machine by connecting directly to Stripe's API."
>
> `raw/github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/files/pkg/cmd/listen.go:68`

> "Fixtures execute a sequence of API requests defined in a JSON file."
>
> `raw/github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/files/pkg/cmd/fixtures.go:41`

> "Capture agent host and self-reported agent identifiers in telemetry"
>
> `raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.0/2026-08-14/release-notes.md:2`

## Architecture and Commands

The CLI uses Cobra for command routing and Viper for flags and configuration. Handwritten commands live under `pkg/cmd`; generated resource namespaces and operations are based on Stripe's OpenAPI data and route generic HTTP operations through `pkg/requests/base.go` and `pkg/stripe/client.go`.

The retained checkout-focused surface includes generic `get`, `post`, and `delete`, resource commands, `fixtures`, `trigger`, `listen`, login/logout, profile/context switching, and request-log WebSocket handling. Generic request commands can address API paths directly; generated resource commands remain a convenience layer rather than separate API behavior.

## API Requests

V1 request data is form encoded while V2 data is JSON. The request layer supports expansion, pagination, API version selection, `Idempotency-Key`, `Stripe-Account`, and `Stripe-Context` headers. A dry-run path renders the resolved method, URL, parameters, and headers without executing the request.

OAuth-backed requests that receive the repository's specific unauthorized response can refresh credentials and re-enter the request path. The earlier summary described this as one retry; the `1.51.0` evidence audit below corrects that unsupported bound. This authentication path is not a guarantee of safe payment or business-operation replay.

Direct POST commands support idempotency keys and expansion. Production scripts should set idempotency explicitly for mutating payment operations and should not infer business success solely from CLI process completion.

## Webhook Listening and Forwarding

`stripe listen` connects to Stripe and receives standard webhook events and V2 thin events. It can:

- forward standard and thin events to separate local URLs;
- route Connect events and custom Connect headers separately;
- filter event types;
- use the account's default or latest API version;
- choose test mode by default or explicit live mode;
- load configured webhook endpoints;
- print JSON or the local signing secret.

Forwarded requests include event context and expose endpoint responses in the terminal. Local HTTP failures are reported without automatically ending the listener, while connection state supports reconnecting. Integrations still need signature verification, duplicate-event handling, idempotent fulfillment, and reconciliation outside the CLI.

## Triggers and Fixtures

`stripe trigger <event>` resolves embedded fixture JSON and executes the ordered API requests needed to produce the requested test event. The capsule includes checkout-session, PaymentIntent, SetupIntent, invoice, customer-subscription, and subscription-schedule examples.

Fixture steps can reference prior responses with `${resource:json_path}` and environment variables with `${.env:VAR|default}`. Operators can skip steps and add, remove, or override parameters, select an API version, target a connected account, edit a fixture, or provide raw/custom fixture content.

These fixtures are test recipes. For unsupported events, the implementation directs the user to perform the corresponding API or Dashboard action or write a custom fixture. The generated object shapes must not override canonical Stripe API documentation for fields, status transitions, or availability.

## Authentication, Modes, and Contexts

The CLI accepts explicit API keys and environment configuration and supports browser, interactive, non-interactive, and OAuth device-code login paths. OAuth tokens and active contexts are stored through the configuration/keyring layer, with refresh and revocation support.

Account and sandbox contexts can be listed and switched. The listener enforces consistency between the active context's mode and the `--live` flag. Organization-sandbox listening is explicitly unsupported in this baseline. Connected-account requests use `Stripe-Account`; V2 context uses `Stripe-Context`.

## Telemetry in `1.50.0`

The exact `1.50.0` release note contains one change: telemetry now captures the agent host and self-reported agent identifiers. Command telemetry also includes command context, selected flags, merchant/account context, machine UUID, user-agent data, and request identifiers in the retained implementation.

Telemetry and error reporting are bypassed when `STRIPE_CLI_TELEMETRY_OPTOUT` or `DO_NOT_TRACK` is interpreted as opted out. This is the only release-specific delta established by the `1.50.0` notes; the broader command behavior is an initial baseline, not functionality newly introduced in `1.50.0`.

## Version `1.50.1`: Authentication and Developer-Tool Changes

### OAuth Destination Checks

The new `ValidateAccessBaseURL` accepts only the exact strings `https://access.stripe.com` and `https://qa-access.stripe.com`. Variations with ports, paths, trailing slashes, query strings, or alternate hosts fail. Command setup validates the destination before OAuth refresh, and saved device-auth continuation validates its stored origin.

Access-service account, device/token, refresh, reauthentication, and revocation requests use a client whose redirect callback returns `http.ErrUseLastResponse`. Device verification and reauthentication browser URLs are checked before display/open: HTTPS and an exact production or QA access/dashboard host are required. This is host validation, not a browser-path allowlist; do not generalize it to every API or legacy login request. See [access-service checks](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/files/pkg/login/access_base.go), [device flow](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/files/pkg/login/oauth_device.go), and [reauthentication](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/files/pkg/login/oauth_reauth.go).

### New-Session Revocation

With an existing OAuth access token, `stripe login --new-session` now calls refresh-token revocation before starting the new login. If revocation fails, the command warns and continues; absent refresh-token/keyring evidence can also return without a network revocation. This is an attempt to retire the old CLI session, not guaranteed invalidation or merchant payment-token deletion. The flag already existed in `1.50.0`; the added behavior is the revocation attempt. See [login command](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/files/pkg/cmd/login.go) and [credential revocation](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/files/pkg/login/oauth_credentials.go).

### Credential Resolution and Errors

`Profile.ResolveCredentialsForAnyMode` retries using the active context's mode only after an `ActiveContextLivemodeMismatchError`. Plugin metadata/list callers retain their explicit API-key fallback on resolution error. This extracts behavior already present in the `1.50.0` plugin-private helper; it does not introduce mode-free payment requests. The listener and generic request commands still report mode mismatches. Many retained command, configuration, fixture, authentication, request, proxy, and WebSocket errors gain categories such as user input, authentication, API, network, filesystem, and internal errors. Trigger failure wrapping additionally preserves the underlying error with `%w`. See [profile helper](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/files/pkg/config/profile.go), [plugin callers](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/files/pkg/requests/plugin.go), and [trigger implementation](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/files/pkg/fixtures/triggers.go).

### Telemetry and Internal Transport

Telemetry now includes `agent_host_raw` alongside `agent_host_kind`, populated by `DetectAgentHost`. Existing opt-out semantics remain. The specific Codex TypeScript and Claude Desktop host mappings are release-note announcements because the host-detection implementation is outside this capsule. See [telemetry](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/files/pkg/stripe/analytics_telemetry.go).

HTTP Unix-socket paths now expand `~/`. WebSocket transport also expands that prefix and checks `HTTPS_PROXY`, then `https_proxy`. With only a Unix socket configured, WebSockets use it with TLS delegated to the proxy; with both configured, `*.dev.stripe.me` uses the socket while other hosts use HTTP CONNECT and TLS for `wss://`. Without a socket it retains environment-proxy routing. This supports internal development/listening paths, not a new checkout integration or proof that every proxy configuration works. See [HTTP transport](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/files/pkg/stripe/client.go) and [WebSocket transport](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/files/pkg/websocket/client.go).

### Announcements and Evidence Gaps

The release notes also announce a `stripe feedback` command, a `ResolveCredentials` CoreCLIHelper plugin RPC, and enforcement of categories for newly created errors. Command registration and retained helper/error-call-site changes corroborate parts of these announcements, but feedback payload/handling, the RPC contract/handler, the category implementation/analyzer, and exact agent-host mappings are outside the snapshot. Obtain an approved supplement at this SHA before answering their detailed behavior. No new merchant payment method or checkout lifecycle change is established by this tooling release.

### Grounding Excerpts for `1.50.1`

> "invalid access base URL: must be exactly https://access.stripe.com or https://qa-access.stripe.com"
>
> `raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/files/pkg/login/access_base.go:11`

> `return http.ErrUseLastResponse`
>
> `raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/files/pkg/login/access_base.go:35`

> "Revoke the previous OAuth session before starting a new one, same as `stripe logout`."
>
> `raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/files/pkg/cmd/login.go:184`

> ``AgentHostRaw      string `url:"agent_host_raw,omitempty"` ``
>
> `raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/files/pkg/stripe/analytics_telemetry.go:54`

## Version `1.50.2`: Profile Cleanup and Reauthorization

`stripe config --remove-profile <name>` now confirms before deletion. Non-interactive callers must provide `--confirm`. Removal supports legacy dotted names and incomplete profile tables; reserved top-level machine settings (including dotted descendants) are rejected. Auth-field cleanup also handles an explicitly named dotted profile. Active dotted profiles warn once per process and suggest logging in with a hyphenated name before removing the old profile. This is local configuration/keyring cleanup, not remote API-key revocation.

`stripe reauth` now polls authorized accounts every three seconds, for up to ten minutes, then prints the shared login/context summary when the signature changes. The signature compares sorted account IDs, names, and modes, not OAuth scopes. There is no dedicated completion signal: a browser reauthorization that leaves those values unchanged may time out. Cancellation and timeout print guidance and return nil, so exit success alone does not prove authorization completed.

Human-facing mode labels change from test to sandbox. The API mode value remains `test`, and `whoami` retains its stable `test_mode_key`/`live_mode_key` fields. Release notes also report GitHub Actions supply-chain hardening and upgrade-test retry/notification changes; those workflow files are outside the retained capsule.

**Grounding:** "Non-interactive runs must pass --confirm rather than silently proceeding." (`raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/cmd/config.go:101`); `reauthPollInterval = 3 * time.Second` and `reauthPollTimeout  = 10 * time.Minute` (`raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/login/oauth_reauth.go:23-24`); "displayMode maps the API's \"test\" mode value to the CLI's \"sandbox\" terminology." (`raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/login/oauth_accounts.go:113`).

See [profile removal](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/cmd/config.go), [configuration cleanup](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/config/config.go), [profile warning](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/config/profile.go), and [reauthorization](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/login/oauth_reauth.go).

## Version `1.50.3`: Plugin RPC Announcement

The release announces `ResolveCredentialsForAnyMode` as a plugin RPC. This is separate from the profile helper extracted in `1.50.1`. All 117 retained files match `1.50.2`; the four changed plugin handler/protocol files are outside capsule policy. An empty retained diff therefore does not mean an unchanged upstream repository. Obtain pinned supplemental evidence before answering RPC argument, response, authorization, or fallback details.

**Grounding:** "Add ResolveCredentialsForAnyMode plugin rpc (#1927)" (release notes line 2); `"version":"1.50.3"` and `"tag":"v1.50.3"` (release manifest line 1). [Release notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.3/2026-10-06/release-notes.md).

## Version `1.50.4`: OAuth Identity Output

OAuth `stripe whoami` fetches authorized contexts once and, for an active context, requests `/v1/stripecli/user_info` to show optional email and role. Identity-request errors are ignored; authorized-account retrieval errors still fail. Account names come from the fetched list, falling back to the account ID. The API-key JSON schema is unchanged, but the OAuth path returns before JSON formatting, including with `--format json`.

> [!warning] Contradiction
> The retained command help says no API calls are made and promotes stable JSON output. That is not true for this version's OAuth branch: it performs network calls and prints text. Do not use this help claim as a universal scripting guarantee.

Root registration corroborates a new provision command; the notes describe it as an alias for `stripe projects add`. Provision handling, agent-aware unstyled docs search, claimable-sandbox status and plugin hints are outside the capsule, so their detailed behavior remains note-only.

**Grounding:** "Fail open: the user's info is less important than the authorized contexts" (`pkg/cmd/whoami.go`, above `GetUserInfo`); "UserInfo is the response from GET /v1/stripecli/user_info." (`pkg/requests/user_info.go:13`); "PrintAuthorizedContextsList prints already-fetched authorized accounts as a" (`pkg/login/oauth_accounts.go:67`). Locations refer to the linked `2f3420a` snapshot.

[Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-2f3420a/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.4/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.4/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.3--1.50.4/comparison.md).

## Version `1.50.5`: Login Prompt and Agent Announcements

The OAuth device-login prompt now displays the authorization URL first, followed by a separated verification-code prompt, and adjusts the browser-opening text. The retained comparison changes presentation, not polling, token exchange, trusted browser validation or credential saving.

Release notes announce Codex-host categorization/agent-detection corrections and restored docs-navigation scroll positions. Their implementations in useragent/ANSI/docs are excluded; test changes in the comparison are not a substitute for implementation evidence. Exact detection rules and navigation behavior need a pinned supplement.

**Grounding:** "To authorize, visit %s" (`pkg/login/oauth_device.go`, login prompt); "When prompted, enter your verification code:" (same function); "Restore docs navigation scroll positions (#1926)" (release notes line 3). Code locations refer to the `f5f390b` snapshot.

[Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-f5f390b/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.5/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.5/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.4--1.50.5/comparison.md).

## Version `1.50.6`: OAuth JSON and Refresh Metadata

OAuth `whoami --format json` now serializes a dedicated OAuth output. It includes `authorized_accounts` and, when an active context exists, optional `display_name`, `account_id`, `mode`, `email`, `role` and Unix-seconds `expires_at`. Mode is `test`/`live` in JSON, while text renders test as sandbox. With no active context only authorized accounts are populated. It omits API-key fields such as `authenticated`, `profile_name`, API versions and key availability. Optional user-info lookup still fails open.

The JSON omission observed in `1.50.4` is resolved here, but help still incorrectly promises no network calls and universal key fields. Scripts must branch by auth context/schema rather than rely on those statements.

OAuth refresh now fills unset display name, account ID, user ID and device name from persisted profile data before CreateProfile rewrites it. Explicit in-memory values remain preferred. Plugin metadata adds `auto_install` (missing field defaults false) and optional `machine_uuid` for rollout selection; root wiring corroborates automatic-plugin invocation, not universal rollout availability. Installation/security handling and preview Data API guidance are outside the capsule.

**Grounding:** "Fields not surfaced in the text output (e.g. profile" (`pkg/cmd/whoami.go`, above `whoamiOAuthOutput`); "preserveProfileMetadata carries forward the display name, account ID, user" (`pkg/login/oauth_refresh.go`, helper comment); "AutoInstall reports whether the server wants this plugin installed on first" (`pkg/requests/plugin.go`, metadata comment). Locations refer to the `ba4ee1f` snapshot.

[Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-ba4ee1f/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.6/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.6/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.5--1.50.6/comparison.md).

## Version `1.50.7`: config v2 migration and base-URL hardening

### Additive full ingest and evidence boundary

The collector suggested delta, but the user approved additive **full** ingest because configuration layout and URL trust boundaries changed. Focused reading covered all 10 added/modified retained files, their comparison and affected prior code, and the cumulative wiki pages; 109 unchanged retained files and both snapshot inventories were verified mechanically. Earlier version knowledge remains intact. Release notes are unavailable; these are implementation findings, not invented release-note claims.

### Config v2, compatibility and credentials

- New `config_version = 2` stores profiles under `[profiles.<name>]`, leaving CLI settings at the root. Reads prefer a nonempty nested value and fall back to the flat layout; writes follow the existing layout. Common config writes refuse unsupported/unreadable schema versions, while initialization can warn and continue best-effort reads.
- `MigrateConfigFile` parses raw TOML to preserve case, recognizes profiles by known fields, keeps unrecognized settings, and fills missing nested fields from flat shadows without replacing existing nested values. It verifies an encoded plan, writes a `.v1.bak`, syncs a same-directory temporary file and renames it, then verifies the result. It attempts rollback on post-write verification failure; rollback itself can fail and reports the backup location. This is not proof of universal crash safety.
- Config paths change, but keyring item IDs remain `<profile>.<field>`; they do not acquire a `profiles.` prefix. Deletes clear both layouts. New empty/dotted names are rejected before profile creation/login mutation; existing profiles are grandfathered rather than automatically renamed.
- Retained `root.go` calls `migrateConfigIfNeeded`, but its implementation (`pkg/cmd/config_migration.go`) and `pkg/plugins/config_compat.go` are excluded. The library does not decide whether migration is safe for plugins. Do not infer when migration runs or exact plugin-blocking criteria.

> **Comment/implementation qualification:** `configFieldForWrite` still says this release line never migrates. That describes neither the new migration library nor the root call; only ordinary profile-write layout selection is established by that function.

### URL validation, switching and listen errors

- API/dashboard base URLs are parsed; userinfo, missing hosts and non-HTTP(S) schemes are rejected. Trusted exact defaults remain, dev hosts must have one allowed label before `.dev.stripe.me`, and IP loopback hosts are allowed only over HTTP. The HTTPS API `/v<digits>` branch validates hostname/path but does not universally forbid ports, queries or fragments. This is distinct from OAuth access-origin validation and from webhook forwarding destinations.
- `SwitchContext` returns `(*SwitchResult, error)`, with account and raw mode; display mode maps test to sandbox. Cancellation returns no result, so callers print active context only for an actual result. UAT preservation during profile recreation was already present in 1.50.6, not a new 1.50.7 feature.
- Listen-session authorization HTTP 429 is now categorized `RateLimit` rather than `API`. Retained evidence does not establish the excluded telemetry classifier's complete reporting behavior.

Implementation: [migration](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/files/pkg/config/migrate.go), [profile compatibility](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/files/pkg/config/profile.go), [config writes](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/files/pkg/config/config.go), [root wiring](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/files/pkg/cmd/root.go), [URL validation](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/files/pkg/stripe/url.go), [switch result](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/files/pkg/login/switch_context.go), [listen error](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/files/pkg/proxy/proxy.go).

**Grounding:** `const ConfigBackupSuffix = ".v1.bak"` ([migrate.go:20](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/files/pkg/config/migrate.go)); `const ConfigVersionV2 = 2` ([profile.go:111](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/files/pkg/config/profile.go)); "This same string is used verbatim as the keyring item ID for livemode" ([profile.go:546](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/files/pkg/config/profile.go)); `u.User != nil` ([url.go:42](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/files/pkg/stripe/url.go)).

[Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.7/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.7/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.6--1.50.7/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.6--1.50.7/comparison.json).

## Version `1.50.8`: plugin minimum-core-version errors

Release notes announce enforcement of `min_core_version` when installing a plugin. The retained request layer adds `PluginRequiresNewerCLI`: it unwraps `RequestError`, requires HTTP 400 and `plugin_requires_newer_cli`, and extracts `error.min_core_version` from a string JSON body. A matching error still returns `ok = true` with an empty minimum if the body is unavailable/malformed or omits the attribute. Other statuses/codes are not recognized. Existing metadata credential fallback, machine UUID and auto-install fields remain.

This identifies a compatibility failure, not a missing release. Actual installer/upgrade rejection, cached-metadata fallback prevention and version comparison live in excluded files; the release announcement does not establish those details. No checkout API migration is evidenced.

**Grounding:** `const ErrCodePluginRequiresNewerCLI = "plugin_requires_newer_cli"` (`pkg/requests/plugin.go`); "An answer that names" / "no minimum is still the same answer" (same file, helper comment); "Enforce min_core_version when installing a plugin (#1959)" (release notes line 2). Code locations refer to the linked `07050f2` snapshot.

[Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-07050f2/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.8/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.8/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.7--1.50.8/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.7--1.50.8/comparison.json).

## Version `1.50.9`: installation telemetry and docs announcements

`NewEventMetadata` now obtains `InstallMethod` from `installmethod.Detect(installmethod.OSEnv())` instead of `useragent.DetectInstallMethod` with three OS helpers. The existing `install_method` field, agent metadata, endpoint and opt-out predicate remain. The shared detector implementation is excluded, so this caller does not establish detection precedence or supported installation categories.

Release notes announce fixing/expanding installation detection, forwarding `Stripe-Context`/`Stripe-Livemode` in the docs client, printing an upgrade command when outdated, and restoring telemetry/root pre-run for docs commands. Docs, version and installation implementations are excluded: these are note-backed announcements, not audited header-routing, migration or update-execution contracts. No merchant checkout capability or checkout SDK migration is established.

[Telemetry implementation](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-6056ace/files/pkg/stripe/analytics_telemetry.go).

**Grounding:** `InstallMethod:   installmethod.Detect(installmethod.OSEnv()),` (`pkg/stripe/analytics_telemetry.go`, NewEventMetadata); "Forward Stripe-Context/Stripe-Livemode headers in docs client (#1986)" (release notes line 3); "Print the upgrade command when the CLI is out of date (#1975)" (release notes line 4). Locations refer to the linked `6056ace` snapshot/release.

[Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-6056ace/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.9/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.9/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.8--1.50.9/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.8--1.50.9/comparison.json).

## Version `1.50.10`: agent usage-report announcement

The release notes announce adding `stripe agent report_usage`, a telemetry command. All 119 retained files match `1.50.9`; the retained comparison is empty. The packet nevertheless classifies upstream changes to agent command registration/implementation/tests and release packaging as policy exclusions. This is a note-backed new command, not evidence that the entire repository is unchanged.

Exact flags, report payload, credential requirements, data destination, opt-out handling and retries cannot be inferred from the older telemetry code. Obtain an approved pinned supplement for those questions. Earlier webhook, fixture, authentication and telemetry implementation knowledge remains version-qualified and preserved.

**Grounding:** "Add stripe agent report_usage telemetry command" (release notes line 5); `"version":"1.50.10"` and `"tag":"v1.50.10"` (release manifest line 1).

[Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-150fa3f/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.10/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.10/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.9--1.50.10/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.9--1.50.10/comparison.json).

## Version `1.50.11`: login reauthorization and device completion

### Additive full scope

The user approved additive full ingest, overriding the collector's delta recommendation because existing-session login behavior changes. Focused reading covered all 10 added/modified retained files, the full comparison and affected prior code, plus cumulative source/changelog; 110 unchanged files and both inventories were hash-verified. Earlier history is preserved.

### Existing sessions and agent continuation

- In `1.50.10`, an OAuth token caused login to print identity/advice and return. In `1.50.11`, `sessionIsValid` accepts an unexpired access token or attempts refresh; a usable session initiates reauthorization. Missing/failed refresh falls through to fresh login. `--new-session` retains the prior revoke-attempt-and-warning behavior.
- Interactive reauthorization prints a best-effort email/context summary and asks Enter before opening the browser. Account/name lookup failures in that courtesy summary are ignored, not proof that subsequent authorization succeeds.
- `stripe login --non-interactive` with a usable OAuth session emits only `browser_url` and `next_step: stripe login --complete-reauth`. This differs from fresh-login JSON, which also includes `verification_code`. Agents must use the returned continuation rather than assume one fixed output shape.
- Initiation best-effort saves authorized accounts beside the credentials file as `pending_reauth_accounts.json` (requested file mode 0600, directory 0700). Completion first reads current accounts: a changed signature clears the saved baseline and prints a summary; without a baseline it prints current contexts immediately, not verified browser completion. With an unchanged baseline it polls every three seconds for ten minutes. The signature includes ID/name/sorted modes, **not scopes**, despite the helper comment referring to scopes. Cancel/timeout return nil; pending state is not cleared on those branches. This file is not scoped per profile/session in its path.
- Root still registers `newReauthCmd`; its excluded command implementation prevents claims about deprecation/alias details. The release's wording does not establish removal.

### Device-code completion and UX

New `RequestDeviceCodeForAccessBase`, `DeviceCodeLoginResult` and `PollAndSaveDeviceCredentials` share token polling, credential saving and account/context population. After token issuance, the helper uses `context.WithoutCancel` so caller cancellation/expiry does not interrupt those steps; this is not a transaction or guarantee that account lookup/storage cannot fail after token storage. Interactive and continuation callers handle SIGINT, stop spinners and return nil on cancellation. The interactive spinner starts after the browser-open attempt signals, or immediately when no signal is available. The continuation still clears device pending state whether polling succeeds or fails.

### Tooling and schema updates

Generated default headers change from `2026-07-29.dahlia` / `.preview` to `2026-08-26.dahlia` / `.preview`; this is an API-version selection change, not proof of every server-side schema difference. The preview thin-event allowlist adds seven `v2.core.approval_request.*` states and `v2.signals.account_evaluation.complete`. Event-name eligibility is not proof of general availability or event semantics.

README now documents removing plugins before the binary via `stripe plugin uninstall --all`, followed by platform-specific binary removal and optional configuration cleanup. It says binary uninstall preserves configuration. Plugin-uninstall implementation is excluded, so exact failure handling and remote revocation are not established.

Implementation: [login command](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c78e4ab/files/pkg/cmd/login.go), [reauthorization](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c78e4ab/files/pkg/login/oauth_reauth.go), [pending state](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c78e4ab/files/pkg/login/oauth_pending.go), [device helper](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c78e4ab/files/pkg/login/oauth_device.go), [device continuation](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c78e4ab/files/pkg/login/login.go), [spinner](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c78e4ab/files/pkg/login/spinner.go), [API defaults](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c78e4ab/files/pkg/requests/stripe_version_header.go), [event names](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c78e4ab/files/pkg/proxy/events_list.go), [uninstall guidance](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c78e4ab/files/README.md).

**Grounding:** `NextStep:   "stripe login --complete-reauth",` ([oauth_reauth.go:101](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c78e4ab/files/pkg/login/oauth_reauth.go)); `ctx = context.WithoutCancel(ctx)` ([oauth_device.go:206](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c78e4ab/files/pkg/login/oauth_device.go)); `const StripeVersionHeaderValue = "2026-08-26.dahlia"` ([stripe_version_header.go:6](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c78e4ab/files/pkg/requests/stripe_version_header.go)); "Package managers only remove the `stripe` binary; they leave installed plugins behind." ([README.md:223](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c78e4ab/files/README.md)).

[Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c78e4ab/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.11/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.11/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.10--1.50.11/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.10--1.50.11/comparison.json).

## Version `1.51.0`: explicit webhook subscriptions and account switching

### Additive full scope and listener migration

User-approved additive full ingest overrides the collector's delta recommendation because public command/forwarding behavior changes. Focused reading covers all 22 modified retained files, affected prior code, full comparison and cumulative source/changelog. Both inventories and 98 unchanged retained files are hash-verified; earlier knowledge remains intact.

- `--events` now accepts snapshot and thin names together; the local classifier treats names beginning `^v\d+\.` as thin. `--all-snapshot` and `--all-thin` select their respective wildcards. Explicit `--events '*'` is rejected.
- Bare `stripe listen` subscribes to both channels without forwarding. Providing `--forward-to` or `--forward-connect-to` requires explicit event selection, including a qualifying deprecated thin flag. The corresponding snapshot/thin destinations cannot be identical when both styles are selected. `--print-secret` bypasses forwarding validation, but still validates event and source flags. These checks occur at the listener handler's start; root pre-run may already have run.
- `--events-from` defaults to `all`; `@self` excludes connected-account events, `@accounts` excludes self events. Filtering happens locally after acknowledgement and before printing/forwarding, using nonempty snapshot `account` or thin `context`; it is not server-side permission isolation.
- `--thin-events`, `--forward-thin-to`, and `--forward-thin-connect-to` are deprecated but functional. Legacy invocation can retain all-snapshot subscription and separate thin destinations. Using legacy `--thin-events` with only `--forward-to` warns that thin events are printed, not forwarded there.
- Configured endpoint loading now propagates API/JSON failures instead of misreporting them as an empty endpoint list. The non-client `WebhookEndpointsList` helper still swallows errors; do not generalize the fix to every caller.

Version-qualified examples, not executed integration tests:

```sh
# Select checkout snapshot events explicitly
stripe listen --events checkout.session.completed --forward-to localhost:4242/webhook
# All snapshot events
stripe listen --all-snapshot --forward-to localhost:4242/webhook
# Thin events from connected accounts
stripe listen --all-thin --events-from @accounts --forward-to localhost:4242/thin
```

Implementation: [listener](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/pkg/cmd/listen.go), [proxy/routes](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/pkg/proxy/proxy.go), [local filtering](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/pkg/proxy/webhook_event_processor.go), [snapshot identity](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/pkg/proxy/stripeevent.go), [thin identity](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/pkg/proxy/v2_stripe_event.go), [endpoint requests](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/pkg/requests/webhook_endpoints.go).

### Contexts, identity and permission errors

`stripe switch [account_id]` becomes preferred; `stripe switch context` remains a hidden alias. JSON output requires an account ID and contains `account_id`, `display_name`, and raw `mode` (`test`/`live`, not display wording sandbox). Cancellation returns no result. `stripe login switch` retains its separate API-key profile fallback; do not assume every switch spelling has identical flags or fallback.

OAuth `whoami` calls extracted `RefreshUATIfNeeded` before fetching accounts. Stored expiry under 60 seconds triggers a serialized, rechecked refresh; missing/unreadable expiry or an absent refresher skips it, while refresh failure propagates. Credential resolution previously contained this refresh logic; its extraction is not newly introduced automatic refresh for all API requests. OAuth and API-key JSON remain distinct. New help removes the historical no-network and universal key-schema assertions, resolving that wording contradiction without erasing the older warning. Optional identity lookup still fails open.

The request layer recognizes HTTP 403 plus `more_permissions_required`, retains the server message and records whether credentials have a nonempty OAK context. Root prints role-reassignment guidance for contextual OAuth, otherwise the server message; listener authorization errors preserve wrapped causes. The excluded stripeauth implementation prevents auditing its classification fully. `Credentials.IsOAK` uses nonnil OAKLivemode, a different predicate from HasOAKContext.

Implementation: [switch](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/pkg/cmd/switch.go), [context storage](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/pkg/login/switch_context.go), [login alias](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/pkg/cmd/login.go), [whoami](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/pkg/cmd/whoami.go), [expiry helper](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/pkg/config/profile.go), [request errors](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/pkg/requests/base.go), [root handling](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/pkg/cmd/root.go), [credential predicate](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/pkg/stripe/client.go).

### Removed-command announcement and tooling boundaries

Notes announce removal of unused commands; README no longer lists samples, serve or status. Root still registers new samples/serve/status constructors and recognizes `errCommandRemoved` to suppress duplicate shim guidance before exiting nonzero. Thus this is not proof those names vanished from routing. Shim definitions are excluded; exact downgrade guidance and fallback behavior require supplemental evidence.

Plugin update configuration defaults off. A present per-plugin value overrides global configuration, including invalid/non-on values that disable updates; only exact `on` enables. Download/auto-upgrade implementation is excluded. Main/root now share telemetry metadata with context-aware panic/error reporting; opt-outs remain at main's entry, but excluded reporting/sanitization implementations prevent claims about exact payload or redaction. go.mod removes several Git/serve-related dependencies and adds indirect gomega/x/exp; no new Go minimum is established by the diff. Codex marketplace detection/fallback remains a release-note announcement with excluded implementation.

See [README](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/README.md), [plugin toggle](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/pkg/config/plugin_configs.go), [main telemetry wiring](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/cmd/stripe/main.go), [module dependencies](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/go.mod).

> [!warning] Contradiction
> The earlier API Requests summary said OAuth refresh retries once. The baseline, prior and 1.51.0 implementation recursively call performRequest without an explicit one-retry guard when the same eligible unauthorized response repeats. Treat one-retry wording as an unsupported bound, not a new 1.51.0 regression; do not infer safe business-operation replay. See [request implementation](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/pkg/requests/base.go) and [[stripe-cli]].

**Grounding:** "must specify events to forward using --events, --all-snapshot, or --all-thin" ([listen.go:625](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/pkg/cmd/listen.go)); `AccountID   string` ([switch.go:28](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/pkg/cmd/switch.go)); `func RefreshUATIfNeeded(p *Profile, uat string) (string, error) {` ([profile.go:1024](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/pkg/config/profile.go)); `return rb.performRequest(ctx, client, path, params, data, errOnStatus, additionalConfigure)` ([base.go:392](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/files/pkg/requests/base.go)).

[Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.51.0/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.51.0/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.11--1.51.0/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.11--1.51.0/comparison.json).

## Version `1.51.1`: resumable device login and config collision fixes

### Additive full scope

User-approved additive full ingest overrides the collector's delta recommendation because persisted login continuation changes. Focused reading covers all five changed retained files, affected prior code, full comparison and cumulative pages; 115 unchanged files and inventories are hash-verified. Earlier findings remain intact. The release-note file contains only a generated-notes comment, so these are implementation findings.

### Reusable helpers versus CLI invocation

- `InitiateOAuthLogin` resumes a still-valid pending device code for the same access origin; `FindPendingOAuthLogin` only discovers one, returning no session for missing/unreadable, mismatched or expired state. The ordinary `stripe login --non-interactive` OAuth path still always mints a fresh code and overwrites pending state.
- `PollPendingOAuthLogin` validates the stored access origin and uses the persisted absolute deadline. Caller cancellation/timeout before that deadline returns no result/no error and keeps pending state. Expiry, success and other errors clear it. This improves on `1.51.0`'s unconditional cleanup, but is not a universal transient-error retry guarantee.
- `CheckPendingOAuthLogin` makes one token request with no polling sleep/loop. Pending/slow-down responses return no result/no error and preserve state; all other errors clear it, including network/cancellation errors. Token issuance is followed by cancellation-detached credential/account saving; saving failure clears the consumed code. A single check is not network-free or zero-latency, and callers must schedule retries themselves.
- `ListAuthorizedAccountsForActiveSession` checks the stored UAT's OAuth prefix, fetches accounts and attaches optional active context. It does not itself refresh or validate the supplied access origin. The retained helpers do not establish the excluded plugin handler/protocol's full RPC contract.

### Persistence and upgrade boundary

Pending state now includes browser URL, user code and `issued_at`. Its local deadline is issued-at plus the greater of server expires-in and ten minutes. The ten-minute floor is not proof that the server accepts a code longer than its advertised expiry. Older pending JSON decodes missing issued-at to Go zero time, so it is treated as expired; start a new non-interactive login after upgrading mid-flow.

Device pending state uses a same-directory temporary write, mode 0600 and rename, with directory creation requesting 0700. No file/directory sync or cross-process lock is present: do not infer crash durability or coordinated writers. A competing fresh login can replace another caller's pending code. Reauthorization pending storage is separate and is not changed to this atomic-write path.

### Config migration corrections

Tables containing recognized profile fields can migrate even when their name matches a reserved setting key; only the profiles container is exempt. Actual setting tables without profile fields remain at the root. `StampNewConfigFile` writes an empty v2 document after a nonexistence check, but its write uses create/truncate rather than exclusive creation, so this is not a race-proof refusal guarantee. Automatic stamping/migration orchestration and plugin-update changes are excluded; their exact invocation/failure rules remain evidence gaps.

Implementation: [login helpers](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/files/pkg/login/login.go), [token check/save](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/files/pkg/login/oauth_device.go), [pending persistence](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/files/pkg/login/oauth_pending.go), [account helper](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/files/pkg/login/oauth_accounts.go), [migration](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/files/pkg/config/migrate.go).

**Grounding:** `IssuedAt        time.Time` ([oauth_pending.go:26](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/files/pkg/login/oauth_pending.go)); `return c.IssuedAt.Add(max(time.Duration(c.ExpiresIn)*time.Second, 10*time.Minute))` ([oauth_pending.go:33](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/files/pkg/login/oauth_pending.go)); `func CheckPendingOAuthLogin(ctx context.Context, cfg *config.Config) (*DeviceCodeLoginResult, error) {` ([login.go:291](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/files/pkg/login/login.go)); `func StampNewConfigFile(path string) error {` ([migrate.go:498](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/files/pkg/config/migrate.go)).

[Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.51.1/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.51.1/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.51.0--1.51.1/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.51.0--1.51.1/comparison.json).

## Version `1.52.0`: automatic CLI update wiring and plugin rollout metadata

### Additive full scope

User-approved additive full ingest covers the new executable-update lifecycle with focused reading: all three changed retained files, affected prior code, complete comparison and cumulative pages; inventories and 117 unchanged files are hash-verified. Older history remains intact.

### Core update lifecycle and evidence limits

Release notes announce automatic updates for CLIs installed by the install script, bounded downloads, refusal to stage unverifiable artifacts, and reporting of update checks/failures. Retained `main.go` calls `autoupdate.ApplyIfPending()` before its own command/telemetry setup and defers `autoupdate.CheckForUpdate()`. This deferral runs on normal-return branches, including telemetry opt-out and invalid-semver branches; `cmd.Execute` calls `os.Exit(1)` on command failure, bypassing the defer.

The entrypoint corroborates automatic-update wiring, not the internals. Eligibility, update opt-out, cadence, download destination/limits, artifact verification, replacement/re-execution, failure recovery and update telemetry payload are outside the capsule. Do not infer that DO_NOT_TRACK or the existing command-telemetry opt-out disables update checks: those hooks are outside the branch. The comment's claim that networking never delays a command describes intended ordering, not proof that process exit incurs no latency.

### Plugin and agent announcements

`GetPluginMetadata` drops its machineUUID argument, associated debug field and optional machine_uuid request parameter. This resolves the older version's rollout-identifier description prospectively, not historically. `PluginMetadata.AutoInstall` and its absent-field false default remain. Root agent guidance now says run a plugin command directly to install rather than to be prompted. The excluded hint/installer/upgrade code prevents claiming universal unattended installation or its approval/error safeguards from this help text.

Notes also announce Grok support in `stripe agent setup`; provider/setup implementation is excluded, so exact setup flags, credential storage and endpoint behavior need pinned supplemental evidence. No new merchant checkout/payment-method capability is established.

Implementation: [entrypoint](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a5d9d6/files/cmd/stripe/main.go), [root command/error exits](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a5d9d6/files/pkg/cmd/root.go), [plugin metadata](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a5d9d6/files/pkg/requests/plugin.go).

**Grounding:** `autoupdate.ApplyIfPending()` (cmd/stripe/main.go:24); `defer autoupdate.CheckForUpdate()` (cmd/stripe/main.go:30); `os.Exit(1)` (pkg/cmd/root.go, Execute error branch); "Bound the update download, and refuse to stage what we cannot verify (#2070)" (release notes:6). Code locations refer to the linked `4a5d9d6` snapshot.

[Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a5d9d6/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.52.0/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.52.0/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.51.1--1.52.0/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.51.1--1.52.0/comparison.json).

## Version `1.52.1`: custom request headers and Endive API defaults

### Request-header support and precedence

Shared request commands add repeatable `--request-header` / `-H`, and `RequestParameters.AppendHeaders` supports programmatic callers. Parsing splits at the first colon, rejects missing separators, empty/invalid token names and CR/LF values, trims surrounding spaces/tabs from values and canonicalizes names. Repeated names use the last value rather than multiple values; additional colons remain in the value.

Custom headers are applied after generated credential, account/context, mode, API-version and idempotency headers. They can override those headers: no protected-name denylist is present. An additional-configure callback runs afterwards; multipart configuration can still replace Content-Type. This is request customization, not a server-permission bypass or a new payment capability.

`--show-headers` adds custom names to printable headers. The verbose redactor masks Basic/Bearer-shaped values, not arbitrary secrets by header name. Dry-run output overlays custom values after ordinary credential redaction, including a custom Authorization value without further redaction. Do not put secrets in examples or share unreviewed verbose/dry-run output. Dry run does not execute the payment request; it is not proof that the server accepts a custom header.

Illustrative, not executed:
```sh
stripe get /v1/customers --request-header 'X-Integration-Variant: pilot' --dry-run
```

### API defaults and event eligibility

Generated defaults advance from `2026-08-26.dahlia` / `.preview` to `2026-09-30.endive` / `.preview`. The retained selection helper uses explicit --stripe-version first, then the preview default for preview commands, then the stable default for V2 paths; ordinary V1 paths do not automatically receive this stable header. The OpenAPI and generated resource bodies are excluded, so this is not a full schema migration analysis.

The snapshot event allowlist adds apps.install created/deleted/updated. The thin list expands V1-prefixed names, including `v1.checkout.session.completed`, PaymentIntent, invoice and subscription events. Two preview signal names are added for fraudulent merchant/website readiness. These lists establish CLI name eligibility, not production event availability, payload schemas or lifecycle semantics; snapshot `checkout.session.completed` and thin `v1.checkout.session.completed` are distinct names.

### Plugin defaults and configuration

`PluginMetadata` adds `auto_update_default` (absent field false). The decision helper now selects per-plugin setting, then global setting, then supplied default; an invalid but present local value disables updates and still overrides the backend default. This supersedes the `1.51.0` helper's unconditional default-off rule without erasing that history. Actual backend rollout, update installer and auto-update command implementation are excluded.

`DeleteConfigField` lowercases the full key path, leaves an unset field/file untouched, otherwise removes the field and persists/reloads configuration. InitConfig removes the repeated chmod call; configured write permissions remain 0600, but initialization no longer universally repairs existing file permissions. Notes also announce holding an upgrade notice until a release is one day old; the excluded version helper prevents auditing timing details.

Evidence: [request implementation](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/files/pkg/requests/base.go), [client header ordering](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/files/pkg/stripe/client.go), [verbose redaction](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/files/pkg/stripe/verbosetransport.go), [API defaults](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/files/pkg/requests/stripe_version_header.go), [events](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/files/pkg/proxy/events_list.go), [plugin decision](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/files/pkg/config/plugin_configs.go), [metadata](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/files/pkg/requests/plugin.go), [configuration](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/files/pkg/config/config.go).

**Grounding:** "Set a custom request header (format: name: value)" ([base.go:223](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/files/pkg/requests/base.go)); `headers[name] = values[len(values)-1]` ([base.go:549](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/files/pkg/requests/base.go)); `return defaultEnabled` ([plugin_configs.go:67](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/files/pkg/config/plugin_configs.go)); `const StripeVersionHeaderValue = "2026-09-30.endive"` ([stripe_version_header.go:6](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/files/pkg/requests/stripe_version_header.go)).

[Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.52.1/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.52.1/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.52.0--1.52.1/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.52.0--1.52.1/comparison.json).

## Version `1.52.2`: OAuth Code Prefilling and Fixture Guidance

This focused delta fully reads five changed retained files and affected prior code; 115 unchanged files and inventories are checked mechanically. Earlier version knowledge remains intact.

### OAuth Browser URLs

Device responses now accept `verification_uri_complete`. `BrowserURL()` prefers that server-provided URL, otherwise `verification_uri`; the CLI does not construct the prefilled URL itself. Fresh interactive and non-interactive login validate the selected HTTPS access/dashboard destination before display, opening or persistence. Invalid nonempty complete URLs fail validation rather than silently falling back. The existing host check permits query strings and is not a path allowlist. Interactive prompts still expose a verification code as a fallback; JSON `browser_url` can now contain the complete URL without changing the response field names.

Pending state preserves the complete URI and continuation prefers it. Valid older pending sessions without that field fall back to their original URI; the earlier issued_at/expiry requirements still apply. Token polling, credential scope, cleanup/cancellation and the local expiry floor are unchanged. This is easier CLI authentication, not automatic authorization or a new payment capability. See [device flow](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-eea8a71/files/pkg/login/oauth_device.go), [interactive login](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-eea8a71/files/pkg/login/login.go), [pending sessions](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-eea8a71/files/pkg/login/oauth_pending.go), and [destination validation](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-eea8a71/files/pkg/login/access_base.go).

### Fixture and Flag Handling

An unexpected HTTP 400 from POST `/v1/accounts` now receives fixture-specific guidance: use an account with Accounts v1 creation support or a custom Accounts v2 fixture. The original error remains wrapped. Every matching 400 receives this guidance; the implementation does not inspect the provider error code to prove that Accounts v1 creation was disabled. Expected-error matches bypass this wrapper. There is no automatic migration, retry or eligibility proof. See [fixtures](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-eea8a71/files/pkg/fixtures/fixtures.go).

The root calls `resource.NormalizeBooleanRequestArgs` before normal command execution (after the map-output early return). Notes announce `--confirm` and boolean resource-flag fixes, but the normalization helper/templates are excluded: exact accepted syntax and coercion remain evidence gaps. The OpenAPI update is also note-backed with excluded schema files; retained default API-version headers remain those introduced in 1.52.1. See [root wiring](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-eea8a71/files/pkg/cmd/root.go).

**Grounding:** `VerificationURIComplete string` (`raw/github/stripe/stripe-cli/snapshots/2026-10-06-eea8a71/files/pkg/login/oauth_device.go:54`); `return r.VerificationURIComplete` (same file, line 65); `return nil, fixtureRequestError(data, err)` (`raw/github/stripe/stripe-cli/snapshots/2026-10-06-eea8a71/files/pkg/fixtures/fixtures.go:312`); `resource.NormalizeBooleanRequestArgs(rootCmd, args)` (`raw/github/stripe/stripe-cli/snapshots/2026-10-06-eea8a71/files/pkg/cmd/root.go:189`).

[Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-eea8a71/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.52.2/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.52.2/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.52.1--1.52.2/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.52.1--1.52.2/comparison.json).

## Version `1.53.0`: Version Release-Notes Command Announcement

The release notes announce `stripe version --notes`. All 120 retained files are hash-identical to 1.52.2, and the retained comparison patch is empty. The ingest packet separately classifies four changed upstream paths: `pkg/cmd/version.go`, its test, `pkg/version/version.go`, and its test, all intentionally outside capsule policy. The comparison's empty upstream-change list must therefore not be interpreted as a whole-repository no-change result.

This focused delta records the release announcement and identity without attributing new behavior to unchanged checkout/authentication/request code. Obtain an approved exact-SHA supplement before answering the notes command's output format, release selection, fetching, errors, caching or network behavior. Prior API-version defaults, login/fixture behavior, custom-header caveats and historical knowledge remain preserved. The command announcement alone establishes no merchant-facing payment integration change.

**Grounding:** "Add stripe version --notes (#2109)" (`raw/github/stripe/stripe-cli/releases/stripe-cli/1.53.0/2026-10-06/release-notes.md:5`); `"version":"1.53.0"` and `"tag":"v1.53.0"` (`raw/github/stripe/stripe-cli/releases/stripe-cli/1.53.0/2026-10-06/manifest.json:1`).

[Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-a915fc6/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.53.0/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.53.0/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.52.2--1.53.0/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.52.2--1.53.0/comparison.json).

## Related
> [!warning] Contradiction
> In `1.50.11`, the reauthorization comment mentions scope changes, but `accountsSignature` compares only ID, name and modes. Scope-only reauthorization is not a reliable completion signal. See [[stripe-cli]].


- Company: [[stripe]]
- Concept: [[stripe-cli]]
- History: [[changelog-github-stripe-cli]]

## Raw Sources

- [1.53.0 snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-a915fc6/manifest.json)
- [1.53.0 notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.53.0/2026-10-06/release-notes.md)

- [1.52.2 snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-eea8a71/manifest.json)
- [1.52.2 notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.52.2/2026-10-06/release-notes.md)

- [1.52.1 snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/manifest.json)
- [1.52.1 notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.52.1/2026-10-06/release-notes.md)

- [1.52.0 snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a5d9d6/manifest.json)
- [1.52.0 notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.52.0/2026-10-06/release-notes.md)

- [1.51.1 snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/manifest.json)
- [1.51.1 notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.51.1/2026-10-06/release-notes.md)

- [1.51.0 snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/manifest.json)
- [1.51.0 notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.51.0/2026-10-06/release-notes.md)

- [1.50.11 snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c78e4ab/manifest.json)
- [1.50.11 notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.11/2026-10-06/release-notes.md)

- [1.50.10 snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-150fa3f/manifest.json)
- [1.50.10 notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.10/2026-10-06/release-notes.md)

- [1.50.9 snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-6056ace/manifest.json)
- [1.50.9 notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.9/2026-10-06/release-notes.md)

- [1.50.8 snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-07050f2/manifest.json)
- [1.50.8 notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.8/2026-10-06/release-notes.md)

- [1.50.7 snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/manifest.json)
- [1.50.7 notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.7/2026-10-06/release-notes.md)

- [1.50.6 snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-ba4ee1f/manifest.json)
- [1.50.6 notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.6/2026-10-06/release-notes.md)

- [1.50.5 snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-f5f390b/manifest.json)
- [1.50.5 notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.5/2026-10-06/release-notes.md)

- [1.50.4 snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-2f3420a/manifest.json)
- [1.50.4 notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.4/2026-10-06/release-notes.md)

- [1.50.3 snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-53f08e9/manifest.json) - unchanged retained capsule; note-only plugin update
- [1.50.3 release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.3/2026-10-06/manifest.json)
- [1.50.3 notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.3/2026-10-06/release-notes.md)

- [1.50.2 snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/manifest.json) - focused delta; prior knowledge retained
- [1.50.2 notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.2/2026-10-06/release-notes.md)

- [1.50.1 snapshot manifest](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/manifest.json) - exact-SHA inventory; focused-reading exception above
- [1.50.1 release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.1/2026-10-06/manifest.json) - package-qualified identity
- [1.50.1 release notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.1/2026-10-06/release-notes.md) - upstream announcements, with gaps qualified above
- [1.50.0 to 1.50.1 comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.0--1.50.1/comparison.md) - retained changes and collection-policy omissions
- [Snapshot manifest](../../../../raw/github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/manifest.json) — exact-SHA capsule inventory and hashes
- [Release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.0/2026-08-14/manifest.json) — package-qualified tag, SHA, and release date
- [Release notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.0/2026-08-14/release-notes.md) — exact `1.50.0` telemetry change
- [Architecture](../../../../raw/github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/files/ARCHITECTURE.md) — command and request architecture
- [README](../../../../raw/github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/files/README.md) — supported workflows and installation
- [Listen command](../../../../raw/github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/files/pkg/cmd/listen.go) — event selection, forwarding, modes, and output
- [Fixture command](../../../../raw/github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/files/pkg/cmd/fixtures.go) — fixture controls and execution entrypoint
- [Trigger implementation](../../../../raw/github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/files/pkg/fixtures/triggers.go) — supported-event routing and custom-fixture fallback
- [Request layer](../../../../raw/github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/files/pkg/requests/base.go) — parameters, headers, dry run, errors, and OAuth retry
- [Stripe HTTP client](../../../../raw/github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/files/pkg/stripe/client.go) — HTTP construction and transport
- [Proxy implementation](../../../../raw/github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/files/pkg/proxy/proxy.go) — listener session and event proxy
- [Webhook forwarding](../../../../raw/github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/files/pkg/proxy/endpoint.go) — local endpoint delivery
- [Login command](../../../../raw/github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/files/pkg/cmd/login.go) — interactive and agent-oriented authentication paths
- [Telemetry](../../../../raw/github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/files/pkg/stripe/analytics_telemetry.go) — metadata, transport, and opt-out behavior
