---
title: "Stripe: Accept Bacs Direct Debit Payments"
type: source
date_ingested: 2026-05-02
original_format: webpage
raw_files:
  - "stripe-bacs-accept-payment-2025.md"
tags: [stripe, bacs, bank-debit, uk, gbp, checkout, elements, payment-element, webhooks, mandates]
---

## Summary

Integration guide for accepting Bacs Direct Debit payments via Checkout or Elements/PaymentIntent. Covers both paths end-to-end including test accounts, failure codes, optional debit date, and mandate reference prefix customization.

## Key Details

### Checkout path

1. Create Product + Price (GBP required)
2. Create Checkout Session: `payment_method_types: ['bacs_debit']`, `mode: 'payment'`, `payment_intent_data.setup_future_usage: 'off_session'`
3. Handle 3 async events: `checkout.session.completed` (mandate authorized), `checkout.session.async_payment_succeeded` (fulfill), `checkout.session.async_payment_failed` (retry request)
4. Optional: `payment_method_options.bacs_debit.target_date` — 3–15 days out; best-effort; delayed to next business day if weekend/holiday/insufficient lead time

### Elements path

1. Create Customer
2. Payment Element collects mandate automatically
3. Create PaymentIntent (`customer` or `customer_account`, `currency: 'gbp'`)
4. `stripe.confirmPayment` with `return_url`
5. Handle `payment_intent.succeeded`, `payment_intent.processing`, `payment_intent.payment_failed` webhooks

### Test accounts (sort code `108800`)

| Account | Token | Behavior |
| --- | --- | --- |
| `00012345` | `pm_bacsDebit_success` | Succeeds immediately |
| `90012345` | `pm_bacsDebit_successDelayed` | Succeeds after 3 min |
| `33333335` | `pm_bacsDebit_debitNotAuthorized` | Fails immediately; mandate → inactive |
| `93333335` | `pm_bacsDebit_debitNotAuthorizedDelayed` | Fails after 3 min; mandate → inactive |
| `22222227` | `pm_bacsDebit_insufficientFunds` | Fails; mandate stays active |
| `92222227` | `pm_bacsDebit_insufficientFundsDelayed` | Fails after 3 min; mandate stays active |
| `55555559` | `pm_bacsDebit_dispute` | Succeeds then dispute created |
| `00033333` | `pm_bacsDebit_mandateRefused` | PM created; mandate → inactive |
| `00044444` | — | Setup fails immediately (invalid account) |
| `34343434` | `pm_bacsDebit_exceedsWeeklyLimit` | Fails: `charge_exceeds_source_limit` |
| `12121212` | `pm_bacsDebit_exceedsTransactionLimit` | Fails: `charge_exceeds_transaction_limit` |

### Failure codes

| Code | Retryable |
| --- | --- |
| `account_closed` | No |
| `bank_ownership_changed` | No |
| `debit_not_authorized` | No |
| `invalid_account_number` | No |
| `generic_could_not_process` | Yes |
| `insufficient_funds` | Yes |

### Mandate reference prefix

`payment_method_options.bacs_debit.mandate_options.reference_prefix` on PaymentIntent, SetupIntent, or Checkout Session. Max 12 chars, uppercase/numbers/spaces/`./_/-/&`. Cannot start with `DDIC` or `STRIPE`. Generates 18-char reference.

## Raw Sources

- [[stripe-bacs-accept-payment-2025]] — verbatim webpage content (Checkout + Elements sections)
