---
title: "GitHub: stripe/stripe-cli"
type: source
date_ingested: 2026-08-14
date_updated: 2026-08-14
original_format: github-repo
raw_files:
  - "github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/manifest.json"
tags: [stripe, stripe-cli, developer-tools, webhooks, fixtures, api-testing, github-repository]
---

## Overview

`stripe/stripe-cli` is Stripe's Go command-line tool for building, testing, and managing integrations. This initial full ingest records package-qualified release `stripe-cli@1.50.0`, exact SHA `a6f40658b99e4142fd63b2e4b560aa9c7ae337b1`, collected on 2026-08-14.

Repository: <https://github.com/stripe/stripe-cli>

## Evidence Boundary

- Findings apply to the retained `stripe-cli@1.50.0` capsule, not an unqualified latest CLI.
- The capsule focuses on checkout-relevant command, authentication, fixture, request, proxy, RPC, telemetry, and WebSocket code. It does not represent the complete upstream tree.
- This first immutable snapshot retains 28 Go test files as an approved one-time collection superset. The corrected future capsule policy excludes Go tests.
- Embedded trigger fixtures demonstrate how the CLI generates test events. They do not independently establish canonical API lifecycle, production availability, or merchant eligibility.
- The CLI is development and operations tooling. A successful local forward or synthetic trigger does not prove production fulfillment correctness.

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

OAuth-backed requests that receive the repository's specific unauthorized response can refresh credentials and retry once. That narrow authentication retry must not be generalized into a guarantee that failed payment or business operations are automatically retried.

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

## Related

- Company: [[stripe]]
- Concept: [[stripe-cli]]
- History: [[changelog-github-stripe-cli]]

## Raw Sources

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
