---
title: "Adyen NetSuite bundle supported payment methods"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/netsuite/supported-payment-methods"
raw_files:
  - "adyen/docs/plugins/netsuite/supported-payment-methods/2026-09-15.md"
tags: [adyen, netsuite, payment-methods, plugins, availability]
---

## Overview

This [[adyen]] page is a method-by-method country/region and availability table for what the page calls the latest version of Adyen's NetSuite bundles. It helps select a bundle-supported method before requesting it for a merchant account. It does not name a bundle version or guarantee current account, currency, shopper, payment, or refund eligibility. See [[adyen-netsuite]] for the NetSuite integration route.

## Key takeaways

- The table separates **Credit and debit cards**, **Cash and ATM**, **Direct Debit**, **Online banking**, **Buy Now Pay Later**, **Prepaid and gift cards**, and **Wallets**. Each row gives its named method, country/region label, and an availability mark. For example, cards include International-labelled Visa/Mastercard; the table also lists country-specific methods such as Brazil's Pix and Netherlands' iDEAL. Use the exact row rather than treating a category or an **International** label as universal merchant eligibility. [Raw: method tables, lines 38–165]
- The bundles do **not** support product-page express payment methods where the **Pay** button appears on the product page. This is a bundle limitation, not a claim that every wallet listed in the table is unavailable in regular checkout. [Raw: opening, lines 19–21]
- The page directs merchants to request methods in the test or live Customer Area for the selected merchant account, filter by location/type, complete any prompted information, review and **Submit request**. The request step does not establish approval or enabled availability on that account. [Raw: Add payment methods to your account, lines 23–36]
- The table marks generic **Gift cards** unavailable while separately marking **Nordic gift card via NETS** available. It marks PayPal available with a specific footnote: the bundles do **not** support PayPal partial captures. Trustly's listed countries have a further support-team note for additional European countries. [Raw: Online banking note, lines 103–109; Prepaid and gift cards, lines 125–131; Wallets and PayPal note, lines 133–165]
- The page lists countries/regions, not supported currencies, tokenization behavior, refunds, POS-terminal flow, ERP transaction-profile setup, or live results. Those need their own applicable sources and account checks. Its embedded last-modified date is 2023-11-30 and the raw was fetched 2026-09-15; the phrase “latest version” is source wording, not a current package/version verification.

## Detail locators

- Scope and express-payment limitation: opening, lines 15–21.
- Test/live merchant-account method-request path: `Add payment methods to your account`, lines 23–36.
- Card and cash/ATM rows: `Credit and debit cards` and `Cash and ATM`, lines 38–77.
- Direct Debit and online-banking rows, including Trustly country note: lines 78–109.
- BNPL and prepaid/gift-card rows: lines 111–131.
- Wallet rows and PayPal partial-capture footnote: lines 133–165.

## Related

- [[adyen]] — provider page.
- [[adyen-netsuite]] — NetSuite bundle scope and source route.
- [[source-adyen-docs-plugins-netsuite-set-up-netsuite-customer-center]] — separate method and processing-profile setup route.

## Raw Sources

- [[raw/adyen/docs/plugins/netsuite/supported-payment-methods/2026-09-15|Adyen NetSuite supported payment methods (2026-09-15)]]
