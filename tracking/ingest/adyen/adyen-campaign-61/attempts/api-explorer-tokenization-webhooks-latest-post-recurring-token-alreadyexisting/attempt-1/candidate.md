---
title: "Adyen recurring.token.alreadyExisting tokenization webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Tokenization-webhooks/latest/post/recurring.token.alreadyExisting"
raw_files:
  - "adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.alreadyExisting/2026-09-15.md"
tags: [adyen, tokenization, webhooks, stored-payment-methods]
---

## Overview

Captured Tokenization webhooks reference for incoming `POST recurring.token.alreadyExisting`. Adyen sends this event when an attempted token creation or update uses details that match an already existing token. It identifies the token involved; it does not describe a newly created token or a payment result. [[adyen]] [[adyen-tokenization]]

## Key takeaways

- The required request envelope includes `createdAt`, `data`, `environment`, `eventId` and `type`; `version` is optional. `environment` is described as `test` or `live`, and `eventId` is the PSP reference of the event that triggered the webhook. See raw lines 11–24.
- Within required `data`, the table marks `merchantAccount`, `operation`, `shopperReference`, `storedPaymentMethodId` and payment-method `type` required. `storedPaymentMethodId` is the token ID, while `operation` is audit-oriented text. The example uses `alreadyExisting` for `operation`; it does not define an operation enum. See raw lines 15–20 and 26–43.
- The response section shows `200 Success`, and its optional `notificationResponse` row says any `2xx` HTTP status code accepts the webhook. Receiver acceptance is distinct from the attempted token operation or any later payment. See raw lines 44–52.

## Detail locators

- Event trigger and incoming POST identity: raw lines 5–7.
- Request envelope and nested data fields: raw lines 11–24.
- Illustrative test-environment request body: raw lines 26–43.
- Receiver response and acceptance rule: raw lines 44–52.

## Related

- [[adyen-tokenization]] — stored-payment-method lifecycle context.
- [[adyen-webhooks]] — general webhook receiver context.

## Raw Sources

- [[raw/adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.alreadyExisting/2026-09-15|recurring.token.alreadyExisting reference captured 2026-09-15]]
