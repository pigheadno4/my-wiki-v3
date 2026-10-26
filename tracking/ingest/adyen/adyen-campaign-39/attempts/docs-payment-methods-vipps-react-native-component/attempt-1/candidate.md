---
title: "Adyen Vipps React Native Component"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/vipps/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/vipps/react-native-component/2026-09-15.md"
tags: [adyen, vipps, react-native, components, redirect, online-payments]
---

## Overview

This 2026-09-15 Adyen guide describes Vipps-specific additions to an existing React Native Components integration. It explicitly excludes Sessions flow and covers Advanced-flow redirect setup, request fields, and TEST/LIVE onboarding. It is a dated guide, not evidence of current merchant enablement or successful payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Flow boundary:** The page states React Native Components do not support Sessions flow. Its supported path here is an existing Advanced React Native Components integration with `action.type: redirect` handling and Vipps added in Customer Area. The Advanced Integration type link is mislabeled in its URL as `integration=Drop-in`, while the redirect and payment links use Components. No separate Checkout API minimum is stated in this guide. (raw lines 19–41)
- **Advanced request:** No additional Vipps configuration parameters are stated. The `/payments` table describes `paymentMethod.telephoneNumber` to prefill the Vipps-hosted page, `shopperStatement` as the app description with `reference` fallback when omitted, a relevant `channel`, and minimum `amount.value` 100 minor units/1.00 NOK. Its Required cells are blank; do not infer that every listed field is mandatory. (raw lines 43–60)
- **Redirect versus outcome:** The example response is `resultCode: RedirectShopper` with `action.type: redirect`; that handoff is not final authorization, capture or settlement. For low-amount live tests, the guide says to receive the `AUTHORISATION` webhook on the merchant server and inspect status in the live Customer Area payment list. The page does not spell out return/details or capture/refund processing. (raw lines 87–101, 121–129)
- **TEST and LIVE:** TEST guidance uses a Vipps developer test app, adds Vipps to the test merchant account, submits a test payment and has the shopper authorize its app notification. Live acceptance requires a separate request in live Customer Area; after Adyen adds Vipps, the page calls for low-amount live payments and status checks. Neither test-app authorization nor the redirect response proves a live payment. (raw lines 103–129)
- **Example caution:** The Advanced Components prerequisite points to a Drop-in URL. The request example uses `channel: React-native` although the table illustrates Web, iOS and Android; its curl command also lacks a line continuation between `-X POST` and `-d`. Treat these as source-level example issues and verify the versioned base integration before use. (raw lines 39, 59, 64–85)

## Detail locators

- Unsupported Sessions and Advanced prerequisites: raw lines 25–41.
- Configuration and `/payments` field table: raw lines 43–60.
- Sample request and redirect response: raw lines 62–101.
- TEST app and live request/status steps: raw lines 103–129.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-react-native-sdk]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/vipps/react-native-component/2026-09-15|Adyen Vipps React Native Component guide, 2026-09-15 snapshot]]
