---
title: "Adyen for Platforms Terms of Service acceptance | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/onboard-users/terms-of-service"
raw_files:
  - "adyen/docs/platforms/onboard-users/terms-of-service/2026-09-15.md"
tags: [adyen, platforms, onboarding, terms-of-service, legal-entities, consent]
---

## Overview

This 2026-09-15 [[adyen]] Docs snapshot describes how an **Adyen for Platforms** integration obtains a user's acceptance of required Adyen Terms of Service. Missing acceptance can prevent particular platform actions. Hosted onboarding includes the acceptance step; a platform using its own onboarding UI must generate the required document, present it, obtain the user's acceptance and submit confirmation. This is an onboarding/legal-entity workflow, not proof that any user accepted current terms or that a capability became allowed. [[adyen-platforms]]

## Key takeaways

- Acceptance must come from an **individual legal entity** representing a physical person. For an organization, that person must be an authorized signatory; for a sole proprietorship, the owner is the individual legal entity. The platform needs the main legal entity of the user with the platform contract and the individual accepting entity, plus Legal Entity Management API credentials and webhook reception. The page calls for standard webhooks and subscription to Configuration webhooks. See raw lines 19–42.
- A `balancePlatform.accountHolder.updated` webhook's `verificationErrors` can indicate that Terms are required for a requested account-holder capability. The sample shows a `sendToTransferInstrument` problem with `allowed=false` and `verificationStatus=invalid`; that is an example, not a universal status rule for every account holder or capability. See raw lines 55–107.
- Query `/legalEntities/{id}/termsOfServiceStatus` for required document **types** using the main entity ID, or the owner ID for a sole proprietorship. More than one document may be required. The test environment returns only `adyenForPlatformsAdvanced` regardless of actual integration because of its default configuration; live returns the actual required types. Generate each document for the main entity with required `type` and `language` (`en` or conditionally `fr`), optional JSON/PDF/TXT format, then decode/present it. The response supplies Base64 document content and a `termsOfServiceDocumentId`; sample API-library versions and IDs are examples, not an installed version or a current legal text. See raw lines 109–383.
- After the person reviews and accepts, the guide uses PATCH `/legalEntities/{id}/termsOfService/{termsOfServiceDocumentId}` with the **main entity** and document ID in the path and required `acceptedBy` individual legal-entity ID in the body; `ipAddress` is optional. For an organization the accepting entity is its authorized signatory; the response records document/type/language and acceptor. A separate GET acceptance-information route exposes `acceptedBy` and `acceptedFor`. These documented requests and sample responses do not establish a real consent record or imply that every blocked capability is automatically enabled. See raw lines 385–396, 596–622, 766–790.
- The page identifies document type and document ID, but does not define a universal Terms revision/version identifier or a re-acceptance rule after later changes. Assess the current required document and actual acceptance state in the appropriate account before any legal or operational conclusion. See raw lines 109–115, 335–363, 596–605, 766–790.

## Detail locators

- **Acceptance actor, hosted versus own UI, prerequisites and webhook setup:** raw lines 15–53.
- **Account-holder capability error example:** raw lines 55–107.
- **Required types, test/live difference, generation fields and versioned code examples:** raw lines 109–359.
- **Presentation by format and acceptance identity/request:** raw lines 361–396.
- **Acceptance response and optional legal-entity information route:** raw lines 596–622, 766–790.

## Related

- [[adyen]]
- [[adyen-platforms]]
- [[source-adyen-docs-platforms-verification-requirements]] — separate user-verification requirements

## Raw Sources

- [[raw/adyen/docs/platforms/onboard-users/terms-of-service/2026-09-15|Adyen platform Terms of Service guide — collected 2026-09-15]]
