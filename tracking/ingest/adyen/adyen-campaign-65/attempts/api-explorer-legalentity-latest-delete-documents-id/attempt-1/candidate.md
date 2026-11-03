---
title: "Adyen Legal Entity Management API v4: delete a document"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/delete/documents/(id)"
raw_files:
  - "adyen/api-explorer/legalentity/latest/delete/documents/(id)/2026-11-03.md"
tags: [adyen, legal-entity-management, documents, verification, api]
---

## Overview

This 2026-11-03 Legal Entity Management API v4 reference documents `DELETE /documents/{id}` for deleting a document. Its captured server is TEST `https://kyc-test.adyen.com/lem/v4`; `latest` does not establish current live access or account eligibility. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The required string path `id` is the document identifier. No query parameter or request body is shown. The page lists limits of 700 requests per five seconds live, 200 per five seconds test, and five failed requests per ten seconds; it gives no named caller role or idempotency key.
- The success entry is `204` and says to inspect the actual response code for request status. No success response body, field schema, or example is provided. This endpoint deletes a document resource; the page does not describe recovery, propagation timing, the effect on an existing verification decision or capability, or a separate review outcome. A successful deletion is not proof of verification approval, compliance, payment, payout, settlement, or bank receipt.
- Documented errors are 400 request problem, 401 authentication required, 403 insufficient permissions, 422 validation error, and 500 server processing failure. Their optional error fields include `errorCode`, `errorType`, `message`, `pspReference`, and `status`; the generic `pspReference` description does not turn document deletion into a payment operation. No 404 or version/conflict response is specified here.

## Detail locators

- Purpose, rate limits, TEST server and required path ID: pinned raw lines 5–25.
- `204` response wording: pinned raw lines 27–30.
- Error descriptions and optional payload fields: pinned raw lines 33–95.

## Related

- [[adyen-platforms]] — legal-entity verification context.
- [[source-adyen-api-explorer-legalentity-latest-post-documents]] — separate captured document-upload reference.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/delete/documents/(id)/2026-11-03|Legal Entity Management DELETE document snapshot]]