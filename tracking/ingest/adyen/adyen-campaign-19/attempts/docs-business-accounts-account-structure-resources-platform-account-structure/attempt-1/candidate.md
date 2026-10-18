---
title: "Adyen Business Accounts: Platform account structure"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/account-structure-resources/platform-account-structure"
raw_files:
  - "adyen/docs/business-accounts/account-structure-resources/platform-account-structure/2026-09-15.md"
tags: [adyen, business-accounts, platforms, account-structure, balance-accounts]
---

## Overview

This 2026-09-15-modified [[adyen]] Business Accounts page maps platform-owned and user-owned resources in a food-delivery example. It distinguishes the platform's company/merchant/balance-platform/liable resources from each user's stores, account holders, balance accounts, legal entities, business lines, transfer instruments and Business Account payment instruments. The diagram and example describe configuration; they do not prove bank ownership, verified onboarding, an opened account, live balances or completed supplier payments. [[adyen-business-accounts]]

## Key takeaways

- The page states that scheme-regulation compliance requires a balance platform and merchant account in each region where the platform is registered and wishes to process transactions (raw line 23). In its illustration, platform resources include a company account, merchant accounts organized by country/region, two balance platforms labelled EU and US, a liable account holder and liable balance account for platform funds, and a legal entity in each acquiring region (raw lines 29–46). The named examples do not establish universal resource counts or present regional eligibility.
- User-side resources include stores tied to relevant merchant accounts; at least one account holder per country of operation to define transfer capabilities; at least one balance account per account holder with base currency to hold the user's funds; a transfer instrument described as a verified payout bank account for each balance account; and a legal entity and business line in each operating country for verification/business information (raw lines 48–66). These are model relationships, not evidence that verification, payout routing or a bank transfer succeeded.
- The page separately describes one or more balance accounts per account holder to link to Business Account payment instruments and says that linked balance account must be separate from the balance account that holds the user's funds (raw line 60). It describes a Business Account payment instrument for each restaurant, with transactions processed using funds in a user's balance account (raw lines 68–70). Keep the page's own different balance-account roles explicit; do not collapse the liable platform account, user's funds account, linked instrument account, and external transfer instrument.
- **Unresolved cardinality conflict:** This structure page says multiple Business Accounts can link to the same balance account (raw line 60). The separately captured Create business accounts guide says a balance account can have only one Business Account number and the API errors if one already exists (raw `business-accounts/create-business-accounts/2026-09-15.md` line 46); the integration checklist also says one `bankAccount` payment instrument per balance account (raw `business-accounts/integration-checklist/2026-09-15.md` line 48). Do not implement multi-number routing from this example without current product/API confirmation.

## Detail locators

- Regional platform/account requirement and illustrative use case: raw lines 21–27.
- Platform-owned company, merchant, balance platform, liable and legal-entity resources: raw lines 29–46.
- User-owned stores, account holders, distinct balance-account roles, transfer instruments, KYC and business lines: raw lines 48–70.
- Diagram reference: raw lines 72–76.

## Related

- [[adyen-business-accounts]]
- [[source-adyen-docs-business-accounts-account-structure-resources]] — parent resource map.
- [[source-adyen-docs-business-accounts-create-business-accounts]] — conflicting one-number-per-balance-account creation guide.
- [[source-adyen-docs-business-accounts-integration-checklist]] — conflicting one-bankAccount-instrument-per-balance-account checklist.
- [[source-adyen-docs-business-accounts-manage-balance-accounts]] — balance-account operations.

## Raw Sources

- [[raw/adyen/docs/business-accounts/account-structure-resources/platform-account-structure/2026-09-15|Captured platform account-structure guide]]
