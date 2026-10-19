---
title: "Adyen Issuing: Terms of Service acceptance"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/onboard-users/terms-of-service"
raw_files:
  - "adyen/docs/issuing/onboard-users/terms-of-service/2026-09-15.md"
tags: [adyen, issuing, onboarding, terms-of-service, verification]
---

## Overview

This 2026-09-15 Adyen Issuing onboarding guide describes how a platform using its own user interface determines which Adyen Terms of Service documents are required, generates and presents them, and records acceptance through the Legal Entity Management API. Hosted onboarding includes the acceptance step within its flow. The accepter must be an individual legal entity representing a person; an organization uses an authorized signatory. This source is an integration guide, not evidence that a particular user has accepted terms or gained a capability.

## Key takeaways

- The guide's requirements table specifies an **Adyen for Platforms integration**, Legal Entity Management API credentials, standard/Configuration webhooks, and legal entities for the user with the contractual relationship and the individual accepter (raw lines 30-42). That integration-type wording appears under an **Issuing** URL; the page does not resolve whether the same instructions apply to Issuing-only configurations. Confirm the actual product and account requirements with Adyen before implementation.
- For the account holder, `balancePlatform.accountHolder.updated` may report a Terms of Service acceptance requirement in `verificationErrors`; its example shows code `2_902` and a capability problem (raw lines 55-107). A reported requirement is not acceptance.
- GET `/legalEntities/{id}/termsOfServiceStatus` for the **main legal entity** to identify required types; for a sole proprietorship, use the owner's individual legal-entity ID. More than one document may be required. The page says test returns only `adyenForPlatformsAdvanced` regardless of integration, while live returns actual required types (raw lines 109-115). Its illustrative JSON response lists three types (raw lines 119-127), so do not treat that example as a test-environment result.
- POST `/legalEntities/{id}/termsOfService` for the main legal entity (sole proprietor: owner's individual ID), specifying document `type` and `language`, with optional format (`JSON` by default, or `PDF`/`TXT`). The response includes Base64 document content and a `termsOfServiceDocumentId`; if multiple documents are required, present each. French language availability is qualified by integration type and region (raw lines 129-137, 335-363).
- Decode and show the generated document to the user (JSON may use Adyen Document Viewer; PDF/TXT may be rendered in the platform UI). Only after the user reviews and accepts it, PATCH `/legalEntities/{id}/termsOfService/{termsOfServiceDocumentId}` with required `acceptedBy`, the **individual legal-entity ID** of the accepter; `ipAddress` is optional. The path uses the main organization ID, or the owner's individual ID for sole proprietorships. For an organization, the accepter is its authorized signatory (raw lines 365-396).
- GET `/legalEntities/{id}/termsOfServiceAcceptanceInfos` optionally retrieves acceptance information for the main legal entity, including `acceptedBy` and `acceptedFor` (raw lines 620-622, 766-790). The examples do not establish actual consent, live eligibility or card issuance.

## Detail locators

- Flow sequence and webhook example: raw lines 44-107. Document generation request, SDK snippets and response: raw lines 129-363. Presentation formats: raw lines 365-383. Acceptance request, response and SDK examples: raw lines 385-618. Optional acceptance-information lookup: raw lines 620-790.
- The captured text has broken placeholders such as `in your .` and a malformed setup table (raw lines 19, 34-42); avoid inferring the missing noun or a broader product scope from those fragments.

## Related

- [[adyen]] — provider.
- [[adyen-issuing]] — Issuing concept and source route.

## Raw Sources

- [[raw/adyen/docs/issuing/onboard-users/terms-of-service/2026-09-15|2026-09-15 Adyen Issuing Terms of Service guide]]
