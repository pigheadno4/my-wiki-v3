---
title: "Stripe: Multibanco Payments"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-multibanco-2025.md"
tags: [stripe, vouchers, multibanco, portugal, eur, online-banking, atm, connect, billing]
---

## Summary

Overview of Stripe's Multibanco integration — Portugal-only voucher paid via online banking or ATM. Delayed confirmation (bank transfer, can take several days especially over weekends). 365-day refunds (1-day to customer). €0.50–€99,999. `send_invoice` only for billing.

## Key Details

**API enum**: `multibanco`. EUR only. Portugal customers only.

**33 merchant countries** — Europe + US (includes Gibraltar/GI).

**Two payment flows**: online banking (entity + reference → log into bank → pay) and ATM (entity + reference → pay at ATM).

**Confirmation delay**: several days, especially over weekends (bank transfer-based — unlike Konbini's instant confirmation).

**Amount limits**: €0.50 – €99,999.

**Refunds**: 365-day window. Typically 1 day to customer bank account. `destination_details.multibanco.reference` provides refund identifier.

**No disputes** (customer pushes funds; no chargeback risk).

**Billing**: `send_invoice` only. No recurring. Capability: `multibanco_payments`.

**Connect**: Direct, Destination, Separate charges and transfers. Standard (no invite required).

## Raw Sources

- [[stripe-multibanco-2025]] — verbatim webpage content (199 lines); fixed `*invoices*` ×1, `*subscriptions*` ×1; 7 SVG flow diagrams downloaded to assets/
