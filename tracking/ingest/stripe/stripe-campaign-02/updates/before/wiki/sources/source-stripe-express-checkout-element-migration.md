---
title: "Migrate to the Express Checkout Element"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-express-checkout-element-migration-2025.md"
tags: [stripe, elements, express-checkout, payment-request-button, migration, apple-pay, google-pay, paypal, payment-intents]
---

## Summary

Step-by-step migration guide from the **Payment Request Button Element** (PRB) to the **Express Checkout Element** (ECE) using the Payment Intents API. The migration simplifies the integration significantly — the `paymentRequest` object and `canMakePayment()` availability check are eliminated; ECE handles availability internally.

> **Prerequisite**: If your existing integration uses the Charges API with tokens, you must first migrate to the Payment Intents API before following this guide.

## What Changes

| Area | Payment Request Button | Express Checkout Element |
| --- | --- | --- |
| Elements init | `stripe.elements()` (no options) | `stripe.elements({ mode, amount, currency })` |
| Availability check | `paymentRequest.canMakePayment()` required | Not needed — ECE handles internally |
| Element creation | `stripe.paymentRequest({...})` + `elements.create('paymentRequestButton', { paymentRequest })` | `elements.create('expressCheckout', { emailRequired, ... })` |
| `setup_future_usage` | Passed at confirm time via `confirmCardPayment` | Moved to Elements instance options |
| Confirmation | `stripe.confirmCardPayment(clientSecret, { payment_method: ev.paymentMethod.id })` | `stripe.confirmPayment({ elements, clientSecret, confirmParams: { return_url } })` |
| Styling | `style.paymentRequestButton.type/theme/height` | `buttonType`, `buttonTheme`, `buttonHeight` + Appearance API `borderRadius` |
| React component | `PaymentRequestButtonElement` + `useStripe` + `paymentRequest` state + `useEffect` | `ExpressCheckoutElement` with `onConfirm` prop — no state management needed |

## Migration Steps

### 1. Update Elements Instance

```js
// Before
const elements = stripe.elements();

// After
const elements = stripe.elements({ mode: 'payment', amount: 1099, currency: 'usd' });
```

### 2. Update PaymentIntent Creation (Server)

```js
const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  automatic_payment_methods: { enabled: true }, // now the API default
});
```

### 3. Replace Element Creation

```js
// Before: complex setup with paymentRequest object
const paymentRequest = stripe.paymentRequest({ country, currency, total, requestPayerName, requestPayerEmail });
const prb = elements.create('paymentRequestButton', { paymentRequest });
paymentRequest.canMakePayment().then(result => { if (result) prb.mount('#...'); });

// After: simple
const ece = elements.create('expressCheckout', { emailRequired: true });
ece.mount('#express-checkout-element');
```

### 4. Replace Confirmation

```js
// Before
paymentRequest.on('paymentmethod', function(ev) {
  stripe.confirmCardPayment(clientSecret, { payment_method: ev.paymentMethod.id }, { handleActions: false })
    .then(/* manual requires_action handling */);
});

// After
ece.on('confirm', async (event) => {
  const { error } = await stripe.confirmPayment({
    elements,
    clientSecret,
    confirmParams: { return_url: 'https://example.com/order/complete' },
  });
});
```

`stripe.confirmPayment` uses the Elements instance (not a PaymentMethod ID) and automatically handles 3DS/redirects.

### 5. Update Styling

```js
// Before
elements.create('paymentRequestButton', {
  paymentRequest,
  style: { paymentRequestButton: { type: 'book', theme: 'dark', height: '55px' } }
});

// After
const elements = stripe.elements({ mode: 'payment', amount: 1099, currency: 'usd',
  appearance: { variables: { borderRadius: '4px' } }
});
elements.create('expressCheckout', {
  buttonType: { googlePay: 'book', applePay: 'book', paypal: 'buynow' },
  buttonTheme: { applePay: 'black' },
  buttonHeight: 55
});
```

### 6. Optional: Apple Pay Merchant Tokens (MPAN)

ECE supports merchant tokens (MPANs) — recommended over device tokens for MIT (recurring, deferred, auto-reload). Works across devices and survives device loss/theft.

## Webhook Events to Handle

| Event | Description | Action |
| --- | --- | --- |
| `payment_intent.succeeded` | Payment completed | Send order confirmation, fulfill |
| `payment_intent.processing` | Payment initiated but pending (bank debit) | Send pending confirmation; fulfill digital goods early if appropriate |
| `payment_intent.payment_failed` | Payment failed | Offer customer another payment attempt |

Always listen server-side — don't rely on client callbacks (customer may close browser).

## Related Pages

- [[stripe-express-checkout-element]] — concept page
- [[source-stripe-express-checkout-element]] — ECE overview/reference
- [[source-stripe-express-checkout-element-accept-payment]] — full integration guide

## Raw Sources

- [[stripe-express-checkout-element-migration-2025]] — verbatim migration guide
