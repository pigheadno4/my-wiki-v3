---
title: "Stripe: Customer Balance Funding Instructions"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-customer-balance-funding-instructions-2025.md"
tags: [stripe, customer-balance, bank-transfers, funding-instructions, virtual-bank-account]
---

## Summary

How to retrieve virtual bank account details (funding instructions) without needing a PaymentIntent. Covers the `createFundingInstructions` API per region, per-region `financial_addresses` response schemas, the EU VBAN limit, and the account ownership letter feature.

## Key Details

**API**: `stripe.customers.createFundingInstructions(CUSTOMER_ID, { funding_type: 'bank_transfer', bank_transfer: { type: REGION_TYPE }, currency })`

**Per-region `bank_transfer.type` and `financial_addresses` format**:

| Region | `type` | `financial_addresses` | Networks |
| --- | --- | --- | --- |
| US | `us_bank_transfer` | ABA hash + SWIFT hash | ACH, domestic_wire_us, SWIFT |
| UK | `gb_bank_transfer` | sort_code hash | Bacs, FPS |
| EU | `eu_bank_transfer` + `country` | IBAN/BIC hash | SEPA |
| JP | `jp_bank_transfer` | zengin hash | zengin |
| MX | `mx_bank_transfer` | SPEI/CLABE hash | SPEI |

**EU**: SEPA countries include up to **1,000 VBANs** per account; contact sales for more. ES unavailable for new localized VBANs.

**Live mode**: unique VBAN per customer. Test mode: invalid (non-unique) details.

**Account ownership letter**: downloadable PDF from Dashboard confirming merchant owns the virtual bank account — useful when account appears Stripe-owned to the customer.

## Raw Sources

- [[stripe-customer-balance-funding-instructions-2025]] — verbatim webpage content (363 lines); fixed `_live mode_` → `*live mode*`; downloaded 1 CDN image to `raw/assets/`
