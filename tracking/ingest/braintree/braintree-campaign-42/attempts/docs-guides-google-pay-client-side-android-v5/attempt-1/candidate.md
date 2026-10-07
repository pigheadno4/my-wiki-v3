---
title: "Braintree Google Pay Client-Side Implementation for Android v5"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/google-pay/client-side/android/v5"
raw_files:
  - "braintree/docs/guides/google-pay/client-side/android/v5-2026-09-16.md"
tags: [braintree, google-pay, android, mobile, client-sdk, tokenization]
---

## Overview

This 2026-09-16 snapshot of a [[braintree]] website guide documents the Android v5 client-side Google Pay path through [[braintree-android-sdk]]: check device readiness, create an authorization request, launch the Google Pay flow, and tokenize the returned authorization result. It is snapshot guidance, not evidence of current SDK support, merchant or device eligibility, server-side transaction completion, or successful payment execution.

## Key takeaways

- The guide initializes `GooglePayLauncher` in the Activity's `onCreate()` and creates `GooglePayClient` with either a tokenization key or a client token. Before displaying the Google Pay button, it calls `isReadyToPay()`; only `ReadyToPay` leads to showing the button, while other results route the buyer to other checkout options.
- After a button click, the client builds `GooglePayRequest`, calls `createPaymentAuthRequest()`, launches only a `ReadyToLaunch` result, and handles `Failure` separately. The shown currency, total and final-price status are example values, not universal transaction requirements.
- After completion or cancellation of the Google Pay flow, the Kotlin example passes the launcher callback's `googlePayPaymentAuthResult` to `GooglePayClient.tokenize()`. It handles failure, cancellation and success, with success yielding a nonce for subsequent processing rather than proving a completed transaction.

> [!warning] Historical certificate notice
> The captured page states that Braintree Mobile iOS and Android SDK certificates expire on March 30, 2026, directs Android upgrades to `4.45.0+` or `5.0.0+`, and warns that customer traffic will fail if affected older app versions are neither decommissioned nor force-upgraded by that date. Because the notice's date precedes this page's 2026-09-16 fetch, retain it as dated page wording rather than current certificate, package-support, or traffic evidence.

> [!warning] Tokenization argument mismatch
> The prose says to pass `GooglePayPaymentAuthRequest` to `tokenize()`, while both Kotlin examples pass the callback's `googlePayPaymentAuthResult`. This snapshot does not resolve the request-versus-result type wording conflict; use the raw locator rather than treating the prose identifier as verified API signature evidence.

## Detail locators

- **Dependency example (`google-pay:5.2.0`):** raw lines 25-44 under `## Get the SDK`.
- **Launcher/client initialization, readiness gating and button guidance:** raw lines 46-77 under `## Initialization`.
- **Request construction, `ReadyToLaunch` launch and failure branch:** raw lines 80-107 under `## Requesting a payment`.
- **Callback tokenization and success/cancel/failure result branches:** raw lines 108-127 under `## Requesting a payment`.
- **Combined Kotlin example:** raw lines 129-183 under `## Complete Integration`.

## Related

- [[braintree-android-sdk]]
- [[braintree]]

## Raw Sources

- [[raw/braintree/docs/guides/google-pay/client-side/android/v5-2026-09-16|Braintree Google Pay client-side Android v5 guide (2026-09-16 snapshot)]]
