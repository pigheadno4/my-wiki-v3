---
title: "Adyen Disputes API v30: POST /retrieveApplicableDefenseReasons"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Disputes/latest/post/retrieveApplicableDefenseReasons"
raw_files:
  - "adyen/api-explorer/Disputes/latest/post/retrieveApplicableDefenseReasons/2026-09-15.md"
tags: [adyen, disputes, defense-reasons, api-reference]
---

## Overview

This captured [[adyen]] Disputes API reference describes `POST /retrieveApplicableDefenseReasons`, which returns applicable defense reasons for a **specific dispute**. The captured server is `https://ca-test.adyen.com/ca/services/DisputeService/v30`; the `latest` URL does not establish current latest version or live availability. This is a lookup, not a defense submission, document upload, dispute acceptance or win.

## Key takeaways

- The request table requires `disputePspReference`, the PSP reference assigned to the **dispute**, and `merchantAccountCode`, the merchant account for the dispute transaction. The dispute reference should not be substituted with a payment PSP reference or a document identifier.
- HTTP 200 says the request succeeded. The response body requires `disputeServiceResult` with a required `success` boolean; an optional `errorMessage` may accompany that result. `defenseReasons` is optional and, when present, contains reason codes plus optional document-type arrays.
- For each document type in a returned reason, `available` reports whether that type has been uploaded. `requirementLevel` distinguishes `Required`, `OneOrMore`, `Optional` and `AlternativeRequired`; the latter is a generic-document route that needs Adyen Support enablement. A reason's `satisfied` reports whether sufficient defense material has been supplied. Neither `available`, `satisfied`, nor `disputeServiceResult.success` means a defense was submitted or accepted by the scheme, or that the dispute was won.
- The 200 example shows selected reasons with `satisfied: false` and one `disputeServiceResult.success: true`; it is illustrative rather than a universal reason list or outcome. The reference lists 400, 401, 403, 422 and 500 error categories and generic response fields, without error examples.

## Detail locators

- Purpose, v30 TEST server and required dispute/merchant identifiers: raw lines 5–18; request example: lines 20–28.
- 200 result and nested reason/document fields: raw lines 29–46; illustrative reason list: lines 113–190.
- Error categories and response shapes: raw lines 49–111.

## Related

- [[adyen-risk-management]] — provider-level disputes and risk route.
- [[source-adyen-docs-risk-management-disputes-api]] — defense workflow guidance.
- [[source-adyen-docs-risk-management-disputes-api-disputes-api-reference]] — broader scheme-specific reason and document codes.

## Raw Sources

- [[raw/adyen/api-explorer/Disputes/latest/post/retrieveApplicableDefenseReasons/2026-09-15|Disputes v30 retrieveApplicableDefenseReasons capture]]
