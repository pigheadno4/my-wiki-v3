---
title: "GitHub: braintree/braintree_php"
type: source
date_ingested: 2026-08-19
date_updated: 2026-10-29
original_format: github-repo
raw_files:
  - "github/braintree/braintree_php/snapshots/2026-10-29-b116668/manifest.json"
  - "github/braintree/braintree_php/snapshots/2026-10-29-883a219/manifest.json"
  - "github/braintree/braintree_php/snapshots/2026-10-10-2a97c3d/manifest.json"
  - "github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/manifest.json"
tags: [braintree, php-sdk, server-sdk, checkout, paypal, venmo, subscriptions, webhooks, github-repository]
---

## Overview

`braintree/braintree_php` is Braintree's PHP server SDK. The retained history begins with `braintree_php@6.37.0` at exact SHA `0f53ece38397c9fed05b94620634a5a23ef8ee48`, released on 2026-08-05.

Repository: <https://github.com/braintree/braintree_php>

Latest ingested package: `braintree_php@6.40.0`, exact SHA `b116668cb1c66b10aceb71e7753a49fbf4e44fd6`. The original baseline and all subsequent version-qualified sections remain historical evidence.

## Evidence Boundary

- The 6.40.0 delta follows the completed 6.39.0 ingest, with approved focused reading of all changed retained source/content, affected prior code, comparison and cumulative wiki history. Six modified/220 unchanged retained files; 33 upstream dispositions (six retained/27 policy exclusions), no gaps or unclassified changes. Generated inventories and unchanged changelog history mechanically checked. Runtime security claims below are attributed to the dated upstream README, not independently validated exploit/advisory findings. No PHP/runtime/payment execution.
- The 6.39.0 delta uses user-approved focused reading: every changed retained implementation file, affected prior code, comparison, new changelog block and cumulative wiki history; unchanged source/history and generated inventories checked mechanically. Six modified/220 unchanged retained files, 11 upstream dispositions (six retained/five excluded tests), no gaps or unclassified changes. No PHP, application, gateway or payment execution.
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

## `6.39.0` Additive Delta Findings

Ruby and Node package histories remain independent. This entry concerns PHP package `braintree_php@6.39.0` at `883a2199aad6f3e1e4796d0f3bea6725c981fd85`, compared with 6.38.0, collected/ingested October 29, 2026. The release manifest's October 19 timestamp is tag/commit-derived; there is no GitHub Release-note body. Existing 6.37.0/6.38.0 sections above are preserved rather than reattributed to this release.

### Reversal API and Result Handling

`Braintree\Transaction::reverse($transactionId, $attribs = [])` delegates to the configured transaction gateway. The gateway calls its existing `_validateId()` (nonempty string ID, ASCII letters/digits/underscore/hyphen; PHP `empty()` also rejects `"0"`), verifies options against `['apiRequestKey']`, and POSTs to `/transactions/{id}/reverse`. Empty options produce a null body; nonempty options are wrapped under `transaction`. Invalid IDs or option keys raise `InvalidArgumentException` locally before HTTP.

The upstream description is void when still voidable, otherwise a full refund. That selection is delegated to the server; the SDK neither evaluates settlement status nor falls back locally between existing void/refund methods. Reversal has no amount input for partial refund. Gateway eligibility, accepted instruments/statuses and request-key semantics require separate product/server evidence; the client method adds no automatic retries or guaranteed idempotency.

`reverse()` returns `Result\Successful` containing the transaction or `Result\Error` for an API validation response; unexpected response shapes throw `Exception\Unexpected`. `reverseNoValidate()` calls `reverse()` first, so its name does not bypass path/option validation. The unchanged `Util::returnObjectOrThrowException()` returns the transaction on success and throws `Braintree\Exception\ValidationsFailed` on a failed validation result, despite docblocks that mention an error-result return. Transport exceptions remain separate.

### External Vault and Error Constants

Transaction create/sale's validated signature adds `externalVault.previousMastercardTransactionLinkId` alongside status and `previousNetworkTransactionId`. `CreditCardVerification::createSignature()` adds the same previous link ID, and the static `CreditCardVerification::create()` wrapper invokes that signature validator before dispatch. Its unchanged direct gateway `create()` posts attributes without that wrapper's `verifyKeys()` call. Do not transfer the Ruby verification signature caveat wholesale to the PHP static entry point.

