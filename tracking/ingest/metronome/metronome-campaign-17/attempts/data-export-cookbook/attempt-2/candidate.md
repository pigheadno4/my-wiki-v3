---
title: "Metronome Data Export SQL Cookbook"
type: source
date_ingested: 2026-08-19
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/reporting-insights/data-export/cookbook.md"
raw_files:
  - "metronome/guides/reporting-insights/data-export/cookbook-2026-07-13.md"
tags: [metronome, data-export, sql, reporting, analytics]
---

## Overview

This cookbook provides starting-point SQL for analyzing Metronome warehouse exports. Its examples span core customer and event entities, finalized and draft invoicing, invoice-breakdown snapshots, contracts and rate cards, and alerts; Metronome directs readers to adapt date functions and syntax to their destination warehouse.

## Key takeaways

- Core-entity examples count non-archived customers with `archived_at IS NULL` and aggregate exported events by timestamp month.
- Invoice examples aggregate monthly invoice totals and line-item totals, follow daily draft totals over `snapshot_time`, and select the globally greatest draft snapshot when grouping draft invoices by contract.
- Draft-breakdown examples join invoice and line-item rows on both invoice-breakdown ID and `snapshot_timestamp`. They select the greatest exported breakdown snapshot, restrict the worked queries to `PRODUCTION`, and the aggregate example excludes negative line-item totals.
- Contract examples identify archived contracts, sort a selected contract's overrides by descending `updated_at`, and count rate-card entries whose `ending_before` is later than `NOW()`.
- Alert examples select webhook-enabled definitions that are not disabled and count customer-alert-history rows by creation day and alert name.

## Query catalog

### Core entities

The customer query treats a null `archived_at` as the cookbook's active-customer predicate. The events query groups `events.timestamp` by month to measure ingestion volume; it is a count of exported event rows, not a documented count of billable, matched, or invoiced usage.

### Invoicing and draft snapshots

The finalized-invoice section groups `invoice.total` by `end_timestamp` month and joins `invoice.id` to `line_item.invoice_id` for a line-item-type breakdown. The draft section first groups all daily `draft_invoice` snapshots by `snapshot_time`, then provides a latest-snapshot view that filters to the maximum `snapshot_time` in the table before grouping by `contract_id`.

For draft invoice breakdowns, the cookbook computes one global maximum `snapshot_timestamp`, joins invoice and line-item breakdown rows on both `i.id = li.invoice_breakdown_id` and equal snapshot timestamps, and filters the worked queries to Production. The aggregate query groups by breakdown start time and line-item name, sums quantity and `total/100`, and drops rows where `li.total` is negative. The customer-detail query selects customer, period, invoice, name, quantity, and `total/100` from the same latest-snapshot join.

### Contracts and pricing

The contract examples query archived rows with `archived_at IS NOT NULL`, retrieve one contract's overrides ordered newest-first by `updated_at`, and join rate cards to rate-card entries to count entries whose end time is in the future. Sorting overrides does not limit the result to one row, and the active-entry example does not test a start-time field; both are starting patterns rather than complete lifecycle definitions.

### Alerts

The active-alert example requires both `webhooks_enabled = TRUE` and `disabled_at IS NULL`. The history example joins `customer_alert_history.alert_id` to `alert.id`, groups by creation day and alert name, and counts alert IDs.

## Query boundaries and contradictions

> [!warning] Query-scope contradiction
> The two queries under **Finalized Invoices** do not filter invoice status. The related database reference says the exported `invoice` table includes both finalized and void records, so these cookbook queries must not be treated as finalized-only totals without reconciling the current schema and adding the intended status rule.

> [!warning] Missing time predicate
> The alert-history example is titled "over the last week", but its SQL has no `WHERE` clause or other date restriction. As written, it groups all rows available to the query rather than establishing a seven-day window.

> [!warning] Standard-SQL inconsistency
> The customer-detail draft-breakdown query selects six nonaggregated expressions but groups only by the first two. Despite the page's standard-SQL framing, strict warehouses generally require every selected nonaggregated expression in the grouping set; validate and repair this example for the target warehouse before use.

The examples do not define export delivery, freshness, duplicate handling, monetary units, currency conversion, or snapshot completeness. In particular, `total/100 AS total_dollars` is an example expression, not proof that every exported total in every currency uses a universal cents-to-dollars conversion. Use the data-export overview and database reference for delivery semantics, table grain, lifecycle state, and field definitions.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-reporting-and-analytics]], [[metronome-invoicing]], [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]], [[metronome-alerts-and-notifications]], [[metronome-event-ingestion]]
- Sources: [[source-metronome-guides-reporting-insights-data-export-overview]], [[source-metronome-guides-reporting-insights-data-export-database-reference]]

## Raw Sources

- [[raw/metronome/guides/reporting-insights/data-export/cookbook-2026-07-13|2026-07-13 snapshot - complete SQL cookbook]]
