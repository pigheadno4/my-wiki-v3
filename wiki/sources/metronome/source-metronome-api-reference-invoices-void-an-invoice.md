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

This API reference defines Metronome's invoice-void operation. The OpenAPI document applies bearer authentication to `POST /v1/invoices/void`. It does not mark the request body itself as required; within the JSON object schema, `id` is required and UUID-formatted. For HTTP 200, the schema defines but does not require a top-level `data` property, requires `id` only within `data`, and shows an example containing `data.id`. The operation description calls the cancellation permanent and immediate, but the page does not define eligible starting states, downstream-system effects, retries, or error behavior.

## Key takeaways

- Metronome describes voiding as setting an invoice's status to `voided`, preventing collection, removing it from customer billing, and immediately stopping payment processing.
- The description presents voiding for correcting billing errors, cancelling incorrect charges, or handling disputed invoices that should not be collected; those examples are not a complete contract for eligible invoice states.
- The operation uses `POST /v1/invoices/void`, has operation ID `voidInvoice-v1`, and inherits the OpenAPI document's global `bearerAuth` requirement, which is defined as an HTTP bearer scheme.
- The OpenAPI operation does not mark `requestBody` as required. Within its JSON object schema, `id` is required and represented as a UUID-formatted string; the request example supplies one UUID.
- The HTTP 200 schema defines a top-level `data` property without requiring it. Within `data`, `id` is required and UUID-formatted, and the response example contains `data.id`. Status and other invoice fields are not documented, but the page does not say an actual response cannot contain additional fields.
- The page does not specify which invoice states can be voided, repeated-call behavior, idempotency, concurrency handling, validation failures, authorization failures, not-found behavior, webhook effects, or downstream reconciliation.

## Endpoint contract

| Attribute | Documented value |
| --- | --- |
| Method and path | `POST /v1/invoices/void` |
| Authentication | Global `bearerAuth`, defined as an HTTP bearer scheme |
| Request body | `requestBody` is not marked required; within the JSON object schema, `id` is required and UUID-formatted |
| Success response | HTTP 200 schema defines but does not require top-level `data`; within `data`, `id` is required and UUID-formatted; the example contains `data.id` |
| Operation ID | `voidInvoice-v1` |

The request and response examples use the same invoice UUID. The description says the status change is applied immediately, but neither the documented 200 schema nor its example includes status, so this page provides no response-body representation of the new status. The schema documents `id` within `data` but does not establish that actual responses cannot contain status or other invoice fields. It also does not document whether the endpoint returns the existing result when the invoice is already voided.

## Intended use and effect

The operation description presents voiding as a way to correct billing errors, cancel incorrect charges, or handle disputed invoices that should not be collected. These are intended-use examples, not an exhaustive eligibility list or evidence that every such invoice can be voided from every starting state. The same description says the operation permanently sets the invoice status to `voided`, prevents collection, removes the invoice from customer billing, and applies the change immediately to stop payment processing.

## Scope and system boundaries

The page's statements about preventing collection, removing the invoice from customer billing, and stopping payment processing do not identify a downstream billing provider, ERP, marketplace, payment processor, or customer-A/R system. A separate Metronome correction guide says that voiding in Metronome does not void a downstream invoice and requires the downstream invoice to be voided or cancelled separately. Accordingly, this endpoint must not be treated as evidence that Stripe, an ERP, a marketplace, or another A/R system is updated, or that a collected payment is refunded, tax is reversed, revenue is adjusted, or ledger and credit effects are reconciled.

## Contradictions and unknowns

No direct contradiction with the existing invoicing concept or credit-and-rebill source was found when the API description is scoped to the Metronome invoice. The broad payment-processing language would conflict with the documented downstream boundary only if it were extended beyond Metronome, which this API page does not explicitly do. The page also leaves invoice-state preconditions, downstream propagation, payment and accounting consequences, response status visibility, error responses, idempotency, concurrency behavior, webhook effects, and partial-failure recovery undocumented.

## Related

- Company: [[metronome]]
- Concept: [[metronome-invoicing]]
- Related source: [[source-metronome-guides-invoices-invoice-optimization-issue-credit-memos]]

## Raw Sources

- [[raw/metronome/api-reference/invoices/void-an-invoice-2026-07-13|2026-07-13 snapshot — invoice void endpoint, request, success response, and operation boundaries]]
