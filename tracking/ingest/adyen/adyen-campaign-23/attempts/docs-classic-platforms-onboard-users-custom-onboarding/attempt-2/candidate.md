---
title: "Adyen Classic Platforms custom onboarding"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/onboard-users/custom-onboarding"
raw_files:
  - "adyen/docs/classic-platforms/onboard-users/custom-onboarding/2026-09-15.md"
tags: [adyen, classic-platforms, onboarding, verification, account-holders]
---

## Overview

This 2020-modified Classic Adyen for Platforms page, captured 2026-09-15, describes building a platform-owned sub-merchant onboarding flow instead of using Adyen's recommended Hosted Onboarding Page. The platform collects the holder's data, creates and updates the Classic account holder, tracks verification through notification webhooks, and uploads documents when needed. It directs new integrations to the separate newer model. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The page recommends Hosted Onboarding as lower implementation effort, but permits a custom flow if the platform collects data for Adyen's verification checks. It requires choosing upfront versus staggered information collection and obtaining country/legal-entity verification requirements before starting (raw lines 19–37). Upfront is described as collecting all data initially for all payment/payout tiers; staggered requests more information when processed funds exceed the current tier. These are flow descriptions, not approval guarantees.
- The Classic four-step sequence is: create an account holder and retain `accountHolderCode`, update it for additional checks, track verification results in notifications, and upload required documents when needed (raw lines 23–28, 39–43, 45–56, 86–98). The page says a newly created holder can immediately process payments, but missing/invalid data or a higher tier can disable payouts until successful verification; do not equate creation or processing with payout eligibility (raw lines 41–51, 84). For each verification check that did not pass, the holder must provide the requested information within the linked deadline; after submission and successful verification, payouts in a higher tier are re-enabled and the check becomes `PASSED` (raw line 84).
- The `updateAccountHolder` example uses a test Account API v6 endpoint. HTTP 200 provides response data, while HTTP 202 acknowledges queuing; for either, the page instructs waiting for `ACCOUNT_HOLDER_UPDATED` before business logic or treating the resource update as confirmed. Verification results arrive in `ACCOUNT_HOLDER_VERIFICATION` notifications; `ACCOUNT_HOLDER_STATUS_CHANGE` can signal disabled payouts when data is missing/invalid (raw lines 49–88).
- Some countries/regions or failed automatic checks may require supporting documents. The page shows Base64 `documentContent`, holder code and document type for `uploadDocument`; its example response has a `pspReference` and empty `verification` object, while validation is asynchronous. The stated average photo-ID and company/bank-document times are examples, not deadlines or proof of approval (raw lines 92–147).
- The document-type table says `COMPANY_REGISTRATION_SCREENING` is supported from v5. Its `ID_CARD_FRONT` row says the front is also required when the front is supplied, while `ID_CARD_BACK` requires front; that self-reference is not a reliable front/back pairing instruction. Consult the detailed document requirements before implementing that case (raw lines 106–115).

## Detail locators

- Classic-only scope, hosted versus custom recommendation, four steps and upfront/staggered choice: raw lines 19–37. Account-holder creation and tier-triggered checks: raw lines 39–55.
- Account API v6 update example and HTTP 200/202 notification gate: raw lines 56–84. Verification-result notification: raw lines 86–90.
- Conditional document upload, payload fields, v5+ table qualifier/self-reference, sample response and asynchronous validation timing: raw lines 92–147.

## Related

- [[adyen-classic-platforms]] — Classic account-holder and account model.
- [[source-adyen-docs-classic-platforms-verification-process]] — verification status, deadline and payout gates.
- [[adyen-platforms]] — separate newer model.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/onboard-users/custom-onboarding/2026-09-15|Classic custom onboarding, captured 2026-09-15]]
