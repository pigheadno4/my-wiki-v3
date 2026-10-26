---
title: "Vipps Android Component"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/vipps/android-component"
raw_files:
  - "adyen/docs/payment-methods/vipps/android-component/2026-09-15.md"
tags: [adyen, vipps, android, components, redirect, online-payments]
---

## Overview

This 2026-09-15 guide adds Vipps to an existing Adyen Android Components integration. It separates Sessions and Advanced server-side flows, using `InstantPaymentComponent` with redirect handling, and gives test-app and live-request steps. The retained page describes integration instructions, not present merchant eligibility or observed authorization, capture, or settlement. [[adyen]] [[adyen-online-payments]] [[adyen-android-sdk]]

## Key takeaways

- **Sessions prerequisites and request:** an existing Android Components Sessions flow, Checkout API v68 or later, `action.type: redirect` handling, and Vipps added in Customer Area. The `/sessions` table describes optional `shopperStatement`; when absent, the payment `reference` populates the statement shown in the Vipps app. It states a Vipps minimum `amount.value` of 100 minor units, or 1.00 NOK. The NOK/NO request is an example, not a claim of broader currency or country support. (raw lines 25–68)
- **Sessions Component:** import `com.adyen.checkout:instant`; add `components-compose` for Jetpack Compose. The page says no Vipps-specific configuration is needed. Its examples select method `vipps` from the checkout session and launch `InstantPaymentComponent` for Compose or an Android view. The Compose example calls for a new unique key on a different screen/session or reset. (raw lines 70–152)
- **Advanced flow:** requires an existing Android Components Advanced flow, additional redirect-action handling, and Customer Area addition. The examples select `vipps` from `/paymentMethods`, then use `InstantPaymentComponent`; they state no extra Component configuration. The `/payments` table lists optional `paymentMethod.telephoneNumber` to prefill the Vipps-hosted page, `shopperStatement` with the same reference fallback, `channel`, and the 100-minor-unit minimum. The sample uses `channel: Android`, NOK and a web return URL as example values. The response example is `RedirectShopper` with a redirect action, an intermediate handoff rather than a final payment result. (raw lines 182–330)
- **Environment and outcome boundary:** test instructions first require the Vipps test app setup, then adding Vipps in the test Customer Area, creating a request and authorizing via the app notification. Live acceptance requires a separate request in the live Customer Area. Once Adyen adds Vipps there, the guide describes a low-amount live test, server receipt of an `AUTHORISATION` webhook carrying payment status, and checking the live payment list. Shopper approval in the app and a redirect response alone do not establish final server-side authorization. (raw lines 154–180, 332–358)

## Detail locators

- Sessions prerequisites, optional statement and minimum: raw lines 29–47.
- Sessions imports, Compose/view examples and key lifecycle: raw lines 70–152.
- Advanced imports, method selection, request parameters and redirect response: raw lines 184–330. The `channel` and `amount.value` parameter links in the `/payments` section point to `/paymentMethods` API-reference anchors; follow the linked API reference before relying on those locators.
- Test-app credentials and steps: raw lines 154–170 and 332–348. Live request and status checks: raw lines 172–180 and 350–358.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-android-sdk]]
- [[source-adyen-docs-payment-methods-vipps]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/vipps/android-component/2026-09-15|Vipps Android Component guide, 2026-09-15 snapshot]]
