---
title: "GitHub: braintree/braintree_ruby"
type: source
date_ingested: 2026-08-23
date_updated: 2026-10-29
original_format: github-repo
raw_files:
  - "github/braintree/braintree_ruby/snapshots/2026-10-29-647f4bb/manifest.json"
  - "github/braintree/braintree_ruby/snapshots/2026-10-29-f3d7014/manifest.json"
  - "github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/manifest.json"
tags: [braintree, ruby-sdk, server-sdk, checkout, paypal, venmo, subscriptions, webhooks, github-repository]
---

## Overview

`braintree/braintree_ruby` is Braintree's Ruby server SDK. The retained history begins with `braintree@4.40.0` at exact SHA `1217992763cc13f33dbd8b6c51ad2ae058ddd2a8`, released on 2026-08-05.

Repository: <https://github.com/braintree/braintree_ruby>

Latest ingested Ruby release: `braintree@4.42.0`, exact SHA `647f4bb8a45a869cb4d664077d28287881d299b1`. The full 4.41.0 and delta 4.42.0 records below preserve all 4.40.0 implementation and release history; identically named Node packages remain separate evidence.

## Evidence Boundary

- For 4.42.0 the user approved delta mode with focused reading: all changed implementation, affected prior context, comparison and cumulative wiki history; generated inventories and unchanged changelog history mechanically verified. The capsule has 201 files: seven modified and 194 unchanged; 17 upstream dispositions comprise seven retained and ten excluded spec changes, with no packet gaps or unclassified changes. No Ruby/gateway/payment execution or publication.
- For 4.41.0 the user approved full additive mode with focused reading. All 21 modified retained files were read fully (new changelog block; 1,308 old lines verified mechanically), affected prior comparison code and cumulative wiki history, plus the unchanged shared Util helper. Both 201-file capsules pass 402 size/SHA-256/Git blob identities; 21 modified/180 unchanged, 46 upstream dispositions (21 retained/25 exclusions), no packet gaps/unclassified changes. Effective full assignment210 paths. Unchanged source, manifests and inventories are mechanically verified, not a new whole-repository semantic read. No Ruby/gem/gateway/payment execution, collection-policy expansion, commit or push.
- This source proves implementation present in `braintree@4.40.0`; it does not replace current product documentation or prove merchant, buyer, country, currency, or payment-method eligibility.
- Browser and native SDKs independently collect payment details or wallet approval and return a payment-method nonce or vaulted token. This package performs server-side gateway operations.
- PayPal customer-session recommendations are experimental in this source. The presence of PAYPAL and VENMO enum values or app-installed inputs does not establish general availability.
- The upstream release record has no release-note body. Exact `4.40.0` changes come from the retained repository changelog and implementation.
- Checkout, vault, transactions, subscriptions, webhooks, and payment-method processing receive detailed treatment. Disputes, OAuth, onboarding, reporting, local payments, disbursement, and exchange rates remain inventory-level evidence for rough queries.

## Grounding Excerpts

> "The Braintree gem provides integration access to the Braintree Gateway."
>
> `raw/github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/files/README.md:3`

> "The Braintree Ruby SDK is tested against Ruby versions 2.6, 2.7, 3.0, 3.4, and 4.0"
>
> `raw/github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/files/README.md:27`

> "The Venmo SDK integration is Unsupported. Please update your integration to use Pay with Venmo instead."
>
> `raw/github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/files/lib/braintree/transaction_gateway.rb:14`

> "This class is experimental and may change in future releases."
>
> `raw/github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/files/lib/braintree/graphql/inputs/customer_recommendations_input.rb:4`

## Server Integration Model

The merchant creates a `Braintree::Gateway` with Sandbox or Production configuration. The package supports merchant ID plus public/private keys, an OAuth access token, or OAuth client credentials, and rejects mixed credential types. It uses REST API version 6 for the XML gateway and a dated GraphQL contract for selected newer services.

The gateway exposes client tokens, customers, payment methods and nonces, transactions, card verification, PayPal accounts and payment-resource updates, plans, subscriptions, and webhooks. It also retains local-payment contexts, SEPA and US bank accounts, disputes, OAuth, merchant accounts, document upload, settlement summaries, and exchange-rate quotes.

