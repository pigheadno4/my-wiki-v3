---
title: "Stripe: Record Usage for Billing Using Amazon S3"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-usage-based-billing-recording-usage-s3-2025.md"
tags: [stripe, billing, usage-based, meters, ingestion, amazon-s3, aws]
---

## Summary

Full guide for bulk meter event ingestion via Amazon S3. Covers supported file formats, S3 connector setup (IAM role + trust policy), polling behavior, rate limits, and two-tier error handling (format errors vs data errors).

## Key Details

**Supported file formats**: CSV, JSON, JSON Lines. Max **1 GB** per file. Contact Stripe for custom formats.

**File fields** (all formats):

| Field | Description |
| --- | --- |
| `identifier` | Optional unique event ID; auto-generated if omitted |
| `timestamp` | Unix epoch seconds |
| `event_name` | Must match meter's event name |
| `payload_stripe_customer_id` | `cus_xxxx` or `acct_xxxx` |
| `payload_value` | Numerical usage; column name mirrors `value_settings` key (e.g., `payload_tokens`) |

**S3 connector setup** (Stripe Dashboard → Data management → Connectors → Add connector → Amazon S3):

1. Create IAM custom trust policy in AWS Console (replace `USER_TARGET_BUCKET` in the provided JSON)
2. Create IAM role with custom trust policy, attach the new permission policy
3. Provide AWS account ID, bucket name, region, and optional folder path in Stripe Dashboard
4. File preview validates credentials; click **Done** to activate

**Polling behavior**:

- Polls every **5 minutes** for objects with `LastModified` date newer than last sync
- Initial sync fetches last **90 days** of data
- Events visible on subscription invoice after successful upload

**Rate limits**:

- Upload a file every **10 seconds** or at **1 million records**, whichever comes first
- Polls max **50 files or 10 GB** per cycle
- Processes at **10,000 events/second** (contact sales for up to 100,000/s)
- Avoid empty files (CSV header-only, JSON `[]`, JSON Lines `{}`) — they inflate object count and delay polling

**Two-tier error handling**:

| Tier | Events | Type |
| --- | --- | --- |
| Format errors (entire file or partial records) | `data_management.import_set.failed` / `data_management.import_set.succeeded` | Snapshot |
| Data errors (invalid `event_name`, `stripe_customer_id`) | `v1.billing.meter.error_report_triggered` / `v1.billing.meter.no_meter_found` | Thin |

`succeeded_with_errors` status → `result.errors` count + `file_id` → use Files API to download full failed-record list.

## Raw Sources

- [[stripe-usage-based-billing-recording-usage-s3-2025]] — verbatim webpage content (353 lines); CDN image saved to `raw/assets/stripe-ubb-csv-format.png`
