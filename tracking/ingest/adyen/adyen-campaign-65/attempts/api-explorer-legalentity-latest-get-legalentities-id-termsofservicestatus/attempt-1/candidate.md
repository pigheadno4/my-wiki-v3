---
title: "Adyen Legal Entity Management API v4: GET /legalEntities/{id}/termsOfServiceStatus"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/get/legalEntities/(id)/termsOfServiceStatus"
raw_files:
  - "adyen/api-explorer/legalentity/latest/get/legalEntities/(id)/termsOfServiceStatus/2026-11-03.md"
tags: [adyen, legal-entity, platforms, terms-of-service, api]
---

## Overview

This 2026-11-03 Legal Entity Management API v4 reference describes `GET /legalEntities/{id}/termsOfServiceStatus`, which returns the types of Terms of Service a legal entity still needs to accept. The only displayed server is TEST `https://kyc-test.adyen.com/lem/v4`; the `latest` URL and a type-list read do not establish live access or a particular entity's accepted terms. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The required path `id` identifies the legal entity. For a sole proprietorship, the page says to use the individual legal-entity ID of its owner; for an organization, use the organization's ID. No query parameter or request body is listed.
- HTTP 200 has one response-body property, optional `termsOfServiceTypes`, an array of types that the legal entity needs to accept. The table says an **empty array** means no Terms of Service needs to be accepted; it does not say an omitted property has that meaning. The 200 JSON sample contains `adyenIssuing`, which is an example rather than an exhaustive type catalog or evidence of a particular entity's obligation.
- The endpoint is a status lookup. It neither submits acceptance nor proves signed documents, Adyen review, verification, capability approval or payment/funds outcomes. The page specifies no acceptance timing or status-propagation contract.
- The introduction states rate limits of 700 requests per five seconds LIVE, 200 per five seconds TEST, and five failed requests per ten seconds. These LIVE limits do not supply a LIVE base URL or prove account eligibility.
- Listed failures are 400 request, 401 authentication, 403 permissions, 422 validation and 500 server errors. The generic error body's optional `pspReference` is labeled a payment reference, but this lookup is not a payment operation; no endpoint-specific credential role or version-conflict behavior is given.

## Detail locators

- Purpose, rate limits and TEST base: pinned raw lines 5–18.
- Legal-entity path identity and sole-proprietor/organization distinction: `## Parameters > ### Path parameters`, lines 20–25.
- Success response and optional-versus-empty `termsOfServiceTypes`: `## Responses > ### 200 Success`, lines 27–35.
- Error schemas: lines 38–100; illustrative `adyenIssuing` response: `## Response examples`, lines 102–113.

## Related

- [[adyen-platforms]] — platform onboarding context.
- [[source-adyen-docs-platforms-onboard-users-terms-of-service]] — separate Terms of Service acceptance guide.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/get/legalEntities/(id)/termsOfServiceStatus/2026-11-03|GET legal-entity Terms of Service status, 2026-11-03 capture]]