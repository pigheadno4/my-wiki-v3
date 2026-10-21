# C24 query checks — docs-marketplaces-verification-overview-data-review-process

## Q1 — Purpose and prerequisites
Q: How does a Marketplace platform handle an Adyen periodic data review, and when can it proactively request one?
A: Adyen may require review of a user's main/associated entity data and reports requirements through an account-holder webhook. A platform may proactively POST /legalEntities/{id}/requestPeriodicReview only for onboarding v3/v4 and an eligible user; HTTP 204 is followed by a review-required webhook. Ineligibility examples and 422 messages are listed in raw/adyen/docs/marketplaces/verification-overview/data-review-process/2026-09-15.md:104-195. The user must confirm data and resolve all verification errors before finalization (raw/adyen/docs/marketplaces/verification-overview/data-review-process/2026-09-15.md:19-31).
Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-verification-overview-data-review-process]] → [[raw/adyen/docs/marketplaces/verification-overview/data-review-process/2026-09-15]].

## Q2 — Deadline and outcome boundary
Q: Does invalid verification immediately disallow a capability, and does confirmation alone establish valid verification?
A: No. The review-required webhook shows verificationStatus invalid while allowed remains true during an active deadline; failure to confirm and resolve errors causes disallowance. Hosted Submit review or API confirmDataReview resolves the review-confirmation error and returns a confirmation timestamp, but Adyen later sends a separate verification-result webhook; invalid results may still show allowed false or true with a deadline and problems. See raw/adyen/docs/marketplaces/verification-overview/data-review-process/2026-09-15.md:31-45, :203-223, :233-285.
Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-verification-overview-data-review-process]] → [[raw/adyen/docs/marketplaces/verification-overview/data-review-process/2026-09-15]].
