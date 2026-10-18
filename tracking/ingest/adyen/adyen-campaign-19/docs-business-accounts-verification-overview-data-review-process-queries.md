# Fixed retrieval checks — periodic data reviews

Q1. What is reviewed, when is it finalized, and what must not be inferred?
- Expected: A 2023-modified, 2026-09-15-captured Business accounts review of main legal-entity/legal-arrangement and associated UBO/signatory data, triggered by Adyen or eligible proactive request. Existing data gets immediate checks; user must confirm and resolve **all** verification errors to finalize. A `204` request response, `dataReviewedAt` timestamp or TEST webhook does not prove passed KYC, opened account or successful transfer.
- Raw locators: `raw/adyen/docs/business-accounts/verification-overview/data-review-process/2026-09-15.md:15-31`, `:104-120`, `:197-245`.
- Canonical URL: `https://docs.adyen.com/business-accounts/verification-overview/data-review-process`.
- Forward route: `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-business-accounts]]` → `wiki/sources/adyen/source-adyen-docs-business-accounts-verification-overview-data-review-process.md` → `[[raw/adyen/docs/business-accounts/verification-overview/data-review-process/2026-09-15]]`.

Q2. How do deadline status, proactive-request eligibility, user confirmation and result webhooks differ?
- Expected: Review-required account-holder webhook names `verificationStatus=invalid`, `allowed=true` for previously allowed capability during deadline, error `3_10`, action `3_100`, and per-capability `verificationDeadlines`; unresolved data/errors can disallow after deadline. Proactive request is onboarding v3/v4 only, via legal-entity ID; ineligible cases include next scheduled review >1 year, onboarding <180 days or recent review <180 days and can yield 422. Hosted user checks box/Submits; API-only UI presents main/associated/supporting data and calls confirmDataReview after user confirmation. Adyen then re-verifies and sends valid/allowed true or invalid/allowed false or deadline-true results. Transfer-instrument problems require separate feature enablement; `x-requested-verification-code` is TEST simulation, not live retry authorization.
- Raw locators: `raw/adyen/docs/business-accounts/verification-overview/data-review-process/2026-09-15.md:31-45`, `:104-132`, `:191-245`, `:247-363`.
- Canonical URL: `https://docs.adyen.com/business-accounts/verification-overview/data-review-process`.
- Forward route: `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-business-accounts]]` → `wiki/sources/adyen/source-adyen-docs-business-accounts-verification-overview-data-review-process.md` → `[[raw/adyen/docs/business-accounts/verification-overview/data-review-process/2026-09-15]]`.
