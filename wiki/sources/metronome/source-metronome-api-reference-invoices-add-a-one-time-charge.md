---
title: "Metronome API Reference: Add a One-Time Charge"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/invoices/add-a-one-time-charge"
raw_files:
  - "metronome/api-reference/invoices/add-a-one-time-charge-2026-07-13.md"
tags: [metronome, invoices, one-time-charges, plans, api]
---

## Overview

This API reference defines the deprecated Plans operation `POST /v1/customers/{customer_id}/addCharge` for adding a one-time charge to an invoice. The documented request identifies the target through a customer UUID, customer-plan UUID, and invoice start timestamp rather than an invoice ID, and it supplies the charge, price, quantity, and description. Metronome directs new clients to Contracts, but this page does not identify the replacement operation or migration mapping.

## Key takeaways

- The endpoint is a deprecated Plans surface; new clients are directed to Contracts without a documented replacement on this page.
- The path requires UUID-formatted `customer_id`. The OpenAPI `requestBody` is not itself marked required, while its referenced payload schema requires `charge_id`, `price`, `quantity`, `invoice_start_timestamp`, `customer_plan_id`, and `description`.
- `charge_id` must refer to a charge on a product that is not on the current plan, and that product must have only fixed charges.
- `price` is a number that must match the invoice currency; the page gives USD cents only as an example. `quantity` is also a number, but neither field has documented positivity, integer, range, precision, or rounding constraints.
- HTTP 200 is documented as an empty object schema and returns no charge, line-item, invoice, or status fields.

## Endpoint contract

| Attribute | Documented value |
| --- | --- |
| Production server | `https://api.metronome.com/v1` |
| Method and path | `POST /customers/{customer_id}/addCharge`, yielding `POST /v1/customers/{customer_id}/addCharge` against the documented server |
| Authentication | HTTP bearer scheme |
| Path parameter | Required `customer_id` string in UUID format |
| Request body | JSON using `AddOneTimeChargePayload`; the `requestBody` object has no `required: true`, while the payload object requires all six documented properties |
| Success response | HTTP 200 with an object marked `x-stainless-empty-object: true` and no documented properties |
| Operation ID | `addOneTimeCharge` |

## Invoice selection and charge constraints

The payload requires `invoice_start_timestamp`, described as the target invoice's `start_timestamp`, and `customer_plan_id`, described as the customer plan to which the charge is added. Together with path-level `customer_id`, those fields are the only documented invoice-selection context; the schema has no invoice ID. The page does not define matching behavior when no invoice or multiple invoices share the supplied context, eligible invoice states, whether a draft or finalized invoice can be changed, or whether the operation creates a new line item versus merging with an existing one.

`charge_id` is a UUID-formatted Metronome charge ID. Its referenced charge must belong to a product that is not on the current plan, and that product must have only fixed charges. The page does not define how "current plan" is selected, whether the charge must belong to the supplied customer plan, whether "only fixed charges" is evaluated at product or version level, or how this legacy Plans restriction maps to Contracts.

## Pricing semantics

The caller supplies numeric `price` and `quantity` plus a string `description`. The only price-unit rule on this page is that the price matches the invoice currency, with USD cents given as an example. It does not document currency discovery, non-USD denomination, tax inclusion, discounts, credits or commits, price precedence, catalog validation, negative or zero values, decimal precision, quantity units, rounding, or recalculation. Accordingly, this endpoint is not evidence that the supplied price changes product, plan, contract, or rate-card pricing outside this invoice charge.

## Success and documentation boundaries

The documented 200 response is an empty JSON object schema, so it provides no returned charge ID, line-item ID, invoice ID, amount, status, or finalization result. The page also does not define error responses, authorization scopes, rate limits, idempotency or duplicate suppression, concurrency behavior, atomicity, webhook events, audit-history effects, downstream invoice synchronization, payment collection, refunds, tax, accounting, or reconciliation. Bearer authentication is documented, but credential issuance and permission granularity are not.

No direct contradiction with the existing invoicing or product-and-rate-card concepts was found when the operation is kept within its deprecated Plans scope. Existing Contract-based one-time and fixed-product guidance should not be treated as the undocumented replacement contract for this endpoint.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-invoicing]], [[metronome-products-and-rate-cards]], [[metronome-customers-and-contracts]]
- Related source: [[source-metronome-guides-pricing-packaging-billing-model-guides-enterprise-commit]]

## Raw Sources

- [[raw/metronome/api-reference/invoices/add-a-one-time-charge-2026-07-13|2026-07-13 snapshot — deprecated Plans one-time-charge endpoint, payload, pricing rule, and empty success response]]
