---
title: "Metronome Data Export Overview"
type: source
date_ingested: 2026-08-29
canonical_url: "https://docs.metronome.com/guides/reporting-insights/data-export/overview"
original_format: webpage
raw_files:
  - "metronome/guides/reporting-insights/data-export/overview-2026-08-28.md"
  - "metronome/guides/reporting-insights/data-export/overview-2026-07-13.md"
tags: [metronome, data-export, reporting, analytics]
---

## Overview

This guide describes how Metronome sends sandbox and production data to one customer-configured warehouse, database, object-storage, or Google Sheets destination for downstream reporting and dashboards. It establishes destination scope, table-specific transfer and average-freshness labels, and object-storage and incremental-delivery behavior; the linked database reference remains the route for table schemas.

## Query-critical facts

- Data export requires one-time destination setup at Metronome's data-export connection page, and the refreshed guide directs customers to `solutions@metronome.com` for setup. After the initial export, updates occur automatically at least daily depending on the table.
- Only one data-export destination can be configured across all Metronome environments. Production and Sandbox cannot use distinct destinations.
- Supported destination categories are data warehouses, databases, object storage, and Google Sheets. The raw page contains the current provider list and destination-specific guide links.
- Object-storage destinations write Parquet files under a bucket, configured folder, table, transfer-date, part, and transfer-timestamp path. Delivery is an append-only log with at-least-once semantics, so updates or transfer retries can place the same primary key in multiple files and consumers must select the most recent data for each row.
- The availability matrix labels selected incremental tables with two-hour transfer frequency and four-hour average freshness, while the listed snapshot tables and some incremental tables have 24-hour transfer frequency and 24-hour average freshness. Transfer frequency means how often new records are sent; average freshness means the average delay between Metronome generation and destination appearance.
- Incremental exports contain only rows changed since the preceding export, and the guide directs consumers to use `updated_at` to pull the latest updates.

## Material boundaries

The overview defines transfer frequency and average freshness, but it does not state a maximum-latency or service-level guarantee. Its `Incremental` and `Snapshot` labels do not by themselves establish exact row grain, snapshot completeness or atomicity, ordering, retention, late-arriving-data treatment, or reconciliation guarantees. Use the linked database reference for table and column definitions rather than inferring schema from this overview.

The one-destination rule establishes a shared destination across environments; it does not describe environment-partitioning fields or prove that a downstream query isolates Production from Sandbox. The append-only, at-least-once and latest-row instructions are specific to the listed object-storage destinations and should not be generalized to every warehouse, database, or Google Sheets connector.

## Raw-detail coverage map

- **Destination setup and catalog:** the exact connection URL, support contact, provider list, and destination-guide links are in the raw page.
- **Object-storage layout:** the exact Parquet path template, path-component definitions, and append-only delivery note are in the raw page.
- **Availability matrix:** the complete table list, database-reference anchors, transfer-frequency values, average-freshness values, and `Incremental` or `Snapshot` labels are in the raw page.
- **Schema authority:** follow the matrix's database-reference links and [[source-metronome-guides-reporting-insights-data-export-database-reference]] for table-specific fields and semantics; this overview is not a row-grain or full-schema authority.

## Related

- Company: [[metronome]]
- Primary concept: [[metronome-reporting-and-analytics]]
- Related source: [[source-metronome-guides-reporting-insights-data-export-database-reference]]

## Raw Sources

- [[raw/metronome/guides/reporting-insights/data-export/overview-2026-08-28|2026-08-28 snapshot - destination scope, object-storage delivery, availability matrix, and incremental-export behavior]]
- [[raw/metronome/guides/reporting-insights/data-export/overview-2026-07-13|2026-07-13 snapshot - prior retained version]]
