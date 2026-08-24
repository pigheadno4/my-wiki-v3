---
title: "GitHub: paypal/paypal-php-server-sdk"
type: source
date_ingested: 2026-04-16
date_updated: 2026-08-24
original_format: github-repo
raw_files:
  - "github/paypal/paypal-php-server-sdk/snapshots/2026-08-24-b6be767/manifest.json"
  - "github-paypal-php-server-sdk.md"
tags: [paypal, php, server-sdk, orders, payments, vault, subscriptions, transaction-search, oauth, github-repository]
---

## Overview

`paypal/paypal-php-server-sdk` publishes the official Composer package `paypal/paypal-server-sdk`. The fully read `2.4.0` baseline is pinned to commit `b6be767b759ac3e3ad1d32dde7143a0927f5892b`. It wraps five PayPal REST API families: Orders v2, Payments v2, Payment Method Tokens v3, Transaction Search v1, and Subscriptions v1.

Install the reviewed package with `composer require "paypal/paypal-server-sdk:2.4.0"`. Repository: <https://github.com/paypal/PayPal-PHP-Server-SDK>

## Evidence Boundary

- The exact-SHA capsule contains 689 files totaling 2,641,320 bytes. The approved ingest packet selected 61 key raw files plus the release and snapshot manifests for full serial review.
- This is package-qualified source evidence for `paypal/paypal-server-sdk@2.4.0`. It does not establish current API availability, merchant eligibility, regional enablement, or production account configuration.
- The README labels the Vault controller as US-only. Do not generalize that package statement to every PayPal vault product or geography.
- Generated PayPal, Venmo, card, Apple Pay, Google Pay, and local-payment models prove package type coverage, not buyer eligibility or an enabled merchant capability.
- The `2.4.0` release record has no release notes, and the repository changelog ends at `2.3.0`. This baseline therefore describes the complete retained `2.4.0` surface but does not label individual behaviors as newly introduced in `2.4.0`.
- The Composer metadata declares `MIT`, while the retained `LICENSE` file contains PayPal SDK license terms. This page records that mismatch without offering a legal interpretation.

## Grounding Excerpts

> "This SDK currently contains only 5 of PayPal's API endpoints."
>
> `raw/github/paypal/paypal-php-server-sdk/snapshots/2026-08-24-b6be767/files/README.md:8`

> "Vault Controller: Payment Method Tokens API v3 ... Available in the US only."
>
> `raw/github/paypal/paypal-php-server-sdk/snapshots/2026-08-24-b6be767/files/README.md:14-18`

> `composer require "paypal/paypal-server-sdk:2.4.0"`
>
> `raw/github/paypal/paypal-php-server-sdk/snapshots/2026-08-24-b6be767/files/README.md:20-26`

> "It takes a maximum of three hours for executed transactions to appear"
>
> `raw/github/paypal/paypal-php-server-sdk/snapshots/2026-08-24-b6be767/files/doc/controllers/transaction-search.md:21`

## Package and Client Contract

Package `2.4.0` supports PHP `^7.2 || ^8.0`, requires JSON and cURL extensions, and uses APIMatic core and Unirest dependencies. The generated namespace is `PaypalServerSdkLib`.

`PaypalServerSdkClientBuilder` configures environment, OAuth credentials, timeouts, retries, logging, and proxies. Sandbox is the default environment and timeout defaults to `0`. Automatic retries are disabled by default with zero retries. If enabled, the retained defaults target GET and PUT requests for timeouts and status codes `408`, `413`, `429`, `500`, `502`, `503`, `504`, `521`, `522`, and `524`. Mutation callers must not assume create, capture, or refund operations are automatically retried.

OAuth uses the client-credentials grant and caches the token until expiry, with configurable token-provider and update callbacks. Production maps to `https://api-m.paypal.com`; Sandbox maps to `https://api-m.sandbox.paypal.com`. Unlike the reviewed TypeScript `2.4.0` implementation, the PHP OAuth controller does not explicitly select a named default base URL before requesting `/v1/oauth2/token`; do not transfer that TypeScript-specific delta to PHP.

Logging uses PSR log levels, masks sensitive headers by default, and leaves request/response bodies and headers disabled unless configured. Proxy support is supplied through `ProxyConfigurationBuilder`.

## Controller Surface

| Controller | API | Retained operations |
| --- | --- | --- |
| `OrdersController` | Orders v2 | create, get, patch, confirm, authorize, capture, create tracking, update tracking |
| `PaymentsController` | Payments v2 | get/capture/reauthorize/void authorization; get capture; refund capture; get refund |
| `VaultController` | Payment Method Tokens v3 | create/list/get/delete payment tokens; create/get setup tokens |
| `TransactionSearchController` | Transaction Search v1 | list transactions and balances |
| `SubscriptionsController` | Subscriptions v1 | plan and subscription lifecycle operations |

