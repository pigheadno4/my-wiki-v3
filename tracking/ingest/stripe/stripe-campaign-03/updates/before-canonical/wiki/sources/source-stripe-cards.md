---
title: "Stripe: Cards"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-cards-2025.md"
tags: [stripe, cards, card-brands, 3d-secure, sca, cartes-bancaires, interac, eftpos]
---

## Summary

Comprehensive guide to card payment acceptance with Stripe, including supported brands, geographic restrictions, 3DS/SCA requirements, and regional nuances.

## Key Details

**Default brands** (no extra config): Amex, CUP, Discover/Diners, eftpos AU, JCB, Mastercard, Visa.

**Extra config required**: Cartes Bancaires, Interac.

**Online brand capabilities**:

| Brand | Account Country | 3DS | Wallets |
| --- | --- | --- | --- |
| Visa/MC | All | ✓ | ✓ |
| Amex | All except BR/MY/TH/UAE | ✓ | ✓ |
| Discover/Diners | US/CA/JP/UK + most EEA | ✓ | ✓ |
| CUP | AU/CA/HK/MY/NZ/SG/UK/US/CH/most EEA | ✓ | ✗ |
| JCB | Similar to CUP | Some countries only | ✓ |
| Cartes Bancaires | SEPA + select others | ✓ | Apple Pay only |
| eftpos | Australia only | ✓ | ✗ |

**Exclude brands**: Radar rule or client-side brand check.

**SCA/3DS**: required in Europe (PSD2, Sept 14 2019) and India. Default in Checkout/Payment Links/Hosted Invoice. Configurable via PaymentIntents/SetupIntents/Elements/Mobile SDKs.

**EU co-badged cards**: must offer card brand choice (e.g. Cartes Bancaires + Visa/MC).

**India**: RBI-specific regulations — see India FAQs for details.

**Cards fund other methods**: Link and digital wallets use card as underlying funding source.

## Raw Sources

- [[stripe-cards-2025]] — verbatim webpage content (brand capabilities table, geographic sections)
