---
title: "Metronome Data Export Overview"
type: source
date_ingested: 2026-07-29
canonical_url: "https://docs.metronome.com/guides/reporting-insights/data-export/overview"
original_format: webpage
raw_files:
  - "metronome/guides/reporting-insights/data-export/overview-2026-07-13.md"
tags: [metronome, data-export, reporting, analytics]
---

## Overview

This guide explains how Metronome exports sandbox and production data to a customer-configured warehouse, database, object-storage provider, or Google Sheets destination. It establishes the delivery model and timing for the exported tables that the related database reference describes in detail.

## Key takeaways

- Data export requires a one-time destination setup at Metronome's data-export connection page; the guide directs customers to contact their Metronome representative to configure the destination.
- Supported destinations span data warehouses, databases, object storage, and Google Sheets, but a customer can configure only one export destination across both Production and Sandbox.
- The initial export is followed by automatic updates at least daily depending on the table. The availability table lists 2-hour transfers with 4-hour average freshness for selected incremental tables, and 24-hour transfers with 24-hour average freshness for the listed snapshot and other incremental tables.
- Object-storage exports use Parquet files under a table and transfer-date path. They are append-only and at-least-once, so downstream consumers must select the most recent row for each primary key.
- Incremental tables contain only rows changed since the preceding export; consumers should use `updated_at` to obtain the latest updates.

## Delivery model and setup

Metronome can export both sandbox and production data. The guide lists BigQuery, ClickHouse, Databricks, Delta Lake, Redshift, Redshift Serverless, and Snowflake as warehouse destinations; a set of database destinations including Athena, MySQL, and Postgres variants; object storage including Azure Blob Storage, Google Cloud Storage, S3, S3-compatible storage, and SFTP; and Google Sheets. Provider availability can change, and the guide asks customers to contact their representative when a preferred vendor is not listed.

The one-destination limit applies across every Metronome environment: Production and Sandbox cannot have distinct export destinations.

## Availability and timing

The guide's availability matrix covers billable metrics, credit types, events, customers, finalized and draft invoices, invoice breakdowns, contracts and contract modifications, contract pricing, packages, alerts, and customer alert history. It distinguishes incremental tables from snapshots. For example, billable metrics, events, customers, finalized invoices and line items, and alerts are listed with 2-hour transfer frequency and 4-hour average freshness, while draft invoices, contract-related data, packages, and invoice breakdowns are listed with 24-hour transfer frequency and 24-hour average freshness.

Transfer frequency is the interval at which new records are sent; average freshness is the average delay from data generation in Metronome to its appearance at the destination.

## Storage and update caveats

For object-storage destinations, files are written in a path shaped as `<bucket_name>/<folder_name>/<table_name>/dt=<transfer_date>/<file_part>_<transfer_timestamp>.parquet`. The files are an append-only log with at-least-once semantics, so repeated primary keys can result from row updates or transfer retries and must be resolved using the most recent data for each row.

Incremental exports include only rows changed since the last export. The guide specifically directs consumers to use the `updated_at` column for the latest updates; it does not state a retention period.

## Related

- Companies: [[metronome]]
- Concepts: [[metronome-reporting-and-analytics]]
- Source: [[source-metronome-guides-reporting-insights-data-export-database-reference]]

## Raw Sources

- [[raw/metronome/guides/reporting-insights/data-export/overview-2026-07-13|overview-2026-07-13]] — verbatim Metronome data-export overview.
