---
title: "Metronome List Credit Ledger Entries API"
type: source
date_ingested: 2026-08-27
canonical_url: "https://docs.metronome.com/api-reference/credit-grants/list-credit-ledger-entries.md"
original_format: webpage
raw_files:
  - "metronome/api-reference/credit-grants/list-credit-ledger-entries-2026-07-13.md"
tags: [metronome, api, credit-grants, ledgers, pagination]
---

## Overview

This reference documents bearer-authenticated `POST /v1/credits/listEntries`, which returns credit ledgers grouped by customer on Metronome's deprecated Plans surface. Metronome directs new clients to Contracts, but this page does not identify an equivalent Contracts operation or migration mapping.

## Query-critical facts

- The optional JSON object can filter by customer UUIDs and credit-type UUIDs. Omitting either property broadens that dimension to all customers or all credit types; neither the payload nor its enclosing `requestBody` is marked required.
- `starting_on` is inclusive by ledger-entry `effective_at`. `ending_before` is exclusive, cannot be in the future, and defaults the upper boundary to the start of each customer's next billing period when omitted.
- The prose states that entries inside the returned ledgers are chronological. Separately, optional query `sort` orders ledgers by date as `asc` or `desc` and defaults to ascending. The page does not define the ledger sort key, tie-breakers, whether `sort` changes entry order inside each ledger, or ordering across customers, credit types, and response pages.
- Optional query `next_page` is a string cursor; HTTP `200` requires a customer-ledger array under `data` and nullable `next_page`. The page defines no page size, cursor lifetime, snapshot consistency, or duplicate/skip behavior during concurrent ledger changes.
- Each returned customer item requires `customer_id` and a `ledgers` array. Every credit-type ledger requires its credit type, starting and ending balances, posted `entries`, and `pending_entries`; each balance separates `excluding_pending` from `including_pending` and carries an effective timestamp.
- A ledger entry requires amount, reason, running balance, effective time, creator, and related credit-grant UUID. Optional nullable `invoice_id` links a deduction to the invoice that consumed it or a grant to the invoice that charged its `paid_amount`.

## Material boundaries and contradiction

- Entries associated with voided credit grants are excluded. The endpoint therefore is not a complete history of every grant-related entry and must not be used alone to reconstruct voided-grant activity.
- This legacy entry schema does not expose a ledger-entry type, and its Plans-specific shape must not be conflated with current Contracts balance and ledger schemas. The page supplies no Plan-to-Contract identity mapping, replacement route, migration procedure, or removal date.

> [!warning] Positive deduction amount conflicts with the shown balance change
> The success example starts with both balances at `400`, keeps ending `excluding_pending` at `400`, but lowers ending `including_pending` and the pending entry's `running_balance` to `110`. The pending entry is an automated invoice deduction whose `amount` is positive `290`, even though the schema describes `amount` as the change to the customer's credit balance. A literal positive change does not reconcile with the shown `400` to `110` decrease. The page does not resolve whether legacy Plans deduction amounts are unsigned magnitudes, whether a sign is missing from the example, or whether another calculation convention applies. Do not import the current Contracts signed-entry model into this endpoint.

- The request object does not declare `additionalProperties: false`, so unknown-field handling is undocumented. Only a generic HTTP `404` is listed; authorization scope, rate limits, malformed-cursor behavior, freshness, cache behavior, and other failures are not defined here.
- The separate API-wide `Idempotency-Key` authority applies to this POST read. An identical same-key retry can replay the original result rather than prove a fresh ledger view; this endpoint adds no cursor-replay, concurrent-update, cached-error, or recovery semantics.

## Raw-detail coverage map

Use the raw snapshot for the complete request filters and example, cursor definition, the distinct entry-chronology and ledger-sort statements, unresolved sort key and cross-page ordering, response envelope, the positive-`290` deduction versus `400`-to-`110` balance example, customer and credit-type grouping schemas, starting and ending balance calculations, posted and pending entry fields, invoice linkage, bearer security declaration, and generic `404` response schema.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-api-reference-credits-and-commits-list-balances]], [[source-metronome-guides-customers-billing-optimize-customer-experience-get-remaining-balance]], [[source-metronome-api-reference-credit-grants-void-a-credit-grant]], [[source-metronome-api-reference-pagination]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/credit-grants/list-credit-ledger-entries-2026-07-13|2026-07-13 snapshot - deprecated Plans credit-ledger listing, filters, pagination, ordering boundaries, balance example, and entry schema]]