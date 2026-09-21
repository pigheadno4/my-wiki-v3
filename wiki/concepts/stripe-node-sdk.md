---
title: "Stripe Node.js SDK (stripe-node)"
type: concept
category: technology
tags: [stripe, node-js, sdk, payment-intents, webhooks, pagination, error-handling, typescript, idempotency]
---

## Definition

The official Stripe Node.js library (`stripe` npm package) wraps the Stripe REST API for server-side JavaScript. The latest ingested release is `stripe@22.6.0` at SHA `2f64e7ac920bd6863fdb851f4fb1fcc6190d963f`, pinning Stripe API `2026-08-26.dahlia` and OpenAPI marker `v2442`. Earlier `22.1.1`, `22.4.0` and `22.5.0` knowledge remains version-qualified in the cumulative source. It supports Node.js 18+ and exports builds for Node, browser/worker, Bun, Deno, and workerd environments, plus an opt-in `extensibility` export condition introduced in 22.5.0. Collected but uningested versions are not this page's knowledge baseline.

**Install**: `npm install stripe`

## SDK Initialization

```js
import Stripe from 'stripe';
const stripe = new Stripe('sk_...', { apiVersion: '2024-06-20' });
```

Key options: `apiVersion`, `maxNetworkRetries`, `timeout` (default 80,000ms), `telemetry`, `emitEventBodies`, `httpClient`, `stripeAccount`, and `stripeContext`.

> [!warning] Version-specific retry default
> In `stripe@22.4.0`, the README documents `maxNetworkRetries: 1`, but the retained constructor source passes `2` as the fallback to `validateInteger`. Treat the effective default as an evidence conflict and set `maxNetworkRetries` explicitly for deterministic behavior.

In 22.5.0 the shared core obtains the fallback from the platform: `2` on the base/Node platform, `0` on the new extensibility platform. The unchanged README still documents one retry; this does not resolve the historical conflict. Source: [[source-github-stripe-node]].

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

`RequestSender` implements exponential backoff with jitter. Set `maxNetworkRetries` on the client or per request. Through 22.5.0, V1 POST requests get an automatic idempotency key when retries are enabled; 22.6.0 generates one even with `maxNetworkRetries: 0`, protecting the existing first `ECONNRESET`/`EPIPE` retry exception. V2 POST and DELETE behavior is unchanged. Separate application calls still need an explicit stable operation key for application-level deduplication. Retry decisions cover connection errors, HTTP 409, HTTP 5xx, and the `stripe-should-retry` response header. Source: [[source-github-stripe-node]].

In 22.6.0, JSON response-body timeouts become `StripeConnectionError`; other body-read failures and invalid JSON remain `StripeAPIError`. Body-read failures terminate that call rather than entering a new SDK retry loop. Fetch keeps its timeout through JSON body consumption but releases it on streaming handoff; Node stream consumers can now receive an `ETIMEDOUT` TypeError instead of an `ECONNRESET` error on a stalled body. These are transport-specific boundaries, not a universal wall-clock deadline.

## Webhook Verification

```js
const event = stripe.webhooks.constructEvent(rawBody, sig, secret);
// or async:
const event = await stripe.webhooks.constructEventAsync(rawBody, sig, secret);
```

Requires raw (unparsed) request body — Express needs `express.raw()` middleware. Default clock skew tolerance: 300 seconds.

V2 event notifications use `parseEventNotification()` or `parseEventNotificationAsync()`. These verify the signature and attach helpers for fetching the full event and related object; they are distinct from V1 webhook events handled by `constructEvent()`.

### Previously Verified Events in 22.5.0

`stripe.webhooks.constructEventWithoutVerification(payload)` and its client-level alias parse snapshot events; `stripe.parseEventNotificationWithoutVerification(payload)` parses thin notifications. These accept JSON strings and unwrap AWS EventBridge `detail` or Azure CloudEvents `data` when `specversion` is present. They perform no signature or timestamp verification. Use only after verification or an independently trusted delivery boundary, never as a replacement for verification on a public webhook endpoint. Envelope shape alone is not evidence of authenticity. Source: [[source-github-stripe-node]].

