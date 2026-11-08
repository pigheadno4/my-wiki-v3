---
title: "Stripe Subscriptions — Set Up iDEAL + SEPA Direct Debit Subscription"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: https://docs.stripe.com/billing/subscriptions/ideal
raw_files:
  - "stripe-subscriptions-ideal-2026.md"
tags: [stripe, billing, subscriptions, ideal, sepa-debit, eur, netherlands, checkout, payment-element, setup-intents]
---

## Summary

The 2026-11-07 capture of this canonical URL is an index to hosted and Direct API variants, not either variant's instructions. The 2026-05-13 capture documents two distinct iDEAL → SEPA Direct Debit subscription paths: hosted Checkout and Direct API with Payment Element and SetupIntent. The November index establishes no change to either path's payment behavior.

## The iDEAL → SEPA conversion (2026-05-13 variants)

iDEAL is single-use and requires customer authentication for each iDEAL payment. In the older hosted Checkout variant, Stripe charges the first subscription payment through iDEAL to collect bank details. For a free trial, it instead charges 0.01 EUR through iDEAL and immediately refunds that collection. After iDEAL authentication, Stripe saves the customer's IBAN in a SEPA Direct Debit payment method for future payments.

In the older Direct API variant, Stripe charges 0.01 EUR through iDEAL to collect bank details and refunds that setup payment after authentication. A successful iDEAL SetupIntent tracks setup and the SEPA mandate; retrieve `latest_attempt.payment_method_details.generated_sepa_debit` and use that SEPA Direct Debit PaymentMethod to create and charge the subscription. Successful setup does not by itself establish that the later SEPA payment succeeded or that the subscription is active; inspect the payment and subscription outcomes.

## Path 1: Hosted Checkout (2026-05-13)

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

## Path 2: Direct API (Payment Element + SetupIntent; 2026-05-13)

**Prerequisites**: Activate SEPA Direct Debit in Dashboard; comply with iDEAL ToS + SEPA Direct Debit ToS.

1. Create a SetupIntent with `payment_method_types=['ideal']` and the applicable customer identity: `customer_account` in the older Accounts v2 example or `customer` in the Customers v1 example.
2. Mount Payment Element; `stripe.confirmSetup({ return_url })` redirects the customer to the bank for setup authorization.
3. Reliably confirm SetupIntent authorization, for example with the optional `setup_intent.succeeded` webhook, instead of relying only on a customer return. Failed authorization emits `setup_intent.setup_failed`.
4. After setup succeeds, retrieve the SetupIntent with `expand: ['latest_attempt']`.
5. Get the `generated_sepa_debit` ID from `latest_attempt.payment_method_details.generated_sepa_debit`.
6. Create the subscription with that SEPA payment method and `off_session=true` as shown in the older Direct API example. Check the ensuing SEPA payment and subscription status separately.

**Updating subscriptions in this older Direct API flow**: the guide instructs `off_session=true` on updates; otherwise a new payment requires user confirmation.

## Test scenarios (Direct API; 2026-05-13)

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

## Related raw API references

- [[raw/stripe-billing-subscriptions-ideal-2026-11-07|2026-11-07 canonical URL index]] — navigation only; links to [hosted](https://docs.stripe.com/billing/subscriptions/ideal.md?payments-ui-type=stripe-hosted) and [Direct API](https://docs.stripe.com/billing/subscriptions/ideal.md?payments-ui-type=direct-api) variant bodies, which were not captured in this four-file review.

## Raw Sources

- [[raw/stripe-subscriptions-ideal-2026|2026-05-13 variant guide]] — historical factual capture (1015 lines, 1 image reused)
