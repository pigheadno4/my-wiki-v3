---
title: "Adyen Webhooks latest REPORT_AVAILABLE notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/REPORT_AVAILABLE"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/REPORT_AVAILABLE/2026-09-15.md"
tags: [adyen, webhooks, reports, reporting]
---

## Overview

This 2026-09-15 snapshot of Adyen Webhooks `latest` POST `/REPORT_AVAILABLE` documents an incoming notification that a report has been generated and is ready to download. The POST heading is the webhook delivery route, not a merchant operation to generate or download a report.

## Key takeaways

- Within `NotificationRequestItem`, the table requires `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, `reason`, and `success`. The table says `pspReference` contains the report filename, `reason` contains the report download URL, and `success` is always `true`. `originalReference` is optional. The outer `live`, `notificationItems`, and wrapper item are marked optional.
- The example has `eventCode: "REPORT_AVAILABLE"`, `reason: "URL_TO_DOWNLOAD_REPORT"`, and `success: "true"`. Its `pspReference` value is reference-shaped rather than an evident report filename, but the page does not establish that it cannot be a filename. `merchantReference` is present as an empty string, despite the table describing it as a unique payment reference; the table gives no nonempty constraint. The `reason` URL placeholder illustrates the table's download-URL description.
- The response section labels `200 Success` and says webhook acceptance depends on HTTP status. Notification availability and receiver acknowledgement do not establish successful download, report contents, complete reconciliation, settlement, or payment outcome. This page gives no download authentication, delivery-order, retry/deduplication, or signature-verification procedure.

## Detail locators

- Report-ready purpose: raw lines 5–7. Field requiredness, filename/URL and success descriptions: raw lines 11–27. Sample payload and evidence-limited field observations: raw lines 29–56. HTTP acceptance: raw lines 57–60.

## Related

- [[adyen]] — provider overview.
- [[adyen-reporting]] — report and reconciliation context.
- [[adyen-webhooks]] — incoming webhook context.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/REPORT_AVAILABLE/2026-09-15|REPORT_AVAILABLE webhook reference (2026-09-15)]]
