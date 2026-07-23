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

Uses `VaultController` from `@paypal/paypal-server-sdk`:

- `vaultController.setupTokensCreate()` — create setup token
- `vaultController.paymentTokensCreate()` — upgrade to payment token

## Eligibility

- US buyers and merchants only (for recurring payments module)
- Card vaulting requires **Expanded Checkout approval**; supported in 35 countries (AU, AT, BE, BG, CA, CN, CY, CZ, DK, EE, FI, FR, DE, HK, HU, IE, IT, **JP**, LV, LI, LT, LU, MT, NL, NO, PL, PT, RO, SG, SK, SI, ES, SE, GB, US)
- **Venmo** can be vaulted during purchase (JS SDK) but is **not supported** for save-for-purchase-later (Vault Payment Methods API)

## Relevant Companies

- [[paypal]] — PayPal company overview

## Save PayPal Wallet (during purchase, Android SDK)

Uses `PayPalWebCheckoutClient` (browser-based web checkout) — not `CardClient`. Key distinctions:

- **Deep link**: requires `deepLinkUrlScheme` (e.g. `"com.myapplication.android"`) for browser return
- **Listener**: `PayPalWebCheckoutListener` with `onPayPalWebSuccess/Failure/Canceled`
- **Returning payer**: pass saved `vault.id` as payment source in next Create Order — no `customer.id` in body
- **Create Order payload**: identical to JS SDK PayPal vault (`store_in_vault: ON_SUCCESS`, `usage_type: MERCHANT`, `customer_type: CONSUMER`)
- **APPROVED vs VAULTED** + webhook — same pattern as all other vault integrations

## Save PayPal Wallet (during purchase, iOS SDK)

Uses `PayPalWebCheckoutClient` — same pattern as Android but Swift/SwiftUI:

- **Button**: `PayPalButton.Representable()` (SwiftUI)
- **Delegate**: `PayPalWebCheckoutDelegate` — `payPal(_:didFinishWithResult:)`, `payPal(_:didFinishWithError:)`, `payPalDidCancel(_:)`
- **Availability**: 35 countries (unlike iOS card vault which says US only)
- **Returning payer**: `vault.id` as payment source — same as Android
- **Snippet uses `environment: .live`** — may require live environment testing

## Save Cards (during purchase, iOS SDK)

Same server-side payload and `customer.id` returning payer pattern as Android SDK. iOS-specific differences:

- **UI**: SwiftUI `Toggle` (vs Android Compose `Checkbox`)
- **Client**: `CardClient(config: coreConfig)` — no `activity` context needed
- **Callbacks**: `CardDelegate` protocol (vs `ApproveOrderListener`)
- **SCA enum**: `.scaAlways` / `.scaWhenRequired` (vs `SCA.SCA_ALWAYS`)

> [!warning] Contradiction — iOS card vault availability
> This page states **US only**, while Android SDK and JS SDK card vaults both support 35 countries. May be a documentation error — verify before assuming geographic restriction.

## Save Cards (during purchase, Android SDK)

Same vault pattern as JS SDK but with Android-specific differences:

- **Returning payer**: `customer.id` passed in `payment_source.card.attributes.customer.id` in Create Order body — not via `target_customer_id` in a token request
- **PCI handling**: `CardClient.approveOrder()` handles card data and PCI compliance; requires `returnUrl` with custom app scheme
- **3DS callbacks**: `onApproveOrderThreeDSecureWillLaunch()` / `onApproveOrderThreeDSecureDidFinish()` on `ApproveOrderListener`
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

Uses `PayPalWebCheckoutClient.vault()` + `PayPalVaultDelegate` — same client as web payments:

- **Module**: `PayPalWebPayments`
- **Request**: `PayPalVaultRequest(setupTokenID:)` — no `fundingSource` param
- **Delegate**: `PayPalVaultDelegate` via `vaultDelegate` property — `paypal(_:didFinishWithVaultResult:)`, `paypal(_:didFinishWithVaultError:)`, `paypalDidCancel(_:)`
- **`usage_type: PLATFORM`** — consistent with Android PayPal purchase-later; both differ from during-purchase (`MERCHANT`)
- **`environment: .sandbox`** — unlike iOS card purchase-later which uses `.live`

## Save Cards for Purchase Later (iOS SDK)

Swift equivalent of Android cards purchase-later. Uses `CardClient.vault()` and `CardVaultDelegate`:

