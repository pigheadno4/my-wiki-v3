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

## Global cautions

- Because of the export methodology, every column may appear nullable in the destination schema even when its business meaning is normally required.
- Deprecated columns remain present in several tables and are documented as expected to be null.
- Draft invoices can be `DRAFT_INCOMPLETE`, with no total or line items until a later snapshot hydrates them.
- Some histories are versioned or effective-dated; selecting the latest exported row is not always equivalent to selecting the row valid for a requested time.

## Sources

- [[source-metronome-guides-reporting-insights-data-export-database-reference]] — exported table families, grains, fields, snapshot behavior, and global cautions

## Related

- [[metronome-event-ingestion]]
- [[metronome-invoicing]]
- [[metronome-customers-and-contracts]]
- [[metronome-products-and-rate-cards]]

