---
title: "Adyen Legal Entity Management API v4: get an onboarding link theme"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/get/themes/(id)"
raw_files:
  - "adyen/api-explorer/legalentity/latest/get/themes/(id)/2026-11-03.md"
tags: [adyen, legal-entity-management, hosted-onboarding, themes, api]
---

## Overview

This captured Legal Entity Management API v4 reference describes `GET /themes/{id}`, which returns details for the onboarding link theme identified by the required path `id`. The listed server is the TEST `https://kyc-test.adyen.com/lem/v4`; the page also states separate Live and Test rate limits. A returned theme is configuration data, not evidence that an onboarding link was issued, a legal entity was verified, or a payment or payout completed. See [[adyen-platforms]] and [[adyen]].

## Key takeaways

- `id` is the theme's unique identifier in the path. The capture lists no query or request-body parameters. The 200 body requires `createdAt`, `id`, and `properties`; `description` and `updatedAt` are optional. The properties object is described as `object (string)`; property names in the example are illustrative, not a stated required set.
- Published endpoint limits are 700 requests per 5 seconds in Live and 200 per 5 seconds in Test. Failed requests have a separate limit of 5 failures per 10 seconds.
- The reference lists 400 request-understanding, 401 authentication, 403 permission, 422 validation, and 500 server errors. It does not state a role, idempotency contract, theme deletion or update behavior, or propagation timing for this GET operation.

## Detail locators

- Purpose, limits, and TEST server: raw lines 5–18.
- Required path identity and 200 response schema: raw lines 20–39.
- Error response tables: raw lines 42–104. The generic error schema includes an optional `pspReference` description but does not turn this theme lookup into a payment operation.
- Illustrative 200 JSON response and example properties: raw lines 106–128.

## Related

- [[source-adyen-api-explorer-legalentity-latest-get-themes]] — captured list of themes.
- [[adyen-platforms]] — platform onboarding context.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/get/themes/(id)/2026-11-03|GET /themes/{id} captured 2026-11-03]]
