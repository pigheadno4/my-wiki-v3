---
title: "GitHub: braintree/braintree_node"
type: source
date_ingested: 2026-08-09
original_format: github-repo
raw_files:
  - "github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/manifest.json"
tags: [braintree, node-js-sdk, server-sdk, checkout, paypal, venmo, subscriptions, webhooks, github-repository]
---

## Overview

`braintree/braintree_node` is Braintree's Node.js server SDK. The retained history begins with `braintree@3.39.0` at exact SHA `7a9270aaf31eb87819add64a768652243f90007c`, released on 2026-08-06.

Repository: <https://github.com/braintree/braintree_node>

## Evidence Boundary

- This source proves implementation present in `braintree@3.39.0`; it does not replace current Braintree product documentation or prove merchant, buyer, country, currency, or payment-method eligibility.
- The SDK performs server-side gateway operations. Browser and native SDKs independently collect payment details and return payment-method nonces or tokens to the merchant server.
- PayPal customer sessions are marked as available only to authorized merchants. Recommendation types and app-installed inputs do not establish general PayPal or Venmo availability.
- The repository's release record contains no upstream release-note body. Exact `3.39.0` changes therefore come from the retained repository changelog and source.
- Checkout, vault, subscriptions, webhooks, and payment-method processing receive detailed treatment. Disputes, OAuth, onboarding, reporting, disbursement, and facilitator features are retained as inventory-level evidence for rough queries and can be recollected at greater depth if needed.

## Grounding Excerpts

> "The Braintree Node library provides integration access to the Braintree Gateway."
>
> `raw/github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/files/README.md:3`

> "Almost all methods that uses a callback can alternatively use a Promise."
>
> `raw/github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/files/README.md:103`

> "This feature is available to authorized merchants."
>
> `raw/github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/files/lib/braintree/customer_session_gateway.js:18-20`

> "The Venmo SDK integration is Unsupported. Please update your integration to use Pay with Venmo instead"
>
> `raw/github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/files/lib/braintree/transaction_gateway.js:722-725`

## Server Integration Model

The merchant creates a `BraintreeGateway` with Sandbox or Production credentials. Configuration supports merchant ID plus public/private keys, an access token, or OAuth client credentials. Credentials encode their environment, and mismatched environments are rejected. The retained package requires Node.js 10 or later and supports callbacks or promises for almost all methods; searches and `merchantAccount.all` return streams when no callback is supplied.

The gateway exposes transaction, client-token, customer, payment-method, payment-method-nonce, verification, PayPal account and payment-resource, plan, subscription, webhook, local-payment, SEPA, and US-bank operations. It also exposes disputes, document upload, merchant/OAuth, settlement reporting, disbursement, and exchange-rate services.

HTTP transport uses Braintree's REST API version 6 and a dated GraphQL API version. A `422` response is converted into a structured unsuccessful API result with nested validation errors; authentication, authorization, not-found, timeout, rate-limit, server, and availability statuses reject with typed exceptions.

## Client Tokens and Vaulting

`clientToken.generate()` defaults to token version 2. A customer ID is required when options request duplicate-payment-method checks, default-method assignment, or card verification. At `3.39.0`, `preferredPaymentMethodToken` is accepted and mapped to the gateway's payment-method identifier, enabling client experiences that need a preferred vaulted method.

Customer records can aggregate cards, PayPal accounts, Venmo accounts, Apple Pay, Android Pay, SEPA, and US bank accounts. The payment-method gateway can create, find, update, delete, grant, and revoke methods. The nonce gateway can create a new nonce from a vaulted token and retrieve nonce details. A nonce is a server-processing input, not a durable payment credential by itself.

## Transaction Lifecycle

`transaction.sale()` accepts a payment-method nonce or token, amount, customer and address data, merchant account, risk and descriptor data, 3DS fields, line items, and processing options. Setting `options.submitForSettlement` requests authorization and settlement submission in one call; otherwise the merchant can submit later.

The lifecycle includes sale and authorization, submit for settlement, partial settlement with optional final capture, authorization adjustment, package tracking, void, refund, and transaction-detail updates. Status values include authorized, submitted for settlement, settling, settled, voided, gateway rejected, processor declined, and failed.

Since `3.37.0`, `apiRequestKey` provides idempotency support for sale, credit, settlement submission, partial settlement, void, and refund. Validation codes distinguish request-key reuse, concurrent processing, prior failure, excessive length, and operations where the key is not allowed. The SDK also supports partial authorization and records whether a transaction was partially authorized.

## PayPal and Venmo

PayPal account operations can find, update, and delete vaulted accounts. PayPal payment-resource updates support amount breakdowns, line items, shipping options and addresses, payee data, payment nonce, and order ID. Transaction options can carry PayPal payee, description, shipping, and recipient fields.

