---
title: "Adyen managed-risk rolling reserve applied webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.rollingReserve.applied"
raw_files:
  - "adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.rollingReserve.applied/2026-09-15.md"
tags: [adyen, platforms, managed-risk, webhooks, rolling-reserve]
---

## Overview

This captured API Explorer page defines the incoming `balancePlatform.managedRisk.rollingReserve.applied` webhook. Adyen sends it when it applies a rolling reserve policy to an account holder's payouts because of that account holder's risk level. It concerns the Adyen for Platforms account holder, not a Classic Platforms Account or an individual payment authorization. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The required `data` object identifies the affected `accountHolderId` and gives `rollingReservePercentage` and `withHoldingPeriodInDays`. The percentage is of the user's daily sales volume withheld from the settlement batch; the period is the number of days after which Adyen releases that withheld percentage.
- Required top-level fields are `data`, `environment` (`test` or `live`), and `type`. `data.balancePlatform`, `data.creationDate`, and top-level `timestamp` are optional. `creationDate` describes when the event was triggered; `timestamp` describes when it was queued.
- The sample includes `data.id`, which is not listed in the request-body table. The sample's 10 percent and 30 days are example values, not limits or defaults.
- The response section says to use any HTTP `2xx` status to accept the webhook. Acceptance does not itself prove a particular payout was withheld or released, settlement completion, or bank receipt.

## Detail locators

- Purpose and request-body schema: pinned raw lines 5–22.
- Illustrative request: lines 24–40.
- Response and acceptance: lines 41–49.

## Related

- [[adyen-platforms]]

## Raw Sources

- [[raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.rollingReserve.applied/2026-09-15|Managed-risk rolling reserve applied API Explorer capture]]
