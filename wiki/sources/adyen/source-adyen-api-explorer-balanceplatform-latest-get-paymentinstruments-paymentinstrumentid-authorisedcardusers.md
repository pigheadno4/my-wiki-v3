---
title: "GET /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers — Get authorized card users | Adyen"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/(paymentInstrumentId)/authorisedCardUsers"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/paymentInstruments/(paymentInstrumentId)/authorisedCardUsers/2026-11-02.md"
tags: [adyen, balance-platform, issuing, payment-instruments, api-explorer]
---

## Overview

This [[adyen]] Balance Platform API Explorer snapshot documents `GET /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers`, which returns authorized users for a card as legal-entity IDs linked to the specified payment instrument. The captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; the URL says `latest` while the server path identifies `v2`. The path identifies a payment instrument, and the response field identifies legal entities; neither is an account-holder or balance-account ID. See [[adyen-issuing]] for card-program resource context.

## Key takeaways

- The only listed request parameter is required string path `paymentInstrumentId`; its description cell is blank. The page lists no query parameters, request body, default, pagination or limit for this GET. [Raw: lines 9–17]
- The 200 response is labeled a successful operation. Its sole response-body field, `legalEntityIds`, is an optional array of strings described as the legal entity IDs of authorized card users linked to the specified payment instrument. The example contains two IDs, but that count and their values are illustrative, not a minimum or proof of a particular live card's users. [Raw: lines 19–27, 105–117]
- Listed failures are 401 unauthorized, 403 forbidden, 404 not found and 422 validation. The error-body fields are optional at the top level; required `invalidFields` children apply only within an included array item. The 403 example says a card partner is not yet allowed, the 404 example names a missing payment instrument, and the 422 example names no linked legal entity. These are sample error details, not universal rules for every request. [Raw: lines 30–103, 119–170]
- Readback of legal-entity IDs does not itself create or activate a card, verify the legal entities or account holder, approve an issuing capability, authorize a transaction, capture a payment, book funds or establish settlement. This endpoint has no response fields for those outcomes. [Raw: lines 5–27, 105–117]

## Detail locators

- Purpose, TEST v2 server and path ID: pinned raw lines 5–17.
- 200 body schema and successful example: lines 19–27, 105–117.
- Error headings, optional error-body fields and examples: lines 30–103, 119–170.

## Related

- [[adyen-issuing]] — issuing card and payment-instrument resource context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/paymentInstruments/(paymentInstrumentId)/authorisedCardUsers/2026-11-02|GET authorized card users — captured 2026-11-02]]