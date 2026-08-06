---
title: "Metronome API Reference: Void an Invoice"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/invoices/void-an-invoice"
raw_files:
  - "metronome/api-reference/invoices/void-an-invoice-2026-07-13.md"
tags: [metronome, invoices, invoice-voiding, billing-corrections, api]
---

## Overview

This API reference defines Metronome's invoice-void operation. A bearer-authenticated `POST /v1/invoices/void` request accepts one invoice UUID, and the documented success response returns that invoice ID. The operation description calls the cancellation permanent and immediate, but the page does not define eligible starting states, downstream-system effects, retries, or error behavior.

## Key takeaways

- Metronome describes voiding as setting an invoice's status to `voided`, preventing collection, removing it from customer billing, and immediately stopping payment processing.
- The operation uses `POST /v1/invoices/void` and the OpenAPI document applies bearer authentication.
- The JSON request requires `id`, represented as a UUID-formatted string.
- HTTP 200 returns an object whose `data.id` is a UUID-formatted string; the documented response schema does not return the invoice status or any other invoice fields.
- The page does not specify which invoice states can be voided, repeated-call behavior, idempotency, concurrency handling, validation failures, authorization failures, not-found behavior, webhook effects, or downstream reconciliation.

## Endpoint contract

| Attribute | Documented value |
| --- | --- |
| Method and path | `POST /v1/invoices/void` |
| Authentication | HTTP bearer scheme |
| Request body | JSON object with required `id` string in UUID format |
| Success response | HTTP 200 with `data.id` in UUID format |
| Operation ID | `voidInvoice-v1` |

The request example and success response use the same invoice UUID. The description says the status change is applied immediately, but the 200 schema contains only the returned ID, so this page does not provide response-body evidence of the new status. It also does not document whether the endpoint returns the existing result when the invoice is already voided.

## Scope and system boundaries

The page's statements about preventing collection, removing the invoice from customer billing, and stopping payment processing do not identify a downstream billing provider, ERP, marketplace, payment processor, or customer-A/R system. A separate Metronome correction guide says that voiding in Metronome does not void a downstream invoice and requires the downstream invoice to be voided or cancelled separately. Accordingly, this endpoint must not be treated as evidence that Stripe, an ERP, a marketplace, or another A/R system is updated, or that a collected payment is refunded, tax is reversed, revenue is adjusted, or ledger and credit effects are reconciled.

## Contradictions and unknowns

No direct contradiction with the existing invoicing concept or credit-and-rebill source was found when the API description is scoped to the Metronome invoice. The broad payment-processing language would conflict with the documented downstream boundary only if it were extended beyond Metronome, which this API page does not explicitly do. The page also leaves invoice-state preconditions, downstream propagation, payment and accounting consequences, response status visibility, error responses, idempotency, and partial-failure recovery undocumented.

## Related

- Company: [[metronome]]
- Concept: [[metronome-invoicing]]
- Related source: [[source-metronome-guides-invoices-invoice-optimization-issue-credit-memos]]

## Raw Sources

- [[raw/metronome/api-reference/invoices/void-an-invoice-2026-07-13|2026-07-13 snapshot — invoice void endpoint, request, success response, and operation boundaries]]
