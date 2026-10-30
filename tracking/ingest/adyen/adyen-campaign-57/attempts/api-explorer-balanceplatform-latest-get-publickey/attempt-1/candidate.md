---
title: "Adyen Balance Platform API: get RSA public key"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/publicKey"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/publicKey/2026-09-15.md"
tags: [adyen, balance-platform, issuing, api-reference, encryption]
---

## Overview

Captured Balance Platform API v2 reference for `GET /publicKey`, which returns an RSA public key used to generate the `encryptedKey` for PIN change, PIN reveal, or PAN reveal. The captured server is the test endpoint `https://balanceplatform-api-test.adyen.com/bcl/v2`. This is a key-retrieval contract, not evidence that a PIN or PAN action succeeded. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- Both query parameters are optional: `format` selects `jwk` or `pem` and defaults to `pem`; `purpose` selects `pinChange`, `pinReveal`, or `panReveal` and defaults to `pinReveal`. Select the purpose for the intended operation instead of assuming the default covers all three.
- A 200 response requires `publicKey` and `publicKeyExpiryDate`. The key is described as encrypting a symmetric session key; the expiry date matters when using it later. This response alone says nothing about the later PIN/PAN operation or cardholder authorization.
- The reference lists 401 authentication, 403 permission, 422 validation, and 500 server errors. Its generic 422/500 examples describe balance-account and payment-instrument operations, so they do not establish endpoint-specific constraints or effects for `GET /publicKey`.

## Detail locators

- Raw `## Parameters` / `### Query parameters`: `format` and `purpose` values, optionality, and defaults.
- Raw `## Responses`: success fields and error schemas.
- Raw `## Response examples`: illustrative success and generic error bodies; the sample expiry date is illustrative.

## Related

- [[source-adyen-docs-issuing-manage-card-data-change-pin]] — PIN-change flow.
- [[source-adyen-docs-issuing-manage-card-data-reveal-pin]] — PIN-reveal flow.
- [[source-adyen-docs-issuing-manage-card-data-reveal-card-details]] — PAN/card-detail reveal flow.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/publicKey/2026-09-15|Balance Platform v2 GET /publicKey reference (2026-09-15 capture)]]
