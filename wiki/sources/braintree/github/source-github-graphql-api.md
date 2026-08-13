---
title: "GitHub: braintree/graphql-api"
type: source
date_ingested: 2026-08-11
original_format: github-repo
raw_files:
  - "github/braintree/graphql-api/snapshots/2026-08-11-3a89f42/manifest.json"
tags: [braintree, graphql, api-specification, checkout, paypal, venmo, vault, subscriptions, three-d-secure, github-repository]
---

## Overview

`braintree/graphql-api` is Braintree's public GraphQL schema and schema-change history. The retained baseline is default branch `master` at exact commit `3a89f427466a0a978dbfcfd953913f4e76c3264a`, committed on 2026-08-04. Its immutable capsule contains `schema.graphql`, `CHANGELOG.md`, and `README.md`.

Repository: <https://github.com/braintree/graphql-api>

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

The 2026-08-04 commit adds merchant-account type and capabilities, including `supportsPublicDescriptors`. Recent 2026 changes also add and expand native recurring billing, direct top-level searches, ACH transaction search, 3DS pass-through network selection, and recurring plan add-on and discount template management.

These are changelog milestones within the cumulative schema. Only exact comparisons against a later commit may be described as future delta findings.

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

- Snapshot manifest: `raw/github/braintree/graphql-api/snapshots/2026-08-11-3a89f42/manifest.json`
- Schema: `raw/github/braintree/graphql-api/snapshots/2026-08-11-3a89f42/files/schema.graphql`
- Repository changelog: `raw/github/braintree/graphql-api/snapshots/2026-08-11-3a89f42/files/CHANGELOG.md`
- README: `raw/github/braintree/graphql-api/snapshots/2026-08-11-3a89f42/files/README.md`
