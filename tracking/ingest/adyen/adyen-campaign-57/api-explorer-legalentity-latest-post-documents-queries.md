# Fixed retrieval queries: api-explorer-legalentity-latest-post-documents

Source: `wiki/sources/adyen/source-adyen-api-explorer-legalentity-latest-post-documents.md` — https://docs.adyen.com/api-explorer/legalentity/latest/post/documents
Pinned raw: `raw/adyen/api-explorer/legalentity/latest/post/documents/2026-09-15.md` (SHA-256 `43fc99fdaa53eec4b13833de6c0a8d6f27803156340a0422d54e8a070e1d6b59`).

## Q1

For `legalentity/latest/post/documents`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** `POST /documents` uploads a document for verification checks; the page advises doing so only after Adyen requests additional information following failed automated legal-entity checks (raw lines 5–11). The body schema requires `description` and document `type`; optional `attachment` or `attachments` containers have required Base64 `content` within supplied entries (lines 34–49, 58). Optional `owner` has required nested ID/type if provided: `legalEntity` ID versus `bankAccount` transfer-instrument ID (lines 55–57). Type values depend on entity type, and `bankStatement` is used for transfer-instrument documents (line 58). Identity card/driver's license sides must both be supplied in one request with front/back `pageType`; photo IDs have a 15-page maximum, and accepted content types are PDF/JPG/JPEG/PNG (lines 13, 39–48). No byte-size ceiling is stated. The test-only requested-verification-code header takes one suberror code (lines 28–31); captured rate limits are lines 15–21. The page lists 401 authentication and 403 permission failures but no specific credential role (lines 126–140).

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** A 200 says the upload request succeeded; its schema lists an optional document ID and repeats document metadata, while the example shows a returned ID (lines 80–110, 177–198). It does not establish successful verification or enabled capabilities. Listed errors are 400, 401, 403, 422 and 500 (lines 113–175). No deletion, review timing, propagation, payment or funds outcome is specified. The only server shown is LEM v4 TEST; `latest` is not a fixed release or proof of live eligibility (lines 1–24).

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-legalentity-latest-post-documents.md` — https://docs.adyen.com/api-explorer/legalentity/latest/post/documents
