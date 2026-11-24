---
title: "Stripe: UPI Payments"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-upi-2025.md"
tags: [stripe, real-time-payments, upi, india, inr, qr-code, recurring, e-mandate, connect, disputes]
---

## Summary

Overview of Stripe's UPI integration — India's real-time payment system (NPCI). QR code on desktop, redirect on mobile. Supports one-time and recurring (UPI AutoPay / e-mandates). Disputes supported but non-contestable. 60-day refunds.

## Key Details

**API enum**: `upi`. INR only. India customers only.

**Payment flows**: Desktop → QR code scan; Mobile → redirect to UPI app.

**Recurring**: Yes — via UPI AutoPay / e-mandates. Customer authorizes mandate in UPI app.

**36 merchant countries** — same broad international list as Pix (AT, AU, BE, BG, CA, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SG, SI, SK, US).

**Transaction limits**: 1 INR – 100,000 INR. Recurring max: **15,000 INR**.

**Refunds**: 60-day window. Asynchronous — up to 7 business days. Via `refund.updated`/`refund.failed`. Non-recoverable on failure.

**Disputes**: Supported but **non-contestable** — if bank/PSP accepts dispute, funds removed from Stripe balance immediately.

**Billing**: Invoicing, Payment Links, Subscriptions (no `send_invoice` restriction mentioned — likely supports `charge_automatically` via e-mandate).

**Connect**: Yes. No capability name stated in overview.

**No pricing listed**. No "beta" label in source page (concept page had noted UPI as in beta — appears to have graduated).

## Raw Sources

- [[stripe-upi-2025]] — verbatim webpage content (123 lines); fixed `*webhook*` ×1
