---
title: "Braintree PayPal One-time Payments (Android v5)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/checkout-with-paypal/android/v5"
raw_files:
  - "braintree/docs/guides/paypal/checkout-with-paypal/android/v5-2026-09-16.md"
tags: [braintree, paypal, android, android-v5, one-time-payments, tokenization]
---

## Overview

This Android v5-routed [[braintree]] website-guide snapshot, collected 2026-09-16, documents the client-side PayPal one-time checkout path. The app creates a `PayPalCheckoutRequest`, obtains and launches a payment-authorization request, persists the started pending request, handles the return intent and tokenizes a successful authorization result into a single-use value inside `PayPalAccountNonce`. It is Braintree Android v5 documentation, not a standalone PayPal Android SDK or direct PayPal Orders API integration, and not evidence about sibling platforms, a current package implementation or a GitHub release.

The returned authorization result and nonce are client-side handoff states, not proof of a server-side transaction, authorization, capture, settlement or funding. The page separately routes shipping-address submission and currency charging to server-side guidance. Follow [[braintree-android-sdk]] for the platform boundary and [[paypal-braintree-integration]] for the broader Braintree-versus-direct-PayPal distinction.

## Key takeaways

- The captured dependency examples use `com.braintreepayments.api:paypal:5.8.0`. The page initializes `PayPalLauncher` in the activity's `onCreate()` and creates `PayPalClient` with a tokenization key or client token, an app-link return URL and a fallback deep-link scheme. This is a captured example, not proof that `5.8.0` is current, installed or compatible with a particular app.
- After a PayPal-button click, the app calls `createPaymentAuthRequest()`. A ready request is launched; a `PayPalPendingRequest.Started` value means the external flow launched and its pending-request string must be persisted. Failure branches remain application responsibilities.
- Return handling depends on Android activity launch mode: `SINGLE_TOP` uses `onNewIntent()`, while all other launch modes use `onResume()`. The persisted request and return intent go to `handleReturnToApp()`; only a successful authorization result proceeds to `tokenize()`, whose success case returns the single-use value inside `PayPalAccountNonce`. Cancellation, no-result and failure branches do not establish a completed payment.
- App Switch is conditional: after `PayPalLauncher().launch`, the SDK attempts the PayPal app only when it is installed and the user meets eligibility requirements; an unsuccessful app switch falls back to the default browser experience. The Contact Module is separately stated as US-only, and shipping changes use a server-side callback URL.
- The snapshot does not demonstrate merchant or buyer eligibility, account setup, dependency installation, an app build, a Sandbox or Production run, callback delivery, server processing or any transaction-lifecycle outcome.

> [!warning] Historical mobile-certificate notice
> The captured page says Braintree Mobile SDK certificates were due to expire on March 30, 2026, advises Android SDK `4.45.0+` or `5.0.0+`, and warns that all customer traffic for affected published app versions would fail unless those versions were decommissioned or force-upgraded by the deadline. Because the page was collected after that date, preserve this as historical page wording rather than current certificate, package-support or app-compatibility proof.

> [!warning] Client/server and outcome boundary
> A ready authorization request, launched flow, returned authorization success or `PayPalAccountNonce` is not a successful Braintree transaction or evidence of authorization, capture, settlement or funding. The page's server-side shipping and currency links are navigation, not execution evidence for this snapshot.

## Detail locators

- Dated mobile-certificate warning, version floors and stated total-traffic consequence: `# One-time Payments > **IMPORTANT**`, raw lines 17-20.
- PayPal module dependency examples at captured version `5.8.0`: `## Setup > ### Get the SDK`, raw lines 28-45.
- Launcher/client initialization, authorization choices and return URLs: `## Invoking the One-time Payments flow > ### Initialization`, raw lines 50-70.
- Checkout-request creation, ready/failure handling, launch and pending-request persistence: `### Request a payment`, raw lines 72-99.
- Activity launch-mode callback split, return-intent handling, authorization-result branches and nonce tokenization: `### Handle the payment result`, raw lines 101-172.
- Combined Kotlin example for initialization, callbacks, return handling and request launch: `## Complete integration`, raw lines 174-253.
- Customization inventory: `## Customizing One-time Payments`, raw lines 255-265.
- Contact Module purpose, US-only qualification and display/edit preferences: `### Integrating Contact Module`, raw lines 268-310.
- Server-side shipping callback behavior and request field: `### Integrating Shipping Module`, raw lines 312-324.
- Line-item presentation locations: `### Integrating Pass Line-item Details`, raw lines 326-341.
- Buyer email and phone prefill example: `### Integrating Pass Buyer Identifier`, raw lines 343-354.
- Pay Now versus Continue descriptions and user-action example: `### Integrating Pay Now or Continue`, raw lines 356-378.
- PayPal-app eligibility condition, default-browser fallback and separate integration-guide route: `### Integrating App Switch`, raw lines 380-395.
- Optional shipping-address handoff to server-side `Transaction.Sale`: `## Shipping address`, raw lines 398-400.
- Country and currency statements plus server-side charging route: `## Country support` and `## Currency presentment`, raw lines 403-412.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-android-sdk]]
- PayPal/Braintree boundary: [[paypal-braintree-integration]]

## Related raw API references

- [[raw/braintree/docs/guides/client-sdk/setup/android/v5-2026-09-16|Braintree Android v5 client SDK setup]] - linked setup context only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/paypal/server-side/node-2026-09-16|Braintree PayPal server-side guide for Node.js]] - linked server-side navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/paypal/checkout-with-paypal/android/v5-2026-09-16|Braintree PayPal one-time payments for Android v5]] - fully read pinned website snapshot covering client request, launch, return handling, tokenization, customization and historical SDK warning