Five new `Braintree\Error\Codes` constants are retained: `TRANSACTION_CANNOT_REVERSE_AT_THIS_TIME` (`915282`); `TRANSACTION_EXTERNAL_VAULT_STATUS_WITH_PREVIOUS_MASTERCARD_TRANSACTION_LINK_ID_IS_INVALID` (`915278`); `TRANSACTION_EXTERNAL_VAULT_PREVIOUS_MASTERCARD_TRANSACTION_LINK_ID_IS_INVALID` (`915279`); `VERIFICATION_EXTERNAL_VAULT_STATUS_WITH_PREVIOUS_MASTERCARD_TRANSACTION_LINK_ID_IS_INVALID` (`942205`); and `VERIFICATION_EXTERNAL_VAULT_PREVIOUS_MASTERCARD_TRANSACTION_LINK_ID_IS_INVALID` (`942206`). These describe server diagnostics, not independent proof of all field relationships or merchant eligibility. Card/customer signatures are not changed by this PHP release; do not infer those additions from Ruby 4.42.0.

### Grounding Excerpts

Locations below are under `raw/github/braintree/braintree_php/snapshots/2026-10-29-883a219/files/`:
- `lib/Braintree/TransactionGateway.php:639`: `return ['apiRequestKey'];`
- `lib/Braintree/TransactionGateway.php:839`: `public function reverse($transactionId, $attribs = [])`
- `lib/Braintree/CreditCardVerification.php:36`: `Util::verifyKeys(self::createSignature(), $attributes);`
- `lib/Braintree/CreditCardVerification.php:89`: `'previousMastercardTransactionLinkId',`
- `lib/Braintree/Util.php:158`: `throw new Exception\ValidationsFailed();`

## `6.40.0` Additive Delta Findings

Package `braintree_php@6.40.0`, exact SHA `b116668cb1c66b10aceb71e7753a49fbf4e44fd6`, compared with 6.39.0, collected/ingested October 29, 2026. The manifest's October 27 timestamp is tag/commit-derived, not verified GitHub Release publication; its release-note body is empty. All 6.37.0/6.38.0/6.39.0 knowledge above remains intact.

### PHP 8.2+ Deprecation Fixes

`SignatureService` now explicitly declares public `$key` and `$digest`, which its constructor previously created dynamically. The constructor assignments, digest invocation (`call_user_func($this->digest, $this->key, $data)`) and `hash|payload` signing format are unchanged. This is property-declaration compatibility, not a cryptographic algorithm or webhook protocol change.

`Error\Validation` gains `#[\AllowDynamicProperties]`. Its existing initializer loops over API response keys, constructs underscore-prefixed property names and applies the existing delimiter conversion to values; its getter is unchanged. The annotation avoids dynamic-property deprecation notices for additional response keys, such as the comment's `at_most_once_processing` example. It does not introduce that field, redefine validation semantics or make these properties a new stable payment-result contract. The upstream comment says PHP 7 treats the attribute line as a comment; no cross-runtime execution was performed here.

`AchMandate` only gains `TODO: Review removing in NEXT_MAJOR_VERSION`. Factory, initialization and string representation are unchanged; it is not removed or behaviorally deprecated by this comment alone. Version metadata advances to 6.40.0; no transaction/reversal implementation or Composer dependency change occurs in this comparison.

### Minimum, Tested and Recommended Runtime

- Composer still requires PHP `>=7.3.0` and the existing extensions. This release does not raise the declared installation minimum.
- The README's tested list changes from 7.3/7.4/8.0 to 7.4/8.2/8.3/8.4/8.5. Absence from the tested list is not itself a Composer rejection or new runtime enforcement.
- The README recommends latest-patch PHP 8.4 or 8.5. Its new security notice names CVE-2026-109618 and CVE-2026-109619 and reports patched versions 8.2.35, 8.3.36, 8.4.27 and 8.5.12, while warning about older unsupported branches. These are Braintree's dated upstream claims; linked PHP advisories were not independently collected or assessed in this ingest.

