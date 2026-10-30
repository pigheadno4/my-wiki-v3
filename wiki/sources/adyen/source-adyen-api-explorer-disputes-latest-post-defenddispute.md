---
title: "Adyen Disputes API POST /defendDispute (captured v30)"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Disputes/latest/post/defendDispute"
raw_files:
  - "adyen/api-explorer/Disputes/latest/post/defendDispute/2026-09-15.md"
tags: [adyen, disputes, dispute-defense, api-explorer]
---

## Overview

This 2026-09-15 API Explorer snapshot documents Disputes API `POST /defendDispute` on the displayed test `https://ca-test.adyen.com/ca/services/DisputeService/v30` server. It submits a defense request for a **specific dispute**. The request identifies the dispute by its dispute PSP reference, with a selected defense reason and merchant account code. See [[adyen]] and [[adyen-risk-management]].

## Key takeaways

- The request property table marks `defenseReasonCode`, `disputePspReference`, and `merchantAccountCode` required. The example uses `SupplyDefenseMaterial` as a defense reason, but the page gives no complete enum, evidence-upload contract, eligibility rule, or deadline. Do not treat the example value as a universal defense option.
- HTTP 200 contains required `disputeServiceResult.success` indicating whether the **request** succeeded, plus optional `errorMessage`; the example has `success: true`. This is not a ruling that the defense was accepted or that the merchant won the dispute. Evidence material and later dispute outcomes require separate sources.
- The page lists 400 parsing, 401 authentication, 403 permissions, 422 validation and 500 server errors with generic response schemas. It has no error-response examples. Its captured `latest` path shows test Disputes API v30 only, not current version, live account eligibility or an actual dispute result.

## Detail locators

- Purpose and displayed test server: raw lines 5–10. Request fields and example: lines 14–30.
- 200 response and request-success meaning: lines 31–41; example: 108–119. Error schemas: lines 44–106.

## Related

- [[source-adyen-docs-risk-management-disputes-api]] — broader dispute-management guide.
- [[adyen-risk-management]] — provider concept and reciprocal route.

## Raw Sources

- [[raw/adyen/api-explorer/Disputes/latest/post/defendDispute/2026-09-15|Disputes API POST /defendDispute snapshot (2026-09-15)]]
