---
title: "PayPal Vault (Payment Method Tokens)"
type: concept
category: technology
tags: [paypal, vault, payment-tokens, setup-token, stored-credentials, recurring-payments, subscriptions]
---

# PayPal Vault (Payment Method Tokens)

PayPal's Vault is a tokenization system that stores a buyer's payment method so merchants can charge them later without buyer interaction. It underpins recurring payments, subscriptions, and "save for later" flows.

## APIs Involved

- **Payment Method Tokens v3 API** — creates and manages setup tokens and payment tokens
- **Orders v2 API** — used with a vault ID (`vault_id`) for subsequent merchant-initiated charges

## Braintree PayPal v6 React Paths

`@paypal/react-paypal-js@9.3.0` adds two Braintree-specific consent paths:

- a billing-agreement session for vault-only, recurring, subscription, unscheduled, or installment plans; and
- checkout with vault, which combines a one-time charge and billing-agreement consent.

These paths use `BraintreePayPalProvider`, a Braintree client token, and `paypalCheckoutV6`. Approval data is converted to a payment-method nonce with `tokenizePayment()`, then processed server-side with a Braintree SDK. They are not Payment Method Tokens v3 or Orders v2 vault flows. See [[paypal-braintree-integration]].

## Token Types

| Token | Created by | Lifetime | Purpose |
| ----- | ---------- | -------- | ------- |
| **Setup token** | `POST /v3/vault/setup-tokens` | 3 days | Represents buyer's in-progress consent flow |
| **Payment token** | `POST /v3/vault/payment-tokens` (upgrades setup token) | Persistent | Stored credential used for future charges |

## Flow

1. Merchant creates a setup token (with billing plan and `usage_pattern`)
2. Buyer approves via PayPal pop-up (`createVaultSetupToken` JS SDK callback)
3. `onApprove` fires with `data.vaultSetupToken`
4. Merchant upgrades to payment token (`paymentTokensCreate`)
5. Merchant stores the payment token ID (`vault_id`)
6. For each recurring charge: `ordersCreate` with `vault_id` + `stored_credential`

### v6 sample server boundary at `b5f2df2`

The current sample implements PayPal and card save-without-purchase by creating a setup token, collecting browser approval, and upgrading it with `VaultController.createPaymentToken()`. The resulting long-lived token is passed to a placeholder database function and deliberately not returned to the browser. Purchase-with-vault examples separately set `storeInVault: ON_SUCCESS` for PayPal and Apple Pay orders.

This is orchestration evidence, not a production token store: `savePaymentTokenToDatabase()` remains unimplemented in the sample.

### Version 10.0.1 package evidence

`@paypal/paypal-js@10.0.1` adds optional `vaultSetupToken` to the legacy Buttons `OnApproveData` type. Its expanded `createVaultSetupToken` JSDoc covers PayPal and Venmo vault-without-purchase: return a server-created Vault API setup token, using `payment_source.venmo` for Venmo. In these flows, `onApprove` returns `data.vaultSetupToken` while `data.orderID` is empty.

### Version 10.0.3 v6 package evidence

`@paypal/paypal-js@10.0.3` adds a typed v6 Venmo vault-without-payment path to the `venmo-payments` component. `createVenmoSavePaymentSession()` accepts save-session callbacks, and approval returns `{ vaultSetupToken }`. The session's `start()` accepts the existing Venmo `auto`, `popup`, or `modal` presentation options plus an optional promise resolving to `{ vaultSetupToken }`.

This package evidence establishes the public TypeScript contract at `10.0.3`; it does not independently prove production eligibility, account enablement, or runtime behavior owned by `paypal/paypal-checkout-components`.

### checkout-components `5.0.425` runtime evidence

The matching checkout runtime provides a Venmo `VAULT_WITHOUT_PURCHASE` funding flow and a `createVaultSetupToken` prop on its protected Venmo component. The funding path is disabled unless the `venmoVaultWithoutPurchase` experiment is true, and vaultable display state cannot be combined with shipping callbacks for native app-switch or QR flows.

This closes the earlier package-only evidence gap at the source-code level, but it does not resolve merchant availability: both the package and runtime can expose staged or gated contracts. Current product documentation and account eligibility remain required before offering Venmo save-without-purchase.

