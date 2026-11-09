---
title: "Stripe: Accept a Canadian Pre-Authorized Debit Payment (ACSS)"
type: source
date_ingested: 2026-05-02
original_format: webpage
raw_files:
  - "stripe-acss-accept-payment-2025.md"
tags: [stripe, acss, acss-debit, canada, cad, checkout, payment-intents, mandates, microdeposits, verification]
---

## Summary

Integration guide for accepting ACSS/PAD payments via Checkout (stripe-hosted or embedded) and Direct API (PaymentIntents + Stripe.js). Covers mandate params, verification options, microdeposit flow, test tokens and accounts, target date, and instant-only vs microdeposit-only verification.

## Key Details

### Checkout path

Checkout Session requirements:
- `payment_method_types: ['acss_debit']`
- All line items in same currency (`cad` or `usd`)
- `payment_method_options.acss_debit.mandate_options`: `payment_schedule` (required), `interval_description` (required if `interval` or `combined`), `transaction_type` (required)
- Optional: `verification_method: 'instant'` or `'microdeposits'`
- Optional: `target_date` — 3–15 days, best-effort; incompatible with `microdeposits` verification

### Direct API path (PaymentIntents)

1. Create Customer (Accounts v2 or Customers v1)
2. Create PaymentIntent with `currency: 'cad'`, mandate options, optional `setup_future_usage: 'off_session'`
3. Pass `client_secret` to client — retrieve via fetch or server-side render
4. Call `stripe.confirmAcssDebitPayment(clientSecret, { payment_method: { billing_details: { name, email } } })` — opens on-page modal for bank collection + verification + mandate agreement
5. Handle two statuses: `processing` (instant verified) → await webhooks; `requires_action` → microdeposit verification
6. Optional: `stripe.verifyMicrodepositsForPayment(clientSecret, { amounts: [32, 45] })` for custom verification page

### Microdeposit verification

- Stripe sends 2 deposits (1–2 business days); statement descriptor includes `ACCTVERIFY`
- Limit: 3 failed attempts; 10-day timeout → `requires_payment_method` + `last_payment_error`
- Hosted verification page URL in `next_action.verify_with_microdeposits.hosted_verification_url`

### Webhooks (PaymentIntent path)

| Event | Meaning |
| --- | --- |
| `payment_intent.processing` | Bank account verified / payment submitted |
| `payment_intent.succeeded` | Payment complete — fulfill order |
| `payment_intent.payment_failed` | Failed (or microdeposit verification failed) — request new PM |

### Test payment method tokens

| Token | Scenario |
| --- | --- |
| `pm_acssDebit_success` | Succeeds immediately |
| `pm_acssDebit_noAccount` | Fails — no account found |
| `pm_acssDebit_accountClosed` | Fails — account closed |
| `pm_acssDebit_insufficientFunds` | Fails — insufficient funds |
| `pm_acssDebit_debitNotAuthorized` | Fails — debits not authorized |
| `pm_acssDebit_dispute` | Succeeds then dispute |

### Test account numbers (institution `000`, transit `11000`)

| Account | Scenario |
| --- | --- |
| `000123456789` | Succeeds immediately after microdeposit verification |
| `900123456789` | Succeeds with 3-min delay after verification |
| `000222222227` | Fails immediately after verification |
| `900222222227` | Fails with 3-min delay after verification |
| `000666666661` | Fails to send microdeposits |
| `000777777771` | Fails — exceeds weekly volume limit |
| `000888888881` | Fails — exceeds transaction limit |

Microdeposit amounts: `32` + `45` = success; `10` + `11` = too many attempts; anything else = fails.

## Raw Sources

- [[stripe-acss-accept-payment-2025]] — verbatim webpage content (Checkout + Direct API sections)
