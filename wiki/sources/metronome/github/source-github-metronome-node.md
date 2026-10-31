---
title: "GitHub: Metronome-Industries/metronome-node"
type: source
date_ingested: 2026-08-12
date_updated: 2026-10-31
original_format: github-repo
raw_files:
  - "github/metronome/metronome-node/snapshots/2026-10-31-5e8d4ac/manifest.json"
  - "github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/manifest.json"
tags: [metronome, node-js, typescript, server-sdk, usage-billing, contracts, webhooks, github-repository]
---

## Versioned Coverage

Full additive ingestion of `@metronome/sdk@3.11.0`, released 2026-10-27 at `5e8d4ac4659f9378f2341e4e18f89274908523ed`, extends the preserved `3.10.0` baseline below. The user approved full mode despite the packet's mechanical delta recommendation because the minor release includes incompatible API/type changes. No older knowledge or raw evidence is replaced. See [[changelog-github-metronome-node]] for the release ledger.

The approved focused read covers every changed implementation/API/documentation section across 39 changed/new retained files, affected prior code, all five newly added files in full, release notes, comparison and cumulative wiki history. Both manifests and duplicated diff/inventories were checked mechanically, along with 66 unchanged files. The current capsule has 105 files / 1,299,665 bytes; all 205 prior/current file sizes, SHA-256 hashes and Git blob IDs were verified. This is bounded package evidence, not a full upstream-repository read, executed integration test or account-enablement proof.

## `3.11.0` Breaking Changes and Migration

### Contract lists now require page traversal

Both V1 and V2 `contracts.list()` change from `APIPromise<ContractListResponse>` to `PagePromise` over shared `Contract`/`ContractV2` items. The old response interfaces and their barrel exports are removed; their replacements are `ContractsBodyCursorPageCursorField` (V1) and `ContractV2sBodyCursorPageCursorField` (V2), exported from the corresponding contract modules and shared type layer.

The generated methods still POST to `/v1/contracts/list` or `/v2/contracts/list`, but now use `getAPIList` and `BodyCursorPageCursorField`. That page class reads response `cursor`, normalizes a missing/falsy cursor to an empty string, preserves the original request options/body and sends the next cursor in the JSON body. Its `hasNextPage()` depends on cursor presence rather than a nonempty item array. Do not substitute query `next_page` from other endpoint families. Both method docstrings describe 20 contracts per page; generated params expose `limit` but do not enforce that bound locally.

```typescript
// 3.11.0: traverse every returned page, not just one awaited data array.
for await (const contract of client.v2.contracts.list({
  customer_id: customerId,
  covering_date: new Date().toISOString(),
})) {
  console.log(contract.id);
}

// Manual traversal remains available when page-level control is needed.
let page = await client.v2.contracts.list({ customer_id: customerId });
while (true) {
  for (const contract of page.data) console.log(contract.id);
  if (!page.hasNextPage()) break;
  page = await page.getNextPage();
}
```

These examples describe package usage, not an executed API call. Traversal prevents treating the first page as exhaustive but does not guarantee cross-page snapshot consistency or atomic duplicate-provisioning prevention. Older website snapshots and the baseline response wrapper remain historical evidence, not a current all-contract guarantee. [[metronome-customers-and-contracts]]

### Required response timestamps and MCP removal

Recurring commit and credit response models now require `anchor_date`; subscription responses require `created_at`. Update typed fixtures and adapters constructing these objects. These are response-model changes, not a statement that every corresponding create request now requires those fields. Credit response `created_at` is optional, with separate recurring-credit and rollover-credit timestamp descriptions.

The upstream tree removes `packages/mcp-server`, and README installation links are removed. Those implementation paths were outside this approved SDK capsule; removal is grounded in the complete upstream changed-path inventory and release notes, not a deep read of excluded MCP code. The release notes say already published MCP versions remain available and recommend pinning an existing version while arranging a replacement; no package unpublication or installed-server failure was tested.

### Additional Stripe type narrowing

