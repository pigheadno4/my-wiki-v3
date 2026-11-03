---
title: "POST /legalEntities/{id}/pciQuestionnaires/signingRequired — Calculate PCI signing requirement | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities/(id)/pciQuestionnaires/signingRequired"
raw_files:
  - "adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/pciQuestionnaires/signingRequired/2026-11-03.md"
tags: [adyen, legal-entity-management, platforms, pci, api-reference]
---

## Overview

This 2026-11-03 snapshot of Adyen's Legal Entity Management API v4 reference describes `POST /legalEntities/{id}/pciQuestionnaires/signingRequired` on the listed TEST server, `https://kyc-test.adyen.com/lem/v4`. It calculates whether the user must sign PCI questionnaires for the legal entity identified by the required path `id`. The optional `additionalSalesChannels` array supplies relevant channels if questionnaires must be generated for signing. A successful `200` response can return `signingRequired`; `false` means no questionnaires need signing. This calculation is distinct from questionnaire generation, signing, submission, or independent PCI compliance. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The path `id` is the legal entity's unique identifier. The request-body table lists only optional `additionalSalesChannels` with possible values `eCommerce`, `pos`, `ecomMoto`, and `posMoto`. It says to include relevant channels when the user needs to sign questionnaires, and says the field is not required if stores and payment methods are set up before questionnaire generation. The snapshot does not state a default array or require the request body as a whole.
- The `200` response table marks `signingRequired` as optional. A returned flag describes whether signing is required; it is not a signed questionnaire, compliance determination, verification approval, product activation, or payment result.
- The page lists 700 requests per 5 seconds in live environments, 200 per 5 seconds in test, and 5 failed requests per 10 seconds. Only a TEST server URL is shown here. The snapshot gives no idempotency, propagation timing, or lifecycle transition for this calculation.

## Detail locators

- Endpoint purpose, rate limits and TEST server: raw lines 5–18.
- Path `id` and `additionalSalesChannels` schema, conditions and values: raw lines 20–31.
- `200` and optional `signingRequired` meaning: raw lines 33–41.
- Error statuses and optional error fields: raw lines 44–106; `400` request problem, `401` authentication required, `403` insufficient permissions, `422` validation error, and `500` processing failure. The repeated error schema includes `errorCode`, `errorType`, `message`, `pspReference`, and `status`.

## Related

- [[source-adyen-api-explorer-legalentity-latest-post-legalentities-id-pciquestionnaires-generatepcitemplates]] — Separate questionnaire-template generation API reference.
- [[source-adyen-docs-platforms-onboard-users-pci-forms]] — Platforms PCI questionnaire guidance.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/pciQuestionnaires/signingRequired/2026-11-03|Pinned Adyen signingRequired API reference (2026-11-03)]]
