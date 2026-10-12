---
title: "Adyen Web v4 to v6 Upgrade Guide"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/upgrade-your-integration/upgrade-to-web-v6/from-v4"
raw_files:
  - "adyen/docs/online-payments/upgrade-your-integration/upgrade-to-web-v6/from-v4/2026-09-15.md"
tags: [adyen, online-payments, adyen-web, migration, web-v6, drop-in, components]
---

## Overview

This Adyen Docs snapshot is a migration guide for Web Drop-in or Components from v4.x.x to v6.x.x. It identifies API, import, initialization, configuration, event, styling, and optional payment-method changes; the page sends v3 and v5 users to separate guides. See [[adyen]] and [[adyen-online-payments]]. This guide describes a version transition, not the behavior of every later Web 6 release or proof of a merchant's successful upgrade.

## Key takeaways

- Web Drop-in/Components v6.0.0 requires Checkout API v69 or later. The guide shows an npm package route and an embedded-script route with environment-specific CDN hosts and integrity hashes. Its `@latest` install command and 6.0.0 script example are snapshot examples; choose assets and API versions for the actual deployment.
- npm `/auto` imports Drop-in with payment methods already included, trading simpler additions for a larger bundle. Tree-shakable imports require importing the chosen payment-method Components and registering them through `paymentMethodComponents`. Embedded scripts expose `AdyenCheckout`, Drop-in, and Components under `window.AdyenWeb`.
- v6 makes `countryCode` mandatory at `AdyenCheckout` initialization or, for Sessions, in `/sessions`. Initialization is awaited, and Drop-in or individual Components are constructed directly instead of through `checkout.create()`. The page also lists removed or relocated configuration properties.
- In v6, `onSubmit` and `onAdditionalDetails` receive `actions`: resolve with a `resultCode` even for an unsuccessful payment, while reject is reserved here for an Adyen API request failure or network issue. `onPaymentCompleted` no longer handles failed payments; `onPaymentFailed` covers the listed `Cancelled`, `Error`, and `Refused` results. Treat the guide's event rules as version-specific SDK control flow, not payment finality on their own.
- Advanced-flow partial payments rename `onOrderCreated` to `onOrderUpdated` and use `onPaymentMethodsRequest` to fetch methods for a remaining balance; the latter callback is not needed for this purpose in Sessions. If Adyen Giving is used, the guide says v6 requires the Giving Campaign Manager Component. Express Apple Pay, Google Pay, and PayPal callback changes, CSS/DOM changes, and placeholder migration are located in the raw.

## Detail locators

- Opening and `## Required API version`, raw lines 15–32 — v4-to-v6 scope, alternative guides, and Checkout API minimum.
- `## Step 1: Use the new package`, raw lines 34–69 — npm and embedded assets, CDN regions, and example integrity values.
- `## Step 2: Upgrade import statements`, raw lines 70–179 — npm auto versus granular imports, payment-method registration, and `window.AdyenWeb`.
- `## Step 3: Upgrade your configuration` and `## Step 4: Upgrade creating an instance`, raw lines 180–261 — `countryCode`, removed or moved settings, awaited checkout initialization, and constructors.
- `## Step 5: Upgrade your event handlers`, raw lines 262–353 — resolve/reject, completion/failure events, Advanced-flow partial payments, and `onError`.
- `## Step 6: Upgrade your styling`, raw lines 354–411 — CSS custom properties, changed DOM/class names, and placeholder configuration.
- `## Step 7` through `## Step 9`, raw lines 412–507 — optional express methods, Giving, and Advanced-flow partial-payment examples.

## Related

- [[adyen]] — provider page.
- [[adyen-online-payments]] — online checkout architecture and source routes.
- [[source-github-adyen-web]] — separately versioned repository implementation evidence.

## Raw Sources

- [[raw/adyen/docs/online-payments/upgrade-your-integration/upgrade-to-web-v6/from-v4/2026-09-15|Adyen Docs — Upgrade Web v4 to v6 (2026-09-15 snapshot)]]
