---
title: "GitHub: stripe/stripe-node"
type: source
date_ingested: 2026-05-08
date_updated: 2026-08-08
original_format: github-repo
raw_files:
  - "github/stripe/stripe-node/snapshots/2026-08-08-57626dc/manifest.json"
  - "github-stripe-node.md"
tags: [stripe, stripe-node, node-js, sdk, typescript, payment-intents, checkout, webhooks, pagination, idempotency, github-repository]
---

## Overview

`stripe/stripe-node` publishes the `stripe` npm package, Stripe's server-side JavaScript SDK. This cumulative page preserves the earlier `stripe@22.1.1` baseline and adds the approved full ingest of `stripe@22.4.0` at exact SHA `57626dcdfb94164fc9f112dfaa3c57aec5130e4f`.

Repository: <https://github.com/stripe/stripe-node>

## Evidence Boundary

- The repository proves the SDK transport, generated request/response types, resource methods, package exports, and retained release history. It does not prove merchant eligibility, account enablement, payment-method geography, or Dashboard configuration.
- This is a server SDK. Browser collection of customer and payment information belongs to Stripe.js; declaration presence in Stripe Node is not proof of a client integration path.
- Generated types track the API version pinned by the package. Version-specific answers must identify both the `stripe` package version and, when relevant, its pinned Stripe API version.
- The source capsule intentionally retains checkout-focused public API files and examples, not the full repository. Tests are excluded; deeper non-checkout questions may require a fresh clone and targeted source search.
- The v22.4.0 README and constructor source disagree on the fallback retry count. Set `maxNetworkRetries` explicitly and treat the default as unresolved for this exact snapshot.

## Grounding Excerpts

> "The Stripe Node library provides convenient access to the Stripe API from applications written in server-side JavaScript."
>
> `raw/github/stripe/stripe-node/snapshots/2026-08-08-57626dc/files/README.md:10-11`

> "For collecting customer and payment information in the browser, use Stripe.js."
>
> `raw/github/stripe/stripe-node/snapshots/2026-08-08-57626dc/files/README.md:13`

> "As of v13 stripe-node will automatically do one reattempt for failed requests that are safe to retry."
>
> `raw/github/stripe/stripe-node/snapshots/2026-08-08-57626dc/files/README.md:304`

> "Please note that you must pass the raw request body, exactly as received from Stripe, to the constructEvent() function; this will not work with a parsed (i.e., JSON) request body."
>
> `raw/github/stripe/stripe-node/snapshots/2026-08-08-57626dc/files/README.md:396`

> "This release changes the pinned API version to 2026-07-29.dahlia."
>
> `raw/github/stripe/stripe-node/releases/stripe/22.4.0/2026-08-08/release-notes.md:1`

## Package Status

| Package | Latest ingested release | Pinned API | OpenAPI marker | Node support | Evidence status |
| --- | --- | --- | --- | --- | --- |
| `stripe` | `22.4.0` | `2026-07-29.dahlia` | `v2349` | Node.js 18+ | Approved full ingest; v22.1.1 history retained |

This table reports wiki ingest progress, not the latest release currently published upstream.

## Package and Runtime Shape

The package has no runtime dependencies and marks `@types/node >=18` as an optional peer dependency. Its exports select CommonJS and ES module builds for Node and separate builds for browser/worker, Bun, Deno, and workerd environments.

The client exposes V1 resources such as `paymentIntents`, `setupIntents`, `checkout.sessions`, `paymentLinks`, `customers`, `invoices`, `subscriptions`, `subscriptionItems`, `subscriptionSchedules`, `refunds`, and `webhookEndpoints`, plus V2 namespaces and event-notification support. `rawRequest()` is an escape hatch for API operations not yet represented by generated resource methods.

Configuration includes API version, timeout, retries, HTTP client/agent, telemetry, event-body emission, Connect account, and Stripe context. The timeout fallback is 80 seconds. Request and response events expose operation metadata and can include bodies only when `emitEventBodies` is enabled.

## Requests, Retries, and Idempotency

