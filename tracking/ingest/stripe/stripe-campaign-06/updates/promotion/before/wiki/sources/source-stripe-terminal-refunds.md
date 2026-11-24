---
title: "Stripe Terminal: Refund Transactions"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-refunds-2025.md"
tags: [stripe, stripe-terminal, refunds, cancellations, interac, payment-intents]
---

## Summary

Guide for canceling pre-capture Terminal PaymentIntents and refunding captured payments. Covers availability by card network, client-side vs server-side cancellation, and online vs in-person refunds.

## Key Takeaways

### Canceling payments (pre-capture)

- Available on Visa, Mastercard, Amex, Discover, girocard
- **Interac/eftpos**: auto-capture — cannot cancel; must initiate a refund at end of checkout instead
- Client-side cancellation via `cancelPaymentIntent`: iOS, Android, React Native SDKs
- Server-side cancellation required for: JavaScript SDK and server-driven integrations (use `stripe.paymentIntents.cancel('pi_...')`)
- Canceling releases all uncaptured funds; the PaymentIntent can no longer be used to charge

### Refunds (post-capture)

- **Online refunds**: available on all card networks except Interac; no card re-presentment required
- **In-person refunds**: Interac only (mandatory — cannot refund Interac via API or Dashboard); available on WisePad 3, WisePOS E, S700/S710, Tap to Pay iPhone, Tap to Pay Android
- Refund by passing PaymentIntent ID or charge ID to the refunds API
- Partial refunds: add `amount` param (integer in cents)
- Recommend daily payment reconciliation to catch unintended authorizations

## API Examples

```javascript
// Full refund
const refund = await stripe.refunds.create({
  payment_intent: 'pi_Aabcxyz01aDfoo',
});

// Partial refund
const refund = await stripe.refunds.create({
  payment_intent: 'pi_Aabcxyz01aDfoo',
  amount: 1000,
});
```

## See Also

- [[stripe-terminal-refunds]] — concept page
- [[source-stripe-terminal-regional]] — Interac in-person refund details (Canada)

## Raw Sources

- [[stripe-terminal-refunds-2025]] — verbatim webpage content
