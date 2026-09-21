---
title: "GitHub: stripe/stripe-node"
type: source
date_ingested: 2026-05-08
date_updated: 2026-09-21
original_format: github-repo
raw_files:
  - "github/stripe/stripe-node/snapshots/2026-09-21-9f82c46/manifest.json"
  - "github/stripe/stripe-node/snapshots/2026-09-21-2f64e7a/manifest.json"
  - "github/stripe/stripe-node/supplements/2026-09-21-2f64e7a-f49df03e/manifest.json"
  - "github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/manifest.json"
  - "github/stripe/stripe-node/snapshots/2026-08-08-57626dc/manifest.json"
  - "github-stripe-node.md"
tags: [stripe, stripe-node, node-js, sdk, typescript, payment-intents, checkout, webhooks, pagination, idempotency, github-repository]
---

## Overview

`stripe/stripe-node` publishes the `stripe` npm package, Stripe's server-side JavaScript SDK. This cumulative page preserves the `stripe@22.1.1` baseline, full `22.4.0` ingest, `22.5.0` delta and full `22.6.0` ingest, then adds approved delta `stripe@22.6.1` at SHA `9f82c466c0a5913906ab1bf39790edd4d231ee5d`. See the separate [[changelog-github-stripe-node]] for release chronology.

Repository: <https://github.com/stripe/stripe-node>

## Evidence Boundary

- The repository proves the SDK transport, generated request/response types, resource methods, package exports, and retained release history. It does not prove merchant eligibility, account enablement, payment-method geography, or Dashboard configuration.
- This is a server SDK. Browser collection of customer and payment information belongs to Stripe.js; declaration presence in Stripe Node is not proof of a client integration path.
- Generated types track the API version pinned by the package. Version-specific answers must identify both the `stripe` package version and, when relevant, its pinned Stripe API version.
- The source capsule intentionally retains checkout-focused public API files and examples, not the full repository. Tests are excluded; deeper non-checkout questions may require a fresh clone and targeted source search.
- The v22.4.0 README and constructor source disagree on the fallback retry count. Set `maxNetworkRetries` explicitly and treat the default as unresolved for this exact snapshot.
- The 22.5.0 ingest used an explicitly approved focused-reading exception: changed implementation and complete comparison read, unchanged historical changelog blocks and snapshot inventories checked mechanically. Entry-point changes outside the capsule are comparison-diff evidence only; no upstream tests, SDK build, or live payment flow were executed.
- The 22.6.0 full-mode ingest also has an explicit one-time focused-reading exception: changed behavior and affected prior context reviewed, unchanged evidence and historical changelog checked mechanically. Two exact-SHA supplemental implementation files close the notification-handler/coercion gap without changing future collection policy. Non-checkout release-note entries remain overview-only; tests/fixtures and the entire repository were not read or executed.

## Grounding Excerpts

The 22.6.1 delta uses an explicitly approved focused-reading exception: changed retained implementation and the complete comparison were read, while unchanged historical changelog and manifest inventories were checked mechanically. Both 68-file snapshots pass size/hash verification. Tests outside the capsule were reviewed as diff evidence only, not executed. No whole-repository read or runtime security guarantee is claimed.

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
| `stripe` | `22.6.1` | `2026-08-26.dahlia` | `v2442` | Node.js 18+ | Approved delta with focused reading; earlier versions retained |

This table reports wiki ingest progress, not the latest release currently published upstream.

## Package and Runtime Shape

The package has no runtime dependencies and marks `@types/node >=18` as an optional peer dependency. Its exports select CommonJS and ES module builds for Node and separate builds for browser/worker, Bun, Deno, and workerd environments.

The client exposes V1 resources such as `paymentIntents`, `setupIntents`, `checkout.sessions`, `paymentLinks`, `customers`, `invoices`, `subscriptions`, `subscriptionItems`, `subscriptionSchedules`, `refunds`, and `webhookEndpoints`, plus V2 namespaces and event-notification support. `rawRequest()` is an escape hatch for API operations not yet represented by generated resource methods.

