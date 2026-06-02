---
title: "Stripe: Cash App Pay Payments"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-cash-app-pay-2025.md"
tags: [stripe, wallets, cash-app-pay, us, usd, manual-capture, disputes, off-session-liability, connect, cloning]
---

## Summary

Overview of Cash App Pay — US-only digital wallet with mobile redirect or desktop QR code flows. USD only. Manual capture supported. Two-tier dispute liability (on-session: Cash App bears; off-session: merchant bears). PaymentMethod cannot be cloned across connected accounts.

## Key Details

**API enum**: `cashapp`. USD only. US customers only (excluding US territories).

**Two payment flows**: mobile redirect (auto-authenticated in Cash App app) or desktop QR code scan.

**Payment limits**: no business-level limit; customer-level variable limits. Recommend below $2,000 to reduce declines. Cannot split balance + debit card for same order.

**Funding**: Cash App balance preferred (if covers full amount), otherwise linked debit card.

**Manual capture**: Yes (alongside Amazon Pay, among the few wallets supporting this).

**Refunds**: 90-day, async, to original form of payment.

**Dispute liability (two-tier)**:
- **On-session**: Cash App bears fraud liability
- **Off-session (saved PM)**: **merchant bears fraud liability**
- 120-day dispute window, 13-day evidence submission, 58-day decision

**Statement descriptor**: `CashApp*` prefix + company name. Dynamic descriptor visible in Cash App app only (not external statements).

**Prohibited**: B2B, financial services, gift cards, fundraising/donations/alcohol platforms.

**Connect**: `cashapp_payments` capability. PaymentMethod **cannot be cloned** across connected accounts when connected account is business of record.

## Raw Sources

- [[stripe-cash-app-pay-2025]] — verbatim webpage content (197 lines); fixed `*webhook*` ×1, `*off-session*` ×1; 1 CloudFront .mp4 video not downloaded
