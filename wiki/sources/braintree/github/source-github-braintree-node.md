---
title: "GitHub: braintree/braintree_node"
type: source
date_ingested: 2026-10-06
original_format: github-repo
raw_files:
  - "github/braintree/braintree_node/snapshots/2026-10-06-deb5227/manifest.json"
  - "github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/manifest.json"
tags: [braintree, node-js-sdk, server-sdk, checkout, paypal, venmo, subscriptions, webhooks, github-repository]
---

## Overview

`braintree/braintree_node` is Braintree's Node.js server SDK. The retained history begins with `braintree@3.39.0` at exact SHA `7a9270aaf31eb87819add64a768652243f90007c`, released on 2026-08-06.

Repository: <https://github.com/braintree/braintree_node>

History now also includes `braintree@3.40.0` at SHA `deb5227f1c4824b1f622115caf2ba4302134d375`, released 2026-09-23 and ingested 2026-10-06. The original broad implementation sections below remain the `3.39.0` baseline; the new version-qualified section adds knowledge without replacing older findings. This is the Node repository's package, independently versioned from Ruby's identically named `braintree` package.

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

## `3.40.0` Full Additive Update from `3.39.0`

The user approved full additive ingest with focused reading because the security change spans many gateway families. All changed retained implementation files and affected prior code were read; unchanged files and cumulative changelog history were verified mechanically. This does not claim a fresh full read of the complete repository. Both snapshots contain 170 retained files: 20 modified and 150 unchanged. The upstream comparison classifies 21 additional paths as excluded tests or lockfile evidence. The GitHub release-note body is empty.

### Grounding Excerpts

> "- Add `achType` to transaction search"
>
> `raw/github/braintree/braintree_node/snapshots/2026-10-06-deb5227/files/CHANGELOG.md:5`

> "- Add support for `surchargeAmount` in `Transaction.refund()`"
>
> `raw/github/braintree/braintree_node/snapshots/2026-10-06-deb5227/files/CHANGELOG.md:7`

> `return typeof value !== "string" || !/^[A-Za-z0-9_-]+$/.test(value);`
>
> `raw/github/braintree/braintree_node/snapshots/2026-10-06-deb5227/files/lib/braintree/util.js:298`

> `this.multipleValueField("achType", { allows: Transaction.AchType.All() }); // eslint-disable-line new-cap`
>
> `raw/github/braintree/braintree_node/snapshots/2026-10-06-deb5227/files/lib/braintree/transaction_search.js:54`

### Path-ID and Token Security

`Util.isInvalidPathSegment` moves from a denylist to a nonempty ASCII letter/digit/underscore/hyphen allowlist. Invalid values, including nonstrings, whitespace, periods, slashes, backslashes and encoded segments, are rejected before HTTP dispatch in the affected methods. Most new guards return `NotFoundError("Not Found")`; existing Dispute methods retain their contextual not-found messages. A local error does not prove an HTTP 404 or absence of the requested object.

Added or replaced checks cover Customer, Transaction, CreditCard, PaymentMethod, PaymentMethodNonce, Subscription, MerchantAccount, PayPalAccount, UsBankAccount, UsBankAccountVerification, CreditCardVerification, Plan, SepaDirectDebitAccount and TransactionLineItem gateways. Transaction checks cover authorization adjustment, cancel release, cloning, lookup, refund, settlement submission, detail updates, package tracking, partial settlement and void. Existing Address and Dispute helper callers inherit the tighter validation without file changes.

Source also adds a TestingGateway transaction-ID guard, although the changelog's gateway list omits it. This guard runs before the Production-environment check: invalid IDs reject as not found; valid IDs in Production still reject test operations. No test operations were executed during ingestion.

The boundary is path-segment use, not universal input validation: Customer lookup validates a truthy `associationFilterId`; payment-method grant/revoke retain their existing token checks for request-body values; subscription retry passes its ID in the sale body. Do not infer identical checks on every body ID, ownership validation, a complete security audit, or any specific advisory/CVE.

**Migration implication:** audit caller-supplied custom IDs and error handling. Values containing spaces or periods may now fail locally in affected operations. Use the actual valid identifier; stripping characters could target a different object. Existing `3.38.0` Address/Dispute hardening and the `3.39.0` baseline remain historical evidence, not a claim that the new rule existed in those versions.

