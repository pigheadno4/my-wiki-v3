---
title: "Adyen Disputes API v30 POST /deleteDisputeDefenseDocument"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Disputes/latest/post/deleteDisputeDefenseDocument"
raw_files:
  - "adyen/api-explorer/Disputes/latest/post/deleteDisputeDefenseDocument/2026-09-15.md"
tags: [adyen, disputes, api, defense, document-deletion]
---

## Overview

This 2026-09-15 [[adyen]] Disputes API Explorer capture documents `POST /deleteDisputeDefenseDocument` on the listed TEST `DisputeService/v30` server. It deletes one previously supplied dispute defense document identified by document type and dispute PSP reference. The `latest` route does not establish a newer captured version or LIVE availability. This is a document-level operation within [[adyen-risk-management]], not acceptance or resolution of the dispute.

## Key takeaways

- The request table marks `defenseDocumentType`, `disputePspReference`, and `merchantAccountCode` required properties. It does not separately state whole-body requiredness. The PSP reference is assigned to the dispute, rather than being the original payment reference. The example uses `DefenseMaterial` as a document-type value, but the page does not present a full type enum.
- This is a deletion request for a document supplied earlier. HTTP 200 says the API request succeeded, while the required `disputeServiceResult.success` boolean reports whether the service request succeeded; `errorMessage` is optional. The example shows `success: true`. The page does not specify restoration, propagation delay, dispute-defense submission, issuer acceptance or a won outcome. Treat deletion as consequential and check the actual response before relying on success.
- Separate 400, 401, 403, 422 and 500 tables describe request, authentication, permission, validation and server errors with optional error fields. The captured page supplies no error response examples and no retry or asynchronous outcome contract.

## Detail locators

- Raw lines 5–19: purpose, TEST DisputeService/v30 server and required request properties. Lines 21–30: request example.
- Raw lines 31–41: 200 response contract. Lines 44–106: API error tables. Lines 108–119: 200 success example.

## Related

- [[adyen]]
- [[adyen-risk-management]]
- [[disputes]]

## Raw Sources

- [[raw/adyen/api-explorer/Disputes/latest/post/deleteDisputeDefenseDocument/2026-09-15|Adyen Disputes API Explorer POST /deleteDisputeDefenseDocument (captured 2026-09-15)]]