Ruby calls return successful or error result objects for gateway validation outcomes. Bang variants such as `sale!` and `create!` return the requested resource or raise `Braintree::ValidationsFailed`; transport failures use typed exceptions for authentication, authorization, not found, timeout, rate limiting, upgrade requirements, and server availability.

## Runtime and Configuration

The gemspec requires Ruby 2.6 or later, `builder >= 3.2.4`, and `rexml >= 3.1.9`. The README says the package is tested on Ruby 2.6, 2.7, 3.0, 3.4, and 4.0. Nokogiri can be used for faster XML parsing; otherwise the implementation falls back to REXML.

Major version 4 is Active, while 3.x and 2.x are deprecated and no longer receive security patches. The README separately warns that SDK releases older than 2.82.0 contain certificates expiring on 2026-03-30 and that impacted traffic will fail after that date.

## Client Tokens, Nonces, and Vaulting

`client_token.generate` defaults to token version 2 and accepts customer, merchant-account, proxy-merchant, address, domain, and card-verification options. Customer-scoped options require a customer ID. Unlike the independently retained Node `3.39.0` and PHP `6.37.0` packages, the Ruby `4.40.0` client-token signature does not expose `preferredPaymentMethodToken`; do not assume optional-field parity across languages.

Customers aggregate cards, PayPal accounts, Venmo accounts, Apple Pay, Google Pay, SEPA, and US bank accounts. Payment methods can be created, found, updated, deleted, granted, and revoked. A vaulted token can be exchanged for a fresh payment-method nonce, including recurring-consent authentication-insight options. A nonce is a processing input, not by itself a durable credential or proof of payment-method eligibility.

## Transaction Lifecycle

`transaction.sale` accepts amount, nonce or token, customer and address data, merchant account, risk and descriptor fields, line items, 3DS evidence, and processing options. `submit_for_settlement` can be requested during sale or called later. The lifecycle also includes partial settlement, authorization adjustment, package tracking, detail updates, void, refund, credit, clone, search, and subscription-charge retry.

Since `4.36.0`, `api_request_key` provides idempotency input for sale or credit, settlement submission, void, and refund. Validation codes distinguish reuse with different data, in-flight processing, prior failure, server failure, excessive length, and disallowed operations. The package also supports partial authorization and records whether processor code `1004` produced a partial authorization.

## PayPal and Venmo

PayPal account operations support create, find, update, delete, vaulted sale, and billing-agreement metadata. PayPal payment-resource updates accept amount breakdowns, line items, shipping options and address, payee data, order ID, and payment-method nonce.

The experimental GraphQL customer-session surface creates and updates PayPal sessions and can return PAYPAL or VENMO recommendations from customer, device, domain, and purchase-unit inputs. This is recommendation evidence, not general enablement proof.

Venmo is represented as a customer payment method and transaction instrument. Legacy `venmo_sdk_payment_method_code` and `venmo_sdk_session` inputs remain only with warnings that the old Venmo SDK integration is unsupported and merchants should use Pay with Venmo. This server repository does not define the current client-side Venmo experience; use the appropriate independently versioned Braintree Web, Android, or iOS evidence.

## Cards and 3D Secure

Card and verification operations support direct card data or nonces, billing addresses, merchant-account selection, verification options, and search. Transaction, card, customer, payment-method, and verification inputs can carry 3DS pass-through evidence.

`4.40.0` adds the pass-through `network` field and constants for Eftpos, Mastercard, and Visa. The SDK transports authentication evidence; the merchant still owns the client-side 3DS flow and acceptance policy.

## Plans and Subscriptions

Plan operations create, update, find, and list plans. Subscription operations create, update, find, cancel, search, and retry charges, with Active, Canceled, Expired, Past Due, and Pending states. Inputs cover plan and merchant account, payment-method token or nonce, price and billing-cycle controls, trials, descriptors, PayPal descriptions, and add-on or discount changes.

Subscription webhooks cover activation, cancellation, expiry, trial ending, past-due transitions, billing skips, and successful or failed charges. These APIs establish a Braintree recurring server surface; they do not prove that every client payment method can be vaulted or used for subscriptions.

## Webhooks, Errors, and Security

Webhook parsing requires both signature and payload. The implementation selects the merchant's public-key pair and verifies an HMAC-SHA1 signature with constant-time comparison before parsing the XML notification. Event kinds cover transactions, subscriptions, payment methods, local payments, refunds, disputes, disbursements, OAuth, and connected merchants. The testing gateway can generate samples, while settlement test operations reject in Production.

