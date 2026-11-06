---
title: "Adyen balance-account sweep execution failed webhook"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweepExecution.failed"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweepExecution.failed/2026-11-07.md"
tags: [adyen, balance-platform, webhooks, sweeps]
---

## Overview

Captured incoming `balancePlatform.balanceAccountSweepExecution.failed` webhook reference. Adyen sends this event when a balance-account sweep execution fails. It reports an execution outcome, distinct from creating or deleting the sweep configuration and from a booked transfer or bank receipt. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The request-body table marks `data`, `environment` (`test` or `live`) and `type` required; it does not separately mark the whole body required. Within `data`, balance-account ID, sweep-configuration ID, balance-platform ID, execution resource `id`, `result`, `resultDetails`, optional `transferId` and `triggeredAt` are all optional schema fields.
- `result` permits `succeeded`, `failed` and `skipped` in the shared execution payload, although this event type is specifically for failure. Optional `resultDetails` can carry reason, reason code and a boolean indicating a disabled sweep configuration. The example's `missingCapabilities` reason is illustrative, not an exhaustive failure rule.
- The event's `timestamp` is when it was queued; `triggeredAt` is when execution was triggered. The optional transfer ID does not itself establish transfer booking or payout arrival.
- Respond with any HTTP `2xx` to accept the webhook. The listed `200` response body has optional `notificationResponse`; acceptance is acknowledgement of delivery, not recovery, retry, successful payout, or funds movement. No authentication, retry, idempotency, or reversal contract is specified on this page.

## Detail locators

- Event name and trigger: raw lines 5–7.
- Request schema and identity/result fields: raw lines 9–28.
- Illustrative failed TEST payload: raw lines 30–51.
- Webhook acceptance response: raw lines 52–60.

## Related

- [[adyen-platforms]] — balance-account sweep and payout context.
- [[adyen]] — provider index.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweepExecution.failed/2026-11-07|Sweep execution failed webhook, captured 2026-11-07]]
