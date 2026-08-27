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

This reference documents bearer-authenticated `POST /v1/contracts/seatBalances/list`, which retrieves credit and commit balances from one customer's contract subscriptions, grouped by individual seat. It is the detailed API authority for customer-dashboard seat balances, optional subscription or seat filtering, and seat-level credit, commit, and nested ledger expansions.

## Query-critical facts

- Within a supplied JSON object, `customer_id` and `contract_id` are required UUID properties. Optional `subscription_ids` restrict results to subscriptions mapped as `SEAT_BASED`; the page says a non-seat-based subscription ID returns an error. Optional `seat_ids` restrict results to named seats.
- Missing requested seat IDs return HTTP `400` by default. `skip_missing_seat_ids: true` instead silently omits them, so a successful response does not prove that every requested seat exists.
- Each result requires `seat_id` and a `balances` array. Every balance item requires `credit_type_id`, current `balance` across all credits and commits for that seat and credit type, and `starting_balance`, the combined initial balance for the same scope. The page does not define currency or custom-unit scaling, precision, rounding, or reconciliation timing.
- `include_credits_and_commits` defaults to `false` and requests seat-level `commits` and `credits` arrays alongside `balances`. `include_ledgers` defaults to `false` and applies only when that first expansion is `true`; each expanded credit or commit can carry its own typed amount-and-timestamp ledger history. The sibling credit and commit item schemas do not expose `credit_type_id`, so this response alone cannot map an expanded object or ledger to a particular per-credit-type `balances` entry.
- Body `limit` controls seats, ranges from 1 to 100, and defaults to 25. Body `cursor` accepts a prior page token; HTTP `200` requires `data` plus `pagination`, whose required counts distinguish seats returned from seats available for the next page. The nullable `next_page` property is documented but is not required by the pagination schema.
- When credit/commit details are requested and their cross-seat total exceeds 100, the page says a total-detail limit of 100 applies and seats are included greedily, yet its example returns two complete seats containing 108 commits. Treat 100 as an inclusion threshold that can be exceeded at a seat boundary, not as a hard maximum number of detail objects returned.

## Material boundaries and contradictions

> [!warning] Sibling expansion schemas do not establish balance attribution or reconciliation
> `balances`, `commits`, and `credits` are sibling fields of a seat object. Only a `balances` item exposes `credit_type_id`; the expanded commit and credit schemas do not. In the success example, seat 1's sole balance item reports current `30000` and starting `50000`, matching the expanded commit's current balance and segment-start amount, while a separate expanded credit reports current `20000` and a `25000` segment-start amount. The page does not identify either expanded record's credit type or establish whether or how the sibling figures reconcile. Do not attribute an expanded credit, commit, or ledger to a per-credit-type balance from this response alone.

> [!warning] Date-filter names conflict across prose and schema
> The usage guideline says to choose `covering_date` or `starting_at`/`ending_before`, and the `covering_date` schema repeats `ending_before`. The actual request properties contain `starting_at`, `effective_before`, and `covering_date`, not `ending_before`; `effective_before` is described as including items effective **on or before** the supplied time. The page does not resolve which upper-bound field name the runtime accepts or whether the upper bound is inclusive. Verify the live contract before implementation.

> [!warning] Documented HTTP 400 paths are absent from the response map
> Property descriptions say non-`SEAT_BASED` subscription IDs and missing requested seats can return an error or HTTP `400`, but the operation response map lists only `200` and generic `404`. The page does not define error bodies or whether mixed valid and invalid subscription IDs fail atomically.

- Neither the enclosing `requestBody` nor the JSON media type is marked required; only properties inside the object are required. Omitted-body runtime behavior is therefore undocumented. The request object also does not declare `additionalProperties: false`, so unknown-field behavior is undocumented.
- The page defines no seat ordering, greedy-selection order or tie-breaker, cursor lifetime, snapshot consistency, duplicate/skip behavior during concurrent balance changes, freshness, retention, authorization scope, rate limits, or broader reconciliation guarantee.
- The separate API-wide `Idempotency-Key` authority applies to this POST read. An identical same-key retry can replay the original result rather than prove a fresh seat-balance view; this endpoint adds no cursor-replay, cached-error, concurrent-update, or recovery semantics.

## Raw-detail coverage map

Use the raw snapshot for the complete request-property catalog and example; customer, contract, subscription, and seat identifiers; missing-seat behavior; the conflicting `effective_before`/`ending_before` time-window descriptions; expansion flags; the seat limit, greedy detail-threshold example, and body cursor; success pagination counts; the sibling placement of `balances`, `commits`, and `credits`; the absence of `credit_type_id` from expanded credit and commit items; the seat-1 `30000`/`50000` balance and commit versus separate `20000`/`25000` credit example; nullable and required-property distinctions; full ledger schemas and enums; bearer security declaration; and generic `404` response schema.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-credits-and-commits]], [[metronome-subscriptions]], [[metronome-reporting-and-analytics]], [[metronome-api-idempotency]]
- Related concept: [[metronome-customers-and-contracts]]
- Related sources: [[source-metronome-guides-pricing-packaging-subscription-manage-seats]], [[source-metronome-api-reference-credits-and-commits-list-balances]], [[source-metronome-api-reference-pagination]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/list-seat-balances-2026-07-13|2026-07-13 snapshot - seat-balance scope, sibling expansion schemas, example reconciliation ambiguity, filters, pagination, completeness limits, and ledger enums]]