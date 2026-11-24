---
title: "Stripe: Wero Payments"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-wero-2025.md"
tags: [stripe, wero, germany, eur, bank-redirect, authenticated]
---

## Summary

Overview page for Wero, a pan-European authenticated bank transfer method available to German customers. Distinct from [[stripe-ideal]] (iDEAL|Wero), which is the Netherlands iDEAL method rebranding to Wero infrastructure.

## Key Details

- **Customer geography**: Germany only (currently)
- **Business geography**: 30 European countries (AT, BE, BG, CY, CZ, DE, DK, EE, ES, FI, FR, GR, HR, HU, IE, IS, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK)
- **Currency**: EUR only; min 0.50 EUR; max varies by customer's bank limits
- **Flow**: redirect → QR code scan → Wero App approval → redirect back; completes under 10 seconds
- **No recurring, no disputes, no manual capture**
- **Refunds**: full + partial; up to 2 years; multiple partial refunds allowed
- **Product support**: Connect, Checkout (payment mode only — not subscription/setup), Payment Links, Elements (ECE not supported)
- **Onboarding**: interest form required (not self-serve)

## Raw Sources

- [[stripe-wero-2025]] — verbatim webpage content (125 lines, overview + payment flow + refunds + limits)
