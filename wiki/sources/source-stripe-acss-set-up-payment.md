---
title: "Stripe: Save ACSS/PAD Payment Details for Future Payments"
type: source
date_ingested: 2026-05-02
original_format: webpage
raw_files:
  - "stripe-acss-set-up-payment-2025.md"
tags: [stripe, acss, acss-debit, canada, cad, setup-intents, mandates, microdeposits, save-payment-method]
---

## Summary

Guide for saving ACSS/PAD bank account details for future payments using SetupIntents, via Checkout (setup mode) or Direct API. Covers mandate params, verification options, microdeposit flow, reusing existing mandates, and off-session charging.

## Key Details

### Checkout setup mode

- `mode: 'setup'` + `payment_method_types: ['acss_debit']`
- Mandate params: `currency` (required — must match bank account), `payment_schedule`, `transaction_type`, `interval_description`, `default_for`
- Optional: `verification_method: 'instant'` or `'microdeposits'`
- After session: retrieve PaymentMethod + Mandate IDs to charge off-session

### Direct API (SetupIntent)

1. Create Customer
2. Create SetupIntent with `payment_method_types: ['acss_debit']`, `customer`, mandate options including `currency`
3. Pass `client_secret` to client — fetch or server-side render
4. Call `stripe.confirmAcssDebitSetup(clientSecret, { payment_method: { billing_details: { name, email } } })` — opens modal for bank collection + verification + mandate
5. Returns `succeeded` (instantly verified) or `requires_action` (microdeposit pending)
6. Optional: `stripe.verifyMicrodepositsForSetup(clientSecret, { amounts: [32, 45] })`

### Off-session charging

After setup, create PaymentIntent with `payment_method`, `customer`, `mandate`, `confirm: true`:

```js
stripe.paymentIntents.create({
  payment_method_types: ['acss_debit'],
  payment_method: '{{PAYMENTMETHOD_ID}}',
  customer: '{{CUSTOMER_ID}}',
  mandate: '{{MANDATE_ID}}',
  confirm: true,
  amount: 100,
  currency: 'cad',
})
```

### Reusing PM with a new mandate

Include `payment_method` on the new PaymentIntent/SetupIntent, but omit `acss_debit` data in the confirm call. Note: charges delayed 3 days; new mandate confirmation email required.

### Microdeposit error codes (SetupIntent-specific)

Uses `last_setup_error` instead of `last_payment_error`. Same 4 error codes as PaymentIntent path.

## Raw Sources

- [[stripe-acss-set-up-payment-2025]] — verbatim webpage content (Checkout + Direct API sections)
