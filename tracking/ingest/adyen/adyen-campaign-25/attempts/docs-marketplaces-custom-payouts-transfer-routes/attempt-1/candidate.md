---
title: "Adyen Marketplaces custom payout transfer routes"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/custom-payouts/transfer-routes"
raw_files:
  - "adyen/docs/marketplaces/custom-payouts/transfer-routes/2026-09-15.md"
tags: [adyen, marketplaces, platforms, custom-payouts, transfer-routes]
---

## Overview

This 2023-modified, 2026-09-15-captured Marketplace-path Adyen for Platforms guide uses the Configuration API to calculate available **bank-payout** transfer routes before sending funds to a user's transfer instrument or other bank counterparty. A bank or regulator may constrain priority, amount or recipient details; Adyen recommends a route calculation for a new recipient to reduce transfer failures. A calculated route is a pre-transfer response, not a payout request, booked transfer or bank receipt. [[adyen]] [[adyen-platforms]] (raw lines 15–21)

## Key takeaways

- **Access:** The page requires an Adyen for Platforms integration and a Configuration API credential with the **Balance Platform BCL role**. Both lookup forms call `POST /transferRoutes/calculate` with `balancePlatform`, a three-character transfer `currency`, and `category: bank`. The documented `priorities` array is optional and selects priorities to calculate. (raw lines 23–30, 32–48, 359–372)
- **Country/region lookup:** Supply the counterparty's two-character ISO `country` code. The response's `transferRoutes` entries each give a supported currency and priority and any additional route requirements. The Netherlands/USD TEST example illustrates regular, cross-border and wire priorities, with illustrative amount, address, bank-identification and payment-instrument requirements; it is not a universal limit or route-availability guarantee. (raw lines 36–50, 54–71, 301–357)
- **Specific-counterparty lookup:** Supply a `counterparty` object with a third-party bank account or transfer instrument instead of only a country. `balanceAccountId`, the source balance-account ID, is **conditionally required when `counterparty` contains `transferInstrumentId`**. The response adds counterparty country to currency, priority and any requirements. The EUR/Netherlands instant-and-wire response is illustrative, including distinct min/max and bank-identification rules per route. (raw lines 359–374, 378–401, 716–780)
- Returned routes and requirements must be assessed for the intended recipient and transfer, then a separate scheduled or on-demand payout flow applies. This page does not establish available funds, the user's payout capability, current bank acceptance, execution timing, transfer booking or receipt at the beneficiary bank. The examples use TEST endpoints and SDK versions, not live-account outcomes. (raw lines 19–21, 52–299, 376–714, 782–785)

## Detail locators

- Raw lines 42–48: country/region request-field table; 56–299: Checkout-independent Configuration API TEST/curl and version-labeled SDK examples; 301–357: country response and route-requirement shapes.
- Raw lines 365–372: counterparty request-field table and source-account condition; 378–714: TEST/curl and SDK examples using bank-account IBAN; 716–780: counterparty response and per-route requirements.
- Raw lines 782–785: separate custom scheduled and on-demand payout guides.

## Related

- [[adyen-platforms]] — existing Adyen for Platforms concept.
- [[source-adyen-docs-marketplaces-custom-payouts]] — Marketplace custom-payout overview.
- [[source-adyen-docs-platforms-custom-payouts-transfer-routes]] — parallel Platforms-path route-calculation guide.

## Raw Sources

- [[raw/adyen/docs/marketplaces/custom-payouts/transfer-routes/2026-09-15|Marketplace transfer routes, captured 2026-09-15]]
