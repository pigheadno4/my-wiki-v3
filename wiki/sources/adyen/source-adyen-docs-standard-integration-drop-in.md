---
title: "Adyen Standard integration with Web Drop-in"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/standard/integration/drop-in"
raw_files:
  - "adyen/docs/standard/integration/drop-in/2026-09-15.md"
tags: [adyen, online-payments, standard-integration, web-drop-in, sessions, webhooks]
---

## Overview

This 2026-09-15 [[adyen]] guide describes a **Standard online-payments integration using Web Drop-in** within [[adyen-online-payments]]. Drop-in supplies the shopper-facing payment-method UI and client-side payment flow; the merchant still implements a payment server to create a Checkout session, a client website to mount Drop-in and handle redirects, and a webhook server for the payment outcome (raw lines 15–19, 42–68).

## Key takeaways

- **Version and setup gates:** The guide specifies Checkout API v72 or later for `/sessions`, a server-side library released March 30, 2026 or later, and Web Drop-in v6.30.0 or later. Its requirements table calls for Merchant admin and Manage API credentials Customer Area roles, an API credential/key and client key, default payment credential roles, a standard webhook with default event codes, and test-account/live-readiness preparation (raw lines 21–52). These are this guide's stated versions and preparations, not proof of live enablement.
- **Session and client boundary:** The payment server posts `/sessions`, passes `session.id` and `session.sessionData` to the website, and the client configures `AdyenCheckout` and mounts Drop-in. The request table describes `merchantAccount`, amount in minor units, `returnUrl`, merchant `reference`, shopper country, `channel: Web` and idempotency key, alongside shopper fields; examples cover multiple server languages (raw lines 56–68, 451–775, 803–958). The raw table marks `countryCode` and `shopperEmail` with required icons while describing a locale fallback and email as “strongly recommended”; do not resolve that inconsistency into an unconditional API-schema claim (raw lines 473–475).
- **Browser and redirect constraints:** The guide calls for same-domain iframe hosting for redirect flows, discourages native-app WebViews, requires client-side initialization under SSR, and says strict CSP can block native 3DS2 challenges unless adjusted or a redirect flow is selected. For redirects, the returning shopper's `sessionId` and `redirectResult` feed `submitDetails`; if the shopper never returns, rely on the webhook rather than assuming a browser result (raw lines 35–38, 973–1024).
- **Outcome authority:** Client `onPaymentCompleted`/`onPaymentFailed` callbacks and `resultCode` inform the shopper of current status. The server uses the standard `AUTHORISATION` webhook, matching `merchantReference` to the session `reference`; `success: true` and `success: false` indicate the authorization event outcome (raw lines 1026–1036, 1054–1134). A shown client result, session creation or authorization webhook is not proof of capture, settlement or merchant receipt.

## Detail locators

- Roles, credentials, embedding and CSP prerequisites: raw lines 21–40.
- Three-part architecture and end-to-end flow: raw lines 42–98.
- API-library examples, session headers/body, response and errors: raw lines 100–801.
- Adyen Web setup, global/Drop-in configuration and mount methods: raw lines 803–971.
- Redirect, shopper result and Drop-in error handling: raw lines 973–1052.
- Standard `AUTHORISATION` webhook and example outcomes: raw lines 1054–1134.

## Evidence boundary

This is a dated Web Sessions/Drop-in integration recipe. The example requests and webhooks are illustrative, not evidence of a live transaction. The guide's own field table contains conditional-versus-required wording tension, and its UI callbacks describe current shopper-facing status; use the server webhook for order-management outcome while keeping authorization distinct from later capture or settlement.

## Related

- [[adyen-online-payments]] — online-payment architecture and release context.
- [[source-adyen-docs-standard]] — Standard integration overview route.

## Raw Sources

- [[raw/adyen/docs/standard/integration/drop-in/2026-09-15|Pinned Standard Web Drop-in guide, captured 2026-09-15]]
