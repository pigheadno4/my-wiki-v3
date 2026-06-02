---
title: "Stripe: Apple Pay Best Practices"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-apple-pay-best-practices-2025.md"
tags: [stripe, wallets, apple-pay, best-practices, certificate-renewal, conversion, express-checkout, merchant-tokens]
---

## Summary

Best practices guide for Apple Pay integration: express checkout placement, post-purchase registration, defaulting to Apple Pay, certificate renewal procedures, and recurring payment configuration. Includes case studies (Indiegogo +250%, Wish 2×).

## Key Details

**Express checkout**: add Apple Pay button to product detail/list/search pages. Indiegogo: +250% conversion. Don't show button in disabled state.

**Post-purchase registration**: skip mandatory sign-up for Apple Pay users. Collect password/account info on confirmation page after payment.

**Default to Apple Pay**: skip payment method selection page for new Apple Pay users. Wish: 2× conversion. Pre-select Apple Pay.

**Set Up Apple Pay prompt**: detect capable devices without a card; show prompt in checkout, account settings, and payment update emails.

**Certificate renewal** (critical details):
- Valid for **25 months** from activation
- Notifications at **30, 15, 7 days** before expiry
- Always download **new CSR** from Stripe — never reuse old CSR
- Upload new certificate to Stripe **before** activating on Apple Developer account
- Keep **both old and new** certificates in Stripe Dashboard during transition (Apple switches key ~5 min after activation)
- No app update required after replacement

**Recurring**: configure for merchant tokens (MPANs) to enable MIT and prevent cryptogram expiration failures.

## Raw Sources

- [[stripe-apple-pay-best-practices-2025]] — verbatim webpage content (87 lines); no italic fixes needed