> [!warning] Version-scoped Stripe configuration change
> Beyond the release-note migration bullets, `customers/customers.ts` and `customers/billing-config.ts` remove `auto_charge_payment_intent` and `manually_charge_payment_intent` from `stripe_collection_method`; only `charge_automatically` and `send_invoice` remain in those `3.11.0` request/response unions. Customer billing-provider configuration also removes the prior PaymentIntent-only restriction from its `tax_provider` description. This establishes a compile-time/docs change, not service-wide removal, wider tax eligibility or retirement of the independently documented threshold PaymentIntent flow. Preserve the `3.10.0` types and separate product authorities rather than conflating the surfaces. [[metronome-integrations]] retains the reciprocal warning.

## `3.11.0` Billing and Notification Additions

- **Quantity balances:** commit/credit access schedules and recurring access amounts add `SPEND` and `QUANTITY`. Creation schedules describe omitted access type as `SPEND`; response optionality does not supply a universal default. Net-balance lookup defaults to spend and forbids `credit_type_id` with quantity. Quantity response docstrings describe the null credit-type UUID, not a nullable JavaScript field. Seat-balance detail gains access-type/credit-type identity; invoice attribution gains `quantity_consumed` and applied-balance access type. [[metronome-credits-and-commits]]
- **Manual balance deduplication:** `addManualBalanceEntry` accepts `uniqueness_key`. Duplicate keys create no new record and return `409`, rather than replaying a successful response. The unchanged generic client retries `409`; use a stable key and reconcile ambiguous outcomes rather than blindly generating a fresh key. Retention, concurrency and service-side retry safety are not established by this docstring.
- **Threshold-created commits:** prepaid threshold commit configuration adds duration, `COMMIT_RATE`/`LIST_RATE`, and rollover fraction from zero to one. Shared duration documentation starts validity at invoice service-period end and defaults to one year; V2 edit fields permit null to clear the setting. Payment-gate completion is a separate boundary.
- **Metric and subscription changes:** `v1.billableMetrics.update({billable_metric_id, name})` sends PUT for display-name-only changes; calculation configuration remains immutable. V2 `update_subscriptions` adds `name`; returned `product_custom_fields` belongs to the referenced subscription product and is distinct from instance custom fields. Subscription/package types also add `custom_credit_type_id`. [[metronome-billable-metrics]]
- **Custom pricing units:** `v1.pricingUnits.create({name})` and `.archive({id})` POST to `/v1/credit-types/create` and `/v1/credit-types/archive`, returning `data.id`. Archival hides the unit from selectors by default; this does not prove deletion, historical repricing or existing-contract effects. [[metronome-products-and-rate-cards]]
- **Lifecycle notifications:** the new `v2.notifications.offset` resource creates, retrieves, lists, archives and edits offset configurations. Its list uses body `cursor`, with a documented maximum of 400 results per request; archive filter defaults to `NOT_ARCHIVED`. Policies carry signed ISO-8601 offsets. The sibling `system.list()` returns a plain response with optional cursor and no typed pagination input, so it is not an automatic complete inventory.
- **System enablement uses the offset namespace:** `v2.notifications.offset.edit({policy:{type}, is_enabled})` enables/disables system webhook publishing without an offset ID. Offset-policy edits instead identify the configuration and require a matching lifecycle-event type. This shared method/union response is not a separate `system.edit()` API. [[metronome-alerts-and-notifications]]
- **Threshold notifications:** types add `low_remaining_contract_credit_and_commit_percentage_reached` and selected access-type filters; quantity access cannot specify a credit type. Archiving an already archived threshold is now explicitly documented as succeeding. Neither statement proves webhook delivery, entitlement enforcement or propagation timing.
- **Named schedules:** `v1.contracts.rateCards.namedSchedules.list()` newly calls `/v1/contracts/listNamedSchedules` for one required customer, optionally one contract, name, covering date and property subset. It uses `BodyCursorPage`/body `next_page`, unlike contract lists and lifecycle offset lists. Existing get/update methods gain property qualifiers. Do not confuse it with the separately nested rate-card-catalog named-schedule resource at `v1.contracts.namedSchedules`.
- **Other pricing/invoice changes:** composite create/update/read shapes expose `include_composite_spend`, default false; package usage-statement day accepts `CUSTOM_DATE`; customer invoice listing adds `include_historical_commit_invoices`, default false. Applied-commit attribution extends to `CPU_CONVERSION` lines, and `billable_status` documentation explains provider-delivery intent while leaving its type `unknown`. These are not payment-success or accounting-completeness guarantees.

