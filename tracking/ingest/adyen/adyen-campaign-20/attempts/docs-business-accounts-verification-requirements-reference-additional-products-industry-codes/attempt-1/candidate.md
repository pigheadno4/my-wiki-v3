---
title: "Adyen Business Accounts: Industry codes list"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/verification-requirements/reference-additional-products/industry-codes"
raw_files:
  - "adyen/docs/business-accounts/verification-requirements/reference-additional-products/industry-codes/2026-09-15.md"
tags: [adyen, business-accounts, verification, industry-codes, mcc]
---

## Overview

This 2026-09-15-captured Business Accounts reference tells a platform to choose the Industry Code (IC) that best represents a user's business activity. Adyen says it maps ICs to Merchant Category Codes (MCCs) under its internal rules, with some MCCs corresponding to more than one IC. The captured raw page contains **no actual code/value list**, despite saying only the following values are accepted. It cannot be used to select a permitted code or establish approval for a user's industry. [[adyen-business-accounts]] [[adyen]]

## Key takeaways

- Accurate IC selection is consequential because the mapping from MCC to IC is not one-to-one. The page directs contact with Adyen or Support if an industry code requires approval before onboarding, or if the platform wants to offer Business Accounts in new industries outside a previous approval process (raw lines 17–24). It does not say that submitting a code grants approval, capability or an opened account.
- The capture states “We only accept the following values for industry codes,” but no values or table follow; only three unanchored footnotes appear before the next heading (raw lines 26–36). The footnotes mention an average transaction value of EUR 2,000 or less, CBD/kava/baby-food inclusion and an American Express exclusion, but no industry codes are attached to them in this raw. Do not apply any footnote to a specific business or code.
- This page is a thin Business Accounts child reference. The parent additional-products guide supplies the separate `POST /businessLines` submission context; the present raw does not specify that endpoint, its fields, or a current accepted-code list. The final link points to a separate brand-specific industry-code list (raw lines 34–36).

## Detail locators

- IC purpose, MCC mapping and selection warning: raw lines 15–19.
- Prior approval and new-industry contact boundary: raw lines 21–24.
- Missing accepted-values list, orphaned footnotes and brand-specific link: raw lines 26–36.

## Related

- [[adyen-business-accounts]] — Business Accounts product and verification context.
- [[source-adyen-docs-business-accounts-verification-requirements-reference-additional-products]] — parent guide with industry-code submission context.
- [Brand-specific industry codes](https://docs.adyen.com/business-accounts/verification-requirements/reference-additional-products/brand-specific-industry-codes/) — linked, unread navigation; no values inferred here.

## Raw Sources

- [[raw/adyen/docs/business-accounts/verification-requirements/reference-additional-products/industry-codes/2026-09-15|Captured industry codes list page]]
