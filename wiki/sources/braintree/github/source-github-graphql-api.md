---
title: "GitHub: braintree/graphql-api"
type: source
date_ingested: 2026-08-11
date_updated: 2026-10-23
original_format: github-repo
raw_files:
  - "github/braintree/graphql-api/snapshots/2026-10-23-9f76e60/manifest.json"
  - "github/braintree/graphql-api/snapshots/2026-08-11-3a89f42/manifest.json"
tags: [braintree, graphql, api-specification, checkout, paypal, venmo, vault, subscriptions, three-d-secure, github-repository]
---

## Overview

`braintree/graphql-api` is Braintree's public GraphQL schema and schema-change history. The retained baseline is default branch `master` at exact commit `3a89f427466a0a978dbfcfd953913f4e76c3264a`, committed on 2026-08-04. Its immutable capsule contains `schema.graphql`, `CHANGELOG.md`, and `README.md`.

Repository: <https://github.com/braintree/graphql-api>

Latest ingested full baseline: `default-branch@9f76e60`, exact SHA `9f76e60580da00f6740a20692d0b5ea2f313d93e`, committed 2026-10-20 and ingested 2026-10-23. The original `3a89f42` baseline and all its findings remain below; changes are qualified separately in the new full-ingest section. This is a schema commit, not a semantic SDK release.

## Evidence Boundary

- The schema proves GraphQL operation names, input and output shapes, enums, nullability, deprecations, and documented constraints at the exact commit. It does not prove merchant enablement, regional availability, client-SDK support, or production rollout.
- This repository is an API contract, not an integration sample or generated client. Use the independently versioned Braintree Web, Android, iOS, and server SDK sources for executable integration behavior.
- The repository has no package release identity. Its history is commit-qualified and must not be described as a Braintree SDK version.
- Checkout, transaction processing, payment methods, vaulting, PayPal, Venmo, 3D Secure, and recurring billing receive detailed treatment below. In-store, disputes, reporting, OAuth, merchant onboarding, and other domains remain inventory-level evidence.

## Grounding Excerpts

> "Authorize an eligible PayPal account and return a payload that includes details of the resulting transaction."
>
> `raw/github/braintree/graphql-api/snapshots/2026-08-11-3a89f42/files/schema.graphql:6184-6187`

> "Create a Venmo payment context."
>
> `raw/github/braintree/graphql-api/snapshots/2026-08-11-3a89f42/files/schema.graphql:6598-6599`

> "Creates a new recurring billing subscription."
>
> `raw/github/braintree/graphql-api/snapshots/2026-08-11-3a89f42/files/schema.graphql:6714-6715`

## GraphQL Integration Model

The top-level `Mutation` surface supports payment authorization, charging, capture, partial capture, refund, reversal, void, tokenization, vaulting, verification, client-token creation, PayPal and Venmo setup flows, 3D Secure lookup, and recurring billing. The top-level `Query` surface exposes node lookup, client configuration, transactions, refunds, payments, verifications, customers, disputes, merchant-related data, and recurring billing resources.

Global IDs coexist with legacy IDs. `idsFromLegacyIds` converts batches of typed legacy identifiers, while `Node`-implementing objects can be fetched through the top-level node query. Search connections use forward pagination and return `pageInfo` plus edges.

## Transaction Lifecycle and Idempotency

The schema separates authorization from capture and also provides combined charge operations. Generic and payment-method-specific mutations include `authorizePaymentMethod`, `authorizePayPalAccount`, `authorizeVenmoAccount`, `authorizeCreditCard`, `chargePaymentMethod`, `chargePayPalAccount`, `chargeVenmoAccount`, and `chargeCreditCard`.

The processing lifecycle includes capture, partial capture, refund, reverse, and void. A reversal attempts a void before settlement and otherwise returns a refund. Transaction status history records authorization, processor decline, gateway rejection, settlement submission, settling, settlement, failure, expiration, and void events.

