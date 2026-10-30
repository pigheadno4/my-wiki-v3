---
title: "Adyen Checkout API v72: POST /originKeys"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/originKeys"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/originKeys/2026-09-15.md"
tags: [adyen, checkout-api, origin-key, client-side-authentication]
---

## Overview

Captured Checkout API reference for `POST /originKeys`. It accepts origin domains and returns corresponding origin keys. Its server listing is `https://checkout-test.adyen.com/v72`; the `latest` URL does not establish a newer contract or live availability. See [[adyen]] and [[adyen-api-access]].

## Key takeaways

- The request table marks `originDomains` as a required array of strings. The basic example supplies three HTTPS origins. The optional `Idempotency-Key` header permits a unique identifier up to 64 characters. The page does not separately state whole-body requiredness or additional origin-format constraints.
- The 200 response schema lists an optional `originKeys` string-valued object mapping requested domains to keys. The example shows all three input domains represented, but it does not establish an unconditional one-to-one issuance guarantee.
- The page recommends switching Web Drop-in or Components integrations still using origin keys to client keys. Its stated benefits include one key for all origins, origin changes without new-key generation, and card-type detection from the entered number. This is migration guidance, not a claim that this endpoint is unavailable or that an existing integration has migrated. Consult the separate client-side authentication and migration guides for version and environment conditions.
- The documented error responses are 400 unreadable request, 401 authentication required, 403 insufficient permissions, 422 validation error, and 500 server processing failure. Their shared error fields are optional in the tables. Generic error examples mention merchant accounts, return URLs and payment details; these examples do not establish endpoint-specific requirements for origin-key creation.

## Detail locators

- Purpose, client-key recommendation and test v72 server: pinned raw lines 5–12. Header and request table: lines 14–25.
- Basic request example: lines 27–38. 200 response table: lines 39–47. Error schemas: lines 50–117. Response examples: lines 119–195.

## Related

- [[adyen-api-access]] — provider API credential and client-side authentication source route.
- [[source-adyen-docs-development-resources-client-side-authentication-migrate-from-origin-key-to-client-key]] — separate version-qualified migration guidance.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/originKeys/2026-09-15|Checkout API POST /originKeys captured 2026-09-15]]
