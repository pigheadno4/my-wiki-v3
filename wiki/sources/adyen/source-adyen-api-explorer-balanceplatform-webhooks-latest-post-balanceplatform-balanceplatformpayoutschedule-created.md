---
title: "Adyen Balance Platform webhook: platform payout schedule created"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balancePlatformPayoutSchedule.created"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balancePlatformPayoutSchedule.created/2026-09-15.md"
tags: [adyen, balance-platform, webhooks, managed-payouts]
---

## Overview

This captured Balance Platform Webhooks API Explorer POST reference describes Adyen's incoming `balancePlatform.balancePlatformPayoutSchedule.created` event when a managed payout schedule is successfully created on a balance platform. This is a platform-level schedule creation event, distinct from a schedule being created on or applied to a specific balance account. The `latest` path is a captured label; this page identifies no numbered webhook API version. See [[adyen-platforms]], [[adyen-webhooks]], and [[adyen]].

## Key takeaways

- The request body requires `data`, `environment`, and `type`. `environment` can be `test` or `live`; optional `timestamp` says when the event was queued. The listed `data` properties, including `balancePlatform` and `balancePlatformPayoutScheduleId`, are all marked optional. The schedule ID description mentions a schedule applied to a balance account, but this event's title and trigger establish creation on the balance platform; the page does not identify a specific balance account or prove application to one.
- Optional schedule attributes include country code, currency, default description, frequency and references, payout amount limits, and retained amount. `defaultFrequencyValue` is allowed only with monthly or weekly `defaultFrequency`; the table gives monthly and weekly value ranges and calendar adjustments. A default reference carries to a balance-account schedule unless a new reference is specified. If available funds are below `retainedAmount`, a payout schedule execution is not initiated. These field descriptions do not establish a payout execution for this event.
- The response section says any HTTP `2xx` accepts the webhook; `notificationResponse` is optional. Platform schedule creation and webhook acceptance do not establish account-level application, payout initiation, booking, settlement, or bank receipt. This page has no example payload and states no delivery ordering, retry/deduplication, signature verification, or financial finality guarantee.

## Detail locators

- Event title and platform-level creation trigger: pinned raw lines 5–7.
- Required envelope and optional platform/schedule identifiers: pinned raw lines 11–18 and 27–29.
- Optional defaults, amount limits and execution condition: pinned raw lines 19–26.
- Webhook acceptance response: pinned raw lines 31–39.

## Related

- [[adyen-platforms]] — managed payout schedule context.
- [[adyen-webhooks]] — webhook family and acceptance context.
- [[source-adyen-api-explorer-balanceplatform-webhooks-latest-post-balanceplatform-balanceaccountpayoutschedule-created]] — distinct balance-account schedule creation event.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balancePlatformPayoutSchedule.created/2026-09-15|Platform managed payout schedule created webhook reference, captured 2026-09-15]]
