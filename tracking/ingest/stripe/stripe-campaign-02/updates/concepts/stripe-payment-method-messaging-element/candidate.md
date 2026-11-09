---
title: "Stripe Payment Method Messaging Element"
type: concept
category: technology
tags: [stripe, elements, bnpl, buy-now-pay-later, payment-method-messaging, klarna, affirm, afterpay, clearpay]
---

## Definition

The Payment Method Messaging Element is a Stripe UI component that displays promotional buy now, pay later (BNPL) messaging on product, cart, and payment pages. It automatically determines which BNPL plans a customer is eligible for based on amount, currency, and location — and renders nothing if no eligible plans are available.

## Key Distinction

The captured web example creates this Element with `stripe.elements()` and no `clientSecret`, and places it on product, cart, and payment pages. That example does not establish a universal PaymentIntent or API validation rule. See [[source-stripe-payment-method-messaging-element]] for the dated example and its scope.

```js
const elements = stripe.elements(); // no clientSecret needed
elements.create('paymentMethodMessaging', { amount: 9900, currency: 'USD', countryCode: 'US' })
        .mount('#payment-method-messaging-element');
```

## Supported BNPL Providers

| Provider | Notes |
| --- | --- |
| Affirm | Listed as a supported plan provider; availability depends on customer eligibility. |
| Afterpay / Clearpay | Listed as a supported plan provider; availability depends on customer eligibility. |
| Klarna | Listed for one-time payments only; availability depends on customer eligibility. |

Nothing renders if only "pay now" options are eligible for the given amount/currency/country.

## Dynamic vs Manual Payment Methods

- **When using Dynamic payment methods**: the Element pulls payment method preferences from the Stripe Dashboard and shows eligible plans.
- **Manual selection**: `paymentMethodTypes: ['klarna', 'afterpay_clearpay', 'affirm']` is an alternative; customer eligibility still filters displayed plans.
- **Display order**: the Element uses dynamic ordering by default; `paymentMethodOrder` sets a preferred order. See [[source-stripe-payment-method-messaging-element]].

## Info Modal

Clicking the built-in ⓘ icon opens a modal showing:
- Step-by-step overview of how BNPL works
- Summary of terms per available plan
- Link to full terms per plan

![BNPL info modal](../raw/assets/stripe-payment-method-messaging-element-info-modal.png)

## Options

| Option | Captured role |
| --- | --- |
| `amount` | Shown in both examples in the smallest currency unit; explicit requiredness is not established by these captures. |
| `currency` | Shown in both examples as a currency code; explicit requiredness is not established by these captures. |
| `countryCode` | Marked optional in examples; buyer country affects eligibility. |
| `paymentMethodTypes` | Manual payment method selection; eligibility still applies. |
| `paymentMethodOrder` | Sets a preferred display order in place of default dynamic ordering. |

See [[source-stripe-payment-method-messaging-element]] for the captured examples; the linked option reference was not assessed here.

## Connect

Direct charge Connect platforms must set `stripeAccount` on the Stripe instance before creating the element.

## Appearance

Uses Appearance API. `.PaymentMethodMessaging` CSS rule controls layout (e.g., `textAlign`). Variables control color, font size, font family, and spacing.

## React Native 0.82.0 Android Font Fix

The `@stripe/stripe-react-native@0.82.0` release announces the underscore-name validation fix for PaymentSheet and PaymentMethodMessagingElement. The shared retained validator now allows alphanumeric characters and underscores, then resolves the named resource from `android/app/src/main/res/font`; unknown resources still fail. The Messaging font contract documents that filename, while iOS continues to use a PostScript font name. This is not a change to web Elements CSS, BNPL eligibility or a device-tested guarantee. See [[source-github-stripe-react-native]] and [[changelog-github-stripe-react-native]].

## Legal Notes

Merchants are responsible for compliance with applicable laws, rules, and regulations regarding the promotion of BNPL payment options. Stripe also requires disclosure of its data collection practices to customers.

## Key Players

- [[stripe]] — the sole provider of this element

## Sources

- [[source-github-stripe-react-native]] - 0.82.0 Android font validation contract/fix announcement; separate from web Elements
- [[source-stripe-payment-method-messaging-element]] — primary reference: initialization, supported plans, info modal, Connect, Appearance API
- [[source-stripe-inapp-payment-method-messaging-element]] — mobile overview: iOS + Android, auto-determines BNPL plans, localized messaging
- [[source-stripe-inapp-display-bnpl-messaging]] — mobile integration guide (beta): iOS UIKit/SwiftUI + Android, configuration/appearance options, Android requires separate `payment-method-messaging` dependency
