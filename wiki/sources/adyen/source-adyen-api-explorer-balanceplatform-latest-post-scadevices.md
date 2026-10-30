---
title: "Adyen Balance Platform API v2: begin SCA device registration"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/scaDevices"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/scaDevices/2026-09-15.md"
tags: [adyen, balance-platform, sca, api-reference]
---

## Overview

Captured Balance Platform API reference for `POST /scaDevices`, beginning registration of a new Strong Customer Authentication device on the listed test `bcl/v2` server. The `201` response creates a device resource and completes only the initial registration step: the device is **not ready for use**. This endpoint is an SCA device lifecycle operation, separate from device association, user authentication, account verification, and payments. See [[adyen]], [[adyen-platforms]], [[adyen-business-accounts]], and [[adyen-issuing]].

## Key takeaways

- The request-property table marks `name` and `sdkOutput` required. `sdkOutput` is a base64-encoded block obtained using Adyen's authentication SDK (raw lines 14–18). The page does not separately state request-body requiredness or describe how the SDK produces that output.
- On `201`, `scaDevice` and `sdkInput` are response fields marked optional. When present, `scaDevice` contains an ID, name, and `ios`, `android`, or `browser` type; `sdkInput` is to be passed to the authentication SDK to continue registration (lines 29–41). The example shows both, but does not make them guaranteed in every response. The follow-up SDK exchange and final registration contract are outside this page.
- Documented errors are `400` invalid input, `401` authentication required, `403` insufficient permissions, `422` request validation, and `500` server processing failure (lines 44–136). The page gives no specific permission role, live endpoint, completion timing, propagation guarantee, or idempotency rule.

## Detail locators

- Request example: raw lines 20–28. Response schema and example: lines 29–41 and 138–152. Error payload field tables: lines 44–136.

## Related

- [[adyen-platforms]] — balance-platform context.
- [[adyen-business-accounts]] — related SCA device registration guidance.
- [[adyen-issuing]] — related issuer SCA device guidance.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/scaDevices/2026-09-15|POST /scaDevices API reference, captured 2026-09-15]]
