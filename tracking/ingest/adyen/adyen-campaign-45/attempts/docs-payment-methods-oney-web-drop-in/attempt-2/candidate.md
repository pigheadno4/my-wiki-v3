---
title: "Adyen Oney Web Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/oney/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/oney/web-drop-in/2026-09-15.md"
tags: [adyen, oney, web, drop-in, installments, capture, refund]
---

## Overview

This 2026-09-15 Adyen Docs guide adds Oney to an **existing Web Drop-in** integration using either Sessions or Advanced flow. It requires Oney setup in Customer Area, shopper and purchased-item details, and successful authorization **and capture before shipping**. The guide is documentation, not evidence that a merchant is enabled or a transaction succeeded. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The guide has separate Sessions and Advanced base-flow requirements. Its API table calls `/sessions` the default with Drop-in v5.0.0 or later; `/payments` is presented for an additional use case. Do not treat the example Checkout API v69 Sessions and v72 payments calls, or language-specific library versions, as a single required version (pinned raw lines 27–51, 72–75, 763–789).
- Both API tables mark `lineItems`, `shopperEmail`, `shopperReference`, `shopperName`, `telephoneNumber` and `billingAddress` required. Oney approval depends on the `lineItems` total matching `amount.value`. The tables give a three-character minimum shopper reference, 32-character maximum name, country-specific mobile prefixes and five-character billing postal code. They describe delivery address (falling back to billing if absent), date of birth, locale and country code without required marks. `oneydata.trustFlag` is optional and requires Oney enablement; `merchantPays` optionally overrides the account's interest-fee setting (lines 53–70 and 767–784).
- Optional Drop-in configuration is per supported installment type: `facilypay_3x`, `4x`, `10x` and `12x` for France/Spain, and `6x` for Spain only. Pre-filled personal and address data and form visibility can be configured; the defaults hide company and bank-account fields and make personal/billing/delivery fields editable (lines 1255–1354).
- Capture can be manual or automatic, with or without delay, according to capture settings. Capture after more than six days is described as expiring authorization and requiring reauthorization; confirm capture before shipping. Cancel uncaptured payments; refund captured payments. Refunds have a EUR 1 minimum and a 13-month window after capture; partial refunds use the `/payments/{paymentPspReference}/refunds` amount field (lines 1356–1376).
- Test instructions give different France amount bands for Authorised, Pending and Refused, a separate 10x/12x scenario, Spanish identification-number outcomes, and country/installment minimum test amounts. The live section directs merchants to request Oney 3x4x in live Customer Area; test samples and this request do not prove live acceptance (lines 1378–1456).

> [!warning] Example and scope inconsistencies
> The installment table spells the 3x type `facilypay_3x`, but two Drop-in configuration snippets use `facilpay_3x` (raw lines 1261, 1273 and 1344). The Advanced C# example sets `CountryCode = "EUR"` while the adjacent FR/EUR examples use `FR` as the country (line 1010). Example phone `+33 1 76 35 07 90` does not match the table's French `+336`/`+337` mobile-prefix description (lines 59–60 and 87). The minimum-test table mentions Italy, although the installment-configuration table lists only France and Spain (lines 1259–1265 and 1448–1452). The Sessions Node v29 JavaScript snippet imports only `Client` and `CheckoutAPI`, and its TypeScript snippet imports `Client`, `CheckoutAPI` and `Types`, but both instantiate `Config` and use `EnvironmentEnum` without importing those names (raw lines 395–404 and 684–693). Verify version-specific imports and configuration before using either snippet; this guide does not supply a corrected SDK signature. These examples and tables should not be copied or combined as proof of an eligible, valid request.

## Detail locators

- Existing-integration purpose, pre-shipping capture and Sessions/Advanced requirements: pinned raw lines 15–43.
- Sessions and Advanced API tables and sample requests, including Sessions Node import/configuration inconsistencies at lines 395–404 and 684–693: lines 45–1253.
- Installment mapping, optional prefill and visibility: lines 1255–1354.
- Capture/refund boundaries: lines 1356–1376; testing and live-request route: lines 1378–1456.

## Related

- [[adyen-online-payments]] — provider online-payments concept
- [[source-adyen-docs-payment-methods-oney]] — Oney overview for method-level scope

## Raw Sources

- [[raw/adyen/docs/payment-methods/oney/web-drop-in/2026-09-15|Oney Web Drop-in guide, captured 2026-09-15]]
