---
title: "Adyen ManagementNotification latest paymentMethodRequest.scheduledForRemoval"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/ManagementNotification/latest/post/paymentMethodRequest.scheduledForRemoval"
raw_files:
  - "adyen/api-explorer/ManagementNotification/latest/post/paymentMethodRequest.scheduledForRemoval/2026-09-15.md"
tags: [adyen, webhooks, management, payment-methods]
---

## Overview

This 2026-09-15 API Explorer ManagementNotification `latest` POST paymentMethodRequest.scheduledForRemoval snapshot describes an incoming notification that a request to add a payment method will be removed in 30 days. The page says to provide missing KYC information to make sure the payment method is added. It describes scheduled future removal of the request, not completed removal of an enabled payment method. See [[adyen]], [[adyen-webhooks]], and [[adyen-payment-method-variants]].

## Key takeaways

- The required body fields are `createdAt` (webhook creation timestamp), `data` (event details), `environment` (`test` or `live`), and outer `type` (notification type). Within `data`, `id` is the resource ID, `merchantId` the merchant-account ID, `status` the add-method request status, and inner `type` the payment-method variant; all four are marked required. The page supplies no request example or exact outer `type` value beyond the POST heading.
- `data.status` values are `success` (method added), `failure` (request failed), and `capabilityPending` (the `receivePayments` capability is not allowed). Optional `allowed` concerns receiving-payments permission after screening; optional `enabled` concerns whether the payment method is enabled. Optional `verificationStatus` has `valid`, `pending`, `invalid`, and `rejected` values. These fields describe different states; this notification's heading alone proves none of them has reached a final approved or enabled state.
- Optional `reference` is the merchant's payment-method reference; optional `storeId` identifies a store if present. The 30-day statement gives a removal horizon for the add request, but the page supplies no exact removal timestamp, remediation deadline calculation, or later removal event contract.
- The response lists `200 Success`, an optional `notificationResponse` string, and acceptance by any `2xx` HTTP status. That is webhook receipt, separate from adding the method, completing KYC, gaining `receivePayments`, or enabling payments. No delivery, ordering, retry, deduplication, signature, or payment-processing guarantee is stated here.

## Detail locators

- Notification purpose, 30-day horizon and KYC direction: raw lines 5–7.
- Body requiredness and nested state/identity fields: raw lines 11–26.
- Receiver response and 2xx acceptance: raw lines 28–36.

## Related

- [[adyen]]
- [[adyen-webhooks]]
- [[adyen-payment-method-variants]]

## Raw Sources

- [[raw/adyen/api-explorer/ManagementNotification/latest/post/paymentMethodRequest.scheduledForRemoval/2026-09-15|ManagementNotification scheduled-for-removal reference (2026-09-15)]]
