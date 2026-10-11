---
title: "GitHub: braintree/braintree_php"
type: source
date_ingested: 2026-08-19
date_updated: 2026-10-11
original_format: github-repo
raw_files:
  - "github/braintree/braintree_php/snapshots/2026-10-10-2a97c3d/manifest.json"
  - "github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/manifest.json"
tags: [braintree, php-sdk, server-sdk, checkout, paypal, venmo, subscriptions, webhooks, github-repository]
---

## Overview

`braintree/braintree_php` is Braintree's PHP server SDK. The retained history begins with `braintree_php@6.37.0` at exact SHA `0f53ece38397c9fed05b94620634a5a23ef8ee48`, released on 2026-08-05.

Repository: <https://github.com/braintree/braintree_php>

## Evidence Boundary

- This source retains the `braintree_php@6.37.0` baseline and the `6.38.0` delta; it does not replace current product documentation or prove merchant, buyer, country, currency, or payment-method eligibility. Unqualified baseline sections below remain `6.37.0` knowledge; the explicit version section owns the newer findings.
- The SDK performs server-side gateway operations. Browser and native SDKs independently collect payment details or wallet approval and return a payment-method nonce or vaulted token.
- The snapshot retains the complete `lib` implementation, package metadata, README, changelog, security policy, and CA certificate bundle. Tests and fixtures are intentionally excluded.
- Checkout, vaulting, subscriptions, webhooks, and payment-method processing receive detailed treatment. Disputes, OAuth, onboarding, reporting, disbursement, facilitator operations, and other API domains remain searchable inventory-level evidence.

## Grounding Excerpts

> "The Braintree PHP library provides integration access to the Braintree Gateway."
>
> `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/README.md:3`

> "Stops billing a payment method for a subscription. Cannot be reactivated"
>
> `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/lib/Braintree/SubscriptionGateway.php:155`

> "The Venmo SDK integration is Unsupported. Please update your integration to use Pay with Venmo instead"
>
> `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/lib/Braintree/PaymentMethodGateway.php:362`

## Runtime and Gateway Model

The package requires PHP 7.3 or later plus cURL, DOM, hash, OpenSSL, and XMLWriter extensions. A merchant creates a `Braintree\Gateway` for Sandbox or Production using merchant ID plus public/private keys or OAuth credentials. The configuration rejects mixing OAuth and key credentials.

Classic gateway operations serialize XML and use cURL with Braintree's pinned CA bundle. Selected newer operations use GraphQL, including customer sessions and payment recommendations, exchange-rate quotes, instant bank verification, and local-payment context. HTTP and GraphQL failures map to typed exceptions, while gateway validation failures return unsuccessful result objects with nested validation errors.

## Client Tokens, Nonces, and Vaulting

`ClientToken::generate()` accepts customer, merchant-account, domain, and version context. At `6.37.0`, it also accepts `preferredPaymentMethodToken` and maps that value to the gateway's payment-method identifier. A customer ID is required for customer-bound behavior such as saved methods.

Customer and payment-method gateways manage cards, PayPal accounts, Venmo accounts, Apple Pay, Google Pay, local payments, SEPA debit, and US bank accounts. A payment-method nonce can be exchanged for processing or created from a vaulted token. The nonce is a server input, not durable payment-method evidence by itself.

## Transaction Lifecycle

`Transaction::sale()` accepts a payment-method nonce or token, trusted amount, customer and address data, merchant account, descriptor and risk context, line items, 3D Secure data, and processing options. `submitForSettlement` can request authorization and settlement submission together; otherwise the merchant can authorize first and submit later.

The lifecycle includes settlement submission, partial settlement, authorization adjustment, package tracking, void, refund, and transaction-detail updates. Since `6.33.0`, `apiRequestKey` supports idempotency for sale, credit, settlement submission, partial settlement, void, and refund. The merchant backend still owns amount calculation, idempotency-key strategy, order state, and fulfillment decisions.

## PayPal and Venmo

PayPal account gateways manage vaulted accounts and payment-resource updates. Transactions can carry PayPal payee, description, shipping, recipient, and supplementary data. Client-side PayPal approval remains an independent SDK boundary; this package processes the resulting Braintree nonce or token rather than creating a direct PayPal Orders API checkout.

Venmo accounts and transaction payment details remain supported payment instruments. Legacy `venmoSdkSession`, `venmoSdkPaymentMethodCode`, and `isVenmoSdk` inputs emit deprecation warnings directing merchants to Pay with Venmo. This server source does not define the current Venmo app-switch, browser, or QR checkout experience; use the appropriate Braintree client SDK and current enablement guidance for that boundary.

GraphQL customer sessions can request PAYPAL and VENMO payment recommendations using customer, purchase, and app-installed signals. The implementation labels customer-session APIs experimental, so these types are not proof of general product availability.