> [!warning] Contradiction — Venmo save without purchase
> The 2025 Save Payment Methods and Pay with Venmo documentation says Venmo is not supported for save-for-purchase-later, while `@paypal/paypal-js@10.0.3` explicitly types a Venmo save-payment session for vault setup without a purchase. This may be a newer v6 capability, a staged/unreleased runtime contract, or a documentation lag. Do not promise merchant availability from the type declaration alone; verify current product documentation, account eligibility, and the matching runtime SDK.

## `stored_credential` Fields (for subsequent charges via Orders API)

> [!warning] Two separate APIs, two different schemas
> `usage_pattern` belongs to the **Payment Method Tokens v3 API** (setup token creation). The **Orders v2 API** `stored_credential` object uses `payment_type` instead. Mixing them causes `MISSING_REQUIRED_PARAMETER`. Verified against sandbox 2026-04-22.

```json
{
  "payment_initiator": "MERCHANT",
  "payment_type": "RECURRING",
  "usage": "SUBSEQUENT",
  "previous_network_transaction_reference": {
    "id": "<network_txn_id from first capture>",
    "network": "VISA"
  }
}
```

`previous_network_transaction_reference.id` comes from `purchase_units[0].payments.captures[0].network_transaction_reference.id` in the first transaction response. Store it — it is required for all subsequent charges.

## `payment_type` Values (Orders API `stored_credential`)

- `RECURRING` — scheduled recurring charge (subscription)
- `UNSCHEDULED` — merchant-initiated, no fixed schedule
- `ONE_TIME` — single use of stored credential

## `usage_pattern` Values (Payment Method Tokens v3 API only)

- `SUBSCRIPTION_PREPAID` / `SUBSCRIPTION_POSTPAID` — subscription billing plan
- `RECURRING_POSTPAID` — recurring without fixed schedule
- Unscheduled and installment patterns also available

## Server SDK

The exact `@paypal/paypal-server-sdk@2.3.0` baseline uses `VaultController`:

- `vaultController.createSetupToken()` — create a setup token
- `vaultController.createPaymentToken()` — create a payment token from an approved source
- `vaultController.listCustomerPaymentTokens()`, `getPaymentToken()`, and `deletePaymentToken()` — manage customer tokens

Its generated model surface includes PayPal, Venmo, Apple Pay, card, bank, and token request/response shapes. That type coverage does not establish merchant eligibility or regional availability; the package README labels its Vault controller US-only. See [[source-github-paypal-typescript-server-sdk]].

### Exact REST contract baseline at `90e8041`

Payment Method Tokens 3.4 defines create/list/get/delete payment tokens and create/get setup tokens. Its payment-source union includes card, PayPal, Venmo, and Apple Pay; wallet `usage_pattern` belongs to this Vault contract. Orders 2.32 separately uses `stored_credential.payment_type` for subsequent card charges. These schemas confirm contract shape, not rollout or merchant eligibility. See [[source-github-paypal-rest-api-specifications]].

## Eligibility

- US buyers and merchants only (for recurring payments module)
- Card vaulting requires **Expanded Checkout approval**; supported in 35 countries (AU, AT, BE, BG, CA, CN, CY, CZ, DK, EE, FI, FR, DE, HK, HU, IE, IT, **JP**, LV, LI, LT, LU, MT, NL, NO, PL, PT, RO, SG, SK, SI, ES, SE, GB, US)
- **Venmo** can be vaulted during purchase. The older Vault Payment Methods guidance says save-for-purchase-later is unsupported, but the `@paypal/paypal-js@10.0.3` v6 type surface now declares a Venmo save-payment session; treat availability as unresolved pending matching runtime and product evidence.

## Relevant Companies

- [[paypal]] — PayPal company overview

## Save PayPal Wallet (during purchase, Android SDK)

Uses `PayPalWebCheckoutClient` (browser-based web checkout) - not `CardClient`. At `paypal-android@2.3.0`, the older listener examples are version 1 history:

- **Deep link**: requires `deepLinkUrlScheme` (e.g. `"com.myapplication.android"`) for browser return
- **Start**: `start(activity, request, callback)` reports browser-presentation success or failure; the synchronous two-argument overload is deprecated
- **Finish**: `finishStart(intent)` reports `Success`, `Canceled`, `Failure`, or `NoResult`
- **Returning payer**: pass saved `vault.id` as payment source in next Create Order — no `customer.id` in body
- **Create Order payload**: identical to JS SDK PayPal vault (`store_in_vault: ON_SUCCESS`, `usage_type: MERCHANT`, `customer_type: CONSUMER`)
- **APPROVED vs VAULTED** + webhook — same pattern as all other vault integrations