Mutating payment operations commonly accept `apiRequestKey`. The schema documents that reuse can return the previously created resource for 30 days, while concurrent reuse or changed inputs produces validation failure. Authentication, authorization, not-found, resource-limit, and not-implemented failures that create no resource do not establish a duplicate result.

`TransactionInput` carries amount, merchant account, order ID, risk data, descriptors, payment initiator, customer association, shipping, tax, line items, optional post-transaction vaulting, industry data, partial-authorization control, and payment-facilitator data. PayPal invoice-number and partner-channel mappings are explicitly documented.

## Client Tokens, Tokenization, and Vaulting

`createClientToken` supplies client-side initialization context. Tokenization mutations cover cards, CVV, network tokens, Apple Pay, PayPal one-time payments and billing agreements, US bank accounts, and other methods. A single-use payment method can be charged directly or converted to a multi-use method through `vaultPaymentMethod` or method-specific vault mutations.

Vaulting can associate a customer, run method verification, carry 3DS or risk inputs, and make a method the default. Transaction inputs can vault a single-use method always or only after successful authorization. Payment methods preserve usage as `SINGLE_USE` or `MULTI_USE`; a nonce or payment-method ID is therefore not, by itself, proof of recurring-payment eligibility.

## PayPal Checkout and Vault

PayPal has distinct one-time-payment and billing-agreement setup paths. `createPayPalOneTimePayment` creates an approval flow, and `tokenizePayPalOneTimePayment` converts approved PayPal identifiers into a single-use payment method. `updatePayPalOneTimePayment` can revise amount, breakdown, line items, shipping options and address, description, order ID, and payee email.

`createPayPalBillingAgreement` and `tokenizePayPalBillingAgreement` establish reusable PayPal consent. The schema also supports importing an externally created billing agreement through `vaultPayPalBillingAgreement`. PayPal app-switch input distinguishes native-app and mobile-web origins and includes native return/cancel URLs plus an allowlisted fallback URL scheme.

PayPal transaction details retain payer/payee information, authorization and capture IDs, payment ID, fee, protection status, recipient data, and transaction description. Contract presence does not establish that every PayPal account or merchant can use a given approval or vault mode.

## Venmo Checkout

Venmo can be authorized or charged through dedicated mutations after obtaining a payment method. `createVenmoPaymentContext` creates a context with amount and currency, merchant profile, customer client, payment-method usage, intent, payer and paysheet details, return URL, risk correlation ID, and app-switch context.

The resulting context can progress through `CREATED`, `SCANNED`, `APPROVED`, `CANCELED`, `EXPIRED`, or `FAILED`. It can return a single-use or multi-use payment-method ID. Paysheet data supports totals, tax, discounts, shipping, billing or shipping-address collection, and line items.

The retained app-switch context is defined for mobile web and carries user-agent and private-browsing indicators. This GraphQL contract does not replace the independently collected native Braintree Android and iOS evidence for Venmo app/browser behavior.

## Cards and 3D Secure

Card tokenization produces a single-use payment method. Card authorization and charge inputs can carry merchant-account selection, 3DS authentication evidence, risk data, external-vault context, account type, and verification options.

`performThreeDSecureLookup` accepts payment method, amount, merchant account, device-data reference, browser/client information, transaction and cardholder information, exemption request, data-only request, card-add context, and merchant-initiated 3RI data. Its result can include challenge URL and protocol identifiers plus a replacement single-use payment method.

Pass-through authentication supports ECI, CAVV, transaction identifiers, protocol version, directory-server response, and network choice for EFTPOS, Mastercard, or Visa. Liability-shift fields and authentication status describe evidence; merchants still need an acceptance policy and compatible client flow.

## Recurring Billing

The schema contains plan and subscription APIs rather than only recurring transaction flags. Plan operations create, update, delete, and list plans, add-on templates, and discount templates. Plans define price and currency, billing frequency and day, cycle count, trials, add-ons, and discounts.

Subscription operations create, update, search, cancel, and manually charge subscriptions. Creation selects a plan and payment method and can override price, merchant account, cycle count, PayPal receipt description, start timing, trial, descriptor, add-ons, and discounts. Update supports plan and payment-method changes, proration, revert-on-proration-failure, and retained or replaced modifications.

