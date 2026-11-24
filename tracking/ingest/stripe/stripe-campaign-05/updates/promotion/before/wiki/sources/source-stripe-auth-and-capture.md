---
title: "Place a Hold on a Payment Method"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-auth-and-capture-2025.md"
tags: [stripe, auth-capture, capture-method, manual-capture, payment-intents, checkout-sessions, authorization-window, automatic-delayed]
---

## Summary

Comprehensive auth+capture reference. Covers authorization validity windows per card brand, per-PM capture rules, API setup for both CS and PI paths, partial capture, and the `automatic_delayed` private preview feature.

## Authorization Validity Windows

### Card-Not-Present (Online)

| Card brand | CIT | MIT |
| --- | --- | --- |
| Visa | 7 days | 5 days (4d 18h — shortened April 14, 2024) |
| Mastercard | 7 days | 7 days |
| Amex | 7 days | 7 days |
| Discover | 7 days | 7 days |

> MIT vs CIT classification is based on signals of cardholder participation, NOT solely on the `off_session` API param. A payment with `off_session: true` may still be CIT if CVC is present.

### Card-Present (Terminal)

| Card brand | Window |
| --- | --- |
| Visa | 5 days (4d 18h) |
| Mastercard/Amex/Discover | 2 days |

### Japan (JPY) — 30-Day Window

JPY transactions on Visa, MC, JCB, Diners, Discover: **30 days**. Non-JPY and Amex: standard 7 days.

## Per-PM Capture Windows (Beyond Cards)

| Payment Method | Capture window | Notes |
| --- | --- | --- |
| Affirm | 30 days | Charges down payment during auth; refunds if uncaptured |
| Afterpay / Clearpay | 13 days | Charges first installment during auth; refunds if uncaptured |
| Cash App Pay | 7 days | — |
| Klarna | 28 calendar days | Must capture by midnight of 28th day after charge request |
| PayPal | 10 days (Stripe auto-extends to 20) | Settlement preference may affect window |

Payment methods that **don't** support auth+capture: ACH, iDEAL.

## API Setup

### Checkout Sessions

```js
stripe.checkout.sessions.create({
  payment_intent_data: { capture_method: 'manual' },
});
```

### Payment Intents — Global

```js
stripe.paymentIntents.create({
  capture_method: 'manual',  // applies to all PMs — only eligible PMs shown
});
```

### Payment Intents — Per-PM (Recommended)

```js
// Cards on hold; SEPA Debit can still be accepted
stripe.paymentIntents.create({
  automatic_payment_methods: { enabled: true },
  payment_method_options: { card: { capture_method: 'manual' } },
});
```

PI status after successful auth: **`requires_capture`**

## Capture

```js
stripe.paymentIntents.capture('pi_...', {
  amount_to_capture: 750,  // partial capture (releases remainder)
});
```

- Partial capture releases the uncaptured remainder automatically
- **Only one capture** for most payments — partial capture is final
- CS: use the PaymentIntent ID from the Checkout Session object

## Cancel Authorization

```js
stripe.paymentIntents.cancel('pi_...');
```

## `automatic_delayed` (Private Preview)

Stripe auto-captures ~6h before authorization expiry as a safety net:

```js
payment_method_options: {
  card: {
    capture_method: 'automatic_delayed',
    capture_delay_days: 3,  // optional custom delay
  },
}
```

- Still allows manual capture/cancel before auto-capture fires
- If authorization window < `capture_delay_days`: captures before expiry, ignoring the delay

## Related Pages

- [[stripe-payment-intents]] — concept page (includes requires_capture status)
- [[stripe-checkout]] — Checkout concept page
- [[source-stripe-payment-intents]] — PI lifecycle + statuses

## Raw Sources

- [[stripe-auth-and-capture-2025]] — verbatim auth+capture guide (248 lines)
