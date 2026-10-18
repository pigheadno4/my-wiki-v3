---
title: "Additional user interface requirements for Capital | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/compliance-financial-products/user-interface/capital-requirements"
raw_files:
  - "adyen/docs/platforms/compliance-financial-products/user-interface/capital-requirements/2026-09-15.md"
tags: [adyen, platforms, capital, financial-products, compliance, user-interface]
---

## Overview

This 2023-modified, 2026-09-15-captured [[adyen]] for Platforms compliance-guideline page adds Capital-specific user-interface requirements on top of the general financial-products UI requirements. It covers offer presentation, KYC and terms, funded-grant insights, security and Ireland-specific precontract disclosures. The page expressly disclaims legal advice. Use [[adyen-capital]] for the product route and [[adyen-financial-products]] for the umbrella context; this dated guidance is not approval, current legal advice, a financing offer or evidence of grant funding.

## Key takeaways

- The platform must also meet the general financial-products UI requirements. For an eligible user's financing offer, the Capital UI must identify the contract type (such as business loan), display the financing-offer fields Adyen supplies for dynamic and static offers, explain that a business loan has a maximum fixed repayment period, and provide a user request action before an offer is received. The example screen distinguishes loan from cash advance, available offers and validity period; it is an illustration, not a universal offer or country-eligibility promise. [Raw: lines 19–41]
- The interface must collect KYC data for Adyen review and show relevant offer terms, including financing amount, total repayment amount, repayment percentage, product fee and applicable alternative repayment methods. The captured page says that in Canada the fee must be shown as an annual interest rate. It separately requires Capital user terms to be available and accepted once, with updates communicated, and enables viewing/acceptance of Capital Terms of Service with all acceptance information captured. Its example says UI acceptance is equivalent to signing a contract; acceptance evidence must not be conflated with Adyen approval or successful disbursement. [Raw: lines 43–78]
- The UI must inform users in real time about Capital funds paid out and repayments and let them monitor balance, repayment requirements, repaid funds and term. The example points to Capital API `GET /grants/{grantId}` plus Capital and Transfer webhooks for grant details; a displayed state or API route description alone is not proof a particular grant was funded, repaid or legally discharged. [Raw: lines 80–100]
- The Capital UI must be protected against unauthorized access and security breaches with reasonable measures such as personal login credentials, safe transmission and validation at access. These are examples of the captured page's security guidance, not a security certification. [Raw: lines 102–108]
- For Ireland, before the user becomes bound by a Capital contract, the page prescribes two Credit Reporting Act/Central Credit Register statements, with a bold boxed notice of at least the size of other text for credit applications/agreements of €500 and above. It also calls for display of Capital Balance and offer-validity length and a tick-box consent statement. Use the raw wording and formatting requirements, and verify current Irish law and applicable product terms before operational use. [Raw: lines 110–123]

## Detail locators

- Disclaimer, general-UI prerequisite, offer fields and illustrative screen: raw lines 19–41.
- KYC, term fields, Canada fee expression, user terms, ToS acceptance and example contract-signing text: raw lines 43–78.
- Disbursement/repayment insight fields, GET grant path, webhook routes and security examples: raw lines 80–108.
- Ireland-specific precontract statements, visual notice, balance/validity fields and tick-box wording: raw lines 110–123.

## Related

- [[adyen-capital]] — Capital product and grant lifecycle boundary
- [[adyen-financial-products]] — umbrella product family
- [General requirements for user interfaces](https://docs.adyen.com/platforms/compliance-financial-products/user-interface) — prerequisite guide
- [Overview of compliance guidelines](https://docs.adyen.com/platforms/compliance-financial-products) — parent guide
- [Keeping records](https://docs.adyen.com/platforms/compliance-financial-products/keeping-records) — linked recordkeeping guidance

## Raw Sources

- [[raw/adyen/docs/platforms/compliance-financial-products/user-interface/capital-requirements/2026-09-15|Adyen Capital UI requirements — collected 2026-09-15]]
