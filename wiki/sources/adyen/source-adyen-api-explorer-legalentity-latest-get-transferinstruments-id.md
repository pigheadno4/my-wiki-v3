---
title: "Adyen Legal Entity Management API v4: get a transfer instrument"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/get/transferInstruments/(id)"
raw_files:
  - "adyen/api-explorer/legalentity/latest/get/transferInstruments/(id)/2026-11-03.md"
tags: [adyen, legal-entity-management, transfer-instruments, verification, api]
---

## Overview

This 2026-11-03 Legal Entity Management API v4 reference documents `GET /transferInstruments/{id}` to read one transfer instrument. The captured server is TEST `https://kyc-test.adyen.com/lem/v4`; `latest` is a documentation route and does not establish live access or account eligibility. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The required string path `id` identifies the transfer instrument. No query parameters or request body are shown. The page lists rate limits of 700 requests per five seconds in live environments, 200 per five seconds in test, and five failed requests per ten seconds; it does not name a caller role, default, or idempotency key.
- A `200` response requires `bankAccount`, transfer-instrument `id`, owning `legalEntityId`, and `type` (`bankAccount`). Nested bank-account identification, account type, bank name, country code and `trustedSource` are optional; `trustedSource` identifies creation through instant bank verification, not a current capability decision. Optional `capabilities` can report supporting-entity `requested`, `allowed`, and `verificationStatus` (`pending`, `invalid`, `valid`, `rejected`). The field description says a supporting entity can be allowed even if its parent legal entity is not, because another supporting entity failed verification. Optional `problems` can contain verification errors and remediating actions. The IBAN response is an example, not a universal identification requirement.
- This GET reports resource details and any included verification state; a returned bank account, `trustedSource`, or `200` does not by itself prove a capability is allowed, a payout is eligible, a transfer was sent, booked, settled, or received by a bank. Verification can be pending, invalid or rejected. Documented errors are 400 request problem, 401 authentication required, 403 insufficient permissions, 422 validation error, and 500 server failure; generic error payloads may include `pspReference`, but this GET is not a payment result. The page does not specify propagation timing, deletion/reversal behavior, or version/conflict semantics for this read.

## Detail locators

- Purpose, rate limits, TEST server and required path ID: pinned raw lines 5–25.
- `200` response schema, optional bank and verification fields: pinned raw lines 27–72; illustrative response: lines 139–157.
- Error descriptions and payload fields: pinned raw lines 75–137.

## Related

- [[adyen-platforms]] — legal-entity and transfer-instrument context.
- [[source-adyen-api-explorer-legalentity-latest-post-transferinstruments]] — separate captured reference for creating the resource before verification.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/get/transferInstruments/(id)/2026-11-03|Legal Entity Management GET transfer instrument snapshot]]