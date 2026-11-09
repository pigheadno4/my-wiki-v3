---
title: "Stripe: ACH Direct Debit"
type: source
date_ingested: 2026-05-02
original_format: webpage
raw_files:
  - "stripe-ach-direct-debit-2025.md"
tags: [stripe, ach, us-bank-account, bank-debit, mandates, disputes, financial-connections, connect]
---

## Summary

Comprehensive guide to ACH Direct Debit: US bank accounts, USD only, business-initiated, delayed notification. T+4 standard / T+2 faster settlement. Disputes final and uncontestable. Mandates required.

## Key Details

**Settlement**: T+4 (cutoff 21:00 ET) or T+2 eligible users (cutoff 14:00 ET).

**Mandates**: online (Stripe-hosted auto) or offline (custom must display text). Nacha requires mandate email to customer billing email.

**Disputes**: personal = 60 days; business = 2 days; final; first dispute invalidates mandate; second dispute blocks account. Submit evidence via Dashboard or Files API.

**Blocked accounts**: `payment_method.automatically_updated` + `us_bank_account.status_details.blocked`.

**Refunds**: 180 days max; 3 business days min; appears as credit not refund.

**Statement descriptor**: 16 alphanumeric char truncation; no `<>'"`.

**Connect**: `us_bank_account_ach_payments` capability; PaymentMethod cloning supported.

**Billing retries**: max 2 retries within 40 days.

**Test accounts**: 11 test account numbers (routing `110000000`); microdeposit test codes.

## Raw Sources

- [[stripe-ach-direct-debit-2025]] — verbatim webpage content (5 SVGs, javascript/node code blocks, settlement/dispute/mandate/testing details)
