---
title: "Adyen Platforms additional-capabilities verification reference"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/verification-requirements/reference-additional-products"
raw_files:
  - "adyen/docs/platforms/verification-requirements/reference-additional-products/2026-09-15.md"
tags: [adyen, platforms, verification, business-accounts, card-issuing]
---

## Overview

This 2023-modified reference, captured 2026-09-15, lists additional information associated with offering financial products to platform users, especially business accounts, and provides FATCA/CRS, industry-code and source-of-funds values. It is a conditional data reference within [[adyen-platforms]], with [[adyen-financial-products]] as the product-family route.

## Key takeaways

- The page says an existing Adyen for Platforms integration has no additional integration requirements, limitations or preparations (line 23), but separately describes data needed for a financial account (lines 25–34), industry codes for business-account users (lines 98–116), and source of funds for business accounts and card issuing (lines 118–133). Read the first statement in that narrower integration-preparation context.
- For financial-account FATCA/CRS assessment, Adyen describes self-certification and says it need not be repeated unless information changes; the page excludes US-based legal entities applying for US business bank accounts from this self-certification (lines 27–34). The decision tree's classification values and GIIN branch are at lines 36–96; they are historical source guidance, not a current tax or legal determination.
- Business-account requests require a user industry code. Some industries require Adyen approval before onboarding, and new industries outside prior approval require contact with Adyen (lines 98–116). The page routes submission through POST `/businessLines` (line 112).
- Source-of-funds information applies to business accounts and card issuing, using `banking` or `issuing` service on POST `/businessLines`. For funds not processed through Adyen, the page calls for `sourceOfFunds.type` and an origin description; supporting documents may be requested depending on funding type (lines 120–133). The dated document examples and age conditions are in the table at lines 135–224.

## Detail locators

- FATCA/CRS classification branches and API values: lines 36–96.
- Industry-code selection, lists, submission and additional-industry contact: lines 98–116.
- Source-of-funds service/fields and conditional evidence table: lines 118–224.

## Evidence boundary

This snapshot is not proof that a platform or user is eligible for a business account, card issuing or Capital; that an industry was approved; that an account was opened or verified; or that a capability was enabled. Capital is not covered by this reference. The page's legal and document guidance is historical and should not be treated as current compliance advice.

## Related

- [[adyen-platforms]] — current-platform model and onboarding route.
- [[adyen-financial-products]] — separate optional product-family overview.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/verification-requirements/reference-additional-products/2026-09-15|Pinned Adyen additional-capabilities reference, captured 2026-09-15]]
