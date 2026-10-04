---
title: "GitHub: Adyen/adyen-node-api-library"
type: source
date_ingested: 2026-10-04
original_format: github-repo
raw_files:
  - "github/adyen/adyen-node-api-library/snapshots/2026-10-04-134f500/manifest.json"
  - "github/adyen/adyen-node-api-library/snapshots/2026-10-04-afd3bb4/manifest.json"
  - "github/adyen/adyen-node-api-library/snapshots/2026-08-02-99d1a0c/manifest.json"
tags: [adyen, nodejs, typescript, server-sdk, checkout-api, cloud-device-api, github-repository]
---

## Overview

`Adyen/adyen-node-api-library` is Adyen's official Node.js server library for its generated and hand-written API clients. This cumulative page begins with package-qualified release `@adyen/api-library@32.0.0` at exact SHA `99d1a0cf69c8660952baffd1437b00aae2fa4f23`. For checkout-focused queries, the retained baseline provides detailed evidence for Checkout API v72, request transport, classic recurring operations, payment notifications, and Cloud Device API v1.

Repository: <https://github.com/Adyen/adyen-node-api-library>

Latest ingested update: `@adyen/api-library@32.2.0` at
`134f50078ca8889ff21e6c76f71c6377ddcb2120`. The original `32.0.0` architecture
and migration sections remain historical evidence, not replaced by this update.

## Evidence boundary

- The snapshots prove version-qualified retained implementation, not current merchant eligibility, API credential roles, or payment-method availability.
- The `32.0.0` capsule has 548 packet readings plus the approved six-path notification supplement. The `32.1.0` snapshot retains 566 files; approved focused reading covers all 103 added/modified retained files, removed paths and affected prior code, with unchanged inventory verified by hash. This is not a claim to read every unchanged file again or the entire upstream repository.
- The README and export barrels list broader services and webhook handlers whose full model trees were not retained. Queries requiring those implementation details must recollect the repository or the relevant delegated specification.
- This is server-library evidence. Shopper UI behavior remains in the independently versioned Web, iOS, Android, and React Native SDK histories.

## Grounding excerpts

> "Our latest integration for accepting online payments."
>
> `raw/github/adyen/adyen-node-api-library/snapshots/2026-08-02-99d1a0c/files/README.md:21`

> "The Cloud device API (`CloudDeviceAPI`) is generated from the [Cloud device API OpenAPI specification](https://github.com/Adyen/adyen-openapi/blob/main/yaml/CloudDeviceService-v1.yaml)"
>
> `raw/github/adyen/adyen-node-api-library/snapshots/2026-08-02-99d1a0c/files/doc/MigratingToCloudDeviceApi.md:7`

> "new In-Person Payments features and products are released exclusively on the Cloud device API."
>
> `raw/github/adyen/adyen-node-api-library/snapshots/2026-08-02-99d1a0c/files/doc/MigratingToCloudDeviceApi.md:19`

> "Consumers must always provide this field."
>
> `raw/github/adyen/adyen-node-api-library/releases/api-library/32.0.0/2026-08-02/release-notes.md:13`

> "Distinguishable errors would reintroduce a CBC padding-oracle side channel."
>
> `raw/github/adyen/adyen-node-api-library/snapshots/2026-08-02-99d1a0c/files/src/security/clouddevice/nexoSecurityManager.ts:82-84`

## Package and client setup

The package is `@adyen/api-library@32.0.0`, requires Node.js 18 or newer, publishes CommonJS JavaScript with TypeScript declarations, and is MIT licensed. A merchant constructs `Config` with an environment and API key or basic credentials, then creates `Client` and the required service family. Configuration also supports request and connection timeouts, application identity, proxy settings, certificate options, a live endpoint prefix, a Terminal API endpoint, region selection, and 308 redirect control.

The client chooses test or live Terminal endpoints and applies regional routing when configured. Generated services serialize request models, issue HTTP requests through a `Resource`, and deserialize typed responses. A merchant may replace the HTTP client, but then owns required headers, authentication, timeout, and response behavior.

## Transport and operational behavior

The default HTTP client supports API-key and basic authentication, custom headers, query parameters, proxying, per-request timeout, and an `idempotencyKey` option promoted to the `Idempotency-Key` header. It identifies the library and optional merchant application in request headers.

HTTP failures preserve status, headers, body, and parsed Adyen error fields when available. A 308 redirect is followed at most once and only when the target host remains under `.adyen.com` or `.adyenpayments.com`. Certificate verification can be configured, but disabling verification with the `unencrypted` certificate mode removes a transport safeguard and should not be treated as a production default.

