---
title: "Adyen Balance Platform sweep deleted webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweep.deleted"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweep.deleted/2026-09-15.md"
tags: [adyen, balance-platform, webhooks, sweeps]
---

## Overview

This 2026-09-15-captured API Explorer `latest` POST reference describes the incoming `balancePlatform.balanceAccountSweep.deleted` webhook Adyen sends after a sweep is successfully deleted. It concerns deletion of the sweep configuration, not reversal or completion of a transfer. [[adyen]] [[adyen-webhooks]] [[adyen-platforms]]

## Key takeaways

- The event body requires `data`, `environment` and `type`; `data.accountId`, `data.balancePlatform`, and `data.sweep` are marked optional. If `sweep` is supplied, its nested `counterparty`, `currency`, `id` and `schedule` are marked required. The configuration ID is `sweep.id`, while `accountId` is the balance account for which it was configured. See raw lines 11–36.
- The nested sweep schema describes bank or internal `category`, source/destination `counterparty`, and `push` or `pull` direction. It describes threshold evaluation on a schedule, with optional `sweepAmount` or `targetAmount` (one or the other), optional `triggerAmount`, and optional `status`. These describe the sweep resource, not a transfer triggered by this deletion event. See raw lines 17–33.
- The test example includes a `push` sweep to another balance account and `status: active` inside the deleted-sweep payload. That example status must not be read as proof the configuration remains active after deletion. No transfer ID, executed amount, booked movement or beneficiary-bank receipt is shown. See raw lines 38–71.
- The response table says any HTTP 2xx accepts the webhook; `notificationResponse` is optional. The page does not establish delivery ordering, retries, deduplication, signature verification, or transfer finality. See raw lines 72–80.

## Detail locators

- Envelope and nested sweep fields: raw lines 9–36.
- Test example and event type: raw lines 38–71.
- Acknowledgment: raw lines 72–80.

## Related

- [[adyen-webhooks]]
- [[adyen-platforms]]
- [[adyen-platform-internal-transfers]]

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweep.deleted/2026-09-15|Sweep deleted webhook reference, captured 2026-09-15]]
