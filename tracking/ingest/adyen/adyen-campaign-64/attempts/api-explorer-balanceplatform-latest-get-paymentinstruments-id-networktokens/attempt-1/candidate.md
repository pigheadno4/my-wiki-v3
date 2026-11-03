---
title: "Adyen Balance Platform API v2: GET payment-instrument network tokens"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/networkTokens"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/networkTokens/2026-11-02.md"
tags: [adyen, balance-platform, issuing, network-tokens, api]
---

## Overview

This 2026-11-02 Balance Platform API reference lists network tokens connected to a payment instrument. The captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; `latest` is a documentation route, not proof of current live availability. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- The only listed input is a required string path `id`, the payment-instrument identifier. No query parameter or request body is shown. The 200 response schema marks `networkTokens` optional; all listed fields inside a returned token object are also optional. The page provides no success JSON example, count, pagination contract, or ordering guarantee.
- A returned token can identify its own `id`, linked `paymentInstrumentId`, brand variant, creation date, device, token requestor, token-last-four, type (examples `wallet`, `cof`), and status (`active`, `inactive`, `suspended`, `closed`). These are token fields, not the payment-instrument's own status or a transaction result.
- The nested device phone object is conditionally returned, available for up to 24 hours after the provisioning request, and requires a specific user role obtained through Adyen. Do not treat its absence as proof no device or phone exists. The page does not name the role or establish that a given caller has it.
- The documented errors are 400, 401, 403, 422 and 500. The generic 422 and 500 examples describe changing a balance-account ID and creating a payment instrument; those examples do not describe network-token listing failures. A successful read or `active` token status does not prove token provisioning approval, wallet activation, card authorization, capture, booking, settlement, or funds receipt. The page gives no GET idempotency key, token mutation/deletion rule, propagation timing, or reversal behavior.

## Detail locators

- Purpose, TEST server and required payment-instrument path ID: pinned raw lines 5–17.
- 200 response token fields, statuses and conditional phone: pinned raw lines 19–41.
- Error schemas: pinned raw lines 44–141; generic error examples: lines 143–209.

## Related

- [[adyen-issuing]] — issued-card and network-token context.
- [[source-adyen-docs-issuing-network-tokens]] — separate dated lifecycle/prerequisites guide.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/networkTokens/2026-11-02|Balance Platform GET network tokens snapshot]]