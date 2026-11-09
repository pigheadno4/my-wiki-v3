---
title: "Stripe: Google Pay"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-google-pay-2025.md"
tags: [stripe, wallets, google-pay, android, react-native, web, dpan, fpan, liability-shift, domain-registration, sigma]
---

## Summary

Comprehensive Google Pay guide covering Android (native `GooglePayLauncher`), React Native (`PlatformPayButton`), and Web (Checkout/Elements). Three liability shift scenarios by token type. Web domain registration required. Sigma `card_token_type` field for monitoring.

## Key Details

**Three integration paths**: Android (native), React Native, Web (Checkout auto, Elements via Express Checkout Element).

**Android setup**: add `com.google.android.gms.wallet.api.enabled` to AndroidManifest.xml. `GooglePayLauncher` (full flow) or `GooglePayPaymentMethodLauncher` (PM collection only). Must request production access from Google Pay & Wallet Console.

**Web domain registration**: same as Apple Pay — all domains including `www`. Direct charges Connect: per-connected-account.

**Liability shift — three cases**:
1. **DPAN** (card on Android device): liability shift by default
2. **FPAN** (card in Chrome/Google property): 3D Secure required for global liability shift including Visa. Customize via Radar rules
3. **E-commerce tokens**: **neither liability shift nor 3D Secure supported**

**Visa liability shift for non-Stripe-hosted**: must enable "Fraud Liability Protection for Visa Device Tokens" in Google Pay & Wallet Console.

**Sigma**: `card_token_type` field: `fpan` for FPAN; `dpan_or_ecommerce_token` for DPAN/e-commerce tokens.

**Test**: physical Android device required; real card in Google Wallet; Test card suite.

**In-app purchase eligibility**: digital goods US/EEA can use Stripe via Mobile Payment Element, Checkout, or Payment Links.

## Raw Sources

- [[stripe-google-pay-2025]] — verbatim webpage content (716 lines); fixed `*subscriptions*` ×1, `*client secret*` ×2, `*live mode*` ×2, `*Connect*` ×1
