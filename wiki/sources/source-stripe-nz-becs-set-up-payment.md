---
title: "Stripe: Save New Zealand BECS Direct Debit Details for Future Payments"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-nz-becs-set-up-payment-2025.md"
tags: [stripe, nz-becs, becs, new-zealand, nzd, setup-intents, elements, mandates, save-payment-method]
---

## Summary

Guide for saving NZ BECS Direct Debit bank details for future payments using SetupIntents + Payment Element. Covers customer creation, SetupIntent setup, DDA mandate acknowledgement, off-session charging, and same 6 test accounts as accept-a-payment.

## Key Details

### SetupIntent flow

1. Create SetupIntent server-side: `payment_method_types: ['nz_bank_account']`, `customer`
2. Pass `clientSecret` to client (SPA fetch or server-side render)
3. Mount Payment Element — automatically collects name, email, bank account number, presents NZ BECS Direct Debit Service T&C for DDA agreement
4. `stripe.confirmSetup({ elements, redirect: 'if_required' })` → returns `succeeded` status
5. PaymentMethod now attached to Customer, ready for off-session use

### Off-session charging (after SetupIntent)

```js
stripe.paymentIntents.create({
  payment_method_types: ['nz_bank_account'],
  customer: '{{CUSTOMER_ID}}',
  payment_method: '{{PAYMENTMETHOD_ID}}',
  confirm: true, off_session: true,
  amount: 100, currency: 'nzd',
})
```

### Test accounts

Same bank code `11`, branch `0000`, 6 account/suffix combinations + 6 PaymentMethod tokens as accept-a-payment source.

## Raw Sources

- [[stripe-nz-becs-set-up-payment-2025]] — verbatim webpage content; reuses appearance example screenshot in `raw/assets/stripe-elements-appearance-example.png`
