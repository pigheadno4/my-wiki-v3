---
title: "Metronome API Reference: Create Historical Invoices"
type: source
date_ingested: 2026-08-31
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/contracts/create-historical-invoices"
raw_files:
  - "metronome/api-reference/contracts/create-historical-invoices-2026-08-28.md"
tags: [metronome, api, contracts, historical-invoices, billing-migration, invoice-corrections, idempotency]
---

## Overview

Bearer-authenticated `POST /v1/contracts/createHistoricalInvoices` creates or previews historical usage invoices for past periods on specified customer contracts. It accepts caller-supplied service windows and custom usage-line quantities, then returns an array of generic invoice objects; use it as a Metronome backfill surface, not as proof that an external invoice, payment, accounting record, or reconciliation result was created.

## Query-critical facts

- The enclosing OpenAPI `requestBody` is not marked `required: true`. Within a supplied JSON object, immediate-parent properties `invoices` and `preview` are required. `invoices` is an array of historical-invoice inputs, but neither it nor each invoice's required `usage_line_items` array declares `minItems`; the wrapper, invoice input, and line-item input do not declare `additionalProperties: false`. Omitted-body, empty-batch, empty-line-array, and unknown-field behavior therefore remain undocumented.
- Each invoice item requires UUID `customer_id`, UUID `contract_id`, UUID `credit_type_id`, inclusive start, exclusive end, issue date, and `usage_line_items`. The names establish half-open service-period bounds, but the schema does not establish that the invoice or line-item periods are in the past, nested within each other, aligned to contract dates, non-overlapping with existing invoices, ordered, or valid for the named customer-contract pair. It also does not define batch order or atomicity.
- Each usage-line item requires only UUID `product_id`, inclusive start, and exclusive end. `quantity`, string-valued pricing and presentation group maps, and `subtotals_with_quantity` are optional siblings. Each supplied subtotal requires its own inclusive start, exclusive end, and quantity, but the schema does not require either line-level `quantity` or subtotals, make them mutually exclusive, or define subtotal ordering, gap and overlap validation, aggregation, precision, rounding, sign, bounds, or reconciliation to the returned line and invoice totals.
- `preview` is a required boolean, and the endpoint description says preview validates invoice data before creation. The related migration guide describes `preview: true` as a dry run before saving, while the example here uses `false`. This operation publishes the same HTTP `200` invoice-array schema for either value and does not define preview persistence, expiration, side effects, stable IDs, a commit token, or whether replaying a preview with `preview: false` creates the exact previewed result.
- HTTP `200` requires top-level `data`, an array of `Invoice`. Each invoice immediately requires `id`, `customer_id`, `credit_type`, `line_items`, `status`, `total`, and `type`; other contract, period, custom-field, billing-provider, revenue-system, correction, payer, and consolidation fields are optional or conditional in the generic schema. The page does not identify the returned UUID as a batch-operation ID, guarantee one result per requested item or input order, define preview-versus-created identity, or state the exact status or type produced.
- The only endpoint error listed is HTTP `400` with a required string `message`. Authentication, authorization, customer-contract mismatch, product or credit-type mismatch, overlap, partial success, rollback, rate limits, timeouts, and ambiguous failures are not mapped to outcomes. Response `external_invoice` and `revenue_system_invoices` surfaces are observations, not proof of provider acceptance, customer delivery, tax, collection, payment, settlement, revenue posting, or reconciliation.

## Financial, state, and correction boundaries

The related import guide is the authority that says supplied quantities are combined with contract unit prices to calculate invoice totals and effects on customer credit and commit balances. This endpoint schema itself accepts no direct invoice-total or unit-price override, does not define balance-ledger entries, and does not establish denomination, tax, discount, precision, rounding, drawdown ordering, effective timestamps, rollback, or reconciliation to an invoice already issued outside Metronome. A returned `total`, line-item set, or balance-related field is not evidence that external A/R was changed.

The migration guide scopes its worked flow to invoices already issued before Metronome provisioning and says imported invoices are not sent through the Stripe integration. This endpoint description additionally calls the operation suitable for correcting past billing periods, but it does not define correction eligibility, starting invoice state, whether an existing invoice is replaced or duplicated, overlap prevention, voiding, regeneration, external credit memos, refunds, or downstream reconciliation. Keep this path distinct from the separate draft-versus-finalized correction and credit-and-rebill authority.

The generic response includes required `status` and `type`, optional external and revenue-system observations, and an optional `created_at` described as present only for correction invoices. Those fields do not prove that this operation always creates a correction invoice, that preview creates any durable invoice, that a non-preview result is finalized or billable, or that any downstream system accepted or reconciled it.

## API-wide POST idempotency boundary

The separate API-wide authority says `Idempotency-Key` applies to every POST endpoint. After execution begins, identical parameters with the same key replay the persisted original result, changed parameters return HTTP `409 Conflict`, retention is at least 24 hours, and the cached result can be HTTP `500`. That request-result replay is distinct from every returned invoice `id`; this endpoint exposes no resource `uniqueness_key` or backfill-batch operation identity.

This page adds no historical-invoice-specific guarantee for an absent, changed, or expired key; concurrent batches; overlap or duplicate-invoice prevention; partial-batch recovery; result freshness; or reconciliation after cached or ambiguous failure. A same-key preview replay is not a fresh validation, and changing either `preview` or the invoice parameters changes the idempotency parameters rather than committing a prior preview. Investigate invoice, balance, ledger, and downstream state before assuming a new key is safe.

## Raw-detail coverage map

- **Operation and envelopes:** use the raw page for the production server, bearer scheme, exact method, path, operation ID, request example, absent request-body required marker, required wrapper properties, HTTP `200` data array, and generic HTTP `400` message schema.
- **Historical invoice input:** use raw for the complete invoice-level fields, UUID and timestamp formats, breakdown-granularity casing variants, configuration-gated billable status, custom fields, required lists, and the absence of array minima and closed-object declarations.
- **Custom usage lines:** use raw for the line-item identity and service-window fields, quantity, pricing and presentation group maps, subtotal schema, and their immediate-parent requiredness; the endpoint does not encode a quantity-versus-subtotal choice or window reconciliation rule.
- **Invoice response:** use raw for the full generic `Invoice` and `InvoiceLineItem` catalogs, required and conditional placement, statuses and types, applied credits or commits, consolidation and hierarchy fields, external-invoice and revenue-system observations, and correction-only `created_at` description.
- **Financial and retry authority:** use the linked import guide for contract-price calculation, balance effects, dry-run and Stripe-exclusion scope; use the correction guide for draft, finalized, credit-memo, refund, void, and regeneration boundaries; and use the dedicated idempotency source for API-wide POST replay, conflict, retention, and cached-error behavior.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-invoicing]], [[metronome-customers-and-contracts]], [[metronome-credits-and-commits]], [[metronome-api-idempotency]]
- Supporting concept: [[metronome-reporting-and-analytics]]
- Related sources: [[source-metronome-guides-invoices-invoice-optimization-import-existing-invoices]], [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-guides-invoices-invoice-optimization-issue-credit-memos]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/contracts/create-historical-invoices-2026-08-28|2026-08-28 snapshot - historical-invoice request, custom usage lines, preview control, generic invoice response, and financial-state boundaries]]
