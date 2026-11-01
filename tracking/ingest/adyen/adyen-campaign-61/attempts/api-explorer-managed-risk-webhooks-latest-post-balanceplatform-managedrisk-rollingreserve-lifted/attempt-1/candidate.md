---
title: "Adyen managed-risk rolling reserve lifted webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.rollingReserve.lifted"
raw_files:
  - "adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.rollingReserve.lifted/2026-09-15.md"
tags: [adyen, platforms, managed-risk, rolling-reserve, webhooks]
---

## Overview

Captured API Explorer reference for the incoming `balancePlatform.managedRisk.rollingReserve.lifted` webhook. Adyen says it sends the event when it lifts a rolling reserve policy from an account holder's payouts. The event concerns a managed-risk payout policy, rather than a merchant-account Reserve balance or a specific payout execution.

## Key takeaways

- The webhook body requires a `data` object, its `accountHolderId`, top-level `environment` (`test` or `live`), and top-level `type`. The table marks `data.balancePlatform`, `data.creationDate`, and top-level `timestamp` optional. `creationDate` denotes event triggering time; `timestamp` denotes queueing time.
- The example includes `data.id` but the parameter table does not define that field. Treat it as example content, not a required or documented identifier contract here.
- The response section says any HTTP `2xx` accepts the webhook; it shows optional `notificationResponse` under `200 Success`. Acceptance does not itself establish a payout, balance change, reserve release amount, or bank receipt. The reference does not specify those amounts or timing, or delivery, ordering, retry, deduplication, or signature behavior.

## Detail locators

- Event meaning and direction: raw lines 5–7.
- Required and optional payload fields, environment values, and time meanings: raw lines 9–20.
- Illustrative test payload, including unlisted `data.id`: raw lines 22–36.
- HTTP response and acceptance rule: raw lines 37–45.

## Related

- [[adyen]]
- [[adyen-platforms]]

## Raw Sources

- [[raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.rollingReserve.lifted/2026-09-15|Managed-risk rolling-reserve-lifted webhook, captured 2026-09-15]]