The GraphQL customer-session surface can create or update sessions and request PAYPAL or VENMO recommendations from customer and device signals. The source explicitly restricts this feature to authorized merchants, so recommendation types and app-installed flags must not be presented as universal enablement.

Venmo is represented as a payment instrument on customers and transactions. Legacy `venmoSdkPaymentMethodCode` and `venmoSdkSession` inputs remain accepted only with runtime warnings that the Venmo SDK integration is unsupported and merchants should use Pay with Venmo. This server source does not define the current client-side Venmo app, browser, or QR experience; consult the independently versioned Braintree client SDK and current guidance for that boundary.

## Cards and 3D Secure

Card and verification operations support direct card data or nonces, billing addresses, merchant-account selection, verification options, and search. Transaction and verification requests accept `threeDSecureAuthenticationId` plus pass-through authentication data; the older `threeDSecureToken` input is deprecated.

`3.39.0` adds `ThreeDSecurePassThruNetwork` and the `network` field to pass-through data on Transaction, Customer, and CreditCardVerification. The SDK transports authentication evidence, while the merchant remains responsible for the client-side 3DS flow and acceptance policy.

## Plans and Subscriptions

Plan operations create, update, find, and list plans. Subscription operations create, update, find, cancel, search, and retry charges. Subscription states include Active, Canceled, Expired, Past Due, and Pending.

Subscription creation validates the plan, merchant account, customer association, and compatible payment-method token or nonce. `retryCharge()` creates a transaction associated with the subscription and can submit it for settlement. Webhook kinds cover subscription activation, cancellation, expiry, trial ending, past-due transitions, billing skips, and successful or failed charges.

These methods establish Braintree's recurring-payment server surface. Wallet-button presence or a reusable client nonce does not independently prove that a payment method supports subscriptions.

## Webhooks and Errors

Webhook parsing requires both signature and payload. The gateway selects the matching public key and verifies an HMAC-SHA1 signature before parsing the notification. Supported events span transactions, subscriptions, payment methods, local payments, refunds, disputes, disbursements, and account changes. The testing gateway can generate sample notifications; settlement test operations reject in Production.

Gateway validation failures return `success: false`, a message, nested validation errors, and sometimes a transaction. The validation collection supports direct, nested, indexed, and deep error access. Transport and HTTP status failures reject rather than returning an unsuccessful result.

## Other Retained API Domains

The capsule also records dispute search and evidence management, document upload, OAuth token and merchant-connect operations, merchant accounts, settlement batch summaries, exchange-rate quotes, disbursement data, and facilitator or transfer metadata. These domains are searchable evidence inventory, but this checkout-focused ingest does not claim full product guidance for them.

## Security and Support

The repository marks major version 3 as Active and version 2 as Inactive and unsupported. Security patches are applied only to Active versions. The cumulative changelog records a `3.38.0` path-traversal fix in AddressGateway operations and DisputeGateway evidence removal; current path construction rejects slash, backslash, encoded, dot, and parent-directory segments.

## `3.39.0` Release Findings

The exact release adds PayPal account validation codes for invalid or excessively long email addresses, adds the 3DS pass-through network enum and fields, and adds `preferredPaymentMethodToken` to client-token generation. No mandatory migration is documented, and the package dependencies remain implementation context rather than evidence of a checkout behavior change.

All broader sections above describe the cumulative implementation present at `3.39.0`, not features introduced by this patch release.

## Related

- [[changelog-github-braintree-node]] - package-qualified release ledger
- [[braintree]] - company and knowledge-status page
- [[braintree-web-sdk]] - browser tokenization and nonce boundary
- [[recurring-payments]] - cross-provider recurring-payment concepts
- [[paypal-braintree-integration]] - PayPal client and Braintree processing boundary

## Raw Sources

- Snapshot manifest: `raw/github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/manifest.json`
- Release manifest: `raw/github/braintree/braintree_node/releases/braintree/3.39.0/2026-08-09/manifest.json`
- Release notes: `raw/github/braintree/braintree_node/releases/braintree/3.39.0/2026-08-09/release-notes.md` (empty upstream body)
- Repository changelog: `raw/github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/files/CHANGELOG.md`
- README: `raw/github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/files/README.md`
- Gateway registry: `raw/github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/files/lib/braintree/braintree_gateway.js`
- Client-token gateway: `raw/github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/files/lib/braintree/client_token_gateway.js`
- Transaction gateway: `raw/github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/files/lib/braintree/transaction_gateway.js`
- Subscription gateway: `raw/github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/files/lib/braintree/subscription_gateway.js`
- Webhook gateway: `raw/github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/files/lib/braintree/webhook_notification_gateway.js`
- Validation codes: `raw/github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/files/lib/braintree/validation_error_codes.js`
