---
title: "Adyen Account API v6: POST /closeStores"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Account/latest/post/closeStores"
raw_files:
  - "adyen/api-explorer/Account/latest/post/closeStores/2026-09-15.md"
tags: [adyen, classic-platforms, account-api, stores]
---

## Overview

This captured Adyen Account API page describes `POST /closeStores`, which closes stores associated with an account holder. Its listed server is the Account v6 TEST endpoint, `https://cal-test.adyen.com/cal/services/Account/v6`. The request body requires `accountHolderCode` (the account holder's code) and `stores` (an array of store strings). It does not identify these values as newer balance-platform account-holder or legal-entity IDs.

## Key takeaways

- The documented 200 response says the request has succeeded. Its optional response fields are `invalidFields`, `pspReference` (a request reference), and `resultCode`. The captured page does not specify result-code values, store-state propagation timing, reversal, idempotency, or a later confirmation workflow; do not infer those from a 200 response.
- The page lists 400 for an unreadable/invalid request, 401 for required authentication, 403 for insufficient permissions, 422 for request validation, and 500 when the server cannot process the request. These are documented response classes, not proof that a specific account holder or store is eligible for closure.
- This is a 2026-09-15 capture of a TEST API reference. It does not establish current availability, a live operation, or any payment or payout outcome.

## Detail locators

- Request purpose, server, and required body fields: pinned raw lines 5–18.
- 200 response and optional fields, including validation-error structure: pinned raw lines 20–36.
- Error responses and their optional fields: pinned raw lines 39–101.
- Illustrative 400 and 403 JSON examples: pinned raw lines 103–127.

## Related

- [[adyen-classic-platforms]] — Classic platform account-holder context and its separate API model.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/Account/latest/post/closeStores/2026-09-15|Account API v6 POST /closeStores capture (2026-09-15)]]
