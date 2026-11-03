---
title: "Adyen Legal Entity Management API v4: list signed PCI questionnaires"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/get/legalEntities/(id)/pciQuestionnaires"
raw_files:
  - "adyen/api-explorer/legalentity/latest/get/legalEntities/(id)/pciQuestionnaires/2026-11-03.md"
tags: [adyen, legal-entity-management, platforms, pci-dss, api]
---

## Overview

This 2026-11-03 [[adyen]] Legal Entity Management API reference describes `GET /legalEntities/{id}/pciQuestionnaires`, a read-only list of signed PCI questionnaires for a specified legal entity. The captured server is `https://kyc-test.adyen.com/lem/v4`; the page separately states live and test rate limits but does not supply a live server URL. The returned questionnaire metadata is not independent proof of current PCI compliance, account-holder verification, card-processing capability or a payment outcome. [[adyen-platforms]]

## Key takeaways

- The only documented input is the required path string `id`, the legal entity's unique identifier. No query parameter or request body is documented. The page does not name a particular platform or merchant caller; its `401` and `403` responses distinguish missing authentication from insufficient permissions.
- A `200` means the lookup request succeeded. Its optional `data` array contains signed-questionnaire objects; the listed child fields are optional `createdAt`, signed-questionnaire `id` and `validUntil`. The two timestamps use ISO 8601 extended format. The legal-entity path ID and signed-questionnaire response IDs are different references. The illustrated two-item response is an example, not a guaranteed count or current-validity result.
- Stated limits are 700 requests per five seconds in live, 200 per five seconds in test, and five failed requests per ten seconds. The page describes `400`, `401`, `403`, `422` and `500` errors. It gives no signing action, idempotency contract, deletion effect, propagation timing, review decision or activation transition for this GET.

## Detail locators

- **Purpose, rate limits and captured v4 test server:** raw lines 5–18.
- **Required legal-entity path ID:** raw lines 20–25.
- **Success fields and optionality:** raw lines 27–38.
- **Error meanings and optional error fields:** raw lines 41–103.
- **Illustrative two-item response:** raw lines 105–125.

## Related

- [[adyen-platforms]] — platform onboarding and legal-entity context.
- [[adyen-pci-dss-compliance]] — broader PCI responsibilities; a questionnaire list alone is not compliance proof.
- [[source-adyen-docs-platforms-onboard-users-pci-forms]] — signed-form flow and separate capability-status context.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/get/legalEntities/(id)/pciQuestionnaires/2026-11-03|Legal Entity Management API v4 GET PCI questionnaires — collected 2026-11-03]]