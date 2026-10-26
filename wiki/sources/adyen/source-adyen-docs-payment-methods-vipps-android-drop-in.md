---
title: "Vipps Android Drop-in"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/vipps/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/vipps/android-drop-in/2026-09-15.md"
tags: [adyen, vipps, android, drop-in, online-payments, redirect]
---

## Overview

This 2026-09-15 Adyen guide describes adding Vipps to an existing Android Drop-in integration. It gives distinct Sessions and Advanced server-side additions, along with TEST-app and LIVE-request instructions. It does not establish a current merchant's Vipps eligibility or an executed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions:** Use an existing Android Sessions Drop-in integration and Checkout API v68 or later; add Vipps in Customer Area (raw lines 25–34). The `/sessions` table describes `shopperStatement` as the in-app description, falling back to `reference` when omitted, and says Vipps has a minimum `amount.value` of 100 minor units, described as 1.00 NOK (lines 38–45). The page says no extra Vipps configuration parameters are needed (lines 68–72).
- **Advanced:** Use an existing Android Advanced Drop-in integration with redirect handling for `action.type: redirect` and add Vipps in Customer Area (lines 104–112). The `/payments` table describes optional phone prefill on the Vipps-hosted page, shopper-statement fallback, relevant `channel` and the same 100-minor-unit minimum (lines 122–131). The example returns a `redirect` action; its `RedirectShopper` response is an intermediate handoff, not payment completion (lines 133–172). No additional Vipps configuration parameters are stated (lines 114–118).
- **Testing and live setup:** The TEST path directs installing the Vipps test app, adding Vipps to the test merchant account, then authorizing a test payment through the app notification (lines 78–92, 176–190). Live acceptance requires a separate request in the LIVE Customer Area; after addition, the page directs a low-amount payment, checking the AUTHORISATION webhook on the merchant server and status in Payment list (lines 94–102, 192–200). Shopper app authorization and redirect response alone do not establish the final payment outcome.
- The examples show `NOK`, `countryCode: NO` in Sessions, `channel: Android` in Advanced, and Checkout API v71/v72 requests (lines 47–66, 133–156). These are examples; the guide's explicit minimum API version is v68+ for Sessions, and it does not state a corresponding Android SDK version or broader country/currency eligibility matrix.

## Detail locators

- Sessions requirement, `/sessions` field table and example: raw lines 25–66.
- Advanced requirement, `/payments` field table and example redirect action: raw lines 104–172. The Advanced `channel` row points to the `/paymentMethods` API reference even though this section is for `/payments`; resolve request schema against the relevant API reference before implementation.
- TEST app setup fixtures and LIVE request/status checks: raw lines 74–102 and 174–200.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/vipps/android-drop-in/2026-09-15|Vipps Android Drop-in, fetched 2026-09-15]]
