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
- The retained source capsule is version-qualified to `stripe-cli@1.50.0`; future behavior requires its cumulative source and changelog.
- Version `1.50.0` adds agent host and self-reported agent identifiers to telemetry. Users can opt out through `STRIPE_CLI_TELEMETRY_OPTOUT` or `DO_NOT_TRACK`.

## Related

- Company: [[stripe]]
- Source: [[source-github-stripe-cli]]
- History: [[changelog-github-stripe-cli]]