Gateway validation errors remain structured and nested. At `4.40.0`, Address and Dispute path construction validates external IDs against an allowlist to block path separators and relative segments. Security fixes apply only to the active major.

## Other Retained API Domains

The capsule also records dispute search and evidence management, document upload, OAuth connect and token operations, merchant accounts, local-payment contexts, settlement summaries, exchange-rate quotes, SEPA and US-bank verification, disbursement data, and facilitator or transfer metadata. These are searchable implementation inventory, not complete product guidance.

## `4.40.0` Release Findings

The exact release adds PayPal account validation codes `92963` for invalid email format and `92964` for excessive length; adds 3DS pass-through network fields and constants across transaction and payment-method surfaces; and fixes path traversal in Address and Dispute gateway IDs. No mandatory migration is documented.

All broader sections above describe cumulative implementation present at `4.40.0`, not features introduced by this patch.

## `4.41.0` Additive Full Ingest

**Identity:** Ruby gem braintree@4.41.0 at f3d70148cb0a68e8a20160b9a8e4e01e7d79d1df, from 4.40.0. The release manifest's September 16, 2026 timestamp is tag/commit-derived evidence; there is no GitHub Release-note body/publication record. Collected/ingested October 29. Full mode is the user's override for broad security-related behavior, not the collector's delta recommendation. All 4.40.0 history remains intact.

### Preferred Payment Method Token

client_token.generate accepts preferred_payment_method_token as a symbol or string key and sends it under payment_method_id. It first shallow-copies the options hash, preserving the caller's top-level input while applying default version/remapping. If both key forms are present, the symbol value wins and the string alias is removed. The option is validated against the expanded public signature before remapping; gateway response still returns the client-token string or raises ArgumentError for an API error response. The retained local option validator does not establish token ownership, customer-token association, token validity or feature enablement; those remain server/product responsibilities.

This adds the Ruby SDK option missing in the 4.40.0 baseline. It is not a new frontend component or automatic proof of PayPal v6 saved-payment editing/returning-buyer support. The backend token-generation capability and independently versioned frontend integration must be verified separately.

### Path Validation and Migration

The existing Util.invalid_path_segment? helper checks value.to_s against `\A[A-Za-z0-9_-]+\z`. 4.41.0 extends calls across CreditCard, CreditCardVerification, Customer, MerchantAccount, PayPalAccount, PaymentMethod, PaymentMethodNonce, Plan, SepaDirectDebitAccount, Subscription, Testing, Transaction, TransactionLineItem, UsBankAccount and UsBankAccountVerification gateway paths. Customer.find also validates a truthy association_filter_id before interpolating its query field. Address/Dispute baseline protection remains historical, not newly added here.

Affected invalid identifiers raise ArgumentError locally before HTTP, not proof that an object is absent or authorized. Unlike string-only rules in other language packages, Ruby stringifies inputs; for example an integer's digit representation can pass. Some transaction operations replace a lowercase-only regex with the broader shared uppercase/digit/underscore/hyphen allowlist. Empty/nil checks and exception messages vary across callers; testing operations still check Production before the path ID. Do not state that every accepted identifier set narrowed or every body ID is validated. Subscription charge retry, for example, still places its ID in a body rather than applying this path helper. Audit custom IDs and exception handling; do not strip invalid characters to manufacture another identity. No exploit test or all-paths security guarantee was performed.

### Query, Search and Refund Changes

Http.get/delete now append the optional query hash through the existing _build_query_string helper. It joins key=value pairs, rejects nested hash-like values and performs no URL encoding or existing-query merge. The changed forwarding is not new general encoding/security protection; higher-level methods may construct their own query strings independently.

TransactionSearch adds ach_type using Transaction::AchType::SameDay=same_day and Standard=standard. This is a search filter, not a new ACH processing mode or timing guarantee. Refund's explicit signature gains surcharge_amount, with the existing scalar-amount/hash-options forms, API request key and result/error handling. Acceptance, amount rules and successful refund remain gateway decisions. Transaction's existing ACH/TLID/surcharge response readers are not new merely because the file changed.

