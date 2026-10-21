---
title: "Adyen Marketplaces upfront and staggered verification"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/verification-overview/verification-types"
raw_files:
  - "adyen/docs/marketplaces/verification-overview/verification-types/2026-09-15.md"
tags: [adyen, marketplaces, platforms, verification, onboarding, payouts]
---

## Overview

This 2026-09-15 **Marketplaces / Adyen for Platforms** page contrasts **upfront** and **staggered** collection of user-verification data. It says staggered verification is the Marketplace default and upfront can be enabled, while a separately captured general Platforms guide gives different default/eligibility advice. The page describes verification choices and conditional permissions, not a specific account holder’s KYC approval, enabled capability, payout or bank receipt. [[adyen-platforms]]

## Verification paths

- **Upfront** requires full verification before payments and payouts. Collect all required information at onboarding, then Adyen verifies it after account-holder creation; the guide says no new information is needed solely on reaching a higher tier. To enable upfront for an account holder, POST `/legalEntities` or PATCH `/legalEntities/{id}` with `verificationPlan: upfront` in the LEM API. A request to set the plan is not an approved capability. See [[raw/adyen/docs/marketplaces/verification-overview/verification-types/2026-09-15|raw lines 19–30]].
- **Staggered**, described here as the default, starts with a minimum determined by volume, country/region and other factors. Higher-tier movement requires additional information and Adyen checks to enable or continue account-holder payouts. On moving up, payouts are **temporarily disallowed** until required data is provided and verified; Adyen reports the change and needed data by webhook. See [[raw/adyen/docs/marketplaces/verification-overview/verification-types/2026-09-15|raw lines 19–24, 32–38]].
- Four tiers depend on country, legal-entity type and processed amount, but high-risk capability requests or triggered checks can also move a holder to a higher tier. The currency table uses AUD, USD, CAD, NZD, SGD and HKD for the listed countries, and EUR for `Other`; it gives **no numeric tier thresholds**. See [[raw/adyen/docs/marketplaces/verification-overview/verification-types/2026-09-15|raw lines 40–56]].

## Cross-page scope conflict

This Marketplace page says **staggered is applied by default** and upfront can be enabled (raw line 24). The separate [[source-adyen-docs-platforms-verification-overview-verification-types|general Platforms verification-types source]] says platforms should collect data **upfront** and **only payment facilitators** can request staggered through an Adyen contact ([[raw/adyen/docs/platforms/verification-overview/verification-types/2026-09-15|related raw lines 24, 30–32]]). Both captures are dated 2026-09-15 and do not explain whether this is a model-specific entitlement difference or inconsistent guidance. Do not infer an individual platform’s staggered eligibility from either overview alone.

## Detail locators

- Upfront/staggered definitions, Marketplace default and LEM plan setting: [[raw/adyen/docs/marketplaces/verification-overview/verification-types/2026-09-15|raw lines 15–30]].
- Tier payout interruption, webhook, non-volume triggers and currencies: [[raw/adyen/docs/marketplaces/verification-overview/verification-types/2026-09-15|raw lines 32–56]].

## Related

- [[adyen-platforms]] — modern Platforms verification model.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/verification-overview/verification-types/2026-09-15|Marketplace verification types (captured 2026-09-15)]]