## `3.11.0` Documentation Corrections and Limits

The stale top-level Payments section is removed from `api.md`. That resolves the baseline index-versus-implementation inconsistency; it does not newly remove a working Payments resource in `3.11.0`, since the retained `3.10.0` source already lacked it.

Usage aggregation docstrings now explicitly require UTC-midnight time bounds separated by at least one day. Grouped usage accepts at most 200 filter values in total across arrays, with a 100-row default/maximum for compound-group pages; the prose qualifies rejection as applying when the limit is enforced. These are docstring clarifications, not new local client validation or measured server behavior. Existing exact metric/group-key matching and product-level calculation boundaries remain controlling.

`customFields.setValues()` documents that changing custom fields on credits, commits or contracts does not emit the corresponding `credit.edit`, `commit.edit` or `contract.edit` events. Do not use those events as guaranteed custom-field refresh signals. Customer-level commit/credit creation guidance favors contract edits for ordinary changes. V2 edit docs now describe an edit ID and optional edit details instead of incorrectly calling it the contract ID; generated `data.edit` remains optional, so the prose does not guarantee complete returned details.

The wider earlier Web Fetch migration guide is retained history. Its only change here adds the new offset-list method to the request-options-overload examples; the old Node/fetch/export migrations are not re-attributed to `3.11.0`.

## `3.11.0` Grounding Excerpts

> "Results are limited to 20 contracts per page. When the response includes a"
>
> `raw/github/metronome/metronome-node/snapshots/2026-10-31-5e8d4ac/files/src/resources/v2/contracts.ts:63`

> "Important: Only the name can be modified via this endpoint; configurations"
>
> `raw/github/metronome/metronome-node/snapshots/2026-10-31-5e8d4ac/files/src/resources/v1/billable-metrics.ts:112`

> "request will fail with a 409 error."
>
> `raw/github/metronome/metronome-node/snapshots/2026-10-31-5e8d4ac/files/src/resources/v1/contracts/contracts.ts:3601`

> "Adding or updating custom fields on credits, commits, or contracts does not emit"
>
> `raw/github/metronome/metronome-node/snapshots/2026-10-31-5e8d4ac/files/src/resources/v1/custom-fields.ts:144`

> "Edit an existing offset notification, or enable/disable a system notification"
>
> `raw/github/metronome/metronome-node/snapshots/2026-10-31-5e8d4ac/files/src/resources/v2/notifications/offset.ts:97`

## `3.11.0` Evidence Routes

- Snapshot manifest: `raw/github/metronome/metronome-node/snapshots/2026-10-31-5e8d4ac/manifest.json`
- Release manifest: `raw/github/metronome/metronome-node/releases/sdk/3.11.0/2026-10-31/manifest.json`
- Release notes: `raw/github/metronome/metronome-node/releases/sdk/3.11.0/2026-10-31/release-notes.md`
- Exact comparison: `tracking/github/repos/metronome/metronome-node/comparisons/sdk/3.10.0--3.11.0/comparison.json`, `comparison.md` and `diff.patch` in the same directory.
- Changed implementation: `raw/github/metronome/metronome-node/snapshots/2026-10-31-5e8d4ac/files/`, especially `src/core/pagination.ts`, `src/resources/shared.ts`, V1/V2 contract modules, customer billing-config/invoice modules, billable metrics, pricing units and V2 notification modules. The manifest maps each exact path to its immutable hash.

## Preserved `3.10.0` Baseline

The following original baseline sections and excerpts are retained unchanged. Their version-scoped behavior and unresolved-at-the-time warnings are not latest-version claims; the additions above describe the `3.11.0` changes and corrections.

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
