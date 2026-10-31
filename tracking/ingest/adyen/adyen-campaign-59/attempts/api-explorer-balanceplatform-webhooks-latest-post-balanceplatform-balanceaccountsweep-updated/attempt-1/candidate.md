---
title: "Sweep updated webhook | Adyen Balance Platform webhooks"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweep.updated"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweep.updated/2026-09-15.md"
tags: [adyen, platforms, sweeps, webhooks]
---

## Overview

This captured Balance Platform webhook POST reference says Adyen sends `balancePlatform.balanceAccountSweep.updated` after a successful sweep-configuration update. It describes an incoming event associated with a balance account and sweep resource, not an instruction to update a sweep or evidence that a sweep transfer executed. The `latest` URL is the captured label, not proof of a current version. [[adyen-platforms]] [[adyen-webhooks]]

## Key takeaways

- The body marks `data`, `environment` (`test` or `live`) and `type` required. Within `data`, the balance-account `accountId`, `balancePlatform`, and `sweep` are optional; within a present `sweep`, `counterparty`, `currency`, `id` and `schedule` are marked required. The counterparty description requires one of `balanceAccountId`, `transferInstrumentId` or `merchantAccount`, according to sweep direction.
- Sweep `type` describes push out of, or pull in to, the balance account and defaults to `push` when omitted. `status` defaults to `active`; `inactive` disables triggering. The optional `triggerAmount` is evaluated on the specified schedule and defaults to zero: pull triggers when balance is at or below it, push when balance is at or above it. `sweepAmount` and `targetAmount` are alternative configuration amounts, not simultaneous settings. The configured currency must match one of the balance currencies.
- The optional category distinguishes bank transfers to a transfer instrument from internal transfers to another platform balance account. The `priorities` description concerns ordered bank-transfer route preferences and states that at least one provided priority must be valid for request acceptance. These configuration descriptions do not establish a particular transfer, balance booking, payout or recipient-bank receipt.
- The test example shows an inactive weekly push sweep with EUR zero target and trigger amounts and a destination balance-account ID; it is illustrative, not a general requirement. The response section says any `2xx` accepts the webhook. This reference does not establish delivery ordering, retries, deduplication, signature verification or transfer finality.

## Detail locators

- Event trigger and identity: raw lines 5–7 and 40–70.
- Body requiredness and resource identities: raw lines 9–22 and 34–36.
- Direction, status, schedule/amount thresholds, currency, category and priorities: raw lines 18–33.
- Example payload and webhook acknowledgment: raw lines 38–80.

## Related

- [[adyen-platforms]] — platform balance-account and sweep context.
- [[adyen-platform-internal-transfers]] — separate internal-fund-transfer context.
- [[adyen-webhooks]] — general webhook handling context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweep.updated/2026-09-15|Captured balancePlatform.balanceAccountSweep.updated reference]]
