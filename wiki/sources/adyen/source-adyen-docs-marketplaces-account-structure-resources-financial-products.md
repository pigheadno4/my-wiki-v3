---
title: "Adyen Marketplaces account structure with financial products"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/account-structure-resources/financial-products"
raw_files:
  - "adyen/docs/marketplaces/account-structure-resources/financial-products/2026-09-15.md"
tags: [adyen, marketplaces, platforms, account-structure, financial-products]
---

## Overview

This 2026-09-15 **Marketplaces / Adyen for Platforms** page illustrates how optional **card issuing, business accounts and business financing** relate to marketplace and user resources. Its named Online Marketplace LLC, NL/DE/US merchant accounts and EU/US balance platforms are an **example account structure**, not evidence that any resource, product, funding or payout exists for a particular platform. [[adyen-platforms]]

## Conditional platform structure

- The page says a marketplace needs a **balance platform and merchant account in each region** where it is registered and wishes to acquire payments. It then gives a separate condition: a **global marketplace with multiregional sellers who can transfer funds to each other** must use a **single balance platform for all acquiring regions** and **cannot offer additional financial products** to its users. Do not combine the example’s regional balance platforms with that mutually exclusive cross-region-seller-transfer case. See [[raw/adyen/docs/marketplaces/account-structure-resources/financial-products/2026-09-15|raw lines 27–40]].
- The illustrative marketplace owns a company account, region/country merchant accounts, regional balance platforms, a liable account holder and liable balance account for its own funds, regional legal entities for KYC, and optionally a grant account to track accepted financing offers and repayment amounts. The example does not prove a grant or financing offer. See [[raw/adyen/docs/marketplaces/account-structure-resources/financial-products/2026-09-15|raw lines 42–63]].

## User resource distinctions

- In the example, each user has at least one account holder per operating country and at least one **funds-holding balance account** per account holder. Balance accounts linked to payment instruments such as a business account or Adyen-issued card are described as **separate** from that funds-holding balance account, though multiple instruments may share the same instrument-linked balance account. See [[raw/adyen/docs/marketplaces/account-structure-resources/financial-products/2026-09-15|raw lines 65–71]].
- The guide lists a **verified-bank transfer instrument for each balance account** as a payout destination, optional payment instruments using balance-account funds, and user legal entities per operating country for KYC. These are resource relationships in the captured example, not proof of bank verification, capability grant, card issuance, business-account opening, payout or bank receipt. See [[raw/adyen/docs/marketplaces/account-structure-resources/financial-products/2026-09-15|raw lines 73–86]].

## Detail locators

- Optional products and the regional-versus-cross-region-transfer condition: [[raw/adyen/docs/marketplaces/account-structure-resources/financial-products/2026-09-15|raw lines 15–40]].
- Marketplace-owned company, merchant, balance, liable, legal-entity and grant resources: [[raw/adyen/docs/marketplaces/account-structure-resources/financial-products/2026-09-15|raw lines 42–63]].
- User account holders, distinct balance-account roles, instruments and legal entities: [[raw/adyen/docs/marketplaces/account-structure-resources/financial-products/2026-09-15|raw lines 65–86]].

## Related

- [[adyen-platforms]] — modern Platforms resource model.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/account-structure-resources/financial-products/2026-09-15|Marketplaces account structure with financial products (captured 2026-09-15)]]
