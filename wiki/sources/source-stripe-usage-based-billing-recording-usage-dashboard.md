---
title: "Stripe: Record Usage in the Dashboard"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-usage-based-billing-recording-usage-dashboard-2025.md"
tags: [stripe, billing, usage-based, meters, ingestion, dashboard, csv]
---

## Summary

Covers the two Dashboard-based ingestion methods for meter events: manual input (one event at a time) and CSV file upload (bulk). Includes CSV field schema and upload workflow.

## Key Details

**Manual input** — Meters page → select meter → Add usage → Manually input usage. One customer, one value at a time.

**CSV upload** — Meters page → select meter → Add usage → Upload file. Max **5 MB** per file.

**CSV fields:**

| Field | Description |
| --- | --- |
| `timestamp` | `yyyy-MM-dd`, `yyyy-MM-dd'T'HH:mm:ssZ`, or Epoch |
| `event_name` | Must match the meter's event name |
| `payload_stripe_customer_id` | `cus_xxxx` (Customer) or `acct_xxxx` (Account) |
| `payload_value` | Numerical usage value; column name mirrors `value_settings` key (e.g., `payload_tokens` if `value_settings.event_payload_key = 'tokens'`) |

**Error handling**: if the file has errors, download an error file with per-record failure reasons, fix, and re-upload.

**Post-upload**: events appear in the live meter feed. File status visible on the Data management page.

## Raw Sources

- [[stripe-usage-based-billing-recording-usage-dashboard-2025]] — verbatim webpage content (59 lines)
