---
title: "Stripe: Record Usage for Billing Using Amazon S3"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-in-bulk"
raw_files:
  - "stripe-billing-subscriptions-usage-based-recording-usage-in-bulk-2026-11-07.md"
  - "stripe-usage-based-billing-recording-usage-s3-2025.md"
tags: [stripe, billing, usage-based, meters, ingestion, amazon-s3, aws]
---

## Summary

Stripe's May 5 and November 7, 2026 captures of the same guide describe bulk meter-event ingestion from Amazon S3 through a Stripe Dashboard connector. Stripe parses, validates, and transforms CSV, JSON, or JSON Lines usage files into meter events; successfully uploaded events can appear on subscription invoices. The captures differ materially on file naming guidance. See [[stripe]] and [[stripe-usage-based-billing]].

## Key Details

**Supported files and fields:** CSV, JSON, JSON Lines; maximum 1 GB per file. Contact Stripe for a different structure or custom format. Files follow the Meter Event schema: optional unique `identifier` (Stripe can generate one), Unix-seconds `timestamp`, `event_name`, customer mapping through `payload_stripe_customer_id` (`cus_xxxx` or `acct_xxxx`), and numerical usage through `payload_value` or the configured `value_settings` payload key. See the raw File format and fields tables and examples for exact layout.

**S3 connector setup:** In Stripe Dashboard, use Data management → Connectors → Add connector → Amazon S3. The captured steps create an AWS permission policy and IAM role with the Dashboard-provided trust policy, substitute the target bucket name in the permission policy, and provide AWS account ID, bucket name, region, and an optional folder path. A configured folder scopes retrieval to that folder. File preview validates the connection; **Done** activates the connection and initiates import.

**File selection and polling:** The November 7 capture says the complete S3 object key can contain up to **1,024 UTF-8 bytes** under Amazon S3 naming rules and should include `.csv`, `.json`, or `.jsonl` as appropriate. It says Stripe skips zero-byte objects and folder markers, and file-count or poll-size limits can defer otherwise eligible files to a later sync. The May 5 capture instead said file names must be **under 255 characters** with an appropriate extension. Both captures describe an initial fetch of data modified in the last **90 days**, then checks every **5 minutes** for objects with `LastModified` later than the last sync. The guide says uploaded events update within five minutes, potentially longer when many files remain unprocessed; it does not quantify any particular deferral.

> [!warning] Contradiction
> The May 5 filename limit and November 7 complete-object-key limit use different units and scopes. These dated captures do not establish which constraint a particular live connector enforces. Do not treat 1,024 UTF-8 bytes as 1,024 filename characters.

**Volume and processing:** The guide advises uploading a new file every **10 seconds** or when the current file reaches **1 million records**, whichever comes first. It describes a ceiling of **50 files or 10 GB per poll** and processing at **10,000 events/second**. It says to contact sales if **100,000 events/second** processing is needed; it does not promise that capacity. Avoid files with only a CSV header, JSON `[]`, or JSON Lines `{}` because they add objects and can delay polling.

**Asynchronous error handling:** A whole-file format failure emits `data_management.import_set.failed`; partial-record format failures can emit `data_management.import_set.succeeded` with `succeeded_with_errors`, `result.errors`, and `file_id` for downloading detailed failed records through the Files API. These are snapshot events. Correctly formatted files can still fail because of invalid data such as `event_name` or `stripe_customer_id`; `v1.billing.meter.error_report_triggered` and `v1.billing.meter.no_meter_found` are thin events. The guide advises correcting invalid events in a new file and uploading it. See the raw Report and handle errors section for payloads, codes, Workbench setup, and webhook examples. The May capture renders a Node.js handler; the November capture renders a Python handler. That example change does not establish removal of Node.js support.

## Raw Sources

- [[raw/stripe-billing-subscriptions-usage-based-recording-usage-in-bulk-2026-11-07|November 7, 2026 Amazon S3 usage guide]] — later capture with complete-object-key guidance, zero-byte and folder-marker exclusions, poll deferral, and Python webhook example.
- [[raw/stripe-usage-based-billing-recording-usage-s3-2025|May 5, 2026 Amazon S3 usage guide]] — historical capture, including the under-255-character filename guidance and Node.js webhook example; captured CSV image at `raw/assets/stripe-ubb-csv-format.png`.
