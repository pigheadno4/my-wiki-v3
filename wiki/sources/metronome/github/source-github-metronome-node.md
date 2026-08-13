---
title: "GitHub: Metronome-Industries/metronome-node"
type: source
date_ingested: 2026-08-12
original_format: github-repo
raw_files:
  - "github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/manifest.json"
tags: [metronome, node-js, typescript, server-sdk, usage-billing, contracts, webhooks, github-repository]
---

## Overview

`Metronome-Industries/metronome-node` publishes `@metronome/sdk`, Metronome's official server-side TypeScript and JavaScript client. This baseline covers `@metronome/sdk@3.10.0` at exact SHA `f8ac11210fbca9616a220e82ea82ac1d340ea2df`, released on 2026-07-23.

Repository: <https://github.com/Metronome-Industries/metronome-node>

## Evidence Boundary

- This source proves the package exports, generated request and response types, client behavior, and API methods present at the exact release. It does not independently prove account enablement, feature-flag access, service behavior, or current REST availability.
- The repository is generated from Metronome's OpenAPI description by Stainless. Dedicated Metronome documentation remains authoritative for product lifecycle, limits, eligibility, and operational guidance.
- The retained capsule includes the complete `src` tree plus repository documentation and release history, but excludes tests and fixtures under the approved capsule policy.
- `api.md` still lists a top-level Payments resource even though `src/resources` contains no Payments implementation and the changelog says deprecated `/payments/*` endpoints were removed in `3.7.0`. Do not use that stale index entry as evidence that those methods exist in `3.10.0`.
- This page describes the cumulative implementation present in `3.10.0`. Only the section explicitly labeled `3.10.0` attributes changes to that release.

## Grounding Excerpts

> "This library provides convenient access to the Metronome REST API from server-side TypeScript or JavaScript."
>
> `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/files/README.md:3`

> "Certain errors will be automatically retried 2 times by default, with a short exponential backoff."
>
> `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/files/README.md:113`

> "The main changes are that the SDK now relies on the builtin Web fetch API instead of node-fetch and has zero dependencies."
>
> `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/files/MIGRATION.md:5`

> "Webhook body must be passed as the raw JSON string sent from the server (do not parse it first)."
>
> `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/files/src/resources/webhooks.ts:94-96`

> "Note that React Native is not supported at this time."
>
> `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/files/README.md:421`

## Package and Runtime Shape

The CommonJS package exports both ESM and CommonJS builds and has no runtime dependencies. It requires TypeScript 4.9 or later and documents support for Node.js 20 LTS or later, current browsers, Deno, Bun, Cloudflare Workers, Vercel Edge Runtime, Jest's Node environment, and Nitro. React Native and Jest `jsdom` are explicitly unsupported in this release.

Authentication defaults to `METRONOME_BEARER_TOKEN`; construction fails when no bearer token is supplied. `METRONOME_BASE_URL`, `METRONOME_WEBHOOK_SECRET`, and `METRONOME_LOG` can configure the base URL, webhook helper, and log level. The default API base URL is `https://api.metronome.com`.

The package includes a `metronome-sdk migrate` command for the earlier migration to the built-in Web Fetch API. The migration guide records Node 20, TypeScript 4.9, and Jest 28 minimums, named path-parameter changes, automatic URI encoding, object-wrapped method parameters, `fetchOptions` replacing `httpAgent`, public export moves, and simplified manual pagination.

## Requests, Errors, and Pagination

The client defaults to a one-minute per-attempt timeout and two retries. It retries connection and timeout failures plus HTTP 408, 409, 429, and `5xx` responses, while the nonstandard `x-should-retry` header can force or suppress a retry. Backoff honors `retry-after-ms` or `Retry-After` before falling back to exponential delay. Callers can override retries and timeout globally or per request.

HTTP failures map to typed error classes for 400, 401, 403, 404, 409, 422, 429, and `5xx`, with separate connection, timeout, and user-abort errors. Debug logging includes request and response headers and bodies; authentication headers are redacted, but sensitive body content may still be logged.

Cursor, body-cursor, and cursor-without-limit page types support async iteration and manual `hasNextPage()`, `getNextPage()`, and `nextPageRequestOptions()` flows. Every generated API promise also supports `.asResponse()` for an unconsumed raw response and `.withResponse()` for parsed data plus the underlying response.

The generic `get`, `post`, `put`, `patch`, and `delete` methods can call undocumented endpoints. Extra typed request fields are sent without runtime schema validation, and extra response fields are not stripped; this flexibility is not evidence that an undocumented operation is supported.

## API Surface at `3.10.0`

The generated client exposes V1 resources for alerts, plans, credit grants, pricing units, customers, dashboards, usage, audit logs, custom fields, billable metrics, services, invoices, contracts, packages, and settings. Nested resources cover customer alerts, plans, invoices, billing configuration, commits, credits, and named schedules, plus contract products, rate cards, rates, product ordering, and named schedules.

