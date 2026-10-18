---
title: "Adyen for Platforms: Checkout components"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/online-payments/checkout-components"
raw_files:
  - "adyen/docs/platforms/online-payments/checkout-components/2026-09-15.md"
tags: [adyen, platforms, online-payments, checkout, web-components]
---

## Overview

Adyen's 2026-09-15 snapshot explains how a platform can build a web checkout page with payment-method-specific Adyen Web Components. It contrasts API-only, Hosted Checkout, Drop-in, and Components, and recommends Components for prebuilt UI with per-method customization. This guide's concrete flow creates a Checkout `/sessions` payment session on the server, then initializes `AdyenCheckout` and mounts available Components on the client. [[adyen]] [[adyen-platforms]] [[adyen-online-payments]]

## Key takeaways

- The integration separates a payment server, client website, and webhook server. The client presents the Component and current payment result; an asynchronous `AUTHORISATION` webhook provides the outcome used to update the order management system, matched by `merchantReference`. A UI callback or session-result display alone is not proof of capture, settlement, or payout.
- Session creation requires merchant account, amount with currency and minor-unit value, return URL, and unique reference. Shopper country and currency filter available methods. The return URL must exclude personally identifiable information; session expiry defaults to one hour and cannot exceed 24 hours when set.
- `AdyenCheckout` represents one payment and its session/environment/amount; individual Components present payment-method-specific UI. The page introduces Web v6, while server API libraries and Checkout API versions are separate version surfaces. Payment-method-specific configuration and eligibility still depend on the relevant method and account setup.
- Customer Area merchant-admin and API-credential-management roles, an API credential, API key, client key, payment API roles, and a Standard webhook are stated prerequisites. The page also flags iframe/redirect, WebView, client-side SSR initialization, and strict-CSP/3DS2 constraints.
- For redirects, the return URL may carry `sessionId` and `redirectResult`; if the shopper does not return, wait for the webhook. The server-side session-result `status` is a fixed response, not a polling route for later changes. Test each intended method, then complete live account/PCI/account/HTTPS/payment-method/endpoint setup. Keep one live endpoint region for the same session and match the Component environment to it.

## Detail locators

- Raw `How it works`, `Integration steps`, and `Payment flow` (lines 52–85): three integration parts and Sessions-flow sequence.
- Raw `Requirements` (lines 111–130): roles, credentials, webhook, browser/embedding/SSR/CSP limitations, and test-account preparation.
- Raw `Install an API library` and `Create a session` (lines 134–510): language-specific server libraries, request fields, minor units, country/method filtering, expiry, and example response.
- Raw `Prepare your front end`, `Create the Component`, and `Localization` (lines 514–869): npm/CDN/SRI delivery, initialization, amount/locale/event configuration, available-method check, and per-method Component mounting.
- Raw `Handle the payment`, `Get the payment outcome`, and `Update your order management system` (lines 870–1063): redirect handling, client events, fixed session-result status, and asynchronous webhook.
- Raw `Test and go live` (lines 1064–1105): test-to-live checklist, endpoint-region consistency, environment mapping, and update guidance.

## Related

- [[adyen-platforms]] — platform integration context.
- [[adyen-online-payments]] — general online-payment architecture and lifecycle.
- [[source-adyen-docs-online-payments-build-your-integration]] — general Sessions and Advanced-flow selection; this page details the Sessions Components route.
- [[source-adyen-docs-online-payments-upgrade-your-integration-upgrade-to-web-v6]] — separate Web v6 migration details.
- [[source-adyen-docs-online-payments-go-live-checklist]] — broader live-readiness route.

## Raw Sources

- [[raw/adyen/docs/platforms/online-payments/checkout-components/2026-09-15|Adyen Checkout components webpage snapshot (2026-09-15)]]
