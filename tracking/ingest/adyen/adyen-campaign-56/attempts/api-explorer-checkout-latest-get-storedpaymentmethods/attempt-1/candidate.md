---
title: "Adyen Checkout API GET /storedPaymentMethods — stored-token listing"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/get/storedPaymentMethods"
raw_files:
  - "adyen/api-explorer/Checkout/latest/get/storedPaymentMethods/2026-09-15.md"
tags: [adyen, checkout-api, tokenization, stored-payment-methods]
---

## Overview

This 2026-09-15 API Explorer snapshot documents Checkout API `GET /storedPaymentMethods`: it lists any available tokens for a shopper's stored payment details, with summaries; a returned token ID can be used in later payment requests for that shopper. It is a token lookup, rather than a token-creation, deletion, or payment-outcome operation. The captured server is `https://checkout-test.adyen.com/v72` even though the canonical route contains `latest`. See [[adyen-tokenization]] and [[adyen]].

## Key takeaways

- The query-parameter table marks both `merchantAccount` and `shopperReference` as **No** under Required. It defines `shopperReference` as the merchant's shopper-unique reference, minimum three characters, without personally identifiable information such as a name or email. The opening prose instead says the shopper is identified **in the path**; the displayed endpoint is `GET /storedPaymentMethods` and the parameter section shows only query parameters. This snapshot does not resolve that placement discrepancy or justify treating table optionality as a complete operational request recipe.
- The documented `200 Success` means the request succeeded. Its response body has optional `merchantAccount`, `shopperReference`, and `storedPaymentMethods` fields. Each stored-method object may expose `id`, `type`, display/card/bank summary, `supportedRecurringProcessingModels`, and optional mandate details; the nested Yes markers apply within an included billing-address or mandate object, not to the whole response or request.
- `supportedRecurringProcessingModels` is described with `Subscription`, `CardOnFile`, and `UnscheduledCardOnFile`; the example includes all three for one card. The example does not guarantee that every returned method supports every model. No error response, authentication prerequisite, live server, token-creation result, or payment authorization/capture outcome is documented on this captured page.

## Detail locators

- Endpoint purpose and captured v72 test server: raw lines 5–10.
- Request query parameters and path/query discrepancy: raw lines 5–7 and 12–18.
- `200 Success`, response top-level fields, token `id`, card/bank summaries and nested address/mandate schema: raw lines 20–80.
- Processing-model descriptions and illustrative response example: raw lines 79 and 82–112.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-tokenization]]
- Related guide: [[source-adyen-docs-online-payments-tokenization-managing-tokens]]

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/get/storedPaymentMethods/2026-09-15|Checkout API GET /storedPaymentMethods (2026-09-15)]]
