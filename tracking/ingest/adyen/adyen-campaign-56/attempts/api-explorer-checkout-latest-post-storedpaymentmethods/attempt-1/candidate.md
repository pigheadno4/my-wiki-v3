---
title: "Adyen Checkout API POST /storedPaymentMethods (captured v72)"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/storedPaymentMethods"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/storedPaymentMethods/2026-09-15.md"
tags: [adyen, checkout-api, tokenization, stored-payment-methods]
---

## Overview

This captured [[adyen]] Checkout API Explorer reference describes `POST /storedPaymentMethods`: creating a shopper-linked token for stored payment details that can be used for future payments. Its listed server is `https://checkout-test.adyen.com/v72`; the `latest` URL is not evidence of a newer or current version. This is a token-creation contract, not a payment authorization or future-payment result. See [[adyen-tokenization]].

## Key takeaways

- The request schema marks `merchantAccount`, `paymentMethod`, `recurringProcessingModel`, and `shopperReference` required. The model distinguishes `Subscription`, `CardOnFile`, and `UnscheduledCardOnFile`; see the source's request-body table for their definitions. The card fields nested under `paymentMethod` are individually shown as optional in this capture, while its `type` description says to set `scheme`.
- Raw `cvc`, `expiryMonth`, `expiryYear`, and `number` fields each carry the fully PCI-compliant collection qualification. The encrypted and unencrypted card examples are examples, not an expanded required-property list.
- `201 Success` says a resource was created. The response schema's optional `id` is the stored payment method identifier; its examples show that ID with masked card details and `shopperReference`. This response alone does not establish a payment authorization, settlement, or later successful token charge.
- This endpoint capture does not state shopper-consent or account-eligibility rules. Consult the broader [[adyen-tokenization]] guides for those separate conditions before treating a stored-token flow as complete.

## Detail locators

- Server and idempotency header: raw lines 9–17.
- Request properties, recurring models, PCI qualification, and request examples: raw lines 20–80.
- `201` response and optional stored-method fields, including `id`, mandate details, and supported models: raw lines 81–138; response examples: lines 140–168.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/storedPaymentMethods/2026-09-15|Checkout API Explorer POST /storedPaymentMethods capture]]
