---
title: "Adyen Platforms account structure with financial products"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/account-structure-resources/financial-products"
raw_files:
  - "adyen/docs/platforms/account-structure-resources/financial-products/2026-09-15.md"
tags: [adyen, platforms, account-structure, financial-products]
---

## Overview

This 2026-09-15 Adyen for Platforms page maps additional financial products—card issuing, business accounts and business financing—to platform and user resources. It gives a food-delivery example, not an account inventory or ownership determination for any actual platform. Route through [[adyen-platforms]]; [[adyen-financial-products]] covers the wider product family.

## Key takeaways

- The page states that a platform acquiring payments must have a balance platform and merchant account in each region where it is registered and wishes to acquire (raw line 29). Its example then shows a company account, regional merchant accounts and balance platforms, a platform liable account holder/balance account, regional legal entities, and an optional grant account for financing (lines 31–58). The example's country counts and names are illustrative.
- For each example user, stores tie to merchant accounts by country; account holders define payment-processing capabilities; balance accounts hold user funds, while a separate balance account links to a business account and/or Adyen-issued card. Multiple payment instruments may link to that same instrument-linked balance account (lines 60–73).
- The example also describes transfer instruments for payout from balance accounts; optional issued cards and business accounts; and user legal entities and business lines by country for KYC and industry information (lines 74–83). A grant account is described for business financing in the platform-resource section, not as a user payment or payout account (line 58).

## Detail locators

- Financial-product list and food-delivery scenario: raw lines 19–35.
- Platform-owned resources and region-specific example: lines 39–58.
- User-owned resources, payment-instrument balance-account separation, transfer instruments and KYC/business lines: lines 60–83.
- Diagram link and product navigation: lines 85–93.

## Evidence boundary

The page describes an example resource structure, not proof that issuing, business accounts or Capital is available, approved or enabled for a given region, platform or user. An account holder's described capabilities do not establish their current status. The example does not identify the merchant of record, legal seller, payee or funds owner for a particular transaction, nor prove verification, transfer execution or bank receipt.

## Related

- [[adyen-platforms]] — platform onboarding and resource context.
- [[adyen-financial-products]] — optional product-family orientation.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/account-structure-resources/financial-products/2026-09-15|Pinned account-structure reference, captured 2026-09-15]]
