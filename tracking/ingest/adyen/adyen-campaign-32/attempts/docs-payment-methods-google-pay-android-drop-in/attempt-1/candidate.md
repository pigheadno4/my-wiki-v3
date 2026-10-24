---
title: "Adyen Google Pay Android Drop-in guide"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/google-pay/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/google-pay/android-drop-in/2026-09-15.md"
tags: [adyen, google-pay, android, drop-in, online-payments]
---

## Overview

This [[adyen]] page, last modified and captured 2026-09-15, explains adding Google Pay to an **existing Android Drop-in** integration. It has separate Sessions and Advanced server-flow sections, each with Customer Area method setup, optional Android configuration and test/live preparation. Use [[adyen-online-payments]] as the main route. The page does not show a completed wallet authorization, 3DS challenge, capture or settlement, and does not prove current merchant/device/card eligibility.

## Key takeaways

- **Flow prerequisites:** the Sessions branch requires an existing Android Sessions Drop-in integration with Checkout API **v69 or later**, plus Google Pay added in Customer Area. It says no additional parameters are needed when creating a payment session. The Advanced branch similarly requires an existing Android Advanced Drop-in and Customer Area method setup; it says no additional fields are needed in its `/payments` request. The v69 minimum is stated for Sessions here, not for the Advanced branch. See raw lines 19–38 and 137–206.
- **Android client controls:** both branches list optional `CheckoutConfiguration` settings for supported card networks, credit/prepaid cards, Google Pay allowed authentication methods, billing/shipping data, merchant details, price status and button display. The listed default auth methods are `PAN_ONLY` and `CRYPTOGRAM_3DS`; this is a configuration value, not completed 3DS authentication. Allowed networks are initially drawn from account settings but can be overridden. `setGooglePayEnvironment` may explicitly choose Google's TEST or PRODUCTION setting and otherwise follows the Adyen environment. Keep Google and Adyen environment choices distinct; the placeholder Kotlin blocks are illustrative, not a full executable integration. See raw lines 40–94 and 146–200.
- **Testing:** the page describes a Google account and wallet, with either Google's TEST card suite or a wallet holding real cards mapped by Adyen to same-brand test cards. It limits test-suite DPAN to native Android/Chrome on Android; in the no-suite path it says only Amex or Discover triggers its 3DS2 test challenges. These test instructions and payment-list lookup do not establish a live charge, an actual challenge result or authorization. See raw lines 98–122 and 208–232.
- **Live preparation and availability:** its live checklist calls for the Adyen API credential's **API Clientside Encryption Payments role**, a configured Google Merchant ID in live Customer Area, and Google's Android production deployment steps. It recommends testing Google's scenarios in live. The page states Google Pay is available in live only when the shopper is logged in to Google and has at least one valid Google Pay payment method. These are stated conditions, not proof a particular merchant, shopper, card or integration can process a live payment. See raw lines 124–135 and 234–245.

## Detail locators

- Sessions prerequisite, Checkout API version and session-field boundary: raw lines 19–38.
- Sessions Android `CheckoutConfiguration` parameters and example: raw lines 40–94.
- Sessions test card suite, non-suite mapping and live checklist: raw lines 96–135.
- Advanced prerequisite, configuration parameters and no-extra-`/payments` statement: raw lines 137–206.
- Advanced repeated test and live preparation: raw lines 208–245.

## Related

- [[adyen-online-payments]]
- [[adyen-3d-secure]]
- [[adyen-payment-testing]]
- [[source-adyen-docs-payment-methods-google-pay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/google-pay/android-drop-in/2026-09-15|Google Pay Android Drop-in guide — collected 2026-09-15]]
