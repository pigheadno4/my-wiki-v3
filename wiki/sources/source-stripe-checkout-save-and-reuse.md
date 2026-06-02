---
title: "Stripe Checkout: Set Up Future Payments"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-save-and-reuse-2025.md"
tags: [stripe, checkout, setup-mode, setup-intents, payment-methods, save-payment, off-session, recurring]
---

## Summary

Guide for using Checkout's setup mode to save payment details for future use. Covers the full flow from session creation through SetupIntent retrieval to off-session charging, for both hosted and embedded modes.

## Key Takeaways

- **Setup mode**: `mode: 'setup'` — saves payment method without charging; uses Setup Intents API
- **`currency` required** in setup mode (needed for Dynamic payment methods selection)
- **Optionally pass `customer`** to auto-attach the payment method to an existing customer
- **Full flow**: session create → customer completes → retrieve session → get `setup_intent` ID → retrieve SetupIntent → get `payment_method` → attach to Customer → charge later
- **Two retrieval methods**: async (`checkout.session.completed` webhook, recommended) or sync (session ID from `success_url`/`return_url`)
- **Expand tip**: expand SetupIntent in session retrieve call to avoid 2 API calls
- **Off-session charge**: `paymentIntents.create({ off_session: true, confirm: true })` — on 402 failure → redirect customer to new Checkout session

## Integration Flow

```
1. stripe.checkout.sessions.create({ mode: 'setup', currency: 'usd', customer: '...' })
2. Customer completes → checkout.session.completed event fires
3. Get setup_intent from session object
4. stripe.setupIntents.retrieve(setup_intent_id) → payment_method ID
   (or expand in step 3 to save one API call)
5. stripe.paymentMethods.attach(pm_id, { customer: cus_id })   ← if no customer in step 1
6. Later: stripe.paymentIntents.create({
     customer, payment_method, off_session: true, confirm: true
   })
7. On 402 failure: redirect customer to new Checkout session
```

## Checkout Session Payload (Setup Mode)

Key fields in `checkout.session.completed`:
- `mode: "setup"`
- `setup_intent: "seti_..."` — ID to retrieve the SetupIntent
- No `payment_intent` or `subscription`

## Related Pages

- [[stripe-checkout]] — Stripe Checkout concept page (3 modes: payment, subscription, setup)
- [[source-stripe-checkout-build-subscriptions]] — Subscription integration (for recurring charges after save)

## Raw Sources

- [[stripe-checkout-save-and-reuse-2025]] — Setup mode: session creation, webhook vs sync retrieval, SetupIntent retrieval, off-session charging, 402 failure handling, hosted + embedded variants
