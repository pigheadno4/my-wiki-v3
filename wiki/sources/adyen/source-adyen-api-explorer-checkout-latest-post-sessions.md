---
title: "Adyen Checkout API POST /sessions (captured v72)"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/sessions"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/sessions/2026-09-14.md"
tags: [adyen, checkout, sessions, api-explorer]
---

## Overview

This 2026-09-14 API Explorer snapshot documents Checkout API `POST /sessions` against the displayed test server `https://checkout-test.adyen.com/v72`. It creates a payment session for Drop-in, Components or Hosted Checkout. The response carries a session identifier and encrypted session data for the front end, or a Hosted Checkout URL where applicable. The payment outcome arrives asynchronously through an `AUTHORISATION` webhook. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The request table marks `amount` (with `currency` and minor-unit `value`), `merchantAccount`, `reference`, and `returnUrl` required. The latter is the redirect return URL and has channel-specific formats; it must exclude personally identifiable information. The optional `Idempotency-Key` header is limited to 64 characters. The table lists no separate request-body requiredness declaration, so these are property-level marks.
- `mode` defaults to `embedded` for Drop-in or Components; `hosted` selects Hosted Checkout. The optional `channel` can filter platform-specific methods. `expiresAt` is optional in the request table: the default is one hour after creation, and the maximum is 24 hours after creation. The response table marks `expiresAt` required while repeating the request-side “when not specified” explanation; read those columns in their separate request/response contexts.
- Conditional inputs include `lineItems` for the listed buy-now-pay-later methods, `shopperName` for some methods or PayPal Seller Protection, `shopperIP` and phone data in specified 3DS cases, `store` for a platform-model Adyen for Platforms integration, and `recurringProcessingModel` when creating a payment-details token. Address and nested-object `Yes` marks apply when those optional parent objects are supplied; see the full request table for each condition.
- The response documents HTTP `201 Success` as creation of a resource. Its `id` identifies the session, `sessionData` is for the front end, and `url` is the Hosted Checkout redirect destination. Creation and the example payloads do not prove authorization, capture, settlement, merchant enablement, or live availability. The snapshot's `latest` URL does not establish today's latest API version.

## Detail locators

- Purpose, asynchronous outcome and displayed test `v72` server: raw lines 5–14.
- Header and request schema: lines 18–303; core amount lines 52–54, merchant/payment references 227 and 253, return URL 254; expiry 117, mode 230, and conditional fields 190, 250, 262–286.
- Request examples: lines 305–440. Response status/schema: lines 441–727; session `id` 608, `sessionData` 683, Hosted Checkout `url` 727; response examples 729–880.

## Related

- [[source-adyen-docs-online-payments-build-your-integration-sessions-flow]] — separate integration guide for client flow and webhook handling.
- [[adyen-online-payments]] — provider concept and source route.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/sessions/2026-09-14|Checkout API POST /sessions snapshot (2026-09-14)]]