Configuration includes API version, timeout, retries, HTTP client/agent, telemetry, event-body emission, Connect account, and Stripe context. The timeout fallback is 80 seconds. Request and response events expose operation metadata and can include bodies only when `emitEventBodies` is enabled.

## Requests, Retries, and Idempotency

`RequestSender` retries connection failures, HTTP 409, HTTP 5xx, and responses explicitly marked retryable by `stripe-should-retry`; an explicit false header suppresses retry. Delay uses bounded exponential backoff with jitter. Stripe Node 22.3.1 removed `Retry-After` handling, so integrations must not assume that this release schedules retries from that response header.

Retry count can be overridden per request. Through 22.5.0, V1 POST requests receive generated idempotency keys when retries are enabled. In 22.6.0 they receive them even with zero configured retries, protecting the existing first closed-connection retry exception. V2 POST and DELETE behavior is unchanged. Automatic keys cover SDK retries of one call, not separate application calls; use a stable explicit operation key for the latter.

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

## 22.6.0: Notification Handlers and Transport

### Thin Event Dispatch

Use instance factories `stripe.notificationHandler(webhookSecret, fallback)` and `stripe.notificationHandlerWithoutVerification(fallback)`. Handler class names are type-only aliases on the public Stripe namespace, not static constructor values. The unverified factory is only for already authenticated delivery boundaries.

- `.on(type, callback)` accepts one callback per type; `.preHandle(callback)` accepts one pre-hook. Register everything at startup. Duplicate registration throws; the first `handle` invocation locks registration even if parsing or signature verification then fails.
- `preHandle` returning false skips both event-specific and fallback callbacks. The fallback receives `{isKnownEventType}`, based on this release's known-type set. It does not mean a known event has a registered callback. `registeredEventTypes()` returns sorted registered keys.
- Verified `handle(rawBody, signature)` calls the synchronous thin-event parser despite being async itself. It exposes no crypto-provider argument; do not assume it works in async-only crypto runtimes. Unverified `handle(rawBody)` accepts string or `Uint8Array` and authenticates nothing.
- Callback failures propagate. The helper neither acknowledges HTTP requests nor implements durable deduplication. The new diff-only sample uses an in-memory Set and records IDs before business processing, which can suppress a retry after failure; its Express endpoints also omit sending a response. Treat it as illustrative, not production-ready.

> [!warning] Contradiction
> The handler's comment describes an event-context client, but `Object.assign` only shallow-copies the client and replaces `_api`. The existing resource objects retain their original `_stripe`, and the shared RequestSender retains its original client reference. Source tracing therefore indicates that ordinary callback-client resource calls can use the original default context rather than the event context. This has not been reproduced with a packaged SDK. Event `fetchEvent()`/`fetchRelatedObject()` explicitly pass context and are a distinct path; otherwise pass per-request context explicitly and verify routing before deployment. The same warning is recorded in [[stripe-node-sdk]].

The client-level `stripe.constructEventWithoutVerification` alias is now deprecated for removal in the next major; use `stripe.webhooks.constructEventWithoutVerification` instead. The 22.5.0 example remains historical. `parseEventNotificationWithoutVerification` now accepts bytes as well as strings. The earlier shared-core versus Node-ESM missing-object inconsistency is not fixed by the reviewed 22.6.0 diff.

### Body Failures, Timeouts and Idempotency

Fetch now retains its request timer after headers while reading JSON. With AbortController it relies on the fetch implementation honoring abort during body consumption; without it, a promise race bounds waiting but cannot cancel underlying work. Streaming handoff releases the fetch timer. Node listens for response errors and incomplete close, and destroys incomplete responses with the timeout error when the socket times out. Node stream consumers can consequently see an `ETIMEDOUT` TypeError instead of the earlier `ECONNRESET` / `aborted` error; this is not the same deadline model as fetch.

