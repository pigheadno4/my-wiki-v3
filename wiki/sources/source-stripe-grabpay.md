---
title: "Stripe: GrabPay Payments"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-grabpay-2025.md"
tags: [stripe, wallets, grabpay, singapore, malaysia, sgd, myr, redirect, otp, branding]
---

## Summary

Overview of Stripe's GrabPay integration — Singapore and Malaysia digital wallet with stored balance. OTP redirect-based authentication. No recurring, no manual capture, no disputes. 90-day refunds. Must follow GrabPay branding guidelines.

## Key Details

**API enum**: `grabpay`. SGD (SG) and MYR (MY) only. Singapore and Malaysia customers and merchants only.

**Redirect flow**: OTP authentication on GrabPay's website → redirect back to merchant site.

**No recurring payments. No manual capture. No disputes** (OTP auth prevents chargebacks).

**Refunds**: 90-day window. Async, up to 5 minutes. No partial refund noted (but Yes/Yes listed in properties).

**Invoicing**: supported. **Subscriptions**: not listed.

**Branding guidelines**: GrabPay provides mandatory brand assets — PDF guidelines and logos/buttons zip download available from CloudFront. Must follow when building checkout UI.

**2 merchant countries** (MY, SG) — narrower than most wallets.

## Raw Sources

- [[stripe-grabpay-2025]] — verbatim webpage content (106 lines); fixed `*webhook*` ×1; 1 .mp4 video + 1 .pdf + 1 .zip not downloaded
