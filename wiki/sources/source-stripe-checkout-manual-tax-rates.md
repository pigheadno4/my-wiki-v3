---
title: "Stripe Checkout: Use Manual Tax Rates"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-manual-tax-rates-2025.md"
tags: [stripe, checkout, tax, tax-rates, manual-tax, fixed-tax, dynamic-tax, checkout-sessions]
---

## Summary

Guide for using manual Tax Rates (the `stripe.taxRates` API) in Checkout — the alternative to Stripe Tax (`automatic_tax`). Covers creating Tax Rate objects, fixed vs dynamic rate strategies, wallet constraints, and tax reporting exports.

## Key Takeaways

- Manual Tax Rates are the legacy/manual alternative to Stripe Tax; **Stripe Tax is recommended** for 60+ country automated support
- **Two strategies**: fixed (known rate upfront) or dynamic (match rate to customer location)
- **TaxRate object**: `percentage`/`country`/`state` are **immutable** — create new + archive old to change
- **Fixed**: `line_items.tax_rates` (payment mode) or `subscription_data.default_tax_rates` (subscription mode)
- **Dynamic**: `line_items.dynamic_tax_rates` — Stripe matches customer address to rate; billing address auto-collected; 30 supported countries
- `tax_rates` and `dynamic_tax_rates` are **mutually exclusive** per line item
- **Apple Pay + Google Pay**: disabled when using dynamic tax rates without `shipping_address_collection`
- **Tax reporting**: Dashboard exports; payment mode uses 2 exports (line item + totals); subscription mode uses Stripe Billing exports

## TaxRate Object

| Field | Required | Notes |
| --- | --- | --- |
| `display_name` | Yes | Shown to customer (e.g. "Sales Tax", "VAT", "GST") |
| `inclusive` | Yes | `true` = tax included in price; `false` = added on top |
| `percentage` | Yes | Up to 4 decimal places; **immutable** |
| `country` | No | ISO two-letter code; required for dynamic matching; **immutable** |
| `state` | No | Required for US dynamic matching; **immutable** |
| `jurisdiction` | No | Region label in Dashboard; differentiates same-% rates |
| `description` | No | Internal only — not shown to customer |

> `percentage`, `country`, and `state` are immutable. To change them: create a new TaxRate and archive the old one.

## Fixed vs Dynamic Tax Rates

| | Fixed | Dynamic |
| --- | --- | --- |
| Use case | Known rate upfront | Rate depends on customer location |
| Payment mode param | `line_items.tax_rates` | `line_items.dynamic_tax_rates` |
| Subscription mode param | `subscription_data.default_tax_rates` | N/A (not supported) |
| Address collection | Not required | Billing address auto-collected; shipping takes precedence |
| Supported countries | Any | 30 (EU + AU + US) |
| Wallet support | Full | Apple Pay + Google Pay disabled without `shipping_address_collection` |

## Dynamic Tax Rate Supported Countries

30 countries: AT, AU, BE, BG, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IT, LT, LU, LV, MT, NL, PL, PT, RO, SE, SI, SK, US (state required for US).

## Tax Reporting Exports

- **Payment mode**: 2 Dashboard exports required:
  1. *Line item tax export* — per-line-item rates, inclusive/exclusive, amounts
  2. *Totals export* — aggregate tax + refund adjustments
- **Subscription mode**: use Stripe Billing tax exports instead

## Related Pages

- [[stripe-tax]] — Stripe Tax concept page (includes both automatic_tax and manual Tax Rates)
- [[source-stripe-checkout-taxes]] — Automatic tax collection via Stripe Tax

## Raw Sources

- [[stripe-checkout-manual-tax-rates-2025]] — Manual Tax Rates: TaxRate API, fixed + dynamic rates, 30-country list, wallet constraints, Dashboard reporting exports