In RequestSender, body-read **timeouts** become `StripeConnectionError` with request ID where available. Other body-read failures, including non-timeout connection loss, still become `StripeAPIError` with the historical invalid-JSON message; actual malformed JSON also remains `StripeAPIError`. The release-note description of connection errors is broader than this implementation. Body-read rejection goes directly to the callback, not through the automatic request retry loop.

Every V1 POST now gets an automatic idempotency key unless overridden, even at `maxNetworkRetries: 0`. This protects the pre-existing first `ECONNRESET`/`EPIPE` reattempt, which can occur after the API processed the request. Zero configured retries still does not mean zero possible reattempts. This release does not resolve the historical README/platform retry-default mismatch.

### V2 Polymorphic Coercion

`V2RuntimeSchema` adds `discriminatedUnion`. For a non-null request object, missing or non-string discriminator values throw before sending; recognized variants recursively coerce schema-marked int64/decimal fields. Unknown string variants pass through without coercion. This is not a complete validator: nullish and mismatched primitive/array shapes can pass through too.

Request object coercion returns a new object and preserves unknown fields. Responses are mutated in place, with recognized int64 strings converted to BigInt and decimal strings to Decimal; missing/unknown discriminators pass through. Invalid numeric conversions throw. Stringifying an already-rounded JavaScript number cannot restore lost precision; retain precise integer values before SDK encoding.

## 22.6.0: Generated API Changes

The package pins API `2026-08-26.dahlia`, OpenAPI `v2442`; the API family remains `dahlia`. The SDK runtime dependency and Node-minimum declarations do not change in this boundary.

| Surface | Change and boundary |
| --- | --- |
| Checkout | Adds `payment_method_options.card.restrictions.funding_types_blocked`, documented as credit/debit/prepaid, on create params and response. Shipping-permission comments now specify `ui_mode=elements`; not proof of runtime availability. |
| PaymentIntent / SetupIntent | Response `allowed_payment_method_types` becomes required but nullable; request create/update/confirm fields remain optional. Adds `touch_n_go` to allowlist enums. |
| Payment Links | Update params gain emptyable application fee amount/percent, `on_behalf_of`, and `transfer_data`. Amount is for non-recurring line items; percentage requires at least one recurring price, 0-100 with up to two decimals. Transfer data requires destination and allows optional emptyable amount. |
| Link / ConfirmationToken | Charge Link details gain funding-source-group fields; ConfirmationToken gains required-but-nullable metadata. These are server response contracts. |
| Billing | Invoice/subscription payment settings gain Billie typings. Subscription cancellation details gain `feedback_option`, with ID-or-expanded-object response and optional ID in update/cancel params. Eligibility/recurring availability is not proven by an enum. |
| TypeScript | Many enums gain `OtherString`, including payment status types. Conversely, WebhookEndpoint create/update `enabled_events` loses `OtherString`; API-version enum gains the new pin. Recheck exhaustive switches, mocks and custom event-name typing. |

Subscription billing-schedule comments additionally clarify flexible-mode/API-version requirements and that `bill_until` must not precede applicable item period ends. These are documentation clarifications, not newly introduced schedule fields.

Release notes also announce Billing FeedbackOption operations, Billing Portal feedback/customer-update flows, CustomerSession components, AccountSession payment-method settings, FinancialConnections country filters, InvoiceItem frozen fields, IGIC registration fields and removal of PaymentRecord/PaymentAttemptRecord `cryptogram`. These are overview/navigation facts only in this ingest; collect/read the relevant full files before a detailed non-checkout integration answer. New generated error-code values do not establish new runtime error classes.

## 22.6.1: Request and Upload Hardening

### Multipart Boundaries and Headers

