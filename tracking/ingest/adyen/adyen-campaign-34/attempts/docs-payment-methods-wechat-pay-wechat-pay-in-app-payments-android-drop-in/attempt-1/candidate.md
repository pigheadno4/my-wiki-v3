---
title: "Adyen WeChat Pay Android Drop-in v5"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/wechat-pay/wechat-pay-in-app-payments/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/android-drop-in/2026-09-15.md"
tags: [adyen, wechat-pay, android, drop-in, mobile-payments]
---

## Overview

This [[adyen]] guide adds WeChat Pay to an **existing Android Drop-in** integration. It explicitly scopes itself to **v5.0.0**, released October 2023, and sends earlier versions to a separate guide. Sessions and Advanced are both described here; do not transfer this page's v5 route to earlier-version evidence. See [[adyen-online-payments]]. This captured guide describes prerequisites and routing, not observed authorization, capture, settlement or current account eligibility. See raw lines 15–21.

## Flow and integration boundaries

- **Sessions:** Requires an existing Android Drop-in Sessions integration at **minimum v5.0.0** and WeChat Pay added in Customer Area. The ordinary `/sessions` request needs no additional WeChat Pay fields, and Drop-in needs no WeChat Pay-specific configuration. After configuration, create the checkout session using the main integration flow. See raw lines 23–32, 41–45, 51–63.
- **Advanced:** Requires an existing Android Drop-in Advanced integration at **minimum v5.0.0** and WeChat Pay added in Customer Area. The ordinary `/payments` request needs no additional WeChat Pay fields or Drop-in configuration; then launch and show Drop-in using the main flow. These “no additional” statements are method-specific additions to a pre-existing integration, not a claim that base request, app setup, payment action handling or merchant setup is unnecessary. See raw lines 34–39, 47–67.
- This v5 page gives no Android-specific WeChat SDK registration snippet, app-switch callback contract or detailed server response/action sequence. Its “See also” links to WeChat Open Platform, Android app, Android Drop-in main guide, Webhooks and API Explorer are navigation rather than implementation proof. Use the selected base flow and version-matched detailed guides for those steps. See raw lines 19–21 and 80–86.

## Testing and outcome boundary

- The page says WeChat Pay has **no test platform** at this snapshot. It describes two ways for a holder of a personal WeChat account to test: cancel when asked to verify payment (**recommended**) or make a low-value **live** WeChat Pay payment. These are source-described options, not operations carried out by this ingest or proof that a live test succeeded. See raw lines 69–74.
- It directs readers to inspect status in the **live Customer Area** Payments list and says the merchant must submit a request for WeChat Pay in the **live Customer Area** before accepting live payments. Submission is not approval or payment success. This page does not spell out a final webhook event contract; the earlier-version Android Drop-in guide and in-app API-only guide have separate result-handling details and should not be substituted without matching version/flow. See raw lines 76–86.

## Detail locators

- **v5.0.0 scope and older-version route:** raw lines 19–21.
- **Sessions/Advanced prerequisites and Customer Area setup:** raw lines 23–39.
- **No method-specific fields/configuration, checkout launch:** raw lines 41–67.
- **No TEST platform, historical test options and live gate:** raw lines 69–78.
- **Provider/main-guide/webhook references:** raw lines 80–86.

## Related

- [[adyen-online-payments]]
- [[adyen-android-sdk]]
- [[adyen-webhooks]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/android-drop-in/earlier-versions/2026-09-15|Earlier-version Android Drop-in]] — separate version baseline and flow details; not applicable to v5 by default.
- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/api-only/2026-09-15|WeChat Pay in-app API-only]] — separate mobile SDK and server request/result flow.

## Raw Sources

- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/android-drop-in/2026-09-15|WeChat Pay Android Drop-in v5 — captured 2026-09-15]]
