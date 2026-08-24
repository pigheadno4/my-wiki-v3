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

## Retry and error boundary

Metronome persists an `Idempotency-Key` result after a request begins execution—that is, after validation and concurrent-request conflict checks. The cached result can be an HTTP `500` error. Reusing that key returns the cached error, so the source recommends investigating system state and deciding whether to resolve manually or retry instead of automatically switching keys after a partial failure.

The best-practice guidance recommends deterministic keys derived from business identity and operation type for resource operations, UUIDs where deterministic identity is unnecessary, exponential backoff, and reuse of the same key within its lifetime. The separate status-code reference advises verifying that a resource was not partially created after a `5XX` response, but its suggestion to retry with a different key must be reconciled with the idempotency page's manual-investigation warning for cached errors.

For periodic usage heartbeats, the event guide gives a concrete deterministic pattern: combine a node identifier with a minute bucket, send at least two heartbeats per measurement period, and rely on transaction-ID duplicate suppression. This event-specific retry pattern does not define safe behavior for other POST operations.

For account-level billing-provider setup, `POST /v1/setUpBillingProvider` falls under the API-wide `Idempotency-Key` guarantee, but its own page documents only generic HTTP 400 and 409 errors and no endpoint-specific retry, concurrency, partial-creation, provider-side deduplication, or recovery semantics. The successful result's UUID `delivery_method_id` is the result that an identical same-key retry should recover under the API-wide authority; after an ambiguous failure, do not assume a changed key is safe or that external-provider state is reconciled. [[source-metronome-api-reference-settings-set-up-account-level-billing-provider]]


`POST /v1/customers/{customer_id}/setName` falls under the API-wide `Idempotency-Key` contract even though its endpoint page lists only HTTP `200` and does not mention retries. An identical same-key retry returns the original mutation result rather than proving a fresh read of the customer's current name; the endpoint adds no behavior for another or expired key, concurrent renames, cached-error customer or document state, or recovery after ambiguous propagation. [[source-metronome-api-reference-customers-update-a-customer-name]] [[source-metronome-api-reference-idempotency]]

## Related platform concepts

- [[metronome-event-ingestion]] owns the usage-event schema, matching, deduplication, and processing boundaries.
- [[metronome-customers-and-contracts]] owns ingest-alias assignment and resource lifecycle.
- [[metronome-credits-and-commits]] covers uniqueness keys on credit and commit creation.

## Sources

- [[source-metronome-guides-events-send-usage-events]] — 34-day transaction-ID duplicate suppression, retry reuse, deterministic heartbeat IDs, and the unqualified-versus-windowed guarantee tension

- [[source-metronome-api-reference-idempotency]] — mechanism selection, key lifetimes, conflict behavior, cached errors, and retry guidance
- [[source-metronome-api-reference-status-codes]] — API-wide conflict, rate-limit, and server-error recovery guidance
- [[source-metronome-guides-implement-metronome-core-concepts-send-usage-events]] — direct-ingest retry safety and deterministic heartbeat identifiers

- [[source-metronome-api-reference-settings-set-up-account-level-billing-provider]] — POST setup mutation, returned configuration identifier, generic conflicts, and endpoint-specific recovery unknowns

- [[source-metronome-api-reference-credits-and-commits-create-a-credit]] - endpoint-specific uniqueness-key schema, duplicate-creation prevention, omitted 409 response-map entry, and interaction unknowns


- [[source-metronome-api-reference-customers-update-a-customer-name]] — POST customer-name mutation, original-result replay context, and endpoint-specific concurrency and recovery unknowns

## Related

- [[metronome]]
- [[metronome-security-principles]]
