---
title: "Adyen Legal Entity Management API v4: generate PCI questionnaire templates"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities/(id)/pciQuestionnaires/generatePciTemplates"
raw_files:
  - "adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/pciQuestionnaires/generatePciTemplates/2026-11-03.md"
tags: [adyen, legal-entity, platforms, pci, api]
---

## Overview

This 2026-11-03-captured Legal Entity Management API v4 reference describes `POST /legalEntities/{id}/pciQuestionnaires/generatePciTemplates`. It generates PCI questionnaires based on the user's sales channel for the legal entity identified by required path `id`. The listed server is TEST `https://kyc-test.adyen.com/lem/v4`; the `latest` URL does not establish current live availability or caller access. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The request-body table has two optional fields. `additionalSalesChannels` can name `eCommerce`, `pos`, `ecomMoto` or `posMoto` when relevant questionnaires are needed for user signing; the prose says it is not required if stores are created and payment methods added before generation. Optional `language` is a two-character ISO 639-1 code. The French-language request example illustrates one selection; no body-field default or specific caller role is stated.
- A 200 says the request succeeded. Optional response fields are Base64 `content`, two-letter `language`, and `pciTemplateReferences` (Adyen-generated questionnaire IDs). The table says an empty reference array means the user is not required to sign questionnaires. The example returns two references and content; it is not a promise that every request returns two templates or a populated body.
- Captured rate limits are 700 requests per 5 seconds in Live, 200 per 5 seconds in Test, and 5 failed requests per 10 seconds. The page lists 400, 401, 403, 422 and 500 errors, but no endpoint-specific credential role or idempotency semantics. Generic errors include optional payment-labeled `pspReference`; template generation is not a payment operation.
- Generation of questionnaire content or references is separate from user signature, submission, verification or an independent PCI compliance determination. This reference does not document an asynchronous signing result, capability activation or financial outcome.

## Detail locators

- Purpose, rates, TEST server, legal-entity path ID and request fields: pinned raw lines 5–32; illustrative request lines 34–41.
- 200 response fields and empty-reference meaning: lines 42–52; illustrative response lines 119–133.
- Generic error schemas: lines 55–117.

## Related

- [[adyen-platforms]] — platform onboarding context.
- [[source-adyen-docs-platforms-onboard-users-pci-forms]] — separate signing and submission guide.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/pciQuestionnaires/generatePciTemplates/2026-11-03|Legal Entity PCI template generation snapshot]]