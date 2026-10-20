---
title: "Adyen Issuing: Accept top-up Terms of Service"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/add-manage-funds/top-ups/sign-terms-of-service"
raw_files:
  - "adyen/docs/issuing/add-manage-funds/top-ups/sign-terms-of-service/2026-09-15.md"
tags: [adyen, issuing, recurring-top-ups, direct-debit, terms-of-service]
---

## Overview

This 2026-09-15-captured, 2026-04-28-modified Adyen Issuing guide describes presenting and recording acceptance of the `directDebit` Terms of Service for recurring top-up contracts. It identifies the main legal entity for the contract and the individual who accepts, with an API workflow for top-up setup and a Customer Area wizard alternative. This guide does not establish that a particular cardholder consented or that a direct debit or top-up succeeded. [[adyen]] [[adyen-issuing]]

## Key takeaways

- Acceptance of top-up contract terms precedes recurring top-up setup. The accepter must be an individual legal entity representing a physical person; an organization acts through its authorized signatory. The guide's requirements specify an Issuing integration and Legal Entity Management API credentials. Before either setup route, create the legal entity connected to the account holder. The API workflow records its acceptance; for Customer Area setup, the wizard handles the Terms-of-Service acceptance workflow. See raw lines 19-36.
- For an API flow, optionally GET `/legalEntities/{id}/termsOfServiceAcceptanceInfos` for the main legal entity: the sole proprietor's individual legal-entity ID or the organization's legal-entity ID. A returned acceptance-information object with `type: directDebit` permits skipping the remaining document steps in this guide; an empty `data` array means none accepted. See raw lines 47-74.
- Otherwise POST `/legalEntities/{id}/termsOfService` for that main entity with `type: directDebit` and a document language. Decode the returned Base64 document before presenting it to the cardholder: decoded JSON may be rendered with Adyen Document Viewer, while decoded PDF or TXT may be presented in the UI. JSON is the default format. French availability is conditional by integration and region. More than one required document/ID can be returned depending on integration. See raw lines 92-170.
- After the cardholder reviews and accepts, PATCH `/legalEntities/{id}/termsOfService/{termsOfServiceDocumentId}` using the main entity and returned document ID in the path and the accepting individual's legal-entity ID in required `acceptedBy`; `ipAddress` is optional. For organizations, the populated document contains organization data and the authorized signatory's individual data. After a successful response, GET acceptance information again and verify `directDebit` is linked. See raw lines 172-224.
- This `directDebit` contract acceptance has a narrower purpose than the separate [[source-adyen-docs-issuing-onboard-users-terms-of-service]] onboarding document-type workflow. Examples using the LEM v3 test URL demonstrate request shape only; they do not prove current live eligibility, acceptance or top-up execution. See raw lines 51-64, 96-119 and 174-224.

## Detail locators

- Acceptance-information response fields (`acceptedBy`, `acceptedFor`, `type`) and sample: raw lines 61-90.
- Generate-document field table, formats and sample request/response: raw lines 96-147. Presentation and JSON viewer example: raw lines 149-170.
- Acceptance request/response field tables and test example: raw lines 176-222. Follow-up links for create/manage top-ups and top-up webhooks: raw lines 226-238.

## Related

- [[adyen-issuing]] — Issuing balance-platform context and reciprocal source route.
- [[source-adyen-docs-issuing-add-manage-funds-top-ups-create-recurring-top-ups]] — recurring top-up configuration and its separate prerequisites.
- [[source-adyen-docs-issuing-onboard-users-terms-of-service]] — general onboarding Terms of Service workflow.

## Raw Sources

- [[raw/adyen/docs/issuing/add-manage-funds/top-ups/sign-terms-of-service/2026-09-15|Adyen top-up Terms of Service, captured 2026-09-15]]
