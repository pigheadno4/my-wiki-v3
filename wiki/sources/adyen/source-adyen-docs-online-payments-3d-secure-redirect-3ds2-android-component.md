---
title: "Adyen Redirect 3DS2 Android Component Integration"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/3d-secure/redirect-3ds2/android-component"
raw_files:
  - "adyen/docs/online-payments/3d-secure/redirect-3ds2/android-component/2026-09-15.md"
tags: [adyen, 3d-secure, 3ds2, android, redirect, components, advanced-flow]
---

## Overview

This Adyen Docs snapshot describes redirect 3D Secure 2 for cards in an Android app, specifically an API-only card integration using Redirect Component v5.0.0 with the Advanced flow. It directs v4.13.3 and earlier users to a separate guide. In a Components integration already using the Card Component, the page says that Component can handle redirect 3DS2 without extra integration; the separate 3DS2 Component is not needed for that case. See [[adyen]] and [[adyen-3d-secure]].

This merchant integration guide is distinct from the version-qualified [[adyen-android-sdk]] checkout implementation and [[adyen-3ds2-android-sdk]] native challenge runtime. The snapshot does not establish account enablement, successful authentication, authorization, or completed payment for a transaction.

## Key takeaways

- The API-only path assumes the merchant builds its own card-entry UI and imports `com.adyen.checkout:redirect`. The merchant sends card and 3DS2 parameters to its server for `/payments`, including `channel: "Android"`, browser information, and the `returnUrl` obtained from `RedirectComponent.getReturnUrl(context)`. The field table marks holder name, shopper IP, and email or phone conditionally required for Visa and JCB; the page also recommends collecting billing address and email and says the schemes require those parameters.
- The merchant checks the `/payments` response. With no `action`, this guide describes the transaction as exempt or outside 3DS2 scope and routes it to the payment-outcome step. With `action.type: redirect`, the merchant passes the action to the Redirect Component, which sends the shopper to a separate authentication page and returns them to the app.
- This page links to the Android Advanced-flow guide for the detailed redirect handler and payment-outcome steps; it does not itself spell out the app-return callback or `/payments/details` request sequence. A redirect action or return to the app is not a successful payment result.
- For live payment sessions, Adyen warns that `/payments` and `/payments/details` requests must use the same live endpoint region; mixing regions can cause 3DS authentication errors.

## Detail locators

- Opening and `## Requirements`, raw lines 15–28 — API-only versus Card Component paths, Redirect Component v5.0.0 and Advanced-flow scope, earlier-version route, and merchant card UI.
- `## Collect additional parameters in your payment form` and `## Import the Redirect Component`, raw lines 30–43 — billing/email guidance and library import.
- `## Make a payment`, raw lines 44–583 — request field requirements, Android return URL, test/API-library examples, and response routing by `action`.
- `## Handle the redirect`, raw lines 584–589 — action handoff, shopper return, and links to detailed Advanced-flow outcome handling.
- `## Test and go live`, raw lines 590–597 — test/go-live routes and live-region consistency warning.

## Related

- [[adyen]] — provider page.
- [[adyen-3d-secure]] — merchant-facing 3DS2 routes.
- [[adyen-android-sdk]] — separate package-qualified checkout SDK architecture.
- [[adyen-3ds2-android-sdk]] — separate native 3DS2 runtime evidence.
- [[source-adyen-docs-online-payments-3d-secure-redirect-3ds2-ios-component]] — iOS Components redirect guide with different app-return handling.

## Raw Sources

- [[raw/adyen/docs/online-payments/3d-secure/redirect-3ds2/android-component/2026-09-15|Adyen Docs — Redirect 3DS2 Android Component (2026-09-15 snapshot)]]
