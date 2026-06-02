---
title: "Stripe: Swish Payments"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-swish-2025.md"
tags: [stripe, real-time-payments, swish, sweden, sek, redirect, qr-code, connect, merchant-of-record]
---

## Summary

Overview of Stripe's Swish integration — Sweden-only real-time payment method with two flows: mobile redirect (via Swish + BankID app) and desktop QR code scan. Stripe acts as merchant of record. 365-day refunds. No recurring/billing support. Extensive prohibited category list.

## Key Details

**API enum**: `swish`. SEK only. Sweden customers only.

**Two payment flows**:
- **Mobile**: redirect to Swish app → authorize with BankID → return to merchant site
- **Desktop**: QR code displayed on website → customer scans with Swish app

**Stripe as merchant of record** — unique: Stripe's name shown as payment recipient in Swish app and as statement descriptor on bank statements. Merchant name appears in message field only. Factoring addendum in Swish legal terms applies.

**27 merchant countries** — European focus (AT, BE, BG, CY, CZ, DE, DK, EE, ES, FI, FR, GR, HR, IE, IS, IT, LI, LT, LU, LV, NL, NO, PL, RO, SE, SI, SK). No US/AU/SG.

**Refunds**: 365-day window. Full and partial refunds. Multiple partials supported. Takes a few minutes.

**No disputes**. No recurring payments. No billing/invoicing/subscriptions support.

**Product support**: Connect, Checkout (not subscription/setup mode), Elements (not Express Checkout Element), Payment Links only.

**Prohibited categories**: Wine/Champagne producers, alcoholic beverage wholesalers, package liquor stores, pawn shops, art dealers, real estate rental agents, legal services/attorneys, precious metals/jewelry, digital wallet top-ups.

**Connect**: Direct, Destination, Separate charges and transfers.

## Raw Sources

- [[stripe-swish-2025]] — verbatim webpage content (164 lines); no italic fixes; 2 PNG flow diagrams downloaded from CloudFront to assets/
