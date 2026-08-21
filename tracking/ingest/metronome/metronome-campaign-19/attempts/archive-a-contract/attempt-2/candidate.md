---
title: "Metronome API: Archive a Contract"
type: source
date_ingested: 2026-08-21
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/contracts/archive-a-contract.md"
raw_files:
  - "metronome/api-reference/contracts/archive-a-contract-2026-07-13.md"
tags: [metronome, api, contracts, archival, invoicing, credits-and-commits]
---

## Overview

This API reference documents the bearer-authenticated `POST /v1/contracts/archive` operation for permanently ending and archiving an incorrectly created contract together with its terms. Archival cancels draft invoices, voids upcoming scheduled invoices, can optionally void finalized invoices, archives associated commits and credits, and creates expiration ledger entries for remaining active prepaid-commit balances. Archived contracts remain available for historical reporting and audit views, but the page does not define restoration, propagation timing, duplicate-call behavior, concurrency ordering, or partial-failure recovery.

## Key takeaways

- Archival is described as permanent and is intended for a contract that was created incorrectly and needs to be removed from the customer, but it is not deletion: the archived record remains available through `ListContracts` with `include_archived=true` and through the UI's "Show archived" option.
- Draft invoices are canceled and all upcoming scheduled invoices are voided. Finalized invoices are optional: `void_invoices` is a required boolean, and the schema explicitly says existing finalized invoices remain when it is `false`.
- All associated commits and credits are archived. For prepaid commits with active segments, Metronome generates expiration ledger entries that close remaining balances and appear in transaction history as `PREPAID_COMMIT_EXPIRATION`.
- The request schema requires UUID `customer_id`, UUID `contract_id`, and boolean `void_invoices`; the enclosing OpenAPI `requestBody` is not itself marked `required: true`.
- A `200` response requires `data` containing an `Id` object. The page also lists `400` and `404` errors, but it does not enumerate validation cases or distinguish missing customer, missing contract, customer-contract mismatch, or an already archived contract.

## Endpoint contract

| Item | Documented value |
| --- | --- |
| Method and path | `POST /v1/contracts/archive` |
| Operation ID | `archiveContract-v1` |
| Authentication | Top-level HTTP bearer authentication through `bearerAuth` |
| Request media type | `application/json` |
| Required payload properties | UUID `customer_id`, UUID `contract_id`, and boolean `void_invoices` |
| Success | `200`; the response object requires `data`, which uses the required-UUID `Id` schema |
| Listed endpoint errors | `400 Bad request` and `404` for a specified resource that was not found; both use an error object requiring string `message` |

The payload identifies both the customer and the contract. The page does not state whether the customer-contract relationship is validated atomically, what happens when the IDs belong to different customers, or whether an omitted body, extra property, malformed UUID, or inaccessible resource is classified as `400` or `404`. The successful example returns a UUID different from the request's `contract_id`; because the generic `Id` schema does not label that identifier, this page does not establish whether `data.id` is the archived contract ID, an archive-operation ID, or another resource ID.

## Archive, invoice, and balance effects

The operation permanently ends the contract and all its terms. Draft invoices are canceled and upcoming scheduled invoices are voided automatically. Finalized invoices are treated separately: the narrative says they can optionally be voided, the request example sends `void_invoices: true`, and the property description guarantees only that existing finalized invoices remain when the flag is `false`. The page does not define eligible invoice states, the cutoff for "upcoming," whether already distributed scheduled or finalized invoices are affected, or any Stripe, ERP, marketplace, payment, refund, tax, revenue-recognition, webhook, or external accounts-receivable effect.

Associated commits and credits are archived with the contract. For prepaid commits that have active segments, Metronome automatically creates expiration ledger entries to close remaining balances and records them in commit transaction history with type `PREPAID_COMMIT_EXPIRATION`. The page does not define how "associated" applies to customer-level balances shared across contracts, the entry amount or effective timestamp, ordering against invoice deductions, whether the balance and invoice mutations are atomic, or how a partial failure is surfaced and reconciled.

> [!warning] Ledger entry casing ambiguity
> This page renders the generated transaction-history type as uppercase `PREPAID_COMMIT_EXPIRATION`, while the separate remaining-balance guide documents the corresponding ledger type as lowercase `prepaid_commit_expiration`. The sources do not say whether these are surface-specific representations of one value, so clients should verify the actual enum serialization rather than normalize the casing by assumption.

## Historical visibility and permanence

Archival preserves the record for historical reporting and audit purposes. A caller can request archived contracts through `ListContracts` by setting `include_archived` to `true`, and the UI exposes them when "Show archived" is enabled. The page does not define default list behavior, visibility latency, retention, export behavior, audit-event fields, an unarchive or restore operation, or whether a replacement contract can reuse identities or uniqueness keys from the archived contract.

## Authorization, errors, retries, and concurrency

The OpenAPI document applies HTTP bearer authentication but names no endpoint-specific permission or scope and lists no `401` or `403` response. It documents generic `400` and `404` responses with a required message only; it does not list `409`, `429`, or `5xx` behavior or provide machine-readable error codes.

This endpoint page does not mention `Idempotency-Key`, repeated archive calls, request deduplication, or retry guidance. It also does not define concurrency ordering when archival races with invoice generation or finalization, contract edits or transitions, balance consumption, or another archive request. No propagation guarantee, transaction boundary, completion signal beyond the `200` response, timeout-recovery procedure, restoration mechanism, or read-after-write consistency rule is stated. Consult the separate API-wide authentication, status-code, and idempotency authorities, and do not assume that changing an idempotency key or retrying after an uncertain response is safe without reconciling the contract, invoices, balances, and ledger history.

## Contradiction check

The automatic treatment of draft and scheduled invoices and the optional treatment of finalized invoices do not contradict the existing edit guidance that finalized invoices remain unchanged unless separately voided: contract archival is a distinct lifecycle operation with an explicit `void_invoices` control. No direct lifecycle contradiction was found. The ledger-entry casing difference above remains unresolved and is preserved as a documentation ambiguity.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-credits-and-commits]], [[metronome-api-idempotency]], [[metronome-security-principles]]
- API context: [[source-metronome-api-reference-authentication]], [[source-metronome-api-reference-status-codes]], [[source-metronome-api-reference-idempotency]]
- Ledger context: [[source-metronome-guides-customers-billing-optimize-customer-experience-get-remaining-balance]]

## Raw Sources

- [[raw/metronome/api-reference/contracts/archive-a-contract-2026-07-13|2026-07-13 snapshot — contract archival lifecycle, invoice treatment, ledger effects, and request/response schema]]
