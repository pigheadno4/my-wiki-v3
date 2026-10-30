---
title: "Adyen Disputes API POST /supplyDefenseDocument — upload dispute evidence"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Disputes/latest/post/supplyDefenseDocument"
raw_files:
  - "adyen/api-explorer/Disputes/latest/post/supplyDefenseDocument/2026-09-15.md"
tags: [adyen, disputes-api, defense-documents, chargebacks, evidence]
---

## Overview

This 2026-09-15 API Explorer snapshot documents Disputes Service `POST /supplyDefenseDocument`, supplying defense documents for a **specific dispute**. The captured server is **v30 test**, although the canonical route contains `latest`. The request identifies the dispute by `disputePspReference`, separate from the merchant account and any payment-reference field in generic error bodies. See [[adyen-risk-management]] and the broader Disputes API workflow guide.

## Key takeaways

- The schema marks `defenseDocuments`, `disputePspReference`, and `merchantAccountCode` required request-body properties. Each listed document object marks `content`, `contentType`, and `defenseDocumentTypeCode` required. The single example uses `application/pdf` and `DefenseMaterial`; it does not establish all permitted formats, type codes, size limits, or that this example fits every dispute's applicable defense reason.
- `200 Success` means the API request succeeded; the required `disputeServiceResult` object contains a required `success` boolean and optional `errorMessage`. The shown `success: true` is a supply-document request result. The related Adyen workflow guide says upload stores evidence for a later `/defendDispute` submission; it is not itself final defense submission, issuer acceptance, or a won dispute.
- The page lists `400` unreadable request, `401` authentication required, `403` insufficient permission, `422` validation error, and `500` server error schemas, but shows no examples of these failures. The generic error body has an optional payment `pspReference`; do not confuse that field with required `disputePspReference` that selects the dispute. This page alone does not define account role, case deadline, scheme-specific evidence requirements, or live availability.

## Detail locators

- Endpoint purpose and captured v30 test server: raw lines 5–10.
- Required dispute/merchant/document request fields: raw lines 14–22.
- Single illustrative PDF/DefenseMaterial request: raw lines 24–39.
- `200` request-level result and example: raw lines 40–50 and 117–128.
- HTTP error classes and generic body fields: raw lines 53–115.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-risk-management]]
- Disputes API workflow: [[source-adyen-docs-risk-management-disputes-api]]
- Applicable reason/type-code reference: [[source-adyen-docs-risk-management-disputes-api-disputes-api-reference]]

## Raw Sources

- [[raw/adyen/api-explorer/Disputes/latest/post/supplyDefenseDocument/2026-09-15|Disputes API POST /supplyDefenseDocument (2026-09-15)]]
