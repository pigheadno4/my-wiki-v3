---
title: "GitHub: stripe/stripe-node"
type: source
date_ingested: 2026-05-08
date_updated: 2026-09-21
original_format: github-repo
raw_files:
  - "github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/manifest.json"
  - "github/stripe/stripe-node/snapshots/2026-08-08-57626dc/manifest.json"
  - "github-stripe-node.md"
tags: [stripe, stripe-node, node-js, sdk, typescript, payment-intents, checkout, webhooks, pagination, idempotency, github-repository]
---

## Overview

`stripe/stripe-node` publishes the `stripe` npm package, Stripe's server-side JavaScript SDK. This cumulative page preserves the `stripe@22.1.1` baseline and full `stripe@22.4.0` ingest, then adds the approved `stripe@22.5.0` delta at SHA `65d99a2b76d0786d7cec8544920affadccc8b670`. See the separate [[changelog-github-stripe-node]] for release chronology.

Repository: <https://github.com/stripe/stripe-node>

## Evidence Boundary

- The repository proves the SDK transport, generated request/response types, resource methods, package exports, and retained release history. It does not prove merchant eligibility, account enablement, payment-method geography, or Dashboard configuration.
- This is a server SDK. Browser collection of customer and payment information belongs to Stripe.js; declaration presence in Stripe Node is not proof of a client integration path.
- Generated types track the API version pinned by the package. Version-specific answers must identify both the `stripe` package version and, when relevant, its pinned Stripe API version.
- The source capsule intentionally retains checkout-focused public API files and examples, not the full repository. Tests are excluded; deeper non-checkout questions may require a fresh clone and targeted source search.
- The v22.4.0 README and constructor source disagree on the fallback retry count. Set `maxNetworkRetries` explicitly and treat the default as unresolved for this exact snapshot.
- The 22.5.0 ingest used an explicitly approved focused-reading exception: changed implementation and complete comparison read, unchanged historical changelog blocks and snapshot inventories checked mechanically. Entry-point changes outside the capsule are comparison-diff evidence only; no upstream tests, SDK build, or live payment flow were executed.

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
| `stripe` | `22.5.0` | `2026-07-29.dahlia` | `v2349` | Node.js 18+ | Approved delta; v22.1.1 and v22.4.0 history retained |

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

### 22.5.0: Parsing Without Verification

Three additive helpers accept a JSON string:

| Method | Result | Authentication performed |
| --- | --- | --- |
| `stripe.webhooks.constructEventWithoutVerification(payload)` | Snapshot `Event` | None |
| `stripe.constructEventWithoutVerification(payload)` | Alias of the webhook-object helper | None |
| `stripe.parseEventNotificationWithoutVerification(payload)` | Thin notification with context and fetch helpers | None |

`utils.maybeExtractFromCloudProviderEnvelope` chooses `detail` when present (AWS EventBridge), then `data` when both `specversion` and `data` exist (Azure CloudEvents), then raw objects tagged `event` or `v2.core.event`. Other raw formats throw. These are shallow shape checks, not a full schema validator or proof of the sender's identity. Snapshot parsing rejects an inner `v2.core.event`; thin parsing rejects an inner `event`. Verified methods still verify the original raw payload first and do not use this cloud-envelope extraction path.

Use these helpers only for events already verified before durable queuing or delivered across an independently trusted boundary. Never replace public webhook verification with one of these calls. Preserve queue integrity and event deduplication separately; the parser neither authenticates the queue nor makes business effects idempotent.

Illustrative server-side flow for snapshot events, based on the retained API (not an executed integration):

```js
// Ingress: throws before enqueueing if signature/age verification fails.
stripe.webhooks.constructEvent(rawBody, signatureHeader, webhookSecret);
await trustedQueue.send(rawBody.toString('utf8'));

// Worker: this queue accepts only authenticated, integrity-protected messages.
const event = stripe.constructEventWithoutVerification(queuedPayload);
// Apply event-ID deduplication before business side effects.
```

For thin notifications use `parseEventNotification` at ingress and `parseEventNotificationWithoutVerification` in the worker. `fetchEvent()` requests `/v2/core/events/{id}`; `fetchRelatedObject()` resolves `null` without `related_object`, otherwise fetches its URL. Both preserve Stripe context and the `Stripe-Request-Trigger` header. These network operations are not performed just by parsing.

> [!warning] Contradiction
> 22.5.0 method comments refer to `webhooks.verifySignatureHeader(...)`, but the actual API is `stripe.webhooks.signature.verifyHeader(...)` or `verifyHeaderAsync(...)`. Calling those low-level helpers without a positive tolerance skips timestamp-age checking (`tolerance || 0`). The high-level verified constructors/parsers supply the 300-second fallback. Prefer those at ordinary webhook ingress; the new comment alone is not a reliable code sample.

> [!warning] Contradiction
> The retained shared core accepts absent/null `object` in its thin-event builder, rejecting other non-null values except `v2.core.event`. The Node ESM implementation in the full comparison requires `object === 'v2.core.event'` in both verified and unverified thin parsers. Thus omitted-object envelope/verified inputs can differ by entrypoint. Direct raw input to the unverified helper must first pass the stricter recognized-format extraction check. Compared with 22.4.0, unexpected non-null object types are now rejected rather than passed through. Do not assume a universal missing-object contract; no packaged-runtime parity test was run.