Subscription states are `PENDING`, `ACTIVE`, `PAST_DUE`, `CANCELED`, and `EXPIRED`. Timeline, balance, failure count, billing-cycle dates, transaction IDs, and status history expose operational state. A subscription payment method can be single-use or multi-use; the schema says a single-use method is vaulted automatically, but product-specific consent and eligibility must still be verified.

## Latest Retained Changes

Historical `3a89f42` snapshot findings follow. The newer `9f76e60` contract is recorded separately below, without replacing this history.

The 2026-08-04 commit adds merchant-account type and capabilities, including `supportsPublicDescriptors`. Recent 2026 changes also add and expand native recurring billing, direct top-level searches, ACH transaction search, 3DS pass-through network selection, and recurring plan add-on and discount template management.

These are changelog milestones within the cumulative schema. Only exact comparisons against a later commit may be described as future delta findings.

## Full additive baseline: `default-branch@9f76e60`

**Boundary:** `3a89f427466a0a978dbfcfd953913f4e76c3264a` -> `9f76e60580da00f6740a20692d0b5ea2f313d93e` on `master`. User-approved full mode overrides the path-based delta recommendation because existing inputs are removed and an output becomes nullable. The explicit focused-reading exception covers changed schema definitions and affected prior definitions in full, new changelog entries and cumulative wiki history; unchanged schema/history, manifests and the duplicated diff were checked mechanically. Relevant shared wiki sections were read. No GraphQL API requests, client generation or payment execution were performed.

**Evidence:** Both snapshots retain the same three paths. `schema.graphql` and `CHANGELOG.md` changed; README is byte-identical. Current capsule: 615,078 bytes. All six current/prior files pass size, SHA-256 and Git blob checks. Applying the stored patch to a temporary copy of the prior snapshot reconstructs every current file byte-for-byte. The old raw changelog is an exact suffix of the new one (48 added lines); no prior raw history was rewritten. A definition-level text comparison identifies 71 changed/added blocks, including one new enum; most changes are descriptions or formatting, not new operations.

### PayPal shipping input migration

Both `PayPalExperienceProfileInput` (one-time checkout) and `PayPalBillingAgreementExperienceProfileInput` remove `collectShippingAddress` and `shippingAddressEditable`. Their replacement is optional `shippingPreference: PayPalShippingPreference`:

| Value | Exact schema meaning |
| --- | --- |
| `BUYER_SELECTS_ADDRESS` | Buyer selects a PayPal address or supplies a new one |
| `MERCHANT_PROVIDED_ADDRESS_LOCKED` | Uses the merchant-provided address without buyer editing |
| `NO_SHIPPING_ADDRESS` | No shipping address collected or displayed |

```graphql
# Input fragment for the selected create-payment/agreement operation:
paypalExperienceProfile: {
  shippingPreference: MERCHANT_PROVIDED_ADDRESS_LOCKED
}
```

Supply the merchant address through the parent operation's `shippingAddress`, observing its own prerequisites. The one-time input requires `addressLine1`, `adminArea2` and `countryCode` when an address is supplied; the billing-agreement input documents those fields as required for Billing Agreements. The enum has no documented default or universal truth-table mapping from the removed booleans. Choose the intended checkout behavior explicitly and validate against the target schema. Do not assume a separately versioned Braintree Web/React wrapper or PayPal Orders API accepts this GraphQL field.

### Merchant-account search migration

`MerchantAccountSearchInput.id: SearchValueInput` is removed and replaced by `merchantAccountId: SearchTextValueInput`, described as the merchant-account ID/token. The old filter accepted `is`/`in` strings; the new text filter also permits `isNot`, `startsWith`, `endsWith` and `contains`. Audit field names, filter types and identifier semantics rather than merely renaming an opaque global ID.

```graphql
# New MerchantAccountSearchInput fragment:
merchantAccountId: { is: "merchant_account_token" }
```

This does not change `MerchantAccount.id` itself or prove account creation/eligibility.

### Recurring billing nullability

