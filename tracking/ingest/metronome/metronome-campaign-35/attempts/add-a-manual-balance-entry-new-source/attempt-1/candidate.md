---
title: "Metronome API Reference: Add a Manual Balance Entry"
type: source
date_ingested: 2026-09-01
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/credits-and-commits/add-a-manual-balance-entry"
raw_files:
  - "metronome/api-reference/credits-and-commits/add-a-manual-balance-entry-2026-08-28.md"
tags: [metronome, credits-and-commits, balances, ledgers, api]
---

## Overview

This OpenAPI page documents bearer-authenticated `POST /v1/contracts/addManualBalanceLedgerEntry`, which changes one commit or credit segment's available balance by appending a new manual ledger event. It is a targeted balance-correction surface, not an authority that the underlying usage, contract pricing, invoice, payment, or downstream accounting state has been recalculated or reconciled.

## Query-critical facts

- The mutation identifies the customer, the commit-or-credit balance, and the target segment through required UUID-formatted `customer_id`, `id`, and `segment_id` properties in a supplied JSON payload. `contract_id` is optional; leaving it blank targets a customer-level balance. The enclosing OpenAPI `requestBody` is not marked required, and the payload schema does not declare `additionalProperties`, so omitted-body and unknown-field behavior are undocumented.
- `amount` is required and is added to the segment; a negative value draws the balance down. The endpoint does not define denomination, pricing unit, precision, rounding, a zero-value rule, numeric bounds, or whether a negative entry can make ledger arithmetic negative even when another balance view floors its displayed result.
- `reason` is required by the payload schema and displayed in the ledger, while the narrative says a description is optional. The page does not expose a separate `description` property, so copy-ready clients should follow the schema's `reason` requirement and preserve the narrative/schema wording conflict.
- Optional `timestamp` is an RFC 3339 effective time and defaults to the start of the segment when omitted. For individually configured commits or credits attached to seat-managed subscriptions, optional `per_group_amounts` supplies an amount per seat and must sum to total `amount`; the page does not define group-key identity, omitted-seat behavior, or validation and atomicity when the map and total disagree.
- The page positions manual entries as discrepancy resolution for malformed usage, invalid configuration, untracked outage usage, or an increase on an existing credit or commit. It separately says most inaccurate-billing corrections can instead be made upstream through contract editing, rate editing, or another action that recalculates an invoice. A manual balance event alone therefore does not establish corrected usage, repricing, invoice regeneration, refund, payment, tax, revenue posting, or external A/R reconciliation.
- HTTP `200` is documented only as `Success` with no response content schema, operation identifier, returned ledger entry, or immediate-parent response object. Generic `400` and `404` errors are listed. The page does not define authorization failures, identifier-relationship validation, duplicate-call behavior without a key, reversal, concurrent adjustment ordering, partial effects, read-after-write visibility, webhook or export propagation, or recovery after a timeout or ambiguous failure.
- Optional 1-128 character `uniqueness_key` is a resource-level duplicate guard: reuse prevents a new record and is documented to fail with HTTP `409`, although `409` is absent from the operation response map. This is distinct from the API-wide [[source-metronome-api-reference-idempotency|`Idempotency-Key` authority]] for POST requests. Under that separate authority, Metronome persists a result only after execution begins—after validation and without a pre-execution concurrent-request conflict—then identical same-key parameters replay the persisted original result and changed parameters return `409`. Validation failures and pre-execution concurrency conflicts are not established cached results, and replay is not fresh proof of ledger, balance, invoice, or downstream state. The authorities do not define the two keys' interaction, uniqueness-key scope or release, another- or expired-header-key behavior, endpoint-specific concurrency, propagation, or ambiguous-failure recovery.

## Material boundaries and contradictions

> [!warning] Reason requiredness conflict
> The narrative says a description is optional, but the only corresponding payload property is `reason`, and `reason` is required. No separate `description` field is documented. Treat `reason` as required for a supplied payload unless current runtime authority establishes otherwise.

The endpoint appends a new event rather than rewriting ledger history, but it does not define a compensating-entry or deletion API, actor identity beyond bearer authentication, audit-log linkage, entry visibility timing, or whether the balance change and any derived views update atomically. Its correction examples are operational guidance, not accounting, tax, refund, entitlement, incident-credit, or customer-communication policy.

## Raw-detail coverage map

Use the exact raw page for the production server and global bearer-security declaration; operation ID; complete narrative use cases and upstream-correction guidance; request example; all payload identifiers and descriptions; required-property list; customer-level versus contract-level targeting; signed amount behavior; seat-level `per_group_amounts` map and sum constraint; reason wording; RFC 3339 timestamp default; uniqueness-key bounds and duplicate-error wording; generic error-object schema; `200`, `400`, and `404` response declarations; shared tag descriptions; and every schema openness or omitted-behavior boundary. The raw page is the deep-dive authority for those details; this source does not reconstruct a complete request or error catalog.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-api-idempotency]]
- Secondary concept: [[metronome-subscriptions]]
- Related sources: [[source-metronome-guides-customers-billing-optimize-customer-experience-get-remaining-balance]], [[source-metronome-api-reference-credits-and-commits-list-balances]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/add-a-manual-balance-entry-2026-08-28|2026-08-28 snapshot - manual commit-or-credit ledger mutation, signed adjustment, effective-time and seat allocation fields, duplicate guard, responses, and correction boundary]]
