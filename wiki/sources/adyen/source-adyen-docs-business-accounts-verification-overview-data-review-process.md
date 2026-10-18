---
title: "Periodic data reviews | Adyen Business accounts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/verification-overview/data-review-process"
raw_files:
  - "adyen/docs/business-accounts/verification-overview/data-review-process/2026-09-15.md"
tags: [adyen, business-accounts, verification, data-review, capabilities]
---

## Overview

This 2023-modified, 2026-09-15-captured [[adyen]] Business accounts guide explains periodic review of a user's existing legal-entity and associated-entity data. Adyen can require a review; a platform using eligible onboarding versions can request one proactively. The flow links a legal-entity review to account-holder capability verification and deadline webhooks. See [[adyen-business-accounts]] for the product route. A request, confirmation timestamp or example webhook is not evidence that a specific user's KYC passed or that a Business account is open.

## Key takeaways

- On trigger, Adyen immediately checks existing main legal-entity/legal-arrangement and associated-entity data, including UBOs and signatories. If errors exist, the user must update data as needed, resolve errors and confirm; without errors, review and confirmation suffice. Updating data triggers re-verification. The review is finalized only after **both** user confirmation and resolution of every verification error. [Raw: lines 19–31]
- The `balancePlatform.accountHolder.updated` review-required webhook uses capability `verificationStatus=invalid` while `allowed` remains `true` during the deadline for previously allowed capabilities; it includes verification error `3_10`, action `3_100`, and `verificationDeadlines` identifying the capability/disallow date. If data is not confirmed and errors resolved by the deadline, the capabilities are disallowed. Thus `invalid` does not always mean immediate loss of `allowed`, and an active account-holder status in an example does not override capability-level checks. [Raw: lines 31–45, 47–101]
- Optional proactive request is available **only for onboarding v3 or v4** via `POST /legalEntities/{id}/requestPeriodicReview`. A successful request returns `204`, then the review-required webhook supplies status/deadline. Adyen may require a review outside schedule for significant data/risk changes. The guide says ineligible requests are not activated, including a next review more than a year away, onboarding within 180 days or a review in the prior 180 days; troubleshooting shows `422` reasons. A `204` is request acceptance, not user confirmation or passed verification. [Raw: lines 104–132, 191–195]
- The platform must tell the user to review by the deadline. Hosted onboarding can pre-read/patch submitted data, then the user confirms with checkbox and **Submit review**. API-only onboarding presents main/associated legal entities and supporting transfer-instrument, business-line and store data, patches changes if needed, then calls `POST /legalEntities/{id}/confirmDataReview` on user confirmation; `dataReviewedAt` is a confirmation time, not approval. [Raw: lines 197–237]
- After submission Adyen verifies and sends results by account-holder update webhook. A valid result has capability `verificationStatus=valid` and `allowed=true`; an invalid result may have `allowed=false` or temporary `allowed=true` with a deadline and problem arrays requiring remediation. Viewing problems on a transfer-instrument resource requires enabling that feature through an Adyen contact. The test flow's `x-requested-verification-code: 3_10` header is a simulated outstanding review for an already-allowed account holder, not a live remediation/retry instruction. [Raw: lines 239–363]

## Detail locators

- Review trigger, entity scope, error/no-error conditions and deadline consequence: raw lines 19–31.
- Required webhook fields, capability scope, `3_10` error versus `3_100` action and TEST example: raw lines 33–101.
- Onboarding-version gate, proactive request, `204` and `422` ineligibility: raw lines 104–195.
- Hosted/API-only review and user-confirmation routes: raw lines 197–237.
- Post-review valid/invalid webhook states and simulation-only flow: raw lines 239–363.

## Related

- [[adyen-business-accounts]] — Business accounts eligibility and evidence boundary
- [Onboard users](https://docs.adyen.com/business-accounts/onboard-users) — linked broader onboarding
- [Remediating actions](https://docs.adyen.com/business-accounts/kyc-verification-codes/remediating-actions) — linked action-code reference

## Raw Sources

- [[raw/adyen/docs/business-accounts/verification-overview/data-review-process/2026-09-15|Adyen Business accounts periodic data reviews — collected 2026-09-15]]
