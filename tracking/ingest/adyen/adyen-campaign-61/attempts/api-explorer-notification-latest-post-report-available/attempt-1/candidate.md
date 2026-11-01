---
title: "Adyen Classic Notification REPORT_AVAILABLE"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Notification/latest/post/REPORT_AVAILABLE"
raw_files:
  - "adyen/api-explorer/Notification/latest/post/REPORT_AVAILABLE/2026-09-15.md"
tags: [adyen, classic-platforms, notification, reporting]
---

## Overview

This API Explorer `POST /REPORT_AVAILABLE` reference describes an incoming Adyen notification when a report has been generated and is available for download. It is a Classic Notification event reference, not an API call to generate or fetch a report. [[adyen]] [[adyen-classic-platforms]] [[adyen-reporting]]

## Key takeaways

- The request table marks `eventDate`, `eventType`, `executingUserKey`, `live`, and `pspReference` required. Optional `content` lists `accountCode`, `accountType`, `eventDate`, `remoteAccessUrl`, and `success`; optional `error` lists `errorCode` and `message`. See the pinned raw's **Parameters → Request body** table.
- The response table describes optional `notificationResponse` set to `[accepted]` to acknowledge receipt. That acknowledgement is separate from report generation or successful download. See **Responses → 200 Success**.
- The `reportAvailable` example contains `eventType: TRANSFER_FUNDS` and transfer-specific `content` fields that are absent from this page's REPORT_AVAILABLE request table. Treat the table and event description as the report-event reference; do not infer report fields from that example. See **Request examples → reportAvailable**.

## Detail locators

- Required and optional fields: **Parameters → Request body**.
- Example mismatch: **Request examples → reportAvailable**.
- Receiver acknowledgement: **Responses → 200 Success**.

## Related

- [[adyen-classic-platforms]]
- [[adyen-reporting]]

## Raw Sources

- [[raw/adyen/api-explorer/Notification/latest/post/REPORT_AVAILABLE/2026-09-15|API Explorer REPORT_AVAILABLE snapshot]]
