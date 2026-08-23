---
title: "GitHub: braintree/braintree_ruby"
type: source
date_ingested: 2026-08-23
original_format: github-repo
raw_files:
  - "github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/manifest.json"
tags: [braintree, ruby-sdk, server-sdk, checkout, paypal, venmo, subscriptions, webhooks, github-repository]
---

## Overview

`braintree/braintree_ruby` is Braintree's Ruby server SDK. The retained history begins with `braintree@4.40.0` at exact SHA `1217992763cc13f33dbd8b6c51ad2ae058ddd2a8`, released on 2026-08-05.

Repository: <https://github.com/braintree/braintree_ruby>

## Evidence Boundary

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

## Related

- [[changelog-github-braintree-ruby]] - package-qualified release ledger
- [[braintree]] - company and knowledge-status page
- [[braintree-server-sdk]] - shared server boundary and language-specific evidence
- [[paypal-braintree-integration]] - PayPal client approval and Braintree processing boundary
- [[recurring-payments]] - cross-provider recurring concepts

## Raw Sources

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
