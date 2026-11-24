---
title: "Stripe: Set Up Future Revolut Pay Payments"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-revolut-pay-set-up-future-payments-2025.md"
tags: [stripe, wallets, revolut-pay, recurring, setup-intent, off-session, mandate, accounts-v2]
---

## Summary

Guide to saving Revolut Pay payment details and charging customers later. Covers Checkout (setup mode), Direct API, iOS, and Android. On-session payments always redirect to Revolut app even with saved PM.

## Key Details

**On-session always redirects**: any on-session Revolut payment redirects to Revolut app for confirmation, even with a saved payment method.

**Authorization text required** before saving (first time only): "By continuing, you authorize [Business] to debit your Revolut Pay account for this payment and future payments in accordance with [Business]'s terms, until this authorization is revoked."

**Two save paths (Direct API)**:
1. **SetupIntent** (`stripe.confirmRevolutPaySetup()`) with `usage: 'off_session'` → save credentials, charge later
2. **PaymentIntent + `setup_future_usage: 'off_session'`** → charge + save simultaneously

**Detach**: `paymentMethods.detach()` triggers both `mandate.updated` and `payment_method.detached` events.

**Accounts v2**: use `customer_account` instead of `customer` throughout.

## Integration by Platform

**Checkout**: `mode: 'setup'` + `payment_method_types: ['card', 'revolut_pay']` + `customer` ID.

**Direct API (SetupIntent)**: `stripe.confirmRevolutPaySetup(clientSecret, { return_url, mandate_data })`. Mandate data: `customer_acceptance.type: 'online'`, `online.infer_from_client: true`.

**iOS**: `STPPaymentMethodRevolutPayParams` → `STPPaymentMethodParams` → `STPPaymentHandler.confirmSetupIntent()`.

**Android**: `PaymentMethodCreateParams.createRevolutPay()` → `ConfirmSetupIntentParams` → `PaymentLauncher.confirm()`.

## Raw Sources

- [[stripe-revolut-pay-set-up-future-payments-2025]] — verbatim multi-platform guide (1,110 lines); 8 italic fixes
