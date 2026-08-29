---
title: "Metronome API Reference: Regenerate an Invoice"
type: source
date_ingested: 2026-08-29
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/invoices/regenerate-an-invoice"
raw_files:
  - "metronome/api-reference/invoices/regenerate-an-invoice-2026-08-28.md"
  - "metronome/api-reference/invoices/regenerate-an-invoice-2026-07-13.md"
tags: [metronome, invoices, invoice-regeneration, billing-corrections, billing-providers, api]
---

## Overview

This API reference documents bearer-authenticated `POST /v1/invoices/regenerate`, which takes a voided invoice and recalculates a replacement from up-to-date rates, available balances, and other fees regardless of billing period. It is a correction mutation with possible configured billing-provider distribution, while endpoint-specific state, accounting, delivery, concurrency, and recovery behavior remain limited or undocumented.

## Query-critical facts

- The documented precondition is a voided invoice. Regeneration creates a recalculated invoice rather than editing the voided invoice in place, using current rate terms, available balance, and fees even for another billing period; the page does not define an as-of timestamp, input snapshot, calculation atomicity, or balance and ledger reconciliation.
- When a JSON object is supplied, its UUID-formatted `id` property is required and identifies the invoice to regenerate. The enclosing OpenAPI `requestBody` is not marked required, and the object schema does not declare `additionalProperties`, so omitted-body and unknown-field behavior are not established.
- The prose says the regenerated invoice ID is distinct from the previously voided invoice. In this refreshed snapshot, the request example uses `6a37bb88-8538-48c5-b37b-a41c836328bd` and the response example uses `d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc`, aligning the examples with that statement; the schema itself constrains UUID format but does not encode inequality.
- HTTP `200` defines an optional top-level `data` property; when `data` is present, its object requires UUID-formatted `id`, described as the new invoice ID. The page documents no returned amount, status, source-invoice linkage field, recalculation inputs, or distribution result.
- If the voided invoice is attached to a contract with a billing provider, the regenerated invoice is distributed according to that configuration. The page does not identify the provider, configuration-resolution time, new invoice state, delivery timing, identifiers, webhooks, failures, retries, duplicate-delivery behavior, or downstream outcome.
- Because this is a POST operation, the separate [[source-metronome-api-reference-idempotency|API-wide idempotency authority]] applies `Idempotency-Key` result replay: identical same-key parameters return the original result, changed parameters conflict, retention is at least 24 hours, and a cached result can be HTTP `500`. This endpoint adds no regeneration-specific rule for another or expired key, concurrent calls, timeout recovery, resulting invoice state after an ambiguous failure, or whether a changed key can create and distribute another invoice.

## Material boundaries

`Regardless of the billing period` qualifies invoice recalculation; it does not establish that corrected historical usage can bypass a separately documented submission window. The page also does not say regeneration voids or cancels an old downstream invoice, collects payment, issues a refund or credit memo, recalculates tax, cancels A/R, adjusts revenue, or reconciles provider and ledger state.

The refreshed request and response example UUIDs are now distinct, resolving the earlier snapshot's example-level conflict with the prose. This alignment is documentation evidence, not a runtime guarantee about lineage fields or the regenerated invoice's lifecycle state.

## Raw-detail coverage map

Use the raw page for the production server and bearer security declaration, exact operation ID, complete request and success schemas, UUID formats, request and response examples, and OpenAPI requiredness nesting. The raw page contains no endpoint-specific error catalog, retry header, state enum, recalculated monetary fields, or distribution-status schema; consult the linked API-wide idempotency authority for POST replay guarantees and the primary concepts for cross-source invoice-lifecycle and downstream-system context.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-invoicing]], [[metronome-integrations]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-api-reference-idempotency]], [[source-metronome-guides-invoices-invoice-optimization-issue-credit-memos]]

## Raw Sources

- [[raw/metronome/api-reference/invoices/regenerate-an-invoice-2026-08-28|2026-08-28 snapshot - refreshed invoice-regeneration mutation, recalculation inputs, distinct replacement example, request and response schema, and configured distribution boundary]]
- [[raw/metronome/api-reference/invoices/regenerate-an-invoice-2026-07-13|2026-07-13 snapshot - prior invoice-regeneration mutation whose request and response examples reused one UUID]]
