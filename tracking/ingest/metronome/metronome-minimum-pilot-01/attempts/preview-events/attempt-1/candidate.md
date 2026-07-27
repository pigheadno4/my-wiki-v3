---
title: "Metronome Preview Events API"
type: source
date_ingested: 2026-07-27
original_format: webpage
raw_files:
  - "metronome/api-reference/invoices/preview-events-2026-07-13.md"
tags: [metronome, invoices, usage-events, api-reference]
---

## Overview
This API endpoint previews how supplied usage events would affect a customer's invoices. `POST /v1/customers/{customer_id}/previewEvents` uses the customer's current contract configuration to generate draft invoices for testing before the events are processed.

## Key takeaways
- The request requires a UUID `customer_id` path parameter and an `events` array containing one to 100 preview events.
- `mode` defaults to `replace`, which ignores historical usage; `merge` combines supplied events with the customer's existing usage and requires at least one event.
- Contracts with SQL billable metrics are not supported. A supplied `transaction_id` is checked against historical events from the past 34 days, and duplicate IDs in the same request cause an error.
- A successful response returns `data`, an array of draft invoice objects with invoice and customer identifiers, credit type, line items, status, total, and type.

## Details
Each preview event requires a nonempty `event_type`; it can include an RFC 3339 `timestamp` (the current time is used when absent), arbitrary `properties`, and an optional `transaction_id` of up to 128 characters. The request object disallows additional top-level properties. Set `skip_zero_qty_line_items` to omit zero-quantity line items from the response.

The preview returns invoice records rather than posting an invoice: the documented example returns `USAGE` invoices with `DRAFT` status, period timestamps, a contract ID, a credit type, a total, and usage line items. Line items include a name, total, credit type, and type, and can also carry quantity, unit price, product, commitment or credit, subscription, discount, and scheduling information when applicable. The API documents a `400` bad-request response and a `404` response when the specified resource is not found; the shared error schema requires a `message`.

## Related
- Companies: [[metronome]]
- Concepts: [[metronome-event-ingestion]], [[metronome-invoicing]], [[metronome-usage-based-billing]]

## Raw Sources
- [[preview-events-2026-07-13]] — verbatim Metronome API reference for previewing invoice effects of usage events
