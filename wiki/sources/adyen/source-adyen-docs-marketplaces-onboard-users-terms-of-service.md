---
title: "Adyen Marketplaces Terms of Service acceptance"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/onboard-users/terms-of-service"
raw_files:
  - "adyen/docs/marketplaces/onboard-users/terms-of-service/2026-09-15.md"
tags: [adyen, marketplaces, platforms, onboarding, terms-of-service]
---

## Overview

This 2026-09-15 Adyen Marketplaces guide explains how users accept Adyen's Terms of Service before particular marketplace actions. For a custom onboarding UI, the platform generates and presents the required document and asks the user to accept it; hosted onboarding includes the step in its own flow. The accepter must be an individual legal entity representing a person, and an organization uses an authorized signatory. This is a Terms of Service acceptance procedure within Adyen for Platforms, not evidence that a user has passed KYC or gained a payment or payout capability. [[adyen]] [[adyen-platforms]]

## Key takeaways

- Prerequisites are an Adyen for Platforms integration, Legal Entity Management API credentials, a server receiving standard/Configuration webhooks, and legal entities for both the marketplace's contractual user and the individual who will accept. The source requirements table is malformed in the captured Markdown, so use the surrounding flow and endpoint sections for precise implementation (raw lines 30–53).
- After requesting an account holder's capabilities, use `balancePlatform.accountHolder.updated` and its `verificationErrors` to detect when Terms of Service acceptance is required; the example has `2_902`, `Accept TOS`, and a capability that is requested/enabled but not allowed. This example does not mean every account holder or capability has that error (raw lines 55–107).
- Call GET `/legalEntities/{id}/termsOfServiceStatus` for the **main legal entity** to determine required document types; for a sole proprietorship, use the owner's individual legal-entity ID. More than one document may be required. TEST always returns `adyenForPlatformsAdvanced` under its default configuration regardless of the actual integration; LIVE returns the actual required types (raw lines 109–125).
- Generate the required Terms of Service document with POST `/legalEntities/{id}/termsOfService`, specifying document `type` and `language` (`en`, or `fr` only for some integration/country combinations); format defaults to JSON and may be JSON, PDF or TXT. The response includes a Base64-encoded document and `termsOfServiceDocumentId`. Decode and present each required document to the user; the JSON option can use Adyen Document Viewer, while PDF/TXT can be rendered in the platform UI (raw lines 127–156, 333–381).
- After the user reviews and accepts, PATCH `/legalEntities/{id}/termsOfService/{termsOfServiceDocumentId}` for the main legal entity and generated document ID. The required `acceptedBy` is the **individual** legal-entity ID of the accepter: the owner for a sole proprietorship, or an authorized organizational signatory. `ipAddress` is optional. The response identifies the accepted document and accepter; acceptance is a separate action from generation or presentation (raw lines 383–394, 594–617).
- Optionally GET `/legalEntities/{id}/termsOfServiceAcceptanceInfos` to retrieve acceptance records for the main legal entity, including `acceptedBy` and `acceptedFor`. The guide's code blocks are TEST examples with versioned client libraries; their sample IDs, document type and IP address are illustrative, not proof of a real acceptance or live account status (raw lines 621–788).

## Detail locators

- Purpose, custom versus hosted onboarding, and required signer: raw lines 17–28. Prerequisites and six-step route: lines 30–53.
- Account-holder capability webhook, `verificationErrors` and example status: lines 55–107. Required-type lookup and TEST/LIVE difference: lines 109–125.
- Generation request, language/format rules, code examples, response fields and multiple-document note: lines 127–361. Document presentation: lines 363–381.
- Acceptance PATCH, owner/organization ID mapping, `acceptedBy`, optional IP, response and SDK samples: lines 383–617. Optional acceptance-information GET and record fields: lines 619–788.

## Related

- [[adyen]] — provider.
- [[adyen-platforms]] — modern Platforms model and Marketplace route.
- [[source-adyen-docs-marketplaces]] — marketplace integration overview.
- [[adyen-classic-platforms]] — separate legacy integration.

## Raw Sources

- [[raw/adyen/docs/marketplaces/onboard-users/terms-of-service/2026-09-15|Marketplace Terms of Service — 2026-09-15 snapshot]]
