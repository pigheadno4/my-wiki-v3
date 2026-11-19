---
title: "Stripe: Save Australia BECS Direct Debit Details for Future Payments"
type: source
date_ingested: 2026-05-02
original_format: webpage
raw_files:
  - "stripe-au-becs-set-up-payment-2025.md"
tags: [stripe, au-becs, becs, australia, aud, setup-intents, elements, ios, android, mandates, save-payment-method]
---

## Summary

Guide for saving AU BECS Direct Debit bank details for future payments using SetupIntents, via Elements (HTML+JS + React), iOS (STPAUBECSFormView), and Android. Covers DDR mandate collection requirements, `AuBankAccountElement`, off-session charging, and 10 test accounts.

## Key Details

### DDR mandate requirements

Before creating a BECS payment, customer must submit a Direct Debit Request (DDR). Required information: Account name, BSB number, account number. Must display Stripe's DDR service agreement (inline or linked). Authorization text (exact) must include Stripe's ACN 160 180 343 Direct Debit User ID 507156. Mandate URL available from `Mandate.url` after confirmation.

### Elements path (HTML+JS)

1. Create SetupIntent server-side: `payment_method_types: ['au_becs_debit']`, `customer_account` or `customer`
2. Mount `AuBankAccountElement` (`elements.create('auBankAccount', options)`) on form
3. Client: `stripe.confirmAuBecsDebitSetup(clientSecret, { payment_method: { au_becs_debit: auBankAccount, billing_details: { name, email } } })`
4. Listen for BSB validation: `auBankAccount.on('change', ...)` to show bank name and errors
5. On success: share mandate URL, business name, payment amount/schedule

### Elements path (React)

- `<AuBankAccountElement>` component from `@stripe/react-stripe-js`
- `useStripe()` + `useElements()` hooks or `ElementsConsumer` for class components
- Same `stripe.confirmAuBecsDebitSetup` flow

### iOS (STPAUBECSFormView)

- Same `STPAUBECSFormView` + `STPPaymentHandler` as accept-a-payment flow, but using SetupIntent client secret
- `stripe.setupIntents.create({ payment_method_types: ['au_becs_debit'], customer_account / customer })`

### Off-session charging (after SetupIntent)

```js
stripe.paymentIntents.create({
  amount: 1000, currency: 'aud',
  payment_method_types: ['au_becs_debit'],
  customer_account / customer: '...',
  payment_method: '{{PAYMENTMETHOD_ID}}',
  confirm: true,
})
```

### Test accounts (BSB `000000`) — same 10 as accept-a-payment

## Raw Sources

- [[stripe-au-becs-set-up-payment-2025]] — verbatim webpage content (Elements + iOS + Android sections)
