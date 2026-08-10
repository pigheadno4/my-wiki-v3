---
title: "GitHub: paypal/paypal-typescript-server-sdk"
type: source
date_ingested: 2026-04-16
date_updated: 2026-08-10
original_format: github-repo
raw_files:
  - "github/paypal/paypal-typescript-server-sdk/snapshots/2026-08-10-dbdbdd0/manifest.json"
  - "github/paypal/paypal-typescript-server-sdk/snapshots/2026-08-10-b37cec5/manifest.json"
  - "github-paypal-ts-server-sdk.md"
tags: [paypal, typescript, server-sdk, orders, payments, vault, subscriptions, transaction-search, oauth, github-repository]
---

## Overview

`paypal/paypal-typescript-server-sdk` publishes the official `@paypal/paypal-server-sdk` package for Node.js. The fully read `2.3.0` baseline is pinned to commit `b37cec58f2cdeecf5b9b7a7c15131cc5f4fff712`; the reviewed `2.4.0` delta is pinned to `dbdbdd06f18a06d633c66bbc27d7d7a54283e1a3`. The package wraps five PayPal REST API families: Orders v2, Payments v2, Payment Method Tokens v3, Transaction Search v1, and Subscriptions v1.

Install the latest reviewed package with `npm install @paypal/paypal-server-sdk@2.4.0`. Repository: <https://github.com/paypal/PayPal-TypeScript-Server-SDK>

## Evidence Boundary

- The `2.3.0` baseline retains 396 policy-selected files totaling 911,587 bytes. The `2.4.0` delta capsule retains 397 files totaling 924,075 bytes and was compared directly with that baseline.
- This is package-qualified `2.3.0` and `2.4.0` source evidence. It does not establish current API availability, merchant eligibility, regional enablement, or production configuration.
- The README labels the Vault controller as US-only. Do not generalize that package statement to every PayPal vault product or geography without current product documentation.
- The `2.4.0` release record has no release notes. Its repository changelog now attributes `2.3.0` to a fix for differences between ESM and CommonJS builds, but does not state which changes constitute the `2.4.0` release. Exact `2.4.0` findings below therefore come from the retained source comparison.
- Generated model presence proves a typed request or response shape in this package. It does not prove that a payment method is enabled for a merchant or available to a buyer.

## Grounding Excerpts

> "This SDK currently contains only 5 of PayPal's API endpoints."
>
> `raw/github/paypal/paypal-typescript-server-sdk/snapshots/2026-08-10-b37cec5/files/README.md:8`

> "The PayPal Server SDK provides integration access to the PayPal REST APIs."
>
> `raw/github/paypal/paypal-typescript-server-sdk/snapshots/2026-08-10-b37cec5/files/README.md:12-18`

> "Use the `/orders` resource to create, update, retrieve, authorize, capture and track orders."
>
> `raw/github/paypal/paypal-typescript-server-sdk/snapshots/2026-08-10-b37cec5/files/doc/controllers/orders.md:3-22`

> "Passing card number, cvv and expiry directly via the API requires PCI SAQ D compliance."
>
> `raw/github/paypal/paypal-typescript-server-sdk/snapshots/2026-08-10-b37cec5/files/src/models/paymentSource.ts:57-60`

> "maxNumberOfRetries: 0"
>
> `raw/github/paypal/paypal-typescript-server-sdk/snapshots/2026-08-10-b37cec5/files/src/defaultConfiguration.ts:21-30`

## Package and Client Contract

Package `2.3.0` supports Node.js `>=14.17.0` and publishes CommonJS and ESM entry points with TypeScript declarations. It is generated with APIMATIC and depends on APIMATIC authentication, OAuth, Axios, core, and schema adapters.

The `Client` supports code-based configuration, JSON configuration, and environment-variable configuration. Authentication uses OAuth 2 client credentials. The default environment is Sandbox, the request timeout default is `0`, and automatic retries are disabled by default with `maxNumberOfRetries: 0`. The retained retry policy, when enabled, targets GET and PUT requests for timeout and selected 4xx/5xx statuses; callers must not assume create or capture calls are automatically retried.

All controller calls return `Promise<ApiResponse<T>>`; the parsed value is exposed as `response.result`. Optional request metadata includes `PayPal-Request-Id`, `PayPal-Partner-Attribution-Id`, `PayPal-Client-Metadata-Id`, `PayPal-Auth-Assertion`, sandbox mock-response headers, and `Prefer` response selection where supported.

## Controller Surface

| Controller | API | Retained `2.3.0` operations |
| --- | --- | --- |
| `OrdersController` | Orders v2 | create, get, patch, confirm, authorize, capture, create tracking, update tracking |
| `PaymentsController` | Payments v2 | get/capture/reauthorize/void authorization; get capture; refund capture; get refund |
| `VaultController` | Payment Method Tokens v3 | create/list/get/delete payment tokens; create/get setup tokens |
| `TransactionSearchController` | Transaction Search v1 | list transactions and balances |
| `SubscriptionsController` | Subscriptions v1 | product, plan, and subscription lifecycle operations |

Orders methods expose partner and risk headers directly. Create Order documents `PayPal-Request-Id` as mandatory for single-step creates that include a payment source, while capture and payment operations have their own idempotency retention descriptions. Callers should follow the endpoint-specific contract instead of treating one retention period as universal.

