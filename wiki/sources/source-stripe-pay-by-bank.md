---
title: "Stripe: Pay by Bank Payments"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-pay-by-bank-2025.md"
tags: [stripe, real-time-payments, pay-by-bank, open-banking, uk, europe, eur, gbp, connect]
---

## Summary

Overview of Stripe's Pay by Bank — an open-banking-based real-time payment method for UK and Europe. Customer selects bank, approves in banking app or web portal. No disputes, 730-day refunds, Connect supported.

## Key Details

**Customer locations**: Finland, France, Germany, Ireland, United Kingdom. France/Germany/Ireland in **private preview**; UK generally available.

**API capability**: `pay_by_bank_payments`. EUR and GBP only.

**Transaction limits**: £0.50–£10,000 GBP default. Higher amounts require contacting Stripe support.

**No disputes** — customer must authenticate in banking app; no chargeback process.

**Refunds**: 730-day (2-year) window. Partial refunds supported. Free of charge; processing fees non-refundable.

**No manual capture. No recurring payments.**

**Connect**: Yes — Direct, Destination, Separate charges and transfers.

**Product support**: Connect, Payment Links, Checkout (not subscription mode), Elements — but Express Checkout Element and Mobile Payment Element do **not** support Pay by Bank.

**35 merchant countries** — AT, AU, BE, BG, CA, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SG, SI, SK, US.

**Payment flow**: customer selects Pay by Bank → chooses bank → redirected to bank → enters credentials → completes authorization → notified payment complete → returns to merchant site.

## Raw Sources

- [[stripe-pay-by-bank-2025]] — verbatim webpage content (166 lines); fixed `*webhook*` ×1; 6 SVG flow diagrams downloaded to assets/