The V2 surface is contract-focused: retrieve and list contracts, make broad contract edits, edit one commit or credit, and retrieve edit history. The shared type layer carries contracts, subscriptions, commits, credits, rates, overrides, scheduled charges, thresholds, payment gates, hierarchy controls, and usage filters.

This is a broad generated API contract, not a guarantee that every field is enabled for every account. Several docstrings explicitly describe configuration-dependent or beta fields.

## Usage Ingestion

`client.v1.usage.ingest({ usage: [...] })` sends usage events to `POST /v1/ingest`. Each typed event requires `customer_id`, `event_type`, RFC 3339 `timestamp`, and `transaction_id`; `properties` is optional. The same resource lists aggregated usage, grouped usage, and raw-event search results.

The generated method documentation repeats a 34-day backdating and duplicate-detection window and an advertised 100,000-events-per-second capability. Dedicated event-ingestion sources remain authoritative for batch size, account limits, partial-ingest recovery, and producer retry policy.

Because the generic SDK retry policy includes HTTP 409 and server failures, integrations should retain deterministic transaction IDs and reconcile the endpoint-specific idempotency rules rather than assuming every retried mutation is safe.

## Contracts, Pricing, and Balances

The SDK supplies both legacy V1 contract methods and the V2 edit model. V1 includes create, retrieve, list, amend, archive, historical-invoice creation, balance and seat-balance retrieval, subscription history, rate schedules, usage filters, professional-services invoices, and end-date updates. V2 adds explicit contract, commit, and credit edits plus edit-history retrieval.

Products and rate cards support reusable pricing, aliases, effective schedules, product ordering, individual and bulk rates, and custom pricing-unit conversions. At `3.10.0`, rate-card updates can add `add_credit_type_conversions`; existing conversions cannot be modified through that field.

Customer-level commits and credits can be limited to selected contracts or left cross-contract. In V2 commit edits, `applicable_contract_ids: null` means all customer contracts, but the field cannot be edited for postpaid or contract-level commits. The shared commit response now includes optional `cost_basis`, defined as the ratio of amount paid to credit granted.

## Billing Providers and Invoices

The customer and settings resources expose billing-provider setup, customer billing configurations, configuration schedules, invoice listing and PDF retrieval, invoice breakdowns, one-time charges, regeneration, and voiding. Generated types include Stripe collection methods, downstream invoice statuses, external payment IDs, provider errors, and provider schedules.

These types describe transport contracts only. They do not transfer payment collection, tax, retry, reconciliation, or provider-readiness ownership from the external billing system to the SDK.

## Webhook Helpers

`client.webhooks.verifySignature()` requires the exact raw body, `X-Metronome-Date`, `Metronome-Webhook-Signature`, and a configured or explicitly passed secret. It signs `<date>\n<payload>` with HMAC-SHA256, rejects timestamps more than five minutes old or five minutes in the future, and uses a timing-resistant byte comparison. `unwrap()` verifies first and then parses the JSON payload.

The helper proves local verification behavior. Delivery retries, duplicate handling, ordering, and event semantics remain governed by the dedicated webhook documentation.

## `3.10.0` Release Findings

The release adds rate-card `add_credit_type_conversions`, commit `cost_basis`, and `applicable_contract_ids` in customer-commit edits. It removes `supersede` from contract transition typing and adds documentation for daily recurring commits and embeddable dashboards. No mandatory migration is documented for this minor release.

## Related

- [[changelog-github-metronome-node]] - package-qualified release ledger
- [[metronome]] - company and knowledge-status page
- [[metronome-integrations]] - SDK and external-system boundaries
- [[metronome-event-ingestion]] - endpoint-specific usage-event behavior
- [[metronome-products-and-rate-cards]] - pricing and conversion concepts
- [[metronome-credits-and-commits]] - balance and applicability concepts
- [[metronome-webhooks]] - delivery and authenticity semantics

## Raw Sources

- Snapshot manifest: `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/manifest.json`
- Release manifest: `raw/github/metronome/metronome-node/releases/sdk/3.10.0/2026-08-12/manifest.json`
- Release notes: `raw/github/metronome/metronome-node/releases/sdk/3.10.0/2026-08-12/release-notes.md`
- Repository changelog: `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/files/CHANGELOG.md`
- README: `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/files/README.md`
- Migration guide: `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/files/MIGRATION.md`
- Package manifest: `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/files/package.json`
- Client implementation: `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/files/src/client.ts`
- Generated API index: `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/files/api.md`
- Usage resource: `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/files/src/resources/v1/usage.ts`
- Contract resources: `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/files/src/resources/v1/contracts/contracts.ts` and `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/files/src/resources/v2/contracts.ts`
- Shared models: `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/files/src/resources/shared.ts`
- Webhook helper: `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/files/src/resources/webhooks.ts`
