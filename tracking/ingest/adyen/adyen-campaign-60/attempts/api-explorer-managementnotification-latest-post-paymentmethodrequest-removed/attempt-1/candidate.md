---
title: "Adyen ManagementNotification paymentMethodRequest.removed webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/ManagementNotification/latest/post/paymentMethodRequest.removed"
raw_files:
  - "adyen/api-explorer/ManagementNotification/latest/post/paymentMethodRequest.removed/2026-09-15.md"
tags: [adyen, management, webhooks, payment-methods]
---

## Overview

This 2026-09-15-captured ManagementNotification `latest` reference describes the incoming `POST paymentMethodRequest.removed` notification: a request to add a payment method was removed. The page says another add-payment-method request must be made. This event concerns the request resource; it does not itself say that an enabled payment method was removed or that a payment was reversed.

## Key takeaways

- The request body requires `createdAt`, `data`, `environment`, and top-level `type`. Within required `data`, it marks `id` (resource ID), `merchantId`, `status`, and nested `type` (payment-method variant) required. Top-level notification `type` and nested payment-method `type` have different meanings; this page shows no example value for either.
- `data.status` is the status of the request to add a payment method, with listed values `success`, `failure`, and `capabilityPending`. The description says `success` means the payment method was added, `failure` means the request failed, and `capabilityPending` means `receivePayments` is not allowed. This is the general field vocabulary; the page gives no removed-event example status or timing, so it does not identify which value accompanies removal.
- Optional `data.allowed` indicates whether receiving payments is allowed and is set true by Adyen after merchant-account screening. Optional `enabled` reports payment-method enablement, `verificationStatus` can be valid/pending/invalid/rejected, and optional `storeId` scopes a store if present. None of these optional fields is a required consequence of removal in this reference.
- The response section labels `200 Success` and says the request has succeeded. Its optional `notificationResponse` row instructs a receiver to return any `2xx` status to accept the webhook. That is event-receipt acceptance, separate from the add-request status, payment-method enablement, screening allowance, or payment outcomes. No delivery, ordering, retry, deduplication or signature rule is specified here.

## Detail locators

- Raw lines 5–7: event meaning and need for another add-method request.
- Raw lines 11–26: body requiredness, identities, status vocabulary and optional capability/enablement fields.
- Raw lines 28–36: receiver response and `2xx` acceptance.

## Related

- [[adyen]] — company route.
- [[adyen-webhooks]] — webhook family and receipt distinctions.
- [[adyen-payment-method-variants]] — variant vocabulary, separate from merchant setup eligibility.

## Raw Sources

- [[raw/adyen/api-explorer/ManagementNotification/latest/post/paymentMethodRequest.removed/2026-09-15|paymentMethodRequest.removed reference, captured 2026-09-15]]
