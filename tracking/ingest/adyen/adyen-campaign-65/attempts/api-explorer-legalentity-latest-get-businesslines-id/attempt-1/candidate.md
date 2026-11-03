---
title: "GET /businessLines/{id} — Read one business line | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/get/businessLines/(id)"
raw_files:
  - "adyen/api-explorer/legalentity/latest/get/businessLines/(id)/2026-11-03.md"
tags: [adyen, legal-entity-management, platforms, business-lines, verification, api-explorer]
---

## Overview

This [[adyen]] Legal Entity Management API Explorer snapshot documents `GET /businessLines/{id}` to return one business line's details. The captured server is TEST `https://kyc-test.adyen.com/lem/v4`; the URL uses `latest`, while the server path identifies v4. See [[adyen-platforms]] for legal-entity resource context. [Raw: lines 5–18]

## Key takeaways

- Required string path `id` is the business-line identifier, separate from the returned owning `legalEntityId`. No query parameter, request body, GET default, pagination, caller-role name or idempotency contract is specified. Captured rate limits are 700 requests per five seconds in live, 200 per five seconds in test, and five failed requests per ten seconds. The live limit is not a live-access guarantee. [Raw: lines 9–25]
- A 200 means the GET succeeded and returns the business-line object. `id`, `industryCode`, `legalEntityId` and `service` are marked required; service can be `paymentProcessing`, `issuing` or `banking`. Optional `problems` can contain verification errors related to capabilities, including granular causes and remediating actions. Its absence is not evidence of approval. [Raw: lines 27–53]
- The response table marks `salesChannels` optional but prose-required with `paymentProcessing`, and `sourceOfFunds` optional but prose-required with `banking` or `issuing`. If `sourceOfFunds` appears, `adyenProcessedFunds` is marked required; false requires `type`, which triggers further conditional fields. For example, `amount` is required for `business`, `assetSale`, `gamblingWinnings` or `inheritance`, with child `currency` and `value` both marked optional despite their own constraints. Optional `webData` and `webDataExemption` describe online presence. These are response fields, not GET inputs or an approved source-of-funds assessment. [Raw: lines 52–78]

> [!warning] Contradiction
> The schema prose requires `sourceOfFunds.amount` for `type: business` [Raw: line 56], but the example banking business line omits `amount` [Raw: lines 151–166]. Do not infer that omission is generally valid from this example.

- The page lists 400 request-reading/understanding, 401 authentication, 403 permission, 422 validation and 500 processing failures. It specifies no creation/update/deletion action, verification review result, capability activation, payment result or funds movement for this GET. [Raw: lines 81–143]

## Detail locators

- Purpose, rate limits, TEST v4 server and business-line path ID: pinned raw lines 5–25.
- 200 identity, industry, service, verification-problem and conditional fields: lines 27–78; sample: lines 145–167.
- Error headings and optional problem-body fields: lines 81–143.

## Related

- [[adyen-platforms]] — platform legal-entity and verification context.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/get/businessLines/(id)/2026-11-03|GET one business line — captured 2026-11-03]]