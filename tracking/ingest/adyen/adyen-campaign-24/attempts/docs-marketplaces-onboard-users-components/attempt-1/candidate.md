---
title: "Adyen Marketplace onboarding components overview"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/onboard-users/components"
raw_files:
  - "adyen/docs/marketplaces/onboard-users/components/2026-09-15.md"
tags: [adyen, marketplaces, platforms, onboarding, components]
---

## Overview

This 2024-modified page captured 2026-09-15 introduces Adyen's prebuilt **Marketplace onboarding UI components**. In a marketplace UI, a component can collect user data and create its relevant resource, reducing the need for the platform to implement that particular resource-creation API call. The components are compatible only with legal entities created using **Legal Entity Management API v3 or v4**; they cover only part of an API-only onboarding flow and do not themselves establish completed verification. [[adyen]] [[adyen-platforms]]

## Key takeaways

- Adyen recommends the components for API-only onboarding to reduce build effort, but the platform still has to implement API calls for other flow steps. The page also offers them as a way for users who were hosted-onboarded to manage submitted data inside the platform's UI. Select component type and library version for the integration; guidance and features may differ across library versions (raw lines 19–33).
- The linked **Individual legal entity** component is presented for personal details, identity-document submission, status view and detail updates. The **Terms of Service** component is presented for viewing/accepting required documents, monitoring status and downloading signed copies. The **Transfer Instrument** component is presented for adding bank accounts for transfers and verification via permissions or document upload. These are descriptions and links to separate component guides, not complete behavior, eligibility or successful-verification evidence from this overview (raw lines 35–53).
- Component submission/resource creation, displayed status and a linked verification path are different from a passed KYC check, activated capability or payout. This page supplies no end-to-end status transition, verification-result evidence, regional eligibility matrix or signed document itself (raw lines 17–23, 35–53).

## Detail locators

- LEM v3/v4 compatibility, component-created resource, incomplete API-only coverage, hosted-management use and library-version caution: raw lines 17–33.
- Individual legal-entity, Terms of Service and Transfer Instrument component navigation/descriptions: raw lines 35–53. Onboarding-steps and library-index routes: lines 55–58.

## Related

- [[adyen]] — provider.
- [[adyen-platforms]] — modern Platforms model and Marketplace route.
- [[source-adyen-docs-marketplaces-onboard-users]] — hosted versus API-only onboarding overview.
- [[source-adyen-docs-marketplaces-onboard-users-terms-of-service]] — separate Terms of Service acceptance procedure.
- [[source-adyen-docs-platforms-onboard-users-components]] — separate Platforms-path component guide.

## Raw Sources

- [[raw/adyen/docs/marketplaces/onboard-users/components/2026-09-15|Marketplace onboarding components — 2026-09-15 snapshot]]
