---
title: "Adyen Docs: Upgrade to Adyen Web v6"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/upgrade-your-integration/upgrade-to-web-v6"
raw_files:
  - "adyen/docs/online-payments/upgrade-your-integration/upgrade-to-web-v6/2026-09-15.md"
tags: [adyen, web, drop-in, components, migration, checkout]
---

## Overview

This Adyen website guide maps the required changes when upgrading **Web** Drop-in or Components from v5.x.x to v6.x.x. It routes v3 and v4 starting points to separate guides. The migration covers Checkout API compatibility, package/import shape, configuration and construction, payment-event handling, styling, and optional express, Giving, and partial-payment integrations. See [[adyen-online-payments]].

## Key takeaways

- Web Drop-in/Components v6.0.0 requires Checkout API v69 or later. The guide recommends npm; embedded scripts need version-appropriate integrity hashes and an environment-specific CDN. The `@adyen/adyen-web/auto` import includes all methods with a larger bundle, while tree-shakable imports require explicit Components and `paymentMethodComponents` registration when used with Drop-in.
- V6 moves embedded globals under `window.AdyenWeb`, makes `countryCode` mandatory at checkout initialization or in a Sessions request, and replaces `checkout.create(...)` with Component/Drop-in constructors. Several old configuration options are removed or moved; see the raw configuration table and before/after examples.
- In `onSubmit` and `onAdditionalDetails`, the new `actions` parameter controls continuation. The prose says to call `actions.resolve()` with `resultCode` even for an unsuccessful payment, and to use `actions.reject()` for API-request or network failures. `onPaymentCompleted` no longer fires for failed payments; `onPaymentFailed` covers `Cancelled`, `Error`, and `Refused`.
- The example handler calls `actions.reject()` when `resultCode` is missing and then can proceed to `actions.resolve()` without returning (raw lines 293–307; repeated at 482–496). Treat the snippet as illustrative and settle the control flow before copying it.
- The optional migration sections have consequential route-specific changes: Apple Pay and Google Pay express `onAuthorized` must resolve or reject before `onSubmit`; PayPal renames authorization and shipping callbacks; v6 Giving uses the Giving Campaign Manager Component; and Advanced-flow partial payments use `onPaymentMethodsRequest` when an order remains unpaid. These are version-scoped Web integration instructions, not evidence of live method availability or successful payment execution.

## Detail locators

- **Introduction / Required API version, raw lines 17–32** — v5-to-v6 scope, separate v3/v4 routes, Checkout API v69 minimum.
- **Steps 1–2, raw lines 34–179** — npm versus embedded resources, region-specific CDN list, `/auto` versus tree-shakable imports, Redirect fallback, and `window.AdyenWeb`.
- **Steps 3–4, raw lines 180–268** — mandatory `countryCode`, removed or relocated configuration, constructors, and conditional `paymentMethodComponents`.
- **Step 5, raw lines 269–353** — `actions` behavior, success/failure callback split, renamed `onOrderUpdated`, and Advanced-only `onPaymentMethodsRequest`.
- **Step 6, raw lines 354–409** — CSS custom properties, retained class overrides, and placeholder behavior.
- **Steps 7–9, raw lines 410–505** — optional Apple Pay, Google Pay, PayPal, Giving, and Advanced-flow partial-payment migrations, including their callback and flow boundaries.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-web-disclaimers]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/online-payments/upgrade-your-integration/upgrade-to-web-v6/2026-09-15|Adyen Docs — Upgrade to Adyen Web v6 (2026-09-15)]]
