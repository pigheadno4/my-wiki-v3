---
title: "Stripe: Accept a New Zealand BECS Direct Debit Payment"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-nz-becs-accept-payment-2025.md"
tags: [stripe, nz-becs, becs, new-zealand, nzd, elements, payment-intents, mandates]
---

## Summary

Integration guide for accepting NZ BECS Direct Debit payments via PaymentIntent + Payment Element. Covers customer creation, PaymentIntent setup, DDA mandate acknowledgement (Payment Element handles automatically), off-session charging, and test accounts.

## Key Details

### Integration flow

1. Create PaymentIntent server-side: `payment_method_types: ['nz_bank_account']`, `currency: 'nzd'`, `customer_account` / `customer`, optional `setup_future_usage: 'off_session'`
2. Pass `clientSecret` to client
3. Mount Payment Element (`elements.create('payment')` / `paymentElement.mount('#payment-element')`) — automatically collects name, email, bank account number, and presents NZ BECS Direct Debit Service T&C for agreement
4. `stripe.confirmPayment({ elements, redirect: 'if_required' })` → returns `processing` status
5. Handle webhooks: `payment_intent.processing` / `payment_intent.succeeded` / `payment_intent.payment_failed`

**Mandate acknowledgement text** (if not using Payment Element):
> By providing your bank account details and confirming this payment, you authorise Stripe New Zealand Limited (authorisation code 3143978), to debit your account with the amounts of direct debits payable to [Merchant] in accordance with this authority... subject to your bank's T&Cs and the [Direct Debit Service Terms and Conditions].

### Off-session charging

After `setup_future_usage: 'off_session'` and PaymentIntent succeeds, PaymentMethod attached to customer. Charge later:
```js
stripe.paymentIntents.create({
  payment_method_types: ['nz_bank_account'],
  customer: '{{CUSTOMER_ID}}',
  payment_method: '{{PAYMENTMETHOD_ID}}',
  confirm: true, off_session: true,
  amount: 100, currency: 'nzd',
})
```

### Target date

`payment_method_options.nz_bank_account.target_date`: 3–15 days out, best-effort. Can cancel PaymentIntent up to 3 business days before. Delayed to next business day if weekend/holiday.

### Test accounts (bank code `11`, branch `0000`)

| Account | Suffix | Behavior |
| --- | --- | --- |
| `0000000` | `010` | Succeeds |
| `2222222` | `027` | Fails — insufficient funds; mandate active |
| `8888888` | `000` | Fails — refer to customer; mandate active |
| `1111111` | `016` | Fails — no account; mandate inactive |
| `5555555` | `059` | Fails — debit not authorized; mandate inactive |
| `9999999` | `000` | Stays `processing` indefinitely |

### Test PaymentMethod tokens

`pm_nzBankAccount_success`, `pm_nzBankAccount_insufficientFunds`, `pm_nzBankAccount_referToCustomer`, `pm_nzBankAccount_noAccount`, `pm_nzBankAccount_debitNotAuthorized`, `pm_nzBankAccount_processing`

## Raw Sources

- [[stripe-nz-becs-accept-payment-2025]] — verbatim webpage content; includes 1 appearance screenshot in `raw/assets/stripe-elements-appearance-example.png`
