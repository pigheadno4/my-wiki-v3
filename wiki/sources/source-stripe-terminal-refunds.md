---
title: "Stripe Terminal: Refund Transactions"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/features/refunds"
raw_files:
  - "stripe-terminal-refunds-2025.md"
tags: [stripe, stripe-terminal, refunds, cancellations, interac, payment-intents]
---

## Summary

The May 1, 2026 guide covers cancellation of uncaptured [[stripe-terminal|Stripe Terminal]] PaymentIntents and refunds of captured payments, with card-network and client/server distinctions. The November 7, 2026 index routes to server-driven, JavaScript, iOS, Android and React Native variants.

## Key Takeaways

### Canceling payments (pre-capture)

- Available on Visa, Mastercard, Amex, Discover, girocard
- **Interac/eftpos**: The May guide describes automatic capture when the payment is routed as a single-message Interac or eftpos transaction. For a captured payment, initiate a refund. Check the actual capture state before choosing a flow.
- Client-side cancellation via `cancelPaymentIntent`: iOS, Android, React Native SDKs
- JavaScript SDK and server-driven integrations cancel on the server (see `stripe.paymentIntents.cancel('pi_...')`). The other client SDKs can use server-side cancellation when the necessary information is unavailable in the app.
- Canceling releases all uncaptured funds; the PaymentIntent can no longer be used to charge

### Refunds (post-capture)

- **Online refunds**: available on all card networks except Interac; no card re-presentment required
- **In-person refunds**: Mandatory for Interac in Canada. The May guide lists WisePad 3, WisePOS E, S700/S710, and Tap to Pay on iPhone and Android.
- In the ordinary server-side refund flow, pass a PaymentIntent ID or Charge ID to the Refunds API to refund the underlying Charge.
- For a partial refund, pass an integer `amount` in the charge currency’s smallest unit.
- The May guide recommends daily backend reconciliation for unintended authorizations and uncollected funds.

> [!note] April 24 and May 1, 2026 Interac refund routes
> Ordinary online refunds through the Refunds API or Dashboard exclude Interac. The separate [[source-stripe-terminal-regional|April 24 regional guide]] documents the server-driven in-person Terminal reader `refund_payment` endpoint. The reader prompts for the original card, and the refund currency must match the original charge.

The May guide’s confirmed-Intent example describes a pre-capture window. Inspect the Intent’s actual capture state before choosing cancellation or refund. See [[stripe-terminal-refunds]] for the separately sourced iOS and Android SDK 6.0.0 conditions.

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

- [[raw/stripe-terminal-refunds-2025|May 1, 2026 full Terminal refunds and cancellation guide]]

## Related raw API references

- [[raw/stripe-terminal-features-refunds-2026-11-07|November 7, 2026 Terminal refunds index for server-driven, JavaScript, iOS, Android and React Native]]
