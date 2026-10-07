---
title: "Braintree PayPal Client-Side Implementation for Android v5"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/client-side/android/v5"
raw_files:
  - "braintree/docs/guides/paypal/client-side/android/v5-2026-09-16.md"
tags: [braintree, paypal, android, mobile, client-sdk, tokenization]
---

## Overview

This 2026-09-16 snapshot of Braintree's Android v5-routed client-side PayPal guide covers account and return-routing setup, direct `PayPalClient` initialization, and SDK-managed XML or Jetpack Compose PayPal buttons that launch authentication and tokenize the result into a nonce. It is website guidance and example code, not proof of current package support, merchant eligibility, or a successful payment transaction. See [[braintree-android-sdk]] and [[braintree]].

> [!warning] Captured certificate deadline
> The page says Braintree Mobile SDK SSL certificates were set to expire on March 30, 2026, directs Android integrations to 4.45.0+ or 5.0.0+, and warns that traffic from app versions retaining older SDK certificates would fail unless those versions were decommissioned or force-upgraded before the deadline. This dated snapshot does not establish current certificate or support status.

## Key takeaways

- Before adding PayPal, the guide requires a PayPal account created, verified, and linked in the Braintree Control Panel, Android SDK setup with a client token, and a URL scheme declared in `AndroidManifest`.
- The direct-client path initializes `PayPalLauncher` in the Activity's `onCreate`, then constructs `PayPalClient` with either a tokenization key or client token plus an app-link return URL.
- The captured dependency examples use `com.braintreepayments.api:paypal:5.8.0` and, for SDK payment buttons, `com.braintreepayments.api:ui-components:5.25.0`; the latter example itself says to replace the version with the latest version. These examples do not prove current package compatibility.
- For the XML/Fragment button example, the button is initialized with authorization and return-routing values, receives a `PayPalRequest`, reports launch failure or a pending request, and later handles success, failure, or cancellation after the app resumes. The example comments call for persisting the pending request and clearing it after return handling.
- For Jetpack Compose, the guide says the SDK handles `handleReturnToApp()` internally; the composable takes the request, authorization, app-link return URL, deep-link fallback scheme, and a callback that distinguishes success, cancellation, and failure.
- Further configuration branches into One-Time Payments, Vaulted Payments, or Recurring Payments; those linked pages are navigation rather than evidence read for this entry.

## Detail locators

- Certificate-expiry notice and failure warning: raw lines 17-20.
- PayPal account, client token, and Android manifest prerequisites: raw lines 25-32.
- PayPal module dependency samples: raw lines 35-52.
- `PayPalLauncher`/`PayPalClient` initialization and return URL: raw lines 54-74.
- SDK-managed payment-button responsibility and UIComponents dependency: raw lines 76-93.
- XML/Fragment button initialization, pending-request persistence, return handling, and result branches: raw lines 94-157.
- Button colors: raw lines 158-175.
- Jetpack Compose return-handling distinction and callback example: raw lines 176-215.
- One-Time, Vaulted, and Recurring next-step routes: raw lines 217-226.

## Related

- [[braintree-android-sdk]]
- [[braintree]]

## Related raw API references

- The One-Time Payments, Vaulted Payments, Recurring Payments, and comparison links at raw lines 217-226 were not read for this entry and are retained only as navigation.

## Raw Sources

- [[raw/braintree/docs/guides/paypal/client-side/android/v5-2026-09-16|Braintree PayPal Client-Side Implementation for Android v5 (2026-09-16 snapshot)]]
