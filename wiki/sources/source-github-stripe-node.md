---
title: "GitHub — stripe/stripe-node (Official Stripe Node.js SDK)"
type: source
date_ingested: 2026-05-08
original_format: github-repo
raw_files:
  - "github-stripe-node.md"
tags: [stripe, node-js, sdk, typescript, payment-intents, checkout, webhooks, pagination, error-handling, idempotency]
---

## Summary

Official Stripe Node.js library (v22.1.1, OpenAPI spec v2252). Thin wrapper around the Stripe REST API with TypeScript support, automatic pagination, retry logic, and webhook verification.

## Key Patterns

### Initialization
```js
const stripe = new Stripe('sk_...', { apiVersion: '2024-06-20' });
```
Initialize once outside request handlers. Options: `maxNetworkRetries`, `timeout` (80s default), `httpClient`, `telemetry`.

### Error Handling
7 error classes: StripeCardError, StripeRateLimitError, StripeAuthenticationError, StripeIdempotencyError, StripeInvalidRequestError, StripeAPIError, StripeConnectionError. All extend `StripeError`.

### Webhooks
```js
const event = stripe.webhooks.constructEvent(rawBody, sig, webhookSecret);
```
Requires raw body (not JSON-parsed). 300s clock skew tolerance. Async variant available.

### Pagination
```js
for await (const pi of stripe.paymentIntents.list().autoPagingEach()) { ... }
```
V1Iterator handles `has_more` + `starting_after` automatically. `autoPagingToArray({ limit })` collects all.

### Retry Logic
Exponential backoff with jitter via `maxNetworkRetries`. Auto-sets idempotency keys on retry.

## Saved Files

| File | Lines | What's there |
| --- | --- | --- |
| `README.md` | 706 | Install, usage, config, TypeScript |
| `src/stripe.core.ts` | 2,562 | Main client, resource factory |
| `src/Error.ts` | 332 | Error taxonomy (7 classes) |
| `src/Webhooks.ts` | 557 | constructEvent, async variant, clock skew |
| `src/autoPagination.ts` | 498 | autoPagingEach, autoPagingToArray |
| `src/StripeResource.ts` | 168 | Base resource class |
| `src/RequestSender.ts` | 781 | HTTP, retry, idempotency, telemetry |
| `src/ResourceNamespace.ts` | 40 | Nested namespace pattern |
| `src/Types.ts` | 211 | RawErrorType, MethodSpec, BaseAddress |
| `src/shared.ts` | 182 | Metadata, Address, pagination types |
| `src/resources/PaymentIntents.ts` | 14,995 | Full PI API: create/confirm/capture/cancel/search |
| `src/resources/Checkout/Sessions.ts` | 7,618 | Full Checkout Session API |
| `examples/webhook-signing/README.md` | 69 | Express/Koa/Next.js/NestJS webhook guide |
| `examples/webhook-signing/express/main.ts` | ~90 | Express webhook handler example |

## Related Pages

- [[stripe-node-sdk]] — concept page
- [[stripe-payment-intents]] — Payment Intents concept
- [[stripe-3d-secure]] — 3DS (webhooks used for fulfillment)
- [[stripe]] — Stripe company page

## Raw Sources

- [[github-stripe-node]] — stub file pointing to `raw/github-stripe-node/` detail directory
