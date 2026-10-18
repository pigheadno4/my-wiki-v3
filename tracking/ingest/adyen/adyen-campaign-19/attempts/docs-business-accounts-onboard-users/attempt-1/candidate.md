---
title: "Adyen Business accounts user onboarding and verification"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/onboard-users"
raw_files:
  - "adyen/docs/business-accounts/onboard-users/2026-09-15.md"
tags: [adyen, business-accounts, platforms, onboarding, verification]
---

## Overview

This Business accounts guide (last modified 2024-03-04; captured 2026-09-15) describes API-only collection of additional user verification data. It says legal-entity type and operating country determine what to collect, and Adyen's verification begins automatically after submission. Building a UI, creating legal entities/account holders or starting verification does not establish an opened Business account, approved capability, live balance or successful transfer. See [[adyen]], [[adyen-business-accounts]] and [[adyen-platforms]].

## Key takeaways

- **Integration path and account-holder state:** For API-only onboarding, the platform builds its own user UI and submits data through Legal Entity Management and Configuration APIs. The page says an existing Adyen for Platforms integration has no additional general preparations, but Business accounts still require the additional product verification information described here and in linked guides. A new account holder first follows Platforms or marketplace onboarding; an already verified account holder supplies the additional Business accounts information. Supported operating countries are referenced in the product overview rather than established for a particular user here.
- **Onboarding-v4 source of funds:** The v4 subsection applies source-of-funds verification to Business accounts and card Issuing, with a POST businessLines service of banking for Business accounts or issuing for cards. If funds were Adyen processed, the prose sets sourceOfFunds.adyenProcessedFunds true; otherwise it says false plus sourceOfFunds.type and a description of origin. Adyen may ask for proof documents depending on funding source and document age. The table gives examples for business earnings, employment, cryptocurrency, investments, loans, grants, third-party funding and other origins; these are conditional document examples, not an instruction to upload every document for every user. The table's processed-funds row uses businessLines.adyenProcessedFunds, unlike the preceding sourceOfFunds.adyenProcessedFunds prose; verify the field against the applicable API schema rather than silently choosing one.
- **Country-specific financial data:** For EU organizations the v4 section asks for annual turnover or annual balance sheet; for UK organizations it adds employee count and one of those financial figures in POST legalEntities. These are dated country/entity requirements in the guide, not global rules or current account eligibility.
- **Verification and consent boundary:** The guide routes onward to verification requirements/process. Its submitting data triggers checks; it does not describe complete Business accounts Terms acceptance or prove a user's consent. Use the separate Terms of Service guide for signer and acceptance evidence, and verification/capability state for account readiness.

## Detail locators

- Type/country-dependent verification and API-only LEM/Configuration route: pinned raw lines 15–31.
- Onboarding-v4 source-of-funds branch, banking/issuing service and conditional document table: pinned raw lines 33–139.
- EU/UK organization financial fields: pinned raw lines 141–145.
- New versus already-verified account-holder onboarding routes and next-step links: pinned raw lines 147–163.

## Related

- [[adyen-business-accounts]] — main Business accounts concept and reciprocal source route.
- [[adyen-platforms]] — parent Platforms integration.
- [[source-adyen-docs-business-accounts-onboard-users-terms-of-service]] — separate consent/ToS route.

## Raw Sources

- [[raw/adyen/docs/business-accounts/onboard-users/2026-09-15|Adyen Business accounts onboarding guide, captured 2026-09-15]]
