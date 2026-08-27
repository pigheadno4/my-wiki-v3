---
title: "Metronome List Seat Balances API"
type: source
date_ingested: 2026-08-27
canonical_url: "https://docs.metronome.com/api-reference/credits-and-commits/list-seat-balances.md"
original_format: webpage
raw_files:
  - "metronome/api-reference/credits-and-commits/list-seat-balances-2026-07-13.md"
tags: [metronome, api, seat-balances, credits, commits, pagination]
---

## Overview

This reference documents bearer-authenticated `POST /v1/contracts/seatBalances/list`, which retrieves credit and commit balances from one customer's contract subscriptions, grouped by individual seat. It is the detailed API authority for customer-dashboard seat balances, optional subscription or seat filtering, credit/commit expansion, and per-balance ledger expansion.

## Query-critical facts

- Within a supplied JSON object, `customer_id` and `contract_id` are required UUID properties. Optional `subscription_ids` restrict results to subscriptions mapped as `SEAT_BASED`; the page says a non-seat-based subscription ID returns an error. Optional `seat_ids` restrict results to named seats.
- Missing requested seat IDs return HTTP `400` by default. `skip_missing_seat_ids: true` instead silently omits them, so a successful response does not prove that every requested seat exists.
- Each result requires `seat_id` and a `balances` array. Every balance item requires `credit_type_id`, current `balance` across all credits and commits for that seat and credit type, and `starting_balance`, the combined initial balance for the same scope. The page does not define currency or custom-unit scaling, precision, rounding, or reconciliation timing.
- `include_credits_and_commits` defaults to `false` and requests the contributing credit and commit records. `include_ledgers` defaults to `false` and applies only when that first expansion is `true`; returned detail identifies each credit or commit and its seat-specific current balance and can include typed amount-and-timestamp transaction history.
- Body `limit` controls seats, ranges from 1 to 100, and defaults to 25. Body `cursor` accepts a prior page token; HTTP `200` requires `data` plus `pagination`, whose required counts distinguish seats returned from seats available for the next page. The nullable `next_page` property is documented but is not required by the pagination schema.
- When credit/commit details are requested and their cross-seat total exceeds 100, the page says a total-detail limit of 100 applies and seats are included greedily, yet its example returns two complete seats containing 108 commits. Treat 100 as an inclusion threshold that can be exceeded at a seat boundary, not as a hard maximum number of detail objects returned.

## Material boundaries and contradictions

> [!warning] Date-filter names conflict across prose and schema
> The usage guideline says to choose `covering_date` or `starting_at`/`ending_before`, and the `covering_date` schema repeats `ending_before`. The actual request properties contain `starting_at`, `effective_before`, and `covering_date`, not `ending_before`; `effective_before` is described as including items effective **on or before** the supplied time. The page does not resolve which upper-bound field name the runtime accepts or whether the upper bound is inclusive. Verify the live contract before implementation.

> [!warning] Documented HTTP 400 paths are absent from the response map
> Property descriptions say non-`SEAT_BASED` subscription IDs and missing requested seats can return an error or HTTP `400`, but the operation response map lists only `200` and generic `404`. The page does not define error bodies or whether mixed valid and invalid subscription IDs fail atomically.

- Neither the enclosing `requestBody` nor the JSON media type is marked required; only properties inside the object are required. Omitted-body runtime behavior is therefore undocumented. The request object also does not declare `additionalProperties: false`, so unknown-field behavior is undocumented.
- The page defines no seat ordering, greedy-selection order or tie-breaker, cursor lifetime, snapshot consistency, duplicate/skip behavior during concurrent balance changes, freshness, retention, authorization scope, rate limits, or reconciliation guarantee.
- The separate API-wide `Idempotency-Key` authority applies to this POST read. An identical same-key retry can replay the original result rather than prove a fresh seat-balance view; this endpoint adds no cursor-replay, cached-error, concurrent-update, or recovery semantics.

## Raw-detail coverage map

Use the raw snapshot for the complete request-property catalog and example; customer, contract, subscription, and seat identifiers; missing-seat behavior; the conflicting `effective_before`/`ending_before` time-window descriptions; expansion flags; the seat limit, greedy detail-threshold example, and body cursor; success pagination counts; seat, balance-by-credit-type, credit, commit, and ledger schemas; nullable and required-property distinctions; full ledger-entry enums; bearer security declaration; and generic `404` response schema.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-credits-and-commits]], [[metronome-subscriptions]], [[metronome-reporting-and-analytics]], [[metronome-api-idempotency]]
- Related concept: [[metronome-customers-and-contracts]]
- Related sources: [[source-metronome-guides-pricing-packaging-subscription-manage-seats]], [[source-metronome-api-reference-credits-and-commits-list-balances]], [[source-metronome-api-reference-pagination]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/list-seat-balances-2026-07-13|2026-07-13 snapshot - seat-balance scope, filters, pagination, completeness limits, response schemas, and ledger enums]]