## Save PayPal Wallet (during purchase, iOS SDK)

Uses `PayPalWebCheckoutClient` - same pattern as Android but Swift/SwiftUI. The older product guide below uses the version 1 delegate API; `paypal-ios@2.0.1` uses completion `Result` or async/await instead.

- **Button**: `PayPalButton.Representable()` (SwiftUI)
- **Version 2 result**: `start(request:completion:)` returns `Result<PayPalWebCheckoutResult, CoreSDKError>`; async `start(request:)` is also available
- **Version 1 history**: `PayPalWebCheckoutDelegate` with success, failure, and cancellation callbacks
- **Availability**: 35 countries (unlike iOS card vault which says US only)
- **Returning payer**: `vault.id` as payment source — same as Android
- **Snippet uses `environment: .live`** — may require live environment testing

## Save Cards (during purchase, iOS SDK)

Same server-side payload and `customer.id` returning payer pattern as Android SDK. iOS-specific differences:

- **UI**: SwiftUI `Toggle` (vs Android Compose `Checkbox`)
- **Client**: `CardClient(config: coreConfig)` — no `activity` context needed
- **Version 2 result**: `approveOrder(request:completion:)` returns `Result<CardResult, CoreSDKError>`; async `approveOrder(request:)` is also available
- **Version 1 history**: `CardDelegate` callbacks remain relevant only to 1.x integrations
- **SCA enum**: `.scaAlways` / `.scaWhenRequired` (vs `SCA.SCA_ALWAYS`)

> [!warning] Contradiction — iOS card vault availability
> This page states **US only**, while Android SDK and JS SDK card vaults both support 35 countries. May be a documentation error — verify before assuming geographic restriction.

## Save Cards (during purchase, Android SDK)

Same vault pattern as JS SDK but with Android-specific differences:

- **Returning payer**: `customer.id` passed in `payment_source.card.attributes.customer.id` in Create Order body — not via `target_customer_id` in a token request
- **PCI handling**: `CardClient.approveOrder()` handles card data and PCI compliance; requires `returnUrl` with custom app scheme
- **Version 2 callback**: `approveOrder(request, CardApproveOrderCallback)` returns `Success`, `Failure`, or `AuthorizationRequired`
- **3DS completion**: present the returned challenge, then pass the deep-link intent to `finishApproveOrder(intent)`
- **APPROVED vs VAULTED** + `VAULT.PAYMENT-TOKEN.CREATED` webhook — same pattern as all other vault integrations
- **RTAU**: subsequent next step links to real-time account updater

## Save PayPal for Purchase Later (JS SDK)

Uses `window.paypal.Buttons({ createVaultSetupToken, onApprove })` — same Buttons component as checkout but with `createVaultSetupToken` instead of `createOrder`:

- Load SDK with `data-user-id-token`; returning payer: `target_customer_id` in token request
- Setup token: `POST /v3/vault/setup-tokens` with `payment_source.paypal` + `experience_context` (return/cancel URLs required)
- Payer approves in PayPal pop-up → `onApprove({ vaultSetupToken })`
- Server upgrades to payment token: `POST /v3/vault/payment-tokens`
- `merchant-id` param included in SDK script tag (unique to this guide)

## Save PayPal for Purchase Later (iOS SDK)

Uses `PayPalWebCheckoutClient.vault()` - the same client as web payments:

- **Module**: `PayPalWebPayments`
- **Request**: `PayPalVaultRequest(setupTokenID:)` — no `fundingSource` param
- **Version 2 result**: `vault(_:completion:)` returns `Result<PayPalVaultResult, CoreSDKError>`; async `vault(_:)` is also available
- **Cancellation**: reported as `PayPalError.vaultCanceledError`, not a separate delegate callback
- **Version 1 history**: the older guide uses `PayPalVaultDelegate` via `vaultDelegate`
- **Usage-type discrepancy**: the older guide uses `PLATFORM`, while the `2.0.1` repository demo uses `MERCHANT`
- **`environment: .sandbox`** — unlike iOS card purchase-later which uses `.live`

> [!warning] iOS PayPal vault `usage_type` discrepancy
> The older iOS purchase-later guide sends `PLATFORM`; the `paypal-ios@2.0.1` demo sends `MERCHANT`. This may reflect platform-facilitated versus direct-merchant context or documentation drift. Verify the merchant model before choosing a value.

