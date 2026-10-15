---
title: "Classic API 3DS2 data-only flow | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/other-3ds-flows/data-only"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/other-3ds-flows/data-only/2026-09-15.md"
tags: [adyen, classic-api, 3ds2, data-only, mastercard]
---

## Overview

This 2026-09-15 capture of a page last modified in 2019 describes 3D Secure 2 **data-only** through Classic Payment API `/authorise`. Adyen says it no longer accepts new Classic integrations and directs migration to Checkout API. This is a dated Classic route, distinct from [[source-adyen-docs-online-payments-3d-secure-data-only|the separately retained Checkout-era data-only guide]]. See [[adyen]] and [[adyen-3d-secure]].

## Key takeaways

- In the page's comparison, a regular 3DS2 flow authenticates with the issuer before authorization. In data-only, the merchant sends 3DS2 data; the scheme handles the authentication-request path and adds its risk data to the authorization message sent to the issuer. The page says no shopper 3DS2 challenge or strong customer authentication occurs, so chargeback liability remains with the merchant rather than shifting to the issuer. Data sharing is not proof of shopper authentication or successful payment authorization.
- This Classic snapshot says data-only was **only available for Mastercard** and warns that using it in markets requiring SCA, such as the EEA example, can increase authentication rejections. The later Checkout-era source describes Visa and Mastercard; do not apply its broader scheme scope retroactively to this Classic guide, or treat the 2019 statement as current universal eligibility.
- The guide's Classic request sets `additionalData.threeDS2DataOnly: true` in `/authorise`. Other required fields and the response depend on the regular 3DS2 flow for the chosen integration; the page routes to browser, iOS, Android, and authentication-only guides. The sample uses a Payment API v50 test URL, not a modern Checkout `/payments` contract.
- It lists a test account, API key, and API library as setup steps, and gives a dated Mastercard test card. Its statement that scheme risk models may improve authorization in specific markets is a possibility, not a transaction outcome guarantee.

## Detail locators

- Classic lifecycle and Checkout migration: lines 19–23.
- Scheme/issuer data route, Mastercard-only and SCA-market warning: lines 25–27.
- Risk-model claim, no challenge, and liability boundary: `Using the data-only flow`, lines 29–37.
- Test-account, API-key, and library setup: `Before you begin`, lines 39–45.
- Classic `/authorise` flag, integration-specific required fields and response, and API v50 example: `Submit a data-only payment request`, lines 47–70.
- Dated test fixture: `Testing the data-only flow`, lines 72–78.

## Related

- [[adyen-3d-secure]] — provider 3DS2 routes and outcome boundaries.
- [[source-adyen-docs-online-payments-3d-secure-data-only]] — separate Checkout-era data-only source with broader documented scheme scope.

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/other-3ds-flows/data-only/2026-09-15|Classic 3DS2 data-only flow (2026-09-15)]]
