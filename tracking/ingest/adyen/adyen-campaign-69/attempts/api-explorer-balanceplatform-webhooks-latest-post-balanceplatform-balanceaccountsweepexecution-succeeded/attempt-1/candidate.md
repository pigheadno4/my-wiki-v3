---
title: "Balance Platform webhook: sweep execution succeeded"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweepExecution.succeeded"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweepExecution.succeeded/2026-11-07.md"
tags: [adyen, balance-platform, webhooks, sweeps]
---

## Overview

This 2026-11-07 Balance Platform webhooks `latest` snapshot describes Adyen's inbound `balancePlatform.balanceAccountSweepExecution.succeeded` event, sent when a sweep execution succeeds. It is an event delivered to a webhook receiver, not a merchant request to execute a sweep. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The request body requires `data`, `environment` (`test` or `live`), and `type`. Within required `data`, balance-account ID, sweep-configuration ID, platform ID, execution resource ID, result, details, and trigger time are individually optional. `timestamp` for queuing is optional.
- The `result` description distinguishes `succeeded` (sweep payout completed), `failed` (not completed due to error), and `skipped` (not triggered as expected). The named event's example uses `succeeded` and includes a transfer ID, but neither `result` nor `resultDetails.transferId` is schema-required. A transfer ID is a correlation reference, not bank-credit evidence.
- Respond with any HTTP 2xx to accept the webhook; optional `notificationResponse` is the only documented response field. Receiver acknowledgement does not cause or prove sweep execution. The snapshot gives no delivery timing or bank-receipt confirmation.

## Detail locators

- Event purpose and full request-body requiredness/result semantics: pinned raw lines 5–28.
- Test example, including separate execution/configuration/account and transfer IDs: pinned raw lines 30–50.
- Receiver acknowledgement response: pinned raw lines 51–59.

## Related

- [[adyen-platforms]] — sweep configuration and execution context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweepExecution.succeeded/2026-11-07|Sweep execution succeeded webhook snapshot]]