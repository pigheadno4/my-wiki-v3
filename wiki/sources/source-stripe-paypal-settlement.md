---
title: "Stripe: PayPal Settlement Preference"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-paypal-settlement-2025.md"
tags: [stripe, wallets, paypal, settlement, reconciliation, payouts, disputes, refunds, currency-conversion]
---

## Summary

Explains the two PayPal settlement modes available in Stripe — settling funds on Stripe vs. settling on PayPal — and their implications for payouts, reconciliation, Dashboard reporting, refunds, and disputes.

## Key Details

**Who chooses**: Direct businesses set preference at PayPal activation. **Connect users always settle on Stripe** (no choice).

**Changing settlement**: requires filing a Stripe support ticket via Dashboard → PayPal settings → "Contact Support to change".

## Settlement on Stripe

- Funds immediately transferred PayPal → Stripe balance
- Normal Stripe payout schedule applies
- Automatic transaction reconciliation
- Dashboard (Gross/Net charts, payment details) works as with other payment methods
- Refunds and dispute coverage draw from Stripe balance; PayPal dispute fees charged via `adjustment` balance transaction

## Settlement on PayPal

- Stripe balance transaction amount = **0** (funds go to PayPal balance, not Stripe)
- Gross and Net volume charts **do not** reflect PayPal sales — use the Payment methods report instead
- Payment details Net value = negative fee amount (only Stripe fee change, no fund movement)
- Refunds and disputes managed from Stripe Dashboard but funds come from PayPal account
- **Must maintain positive balance in both accounts** to cover refunds, disputes, and PayPal fees
- Manual reconciliation required; Stripe provides support via payout reconciliation guide
- Payouts managed on PayPal side

## Currency Conversions

Occurs when presentment currency ≠ settlement currency. Prevent via multicurrency settlement (add a settlement currency for every presentment currency).

## Raw Sources

- [[stripe-paypal-settlement-2025]] — verbatim settlement preference guide (59 lines); 2 italic fixes
