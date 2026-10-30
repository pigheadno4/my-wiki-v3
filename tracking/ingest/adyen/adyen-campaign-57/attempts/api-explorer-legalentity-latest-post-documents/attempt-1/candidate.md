---
title: "Adyen Legal Entity Management API v4: upload a verification document"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/post/documents"
raw_files:
  - "adyen/api-explorer/legalentity/latest/post/documents/2026-09-15.md"
tags: [adyen, platforms, legal-entity, verification, documents, api]
---

## Overview

This captured Legal Entity Management API v4 test-server reference documents `POST /documents` to upload a document for verification checks. Adyen first runs automated checks from legal-entity information and may ask for additional documents when those checks fail; the page advises uploading only when Adyen requests them. A successful upload is not verification approval. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The request table marks `description` and `type` required. It lists singular `attachment` and plural `attachments` as optional containers, but `content` is required within an attachment supplied and must be Base64 encoded. The page does not make either attachment container unconditionally required in its schema.
- Optional `owner` has required nested `id` and `type` when present: `legalEntity` maps to a legal-entity ID, while `bankAccount` maps to a transfer-instrument ID. Document `type` values depend on legal-entity type; `bankStatement` is the listed type for transfer-instrument documents. Supported content types are PDF, JPG/JPEG and PNG.
- For `driversLicense` or `identityCard`, each side must have `pageType` front/back and both sides must be included in one API request. Photo IDs are limited to 15 pages. This page specifies no byte-size limit.
- The optional `x-requested-verification-code` header accepts one suberror code per request and is test-only. Published limits are 700 requests per five seconds live, 200 per five seconds test, and five failed requests per ten seconds.
- A 200 says the upload request succeeded and may include a document `id`; it does not say checks passed or a capability was approved. Listed errors are 400, 401, 403, 422 and 500. The captured server is `https://kyc-test.adyen.com/lem/v4`; `latest` is not a fixed current release.

## Detail locators

- Purpose, upload advice, page/rate limits, test server: pinned raw lines 5–24.
- Test-only header and request fields/type matrix: pinned raw lines 28–58; request example: lines 60–77.
- Response fields and example: pinned raw lines 78–110, 177–198.
- Error status/schema sections: pinned raw lines 113–175.

## Related

- [[adyen-platforms]] — platform onboarding and verification context.
- [[source-adyen-docs-platforms-verification-requirements-document-requirements]] — separate country, entity, product and document conditions.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/post/documents/2026-09-15|Captured POST /documents API Explorer page]]