Controller methods return `ApiResponse`; parsed response models are available through `getResult()`. Error types retain PayPal `debug_id`, details, and HATEOAS links where provided.

## Orders and Payments

Orders covers creation, retrieval, patching, confirmation, authorization, capture, and shipment tracking. Create Order documents `PayPal-Request-Id` keys as retained for six hours, extendable to 72 hours through an account manager, and mandatory for single-step creates that include payment-source information. This endpoint-specific rule must not be generalized to every API call.

The payment-source model includes PayPal, Venmo, cards, Apple Pay, Google Pay, and multiple local methods. Raw card number, CVV, and expiry handling remains a PCI-sensitive server integration; generated model availability is not an eligibility catalog.

Payments supports authorization capture, reauthorization, void, and full or partial refunds. The retained documentation places reauthorization after the three-day honor period and within the 29-day authorization period. Mutation methods document longer request-ID retention than Create Order, reinforcing that idempotency policy is endpoint-specific.

## Vault and Stored Payment Methods

The Vault controller creates setup tokens and payment tokens and lists, retrieves, or deletes customer payment tokens. The payment token ID is server-side state that must be stored for future payments. Its model set includes PayPal, Venmo, Apple Pay, card, and token shapes, but the README still labels this controller US-only.

The presence of `VaultVenmoRequest`, Venmo token, and Venmo vault-response models shows that the generated package can represent those API shapes. It does not independently prove that Venmo vaulting is available to a particular merchant, buyer, integration channel, or deployed PayPal runtime.

## Transaction Search

Transaction Search lists transactions and balances. The retained contract warns of a delay of up to three hours, limits a transaction query to a 31-day range, and covers the preceding three years. Page size defaults to 100 and is capped at 500. Treat this controller as reporting evidence rather than checkout execution.

## Subscriptions

The package exposes a broad Subscriptions API lifecycle:

- Plans: create, list, get, patch, activate, deactivate, and update pricing.
- Subscriptions: create, list, get, patch, revise, suspend, cancel, activate, capture outstanding balances, and list transactions.

Plan filters accept up to 70 plan IDs; subscription filters accept up to 10 vault customer IDs. A plan can contain at most two trial cycles and one regular cycle. Subscription overrides are independent of later plan changes, completed cycles cannot be modified, and PayPal-funded price updates do not affect billing cycles in the next ten days. Revision changes require the buyer-consent flow described by the endpoint contract.

## Version-Qualified History

The repository changelog records `1.0.0` as the GA Orders, Payments, and Vault release; `1.1.0` added Apple Pay and Google Pay models plus proxy support; `2.0.0` added Transaction Search and Subscriptions with breaking model renames; `2.1.0` corrected Transaction Search naming and a shipment-carrier enum; `2.2.0` added subscriber and PayPal vault fields; and `2.3.0` added `processing_instruction` fields and corrected documentation URLs.

Package `2.4.0` is the latest reviewed PHP baseline. Because upstream supplies neither `2.4.0` release notes nor a `2.4.0` changelog entry, no individual retained behavior is attributed specifically to that release. See [[changelog-github-paypal-php-server-sdk]].

## Related

- Company: [[paypal]]
- Checkout: [[paypal-checkout]]
- Vault: [[paypal-vault]]
- Subscriptions: [[paypal-subscriptions]]
- REST schemas: [[source-github-paypal-rest-api-specifications]]
- TypeScript server SDK: [[source-github-paypal-typescript-server-sdk]]
- Payouts PHP SDK: [[source-github-paypal-payouts-php-sdk]]

## Raw Sources

- `raw/github/paypal/paypal-php-server-sdk/snapshots/2026-08-24-b6be767/manifest.json` - 689-file exact-SHA `2.4.0` source capsule.
- `raw/github/paypal/paypal-php-server-sdk/releases/paypal-server-sdk/2.4.0/2026-08-24/manifest.json` - package-qualified release identity and date.
- `raw/github/paypal/paypal-php-server-sdk/snapshots/2026-08-24-b6be767/files/README.md` - package scope, installation, environments, and configuration.
- `raw/github/paypal/paypal-php-server-sdk/snapshots/2026-08-24-b6be767/files/doc/controllers/` - generated controller contracts.
- `raw/github/paypal/paypal-php-server-sdk/snapshots/2026-08-24-b6be767/files/src/` - client, authentication, HTTP, logging, errors, and generated models.
- `raw/github-paypal-php-server-sdk.md` - legacy collection stub preserved as historical raw evidence.
