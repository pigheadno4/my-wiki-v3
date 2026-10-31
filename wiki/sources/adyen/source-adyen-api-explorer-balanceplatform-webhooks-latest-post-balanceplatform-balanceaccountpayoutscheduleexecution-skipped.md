---
title: "Adyen Balance Platform webhook: payout schedule execution skipped"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleExecution.skipped"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleExecution.skipped/2026-09-15.md"
tags: [adyen, balance-platform, webhooks, managed-payouts]
---

## Overview

This captured Balance Platform Webhooks API Explorer POST reference describes the incoming `balancePlatform.balanceAccountPayoutScheduleExecution.skipped` event. Adyen sends it when a scheduled payout execution is skipped. It describes an event, not a merchant request to execute or skip a payout. The `latest` URL label does not state a numbered webhook API version. See [[adyen-webhooks]], [[adyen-platforms]], and [[adyen]].

## Key takeaways

- The event body requires `data`, `environment` (`test` or `live`), and `type`; `timestamp` is optional and records when the event was queued.
- All listed properties inside `data` are marked optional: `balanceAccountId` (source balance account), `balanceAccountPayoutScheduleId` (managed payout schedule), `balancePlatform`, `result`, `resultDetails`, and `triggeredAt` (execution trigger time). Within optional `resultDetails`, `reason`, `reasonCode` (a string containing a numeric code), and `transferId` are also marked optional. The `transferId` description calls it an identifier of a transfer created for the execution; the schema does not guarantee that a skipped event includes one or that a transfer completed.
- The page gives no request example, result values, reason-code mapping, or state-transition sequence. The skipped notification alone does not prove a payout was sent, booked, settled, returned, or received by a bank. The response table says any HTTP `2xx` accepts the webhook; `notificationResponse` is optional. This reference does not establish delivery ordering, retry, deduplication or signature rules.

## Detail locators

- Event name and trigger: pinned raw lines 5–7.
- Required envelope and optional execution, reason and transfer fields: pinned raw lines 11–26.
- Acknowledgment response: pinned raw lines 28–36.

## Related

- [[adyen-webhooks]] — webhook family and receipt context.
- [[adyen-platforms]] — platform managed-payout context.
- [[source-adyen-docs-platforms-managed-payouts-view-payout-executions]] — separate schedule execution and transfer lifecycle guide.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleExecution.skipped/2026-09-15|Payout schedule execution skipped webhook reference, captured 2026-09-15]]
