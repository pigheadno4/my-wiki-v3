---
title: "Adyen Touch 'n Go Android Redirect Component earlier-version guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/touchngo/android-component/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/touchngo/android-component/earlier-versions/2026-09-15.md"
tags: [adyen, touchngo, android, component, redirect, earlier-versions]
---

## Overview

This [[adyen]] **earlier-version Touch 'n Go Android Component** guide describes a merchant-server **Advanced** payment request, Android Redirect Component handoff, and a server-side `/payments/details` call after shopper return. The displayed title is malformed (“Touch v4.x.x integration'n Go Android Component”); treat **v4.x.x** as the page's historical label, not a verified current Android SDK minimum. The source was recorded as last modified in 2019 and captured in 2026. Its example responses and status lookup are illustrative, not evidence of a completed or final transaction. [[adyen-online-payments]]

## Key takeaways

- **Integration/setup conflict:** The introduction and See also route to a **Sessions-flow Android Components** guide, but the Requirements table explicitly says to have an **Advanced-flow Android Components** integration. The redirect-handling step also links a Sessions guide. Preserve this mismatch and use the flow-specific requirements plus the main guide rather than combining the links into a single supported flow. Before setup, the page directs contacting Adyen Support to add Touch 'n Go in Customer Area; live acceptance has a further Support/live Customer Area instruction. See raw lines 19–26, 366–368 and 399–409.
- **Method discovery and request:** The guide says no shopper fields need be collected in the payment form. It instructs `/paymentMethods` discovery with **MY** country and **MYR** currency, but its `channel` value is blank (`****`), so this page cannot supply that value. It identifies response `paymentMethod.type: touchngo`. For server `/payments`, it lists `paymentMethod.type: touchngo` and a return URL no longer than **1024 characters**, obtained from `RedirectComponent.getReturnUrl(context)`. Prose spells the field `returnURL`, while code examples use `returnUrl`; do not silently normalize this conflict. See raw lines 28–47 and 49–348.
- **Redirect and return:** The page says to use the Redirect Component to send the shopper to Touch 'n Go, then submit `actionComponentData.details` in server `POST /payments/details` after return. An example `/payments` response has `RedirectShopper` and a redirect action; an example details response has `Authorised` and `pspReference`. The examples show **v68 /payments** but **v72 /payments/details**, and library examples have differing versions. The page does not establish a single API-version minimum or webhook-final outcome rule; the Webhooks item is only a link. A sample Authorised response is not evidence for any real payment. See raw lines 49–348 and 350–409.
- **Environment boundary:** Examples use TEST endpoints and placeholder credentials. The guide directs test-status lookup in TEST Customer Area and says to contact Support to add Touch 'n Go in **live** Customer Area before live acceptance. Neither operation proves live merchant eligibility or successful authorization, capture or settlement. See raw lines 49–101 and 399–403.

## Detail locators

- Historical title, route conflict and setup: raw lines 6–26.
- MY/MYR discovery, incomplete channel and request/return URL: raw lines 28–47.
- Multi-language TEST examples and version variation: raw lines 49–348.
- Redirect action, details call and illustrative responses: raw lines 350–397.
- TEST/live status and navigation: raw lines 399–409.

## Related

- [[adyen-online-payments]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/touchngo/android-component/earlier-versions/2026-09-15|Adyen Touch 'n Go Android earlier-version snapshot]]
