---
title: "Adyen Business Accounts Terms of Service acceptance"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/onboard-users/terms-of-service"
raw_files:
  - "adyen/docs/business-accounts/onboard-users/terms-of-service/2026-09-15.md"
tags: [adyen, business-accounts, platforms, onboarding, terms-of-service, consent]
---

## Overview

This 2026-09-15 Adyen Business Accounts onboarding guide describes how a platform identifies required Adyen Terms of Service documents, generates and presents them, then records acceptance for a legal entity. Terms acceptance is a gate before particular balance-platform actions. Generating a document, configuring the flow, or seeing a sample acceptance response does not establish that a specific user accepted terms or that a Business Account opened.

## Key takeaways

- The platform **must** generate the required document, show it to the user, and ask for acceptance. Acceptance must come from an individual legal entity representing a physical person; for an organization, an authorized signatory accepts on its behalf. The guide requires an Adyen for Platforms integration, Legal Entity Management API credentials, a server that receives/accepts subscribed Configuration webhooks, and legal entities for the contracting user and individual signer.
- When account-holder capabilities are requested, inspect `balancePlatform.accountHolder.updated` for `verificationErrors` showing a Terms-of-Service requirement. The example has `sendToTransferInstrument` requested/enabled but `allowed=false`, `verificationStatus=invalid`, and error `2_902` with an Accept TOS remedial action. That is a **test example**, not a live user's status or proof that acceptance alone will make a capability allowed.
- For the **main legal entity** (the owner's individual legal entity for a sole proprietorship), GET `/legalEntities/{id}/termsOfServiceStatus` determines the required document **types**. A user may need more than one document. The guide says test returns only `adyenForPlatformsAdvanced` under default configuration regardless of actual integration, while live returns the actual required types. The sample response listing `adyenForPlatformsAdvanced`, `adyenCapital`, and `adyenAccount` is illustrative and must not override that stated test rule or imply every Business Accounts user needs all three.
- POST `/legalEntities/{id}/termsOfService` generates a document for a requested `type` and `language` (English or conditionally French); optional format defaults to JSON, with PDF/TXT alternatives. The response supplies Base64 `document` and a unique `termsOfServiceDocumentId`. Present each decoded document in the UI. The page records document **type and ID**, not an explicit fixed Terms-of-Service version; use the actual generated document ID rather than assuming a static version or a library sample's LEM v3 endpoint/SDK version is universal.
- After the actual user accepts, PATCH `/legalEntities/{id}/termsOfService/{termsOfServiceDocumentId}` for the main legal entity and generated document ID with required `acceptedBy`: the owner's individual legal entity ID for sole proprietorships or an authorized signatory's individual legal entity ID for organizations. `ipAddress` is optional. The acceptance response identifies signer, accepted document ID, type and language; optional GET `/legalEntities/{id}/termsOfServiceAcceptanceInfos` returns records including `acceptedBy`, `acceptedFor`, `createdAt`, ID and type. A generated document or submitted PATCH example is not proof of actual consent; correlate the correct signer, entity, document and real acceptance record. This page does not define an automatic account-opening or transfer-completion outcome after acceptance.

## Detail locators

- Opening and `## Requirements`: mandatory presentation/acceptance, authorized physical-person signer, Platforms/LEM/webhook/entity prerequisites.
- `## 1. Confirm Terms of Service requirements`: capability webhook and verificationErrors example.
- `## 2. Get the types of Terms of Service required`: main-entity scope, multiple types, test default versus live actual types.
- `## 3. Generate the Terms of Service documents` / `## 4. Present the Terms of Service document to your user`: type/language/format, Base64 document ID and UI presentation.
- `## 5. Accept the Terms of Service`: main legal entity and signer IDs, generated document ID, optional IP and acceptance response.
- `## 6. (Optional): Get the Terms of Service information for a legal entity`: readback fields and example.

## Related

- [[adyen-business-accounts]] — main Business Accounts concept.
- [[adyen-platforms]] — platform and legal-entity context.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/business-accounts/onboard-users/terms-of-service/2026-09-15|Adyen Business Accounts Terms of Service guide (fetched 2026-09-15)]]
