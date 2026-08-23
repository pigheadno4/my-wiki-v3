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

This API reference documents the bearer-secured `POST /v1/contracts/customerBalances/list` detailed balance read. Its success payload is an object that requires `data` and nullable `next_page`; `data` is an array whose members use either the Commit or Credit schema. The separate `/getNetBalance` surface remains the single combined customer-balance view.

The JSON payload schema requires `customer_id`, but the enclosing OpenAPI `requestBody` is not marked required. Omitted-body runtime behavior is therefore unknown, and the payload schema does not specify top-level `additionalProperties`, so unknown-field handling must not be inferred.

## Request and pagination

Optional balance selectors are UUID `id`, `covering_date`, `starting_at`, and `effective_before`. The last includes balances with any access before the supplied timestamp and explicitly makes that boundary exclusive. The page does not define what resource `id` identifies, how the three time filters compose, time-zone normalization, or other boundary behavior.

Optional flags request contract-level balances, archived records, ledgers, calculated balances, and feature-gated exclusion of zero balances. `webhook_notification_id` is also feature-gated and skipped from Stainless. No defaults are stated for the balance-inclusion booleans. Both `include_ledgers` and `include_balance` may make the query slower.

This endpoint places `next_page` and `limit` inside the JSON body. Its limit is 1 through 25 and defaults to 25, although the description says "commits" while the response may also contain credits. The separate API-wide pagination reference instead describes `limit` and `next_page` as query parameters and gives general guidance up to 100. Preserve this as an endpoint-specific documentation difference: do not move these fields into the URL or raise this endpoint's limit to 100. Both pages leave ordering, cursor lifetime, invalid-cursor behavior, and cross-page snapshot consistency undefined.

## Response envelope and record schemas

HTTP 200 returns an object requiring `data` and `next_page`; `data` contains the Commit-or-Credit union and `next_page` is a nullable string. Commits require `id`, `type`, `product`, and `created_at`, while credits require `id`, `type`, and `product`. Product objects require UUID `id` and string `name`. The operation documents no non-200 responses, endpoint-specific scopes, rate limits, or validation-error mapping.

Optional record fields cover contract association, access and invoice schedules, applicability, priority, recurrence, rollover origin, subscription allocation, ledgers, calculated balance, custom fields, hierarchy configuration, uniqueness keys, and creator metadata. A lower numeric `priority` is described as applying first when multiple balances are applicable, but this field-level statement does not replace the broader type, rollover, applicability, and schedule ordering rules, and it does not define response-array order.

## Archive asymmetry

The request's exact `include_archived` description is "Include archived credits and credits from archived contracts." Its repeated noun does not establish whether archived commits are returned. Separately, the Commit response schema exposes optional RFC 3339 `archived_at` and says omission means the commit is not archived; the complete Credit schema has no `archived_at` property.

> [!warning] Archive visibility ambiguity
> The contract-archive authority says archiving a contract archives its associated commits and credits. This list schema does not reconcile that lifecycle fact with its asymmetric response: do not infer whether archived commits are returned, how an archived credit exposes archival status, whether credits from archived contracts are themselves archived, or what omitting `include_archived` does.

## Denomination and custom fields

Access-schedule and invoice-schedule amounts are numbers. Each schedule may reference optional `credit_type`; the referenced object requires only UUID `id` and string `name` on this page. The schema does not expose `is_currency` here and independently defines no denomination, precision, conversion, or rounding rule. The example labels one type `USD (cents)`, but that example cannot establish rules for other fiat currencies or custom units. Use [[metronome-currencies-and-custom-pricing-units]] for the platform's documented USD, non-USD, and custom-unit boundaries.

Commit and Credit records can expose optional `custom_fields` through a shared arbitrary-key object whose values are strings. The schema annotates the Commit field with entity `commit` and the Credit field with entity `contract_credit`. It provides no key format, value-length, field-count, visibility, redaction, permission, availability, or unset-value semantics; use [[metronome-custom-fields]] for the broader persistence and entity-scope authority.

## Balance calculation and ledger names

With `include_balance=true`, the numeric balance represents value accessible now: expired and upcoming segments contribute zero. It ordinarily matches ledger sum, except that when negative manual entries exceed the remaining positive amount, calculated balance is floored at zero. Manual entries associated with active segments are included even when future-dated.

> [!warning] Contradiction
> The remaining-balance guide broadly says the signed ledger sum yields the individual remaining balance. This schema adds a material exception: excessive negative manual entries can make the ledger sum negative while the expanded calculated `balance` is zero. Preserve the transaction-history arithmetic separately from the non-negative calculated value.

Ledgers are described as ordered balance-impacting events, but the endpoint does not define their sort key, tie-breakers, late-arrival behavior, or atomic consistency with `balance`. The OpenAPI serialization uses uppercase and often expanded enum tokens, including `PREPAID_COMMIT_EXPIRATION`, `POSTPAID_COMMIT_INITIAL_BALANCE`, and `CREDIT_EXPIRATION`. The remaining-balance guide instead names lowercase and sometimes shorter families such as `prepaid_commit_expiration`, `postpaid_initial_balance`, and `credit_segment_expiration`.

> [!warning] Ledger enum contradiction
> Preserve the exact name documented by each surface. The pages do not establish casing normalization or one-to-one equivalence; `CREDIT_EXPIRATION` versus `credit_segment_expiration` is not merely a casing difference, and the guide also distinguishes two prepaid expiration names while this OpenAPI union exposes one `PrepaidCommitExpirationLedgerEntry`. Verify actual serialization before mapping or aggregating these event types.

## Freshness, retry, and lifecycle unknowns

The overview calls the view real-time but gives no freshness, read-after-write, snapshot-isolation, or cross-page consistency SLA. Amount changes, archive propagation, ledger late arrivals, and concurrent pagination therefore remain unspecified.

Because this read uses POST, the separate API-wide [[metronome-api-idempotency|`Idempotency-Key` authority]] applies: identical parameters with the same key replay the original result, changed parameters conflict, and retention is at least 24 hours. This endpoint does not say whether keyed caching is recommended for a balance read, how replay affects freshness or cursor traversal, or how to recover from an endpoint-specific cached error.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-currencies-and-custom-pricing-units]], [[metronome-custom-fields]], [[metronome-api-idempotency]]
- API conventions: [[source-metronome-api-reference-pagination]], [[source-metronome-api-reference-idempotency]]
- Lifecycle context: [[source-metronome-api-reference-contracts-archive-a-contract]]
- Balance guide: [[source-metronome-guides-customers-billing-optimize-customer-experience-get-remaining-balance]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/list-balances-2026-07-13|2026-07-13 snapshot - List balances API reference]]
