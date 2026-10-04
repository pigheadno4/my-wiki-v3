---
title: "Adyen Node.js API Library"
type: concept
category: technology
tags: [adyen, nodejs, typescript, server-sdk, checkout-api, cloud-device-api]
---

## Adyen Node.js API Library

The Adyen Node.js API Library is the merchant-server SDK for typed access to Adyen APIs. It complements, but does not replace, shopper-side Web or mobile SDKs. A typical checkout architecture creates payments or Sessions on the merchant server and presents payment methods or actions through an independently versioned client SDK.

## Current baseline

The first retained baseline is `@adyen/api-library@32.0.0` at exact SHA `99d1a0cf69c8660952baffd1437b00aae2fa4f23`. It requires Node.js 18 or newer and includes Checkout API v72 and Cloud Device API v1.

This is version-qualified implementation evidence. Merchant account configuration, API credential roles, geography, shopper context, and backend responses remain authoritative for product and payment-method availability.

## Checkout server surface

Checkout API groups typed operations for payment methods, payments, additional details, Sessions, modifications, orders, payment links, stored methods, donations, and utilities. Request and response models cover payment methods, 3D Secure, actions, recurring details, and result codes.

The library does not render checkout UI and a payment-method model does not prove eligibility. Web, iOS, Android, or React Native SDK evidence is required for client presentation and action behavior. Final status comes from the server response and, where required, the action and additional-details sequence.

## Client and transport

`Config` and `Client` select environment, credentials, live prefix, timeouts, region, proxy, certificate behavior, and redirect handling. Generated services serialize typed requests and deserialize typed responses. Request options can carry custom headers, query parameters, timeout, and an idempotency key.

The default transport restricts its one permitted 308 redirect to Adyen-owned host suffixes. Custom HTTP clients are supported but transfer responsibility for authentication, required headers, timeouts, and response handling to the integration.

## Cloud Device and Terminal API

Cloud Device API is the recommended cloud path for new in-person integrations in this baseline. It uses generated `tapi` models, requires merchant and device identifiers, supports regional live endpoints, exposes device status, and wraps asynchronous responses differently from legacy `TerminalCloudAPI`.

The encrypted variant adds Nexo payload encryption, HMAC integrity validation, credential metadata checks, and notification decryption. Legacy Terminal cloud remains present, while new cloud features are directed to Cloud Device API. Local Terminal API communication is a separate architecture.

## Version and query boundary

### `32.1.0` additive full update

Checkout remains v72 and Node.js remains 18 or newer. `PaymentsApi.updateSession`
adds `PATCH /sessions/{sessionId}` with required `amount` (currency and minor-unit
value) and `sessionData` from the client `beforeSubmit` callback. Optional
`payable: true` finalizes the amount and prevents further session updates;
`false` requires a later update to `true` before submission. The response's
`sessionData` is optional. Merchant servers must calculate the trusted amount;
this server evidence does not establish Web SDK callback behavior by itself.

Payment-method, donation and action discriminator classes gain concrete `type`
mappings used by the serializer. Checkout adds au PAY, d払い and SEPA donation
models, third-party token-request template data, richer enhanced-scheme data,
and PayPal order-update shipping address/amount and discount amount. Model
presence does not establish merchant eligibility. Old Checkout error-model
exports are removed; consumers must review generated type imports.

Custom HTTP implementations now accept `string | Buffer`, not only JSON strings.
The multipart helper buffers its payload and supplies content headers/length;
Document Collector upload and Session Authentication exports remain broader
API inventory because their full domain model trees are outside this capsule.
The newly retained standard-notification types are unchanged from the older
supplement, not newly introduced payment events. See
[[source-github-adyen-node-api-library]] and
[[changelog-github-adyen-node-api-library]] for exact-SHA evidence and migration.

Release `32.0.0` is a major migration boundary because Checkout v72 removes or changes request fields and introduces Cloud Device API. Future source-page updates must append package-qualified release history. Minor releases should use delta ingest when the classifier and evidence show a bounded change; major or broad upgrades should use additive full ingest without deleting older version knowledge.

### `32.2.0` transport delta

The latest ingested release is `@adyen/api-library@32.2.0`. Its non-proxy
`HttpURLConnectionClient` caches one HTTPS Agent per instance and accepts
constructor `AgentOptions`, including opt-in `keepAlive`. Reuse the merchant
`Client`/HTTP client instance to retain that cache. HTTPS 308 redirects preserve
the request's agent; the existing one-hop and Adyen-host restrictions remain.
The proxy branch still constructs an agent per request.

A changed non-empty certificate path resets the cached agent while retaining
initial agent options. An identical path returns early, so replacing certificate
file contents at that path is not automatically detected by this code. Certificate
loading failures reject the request before sending. The default constructor does
not explicitly enable keep-alive; no latency benchmark was performed. Payments
App sub-merchant boarding-token data is a release-note claim outside the retained
domain model scope. Checkout stays v72 and Node.js stays >=18.

For non-checkout API families, the current capsule supports only service/version inventory unless the retained source covers the queried domain. Detailed questions about those domains should trigger a temporary clone or focused immutable supplement.

## Related

- [[source-github-adyen-node-api-library]] - cumulative exact-SHA repository evidence
- [[changelog-github-adyen-node-api-library]] - package-qualified release history
- [[source-github-adyen-web]] - browser checkout implementation
- [[adyen-ios-sdk]] - native iOS checkout architecture
- [[adyen-android-sdk]] - native Android checkout architecture
- [[adyen-react-native-sdk]] - cross-platform wrapper architecture
- [[adyen]] - company and knowledge-status page
