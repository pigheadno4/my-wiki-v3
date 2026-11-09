---
title: "Stripe Payment Method Messaging Element"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-payment-method-messaging-element-2025.md"
tags: [stripe, elements, bnpl, buy-now-pay-later, payment-method-messaging, klarna, affirm, afterpay, clearpay, connect]
---

## Summary

The Payment Method Messaging Element is a Stripe UI component for displaying BNPL (buy now, pay later) promotional messaging on product, cart, and payment pages. It automatically determines eligible plans based on amount, currency, and customer location — and renders nothing if no plans are available.

## Key Takeaways

- **No `clientSecret` required** — initialized with `stripe.elements()` only (no PaymentIntent needed)
- **Placement**: product pages, cart pages, and payment pages — not just checkout
- **Dynamic by default**: pulls BNPL preferences from Dashboard; falls back to hiding if only "pay now" is available
- **3 supported BNPL providers**: Affirm, Afterpay/Clearpay, Klarna (one-time payments only)
- **Info modal**: ⓘ icon opens a modal with BNPL plan terms and full terms links
- **Legal**: merchants responsible for BNPL promotion regulatory compliance

## Initialization

```js
const stripe = Stripe('<<YOUR_PUBLISHABLE_KEY>>');
const elements = stripe.elements();
const options = {
  amount: 9900,       // in cents — 99.00 USD
  currency: 'USD',
  countryCode: 'US',  // optional: buyer's country
};
elements.create('paymentMethodMessaging', options).mount('#payment-method-messaging-element');
```

React: `<PaymentMethodMessagingElement options={{...}} />` from `@stripe/react-stripe-js` inside `<Elements>`.

## Options

| Option | Required | Description |
| --- | --- | --- |
| `amount` | Yes | Amount in smallest currency unit (cents) |
| `currency` | Yes | Currency code (e.g. `'USD'`) |
| `countryCode` | No | Buyer's country — affects eligible plans |
| `paymentMethodTypes` | No | Manual override; default pulls from Dashboard |
| `paymentMethodOrder` | No | Override dynamic ordering |

## Supported BNPL Plans

| Provider | Notes |
| --- | --- |
| Affirm | Full plan options |
| Afterpay / Clearpay | Full plan options |
| Klarna | One-time payments only |

Nothing renders if only "pay now" options are available for the amount/currency/country combination.

## Info Modal

Clicking the ⓘ icon opens a modal showing:
- Step-by-step overview of how BNPL works
- Summary of terms per available plan
- Link to full terms per plan

![Payment Method Messaging Element info modal](../raw/assets/stripe-payment-method-messaging-element-info-modal.png)

## Connect

Direct charge Connect platforms must set `stripeAccount` on the Stripe instance before creating the element:

```js
const stripe = Stripe('<<YOUR_PUBLISHABLE_KEY>>', { stripeAccount: 'CONNECTED_ACCOUNT_ID' });
```

## Appearance

Uses Appearance API. Key customization surface: `.PaymentMethodMessaging` CSS rule for layout; variables for color/font/spacing.

```js
const appearance = {
  variables: { colorText: 'rgb(84,51,255)', fontSizeBase: '16px', fontFamily: 'Ideal Sans, system-ui, sans-serif' },
  rules: { '.PaymentMethodMessaging': { textAlign: 'right' } }
};
```

## Related Pages

- [[stripe-payment-method-messaging-element]] — concept page
- [[stripe-elements]] — parent Elements framework
- [[stripe]] — company page

## Raw Sources

- [[stripe-payment-method-messaging-element-2025]] — verbatim Stripe docs webpage
