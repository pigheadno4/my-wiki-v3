---
title: "Adyen Legal Entity Management API v4: GET /documents/{id}"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/get/documents/(id)"
raw_files:
  - "adyen/api-explorer/legalentity/latest/get/documents/(id)/2026-11-03.md"
tags: [adyen, legal-entity, platforms, verification, documents, api]
---

## Overview

This 2026-11-03-captured Legal Entity Management API v4 reference describes `GET /documents/{id}` for retrieving one document by its unique ID. The listed server is TEST `https://kyc-test.adyen.com/lem/v4`; the page separately gives Live and Test rate limits. The `latest` documentation route is not evidence of current live access. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- Required path `id` is the document ID. Optional boolean query `skipContent` means “do not load document content while fetching the document.” The reference does not state a default or exact omitted-content response shape. No GET request body, specific caller role or idempotency key is documented.
- The 200 response table marks root `description` and `type` required; `id`, `owner`, `attachment` and `attachments` are optional. If an `attachment` or `attachments` item is present, its nested Base64 `content` field is table-required. Read this nested requiredness in context of the optional parent and `skipContent`; do not infer that content is always returned. The success example contains an organization registration document with one attachment and legal-entity owner, but is not a universal response template.
- Optional `owner` has required child `id` and `type` if present; owner type `legalEntity` uses a legal-entity ID, while `bankAccount` uses a transfer-instrument ID. Document `type` varies by entity type, and `bankStatement` is cited for transfer instruments. The schema also lists format, page side, filename and date fields; its front/back ID-card prose describes upload behavior and should not be interpreted as a GET requirement.
- Captured limits are 700 requests per 5 seconds in Live, 200 per 5 seconds in Test, and 5 failed requests per 10 seconds. The page lists 400, 401, 403, 422 and 500 errors. Its generic error response includes optional payment-labeled `pspReference`, which does not make document retrieval a payment operation. A 200 readback establishes neither document validation nor legal-entity verification, capability approval, PCI compliance or funds movement.

## Detail locators

- Purpose, rates, TEST server, path and optional `skipContent`: pinned raw lines 5–31.
- Response parent/child requiredness, owner identity and document types: `## Responses > ### 200 Success`, lines 33–65.
- Generic error schemas: lines 68–130. Illustrative response JSON: lines 132–153.

## Related

- [[adyen-platforms]] — legal-entity verification context.
- [[source-adyen-api-explorer-legalentity-latest-post-documents]] — separate document-upload reference.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/get/documents/(id)/2026-11-03|Legal Entity document GET snapshot]]