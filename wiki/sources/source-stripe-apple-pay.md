---
title: "Stripe: Apple Pay"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-apple-pay-2025.md"
tags: [stripe, wallets, apple-pay, ios, react-native, web, merchant-id, domain-registration, recurring, merchant-tokens, app-clips]
---

## Summary

Comprehensive Apple Pay integration guide covering Native iOS (Swift), React Native, and Web. No extra fees (same as card). Worldwide except India. Setup requires Apple Merchant ID + Stripe CSR. Web requires domain registration. iOS 16+ adds merchant tokens for recurring. Test limitation: real card required.

## Key Details

**Three integration paths**: Native iOS (Swift/`StripeApplePay`), React Native, Web (Checkout/Elements — no extra config for Checkout).

**iOS setup flow**: Apple Developer enrollment → Apple Merchant ID → Stripe Dashboard CSR → Apple certificate → Xcode Apple Pay capability. Must use Stripe-provided CSR (not self-generated).

**Web domain registration**: all domains showing Apple Pay button must be registered via Stripe's `paymentMethodDomains` API or Dashboard. Includes subdomains and `www`. Direct charges via Connect require per-connected-account registration.

**iOS recurring (iOS 16+)**: merchant tokens via `PKPaymentRequest.recurringPaymentRequest` or `automaticReloadPaymentRequest` — enables MIT transactions.

**iOS order tracking (iOS 16+)**: `applePayContext(context:willCompleteWithResult:handler:)` or `PlatformPayButton.setOrderTracking`.

**App Clips**: `StripeApplePay` module is lightweight, optimized for App Clips.

**Web Checkout `embedded_page`**: Safari 17+ / iOS 17+ only.

**In-app purchase eligibility**: physical goods accept Apple Pay directly; digital goods (US/EEA) redirect to Checkout, Web Elements, or Payment Links.

**Test limitation**: real card with test API keys required — cannot save test cards to Apple Pay wallet.

## Raw Sources

- [[stripe-apple-pay-2025]] — verbatim webpage content (906 lines); fixed `*or*` ×1, `*Connect*` ×1; 1 GIF animation + 1 PNG screenshot downloaded to assets/
