---
title: "Metronome API: Disable True-up for a Commit"
type: source
date_ingested: 2026-08-21
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/credits-and-commits/disable-trueup-for-commit.md"
raw_files:
  - "metronome/api-reference/credits-and-commits/disable-trueup-for-commit-2026-07-13.md"
tags: [metronome, api, credits-and-commits, postpaid-commit, true-up]
---

## Overview

This API reference documents globally bearer-secured `POST /v1/contracts/commits/disableTrueup`, an operation that prevents Metronome from generating the true-up invoice for one postpaid commit. It is a narrow invoice-generation control: the page does not define a balance mutation, forgiveness of the unmet commitment, or any downstream accounting effect.

## Key takeaways

- Postpaid-commit usage is paid in arrears. When total payment during the access period is below the committed amount, Metronome otherwise describes a final true-up invoice on `invoice_date`.
- The operation's `requestBody` object is not itself marked required. Within the referenced JSON payload, `customer_id`, `commit_id`, and `contract_id` are required UUID-formatted properties; `amendment_id` is optional when applicable. The page does not define omitted-body runtime behavior.
- The endpoint says the true-up invoice will not be generated. It does not document a cutoff relative to `invoice_date`, retroactive effect, reversal or re-enablement, or already-disabled behavior.
- The `200` schema requires a `data.id` UUID. The operation lists generic `400` and `404` responses but does not map specific failure conditions to them.
- Metronome's separate API-wide [[metronome-api-idempotency|POST idempotency contract]] applies, but this endpoint does not define state-level behavior for another or expired key, concurrent calls, or recovery after cached errors.

## Operation and request contract

The OpenAPI document declares global HTTP bearer security and defines `POST /v1/contracts/commits/disableTrueup`. The operation includes a JSON `requestBody` referencing `DisableCommitTrueupPayload`, but the `requestBody` object has no `required: true` marker. The payload schema itself requires `customer_id`, `commit_id`, and `contract_id`, each UUID-formatted; `amendment_id` is an optional UUID identifying the amendment containing the commit when applicable. This schema distinction does not establish whether an omitted body is accepted or how the runtime reports one.

A successful `200` response requires top-level `data`, whose referenced `Id` schema requires UUID-formatted `id`. The example value matches the submitted `commit_id`, but the generic schema does not independently define that equality as a guarantee. The operation also lists `400 Bad request` with an error body and a referenced `404 Not Found` response; both error schemas require a string `message`, without endpoint-specific condition mapping.

## True-up and lifecycle boundaries

The operation suppresses generation of the final true-up invoice for the identified postpaid commit. The source does not say that it archives, deletes, edits, or resets the commit; changes the access-period usage or paid amount; changes the commit balance or ledger; voids an invoice already generated or finalized; or waives the underlying commercial obligation.

The source also does not specify how late the call may occur relative to `invoice_date`, whether it acts retroactively, whether suppression can be reversed, or whether another API or contract edit can re-enable the invoice. It does not map malformed identifiers, cross-customer or cross-contract mismatches, wrong commit type, already-disabled state, already-generated invoices, repeated calls, concurrency, or timing violations to specific responses. It likewise does not define propagation to ledger entries, balance retrieval, revenue reports, data exports, webhooks, external accounts-receivable systems, or other invoices.

> [!warning] Scope qualification
> Existing descriptions that a shortfall produces a final postpaid true-up invoice need the qualifier that the invoice may be disabled with this endpoint. That is a conditional exception, not evidence that the normal true-up rule or the underlying commit balance is removed.

## Idempotency and retry boundary

The separate [[source-metronome-api-reference-idempotency|Metronome API idempotency reference]] states that `Idempotency-Key` applies to all POST endpoints. Reusing the same key with identical parameters returns the original result; changing parameters with the same key returns HTTP `409 Conflict`; and keys are retained for at least 24 hours. That API-wide contract also says a cached result can be an HTTP `500` error and should be investigated before choosing recovery.

Those guarantees do not define this operation's already-disabled result without a key, replay with a different or expired key, concurrent calls, or `disableTrueup`-specific state recovery after a cached error. A request-result replay contract must not be promoted into an undocumented guarantee about the underlying commit or invoice state.

## Related

- Companies: [[metronome]]
- Concepts: [[metronome-credits-and-commits]], [[metronome-invoicing]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-api-reference-idempotency]] — API-wide POST request-result replay, conflict, retention, and cached-error context

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/disable-trueup-for-commit-2026-07-13|2026-07-13 snapshot — disable-true-up endpoint and OpenAPI schema]]
