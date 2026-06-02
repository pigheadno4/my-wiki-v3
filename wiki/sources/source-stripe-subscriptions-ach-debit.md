---
title: "Stripe Subscriptions — Set Up ACH Direct Debit Subscription"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-ach-debit-2026.md"
tags: [stripe, billing, subscriptions, ach, us-bank-account, direct-debit, financial-connections, microdeposits]
---

## Summary

End-to-end guide for setting up ACH Direct Debit subscriptions. Covers two integration paths (Elements/advanced and Checkout/hosted), the microdeposit verification extended window for subscriptions, trial period flow, and the required webhook step to set default payment method.

## Two integration paths

| Path | Method | Best for |
|---|---|---|
| Elements (advanced) | `stripe.collectBankAccountForPayment` + Financial Connections | Custom checkout UI |
| Checkout (hosted) | `checkout.sessions.create` with `payment_method_types: ['us_bank_account']` | No-code/low-code |

## Subscription creation (Elements path)

```js
stripe.subscriptions.create({
  customer: customerId,
  items: [{ price: priceId }],
  payment_behavior: 'default_incomplete',
  payment_settings: { payment_method_types: ['us_bank_account'] },
  expand: ['latest_invoice.payments', 'latest_invoice.confirmation_secret']
})
// Use confirmation_secret.client_secret on client (not full PaymentIntent)
```

## Elements verification flow

1. `stripe.collectBankAccountForPayment()` — opens Financial Connections modal
2. Returns `requires_confirmation` → display mandate terms
3. `stripe.confirmUsBankAccountPayment()` → instant verify: sub active; manual entry: microdeposit verification

## Microdeposit extended window for subscriptions

Customers have **10 days** to verify (vs 23h normal `incomplete_expired`), but cannot exceed the billing cycle date. Two microdeposit types:
- **Descriptor code**: single 0.01 USD deposit, 6-digit SM-prefixed code. Max 10 verification attempts.
- **Amounts**: two non-unique deposits with "ACCTVERIFY" descriptor. Max 3 attempts.
- 10-day timeout total. Stripe-hosted verification page or custom form via `stripe.verifyMicrodepositsForPayment`.

## Critical: setting default payment method

ACH PM is NOT automatically set as subscription default after first payment. Must listen to `invoice.payment_succeeded` with `billing_reason=subscription_create` and explicitly update:

```js
stripe.subscriptions.update(subscriptionId, {
  default_payment_method: paymentIntent.payment_method
})
```

## Trial period flow

With `payment_behavior=default_incomplete` + `trial_end`, response includes `pending_setup_intent` (not PaymentIntent). Use Setup variants:
- `collectBankAccountForSetup`, `confirmUsBankAccountSetup`, `verifyMicrodepositsForSetup`
- SetupIntent reaching `succeeded` automatically sets subscription `default_payment_method`

## Checkout (hosted) key events

Delayed notification payment — do NOT fulfill on `checkout.session.completed` alone:
- `checkout.session.completed` — customer authorized debit
- `checkout.session.async_payment_succeeded` — funds confirmed (~4 days) → fulfill
- `checkout.session.async_payment_failed` → retry email
- `invoice.paid` / `invoice.payment_failed` — subscription renewal events

## Sandbox testing

Email format: `{username}+test_email@{domain}` (required to receive mandate/microdeposit emails).

Test accounts (routing `110000000`):
- `000123456789` / `pm_usBankAccount_success` — succeeds
- `000111111113` / `pm_usBankAccount_accountClosed` — fails (account closed)
- `000222222227` / `pm_usBankAccount_insufficientFunds` — fails
- `000333333335` / `pm_usBankAccount_debitNotAuthorized` — fails
- `000555555559` / `pm_usBankAccount_dispute` — triggers dispute
- `000000004954` / `pm_usBankAccount_riskLevelHighest` — blocked by Radar

Test microdeposit codes:
- `32,45` / SM11AA — successful verification
- `10,11` / SM33CC — exceed attempt limit
- `40,41` / SM44DD — microdeposit timeout

## Related pages

- [[stripe-ach-direct-debit]] — ACH concept page (updated with subscription facts)
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-ach-debit-2026]] — verbatim Stripe docs webpage (1017 lines, 1 image)
