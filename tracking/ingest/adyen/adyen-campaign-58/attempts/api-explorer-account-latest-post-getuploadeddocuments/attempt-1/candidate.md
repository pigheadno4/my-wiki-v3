---
title: "Adyen Account API v6: POST /getUploadedDocuments"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Account/latest/post/getUploadedDocuments"
raw_files:
  - "adyen/api-explorer/Account/latest/post/getUploadedDocuments/2026-09-15.md"
tags: [adyen, classic-platforms, account-api, verification, documents]
---

## Overview

This captured Account API page describes `POST /getUploadedDocuments`, which returns documents previously uploaded for an account holder; Adyen uses those documents during verification. The listed server is the Account v6 TEST endpoint, `https://cal-test.adyen.com/cal/services/Account/v6`. The request body requires `accountHolderCode`; `bankAccountUUID` and `shareholderCode` are optional selectors. The example includes an account-holder code and bank-account UUID, but does not make that selector mandatory.

## Key takeaways

- The optional 200-response `documentDetails` array describes linked document metadata: account-holder code, bank-account UUID, description, document type, filename, legal-arrangement and entity codes, shareholder code, and signatory code. Within each returned document-detail object, `documentType` is marked required; the table lists permitted types and their meanings. The response schema shown here does not include a document-content field or establish verification approval.
- The response descriptions conditionally require a linked `bankAccountUUID` for a `BANK_STATEMENT` submitted to verify a bank account, and a linked `shareholderCode` for listed identity-document types when the account holder's `legalEntity` is **Business**. These are descriptions of document linkage in the response schema, not extra required request-body properties.
- The `DRIVING_LICENCE_BACK` description says both `DRIVING_LICENCE_FRONT` and `DRIVING_LICENCE_FRONT` must be submitted, while the adjacent front entry names front and back. This is an internal wording conflict in the captured page; consult the linked verification-check guidance before relying on that pair requirement.
- A 200 says the request succeeded and lists optional `invalidFields`, request `pspReference`, and `resultCode`. The page lists 400, 401 (authentication required), 403 (insufficient permissions), 422, and 500 responses. Retrieving uploaded document details does not, by itself, prove a successful verification decision, current live availability, or a payment or payout outcome.

## Detail locators

- Purpose, Account v6 TEST server, request fields, and illustrative request: pinned raw lines 5–29.
- 200 response document details, conditional linkage descriptions, type list, and internal licence wording conflict: pinned raw lines 30–56.
- Error response descriptions and fields: pinned raw lines 59–121.
- Illustrative 400 and 403 JSON responses: pinned raw lines 123–147.

## Related

- [[adyen-classic-platforms]] — Classic account-holder and verification context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/Account/latest/post/getUploadedDocuments/2026-09-15|Account API v6 POST /getUploadedDocuments capture (2026-09-15)]]
