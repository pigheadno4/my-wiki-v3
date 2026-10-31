---
title: "Adyen Account API v6: POST /deleteSignatories"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Account/latest/post/deleteSignatories"
raw_files:
  - "adyen/api-explorer/Account/latest/post/deleteSignatories/2026-09-15.md"
tags: [adyen, classic-platforms, account-api, account-holder, signatories]
---

## Overview

This 2026-09-15-captured API Explorer reference documents `POST /deleteSignatories`, a destructive operation that deletes signatories associated with a Classic Platforms account holder. The page lists the **test** Account API `/cal/services/Account/v6` server, despite `latest` in the canonical route. It selects a Classic `accountHolderCode` and signatory codes, not newer balance-platform identities. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The request-body table marks both `accountHolderCode` (string) and `signatoryCodes` (array of strings) as required properties. The former identifies the account holder **from which** to delete signatories; the latter identifies the signatories to delete. The page gives no request example or further cardinality/uniqueness condition for the array (raw lines 12–19).
- The page labels 200 as succeeded and 202 as accepted for processing while processing is incomplete. Both response schemas list optional `invalidFields`, `pspReference`, and `resultCode`; `invalidFields` represents field validation errors that would prevent processing. In particular, a 202 or request reference does not establish that deletion has completed or that any downstream verification state has changed (raw lines 20–53).
- Listed error categories are 400 request reading/understanding, 401 authentication, 403 insufficient permissions, 422 request validation, and 500 server processing. The page names no specific credential role. Error body properties are optional in its tables; the 400 and 403 JSON bodies are illustrative examples (raw lines 56–144).

## Detail locators

- Purpose and test v6 server: raw lines 5–10. Required request properties and deletion selectors: lines 12–19.
- Success/accepted response descriptions and fields: raw lines 20–53. Error descriptions and schemas: lines 56–118. Example error bodies: lines 120–144.

## Related

- [[adyen-classic-platforms]] — Classic Platforms account-holder model and separation from newer balance-platform resources.

## Raw Sources

- [[raw/adyen/api-explorer/Account/latest/post/deleteSignatories/2026-09-15|Account API deleteSignatories reference, captured 2026-09-15]]
