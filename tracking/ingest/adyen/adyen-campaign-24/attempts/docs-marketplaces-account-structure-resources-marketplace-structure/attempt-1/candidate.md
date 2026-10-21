---
title: "Adyen Marketplace account structure and example funds flow"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/account-structure-resources/marketplace-structure"
raw_files:
  - "adyen/docs/marketplaces/account-structure-resources/marketplace-structure/2026-09-15.md"
tags: [adyen, marketplaces, platforms, account-structure, funds-flow]
---

## Overview

This 2026-09-15 Marketplaces guide describes the account/resources structure for a branded **online-payment marketplace**. Customers recognize the marketplace brand while the marketplace processes payments on behalf of users. It separates marketplace-owned company/merchant/balance-platform/liable/legal-entity resources from user account-holder/balance-account/transfer-instrument/legal-entity resources, then gives an NL-to-EU payment and payout example. The example does not establish the legal seller, merchant of record or fund ownership for a particular transaction. [[adyen]] [[adyen-platforms]]

## Key takeaways

- The page states that a marketplace needs a balance platform and merchant account in each region where it is registered and wishes to acquire payments. A separate **conditional** rule says a global marketplace with multiregional sellers who can transfer funds to each other must use a single balance platform across acquiring regions and cannot offer additional financial products to users (raw lines 19–28).
- Its illustrated Online Marketplace operates in EU and US acquiring regions and NL, DE and US countries/areas. It lists one company account, three merchant accounts by country/region, two balance platforms by acquiring region, a liable account holder and liable balance account for marketplace funds, and a marketplace legal entity in each acquiring region for KYC information (raw lines 30–51). The two-platform example is not stated to have the cross-region seller-transfer condition, so it should not override the separate single-platform rule (raw lines 25–30, 44–47).
- For each user, the example lists at least one account holder per operating country to define payment-processing capabilities; at least one balance account with base currency per account holder for user funds; a transfer instrument described as a verified bank account for payout from each balance account; and a legal entity in each operating country for KYC information. These are different resources and roles, not interchangeable names for one account (raw lines 53–61).
- In the Netherlands payment example, the customer's payment is processed in `OnlineMarketplace_NL` merchant account, settled in balance accounts of `OnlineMarketplace_EU` balance platform, retained in user balance accounts until payout, then paid to the account holder's transfer instrument. This is the documented example flow, not evidence of an actual authorization, settlement, payout or bank receipt (raw lines 69–76).

## Detail locators

- Marketplace online-payment model and conditional regional structure: raw lines 17–28. Example geography and marketplace resource hierarchy: lines 30–51.
- User account-holder, balance-account, transfer-instrument and legal-entity mapping: lines 53–61. Diagram link: lines 63–67. NL merchant-account to EU balance-platform to user balance-account to bank payout example: lines 69–76.

## Related

- [[adyen]] — provider.
- [[adyen-platforms]] — modern Platforms model and Marketplace route.
- [[source-adyen-docs-marketplaces]] — marketplace overview.
- [[source-adyen-docs-marketplaces-manage-balance-accounts]] — separate balance-account operations guide.
- [[adyen-classic-platforms]] — distinct legacy integration.

## Raw Sources

- [[raw/adyen/docs/marketplaces/account-structure-resources/marketplace-structure/2026-09-15|Marketplace account structure — 2026-09-15 snapshot]]