POST multipart generation now obtains its delimiter from the platform's cryptographically secure `uuid4()` instead of combining `Math.random()` values. The base platform requires `crypto.randomUUID`; Node calls its imported crypto module, so absence of global crypto alone does not break the supported Node path. Failure to obtain secure randomness rejects multipart generation before sending, without a weak-boundary fallback.

Automatic idempotency key generation is deliberately different: RequestSender catches a UUID failure and falls back to a Math.random-derived UUID-shaped value. This preserves automatic key generation but is not a uniqueness guarantee or a substitute for stable application-operation keys across separate calls.

The file part's MIME Content-Type now replaces CR/LF with spaces to prevent injected header lines. Name/filename quote escaping and CR/LF replacement already existed in 22.6.0 and are refactored, not newly introduced protections. File bytes are preserved; unpredictable boundaries are not file-content sanitization.

### Request Paths and Thin Event IDs

`utils.validatePath` rejects non-string paths, strings without a leading `/`, and strings beginning `//`. RequestSender invokes it before deriving V1/V2 mode, authentication or network dispatch. Invalid raw requests reject with an ordinary Error rather than requiring an HTTP response. This protects the shared sink used by raw requests and remotely supplied paths, but is not a complete URL validator or an authorization mechanism.

Thin-notification `fetchEvent()` now builds its path with `encodeURIComponent(parsed.id)`, preventing ID characters from injecting path/query segments. `fetchRelatedObject()` still uses the supplied related-object URL, subject to the shared path guard. Both retain explicit Stripe context and request-trigger metadata. The Node ESM change is corroborated by the comparison diff, not a standalone retained entrypoint file. Parsing without verification remains unauthenticated; these changes do not make untrusted notifications safe to accept.

### GET/DELETE Coercion and Enum Documentation

StripeResource now applies `requestSchema` coercion before separating query data from body data. Schema-marked int64/Decimal values, including nested fields, therefore serialize in GET/DELETE queries as well as POST bodies. GET/DELETE bodies remain null. Unknown fields and the prior coercion limitations remain; this is not general schema validation. The separate `rawRequest()` API still rejects non-POST requests with nonempty structured params, so its callers must not infer new query-object support from this fix.

README and `OtherString` comments clarify that open enums may gain values on older API versions. `OtherString = string & Record<never, never>` itself is unchanged. API pin `2026-08-26.dahlia`, OpenAPI `v2442`, generated checkout resource files, Node minimum, package exports and runtime dependencies are unchanged. No new checkout product or merchant eligibility is established.

The historical handler-context and parser-entrypoint caveats above are not resolved by this patch. Upstream CI also pins actions and adds workflow security checks; these are repository-maintenance changes, not SDK runtime behavior.

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

### `stripe@22.6.0`

The September 21 full-mode ingest adds the August 26 changelog release (GitHub release timestamp August 27 UTC), with 33 modified and 35 unchanged capsule files plus two approved supplemental implementation files. It appends notification, transport, coercion and generated-contract knowledge without replacing the earlier baselines. Reading scope and verification are recorded in the [review receipt](../../../../tracking/github/repos/stripe/stripe-node/ingest-review-436c32c5.md).

### `stripe@22.6.1`

The September 21 delta ingest retains the September 1 release: 13 modified and 55 unchanged capsule files, with older raw evidence and all source/changelog history preserved. See the [review receipt](../../../../tracking/github/repos/stripe/stripe-node/ingest-review-2402efbb.md).

## Related

- Company: [[stripe]]
- Concepts: [[stripe-node-sdk]], [[stripe-payment-intents]], [[stripe-checkout]]
- History: [[changelog-github-stripe-node]]

## Raw Sources

