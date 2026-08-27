---
title: "Metronome API Idempotency"
type: concept
category: technology
tags: [metronome, api, idempotency, retries]
---

## Definition

Metronome uses several idempotency mechanisms rather than one universal key. The correct mechanism depends on whether a client is ingesting usage, associating customers, creating a resource with a supported uniqueness field, or retrying a POST request.

## Mechanisms

| Mechanism | Scope | Duplicate or conflict behavior | Documented lifetime |
| --- | --- | --- | --- |
| `transaction_id` | Usage events sent through `/ingest` or Segment | Later events with the same ID are ignored | 34 days |
| Ingest alias | Customer writes and usage attribution | An alias already assigned to a customer conflicts until it is removed | Until released |
| `uniqueness_key` | Supported resource-creation endpoints | Reuse returns HTTP `409 Conflict` | Until released; the overview notes release is available only for alerts |
| `Idempotency-Key` | All POST endpoints | Identical parameters return the original result; changed parameters return HTTP `409 Conflict` | At least 24 hours |

The documented `uniqueness_key` examples include contracts, alerts, and customer-level commits and credits. The source labels contract-edit support as coming soon, so support should be verified against the specific endpoint rather than inferred for all writes.

`POST /v1/contracts/customerCredits/create` specifically exposes a 1-128 character `uniqueness_key`; reuse after a credit or commit creation prevents a new record and returns HTTP 409, although 409 is absent from the operation's response map. This resource-identity guard is separate from the API-wide `Idempotency-Key` result-replay mechanism for POST. The API-wide authority says uniqueness keys last until released but documents release only for Alerts, so no customer-credit release path is documented. The sources do not define interaction or precedence between the two keys, uniqueness-key scope, normalization, races, failed-attempt consumption, expired-header-key retries, or endpoint-specific cached-error recovery.

> [!warning] Endpoint-specific qualification
> The deprecated Plans credit-grant void endpoint documents `release_uniqueness_key: true`, which resets that grant's uniqueness key for reuse. This qualifies the API-wide overview's statement that release is available only for Alerts. The endpoint does not define release visibility, concurrent reuse, rollback, or interaction with the API-wide `Idempotency-Key` mechanism. [[source-metronome-api-reference-credit-grants-void-a-credit-grant]]

## Retry and error boundary

The `POST /v2/contracts/edit` snapshot exposes optional 1-128 character `uniqueness_key`; its schema says reuse prevents a duplicate record and fails with HTTP `409`, even though the operation response map omits `409`. The same-date API-wide idempotency page still labels contract-edit uniqueness-key support as coming soon. Preserve that unresolved documentation/runtime-enablement conflict: endpoint schema exposure alone does not prove the feature is enabled. This resource-uniqueness mechanism is distinct from API-wide POST `Idempotency-Key` result replay. The sources do not define uniqueness-key scope or release, failed-attempt consumption, interaction or precedence between the two keys, safe use after expiry, concurrency ordering, or recovery after cached or ambiguous failures. [[source-metronome-api-reference-contracts-edit-a-contract]] [[source-metronome-api-reference-idempotency]]

`POST /v1/customer-alerts/get` is a point-in-time threshold-status read under the API-wide `Idempotency-Key` contract. Identical same-key parameters replay the original result, so that replay is not evidence of a fresh `ok`, `in_alarm`, `evaluating`, or archived-state evaluation. The endpoint page adds no read-specific guarantee for caching, freshness, another or expired key, concurrent calls, or ambiguous-failure recovery. [[source-metronome-api-reference-alerts-get-a-threshold-notification]]

The SDK reference says the Python, Go, Ruby, and Node.js clients automatically retry each request upon failure up to three times by default and allow the count to be configured. It does not identify retryable statuses or exceptions, attempt counting, backoff, jitter, timeout behavior, method safety, or whether retries inject or preserve an API-wide `Idempotency-Key`. Event `transaction_id` is a separate usage-deduplication identity and must not be generalized to billable-metric, customer, product, rate-card, rate, or contract creation. [[source-metronome-api-reference-sdks]]

