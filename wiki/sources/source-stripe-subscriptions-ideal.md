---
title: "Stripe Subscriptions — Set Up iDEAL + SEPA Direct Debit Subscription"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-ideal-2026.md"
tags: [stripe, billing, subscriptions, ideal, sepa-debit, eur, netherlands, checkout, payment-element, setup-intents]
---

## Summary

Integration guide for iDEAL → SEPA Direct Debit subscriptions. iDEAL is single-use; Stripe collects IBAN via iDEAL and converts to SEPA PM for recurring charges. Two paths: Checkout (simpler) and Direct API (Payment Element + SetupIntent). Free trial: 0.01 EUR charged + immediately refunded.

## The iDEAL → SEPA conversion

iDEAL is single-use — each payment requires customer authentication. For subscriptions, Stripe:
1. Collects first payment via iDEAL (captures IBAN)
2. Creates a SEPA Direct Debit PM (`generated_sepa_debit`)
3. Uses SEPA PM for all subsequent recurring charges

Free trial: charges 0.01 EUR via iDEAL → immediately refunded → IBAN captured → SEPA PM created.

## Path 1: Checkout

```js
stripe.checkout.sessions.create({
  payment_method_types: ['ideal'], // or omit to use Dashboard settings
  line_items: [{ price: priceId, quantity: 1 }],
  mode: 'subscription',
  success_url: '...'
})
```

**Dashboard-managed PM**: omit `payment_method_types` but must enable "iDEAL recurring payments" in Dashboard. This enables SEPA for recurring iDEAL only — does NOT turn on standalone SEPA.

Supports: `subscription_data.trial_period_days`, `subscription_data.trial_end`.

## Path 2: Direct API (Payment Element + SetupIntent)

**Prerequisites**: Activate SEPA Direct Debit in Dashboard; comply with iDEAL ToS + SEPA Direct Debit ToS.

1. Create SetupIntent: `payment_method_types=['ideal']`, customer ID
2. Mount Payment Element; `stripe.confirmSetup({ return_url })` → customer redirected to bank
3. Listen for `setup_intent.succeeded` webhook
4. Retrieve SetupIntent with `expand: ['latest_attempt']`
5. Get `generated_sepa_debit` ID from `latest_attempt.payment_method_details.generated_sepa_debit`
6. Create subscription with that SEPA PM + `off_session=true`

**Updating subscriptions**: always use `off_session=true` on updates (same pattern as PayPal).

## Test scenarios (Direct API)

### Email-based (6 patterns)
- `generatedSepaDebitIntentsSucceed@example.com` → processing → succeeded
- `generatedSepaDebitIntentsSucceedDelayed@example.com` → succeeded after 3+ min
- `generatedSepaDebitIntentsFail@example.com` → processing → requires_payment_method
- `generatedSepaDebitIntentsFailDelayed@example.com` → requires_payment_method after 3+ min
- `generatedSepaDebitIntentsSucceedDisputed@example.com` → succeeded + immediate dispute
- `generatedSepaDebitIntentsFailsDueToInsufficientFunds@example.com` → insufficient_funds

### PM tokens (6 patterns)
`pm_ideal_generatedSepaDebit{Scenario}` (same 6 scenarios, for automated testing)

## Related pages

- [[stripe-ideal]] — concept page (updated)
- [[stripe-sepa-debit]] — concept page (updated)
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-ideal-2026]] — verbatim Stripe docs webpage (1015 lines, 1 image reused)
