---
title: "Adyen Platforms custom payout transfer routes"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/custom-payouts/transfer-routes"
raw_files:
  - "adyen/docs/platforms/custom-payouts/transfer-routes/2026-09-15.md"
tags: [adyen, platforms, custom-payouts, transfer-routes, bank-transfers]
---

## Overview

This Adyen for Platforms Configuration API guide (last modified 2023-03-13; captured 2026-09-15) describes calculating available routes for bank payouts to transfer instruments before sending funds. Banks or regulators can limit priorities, transfer amounts or required recipient information. The route calculation is a pre-transfer check: its response lists routes and requirements, not a bank transfer request, an approved payout, or beneficiary receipt. See [[adyen]], [[adyen-platforms]] and the parent custom-payout guide [[source-adyen-docs-platforms-custom-payouts]].

## Key takeaways

- **Access and methods:** The guide requires an Adyen for Platforms integration and a Configuration API credential with Balance Platform BCL role. POST /transferRoutes/calculate can query by destination country/region or by a particular counterparty. Both variants specify a balance platform, currency and bank transfer category. Country/region mode supplies a two-character counterparty country code; counterparty mode supplies bank-account details or a transfer instrument. A source balanceAccountId is conditionally required when the counterparty contains transferInstrumentId. The priorities array is optional in the documented request tables.
- **What comes back:** The transferRoutes response lists supported route currency and priority plus any additional requirements. The counterparty variant also lists country. Example responses show amount min/max, address, bank-account identification and payment-instrument requirements. Their numeric values and supported priorities are examples for the illustrated request, not universal limits or present-day eligibility.
- **Decision boundary:** The page recommends checking available routes before sending funds to a new recipient to reduce failures from bank or regulatory limitations. A returned route still requires satisfying its listed conditions and following a separate scheduled or on-demand payout flow. It does not establish account-holder capability, current bank acceptance, cutoff timing, funds availability, payout initiation, booking, or bank receipt.

## Detail locators

- Purpose, bank/regulatory limitations, recommendation and requirements: pinned raw lines 15-30.
- Country/region POST field table and test request: pinned raw lines 32-71; response shape and illustrative requirements: lines 301-357.
- Counterparty POST field table, transferInstrumentId/source-balance-account condition and test request: pinned raw lines 359-402; response shape and illustrative requirements: lines 716-780.
- Separate scheduled/on-demand payout routes: pinned raw lines 782-785.

## Related

- [[adyen-platforms]] — main Platforms concept and reciprocal source route.
- [[source-adyen-docs-platforms-custom-payouts]] — parent custom-payout overview.

## Raw Sources

- [[raw/adyen/docs/platforms/custom-payouts/transfer-routes/2026-09-15|Adyen Transfer routes, captured 2026-09-15]]
