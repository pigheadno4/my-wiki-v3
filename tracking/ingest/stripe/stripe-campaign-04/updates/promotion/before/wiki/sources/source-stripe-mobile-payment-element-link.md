---
title: "Stripe Docs — Link in the Mobile Payment Element"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-mobile-payment-element-link-2025.md"
tags: [stripe, link, mobile, ios, android, react-native, payment-element, defaultBillingDetails]
---

## Summary

Guide for enabling Link in the Mobile Payment Element across iOS, Android, and React Native. Covers setup steps, prefilling customer details, and sandbox testing.

## Key Facts

- **Platforms**: iOS (Swift), Android (Kotlin), React Native
- **Setup**: latest Stripe Mobile SDK + Link enabled in Dashboard + dynamic PMs (`automatic_payment_methods`)
- **Sandbox OTP**: `000000` — differs from web (web uses any 6 random digits)

## Prefilling `defaultBillingDetails` (iOS / Android / React Native)

| Platform | Code |
| --- | --- |
| iOS | `configuration.defaultBillingDetails.name/email/phone = "..."` |
| Android | `PaymentSheet.BillingDetails(name, email, phone)` in `PaymentSheet.Configuration(...)` |
| React Native | `initPaymentSheet({ defaultBillingDetails: { name, email, phone } })` |

## CDN Assets

- `raw/assets/stripe-link-in-ios.png` — Link in iOS Mobile Payment Element (248 KB)

## Related Pages

- [[stripe-link]] — Link concept page (Mobile Payment Element section)
- [[source-stripe-payment-element-link]] — Link in web Payment Element
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-mobile-payment-element-link-2025]] — verbatim webpage content (77 lines)