Applied to manage-seats operations, the existing API-wide POST rule has financially material retry consequences. `quantity_delta` expresses a change, while `add_unassigned_seats` increases capacity with configuration-dependent invoice and credit effects; reissuing either mutation with a different or expired key after an ambiguous result may apply the change again. The guide adds no edit-, alert-, history-, or balance-endpoint guarantee for atomicity, read-after-write visibility, concurrency, another-key behavior, or ambiguous-failure recovery. Investigate state after a cached or ambiguous failure under the separate API-wide authority rather than assuming a new key is safe. [[source-metronome-guides-pricing-packaging-subscription-manage-seats]]

The API-wide `Idempotency-Key` contract applies to `POST /v1/contracts/updateInvoiceIssueDate`: identical same-key parameters replay the original result, changed parameters conflict, retention is at least 24 hours, and a cached result can be HTTP `500`. The endpoint adds no issue-date-specific semantics for another or expired key, concurrent rescheduling, read-after-write visibility, or recovery and final invoice state after a cached or ambiguous failure. [[source-metronome-api-reference-contracts-update-invoice-issue-date]] [[source-metronome-api-reference-idempotency]]

Metronome persists an `Idempotency-Key` result after a request begins execution—that is, after validation and concurrent-request conflict checks. The cached result can be an HTTP `500` error. Reusing that key returns the cached error, so the source recommends investigating system state and deciding whether to resolve manually or retry instead of automatically switching keys after a partial failure.

The best-practice guidance recommends deterministic keys derived from business identity and operation type for resource operations, UUIDs where deterministic identity is unnecessary, exponential backoff, and reuse of the same key within its lifetime. The separate status-code reference advises verifying that a resource was not partially created after a `5XX` response, but its suggestion to retry with a different key must be reconciled with the idempotency page's manual-investigation warning for cached errors.

For periodic usage heartbeats, the event guide gives a concrete deterministic pattern: combine a node identifier with a minute bucket, send at least two heartbeats per measurement period, and rely on transaction-ID duplicate suppression. This event-specific retry pattern does not define safe behavior for other POST operations.

For account-level billing-provider setup, `POST /v1/setUpBillingProvider` falls under the API-wide `Idempotency-Key` guarantee, but its own page documents only generic HTTP 400 and 409 errors and no endpoint-specific retry, concurrency, partial-creation, provider-side deduplication, or recovery semantics. The successful result's UUID `delivery_method_id` is the result that an identical same-key retry should recover under the API-wide authority; after an ambiguous failure, do not assume a changed key is safe or that external-provider state is reconciled. [[source-metronome-api-reference-settings-set-up-account-level-billing-provider]]


`POST /v1/customers/{customer_id}/setName` falls under the API-wide `Idempotency-Key` contract even though its endpoint page lists only HTTP `200` and does not mention retries. An identical same-key retry returns the original mutation result rather than proving a fresh read of the customer's current name; the endpoint adds no behavior for another or expired key, concurrent renames, cached-error customer or document state, or recovery after ambiguous propagation. [[source-metronome-api-reference-customers-update-a-customer-name]] [[source-metronome-api-reference-idempotency]]

`POST /v1/contract-pricing/products/get` is a product read whose request schema requires a product UUID inside an enclosing body that is not marked required; HTTP `200` requires `data`, and the product requires identity plus initial, current, and update-history surfaces. Its endpoint page adds no endpoint-specific idempotency, retry, cache, freshness, concurrency, or recovery guarantee.

The assigned product-catalog reference documents `POST /v1/contract-pricing/products/list`. Its complete operation response map lists only HTTP `200`, and it supplies no endpoint-specific idempotency, retry, caching, cursor-replay, or freshness contract. [[source-metronome-api-reference-products-list-products]]

