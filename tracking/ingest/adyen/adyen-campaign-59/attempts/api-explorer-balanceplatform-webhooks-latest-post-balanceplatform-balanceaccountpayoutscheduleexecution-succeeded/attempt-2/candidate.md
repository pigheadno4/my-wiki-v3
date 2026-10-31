---
title: "Adyen Balance Platform webhook: payout schedule execution succeeded"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleExecution.succeeded"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleExecution.succeeded/2026-09-15.md"
tags: [adyen, balance-platform, webhooks, managed-payouts]
---

## Overview

Captured API Explorer `latest` POST reference for the incoming `balancePlatform.balanceAccountPayoutScheduleExecution.succeeded` webhook. Adyen says it sends this event when a scheduled payout execution succeeds. This is an execution-result event, not proof of bank receipt or a completed external transfer. See [[adyen-platforms]] and [[adyen-webhooks]].

## Key takeaways

- The request-body table requires top-level `data`, `environment`, and `type`; it marks **every listed field inside `data` optional**. These include `balanceAccountId` (account from which payout is initiated), `balanceAccountPayoutScheduleId` (managed payout schedule), `balancePlatform`, `result`, `resultDetails`, and `triggeredAt`. The table does not define `result` values.
- `resultDetails.transferId` is optional and identifies a transfer created for this execution when supplied. The same optional object also describes `reason` and `reasonCode` for an unsuccessful execution; their inclusion in this succeeded-event schema does not mean this event reports a failure or that those fields are present.
- `environment` is `test` or `live`; optional `timestamp` records when the event was queued, while optional `data.triggeredAt` records when the execution was triggered.
- Any HTTP `2xx` accepts the webhook. The response table lists optional `notificationResponse`; receiver acknowledgement is separate from the execution outcome. The captured `latest` route supplies no numbered version or delivery, ordering, retry, deduplication, or signature contract.

## Detail locators

- Event identity and trigger: raw lines 5–7.
- Request-body requiredness and resource identities: raw lines 9–26.
- Optional transfer ID, result fields, and timestamps: raw lines 18–25.
- Receiver acknowledgement: raw lines 28–36.

## Related

- [[adyen]]
- [[adyen-platforms]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleExecution.succeeded/2026-09-15|Captured payout schedule execution succeeded webhook reference]]