The returned `RecurringBillingSubscription.paymentMethodId` changes from `ID!` to `ID`. Regenerate or audit client output types, null checks and display/reconciliation paths. This does not permit creation without a payment method: unchanged `CreateRecurringBillingSubscriptionInput.paymentMethodId` is still `ID!`; the existing update input remains optional `ID`. No subscription create/update/cancel/charge operation is added in this comparison.

### 3DS device ID and status vocabulary

`PerformThreeDSecureLookupInput.deviceId: String` is an optional stable device identifier, documented as usable for DCAP eligibility. It is distinct from `dfReferenceId`, which connects the lookup with previously collected CardinalCommerce device data. `paymentMethodId: ID!` and `amount: Amount!` remain required. Schema presence does not prove client-SDK forwarding, enrollment or exemption eligibility.

`ThreeDSecureAuthenticationStatus` adds `SKIPPED_DUE_TO_SMART_AUTHENTICATION` and marks the Adaptive Authentication value deprecated in favor of it. The changelog entry is dated 2026-10-20; the deprecation description says since 2026-10-01. Those are announcement and annotation dates, not an inferred deployment timeline. Handle both values during migration; a skipped state is not proof of successful authentication, liability shift, authorization or capture. Existing flattened `ThreeDSecureDetails` deprecations gain dated descriptions; use the already-existing nested `authentication` fields rather than treating them as newly introduced.

### Refund surcharge and transaction customer details

Optional `surchargeAmount: String` is added to `RefundInput`, `Refund` and `CreditCardDetachedRefundOptionsInput`. Each describes the surcharge as a portion of the total refund, already included and not to be added separately, non-negative and applicable to US-region e-commerce credit-card transactions only. A 10.00 total refund including 0.30 surcharge remains a 10.00 refund, not 10.30. This is schema documentation, not confirmation that a specific merchant/refund is accepted; detached refunds remain separately eligibility-gated.

`TransactionCustomerDetailsInput` adds optional `firstName` and `lastName`, each documented with a 255-character maximum. The input describes details stored on a transaction when no customer is associated, for fraud-detection purposes; it is not a new customer-creation or identity-verification operation.

### OAuth scope clarifications in descriptions

The mutation/query signatures remain present; the changed descriptions now specify:

| Operation | Documented OAuth token scopes |
| --- | --- |
| `chargePaymentMethod` | `TRANSACTION_SALE` and `TRANSACTION_MANAGE_SETTLEMENT` |
| `vaultPaymentMethod` | `CUSTOMER_CREATE` and `MULTI_USE_PAYMENT_METHOD_CREATE` |
| `reverseTransaction` | `TRANSACTION_REFUND` and `TRANSACTION_VOID` |
| `verifyPaymentMethod`, `verifyUsBankAccount` | `MULTI_USE_PAYMENT_METHOD_UPDATE` |
| `verifyCreditCard` | `MULTI_USE_PAYMENT_METHOD_UPDATE` for multi-use; `STANDALONE_VERIFICATIONS` for single-use |
| `idsFromLegacyIds` | A `_FIND` scope; `PAYMENT_METHOD` conversion requires `MULTI_USE_PAYMENT_METHOD_FIND`, also recommended there for integrations supporting every `LegacyIdType` |

Treat these as newly retained contract documentation, not proof that OAuth enforcement first changed at this commit. They do not apply indiscriminately to API-key authentication.

### Payment-method inventory and deprecation attribution

The comparison adds `BLIK_PAY_LATER`, `OXXO_PAY` and `PIX_INTERNATIONAL` to local-payment inventory, OXXO Pay to non-instant methods, and corresponding `_VIA_PAYPAL` search values. The larger `ExternalProcessor` enum adds many processor names. Neither enum establishes a working connector, geography, account enablement or client implementation.

