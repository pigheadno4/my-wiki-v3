---
title: "Adyen Docs: Partial payments"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/partial-payments"
raw_files:
  - "adyen/docs/online-payments/partial-payments/2026-09-15.md"
tags: [adyen, online-payments, partial-payments, orders, webhooks]
---

## Overview

This unversioned [[adyen]] website-guide snapshot documents an [[adyen-online-payments]] order flow for combining multiple payment methods in one purchase. The merchant creates an order, submits one or more payments against its remaining amount, and then either observes completion through final payment states and the order-closed webhook or cancels the order.

The page is integration guidance with version-specific examples, not proof of current endpoint behavior, payment-method availability, merchant eligibility, production configuration, or successful payment execution.

## Key takeaways

- `POST /orders` establishes the full order amount and returns `pspReference`, `orderData`, and `remainingAmount`; the page says omitted `expiresAt` defaults to 24 hours after creation. Adyen also documents an `ORDER_OPENED` webhook when the order is created.
- Each `POST /payments` request supplies the order `pspReference` and current `orderData`. An amount below the prior `remainingAmount` is a partial payment. A payment response returns the new remaining amount and a new `orderData` value for the next payment. Redirect methods additionally require their redirect handling.
- `remainingAmount.value` reaching `0` is not completion by itself. The page defines completion as all payments reaching a final payment status and an `ORDER_CLOSED` webhook carrying `success: true`.
- An incomplete order with a positive remaining amount is automatically canceled at expiry. A merchant can also request `/orders/cancel`; the page says the order's previous payments are then canceled or refunded according to payment-method type, and the closing webhook carries `success: false`.
- Once the remaining amount is zero, balance-specific changes operate on individual partial payments through cancellation or refund routes. A full-order reversal instead dynamically cancels or refunds the full order amount according to current payment state.

> [!warning] Evidence and version boundary
> The snapshot's code examples mix explicitly versioned API paths and library releases, including Checkout API `v69` order examples, a `v72` payment curl example, and dated SDK versions. Treat the narrative as a collected guide, use the linked API references for current request contracts, and do not infer account eligibility, webhook delivery timing or ordering, atomic cancellation across payments, or a successful authorization, cancellation, refund, reversal, or settlement from this page alone.

## Detail locators

- **Purpose and lifecycle outline:** raw lines 15-21.
- **Create-order fields, default expiry, examples, response state, and `ORDER_OPENED`:** raw lines 23-315.
- **Payment request fields and versioned examples:** raw lines 317-696.
- **Updated `remainingAmount` and `orderData` for the next payment:** raw lines 698-717.
- **Completion condition and `ORDER_CLOSED` success signal:** raw lines 719-741.
- **Expiry and manual cancellation effects, request fields, examples, and closing failure signal:** raw lines 743-1012.
- **Completed-order individual modifications versus full-order reversal:** raw lines 1014-1023.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-webhooks]] — broader webhook integration and delivery boundaries

## Raw Sources

- [[raw/adyen/docs/online-payments/partial-payments/2026-09-15|Adyen Docs — Partial payments (2026-09-15)]]
