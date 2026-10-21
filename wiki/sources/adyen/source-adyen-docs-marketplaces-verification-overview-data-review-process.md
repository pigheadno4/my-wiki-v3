---
title: "Adyen Marketplaces periodic data reviews"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/verification-overview/data-review-process"
raw_files:
  - "adyen/docs/marketplaces/verification-overview/data-review-process/2026-09-15.md"
tags: [adyen, marketplaces, platforms, verification, onboarding, data-review]
---

## Overview

This 2023-modified page, captured 2026-09-15 under the Marketplaces route of [[adyen-platforms]], describes periodic user-data reviews. [[adyen]] may require a user to review and confirm legal-entity and associated-entity information, or a platform may proactively request a review for an eligible user. Triggering a review runs checks on existing data and produces account-holder webhook requirements. The page is process guidance, not an account-specific verification result.

## Key takeaways

- A user with verification errors must update data if needed, resolve the errors, **and** confirm it. A user without errors still must review and confirm. A review is finalized only after confirmation and resolution of all verification errors. During the stated deadline, previously allowed capabilities can continue; failure to confirm and resolve errors leads to disallowance. See raw lines 19–31.
- A review-required `balancePlatform.accountHolder.updated` webhook reports `verificationStatus=invalid` while `allowed=true`, error `3_10`, action `3_100`, and `verificationDeadlines` for capabilities at risk. Invalid verification and current allowance are distinct states; the sample IDs, capability and TEST timestamp are illustrative. See raw lines 33–102.
- Optional proactive POST `/legalEntities/{id}/requestPeriodicReview` uses the user's legal-entity ID and is available only with onboarding v3 or v4. A successful request receives HTTP 204; the ensuing webhook reports review requirements. Adyen may independently request a review outside schedule after significant information or risk changes. Ineligible requests are not activated: examples include a next scheduled review more than a year away, onboarding within 180 days, or a last review within 180 days. The page lists 422 rejection messages. See raw lines 104–195.
- Hosted onboarding uses a summary page and user **Submit review** confirmation after any needed data updates. API-only onboarding requires presenting the main and associated entities' information, retrieving supporting resources as relevant, updating data if needed, and POSTing `/legalEntities/{id}/confirmDataReview` only after user confirmation. Its `dataReviewedAt` response gives confirmation time, not valid-verification proof. See raw lines 197–231.
- After submission, another account-holder webhook reports Adyen's verification result. A valid check has `verificationStatus=valid` and `allowed=true`; an invalid check may have `allowed=false` or `allowed=true` with a deadline, plus errors to resolve. Transfer-instrument-resource problem visibility requires Adyen contact to enable it. The `x-requested-verification-code: 3_10` PATCH recipe is for testing, requiring an account holder with already allowed capabilities; it does not demonstrate a live outcome. See raw lines 233–357.

## Detail locators

- Review trigger, error/no-error user obligations and deadline effect: raw lines 19–31.
- Review-required webhook fields and TEST example: raw lines 33–102.
- v3/v4 proactive request, eligibility and 422 errors: raw lines 104–195.
- Hosted and API-only user confirmation: raw lines 197–231.
- Valid/invalid verification webhook branches and transfer-instrument visibility: raw lines 233–333.
- Test-only forced `3_10` flow: raw lines 335–357.

## Related

- [[adyen]] — provider profile.
- [[adyen-platforms]] — modern Platforms and Marketplaces verification context.
- [[source-adyen-docs-marketplaces-kyc-verification-codes-general-verification-errors]] — Marketplace-path general error code `3_10`.
- [[source-adyen-docs-platforms-verification-overview-data-review-process]] — separate Platforms URL with closely related guidance; preserve source provenance.
- [[adyen-classic-platforms]] — legacy Classic Platforms, a distinct resource model.

## Raw Sources

- [[raw/adyen/docs/marketplaces/verification-overview/data-review-process/2026-09-15|Periodic data reviews — pinned 2026-09-15 raw snapshot]]
