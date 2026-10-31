---
title: "Adyen Balance Platform webhook: payout schedule execution failed"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleExecution.failed"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleExecution.failed/2026-09-15.md"
tags: [adyen, webhooks, balance-platform, payouts]
---

## Overview

This 2026-09-15 capture documents the incoming `balancePlatform.balanceAccountPayoutScheduleExecution.failed` webhook, which Adyen sends when a scheduled payout execution fails. It describes an event, not a merchant POST operation. The `latest` documentation route does not establish a current API version. See [[adyen]], [[adyen-platforms]] and [[adyen-webhooks]].

## Key takeaways

- The request-body table requires top-level `data`, `environment` (`test` or `live`) and `type`. `timestamp`, meaning the event queue time, is optional. Every listed field inside `data` is optional: the source balance-account ID, managed payout-schedule ID, balance-platform ID, execution `result`, `resultDetails` and `triggeredAt`. The page provides no example payload or permitted `result` values.
- Optional `resultDetails` may include a failure `reason`, numeric `reasonCode` and `transferId` for a transfer created for this execution. A failed-execution event does not establish that a transfer was created; `transferId` is optional. The page does not define reason-code meanings or any later transfer outcome.
- The `2xx` response accepts the webhook. The page does not establish debit, bank receipt, retry, delivery order, duplicate handling or signature verification. A failed payout-schedule execution is distinct from a completed transfer or payout.

## Detail locators

- Event trigger and identity: pinned raw title/introduction, lines 5–7.
- Required envelope and optional execution identifiers, result/details and trigger time: `## Parameters > ### Request body`, lines 11–26.
- Webhook acknowledgement: `## Responses > ### 200 Success`, lines 28–36.

## Related

- [[source-adyen-docs-platforms-managed-payouts-view-payout-executions]] — separate managed payout execution guidance.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleExecution.failed/2026-09-15|Failed payout-schedule execution webhook snapshot]]
