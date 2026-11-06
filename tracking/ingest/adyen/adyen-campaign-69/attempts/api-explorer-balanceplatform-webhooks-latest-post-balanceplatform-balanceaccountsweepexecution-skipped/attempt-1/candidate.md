---
title: "Balance Platform webhook: sweep execution skipped"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweepExecution.skipped"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweepExecution.skipped/2026-11-07.md"
tags: [adyen, balance-platform, webhooks, sweeps]
---

## Overview

This captured Balance Platform webhook reference describes an inbound `balancePlatform.balanceAccountSweepExecution.skipped` event that Adyen sends when a sweep execution is skipped. It is a notification to the receiver, not an outbound sweep command. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- The request schema requires top-level `data`, `environment` (`test` or `live`), and `type`. Within required `data`, balance account, sweep configuration, platform and resource identifiers, `result`, `resultDetails`, and `triggeredAt` are all marked optional. `timestamp`, when present, is when the event was queued.
- The `result` enum distinguishes `succeeded`, `failed`, and `skipped`; `skipped` means the sweep payout was not triggered as expected. Optional `resultDetails` can carry a reason, reason code, disabled-configuration flag, or transfer ID. The sample's `noBalanceToPayOut` reason is illustrative, not a universal skipped cause.
- The documented 200 response schema has optional `notificationResponse` and says to respond with any `2xx` HTTP status to accept the webhook. Receiver acceptance does not change the sweep result or prove any payout, transfer booking, settlement, or bank receipt.

## Detail locators

- Event purpose and request-body field table: raw lines 5–28.
- Illustrative skipped event payload: raw lines 30–51.
- Receiver response and acknowledgment: raw lines 52–60.

## Related

- [[adyen-webhooks]] — Adyen webhook receipt and acknowledgment.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweepExecution.skipped/2026-11-07|Balance Platform skipped sweep-execution webhook (2026-11-07)]]
