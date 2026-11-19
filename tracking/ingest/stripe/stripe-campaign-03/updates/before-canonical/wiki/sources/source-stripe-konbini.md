---
title: "Stripe: Konbini Payments"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-konbini-2025.md"
tags: [stripe, vouchers, konbini, japan, jpy, cash, convenience-store, connect, billing, prohibited-categories]
---

## Summary

Overview of Stripe's Konbini integration — Japan-only cash voucher paid at FamilyMart, Lawson, Ministop, and Seicomart. Instant payment confirmation, T+4 payout. 120–300,000 JPY. Restricted Connect. Extensive prohibited category list (19+). `send_invoice` only for billing.

## Key Details

**API enum**: `konbini`. JPY only. Japan customers and merchants only (JP accounts only).

**Stores**: FamilyMart, Lawson, Ministop, Seicomart.

**Payment confirmation**: Instant. **Payout**: T+4 business days.

**Amount limits**: 120 JPY – 300,000 JPY.

**Refunds**: Yes/Yes — customer must provide bank account info; Stripe emails to request, then auto-processes.

**Billing**: `send_invoice` only — no `charge_automatically` (in-person nature precludes auto-debit).

**Connect**: Partial — requires invite for `on_behalf_of` charges. No Customer Portal support.

**Extensive prohibited categories** (19+): sole proprietors under 3 years, RMT (sale of in-game characters/currency), gambling, information selling (money-making schemes, investment tips, gambling strategies), MLM/pyramid schemes, gore, unscientific/superstition content, prohibited medical products, content offensive to public order, personal import facilitation, foreign money transfer, loans, dating sites, e-cigarettes/vaping, fortune-telling. Financial partner and convenience stores may also reject at their discretion.

## Raw Sources

- [[stripe-konbini-2025]] — verbatim webpage content (156 lines); fixed `*payout*` ×1, `*subscriptions*` ×1, `*invoices*` ×1; 4 SVG flow diagrams downloaded to assets/
