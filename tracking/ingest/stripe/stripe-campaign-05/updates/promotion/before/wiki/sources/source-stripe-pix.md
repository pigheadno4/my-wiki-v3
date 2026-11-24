---
title: "Stripe: Pix Payments"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-pix-2025.md"
tags: [stripe, real-time-payments, pix, brazil, brl, qr-code, iof, ebanx, recurring, pix-automatico, connect, disputes]
---

## Summary

Overview of Stripe's Pix integration — Brazil's real-time payment system (Central Bank of Brazil). QR code or Pix string. Processed via Ebanx. Supports one-time and recurring (Pix Automático). IOF tax applies to international transactions. Disputes supported but non-challengeable.

## Key Details

**API enum**: `pix`. BRL currency. Brazil customers only.

**Partner**: Ebanx handles processing, receipts, and IOF collection/remittance for Stripe.

**Business locations**: 35 international countries (settlement in USD/EUR/GBP/CAD/AUD/SGD) + BR accounts (invite only, one-time only, BRL settlement). Pix Automático not available for BR accounts.

**Transaction limits**: min 0.50 BRL, max 3,000 USD per payment. Recurring capped at mandate amount. Single buyer cap: 10,000 USD/month per business.

**Refunds**: 90-day window. Reflected within minutes.

**Disputes**: Limited circumstances (fraud, account takeover). Non-challengeable — funds removed from Stripe balance automatically.

**IOF tax** (Brazilian foreign exchange tax on international transactions): 3.5% rate.
- `amount_includes_iof: never` (default) — customer pays; amount marked up 3.5% in banking app
- `amount_includes_iof: always` — merchant absorbs; IOF deducted from settlement
- API users must show Ebanx T&C disclosures and IOF language (bilingual templates provided)
- Checkout/Elements: Stripe handles disclosures automatically

**Statement descriptor**: ignored — Ebanx shown as recipient. Merchant name in `identifier` field only.

**Customer emails**: Ebanx sends receipts by default (can disable). Completion reminder emails with QR code disabled by default (can enable). Both configurable in Dashboard Customer emails settings.

**Recurring**: via **Pix Automático** (separate sub-product; see separate source when ingested).

**Prohibited categories**: crypto businesses, insurance companies, telehealth/medicine vendors, non-profits/charities.

**Connect**: Direct, Destination, Separate charges and transfers. Availability is MoR-sensitive — if connected account is MoR, connected account must be in supported country; if platform is MoR, platform must be in supported country. Capability: `pix_payments`.

**Product support**: Connect, Payment Links, Checkout (subscription mode → use Pix Automático), Elements.

## Raw Sources

- [[stripe-pix-2025]] — verbatim webpage content (243 lines); fixed `*Connect*` ×1; 4 SVG flow diagrams downloaded to assets/
