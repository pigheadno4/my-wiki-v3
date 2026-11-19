---
title: "Stripe: Bizum Payments"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-bizum-2025.md"
tags: [stripe, real-time, bizum, spain, eur, phone-authentication]
---

## Summary

Overview of Bizum — a Spanish real-time payment method using phone-number authentication via the buyer's bank app. No Connect. No manual capture. Notable for the longest refund window (395 days) and longest merchant evidence window (40 days) of any reviewed payment method.

## Key Details

**Real-time payment** — Spain customers only, EUR only. **No Connect**. **No manual capture**. 28 merchant countries (all EUR).

**Authentication**: buyer enters Bizum-registered phone number → approves in bank app.

**Transaction limits**: min €0.50, max €5,000.

**Onboarding requirements**: must provide tax ID (companies) or national ID (DNI/NIE for Spain, or country equivalent). Must set `business_type`. Capability stays `pending` until verified.

**Disputes**: 120-day customer window; **40-day** merchant evidence window (longest of any method reviewed); 90-day Bizum decision.

**Refunds**: **395-day** window (longest of any payment method reviewed); async (up to 5 min).

**Prohibited**: gambling, crypto, jewelry/precious metals, financial institutions, political/religious organizations, charities, timeshares.

## Raw Sources

- [[stripe-bizum-2025]] — verbatim webpage content (197 lines); fixed `_before_` + `_webhook_` → `*italic*`
