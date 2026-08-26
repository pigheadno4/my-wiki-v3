---
title: "Metronome List Invoices API"
type: source
date_ingested: 2026-08-26
canonical_url: "https://docs.metronome.com/api-reference/invoices/list-invoices.md"
original_format: webpage
raw_files:
  - "metronome/api-reference/invoices/list-invoices-2026-07-13.md"
tags: [metronome, api, invoices, pagination, reporting]
---

## Overview

This reference documents bearer-authenticated `GET /v1/customers/{customer_id}/invoices` on `https://api.metronome.com`. It lists one customer's invoices for billing-history, current-draft, support, reconciliation, and reporting views, with cursor pagination and filters over invoice state, type, contract, credit type, and billing period.

## Query-critical facts

- `customer_id` is a required UUID-formatted path parameter. Optional filters include `status`, invoice `type`, `credit_type_id`, UUID `contract_id`, and `skip_zero_qty_line_items`.
- The inclusive `starting_on` filter selects billing periods starting at or after its RFC 3339 timestamp; exclusive `ending_before` selects billing periods ending before its timestamp. These filters apply to billing-period boundaries, not issue date.
- `limit` accepts 1 through 100 results. HTTP `200` requires both an invoice array under `data` and nullable string `next_page`; callers must continue through cursors to retrieve all matching invoices. The page gives no cursor lifetime, snapshot-consistency, or concurrent-update guarantee.
- The type filter explicitly enumerates `USAGE`, `USAGE_CONSOLIDATED`, and `SCHEDULED`, while the status filter is only an open string whose examples are `DRAFT`, `FINALIZED`, and `VOID`. The prose says void invoices are included unless status-filtered.
- Draft invoices are described as continuously updated as usage arrives. Treat the list as a live view without a documented freshness SLA, read snapshot, or stability guarantee; downstream billing-provider fields, when present, are observations rather than proof of delivery, payment, settlement, tax, accounting, or reconciliation.

## Material boundaries and contradictions

> [!warning] Conflicting default-order authorities
> The prose says results default to creation-date descending (newest first), but the operation's `sort` parameter says it orders by `issued_at` and defaults to `date_asc`. The page does not reconcile creation time with issue time or identify which default governs, so clients that require deterministic ordering should pass `sort` explicitly and must not infer a creation-date order from that parameter.

> [!warning] Summary-versus-schema tension
> The prose calls these invoice summaries and directs detailed-line-item queries to Get Invoice, yet the success schema references the shared `Invoice` object whose required fields include `line_items`, and the example includes a line item. Do not assume the list omits line items or that it provides the same completeness as the single-invoice read; the page gives no projection or truncation contract.

The narrative mentions issue date, due date, subtotal, and amount due, but the referenced invoice schema does not define separate `due_date`, `subtotal`, or `amount_due` properties. Most response objects omit `additionalProperties: false`, so the documented properties are not a closed runtime schema and those narrative labels must not be synthesized into undocumented fields. Only HTTP `404` is specified, with a generic required message; authentication, authorization, throttling, timeout, retry, cache, and other failure behavior remain undocumented on this page.

## Raw-detail coverage map

Use the raw snapshot for the complete query-parameter catalog, filter formats and enums, response envelope and example, the full invoice and line-item schemas, credit and commit attribution, consolidation and payer fields, correction lineage, custom fields, rate and tier structures, external billing and revenue-system records, provider/status enums, feature-gated annotations, and the generic `404` schema.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-invoicing]], [[metronome-reporting-and-analytics]]
- Related sources: [[source-metronome-api-reference-invoices-get-an-invoice]], [[source-metronome-api-reference-pagination]], [[source-metronome-plans-shared-endpoints-invoices]]

## Raw Sources

- [[raw/metronome/api-reference/invoices/list-invoices-2026-07-13|2026-07-13 snapshot - customer invoice listing, filters, pagination, ordering conflict, and complete response schema]]
