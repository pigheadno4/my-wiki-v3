---
title: "Metronome List Invoice Breakdowns API"
type: source
date_ingested: 2026-08-05
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/invoices/list-invoice-breakdowns.md"
raw_files:
  - "metronome/api-reference/invoices/list-invoice-breakdowns-2026-07-13.md"
tags: [metronome, invoicing, invoice-breakdowns, usage-analytics, api]
---

## Overview

This API reference documents bearer-authenticated `GET /v1/customers/{customer_id}/invoices/breakdowns`, which returns customer invoice data divided into hourly or daily time windows. The endpoint supports usage analysis, billing-detail reporting, dispute investigation, and cost monitoring while preserving invoice and line-item context for each window.

## Key takeaways

- `customer_id` is a required UUID path parameter. Required RFC 3339 query parameters `starting_on` and `ending_before` select windows that start on or after the first timestamp and end on or before the second.
- `window_size` defaults to `day` and accepts case variants of hour or day. A response can cover up to 35 days for daily windows or 24 hours for hourly windows; additional results use cursor pagination.
- Optional filters include non-void invoice `status`, `credit_type_id`, and `skip_zero_qty_line_items`. Results can be ordered by invoice `issued_at` using `date_asc` or `date_desc`, with `date_asc` documented as the default.
- Each `BreakdownInvoice` extends the standard invoice schema with required `breakdown_start_timestamp` and `breakdown_end_timestamp` fields. The response envelope requires both the `data` array and nullable `next_page` cursor.
- The prose says breakdowns reflect usage events that arrive after invoice finalization. It does not establish that the underlying finalized invoice total, status, balance effects, downstream invoice, or exported snapshot changes in the same way.

## Request and pagination

The endpoint uses Metronome's global bearer-authentication scheme. The `limit` query parameter accepts values from 1 through 100, but the documented time coverage remains capped at 35 days for daily breakdowns and 24 hours for hourly breakdowns per response. When more results remain, the response-level `next_page` cursor can be supplied through the optional `next_page` query parameter.

The date filters apply to complete breakdown windows: `starting_on` includes windows starting at or after its RFC 3339 timestamp, while `ending_before` includes windows ending at or before its timestamp. The page does not define behavior for an inverted interval, partial boundary windows, cursor lifetime, concurrent usage updates during traversal, or a consistency snapshot across pages.

## Response model

A successful HTTP 200 response contains `data`, an array of `BreakdownInvoice` objects, and nullable `next_page`. Each breakdown inherits invoice identity, customer and contract context, credit type, line items, status, total, type, and other optional invoice fields. Its two additional required timestamps delimit the specific breakdown window. Line items can expose quantities, totals, products, pricing and presentation groups, discounts, applied credits or commits, subscriptions, tiers, and consolidated-invoice origin data when applicable.

> [!warning] Documentation ambiguity
> The introductory prose lists `next_page` among fields contained by each `BreakdownInvoice`, while the OpenAPI schema places it once on the response envelope beside `data`. Implement against the response schema and verify the live payload before depending on cursor placement.

## Finalization and freshness boundary

The page explicitly says late usage events can cause breakdowns to reflect updated usage after invoice finalization. This is narrower than a general finalized-invoice mutation guarantee. It does not define recalculation timing, correction limits, whether prior pages or cursors remain stable, whether totals and balance applications are recomputed, whether downstream providers receive updates, or how the API behavior relates to Data Export's finalized and draft breakdown tables.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-invoicing]], [[metronome-reporting-and-analytics]], [[metronome-usage-based-billing]]
- Related source: [[source-metronome-api-reference-pagination]]

## Raw Sources

- [[raw/metronome/api-reference/invoices/list-invoice-breakdowns-2026-07-13|2026-07-13 snapshot — invoice-breakdown endpoint, filters, response schema, and timing boundaries]]
