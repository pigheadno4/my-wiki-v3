---
title: "Adyen Balance Platform API v2: GET /paymentInstruments/{id}"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/2026-11-02.md"
tags: [adyen, balance-platform, payment-instruments, issuing, api]
---

## Overview

This 2026-11-02 Balance Platform API v2 reference describes `GET /paymentInstruments/{id}` for details of one card or bank-account payment instrument. The displayed server is TEST, `https://balanceplatform-api-test.adyen.com/bcl/v2`; `latest` is a documentation route, not independent proof of current live availability. See [[adyen]], [[adyen-issuing]] and [[adyen-business-accounts]].

## Key takeaways

- `id`, the payment-instrument identifier, is the only required **path** parameter. The page lists no query parameter, request body, or idempotency contract for this read.
- A 200 response schema requires the linked `balanceAccountId`, instrument `id`, `issuingCountryCode`, and `type` (`card` or `bankAccount`). `card` and `bankAccount` are optional type-dependent response objects; fields marked required beneath an optional parent do not make that parent a GET input. Other optional response fields include status, status reason/comment, group ID and replacement links.
- The status description distinguishes active, inactive, suspended, and irreversibly closed. It notes active as a creation default with card form-factor and issuing-country exceptions, such as inactive US physical cards. This GET does not create or change status. Its example shows `active` alongside a January 2024 card expiry in a 2026 capture; that example cannot establish current card usability or a successful authorization or capture.
- The card schema says CVC is returned only in the **POST** response for single-use virtual cards; PAN is masked by default. The GET example contains a masked number and no CVC. Do not infer card-detail reveal from this endpoint; the separate reveal route has its own contract.
- Documented errors are 400, 401 (authentication required), 403 (insufficient permissions), 422, and 500. The 422 example concerns a `balanceAccountId` change and the 500 example concerns instrument creation, rather than this read; they are generic examples, not GET-specific failure conditions.

## Detail locators

- Purpose, captured TEST server and required path ID: pinned raw lines 5–17.
- 200 resource schema, type branches, card detail limits and status fields: pinned raw lines 19–90.
- Error schemas and illustrative 200/error bodies: pinned raw lines 93–286.

## Related

- [[adyen-issuing]] — issued-card context.
- [[adyen-business-accounts]] — bank-account instrument context.
- [[source-adyen-api-explorer-balanceplatform-latest-get-paymentinstruments-id-reveal]] — separate card-detail reveal route.
- [[source-adyen-api-explorer-balanceplatform-latest-post-paymentinstruments]] — separate creation endpoint.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/2026-11-02|Payment-instrument GET snapshot]]