## Save Cards for Purchase Later (iOS SDK)

Swift equivalent of Android cards purchase-later. Uses `CardClient.vault()`:

- **Installation**: CardPayments framework via SPM (`https://github.com/paypal/paypal-ios/`)
- **Version 2 result**: `vault(_:completion:)` returns `Result<CardVaultResult, CoreSDKError>`; async `vault(_:)` is also available
- **Cancellation**: reported as `CardError.threeDSecureCanceledError` when the 3DS challenge is canceled
- **Version 1 history**: the older guide uses `CardVaultDelegate` callbacks
- **Setup token status**: `CREATED` (same as Android, no payer action for cards)
- **Returning customer**: `customer.id` in setup token request body
- **`environemnt: .live` typo** — same as iOS card during-purchase guide

## Save PayPal for Purchase Later (Android SDK)

Uses `PayPalWebCheckoutClient.vault()` — same client as during-purchase, vault-specific method:

- **Module**: `paypal-web-payments`
- **Request**: `PayPalWebVaultRequest(setupTokenId)`
- **Presentation result**: `vault(activity, request)` returns success or failure for launching the browser challenge
- **Completion result**: `finishVault(intent)` returns `Success`, `Failure`, `Canceled`, or `NoResult`
- **Setup token**: `usage_type: PLATFORM` (vs `MERCHANT` in during-purchase — potential doc inconsistency)
- **Setup token status**: `PAYER_ACTION_REQUIRED` (unlike cards which return `CREATED`)

> [!warning] `usage_type` discrepancy
> Purchase-later Android PayPal uses `PLATFORM`; during-purchase Android and JS SDK purchase-later use `MERCHANT`. May reflect platform-facilitated vs direct merchant payments — verify before deploying.

## Save Cards for Purchase Later (Android SDK)

Uses `CardClient.vault()` — not `approveOrder()`. Key distinctions:

- **Version 2 callback**: `CardVaultCallback` receives `Success`, `Failure`, or `AuthorizationRequired`
- **Challenge completion**: `finishVault(intent)` resolves the returned deep link
- **Setup token status**: `CREATED` (not `PAYER_ACTION_REQUIRED`)
- **Returning customer**: `customer.id` in setup token request body
- **Result**: `CardVaultResult.setupTokenID` → send to server → upgrade to payment token
- **`CoreConfig`** uses `.live` environment in snippet (same pattern as iOS PayPal vault)

## Save PayPal (Payment Method Tokens API — server-side)

Pure server-side; no client SDK. Requires billing agreement / reference transaction approval from account manager.

- **Setup token**: `usage_type: MERCHANT` (not `PLATFORM`); includes `shipping_preference: SET_PROVIDED_ADDRESS` and `payment_method_preference: IMMEDIATE_PAYMENT_REQUIRED` — not seen in other guides
- **`description`** field on PayPal payment source (payer-visible)
- **Setup token expires after 3 days** — explicitly documented
- **Merchant Customer ID** optional field for mapping to internal system
- **`PayPal-Client-Metadata-Id` header** in off-session Orders API request

## Save Cards (Payment Method Tokens API — server-side SAQ D)

Pure server-side; raw card number in setup token request — PCI SAQ D required. Three verification modes:

| Mode | `verification_method` | Status | Notes |
| --- | --- | --- | --- |
| None | (absent) | `APPROVED` | Format check only |
| Smart auth | `SCA_WHEN_REQUIRED` | `APPROVED` | Zero-value auth; minimal hold if unsupported (not auto-voided) |
| 3D Secure | `SCA_WHEN_REQUIRED`/`SCA_ALWAYS` | `PAYER_ACTION_REQUIRED` | Payer redirected; GET setup token after approval for 3DS data |

- **`experience_context`** with `brand_name`/`locale` on card setup token (unusual — typically for PayPal)
- **Off-session charge**: list tokens by `customer_id` → `payment_source.card.vault_id` in Orders API
- **Sandbox AVS/CVV testing**: set Address Line 1 to `AVS_X_NNN` values; set CVV to specific codes (see source)

## Save Cards for Purchase Later (JS SDK)

No purchase transaction — pure vault flow using setup token → payment token:

1. Server: `POST /v3/vault/setup-tokens` with empty `payment_source.card: {}`
2. Client: `createVaultSetupToken` callback (replaces `createOrder` — **cannot coexist**)
3. Payer fills CardFields → SDK updates setup token
4. `onApprove` returns `{ vaultSetupToken }` (+ `liabilityShift` for 3DS)
5. Server: `POST /v3/vault/payment-tokens` → payment token + `customer.id`

