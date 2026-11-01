---
title: "Adyen Tokenization webhooks: recurring.token.created"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Tokenization-webhooks/latest/post/recurring.token.created"
raw_files:
  - "adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.created/2026-09-15.md"
tags: [adyen, tokenization, webhooks, stored-payment-methods]
---

## Overview

This 2026-09-15 API Explorer snapshot describes Adyen's incoming `recurring.token.created` webhook when a token is created. It documents an event payload and receiver acceptance, not a token-creation request or payment authorization. [[adyen]] [[adyen-tokenization]] [[adyen-webhooks]]

## Key takeaways

- The body requires `createdAt` (ISO 8601 extended event time), `data`, `environment` (`test` or `live`), `eventId`, and outer `type`. `eventId` is described as the PSP reference of the event that triggered the webhook; outer `type` identifies the webhook. The entity `version` field is optional (raw lines 14–24).
- Within required `data`, the table marks `merchantAccount`, `operation`, `shopperReference`, `storedPaymentMethodId`, and nested `type` required. `storedPaymentMethodId` is the token ID; `shopperReference` is the unique shopper reference associated with it; nested `type` is the payment-method type. `operation` is audit-purpose descriptive text, not a documented status enum (raw lines 15–20).
- The sample shows `operation: "created"`, `environment: "test"`, and outer `type: "recurring.token.created"`; these are example values, not a rule about all events or payment success (raw lines 28–43).
- The response section describes HTTP 200 success and says any `2xx` HTTP status accepts the webhook. Its `notificationResponse` response-body field is optional; no literal response-body value is required by this captured table (raw lines 44–52). Acceptance does not establish later token usability or a payment outcome. This page states no delivery order, retry, deduplication, signature, or token deletion/propagation rule.

## Detail locators

- Event purpose and required payload fields: raw lines 5–24.
- Full request example: raw lines 26–43.
- Receiver acknowledgment: raw lines 44–52.

## Related

- [[adyen-tokenization]] — stored-method token lifecycle and reciprocal source route.
- [[source-adyen-docs-online-payments-tokenization-managing-tokens]] — separate token management and lifecycle guidance.

## Raw Sources

- [[raw/adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.created/2026-09-15|Tokenization webhook recurring.token.created capture]]