The Payments controller covers authorization retrieval, capture, reauthorization, void, capture retrieval, refunds, and refund retrieval. The Subscriptions controller exposes product and plan creation/retrieval/update plus plan activation, deactivation, and pricing updates; subscription operations include create, list, get, patch, revise, suspend, cancel, activate, capture, and transaction listing.

Transaction Search is reporting evidence rather than checkout execution. Its retained documentation warns that transactions can take up to three hours to appear, limits a request to a 31-day range, and supports the preceding three years.

## Checkout and Payment Sources

The `PaymentSource` model includes card, token, PayPal, Venmo, Apple Pay, Google Pay, Bancontact, BLIK, EPS, Giropay, iDEAL, MyBank, P24, Sofort, and Trustly request branches. These are typed Orders API inputs, not an eligibility catalog.

Passing raw card number, CVV, and expiry through the API requires PCI SAQ D compliance; the model points merchants to hosted fields to avoid handling those values directly. Payment-source-specific `experience_context` models carry buyer-return and presentation settings. Several retained models mark top-level `application_context` fields as deprecated in favor of the applicable payment source's `experience_context`.

The Orders request surface includes Venmo payment and vault-related models, and the Vault model set includes PayPal, Venmo, Apple Pay, card, bank, and token shapes. This confirms server-side type coverage in `2.3.0`; it does not supersede current Venmo or Vault product eligibility rules.

## Subscription Surface

The package contains a broad Subscriptions API lifecycle, not only subscription creation. Plan operations cover create, list, get, patch, activate, deactivate, and pricing updates. Subscription operations cover create, list, get, patch, revise, suspend, cancel, activate, outstanding-balance capture, and transaction listing.

Billing models support trial and regular cycles, pricing schemes, payment preferences, merchant preferences, taxes, quantity support, and subscription-level cycle overrides. A plan can have at most two trial cycles and one regular cycle. Card-funded subscription models retain a package comment that merchants must sign up for PayPal Complete Payments and that only non-3DS cards and US/Australia merchants are supported; verify this against current product documentation before using it as sales or implementation guidance.

## Version-Qualified History

### `2.4.0` delta

- Adds the public `ProcessingInstruction` enum with `ORDER_COMPLETE_ON_PAYMENT_APPROVAL`. Optional `processingInstruction` fields are exposed on create- and confirm-order requests and returned Order/authorization models. This proves typed Orders API support for the instruction; it does not establish eligibility for every payment source.
- The OAuth token controller now explicitly selects the `default` base URL before calling `/v1/oauth2/token`, preventing an alternate API-server selection from leaking into token acquisition.
- Generated controller documentation now states OAuth requirements and successful HTTP response semantics. Many response fields are newly marked read-only and relative PayPal documentation links are normalized to absolute URLs. These are contract/documentation clarifications, not new payment-method availability.
- Package and README references advance from `2.3.0` to `2.4.0`. No upstream `2.4.0` release notes were available in the collected release record.

The retained repository changelog records `1.0.0` as the GA Orders, Payments, and Vault release; `1.1.0` added Apple Pay and Google Pay models; `2.0.0` added Transaction Search and Subscriptions with breaking model renames; `2.1.0` fixed Transaction Search naming and a shipment-carrier enum; `2.2.0` added missing subscriber and PayPal vault fields; and `2.3.0` fixed ESM/CommonJS build differences. Package `2.3.0` remains the full baseline and `2.4.0` is the latest reviewed delta.

See [[changelog-github-paypal-typescript-server-sdk]] for the release ledger and future deltas.

## Related

- Company: [[paypal]]
- Checkout: [[paypal-checkout]]
- Vault: [[paypal-vault]]
- Subscriptions: [[paypal-subscriptions]]
- REST schemas: [[source-github-paypal-rest-api-specs]]
- PHP server SDK: [[source-github-paypal-php-server-sdk]]

## Raw Sources

- `raw/github/paypal/paypal-typescript-server-sdk/snapshots/2026-08-10-dbdbdd0/manifest.json` - 397-file exact-SHA `2.4.0` source capsule.
- `raw/github/paypal/paypal-typescript-server-sdk/releases/paypal-server-sdk/2.4.0/2026-08-10/manifest.json` - package-qualified `2.4.0` release identity and release date.
- `tracking/github/repos/paypal/paypal-typescript-server-sdk/comparisons/paypal-server-sdk/2.3.0--2.4.0/` - deterministic comparison artifacts.
- `raw/github/paypal/paypal-typescript-server-sdk/snapshots/2026-08-10-b37cec5/manifest.json` - 396-file exact-SHA `2.3.0` source capsule.
- `raw/github/paypal/paypal-typescript-server-sdk/releases/paypal-server-sdk/2.3.0/2026-08-10/manifest.json` - package-qualified release identity and release date.
- `raw/github/paypal/paypal-typescript-server-sdk/snapshots/2026-08-10-b37cec5/files/README.md` - package scope, installation, initialization, environments, and authentication.
- `raw/github/paypal/paypal-typescript-server-sdk/snapshots/2026-08-10-b37cec5/files/doc/controllers/` - generated controller contracts.
- `raw/github/paypal/paypal-typescript-server-sdk/snapshots/2026-08-10-b37cec5/files/src/models/` - generated request and response model surface.
- `raw/github-paypal-ts-server-sdk.md` - legacy collection stub preserved as historical raw evidence.
