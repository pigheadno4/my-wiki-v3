---
title: "Stripe Payment Method Messaging Element"
type: concept
category: technology
tags: [stripe, elements, bnpl, buy-now-pay-later, payment-method-messaging, klarna, affirm, afterpay, clearpay]
---

## Definition

The Payment Method Messaging Element is a Stripe UI component that displays promotional buy now, pay later (BNPL) messaging on product, cart, and payment pages. It automatically determines which BNPL plans a customer is eligible for based on amount, currency, and location — and renders nothing if no eligible plans are available.

## Key Distinction

Unlike other Elements, the Payment Method Messaging Element **does not require a `clientSecret`** or a PaymentIntent. It can be placed anywhere on the page — product listings, cart pages, and checkout — not just at the payment step.

```js
const elements = stripe.elements(); // no clientSecret needed
elements.create('paymentMethodMessaging', { amount: 9900, currency: 'USD', countryCode: 'US' })
        .mount('#payment-method-messaging-element');
```

## Supported BNPL Providers

| Provider | Notes |
| --- | --- |
| Affirm | Full plan options |
| Afterpay / Clearpay | Full plan options |
| Klarna | One-time payments only |

Nothing renders if only "pay now" options are eligible for the given amount/currency/country.

## Dynamic vs Manual Payment Methods

- **Default (dynamic)**: pulls BNPL preferences from Stripe Dashboard; automatically shows most relevant plans
- **Manual override**: pass `paymentMethodTypes: ['klarna', 'afterpay_clearpay', 'affirm']` to specify explicitly
- `paymentMethodOrder` option overrides the default dynamic ordering

## Info Modal

Clicking the built-in ⓘ icon opens a modal showing:
- Step-by-step overview of how BNPL works
- Summary of terms per available plan
- Link to full terms per plan

![BNPL info modal](../raw/assets/stripe-payment-method-messaging-element-info-modal.png)

## Options

| Option | Required | Description |
| --- | --- | --- |
| `amount` | Yes | Amount in smallest currency unit (e.g. cents) |
| `currency` | Yes | Currency code (e.g. `'USD'`) |
| `countryCode` | No | Buyer's country — affects plan eligibility |
| `paymentMethodTypes` | No | Manual list of BNPL providers to show |
| `paymentMethodOrder` | No | Override dynamic plan ordering |

## Connect

Direct charge Connect platforms must set `stripeAccount` on the Stripe instance before creating the element.

## Appearance

Uses Appearance API. `.PaymentMethodMessaging` CSS rule controls layout (e.g., `textAlign`). Variables control color, font size, font family, and spacing.

## Legal Notes

Merchants are responsible for compliance with applicable laws, rules, and regulations regarding the promotion of BNPL payment options. Stripe also requires disclosure of its data collection practices to customers.

## Key Players

- [[stripe]] — the sole provider of this element

## Sources

- [[source-stripe-payment-method-messaging-element]] — primary reference: initialization, supported plans, info modal, Connect, Appearance API
- [[source-stripe-inapp-payment-method-messaging-element]] — mobile overview: iOS + Android, auto-determines BNPL plans, localized messaging
- [[source-stripe-inapp-display-bnpl-messaging]] — mobile integration guide (beta): iOS UIKit/SwiftUI + Android, configuration/appearance options, Android requires separate `payment-method-messaging` dependency
