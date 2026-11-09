---
title: "Stripe: Save ACH Direct Debit Details for Future Payments"
type: source
date_ingested: 2026-05-02
original_format: webpage
raw_files:
  - "stripe-ach-set-up-payment-2025.md"
tags: [stripe, ach, us-bank-account, setup-intent, checkout, financial-connections, microdeposits]
---

## Summary

Guide for saving ACH bank account details for future payments via Checkout (setup mode) or Elements (SetupIntents API). Covers Financial Connections verification, microdeposit verification, and balance checks.

## Key Integration Details

**Checkout (setup mode)**: `mode: 'setup'`; `permissions: ['payment_method']` required; update `invoice_settings.default_payment_method` after `setup_intent.succeeded`.

**Elements + SetupIntents**:
1. Create SetupIntent server-side with `payment_method_types: ['us_bank_account']` and `permissions`
2. Client: `stripe.collectBankAccountForSetup` (opens Financial Connections)
3. Client: display mandate; `stripe.confirmUsBankAccountSetup`
4. If `requires_action`: microdeposit verification via `stripe.verifyMicrodepositsForSetup`

**SetupIntent statuses**: `succeeded` (instant) or `requires_action` → microdeposits.

**Microdeposit verification**: `descriptor_code` (10 attempts) or `amounts` (3 attempts); 10-day timeout.

**Balance check**: use `permissions: ['payment_method', 'balances']` to check balance before initiating payment.

**Accounts v2**: `customer_account` on session/intent; expand `payment_method` on SetupIntent for Financial Connections account ID.

## Raw Sources

- [[stripe-ach-set-up-payment-2025]] — verbatim webpage content (2809 lines; Checkout + Elements paths, Accounts v2 + Customers v1, microdeposit error table)
