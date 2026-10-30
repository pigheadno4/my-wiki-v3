---
title: "Adyen Balance Platform API: change a card PIN"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/pins/change"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/pins/change/2026-09-15.md"
tags: [adyen, balance-platform, issuing, pin, api-reference]
---

## Overview

Captured Balance Platform API v2 test-server reference for `POST /pins/change`, which requests a PIN change for the card identified by `paymentInstrumentId`. The API credential needs the **Bank Issuing PIN Change Webservice role**. This endpoint is distinct from fetching the public key and from revealing a PIN or PAN. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- The request-body schema lists four required properties: `paymentInstrumentId` (the card), `encryptedKey` (a symmetric session key encrypted with Adyen's public key), `encryptedPinBlock`, and the 16-digit `token` used to generate that block. The capture does not separately mark the body object as required. See the raw `### Request body` and the related public-key reference.
- A 200 response requires a request `status` with values `completed`, `pending`, or `unavailable`. A successful HTTP response or the sample `completed` value does not establish that every submitted PIN change completed; inspect the returned status.
- The documented errors are 401 authentication, 403 insufficient permission, 422 validation, and 500 server failure. The generic 422/500 examples refer to balance-account reassignment and payment-instrument creation, so they do not establish PIN-change-specific constraints or effects.

## Detail locators

- Raw `## Parameters` / `### Request body`: required properties and descriptions.
- Raw `## Request examples`: illustrative encrypted values and card identifier.
- Raw `## Responses` and `## Response examples`: status enum, error schemas, and illustrative bodies.

## Related

- [[source-adyen-api-explorer-balanceplatform-latest-get-publickey]] — RSA public-key retrieval for generating `encryptedKey`.
- [[source-adyen-docs-issuing-manage-card-data-change-pin]] — PIN-change guide with broader flow context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/pins/change/2026-09-15|Balance Platform v2 POST /pins/change reference (2026-09-15 capture)]]
