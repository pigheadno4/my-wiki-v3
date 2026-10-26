---
title: "Adyen Vipps Flutter Drop-in"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/vipps/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/vipps/flutter-drop-in/2026-09-15.md"
tags: [adyen, vipps, flutter, drop-in, online-payments]
---

## Overview

Adyen's 2026-09-15 Vipps Flutter Drop-in page describes Vipps-specific additions to an existing Flutter Drop-in integration, separately for Sessions and Advanced server-side flows. It refers general steps to the main integration guides. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- For Sessions, the page requires an existing Flutter Drop-in Sessions integration, Checkout API v68 or later, and redirect handling for `action.type: redirect`. Its setup row says to contact Adyen Support to add Vipps in Customer Area. The `/sessions` table lists `shopperStatement` (falling back to `reference` for the Vipps app description) and `amount.value` in minor units, with a Vipps minimum of 100 minor units, or 1.00 NOK. The table leaves its Required cells blank, so it does not establish these as additional mandatory properties. No Vipps-specific Drop-in configuration is stated.
- For Advanced, the page requires an existing Flutter Drop-in Advanced integration and redirect handling, but its setup row instead says to add Vipps in Customer Area. Its `/payments` table lists `paymentMethod.telephoneNumber` for prefill on the Vipps-hosted page, `shopperStatement` with the same fallback, `channel`, and `amount.value` with the same minimum; Required cells are blank. The example uses NOK, `type: vipps`, and `channel: Flutter`. The example response is `RedirectShopper` with `action.type: redirect`, an intermediate action rather than payment authorization or settlement.
- TEST guidance directs the merchant to configure a Vipps test app, add Vipps to the test merchant account, make a payment request, and have the shopper authorize the notification in the app. Live acceptance requires a separate request in live Customer Area; the page then recommends a low-amount payment and checking the server's `AUTHORISATION` webhook and payment list for status. Shopper app authorization is not itself the later payment-status event.
- Preserve source discrepancies: the Sessions integration-type row links to an Advanced-flow URL despite its Sessions heading; Sessions says contact Support for Customer Area setup while Advanced gives a direct add-method link. The Advanced channel table gives Web/iOS/Android as examples, while its request uses `Flutter`; the Advanced sample return URL is an HTTPS web checkout URL despite the Flutter title and the Sessions sample's app-scheme return URL. These examples do not establish universal channel/return-URL rules. The v71 `/sessions` and v72 `/payments` examples do not replace the explicit Sessions v68-or-later minimum.

## Detail locators

- Sessions requirements, including URL/setup discrepancy: raw lines 25-36.
- Sessions parameter table, 100-unit minimum and v71 example: raw lines 38-68.
- Sessions configuration and TEST/live guidance: raw lines 70-102.
- Advanced requirements and configuration: raw lines 104-120.
- Advanced `/payments` table, v72 example and redirect response: raw lines 122-174.
- API-reference mismatch: in that Advanced `/payments` table, `channel` and `amount.value` link to `/paymentMethods` field anchors (raw lines 132-133). Those links do not establish the `/payments` field schema; verify against the `/payments` reference before implementation.
- Repeated Advanced TEST/live guidance and status checks: raw lines 176-202.

## Related

- [[adyen-webhooks]] — payment-status event context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/vipps/flutter-drop-in/2026-09-15|Vipps Flutter Drop-in (2026-09-15 snapshot)]]
