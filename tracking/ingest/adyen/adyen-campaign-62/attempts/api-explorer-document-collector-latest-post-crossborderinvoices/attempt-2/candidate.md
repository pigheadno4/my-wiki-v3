---
title: "Adyen Document Collector POST /crossBorderInvoices — upload document"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Document-Collector/latest/post/crossBorderInvoices"
raw_files:
  - "adyen/api-explorer/Document-Collector/latest/post/crossBorderInvoices/2026-09-15.md"
tags: [adyen, document-collector, invoice, merchant-account]
---

## Overview

This captured **Document Collector latest** API Explorer page describes `POST /crossBorderInvoices` for uploading a document belonging to a merchant account. It lists test and live `/v1` Document Collector server URLs. Its “latest” navigation label does not add a separate version number beyond those listed URLs. [[adyen]] [[adyen-account-structure]]

## Key takeaways

- The request body requires `context` with the sole listed value `paCbInvoice`, a PDF `file` named `{pspReference}.pdf`, and `merchantAccount` identifying the account that owns the document. The example shows a binary PDF placeholder, not a literal upload encoding specification. See raw lines 17–35.
- `201 Success` says the document was uploaded successfully. Optional response properties are `context`, `fileName`, `merchantAccount`, and `pspReference` extracted from the filename. The example has values for all four; the table does not require them. See raw lines 36–47 and 144–156.
- The page documents `400`, `401`, `403`, `422`, and `500` errors with optional problem-detail fields, including optional `requestId` and `invalidFields`. If an `invalidFields` item is present, its `message`, `name`, and `value` are marked required. The `403` and `422` example bodies illustrate account-access and PDF-filename validation failures, not an exhaustive error policy. See raw lines 50–142 and 158–224.
- Upload success establishes document receipt by this endpoint, not invoice validation, reconciliation, payment authorization, settlement, or bank receipt. This page gives no retention, processing, replacement, retry/idempotency, or asynchronous outcome rule.

## Detail locators

- Endpoint purpose and test/live server URLs: raw lines 5–15.
- Required request properties and example: raw lines 17–35.
- Success contract and example: raw lines 36–47 and 144–156.
- Error schemas and examples: raw lines 50–142 and 158–224.

## Related

- [[adyen-account-structure]] — merchant-account context and separate invoice/account guidance.

## Raw Sources

- [[raw/adyen/api-explorer/Document-Collector/latest/post/crossBorderInvoices/2026-09-15|Captured Document Collector upload reference]]
