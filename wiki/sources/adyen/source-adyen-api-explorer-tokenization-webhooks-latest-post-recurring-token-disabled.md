---
title: "Adyen Tokenization webhook: recurring.token.disabled"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Tokenization-webhooks/latest/post/recurring.token.disabled"
raw_files:
  - "adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.disabled/2026-09-15.md"
tags: [adyen, tokenization, webhooks, stored-payment-methods]
---

## Overview

This 2026-09-15-captured Tokenization webhooks API Explorer reference describes an incoming `recurring.token.disabled` event that Adyen sends when a stored-payment-method token is disabled, including after deletion of stored payment details or a third party disabling the details. The related overview labels this webhook family v1; the pinned event page itself uses `latest` and has an optional entity `version` field. This is a token lifecycle notification, not a token-management API call or a network-token event. [[adyen-tokenization]] [[adyen]]

## Key takeaways

- The request schema marks `createdAt`, `data`, `environment`, `eventId`, and outer `type` required. Within `data`, it marks `merchantAccount`, `shopperReference`, `storedPaymentMethodId` (the token ID), and payment-method `type` required. `eventId` is described as the PSP reference of the triggering event, distinct from the stored payment method ID. `environment` can be `test` or `live`; `version` is optional. See [[raw/adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.disabled/2026-09-15|raw lines 11–23]].
- The example has outer `type: "recurring.token.disabled"`, a test environment, and illustrative IDs. It demonstrates payload shape but does not add a cause, disablement timestamp beyond `createdAt`, or a later payment outcome. See [[raw/adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.disabled/2026-09-15|raw lines 25–41]].
- The 200 response section says the recipient accepts the webhook with any 2xx HTTP status; optional `notificationResponse` is listed in the response body table. That receiver acceptance is separate from the token state reported by the event, and the page does not state a retry, ordering, deduplication, signature, propagation or payment-authorization rule. See [[raw/adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.disabled/2026-09-15|raw lines 42–50]].

## Detail locators

- Event purpose and two example causes: [[raw/adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.disabled/2026-09-15|raw lines 5–7]].
- Complete required/optional request-body fields: [[raw/adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.disabled/2026-09-15|raw lines 9–23]].
- Illustrative request payload: [[raw/adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.disabled/2026-09-15|raw lines 25–41]].
- Receiver response: [[raw/adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.disabled/2026-09-15|raw lines 42–50]].

## Related

- [[adyen-tokenization]] — stored-payment-method token lifecycle context.
- [[source-adyen-api-explorer-tokenization-webhooks-latest-overview]] — v1 family inventory.
- [[source-adyen-docs-online-payments-tokenization-managing-tokens]] — separately sourced token deletion and merchant-held detail cleanup guidance.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.disabled/2026-09-15|recurring.token.disabled API Explorer reference (captured 2026-09-15)]]