### ACH Transaction Search

`Transaction.AchType` adds `SameDay: "same_day"`, `Standard: "standard"` and `All()`. The new `achType` multiple-value search field restricts values to that enum; its existing search-node implementation supports `.is()` and `.in()` and rejects unsupported values.

```javascript
// Illustrative server-side search; not executed during ingestion.
const matchingTransactions = gateway.transaction.search((search) => {
  search.achType().is(braintree.Transaction.AchType.SameDay);
});
matchingTransactions.on("data", (transaction) => {
  // Consume matching transaction records in your application.
});
matchingTransactions.on("error", (error) => {
  // Handle search failure without exposing provider details to buyers.
});
```

This is a search addition, not introduction of ACH sale options, ACH enablement, or a same-day settlement guarantee. The existing transaction sale signature already retained US-bank-account ACH processing options at `3.39.0`.

### Refund Surcharge Announcement versus Implementation

The changelog announces `surchargeAmount` support for `Transaction.refund()`. Both retained versions already forward the refund options object as `{ transaction: options }` without a field allowlist. The changed refund implementation adds the path-ID guard; it does not introduce a new surcharge mapping. The announcement therefore must not be presented as proof that `3.39.0` could not transport that field, or that a gateway accepts it for every merchant or transaction.

```javascript
// Illustrative request shape only; eligibility and gateway acceptance unverified.
const result = await gateway.transaction.refund(transactionId, {
  amount: "10.00",
  surchargeAmount: "1.00",
});
```

This example does not establish surcharge arithmetic, refund eligibility or a successful payment/refund. No payment or integration tests were run.

### Preserved Runtime and Integration Knowledge

`package.json` changes only the version. Node.js `>=10.0`, npm `>=6`, dependencies and development dependencies are unchanged. Client-token preferred-payment-method handling, server/client separation, authorization/settlement, vault, subscriptions and webhook knowledge remain preserved from the prior baseline. No newly introduced client checkout, PayPal/Venmo enablement or mandatory runtime migration is established by this comparison.

## Related

- [[changelog-github-braintree-node]] - package-qualified release ledger
- [[braintree]] - company and knowledge-status page
- [[braintree-web-sdk]] - browser tokenization and nonce boundary
- [[recurring-payments]] - cross-provider recurring-payment concepts
- [[paypal-braintree-integration]] - PayPal client and Braintree processing boundary

## Raw Sources

- Current snapshot manifest: `raw/github/braintree/braintree_node/snapshots/2026-10-06-deb5227/manifest.json`
- Current release manifest: `raw/github/braintree/braintree_node/releases/braintree/3.40.0/2026-10-06/manifest.json`
- Current release notes: `raw/github/braintree/braintree_node/releases/braintree/3.40.0/2026-10-06/release-notes.md` (empty upstream body)
- Exact comparison: `tracking/github/repos/braintree/braintree_node/comparisons/braintree/3.39.0--3.40.0/comparison.md`
- Current changelog: `raw/github/braintree/braintree_node/snapshots/2026-10-06-deb5227/files/CHANGELOG.md`
- Identifier helper: `raw/github/braintree/braintree_node/snapshots/2026-10-06-deb5227/files/lib/braintree/util.js`
- Current transaction implementation: `raw/github/braintree/braintree_node/snapshots/2026-10-06-deb5227/files/lib/braintree/transaction_gateway.js`
- ACH enum: `raw/github/braintree/braintree_node/snapshots/2026-10-06-deb5227/files/lib/braintree/transaction.js`
- ACH search: `raw/github/braintree/braintree_node/snapshots/2026-10-06-deb5227/files/lib/braintree/transaction_search.js`
- Search operators: `raw/github/braintree/braintree_node/snapshots/2026-10-06-deb5227/files/lib/braintree/advanced_search.js`
- Inherited Address checks: `raw/github/braintree/braintree_node/snapshots/2026-10-06-deb5227/files/lib/braintree/address_gateway.js`
- Inherited Dispute checks: `raw/github/braintree/braintree_node/snapshots/2026-10-06-deb5227/files/lib/braintree/dispute_gateway.js`
- Testing guard: `raw/github/braintree/braintree_node/snapshots/2026-10-06-deb5227/files/lib/braintree/testing_gateway.js`
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