- [22.6.1 snapshot](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-9f82c46/manifest.json), [release manifest](../../../../raw/github/stripe/stripe-node/releases/stripe/22.6.1/2026-09-21/manifest.json), [release notes](../../../../raw/github/stripe/stripe-node/releases/stripe/22.6.1/2026-09-21/release-notes.md)
- [22.6.0 to 22.6.1 comparison](../../../../tracking/github/repos/stripe/stripe-node/comparisons/stripe/22.6.0--22.6.1/comparison.json), [complete diff](../../../../tracking/github/repos/stripe/stripe-node/comparisons/stripe/22.6.0--22.6.1/diff.patch)
- [Multipart](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-9f82c46/files/src/multipart.ts), [base platform](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-9f82c46/files/src/platform/PlatformFunctions.ts), [Node platform](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-9f82c46/files/src/platform/NodePlatformFunctions.ts), [request sender](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-9f82c46/files/src/RequestSender.ts) - boundary generation, fallback and request dispatch
- [Utilities](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-9f82c46/files/src/utils.ts), [core](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-9f82c46/files/src/stripe.core.ts), [resource](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-9f82c46/files/src/StripeResource.ts) - path checks, event-ID encoding and query coercion
- [README](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-9f82c46/files/README.md), [shared types](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-9f82c46/files/src/shared.ts), [package](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-9f82c46/files/package.json) - enum clarification and unchanged compatibility boundary

- [22.6.0 snapshot manifest](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-2f64e7a/manifest.json), [release manifest](../../../../raw/github/stripe/stripe-node/releases/stripe/22.6.0/2026-09-21/manifest.json), [release notes](../../../../raw/github/stripe/stripe-node/releases/stripe/22.6.0/2026-09-21/release-notes.md)
- [22.5.0 to 22.6.0 comparison](../../../../tracking/github/repos/stripe/stripe-node/comparisons/stripe/22.5.0--22.6.0/comparison.json) and [diff](../../../../tracking/github/repos/stripe/stripe-node/comparisons/stripe/22.5.0--22.6.0/diff.patch) - includes excluded entrypoint/sample files; not all test/fixture or non-checkout content was read
- [Supplement manifest](../../../../raw/github/stripe/stripe-node/supplements/2026-09-21-2f64e7a-f49df03e/manifest.json), [notification handler](../../../../raw/github/stripe/stripe-node/supplements/2026-09-21-2f64e7a-f49df03e/files/src/StripeEventNotificationHandler.ts), [V2 coercion](../../../../raw/github/stripe/stripe-node/supplements/2026-09-21-2f64e7a-f49df03e/files/src/V2Coercion.ts), [canonical attachment](../../../../tracking/github/repos/stripe/stripe-node/evidence-attachments/github-436c32c59360977be8fa/attachment.json) - both implementations read fully
- [22.6.0 RequestSender](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-2f64e7a/files/src/RequestSender.ts), [StripeResource](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-2f64e7a/files/src/StripeResource.ts), [core](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-2f64e7a/files/src/stripe.core.ts) - request binding, context, idempotency and error dispatch
- [Fetch transport](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-2f64e7a/files/src/net/FetchHttpClient.ts), [Node transport](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-2f64e7a/files/src/net/NodeHttpClient.ts), [HTTP base](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-2f64e7a/files/src/net/HttpClient.ts) - fully read transport implementations
- [Checkout](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-2f64e7a/files/src/resources/Checkout/Sessions.ts), [PaymentIntents](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-2f64e7a/files/src/resources/PaymentIntents.ts), [SetupIntents](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-2f64e7a/files/src/resources/SetupIntents.ts), [Payment Links](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-2f64e7a/files/src/resources/PaymentLinks.ts) - focused changed-contract reading
- [Invoices](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-2f64e7a/files/src/resources/Invoices.ts), [Subscriptions](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-2f64e7a/files/src/resources/Subscriptions.ts), [Charges](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-2f64e7a/files/src/resources/Charges.ts), [ConfirmationTokens](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-2f64e7a/files/src/resources/ConfirmationTokens.ts), [WebhookEndpoints](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-2f64e7a/files/src/resources/WebhookEndpoints.ts) - focused type/field deltas

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