> [!warning] Contradiction
> The 22.5.0 comments name `webhooks.verifySignatureHeader(...)`, but the implemented low-level method is `stripe.webhooks.signature.verifyHeader(...)` (or `verifyHeaderAsync`). That low-level helper needs an explicit positive tolerance for timestamp-age checking; the high-level verified constructors/parsers retain their default 300-second age limit.

> [!warning] Contradiction
> In this exact release, shared core permits absent/null `object` after envelope extraction or verified parsing, while the Node ESM implementation requires `object === 'v2.core.event'`. Both reject a V1 event in the thin parser. The direct unverified raw-JSON path requires a recognized `object` before reaching that check. Do not assume import/require parity for omitted-object inputs; this is source/diff evidence, not a packaged-runtime test. See [[changelog-github-stripe-node]].

### Thin Notification Handlers in 22.6.0

Create handlers with `stripe.notificationHandler(secret, fallback)` or, only behind an authenticated delivery boundary, `stripe.notificationHandlerWithoutVerification(fallback)`. Register one `.on(type, callback)` per type and at most one `.preHandle(callback)` before the first `.handle()` invocation. A failed parse also locks further registration. A false pre-hook result skips both the registered callback and fallback; durable deduplication remains application-owned. Despite returning a promise, verified `handle` calls the synchronous parser, not the async-crypto parser.

> [!warning] Contradiction
> The 22.6.0 handler comment promises an event-context client, but its shallow copy shares resource objects and RequestSender still bound to the original client. Source tracing therefore does not establish automatic context propagation for ordinary callback-client API calls. Prefer event fetch helpers, which explicitly pass context, or explicit per-request context; validate the packaged runtime before relying on implicit routing. This is a source-level finding, not an executed SDK reproduction. See [[source-github-stripe-node]].

The client-level `constructEventWithoutVerification` alias is deprecated in 22.6.0; use `stripe.webhooks.constructEventWithoutVerification`. The thin unverified parser now accepts `Uint8Array` as well as strings. The historical 22.5.0 APIs above remain evidence for that version.

## Runtime Additions in 22.5.0

- `Stripe.MAJOR_API_VERSION` is the static constant, with value `dahlia`; the release note's lowercase `stripe.major_api_version` spelling is not the implementation. It does not change the full API pin.
- The conditional extensibility entrypoint uses runtime-provided `endpointFetch`, defaults to zero configured retries, and permits runtime-injected authentication. It only targets `api.stripe.com`, exposes no response headers or streaming, and requires an explicit crypto provider for crypto-dependent helpers. This is not a keyless ordinary Node integration.
- `HttpClientRuntimeError` bypasses connection retry/wrapping in RequestSender. This exception means not every transport/runtime failure is a `StripeError` subclass.
- Initializing under `CLAUDECODE` or `CLAUDE_CODE_CHILD_SESSION` can write a plugin hint to stderr; synchronous hint-write failures are caught.

Source: [[source-github-stripe-node]]. Existing checkout resource files are unchanged across this release boundary.

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

22.6.0 adds discriminated-union V2 coercion: a missing/non-string discriminator on a non-null request object throws; a recognized variant enables int64/decimal conversion; an unknown string passes through. Response coercion is in-place and tolerates missing/unknown discriminators. This is not complete schema validation and cannot recover precision already lost in a JavaScript number. Its generated types also make PaymentIntent/SetupIntent response allowlists required but nullable, extend open enums, and remove `OtherString` from WebhookEndpoint create/update `enabled_events`. Recheck typed mocks and exhaustive switches. Source: [[source-github-stripe-node]].

## Sources

- [[source-github-stripe-node]] — cumulative SDK repository evidence through `stripe@22.6.0`, preserving `22.1.1`, `22.4.0` and `22.5.0`
- [[changelog-github-stripe-node]] — package-qualified retained release history