**Security**: don't expose token IDs client-side — create separate IDs server-side.

## Save for Purchase Later (off-session)

The 2025 integration matrix says all four paths (JS SDK, Payment Method Tokens API, Android SDK, and iOS SDK) support PayPal and cards, with no Venmo purchase-later path. The later `@paypal/paypal-js@10.0.3` declaration conflicts with that matrix by adding a v6 Venmo save-payment session; use package-qualified evidence and verify the deployed runtime before treating Venmo as supported.

JS SDK caveat: client-side only integration saves PayPal Wallets only; client+server (Expanded Checkout) required to also save cards.

See [[source-paypal-save-payment-methods]] for integration path table.

## Save PayPal Wallet (during purchase, Orders API)

Server-side only, no client SDK. Requires **reference transaction approval** (contact account manager).

- **Two-step flow**: Create order → `PAYER_ACTION_REQUIRED` → payer approves via redirect → capture
- **`experience_context`**: `return_url` + `cancel_url` required; no `data-user-id-token`
- **`customer_type`** absent from payload (unlike JS SDK which includes it)
- **Webhook `VAULT.PAYMENT-TOKEN.DELETION-INITIATED`** — only documented on this page
- **No Venmo** support

## Save Cards (during purchase, Orders API)

For merchants who are PCI SAQ D compliant. Raw card `number` + `expiry` passed directly in the Create Order body — no client-side SDK component.

- **Single-step**: create + capture in one request (no separate approve step)
- **3DS**: `payment_source.card.attributes.verification.method: SCA_WHEN_REQUIRED` inline; `PAYER_ACTION_REQUIRED` returned if triggered
- **Limitation**: Orders API supports PayPal and card only — no Venmo
- **Returning payer**: no `customer.id` shown in this guide (unlike SDK flows)
- **APPROVED vs VAULTED** + webhook — same pattern

See [[source-paypal-save-cards-orders-api]] for full detail.

## Save Venmo (during purchase, JS SDK)

Venmo vault follows the same pattern as PayPal Wallet but with key restrictions:

