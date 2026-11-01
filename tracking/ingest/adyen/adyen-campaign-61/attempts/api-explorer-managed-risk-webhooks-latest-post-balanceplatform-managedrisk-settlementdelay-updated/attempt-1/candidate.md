---
title: "Adyen Managed Risk webhook: Settlement delay updated"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.settlementDelay.updated"
raw_files:
  - "adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.settlementDelay.updated/2026-09-15.md"
tags: [adyen, platforms, managed-risk, webhooks, settlement]
---

## Overview

This 2026-09-15-captured API Explorer reference describes an incoming `balancePlatform.managedRisk.settlementDelay.updated` webhook sent when Adyen updates an account holder's payout settlement delay because of risk level. The related Managed Risk webhooks overview identifies this family as v1; the pinned event page uses `latest`. This is a balance-platform account-holder risk-setting event, not a Classic `accountHolderCode` notification or proof of a payout. [[adyen-platforms]] [[adyen]]

## Key takeaways

- The request schema requires `data`, `environment` (`test` or `live`), and outer `type`. Within `data` it requires `accountHolderId`, `configurations`, and `reason`; each configuration requires `paymentMethod` and integer `settlementDelay`. The delay is the number of days after which the user's funds become available in the balance account for that payment method. See [[raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.settlementDelay.updated/2026-09-15|raw lines 11–24]].
- `reason` permits `paymentProcessingEnabled`, `settlementDelayChanged`, or `riskReviewPeriodPassed`. `balancePlatform`, event-trigger `creationDate`, and queue `timestamp` are optional. The example uses a five-day delay and includes `data.id`, but `id` is absent from the field table; do not treat that sample field as a defined required identifier. The example does not establish that funds actually became available after five days in any particular case. See [[raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.settlementDelay.updated/2026-09-15|raw lines 15–45]].
- The HTTP 200 response section lists optional `notificationResponse` and says any 2xx HTTP status accepts the webhook. Receiver acceptance is separate from the settlement-delay setting, balance availability, transfer, or payout outcome. See [[raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.settlementDelay.updated/2026-09-15|raw lines 48–56]].

## Detail locators

- Event purpose and request field table: [[raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.settlementDelay.updated/2026-09-15|raw lines 5–24]].
- Example payload, including sample-only `data.id`: [[raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.settlementDelay.updated/2026-09-15|raw lines 26–47]].
- Receiver response and 2xx acceptance: [[raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.settlementDelay.updated/2026-09-15|raw lines 48–56]].

## Related

- [[adyen-platforms]] — balance-platform and account-holder context.
- [[source-adyen-api-explorer-managed-risk-webhooks-latest-overview]] — Managed Risk webhook family inventory.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.settlementDelay.updated/2026-09-15|Settlement-delay update API Explorer reference (captured 2026-09-15)]]
