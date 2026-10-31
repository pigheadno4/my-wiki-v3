---
title: "Adyen negative balance compensation warning scheduled webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/negative-balance-compensation-warning-webhooks/latest/post/balancePlatform.negativeBalanceCompensationWarning.scheduled"
raw_files:
  - "adyen/api-explorer/negative-balance-compensation-warning-webhooks/latest/post/balancePlatform.negativeBalanceCompensationWarning.scheduled/2026-09-15.md"
tags: [adyen, webhooks, platforms, negative-balances]
---

## Overview

Captured 2026-09-15 API Explorer incoming `POST balancePlatform.negativeBalanceCompensationWarning.scheduled` webhook reference. Adyen says the warning concerns a balance account negative for 20 or more days and a future scheduled compensation from the platform's liable balance account if the shortfall is not covered first. The warning does not establish that the compensating transfer has occurred. See [[adyen]], [[adyen-platforms]], and [[adyen-webhooks]].

## Key takeaways

- The body requires `data`, `environment` (`test` or `live`), and `type`; `timestamp` and all listed `data` properties are optional. If the optional `amount` object is present, its `currency` and minor-unit integer `value` are required within that object. Optional identifiers include account holder, balance platform, event/resource ID, and liable balance account ID.
- `negativeBalanceSince` and `scheduledCompensationAt` describe dates; the latter is a planned compensation date, not transfer execution evidence. The sample is a TEST example with EUR -145050, a liable balance account ID, and a future compensation date; its example values do not establish a specific account's current state.
- **Timing conflict in this captured page:** prose says the balance has been negative for 20 or more days, but the example shows `negativeBalanceSince` 2024-10-19 and event `creationDate` 2024-10-22, about three days later. Do not derive a reliable warning threshold from that example.
- The response says webhook acceptance is based on HTTP status code, without a specific acceptance code on this page. This reference does not establish delivery order, retries, deduplication, signature verification, actual compensation, or final balance.

## Detail locators

- Trigger and conditional future transfer: raw lines 5–7.
- Requiredness, amount, identities and dates: raw lines 11–30.
- TEST example and timing discrepancy: raw lines 32–58.
- Response wording: raw lines 59–62.

## Raw Sources

- [[raw/adyen/api-explorer/negative-balance-compensation-warning-webhooks/latest/post/balancePlatform.negativeBalanceCompensationWarning.scheduled/2026-09-15|Captured negative balance compensation warning reference]]
