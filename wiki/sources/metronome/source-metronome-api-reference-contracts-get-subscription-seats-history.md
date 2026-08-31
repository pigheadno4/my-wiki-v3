---
title: "Metronome API Reference: Get Subscription Seats History"
type: source
date_ingested: 2026-08-31
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/contracts/get-subscription-seats-history"
raw_files:
  - "metronome/api-reference/contracts/get-subscription-seats-history-2026-07-13.md"
tags: [metronome, api, contracts, subscriptions, seats, temporal-history]
---

## Overview

Bearer-authenticated `POST /v1/contracts/getSubscriptionSeatsHistory` reads the effective-dated seat schedule for one subscription identified within a customer contract. It can select the segment covering one timestamp or page through range-filtered history, returning each period's total capacity and assigned seat identities; it does not establish whether future scheduled segments are included or whether a multi-page traversal is a stable snapshot.

## Query-critical facts

- Within a supplied JSON object, UUID `customer_id`, `contract_id`, and `subscription_id` are required properties. The enclosing OpenAPI `requestBody` is not marked `required: true`, and the object does not declare `additionalProperties: false`, so omitted-body and unknown-field behavior are not documented. The three identifiers jointly scope the read, but the page does not define mismatch behavior when each UUID exists under a different customer, contract, or subscription relationship.
- `covering_date` asks for the seat-history segment active at one point in time and cannot be combined with `starting_at` or `ending_before`. The range filters may be used together or independently: the lower description includes segments active at or after its timestamp and the upper description includes segments active at or before its timestamp; omission removes the corresponding bound. The page does not define equality and overlap treatment beyond that wording, validate that a lower bound precedes an upper bound, or reconcile the parameter name `ending_before` with its description's "at or before" language.
- Body `limit` defaults to 10 and permits 1 through 10 seat-schedule entries. Body `cursor` consumes the prior response's `next_page`; HTTP `200` requires `data` and nullable `next_page` as siblings. Results are ordered by `starting_at`, but direction and tie handling are unspecified. The endpoint does not define cursor lifetime, snapshot consistency across pages, behavior when schedules change during traversal, or an endpoint-specific completeness guarantee.
- Each object directly inside `data` requires `starting_at`, nullable `ending_before`, `total_quantity`, and `assigned_seat_ids`. `total_quantity` is a non-negative integer covering assigned plus unassigned seats, while `assigned_seat_ids` contains only assigned identities. A null entry-level `ending_before` means the period is ongoing; these fields are immediate children of each array item, not nested under another schedule object, and `next_page` remains outside `data`.
- The page calls this seat-schedule history and shows an ongoing segment, but it does not say whether results contain only recorded effective state, also include future scheduled seat changes, retain all past periods, or reconcile exactly with the separate quantity-history, contract-state, seat-balance, invoice, credit, or ledger surfaces. The separate quantity-history page explicitly excludes future quantity changes; that boundary must not be generalized to this endpoint without authority.
- The documented HTTP `400` object requires `code` and `message`, with `ContractNotFound`, `CustomerNotFound`, `SubscriptionNotFound`, and `InvalidArgument` codes. The page gives no code-to-condition mapping and no endpoint-specific authorization, malformed-UUID, identifier-relationship, empty-result, rate-limit, timeout, retry, partial-page, freshness, read-after-edit, or recovery contract.
- The separate API-wide authority applies `Idempotency-Key` result replay to all POST endpoints. For this read, an identical same-key retry can recover the original result, but replay is not evidence of a fresh seat schedule, a new pagination snapshot, or current assignment state; the endpoint adds no local guarantee for another or expired key, concurrent reads and edits, cursor replay, cached errors, or ambiguous failures.

## Material boundaries and tensions

> [!warning] Upper-bound naming tension
> The request property is named `ending_before`, while its description says to include segments active "at or before" the supplied timestamp. The page does not define whether the cutoff is exclusive, inclusive, or evaluated against any overlap with a segment; consumers should not derive exact boundary logic from the name alone.

A null segment `ending_before` establishes an ongoing period in the returned representation, not that the segment is the authoritative current state at read time or that no future replacement is scheduled. Likewise, ordered pages do not prove retained-history exhaustiveness or a transactionally consistent snapshot. Reconcile operational access, billing capacity, credits, invoices, and current contract state through their dedicated authorities rather than treating this history read as proof of downstream convergence.

API-wide same-key POST replay can preserve an earlier response. It must not be used as a freshness check after seat edits, and this endpoint supplies no read-after-write delay, cache invalidation, mutation-to-history propagation, or concurrent-edit ordering guarantee.

## Raw-detail coverage map

- **Operation and identity:** use the raw page for the production path, POST method, bearer-security declaration, operation ID, request example, the three required UUID properties inside a supplied payload, and the absence of operation-level request-body requiredness or a closed-object declaration.
- **Temporal selection:** use raw for `covering_date` exclusivity, independent lower and upper range fields, exact "active at or after" and "active at or before" descriptions, nullable fields, and unbounded-side behavior.
- **Pagination and order:** use raw for the 1-10 body limit, default 10, body `cursor`, required nullable sibling `next_page`, sample cursor, and the documented `starting_at` ordering statement; direction, ties, cursor stability, and snapshot completeness remain unspecified.
- **Schedule representation:** use raw for the complete immediate-parent entry schema and example periods, including start and end placement, ongoing-null representation, assigned IDs, total assigned-plus-unassigned quantity, and the non-negative quantity constraint.
- **Failure and consistency:** use raw for the complete documented `400` enum and message placement. It provides no additional status catalog, retention, future-state, freshness, propagation, read-after-write, concurrency, retry, or reconciliation contract.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-subscriptions]], [[metronome-customers-and-contracts]], [[metronome-reporting-and-analytics]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-api-reference-contracts-get-subscription-quantity-history]], [[source-metronome-guides-pricing-packaging-subscription-manage-seats]], [[source-metronome-api-reference-pagination]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/contracts/get-subscription-seats-history-2026-07-13|2026-07-13 snapshot - subscription and contract identity, covering-date and range filters, ordered paginated seat-schedule entries, quantity and assignment placement, and documented errors]]