`POST /v1/customers/archive` says ingest aliases remain idempotent for archived customers and directs callers to remove an alias before archival when it must be reused. This archived-customer alias reservation is distinct from request replay, and the endpoint itself gives no archive-specific retry contract. [[source-metronome-api-reference-customers-archive-a-customer]]




## Related platform concepts

- [[metronome-event-ingestion]] owns the usage-event schema, matching, deduplication, and processing boundaries.
- [[metronome-customers-and-contracts]] owns ingest-alias assignment and resource lifecycle.
- [[metronome-credits-and-commits]] covers uniqueness keys on credit and commit creation.

## Sources

- [[source-metronome-guides-pricing-packaging-subscription-manage-seats]] — quantity-delta and unassigned-seat retry materiality plus endpoint-specific atomicity, visibility, concurrency, and recovery unknowns

- [[source-metronome-guides-get-started-api-quickstart]] — multi-POST onboarding walkthrough whose event `transaction_id` deduplication is distinct from the API-wide POST `Idempotency-Key` authority

- [[source-metronome-api-reference-contracts-get-the-rate-schedule-for-a-contract]] - POST contract-rate read, effective-time and entitlement scope, and the boundary that same-key result replay does not establish a fresh schedule
- [[source-metronome-guides-events-send-usage-events]] — 34-day transaction-ID duplicate suppression, retry reuse, deterministic heartbeat IDs, and the unqualified-versus-windowed guarantee tension

- [[source-metronome-api-reference-idempotency]] — mechanism selection, key lifetimes, conflict behavior, cached errors, and retry guidance
- [[source-metronome-api-reference-status-codes]] — API-wide conflict, rate-limit, and server-error recovery guidance
- [[source-metronome-guides-implement-metronome-core-concepts-send-usage-events]] — direct-ingest retry safety and deterministic heartbeat identifiers

- [[source-metronome-api-reference-settings-set-up-account-level-billing-provider]] — POST setup mutation, returned configuration identifier, generic conflicts, and endpoint-specific recovery unknowns

- [[source-metronome-api-reference-credits-and-commits-create-a-credit]] - endpoint-specific uniqueness-key schema, duplicate-creation prevention, omitted 409 response-map entry, and interaction unknowns


- [[source-metronome-api-reference-customers-update-a-customer-name]] — POST customer-name mutation, original-result replay context, and endpoint-specific concurrency and recovery unknowns

- [[source-metronome-api-reference-products-get-a-product]] - POST product-read method, required identity and history response surface, and endpoint-specific idempotency, retry, caching, and freshness unknowns

- [[source-metronome-api-reference-products-list-products]] — POST product-catalog listing, its sole listed HTTP `200` response, and endpoint-specific idempotency, retry, caching, cursor-replay, and freshness unknowns

- [[source-metronome-api-reference-customers-archive-a-customer]] - POST customer archival, archived-customer ingest-alias reservation and reuse prerequisite, and absence of an archive-specific retry contract




- [[source-metronome-api-reference-contracts-get-a-contract-v2]] - POST contract-state read, historical-view and optional balance/ledger controls, and the boundary that same-key result replay does not establish a fresh read
- [[source-metronome-api-reference-credit-grants-list-credit-ledger-entries]] - read-only POST ledger listing, cursor and time-window inputs, and the boundary that API-wide same-key replay does not establish a fresh ledger view

- [[source-metronome-api-reference-credits-and-commits-list-seat-balances]] - read-only POST seat-balance listing, body cursor and time-window inputs, and the boundary that API-wide same-key replay does not establish a fresh balance view

- [[source-metronome-api-reference-alerts-get-a-threshold-notification]] — POST threshold-status read and the boundary that same-key result replay does not establish a fresh evaluation

## Related

- [[metronome]]
- [[metronome-security-principles]]
