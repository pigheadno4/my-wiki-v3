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
- `amount` is required and is added to the segment; a negative value draws the balance down. The separate remaining-balance authority establishes that balance-ledger amounts may be fractional and that USD amounts are cents. This endpoint itself does not define non-USD or custom-unit selection, precision, rounding, a zero-value rule, or numeric bounds. The detailed-balance authority further establishes that excessive negative manual entries can leave signed ledger arithmetic negative while the calculated balance is floored at zero; that calculated-view rule is not an endpoint-local atomicity or read-after-write guarantee.
- `reason` is required by the payload schema and displayed in the ledger, while the narrative says a description is optional. The page does not expose a separate `description` property, so copy-ready clients should follow the schema's `reason` requirement and preserve the narrative/schema wording conflict.
- Optional `timestamp` is an RFC 3339 effective time and defaults to the start of the segment when omitted. The separate detailed-balance authority says manual entries associated with active segments contribute to calculated balance even when future-dated; it does not establish when this mutation becomes visible or whether ledger and calculated views update atomically. For individually configured commits or credits attached to seat-managed subscriptions, optional `per_group_amounts` supplies an amount per seat and must sum to total `amount`; the page does not define group-key identity, omitted-seat behavior, or validation and atomicity when the map and total disagree.
- The resulting manual adjustment is represented in ledger-family terminology as `credit_manual`, `prepaid_manual`, or `postpaid_manual` for a credit, prepaid commit, or postpaid commit respectively. Those names come from the separate remaining-balance authority; this endpoint does not return an entry representation or identify the serialized type in its HTTP `200` response.
- The page positions manual entries as discrepancy resolution for malformed usage, invalid configuration, untracked outage usage, or an increase on an existing credit or commit. It separately says most inaccurate-billing corrections can instead be made upstream through contract editing, rate editing, or another action that recalculates an invoice. A manual balance event alone therefore does not establish corrected usage, repricing, invoice regeneration, refund, payment, tax, revenue posting, or external A/R reconciliation.
- HTTP `200` is documented only as `Success` with no response content schema, operation identifier, returned ledger entry, or immediate-parent response object. Generic `400` and `404` errors are listed. The page does not define authorization failures, identifier-relationship validation, duplicate-call behavior without a key, reversal, concurrent adjustment ordering, partial effects, read-after-write visibility, webhook or export propagation, or recovery after a timeout or ambiguous failure.
- Optional 1-128 character `uniqueness_key` is a resource-level duplicate guard: reuse prevents a new record and is documented to fail with HTTP `409`, although `409` is absent from the operation response map. This is distinct from the API-wide [[source-metronome-api-reference-idempotency|`Idempotency-Key` authority]], which recommends a dedicated `uniqueness_key` when available. For a provided header key, Metronome persists a result only after execution begins—after validation and without a pre-execution concurrent-request conflict. It then replays the persisted original result for identical same-key parameters, returns `409` for changed parameters, retains keyed results for at least 24 hours, and persists and replays an admitted HTTP `500` result. Validation failures and pre-execution concurrency conflicts are not established cached results. After a cached or ambiguous failure, investigate system state rather than assuming a different key is safe; replay is not fresh proof of ledger, balance, invoice, or downstream state. The authorities do not define the two keys' interaction, uniqueness-key scope or release, another- or expired-header-key behavior, endpoint-specific concurrency or ledger state, propagation, or recovery.

## Material boundaries and contradictions

> [!warning] Reason requiredness conflict
> The narrative says a description is optional, but the only corresponding payload property is `reason`, and `reason` is required. No separate `description` field is documented. Treat `reason` as required for a supplied payload unless current runtime authority establishes otherwise.

The endpoint describes creation as appending a new event rather than rewriting an existing entry. That wording is not a global append-only or permanent-retention guarantee: the current contract-edit authority says removing an access-schedule segment also removes its manual ledger entry. The endpoint itself does not define a general compensating-entry or deletion API, actor identity beyond bearer authentication, audit-log linkage, entry visibility timing, or whether the balance change and derived views update atomically. Its correction examples are operational guidance, not accounting, tax, refund, entitlement, incident-credit, or customer-communication policy.

## Raw-detail coverage map

Use the exact raw page for the production server and global bearer-security declaration; operation ID; complete narrative use cases and upstream-correction guidance; request example; all payload identifiers and descriptions; required-property list; customer-level versus contract-level targeting; signed amount behavior; seat-level `per_group_amounts` map and sum constraint; reason wording; RFC 3339 timestamp default; uniqueness-key bounds and duplicate-error wording; generic error-object schema; `200`, `400`, and `404` response declarations; shared tag descriptions; and every schema openness or omitted-behavior boundary. Use the linked remaining-balance, detailed-balance, contract-edit, and API-wide idempotency authorities for the scoped ledger denomination, manual-entry family, calculated-balance, access-segment-removal, and retry facts above. The assigned raw page remains the deep-dive authority for its endpoint details; this source does not reconstruct a complete request or error catalog.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-api-idempotency]]
- Secondary concept: [[metronome-subscriptions]]
- Related sources: [[source-metronome-guides-customers-billing-optimize-customer-experience-get-remaining-balance]], [[source-metronome-api-reference-credits-and-commits-list-balances]], [[source-metronome-guides-pricing-packaging-make-pricing-changes-edit-contract]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/add-a-manual-balance-entry-2026-08-28|2026-08-28 snapshot - manual commit-or-credit ledger mutation, signed adjustment, effective-time and seat allocation fields, duplicate guard, responses, and correction boundary]]
