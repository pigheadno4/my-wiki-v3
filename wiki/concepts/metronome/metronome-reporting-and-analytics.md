---
title: "Metronome Reporting and Analytics"
type: concept
category: technology
tags: [metronome, data-export, warehouse, reporting, analytics]
---

## Definition

Metronome data export exposes billing and operational data as warehouse tables for reporting, reconciliation, and custom analysis. The database reference spans raw events, customers, invoices, contracts and balances, pricing, packages, payments, alerts, and client-specific metadata.

## Query model

- Treat table grain explicitly: finalized invoices and line items are distinct from daily draft snapshots and daily invoice-breakdown snapshots.
- Use snapshot, watermark, effective-time, and version columns where documented instead of assuming one current row per object.
- Join through stable object IDs such as customer, contract, invoice, line-item, product, billable-metric, and rate-card IDs.
- Follow table-specific scope notes. For example, `contracts_commits` contains contract-level commits but excludes customer-level commits or credits and contract-level credits.

## Delivery and freshness

## Commercial export-row accounting

Metronome defines one Row Exported as one row written to a configured Data Export destination across any schema table. Incremental tables count new or updated rows in each sync; snapshot tables re-export the whole table, and every row in every full cycle counts again. This usage measure is separate from transfer cadence, freshness, destination delivery semantics, and table availability. [[source-metronome-guides-platform-configuration-metronome-pricing-model]]

- One export destination is configured across all Metronome environments, so Production and Sandbox cannot use distinct destinations.
- Selected incremental tables transfer every two hours with four-hour average freshness; the listed snapshot tables and some other exports transfer every 24 hours with 24-hour average freshness.
- Object-storage destinations produce append-only Parquet files with at-least-once semantics. Consumers must resolve repeated primary keys from updates or retries by selecting the most recent row.
- Incremental exports include rows changed since the prior export; Metronome directs consumers to use `updated_at` to obtain the latest updates.

## Global cautions

- Because of the export methodology, every column may appear nullable in the destination schema even when its business meaning is normally required.
- Deprecated columns remain present in several tables and are documented as expected to be null.
- Draft invoices can be `DRAFT_INCOMPLETE`, with no total or line items until a later snapshot hydrates them.
- Some histories are versioned or effective-dated; selecting the latest exported row is not always equivalent to selecting the row valid for a requested time.

## Architecture requirements

Billing architecture should define the freshness and granularity customers need, how sales teams access billing context through a CRM or custom reporting, and how revenue-recognition data and audit trails are handled. The planning guide does not promise a particular API, CRM integration, reporting latency, accounting treatment, or compliance outcome.

## Sources

- [[source-metronome-guides-reporting-insights-data-export-database-reference]] — exported table families, grains, fields, snapshot behavior, and global cautions
- [[source-metronome-guides-reporting-insights-data-export-overview]] — destination scope, delivery cadence, freshness, and object-storage semantics
- [[source-metronome-guides-implement-metronome-planning-your-billing-architecture]] — customer, sales, finance, and audit distribution requirements

## Related

- [[metronome-event-ingestion]]
- [[metronome-invoicing]]
- [[metronome-customers-and-contracts]]
- [[metronome-products-and-rate-cards]]
