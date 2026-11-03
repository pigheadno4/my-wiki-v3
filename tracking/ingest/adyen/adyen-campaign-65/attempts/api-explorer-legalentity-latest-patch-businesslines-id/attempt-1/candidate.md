---
title: "Adyen Legal Entity Management API v4: PATCH /businessLines/{id}"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/patch/businessLines/(id)"
raw_files:
  - "adyen/api-explorer/legalentity/latest/patch/businessLines/(id)/2026-11-03.md"
tags: [adyen, legal-entity, business-line, platforms, verification, api]
---

## Overview

This 2026-11-03 Legal Entity Management API reference describes `PATCH /businessLines/{id}` to update a business line. The required path `id` is the business-line ID, distinct from the response's owning `legalEntityId`. The shown server is TEST `https://kyc-test.adyen.com/lem/v4`; the `latest` URL does not establish live access. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The request table marks top-level `industryCode`, `salesChannels`, `sourceOfFunds`, `webData` and `webDataExemption` optional; the page does not separately state whole-body requiredness or omitted-field PATCH behavior. `salesChannels` is required in combination with `service: paymentProcessing`; `sourceOfFunds` is required when the service is `banking` or `issuing`. The response lists `service` as required and permits `paymentProcessing`, `issuing` or `banking`, but this PATCH request table has no `service` field.
- When `sourceOfFunds` is present, its `adyenProcessedFunds` child is marked required; if false, `type` is required by prose. Other conditionally required source-of-funds fields vary by `type`: `amount` for business/asset sale/gambling winnings/inheritance; `financiers` for third-party funding, with required child amount, first and last name, and location; cryptocurrency exchange, dates, originator legal-entity ID, purpose, relationship, description or gambling website for their stated cases. Consult the raw rows for exact combinations, units and date format.
- `webData` lists sales website or app-store URLs. When it is required for a service but the user has no online presence, the page directs a reason in `webDataExemption`; its listed reason is `noOnlinePresence`. The request example updates industry code and web data only and does not establish a universal request shape.
- HTTP 200 returns the business-line `id`, `industryCode`, owning `legalEntityId` and `service` as required fields. Optional fields include sales channels, source-of-funds, web data and `problems` with verification errors. A returned business-line representation or error list does not prove verification completion, enabled capabilities or payment/funds outcomes.
- The page states limits of 700 requests per five seconds LIVE, 200 per five seconds TEST, and five failed requests per ten seconds. It documents 400, 401, 403, 422 and 500 errors. The generic error schema's optional `pspReference` is labeled as a payment reference; this is still a business-line update, not a payment operation.

> [!warning] Contradiction
> The request/response tables say `sourceOfFunds.amount` is required when `type` is `business`, but the 200 banking/business example omits `amount`. The example does not remove that stated condition. The `originatorLegalEntityId` row also refers to `originatorOfFundsReference` in its example prose; preserve the table field name without treating the prose spelling as a second API field.

## Detail locators

- Purpose, rate limits, TEST base and path ID: pinned raw lines 5–25.
- Complete PATCH request table, conditional source-of-funds fields and web-data exemption: `## Parameters > ### Request body`, lines 28–56.
- Illustrative update request: `## Request examples`, lines 58–70.
- Full 200 response schema, verification-error shape and owner/service IDs: `## Responses > ### 200 Success`, lines 71–122.
- Error schemas: lines 125–187; 200 banking/business example with omitted `amount`: `## Response examples`, lines 189–212.

## Related

- [[adyen-platforms]] — platform onboarding and verification context.
- [[source-adyen-api-explorer-legalentity-latest-get-legalentities-id-businesslines]] — separate business-line list readback, with a related amount/example conflict.
- [[source-adyen-docs-platforms-account-structure-resources-legal-entity-management]] — separate business-line resource guide.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/patch/businessLines/(id)/2026-11-03|PATCH business line, 2026-11-03 capture]]