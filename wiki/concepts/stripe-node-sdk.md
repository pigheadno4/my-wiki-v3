---
title: "Stripe Node.js SDK (stripe-node)"
type: concept
category: technology
tags: [stripe, node-js, sdk, payment-intents, webhooks, pagination, error-handling, typescript, idempotency]
---

## Definition

The official Stripe Node.js library (`stripe` npm package) wraps the Stripe REST API for server-side JavaScript. The latest retained release is `stripe@22.4.0` at SHA `57626dcdfb94164fc9f112dfaa3c57aec5130e4f`; it pins Stripe API `2026-07-29.dahlia` and records OpenAPI generation marker `v2349`. It supports Node.js 18+ and exports builds for Node, browser/worker, Bun, Deno, and workerd environments.

**Install**: `npm install stripe`

## SDK Initialization

```js
import Stripe from 'stripe';
const stripe = new Stripe('sk_...', { apiVersion: '2024-06-20' });
```

Key options: `apiVersion`, `maxNetworkRetries`, `timeout` (default 80,000ms), `telemetry`, `emitEventBodies`, `httpClient`, `stripeAccount`, and `stripeContext`.

> [!warning] Version-specific retry default
> In `stripe@22.4.0`, the README documents `maxNetworkRetries: 1`, but the retained constructor source passes `2` as the fallback to `validateInteger`. Treat the effective default as an evidence conflict and set `maxNetworkRetries` explicitly for deterministic behavior.

⚠️ Initialize outside request handlers — don't recreate per request.

## Resource Pattern

Resources are nested namespaces mirroring the API: `stripe.paymentIntents`, `stripe.checkout.sessions`, `stripe.issuing.cards`, `stripe.billing.invoicing`. Each resource inherits from `StripeResource` and delegates to `RequestSender`.

## Error Handling

The SDK maps API and transport failures to typed classes extending `StripeError`. Common classes include:

| Class | When |
| --- | --- |
| `StripeCardError` | Card declined |
| `StripeRateLimitError` | Too many requests |
| `StripeAuthenticationError` | Invalid API key |
| `StripeIdempotencyError` | Idempotency conflict |
| `StripeInvalidRequestError` | Bad parameters |
| `StripeAPIError` | Stripe server error |
| `StripeConnectionError` | Network failure |

The current namespace also exposes permission, signature-verification, OAuth, and V2 session/rate-limit error types. Do not assume the historical seven-class summary is exhaustive.

```js
try {
  await stripe.paymentIntents.create({ ... });
} catch (err) {
  if (err instanceof Stripe.errors.StripeCardError) { /* decline */ }
}
```

## Retry Logic

`RequestSender` implements exponential backoff with jitter. Set `maxNetworkRetries` on the client or per request. For V1, POST requests get an automatic idempotency key when retries are enabled; for V2, POST and DELETE requests get one. Retry decisions cover connection errors, HTTP 409, HTTP 5xx, and the `stripe-should-retry` response header.

## Webhook Verification

```js
const event = stripe.webhooks.constructEvent(rawBody, sig, secret);
// or async:
const event = await stripe.webhooks.constructEventAsync(rawBody, sig, secret);
```

Requires raw (unparsed) request body — Express needs `express.raw()` middleware. Default clock skew tolerance: 300 seconds.

V2 event notifications use `parseEventNotification()` or `parseEventNotificationAsync()`. These verify the signature and attach helpers for fetching the full event and related object; they are distinct from V1 webhook events handled by `constructEvent()`.

## Pagination

```js
// Iterate all items automatically
for await (const item of stripe.paymentIntents.list().autoPagingEach()) { ... }

// Collect all into array (careful with large datasets)
const all = await stripe.paymentIntents.list().autoPagingToArray({ limit: 10000 });
```

## Key PaymentIntent Methods

`create`, `retrieve`, `update`, `list`, `confirm`, `capture`, `cancel`, `incrementAuthorization`, `applyCustomerBalance`, `verifyMicrodeposits`, `search`

## Key Checkout Session Methods

`create`, `retrieve`, `update`, `list`, `expire`, `listLineItems`

## Versioning Boundary

Stripe Node types always follow the latest API shape retained by that SDK release. Minor releases can add response enum values or otherwise weaken TypeScript exhaustiveness without a runtime-breaking API change, so minor upgrades still require a TypeScript check. Major SDK updates correspond to backwards-incompatible Stripe API changes; validated older-version knowledge remains in the cumulative source history.

## Sources

- [[source-github-stripe-node]] — cumulative SDK repository evidence through `stripe@22.4.0`
- [[changelog-github-stripe-node]] — package-qualified retained release history
