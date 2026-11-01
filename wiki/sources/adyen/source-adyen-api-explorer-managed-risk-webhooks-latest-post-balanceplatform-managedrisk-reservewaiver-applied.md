---
title: "Adyen managed risk reserve waiver applied webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.reserveWaiver.applied"
raw_files:
  - "adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.reserveWaiver.applied/2026-09-15.md"
tags: [adyen, platforms, managed-risk, reserves, webhooks]
---

## Overview

This API Explorer reference describes Adyen's incoming `balancePlatform.managedRisk.reserveWaiver.applied` webhook. Adyen says it sends the event when it applies a reserve waiver to an account holder, so reserves are no longer withheld from that holder's payouts. This is an account-holder managed-risk event, not a balance-account balance update or a payout execution result. [[adyen]] [[adyen-platforms]]

## Key takeaways

- The request table requires the `data` object and its `accountHolderId` and `eventDate` properties, plus outer `environment` and `type`. `balancePlatform`, `creationDate`, and outer `timestamp` are optional. `environment` lists `test` and `live`. See **Parameters → Request body**.
- `eventDate` is the waiver-application date as described in the table; optional `creationDate` is when the event was triggered, and optional `timestamp` is when it was queued. Do not collapse these dates into one timestamp. See **Parameters → Request body**.
- The example includes `data.id`, although the request table does not define that field. Treat it as example data, not a documented required identifier. See **Request examples → reserve-waiver-applied**.
- The response table directs the receiver to use any HTTP `2xx` status to accept the webhook. Receipt acceptance does not establish a payout execution or bank receipt. See **Responses → 200 Success**.

## Detail locators

- Payload field names and requiredness: **Parameters → Request body**.
- Example payload: **Request examples → reserve-waiver-applied**.
- Receiver response: **Responses → 200 Success**.

## Related

- [[adyen-platforms]]

## Raw Sources

- [[raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.reserveWaiver.applied/2026-09-15|Managed risk reserve waiver applied snapshot]]
