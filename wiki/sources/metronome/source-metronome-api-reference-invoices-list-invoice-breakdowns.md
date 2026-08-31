---
title: "Metronome List Invoice Breakdowns API"
type: source
date_ingested: 2026-08-31
canonical_url: "https://docs.metronome.com/api-reference/invoices/list-invoice-breakdowns"
original_format: webpage
raw_files:
  - "metronome/api-reference/invoices/list-invoice-breakdowns-2026-08-28.md"
tags: [metronome, api, invoices, time-series, reporting, pagination]
---

## Overview

This OpenAPI page documents bearer-authenticated `GET /v1/customers/{customer_id}/invoices/breakdowns`, which expands one customer's invoice data into hourly or daily time windows for usage and cost analysis. It is a cursor-paginated reporting read, not a stable accounting snapshot or evidence that a downstream billing, payment, tax, revenue, or reconciliation process completed.

## Query-critical facts

- Required UUID path `customer_id` scopes the read to one customer. Required RFC 3339 query fields `starting_on` and `ending_before` select only breakdown windows whose starts are on or after the first timestamp and whose ends are on or before the second; despite the second field's name, this page does not document an exclusive comparison. Optional `window_size` defaults to day and accepts six case variants of hour or day.
- Optional integer `limit` is constrained to `1` through `100`, while the prose separately caps one request at 35 days of daily breakdowns or 24 hours of hourly breakdowns. If more results exist, the page returns a cursor, but it does not reconcile result count with those temporal caps or define whether several invoice-window records can consume the same period allowance.
- Optional `status` is an open string illustrated by `DRAFT` or `FINALIZED`; `credit_type_id` filters invoices; `sort` orders invoices by `issued_at` and defaults to `date_asc`; and `skip_zero_qty_line_items` removes zero-quantity line items. The page does not define filter interactions, status normalization or exhaustiveness, void inclusion, tie ordering among several windows of one invoice, or how zero-line filtering affects totals and otherwise-empty breakdown records.
- HTTP `200` is an object whose immediate parent requires sibling `data` and nullable string `next_page`. `data` contains `BreakdownInvoice` items; each item combines the reusable `Invoice` schema with required `breakdown_start_timestamp` and `breakdown_end_timestamp`. The inherited invoice object requires `id`, `customer_id`, `credit_type`, `line_items`, `status`, `total`, and `type`, while each line item requires `name`, `total`, `credit_type`, and `type`. Most objects do not declare `additionalProperties: false`, so the property catalog is not proven closed.
- The response example repeats one invoice `id` across two adjacent breakdown windows. It therefore illustrates invoice identity persisting across time buckets, not a unique row key; the page does not guarantee uniqueness even for invoice ID plus window bounds. Keep the invoice service period (`start_timestamp` and `end_timestamp`) distinct from each breakdown interval, and keep top-level invoice total distinct from a line item's quantity and total for a specific window.
- Line items can identify products, service periods, pricing and presentation groups, discounts, tiers, scheduled charges, subscriptions, consolidated-invoice origin, and applied commits or credits. An `applied_commit_or_credit` line has a negative total; a postpaid-commit application line is not included in the invoice total because postpaid commits are paid in arrears. This read does not establish balance or ledger mutation, denomination, precision, rounding, allocation, or total-reconciliation rules.

## Mutable state, pagination, and reconciliation boundaries

The page explicitly says backdated usage that arrives after invoice finalization is reflected in breakdowns. A consumer must therefore not assume that a previously read finalized-period breakdown is immutable, but the endpoint provides no update timestamp, revision, as-of selector, freshness SLA, cursor snapshot, late-arrival cutoff, or correction history. Cursor lifetime, duplicate or skipped records under concurrent changes, caching, and read-after-write visibility are undocumented. Follow non-null envelope cursors for traversal, but do not treat cursor exhaustion as proof of an immutable historical population.