README, gemspec, runtime requirements, credentials, webhook parser and legacy Venmo warnings are unchanged. The 4.40.0 runtime/PayPal/3DS/subscription knowledge remains version-qualified above, not reattributed as 4.41.0 features. No new cross-company comparison or source count change.

### Grounding Excerpts

All locations below are in `raw/github/braintree/braintree_ruby/snapshots/2026-10-29-f3d7014/files/`:
- `lib/braintree/client_token_gateway.rb:12`: `options = options.dup`
- `lib/braintree/client_token_gateway.rb:21`: `options[:payment_method_id] = options.delete(:preferred_payment_method_token)`
- `lib/braintree/util.rb:5`: `!value.to_s.match?(/\A[A-Za-z0-9_-]+\z/)`
- `lib/braintree/http.rb:23`: `full_path = path + _build_query_string(query_params)`
- `lib/braintree/transaction_search.rb:49`: `multiple_value_field :ach_type, :allows => Transaction::AchType::All`

## `4.42.0` Delta Ingest

**Identity:** Ruby gem `braintree@4.42.0`, exact SHA `647f4bb8a45a869cb4d664077d28287881d299b1`, compared with 4.41.0. Collected/ingested October 29, 2026. The manifest's October 19 timestamp is tag/commit-derived, not a verified GitHub Release publication date; the release-note body is absent. All older sections above remain historical evidence.

### Transaction Reversal

`Braintree::Transaction.reverse` and `reverse!` delegate to the configured transaction gateway. `gateway.transaction.reverse(transaction_id, options = {})` validates the ID using the existing stringifying ASCII path helper and validates options against a signature containing only `api_request_key`. It posts to `/transactions/{transaction_id}/reverse`, with no body for empty options or a transaction-wrapped options body otherwise. It uses the existing transaction result handler. `reverse!` returns the transaction on success or raises `Braintree::ValidationsFailed` on a validation result; path, transport and unexpected-response exceptions remain separate.

The upstream changelog says this automatically voids or fully refunds a transaction. The SDK delegates that choice to the gateway: it does not inspect settlement status, call void/refund as a client fallback, or accept an amount for partial refund. Existing explicit void/refund APIs remain. `api_request_key` is a supported input, not proof of local retries or guaranteed server idempotency semantics. New `ErrorCodes::Transaction::CannotReverseAtThisTime` is `915282`; no universal status, instrument or merchant eligibility is established by its presence.

### Mastercard External-Vault Inputs

- Card create/update's shared `external_vault` signature adds `mastercard_transaction_link_id` alongside `network_transaction_id`. Unchanged Customer create/update signatures inherit the card signature for nested card inputs.
- Transaction create/sale's `external_vault` signature adds `previous_mastercard_transaction_link_id` alongside status and previous network transaction ID.
- Card-verification's declared create signature adds that previous Mastercard link ID. Its actual create method posts parameters directly without invoking `verify_keys`; do not describe this declaration as newly enforced local allowlisting or prove that prior verification callers rejected the field.
- Generic PaymentMethod signatures did not change. Transaction's response `mastercard_transaction_link_id` reader already existed, so it is not a new response feature here. These request inputs do not replace network IDs or establish network validation rules or merchant enablement.

Six new error constants are recorded: `CreditCard::ExternalVault::MastercardTransactionLinkIdIsInvalid` (`91767`); `Transaction::CannotReverseAtThisTime` (`915282`); `Transaction::ExternalVault::PreviousMastercardTransactionLinkIdIsInvalid` (`915279`) and `StatusWithPreviousMastercardTransactionLinkIdIsInvalid` (`915278`); `Verification::ExternalVault::PreviousMastercardTransactionLinkIdIsInvalid` (`942206`) and `StatusWithPreviousMastercardTransactionLinkIdIsInvalid` (`942205`). Names are relative to `Braintree::ErrorCodes`; these are server-validation diagnostics, not independently proven required-field rules.

### Grounding Excerpts

Locations are under `raw/github/braintree/braintree_ruby/snapshots/2026-10-29-647f4bb/files/`:
- `lib/braintree/transaction_gateway.rb:103`: `def reverse(transaction_id, options = {})`
- `lib/braintree/transaction_gateway.rb:416`: `:api_request_key,`
- `lib/braintree/credit_card_gateway.rb:123`: `{:external_vault => [:network_transaction_id, :mastercard_transaction_link_id]},`
- `lib/braintree/credit_card_verification_gateway.rb:64`: `:previous_mastercard_transaction_link_id,`
- `lib/braintree/error_codes.rb:374`: `CannotReverseAtThisTime = "915282"`

