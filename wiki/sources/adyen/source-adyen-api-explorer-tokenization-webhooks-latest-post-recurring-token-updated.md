---
title: "Adyen Tokenization webhook: recurring.token.updated"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Tokenization-webhooks/latest/post/recurring.token.updated"
raw_files:
  - "adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.updated/2026-09-15.md"
tags: [adyen, tokenization, webhooks, recurring-tokens]
---

## Overview

This 2026-09-15-captured `Tokenization-webhooks/latest` API Explorer page describes the incoming `recurring.token.updated` webhook Adyen sends when a stored payment-method token is updated. Updating stored details is one example trigger; the page also says card networks can update tokens. This is a token lifecycle event, not a network-token provisioning event or a payment result. [[adyen]] [[adyen-tokenization]]

## Key takeaways

- The request table marks `createdAt`, `data`, `environment`, `eventId` and outer `type` required. Inside required `data`, it marks `merchantAccount`, `operation`, `shopperReference`, `storedPaymentMethodId` and payment-method `type` required. The optional outer `version` is the version of this entity; the page does not identify an API release number.
- `data.storedPaymentMethodId` is the token ID, associated with `data.shopperReference`; `eventId` is the PSP reference of the event that triggered the webhook. Keep these distinct. `data.operation` is described as audit text, while the sample's `"updated"` value is illustrative rather than an enumerated contract. `environment` lists `test` and `live`.
- The response section says any `2xx` HTTP status accepts the webhook. Receiver acceptance does not establish a later payment, card-network update completion beyond the reported event, or delivery-order/retry/deduplication/signature behavior; this endpoint reference states none of those mechanics.

## Detail locators

- Trigger and possible card-network actor: pinned raw lines 5–7.
- Full required-field table and ID meanings: `## Parameters > ### Request body`, lines 12–24.
- Example event and its sample-only `operation` value: `## Request examples > ### recurring-token-updated`, lines 28–43.
- Receiver acceptance: `## Responses > ### 200 Success`, lines 44–52.

## Related

- [[adyen-tokenization]] — stored-method token lifecycle context.
- [[adyen-webhooks]] — general receiver context, not an event-specific delivery contract.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/Tokenization-webhooks/latest/post/recurring.token.updated/2026-09-15|recurring.token.updated reference captured 2026-09-15]]
