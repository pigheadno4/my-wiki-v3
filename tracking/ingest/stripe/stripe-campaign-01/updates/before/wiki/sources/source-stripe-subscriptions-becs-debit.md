---
title: "Stripe Subscriptions — Set Up BECS Direct Debit Subscription (Australia)"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-becs-debit-2026.md"
tags: [stripe, billing, subscriptions, becs, australia, aud, direct-debit, setup-intents, mandate]
---

## Summary

End-to-end guide for BECS Direct Debit subscriptions in Australia using SetupIntents + Elements. Key distinctions: mandatory DDR compliance, no auto-retry, SetupIntent pre-authorization flow before subscription creation.

## Integration flow

1. Server: Create SetupIntent with `payment_method_types=['au_becs_debit']`
2. Client: Mount `auBankAccount` Element, collect BSB + account number + account holder name + email
3. Client: `stripe.confirmAuBecsDebitSetup(clientSecret, { payment_method: { au_becs_debit, billing_details } })`
4. SetupIntent → `succeeded`; share mandate URL with customer
5. Server: Create Customer with PM as `default_payment_method` (and `payment_method`)
6. Server: Create subscription (PM already default — no extra params needed)

## Mandatory DDR/mandate compliance

Must include in checkout form:
- BSB number, account number, account holder name
- Display Stripe's DDR service agreement (inline or linked, labeled "DDR service agreement")
- Display exact authorization text including: Stripe Payments Australia Pty Ltd ACN 160 180 343, BECS User ID 507156
- After confirmation: share mandate URL, business name, payment amount/schedule, DDR link
- Stripe hosts the mandate URL under `Mandate.payment_method_details.au_becs_debit.url`

## Critical: No auto-retry

**BECS Direct Debit payments are never automatically retried**, even if a retry schedule is configured for other payment methods.

## Subscription creation (after SetupIntent succeeds)

```js
// Customer created with PM as default_payment_method
stripe.subscriptions.create({
  customer: customerId,
  items: [{ price: priceId }]
  // No PM params needed — already set as customer default
})
```

## Optional features

- `billing_cycle_anchor` — manual billing cycle; prorates time until anchor (use `proration_behavior='none'` to suppress)
- `trial_end` — free trial period; can combine with billing_cycle_anchor

## Test accounts (BSB `000000`)

| Account | Token | Behavior |
|---|---|---|
| `000123456` | `pm_auBecsDebit_success` | Instant success; mandate active |
| `900123456` | `pm_auBecsDebit_successDelayed` | Success after 3 min; mandate active |
| `111111113` | `pm_auBecsDebit_accountClosed` | Fails; mandate → inactive |
| `111111116` | `pm_auBecsDebit_noAccount` | Fails; mandate → inactive |
| `222222227` | `pm_auBecsDebit_referToCustomer` | Fails; mandate stays active |
| `922222227` | `pm_auBecsDebit_referToCustomerDelayed` | Fails after 3 min; mandate stays active |
| `333333335` | `pm_auBecsDebit_debitNotAuthorized` | Fails; mandate → inactive |
| `666666660` | `pm_auBecsDebit_dispute` | Succeeds then dispute |
| `343434343` | `pm_auBecsDebit_exceedsWeeklyLimit` | Fails with `charge_exceeds_source_limit` |
| `121212121` | `pm_auBecsDebit_exceedsTransactionLimit` | Fails with `charge_exceeds_transaction_limit` |

## Related pages

- [[stripe-au-becs-debit]] — concept page (updated with subscription facts)
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-becs-debit-2026]] — verbatim Stripe docs webpage (843 lines)
