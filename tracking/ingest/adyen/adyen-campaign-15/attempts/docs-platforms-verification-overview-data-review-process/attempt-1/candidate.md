---
title: "Adyen Platforms periodic data-review process"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/verification-overview/data-review-process"
raw_files:
  - "adyen/docs/platforms/verification-overview/data-review-process/2026-09-15.md"
tags: [adyen, platforms, verification, onboarding, data-review]
---

## Overview

Adyen describes periodic reviews in which a platform user confirms that legal-entity and associated-entity data remains current. Adyen may require a review; a platform may optionally request one for an eligible user. After a review is triggered, Adyen checks existing data and reports requirements through an account-holder webhook. See [[adyen]] and [[adyen-platforms]]. This 2026-09-15 documentation capture is a process reference, not evidence of any present user's status, eligibility, approved capability, or payment outcome.

## Key takeaways

- A user with verification errors must update data if needed, resolve the errors, **and** confirm the data; without errors the user still must review and confirm. The review is finalized only after confirmation and resolution of all verification errors. While the deadline is active, capabilities allowed before the review request can remain usable; unresolved errors or missing confirmation cause them to be disallowed at the deadline. See raw lines 19–31.
- The `balancePlatform.accountHolder.updated` review-required webhook identifies a `3_10` “Review of data is required” error and `3_100` confirmation action, with `verificationStatus=invalid`, `allowed=true`, and `verificationDeadlines`. These fields have different meanings: invalid verification does not itself mean the capability is already disallowed. The example's account holder, legal entity IDs, `sendToBalanceAccount` capability, deadline timestamp and test environment are illustrative. See raw lines 33–102.
- Optional proactive requests use POST `/legalEntities/{id}/requestPeriodicReview` with the **user legal entity ID**, and are available only for onboarding v3 or v4. A 204 means the request succeeded; the subsequent webhook conveys review requirements. Adyen says an ineligible request is not activated, with example reasons including next scheduled review more than one year away, onboarding within 180 days, or a previous review within 180 days; the page documents 422 errors. Adyen may also require review outside the scheduled period after significant information/risk changes. See raw lines 104–195.
- Hosted onboarding presents a summary/Submit review flow after the platform reviews and, if needed, updates submitted data. API-only onboarding requires presenting the user and associated entities' information, gathering supporting resources as relevant, updating as needed, and POSTing `/legalEntities/{id}/confirmDataReview` after user confirmation. Its `dataReviewedAt` response is a confirmation timestamp, not a valid-verification result. See raw lines 197–237.
- After submission, Adyen reports verification results through another account-holder webhook. Valid checks show `verificationStatus=valid` and `allowed=true`; invalid checks can show `allowed=false` or `allowed=true` with a deadline and unresolved `problems`. The platform must address returned verification errors. Transfer-instrument-resource problems require Adyen contact to enable that view. See raw lines 239–339.

## Detail locators

- **Review-required notification and object identities:** raw lines 33–102; the sample's account holder links a legal entity, while a `problems.entity` entry identifies the affected legal entity.
- **Optional request and rejection messages:** raw lines 104–195, especially onboarding-version gate at 106, eligibility cases at 110–117, request/204 at 119–122, and troubleshooting at 191–195.
- **Hosted and API-only user review:** raw lines 197–237. The user confirms; the platform retrieves/updates data and, in API-only mode, calls the confirmation endpoint.
- **Valid/invalid result branches:** raw lines 239–339, including status and allowed distinctions at 247–289. Sample webhook values are illustrative, not current account proof.
- **Test-only flow:** raw lines 341–363. The documented `x-requested-verification-code: 3_10` PATCH scenario requires the account holder's capabilities to already be allowed; it is a test recipe, not an operation performed here.

## Related

- [[adyen-platforms]] — platform user-onboarding and verification context.
- [[source-adyen-docs-platforms-kyc-verification-codes-general-verification-errors]] — general error-code `3_10` lookup.
- [[source-adyen-docs-platforms-kyc-verification-codes-sub-errors]] — granular verification suberror lookup.

## Raw Sources

- [[raw/adyen/docs/platforms/verification-overview/data-review-process/2026-09-15|Adyen Periodic data reviews, fetched 2026-09-15]]
