---
title: "Stripe — Review Uncaptured Payments (Auth and Capture)"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-reviews-auth-capture-2026.md"
tags: [stripe, radar, reviews, auth-and-capture, payment-intent, webhooks]
---

## Summary

Integration guide for using Radar reviews with auth-and-capture payment flows. Approve and capture are separate actions; use `review.closed` webhook to auto-capture approved payments.

## Key Rule

**Approving a review ≠ capturing the payment.** You must explicitly capture after approving.

## Dashboard Behavior

- Uncaptured payments in review: show **Capture** + **Cancel** buttons (not Refund)
- Cancel releases the authorization without creating a Refund object

## API Integration Pattern

1. Create PaymentIntent with `capture_method: 'manual'`
2. If `paymentIntent.review` is empty → capture immediately
3. If `paymentIntent.review` is set → leave uncaptured; wait for review
4. Listen for `review.closed` webhook
5. If `review.reason === 'approved'` → `stripe.paymentIntents.capture(pi.id)`

```js
// Step 2: capture if not in review
if (!paymentIntent.review) {
  await stripe.paymentIntents.capture(paymentIntent.id);
}

// Step 4-5: webhook handler
if (event.type === 'review.closed' && review.reason === 'approved') {
  await stripe.paymentIntents.capture(review.payment_intent);
}
```

## Related Pages

- [[stripe-radar]] — concept page
- [[source-stripe-radar-reviews]] — review queue overview

## Raw Sources

- [[stripe-radar-reviews-auth-capture-2026]] — verbatim auth-and-capture review guide (1 screenshot)