## Checkout API v72

`CheckoutAPI` exposes seven endpoint groups:

| Group | Retained operations |
| --- | --- |
| Payments | payment methods, payments, payment details, sessions, session result, and card details |
| Modifications | cancel, capture, refund, reversal, and authorization amount update |
| Orders | create, cancel, and balance check |
| Payment links | create, retrieve, and update status |
| Recurring | create, list, and delete stored payment methods, plus forward requests |
| Donations | list campaigns and submit donations |
| Utility | Apple Pay session, PayPal order update, shopper validation, and deprecated origin keys |

The generated Checkout model set covers payment-method details, stored methods, sessions, payment responses and actions, 3D Secure data, orders, links, recurring contracts, and modification requests. Model presence proves a typed server contract, not that a method is enabled or will be returned for a merchant.

The response `resultCode` and follow-up `action` remain server response data. Integrations should preserve the payment reference and continue any action/details flow before treating the payment as final.

## Checkout v72 migration boundary

Release `32.0.0` upgrades Checkout API to v72 and introduces breaking model changes:

- `DirectDebitAuDetails.holderName` becomes required.
- `donationType` becomes optional and deprecated in favor of `type`.
- `DonationPaymentRequest` removes `additionalData`, `conversionId`, `deliverAt`, and `threeDSAuthenticationOnly`; the authentication-only replacement is `authenticationData.authenticationOnly`.
- `PaymentAmountUpdateRequest` and `StandalonePaymentCancelRequest` remove `enhancedSchemeData`; amount updates use `mpiData` instead.
- `PaymentRequest.conversionId` is removed in favor of `checkoutAttemptId`.

Authorization amount updates add `adjustAuthType` for cardholder-initiated or merchant-initiated transactions, `adjustAuthorisationData` for synchronous adjustments, and `mpiData`. These are typed request capabilities and do not independently establish an authorization policy or recurring-payment entitlement.

## Cloud Device API v1

Cloud Device API is the first-class cloud integration for sending Terminal API messages. Its synchronous and asynchronous methods require `merchantAccount` and `deviceId`; the message header `POIID` should match the device ID. It also exposes connected-device listing and device-status lookup. Live integrations must configure the region nearest their terminals and require the Cloud Device API credential role.

The generated `tapi` models differ from legacy hand-written `terminal` models. Migration changes include dropped `Type` suffixes on many enums, renamed model classes, `Date` timestamp fields, standalone enums, several string-to-number conversions, some arrays becoming scalar values, property renames, and a wrapped asynchronous response. Legacy Terminal cloud remains functional in this baseline, but new cloud integrations are directed to Cloud Device API.

`EncryptedCloudDeviceApi` encrypts and decrypts the Terminal message payload using configured credential metadata. The implementation derives key material, uses AES-256-CBC, authenticates plaintext with HMAC-SHA256, checks nonce length, validates key metadata, and emits one generic decryption failure before metadata diagnostics to avoid distinguishable cryptographic failure paths. Unencrypted responses claiming a successful or partial terminal outcome are rejected.

## Notifications and HMAC

The retained notification handler parses standard payment notifications into `notificationItems`. Each item carries event code, amount, PSP reference, merchant reference, event date, merchant account, outcome, and optional operations or original reference. `AUTHORISATION` alone is not success; the item-level `success` field is also required.

The HMAC validator builds the standard-notification signing payload from payment fields. Its separate map-payload branch escapes backslashes and colons; do not generalize that escaping to every branch. Decoded signatures are compared with a length guard before constant-time comparison. The `32.0.0` release notes record webhook HMAC and discriminator fixes. Standard-notification models are covered by the approved baseline supplement and, unchanged, the `32.1.0` capsule; broader banking and management webhook exports remain inventory-level unless their full generated model evidence is collected.

## Broader API inventory

The public service and type barrels also expose classic Payments and Recurring APIs, Management, Legal Entity Management, Balance Platform, Transfers, Payouts, Disputes, Data Protection, BIN Lookup, Stored Value, POS Mobile, Open Banking, and other platform services. This baseline can answer which families are exported and their README-listed versions. Detailed domain queries outside checkout should trigger a temporary clone or a focused source supplement before making implementation-level claims.

## `32.0.0` release finding

