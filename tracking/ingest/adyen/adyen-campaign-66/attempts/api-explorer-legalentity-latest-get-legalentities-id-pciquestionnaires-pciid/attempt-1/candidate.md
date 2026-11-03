---
title: "Adyen Legal Entity Management API v4: Get signed PCI questionnaire"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/get/legalEntities/(id)/pciQuestionnaires/(pciid)"
raw_files:
  - "adyen/api-explorer/legalentity/latest/get/legalEntities/(id)/pciQuestionnaires/(pciid)/2026-11-03.md"
tags: [adyen, legal-entity, platforms, pci, api]
---

## Overview

This 2026-11-03-captured Legal Entity Management API v4 reference describes `GET /legalEntities/{id}/pciQuestionnaires/{pciid}`, a read of a signed PCI questionnaire. The listed server is TEST `https://kyc-test.adyen.com/lem/v4`. The `latest` URL is a snapshot label, not evidence of current live availability or caller access. See [[adyen]], [[adyen-platforms]] and [[adyen-pci-dss-compliance]].

## Key takeaways

- Both path parameters are required strings: `id` is the legal entity ID of the individual who signed the questionnaire, and `pciid` is the signed questionnaire's unique ID. The captured page specifies no query parameters or request body, and does not name a particular caller role.
- A 200 says the request succeeded. The response schema marks all four fields optional: Base64-encoded generated questionnaire `content`, questionnaire `id`, ISO 8601 extended `createdAt`, and ISO 8601 extended `validUntil`. The populated 200 example illustrates a response, not a guarantee that every successful response includes each field or that a retrieved questionnaire remains unexpired.
- Captured limits are 700 requests per 5 seconds in Live, 200 per 5 seconds in Test, and 5 failed requests per 10 seconds. The page lists 400, 401, 403, 422 and 500 errors; 401 requires authentication and 403 indicates insufficient permissions. It does not specify a credential mechanism, an endpoint-specific role or idempotency semantics. Generic error schemas include optional payment-labeled `pspReference`; this questionnaire retrieval is not a payment operation.
- Retrieval is evidence of the endpoint's signed-questionnaire readback only. It does not sign or submit a new questionnaire, independently establish PCI compliance, approve verification or activate a capability. The page states no deletion, propagation, reversal or asynchronous review result for this GET.

## Detail locators

- Purpose, rate limits, TEST server and both path IDs: pinned raw lines 5–26.
- 200 semantics and optional response fields: lines 28–39; illustrative response: lines 106–117.
- Error descriptions and optional generic error fields: lines 42–104.

## Related

- [[adyen-platforms]] — platform onboarding context.
- [[adyen-pci-dss-compliance]] — PCI responsibilities and evidence boundaries.
- [[source-adyen-api-explorer-legalentity-latest-post-legalentities-id-pciquestionnaires-generatepcitemplates]] — separate template-generation endpoint.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/get/legalEntities/(id)/pciQuestionnaires/(pciid)/2026-11-03|Signed PCI questionnaire GET snapshot]]
