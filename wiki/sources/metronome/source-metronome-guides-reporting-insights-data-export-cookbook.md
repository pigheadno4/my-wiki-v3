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
- Only the two draft-breakdown examples explicitly filter `environment_type = 'PRODUCTION'`; the other cookbook counts and totals are not environment-scoped as written.
- Global maximum snapshot filters do not replace latest-row resolution per primary key for append-only, at-least-once object-storage exports, and they do not guarantee that every object is complete at that snapshot.
- The rate-card count checks only `ending_before > NOW()` and is not a complete current-state selector without start-time, nullable-end, version, and snapshot handling.

## Query catalog

### Core entities

The customer query treats a null `archived_at` as the cookbook's active-customer predicate. The events query groups `events.timestamp` by month to measure ingestion volume; it is a count of exported event rows, not a documented count of billable, matched, or invoiced usage.

### Invoicing and draft snapshots

The finalized-invoice section groups `invoice.total` by `end_timestamp` month and joins `invoice.id` to `line_item.invoice_id` for a line-item-type breakdown. The draft section first groups all daily `draft_invoice` snapshots by `snapshot_time`, then provides a latest-snapshot view that filters to the maximum `snapshot_time` in the table before grouping by `contract_id`.

The database reference permits `DRAFT_INCOMPLETE` rows with no `total` or line items. Consequently, the cookbook's `COUNT(0)` can include incomplete draft rows while `SUM(total)` ignores their null totals; if status and completeness are not handled explicitly, the count and sum describe different included populations. A global maximum `snapshot_time` is a table-level cutoff, not evidence that every draft object is hydrated or represented by its own latest complete row.

For draft invoice breakdowns, the cookbook computes one global maximum `snapshot_timestamp`, joins invoice and line-item breakdown rows on both `i.id = li.invoice_breakdown_id` and equal snapshot timestamps, and filters the worked queries to Production. The aggregate query groups by breakdown start time and line-item name, sums quantity and `total/100`, and drops rows where `li.total` is negative. The customer-detail query selects customer, period, invoice, name, quantity, and `total/100` from the same latest-snapshot join.

Those two breakdown examples are the only cookbook queries that add `environment_type = 'PRODUCTION'`. The export overview says one destination spans Production and Sandbox, so every other count or total is cross-environment or otherwise unscoped as written unless the intended table-specific environment predicate is added. The global greatest breakdown snapshot also does not prove per-object completeness or perform per-primary-key delivery deduplication.

### Contracts and pricing

The contract examples query archived rows with `archived_at IS NOT NULL`, retrieve one contract's overrides ordered newest-first by `updated_at`, and join rate cards to rate-card entries to count entries whose end time is in the future. Sorting overrides by descending `updated_at` does not limit the result to one override. The query titled active rate-card entries tests only `crce.ending_before > NOW()`: it omits `starting_at`, does not state how a nullable `ending_before` should represent activity, and does not select among exported version or snapshot rows. Reconcile the database-reference grain, effective-time interval, nullable-end semantics, and version/snapshot selection before treating either query as a current-state result.

### Alerts

The active-alert example requires both `webhooks_enabled = TRUE` and `disabled_at IS NULL`. The history example joins `customer_alert_history.alert_id` to `alert.id`, groups by creation day and alert name, and counts alert IDs.

## Query boundaries and contradictions

> [!warning] Query-scope contradiction
> The two queries under **Finalized Invoices** do not filter invoice status. The related database reference says the exported `invoice` table includes both finalized and void records, so these cookbook queries must not be treated as finalized-only totals without reconciling the current schema and adding the intended status rule.

> [!warning] Missing time predicate
> The alert-history example is titled "over the last week", but its SQL has no `WHERE` clause or other date restriction. As written, it groups all rows available to the query rather than establishing a seven-day window.

> [!warning] Standard-SQL inconsistency
> The customer-detail draft-breakdown query selects six nonaggregated expressions but groups only by the first two. Despite the page's standard-SQL framing, strict warehouses generally require every selected nonaggregated expression in the grouping set; validate and repair this example for the target warehouse before use.

> [!warning] Environment scope
> One configured export destination spans Production and Sandbox, but only the two draft-breakdown examples filter `environment_type = 'PRODUCTION'`. The other cookbook counts and totals are not environment-scoped as written. Add the intended predicate for each table before interpreting a result as a production metric.

> [!warning] At-least-once delivery and snapshot scope
> Object-storage exports are append-only and at-least-once. Updates or transfer retries can repeat a primary key, so consumers must resolve the latest row per primary key before aggregation. A global maximum `snapshot_time` or `snapshot_timestamp` is neither per-key deduplication nor a guarantee that every object is present and complete at that cutoff.

> [!warning] Incomplete draft aggregation
> The database reference permits `DRAFT_INCOMPLETE` rows with no total or line items. `COUNT(0)` can include those rows while `SUM(total)` ignores their null totals, so status and hydration must be handled before treating the two measures as a coherent invoice population.

> [!warning] Rate-card current-state boundary
> The active-entry example checks only `ending_before > NOW()`. It omits `starting_at`, does not define intended handling for null `ending_before`, and does not choose among version or snapshot rows; reconcile effective time and exported row grain before calling its count active or current.

> [!warning] Currency denomination boundary
> `total/100 AS total_dollars` is an example alias, not a universal conversion rule. Metronome's direct denomination authority documents USD API values in cents but the listed non-USD fiat currencies in whole units. Determine the row's pricing unit and follow [[metronome-currencies-and-custom-pricing-units]] and [[source-metronome-guides-pricing-packaging-make-pricing-changes-use-currency-custompricingunits]] before scaling. This currency issue is separate from delivery duplication, environment scope, and invoice status.

Use the data-export overview and database reference for delivery semantics, table grain, lifecycle state, and field definitions.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-reporting-and-analytics]], [[metronome-invoicing]], [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]], [[metronome-alerts-and-notifications]], [[metronome-event-ingestion]], [[metronome-currencies-and-custom-pricing-units]]
- Sources: [[source-metronome-guides-reporting-insights-data-export-overview]], [[source-metronome-guides-reporting-insights-data-export-database-reference]], [[source-metronome-guides-pricing-packaging-make-pricing-changes-use-currency-custompricingunits]]

## Raw Sources

- [[raw/metronome/guides/reporting-insights/data-export/cookbook-2026-07-13|2026-07-13 snapshot - complete SQL cookbook]]
