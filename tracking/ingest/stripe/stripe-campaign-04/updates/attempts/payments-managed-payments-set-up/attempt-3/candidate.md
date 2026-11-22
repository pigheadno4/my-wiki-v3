---
title: "Build a Checkout Integration with Managed Payments"
type: source
date_ingested: 2026-04-23
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/managed-payments/set-up"
raw_files:
  - "stripe-payments-managed-payments-set-up-2026-11-07.md"
  - "stripe-managed-payments-setup-2025.md"
tags: [stripe, managed-payments, checkout, merchant-of-record, subscriptions, one-time-payments, tax-behavior, webhooks]
---

## Summary

The April 23 and November 7, 2026 captures show how to build a **new Stripe-hosted Checkout integration** with Managed Payments for subscriptions and one-time purchases. The November guide describes Stripe as the merchant of record for eligible digital products such as SaaS, software, and digital content. It describes indirect-tax compliance in more than 80 countries, fraud prevention, dispute management, and transaction-level customer support. See [[source-stripe-managed-payments-how-it-works]] for coverage boundaries, including seller responsibility where Stripe does not handle indirect tax. Its November capture explicitly excludes custom domains from Managed Payments checkouts.

## Prerequisites

- Both captures require Dashboard activation, a development environment, and API version `2025-03-31.basil` or later.
- The April 23 guide explicitly requires accepting the Managed Payments terms of service in the Dashboard before use and says all products the customer is purchasing must be eligible to process the payment with Managed Payments.
- The November 7 guide calls for product eligibility before processing and an eligible tax code on the product. It omits the express merchant terms-acceptance sentence. The captures leave the current terms-acceptance workflow and mixed-cart error or fallback behavior undetermined. See [[source-stripe-managed-payments-eligibility]] for the dated eligibility rules.

## Create a hosted Checkout Session

Create products and one-time or recurring Prices through the Dashboard or API. Give each product sold through Managed Payments an eligible `tax_code`; the Dashboard labels these codes. The preview pane shows tax by customer location. For subscriptions the Price example sets `recurring.interval`; the one-time Price omits `recurring`.

The checkout button calls a merchant server endpoint. Use the Price as a line item, choose `mode: 'subscription'` for a subscription or `mode: 'payment'` for a one-time purchase, and set `managed_payments.enabled: true` to enable Managed Payments. **The November guide explicitly documents `managed_payments.enabled: false` to disable Managed Payments for a specific Session at creation.** These captures leave the field's omission default and any post-creation effect undetermined.

Use `success_url` for the hosted success page and the optional `cancel_url` for the cancellation destination. The November Checkout Sessions Create reference documents them as separate fields, clarifying the ambiguous setup prose. After creating the Session, the server redirects the browser to the returned Stripe-hosted Session URL. The examples use HTTP 303.

April hosted Node example, with a merchant success URL:

```javascript
stripe.checkout.sessions.create({
    line_items: [{ price: priceId, quantity: 1 }],
    managed_payments: { enabled: true },
    mode: 'subscription', // or 'payment'
    success_url: 'https://example.com/success',
})
```

The November capture uses cURL to create Sessions at lines 282–314 and Ruby/Sinatra for the endpoint at lines 316–380.

## Hosted and embedded scope

This setup guide demonstrates hosted Checkout. The separate November 7 [[source-stripe-managed-payments-update-checkout]] guide lists existing hosted or embedded Checkout pages that create `payment`- or `subscription`-mode Sessions as a migration prerequisite. It limits subscription adoption to new eligible purchases, and its server examples use the hosted `success_url`. Those examples document the hosted implementation.

The November Checkout Sessions Create reference distinguishes an embedded Checkout form (`ui_mode: embedded_page`) from Checkout Elements (`ui_mode: elements`). Both modes exclude `success_url` and `cancel_url`, and require `return_url` when redirect-based payment methods are enabled. This is API field scope, separate from Managed Payments product eligibility.

## Webhooks

| Event | What it signals |
| --- | --- |
| `checkout.session.completed` | The customer completed Checkout. A delayed payment may still be pending. |
| `checkout.session.async_payment_succeeded` | A delayed payment succeeded. |
| `checkout.session.async_payment_failed` | A delayed payment failed. |

Use server webhooks for downstream paid-order actions. Check paid status on Session completion and handle delayed success or failure separately. A 303 and the browser's return describe navigation. ACH Direct Debit illustrates a delayed method in the event table.

## Tax behavior

An explicit Price `tax_behavior` takes precedence: `exclusive` adds tax and `inclusive` includes tax in the price. Where Price tax behavior is unspecified, the guide says Managed Payments adds tax on top by default. Change the fallback in **Dashboard → Tax settings → Include tax in prices**.

## Subscription consent and Link testing

- When a customer purchases a subscription through Managed Payments, the purchase authorizes only Managed Payments to charge that payment method. Obtain appropriate separate customer consent before using the method outside Managed Payments.
- The guide describes Link as the customer-facing merchant of record at checkout, with subscription management and transaction support on Link. The test passcode is `000000` when testing with the same Link email. Test purchases stay out of the Link app. The guide describes a live-mode Checkout Session for testing the app's order-management tools. Sandbox receipt emails can be sent manually.

## Related Pages

- [[stripe]] — payment provider
- [[stripe-managed-payments]] — Managed Payments integration options
- [[stripe-checkout]] — Checkout UI, API, and fulfillment
- [[source-stripe-managed-payments-how-it-works]] — Link, coverage, and checkout restrictions

## Raw Sources

- [[raw/stripe-payments-managed-payments-set-up-2026-11-07|2026-11-07 hosted Checkout setup guide]]
- [[raw/stripe-managed-payments-setup-2025|2026-04-23 hosted Checkout setup guide]] — 531 lines

## Related raw API references

- [[raw/stripe-api-checkout-sessions-create-2026-11-07|2026-11-07 Checkout Sessions Create reference]] — hosted URLs and UI-mode fields at lines 198–199, 464–477, and 512–525