## Plans and Subscriptions

Plan gateways create, update, find, and list plans. Subscription operations create, find, search, update, retry a charge, and cancel. Creation can use a payment-method token or nonce and configure plan, merchant account, first billing date, trial, descriptor, add-ons, discounts, and PayPal description.

Cancellation stops billing and cannot reactivate the subscription through the cancel operation. `retryCharge()` can optionally submit the resulting transaction for settlement. Webhook kinds cover activation, cancellation, expiry, trial ending, past-due state, skipped billing, and successful or failed charges. These APIs establish a recurring-payment server surface; client wallet availability alone does not establish recurring support.

## Webhooks, Errors, and Security

`WebhookNotification::parse()` verifies the supplied signature before parsing the payload. The PHP SDK explicitly requires public/private API keys for webhook signature verification; an OAuth access token alone is insufficient. Event kinds cover transactions, subscriptions, payment methods, refunds, disputes, disbursements, local payments, and account changes.

The package distinguishes structured validation results from authentication, authorization, not-found, timeout, rate-limit, server, availability, and signature exceptions. The security policy says only active versions receive security patches. The retained README warns that versions older than `3.27.0` contain certificates expiring on 2026-03-30 and will fail impacted traffic.

## `6.37.0` Release Findings

The exact release rejects path separators and relative-path segments in Address and Dispute gateway IDs, adds PayPal email validation codes `92963` and `92964`, and adds `preferredPaymentMethodToken` to client-token generation. No mandatory migration is documented.

All broader sections above describe cumulative implementation present at `6.37.0`, not features introduced by this patch release.

## `6.38.0` Release Findings (2026-09-16)

Approved serial delta from `6.37.0` to `6.38.0`, exact SHA `2a97c3d516a1ee66e710db8140a835d79789627a`, collected 2026-10-10 and ingested 2026-10-11. Nineteen retained files changed, 207 are unchanged. The upstream release-note body is empty; the repository changelog and exact source comparison establish the findings. No package dependency change appears in this capsule comparison.

### Path IDs and Error Handling

The release extends the existing, unchanged `Util::isInvalidPathSegment()` helper to 14 gateway classes: CreditCard, Customer, MerchantAccount, PayPalAccount, PaymentMethod, PaymentMethodNonce, Plan, SepaDirectDebitAccount, Subscription, Testing, Transaction, TransactionLineItem, UsBankAccount and UsBankAccountVerification.

- The helper rejects non-strings and strings outside `^[A-Za-z0-9_-]+$`; separators, relative-path segments and empty strings fail. Several callers additionally use PHP `empty()`, rejecting `"0"`. Some prior regex checks accepted numeric scalars through coercion; the shared helper now requires strings. This is not universal validation of body IDs or merchant authorization.
- New checks cover payment-method update, plan update, subscription update/cancel, transaction cloning, nonce create/find, merchant-account find, US-bank-account find, verification find/confirm and testing requests. Transaction's shared validator also protects existing find, adjust, void, settlement, partial-settlement, detail-update, tracking and refund callers. SEPA's existing validator gains the helper.
- CreditCard, Customer, PayPalAccount, PaymentMethod, Plan, Subscription, SEPA, Transaction and TransactionLineItem private validators throw `InvalidArgumentException`; newly guarded inline lookup/nonce/verification/testing methods use `Braintree\Exception\NotFound`. A local `NotFound` does not prove a gateway lookup occurred.
- TransactionLineItem previously allowed only lowercase letters/digits; it now also allows uppercase letters, underscore and hyphen. Do not describe every change as a narrower character allowlist.
- Subscription `retryCharge()` remains a POST with a body `subscriptionId`; it does not gain the new path-ID guard. Request-body IDs are not universally covered.

### Settlement, Refunds and ACH Search

`TransactionGateway::submitForSettlement($transactionId, $amount, $attribs)` now permits `shipping` address/contact fields, nested `internationalPhone` (`countryCode`, `nationalNumber`), and `shippingAddressId` in its third argument. `submitForPartialSettlementSignature()` merges that same signature with `finalCapture`, so partial-settlement requests inherit the additions. The new settlement shipping signature does not include sale's `shippingMethod` field. SDK request acceptance does not prove gateway permission, shipping persistence or successful capture/settlement.

`refund($transactionId, $amount_or_options)` now permits `surchargeAmount` in the options array alongside `amount`, `apiRequestKey`, `merchantAccountId` and `orderId`. Unlike an SDK that already forwards arbitrary refund options, this PHP release changes the explicit signature used by `Util::verifyKeys()`. It also adds `Error\Codes::TRANSACTION_SURCHARGE_NOT_ON_ORIGINAL_SALE = '97605'`. The constant identifies a validation response; it does not establish all surcharge-refund eligibility rules or a successful refund.

