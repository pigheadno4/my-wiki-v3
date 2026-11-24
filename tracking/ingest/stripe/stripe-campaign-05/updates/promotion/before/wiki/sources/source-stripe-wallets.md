---
title: "Stripe: Wallets Overview"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-wallets-2025.md"
tags: [stripe, wallets, alipay, amazon-pay, apple-pay, cash-app, google-pay, grabpay, link, mb-way, mobilepay, paypal, paypay, revolut-pay, samsung-pay, satispay, stablecoins, vipps, wechat-pay]
---

## Summary

Hub page for Stripe's 17 wallet payment methods. Covers two wallet types (saved credential vs stored balance), subscription caveats, and product/API support matrices. Samsung Pay is Terminal-only; MoMo/GCash on waitlist.

## Key Details

**17 wallet methods**: Alipay, Amazon Pay, Apple Pay, Cash App Pay, Google Pay, GrabPay, Link, MB WAY, MobilePay, PayPal, PayPay, Revolut Pay, Samsung Pay, Satispay, Stablecoins/crypto, Vipps, WeChat Pay.

**Waitlist**: MoMo (Vietnam) and GCash (Philippines) — not yet available.

**Two wallet types**: (1) saved payment credential (tokenized card/bank); (2) stored wallet balance.

**Subscription caveats**: many wallets have limited recurring support — verify token/billing agreement creation, MIT support, card-update continuity, retry/dunning behavior before committing.

**Notable product support**:
- Samsung Pay: **Terminal only** — no online product support
- Apple Pay / Google Pay: no explicit API enum; not displayed for Indian IPs; Terminal supported
- Link: Payment Element doesn't support in Brazil or India
- Alipay: subscriptions/invoicing invite-only
- PayPay Connect: requires invite

**API support highlights** — SetupIntents + setup_future_usage supported by:
- Amazon Pay (`amazon_pay`), Cash App (`cashapp`), Link (`link`), PayPal (`paypal`), Revolut Pay (`revolut_pay`)

**Stablecoins/crypto** (`crypto`): SetupIntents invite-only; no manual capture; redirect required.

## Raw Sources

- [[stripe-wallets-2025]] — verbatim webpage content (113 lines); fixed `*subscriptions*` ×1, `*confirm*` ×1; 6 SVG flow diagrams downloaded to assets/
