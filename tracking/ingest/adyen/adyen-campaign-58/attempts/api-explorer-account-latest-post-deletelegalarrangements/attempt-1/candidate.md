---
title: "Adyen Account API v6: delete legal arrangements"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Account/latest/post/deleteLegalArrangements"
raw_files:
  - "adyen/api-explorer/Account/latest/post/deleteLegalArrangements/2026-09-15.md"
tags: [adyen, classic-platforms, account-api, legal-arrangements]
---

## Overview

Captured API Explorer reference for Classic Platforms Account API v6 `POST /deleteLegalArrangements` on the TEST server. It deletes legal arrangements associated with an account holder, or only specified entities within an arrangement. This is an account-holder/legal-arrangement operation, not a payout or balance-account deletion. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The request body marks `accountHolderCode` and `legalArrangements` as required; each listed object marks `legalArrangementCode` required. Optional `legalArrangementEntityCodes` limits deletion to the listed entities; without it, the described action deletes the legal arrangement. See raw lines 14–20 and the arrangement/entity request examples at lines 22–49.
- Deletion is consequential: distinguish removing an entire legal arrangement from removing only listed legal arrangement entities. The captured page does not state verification reset, approval, propagation time, restoration, or idempotency behavior.
- A 200 response says the request succeeded; 202 says accepted for processing and explicitly not completed. The response schema lists optional `invalidFields`, `pspReference`, and `resultCode`, with `pspReference` identifying the request. Do not read a 202 or the sample reference as proof of completed deletion. See raw lines 50–83 and 150–168.
- The page lists 400 request-reading, 401 authentication, 403 insufficient-permission, 422 validation, and 500 server errors. Its 400 examples include invalid arrangement and entity codes; these examples illustrate validation, not an exhaustive error contract. See raw lines 86–149 and 170–226.

## Detail locators

- TEST server and v6 path: raw lines 5–10.
- Required request properties and conditional deletion scope: raw lines 14–20.
- Arrangement and entity request shapes: raw lines 22–49.
- Response schemas and HTTP meanings: raw lines 50–149.
- Success and error examples: raw lines 150–226.

## Related

- [[adyen-classic-platforms]] — Classic Platforms context and other captured Account API references.

## Raw Sources

- [[raw/adyen/api-explorer/Account/latest/post/deleteLegalArrangements/2026-09-15|Account API v6 deleteLegalArrangements captured 2026-09-15]]
