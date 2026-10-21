---
title: "Adyen Marketplaces additional-capability verification reference"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/verification-requirements/reference-additional-products"
raw_files:
  - "adyen/docs/marketplaces/verification-requirements/reference-additional-products/2026-09-15.md"
tags: [adyen, marketplaces, platforms, financial-products, verification]
---

## Overview

This 2023-modified page captured 2026-09-15 is a **Marketplace-path Adyen for Platforms reference** for extra information used when offering financial products such as business accounts. It points to possible FATCA/CRS self-certification values, industry codes, and source-of-funds information when creating legal entities and business lines. It is a data-collection reference, not proof that a user is eligible, verified or approved for a financial account. [[adyen]] [[adyen-platforms]]

## Key takeaways

- The Requirements section says an existing Adyen for Platforms integration has no additional requirements, limitations or preparations. Read that narrow setup statement alongside the page's later **product-specific information obligations**: FATCA/CRS self-certification for a financial-account application (with an exception), industry codes for business-account requests, and source-of-funds data. The broad sentence must not be used to skip those later conditions (raw lines 19–34, 98–120).
- For a financial account, the page says Adyen requires self-certified FATCA/CRS qualification to determine reportability; after certification, it says no further action is required unless information changes. It expressly exempts US-based legal entities applying for **US business bank accounts** from FATCA/CRS self-certification. These statements are from a 2023-modified product document, not a determination of current tax law or an individual user's reportable status (raw lines 25–34).
- The rendered decision tree offers `nonFinancialActive`, `nonFinancialPassive`, `nonFinancialNonReportable`, and `financialNonReportable` with GIIN in described branches. It directs uncertain or disputed classifications to Adyen. Its nesting is irregular in the captured Markdown; use the raw decision tree and Adyen guidance rather than treating the indentation as a universal automated classifier (raw lines 36–96).
- For business accounts, provide an industry code for the user's line of business. The page distinguishes marketplace payment-processing activity from a business-account user's locally registered industry, points to general and brand-specific code lists, and says some industries require approval before onboarding. Submit the best-representing code through POST `/businessLines`; contact Adyen or Support before offering business accounts in **new industries** outside the previous approval process (raw lines 98–116).
- The source-of-funds section routes submission through POST `/businessLines`. The captured table lists only a Business/commercial-profits row, specifying the main source as the payments-acquiring business with Adyen; it is not an exhaustive source-of-funds taxonomy (raw lines 118–124).

## Detail locators

- Reference identity, scope and broad Requirements sentence: raw lines 15–23. FATCA/CRS rationale, certification, US-based/US-business-bank-account exception and decision tree: lines 25–96.
- Industry-code purpose, two business-activity meanings, possible approval, code-list routes, `/businessLines` submission and new-industry contact: lines 98–116. Source-of-funds route and sole displayed row: lines 118–124.

## Related

- [[adyen]] — provider.
- [[adyen-platforms]] — modern Platforms model and Marketplace route.
- [[source-adyen-docs-marketplaces]] — marketplace integration overview.
- [[source-adyen-docs-platforms-financial-products]] — separate financial-product overview; this page does not establish grants or availability.
- [[adyen-classic-platforms]] — distinct legacy integration.

## Raw Sources

- [[raw/adyen/docs/marketplaces/verification-requirements/reference-additional-products/2026-09-15|Marketplace additional-capability verification reference — 2026-09-15 snapshot]]
