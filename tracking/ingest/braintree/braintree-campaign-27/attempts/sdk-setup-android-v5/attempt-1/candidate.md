---
title: "Braintree Android Client SDK Setup (v5)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/client-sdk/setup/android/v5"
raw_files:
  - "braintree/docs/guides/client-sdk/setup/android/v5-2026-09-16.md"
tags: [braintree, android, client-sdk, setup, gradle, app-links, authorization]
---

## Overview

This historical Braintree Android client SDK v5 setup snapshot covers the modular Gradle dependencies, Android return routing, and authorization inputs used to integrate payment-method clients. It is a setup and navigation source, not evidence of current SDK support, merchant eligibility, a successful payment flow, or the current package version.

## Key takeaways

- The captured page describes the Braintree Android SDK as helping an Android app accept payments. Its stated environment requirements are Android API 23+, Gradle JDK 11+, Kotlin 1.9.10+, and Android Gradle Plugin 8.1.4+; these are snapshot requirements, not a current support matrix.
- The installation examples add only the desired payment-feature modules and display version `5.18.0` for Card, Data Collector, PayPal, Local Payment, Google Pay, 3D Secure, and Venmo. The page says Android SDK modules follow semantic versioning and recommends updating every module to the latest version. The displayed version is an example from this page, not the independently retained current or latest package baseline.
- Some payment flows return through Android App Links. The guide requires registering the App Link domain in the Braintree Control Panel, matching the fully qualified domain name exactly, passing the App Link return URL to a payment-method client, and configuring the manifest intent filter. These are setup instructions from the captured page, not proof that a domain was registered or a return flow succeeded.
- Browser-switch flows instead require a URL scheme for returning to the app. The page says the scheme must begin with the app package ID and end with `.braintree`; it also notes that `android:exported` is required when the compile SDK is API 31 or later.
- Each payment-method client requires authorization as either a tokenization key or client token. The tokenization-key example passes the key directly to a client constructor. The client-token-provider example assumes a merchant server endpoint that returns a client token, then passes the fetched token to the client constructor; the sample endpoint, JSON shape, Retrofit code, and constructor calls are examples rather than a complete production security design.
- The page says Braintree-specific ProGuard rules are already supplied by the SDK.

> [!warning] Historical mobile-certificate notice
> The snapshot says Braintree Mobile SDK SSL certificates were set to expire on March 30, 2026, names Android SDK 4.45.0+ or 5.0.0+ as upgrade targets, and warns that customer traffic from app versions retaining older certificates would fail if those versions were not decommissioned or force-upgraded by that date. Because this page was fetched after the stated deadline, preserve this as historical snapshot evidence rather than a claim about present certificate status, current SDK support, or observed traffic failure.

## Detail locators

- Mobile SDK certificate-expiry date, Android upgrade targets, and conditional traffic-failure warning: `# Setup > IMPORTANT`, lines 17-22.
- SDK purpose and captured Android, JDK, Kotlin, and Android Gradle Plugin requirements: `# Setup` and `## Requirements`, lines 26-37.
- Semantic-versioning note and per-module update guidance: `## Requirements > NOTE`, lines 40-41.
- Kotlin and Groovy Gradle dependency examples for the displayed `5.18.0` modules: `## Installation > Get the SDK`, lines 46-110.
- App Link purpose, Control Panel registration, exact-domain condition, client constructor, and manifest setup: `### App Link setup`, lines 112-179.
- Browser-switch manifest example, API 31 `android:exported` note, and package-ID-plus-`.braintree` scheme rule: `### Browser switch setup`, lines 182-209.
- Authorization choices and tokenization-key constructor example: `## Initialization > Authorization`, lines 214-233.
- Assumed server endpoint, client-token-provider examples, and client-token constructor example: `### Client Token Provider`, lines 235-357.
- ProGuard configuration statement: `### ProGuard`, lines 359-361.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-android-sdk]]

## Raw Sources

- [[raw/braintree/docs/guides/client-sdk/setup/android/v5-2026-09-16|Braintree Android Client SDK Setup (v5)]] - complete collected setup snapshot for modular dependencies, Android return routing, authorization choices, and the historical mobile-certificate notice
