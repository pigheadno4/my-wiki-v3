---
title: "Stripe: Migrate Existing Bank Accounts to Payment Intents API"
type: source
date_ingested: 2026-05-02
original_format: webpage
raw_files:
  - "stripe-ach-migrate-bank-accounts-2025.md"
tags: [stripe, ach, us-bank-account, migration, bank-account, mandates, checkout-sessions, payment-intents]
---

## Summary

Guide for migrating existing BankAccount objects (from Tokens API) to work with Payment Intents or Checkout Sessions API. Covers mandate creation, using BankAccount as PaymentMethod, and updating Invoices/Subscriptions.

## Key Details

**Checkout Sessions**: use `saved_payment_method_options.allow_redisplay_filters: ['unspecified', 'always']` + `customer` + `payment_method_types: ['us_bank_account']` to display saved bank accounts. Prefill customer email if already set.

**Payment Intents mandate**: must create mandate before first use. Options:
1. SetupIntent with `confirm: true` and `mandate_data.customer_acceptance.type: 'offline'`
2. PaymentIntent confirmation with `mandate_data`
3. PPD mandate for offline pre-authorization

**Authorization is only required once** — BankAccount is reusable afterward.

**BankAccount as PaymentMethod**: pass BankAccount ID directly as `payment_method` in PaymentIntents/SetupIntents. `paymentMethods.retrieve()` returns same object with `type: us_bank_account`.

**Invoices/Subscriptions**: update `invoice_settings.default_payment_method` on customer, or set `default_payment_method` directly on invoice/subscription.

## Raw Sources

- [[stripe-ach-migrate-bank-accounts-2025]] — verbatim webpage content (Checkout Sessions + Payment Intents paths, mandate creation, BankAccount view comparison, Invoices/Subscriptions)
