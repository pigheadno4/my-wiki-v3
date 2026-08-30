---
title: "Apple Pay (via PayPal)"
type: concept
category: technology
tags: [apple-pay, paypal, apm, mobile-payments, vault, recurring-payments, ios, safari]
---

## Apple Pay (via PayPal)

Apple Pay is a mobile and web payment method that allows buyers to pay using cards stored in their Apple Wallet, authenticated via Face ID, Touch ID, or passcode. PayPal supports Apple Pay as an alternative payment method (APM) through its JS SDK and Orders v2 API.

## Key Constraints

- **Browser support**: Safari on iOS/macOS by default. With the [latest Apple Pay SDK](https://applepay.cdn-apple.com/jsapi/1.latest/apple-pay-sdk.js), non-Safari browsers are also supported.

> [!warning] Previous "Safari only" claim updated
> Earlier documentation stated Safari only. The current integration guide clarifies that non-Safari browsers are supported with the latest Apple Pay SDK.

- **Cannot be shown as a saved payment for returning buyers**: per Apple guidelines, vaulted Apple Pay is for **merchant-initiated recurring charges only** — merchants cannot display it as a one-click option at checkout.
- **JS SDK has no direct support to show saved Apple Pay**: merchants must use the Payment Method Tokens v3 API to list saved methods.
- **One-time payments only** in this integration; Apple Pay Recurring for Japan is not supported.
- **Domain validation required**: must download and host domain association file at `/.well-known/apple-developer-merchantid-domain-association`; no HTTP redirects; `Content-Type: application/octet-stream`.

## One-Time Checkout Integration

Four integration touchpoints:

1. `paypal.Applepay().config()` — check eligibility, get `countryCode`/`merchantCapabilities`/`supportedNetworks`
2. `new ApplePaySession(4, paymentRequest)` — create inside onclick gesture handler only
3. `paypal.Applepay().validateMerchant()` — in `onvalidatemerchant` callback
4. `paypal.Applepay().confirmOrder({ orderId, token, billingContact })` — in `onpaymentauthorized` callback

For this merchant-driven integration, both PayPal JS SDK (`components=applepay`) and Apple Pay JS SDK (`applepay.cdn-apple.com/jsapi/1.latest/apple-pay-sdk.js`) must be loaded. The v6 Basic flow below is a separate contract.

### v6 Basic versus recommended integration

The `paypal-examples/v6-web-sdk-sample-integration` sample at `default-branch@de90a89` adds a second, explicitly **Basic** one-time-payment path alongside the existing merchant-driven integration:

| Concern | Basic flow at `de90a89` | Existing recommended flow |
| --- | --- | --- |
| Browser initialization | Browser-safe client token; the sample says the Web SDK derives merchant identity from the token | Browser-safe client ID |
| Eligibility key | `basic_apple_pay` | `applepay` plus method details/config |
| Session | `createBasicApplePayOneTimePaymentSession()` | `createApplePayOneTimePaymentSession()` |
| Apple Pay lifecycle | PayPal session `start()` drives merchant validation, method selection, and authorization | Merchant code creates `ApplePaySession`, handles Apple callbacks, validates the merchant, and confirms the order |
| Apple JavaScript SDK | Not loaded by the Basic sample | Loaded explicitly |
| Order completion | `onApprove` receives `orderId`, then the merchant server captures | Merchant confirms with Apple's token/contact data, then captures |

The Basic sample still checks PayPal eligibility and device capability separately, creates the PayPal order on the merchant server, and captures on the merchant server. It demonstrates a simpler orchestration contract, not merchant enablement, production availability, or regional support.

### React v10.1.2 button behavior

`@paypal/react-paypal-js@10.1.2` removes the non-functional `disabled` prop from `ApplePayOneTimePaymentButton`. The component no longer writes a `disabled` attribute while its payment hook is pending because Apple's `<apple-pay-button>` ignores that attribute and manages its own state through `canMakePayments()`. Merchants control whether and how the button is presented; the component still attaches its click listener directly because React's `onClick` does not cross the element's shadow DOM.

### Core v11 TypeScript migration

`@paypal/paypal-js@11.0.0` removes PayPal's reduced `ApplePaySession` declaration and its augmentation of `window.ApplePaySession` from the `/sdk-v6` type barrel. The bundled declaration conflicted with the community Apple Pay definitions and affected compilation even when an integration did not use Apple Pay. TypeScript applications that reference Apple's browser global should install `@types/applepayjs` and use the native `ApplePaySession` type. This is a breaking compile-time contract change; the retained loader implementation and Apple Pay session bridge do not establish a new payment flow.

`@paypal/react-paypal-js@10.4.0` adopts that migration in its Apple Pay hook. It guards the bare native global with `typeof ApplePaySession`, uses the community payment-request and authorization-event types internally, and updates its core dependency to `@paypal/paypal-js ^11.0.0`. The React package's development dependency does not supply typings to merchant application code, so direct application references still require `@types/applepayjs`.

## Vault Flow

1. Buyer opts in during checkout
2. PayPal generates a `customer.id` — merchant stores this
3. Orders API saves Apple Pay token; `vault.status` may be `APPROVED` (async) or `VAULTED` (immediate)
4. If `APPROVED`: subscribe to `VAULT.PAYMENT-TOKEN.CREATED` webhook to get `vault_id`
5. Subsequent merchant-initiated charges use `vault_id` + `stored_credential` (`payment_initiator: "MERCHANT"`, `usage: "SUBSEQUENT"`)

The `default-branch@b5f2df2` sample includes both one-time and purchase-with-vault variants. Both validate the merchant, confirm the PayPal order with Apple's payment token and contact data, and capture. The vault variant creates the order with `paymentSource.applePay.attributes.vault.storeInVault: ON_SUCCESS`. This demonstrates the request shape but does not prove account approval or production eligibility.

## Key Request Fields

| Field | First save | Returning payer | Merchant-initiated |
| --- | --- | --- | --- |
| `stored_credential.payment_initiator` | `CUSTOMER` | `CUSTOMER` | `MERCHANT` |
| `stored_credential.payment_type` | `RECURRING` | `RECURRING` | `RECURRING` |
| `stored_credential.usage` | — | — | `SUBSEQUENT` |
| `attributes.vault.store_in_vault` | `ON_SUCCESS` | `ON_SUCCESS` | — |
| `attributes.customer.id` | — | Required | — |
| `vault_id` | — | — | Required |

## Go Live Onboarding

Requires manual approval through PayPal account settings:
Account Settings → Payment Method → Enable Apple Pay → Get Started → submit Profile collection → review → Success

## Relevant Companies

- [[paypal]] — PayPal supports Apple Pay as an APM via JS SDK and Orders API

## Sources

- [[source-paypal-apm-apple-pay]] — One-time checkout integration: domain validation, 4 SDK touchpoints, `ApplePaySession`, non-Safari browser support, go-live onboarding
- [[source-paypal-save-applepay-js-sdk]] — Save Apple Pay vault integration: request/response samples, APPROVED vs VAULTED status, webhook, platform headers, go-live steps
- [[source-github-paypal-js]] — package-qualified React v10.1.2 button behavior, core v11 Apple Pay type migration, and React v10.4 adoption
- [[source-github-v6-web-sdk-sample-integration]] — runnable recommended merchant-driven Apple Pay, purchase-with-vault, and `de90a89` Basic SDK-managed examples
