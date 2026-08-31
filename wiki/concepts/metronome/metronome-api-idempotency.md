---
title: "Metronome API Idempotency"
type: concept
category: technology
tags: [metronome, api, idempotency, retries]
---

## Definition

Metronome uses several idempotency mechanisms rather than one universal key. The correct mechanism depends on whether a client is ingesting usage, associating customers, creating a resource with a supported uniqueness field, or retrying a POST request.

## Mechanisms

`POST /v1/alerts/create` attaches a 1-128 character resource `uniqueness_key` to `CreateCustomerAlertPayload`. Narrative guidance says every threshold notification must have one unique within the organization and may release it during archival, while the payload required array omits the field. Reuse prevents a new record and documents HTTP `409`, although the operation response map lists only `200`. This organizational resource-identity guard is distinct from API-wide POST `Idempotency-Key` result replay. The endpoint and API-wide authority do not define the two keys' interaction or precedence, uniqueness-key normalization, concurrent-creation ordering, release visibility, failed-attempt key consumption, behavior after the header key expires, or recovery after a cached or ambiguous failure. [[source-metronome-api-reference-alerts-create-a-threshold-notification]] [[source-metronome-api-reference-idempotency]]

| Mechanism | Scope | Duplicate or conflict behavior | Documented lifetime |
| --- | --- | --- | --- |
| `transaction_id` | Usage events sent through `/ingest` or Segment | Later events with the same ID are ignored | 34 days |
| Ingest alias | Customer writes and usage attribution | An alias already assigned to a customer conflicts until it is removed | Until released |
| `uniqueness_key` | Supported resource-creation endpoints | Reuse returns HTTP `409 Conflict` | Until released; the overview notes release is available only for alerts |
| `Idempotency-Key` | All POST endpoints | Identical parameters return the original result; changed parameters return HTTP `409 Conflict` | At least 24 hours |

The documented `uniqueness_key` examples include contracts, alerts, and customer-level commits and credits. The source labels contract-edit support as coming soon, so support should be verified against the specific endpoint rather than inferred for all writes.

`POST /v1/contracts/customerCredits/create` specifically exposes a 1-128 character `uniqueness_key`; reuse after a credit or commit creation prevents a new record and returns HTTP 409, although 409 is absent from the operation's response map. This resource-identity guard is separate from the API-wide `Idempotency-Key` result-replay mechanism for POST. The API-wide authority says uniqueness keys last until released but documents release only for Alerts, so no customer-credit release path is documented. The sources do not define interaction or precedence between the two keys, uniqueness-key scope, normalization, races, failed-attempt consumption, expired-header-key retries, or endpoint-specific cached-error recovery.

Customer-commit creation exposes a 1-128 character `uniqueness_key`; reuse after creation of a commit or credit prevents a new record and fails with HTTP `409`, although the operation response map lists only `200`, `400`, and `404`. This resource-creation guard remains distinct from the separately documented API-wide POST `Idempotency-Key` result-replay authority. The endpoint page defines neither the two keys' interaction or precedence nor uniqueness scope, release, failed-attempt consumption, concurrent creation, or ambiguous-failure recovery. [[source-metronome-api-reference-credits-and-commits-create-a-commit]] [[source-metronome-api-reference-idempotency]]

> [!warning] Endpoint-specific qualification
> The deprecated Plans credit-grant void endpoint documents `release_uniqueness_key: true`, which resets that grant's uniqueness key for reuse. This qualifies the API-wide overview's statement that release is available only for Alerts. The endpoint does not define release visibility, concurrent reuse, rollback, or interaction with the API-wide `Idempotency-Key` mechanism. [[source-metronome-api-reference-credit-grants-void-a-credit-grant]]

## Retry and error boundary

`POST /v1/setCustomerBillingProviderConfigurations` creates a batch of customer-level provider configurations and returns configuration records whose `id` is resource identity, not an idempotency key. The separate API-wide `Idempotency-Key` contract applies to this POST and replays the original result for identical same-key parameters, but the endpoint adds no semantics for another or expired key, concurrent mutations, partial batch success or recovery, duplicate resource prevention, read-after-write visibility, or provider-side deduplication and reconciliation. After a cached or ambiguous failure, investigate state rather than assume a changed key is safe. [[source-metronome-api-reference-customers-set-billing-provider-configurations-for-a-customer]] [[source-metronome-api-reference-idempotency]]

`POST /v1/customFields/addKey` falls under the separate API-wide `Idempotency-Key` contract: identical same-key parameters replay the original result, changed parameters conflict, retention is at least 24 hours, and a cached result can be HTTP `500`. The endpoint documents only HTTP `200` and adds no create-key-specific behavior for another or expired key, concurrent calls, read-after-create visibility, cached-error state, or recovery. Its required `enforce_uniqueness` boolean constrains later custom-field values; it is not a resource `uniqueness_key` or a request-result replay mechanism, and the page does not define duplicate-key creation. [[source-metronome-api-reference-custom-fields-create-a-custom-field-key]] [[source-metronome-api-reference-idempotency]]