The major release combines Checkout API v72 breaking changes with the introduction of Cloud Device API v1. It also adds transfer-domain capabilities and fixes Nexo and webhook HMAC behavior. Transfer changes are retained as release inventory because they are outside the checkout-focused evidence boundary.

Node.js 24 appears in CI tooling updates, while the published package manifest still declares Node.js 18 or newer. It must not be interpreted as a Node.js 24 runtime requirement.

## `32.1.0` additive full update (2026-09-03)

This release retains Checkout API v72 and the Node.js >=18 runtime declaration.
It was ingested as additive full because capsule policy, public model compatibility
and security-related dependencies changed; focused reading was explicitly approved.

### Grounding excerpts

> "When you set this to **true**, you can no longer update the session."
>
> `raw/github/adyen/adyen-node-api-library/snapshots/2026-10-04-afd3bb4/files/src/typings/checkout/checkoutSessionPatchSessionRequest.ts:16`

> "The encoded payment session data from the `beforeSubmit` callback"
>
> Same snapshot, `src/typings/checkout/checkoutSessionPatchSessionRequest.ts:20`.

> "static readonly mapping: {[index: string]: string} | undefined = {"
>
> Same snapshot, `src/typings/checkout/paymentRequestPaymentMethod.ts:93`.

> "Identifier for the third-party token request template configured in your Adyen account."
>
> Same snapshot, `src/typings/checkout/thirdPartyTokenRedundancyInfo.ts:17`.

> "endpoint: string, json: string | Buffer, config: Config, isApiKeyRequired: boolean, requestOptions?: IRequest.Options,"
>
> Same snapshot, `src/httpClient/clientInterface.ts:25`.

### Sessions amount-update lifecycle

`PaymentsApi.updateSession(sessionId, request, requestOptions?)` serializes a
`CheckoutSessionPatchSessionRequest`, encodes the session ID and sends
`PATCH /sessions/{sessionId}`. Required fields are `amount` (currency and integer
minor-unit value) and `sessionData` obtained from Drop-in/Component `beforeSubmit`.
Optional `payable: true` marks the final amount payable and prevents further
updates; `false` requires another update setting it to `true` before submission.
The typed response's `sessionData` is optional, not guaranteed to be returned.

Integration implication: calculate the final amount from a trusted server order,
then update the session with client callback data. This is an integration outline,
not tested client code; exact callback continuation belongs to independently
versioned Web SDK evidence. A successful session update is not payment success.

### Checkout model and serializer changes

- Payment-request, donation-method and payment-action union classes now define
  concrete discriminator mappings. `ObjectSerializer.findCorrectType` resolves
  a recognized `type` to its mapped class, whose attribute map controls serialization
  and deserialization; unknown/missing discriminators retain fallback behavior.
  The resolver existed before this release; the generated mappings are the change.
- New `AuPayDetails` (`aupay`), `DBaraiDetails` (`dbarai`) and
  `SepaDirectDebitDonations` models extend typed payment/donation coverage, not
  merchant enablement. SEPA debit IBAN and owner name become optional in the types;
  this does not prove the server permits arbitrary missing bank details.
- `EnhancedSchemeData` gains car-rental, healthcare, lodging and temporary-services
  branches. Car rental requires `renterName`; healthcare requires
  `totalHealthcareValue`. Generated constructors are not runtime business validators.
- `thirdPartyTokenRedundancyInfo` is added to payment and create-session request/
  response models. It requires an account-configured `requestTemplateCode`;
  optional `requestParameters` keys must match template placeholders.
- `CreateCheckoutSessionRequest.shopperConversionId` links requests for conversion
  insights, not shopper identity or request idempotency. Line items gain shipping
  and return tracking fields. Stored methods gain `externalToken`; Affirm gains
  `financingProgram`; Klarna/Riverty gain base64 `merchantData`; CardBrand gains
  a healthcare/FSA/HSA indicator; donation campaigns gain `label`.
- `PaypalUpdateOrderRequest` adds optional nullable `deliveryAddress`,
  `shippingAmount` and `discountAmount`. Existing `paymentData` changes after each
  update; preserve the appropriate current data/session or PSP-reference context.
- Checkout removes `DefaultErrorResponseEntity` and `InvalidField` exports;
  `CheckoutErrorResponseEntity` has required `errorCode`, `errorType`, `message`
  and optional status/PSP reference. This does not change every thrown HTTP exception
  into that model. `PaymentDetails.TypeEnum.Paybright` is removed and
  `gopay_wallet` maps to stored-method details rather than generic payment details.
