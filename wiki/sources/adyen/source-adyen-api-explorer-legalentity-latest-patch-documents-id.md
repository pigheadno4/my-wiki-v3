---
title: "Adyen Legal Entity Management API v4: Update a document"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/patch/documents/(id)"
raw_files:
  - "adyen/api-explorer/legalentity/latest/patch/documents/(id)/2026-11-03.md"
tags: [adyen, legal-entity-management, platforms, documents, verification, api-reference]
---

## Overview

The 2026-11-03-captured Legal Entity Management API v4 TEST reference describes `PATCH /documents/{id}` to update the document named by required path `id`. A `200` response means this update request succeeded; it is not an Adyen verification decision or capability approval. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- `description` and document `type` are required in the request body. The type choices depend on the legal entity category; `bankStatement` is the named type for a transfer instrument. The optional `owner` object has required nested `id` and `type` when supplied: `legalEntity` owner ID names a legal entity, while `bankAccount` owner ID names a transfer instrument. Neither owner ID is the document path ID.
- Optional singular `attachment` and plural `attachments` fields carry Base64 `content` required within each supplied object, plus optional file format, name and page fields. The listed formats are PDF, JPG/JPEG and PNG. Photo IDs have a 15-page maximum. For `driversLicense` or `identityCard`, `pageType` must be `front` or `back` and both sides must be included in the same API request; for other types, omitted `pageType` leads to inferred page order. Optional expiry, filename, issuer country/state and document number fields have further raw-schema detail.
- The optional `x-requested-verification-code` header describes `0_0001` for resolving document suberrors in TEST only. The captured server is `https://kyc-test.adyen.com/lem/v4`. The page states 700 requests per five seconds live, 200 per five seconds test, and five failed requests per ten seconds. Listed errors are `400`, `401`, `403`, `422` and `500`.
- In the `200` schema, `description` and `type` are required; response `id`, `owner`, `attachment(s)` and dates are optional. The example includes an ID, legal-entity owner and Base64 attachment, but does not demonstrate review, successful verification, compliance approval, capability permission, payment or payout. No idempotency key, propagation/verification timing or version-conflict behavior is specified. The dated TEST snapshot is not proof of current live eligibility.

## Detail locators

- Raw lines 5–33: operation, 15-page photo-ID maximum, rate limits, TEST server, document path ID and TEST-only header.
- Raw lines 36–60: complete request schema, optional attachment parents with required `content`, two-sided ID rule, owner identity and conditional document types.
- Raw lines 62–70: request example with type and description only.
- Raw lines 71–103: `200` response schema and optional response ID/owner/attachment fields.
- Raw lines 106–168: `400`, `401`, `403`, `422` and `500` error schemas.
- Raw lines 170–190: illustrative `200` response with attachment and legal-entity owner.

## Related

- [[adyen-platforms]] — Platforms legal-entity document and verification context; this v4 reference governs the PATCH contract.
- [[source-adyen-api-explorer-legalentity-latest-post-documents]] — separate document creation/upload reference.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/patch/documents/(id)/2026-11-03|Update document API reference (2026-11-03)]]