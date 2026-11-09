---
title: "Stripe Currencies"
type: concept
category: technology
tags: [stripe, currencies, presentment, settlement, minor-units, zero-decimal, isk, huf, twd, ugx, eea, amex]
---

## Definition

Stripe supports 135+ currencies for charges; settlements paid out in your preferred currency. The guide describes payment method, presentment, and settlement currencies, and separately defines the integration currency set on a Price or PaymentIntent. That integration currency appears in the Dashboard and is used by Stripe Tax when recording tax liability in Stripe Tax reports. See [[source-stripe-currencies]] (https://docs.stripe.com/currencies; November capture `raw/stripe-currencies-2026-11-07.md:13-29`, May capture `raw/stripe-currencies-2025.md:12-24`).

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

**American Express**: asterisk-marked currencies are unsupported in every Stripe account country; an unmarked currency might still be unavailable for Amex in a particular account country. See [[source-stripe-currencies]] (https://docs.stripe.com/currencies; November capture `raw/stripe-currencies-2026-11-07.md:39-41`, May capture `raw/stripe-currencies-2025.md:32-34`).

## Special Currency Rules

| Currency | Rule |
| --- | --- |
| **ISK** (Icelandic Króna) | Zero-decimal, but API requires two-decimal with `00` cents: 5 ISK = `500` |
| **HUF** (Hungarian Forint) | Two-decimal for charges; zero-decimal for payouts — payout `amount` must be divisible by 100 |
| **TWD** (New Taiwan Dollar) | Same as HUF — two-decimal charges, zero-decimal payouts divisible by 100 |
| **UGX** (Ugandan Shilling) | Zero-decimal, but API requires two-decimal with `00` cents: 5 UGX = `500` |

## Minimum Charge Amounts (Key Currencies)

0.50 USD / 0.30 GBP / 0.50 EUR / 0.50 AUD / 0.50 CAD / 0.50 CHF / 50 JPY / 50 KRW / 175 HUF / 0.50 SGD / 2.00 MYR / 4.00 HKD

The applicable minimum depends on the payout bank account's settlement currency; a charge converted into the default settlement currency must meet that currency's equivalent minimum. Subscription charges may be zero for coupons or free trials, but nonzero amounts still face the applicable minimum. iDEAL is a payment-method exception allowing `amount` as low as `1`. See [[source-stripe-currencies]] (https://docs.stripe.com/currencies; May `raw/stripe-currencies-2025.md:60-106`, November `raw/stripe-currencies-2026-11-07.md:67-113`).

## Maximum Charge Amounts

> [!warning] Contradiction
> The May capture describes a general eight-digit ceiling with currency-specific card exceptions; the November capture separates card-network and non-card limits. The May COP/HUF/JPY card examples also have inconsistent stated digit counts and numeric values. Apply the relevant dated network, method, currency and region rule; an omitted May example is not evidence of withdrawn support. See [[source-stripe-currencies]] (https://docs.stripe.com/currencies; May `raw/stripe-currencies-2025.md:108-126`, November `raw/stripe-currencies-2026-11-07.md:115-140`).

- **Cards, November capture:** most card payments support 12 minor-unit digits (`999999999999`); Cartes Bancaires 10 (`9999999999`); Amex 9 (`999999999`) in most currencies. Network limits can be tighter by currency or region. JCB, Diners Club and Discover processed from Japanese Stripe accounts have an eight-digit JPY maximum (`99999999`).
- **Other payment methods, November capture:** IDR supports 12 minor-unit digits, COP 10, INR 9, and other currencies 8, subject to tighter method-specific limits. These documented ceilings do not guarantee an accepted charge.

## EEA Cards

Stripe's captured EEA card-pricing inventory contains 43 country or territory entries in both captures, including the UK and Türkiye. It is a Stripe fee-classification list, not an independent legal EEA definition or a fixed fee quote; fees can vary with issuing region and transaction currency. See [[source-stripe-currencies]] (https://docs.stripe.com/currencies; May `raw/stripe-currencies-2025.md:134-182`, November `raw/stripe-currencies-2026-11-07.md:148-196`).

## Sources

- [[source-stripe-currencies]] — primary: API formatting, special cases (ISK/HUF/TWD/UGX), min/max charge amounts, EEA card list, Connect FX
