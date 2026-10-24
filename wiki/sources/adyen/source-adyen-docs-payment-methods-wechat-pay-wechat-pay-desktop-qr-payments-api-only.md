---
title: "Adyen WeChat Pay web API-only redirect guide (desktop QR path)"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/wechat-pay/wechat-pay-desktop-qr-payments/api-only"
raw_files:
  - "adyen/docs/payment-methods/wechat-pay/wechat-pay-desktop-qr-payments/api-only/2026-09-15.md"
tags: [adyen, wechat-pay, api-only, redirect, web]
---

## Overview

The canonical path places this 2026-09-15 capture under WeChat Pay **desktop QR payments**, but its own title/body say **WeChat Pay web for API only** and describe a `wechatpayWeb` **redirect** flow. It provides no QR-code payload, rendering step or expiry rule. Treat the path as navigation, not proof that this body documents desktop QR mechanics. The page carries 2019-09-06 last-modified metadata and is not evidence of current merchant eligibility or payment success. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- Start from an existing Web API-only Advanced integration and add WeChat Pay web in **test** Customer Area. Build the payment form with a WeChat Pay web option; this page says no shopper fields need collecting there. For `/paymentMethods` discovery it says a supported shopper country/region **outside China** (NL example), any **supported** currency (EUR example), and channel `Web`, `iOS` or `Android`; illustrative response type is `wechatpayWeb`. It does not supply a complete supported-country/currency list. The processing-currency link points to an Alipay URL, so that link should not be treated as a verified WeChat currency list.
- A server `/payments` request uses `paymentMethod.type: wechatpayWeb`, amount, merchant account, reference and `returnUrl` in the TEST **v68** curl example. The illustrative response is `RedirectShopper` with a GET `action.url`; redirecting to that URL is an intermediate shopper action, not authorization. For mobile use, the guide recommends the default device browser, with SFSafariViewController/Chrome Custom Tabs preferred over WebView for an in-app GET display. This API-only web page does not define H5-in-WeChat, Mini Program or QR-specific setup.
- On return to the website, send the URL-decoded `redirectResult` in `/payments/details`; its example uses TEST **v72**, different from the v68 `/payments` example. Use the details `resultCode` for shopper-facing status and `pspReference` as transaction identifier. Its example `Authorised` is illustrative; `Pending`/`Received` mean the order was received and await final AUTHORISATION webhook. The result table also gives `Error` and `Refused` handling. The stated two-to-three-day funds timing is a guide claim, not actual capture, settlement or bank-receipt evidence.
- The page says WeChat Pay has **no test platform**, despite Adyen Checkout TEST endpoint and redirect examples. Its suggested personal-account test routes are canceling at verification or making a small live payment; neither was performed. A separate request in live Customer Area is required before accepting live WeChat Pay payments. The snippets and example redirect cannot establish a provider test payment or live enablement.

## Detail locators

- Identity/title and 2019 metadata, prerequisites, form and `/paymentMethods` country/currency/channel/type: raw lines 1–40. TEST v68 `/payments` method/request and versioned library examples: raw lines 42–347.
- Redirect action example and client/browser guidance: raw lines 349–374. Returned `redirectResult`, TEST v72 `/payments/details` and illustrative result: raw lines 375–404. Result table and webhook-final Pending/Received boundary: raw lines 406–417. Provider test-platform/live setup limits: raw lines 419–428.

## Related

- [[adyen-online-payments]] — parent server/client and outcome context.
- [[source-adyen-docs-payment-methods-wechat-pay]] — separately captured overview of desktop QR, H5, in-app and Mini Program routes; this page's body should not be used to fill absent QR mechanics.

## Raw Sources

- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-desktop-qr-payments/api-only/2026-09-15|WeChat Pay web API-only page at desktop QR path, captured 2026-09-15]]