> [!info] Upstream Runtime Advisory
> The retained README/changelog report PHP-runtime security fixes and SDK compatibility with patched runtimes. Installing SDK 6.40.0 does not patch the PHP interpreter. Verify current PHP/vendor advisories and deployment runtime independently; the wiki has not reproduced an exploit, certified those patch levels or tested runtime compatibility.

### Grounding Excerpts

Locations below are under `raw/github/braintree/braintree_php/snapshots/2026-10-29-b116668/files/`:
- `lib/Braintree/SignatureService.php:8`: `public $key;`
- `lib/Braintree/SignatureService.php:9`: `public $digest;`
- `lib/Braintree/Error/Validation.php:22`: `#[\AllowDynamicProperties]`
- `README.md:26`: `PHP version >= 7.3 is required. The Braintree PHP SDK is tested against PHP versions 7.4, 8.2, 8.3, 8.4 and 8.5.`
- `lib/Braintree/AchMandate.php:12`: `// TODO: Review removing in NEXT_MAJOR_VERSION`

## Related

- [[changelog-github-braintree-php]] - package-qualified release ledger
- [[braintree-server-sdk]] - shared server integration boundary
- [[source-github-braintree-node]] - independent Node.js implementation evidence
- [[braintree-web-sdk]] - browser tokenization and nonce boundary
- [[recurring-payments]] - cross-provider recurring-payment concepts
- [[paypal-braintree-integration]] - PayPal client and Braintree processing boundary

## Raw Sources

- Snapshot manifest: `raw/github/braintree/braintree_php/snapshots/2026-10-29-b116668/manifest.json`
- Release manifest: `raw/github/braintree/braintree_php/releases/braintree_php/6.40.0/2026-10-29/manifest.json` - adjacent empty release-notes.md
- Comparison: `tracking/github/repos/braintree/braintree_php/comparisons/braintree_php/6.39.0--6.40.0/comparison.json` - adjacent comparison.md/diff.patch
- Runtime guidance: `raw/github/braintree/braintree_php/snapshots/2026-10-29-b116668/files/README.md`
- Package requirements: `raw/github/braintree/braintree_php/snapshots/2026-10-29-b116668/files/composer.json`
- Signing service: `raw/github/braintree/braintree_php/snapshots/2026-10-29-b116668/files/lib/Braintree/SignatureService.php`
- Validation object: `raw/github/braintree/braintree_php/snapshots/2026-10-29-b116668/files/lib/Braintree/Error/Validation.php`
- ACH mandate: `raw/github/braintree/braintree_php/snapshots/2026-10-29-b116668/files/lib/Braintree/AchMandate.php`
- Repository changelog: `raw/github/braintree/braintree_php/snapshots/2026-10-29-b116668/files/CHANGELOG.md`
- Snapshot manifest: `raw/github/braintree/braintree_php/snapshots/2026-10-29-883a219/manifest.json`
- Release manifest: `raw/github/braintree/braintree_php/releases/braintree_php/6.39.0/2026-10-29/manifest.json` - adjacent empty release-notes.md
- Comparison: `tracking/github/repos/braintree/braintree_php/comparisons/braintree_php/6.38.0--6.39.0/comparison.json` - adjacent comparison.md/diff.patch
- Transaction gateway: `raw/github/braintree/braintree_php/snapshots/2026-10-29-883a219/files/lib/Braintree/TransactionGateway.php`
- Transaction class: `raw/github/braintree/braintree_php/snapshots/2026-10-29-883a219/files/lib/Braintree/Transaction.php`
- Verification wrapper: `raw/github/braintree/braintree_php/snapshots/2026-10-29-883a219/files/lib/Braintree/CreditCardVerification.php`
- Verification gateway: `raw/github/braintree/braintree_php/snapshots/2026-10-29-883a219/files/lib/Braintree/CreditCardVerificationGateway.php`
- Error constants: `raw/github/braintree/braintree_php/snapshots/2026-10-29-883a219/files/lib/Braintree/Error/Codes.php`
- Result/validation helper: `raw/github/braintree/braintree_php/snapshots/2026-10-29-883a219/files/lib/Braintree/Util.php`
- Repository changelog: `raw/github/braintree/braintree_php/snapshots/2026-10-29-883a219/files/CHANGELOG.md`
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
