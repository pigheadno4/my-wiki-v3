---
title: "DELETE /businessLines/{id} — Delete a business line | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/delete/businessLines/(id)"
raw_files:
  - "adyen/api-explorer/legalentity/latest/delete/businessLines/(id)/2026-11-03.md"
tags: [adyen, legal-entity-management, business-lines, api-explorer]
---

## Overview

This [[adyen]] Legal Entity Management API Explorer snapshot documents `DELETE /businessLines/{id}`, which deletes a business line. The captured server is TEST `https://kyc-test.adyen.com/lem/v4`; the URL says `latest` while the server path identifies `v4`. See [[adyen-platforms]] for platform and legal-entity context.

## Key takeaways

- Required string path `id` identifies the business line to delete. The page lists no query parameters, request body, caller role, conditional request fields or idempotency key. It specifies rate limits of 700 requests per five seconds in live environments, 200 per five seconds in test, and five failed requests per ten seconds; only a TEST server URL is listed. [Raw: lines 5–27]
- Deleting a business line removes it from **all linked merchant accounts**. If the line is linked to a payment method, deletion **can affect** a merchant account's ability to use that method. The page gives no affected-account list, propagation timing, rollback or recovery procedure. Preserve this cross-account effect when assessing the deletion. [Raw: lines 7–9]
- The success section is `204` and instructs readers to look at the actual response code for request status. It documents no success response body, returned business-line state or confirmation of when linked merchant-account changes have propagated. [Raw: lines 29–33]
- Listed failures are 400 request-reading/understanding, 401 authentication, 403 insufficient permissions, 422 validation and 500 server processing. The generic error-body fields are optional, and the page does not specify duplicate deletion, state-conflict or retry semantics. [Raw: lines 35–97]
- A successful delete response is about this business-line request and the stated link-removal effect; it does not establish legal-entity verification, payment-method usability for a particular account after propagation, successful payment, payout, settlement or bank receipt. This dated TEST v4 snapshot does not prove current live availability. [Raw: lines 5–33]

## Detail locators

- Purpose, linked-merchant-account and payment-method effect, limits and TEST v4 server: pinned raw lines 5–20.
- Required business-line path ID and 204 success: lines 22–33.
- Error meanings and response-body schemas: lines 35–97.

## Related

- [[adyen-platforms]] — platform legal-entity and business-line context.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/delete/businessLines/(id)/2026-11-03|DELETE business line — captured 2026-11-03]]