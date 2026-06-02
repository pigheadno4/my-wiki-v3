---
title: "Stripe Terminal: Refunds and Cancellations"
type: concept
category: technology
tags: [stripe, stripe-terminal, refunds, cancellations, interac, payment-intents]
---

## Definition

Stripe Terminal supports two post-payment reversal flows: canceling pre-capture PaymentIntents (releases the hold) and refunding captured charges (returns funds to the cardholder). The right approach depends on whether the PaymentIntent has been captured.

## Canceling Payments (Pre-Capture)

**When to use**: PaymentIntent is confirmed but not yet captured.

**Available on**: Visa, Mastercard, Amex, Discover, girocard.

**Not available on Interac/eftpos**: these use automatic capture — the PaymentIntent is captured immediately at confirmation, so cancellation is not possible. Instead, ensure your app can initiate a refund at the end of the checkout flow.

**How to cancel**:
- **Client-side** (iOS/Android/React Native SDKs): `cancelPaymentIntent`
- **Server-side** (required for JS SDK and server-driven; optional for other SDKs):
  ```javascript
  await stripe.paymentIntents.cancel('pi_ANipwO3zNfjeWODtRPIg');
  ```

Canceling releases all uncaptured funds; the PaymentIntent cannot be used again.

**UX note**: allow customers to cancel after payment confirmation, but before your backend captures — this is the ideal window.

## Performing Refunds (Post-Capture)

**When to use**: PaymentIntent has already been captured (succeeded).

**Online refunds**: available on all card networks **except Interac** — no card re-presentment needed.

**Interac in-person refunds**: mandatory for Interac transactions (cannot refund Interac via API or Dashboard). Available on WisePad 3, WisePOS E, S700/S710, Tap to Pay iPhone, Tap to Pay Android.

**Full refund**:
```javascript
const refund = await stripe.refunds.create({
  payment_intent: 'pi_Aabcxyz01aDfoo',
});
```

**Partial refund** (add `amount` in cents):
```javascript
const refund = await stripe.refunds.create({
  payment_intent: 'pi_Aabcxyz01aDfoo',
  amount: 1000,
});
```

Refunds can also be initiated through the Stripe Dashboard.

## Reconciliation

Stripe recommends reconciling payments daily on your backend to catch unintended authorizations and uncollected funds.

## Sources

- [[source-stripe-terminal-refunds]] — primary source: availability, cancel flows, refund API
- [[source-stripe-terminal-regional]] — Interac in-person refund details (Canada)
