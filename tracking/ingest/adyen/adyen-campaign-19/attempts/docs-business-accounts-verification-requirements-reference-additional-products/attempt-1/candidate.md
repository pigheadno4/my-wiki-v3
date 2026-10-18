---
title: "Reference for additional capabilities | Adyen Business accounts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/verification-requirements/reference-additional-products"
raw_files:
  - "adyen/docs/business-accounts/verification-requirements/reference-additional-products/2026-09-15.md"
tags: [adyen, business-accounts, verification, fatca, industry-codes, source-of-funds]
---

## Overview

This 2023-modified, 2026-09-15-captured [[adyen]] Business accounts reference identifies additional information associated with financial-account verification: FATCA/CRS self-certification, industry codes and source of funds (SOF). The SOF section also applies to card Issuing. See [[adyen-business-accounts]] for the product route. These are dated, conditional information/document routes, not tax advice, a universal field checklist, proof of classification approval, completed KYC or an opened Business account.

## Key takeaways

- The page says Adyen N.V. identifies and reports reportable financial-account holders under FATCA/CRS, requiring a self-certified qualification to determine reportability when opening a financial account. It says no further action is needed after self-certification **unless information changes**. It explicitly exempts **US-based legal entities applying for US business bank accounts** from FATCA/CRS self-certification; do not broaden that exception to every US person, product or account. [Raw: lines 21–30]
- Its decision-tree examples include `nonFinancialActive`, `nonFinancialPassive`, `nonFinancialNonReportable`, and `financialNonReportable` with GIIN. The tree conditions distinguish operational versus passive income and entity categories; where classification is uncertain or disputed, the page directs contact with Adyen. These sample categories do not establish a particular user's tax classification or replace current legal/tax assessment. [Raw: lines 32–92]
- Adyen requires an industry code when requesting Business accounts; the code should reflect the user's business activity and is submitted through a `POST /businessLines` route. Codes are mapped to MCCs and adapted under Adyen rules, and some industries require approval before onboarding. The actual industry/brand-specific code lists live in linked pages. Offering accounts in **new industries** outside a prior approval process requires contacting Adyen or Support; an industry code submission alone is not approval or capability enablement. [Raw: lines 94–109]
- SOF verification is stated for **Business accounts and card Issuing**. `POST /businessLines` uses `service=banking` for Business accounts or `service=issuing` for Issuing. The prose instructs `sourceOfFunds.adyenProcessedFunds=true` for Adyen-processed funds, or false plus `sourceOfFunds.type` and an origin description for other funds. Adyen **may** request supporting documents depending on fund type; the table gives condition-specific accepted categories, content and age windows, rather than a universal upload requirement. [Raw: lines 111–126, 128–217]
- **Field-path inconsistency in the capture:** SOF prose names `sourceOfFunds.adyenProcessedFunds`, while the first table row says `businessLines.adyenProcessedFunds`. The `POST /businessLines` links also point to mixed `latest` and explicit LEM v4 references. Check the actual applicable API schema/version before implementation; do not silently merge the paths or treat the examples as successful verification. [Raw: lines 105, 119–130]

## Detail locators

- FATCA/CRS purpose, self-certification and US legal-entity/US-account exception: raw lines 21–30.
- Classification decision-tree values and contact route: raw lines 32–92.
- Industry-code requirement, approval boundary, linked lists and business-line submission: raw lines 94–109.
- SOF product/service split, Adyen-processed versus external-funds fields, conditional document table and age/content requirements: raw lines 111–217.
- Field-path/version inconsistency: raw lines 105, 119–130.

## Related

- [[adyen-business-accounts]] — Business accounts product and verification boundary
- [Industry code list](https://docs.adyen.com/business-accounts/verification-requirements/reference-additional-products/industry-codes/) — linked codes
- [Brand-specific industry codes](https://docs.adyen.com/business-accounts/verification-requirements/reference-additional-products/brand-specific-industry-codes/) — linked brand-specific codes
- [Business accounts onboarding](https://docs.adyen.com/business-accounts/onboard-users) — linked onboarding context

## Raw Sources

- [[raw/adyen/docs/business-accounts/verification-requirements/reference-additional-products/2026-09-15|Adyen Business accounts additional capabilities reference — collected 2026-09-15]]
