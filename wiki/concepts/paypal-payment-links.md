---
title: "PayPal Payment Links and Buttons"
type: concept
category: technology
tags: [paypal, payment-links, buy-button, qr-code, no-code, invoicing]
---

## PayPal Payment Links and Buttons

PayPal's suite of no-code payment acceptance tools. Customers complete payment on a PayPal-hosted page; no checkout integration required. 200+ countries, 23+ currencies, PCI compliance handled by PayPal.

## Four Options

| Option | Use case |
| --- | --- |
| **Payment Link** | Shareable URL via email/social/messages; reusable |
| **Buy Button** | Single product HTML embed on a website |
| **Shopping Cart Button** | Multi-product cart with Add to Cart + View Cart buttons |
| **QR Code** | In-person / contactless payments |

All are no-code. Buy Button and Shopping Cart Button require basic HTML editing on a website.

## API Details

Endpoint: `POST /v1/checkout/payment-resources` — returns `PLB-*` ID; payment link URL is in `links[]` with `rel: "payment_link"`. PUT is full replace. DELETE is permanent. Must enable "Payment Links & Buttons" in app credentials.

The `paypal/postman-collections` baseline at `7f7240a` provides create, list, retrieve, replace, and delete payment-resource examples. This is runnable payload evidence only; current enablement and endpoint behavior remain governed by product documentation and the live API.

## Integration Options

> [!info] API scope limitation
> The Payment Links and Buttons **API supports payment links only**. Buy buttons and shopping cart buttons are dashboard-only.

- **UI Editor**: dashboard, no-code, manual management, low-to-medium volume
- **API**: programmatic creation, high-volume/dynamic, returns URLs to embed in your own flows

### Native mobile hosted-browser pattern

The `paypal-examples/paypal-android-sdk-demo-app` baseline at `d1137d5` opens a pre-created sandbox Payment Link in an Android Custom Tab and handles both warm and cold App Link returns. This is a hosted checkout path, independent of the app's direct PayPal Android SDK order flow.

> [!warning] Return links do not prove payment
> The sample marks its UI complete from an expected return host and a path containing `success`; it does not verify the transaction first. Production apps must use trusted server-side payment state, APIs, or webhooks before fulfillment.

## Payment Methods

PayPal, Pay Later, Venmo, Apple Pay, debit/credit cards. Invoicing also adds Pay by Bank (ACH).

## Key Constraints

- **No expiration** — links never expire; no single-use support
- **One-time payments only** — no subscriptions
- **Venmo not testable in sandbox** — must test live
- **Account shipping settings ignored** — bulk shipping profile doesn't apply
- **PDT + IPN + webhooks** all supported

## Payment Links vs Invoicing

Key differences:

- **Payment Links**: reusable, anyone with the link, one-time only, customer can set amount, no partial payments, no ACH
- **Invoicing**: specific customer, one per transaction, partial payments, reminders/tracking, ACH supported

Both support: hosted payment page, discounts, taxes, PCI compliance, Dashboard or API integration.

## Key Players

- [[paypal]] — Payment Links and Buttons product owner
- See also [[stripe-payment-links]] — Stripe's equivalent product

## Sources

- [[source-paypal-payment-links-overview]] — 4-option comparison, Payment Links vs Invoicing table
- [[source-paypal-invoicing-overview]] — Invoicing detailed docs
- [[source-github-postman-collections]] — exact-commit Payment Resources API request examples
- [[source-github-paypal-android-sdk-demo-app]] — Android Custom Tab and App Link reference flow with settlement-verification boundary
