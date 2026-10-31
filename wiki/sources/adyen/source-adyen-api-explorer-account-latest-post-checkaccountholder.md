---
title: "Adyen Account API v6: POST /checkAccountHolder"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Account/latest/post/checkAccountHolder"
raw_files:
  - "adyen/api-explorer/Account/latest/post/checkAccountHolder/2026-09-15.md"
tags: [adyen, classic-platforms, account-api, account-holder, verification]
---

## Overview

This 2026-09-15-captured API Explorer reference documents `POST /checkAccountHolder` for triggering verification of a Classic Platforms account holder before the checks are otherwise required by current processing volume. The page's listed server is the **test** Account API `/cal/services/Account/v6`, although the canonical route contains `latest`. The subject is a Classic `accountHolderCode`, not a newer balance-platform account-holder ID. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The request-body table marks `accountHolderCode` (string), `accountStateType` (string), and `tier` (integer) as required properties. `accountStateType` permits `Processing` or `Payout`; the page calls `tier` the required tier. The basic example gives `tier` as the JSON string `"2"` despite the table's integer type; use the table for the declared type and treat the example as illustrative (raw lines 14–30).
- The page labels both 200 and 202 as success responses, but expressly says 202 is accepted for processing and processing is not complete. Their listed optional fields are `invalidFields`, `pspReference`, and `resultCode`; `invalidFields` contains field validation errors that would prevent processing. Neither status alone establishes completed verification, account-holder approval, payout eligibility or money movement (raw lines 31–64).
- The listed errors are 400 request reading/understanding, 401 authentication, 403 insufficient permissions, 422 request validation, and 500 server processing. The page does not name a specific credential role. Error-body properties are optional in its tables, and the 400/403 JSON bodies are examples rather than a complete error catalog (raw lines 67–155).

## Detail locators

- Endpoint purpose and listed test v6 server: raw lines 5–10. Request properties, allowed state values, and example: lines 12–30.
- 200 and 202 descriptions and response field schemas: raw lines 31–64. Error descriptions and schemas: lines 67–129. Example 400/403 bodies: lines 131–155.

## Related

- [[source-adyen-docs-classic-platforms-onboard-users]] — Classic onboarding guide for the different `Payout` and `Processing` precheck consequences and notification-based verification outcomes.
- [[adyen-classic-platforms]] — Classic Platforms context and separation from the newer balance-platform model.

## Raw Sources

- [[raw/adyen/api-explorer/Account/latest/post/checkAccountHolder/2026-09-15|Account API checkAccountHolder reference, captured 2026-09-15]]
