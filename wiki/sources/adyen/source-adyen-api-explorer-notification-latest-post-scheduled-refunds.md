---
title: "Adyen Classic SCHEDULED_REFUNDS notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Notification/latest/post/SCHEDULED_REFUNDS"
raw_files:
  - "adyen/api-explorer/Notification/latest/post/SCHEDULED_REFUNDS/2026-09-15.md"
tags: [adyen, classic-platforms, notifications, refunds]
---

## Overview

This 2026-09-15-captured Notification API Explorer reference describes the incoming `POST /SCHEDULED_REFUNDS` notification. Adyen sends it when a request to refund transfers that have not yet been paid out has been processed and the associated refunds have been scheduled. It concerns Classic account-holder/account codes and the linked Fund API request, not a new merchant refund request or a modern balance-platform transfer event.

## Key takeaways

- The required outer notification fields are `eventDate`, `eventType`, `executingUserKey`, `live`, and `pspReference`. Here `pspReference` identifies the request from which the notification originates; `live` identifies the originating environment. The `content` and `error` objects are optional in this schema.
- Optional `content` includes `accountCode`, `accountHolderCode`, validation `invalidFields`, `lastPayout`, and `refundResults`. The last-payout description places it before the transactions scheduled for refund. Each refund-result entry can include an `originalTransaction`, a refund `pspReference`, and a `response` indicating whether that refund was received for processing. These fields distinguish request identity from individual refund identity; their schema presence does not prove completed refunds or bank credit.
- Optional `error` contains failure information when processing failed and has no value if no error occurred. The page's 200 response uses optional `notificationResponse` set to **[accepted]** to acknowledge receipt of Adyen's notification. Receiver acknowledgment is separate from the processing and financial state described by the event.

## Detail locators

- Event purpose and linked Fund request: raw lines 5–7.
- Request-body schema, field requiredness, last-payout and refund-result descriptions: raw lines 9–49.
- Illustrative request example, including Classic account codes and nested transaction fields: raw lines 51–165.
- HTTP 200 acknowledgment response: raw lines 166–174.

## Related

- [[adyen]] — provider.
- [[adyen-classic-platforms]] — Classic account-holder/account and notification context.
- [[source-adyen-api-explorer-fund-latest-post-refundnotpaidouttransfers]] — request whose processing leads to this scheduled-refunds notification; its 202 response is still pending.

## Raw Sources

- [[raw/adyen/api-explorer/Notification/latest/post/SCHEDULED_REFUNDS/2026-09-15|Notification POST /SCHEDULED_REFUNDS (captured 2026-09-15)]]
