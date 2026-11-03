---
title: "Adyen Balance Platform API v2: Get a network token"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/networkTokens/(networkTokenId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/networkTokens/(networkTokenId)/2026-11-03.md"
tags: [adyen, balance-platform, issuing, network-tokens, api-reference]
---

## Overview

The 2026-11-03-captured Balance Platform API v2 TEST reference describes `GET /networkTokens/{networkTokenId}` for retrieving one network token's details. The required path value is the network token's unique ID, distinct from the returned `paymentInstrumentId` identifying the associated payment instrument. This is a readback of a token resource, not a provisioning, activation, status-change or card-payment operation. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- The captured server is `https://balanceplatform-api-test.adyen.com/bcl/v2`; no live server or specific credential role for this GET is stated. A `200` response requires the `token` object, while its listed child fields, including `id`, `paymentInstrumentId`, `status`, `type`, `tokenRequestor` and `device`, are response-optional. The listed status values are `active`, `inactive`, `suspended` and `closed`.
- `device.phone` is conditionally returned for up to 24 hours after the provisioning request and requires a specific user role that the reference does not name; the reader is directed to an Adyen representative for permission. Do not treat its absence as evidence that no device or phone exists.
- `401` denotes required authentication, `403` insufficient permission, `422` request validation failure and `500` a server processing failure. The generic `422` and `500` response examples refer to changing a payment instrument's balance account and creating a payment instrument, respectively; they do not establish mutations or these failure causes for this GET.
- The page describes no request body, query parameters, idempotency key, default, limit, asynchronous confirmation, or token lifecycle transition for this operation. A successful resource read does not prove token provisioning completion, usable card status, authorization, capture, settlement or current account eligibility.

## Detail locators

- Raw lines 5–17: purpose, TEST v2 server and required `networkTokenId` path parameter.
- Raw lines 19–41: `200` response schema; required parent versus optional children, timestamp, device, token identity, associated payment instrument, status, token requestor and type.
- Raw lines 44–121: `401`, `403`, `422` and `500` error schemas.
- Raw lines 123–176: generic response examples; the `422`/`500` descriptions are about payment-instrument operations rather than this GET.

## Related

- [[adyen-issuing]] — Issuing card and network-token context; this API reference controls its own GET contract.
- [[source-adyen-api-explorer-balanceplatform-latest-get-paymentinstruments-id-networktokens]] — separate list operation by payment-instrument ID.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/networkTokens/(networkTokenId)/2026-11-03|GET network token API reference (2026-11-03)]]