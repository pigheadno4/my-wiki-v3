---
title: "Adyen Legal Entity Management API v4: POST /legalEntities/{id}/confirmDataReview"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities/(id)/confirmDataReview"
raw_files:
  - "adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/confirmDataReview/2026-11-03.md"
tags: [adyen, legal-entity, platforms, verification, data-review, api]
---

## Overview

This 2026-11-03 Legal Entity Management API reference describes `POST /legalEntities/{id}/confirmDataReview`. It informs Adyen that the platform's user reviewed and verified that the specified legal entity's data is up to date; the response reports when Adyen received the request. The shown server is TEST `https://kyc-test.adyen.com/lem/v4`. The endpoint is a user-review confirmation, not an Adyen verification or capability decision. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The required path `id` identifies the legal entity whose data the user reviewed. This captured endpoint lists no query parameters or request body, and it does not identify a credential role or describe a user-authentication workflow. The platform should not infer from a 200 alone that the user actually reviewed data; the endpoint is the mechanism for reporting that review to Adyen.
- The success response is HTTP 200. Its only response-body property, `dataReviewedAt`, is marked optional and described as the confirmation date; the introduction calls it the timestamp when Adyen received the request. The sample date is illustrative, not proof of a particular legal entity's current review or subsequent verification outcome.
- The introduction gives rate limits of 700 requests per five seconds in LIVE, 200 per five seconds in TEST, and five failed requests per ten seconds. These stated LIVE limits do not supply a LIVE server URL or prove account access.
- The page lists 400 request error, 401 authentication required, 403 insufficient permissions, 422 validation error and 500 server failure. Its generic error schema includes an optional `pspReference` described as a payment reference; that label does not turn this legal-entity confirmation into a payment operation. The page gives no idempotency/retry or downstream review timing contract.

## Detail locators

- Purpose, rate limits and TEST server: pinned raw lines 5–18.
- Required legal-entity path ID: `## Parameters > ### Path parameters`, lines 20–25.
- Success response and optional `dataReviewedAt`: `## Responses > ### 200 Success`, lines 27–35.
- Error descriptions and generic fields: `## Responses`, lines 38–100.
- Illustrative 200 timestamp: `## Response examples > ### 200 Success`, lines 102–111.

## Related

- [[adyen-platforms]] — platform onboarding and verification context.
- [[source-adyen-docs-platforms-verification-overview-data-review-process]] — separate periodic data-review guide.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/confirmDataReview/2026-11-03|Confirm legal-entity data review, 2026-11-03 capture]]