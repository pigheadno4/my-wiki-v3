---
title: "Stripe Billing — Customer Tax IDs"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-billing-customer-tax-ids-2026.md"
tags: [stripe, billing, tax, tax-ids, vat, eu-vat, invoices, customers, validation]
---

## Summary

Reference guide for Customer Tax IDs in Stripe Billing. 130+ supported tax ID types across 100+ countries. Tax IDs display in invoice/credit note PDF headers. Automatic validation for AU ABN, EU VAT, and GB VAT. IDs marked "Yes" in Impact column cause Stripe Tax to not apply tax (reverse charge / B2B exemption).

## Key facts

- Tax IDs appear in invoice and credit note PDF headers
- ~130+ supported enums (table in raw file): `eu_vat`, `gb_vat`, `au_abn`, `us_ein`, `in_gst`, `jp_trn`, `sa_vat`, etc.
- **"Impact in Tax Calculation" = Yes**: Stripe Tax won't apply tax if this ID is provided (reverse charge / B2B rules)
- To update a tax ID: delete old + create new (no direct update)
- Can manage via Dashboard, customer portal, or Tax ID API

## API

```bash
# Create
POST /v1/tax_ids
  type=eu_vat
  value=DE123456789
  owner[type]=customer
  owner[customer]={{CUSTOMER_ID}}
  # or owner[customer_account]={{ACCOUNT_ID}} for Accounts v2

# Delete
DELETE /v1/tax_ids/{{TAXID_ID}}
```

## Automatic validation

| Tax ID type | Validated against | Notes |
|---|---|---|
| AU ABN | Australian Business Register (ABR) | Validates format only; not name/address match |
| EU VAT | European Commission VIES | Async; hover tooltip shows gov data (name, address) |
| GB VAT | UK HMRC | Async |

Async → `customer.tax_id.updated` webhook fires on status change.

Dashboard: hover over EU VAT number to see VIES validation tooltip.

## Test magic IDs

| Value | Result |
|---|---|
| `000000000` | Successful verification |
| `111111111` | Unsuccessful verification |
| `222222222` | Pending indefinitely |

(Type must be ABN, EU VAT, or GB VAT)

## Related pages

- [[stripe-tax]] — concept page (updated)
- [[stripe-tax-id-element]] — Tax ID Element UI component
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-billing-customer-tax-ids-2026]] — verbatim Stripe docs webpage (253 lines, 1 CDN image URL preserved)