- Classic Payments API v68 adds `transactionLinkId` in request/response additional
  data for Mastercard transaction-link references in qualifying recurring/card-on-file
  flows when Adyen does not tokenize. This is not a Checkout field or blanket
  replacement for the still-present `networkTxReference`.

### Transport, dependencies and evidence limits

The client interface, resource and JSON helper accept `string | Buffer`. The
helper passes strings/Buffers through instead of JSON-stringifying Buffers.
The HTTP client preserves caller-supplied Content-Type case-insensitively and
defaults to JSON only when absent. Custom clients must handle both payload kinds;
the README's JSON-only Axios example is not proof of multipart compatibility.

The new `requestForm` helper builds multipart or URL-encoded bodies, removes
stale content-type/length headers, supplies form headers and correct byte length,
and buffers multipart bodies via `getBuffer` rather than streaming them.
Runtime dependency `form-data` is 4.0.6; `micromatch` override is ^4.0.8. Other
security/transitive updates in release notes remain announcement-level because
the lockfile is excluded; no vulnerability audit or SDK execution was performed.

Document Collector API v1 exports multipart `DocumentsApi.uploadCrossBorderInvoice`
with non-null checks for context, file and merchant account. The complete
`HttpFile`/DocumentContext/domain model set is not retained, so exact supported
uploads, roles and broader document lifecycle remain evidence gaps. Session
Authentication is also exported but inventory-only. Cloud Device docs add an
`additionalData.captureDelayHours` example, not a new terminal endpoint.

Five newly retained standard-notification types match the older supplement by
hash; this is capsule coverage, not new upstream notification behavior. Removal
of banking/management handlers from this snapshot is likewise selection policy,
not proof their upstream APIs were removed. Two removed Checkout model paths
move into excluded Document Collector scope; patch rename similarity to an
unrelated new Session model is not a semantic migration instruction.

The README corrects generic-webhook HMAC usage to `new hmacValidator()` and
`validateHMACSignature(hmacKey, hmacSignature, jsonString)`. The validator code
itself is unchanged; this is a documentation correction, not a new algorithm.

## `32.2.0` delta update (2026-09-24)

Three retained files change: VERSION, package.json and the default HTTP client;
563 retained files are unchanged and verified mechanically. Checkout remains
v72, Node.js remains >=18 and package dependencies are unchanged from `32.1.0`.

### Grounding excerpts

> "public constructor(agentOptions: AgentOptions = {}) {"
>
> `raw/github/adyen/adyen-node-api-library/snapshots/2026-10-04-134f500/files/src/httpClient/httpURLConnectionClient.ts:45`

> "this.agent ??= new Agent(this.agentOptions);"
>
> Same snapshot, `src/httpClient/httpURLConnectionClient.ts:137`.

> "if (this.certificatePath === terminalCertificatePath) {"
>
> Same snapshot, `src/httpClient/httpURLConnectionClient.ts:295`.

### Agent reuse and integration implications

Previously, the non-proxy branch constructed a new HTTPS Agent for each request.
Now it lazily caches one per `HttpURLConnectionClient` instance. Its new constructor
copies optional `AgentOptions`, allowing explicit `keepAlive: true` and other
HTTPS agent settings. `Client.httpClient` already caches its HTTP client instance;
reuse the merchant Client/HTTP client instead of recreating it for each API call.
Agent reuse is not proof keep-alive is enabled: the default options are `{}`.
No runtime benchmark or network/payment test was performed.

The request agent is carried into `doRequest` and supplied to HTTPS redirects;
HTTP redirects do not receive that HTTPS agent. The existing trusted-host check
and single-308-hop limit remain. The proxy branch still creates a new
`HttpsProxyAgent` per request, so the non-proxy caching claim does not cover it.

`installCertificateVerifier` returns early for the same certificate-path string.
A different non-empty path rebuilds options from the initial constructor options
plus the selected certificate configuration and invalidates the cached agent.
The `unencrypted` mode still disables verification and is not a secure production
default. File-read failures now throw internally and become rejected request
promises before sending. Replacing file contents at an unchanged path is not
detected by this cache; do not infer automatic certificate rotation or reset
on an absent certificate-path option.

### Payments App inventory and release provenance

The release notes announce `BoardingTokenRequest.subMerchantData` with
`SubMerchantData` identity, contact and address details. The corresponding
Payments App models are explicitly excluded by the checkout-focused capsule,
so this is notes-level inventory, not validated field definitions or eligibility.
The notes' Full Changelog URL ends in `HEAD`; exact update claims here use the
stored `32.1.0` -> `32.2.0` SHA comparison, not the mutable branch boundary.