`POST /v1/customFields/removeKey` falls under the separate API-wide `Idempotency-Key` contract. Identical same-key parameters replay the original result, but that replay is not fresh proof that the key remains absent or that existing-value inaccessibility has propagated to every read, export, invoice, or integration surface. The endpoint adds no local behavior for an already absent key, another or expired key, concurrent removal or re-creation, read-after-write visibility, or recovery after cached or ambiguous failure. [[source-metronome-api-reference-custom-fields-delete-a-custom-field-key]] [[source-metronome-api-reference-idempotency]]

`POST /v2/contracts/commits/edit` uses required payload `commit_id` to identify an existing commit and returns a generic UUID `data.id` whose meaning is not defined by the endpoint. The separate API-wide `Idempotency-Key` contract applies to this POST and replays the original result for identical same-key parameters; that request-result replay is not a commit-resource uniqueness key or evidence of current commit state. The endpoint adds no behavior for another or expired key, concurrent edits, cached or ambiguous failure, read-after-write visibility, or recovery. [[source-metronome-api-reference-credits-and-commits-edit-a-commit]] [[source-metronome-api-reference-idempotency]]

`POST /v1/invoices/regenerate` regenerates a voided invoice and can distribute the replacement through configured billing-provider routing. The existing API-wide `Idempotency-Key` contract applies to this POST, but the endpoint adds no regeneration-specific behavior for another or expired key, concurrent calls, timeout recovery, resulting invoice state after cached or ambiguous failure, or whether a changed key can create and distribute another invoice. Investigate state rather than assuming a new key is safe. [[source-metronome-api-reference-invoices-regenerate-an-invoice]] [[source-metronome-api-reference-idempotency]]

The 2026-08-28 `POST /v2/contracts/edit` snapshot exposes optional 1-128 character `uniqueness_key`; its schema says reuse prevents a duplicate record and fails with HTTP `409`, even though the operation response map omits `409`. The earlier 2026-07-13 API-wide idempotency page labels contract-edit uniqueness-key support as coming soon. Preserve that unresolved documentation/runtime-enablement conflict: newer endpoint schema exposure alone does not prove the feature is enabled. This resource-uniqueness mechanism is distinct from API-wide POST `Idempotency-Key` result replay. The sources do not define uniqueness-key scope or release, failed-attempt consumption, interaction or precedence between the two keys, safe use after expiry, concurrency ordering, or recovery after cached or ambiguous failures. [[source-metronome-api-reference-contracts-edit-a-contract]] [[source-metronome-api-reference-idempotency]]

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

`POST /v1/dashboards/getEmbeddableUrl` generates a customer-specific URL that its endpoint prose calls time-limited. The separate API-wide `Idempotency-Key` contract applies to this POST and returns the original result for identical same-key parameters, but the endpoint does not relate the at-least-24-hour idempotency retention window to the URL's unspecified lifetime. A same-key replay is therefore recovery of the original result, not evidence that the URL was newly minted, remains unexpired, or reflects current dashboard configuration, customer state, contract filters, or security settings. The endpoint also adds no local behavior for another or expired key, concurrent generation, cached or ambiguous failure, revocation, or regeneration. [[source-metronome-api-reference-customers-get-an-embeddable-customer-dashboard]] [[source-metronome-api-reference-idempotency]]

`POST /v1/customers/{customer_id}/setIngestAliases` is endpoint-idempotent desired-state replacement: repeating the same alias set should not create another alias resource or a different final set. This is distinct from ingest-alias identity reservation and from the API-wide `Idempotency-Key` request cache. The alias authority says an alias in use conflicts with HTTP `409` until removed from its original active or archived customer. Separately, identical same-key POST parameters replay the persisted original result, changed parameters conflict, retention is at least 24 hours, and a cached result can be HTTP `500`; replay is not a fresh read of the current alias set or usage attribution. The endpoint itself lists HTTP `200` with description `Success` but provides no response content schema or example, and therefore exposes no documented applied-set representation, affected-event list, propagation state, or operation identifier; it adds no no-key, another-key, expired-key, concurrent-replacement, partial-failure, propagation, cached-error-state, or ambiguous-failure recovery behavior. [[source-metronome-api-reference-customers-create-or-update-customer-ingest-aliases]] [[source-metronome-api-reference-idempotency]]

