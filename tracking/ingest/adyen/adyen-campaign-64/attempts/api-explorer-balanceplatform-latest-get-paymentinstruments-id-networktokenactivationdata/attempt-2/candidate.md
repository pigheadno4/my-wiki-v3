---
title: "Adyen Balance Platform API v2: Get network token activation data"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/networkTokenActivationData"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/networkTokenActivationData/2026-11-02.md"
tags: [adyen, platforms, balance-platform, issuing, network-token, api-reference]
---

## Overview

Captured Balance Platform API v2 TEST `GET /paymentInstruments/{id}/networkTokenActivationData` reference. It retrieves network-token activation data for the payment instrument identified by required path `id`. The returned data can initialize Adyen's network-token provisioning SDKs; this [[adyen]] [[adyen-issuing]] endpoint does not itself activate a token or confirm wallet provisioning.

## Key takeaways

- The listed server is `https://balanceplatform-api-test.adyen.com/bcl/v2`. The reference lists one required path parameter, payment-instrument `id`, and no request body or query parameters.
- A 200 means the GET request succeeded. Its only listed response field is string `sdkInput`, marked **optional** in the schema, while its description says that `sdkInput` is required to initialize Adyen's SDK for network-token provisioning. The former is response-field requiredness; the latter is a downstream SDK-use requirement. Neither guarantees the field is present in every 200 response.
- The raw points to Apple Pay and Google Wallet provisioning SDK repositories for further implementation information. Those linked repositories were not part of this pinned source, so this entry does not infer their supported platforms, API contracts or current versions.
- Error classes are 400, 401, 403, 422 and 500. The generic 422 and 500 examples mention payment-instrument balance-account changes and creation, not network-token activation; they do not establish endpoint-specific failure or activation behavior. No 200 response example is included.

## Detail locators

- Purpose, TEST server and required path ID: pinned raw lines 5–17. Success status and `sdkInput` schema/prose: lines 19–27. Error schemas: lines 30–127; generic examples: lines 129–195.

## Related

- [[adyen-issuing]] — issuer provisioning and payment-instrument context.
- [[adyen-platforms]] — Balance Platform API family context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/networkTokenActivationData/2026-11-02|Pinned 2026-11-02 API reference]]
