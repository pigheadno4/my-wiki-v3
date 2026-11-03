---
title: "Adyen Legal Entity Management API PATCH /legalEntities/{id}/termsOfService/{termsofservicedocumentid} — accept Terms"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/patch/legalEntities/(id)/termsOfService/(termsofservicedocumentid)"
raw_files:
  - "adyen/api-explorer/legalentity/latest/patch/legalEntities/(id)/termsOfService/(termsofservicedocumentid)/2026-11-03.md"
tags: [adyen, legal-entity-management, platforms, terms-of-service, onboarding]
---

## Overview

The 2026-11-03 Legal Entity Management API Explorer capture describes `PATCH /legalEntities/{id}/termsOfService/{termsofservicedocumentid}` to accept a Terms of Service document. The listed server is TEST `https://kyc-test.adyen.com/lem/v4`. In [[adyen-platforms]] onboarding, the path identifies the relevant legal entity and document, while the required body `acceptedBy` identifies the individual legal entity of the person accepting. This is an acceptance-record operation, not legal-entity verification or capability approval.

## Key takeaways

- Both path IDs are required strings. The `id` is the owner individual for a sole proprietorship, the organization ID for an organization, or the individual ID for a legal representative of an individual. `termsofservicedocumentid` identifies the Terms document. Required `acceptedBy` is the accepting user's legal-entity ID: an authorized individual signatory for an organization, the individual owner for a sole proprietorship, or the individual, parent or guardian for an individual. Optional `ipAddress` is the accepter's IP address. Do not interchange the path entity, document ID and signer ID.
- The captured limits are 700 requests per five seconds in live, 200 per five seconds in test, and five failed requests per ten seconds. The page lists only the TEST base; the live rate limit is not a live URL or proof of current live availability.
- A 200 says the request succeeded. Its response body lists only optional fields: `acceptedBy`, acceptance `id`, `ipAddress`, `language`, `termsOfServiceDocumentId`, and Terms `type`. The returned acceptance `id` is distinct from the document ID. Listed document languages are `en` and conditionally `fr`; type values include Platforms, Issuing, Capital, account/card, franchisee, invite, and direct-debit variants. See the raw table for the exact enum.
- Listed failures are 400 request problem, 401 authentication required, 403 insufficient permission, 422 validation, and 500 server processing. The generic error schema has an optional `pspReference` described as a payment reference; that field does not turn Terms acceptance into a payment operation. No named credential role, idempotency rule, document-generation/revision rule, deletion/reversal, propagation timing or automatic verification/capability effect is specified here.

## Detail locators

- Raw lines 5–18 — purpose, live/test/failure rate limits, and listed TEST server.
- `## Parameters > ### Path parameters` and `### Request body` (raw lines 22–33) — legal-entity/document/signer identities and optional IP.
- `## Request examples` and `## Responses > ### 200 Success` (raw lines 35–56) — illustrative request and optional acceptance fields/type values.
- `## Responses > ### 400 Client Error` through `### 500 Server Error` (raw lines 59–121) — error schemas; `## Response examples` (raw lines 123–136) — illustrative acceptance record.

## Related

- [[adyen]] — provider.
- [[adyen-platforms]] — platform onboarding and verification context.
- [[source-adyen-docs-platforms-onboard-users-terms-of-service]] — separate Platforms guide to document presentation and acceptance workflow.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/patch/legalEntities/(id)/termsOfService/(termsofservicedocumentid)/2026-11-03|2026-11-03 captured API Explorer reference]]
