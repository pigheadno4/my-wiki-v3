---
title: "Accept a Payment with the Express Checkout Element"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-express-checkout-element-accept-payment-2025.md"
tags: [stripe, elements, express-checkout, apple-pay, google-pay, paypal, link, klarna, amazon-pay, checkout-sessions, payment-intents, integration-guide, connect]
---

## Summary

Full integration guide for the Express Checkout Element covering two API paths: **Checkout Sessions API** (recommended) and **Payment Intents API**. Both paths support the same six wallet methods and share the same ECE component, but differ significantly in how the payment is initialized and confirmed.

## Payment Method Type Mappings

Both API paths require specific `payment_method_types` values:

| Payment Method | Type(s) Required |
| --- | --- |
| Apple Pay | `card` |
| Google Pay | `card` |
| Link | `link` + `card` |
| PayPal | `paypal` |
| Amazon Pay | `amazon_pay` |
| Klarna | `klarna` (Payment Intents only) |

`card` automatically enables both Apple Pay and Google Pay. Klarna is only listed in the Payment Intents supported methods table — not in the Checkout Sessions table.

## Checkout Sessions API Integration

### Server

```js
const session = await stripe.checkout.sessions.create({
  line_items: [{ price: 'PRICE_ID', quantity: 1 }],
  mode: 'payment',
  ui_mode: 'elements',        // key: enables Elements mode
  return_url: 'RETURN_URL',
});
// session.client_secret → send to client
```

Optional session params: `phone_number_collection`, `shipping_address_collection`, `shipping_options`, `automatic_tax`.

### Client (HTML+JS)

```js
const checkout = stripe.initCheckoutElementsSdk({ clientSecret });
const expressCheckoutElement = checkout.createExpressCheckoutElement();
expressCheckoutElement.mount('#express-checkout-element');

// Confirm
const { actions } = await checkout.loadActions();
expressCheckoutElement.on('confirm', (event) => {
  actions.confirm({ expressCheckoutConfirmEvent: event });
});
```

### Client (React)

```jsx
import { CheckoutElementsProvider } from '@stripe/react-stripe-js/checkout';
// Wrap app with CheckoutElementsProvider (clientSecret + stripe instance)
// Use useCheckout() hook; call checkout.confirm({ expressCheckoutConfirmEvent: event })
// <ExpressCheckoutElement onConfirm={handleConfirm} />
```

## Payment Intents API Integration

### Client Setup

```js
const elements = stripe.elements({ mode: 'payment', amount: 1099, currency: 'usd' });
const expressCheckoutElement = elements.create('expressCheckout');
expressCheckoutElement.mount('#express-checkout-element');
```

### Confirm

```js
expressCheckoutElement.on('confirm', async (event) => {
  const { error } = await stripe.confirmPayment({
    elements,
    confirmParams: { return_url: 'https://example.com/order/123/complete' },
  });
});
```

### Elements Options (Payment Intents path)

| Option | Type | Notes |
| --- | --- | --- |
| `mode` | `payment` \| `setup` \| `subscription` | Required |
| `currency` | string | Required |
| `amount` | number | Required for payment/subscription |
| `setupFutureUsage` | `off_session` \| `on_session` | Not supported for Klarna |
| `captureMethod` | `automatic` \| `automatic_async` \| `manual` | — |
| `onBehalfOf` | string | Connect only |
| `paymentMethodTypes` | string[] | Omit to use Dashboard settings |
| `paymentMethodCreation` | `manual` | Creates PM from Elements instance |
| `paymentMethodOptions` | object | US bank verification, card installments, per-PM `setup_future_usage` |

Must match equivalent params on the PaymentIntent during confirmation — mismatches cause errors.

## Customer Detail Collection (Payment Intents Path)

### Payer Info

```js
elements.create('expressCheckout', {
  emailRequired: true,
  phoneNumberRequired: true,
});
```

`billingAddressRequired` defaults to `true` unless `allowedShippingCountries`, `phoneNumberRequired`, `shippingAddressRequired`, `emailRequired`, `applePay`, `lineItems`, or `business` are passed — then defaults to `false`.

**PayPal limitation**: normally doesn't provide billing address (except country) or phone. If required and unavailable, the PayPal button is hidden.

### Shipping

```js
elements.create('expressCheckout', {
  shippingAddressRequired: true,
  allowedShippingCountries: ['US'],
  shippingRates: [{ id: 'free-shipping', displayName: 'Free shipping', amount: 0, deliveryEstimate: {...} }],
});
```

> Browsers may anonymize the shipping address (city/state/postal only) before confirmation. Full address appears in the `confirm` event after purchase is confirmed.

### Events

| Event | When | Response required |
| --- | --- | --- |
| `shippingaddresschange` | Customer selects a shipping address | `resolve({lineItems})` or `reject()` |
| `shippingratechange` | Customer selects a shipping rate | `resolve({lineItems})` + `elements.update({amount})` or `reject()` |
| `cancel` | Customer dismisses payment UI | Reset amount: `elements.update({amount: originalAmount})` |
| `confirm` | Customer confirms payment | Call `stripe.confirmPayment(...)` |
| `ready` | Element determines available methods | Show/hide fallback UI |
| `click` | Customer clicks a button | Can request Apple Pay merchant tokens (MIT) |

### Line Items Display

```js
elements.create('expressCheckout', {
  lineItems: [
    { name: 'Sample item', amount: 1000 },
    { name: 'Tax', amount: 100 },
    { name: 'Shipping cost', amount: 1000 },
  ]
});
```

## Apple Pay Merchant Tokens (MIT)

For recurring, deferred, or auto-reload payments via Apple Pay, request the relevant merchant token type in the `click` event. Aligns with Apple Pay's latest guidelines.

## Testing

### Link

OTP values accepted in sandbox:

| Value | Outcome |
| --- | --- |
| Any 6 digits except below | Success |
| 000001 | Error — code invalid |
| 000002 | Error — code expired |
| 000003 | Error — max attempts exceeded |

### Apple Pay / Google Pay
Use test API keys — Stripe intercepts and returns a successful test card token. Live card is not charged. Google Pay also supports its own [test card suite](https://developers.google.com/pay/api/web/guides/resources/test-card-suite).

### PayPal
Create a sandbox account at developer.paypal.com (must be in sandbox mode). Cannot use a personal PayPal account in sandbox.

### Amazon Pay

| Card | Outcome |
| --- | --- |
| Discover ending 9424 | Success |
| Visa ending 1111 | Success |
| Visa ending 0701 | 3D Secure |
| Amex ending 0005 | Decline |
| JCB ending 0000 | Decline |

## Connect Integration

**Checkout Sessions path**: pass `Stripe-Account: CONNECTED_ACCOUNT_ID` header when creating the session.

**Payment Intents path**: pass `stripeAccount` option on the Stripe instance before creating Elements:
```js
const stripe = Stripe('PK', { stripeAccount: 'CONNECTED_ACCOUNT_ID' });
```

Both paths require registering all domains where the ECE will appear.

## Privacy Disclosure Requirement

Stripe collects interaction data (cookies, IP) to prevent fraud. Merchants must disclose this and obtain customer consent per Stripe's privacy center requirements.

## Related Pages

- [[stripe-express-checkout-element]] — concept page
- [[source-stripe-express-checkout-element]] — overview/reference source
- [[stripe-elements]] — parent Elements framework
- [[stripe]] — company page

## Raw Sources

- [[stripe-express-checkout-element-accept-payment-2025]] — verbatim integration guide (Checkout Sessions + Payment Intents paths)
