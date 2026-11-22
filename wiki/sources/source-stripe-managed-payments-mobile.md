---
title: "iOS Digital Products with Managed Payments (MoR)"
type: source
date_ingested: 2026-04-23
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/managed-payments/set-up-mobile"
raw_files:
  - "stripe-payments-managed-payments-set-up-mobile-2026-11-07.md"
  - "stripe-managed-payments-mobile-2025.md"
tags: [stripe, managed-payments, merchant-of-record, mobile, ios, digital-goods, checkout, universal-links, origin-context]
---

## Summary

The 2026-04-23 and 2026-11-07 [[stripe|Stripe]] guides describe an iOS app-to-web flow for eligible digital goods and subscriptions in some countries where iOS apps can link to external payment pages. The app opens Stripe-hosted Checkout in Safari. Stripe acts as merchant of record, and Link provides the customer-facing checkout, subscription management, and transaction support. The app operator maintains the app user, the Stripe Customer association, and the entitlement ledger. Product-level support stays with the operator. The captures leave current country, storefront, account, and App Store eligibility unverified.

## Eligibility and Setup

Both guides require all products in the purchase to qualify, including an eligible tax code for each Product. They also call for Dashboard activation, a configured development environment, and API version `2025-03-31.basil` or later. The video-game coin example uses tax code `txcd_10201000` for downloaded, non-subscription games with permanent rights. The guide assumes an existing system for app user authentication. Native StoreKit in-app purchases are outside its scope.

The 2026-04-23 mobile and [[source-stripe-managed-payments-setup|general Checkout setup]] captures explicitly require accepting the Managed Payments terms in the Dashboard before use. The 2026-11-07 guides retain Dashboard activation in their checklists and omit the separate terms callout. The omission leaves current terms and account onboarding requirements unresolved.

## Key Checkout Session Parameters

The merchant's server creates or reuses a Stripe Customer and stores the app-user-to-Customer mapping so customers can recover purchases. It creates the Checkout Session for that Customer and returns the hosted Session URL to the app. The examples use a Price ID in `line_items`, `mode: 'payment'` for one-time purchases or `mode: 'subscription'` with a recurring Price, `managed_payments.enabled` to use Managed Payments, and `origin_context: 'mobile_app'` to opt in to the app-to-web UI.

```javascript
stripe.checkout.sessions.create({
  line_items: [{ price: priceId, quantity: 1 }],
  managed_payments: { enabled: true },
  origin_context: 'mobile_app',
  mode: 'payment',
  customer: customerId,
  success_url: 'https://example.com/checkout_redirect/success',
})
```

## Safari and Universal Link Return

The Swift sample checks `SKPaymentQueue.canMakePayments()` for device purchase restrictions such as parental controls, then opens the server-provided URL with `UIApplication.shared.open`. Configure the domain's `apple-app-site-association` file, the app's Associated Domains entitlement, and a fallback page at the Universal Link `success_url`. The return lets the app update its UI and fetch current entitlements from the server.

The captures describe redirect after webhook acknowledgement, or after 10 seconds following a successful payment if the event is unacknowledged. Redirect and event acknowledgement are separate from the server persisting the entitlement.

## Server Fulfillment

The mobile example receives `checkout.session.completed` for a successful purchase, maps `session.customer` to the app user, and passes `session.id` to a coin-transaction operation. Grant credits from verified server events after confirming the paid outcome, using an idempotent per-Session entitlement operation. If a delayed method is offered and completion arrives with payment still pending, wait for `checkout.session.async_payment_succeeded` and handle `checkout.session.async_payment_failed`. The [[source-stripe-managed-payments-setup|general Managed Payments setup guide]] lists both asynchronous events, and the [[source-stripe-inapp-digital-goods-checkout|separate non-MoR iOS Checkout guide]] explains the paid-status check. The mobile captures leave delayed-method availability and the sample's end-to-end idempotency unverified. The return URL is an app refresh signal only.

Both captured Node.js examples show raw-body signature verification with the configured secret, include an unsigned fallback, and later read `event.data.object` outside the block that declares `event` instead of using the extracted data. Apply verified event handling and paid-status checks in production. The archived example is illustrative and leaves production execution unverified.

## Subscription Authorization

Both captures say a Managed Payments subscription authorizes charges by Managed Payments only. Obtain appropriate customer consent before charging that method for transactions outside Managed Payments.

## Optional Price and Tax Display

The 2026-11-07 guide adds optional controls in Dashboard Checkout and Payment Links settings for whether yearly subscription prices display in monthly terms and whether taxes are shown. This documentation covers presentation. It gives no change to the recurring interval, charged amount, or tax calculation or collection.

## Related Pages

- [[stripe-managed-payments]] — merchant-of-record concept and general setup routes
- [[stripe-inapp-payments]] — overview of mobile integration routes
- [[source-stripe-inapp-digital-goods-checkout]] — separate US-scoped non-MoR app-to-web route, with a storefront check and a qualified Accounts v2 `customer_account` branch. The Managed Payments mobile samples use the mapped Customer ID in `customer`.
- [[source-stripe-managed-payments-setup]] — general Checkout setup, dated terms wording, tax behavior, and asynchronous event handling

## Detail Locators

- 2026-11-07 raw lines 36–67 and 142–173 cover prerequisites, the Product and Price example, and Customer mapping.
- 2026-11-07 raw lines 175–323 and 335–379 cover the Universal Link setup, Checkout Session examples, StoreKit device check, and Safari return.
- 2026-11-07 raw lines 429–489 cover acknowledgement, redirect, and the fulfillment sample. Lines 515–517 cover subscription authorization.
- 2026-11-07 raw lines 491–554 cover sandbox card examples, manual receipt previews, and Link's test passcode `000000`. Test purchases do not appear in the Link app. Lines 556–599 cover Universal Link diagnostics.
- 2026-04-23 raw lines 8–10 retain the explicit terms instruction. 2026-11-07 raw lines 601–603 describe the display settings.

## Raw Sources

- [[raw/stripe-payments-managed-payments-set-up-mobile-2026-11-07|2026-11-07 iOS Managed Payments guide]]
- [[raw/stripe-managed-payments-mobile-2025|2026-04-23 iOS Managed Payments guide]]
