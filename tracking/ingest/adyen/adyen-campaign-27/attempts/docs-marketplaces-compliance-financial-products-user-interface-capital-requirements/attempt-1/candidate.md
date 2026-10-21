---
title: "Marketplace Capital-specific user interface requirements"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/compliance-financial-products/user-interface/capital-requirements"
raw_files:
  - "adyen/docs/marketplaces/compliance-financial-products/user-interface/capital-requirements/2026-09-15.md"
tags: [adyen, marketplaces, capital, financial-products, compliance, user-interface]
---

## Overview

This Marketplace Capital-specific UI guideline, last modified 2023-12-12 and captured 2026-09-15, supplements the general Marketplace financial-products UI requirements. It expressly disclaims legal advice. Its offer, terms, information-access and Ireland disclosure guidance is historical source evidence, not current legal advice, user eligibility, accepted terms, funded grant or repayment proof. See [[adyen]], [[adyen-capital]] and [[adyen-financial-products]] (raw lines 5–21).

## Key takeaways

- For **eligible users**, the interface should show the financing contract type, all fields Adyen provides for dynamic/static offers, a business loan's **maximum/fixed repayment period**, and how to request Capital. The page says users must request the product before receiving any financing offer. The displayed example illustrates loan-versus-cash-advance labeling, offer options, a Request button and validity period; it is not evidence of a particular offer or grant (raw lines 23–43).
- The interface should collect KYC information for Adyen review and present offer-specific terms: financing amount, total repayment, repayment percentage, fee, and any Adyen alternative repayment methods. **Canada** requires displaying that fee as an annual interest rate. Capital user terms are to be available and accepted once, with updates communicated to users; the UI must let users view and accept relevant Terms of Service and capture all acceptance information. If required Terms of Service cannot be generated, the page directs the marketplace to its Adyen contact (raw lines 45–79).
- The interface should provide real-time information about paid-out Capital funds and repayments and let users monitor balance, repayment requirements, repaid funds and term. The page points to Capital GET grant details plus Capital and Transfer webhooks as data paths; an example insight screen or API route alone does not prove disbursement, repayment or current balances. It also calls for reasonable access controls, including unique personal login credentials, secure transmission and validation at access (raw lines 81–108).
- **Ireland only:** before the user becomes bound by the Capital contract, the interface must display the specified credit-reporting statements, including a styled Central Credit Register notice for applications/agreements of **€500 and above**, the total amount lent and offer-validity length, then prompt tick-box consent to the specified Capital understanding statement. Exact wording and formatting remain in the pinned raw (raw lines 110–123).

## Detail locators

- General UI prerequisite and offer presentation/example: raw lines 19–43.
- KYC, offer terms, Canada fee, Capital terms and acceptance: raw lines 45–79.
- Fund/repayment insights, API/webhook pointers and access security: raw lines 81–108.
- Ireland precontract disclosure, amount/validity and tick-box consent: raw lines 110–123.

## Related

- [[source-adyen-docs-marketplaces-compliance-financial-products-user-interface]]
- [[source-adyen-docs-capital-user-interface]]
- [[source-adyen-docs-platforms-compliance-financial-products-user-interface-capital-requirements]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/compliance-financial-products/user-interface/capital-requirements/2026-09-15|Pinned Marketplace Capital UI requirements]]
