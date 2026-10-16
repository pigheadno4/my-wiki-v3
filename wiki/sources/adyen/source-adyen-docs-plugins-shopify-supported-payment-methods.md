---
title: "Adyen Shopify supported payment methods"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/shopify/supported-payment-methods"
raw_files:
  - "adyen/docs/plugins/shopify/supported-payment-methods/2026-09-15.md"
tags: [adyen, shopify, payment-methods, plugin]
---

## Overview

This Adyen webpage snapshot lists payment methods marked available in what it calls the **latest version** of its Shopify plugin, with a **Countries/regions** column. It names no exact plugin/app version or currency matrix. A checked row is a dated plugin-support entry, not proof that a given merchant account has the method enabled, a shopper is eligible, or a payment, refund, or recurring charge will succeed. See [[adyen]] and [[adyen-shopify]].

## Key takeaways

- The table covers **credit/debit cards**, **cash and ATM**, **direct debit**, **online banking**, and **wallets** (raw lines 21–84). For example, it lists **Pix — BR** (line 64), **ACH Direct Debit — US** (line 49), and **Apple Pay — International** (line 75). Read each row's stated region; “International” is the table label, not a guarantee of universal country/currency eligibility.
- **Trustly** is listed for DK, FI, NO, SE “and more,” with a Support contact note for additional European countries/regions (raw lines 65–67). The table's “See note [4]” marker and the captured note's “1 Trustly” prefix do not line up; preserve the qualified country list rather than silently assigning a definitive complete set.
- The page does not state method-specific **currency**, merchant-account approval, checkout feature setup, recurring-payment support, refund handling, or capture/order lifecycle. The related Shopify installation guide owns app setup and merchant-account method requests; method presence here does not establish those downstream capabilities.
- The raw frontmatter says last modified **2024-12-24**, while the page simply says “latest version” without a number (raw lines 11, 19). Treat this as a captured compatibility list, not a verified current-release inventory.

## Detail locators

- Card table, raw lines 21–35; cash/ATM, 37–43; direct debit, 45–49; online banking, 51–67; wallets, 69–84.
- Trustly country note, raw lines 65–67; exact version/date qualification, lines 11 and 19.

## Related

- [[adyen-shopify]] — two-app Shopify setup and merchant-account configuration route.
- [[source-adyen-docs-plugins-shopify]] — installation/testing and test-to-live account transition.

## Raw Sources

- [[raw/adyen/docs/plugins/shopify/supported-payment-methods/2026-09-15|Supported payment methods, fetched 2026-09-15]]
