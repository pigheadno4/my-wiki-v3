---
title: "Stripe Docs — Authenticate with 3D Secure"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-3d-secure-authentication-flow-2025.md"
tags: [stripe, 3d-secure, 3ds2, sca, payment-intents, liability-shift, radar, ios, android, react-native]
---

## Summary

Comprehensive 3D Secure integration guide covering Web, iOS, Android, and React Native. Includes PaymentIntent flow, manual API triggering, web display options (popup/redirect/iframe), mobile SDK integration, test cards, and liability shift rules.

## Key Facts

- **3DS1 deprecated** — use Payment Intents/Setup Intents for 3DS2
- **Platforms**: Web, iOS, Android, React Native; also standalone 3DS for other PSPs
- **Automatic triggers**: SCA (EU), Japan guidelines, issuer soft decline, Stripe optimizations, Radar rules
- **Manual**: `payment_method_options[card][request_three_d_secure]: 'any' | 'challenge'`
- **PaymentSheet handles 3DS automatically** on iOS/Android/RN — no additional work

## Notable Details

- **Iframe**: no `sandbox` attribute; `postMessage('3DS-authentication-complete')` back to parent; sizes 250×400 / 390×400 / 500×600 / 600×400 / fullscreen
- **Mobile timeout**: ≥ 5 minutes required (compliance)
- **Liability shift**: must respond to dispute inquiries on 3DS payments or risk "no-reply" chargeback
- **ECI**: returned in `three_d_secure.electronic_commerce_indicator` on Charge

## CDN Assets (10 screenshots)

- Web: `stripe-3ds-checkout-page.png`, `stripe-3ds-frictionless-flow.png`, `stripe-3ds-challenge-flow.png`
- iOS: `stripe-3ds-ios-checkout.png`, `stripe-3ds-ios-loading.png`, `stripe-3ds-ios-otp.png`, `stripe-3ds-ios-customization.png`
- Android: `stripe-3ds-android-confirm.png`, `stripe-3ds-android-processing.png`, `stripe-3ds-android-otp.png`

## Related Pages

- [[stripe-3d-secure]] — 3D Secure concept page
- [[stripe-authorization-boost]] — includes recommendations on 3DS reduction
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-3d-secure-authentication-flow-2025]] — verbatim webpage content (566 lines; deprecation notice bullets reformatted by linter)
