---
title: "Adyen ManagementNotification latest: paymentMethod.created"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/ManagementNotification/latest/post/paymentMethod.created"
raw_files:
  - "adyen/api-explorer/ManagementNotification/latest/post/paymentMethod.created/2026-09-15.md"
tags: [adyen, webhooks, management, payment-methods]
---

## Overview

This 2026-09-15 snapshot of Adyen's ManagementNotification `latest` `paymentMethod.created` reference describes an incoming webhook after a request to add a payment method has completed. It is a notification contract, not the request to add a method or proof that the method can receive payments. [[adyen]] [[adyen-webhooks]]

## Key takeaways

- The required `data.status` reports the add-request outcome: `success` means the method was added; `failure` means the request failed; `capabilityPending` means the `receivePayments` capability is not allowed. Keep this request status separate from optional `data.enabled`, `data.allowed`, and `data.verificationStatus`. The reference says Adyen sets `allowed` to true after merchant-account screening.
- Required identifiers include `data.id` for the payment-method resource and `data.merchantId` for the merchant account. `data.storeId` and merchant-supplied `data.reference` are optional. `data.type` is the payment-method variant; the outer `type` is the notification type.
- The sample is for `environment: test` and `type: paymentMethod.created`, with `data.status: success`. It does not illustrate `allowed`, `enabled`, or `verificationStatus`, so sample success alone does not establish those states.
- The response section says any `2xx` HTTP status code accepts the webhook. That response concerns receipt, not the add-request status or permission to receive payments.

## Detail locators

- Request body requiredness, statuses and identifiers: pinned raw lines 9–26. `createdAt` is the webhook creation timestamp; `environment` is `test` or `live`.
- Example payload: pinned raw lines 28–44.
- `200 Success` and optional `notificationResponse` response-body field: pinned raw lines 45–53. The page gives no delivery ordering, retry, deduplication, or signature rule.

## Related

- [[adyen]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/api-explorer/ManagementNotification/latest/post/paymentMethod.created/2026-09-15|Adyen ManagementNotification paymentMethod.created reference (2026-09-15)]]