`POST /v1/billable-metrics/archive` uses required payload UUID `id` to select the billable metric. HTTP `200` requires top-level `data` referencing the generic `Id` schema, which requires UUID `data.id`; the example repeats the request UUID, but the schema does not separately label the returned value or establish metric-resource versus archive-operation identity. `data.id` is not documented as an `Idempotency-Key` or as a separate archive-operation resource. The API-wide `Idempotency-Key` authority applies to this POST: after execution begins, identical same-key parameters replay the persisted original result, changed parameters return HTTP `409`, retention is at least 24 hours, and a cached result can be HTTP `500`. The endpoint itself documents only `200` and generic `404` and adds no semantics for repeated archival, an already archived metric, another or expired key, no-key retries, concurrent archival or Product association, read-after-write freshness, cached-error state, partial effects, rollback, or ambiguous-failure recovery. A same-key replay is not fresh proof of current archive visibility, Product behavior, event processing, invoice state, or downstream propagation. [[source-metronome-api-reference-billable-metrics-archive-a-billable-metric]] [[source-metronome-api-reference-idempotency]]

`PUT /v1/billable-metrics/{billable_metric_id}` changes only a metric display name. The separate API-wide `Idempotency-Key` authority explicitly covers all POST endpoints, not this PUT, and the Update Metric page exposes no resource `uniqueness_key` or endpoint-specific repeated-call, retry, concurrent-rename, lost-update, timeout, cached-error, or ambiguous-failure recovery guarantee. Its required path UUID and returned generic `data.id` are operation input and response identity surfaces, not documented idempotency keys. [[source-metronome-api-reference-billable-metrics-update-a-billable-metric]] [[source-metronome-api-reference-idempotency]]

`POST /v1/contracts/getSubscriptionSeatsHistory` is a paginated temporal read under the separate API-wide `Idempotency-Key` contract. Identical same-key parameters replay the original result, so replay is not proof of a fresh seat schedule, current assignments, a newly established pagination snapshot, or visibility of a recent seat edit. The endpoint adds no read-specific behavior for another or expired key, cursor replay with a key, concurrent reads and edits, cached errors, read-after-write timing, or ambiguous-failure recovery. [[source-metronome-api-reference-contracts-get-subscription-seats-history]] [[source-metronome-api-reference-idempotency]]

`POST /v1/contracts/createHistoricalInvoices` falls under API-wide `Idempotency-Key` result replay: identical same-key parameters replay the original result, changed parameters conflict, retention is at least 24 hours, and a cached result can be HTTP `500`. This is distinct from each returned invoice `data[].id`; the endpoint exposes no batch-operation ID or resource `uniqueness_key`. Because `preview` is a required request parameter, changing it from `true` to `false` changes the idempotency parameters rather than committing a prior preview, while replaying the preview key returns the original result rather than fresh validation. The endpoint adds no safe behavior for an absent, another, or expired key; concurrent or overlapping batches; partial creation; duplicate-invoice prevention; result freshness; or recovery and ledger/downstream reconciliation after cached or ambiguous failure. [[source-metronome-api-reference-contracts-create-historical-invoices]] [[source-metronome-api-reference-idempotency]]

## Related platform concepts

- [[metronome-event-ingestion]] owns the usage-event schema, matching, deduplication, and processing boundaries.
- [[metronome-customers-and-contracts]] owns ingest-alias assignment and resource lifecycle.
- [[metronome-credits-and-commits]] covers uniqueness keys on credit and commit creation.

## Sources

- [[source-metronome-api-reference-billable-metrics-update-a-billable-metric]] - name-only PUT mutation outside the documented all-POST `Idempotency-Key` scope and its endpoint-specific retry, concurrency, and recovery unknowns
- [[source-metronome-api-reference-contracts-get-subscription-seats-history]] - paginated POST seat-schedule history and the boundary that same-key replay does not establish fresh assignments, recent-edit visibility, or a new stable pagination snapshot
- [[source-metronome-api-reference-customers-get-an-embeddable-customer-dashboard]] - time-limited generated URL response and the boundary that same-key POST replay does not establish a newly minted, unexpired, or fresh dashboard URL
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-guarantee-zero-overages]] - multiple POST pricing and contract examples that omit `Idempotency-Key`, requiring the separate API-wide replay and cached-error boundary
- [[source-metronome-api-reference-customers-set-billing-provider-configurations-for-a-customer]] - POST customer-configuration mutation, returned resource identity, API-wide result replay, and endpoint-specific batch, concurrency, and recovery unknowns

- [[source-metronome-api-reference-invoices-regenerate-an-invoice]] - POST invoice regeneration, configured distribution side effect, and endpoint-specific concurrency and ambiguous-failure recovery boundaries

- [[source-metronome-guides-pricing-packaging-billing-model-guides-token-billing]] - contract-create and usage-ingest POST examples that omit `Idempotency-Key`, with event transaction identity remaining a separate deduplication mechanism

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
