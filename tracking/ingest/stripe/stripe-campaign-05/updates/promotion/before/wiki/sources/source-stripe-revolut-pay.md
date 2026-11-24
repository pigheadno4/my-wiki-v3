---
title: "Stripe: Revolut Pay Payments"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-revolut-pay-2025.md"
tags: [stripe, wallets, revolut-pay, uk, eu, gbp, eur, ron, huf, pln, dkk, recurring, disputes, manual-capture]
---

## Summary

Overview of Stripe's Revolut Pay integration — UK and EU digital wallet with redirect-based authentication. Supports recurring, Connect, disputes, and manual capture. Non-Revolut customers can save details after first purchase.

## Key Details

**API enum**: `revolut_pay`. UK and EU customers. 30 merchant countries.

**Currencies**: EUR, GBP, RON, HUF, PLN, DKK. Default: GBP (UK), EUR (EU).

**Non-Revolut customers**: can save details after first purchase for future use.

**Full feature set**: recurring ✓, Connect ✓, disputes ✓, manual capture ✓, refunds ✓.

**Product support**: Connect, Checkout, Payment Links, Elements, Subscriptions, Invoicing.

**Refunds**: full + partial, 180-day window, async up to 5 minutes.

**Disputes**: 120-day customer window. Evidence: 14-day submission. Revolut decision: within 35 days. Revolut's Buyer Protection Policy applies. Evidence types: return confirmation, tracking ID, shipping date, IP address/email receipt, phone/proof of receipt.

**Merchant countries** (30): AT, BE, BG, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK.

## Raw Sources

- [[stripe-revolut-pay-2025]] — verbatim hub page (154 lines); 1 italic fix (_webhook_); .mp4 video downloaded to assets/stripe-revolut-pay-flow.mp4
