---
title: "Stripe: Record Usage for Billing"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-usage-based-billing-recording-usage-2025.md"
tags: [stripe, billing, usage-based, meters, ingestion]
---

## Summary

Hub page for usage ingestion methods. Three paths for recording meter events; must configure meter first. Meter events process asynchronously.

## Key Details

- **API**: `recording-usage-api` — record meter events via Stripe API
- **Dashboard CSV**: `recording-usage-in-bulk-dashboard` — upload CSV file with usage data
- **Amazon S3**: `recording-usage-in-bulk` — bulk ingestion via S3

Meter events are processed asynchronously — summaries and upcoming invoices may not immediately reflect recent events. Legacy UBB had a separate process (see legacy docs).

## Raw Sources

- [[stripe-usage-based-billing-recording-usage-2025]] — verbatim webpage content (20 lines, index of 3 ingestion paths)
