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

## iOS SDK 6.0.0 Boundaries

`StripeTerminal@6.0.0` defaults client-created PaymentIntents to automatic-async capture. A post-authorization/pre-capture cancellation window must not be assumed without an explicit manual-capture configuration and an eligible Intent state.

For in-person refunds, use `processRefund` with renamed `ProcessRefundParameters`/`ProcessRefundParametersBuilder`. The deprecated collect-then-confirm refund overloads are removed; their v5 history is preserved in [[source-github-stripe-terminal-ios]].

A separate **private-preview** `confirmRefund(parameters)` creates a full or partial refund without presenting a card or reader UI, but **still requires a connected reader to authenticate**. It takes the PaymentIntent ID and client secret; omitting amount refunds the entire remaining refundable amount. If it returns an error without a Refund, reconcile with the backend before creating another refund. This preview does not remove Interac's in-person requirement. `Refund.stripeId` is nullable, and `requiresAction`, `canceled` and `nextAction` must be handled rather than equating a returned object with completed reimbursement. See [[source-github-stripe-terminal-ios]] and [[changelog-github-stripe-terminal-ios]].

## Android SDK 6.0.0 Boundaries

For `stripeterminal@6.0.0`, use `ProcessRefundParameters` (including `ByChargeId`/`ByPaymentIntentId`) with `processRefund` for in-person collection. The deprecated split collect/confirm API is removed. The separate new private-preview `confirmRefund(parameters, callback)` does not collect a payment method; a successful callback may still return `requires_action`, so inspect `nextAction`. An error without an attached Refund can mean an unknown outcome: reconcile with the backend before creating another refund. Refund IDs are nullable, and Interac's in-person rule remains. Android's retained evidence here does not establish every preview parameter or the iOS-specific authentication contract.

Reader-originated `CANCELED_BY_READER` differs from SDK `CANCELED`; neither an operation-cancel callback nor the v6 automatic-async default proves a PaymentIntent is still cancelable before capture. Inspect its state. See [[source-github-stripe-terminal-android]] and [[changelog-github-stripe-terminal-android]].

## Reconciliation

Stripe recommends reconciling payments daily on your backend to catch unintended authorizations and uncollected funds.

## Sources

- [[source-stripe-terminal-refunds]] — primary source: availability, cancel flows, refund API
- [[source-stripe-terminal-regional]] — Interac in-person refund details (Canada)
