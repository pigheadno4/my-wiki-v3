---
title: "Adyen Marketplace-path Checkout Components"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/checkout-components"
raw_files:
  - "adyen/docs/marketplaces/checkout-components/2026-09-15.md"
tags: [adyen, marketplaces, platforms, online-payments, checkout, web-components]
---

## Overview

This Marketplace-path Adyen Web Components guide describes a Sessions-based web checkout with a server-created Checkout `/sessions` resource, client-side `AdyenCheckout` and payment-method Components, and a webhook server for the asynchronous payment outcome. It contrasts API-only, Hosted Checkout, Drop-in and per-method Components, recommending Components for prebuilt but customizable UI. The page introduces Web v6 improvements, but its language-library snippets and live endpoint regions are separate version surfaces. See [[adyen]], [[adyen-platform-components]] and [[adyen-platforms]]. This checkout setup does not define Marketplace split instructions or prove balance-account booking, capture, settlement, payout or bank receipt.

## Key takeaways

- The integration has three parts: payment server, client website and webhook server. The server creates a session; the client mounts an available payment-method Component and displays the current result; the Standard `AUTHORISATION` webhook supplies the asynchronous payment outcome for order management, matched by `merchantReference`. A Component callback or displayed session result alone is not a financial outcome beyond its stated authorization status.
- Prerequisites in the snapshot include Merchant admin and Manage API credentials Customer Area roles; an API credential, API key and client key; payment API credential roles; a Standard webhook; and TEST-account preparation. It flags same-domain iframe redirect support, WebView limitations, client-side initialization with SSR, and CSP blocking native 3DS2 challenges unless the redirect route is selected. These are integration conditions, not proof of account enablement.
- The server's `/sessions` request identifies merchant account, currency/minor-unit amount, `returnUrl` and unique payment reference; shopper country affects available methods. The `returnUrl` must be URL-encoded if needed and contain no personally identifiable information. Default session expiry is one hour; the configured expiry cannot exceed 24 hours. The client passes session ID/data, environment, amount and client key to `AdyenCheckout`, checks available methods and mounts each selected Component. Payment-method configuration can override global configuration.
- Redirect methods can return `sessionId` and `redirectResult` to the `returnUrl`; submit the result after return or confirm it through a separate server endpoint. If the shopper never returns, do not call `submitDetails` without a result; wait for the webhook. The optional GET session-result response is fixed and should not be polled for later changes. `completed` in that response means authorized in this guide, not captured or settled.
- Go-live steps include a live account/application path, PCI assessment, live configuration, HTTPS, live payment-method requests and switching both API endpoints and Component `environment`. Keep requests for one session in the same live endpoint region; mixing regions for `/payments` and `/payments/details` may fail, including during 3DS2. The sample `AUTHORISATION` event and TEST payment screens are not hosted-live or user-balance evidence.

## Detail locators

- Integration options, Web v6 introduction, three parts and Sessions flow: raw lines 15–85. Roles, credentials, webhook and iframe/WebView/SSR/CSP setup: lines 109–130.
- Server API-library examples and `/sessions` fields, amount units, return URL and expiry: lines 132–512. Adyen Web delivery, Component initialization, configuration/events, localization and mounting: lines 514–869.
- Redirect/no-return handling, fixed session-result statuses and `AUTHORISATION` webhook: lines 870–1062. TEST and live transition, endpoint-region matching and environment values: lines 1064–1105.

## Related

- [[adyen]] — provider context.
- [[adyen-platform-components]] — main platform UI-components concept.
- [[adyen-platforms]] — modern platform and Marketplace model.
- [[source-adyen-docs-platforms-online-payments-checkout-components]] — separately pinned Platforms-path Sessions Components guide.
- [[source-adyen-docs-marketplaces-process-payments]] — Marketplace payment/split and balance-account route; this UI guide does not establish split booking.
- [[adyen-online-payments]] — general online-payment lifecycle.

## Related raw API references

- The raw page links to Checkout `/sessions`, payment result codes, Web v6 upgrade, payment-method configuration, PCI and go-live guides; those linked pages own their detailed or current behavior.

## Raw Sources

- [[raw/adyen/docs/marketplaces/checkout-components/2026-09-15|Adyen Docs: Checkout components (2026-09-15 snapshot)]]
