---
title: "Adyen Checkout API POST /forward (captured v72)"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/forward"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/forward/2026-09-15.md"
tags: [adyen, checkout-api, tokenization, forwarding]
---

## Overview

This captured [[adyen]] Checkout API Explorer reference describes `POST /forward`, which sends stored card details or network tokens to a merchant-specified third-party API and returns the response received from that third party. The listed server is `https://checkout-test.adyen.com/v72`; the `latest` URL does not establish a newer or current version. See [[adyen-tokenization]] and the broader [[source-adyen-docs-online-payments-tokenization-forward-payment-details|forwarding guide]] for setup and eligibility.

## Key takeaways

- The request table marks `baseUrl`, `merchantAccount`, `request`, and `shopperReference` required. The nested `request.body` and `request.httpMethod` are marked required; the body uses placeholders that Adyen replaces with payment details before calling the third party. The `shopperReference` description requires at least three characters, is case-sensitive, and excludes personally identifiable information.
- `storedPaymentMethodId` is optional in this request schema; the page also exposes optional `paymentMethod` card details and `options.tokenize`. Network-token options and conditional placeholders have their own descriptions in the raw table. Do not infer that the optional token ID is required for every forwarding mode. Collection of a raw card number is qualified by full PCI compliance.
- `options.dryRun` is test-only and returns a masked copy of Adyen's third-party request. The page's card-forwarding JSON is an example, not a universal required-property list.
- `200 Success` states that the forward request succeeded and includes a `response` object for what Adyen received from the third party, including optional body, headers, and HTTP status. The example third-party body has a `success` value, but neither that example nor Adyen's `200` establishes a third-party payment authorization or settlement. No failure-response table appears in this capture.

## Detail locators

- Purpose, test server, idempotency header: raw lines 5–17.
- Request body, forwarding options, network token and placeholder conditions: raw lines 20–56; card example: lines 58–77.
- `200` response fields and third-party example: raw lines 78–111.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/forward/2026-09-15|Checkout API Explorer POST /forward capture]]
