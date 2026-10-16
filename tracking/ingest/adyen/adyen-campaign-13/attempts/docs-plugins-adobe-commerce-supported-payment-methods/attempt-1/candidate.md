---
title: "Supported payment methods for Adobe Commerce | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/adobe-commerce/supported-payment-methods"
raw_files:
  - "adyen/docs/plugins/adobe-commerce/supported-payment-methods/2026-09-15.md"
tags: [adyen, adobe-commerce, magento2, payment-methods, standard, headless]
---

## Overview

This 2026-09-15 capture of an Adyen Docs page last modified in 2024 lists payment-method support for the Adobe Commerce plugin in **Standard** and **Headless** integrations, with country/region columns and supported/unsupported marks. Its phrase “latest version” does not identify a specific package release or override the separately version-qualified [[adyen-magento2]] GitHub baseline. The matrix describes plugin support by integration type, not a merchant account's enabled methods, live regional eligibility, or a completed payment. [[adyen]]

## Key takeaways

- The merchant must separately request methods for its merchant account in test or live Customer Area: switch to the merchant account, inspect available methods, filter by location/type, submit selected methods and supply prompted information. A checked matrix cell alone does not show that a method is available to or configured for that merchant. See raw lines 19–38.
- Each row must be read with its method, **Countries/regions**, **Standard**, and **Headless** cells. The page includes supported and unsupported rows in credit/debit cards, cash and ATM, direct debit, online banking, buy now pay later, prepaid/gift cards and wallets. The raw matrix is the locator for exact method-country-integration answers; a method's presence in the list alone is insufficient. See raw lines 40–187.
- The Trustly row says DK, FI, NO, SE “and more,” with a footnote directing readers to Support for other European countries/regions. Express Apple Pay, Google Pay and PayPal rows have a separate footnote requiring the express checkout module to offer express checkout. These conditions are not a blanket feature claim for every listed method. See raw lines 119–122, 159–179, 189.
- This page gives **country/region**, not currency eligibility, and does not define recurring, refund or partial-payment support per method. It also does not state an exact plugin version. Check method-specific and release-qualified evidence for those questions. See raw lines 15–21, 40–189.

## Detail locators

- **Matrix scope and account method-request path:** raw lines 15–38.
- **Cards, cash/ATM and direct debit:** raw lines 40–88.
- **Online banking and Trustly country footnote:** raw lines 90–122.
- **BNPL and prepaid/gift cards:** raw lines 124–150.
- **Wallets and express-checkout module footnote:** raw lines 152–189.

## Related

- [[adyen]]
- [[adyen-magento2]]
- [[source-adyen-docs-plugins-adobe-commerce]] — website integration/version overview
- [[source-github-adyen-magento2]] — separately qualified repository implementation baseline

## Raw Sources

- [[raw/adyen/docs/plugins/adobe-commerce/supported-payment-methods/2026-09-15|Adobe Commerce supported methods — collected 2026-09-15]]
