---
title: "Stripe Currencies"
type: concept
category: technology
tags: [stripe, currencies, presentment, settlement, minor-units, zero-decimal, isk, huf, twd, ugx, eea, amex]
---

## Definition

Stripe supports 135+ currencies for charges; settlements paid out in your preferred currency. Three distinct currency concepts apply to every payment: payment method currency, presentment currency, and settlement currency.

## Three Currency Concepts

| Currency | What it is |
| --- | --- |
| **Payment method currency** | Card/bank account currency (issuer-set) |
| **Presentment currency** | Currency of the charge you create |
| **Settlement currency** | Currency your bank account receives |

If presentment ≠ payment method currency → issuer may charge customer FX fee.
If presentment ≠ settlement currency → Stripe converts (see Stripe pricing for conversion costs).

## API Amount Formatting

All API `amount` values must be in the **currency's smallest unit** (minor units), no decimals.

- Two-decimal currency: `1000` = 10 USD
- Zero-decimal currency: `10` = 10 JPY

**American Express**: doesn't support currencies marked with `*` in Stripe's presentment currency list.

## Special Currency Rules

| Currency | Rule |
| --- | --- |
| **ISK** (Icelandic Króna) | Zero-decimal, but API requires two-decimal with `00` cents: 5 ISK = `500` |
| **HUF** (Hungarian Forint) | Two-decimal for charges; zero-decimal for payouts — payout `amount` must be divisible by 100 |
| **TWD** (New Taiwan Dollar) | Same as HUF — two-decimal charges, zero-decimal payouts divisible by 100 |
| **UGX** (Ugandan Shilling) | Zero-decimal, but API requires two-decimal with `00` cents: 5 UGX = `500` |

## Minimum Charge Amounts (Key Currencies)

0.50 USD / 0.30 GBP / 0.50 EUR / 0.50 AUD / 0.50 CAD / 0.50 CHF / 50 JPY / 50 KRW / 175 HUF / 0.50 SGD / 2.00 MYR / 4.00 HKD

Note: iDEAL allows `amount` as low as `1`.

## Maximum Charge Amounts

- **8 digits** for most currencies: max 999,999.99 (e.g., `99999999`)
- **12 digits**: IDR, LBP
- **10 digits**: COP, HUF, JPY (card only)
- **9 digits**: INR, IDR+Amex

JCB/Diners/Discover from Japan: 8 digit max (99,999,999 JPY) regardless.

## EEA Cards

Cards from 44 EEA countries (EU + UK, Iceland, Norway, Liechtenstein + others) may incur different cross-border fees. Türkiye and UK are included in Stripe's EEA definition.

## Sources

- [[source-stripe-currencies]] — primary: API formatting, special cases (ISK/HUF/TWD/UGX), min/max charge amounts, EEA card list, Connect FX
