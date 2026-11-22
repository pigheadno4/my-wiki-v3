---
title: "Tax Compliance with Managed Payments"
type: source
date_ingested: 2026-04-23
original_format: webpage
raw_files:
  - "stripe-managed-payments-tax-compliance-2025.md"
tags: [stripe, managed-payments, merchant-of-record, tax-compliance, vat, gst, sales-tax, stripe-tax, japan, singapore]
---

## Summary

Details of Managed Payments' tax coverage: 80+ countries where Stripe handles everything automatically, domestic exceptions (Japan, Singapore B2B), Serbia caveat, and how to handle unsupported countries using Stripe Tax (the only compatible solution).

## What Stripe Does Automatically (80+ countries)

- Calculates and collects correct tax
- Registers and files tax returns with local authorities
- Remits collected taxes to local authorities
- Issues tax invoices where required

**No action required from seller** in supported countries.

## Domestic Sales Exceptions

| Country | Exception |
| --- | --- |
| Japan | ALL domestic transactions — seller responsible |
| Singapore | B2B domestic only — seller responsible |

Singapore B2B = buyer self-identifies as a business at checkout. All other domestic sales in supported countries are covered by Stripe.

## Cross-Border Sales Coverage (~81 countries)

### Africa (9)
CM, EG, GH, KE, NG, UG, ZA, ZM, ZW

### Asia Pacific (28)
AM, AU, AZ, BN, GE, HK, ID, IL, IN, JP, KG, KR, KW, KZ, LA, MO, MY, NP, NZ, PH, QA, SA, SG, TH, TJ, TR, TW, VN

### Europe non-EU (11)
AL, BY, CH, GB, GI, IS, LI, MD, NO, RS, UA

### European Union (26)
AT, BE, BG, CY, CZ, DE, DK, EE, ES, FI, FR, GR, HR, HU, IE, IT, LT, LU, LV, MT, NL, PL, PT, RO, SE, SI, SK

### Latin America & Caribbean (5)
BB, BM, KY, MX, VG

### North America (2)
CA, US

**Serbia caveat**: cross-border only for sellers NOT VAT-registered in Serbia.

## Unsupported Countries

Seller responsible for all: registration, calculation, collection, filing, remittance.

**Stripe Tax is the ONLY compatible tax solution** — third-party tax providers are not supported with Managed Payments.

**No extra charge**: Stripe Tax calculation fees are free on Managed Payments transactions.

## Stripe Tax Setup for Unsupported Countries

Dashboard → Settings → Tax → Integrations. Provides:
- Threshold monitoring per country
- Registration support (via third-party partners)
- Automatic calculation once registered
- Filing/remittance support (via third-party partners)

## Invoices for Unsupported Countries

For seller-responsible transactions, Managed Payments sends invoices under your business name and tax details (not "Sold through Link, LLC"). Configure on Dashboard → Settings → Billing → Invoices. Must keep up to date for local tax documentation compliance.

## Related Pages

- [[stripe-managed-payments]] — concept page
- [[source-stripe-managed-payments-eligibility]] — supported business countries and tax codes
- [[stripe-tax]] — the only compatible third-party tax solution for unsupported countries

## Raw Sources

- [[stripe-managed-payments-tax-compliance-2025]] — verbatim tax compliance guide (157 lines)