The synchronous test-header generator now adds guidance to use `generateTestHeaderStringAsync` when its crypto provider only supports async operations.

## 22.5.0 Runtime and Metadata Additions

`Stripe.MAJOR_API_VERSION` is a static class constant with value `dahlia`. The full API pin remains `2026-07-29.dahlia` and no generated checkout resource file changes in this comparison.

> [!warning] Contradiction
> The release notes call this `stripe.major_api_version`; retained core and Node ESM changes, corroborated by type-test diffs, expose `Stripe.MAJOR_API_VERSION`. Use the implemented spelling, not the release-note spelling. This is API-family metadata, not the installed SDK version or a new per-client API setting.

The package adds an `extensibility` **export condition**, ahead of `browser`, selecting dedicated CommonJS/ESM entrypoints. It is not a `stripe/extensibility` subpath. The adapter is specific to a Stripe Script runtime providing `endpointFetch`; it is not an ordinary Node/browser payment SDK mode:

- Authentication can be injected by that runtime through a no-op default authenticator; standard Node still requires a key or custom authenticator.
- The adapter sends the `stripe_api` endpoint, relative path, method, stringified headers and optional body, only for host `api.stripe.com`. A missing runtime function or unsupported host produces `HttpClientRuntimeError`.
- It returns empty response headers and does not support streaming. Therefore request-ID/header-driven behavior available with ordinary transports cannot be assumed here. Port/protocol/timeout arguments are not forwarded by this adapter; it establishes no local timeout guarantee.
- Its configured retry default is `0`, versus `2` for the base/Node platform. This does not remove RequestSender's existing first connection-closed retry exception. The unchanged README's one-retry description remains inconsistent with source defaults; configure retry budgets explicitly.
- Ordinary Node/fetch client factories and default crypto provider are unavailable in this platform. Crypto-dependent helpers require an explicitly supplied provider. Its pure-JavaScript emitter implementation is visible in the diff, not a standalone retained file.

`RequestSender` now passes `HttpClientRuntimeError` directly to the caller without retrying or wrapping it as `StripeConnectionError`. Node, fetch and endpointFetch JSON responses share `_parseResponseBody`, retaining `rawBody` on JSON parse errors. These are bounded transport changes, not new payment methods or merchant eligibility.

Initialization checks `CLAUDECODE` or `CLAUDE_CODE_CHILD_SESSION` and writes a plugin hint to stderr where supported; synchronous write errors are caught. Runtime dependencies, Node minimum and full API marker are unchanged. The lockfile's development-tool dependency refresh is not a new runtime dependency.

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

### `stripe@22.5.0`

The September 21 delta ingest adds trusted-event parsing, the API-family constant, opt-in extensibility runtime, and initialization hint. The 68-file capsule has two additions, 12 modifications and 54 unchanged files relative to 22.4.0. The upstream changelog also clarifies 22.4.0's `OtherString` open-enum entry retrospectively; that is not a new 22.5.0 checkout API change. All prior sections and snapshots remain available.

## Related

- Company: [[stripe]]
- Concepts: [[stripe-node-sdk]], [[stripe-payment-intents]], [[stripe-checkout]]
- History: [[changelog-github-stripe-node]]

## Raw Sources

- [22.5.0 snapshot manifest](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/manifest.json) - exact SHA, 68 retained files and hashes
- [22.5.0 release manifest](../../../../raw/github/stripe/stripe-node/releases/stripe/22.5.0/2026-09-21/manifest.json) and [release notes](../../../../raw/github/stripe/stripe-node/releases/stripe/22.5.0/2026-09-21/release-notes.md)
- [22.4.0 to 22.5.0 comparison](../../../../tracking/github/repos/stripe/stripe-node/comparisons/stripe/22.4.0--22.5.0/comparison.json) and [complete diff](../../../../tracking/github/repos/stripe/stripe-node/comparisons/stripe/22.4.0--22.5.0/diff.patch) - includes Node ESM, entrypoints, emitter and test changes outside the raw capsule
- [22.5.0 webhooks](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/src/Webhooks.ts), [core](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/src/stripe.core.ts), [utilities](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/src/utils.ts) - verified/unverified parsing and boundary checks
- [22.5.0 endpointFetch](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/src/net/EndpointFetchHttpClient.ts), [extensibility platform](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/src/platform/ExtensibilityPlatformFunctions.ts), [base platform](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/src/platform/PlatformFunctions.ts), [Node platform](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/src/platform/NodePlatformFunctions.ts) - runtime limits and defaults
- [22.5.0 request sender](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/src/RequestSender.ts), [HTTP base](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/src/net/HttpClient.ts), [fetch client](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/src/net/FetchHttpClient.ts), [Node client](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/src/net/NodeHttpClient.ts) - runtime errors and shared response parsing
- [22.5.0 package](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/package.json), [API marker](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/src/apiVersion.ts), [changelog](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/CHANGELOG.md) - exports, API identity, new entry and historical clarification; unchanged changelog history mechanically checked
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
