---
title: "GET /legalEntities/{id}/termsOfServiceAcceptanceInfos — Read Terms of Service acceptance information | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/get/legalEntities/(id)/termsOfServiceAcceptanceInfos"
raw_files:
  - "adyen/api-explorer/legalentity/latest/get/legalEntities/(id)/termsOfServiceAcceptanceInfos/2026-11-03.md"
tags: [adyen, legal-entity-management, platforms, terms-of-service, acceptance, api-explorer]
---

## Overview

This [[adyen]] Legal Entity Management API Explorer snapshot documents `GET /legalEntities/{id}/termsOfServiceAcceptanceInfos` to return Terms of Service information for a legal entity. The captured server is TEST `https://kyc-test.adyen.com/lem/v4`; `latest` is the URL segment, while the server path identifies v4. See [[adyen-platforms]] for legal-entity onboarding context. [Raw: lines 5–18]

## Key takeaways

- Required string path `id` is the legal-entity identifier: for a sole proprietorship, the owner's individual legal-entity ID; for an organization, the organization's ID. No query parameter, request body, GET default, pagination, caller-role name or idempotency contract is specified. Captured limits are 700 requests per five seconds in live, 200 per five seconds in test, and five failed requests per ten seconds. These limits do not establish live access. [Raw: lines 9–25]
- A 200 means the request succeeded. Its `data` array of acceptance information is marked optional. Within any record, `acceptedBy` identifies the accepting user, `acceptedFor` the legal entity for which terms were accepted, `createdAt` the acceptance time, `id` an Adyen-generated acceptance reference, `type` the Terms of Service category, and `validTo` the expiration time; every one is table-optional. `acceptedBy`, `acceptedFor`, the path `id` and the record `id` serve different roles. The type list spans Platforms, Issuing, Capital, account/card and direct-debit terms; see the raw enum. [Raw: lines 27–41]
- The example shows one `adyenIssuing` acceptance record, with distinct `acceptedBy`, `acceptedFor` and acceptance reference, but no `validTo`. It illustrates shape; omission of expiration does not prove perpetual validity, current required terms, legal sufficiency, verification approval or a product capability. This GET neither presents nor records terms acceptance. [Raw: lines 108–124]
- The documented failures are 400 request-reading/understanding, 401 authentication, 403 permission, 422 validation and 500 server processing. No named credential role, acceptance creation/update/deletion action, review timing, status propagation or financial outcome is specified. [Raw: lines 44–106]

## Detail locators

- Purpose, rate limits, TEST v4 server and legal-entity path ID: pinned raw lines 5–25.
- 200 acceptance-info schema and term categories: lines 27–41; example: lines 108–124.
- Error headings and optional problem-body fields: lines 44–106.

## Related

- [[adyen-platforms]] — platform legal-entity onboarding context.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/get/legalEntities/(id)/termsOfServiceAcceptanceInfos/2026-11-03|GET legal-entity Terms acceptance information — captured 2026-11-03]]