- **US only** — no other countries supported
- **No sandbox** — must test in the live environment; use [Venmo testing guidelines](https://developer.paypal.com/docs/checkout/pay-with-venmo/integrate/#link-testandgolive)
- **payment_source field**: `venmo` (not `paypal`); `customer_type` field is absent from the payload
- **Desktop fallback**: QR code shown if Venmo app not installed
- **Incompatible callbacks**: `onShippingAddressChange`, `onShippingChange`, `onShippingOptionsChange` cannot be used
- **Richer capture response**: includes `user_name` (Venmo handle) and full address (vs PayPal Wallet which returns only `country_code`)

## Save PayPal Wallet (during purchase, JS SDK)

A distinct vault path that uses the Orders v2 API rather than the setup token flow:

1. Generate user ID token: `POST /v1/oauth2/token` with `response_type=id_token`
2. For returning payers, include `target_customer_id` (PayPal-generated ID, not your internal ID)
3. Load JS SDK with `data-user-id-token="YOUR-ID-TOKEN"` — triggers vault-aware button rendering
4. Create order with `payment_source.paypal.attributes.vault.store_in_vault: ON_SUCCESS`
5. After capture: `vault.id` + `customer.id` returned in response

The `customer.id` is a PayPal-generated identifier — store it against the payer in your system. On return visits, pass it via `target_customer_id` in the token request; the SDK renders saved methods as one-click buttons automatically.

## Sources

- [[source-paypal-checkout-recurring-payment]] — Full recurring payments integration guide
- [[source-paypal-save-payment-methods]] — Save payment methods overview: two vault modes, 34-country eligibility, Venmo vault limitation, integration path table; JS SDK PayPal vault flow (`data-user-id-token`, `target_customer_id`, Create Order payload, APPROVED/VAULTED); Venmo vault (US-only, no sandbox, incompatible callbacks, `user_name` response field)
- [[source-paypal-save-paypal-payment-tokens-api]] — Payment Method Tokens API PayPal vault: billing agreement approval required, `shipping_preference`, `payment_method_preference: IMMEDIATE_PAYMENT_REQUIRED`, 3-day expiry, `PayPal-Client-Metadata-Id` header
- [[source-paypal-save-cards-payment-tokens-api]] — Payment Method Tokens API card vault: SAQ D, 3 verification modes (none/smart-auth/3DS), AVS/CVV test tables, off-session charge via `vault_id`
- [[source-paypal-save-paypal-purchase-later-ios-sdk]] — iOS SDK PayPal purchase-later: `PayPalVaultDelegate`, `PayPalVaultRequest`, `usage_type: PLATFORM`, `PAYER_ACTION_REQUIRED` status
- [[source-paypal-save-cards-purchase-later-ios-sdk]] — iOS SDK cards purchase-later: `CardVaultDelegate`, `cardVaultDidCancel`, `CREATED` setup token status, `customer.id` in setup token body
- [[source-paypal-save-paypal-purchase-later-android-sdk]] — Android SDK PayPal purchase-later: `PayPalWebCheckoutClient.vault()`, `usage_type: PLATFORM` (vs MERCHANT elsewhere), `PAYER_ACTION_REQUIRED` status
- [[source-paypal-save-cards-purchase-later-android-sdk]] — historical Android version 1 card-vault guide, `CREATED` setup token status, and `customer.id` in setup token body
- [[source-paypal-save-paypal-purchase-later-js-sdk]] — JS SDK PayPal purchase-later: Buttons with `createVaultSetupToken`, setup token with `experience_context`, `merchant-id` param, pop-up approval
- [[source-paypal-save-cards-purchase-later-js-sdk]] — JS SDK cards purchase-later: setup token → payment token, `createVaultSetupToken` replaces `createOrder`, 3DS option, token ID security note, 14 test cards
- [[source-paypal-save-paypal-orders-api]] — Orders API PayPal Wallet vault: reference transaction approval required, two-step flow, `experience_context`, `VAULT.PAYMENT-TOKEN.DELETION-INITIATED` webhook
- [[source-paypal-save-cards-orders-api]] — Orders API card vault: SAQ D required, raw card in request, single-step capture, no Venmo support
- [[source-paypal-save-paypal-ios-sdk]] — iOS SDK PayPal Wallet vault: `PayPalWebCheckoutClient`, `PayPalWebCheckoutDelegate`, 35 countries, `vault.id` for returning payers
- [[source-paypal-save-cards-ios-sdk]] — iOS SDK card vault: SwiftUI Toggle, `CardDelegate` protocol, US-only availability (contradicts Android/JS SDK 35-country support)
- [[source-paypal-save-paypal-android-sdk]] — Android SDK PayPal Wallet vault: `PayPalWebCheckoutClient`, deep link scheme, `vault.id` for returning payers, identical payload to JS SDK
- [[source-paypal-save-cards-android-sdk]] — historical Android version 1 listener guide plus Compose checkbox UX, returning-payer `customer.id`, and RTAU
- [[source-paypal-save-applepay-js-sdk]] — Apple Pay vault: APPROVED vs VAULTED status, VAULT.PAYMENT-TOKEN.CREATED webhook, merchant-initiated recurring pattern
- [[source-paypal-save-cards-js-sdk]] — Card vault JS SDK: checkbox UX, SCA_ALWAYS/SCA_WHEN_REQUIRED with vault, usage_type/customer_type/permit_multiple_payment_tokens fields, 14 test cards
- [[source-github-paypal-js]] — versioned core v10.0.1 legacy Buttons setup-token approval types plus React Braintree billing-agreement, checkout-with-vault, and Pay Later evidence
- [[source-github-paypal-checkout-components]] — package-qualified runtime, Venmo setup-token, and eligibility evidence
- [[source-github-paypal-ios]] — cumulative native iOS evidence through `paypal-ios@2.0.1`, including v2 Result/async APIs, cancellation handling, and the no-native-Venmo enum boundary
- [[changelog-github-paypal-ios]] — package-qualified iOS major-version and patch history
- [[source-github-paypal-android]] — cumulative native Android evidence through `paypal-android@2.3.0`, including v2 callbacks, manual browser completion, and the native Venmo evidence boundary
- [[source-github-v6-web-sdk-sample-integration]] — current Web SDK setup-token, payment-token, and purchase-with-vault sample paths
- [[changelog-github-paypal-android]] — package-qualified Android major-version and `2.3.0` callback history
- [[source-github-paypal-rest-api-specifications]] — exact-SHA Payment Method Tokens 3.4 and Orders 2.32 schema boundary
