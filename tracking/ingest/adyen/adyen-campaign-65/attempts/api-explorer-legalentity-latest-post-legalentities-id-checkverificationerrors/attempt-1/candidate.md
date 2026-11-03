---
title: "POST /legalEntities/{id}/checkVerificationErrors — Check verification errors | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities/(id)/checkVerificationErrors"
raw_files:
  - "adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/checkVerificationErrors/2026-11-03.md"
tags: [adyen, legal-entity-management, verification, api-explorer]
---

## Overview

This [[adyen]] Legal Entity Management API Explorer snapshot documents `POST /legalEntities/{id}/checkVerificationErrors`, which returns verification errors for a legal entity and its supporting entities. The captured server is TEST `https://kyc-test.adyen.com/lem/v4`; the URL says `latest` while the server path identifies `v4`. See [[adyen-platforms]] for platform onboarding and verification context.

## Key takeaways

- Required string path `id` identifies the legal entity. The page lists no query parameters, request body, caller role or idempotency key. It specifies rate limits of 700 requests per five seconds in live environments, 200 per five seconds in test, and five failed requests per ten seconds. The only listed server is TEST, despite the separate live rate-limit statement. [Raw: lines 5–25]
- A 200 says the request succeeded. Its `problems` array is response-optional, as are the nested `entity` and `verificationErrors` fields. An included problem can identify an entity and documents, plus general error code/message, error type (`invalidInput`, `dataMissing`, `pendingStatus`, `rejected`, `dataReview`), capability names, suberrors and possible remediating actions. The table does not require any of these nested fields. [Raw: lines 27–47]

> [!warning] Contradiction
> The `capabilities` field is typed as an array of strings [Raw: line 42] and the example shows string capability names [Raw: lines 129–132], but the same field description calls it key-value pairs whose value is an object. This snapshot does not reconcile the field description with its type and example; do not treat the description as a confirmed object shape.

- The sample shows `dataMissing` problems for a legal entity, including VAT number, signatory, UBO, business line, addresses and documents, with remediation examples. These are illustrative error records, not a universal checklist or proof that any remediation has been submitted or approved. [Raw: lines 114–295]
- Errors listed are 400 request-reading/understanding, 401 authentication, 403 insufficient permissions, 422 validation and 500 server processing. Their problem bodies mark `errorCode`, `errorType`, `message`, `pspReference` and `status` optional; this generic `pspReference` field does not turn the endpoint into a payment-status check. [Raw: lines 50–112]
- A returned error list reports detected issues at read time. A 200, absent `problems`, or suggested remediation does not establish completed legal-entity verification, enabled capabilities, account eligibility, compliance, payment acceptance, payout or bank receipt. This dated TEST v4 capture also does not establish current live behavior. [Raw: lines 5–47, 114–295]

## Detail locators

- Purpose, rate limits, TEST v4 server and required legal-entity ID: pinned raw lines 5–25.
- 200 optional problem/entity/error fields and error types: lines 27–47.
- HTTP error schemas: lines 50–112; illustrative verification-error response: lines 114–295.

## Related

- [[adyen-platforms]] — platform onboarding and legal-entity context.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/checkVerificationErrors/2026-11-03|POST check legal-entity verification errors — captured 2026-11-03]]