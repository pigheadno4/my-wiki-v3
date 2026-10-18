---
title: "Adyen Capital Terms of Service acceptance"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/terms-of-service"
raw_files:
  - "adyen/docs/capital/terms-of-service/2026-09-15.md"
tags: [adyen, capital, platforms, terms-of-service, consent, grants]
---

## Overview

This 2026-09-15 Adyen Capital guide describes the legal-entity Terms of Service (ToS) document flow that precedes payout of a Capital grant: check the requirement, determine document types, generate and present the document, record acceptance by the correct individual, and optionally read back acceptance information. The page says accepting the required ToS enables the `receiveGrants` capability, but acceptance can occur before or after a grant offer and must precede grant payout. It does not itself evidence a particular offer, grant request, disbursement or receipt of funds.

## Key takeaways

- The guide's prerequisites include Adyen for Platforms with Capital enabled, Legal Entity Management API credentials, a requested `receiveGrants` capability, subscribed Configuration webhooks, a supported Capital region, Adyen configuration and compliance, and legal entities for the contracting user and individual signer. An individual legal entity representing a physical person must accept. For an organization that signer must be an authorized signatory.
- A `balancePlatform.accountHolder.updated` webhook can expose ToS-related `verificationErrors`. Its sample is for `sendToTransferInstrument` with error `2_902 Accept TOS`; this generic example does **not** show a Capital user's actual `receiveGrants` state or prove a grant is ready.
- GET `/legalEntities/{id}/termsOfServiceStatus` for the main legal entity (the owner's individual legal entity for a sole proprietorship) identifies required document types; more than one may be needed. The guide says the **test** environment returns only `adyenForPlatformsAdvanced` under a shared default configuration, while **live** returns actual types. A nearby response example lists three types including `adyenCapital`; treat it as illustrative, not as a guarantee about test or a universal required set.
- To generate the Capital document, POST `/legalEntities/{id}/termsOfService` with `type=adyenCapital` and language `en` or, for some integrations/regions, `fr`. The optional format defaults to JSON, with PDF and TXT alternatives. The response carries a Base64 document and a unique `termsOfServiceDocumentId`; decode and present the generated document. The page gives a document **type and ID**, not a fixed ToS version; LEM v3 test endpoint and language-library versions are examples, not the document version.
- After the user actually accepts, PATCH `/legalEntities/{id}/termsOfService/{termsOfServiceDocumentId}` for the main legal entity and that generated document ID with required `acceptedBy`: the owner's individual legal entity ID for a sole proprietorship or an authorized signatory's individual legal entity ID for an organization. `ipAddress` is optional. The response identifies the accepted document and signer; optional GET `/legalEntities/{id}/termsOfServiceAcceptanceInfos` returns records including `acceptedBy`, `acceptedFor`, `createdAt`, acceptance ID and type. A generated document or sample response does not establish real consent; correlate the actual entity, signer, document and acceptance record. The stated `receiveGrants` enablement is a prerequisite boundary, not proof of an offer, grant disbursement or bank receipt.

## Detail locators

- Opening and `## Requirements`: ToS prerequisite for grant payout, signer identity, Capital/Platforms/API/webhook/region prerequisites.
- `## 1. Confirm Terms of Service requirements`: configuration webhook and generic capability-error example.
- `## 2. Get the types of Terms of Service required`: main legal entity, multiple documents, test default versus live actual types.
- `## 3. Generate the Terms of Service documents` and `## 4. Present the Terms of Service document to your user`: Capital type, language/format, Base64 document and generated ID.
- `## 5. Accept the Terms of Service`: generated document ID, main legal entity, authorized individual signer, optional IP and acceptance response.
- `## 6. (Optional): Get the Terms of Service information for a legal entity`: acceptance-record readback.

## Related

- [[adyen-capital]] — main Capital concept.
- [[adyen-platforms]] — platform and legal-entity context.
- [[source-adyen-docs-capital-manage-user-capabilities]] — Capital capability context.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/capital/terms-of-service/2026-09-15|Adyen Capital Terms of Service guide (fetched 2026-09-15)]]
