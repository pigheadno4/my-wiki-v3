---
title: "MB Way Android Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mb-way/android-component"
raw_files:
  - "adyen/docs/payment-methods/mb-way/android-component/2026-09-15.md"
tags: [adyen, mb-way, android, components, payments]
---

## Overview

This 2026-09-15 guide gives MB Way-specific additions to an existing Adyen Android Components integration. It separates Sessions and Advanced server-side flows, with Jetpack Compose and view-based Component examples. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions flow:** requires an existing Android Components Sessions integration, Checkout API v68 or later, and MB Way added in Customer Area. The method-specific `/sessions` table marks `shopperStatement` required. The guide imports the `mbway` module, plus `components-compose` when using Compose, and launches `MBWayComponent` using the session payment method. See raw lines 25–165.
- **Advanced flow:** requires an existing Android Components Advanced integration, MB Way setup, and handling of an additional `await` action. The method-specific `/payments` table marks `paymentMethod.type = mbway` and `paymentMethod.telephoneNumber` required, while `shopperStatement` is optional. This requirement table differs from the Sessions table; no Checkout API minimum is stated in the Advanced requirements. See raw lines 189–311.
- The standard Advanced response is described as `Pending`: the shopper must complete payment in the MB WAY app, and the returned action displays a waiting screen. The example action has `type: await`. `Pending` is not final payment success. See raw lines 337–354.
- The optional **App2App** flow deep links the shopper to the MB WAY app without manual phone entry. It says to include `channel` as **iOS or Android** and a `returnUrl` in `/payments`; missing `channel` or **Web** uses the standard phone-number flow. The response `action.url` contains an MB WAY deep link with the return URL appended. Redirect directly to that URL, without an intermediate page; after authorization in the app, the shopper is redirected to the supplied return URL. This is a distinct flow from the standard Advanced request field table, which marks the telephone number required. See raw lines 356–412.
- Both sections say any telephone number can be used for testing, show Customer Area payment-list checks, and require MB Way to be added in the **live Customer Area** before accepting live payments. Test-only `shopperStatement` suffixes trigger `Authorised` (`-c1`, described as default), `Pending` (`-c3`), or `Refused` (`-c5`) responses; the suffix guidance expressly refers to `/payments` even where it appears under Sessions. These test outcomes do not establish live payment behavior. See raw lines 168–187 and 414–433.

## Detail locators

- Sessions prerequisites, request field, import, configuration and Component mounting: raw lines 25–165.
- Advanced prerequisites, Compose/view imports and mounting, request fields: raw lines 189–335.
- Advanced Pending/await response and App2App: raw lines 337–412.
- Test, live enablement and result-code suffixes: raw lines 168–187 and 414–433.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/mb-way/android-component/2026-09-15|MB Way Android Component, captured 2026-09-15]]
