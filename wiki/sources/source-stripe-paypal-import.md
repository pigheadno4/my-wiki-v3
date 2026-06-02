---
title: "Stripe: Import Saved PayPal Payment Methods"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-paypal-import-2025.md"
tags: [stripe, wallets, paypal, billing-agreement, import, migration, setup-intent, mandate]
---

## Summary

Short guide for importing existing PayPal billing agreements (created outside Stripe) into Stripe, allowing merchants to reuse them without requiring customer reauthorization.

## Key Details

**Prerequisite**: recurring payments must be enabled (see set-up-future-payments guide).

**Mechanism**: create a SetupIntent with:
- `payment_method_options.paypal.billing_agreement_id`: the existing BAID (e.g., `B-1234556789`)
- `confirm: true`
- `usage: 'off_session'`
- `mandate_data.customer_acceptance.type: 'offline'` — indicates offline acceptance (no redirect needed, customer already authorized elsewhere)

**Cancellation webhooks**: PayPal only sends billing agreement cancellation webhooks for agreements **created through Stripe**. Imported agreements do not trigger cancellation webhooks.

**After import**: use the resulting PaymentMethod the same way as any normally set-up PayPal PM (off-session charging via PaymentIntent).

## Raw Sources

- [[stripe-paypal-import-2025]] — verbatim import guide (65 lines); no fixes needed
