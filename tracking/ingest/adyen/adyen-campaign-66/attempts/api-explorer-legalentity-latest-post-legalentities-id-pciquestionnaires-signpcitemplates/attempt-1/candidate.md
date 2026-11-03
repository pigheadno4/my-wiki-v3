---
title: "Adyen LEM API v4: Sign PCI questionnaire"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities/(id)/pciQuestionnaires/signPciTemplates"
raw_files:
  - "adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/pciQuestionnaires/signPciTemplates/2026-11-03.md"
tags: [adyen, legal-entity-management, platforms, pci-questionnaire]
---

## Overview

The captured Legal Entity Management API v4 TEST reference documents `POST /legalEntities/{id}/pciQuestionnaires/signPciTemplates` to sign required PCI questionnaires. The path `id` identifies the legal entity of the user with a contractual relationship to the platform; `signedBy` identifies the individual legal entity signing; `pciTemplateReferences` contains Adyen-generated questionnaire-template references. These are distinct identities. This is a [[adyen]] [[adyen-platforms]] API reference, related to [[adyen-pci-dss-compliance]].

## Key takeaways

- The request-body table marks both `pciTemplateReferences` (array of strings) and `signedBy` (string) required. It does not separately state whole-body requiredness, conditional fields, a default, or an idempotency contract.
- A 200 response says the request succeeded. Its `pciQuestionnaireIds` array identifies signed PCI documents, and its `signedBy` identifies the signer; both response fields are marked optional. The example shows IDs but cannot establish that both fields always appear.
- The captured server is `https://kyc-test.adyen.com/lem/v4`. The page states limits of 700 requests per five seconds in live, 200 per five seconds in test, and five failed requests per ten seconds.
- Signing and returned document IDs do not establish PCI DSS compliance, merchant eligibility, Adyen verification or approval, payment authorization, settlement, or bank receipt. This snapshot states no deletion, reversal, status-propagation, or asynchronous review/activation behavior. Its `latest` URL and 2026-11-03 capture are not evidence of current availability.

## Detail locators

- Purpose, server, rate limits: pinned raw lines 5–18.
- Path and request-body parameters: pinned raw lines 20–32; example: lines 34–45.
- 200 response body and example: pinned raw lines 46–55 and 122–133.
- Error cases: 400, 401, 403, 422, and 500 at pinned raw lines 58–120. The page describes authentication required for 401 and insufficient permission for 403; it does not list a required credential or role here. Generic error schema includes `pspReference`, which is not evidence of a payment for this signing request.

## Related

- [[source-adyen-api-explorer-legalentity-latest-post-legalentities-id-pciquestionnaires-generatepcitemplates]] — generation of PCI questionnaire templates; generation and signing are separate operations.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/pciQuestionnaires/signPciTemplates/2026-11-03|2026-11-03 pinned API Explorer snapshot]]
