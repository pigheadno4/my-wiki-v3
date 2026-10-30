---
title: "Adyen Legal Entity Management API: create a business line"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/post/businessLines"
raw_files:
  - "adyen/api-explorer/legalentity/latest/post/businessLines/2026-09-15.md"
tags: [adyen, legal-entity, business-line, verification, api-reference]
---

## Overview

Captured Legal Entity Management API v4 test-server `POST /businessLines` reference. A business line records a user's industry and source-of-funds information for verification and belongs to the legal entity named by `legalEntityId`; the returned `id` identifies the business line, not the legal entity. Adyen says verification results arrive through webhooks or API responses, so creation alone does not establish verified capabilities. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The request property table requires `industryCode`, `legalEntityId`, and `service` (`paymentProcessing`, `issuing`, or `banking`). It does not separately mark the enclosing body object required. `salesChannels` is required with `paymentProcessing`; `sourceOfFunds` is required with `banking` or `issuing`. Within `sourceOfFunds`, `adyenProcessedFunds` is required, and `type` is required when that boolean is false. Further fields depend on the fund type; use the raw table for those conditions and web-data rules.
- The captured page caps **payment-processing** business lines at 200 per legal entity. Its stated rate limits are 700 requests per five seconds in live, 200 in test, and five failed requests per ten seconds; these are snapshot statements, not current capacity guarantees.
- A 200 response requires the business-line `id`, `industryCode`, `legalEntityId`, and `service`. Optional `problems` may contain verification errors; receipt of a created business line is not approval, enabled capability, or successful payment/funds movement.

## Detail locators

- Raw `## Parameters` / `### Request body`: all conditional source-of-funds, website, and sales-channel fields. Nested required properties apply when their containing object is present.
- Raw `## Request examples`: banking, issuing, and payment-processing examples; values are illustrative.
- Raw `## Responses`: success/verification-problem fields and 400/401/403/422/500 error schemas.

## Related

- [[source-adyen-docs-platforms-account-structure-resources-legal-entity-management]] — resource relationships.
- [[source-adyen-docs-platforms-verification-requirements-reference-additional-products]] — additional-capability verification context.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/post/businessLines/2026-09-15|LEM v4 POST /businessLines reference (2026-09-15 capture)]]
