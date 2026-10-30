---
title: "Adyen Balance Platform API GET /grantOffers — available grant offers"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/grantOffers"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/grantOffers/2026-09-15.md"
tags: [adyen, capital, balance-platform-api, grant-offers]
---

## Overview

This 2026-09-15 capture of the Balance Platform API Explorer `GET /grantOffers` reference shows a test server at `/bcl/v2`. It describes returning grant offers available for the supplied `accountHolderId`. The query parameter is required; the response's `grantOffers` array is required and each offer's `accountHolderId` identifies the account holder to which it is offered. This is an offer lookup for [[adyen-capital]], not a grant request, acceptance, disbursement or repayment record.

## Key takeaways

- The query table calls `accountHolderId` the unique identifier of the **grant account**, while the overview and response row identify an **account holder**. The captured reference does not resolve that identity conflict; do not substitute a grant-account ID on this page's authority alone.
- The 200 schema lists optional offer fields including principal `amount`, `contractType` (`cashAdvance` or `loan`), validity dates, fee, offer `id` and repayment configuration. Where the optional parent object is present, nested rows mark currency/value, fee amount or repayment basis points required; this does not make the optional parent required.
- Listed errors are 400 (request problem), 401 (authentication), 403 (insufficient permission), 422 (validation) and 500 (server processing). The generic 422 and 500 examples describe payment-instrument operations, so they do not establish grant-offer-specific status rules or failures.
- This captured contract gives no named credential role, eligibility gate, offer-count or expiry guarantee, live endpoint, current `latest` version, or evidence that any account holder received an offer or funds.

## Detail locators

- `## Servers` and `## Parameters` → captured test base URL and required query parameter.
- `## Responses` → 200 offer fields, nested requiredness and error response schemas.
- `## Response examples` → generic 400/401/403/422/500 payloads; the latter two include unrelated payment-instrument details.

## Related

- [[adyen]] — provider.
- [[adyen-capital]] — financing product and offer context.
- [[source-adyen-docs-capital-get-grant-offers]] — offer-choice documentation; separate from this endpoint contract.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/grantOffers/2026-09-15|2026-09-15 captured API Explorer reference]]
