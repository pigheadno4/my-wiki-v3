---
title: "Onboard and verify users | Adyen Classic Platforms"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/onboard-users"
raw_files:
  - "adyen/docs/classic-platforms/onboard-users/2026-09-15.md"
tags: [adyen, classic-platforms, onboarding, verification, payouts]
---

## Overview

This 2020-modified, 2026-09-15-captured [[adyen]] [[adyen-classic-platforms]] guide describes verification choices for Classic sub-merchant account holders before payouts can be enabled. It explicitly routes new implementations to a separate new-integration guide. Its Classic Account API `/checkAccountHolder`, account-holder tiers and notifications should be read in the Classic model, separate from the newer Adyen for Platforms resources.

## Key takeaways

- A platform chooses when to collect required information: upfront, immediately after account-holder creation, or in staggered tiers as processing volume increases. It also chooses Adyen's Hosted Onboarding Page or a custom application that sends collected information through the API. Adyen says it conducts verification after receiving the information; upfront verification must be enabled through Support. See raw **Onboard and verify users**, **Upfront verification**, and **Onboarding options** (lines 19–34, 232–247).
- In the staggered approach, processing tiers reflect funds processed and payout tiers reflect passed checks. Country, legal entity and processing volume shape the tiers/limits. A higher processing tier disables payouts and triggers additional checks; missing or incorrect information leads to `ACCOUNT_HOLDER_UPDATED` and `ACCOUNT_HOLDER_VERIFICATION` notifications. Payouts resume at a higher payout tier after Adyen validates sufficient data successfully. See raw **Staggered verification** and **Verification tiers** (lines 36–51).
- `POST /checkAccountHolder` with `accountStateType: Payout` and a selected `tier` proactively checks the holder while preserving the current payout state if information is insufficient or checks fail. `accountStateType: Processing` forces immediate checks and permits payouts only if verification succeeds; on insufficient data or failure, payouts are disabled and the platform must collect details and call `/checkAccountHolder` again. See raw **Precheck the required information** and its two tabs (lines 53–97, 138–175). A successful request response example is not itself verification success or a completed payout.

## Detail locators

- The Payout precheck test-environment Account API v6 request/response and status-change sample are at raw lines 62–136.
- The Processing forced-verification test-environment request/response and status-change sample are at raw lines 138–230. The samples describe status fields; actual outcomes are communicated by `ACCOUNT_HOLDER_VERIFICATION` and `ACCOUNT_HOLDER_STATUS_CHANGE` notifications (lines 94–97, 172–175).
- The Hosted Onboarding Page and custom-onboarding routes are listed at raw lines 232–247.

## Related

- [[adyen-classic-platforms]] — Classic model, money flow, and other source routes.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/onboard-users/2026-09-15|Onboard and verify users, captured 2026-09-15]]
