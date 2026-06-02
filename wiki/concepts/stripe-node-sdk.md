---
title: "Stripe Node.js SDK (stripe-node)"
type: concept
category: technology
tags: [stripe, node-js, sdk, payment-intents, webhooks, pagination, error-handling, typescript, idempotency]
---

## Definition

The official Stripe Node.js library (`stripe` npm package) wraps the Stripe REST API. Version 22.1.1 targets the OpenAPI spec v2252. Supports Node.js and edge runtimes (Cloudflare Workers, Deno).

**Install**: `npm install stripe`

## SDK Initialization

```js
import Stripe from 'stripe';
const stripe = new Stripe('sk_...', { apiVersion: '2024-06-20' });
```

Key options: `apiVersion`, `maxNetworkRetries` (default 0), `timeout` (default 80,000ms), `telemetry`, `httpClient`.

⚠️ Initialize outside request handlers — don't recreate per request.

## Resource Pattern

Resources are nested namespaces mirroring the API: `stripe.paymentIntents`, `stripe.checkout.sessions`, `stripe.issuing.cards`, `stripe.billing.invoicing`. Each resource inherits from `StripeResource` and delegates to `RequestSender`.

## Error Handling

Seven error classes extend `StripeError`:

| Class | When |
| --- | --- |
| `StripeCardError` | Card declined |
| `StripeRateLimitError` | Too many requests |
| `StripeAuthenticationError` | Invalid API key |
| `StripeIdempotencyError` | Idempotency conflict |
| `StripeInvalidRequestError` | Bad parameters |
| `StripeAPIError` | Stripe server error |
| `StripeConnectionError` | Network failure |

```js
try {
  await stripe.paymentIntents.create({ ... });
} catch (err) {
  if (err instanceof Stripe.errors.StripeCardError) { /* decline */ }
}
```

## Retry Logic

`RequestSender` implements exponential backoff with jitter. Set `maxNetworkRetries` on the client or per-request. Idempotency keys are auto-set for POST requests when retrying.

## Webhook Verification

```js
const event = stripe.webhooks.constructEvent(rawBody, sig, secret);
// or async:
const event = await stripe.webhooks.constructEventAsync(rawBody, sig, secret);
```

Requires raw (unparsed) request body — Express needs `express.raw()` middleware. Default clock skew tolerance: 300 seconds.

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

## Sources

- [[source-github-stripe-node]] — primary: SDK repo (14 key files), error taxonomy, webhook verification, pagination, PaymentIntent + Checkout Session APIs