## Related

- [[changelog-github-adyen-node-api-library]] - package-qualified release ledger
- [[adyen-node-api-library]] - server SDK concept and query boundary
- [[source-github-adyen-web]] - browser checkout SDK
- [[source-github-adyen-ios]] - native iOS checkout SDK
- [[source-github-adyen-android]] - native Android checkout SDK
- [[source-github-adyen-react-native]] - cross-platform checkout wrapper
- [[adyen]] - company and knowledge-status page

## Raw sources

- `32.2.0` snapshot: `raw/github/adyen/adyen-node-api-library/snapshots/2026-10-04-134f500/manifest.json`
- `32.2.0` release manifest: `raw/github/adyen/adyen-node-api-library/releases/api-library/32.2.0/2026-10-04/manifest.json`
- `32.2.0` notes: `raw/github/adyen/adyen-node-api-library/releases/api-library/32.2.0/2026-10-04/release-notes.md`
- Transport: `raw/github/adyen/adyen-node-api-library/snapshots/2026-10-04-134f500/files/src/httpClient/httpURLConnectionClient.ts`
- Version/package: `raw/github/adyen/adyen-node-api-library/snapshots/2026-10-04-134f500/files/VERSION` and `package.json`
- `32.1.0` -> `32.2.0`: `tracking/github/repos/adyen/adyen-node-api-library/comparisons/api-library/32.1.0--32.2.0/comparison.json`, `comparison.md` and `diff.patch`

- `32.1.0` snapshot: `raw/github/adyen/adyen-node-api-library/snapshots/2026-10-04-afd3bb4/manifest.json`
- `32.1.0` release: `raw/github/adyen/adyen-node-api-library/releases/api-library/32.1.0/2026-10-04/manifest.json` and `release-notes.md`
- `32.0.0` -> `32.1.0` comparison: `tracking/github/repos/adyen/adyen-node-api-library/comparisons/api-library/32.0.0--32.1.0/comparison.json`, `comparison.md` and `diff.patch`
- Session update: `raw/github/adyen/adyen-node-api-library/snapshots/2026-10-04-afd3bb4/files/src/services/checkout/paymentsApi.ts` and `src/typings/checkout/checkoutSessionPatchSessionRequest.ts`, `checkoutSessionPatchSessionResponse.ts`, `sessionAmountUpdate.ts`
- Model/serialization evidence: `raw/github/adyen/adyen-node-api-library/snapshots/2026-10-04-afd3bb4/files/src/typings/checkout/` and `src/typings/payment/additionalDataCommon.ts`, `responseAdditionalDataCommon.ts`
- Transport evidence: `raw/github/adyen/adyen-node-api-library/snapshots/2026-10-04-afd3bb4/files/src/httpClient/`, `src/helpers/requestForm.ts`, `src/helpers/getJsonResponse.ts`, `src/services/resource.ts` and `package.json`

- Snapshot manifest: `raw/github/adyen/adyen-node-api-library/snapshots/2026-08-02-99d1a0c/manifest.json`
- Release manifest: `raw/github/adyen/adyen-node-api-library/releases/api-library/32.0.0/2026-08-02/manifest.json`
- Release notes: `raw/github/adyen/adyen-node-api-library/releases/api-library/32.0.0/2026-08-02/release-notes.md`
- README and package: `raw/github/adyen/adyen-node-api-library/snapshots/2026-08-02-99d1a0c/files/README.md` and `package.json`
- Client and transport: `raw/github/adyen/adyen-node-api-library/snapshots/2026-08-02-99d1a0c/files/src/client.ts`, `src/config.ts`, `src/service.ts`, and `src/httpClient/`
- Checkout API: `raw/github/adyen/adyen-node-api-library/snapshots/2026-08-02-99d1a0c/files/src/services/checkout/` and `src/typings/checkout/`
- Cloud Device: `raw/github/adyen/adyen-node-api-library/snapshots/2026-08-02-99d1a0c/files/doc/CloudDeviceApi.md`, `doc/MigratingToCloudDeviceApi.md`, `src/services/clouddevice/`, and `src/security/clouddevice/`
- Notification supplement: `raw/github/adyen/adyen-node-api-library/supplements/2026-08-02-99d1a0c-54d15e5f/manifest.json`
