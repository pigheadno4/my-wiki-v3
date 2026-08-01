---
title: "Metronome API Reference: Regenerate an Invoice"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/invoices/regenerate-an-invoice"
raw_files:
  - "metronome/api-reference/invoices/regenerate-an-invoice-2026-07-13.md"
tags: [metronome, invoices, invoice-regeneration, billing-corrections, billing-providers, api]
---

## Overview

This API reference documents Metronome's invoice-regeneration operation. A bearer-authenticated `POST /v1/invoices/regenerate` identifies a voided invoice and recalculates a new invoice from up-to-date rates, available balances, and other fees regardless of billing period. The page also describes configured billing-provider distribution, but it leaves the new invoice's state, delivery outcome, failure behavior, retry safety, and accounting effects undefined.

## Key takeaways

- The operation description scopes regeneration to a voided invoice and says the replacement is recalculated from up-to-date rate terms, available balances, and other fees, regardless of billing period. It does not define an as-of timestamp, snapshot boundary, or atomicity for those inputs.
- The prose says the regenerated invoice ID is distinct from the previously voided invoice, but the request and response examples show the same UUID. The schema constrains UUID format only and does not resolve that identity contradiction.
- If the invoice is attached to a contract with a billing provider, the page says the regenerated invoice will be distributed according to that configuration. It does not identify the provider, timing, new invoice state, delivery guarantees, or partial-failure behavior.
- The OpenAPI operation uses `POST /v1/invoices/regenerate` with global bearer security. Its JSON object schema requires UUID-formatted `id` within the object, but the `requestBody` itself is not marked required.
- HTTP 200 defines a `data` property whose object requires UUID-formatted `id` when `data` is present, and the example contains `data.id`; the top-level schema does not require `data` and documents no amount, status, recalculation inputs, or distribution result.

## Endpoint contract

| Attribute | Documented value |
| --- | --- |
| Server | `https://api.metronome.com` |
| Method and path | `POST /v1/invoices/regenerate` |
| Authentication | Global `bearerAuth`; HTTP bearer scheme |
| Request media type | `application/json` |
| Request schema | Object with `id` required within the object; `id` is a UUID-formatted string. The operation does not mark `requestBody` itself required. |
| Success response | HTTP 200 with an `application/json` schema that defines optional top-level `data`; within `data`, `id` is required and UUID-formatted. The example contains `data.id`. |
| Operation ID | `regenerateInvoice-v1` |

The request example identifies the invoice to regenerate with UUID `6a37bb88-8538-48c5-b37b-a41c836328bd`. The success example places that same UUID in `data.id`, even though the descriptive prose calls the new invoice ID distinct. Neither the schema nor the examples document the returned invoice object, recalculated amount, status, source invoice ID, or billing-provider delivery state.

## Recalculation and invoice-state boundaries

The endpoint is described as regenerating a voided invoice rather than editing that invoice in place. Its calculation uses up-to-date rates, available balances, and other fees regardless of the billing period, so this page does not establish that the result reproduces the original invoice's pricing or balance application. It also does not define when those inputs are read, whether balance effects are reserved or consumed atomically, how concurrent changes are handled, or how taxes, discounts, credits, commits, rounding, or previously recorded ledger effects are reconciled.

The page supplies no starting-state enum or precondition response beyond calling the input invoice voided. It does not say what happens for a draft, finalized, already-regenerated, nonexistent, or inaccessible invoice, nor whether the old voided invoice is mutated beyond its existing state. The regenerated invoice's draft or finalized state, issue and service dates, lineage fields, and relationship to the old invoice remain undocumented.

A related Metronome correction guide sequences corrected usage, voiding, and regeneration, and separately limits historical usage submission to 34 days. This endpoint's `regardless of the billing period` wording describes invoice recalculation; it does not establish that callers can submit corrected historical usage outside that window or bypass the guide's external invoicing and A/R boundary.

## Distribution and downstream side effects

For an invoice attached to a contract with a billing provider, the page says the regenerated invoice will be distributed based on the configuration. That statement establishes a configured distribution side effect but does not identify supported providers, whether distribution is synchronous, when it occurs, which provider configuration version applies, or how delivery IDs, retries, webhooks, failures, and duplicate deliveries are represented.

The endpoint page does not say that regeneration voids or cancels the old downstream invoice. The related credit-and-rebill guide explicitly assigns downstream voiding to the merchant and says a regenerated invoice using the Metronome Stripe integration is sent to Stripe automatically. This API page does not establish payment collection, refund, tax reversal or recalculation, A/R cancellation, revenue adjustment, credit-memo creation, or ledger reconciliation for any provider.

## Identity contradiction and retry boundary

> [!warning] Documentation contradiction
> The prose says the regenerated invoice ID is distinct from the previously voided invoice, while the request and response examples use the same UUID. The schema only requires UUID format and provides no equality or inequality constraint. Treat neither example equality nor prose distinctness as a verified runtime identity guarantee until Metronome confirms the behavior.

This endpoint page documents only HTTP 200 and no error responses. It does not describe endpoint-specific repeated-call, request-deduplication, concurrency, timeout-recovery, or replay behavior. A separate Metronome idempotency source says all POST endpoints accept `Idempotency-Key`, cache the original result for identical parameters for at least 24 hours, and return HTTP 409 when parameters change. This page neither repeats nor narrows that API-wide contract, so its omission is not evidence that the header is unsupported; it still does not establish regeneration-specific resource state after a cached error or whether a changed key can create or distribute another invoice. Authorization failures, validation failures, not-found behavior, rate limits, and recalculation or distribution observability are also undocumented here.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-invoicing]], [[metronome-integrations]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-guides-invoices-invoice-optimization-issue-credit-memos]], [[source-metronome-api-reference-credits-and-commits-edit-a-commit]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/invoices/regenerate-an-invoice-2026-07-13|2026-07-13 snapshot - invoice regeneration endpoint, recalculation inputs, replacement identity, and billing-provider distribution boundary]]
