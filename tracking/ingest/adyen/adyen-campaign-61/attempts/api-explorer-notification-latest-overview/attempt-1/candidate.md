---
title: "Adyen Classic Platforms Notification API v6 overview"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Notification/latest/overview"
raw_files:
  - "adyen/api-explorer/Notification/latest/overview/2026-09-15.md"
tags: [adyen, classic-platforms, notifications, api-explorer]
---

## Overview

Captured API Explorer overview of **Classic Platforms – Notifications v6**. The Notification API sends notifications to endpoints specified in a subscription; the separate Notification Configuration API manages subscriptions. This is the classic integration, and the page directs new implementations to a newer integration guide. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The 19-entry POST catalog names Classic event paths for account and account-holder changes, verification, payouts, funds movement, payment booking failure, reports and scheduled refunds. The overview is a route index, not an individual event's payload or response contract. See raw lines 14–37.
- The catalog distinguishes `/PAYMENT_FAILURE` (a failed booking for a capture or refund), `/TRANSFER_FUNDS` (funds transferred between accounts), and `/REPORT_AVAILABLE` (report available). See raw lines 33–37.
- The overview does not specify event payload fields, receiver responses, retries, delivery order or a result for any particular account or payment. Follow each endpoint reference or the linked Classic notifications documentation for those details. See raw lines 9–12 and 14–37.

## Detail locators

- Classic integration and newer-guide direction: raw lines 5–7.
- Subscription delivery and configuration split: raw lines 9–12.
- Complete POST event-path table: raw lines 14–37.

## Related

- [[adyen-classic-platforms]] — Classic resource and integration context.
- [[source-adyen-api-explorer-notificationconfiguration-latest-overview]] — separate subscription-configuration API v6 catalog.

## Raw Sources

- [[raw/adyen/api-explorer/Notification/latest/overview/2026-09-15|Classic Platforms Notifications v6 overview captured 2026-09-15]]
