---
title: "Metronome Get an Invoice API"
type: source
date_ingested: 2026-08-30
canonical_url: "https://docs.metronome.com/api-reference/invoices/get-an-invoice"
original_format: webpage
raw_files:
  - "metronome/api-reference/invoices/get-an-invoice-2026-08-28.md"
  - "metronome/api-reference/invoices/get-an-invoice-2026-07-13.md"
tags: [metronome, api, invoices, line-items, billing-providers]
---

## Overview

This OpenAPI page documents bearer-authenticated `GET /v1/customers/{customer_id}/invoices/{invoice_id}`, a Read operation for one customer-scoped draft or finalized invoice. It returns the invoice under a required `data` envelope with line-item, balance-application, hierarchy, correction, and downstream-system context, but the Get contract does not replace lifecycle mutations, ledger authorities, or external-provider outcome evidence.

## Query-critical facts

- `customer_id` and `invoice_id` are required UUID-formatted path parameters. Optional boolean `skip_zero_qty_line_items` filters all zero-quantity line items from the response; this page does not define effects on totals, item identity, or ordering.
- HTTP `200` requires top-level `data`. The referenced `Invoice` object requires only `id`, `customer_id`, `credit_type`, `line_items`, `status`, `total`, and `type`; complete optional fields and immediate-parent schemas remain in raw.
- The narrative names `DRAFT`, `FINALIZED`, and `VOID`, says drafts update in real time as usage arrives and may change before finalization, and says voided invoices retain original line-item detail. `InvoiceStatus` is a string with an example rather than a closed enum, and this page defines no freshness SLA, stable snapshot, read-after-write, or retention guarantee.
- In the refreshed schema, `Invoice.billable_status` says it indicates whether the invoice has been or will be sent to the configured customer billing provider and defaults to `billable`. The property also combines a `$ref` to string-backed `BillableStatus` with sibling `type: object`, so its documented shape remains internally unresolved.
- `InvoiceLineItem.quantity_consumed` is described on applied-commit lines for quantity-based commits as the unit quantity deducted from the commit. Nested `AppliedCommitOrCredit.access_type` is not in that object's required list and distinguishes `SPEND`, which deducts the dollar cost of usage, from `QUANTITY`, which deducts units; this response component states no default and does not establish mutation acceptance or ledger reconciliation.
- Nullable `external_invoice` and `revenue_system_invoices` can expose provider, status or sync observations, identifiers, errors, and selected amounts. Their presence does not independently prove provider acceptance, customer delivery, collection, payment, settlement, tax correctness, revenue posting, or reconciliation.

## Material boundaries and contradictions

> [!warning] Narrative fields versus schema
> The narrative names total amount and amount due after credits, but the `Invoice` schema defines numeric `total` and no separate `amount_due`. Likewise, `InvoiceLineItem.list_price` refers to `include_list_prices=true`, while the operation parameter list defines only the two path identifiers and `skip_zero_qty_line_items`. Do not synthesize `amount_due` or assume an undocumented query parameter contract from those descriptions.

> [!warning] Invoice status casing across authorities
> This Get page uses uppercase `VOID`, while the separate void-operation prose says an invoice status is set to lowercase `voided` and its success schema does not return status. Preserve both source-scoped statements; enum exhaustiveness, normalization, and whether the lowercase wording is a literal value observable through this Get response remain unresolved.

Only generic HTTP `404` is documented. Authentication failure, authorization, throttling, timeout, retry, caching, and other failure behavior remain unspecified here. Because this operation is GET, the separate API-wide POST idempotency authority does not establish endpoint-specific read consistency or recovery behavior. Most response objects omit `additionalProperties: false`, so their documented property sets are not proven closed.

## Raw-detail coverage map

- **Request and envelope:** production server, bearer security, operation ID, exact path and query parameters, UUID formats, success example, required `data` envelope, and generic `404` are in the current raw page.
- **Invoice identity and lifecycle:** complete required and optional `Invoice` properties, timestamps, status/type examples, correction lineage, consolidated-invoice constituents, payer context, regeneration lineage, and reseller fields are in raw.
- **Line items and financial attribution:** the full `InvoiceLineItem` catalog, charge-type descriptions, quantities and prices, service periods, products, discounts, tiers, custom pricing-unit conversion, applied credit or commit identity, quantity consumption, origins, and immediate-parent requiredness are in raw.
- **External and schema surfaces:** billing-provider and revenue-system objects, provider/status enums, beta tax and amount fields, errors, custom fields, arbitrary-property declarations, feature/client annotations, rates, and tiers are in raw; these response observations do not prove downstream outcomes.
- **Schema history:** the retained 2026-07-13 snapshot preserves the prior configuration-dependent `billable_status` description and predates `InvoiceLineItem.quantity_consumed` and `AppliedCommitOrCredit.access_type`. List, Get, and mutation pages remain separate versioned authorities.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-invoicing]], [[metronome-credits-and-commits]], [[metronome-integrations]]
- Related sources: [[source-metronome-api-reference-invoices-list-invoices]], [[source-metronome-api-reference-invoices-get-an-invoice-pdf]], [[source-metronome-api-reference-invoices-void-an-invoice]], [[source-metronome-api-reference-invoices-regenerate-an-invoice]], [[source-metronome-plans-shared-endpoints-invoices]]

## Raw Sources

- [[raw/metronome/api-reference/invoices/get-an-invoice-2026-08-28|2026-08-28 snapshot - single-invoice retrieval, delivery-intent status, quantity-based commit attribution, and current Get schema]]
- [[raw/metronome/api-reference/invoices/get-an-invoice-2026-07-13|2026-07-13 snapshot - prior Get schema and immutable description history]]