For non-monotonically increasing `LATEST` metrics, the separate metric guide says invoice breakdown quantities are incremental changes while usage-query quantities are absolute latest values. This endpoint itself does not define aggregation-specific quantity semantics, baselines, missing windows, or negative adjustments, so use that guide for the `LATEST` distinction and this page for request, envelope, interval, and pagination authority.

Inherited `external_invoice` and `revenue_system_invoices` objects can expose provider or revenue-system identifiers, statuses, errors, selected amounts, and sync observations. Their presence does not prove external acceptance, customer delivery, payment, tax correctness, settlement, posting, or reconciliation. The inherited `product_tags` field is described as the current tags for a line item's product, so it is not documented as metadata frozen to the breakdown window.

## Material contradictions and documentation gaps

> [!warning] Envelope placement conflict
> The narrative lists `next_page` among fields contained by each `BreakdownInvoice`, but the success schema places one required nullable `next_page` beside the `data` array at the response-envelope level. Implement against the immediate-parent schema and do not look for a cursor inside each item.

> [!warning] Finalized immutability versus changing breakdowns
> This endpoint says backdated usage after invoice finalization changes the breakdowns, while [[source-metronome-guides-implement-metronome-core-concepts-how-invoicing-works]] says `FINALIZED` invoices are immutable within Metronome. Neither source explains whether only the analytical breakdown is recomputed, whether invoice quantities or totals change, or how exports and downstream copies reconcile. Treat that scope as unresolved rather than using breakdown mutation as authority to change a finalized invoice.

The narrative also calls `commit` a standard invoice field, but the immediate `Invoice` schema has no required top-level commit property; commit identity and application detail appear under line items. The example contains `subtotal`, which the embedded `Invoice` schema does not define. Because the objects are not documented as closed, these are placement and schema-coverage gaps rather than proof that runtime fields are invalid. Only generic HTTP `404` is specified; authentication, authorization, invalid-filter, throttling, timeout, retry, partial-page, and other failure behavior are undocumented. This is a GET operation with no OpenAPI `requestBody`; the page does not define runtime treatment of a supplied body, and API-wide POST idempotency does not establish read consistency or recovery here.

## Raw-detail coverage map

- **Operation and filters:** production server, bearer security, operation ID, complete path/query catalog, formats, defaults, enums, examples, interval predicates, temporal caps, and generic `404` are in raw.
- **Envelope and traversal:** required `data` and nullable `next_page`, response example, cursor request placement, page-size bounds, and the narrative-versus-schema cursor conflict are in raw; cursor lifetime and stable-snapshot behavior are not documented.
- **Invoice and window scope:** complete inherited invoice properties, required fields, service period, breakdown interval, status/type examples, correction, hierarchy, payer, consolidation, regeneration, and configuration-gated fields are in raw.
- **Line items and attribution:** complete charge-type, quantity, price, rate, tier, product, group, discount, commit/credit, quantity-consumption, custom-unit conversion, origin, service-period, and metadata schemas are in raw; exact monetary units and reconciliation rules require their dedicated authorities.
- **External observations:** billing-provider, tax, payment, revenue-system, error, status, and sync fields are in raw; these are response observations rather than proof of downstream outcomes.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-invoicing]], [[metronome-reporting-and-analytics]], [[metronome-usage-based-billing]]
- Additional affected concepts: [[metronome-billable-metrics]], [[metronome-credits-and-commits]]
- Related sources: [[source-metronome-api-reference-invoices-list-invoices]], [[source-metronome-api-reference-invoices-get-an-invoice]], [[source-metronome-api-reference-pagination]], [[source-metronome-guides-implement-metronome-core-concepts-how-invoicing-works]], [[source-metronome-guides-implement-metronome-core-concepts-non-monotonically-increasing-metrics]], [[source-metronome-guides-reporting-insights-data-export-database-reference]]

## Raw Sources

- [[raw/metronome/api-reference/invoices/list-invoice-breakdowns-2026-08-28|2026-08-28 snapshot - customer-scoped hourly or daily invoice windows, filters, cursor envelope, mutable breakdown boundary, and complete embedded invoice schema]]