Boleto/Samsung Pay enum entries and `VenmoPaymentContext.userName` gain formal `@deprecated` markers. The prior schema already described these entries as deprecated/unsupported in prose, so this is not proof that a payment flow was newly discontinued in October. Use `payerInfo.userName` for Venmo; its existing consent, payment-method-usage and return-context fields are not new features. Many other fields only gain dated legacy deprecation descriptions or wording normalization. Existing View/Edit funding-instrument mutations were already present in `3a89f42`; this update does not introduce that returning-buyer workflow.

### Grounding excerpts at `9f76e60`

> `merchantAccountId: SearchTextValueInput`
>
> `raw/github/braintree/graphql-api/snapshots/2026-10-23-9f76e60/files/schema.graphql:6219`

> `shippingPreference: PayPalShippingPreference`
>
> `raw/github/braintree/graphql-api/snapshots/2026-10-23-9f76e60/files/schema.graphql:8270`

> `deviceId: String`
>
> `raw/github/braintree/graphql-api/snapshots/2026-10-23-9f76e60/files/schema.graphql:9058`

> `paymentMethodId: ID`
>
> `raw/github/braintree/graphql-api/snapshots/2026-10-23-9f76e60/files/schema.graphql:9461`

> `SKIPPED_DUE_TO_SMART_AUTHENTICATION`
>
> `raw/github/braintree/graphql-api/snapshots/2026-10-23-9f76e60/files/schema.graphql:12817`

### Historical and query boundary

Keep the `3a89f42` contract for older queries, including its shipping booleans and non-null subscription response field. For new integrations targeting `9f76e60`, use this section and [[changelog-github-graphql-api]], not the older baseline alone. The repository schema does not prove the exact schema deployed to a particular account/environment or the availability of a separately versioned SDK binding. Broader domains remain inventory-level unless their exact definitions were read for the query.

## Other API Inventory

The schema also contains customer and merchant records, disputes and evidence, fraud evaluation, Apple Pay domain management, local payments, ACH and SEPA, in-store locations and readers, reporting, OAuth client-secret management, package tracking, exchange-rate quotes, and onboarding-related objects. These domains are searchable inventory; field-level guidance should return to the exact raw schema or trigger a deeper recollection.

## Related

- [[changelog-github-graphql-api]] - commit-qualified schema history
- [[braintree]] - company and knowledge-status page
- [[source-github-braintree-node]] - Node.js gateway implementation
- [[braintree-web-sdk]] - browser tokenization and nonce behavior
- [[braintree-android-sdk]] - native Android PayPal and Venmo behavior
- [[braintree-ios-sdk]] - native iOS PayPal and Venmo behavior
- [[paypal-braintree-integration]] - PayPal client and Braintree processing boundary
- [[recurring-payments]] - cross-provider recurring-payment concepts

## Raw Sources

- [9f76e60 snapshot manifest](../../../../raw/github/braintree/graphql-api/snapshots/2026-10-23-9f76e60/manifest.json)
- [Exact schema](../../../../raw/github/braintree/graphql-api/snapshots/2026-10-23-9f76e60/files/schema.graphql) - changed definitions read under the explicit focused-reading exception, unchanged sections verified mechanically
- [[raw/github/braintree/graphql-api/snapshots/2026-10-23-9f76e60/files/CHANGELOG|New changelog]] - six new milestones; older history verified byte-for-byte
- [[raw/github/braintree/graphql-api/snapshots/2026-10-23-9f76e60/files/README|Repository evidence scope]]
- [Exact comparison](../../../../tracking/github/repos/braintree/graphql-api/comparisons/default-branch/3a89f42--9f76e60/comparison.json) and [reconstructable diff](../../../../tracking/github/repos/braintree/graphql-api/comparisons/default-branch/3a89f42--9f76e60/diff.patch)
- Snapshot manifest: `raw/github/braintree/graphql-api/snapshots/2026-08-11-3a89f42/manifest.json`
- Schema: `raw/github/braintree/graphql-api/snapshots/2026-08-11-3a89f42/files/schema.graphql`
- Repository changelog: `raw/github/braintree/graphql-api/snapshots/2026-08-11-3a89f42/files/CHANGELOG.md`
- README: `raw/github/braintree/graphql-api/snapshots/2026-08-11-3a89f42/files/README.md`
