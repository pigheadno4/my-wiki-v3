---
title: "Stripe: Pix Automático"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-22
canonical_url: "https://docs.stripe.com/payments/pix/pix-automatico"
original_format: webpage
raw_files:
  - "stripe-payments-pix-pix-automatico-2026-11-07.md"
  - "stripe-pix-automatico-2025.md"
tags: [stripe, real-time-payments, pix, brazil, brl, pix-automatico, recurring, mandates, pre-debit, iof]
---

## Summary

Pix Automático is [[stripe]]'s mandate-based method for collecting recurring Pix payments from customers in Brazil. The May 6 and November 7, 2026 captures document the same bank-app authorization, pre-debit notice and capture process. Merchant domicile and IOF eligibility come from the separate [[source-stripe-pix|Pix overview]].

## Mandate authorization and recurring charges

- The customer authorizes the payment amount and permitted billing cycle in their banking app. The initial flow takes the first charge when applicable. A subscription with a free trial creates the mandate without a charge. The Pix overview identifies a SetupIntent for setup alone and a PaymentIntent for an initial charge with mandate creation.
- For a later charge, the merchant confirms the recurring PaymentIntent. Stripe triggers the pre-debit notification process. The customer's bank generates and sends the notice with the exact amount and an option to cancel. Stripe waits three days before attempting automatic capture. No further merchant action is required for this sequence.
- The PaymentIntent is `processing` during the wait and retries. Confirmation typically comes three days after the notice and may take up to seven days with retries. The November diagram illustrates a September 1 initial payment, October 1 notice on the next monthly cycle, and October 4 debit.
- If the scheduled capture fails for a retryable reason such as insufficient funds or network failure, Stripe retries once daily for the next three days by default. Separately, Stripe Billing can retry once after one day if the payment was never scheduled, for example after a partner error. Contact Stripe Support to enable that Billing behavior.
- The guide describes an eventual successful or failed outcome. The November [PaymentIntent API object](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-status) includes `succeeded` in its status enum. The guide uses “failed” as outcome wording and leaves the exact API failure state and webhook mapping unspecified.

## Mandate options

Configure `payment_method_options.pix.mandate_options`. Both full guide captures document these defaults.

| Field | Meaning | Default |
| --- | --- | --- |
| `reference` | Subscription name displayed in the customer's banking app at enrollment | Business display name |
| `amount` | Amount that bounds the charge under a maximum mandate or specifies the charge under a fixed mandate | 400 BRL |
| `amount_type` | `maximum` authorizes up to the amount and `fixed` authorizes the exact amount | `maximum` |
| `amount_includes_iof` | Controls whether the customer pays applicable IOF or the business absorbs it | `never` (customer pays when applicable) |
| `payment_schedule` | Permitted billing frequency. Later charges must follow the mandate's terms. | `monthly` |
| `end_date` | Mandate expiry | No expiry if omitted |
| `start_date` | Mandate start in YYYY-MM-DD, at least three days in the future | Current date plus three days |

The billing cycle defines permitted frequency. A daily `payment_schedule` causes all payments to fail. Factor potential price changes, conversion fees and customer-paid Stripe Tax into a maximum mandate amount where applicable.

## Merchant scope and IOF

The separate [[source-stripe-pix|Pix overview]] says Stripe accounts in Brazil can accept one-time Pix in BRL and that businesses outside Brazil can accept eligible recurring Pix Automático payments from customers in Brazil. Pix Automático is unavailable to businesses domiciled in Brazil. The standalone guide points to the same IOF handling as one-time Pix. The Pix overview scopes IOF to foreign-exchange transactions when Brazilian customers pay international businesses and records a 3.5% rate in the November capture, subject to change. Apply that scope to each qualifying recurring transaction.

The separate [2026-04-22.dahlia changelog entry](https://docs.stripe.com/changelog/dahlia/2026-04-22/pix-recurring-payments-support) covers versioned Pix mandate options on PaymentIntents, SetupIntents and Checkout Sessions for recurring payments from customers in Brazil.

## Related

- [[source-stripe-pix-save-payment-details]] — mandate setup and saved payment details.
- [[source-stripe-subscriptions-pix]] — Pix subscription integration.
- [[source-stripe-pix-accept-payment]] — one-time Pix acceptance.
- [[stripe-real-time-payments]] — Pix and other real-time payment methods.

## Raw Sources

- [[raw/stripe-payments-pix-pix-automatico-2026-11-07]] — full Pix Automático guide captured 2026-11-07 (86 lines).
- [[raw/stripe-pix-automatico-2025]] — historical full guide captured 2026-05-06 (79 lines).
