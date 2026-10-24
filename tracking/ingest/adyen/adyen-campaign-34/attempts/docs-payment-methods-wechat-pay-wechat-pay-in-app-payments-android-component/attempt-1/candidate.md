---
title: "Adyen WeChat Pay in-app Android Component v5"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/wechat-pay/wechat-pay-in-app-payments/android-component"
raw_files:
  - "adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/android-component/2026-09-15.md"
tags: [adyen, wechat-pay, android, components, in-app, online-payments]
---

## Overview

This 2026-09-15 Adyen guide adds **WeChat Pay** to an existing **Android Components** integration on the page's **v5.0.0** path. It gives separate Sessions and Advanced base-guide routes and limited method-specific additions. It sends earlier SDK versions to a separate guide; do not import that guide's steps into this version's claims. The dated page does not establish current provider or merchant eligibility or successful processing. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Version and flow:** The page calls itself the guide for **v5.0.0, released October 2023**, and directs earlier versions elsewhere. Both Sessions and Advanced tabs require an existing corresponding Android Components integration with a **minimum required version 5.0.0**, and both say to add WeChat Pay in Adyen Customer Area. This is the SDK Component integration minimum stated here, not a Checkout API version minimum. (raw lines 19–39)
- **Method-specific request/configuration:** The Sessions tab says WeChat Pay requires no additional fields in `/sessions`; Advanced says no additional fields in `/payments`. Both tabs say no additional **WeChat Pay Component** configuration is required. The page then points Sessions to creation of the checkout session and Advanced to launching and showing the Component. These statements assume the linked base integration and do not waive its general fields, client key, SDK setup or server responsibilities. (raw lines 41–67)
- **Scope of procedure:** This short add-on does not state how to register a WeChat app, obtain credentials, perform an SDK app switch, return an Android Intent, submit `/payments/details`, or interpret an asynchronous webhook. It links WeChat Open Platform, Android, Webhooks and API Explorer only as further navigation. Its final generic Android Components See also link targets the **Sessions** guide even though it also has an Advanced tab; follow the tab's flow-specific base link. The separate [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments-android-component-earlier-versions]] covers a different version scope. (raw lines 19–86)
- **TEST/LIVE qualification:** The page says WeChat Pay had **no test platform** and suggests, for a personal WeChat account, cancelling at payment verification or making a low-value **live** payment. It points to live Customer Area for checking status and says a WeChat Pay request must be submitted there before accepting live payments. These are instructions, not proof a request was approved or any payment was run; no real provider, account or financial operation was performed during ingestion. (raw lines 69–78)

## Detail locators

- v5.0.0 scope, Sessions and Advanced requirements: raw lines 19–39.
- Flow-specific no-extra-fields/configuration and next base-guide links: raw lines 41–67.
- No-test-platform guidance, live request and See also navigation: raw lines 69–86.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-android-sdk]]
- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments-android-component-earlier-versions]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/android-component/2026-09-15|Adyen WeChat Pay in-app Android Component v5 guide, 2026-09-15 snapshot]]
