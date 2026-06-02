---
title: "Stripe Docs — Supported currencies"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-currencies-2025.md"
tags: [stripe, currencies, presentment, settlement, minor-units, zero-decimal, isk, huf, twd, ugx, eea, minimum-charge]
---

## Summary

Reference for Stripe's currency support — 135+ presentment currencies, API amount formatting (minor units), special currency rules, minimum/maximum charge amounts, and EEA card definitions.

## Key Facts

- **135+ currencies** for charges; settle in preferred currency
- **API amounts**: smallest denomination, no decimals (two-decimal: `1000` = 10 USD; zero-decimal: `10` = 10 JPY)
- **American Express**: doesn't support currencies marked with `*`

## Special Currency Rules

| Currency | Rule |
| --- | --- |
| ISK | Zero-decimal but API uses two-decimal with `00`: 5 ISK = `500` |
| HUF | Two-decimal charges; zero-decimal payouts (divisible by 100) |
| TWD | Same as HUF |
| UGX | Same as ISK |

## Minimum Charge Amounts (Selected)

0.50 USD / 0.30 GBP / 0.50 EUR / 0.50 AUD / 0.50 CAD / 50 JPY / 50 KRW / 175 HUF / 4.00 HKD

## Maximum Charge Amounts

- 8 digits (most); 12 digits (IDR, LBP); 10 digits (COP, HUF, JPY cards); 9 digits (INR)
- JCB/Diners/Discover from Japan: 8 digits max regardless

## EEA Cards Definition (44 countries)

Includes EU member states + UK, Iceland, Norway, Liechtenstein, Andorra, Monaco, San Marino, Türkiye, and others. Different fees may apply.

## Related Pages

- [[stripe-currencies]] — concept page
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-currencies-2025]] — verbatim webpage content (191 lines)
