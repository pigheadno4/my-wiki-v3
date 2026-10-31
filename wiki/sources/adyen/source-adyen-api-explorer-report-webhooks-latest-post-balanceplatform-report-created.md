---
title: "Adyen Report webhooks v1: report created event"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/report-webhooks/latest/post/balancePlatform.report.created"
raw_files:
  - "adyen/api-explorer/report-webhooks/latest/post/balancePlatform.report.created/2026-09-15.md"
tags: [adyen, webhooks, reports, balance-platform]
---

## Overview

Captured incoming `balancePlatform.report.created` webhook reference in the Report webhooks catalog, whose separately captured overview is headed v1. Adyen says it sends this event after a report is generated and ready for download, with a URL in the event body. This is report-availability notification, not a merchant POST operation or evidence that a report has been fetched, reconciled, or used to prove settlement. See [[adyen]], [[adyen-webhooks]], and [[adyen-reporting]].

## Key takeaways

- The request-body table requires top-level `data`, `environment` (`test` or `live`), and `type`; `timestamp` is optional. Within `data`, `downloadUrl`, `fileName`, and `reportType` are required. Account-holder, balance-account, platform and resource identifiers, plus event `creationDate`, are optional. The listed report types include accounting, interactive accounting, balance, fee, payment-instrument, payout and statement reports. The TEST example shows an accounting-report URL and filename; it does not define every report's contents or account scope.
- Download requires an authenticated GET. The prose says to ask an Adyen contact for **report credentials** and use them for the GET, while the `downloadUrl` field description says to authenticate with **API credentials**. This wording conflict needs route-specific confirmation before choosing credentials; the webhook does not itself grant access to the report.
- The response section says any `2xx` accepts the webhook; its `200 Success` example includes `[accepted]` as `notificationResponse`. Receiver acceptance does not establish completed report download, accurate reconciliation, booked funds, settlement, or bank receipt. This reference gives no delivery-order, retry, deduplication, or signature rule. The captured `latest` URL and v1 family heading do not prove the current served version.

## Detail locators

- Event trigger, download availability and prose credential instruction: pinned raw lines 5–9.
- `## Parameters` → `### Request body`: requiredness, optional scope IDs, report types and field-level credential instruction, lines 11–33.
- `## Request examples`: TEST accounting-report event, lines 35–52.
- `## Responses` and `## Response examples`: `2xx` acceptance and sample response, lines 53–72.

## Raw Sources

- [[raw/adyen/api-explorer/report-webhooks/latest/post/balancePlatform.report.created/2026-09-15|Captured report created webhook reference (2026-09-15)]]
