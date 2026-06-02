---
title: "PayPal Expanded Checkout: 3D Secure Authentication"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-3d-secure.md"
tags: [paypal, expanded-checkout, 3d-secure, sca, fraud, chargeback, liability-shift, psd2, eligibility, card-brands, countries]
---

## PayPal Expanded Checkout: 3D Secure Authentication

Official reference for PayPal's 3D Secure integration — how it works, eligibility by country/card brand/currency, and the liability shift benefit.

Source URL: <https://developer.paypal.com/docs/checkout/advanced/customize/3d-secure/>

Last updated: 2025-06-25

## Key Takeaways

### What 3D Secure does

- Authenticates the cardholder through their card issuer
- Reduces fraud likelihood on supported cards
- **Shifts chargeback liability** from merchant to card issuer on successful authentication
- Only triggered if the card is enrolled for 3D Secure

### Buyer experience

Buyer is prompted by their card-issuing bank to complete an additional step: one-time password or static password (implementation-dependent).

### Eligibility — 36 countries, 22 currencies

Most countries support the same full set of 22 currencies. Notable exceptions:

| Country | Card brand restriction | Currency restriction |
| ------- | ---------------------- | ------------------- |
| Mexico (MX) | Mastercard, Visa, Amex | **MXN only** (not multi-currency) |
| Canada (CA) | Amex: CAD and USD only; JCB: CAD only | Full currency set |
| Japan (JP) | Amex: JPY only; JCB: JPY only | Full currency set |
| Hong Kong (HK) | Mastercard, Visa only (no Amex) | Full currency set |
| Singapore (SG) | Mastercard, Visa only (no Amex) | Full currency set |
| France (FR) | + Carte Bancaire (EUR only) | Full currency set |
| Australia (AU) | + eftpos (AUD only) | Full currency set |
| United States (US) | + Discover, debit networks (Star/Pulse/Nyce/Accel), CUP, JCB, Diners — all USD only | Full currency set |

### Covered countries (36 total)

All EU member states plus: AU, CA, HK, JP, MX, NO, SG, GB, US, LI (Liechtenstein), LV, LT (Baltic states)

**Not covered**: Most of Asia-Pacific, Latin America (except MX), Africa, Middle East

### Currency footnotes

- JPY (⁰) and TWD (⁰) are 0-digit denomination currencies — no decimal places

## Raw Sources

- [[paypal-expanded-checkout-3d-secure]] — verbatim webpage content with full eligibility table (demo GIF CDN-restricted, not saved)

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout concept page
- [[source-paypal-expanded-checkout-integrate]] — 3DS integration code (SCA_ALWAYS / SCA_WHEN_REQUIRED)
- [[source-paypal-android-card-payments]] — Android SCA options
- [[source-paypal-ios-card-payments]] — iOS SCA options
- [[source-paypal-expanded-checkout-customize-overview]] — full customization catalog
