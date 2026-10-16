---
title: "Manage multiple merchant accounts in Adobe Commerce"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/adobe-commerce/set-up-the-plugin-in-adobe-commerce/multiple-merchant-accounts"
raw_files:
  - "adyen/docs/plugins/adobe-commerce/set-up-the-plugin-in-adobe-commerce/multiple-merchant-accounts/2026-09-15.md"
tags: [adyen, adobe-commerce, merchant-accounts, store-views]
---

## Overview

Adyen's Adobe Commerce page (metadata last modified 2023-05-03; captured 2026-09-15) explains how to arrange websites, stores and store views when one installation processes payments for multiple merchant accounts. Its operative separation is the store view and its payment-method configuration scope. It is configuration guidance, not evidence of account activation, credential/webhook routing, token portability, payment execution or cross-account funds movement. The version-qualified plugin baseline is [[adyen-magento2]].

## Key takeaways

- Adobe Commerce hierarchy is **website → store → store view**. The page describes adding websites with separate IP/domain, stores under a website with shared administration and checkout but distinct catalog/prices, and store views for languages, layouts or other functions (raw lines 21–33).
- For payments from different merchant accounts in one installation, the page says multiple store views are required. Different websites may be added to separate accounts; if accounts use the same website, add separate store views. Website separation does not replace the stated store-view requirement (raw lines 35–41).
- In Adobe Commerce admin, create a store view under the selected store, give it a name and identifier code, enable its status, and save. A name may match the merchant account, but the example is a naming choice, not an account binding by itself (raw lines 51–66).
- To configure the new view, use **Stores → Configuration → Sales → Payment Methods**, select it under **Scope: Default Config**, set view-specific payment-method options (the example disables cards), and save configuration (raw lines 68–75). The page links onward to payment-method and stored-payment-method setup, but those linked pages own their behavior; this page does not specify merchant API credentials, webhook endpoints, account-specific token behavior, or which account receives funds (raw lines 77–87).

## Detail locators

- Adobe Commerce website/store/store-view hierarchy: raw lines 21–33.
- Multiple merchant-account separation requirement: raw lines 35–41.
- Website and store-view creation: raw lines 43–66.
- Store-view payment-method configuration and onward setup links: raw lines 68–87.

## Related

- [[adyen-magento2]] — Adobe Commerce plugin concept and separately version-qualified implementation baseline.
- [[adyen]] — Adyen provider page.

## Raw Sources

- [[raw/adyen/docs/plugins/adobe-commerce/set-up-the-plugin-in-adobe-commerce/multiple-merchant-accounts/2026-09-15|Adobe Commerce multiple merchant accounts, captured 2026-09-15]]
