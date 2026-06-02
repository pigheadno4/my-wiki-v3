---
title: "Stripe: How Cards Work"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-how-cards-work-2025.md"
tags: [stripe, cards, authorization, capture, card-account-updater, webhooks]
---

## Summary

Explains the 4-step card payment flow, manual card update limitations, how to change default payment methods, and automatic card updates via the Card Account Updater.

## Key Details

**4-step payment flow**: format validation → customer authentication (SCA/3DS) → authorization (bank holds funds) → capture (funds move to Stripe).

**Manual card updates**: can only change name, billing address, expiration, metadata; anything else requires delete + create new.

**Change default payment method for invoices/subscriptions**: `stripe.customers.update(id, { invoice_settings: { default_payment_method: 'pm_...' } })`.

**Automatic card updates**: widely supported in US (Amex/Visa/MC/Discover); international varies; cannot identify which cards support it. Webhooks:
- `payment_method.updated`: API call update
- `payment_method.automatically_updated`: network auto-update

If new card number included in update → **fingerprint changes**.

## Raw Sources

- [[stripe-how-cards-work-2025]] — verbatim webpage content
