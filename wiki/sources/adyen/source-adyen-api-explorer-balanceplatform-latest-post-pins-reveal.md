---
title: "Adyen Balance Platform API v2: reveal an encrypted card PIN block"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/pins/reveal"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/pins/reveal/2026-09-15.md"
tags: [adyen, balance-platform, issuing, pin, api]
---

## Overview

This captured API Explorer reference documents `POST /pins/reveal` on the Balance Platform API v2 test server. For the card identified by its `paymentInstrumentId`, it returns an **encrypted PIN block**, not a plaintext PIN. Decrypted data can be used to display the PIN in a user interface. See [[adyen]], [[adyen-issuing]], and the separate [[source-adyen-docs-issuing-manage-card-data-reveal-pin]] guide for the broader client flow.

## Key takeaways

- The API credential must have the `Bank Issuing PIN Reveal Webservice` role. The request schema marks `paymentInstrumentId` and `encryptedKey` required; `encryptedKey` is the symmetric session key encrypted with Adyen's public key.
- A 200 response marks the request successful and requires `encryptedPinBlock` and a 16-digit `token` needed to extract it. The reference does not itself specify the full client-side decryption procedure, prove that a user saw the PIN, or establish cardholder authentication or payment authorization.
- Listed errors are 401 (authentication), 403 (insufficient permission), 422 (validation), and 500 (server error). The generic 422 and 500 examples discuss unrelated payment-instrument changes/creation; they do not specify this endpoint's PIN or card lifecycle behavior.
- The only captured server is `https://balanceplatform-api-test.adyen.com/bcl/v2`. The `latest` URL does not establish a fixed current release or live account access.

## Detail locators

- Purpose, role, and test server: pinned raw lines 5–14.
- Required request fields and request example: pinned raw lines 18–32.
- Success response fields and example: pinned raw lines 35–42, 124–134.
- Error schemas and examples: pinned raw lines 45–122, 136–188.

## Related

- [[adyen-issuing]] — issuer-side card management context.
- [[source-adyen-api-explorer-balanceplatform-latest-get-publickey]] — separate public-key endpoint reference.
- [[source-adyen-docs-issuing-manage-card-data-reveal-pin]] — separate PIN-reveal flow guide.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/pins/reveal/2026-09-15|Captured POST /pins/reveal API Explorer page]]
