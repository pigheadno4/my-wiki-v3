---
title: "Adyen Notification TRANSFER_FUNDS event"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Notification/latest/post/TRANSFER_FUNDS"
raw_files:
  - "adyen/api-explorer/Notification/latest/post/TRANSFER_FUNDS/2026-09-15.md"
tags: [adyen, classic-platforms, notifications, fund-transfers]
---

## Overview

This captured API Explorer page specifies the incoming `POST /TRANSFER_FUNDS` notification that Adyen sends when funds are transferred between Classic Platforms accounts. It is a notification payload reference, not the Fund API request to initiate a transfer. See [[adyen]] and [[adyen-classic-platforms]].

## Key takeaways

- The required top-level notification fields are `eventDate`, `eventType`, `executingUserKey`, `live`, and `pspReference`. The page defines `eventDate` as the time an event has been completed and `pspReference` as the reference of the request from which the notification originates.
- `content` is optional at the top level. If supplied, its documented fields include transferred amount, source and destination Account codes, merchant reference, transfer code, status and invalid fields. Within the optional `amount` object, `currency` and minor-unit `value` are marked required. Do not read the example's `Success` status or error object as a universal outcome.
- The `200 Success` response section describes an optional `notificationResponse` string set to `[accepted]` to acknowledge receipt. Receipt acknowledgment is separate from the transfer's business status and does not establish settlement or bank receipt.

## Detail locators

- Request body schema and requiredness: pinned raw lines 9–36.
- Illustrative `transferFunds` JSON, including status and error fields: lines 38–81.
- Response and acknowledgment: lines 82–90.

## Related

- [[adyen-classic-platforms]]
- [[source-adyen-api-explorer-fund-latest-post-transferfunds]]

## Raw Sources

- [[raw/adyen/api-explorer/Notification/latest/post/TRANSFER_FUNDS/2026-09-15|Notification TRANSFER_FUNDS API Explorer capture]]
