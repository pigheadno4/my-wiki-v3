---
title: "Stripe Docs — Pix on Link"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-pix-on-link-2025.md"
tags: [stripe, link, pix, brazil, brl, us-only, ebanx, iof, real-time-payments]
---

## Summary

Guide for Pix as a Link payment method. US businesses can accept Pix (Brazilian real-time QR code payments) via Link with zero integration changes. Auto-enabled when Link is turned on.

## Key Facts

- **US businesses only** (despite serving Brazilian customers); BRL only
- **Supported integrations**: Payment Links, Stripe Checkout (Hosted), Payment Element only
- **Transaction limits**: 5 BRL – 3,000 USD equivalent in BRL
- **Payment types**: one-time and on-session only (no recurring)
- **Required buyer info**: name, address, tax identifier (at first checkout)

## Service Provider: Ebanx

- Statement descriptor shows **Ebanx** as payment recipient; business name appears in "Message to payor"
- Ebanx sends customer receipts on merchant's behalf (Brazilian receipt requirement)

## IOF Tax (Brazilian Currency Exchange Tax)

- **Rate**: 3.5% of transaction value
- **Who pays**: customer (marked-up amount shown in banking app)
- Stripe/Ebanx handle calculation, disclosures, and customer receipts automatically

## Payment Flow

**New customer**: select Pix → enter name/address/tax ID → Pay → receive QR code + Pix code → scan in banking app → authorize → redirect back

**Returning customer**: select Pix → Pay (saved details autofilled) → receive QR code → scan → authorize → redirect back

## Disputes

Low fraud risk (bank app authentication required); handled same as other Link payment methods.

## Related Pages

- [[stripe-link]] — Link concept page (Pix on Link section)
- [[source-stripe-pix-on-link]] — this source
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-pix-on-link-2025]] — verbatim webpage content (67 lines)
