---
title: "Stripe: Boleto Payments"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-boleto-2025.md"
tags: [stripe, vouchers, boleto, brazil, brl, cash, recurring, connect, subscriptions]
---

## Summary

Overview of Stripe's Boleto integration — Brazil's official cash voucher payment method regulated by the Central Bank of Brazil. No refunds. No customer disputes. 1-day confirmation, T+2 payout. 5–49,999.99 BRL limits. Supports subscriptions and Customer Portal.

## Key Details

**API enum**: `boleto`. BRL only. Brazil customers and merchants only (BR accounts only).

**Regulated** by the Central Bank of Brazil.

**Payment confirmation**: 1 business day. **Payout**: T+2 business days after confirmation.

**Amount limits**: 5.00 BRL – 49,999.99 BRL.

**No refunds** — must create separate process for customers. No exceptions.

**No disputes** (by customers) — bank-side irregularities can occur; Stripe handles those cases.

**Recurring**: Yes — full subscriptions and invoicing support (not `send_invoice`-only, unlike Konbini/Multibanco).

**SetupIntents**: Yes. **setup_future_usage**: Yes. **Customer Portal**: Yes.

**Product support**: Connect, Checkout, Payment Links, Elements (Express Checkout Element not supported), Subscriptions, Invoicing.

**Connect**: standard (no invite required, unlike Konbini).

## Raw Sources

- [[stripe-boleto-2025]] — verbatim webpage content (116 lines); no italic fixes; 4 SVG flow diagrams downloaded to assets/
