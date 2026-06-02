---
title: "Stripe: Amazon Pay Payments"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-amazon-pay-2025.md"
tags: [stripe, wallets, amazon-pay, worldwide, multi-currency, manual-capture, disputes, recurring, sepa, a-to-z-guarantee]
---

## Summary

Overview of Stripe's Amazon Pay integration. Worldwide customers, 12 currencies, 17 European+US merchant countries. 240-day dispute window (longest reviewed). Manual capture supported. Full subscriptions. Stores Amazon account payment methods including SEPA Direct Debit (EU) and installment options (US).

## Key Details

**API enum**: `amazon_pay`. Worldwide customers. Redirect to Amazon for checkout.

**12 currencies**: USD, AUD, GBP, DKK, EUR, HKD, JPY, NZD, NOK, ZAR, SEK, CHF (any currency available to all countries except US).

**17 merchant countries**: US + 16 European (AT, BE, CH, CY, DE, DK, ES, FR, GB, HU, IE, IT, LU, NL, PT, SE).

**Disputes: Yes** — **240-day** customer window (longest of any payment method reviewed). 10-day evidence submission, 90-day Amazon decision. A-to-z Guarantee claims (`dispute_type = claim`) don't incur dispute fees.

**Manual capture: Yes** — unique among reviewed wallets.

**Refunds**: 90-day, async. Non-card payment method refunds can take up to **14 calendar days**.

**Recurring**: Yes — full subscriptions and invoicing (no invite required).

**Connect**: Yes (full, no restrictions).

**Alternative payment methods stored in Amazon Pay**:
- US: Amazon Store Card, Installments, Visa Installments, Citi Flex Pay, Affirm, Shop with Points
- EU: SEPA Direct Debit

## Raw Sources

- [[stripe-amazon-pay-2025]] — verbatim webpage content (151 lines); fixed `*webhook*` ×1; 1 CloudFront .mp4 video not downloaded
