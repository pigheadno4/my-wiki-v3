---
title: "Adyen deprecated Payment webhook: balancePlatform.payment.updated"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/payment-webhooks/latest/post/balancePlatform.payment.updated"
raw_files:
  - "adyen/api-explorer/payment-webhooks/latest/post/balancePlatform.payment.updated/2026-09-15.md"
tags: [adyen, platforms, payment-webhooks, deprecated, authorisation]
---

## Overview

Captured incoming `POST balancePlatform.payment.updated` reference for a payment authorisation that expired or was cancelled. The page says to use `data.id` to track the original authorisation from `balancePlatform.payment.created`; the parameter table nevertheless marks `data.id` optional. This is a legacy Payment webhook event, not a Transfer or Transaction webhook. [[adyen]] [[adyen-platforms]]

The separate [Payment webhooks v1 family overview](https://docs.adyen.com/api-explorer/payment-webhooks/latest/overview), captured 2026-09-15, explicitly marks this family deprecated and directs readers to accounting webhooks at the Transfer-webhooks overview. That migration statement comes from the family overview, not this endpoint's raw page.

## Key takeaways

- The request table requires top-level `data`, `environment` and `type`. Within `data`, its listed fields, including `id`, `status`, `modification`, account-holder and balance-account objects, are optional. For optional `amount` and `originalAmount` objects, `currency` and minor-unit `value` are required when the object is present. See raw lines 11–30 and 37–79.
- The page's introductory trigger is expiry or cancellation. Its `data.status` row additionally lists `AuthAdjustmentAuthorised` and `AuthAdjustmentRefused` for this event type; the wider row also lists values for other event types. Preserve that type-specific distinction. See raw lines 5–7 and 63.
- Optional `data.modification` describes the amount and type that triggered the notification, including partial cancellation or partial expiry. The converted `amount` and `modification.amount` descriptions define positive as added to the balance account and negative as deducted; `originalAmount` is in the transaction's original currency. See raw lines 19–21 and 37–42.
- The three TEST request examples are labelled expired, partially cancelled and partially expired. All three show `data.status: "Expired"` and `modification.type: "Expired"`; the “partially cancelled” label therefore does not by itself establish a `Cancelled` payload. Their `timestamp` precedes `creationDate` despite the table describing queue time and event-trigger time respectively, so these examples should not be used to infer an event-to-queue interval. See raw lines 83–387, especially 88, 118, 136, 180, 190, 220, 238 and 282.
- The response section shows `200 Success`; any `2xx` status accepts the webhook, with optional `notificationResponse`. Receipt does not show payment settlement, a balance-account booking, or a final funds outcome. See raw lines 388–396.

## Detail locators

- Event purpose and `data.id` correlation to the created event: raw lines 5–7.
- Full optional/required field table, identifiers, platform-payment references, relayed-authorisation fields, validation and status types: raw lines 11–79.
- Expired, partially cancelled and partially expired TEST examples: raw lines 81–387.
- Receiver response and acceptance: raw lines 388–396.

## Related

- [[adyen-platforms]] — platform payment and account context.
- [[adyen-webhooks]] — general receiver context.

## Raw Sources

- [[raw/adyen/api-explorer/payment-webhooks/latest/post/balancePlatform.payment.updated/2026-09-15|Payment updated webhook reference captured 2026-09-15]]
