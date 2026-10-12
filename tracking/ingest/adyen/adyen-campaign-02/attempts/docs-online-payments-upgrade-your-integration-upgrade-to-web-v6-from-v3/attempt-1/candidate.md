---
title: "Adyen Web v3 to v6 Upgrade Guide"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/upgrade-your-integration/upgrade-to-web-v6/from-v3"
raw_files:
  - "adyen/docs/online-payments/upgrade-your-integration/upgrade-to-web-v6/from-v3/2026-09-15.md"
tags: [adyen, web-sdk, drop-in, components, migration, checkout]
---

## Overview

This [[adyen]] website guide describes the changes for moving a Web Drop-in or Components integration from v3.x.x to v6.0.0. It routes v4.x.x and v5.x.x starting points to different guides. Web v6.0.0 requires Checkout API v69 or later. The page documents client-library migration steps; it does not establish the behavior of every later v6 release or prove a merchant deployment has been upgraded. See [[adyen-online-payments]].

## Key takeaways

- Package and import choices change. npm can import all Drop-in payment methods through `@adyen/adyen-web/auto`, with larger bundles, or import individual Components through the tree-shakable package. The latter requires registering added methods in Drop-in's `paymentMethodComponents`; embedded scripts expose `AdyenCheckout` and Components on `window.AdyenWeb`. CDN URLs and Subresource Integrity hashes are environment and version dependent.
- Initialization and configuration change: `AdyenCheckout(...)` is awaited, Drop-in/Components use constructors instead of `checkout.create()`, and `countryCode` is mandatory in configuration or, for Sessions, may be set in the `/sessions` request. `originKey` is unsupported and must move to a client key. The page lists further removed or relocated core, Card, Apple Pay, Google Pay, IssuerList, and PayPal properties.
- `onSubmit` and `onAdditionalDetails` receive `actions`. Resolve with `resultCode` even for an unsuccessful payment; reject only when the merchant server's Adyen API request fails or a network connection fails. `onPaymentCompleted` no longer handles failed payments; `onPaymentFailed` receives the documented `Cancelled`, `Error`, or `Refused` result codes. The v6 partial-payment route renames `onOrderCreated` to `onOrderUpdated` and uses `onPaymentMethodsRequest` for new methods in Advanced flow only.
- Styling uses CSS custom properties in v6. The guide warns that class names and DOM structure changed, so existing overrides need checking. Placeholders cease to be default and move from translations to payment-method configuration. Optional express-wallet, Giving, and Advanced partial-payment sections have separate migration steps; in express Apple Pay and Google Pay, `onAuthorized` runs before `onSubmit` and must be resolved or rejected to continue.

## Detail locators

- **Opening and Required API version**, raw lines 15–32 — source v3.x.x, target v6.0.0, alternative starting-version routes, and Checkout API v69 floor.
- **Steps 1–2**, raw lines 34–178 — package, environment CDN/SRI, npm and embedded imports, bundle tradeoff, and method registration.
- **Step 3**, raw lines 180–284 — mandatory `countryCode`, unsupported `originKey`, relocated settings, and payment-method-specific removed properties.
- **Step 4**, raw lines 286–355 — awaited checkout creation and constructor-based Drop-in/Component mounting.
- **Step 5**, raw lines 356–447 — action resolution, successful versus failed callback split, Advanced partial-payment callback, and error callback.
- **Steps 6–9**, raw lines 448–601 — style and placeholder migration; conditional express Apple Pay, Google Pay, PayPal, Giving, and Advanced partial-payment updates.

## Related

- [[adyen-online-payments]]
- [[source-github-adyen-web]]

## Raw Sources

- [[raw/adyen/docs/online-payments/upgrade-your-integration/upgrade-to-web-v6/from-v3/2026-09-15|Adyen Web v3-to-v6 migration guide (2026-09-15 snapshot)]]
