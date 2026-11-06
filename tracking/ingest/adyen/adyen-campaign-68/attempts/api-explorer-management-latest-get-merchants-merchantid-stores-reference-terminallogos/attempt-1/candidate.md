---
title: "Get a store-level terminal logo by model (Adyen Management API)"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/stores/(reference)/terminalLogos"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/stores/(reference)/terminalLogos/2026-11-07.md"
tags: [adyen, management-api, point-of-sale, terminal-logo, store]
---

## Overview

This captured Management API `latest` reference documents `GET /merchants/{merchantId}/stores/{reference}/terminalLogos`: read the logo configured for one payment-terminal model at the store identified by the merchant-account ID and store reference. The listed Test server is `https://management-test.adyen.com/v3`; Live requests are subject to rate limits. The API credential needs either Terminal settings read or Terminal settings read and write.

## Key takeaways

- `merchantId` and store `reference` are required path parameters; `model` is a required query parameter selected from the raw's enumerated terminal models. There is no request body or documented default.
- The store-level logo applies to terminals of that model under the store unless an individual terminal has a different logo. On `200`, the response schema lists optional `data`, a Base64-encoded image string that must be decoded to obtain the image file. The reference also documents `204` success without content. A readback does not establish that any particular terminal has displayed the logo.
- This is a configuration read, not a logo update, terminal readiness check, payment action, or proof of present Live account eligibility.

## Detail locators

- Raw lines 5–17: operation purpose, inheritance exception, credential roles, Live rate-limit notice.
- Raw lines 19–44: Test server, required path and query parameters, full model enumeration, `200` response schema.
- Raw lines 47–148: `204` no-content response and documented `400`, `401`, `403`, `422`, `500` error bodies.
- Raw lines 150–158: illustrative `200` response example.

## Related

- [[adyen]]
- [[adyen-terminal-management]]
- [[adyen-pos-store-management]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/stores/(reference)/terminalLogos/2026-11-07|GET store-level terminal logo by model, 2026-11-07 capture]]