`RequestSender` retries connection failures, HTTP 409, HTTP 5xx, and responses explicitly marked retryable by `stripe-should-retry`; an explicit false header suppresses retry. Delay uses bounded exponential backoff with jitter. Stripe Node 22.3.1 removed `Retry-After` handling, so integrations must not assume that this release schedules retries from that response header.

Retry count can be overridden per request. V1 POST requests receive generated idempotency keys when retries are enabled. V2 POST and DELETE requests receive generated keys under the retained implementation.

There is a concrete v22.4.0 contradiction: README lines 237 and 304 document one retry, while `src/stripe.core.ts:1139-1143` supplies fallback `2`. The wiki therefore does not claim an implicit effective value. Integrations that depend on a specific retry budget should configure it directly.

## Errors and Observability

The SDK maps API errors into card, invalid-request, API, authentication, permission, rate-limit, connection, signature-verification, idempotency, OAuth, and V2 temporary-session classes. Consumers should branch on typed error classes and still preserve request IDs and API error details for support.

Request/response events expose API version, account or context, idempotency key, method, path, timing, status, and request ID. Telemetry can be disabled; event bodies are opt-in.

## Webhooks and Event Notifications

V1 webhook verification uses `constructEvent()` or `constructEventAsync()` and requires the exact unparsed request body. The default timestamp tolerance exposed by the webhook object is 300 seconds. The retained Express, Koa, NestJS, and Next.js examples all preserve the raw-body boundary before verification.

V2 event notifications use `parseEventNotification()` or `parseEventNotificationAsync()`. After signature verification, the SDK parses Stripe context and attaches `fetchEvent()` and `fetchRelatedObject()` helpers. Passing a V1 webhook event to this V2 parser is rejected explicitly.

Webhook endpoint resources support create, retrieve, update, list, and delete. Endpoints can pin an API version, select events, and receive either account or connected-account events.

## Pagination and Search

List promises support async iteration, `autoPagingEach()`, and bounded `autoPagingToArray()`. Array collection requires an explicit limit and caps it at 10,000 to prevent accidental unbounded accumulation.

Search resources are eventually consistent and must not be used in strict read-after-write workflows. The generated Product documentation warns that indexing normally takes less than a minute but can lag by up to an hour during outages.

## Checkout and Payment APIs

### PaymentIntents and SetupIntents

PaymentIntent methods include create, retrieve, update, list, search, confirm, capture, cancel, incremental authorization, customer-balance application, microdeposit verification, and amount-detail line-item listing. SetupIntent methods cover create, retrieve, update, list, confirm, cancel, and microdeposit verification.

Both resources model multi-step statuses and next actions. In 22.4.0 they add `allowed_payment_method_types` to object and create/update/confirm parameter surfaces. `setup_future_usage` remains the server signal for reuse and SCA optimization, but each payment method's accepted values differ; a generic field does not establish recurring support for every method.

### Checkout Sessions and Payment Links

Checkout Session methods are create, retrieve, update, list, expire, and list line items. The generated contract covers payment, setup, and subscription modes; hosted, embedded, and custom UI modes; customer creation; consent and tax collection; shipping; discounts; optional items; and subscription data.

The 22.4.0 release removes the limited-use `dynamic_tax_rates` field from Checkout Session create line items. It adds Payco and Samsung Pay `setup_future_usage` options and adds `ic_nif` to Checkout customer tax-ID typing.

Payment Links support create, retrieve, update, list, and line-item listing. The current release adds update-time `consent_collection` and `shipping_options`, and extends `payment_intent_data` for future-usage handling.

### Billing and Refunds

Subscriptions support create, retrieve, update, list, search, cancel, migrate, resume, and discount deletion. Subscription schedules support phased create/update, cancel, and release, while subscription items support independent item changes and proration controls.

The 22.4.0 generated billing surface adds Alipay and MB WAY to invoice/subscription payment-method type enums and adds `trial` to subscription schedule phases. These are typed API capabilities, not proof that a specific merchant can use those methods or that they support every recurring scenario.

