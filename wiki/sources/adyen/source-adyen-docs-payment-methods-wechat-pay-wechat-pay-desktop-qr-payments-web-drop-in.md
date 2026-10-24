---
title: "WeChat Pay Web Drop-in: desktop QR and mobile-browser setup"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/wechat-pay/wechat-pay-desktop-qr-payments/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/wechat-pay/wechat-pay-desktop-qr-payments/web-drop-in/2026-09-15.md"
tags: [adyen, wechat-pay, web, drop-in, qr]
---

## Overview

This 2026-09-15 capture of a page last modified in 2020 describes adding WeChat Pay to an **existing Web Drop-in** integration. Although its URL sits under desktop QR payments, it states distinct setup steps for desktop QR and mobile-browser flows. It is an add-on and routing guide, not a QR rendering, scan, redirect-processing or payment-outcome procedure. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Base flow:** the `/sessions` tab requires an existing Sessions-flow Web Drop-in integration; the `/payments` tab requires an existing Advanced-flow Web Drop-in integration. The page does not give a Checkout API minimum for either flow. (raw lines 21–39)
- **Different WeChat enrollment paths:** for **desktop QR code**, both tabs say to add WeChat Pay in Customer Area. For **mobile browser**, both say to contact Adyen Support with the web shop URL for enrollment with WeChat Pay. The page does not say the desktop setup alone enrolls the mobile-browser flow, or give QR display/scan or H5 redirect details. (raw lines 29–39)
- **Web Drop-in v6 resource and request scope:** v6 users are shown an import of `AdyenCheckout` and `WeChat` from `@adyen/adyen-web`. The page says no additional WeChat Pay-specific fields and points to optional common fields at `/sessions` and `/payments`; it calls `/sessions` the default with Web Drop-in **v5.0.0 or later** and `/payments` an additional-use-case route. It says no required WeChat Pay-specific Drop-in configuration. Those method-specific statements do not replace the selected base integration. (raw lines 41–58)
- **Status and LIVE gate:** the page routes payment-status lookup to Customer Area's payment list and says a request in **live Customer Area** is needed before accepting live WeChat Pay. It does not specify a TEST platform or show a successful authorization, webhook, capture, settlement or refund. The “Webhooks” item in See also is navigation, not an on-page event sequence. (raw lines 60–70)

## Detail locators

- Sessions and Advanced prerequisites plus separate desktop QR/mobile-browser enrollment wording: raw lines 21–39.
- v6 imports and endpoint/configuration scope: raw lines 41–58.
- Customer Area status path, live request and further links: raw lines 60–70.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-wechat-pay]]
- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-desktop-qr-payments-api-only]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-desktop-qr-payments/web-drop-in/2026-09-15|Adyen WeChat Pay Web Drop-in, 2026-09-15 snapshot]]
