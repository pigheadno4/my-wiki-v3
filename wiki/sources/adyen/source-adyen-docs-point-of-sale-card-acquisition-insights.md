---
title: "Adyen POS Shopper Insights"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/card-acquisition/insights"
raw_files:
  - "adyen/docs/point-of-sale/card-acquisition/insights/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, shopper-insights, card-alias, payment-account-reference, webhooks]
---

## Overview

This short Adyen guide proposes merchant analysis of POS payment identifiers alongside purchase data, optionally spanning an online channel. Its documented collection routes for insights are **standard webhooks** and **Terminal API payment responses**; it links the separate card/shopper-identifiers guide for exact enablement and examples. The pinned webpage was fetched 2026-09-15 and lists `last_modified` 2025-02-24. Example questions about shopper origin, repeat purchasers and cross-channel behavior are possible analytic uses, not provided reports, accurate identity matches or authorization to retain personal data.

## Key takeaways

- The named insight inputs are card alias, funding source, issuer country and Payment Account Reference (PAR). Alias represents a card PAN for recognition but cannot make payments; it does not prove a unique human shopper. Issuer country identifies the card's issuer country and is described as an indicator of shopper residence, not verified residence. PAR can link a card or NFC wallet to a payment account when available; this dated snapshot names Visa and MasterCard availability conditionally, including possible ecommerce, Terminal API payment and card-acquisition responses. None of these values alone is a payment token or proof of an approved payment.
- For cross-channel collection, Adyen **recommends** standard webhooks because they have a common format and delivery pattern across channels. The merchant must select desired identifiers in webhook settings. Terminal API payment-response analysis likewise requires deciding which fields are needed and enabling some of them. This page does not list all response/webhook switches, BIN fields, or a guaranteed universal data set; use [[source-adyen-docs-point-of-sale-card-acquisition-identifiers]] for those details and privacy considerations.
- The requirements identify a Terminal API POS integration and optional online payments integration, with standard webhooks for data gathering. Card-acquisition is mentioned as one context where PAR may be returned, but the guide's two described insight collection routes are payment responses and standard webhooks. Merchant analysis, joining and interpretation remain merchant-owned.

## Detail locators

- `# Shopper insights` — example analysis questions about origin, repeat shoppers and optional ecommerce/POS overlap.
- `## Requirements` — Terminal API, optional online integration and standard-webhook setup.
- `## Gathering shopper insight data` — four named identifier types and the conditional scheme/PAR claim.
- `### Using data from webhooks`, `### Using data from Terminal API responses` — recommended common webhook collection versus enabled payment-response fields; links to the detailed identifier guide.

## Related

- Company: [[adyen]]
- Terminal API/POS context: [[adyen-terminal-api]]
- Field-level enablement and privacy: [[source-adyen-docs-point-of-sale-card-acquisition-identifiers]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/card-acquisition/insights/2026-09-15|2026-09-15 Adyen shopper-insights guide snapshot]]