- **Installation**: CardPayments framework via SPM (`https://github.com/paypal/paypal-ios/`)
- **Delegate**: `CardVaultDelegate` — `didFinishWithVaultResult`, `didFinishWithVaultError`, `cardVaultDidCancel`, `cardThreeDSecureWillLaunch/DidFinish`
- **Setup token status**: `CREATED` (same as Android, no payer action for cards)
- **Returning customer**: `customer.id` in setup token request body
- **`environemnt: .live` typo** — same as iOS card during-purchase guide

## Save PayPal for Purchase Later (Android SDK)

Uses `PayPalWebCheckoutClient.vault()` — same client as during-purchase, vault-specific method:

- **Module**: `paypal-web-payments`
- **Request**: `PayPalWebVaultRequest(setupTokenId)`
- **Listener**: `vaultListener` with `onPayPalWebVaultSuccess/Failure/Canceled`
- **Setup token**: `usage_type: PLATFORM` (vs `MERCHANT` in during-purchase — potential doc inconsistency)
- **Setup token status**: `PAYER_ACTION_REQUIRED` (unlike cards which return `CREATED`)

> [!warning] `usage_type` discrepancy
> Purchase-later Android PayPal uses `PLATFORM`; during-purchase Android and JS SDK purchase-later use `MERCHANT`. May reflect platform-facilitated vs direct merchant payments — verify before deploying.

## Save Cards for Purchase Later (Android SDK)

Uses `CardClient.vault()` — not `approveOrder()`. Key distinctions:

- **Listener**: `CardVaultListener` with `onVaultSuccess(result: CardVaultResult)` / `onVaultFailure`
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

All 4 paths (JS SDK, Payment Method Tokens API, Android SDK, iOS SDK) support PayPal + cards. **No Venmo** on any purchase-later path.

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
- [[source-paypal-save-cards-purchase-later-android-sdk]] — Android SDK cards purchase-later: `CardClient.vault()`, `CardVaultListener`, `CREATED` setup token status, `customer.id` in setup token body
- [[source-paypal-save-paypal-purchase-later-js-sdk]] — JS SDK PayPal purchase-later: Buttons with `createVaultSetupToken`, setup token with `experience_context`, `merchant-id` param, pop-up approval
- [[source-paypal-save-cards-purchase-later-js-sdk]] — JS SDK cards purchase-later: setup token → payment token, `createVaultSetupToken` replaces `createOrder`, 3DS option, token ID security note, 14 test cards
- [[source-paypal-save-paypal-orders-api]] — Orders API PayPal Wallet vault: reference transaction approval required, two-step flow, `experience_context`, `VAULT.PAYMENT-TOKEN.DELETION-INITIATED` webhook
- [[source-paypal-save-cards-orders-api]] — Orders API card vault: SAQ D required, raw card in request, single-step capture, no Venmo support
- [[source-paypal-save-paypal-ios-sdk]] — iOS SDK PayPal Wallet vault: `PayPalWebCheckoutClient`, `PayPalWebCheckoutDelegate`, 35 countries, `vault.id` for returning payers
- [[source-paypal-save-cards-ios-sdk]] — iOS SDK card vault: SwiftUI Toggle, `CardDelegate` protocol, US-only availability (contradicts Android/JS SDK 35-country support)
- [[source-paypal-save-paypal-android-sdk]] — Android SDK PayPal Wallet vault: `PayPalWebCheckoutClient`, deep link scheme, `vault.id` for returning payers, identical payload to JS SDK
- [[source-paypal-save-cards-android-sdk]] — Android SDK card vault: Compose checkbox UX, `customer.id` in Create Order body for returning payers, `ApproveOrderListener` 3DS callbacks, RTAU next step
- [[source-paypal-save-applepay-js-sdk]] — Apple Pay vault: APPROVED vs VAULTED status, VAULT.PAYMENT-TOKEN.CREATED webhook, merchant-initiated recurring pattern
- [[source-paypal-save-cards-js-sdk]] — Card vault JS SDK: checkbox UX, SCA_ALWAYS/SCA_WHEN_REQUIRED with vault, usage_type/customer_type/permit_multiple_payment_tokens fields, 14 test cards
- [[source-github-paypal-js]] — versioned React v9.3.0 Braintree billing-agreement and checkout-with-vault evidence
