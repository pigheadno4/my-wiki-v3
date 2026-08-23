---
title: "List balances"
type: source
date_ingested: 2026-08-23
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/credits-and-commits/list-balances.md"
raw_files:
  - "metronome/api-reference/credits-and-commits/list-balances-2026-07-13.md"
tags: [metronome, api-reference, credits-and-commits, balances, ledgers, pagination]
---

## Overview

This API reference documents `POST /v1/contracts/customerBalances/list`, Metronome's detailed customer-balance read. It returns individual commit and credit records, optionally expanding each calculated balance and ordered ledger, while `/getNetBalance` remains the separate single combined-balance view.

The operation is globally bearer-secured. Although the JSON schema requires `customer_id`, the enclosing OpenAPI `requestBody` is not marked required, so omitted-body runtime behavior is not established.

## Key takeaways

- The response is a paginated array whose members are either commits (`PREPAID` or `POSTPAID`) or credits (`CREDIT`); HTTP 200 requires both `data` and nullable `next_page`.
- Optional access-window filters are `covering_date`, `starting_at`, and exclusive `effective_before`. An optional UUID `id` is also accepted, but the page does not describe whether it identifies a credit, a commit, or either.
- `include_balance` and `include_ledgers` request calculated balances and ledger history, respectively, and the page warns that either expansion may make the query slower. `include_contract_balances` requests contract-level balances.
- Pagination uses a request-body `next_page` cursor and an endpoint-specific `limit` from 1 through 25, defaulting to 25. This is narrower than the separate API-wide pagination page's general 100-item cap.
- A calculated balance counts expired and upcoming access segments as zero. It ordinarily matches the sum of ledger entries, except that excessive negative manual adjustments cannot push it below zero; future-dated manual entries tied to active segments are included.
- The schema defines numeric amounts but no universal precision, rounding, currency-exponent, conversion, or display rule. Interpret amounts with their `credit_type` rather than assuming every balance is an integer fiat amount.

## Request contract

The JSON object requires only UUID `customer_id` inside the payload schema. The operation also accepts:

- UUID `id`, without documented identity semantics.
- `covering_date` for schedules covering a date, `starting_at` for any access on or after a date, and `effective_before` for any access before an exclusive cutoff. The page does not define how these filters compose, time-zone normalization, or boundary behavior beyond the stated exclusivity.
- `include_contract_balances`, `include_archived`, `include_ledgers`, and `include_balance`. No defaults are supplied for these booleans.
- Feature-gated `exclude_zero_balances`, plus a skipped, feature-gated `webhook_notification_id` that marks a request as webhook-triggered. Their general availability is not established.
- `next_page` and `limit`; the limit description says "commits" even though the response can also contain credits.

The request schema does not specify top-level `additionalProperties`, so unknown-field handling must not be inferred. No non-200 responses or endpoint-specific authorization scopes, rate limits, invalid-cursor behavior, or validation-error mappings are documented.

## Response shape

HTTP 200 returns `data` plus nullable `next_page`. Each `data` member is a `Commit` or `Credit`. Commits require `id`, `type`, `product`, and `created_at`; credits require `id`, `type`, and `product`. Product objects require their own `id` and `name`. Other optional fields can describe contract association, access and invoice schedules, applicability, priority, recurring or rollover origin, subscription allocation, custom fields, hierarchy access, uniqueness keys, archival time, and creator metadata.

Access schedules contain typed amount segments with inclusive-looking `starting_at` and `ending_before` fields, but this page does not explicitly define their boundary operators. Commit invoice schedules can include amount, unit price, quantity, timestamp, nullable invoice ID, and `do_not_invoice`; the endpoint is a read and does not define how those values were validated or mutated.

The `priority` descriptions say the lower value applies first when several balances are applicable. That field-level statement does not replace the broader credits-and-commits authority's type, rollover, applicability, and schedule ordering rules, and the endpoint does not document response-array order.

## Balance and ledger semantics

`include_balance=true` exposes the current usable amount for each returned credit or commit. Expired and upcoming segments contribute zero. The value matches ledger sum except when negative manual entries exceed the positive remaining amount, in which case it is floored at zero. All manual entries associated with active segments contribute, including future-dated manual entries.

> [!warning] Contradiction
> The existing remaining-balance guide says summing every signed ledger entry yields an individual ledger's remaining balance. This endpoint's schema adds a material exception: excessive negative manual entries do not produce a negative calculated balance; the returned balance is zero. Preserve the signed ledger as transaction history and do not assume its arithmetic sum always equals the expanded `balance`.

With `include_ledgers=true`, commit and credit ledgers are described as ordered balance-impacting events. The schema distinguishes start, automated invoice deduction, rollover, expiration, cancellation, credited, manual, true-up, and seat-adjustment variants according to balance type. Required fields vary by event; for example, several events require a segment or invoice UUID, while manual entries require a reason. The page does not define ordering keys or tie-breakers, late-arriving entry behavior, or snapshot consistency between the returned ledger, balance, and pagination cursor.

## Archive, freshness, and retry boundaries

`include_archived` is described as including "archived credits and credits from archived contracts." The repeated noun leaves archived-commit behavior unresolved. Likewise, `include_contract_balances=true` establishes an opt-in for contract-level balances but the page does not state the false or omitted default, hierarchy behavior, or interaction with customer-level balances.

The overview calls the view real-time, but supplies no freshness, read-after-write, snapshot-isolation, or cross-page consistency guarantee. Concurrent balance changes could therefore affect a multi-page traversal in undocumented ways.

Because this read uses POST, the separate API-wide [[metronome-api-idempotency|`Idempotency-Key` authority]] applies: identical parameters with the same key replay the original result, changed parameters conflict, and retention is at least 24 hours. This endpoint does not say whether keyed caching is recommended for a balance read, how it affects freshness or cursor traversal, or how to recover from an endpoint-specific cached error.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-api-idempotency]]
- API conventions: [[source-metronome-api-reference-pagination]], [[source-metronome-api-reference-idempotency]]
- Balance guide: [[source-metronome-guides-customers-billing-optimize-customer-experience-get-remaining-balance]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/list-balances-2026-07-13|2026-07-13 snapshot - List balances API reference]]
