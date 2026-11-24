---
title: "Stripe: Secure Remote Commerce Program Guide"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-secure-remote-commerce-2025.md"
tags: [stripe, src, click-to-pay, masterpass, visa-checkout, card-networks, checkout]
---

## Summary

Guide to accepting payments via Secure Remote Commerce (SRC) / Click to Pay through Stripe. SRC is a card network industry standard replacing Visa Checkout and Masterpass, supporting Visa, Mastercard, American Express, and Discover.

## Key Details

**US only** at this time.

**Masterpass deprecation**: Mastercard deprecated Masterpass. New Masterpass Checkout IDs can't be generated in the Dashboard. Stripe is working to re-enable SRC onboarding.

**SRC replaces** both Visa Checkout and Masterpass with a unified checkout supporting multiple card brands.

**Integration**:
1. Generate Masterpass Checkout ID in Stripe Dashboard
2. Configure sandbox and production callback URLs
3. Include Mastercard's `merchant.js` script (sandbox or production URL)
4. Display SRC button image (black or white text variants)
5. Attach click handler → `masterpass.checkout({ checkoutId, allowedCardTypes, amount, currency, cartId, callbackUrl })`
6. Handle callback: extract `oauth_verifier` query param → confirm PaymentIntent with `payment_method_data.type: 'card'` + `card.masterpass.transaction_id`

**Payment method type**: `card` (not a separate enum) — SRC data passed as nested `card.masterpass` object.

**`masterpass.checkout` parameters**: `checkoutId`, `allowedCardTypes` (master/amex/visa/etc.), `amount` (decimal), `currency`, `cartId` (unique ID), `callbackUrl` (optional override).

**Testing**: Mastercard sandbox with [test cards](https://developer.mastercard.com/masterpass/documentation/migration/masterpass_to_src_migration/#mastercard-test-cards). Must serve from http/https (filesystem not supported).

## Raw Sources

- [[stripe-secure-remote-commerce-2025]] — verbatim SRC program guide (137 lines); 1 italic fix
