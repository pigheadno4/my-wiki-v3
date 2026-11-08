---
title: "Stripe Subscriptions — Set Up Canadian Pre-Authorized Debit (ACSS Debit) Subscription"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-acss-debit-2026.md"
tags: [stripe, billing, subscriptions, acss-debit, canada, cad, pad, mandate, microdeposit]
---

## Summary

Integration guide for Canadian pre-authorized debit (ACSS, PAD) subscriptions. Canada/CAD only. Checkout NOT supported. Single integration path: Elements with `stripe.confirmAcssDebitPayment`. Key distinctions: no auto-retry, manual default PM setup via webhook, 10-day microdeposit window, mandate auto-configured by Stripe.

## Key constraints

- **Canada only, CAD** — pre-authorized debit agreement (PAD)
- **Checkout NOT supported** — waitlist only
- **No auto-retry** — ACSS payments never automatically retried
- `acss_debit` PM type

## Subscription creation

```js
stripe.subscriptions.create({
  customer: customerId,
  items: [{ price: priceId }],
  payment_behavior: 'default_incomplete',
  payment_settings: { payment_method_types: ['acss_debit'] },
  expand: ['latest_invoice.payments', 'latest_invoice.confirmation_secret']
})
```

## Client-side mandate flow

`stripe.confirmAcssDebitPayment(clientSecret, { payment_method: { billing_details: { name, email } } })`

- Required: `name` + `email` in billing_details
- Opens on-page modal UI for bank account collection + verification + mandate acknowledgment
- Customer acknowledges mandate once; subsequent charges need no re-authorization
- Instant verification → sub `active`; manual → 10-day microdeposit window

## Microdeposit extended window

Customers have **10 days** to verify (vs 23h normal), but not past billing period date. Max 3 failed attempts. Standard microdeposit codes: `32,45`=verify, `10,11`=exceed attempts.

## Default PM must be set manually

Listen to `invoice.payment_succeeded` + `billing_reason=subscription_create` → update `subscription.default_payment_method` (same pattern as BECS AU).

## Trial period

Returns `pending_setup_intent`. Use `stripe.confirmAcssDebitSetup` / `verifyMicrodepositsForSetup`. SetupIntent `succeeded` → auto-sets `default_payment_method`.

## Save for future use

SetupIntent with `mandate_options.default_for=['invoice','subscription']` → after `succeeded` → update customer `invoice_settings.default_payment_method`.

## Test tokens (6)

`pm_acssDebit_success`, `pm_acssDebit_noAccount`, `pm_acssDebit_accountClosed`, `pm_acssDebit_insufficientFunds`, `pm_acssDebit_debitNotAuthorized`, `pm_acssDebit_dispute`

## Test accounts (7)

Institution `000`, Transit `11000`. Accounts: `000123456789` (success), `900123456789` (3-min delay success), `000222222227` (fail), `900222222227` (3-min fail), `000666666661` (fail microdeposits), `000777777771` (weekly limit), `000888888881` (transaction limit).

## Related pages

- [[stripe-acss-debit]] — concept page (updated with subscription facts)
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-acss-debit-2026]] — verbatim Stripe docs webpage (442 lines)
