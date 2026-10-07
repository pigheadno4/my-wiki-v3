---
title: "Braintree Google Pay Configuration for Android v5"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/google-pay/configuration/android/v5"
raw_files:
  - "braintree/docs/guides/google-pay/configuration/android/v5-2026-09-16.md"
tags: [braintree, google-pay, android, mobile, configuration, control-panel]
---

## Overview

This 2026-09-16 snapshot of a [[braintree]] website guide documents configuration prerequisites on an Android v5 route: enable Google Pay in the Braintree Control Panel for the relevant sandbox or production environment, obtain merchant-account-specific activation when needed, and separately work with Google for production; PayPal via Google Pay requires both PayPal and Google Pay enabled. It complements the client flow in [[braintree-android-sdk]] but does not establish an exact Android package version, current certificate or account state, merchant eligibility, client tokenization, server transaction processing, or payment execution.

## Key takeaways

- The page directs merchants to the matching sandbox or production Control Panel and to turn on Google Pay under **Account Settings** → **Payment Methods**. If Google Pay is active generally but not for a particular merchant account, it directs the merchant to contact Braintree.
- Production additionally requires work with Google to go live. The snapshot does not establish that either the Braintree-side enablement or Google's production process has been completed for a merchant.
- Accepting PayPal through Google Pay requires both PayPal and Google Pay to be enabled in the Control Panel. This configuration condition is separate from the Android v5 client authorization/tokenization flow and subsequent server-side transaction handling.

> [!warning] Historical certificate notice
> The captured page states that Braintree Mobile iOS and Android SDK certificates expire on March 30, 2026, directs Android upgrades to `4.45.0+` or `5.0.0+`, and warns that all customer traffic will fail if affected older app versions are neither decommissioned nor force-upgraded by that date. Because the notice predates the 2026-09-16 fetch, retain it as dated page wording rather than current certificate status, exact package compatibility, runtime behavior, or traffic evidence.

## Detail locators

- **Mobile SDK certificate notice and Android version thresholds:** raw lines 17–20.
- **Sandbox/production Control Panel setup steps:** `## Setup`, raw lines 25–35.
- **Merchant-account-specific activation route:** raw line 36.
- **Separate Google production requirement:** raw line 38.
- **PayPal via Google Pay dual-enablement condition:** `### PayPal via Google Pay`, raw lines 41–43.

## Related

- [[braintree-android-sdk]]
- [[braintree]]

## Raw Sources

- [[raw/braintree/docs/guides/google-pay/configuration/android/v5-2026-09-16|Braintree Google Pay configuration — Android v5 (2026-09-16 snapshot)]]
