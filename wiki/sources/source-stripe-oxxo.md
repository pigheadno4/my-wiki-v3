---
title: "Stripe: OXXO Payments"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-oxxo-2025.md"
tags: [stripe, vouchers, oxxo, mexico, mxn, cash, convenience-store, connect]
---

## Summary

Overview of Stripe's OXXO integration — Mexico-only cash voucher paid at OXXO convenience stores. Next business day confirmation + settled funds. 10–10,000 MXN. No refunds. No subscriptions/invoicing. 4 unsupported business categories.

## Key Details

**API enum**: `oxxo`. MXN only. Mexico customers and merchants only (MX accounts only).

**OXXO stores** — Latin America's largest convenience store chain.

**Payment confirmation**: next business day (with settled funds included).

**Amount limits**: 10.00 MXN – 10,000.00 MXN (lower ceiling than Boleto's 49,999.99 BRL).

**No refunds** — must create separate customer credit process.

**No disputes** — cash in-person; no chargeback risk.

**No subscriptions, no invoicing** — most limited billing support of the 4 voucher methods.

**Connect**: Yes (standard, no invite required).

**Unsupported categories** (4): Direct Marketing - Other, Direct Marketing - Subscription, Gift/Card/Novelty/Souvenir Shops, Service Stations.

## Raw Sources

- [[stripe-oxxo-2025]] — verbatim webpage content (117 lines); no italic fixes; 4 SVG flow diagrams downloaded to assets/
