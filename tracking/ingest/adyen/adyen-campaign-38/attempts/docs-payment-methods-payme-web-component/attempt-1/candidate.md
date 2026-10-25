---
title: "PayMe Web Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payme/web-component"
raw_files:
  - "adyen/docs/payment-methods/payme/web-component/2026-09-15.md"
tags: [adyen, payme, web-components, qr-code, redirect, online-payments]
---

## Overview

This 2019-modified, 2026-09-15-captured guide describes adding PayMe QR to an existing Adyen Web Components integration. It differentiates desktop QR scanning from mobile PayMe-app redirect and gives Sessions/Advanced, versioned Component, and sandbox examples. It does not show a real authorized or settled payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Device and integration scope:** on desktop/laptop, the Component shows a QR code to scan with the PayMe app; on mobile browser, it redirects to the app. The guide says to implement both device flows and states PayMe support begins at Web Components **5.56.0**. Sessions and Advanced paths each require an existing Web Components integration and PayMe added in Customer Area. (raw lines 19–46)
- **Versioned Component construction:** for Web Components v6, the page imports `AdyenCheckout` and `PayMe` and later uses `new PayMe(checkout).mount(...)`; for v5.x.x or earlier, it shows `checkout.create('payme').mount(...)`. The “v5.x.x or earlier” snippet must be read with the page's 5.56.0 PayMe-support floor; it does not establish support in versions below that floor. The v6 import link targets an `integration=Drop-in` URL despite this Components guide. (raw lines 28, 48–54, 228–258)
- **API table and examples:** the page lists `channel` and `lineItems` fields for both `/sessions` and `/payments`; the Required column is blank, so it does not mark those table entries required. `lineItems.sku` is stated as available with Checkout API v70+. The sessions tab calls that endpoint the Components v5.0.0+ default, a generic integration statement that does not override PayMe's 5.56.0 support floor. The illustrated `/v72/payments` TEST requests use `payme`, HK/HKD and line items, but are examples rather than a universal API minimum or live eligibility proof. (raw lines 56–84, 86–224)
- **Example conflict and outcome boundary:** the mobile curl example sets `channel: "Web"`, while the mobile NodeJS example uses `"Web/iOS/Android"`; the guide does not reconcile them. It sends payment-outcome handling to the main Web Components guide. A QR display, app redirect, request or return is not final payment proof. (raw lines 156–226)
- **Sandbox cases:** the PayMe sandbox does not require the PayMe app, and amount endings are documented to simulate `Authorised` (30/81), `OfferCancelled` after PayMe's default ten-minute expiry (77/90), or request-creation `Error` (40/44). These are simulator mappings, not observed production outcomes or authorization to transact. The page gives no separate live-enablement procedure. (raw lines 260–270)

## Detail locators

- Desktop QR/mobile app paths, Web support floor and integration prerequisites: raw lines 19–46.
- v6 import and v6/v5 Component construction: raw lines 48–54, 228–258.
- API tables, v70+ SKU gate and TEST examples: raw lines 56–224.
- Conflicting mobile channel snippets and outcome-route link: raw lines 156–226.
- Sandbox amount-ending outcomes and ten-minute expiry: raw lines 260–270.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payme/web-component/2026-09-15|Adyen PayMe Web Component guide, 2026-09-15 snapshot]]
