---
title: "Adyen balance-platform managed payout schedule updated webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balancePlatformPayoutSchedule.updated"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balancePlatformPayoutSchedule.updated/2026-09-15.md"
tags: [adyen, webhooks, balance-platform, managed-payouts]
---

## Overview

Captured API Explorer reference for the incoming `balancePlatform.balancePlatformPayoutSchedule.updated` webhook. Adyen sends it when a managed payout schedule is successfully updated **on the balance platform**. This is a schedule-definition update, not evidence that the schedule was applied to a particular balance account or that a payout ran. The `latest` URL was captured on 2026-09-15 and does not pin an API version.

## Key takeaways

- The webhook body requires top-level `data`, `environment`, and `type`; `timestamp` is optional. Every listed `data` property is marked optional, including the balance-platform and payout-schedule IDs, country, currency, default description/frequency/references, minimum and maximum payout amounts, and retained amount. `environment` can be `test` or `live`.
- The schedule ID field describes a balance-platform payout schedule “that is applied to the balance account,” although this event's heading and trigger describe an update on the balance platform. The field description alone does not establish application to any specific account; no balance-account ID is listed.
- The `defaultFrequencyValue` description allows it only for monthly or weekly default frequency and describes date and weekday ranges, weekend shift, and nonexistent month-end date handling. The monthly 1–31 range sentence uses `frequency`, while the weekly 1–5 range sentence uses `defaultFrequency`; preserve those distinct labels rather than resolving them by inference.
- `retainedAmount` is the amount that must remain available after a schedule execution; the description says execution is not initiated if account funds are below that amount. The reference does not specify amount units or a particular currency conversion for the integer amount fields.
- The response section says any HTTP `2xx` accepts the webhook. It supplies no example payload or event-specific ordering, retry, deduplication, signature, payout execution or bank-receipt guarantee.

## Detail locators

- Event identity and platform-level update trigger: raw lines 5–7.
- Envelope and schedule fields: raw lines 11–29; frequency/date wording at line 21 and retained amount at line 26.
- Acknowledgment: raw lines 31–39.

## Related

- [[adyen]]; [[adyen-webhooks]]; [[adyen-platforms]].

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balancePlatformPayoutSchedule.updated/2026-09-15|2026-09-15 captured API Explorer reference]]
