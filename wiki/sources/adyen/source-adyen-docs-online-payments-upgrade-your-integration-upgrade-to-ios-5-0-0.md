---
title: "Adyen iOS v5.0.0 Upgrade Guide"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/upgrade-your-integration/upgrade-to-ios-5-0-0"
raw_files:
  - "adyen/docs/online-payments/upgrade-your-integration/upgrade-to-ios-5-0-0/2026-09-15.md"
tags: [adyen, ios, sdk, migration, drop-in, components]
---

## Overview

This [[adyen]] guide lists changes for an **online-checkout iOS SDK** integration upgrading from v4.10.1 or earlier to v5.0.0. It covers method signatures, required initialization context, Component and payment-method configuration, and Drop-in configuration. This is migration guidance for [[adyen-ios-sdk]], separate from the iOS Mobile POS SDK and from Checkout API versioning.

## Key takeaways

- The page **recommends** Checkout API v69; it does not state v69 as a hard prerequisite in this guide. The iOS SDK package version and merchant-server Checkout API version are separate. Check the current compatibility matrix and exact integration's server-side API configuration before choosing versions.
- Update the listed iOS method signatures from the v4.10.1-or-earlier column to the v5.0.0 column. The table includes completion, external-app, partial-order request and cancel callbacks; `finalizeIfNeeded(with success: Bool, completion: (() -> Void)?)` appears unchanged in both columns. Use the raw table for exact Swift spelling and parameters.
- Initializing Drop-in or any Component now requires an `AdyenContext`. The example builds `APIContext` with a client key and test environment, then `AdyenContext` with analytics configuration, and passes it into Drop-in configuration. This is a client-side initialization example; `Environment.test` is not a live-environment instruction, and a client key does not replace merchant-server API credentials or prove payment execution.
- Component and payment-method settings move to configuration objects for their respective types. The guide illustrates `RedirectComponent.Configuration` styling and `CardComponent.Configuration` storage-field/localization settings; these snippets are examples, not a complete configuration contract.
- For Apple Pay in v5.0.0, the `ApplePayComponent.Configuration.init()` parameters named here are `merchantIdentifier` and `payment`, while other Apple Pay configuration properties become mutable; `payment` changes from `Payment` to `ApplePayPayment`. Card brand properties named in the guide become strongly typed `CardType` arrays. Consult the raw for the exact properties.
- Step 5 is labeled optional generally but explicitly required for a Drop-in integration: use `DropInComponent.Configuration()`. The `allowsSkippingPaymentList` assignment is an example optional setting. A separate sentence says that **in v5.9.0** iDEAL uses `InstantPaymentComponent`; do not attribute that later change to v5.0.0.
- The page was collected 2026-09-15 but its metadata says last modified 2022-11-07. It does not verify the current iOS SDK release, app build, device behavior, account eligibility, Checkout API response, payment authorization, capture, or settlement.

## Detail locators

- Upgrade starting range and Checkout API v69 recommendation: raw lines 15–23.
- Exact old/new callback method signatures: `## Step 1: Upgrade methods`, raw lines 25–35.
- Required `AdyenContext` and test-environment initialization example: `## Step 2: Upgrade initializing Drop-in and Components`, raw lines 37–50.
- Component-specific and payment-method-specific configuration examples: `## Step 3` and `## Step 4`, raw lines 52–73.
- Later v5.9.0 iDEAL note, Apple Pay initializer/payment-type change, and `CardType` brand properties: raw lines 75–93.
- Conditional Drop-in-only requirement and configuration example: `## Step 5: (Optional) Update Drop-in configuration`, raw lines 95–106.

## Related

- [[adyen]] — provider context.
- [[adyen-ios-sdk]] — separately versioned native online-checkout SDK concept and retained repository baseline.
- [[source-adyen-docs-online-payments-upgrade-your-integration]] — version policy and compatibility-table route.

## Raw Sources

- [[raw/adyen/docs/online-payments/upgrade-your-integration/upgrade-to-ios-5-0-0/2026-09-15|Adyen iOS v5 upgrade guide — collected 2026-09-15]]
