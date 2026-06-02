---
title: "Stripe: iDEAL | Wero Payments"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-ideal-2025.md"
tags: [stripe, ideal, wero, netherlands, eur, bank-redirect, authenticated, sepa-debit, kvk]
---

## Summary

Reference page for iDEAL | Wero on Stripe. Netherlands-only, EUR, customer-initiated with 2FA bank auth. Currently migrating from iDEAL to Wero (Q1 2026 rebrand; full switch 2026–2027). No disputes, 180-day refunds, recurring via SEPA Direct Debit. KVK number website requirement for NL businesses.

## Key Details

- **Migration**: iDEAL → Wero; rebrand to "iDEAL | Wero" by Q1 2026; fully switch to Wero in 2026–2027
- **Currency**: EUR; **Customers**: Netherlands; **Business**: 40 countries
- **Recurring**: via [[stripe-sepa-debit]] — same pattern as Bancontact
- **No disputes**: customers can't dispute with bank
- **Refunds**: 180 days; up to 7 days pending; after 7 days without failure signal → considered successful
- **KVK requirement**: NL-based businesses must display KVK (Chamber of Commerce) number; others must show equivalent local registration number
- **Connect**: connected account name must match actual business (not platform) — regulatory compliance

## Raw Sources

- [[stripe-ideal-2025]] — verbatim webpage content; MP4 demo video kept as external URL
