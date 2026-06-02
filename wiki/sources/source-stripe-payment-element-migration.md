---
title: "Stripe: Migrate to the Payment Element (Payment Intents API)"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-payment-element-migration-2025.md"
  - "stripe-confirmation-tokens-migration-2025.md"
tags: [stripe, payment-element, card-element, migration, payment-intents, setup-intents, elements, confirmPayment, elements-submit, confirmation-tokens]
---

## Summary

Migration guide from Card Element to Payment Element using the Payment Intents API. Covers both PaymentIntent (one-time) and SetupIntent (future payments) paths. Key changes: Elements options now required, `elements.submit()` before confirm, new confirm methods.

## Key Takeaways

- **LLM instruction**: Use Checkout Sessions API over Payment Intents for most integrations; migrate to Payment Element with Checkout Sessions if you need subscriptions, tax, discounts, shipping, or currency conversion
- **Two migration paths**: PaymentIntent (one-time payments) + SetupIntent (future payments)
- **3 main code changes**: (1) add options to `stripe.elements()`, (2) replace CardElement with PaymentElement, (3) replace confirm method
- **New required step**: `await elements.submit()` before confirm — validates form + collects wallet data
- **Unsupported**: BLIK, ACSS; `customer_balance` needs server-side intent creation

## PaymentIntent Migration Steps

### 1. Update Elements instance

```javascript
// Before
const elements = stripe.elements();

// After
const elements = stripe.elements({
  mode: 'payment',
  currency: 'usd',
  amount: 1099,
  setup_future_usage: 'off_session',  // optional
});
```

### 2. Replace CardElement with PaymentElement

```jsx
// Before: <CardElement />
// After:
<PaymentElement />
```

### 3. Update submit handler

```javascript
// Before: stripe.confirmCardPayment(clientSecret, {...})

// After:
const { error: submitError } = await elements.submit();  // NEW — required first
if (submitError) { handleError(submitError); return; }

const { client_secret: clientSecret } = await fetch('/create-intent', ...).then(r => r.json());

const { error } = await stripe.confirmPayment({
  elements,
  clientSecret,
  confirmParams: { return_url: 'https://example.com/complete' },
  // redirect: 'if_required'  // optional: only redirect for redirect-based PMs
});
```

### 4. Update PaymentIntent creation

```javascript
stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  automatic_payment_methods: { enabled: true },
})
```

## SetupIntent Migration Steps

Same pattern but:
- `mode: 'setup'` (no `amount` needed)
- `stripe.confirmSetup()` instead of `stripe.confirmPayment()`
- `stripe.confirmCardSetup()` → `stripe.confirmSetup()`

## 11 Elements Options

| Option | Required | Notes |
| --- | --- | --- |
| `mode` | Yes | `payment` / `setup` / `subscription` |
| `currency` | Yes | Currency string |
| `amount` | For payment/subscription | Shown in Apple Pay, Google Pay, BNPL UIs |
| `setupFutureUsage` | No | `off_session` or `on_session` |
| `captureMethod` | No | `automatic` / `automatic_async` / `manual` |
| `onBehalfOf` | No | Connect only |
| `paymentMethodTypes` | No | Omit to use Dashboard-managed PMs |
| `paymentMethodConfiguration` | No | Specific PM configuration ID |
| `paymentMethodCreation` | No | `manual` — enables `stripe.createPaymentMethod` from Elements |
| `paymentMethodOptions.us_bank_account` | No | Verification method |
| `paymentMethodOptions.card.installments` | No | Card installment UI (requires explicit `paymentMethodTypes`) |

> **Important**: Elements options must match PaymentIntent params exactly — mismatches cause errors.

## CVC Recollection

For subsequent charges requiring CVC verification:

```javascript
// Use cardCvc Element + confirmCardPayment (not confirmPayment)
await stripe.confirmCardPayment(clientSecret, {
  payment_method: 'pm_...',
  payment_method_options: { card: { cvc: cardCvcElement } }
});
```

Configure Radar rules to block payments when CVC verification fails.

## Webhook Events

| Event | Action |
| --- | --- |
| `payment_intent.succeeded` | Fulfill order |
| `payment_intent.processing` | Send "pending" confirmation; fulfill digital goods |
| `payment_intent.payment_failed` | Offer customer another attempt |

## ConfirmationToken Migration

`ConfirmationToken` is a superset of `PaymentMethod` — includes `shipping`, `mandate_data`, `return_url`, and enables future Stripe features.

**Client change**:

```javascript
// Before: stripe.createPaymentMethod({ elements })
// After:
const { error, confirmationToken } = await stripe.createConfirmationToken({
  elements,
  params: {
    payment_method_data: { billing_details: { name: '...' } },
    shipping: { name: '...', address: {...} },
    return_url: 'https://example.com/complete',
  }
});
// → send confirmationToken.id to server
```

**Server change**: pass `confirmation_token: req.body.confirmationTokenId` to `paymentIntents.create()` instead of `payment_method`.

**Conditional `setup_future_usage`/`capture_method`**: don't set at Elements level or PI top-level — use `payment_method_options.{method}.setup_future_usage` per payment method.

## Related Pages

- [[stripe-elements]] — Stripe Elements concept page
- [[source-stripe-payment-element-vs-card-element]] — Card Element vs Payment Element comparison
- [[source-stripe-payment-intents-quickstart]] — Payment Intents quickstart

## Raw Sources

- [[stripe-payment-element-migration-2025]] — Full migration: PaymentIntent + SetupIntent paths, 11 Elements options, submit handler pattern, CVC recollection, comprehensive test tables
- [[stripe-confirmation-tokens-migration-2025]] — ConfirmationToken migration: createConfirmationToken vs createPaymentMethod, confirmation_token param on PaymentIntent, per-PM setup_future_usage pattern
