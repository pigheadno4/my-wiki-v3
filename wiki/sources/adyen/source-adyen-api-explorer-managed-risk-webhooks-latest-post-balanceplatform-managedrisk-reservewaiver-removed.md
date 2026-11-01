---
title: "Adyen managed-risk reserve-waiver removed webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.reserveWaiver.removed"
raw_files:
  - "adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.reserveWaiver.removed/2026-09-15.md"
tags: [adyen, platforms, managed-risk, webhooks, reserves]
---

## Overview

This 2026-09-15-captured API Explorer reference describes the incoming `balancePlatform.managedRisk.reserveWaiver.removed` webhook. Adyen sends it when it removes a reserve waiver from an account holder, so reserves are withheld from that holder's payouts again. It is a managed-risk reserve-waiver event, not a balance update or a payout-result event.

## Key takeaways

- The required `data.accountHolderId` identifies the holder whose reserves will no longer be waived. `data.eventDate` is required and describes the date the waiver was removed. `data.balancePlatform` and `data.creationDate` are optional; `creationDate` is described as the time the event was triggered. The outer `environment` (`test` or `live`) and `type` are required, while `timestamp` is optional and means queue time.
- The example has an additional `data.id` but the request-body table does not define that field. Treat it as example content, not a required event identifier.
- The 200 response table says the receiver accepts the webhook with any `2xx` HTTP status code. That acknowledgment does not establish a specific withheld amount, an executed payout, or bank receipt; none is specified here.

## Detail locators

- Event purpose: raw lines 5–7.
- Request-body requiredness, identifier and time descriptions: raw lines 9–21.
- Illustrative TEST payload and example-only `data.id`: raw lines 23–37.
- Receiver acknowledgment: raw lines 38–46.

## Related

- [[adyen]] — provider.
- [[adyen-platforms]] — account-holder and payout context for the modern balance-platform model.

## Raw Sources

- [[raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.reserveWaiver.removed/2026-09-15|Managed Risk reserve-waiver removed webhook (captured 2026-09-15)]]
