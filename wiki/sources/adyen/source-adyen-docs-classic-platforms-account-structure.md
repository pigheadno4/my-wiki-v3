---
title: "Adyen Classic Platforms account structure"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/account-structure"
raw_files:
  - "adyen/docs/classic-platforms/account-structure/2026-09-15.md"
tags: [adyen, classic-platforms, account-structure, sub-merchants, fund-flow]
---

## Overview

This 2021-modified page, captured 2026-09-15, is explicitly for **classic Adyen for Platforms** integrations and directs a new implementation to the separate newer integration guide. It describes a classic platform's company/merchant-account side, sub-merchant account-holder/account resources, its own liable pair, and the payment-to-payout money flow. Do not equate these classic `account` resources with the current Platforms `balanceAccount` model. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- Signing up for an Adyen account gives the platform a company account and one or more merchant accounts. Payment methods and processing currencies are configured at merchant-account level. One merchant account per country is described as common for many Platforms customers, not mandatory (raw lines 31–37).
- In the classic platform, each sub-merchant has an **account holder** representing its entity and containing individual/company and payout-bank details used for KYC, plus an **account** holding its funds. An account holder may have multiple accounts; the page says one suffices in most use cases (raw lines 39–49).
- The platform's entity has its own **liable account holder** and **liable account**. The liable account holds platform funds, is charged fees, and bears liability when other platform accounts become negative from refunds or chargebacks; multiple liable accounts can separate transaction/fund sets for accounting (raw lines 50–55).
- Customer payments are processed through the platform's Adyen merchant accounts, then captured and settled to platform accounts selected by split instructions at payment or capture. Funds remain there until payout from the account holder's account to one of that holder's verified bank accounts. Refund requests run through the merchant account while platform accounts are debited and the customer is credited (raw lines 57–74). This is a described flow, not proof that a particular capture, settlement, payout or refund succeeded.

## Detail locators

- Classic-only scope and new-integration redirect: raw lines 15–23. Company and merchant-account structure: raw lines 25–37.
- Sub-merchant and liable account-holder/account ownership, KYC and fee/negative-balance liability: raw lines 39–55. Captured payment splits, verified-bank payout and refund direction: raw lines 57–74.

## Related

- [[adyen-classic-platforms]] — dedicated classic model and reciprocal source route.
- [[adyen-platforms]] — separate current Platforms model.
- [[adyen-account-structure]] — generic company/merchant-account hierarchy.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/account-structure/2026-09-15|Classic Platforms account structure, captured 2026-09-15]]
