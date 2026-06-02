---
title: "PayPal Expanded Checkout: Eligibility"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-eligibility.md"
tags: [paypal, expanded-checkout, eligibility, countries, currencies, card-brands, payment-methods, apm, psd2, 3ds]
---

## PayPal Expanded Checkout: Eligibility

Comprehensive reference for countries, currencies, card brands, and payment methods supported by Expanded Checkout (37 countries, 22 currencies, 21 payment methods).

Source URL: <https://developer.paypal.com/docs/checkout/advanced/eligibility/>

Last updated: 2025-08-07

## Key Takeaways

### Coverage

- **37 countries**, **22 currencies**
- All countries except Mexico support all 22 currencies; Mexico supports MXN only
- JPY and TWD are zero-digit currencies (no decimal places)

### Card brand highlights by country

| Country | Notable card-brand restrictions |
| ------- | ------------------------------- |
| **US** | Widest: MC, Visa, Amex, Discover, Debit networks (Star/Pulse/Nyce/Accel), CUP, JCB, Diners — all USD only for non-MC/Visa |
| **AU** | + eftpos (AUD only) |
| **FR** | + Carte Bancaire (EUR only) |
| **CA** | Amex = CAD + USD only; JCB = CAD only |
| **JP** | Amex = 16 currencies only (no ILS, MXN, PHP, THB, TWD, BRL); JCB = JPY only; + Diners |
| **CN** | MC + Visa only |
| All others | MC, Visa, Amex — all 22 currencies |

### Payment methods — key refund and country notes

| Method | Type | Refunds | Key geography |
| ------ | ---- | ------- | ------------- |
| PayPal | Digital wallet | Yes | Global |
| Venmo | Digital wallet | Yes | US only |
| Pay Later | Loan | Yes | AU, FR, DE, IT, ES, UK, US |
| PayPal Credit | Revolving credit | Yes | US + UK |
| Apple Pay | Push payment | Up to 180 days | See Apple Pay docs |
| Google Pay | Push payment | Up to 180 days | See Google Pay docs |
| Trustly | Bank redirect | **Up to 365 days** | AT, DE, DK, EE, ES, FI, GB, LT, LV, NL, NO, SE |
| Multibanco | Voucher | **No refunds** | Buyer: PT only |
| Bancontact | Bank redirect | 180 days | Buyer: BE only |
| BLIK / Przelewy24 | Bank redirect | 180 days | Buyer: PL only |
| iDEAL | Bank redirect | 180 days | Buyer: NL only |
| eps | Bank redirect | 180 days | Buyer: AT only |
| MyBank | Bank redirect | 180 days | Buyer: IT only |
| Pay upon Invoice | Deferred | 180 days | Buyer: DE only |
| giropay | Bank redirect | ~~Sunset June 30, 2024~~ | Buyer: DE only |
| Sofort | Bank redirect | ~~Sunset April 18, 2024~~ | Buyer: AT/BE/DE/NL/ES/UK |

### Sunset APMs

> **giropay** — sunset July 1, 2024. No longer supported.
> **Sofort** — sunset April 19, 2024. No longer supported.

Both were German/European bank redirect methods. Replace with PayPal wallet or other APMs.

### PSD2 / 3DS requirement

European merchants subject to PSD2 must:

1. Include 3D Secure in their integration
2. Pass the cardholder's billing address in the transaction

### APM buyer-country pattern

Most APMs (Bancontact, BLIK, eps, iDEAL, etc.) follow the same pattern:
- **Buyer country**: one specific country
- **Merchant country**: all PayPal-supported countries except Brazil, Russia, Japan

## Raw Sources

- [[paypal-expanded-checkout-eligibility]] — verbatim webpage content with full 37-country card brand/currency table and 21-method payment table

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout concept page
- [[source-paypal-expanded-checkout-3d-secure]] — 3DS details (required for PSD2/Europe)
- [[source-paypal-expanded-checkout-getting-started]] — Expanded Checkout getting started guide
