---
title: "Stripe: Accept an ACH Direct Debit Payment"
type: source
date_ingested: 2026-05-02
original_format: webpage
raw_files:
  - "stripe-ach-accept-payment-2025.md"
tags: [stripe, ach, us-bank-account, checkout, payment-element, payment-intents, financial-connections, verification]
---

## Summary

Comprehensive integration guide for ACH Direct Debit across 4+ paths: Checkout (hosted/embedded), Checkout Sessions API + Payment Element, PaymentIntents API, and Direct API. Covers verification, disputes, payment references, and target debit dates.

## Key Integration Details

**Dynamic payment methods** (recommended): enable from Dashboard, no code changes.

**Checkout**: `payment_method_types: ['card', 'us_bank_account']`; all line_items in USD; recommend `payment_intent_data.setup_future_usage: 'off_session'` for saving.

**Verification**:
- Automatic (default): Financial Connections instant + microdeposit fallback
- Instant-only: `verification_method: 'instant'`, `permissions: ['payment_method']`
- Microdeposit: 10-day window; fails on: sending failure, 10 attempts exceeded, timeout

**Financial Connections account**: access via `us_bank_account.financial_connections_account` after expanding `payment_intent.payment_method` on Checkout Session.

**Payment reference**: `charge.payment_method_details.us_bank_account.payment_reference` after `charge.succeeded`.

**Target debit date**: min 3 days future, max 15 days; incompatible with microdeposit verification.

**Test emails**: `{username}+test_email@{domain}` format for sandbox mandate/microdeposit emails.

**Dispute resolution**: first dispute invalidates mandate; second blocks account; reconfirm mandate with `mandate_data[customer_acceptance][type]=offline` curl.

## Raw Sources

- [[stripe-ach-accept-payment-2025]] — verbatim webpage content (6569 lines; Checkout/Elements/PaymentIntents/Direct API + Accounts v2 + Customers v1 variants)
