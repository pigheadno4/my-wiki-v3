---
title: Subscriptions webhooks
slug: /docs/subscriptions/reference/webhooks/
createTime: "2025-03-18T01:40:44.873Z"
updateTime: "2025-03-18T01:52:30.559Z"
---

# Subscriptions webhooks

A webhook is an HTTP callback that receives notification messages for events. See [configure webhooks](/api/rest/webhooks/) for more details.

PayPal APIs use webhooks for event notification. Most subscription-related actions trigger webhook events:

| Webhook                               | Trigger                                   | Related method                                                                                |
| ------------------------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------- |
| CATALOG.PRODUCT.CREATED               | A product is created.                     | [Create product](/docs/api/catalog-products/v1/#products_create)                              |
| CATALOG.PRODUCT.UPDATED               | A product is updated.                     | [Update product](/docs/api/catalog-products/v1/#products_patch)                               |
| PAYMENT.SALE.COMPLETED                | A payment is made on a subscription.      |                                                                                               |
| PAYMENT.SALE.REFUNDED                 | A merchant refunds a sale.                |                                                                                               |
| PAYMENT.SALE.REVERSED                 | A payment is reversed on a subscription.  |                                                                                               |
| BILLING.PLAN.CREATED                  | A billing plan is created.                | [Create plan](/docs/api/subscriptions/v1/#plans_create)                                       |
| BILLING.PLAN.UPDATED                  | A billing plan is updated.                | [Update plan](/docs/api/subscriptions/v1/#plans_patch)                                        |
| BILLING.PLAN.ACTIVATED                | A billing plan is activated.              | [Activate plan](/docs/api/subscriptions/v1/#plans_activate)                                   |
| BILLING.PLAN.PRICING-CHANGE.ACTIVATED | A price change for the plan is activated. | [Update pricing](/docs/api/subscriptions/v1/#plans_update-pricing-schemes)                    |
| BILLING.PLAN.DEACTIVATED              | A billing plan is deactivated.            | [Deactivate plan](/docs/api/subscriptions/v1/#plans_deactivate)                               |
| BILLING.SUBSCRIPTION.CREATED          | A subscription is created.                | [Create subscription](/docs/api/subscriptions/v1/#subscriptions_create)                       |
| BILLING.SUBSCRIPTION.ACTIVATED        | A subscription is activated.              | [Activate subscription](/docs/api/subscriptions/v1/#subscriptions_activate)                   |
| BILLING.SUBSCRIPTION.UPDATED          | A subscription is updated.                | [Update subscription](/docs/api/subscriptions/v1/#subscriptions_patch)                        |
| BILLING.SUBSCRIPTION.EXPIRED          | A subscription expires.                   | [Show subscription details](/docs/api/subscriptions/v1/#subscriptions_get)                    |
| BILLING.SUBSCRIPTION.CANCELLED        | A subscription is cancelled.              | [Cancel subscription](/docs/api/subscriptions/v1/#subscriptions_cancel)                       |
| BILLING.SUBSCRIPTION.SUSPENDED        | A subscription is suspended.              | [Suspend subscription](/docs/api/subscriptions/v1/#subscriptions_suspend)                     |
| BILLING.SUBSCRIPTION.PAYMENT.FAILED   | Payment failed on subscription.           | [Subscription failed payment details](/docs/api/subscriptions/v1/#subscriptions-get-response) |
