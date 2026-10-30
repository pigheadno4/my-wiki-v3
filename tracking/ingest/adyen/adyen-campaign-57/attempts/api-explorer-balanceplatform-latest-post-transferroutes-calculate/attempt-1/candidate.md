---
title: "Adyen Configuration API v2: calculate transfer routes"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/transferRoutes/calculate"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/transferRoutes/calculate/2026-09-15.md"
tags: [adyen, configuration-api, transfer-routes, balance-platform]
---

## Overview

This 2026-09-15 Configuration API v2 reference describes `POST /transferRoutes/calculate`, a pre-transfer lookup for available bank-transfer priorities and their requirements from a country/currency/counterparty/priority combination. The request does not initiate a transfer; the page points separately to the Transfers API for that action. [[adyen]] [[adyen-platforms]] [[adyen-business-accounts]]

## Key takeaways

- The request-body table marks `balancePlatform`, `category` (documented value `bank`) and `currency` required. Either `counterparty` or `country` must be supplied. `counterparty` may identify a bank account or transfer instrument; `balanceAccountId` is required when `counterparty` uses `transferInstrumentId`. Within `bankAccount`, `accountIdentification` is marked required, and its fields vary by bank country and transfer currency. See raw lines 14–26. These are property/conditional requirements; the capture does not separately state whether the whole request body is required.
- Optional `priorities` select requested speed/fee categories; the table names regular, fast, wire, instant, crossBorder and internal, with stated scope or recommendations. Returned routes expose priority and clearing-house/banking-partner requirements for a later transfer request. See lines 26, 48–59.
- The page lists a TEST `/bcl/v2` server. A 200 response means route calculation succeeded, not that a priority is live-eligible for a specific account or that a transfer was submitted, booked or received. See lines 5–10 and 46–59.

## Error and example boundaries

The reference lists 401 authentication, 403 permissions, 422 validation and 500 server failures, with common problem fields (raw lines 62–139). The 422 example refers to changing a payment instrument's `balanceAccountId`, and the 500 example refers to creating a payment instrument—neither describes route calculation. Do not infer route-specific conditions from those examples (lines 249–275). The 200 sample shows NL/USD crossBorder and wire routes with amount, address, bank-identification and instrument requirements; these sample values are illustrative, not general limits or current route availability (lines 141–221).

## Detail locators

- Request property and conditional matrix: raw lines 14–26; request example: 28–45.
- Success response shape and requirement meaning: 46–59; example requirement variants: 141–221.
- Error schemas and examples: 62–139, 223–275.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/transferRoutes/calculate/2026-09-15|Configuration API v2 calculate transfer routes, captured 2026-09-15]]
