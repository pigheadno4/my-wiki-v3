---
title: "Stripe — Advanced Fraud Detection"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-disputes-advanced-fraud-detection-2026.md"
tags: [stripe, radar, fraud, stripe-js, advanced-fraud-detection, device-fingerprint, hcaptcha, mobile-sdk]
---

## Summary

Advanced fraud detection via Stripe.js and mobile SDKs: device characteristics + activity indicators power Radar. >$500M/month in fraud prevented. Privacy-preserving and session-scoped.

## Two Risk Factor Types

**Device characteristics**: browser, screen, device configs → identifies anomalous environments inconsistent with real users.

**Activity indicators**: mouse movement, time-on-page, copy-paste detection → distinguishes bots from humans. Scoped to single session on single site — not linked across sessions, sites, or apps. Page contents only collected if matching Stripe Elements input fields.

## Key Points

- Include Stripe.js on **every page** (not just checkout) for richest signal set
- hCaptcha loaded per page via Stripe.js (opt out via Stripe Support)
- Stripe prevents >$500M/month in payment fraud
- Not used for advertising; strict internal access control; retained only as long as useful for fraud detection
- Mobile SDKs: collect at SDK instantiation; transmit only during tokenization

## Disable Advanced Fraud Detection (increases fraud risk)

| Platform | Minimum version | Code |
| --- | --- | --- |
| Stripe.js (ES module) | Latest | `loadStripe.setLoadParameters({advancedFraudSignals: false})` |
| iOS SDK | v19.1.1+ | `StripeAPI.setAdvancedFraudSignalsEnabled(false)` |
| Android SDK | v14.4.0+ | `Stripe.advancedFraudSignalsEnabled = false` (before any SDK instantiation) |

**Cannot disable**: events from Stripe-managed Elements fields; 3DS2 device info (required by issuing banks).

## Related Pages

- [[stripe-radar]] — concept page (updated with advanced fraud detection details)
- [[source-stripe-radar-optimize-risk-factors]] — risk factor impact percentages

## Raw Sources

- [[stripe-disputes-advanced-fraud-detection-2026]] — verbatim advanced fraud detection guide
