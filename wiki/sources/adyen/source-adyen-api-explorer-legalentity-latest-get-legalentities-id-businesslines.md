---
title: "GET /legalEntities/{id}/businessLines — List a legal entity's business lines | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/get/legalEntities/(id)/businessLines"
raw_files:
  - "adyen/api-explorer/legalentity/latest/get/legalEntities/(id)/businessLines/2026-11-03.md"
tags: [adyen, legal-entity-management, platforms, business-lines, verification, api-explorer]
---

## Overview

This [[adyen]] Legal Entity Management API Explorer snapshot documents `GET /legalEntities/{id}/businessLines` to return business lines owned by one legal entity. The captured server is TEST `https://kyc-test.adyen.com/lem/v4`; the URL uses `latest`, while the server path identifies v4. See [[adyen-platforms]] for legal-entity resource context. [Raw: lines 5–18]

## Key takeaways

- Required string path `id` identifies the legal entity. The page lists no query parameter, request body, pagination, caller-role name or GET idempotency contract. It states rate limits of 700 requests per five seconds in live environments, 200 per five seconds in test, and five failed requests per ten seconds. These are captured limits, not proof of access to either environment. [Raw: lines 9–25]
- A 200 means the request succeeded and requires a `businessLines` array. Each listed business line requires its own `id`, `industryCode`, owning `legalEntityId` and `service` (`paymentProcessing`, `issuing` or `banking`). The business-line ID differs from the legal-entity path ID. Optional `problems` hold verification errors related to capabilities; their absence is not an approval signal. [Raw: lines 27–44]
- The response schema marks `salesChannels` optional in the table but says it is required with `paymentProcessing`; it marks `sourceOfFunds` optional in the table but says it is required for `banking` or `issuing`. Inside a returned `sourceOfFunds`, `adyenProcessedFunds` is marked required, and a false value requires `type`. Further fields depend on `type` (for example amount for `business`, `assetSale`, `gamblingWinnings` or `inheritance`). Optional `webData` and `webDataExemption` describe online presence or its absence. These are response descriptions, not GET request fields or proof of a completed verification review. [Raw: lines 43–63]

> [!warning] Contradiction
> The table says `sourceOfFunds.amount` is required for `type: business` [Raw: line 47], but the sample banking business line has `sourceOfFunds.type: business` without `amount` [Raw: lines 138–153]. The sample does not establish a generally valid omission or override the conditional field description.

- Error headings are 400 request problem, 401 authentication, 403 permission, 422 validation and 500 server processing. The source provides no named credential role, business-line creation/update/deletion action, review completion, capability activation, payment outcome or financial movement result for this GET. [Raw: lines 66–128]

## Detail locators

- Purpose, rate limits, TEST v4 server and path ID: pinned raw lines 5–25.
- 200 business-line identities, service, conditional fields and verification-problem schema: lines 27–63; sample: lines 130–172.
- Error meanings and optional problem-body fields: lines 66–128.

## Related

- [[adyen-platforms]] — platform legal-entity and verification context.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/get/legalEntities/(id)/businessLines/2026-11-03|GET legal-entity business lines — captured 2026-11-03]]