---
title: "Adyen managed-risk rolling reserve updated webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.rollingReserve.updated"
raw_files:
  - "adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.rollingReserve.updated/2026-09-15.md"
tags: [adyen, managed-risk, rolling-reserve, webhooks, platforms]
---

## Overview

Captured Managed Risk webhook reference for incoming `POST balancePlatform.managedRisk.rollingReserve.updated`. Adyen says it sends this event when it updates a rolling reserve policy applied to an account holder's payouts because of their risk level. This is a policy-change notification, not a payout, balance-account reserve transfer, or proof that withheld funds have been released. [[adyen]] [[adyen-platforms]]

## Key takeaways

- Required `data.accountHolderId` identifies the account holder whose risk settings changed. The same nested data requires `rollingReservePercentage`, the percentage of the user's daily sales volume withheld from the settlement batch, and `withHoldingPeriodInDays`, the number of days after which that withheld percentage is released. The page gives no minimum, maximum or effective-date rule. See raw lines 14–19.
- Nested `balancePlatform` and `creationDate` are optional; `creationDate` is the event-trigger time in ISO 8601 extended format. The top-level `environment` and `type` are required, while `timestamp` is optional and means queue time. See raw lines 16–22.
- The test example contains `data.id`, which is absent from the request-body parameter table; the example alone does not make it a documented required field. See raw lines 11–22 and 24–40.
- The response section shows `200 Success`; the optional `notificationResponse` row says any `2xx` HTTP status code accepts the webhook. That acceptance describes receiver handling, not settlement, payout execution or fund release. See raw lines 41–49.

## Detail locators

- Event trigger and policy scope: raw lines 5–7.
- Request envelope, account-holder identity and reserve policy values: raw lines 11–22.
- Illustrative test event, including example-only `data.id`: raw lines 24–40.
- Receiver response and acceptance: raw lines 41–49.

## Related

- [[adyen-platforms]] — modern account-holder and payout context.
- [[adyen-webhooks]] — general receiver context.

## Raw Sources

- [[raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.rollingReserve.updated/2026-09-15|Managed Risk rolling reserve updated reference captured 2026-09-15]]
