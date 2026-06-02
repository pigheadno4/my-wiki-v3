---
title: "Stripe: Bacs Direct Debit Payments in the UK"
type: source
date_ingested: 2026-05-02
original_format: webpage
raw_files:
  - "stripe-bacs-direct-debit-2025.md"
tags: [stripe, bacs, bank-debit, uk, gbp, mandates, disputes, connect, custom-branding]
---

## Summary

Reference page for Bacs Direct Debit on Stripe. UK-only bank debit method requiring a mandate (DDI). Covers settlement timing, disputes, mandates, refunds, Connect/capability setup, and Custom Branding.

## Key Details

**Limits**: 100,000 GBP per transaction; 10,000 GBP weekly for new users (increases over time).

**Settlement**:
- Existing mandate: T+3 payment success, T+4 funds available; cutoff 20:00 Europe/London
- New mandate: T+7 funds available (mandate active at T+3, funds leave customer bank at T+5)

**Disputes**: unlimited time window; final and uncontestable — must resolve directly with customer.

**Mandates (DDI)**: requires sort code, account number, name, email, full address. Customer can cancel via merchant or their bank; cancellation invalidates future debits. Events: `mandate.updated`, `payment_method.automatically_updated`.

**Refunds**: 180-day window; 3–4 business days. Refunds are outside Bacs scheme — if customer disputes after refund, lose both disputed amount and refund amount separately.

**Debit notifications**: Stripe auto-emails on mandate creation and before each debit. Custom email templates require approval.

**Product support**: Connect, Checkout, Payment Links, Subscriptions, Invoicing, Elements. Exceptions: Payment Element can't create SetupIntents for Bacs (use Checkout setup mode); Express Checkout Element not supported.

**Connect / capability**: UK platforms don't need `bacs_debit_payments` for destination charges. All platforms need it for `on_behalf_of`. Request `bacs_debit_payments` capability.

**Custom Branding**: 50 GBP/month. Set `settings.bacs_debit_payments.display_name` when requesting capability (or on account). Business name appears on new mandates 5 business days after request. Without display_name → defaults to Stripe branding.

**Billing Retries** (private preview): automatic retry for insufficient funds failures, for subscription or one-off invoices.

## Raw Sources

- [[stripe-bacs-direct-debit-2025]] — verbatim webpage content