## Related

- [[changelog-github-braintree-ruby]] - package-qualified release ledger
- [[braintree]] - company and knowledge-status page
- [[braintree-server-sdk]] - shared server boundary and language-specific evidence
- [[paypal-braintree-integration]] - PayPal client approval and Braintree processing boundary
- [[recurring-payments]] - cross-provider recurring concepts

## Raw Sources

- Snapshot manifest: `raw/github/braintree/braintree_ruby/snapshots/2026-10-29-647f4bb/manifest.json`
- Release manifest: `raw/github/braintree/braintree_ruby/releases/braintree/4.42.0/2026-10-29/manifest.json` - adjacent empty release-notes.md
- Comparison: `tracking/github/repos/braintree/braintree_ruby/comparisons/braintree/4.41.0--4.42.0/comparison.json` - adjacent comparison.md/diff.patch
- Reversal and transaction inputs: `raw/github/braintree/braintree_ruby/snapshots/2026-10-29-647f4bb/files/lib/braintree/transaction_gateway.rb`
- Transaction class: `raw/github/braintree/braintree_ruby/snapshots/2026-10-29-647f4bb/files/lib/braintree/transaction.rb`
- Card inputs: `raw/github/braintree/braintree_ruby/snapshots/2026-10-29-647f4bb/files/lib/braintree/credit_card_gateway.rb`
- Verification inputs: `raw/github/braintree/braintree_ruby/snapshots/2026-10-29-647f4bb/files/lib/braintree/credit_card_verification_gateway.rb`
- Error codes: `raw/github/braintree/braintree_ruby/snapshots/2026-10-29-647f4bb/files/lib/braintree/error_codes.rb`
- Bang result handling: `raw/github/braintree/braintree_ruby/snapshots/2026-10-29-647f4bb/files/lib/braintree/base_module.rb`
- Repository changelog: `raw/github/braintree/braintree_ruby/snapshots/2026-10-29-647f4bb/files/CHANGELOG.md`
- Snapshot manifest: `raw/github/braintree/braintree_ruby/snapshots/2026-10-29-f3d7014/manifest.json`
- Release manifest: `raw/github/braintree/braintree_ruby/releases/braintree/4.41.0/2026-10-29/manifest.json` - adjacent empty release-notes.md
- Comparison: `tracking/github/repos/braintree/braintree_ruby/comparisons/braintree/4.40.0--4.41.0/comparison.json` - adjacent comparison.md/diff.patch
- Client token: `raw/github/braintree/braintree_ruby/snapshots/2026-10-29-f3d7014/files/lib/braintree/client_token_gateway.rb`
- Shared validator: `raw/github/braintree/braintree_ruby/snapshots/2026-10-29-f3d7014/files/lib/braintree/util.rb`
- Transport: `raw/github/braintree/braintree_ruby/snapshots/2026-10-29-f3d7014/files/lib/braintree/http.rb`
- Transaction gateway: `raw/github/braintree/braintree_ruby/snapshots/2026-10-29-f3d7014/files/lib/braintree/transaction_gateway.rb`
- Repository changelog: `raw/github/braintree/braintree_ruby/snapshots/2026-10-29-f3d7014/files/CHANGELOG.md`
- Snapshot manifest: `raw/github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/manifest.json`
- Release manifest: `raw/github/braintree/braintree_ruby/releases/braintree/4.40.0/2026-08-23/manifest.json`
- Release notes: `raw/github/braintree/braintree_ruby/releases/braintree/4.40.0/2026-08-23/release-notes.md` (empty upstream body)
- Repository changelog: `raw/github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/files/CHANGELOG.md`
- README: `raw/github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/files/README.md`
- Client-token gateway: `raw/github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/files/lib/braintree/client_token_gateway.rb`
- Transaction gateway: `raw/github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/files/lib/braintree/transaction_gateway.rb`
- Subscription gateway: `raw/github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/files/lib/braintree/subscription_gateway.rb`
- Webhook gateway: `raw/github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/files/lib/braintree/webhook_notification_gateway.rb`
- Validation codes: `raw/github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/files/lib/braintree/error_codes.rb`
