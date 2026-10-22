---
title: "Payout Service recurring top-up Terms of Service acceptance"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/top-up-balance-accounts/sign-terms-of-service"
raw_files:
  - "adyen/docs/payouts/payout-service/top-up-balance-accounts/sign-terms-of-service/2026-09-15.md"
tags: [adyen, payouts, payout-service, recurring-top-ups, terms-of-service]
---

## Overview

This Payout Service page, last modified 2026-04-28 and captured 2026-09-15, describes accepting Adyen's **direct-debit top-up contract Terms of Service** before setting up recurring top-ups. For an organization, the accepting person must be its **authorized signatory**, represented by an individual legal entity. This is a prerequisite workflow, not proof that a real signatory accepted, a schedule was created or funds moved. See [[adyen]] and [[adyen-payouts]] (raw lines 5–26).

## Key takeaways

- The stated scope is an **enterprise payouts** integration with Legal Entity Management API credentials. This manual API workflow is required only when configuring top-ups using the API; the Customer Area setup wizard handles acceptance in its own flow. The legal entity connected to the account holder is the same main entity for which the Terms are accepted (raw lines 28–35).
- The optional first check is GET `/legalEntities/{id}/termsOfServiceAcceptanceInfos` for the **main/organization legal entity**. An empty `data` array means no accepted terms are returned; a `data` object with `type: directDebit` means this top-up Terms acceptance already exists and the remaining generation/presentation steps can be skipped. Its `acceptedBy` is the individual signatory legal-entity ID, distinct from `acceptedFor`, the main entity ID (raw lines 47–88).
- To generate, POST `/legalEntities/{id}/termsOfService` with `type: directDebit` and a language, receiving a Base64 document and `termsOfServiceDocumentId`. The page lists English and conditionally French; French is only available for some integration types/countries. JSON is the default document format, with PDF/TXT options. Depending on the integration, **more than one document may need acceptance**; every required document and ID is returned. The document must be presented for review: JSON via Document Viewer after decoding or decoded PDF/TXT in the UI (raw lines 90–169).
- Confirmation uses PATCH on the main legal entity and generated document ID with `acceptedBy` set to the **individual** legal-entity ID; `ipAddress` is optional. A successful PATCH response is followed by a GET check that `type: directDebit` appears in acceptance information linked to that main entity. This documents an acceptance-record verification step, not live legal authority or a successful top-up (raw lines 171–223).
- The page's final “See also” links point to **Issuing** `/issuing/add-manage-funds/top-ups/` paths even though this source and its described workflow are under **Payout Service**. Treat those links as related navigation, not evidence that Payout Service and Issuing top-up setups share every condition or state (raw lines 225–237).

## Detail locators

- Signatory and API-vs-Customer-Area prerequisite: raw lines 19–35.
- Existing `directDebit` acceptance lookup and entity IDs: raw lines 47–88.
- Document generation, conditional language/format and multiple documents: raw lines 90–146.
- Presentation and PATCH acceptance plus GET verification: raw lines 148–223.
- Issuing-path “See also” navigation boundary: raw lines 225–237.

## Related

- [[source-adyen-docs-payouts-payout-service-top-up-balance-accounts-create-recurring-top-ups]]
- [[source-adyen-docs-payouts-payout-service-top-up-balance-accounts-manage-recurring-top-ups]]
- [[source-adyen-docs-payouts-payout-service-top-up-balance-accounts-top-up-webhooks]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/top-up-balance-accounts/sign-terms-of-service/2026-09-15|Pinned top-up Terms of Service guide]]
