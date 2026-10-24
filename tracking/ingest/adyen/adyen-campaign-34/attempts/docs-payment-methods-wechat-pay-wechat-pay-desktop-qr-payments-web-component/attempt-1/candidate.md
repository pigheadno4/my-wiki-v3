---
title: "Adyen WeChat Pay Web Component guide under desktop QR path"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/wechat-pay/wechat-pay-desktop-qr-payments/web-component"
raw_files:
  - "adyen/docs/payment-methods/wechat-pay/wechat-pay-desktop-qr-payments/web-component/2026-09-15.md"
tags: [adyen, wechat-pay, web, component, desktop-qr]
---

## Overview

This [[adyen]] page sits under a **desktop QR payments** URL, but its body is a general **WeChat Pay Web Components** add-on guide. It distinguishes desktop QR setup from **mobile browser** enrolment and gives Sessions/Advanced and Web Component versioned routes. It does not document QR-code payload/rendering/scanning mechanics, expiry, redirect-return handling or a final webhook result; the path label alone must not supply those facts. The source was last modified in 2019 and captured in 2026. [[adyen-online-payments]]

## Key takeaways

- **Flow and setup:** For `/sessions`, the page requires an existing Sessions Web Components integration; for `/payments`, an existing Advanced Web Components integration. In each setup row, the **desktop QR** route says to add WeChat Pay in Customer Area, while the **mobile browser** route says to contact Adyen Support with the web shop URL for WeChat Pay enrolment. These provider/merchant setup paths are distinct, and a request or enrolment contact does not prove approval. See raw lines 21–37.
- **Server fields:** It says no **additional WeChat Pay-specific** fields are needed; optional general-method fields remain available on the integrated endpoint. It labels `/sessions` the default for Components **v5.0.0 or later** and `/payments` an additional-use-case route. This does not eliminate the base request or establish Checkout API version minima. See raw lines 47–52.
- **Client version split:** For **Web Components v6**, the guide imports `AdyenCheckout` and `WeChat` from `@adyen/adyen-web`. For **v6.0.0 or later**, its example mounts `new WeChat(checkout)`; for **v5.x.x or earlier**, it mounts `checkout.create('wechatpayWeb')`. Both examples target a `wechatpayWeb-container` DOM element. The import link in the v6 section contains `integration=Drop-in` despite Web Components prose; follow the versioned prose and validate the appropriate main guide. See raw lines 39–45 and 54–84.
- **Live/status boundary:** The page points to the **live Customer Area** Payments list for payment status and says to submit a separate WeChat Pay request there before accepting live payments. It links general Web Components, webhooks and API Explorer references without describing webhook event conditions. Status lookup and request submission do not establish live enablement, authorization, capture or settlement. No TEST procedure is stated. See raw lines 86–96.

## Detail locators

- Sessions/Advanced and desktop QR/mobile-browser setup rows: raw lines 21–37.
- Endpoint scope and versioned Web Component import/init: raw lines 39–84.
- Live request/status and navigation-only webhook link: raw lines 86–96.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-desktop-qr-payments-api-only]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-desktop-qr-payments/web-component/2026-09-15|Adyen WeChat Pay Web Component snapshot]]
