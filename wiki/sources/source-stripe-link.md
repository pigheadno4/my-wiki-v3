---
title: "Stripe: Link"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-link-2025.md"
tags: [stripe, wallets, link, digital-wallet, instant-bank-payments, klarna, card-wallet, manual-capture, recurring]
---

## Summary

Overview of Stripe's Link digital wallet. Two integration paths produce different PaymentMethod types. Instant Bank Payments available exclusively through Link. Payment Element not supported in Thailand or Brazil. Manual capture and recurring supported.

## Key Details

**API enum**: `link` (as payment method path) or `card` + `card.wallet.type: 'link'` (card-specific path).

**Two integration paths**:
1. **Link as payment method** (recommended): PaymentMethod type = `link`, no `wallet` hash. Works with dynamic payment methods, no extra config
2. **Link within card-specific integration**: PaymentMethod type = `card`, `card.wallet.type = 'link'`. Use when you need card brand/last 4

**Funding methods**: cards, US bank accounts, Instant Bank Payments (Link-exclusive — lower cost than cards), Klarna, BNPLs.

**Immediate confirmation** regardless of funding method. Settlement same timeline as cards.

**Not supported in Payment Element** in Thailand or Brazil.

**Manual capture**: Yes. **Recurring**: Yes. **Disputes**: Yes (process varies by funding method).

**Refunds**: 5-10 business days depending on bank.

## Related Pages

- [[stripe-link]] — Link concept page

## Raw Sources

- [[stripe-link-2025]] — verbatim webpage content (109 lines); fixed `*Link*` ×1 (line-start pattern)