`TransactionSearch::achType()` returns a multiple-value node named `ach_type`, limited to `Transaction::ACH_TYPE_SAME_DAY` (`same_day`) and `ACH_TYPE_STANDARD` (`standard`). Use `.is()` for one value or `.in()` for an array. This filters search, not ACH enablement or a settlement-speed guarantee.

### Grounding Excerpts

- `return !is_string($value)` - `raw/github/braintree/braintree_php/snapshots/2026-10-10-2a97c3d/files/lib/Braintree/Util.php:473` (read with the following regex condition).
- `$this->_validateId($subscriptionId);` - same snapshot, `files/lib/Braintree/SubscriptionGateway.php:164`, before cancel dispatch.
- `'shippingAddressId',` - same snapshot, `files/lib/Braintree/TransactionGateway.php:584`, settlement signature.
- `return new MultipleValueNode('ach_type', [` - same snapshot, `files/lib/Braintree/TransactionSearch.php:27`.
- `const TRANSACTION_SURCHARGE_NOT_ON_ORIGINAL_SALE` - same snapshot, `files/lib/Braintree/Error/Codes.php:633`, value `97605`.

### Migration and Reading Boundary

Audit externally supplied IDs and tokens plus exception handling before adopting the release. Keep trusted identifiers intact rather than stripping rejected characters. Shipping and surcharge fields are optional SDK additions, not a merchant enablement promise. No application or gateway execution was performed.

The user approved focused reading for this work item: all changed implementation files were read completely, with affected prior code and unchanged `Util.php`/`MultipleValueNode.php` dependencies. Both inventories were verified mechanically (452 file hash/size checks); unchanged cumulative changelog history was checked for exact equality. Tests and fixtures remain intentionally excluded. This is not a full upstream repository read.

## Related

- [[changelog-github-braintree-php]] - package-qualified release ledger
- [[braintree-server-sdk]] - shared server integration boundary
- [[source-github-braintree-node]] - independent Node.js implementation evidence
- [[braintree-web-sdk]] - browser tokenization and nonce boundary
- [[recurring-payments]] - cross-provider recurring-payment concepts
- [[paypal-braintree-integration]] - PayPal client and Braintree processing boundary

## Raw Sources

- Current snapshot manifest: `raw/github/braintree/braintree_php/snapshots/2026-10-10-2a97c3d/manifest.json`
- Current release manifest: `raw/github/braintree/braintree_php/releases/braintree_php/6.38.0/2026-10-10/manifest.json`
- Current release notes: `raw/github/braintree/braintree_php/releases/braintree_php/6.38.0/2026-10-10/release-notes.md` (empty upstream body)
- Comparison: `tracking/github/repos/braintree/braintree_php/comparisons/braintree_php/6.37.0--6.38.0/comparison.json`, `comparison.md`, and `diff.patch`
- Current changelog: `raw/github/braintree/braintree_php/snapshots/2026-10-10-2a97c3d/files/CHANGELOG.md`
- Path helper: `raw/github/braintree/braintree_php/snapshots/2026-10-10-2a97c3d/files/lib/Braintree/Util.php`
- Current transaction gateway: `raw/github/braintree/braintree_php/snapshots/2026-10-10-2a97c3d/files/lib/Braintree/TransactionGateway.php`
- Current transaction constants and search: `raw/github/braintree/braintree_php/snapshots/2026-10-10-2a97c3d/files/lib/Braintree/Transaction.php` and `files/lib/Braintree/TransactionSearch.php`
- Search-node dependency: `raw/github/braintree/braintree_php/snapshots/2026-10-10-2a97c3d/files/lib/Braintree/MultipleValueNode.php`
- Current subscription gateway: `raw/github/braintree/braintree_php/snapshots/2026-10-10-2a97c3d/files/lib/Braintree/SubscriptionGateway.php`
- Current validation codes: `raw/github/braintree/braintree_php/snapshots/2026-10-10-2a97c3d/files/lib/Braintree/Error/Codes.php`
- Snapshot manifest: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/manifest.json`
- Release manifest: `raw/github/braintree/braintree_php/releases/braintree_php/6.37.0/2026-08-19/manifest.json`
- Release notes: `raw/github/braintree/braintree_php/releases/braintree_php/6.37.0/2026-08-19/release-notes.md` (empty upstream body)
- Repository changelog: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/CHANGELOG.md`
- README: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/README.md`
- Gateway registry: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/lib/Braintree/Gateway.php`
- Configuration: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/lib/Braintree/Configuration.php`
- Client-token gateway: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/lib/Braintree/ClientTokenGateway.php`
- Transaction gateway: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/lib/Braintree/TransactionGateway.php`
- Subscription gateway: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/lib/Braintree/SubscriptionGateway.php`
- Webhook gateway: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/lib/Braintree/WebhookNotificationGateway.php`
- Validation codes: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/lib/Braintree/Error/Codes.php`
