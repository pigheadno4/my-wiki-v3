---
title: "GitHub: Adyen/adyen-node-api-library"
type: source
date_ingested: 2026-08-02
original_format: github-repo
raw_files:
  - "github/adyen/adyen-node-api-library/snapshots/2026-08-02-99d1a0c/manifest.json"
tags: [adyen, nodejs, typescript, server-sdk, checkout-api, cloud-device-api, github-repository]
---

## Overview

`Adyen/adyen-node-api-library` is Adyen's official Node.js server library for its generated and hand-written API clients. This cumulative page begins with package-qualified release `@adyen/api-library@32.0.0` at exact SHA `99d1a0cf69c8660952baffd1437b00aae2fa4f23`. For checkout-focused queries, the retained baseline provides detailed evidence for Checkout API v72, request transport, classic recurring operations, payment notifications, and Cloud Device API v1.

Repository: <https://github.com/Adyen/adyen-node-api-library>

## Evidence boundary

- The snapshot proves implementation retained at `@adyen/api-library@32.0.0`; it does not prove current merchant eligibility, API credential roles, or payment-method availability.
- The capsule retains 548 packet readings plus the approved six-path notification supplement. Checkout, client transport, Cloud Device, payment, and recurring code receive detailed treatment. Other generated API families are inventory evidence only.
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

The HMAC validator builds the signing payload from the documented payment fields, escapes separators, and compares decoded signatures with a length guard before constant-time comparison. The release notes also record fixes for webhook HMAC validation and discriminator mappings. Only the approved standard-notification supplement is deep evidence here; broader banking and management webhook exports are inventory-level unless their full generated model evidence is collected.

## Broader API inventory

The public service and type barrels also expose classic Payments and Recurring APIs, Management, Legal Entity Management, Balance Platform, Transfers, Payouts, Disputes, Data Protection, BIN Lookup, Stored Value, POS Mobile, Open Banking, and other platform services. This baseline can answer which families are exported and their README-listed versions. Detailed domain queries outside checkout should trigger a temporary clone or a focused source supplement before making implementation-level claims.

## `32.0.0` release finding

The major release combines Checkout API v72 breaking changes with the introduction of Cloud Device API v1. It also adds transfer-domain capabilities and fixes Nexo and webhook HMAC behavior. Transfer changes are retained as release inventory because they are outside the checkout-focused evidence boundary.

Node.js 24 appears in CI tooling updates, while the published package manifest still declares Node.js 18 or newer. It must not be interpreted as a Node.js 24 runtime requirement.

## Related

- [[changelog-github-adyen-node-api-library]] - package-qualified release ledger
- [[adyen-node-api-library]] - server SDK concept and query boundary
- [[source-github-adyen-web]] - browser checkout SDK
- [[source-github-adyen-ios]] - native iOS checkout SDK
- [[source-github-adyen-android]] - native Android checkout SDK
- [[source-github-adyen-react-native]] - cross-platform checkout wrapper
- [[adyen]] - company and knowledge-status page

## Raw sources

- Snapshot manifest: `raw/github/adyen/adyen-node-api-library/snapshots/2026-08-02-99d1a0c/manifest.json`
- Release manifest: `raw/github/adyen/adyen-node-api-library/releases/api-library/32.0.0/2026-08-02/manifest.json`
- Release notes: `raw/github/adyen/adyen-node-api-library/releases/api-library/32.0.0/2026-08-02/release-notes.md`
- README and package: `raw/github/adyen/adyen-node-api-library/snapshots/2026-08-02-99d1a0c/files/README.md` and `package.json`
- Client and transport: `raw/github/adyen/adyen-node-api-library/snapshots/2026-08-02-99d1a0c/files/src/client.ts`, `src/config.ts`, `src/service.ts`, and `src/httpClient/`
- Checkout API: `raw/github/adyen/adyen-node-api-library/snapshots/2026-08-02-99d1a0c/files/src/services/checkout/` and `src/typings/checkout/`
- Cloud Device: `raw/github/adyen/adyen-node-api-library/snapshots/2026-08-02-99d1a0c/files/doc/CloudDeviceApi.md`, `doc/MigratingToCloudDeviceApi.md`, `src/services/clouddevice/`, and `src/security/clouddevice/`
- Notification supplement: `raw/github/adyen/adyen-node-api-library/supplements/2026-08-02-99d1a0c-54d15e5f/manifest.json`