Refunds support create, retrieve, update, list, and cancellation for refunds requiring action. The current object adds customer, customer-account, and payment-method attribution. Create parameters permit an optional partial amount, while proportional application-fee and transfer reversal behavior is separately configurable.

## TypeScript Versioning

Stripe Node types reflect the latest API shape associated with the package. Minor releases may add response enum values or weaken exhaustiveness without runtime incompatibility, so TypeScript errors can appear on minor upgrades. Major SDK releases carry backwards-incompatible Stripe API changes. Exact package and API versions should therefore be recorded in implementation and comparison answers.

## Retained History

### `stripe@22.1.1`

The May 2026 baseline at SHA `1899375db06ae1e102a93637e193f8c9cb1de831` established the SDK's resource pattern, retry/idempotency behavior, webhook verification, pagination, PaymentIntent methods, and Checkout Session methods against OpenAPI marker `v2252`. Those validated behaviors remain historical evidence; they are not relabeled as 22.4.0 changes.

### `stripe@22.4.0`

The August 2026 ingest advances the retained package and API baseline, expands the source capsule to 66 key files, corrects stale retry and error-taxonomy summaries, and records the release-specific Checkout, payment-method, subscription, refund, event, and typing changes above.

## Related

- Company: [[stripe]]
- Concepts: [[stripe-node-sdk]], [[stripe-payment-intents]], [[stripe-checkout]]
- History: [[changelog-github-stripe-node]]

## Raw Sources

- [Snapshot manifest](../../../../raw/github/stripe/stripe-node/snapshots/2026-08-08-57626dc/manifest.json) — exact-SHA source capsule and file hashes
- [Release manifest](../../../../raw/github/stripe/stripe-node/releases/stripe/22.4.0/2026-08-08/manifest.json) — package-qualified release record
- [Release notes](../../../../raw/github/stripe/stripe-node/releases/stripe/22.4.0/2026-08-08/release-notes.md) — exact release notes
- [README](../../../../raw/github/stripe/stripe-node/snapshots/2026-08-08-57626dc/files/README.md) — package boundary, configuration, retries, TypeScript policy, webhooks, and pagination
- [Stripe core](../../../../raw/github/stripe/stripe-node/snapshots/2026-08-08-57626dc/files/src/stripe.core.ts) — client construction, defaults, resources, exports, and V2 event parsing
- [Request sender](../../../../raw/github/stripe/stripe-node/snapshots/2026-08-08-57626dc/files/src/RequestSender.ts) — request, retry, idempotency, headers, and telemetry behavior
- [Webhooks](../../../../raw/github/stripe/stripe-node/snapshots/2026-08-08-57626dc/files/src/Webhooks.ts) — V1 signature verification and tolerance
- [Automatic pagination](../../../../raw/github/stripe/stripe-node/snapshots/2026-08-08-57626dc/files/src/autoPagination.ts) — V1/V2 iteration and collection limits
- [Checkout Sessions resource](../../../../raw/github/stripe/stripe-node/snapshots/2026-08-08-57626dc/files/src/resources/Checkout/Sessions.ts) — Checkout Session public API
- [PaymentIntents resource](../../../../raw/github/stripe/stripe-node/snapshots/2026-08-08-57626dc/files/src/resources/PaymentIntents.ts) — PaymentIntent public API
- [SetupIntents resource](../../../../raw/github/stripe/stripe-node/snapshots/2026-08-08-57626dc/files/src/resources/SetupIntents.ts) — SetupIntent public API
- [Subscriptions resource](../../../../raw/github/stripe/stripe-node/snapshots/2026-08-08-57626dc/files/src/resources/Subscriptions.ts) — subscription public API
- [Subscription schedules resource](../../../../raw/github/stripe/stripe-node/snapshots/2026-08-08-57626dc/files/src/resources/SubscriptionSchedules.ts) — phased subscription schedule public API
- [Repository changelog](../../../../raw/github/stripe/stripe-node/snapshots/2026-08-08-57626dc/files/CHANGELOG.md) — upstream repository history
- [Legacy v22.1.1 navigation record](../../../../raw/github-stripe-node.md) — legacy raw navigation record
