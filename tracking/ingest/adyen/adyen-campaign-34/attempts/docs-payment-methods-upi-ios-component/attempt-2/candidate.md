---
title: "Adyen UPI iOS Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/upi/ios-component"
raw_files:
  - "adyen/docs/payment-methods/upi/ios-component/2026-09-15.md"
tags: [adyen, upi, ios, components, india, wallet-payments]
---

## Overview

This [[adyen]] page adds UPI-specific steps to an **existing iOS Components** integration, with separate Sessions and Advanced server-side flows. It focuses on **UPI Intent** and iOS app discovery, not an iOS QR or legacy Collect implementation. See [[adyen-online-payments]]. Its test checklist mentions UPI QR **on web** only. This page gives no Collect deprecation date; see the separate UPI overview/API-only evidence for those historical notices rather than importing them into this iOS procedure. The captured guide and examples do not prove current eligibility, app availability or a successful live payment. See raw lines 15–23, 94–136 and 254–274.

## Sessions flow

- Requires an existing Sessions iOS Components integration, Checkout API **v68 or later**, and UPI added in Customer Area. No UPI-specific parameters are needed in the base `/sessions` request. See raw lines 25–41.
- For UPI Intent, Smart Intent detects installed UPI apps **only among apps whose URL schemes the merchant declares** under `LSApplicationQueriesSchemes` in its iOS `Info.plist`. iOS privacy rules prevent detection without declaration, limit the list to **50** schemes per app, and the Component handles none detected. The page lists twelve app/scheme pairs as of its snapshot, including `tez` for Google Pay and `phonepe` for PhonePe; the list is not proof any app is installed on a shopper device or currently supported. See raw lines 43–92.
- The example initializes `UPIComponent` only after finding an `InstantPaymentMethod` in session payment methods, assigns the session as delegate, and presents the Component. Its `configuration:` argument is blank in the snippet; the sample is not a complete compile-ready integration. See raw lines 94–114.

## Advanced flow

- Requires an existing Advanced iOS Components integration, handling an additional `action.type: await`, and UPI added in Customer Area. The Integration type link nevertheless points to `integration=Drop-in` despite saying Components; the Action handling link is Components-scoped but its anchor says “handle-the-redirect” while the declared action type is **await**. Verify the correct base integration step rather than treating either link label as the flow definition. The Advanced table does not restate the Sessions section's v68 minimum. See raw lines 138–148.
- Smart Intent has the same declared-schemes/50-slot/no-app boundary. The Advanced example selects `InstantPaymentMethod`, creates `UPIComponent`, assigns `self` as delegate and presents it; its `configuration:` is also blank. See raw lines 150–220.
- For **Advanced UPI Intent** (`paymentMethod.type: upi_intent`), `paymentMethod.appId` is required and identifies the selected third-party application provider. The table enumerates app IDs, including `gpay`, `phonepe`, `wapay` for WhatsApp Pay and others. The illustrative test `/v72/payments` request uses `INR`, country `IN`, `appId: gpay`, and a return URL; `v72` is the example endpoint, not a separately stated minimum for the whole guide. These fields and URL describe a request/return path, not proof of authorization. See raw lines 222–252.

## Testing and outcome boundary

- In the **test** environment the guide points to Adyen's Payment Simulator. For UPI Intent, it says the test integration redirects to the simulator; its UPI QR instruction is expressly labeled **on web**, so it does not establish an iOS QR Component flow. Select an outcome in the simulator, verify the integration handles it, then follow the TEST checklist's literal `eventCode: AUTHORISED` webhook and Customer Area check; it also recommends testing modifications. This checklist spelling is **not** a verified UPI eventCode contract: the separately retained UPI API-only outcome tables say `AUTHORISATION` (raw API-only lines 112–117, 216–221, 382–387), while that page's TEST checklists repeat `AUTHORISED`. Preserve this cross-page and intra-page conflict and verify the authoritative webhook schema or live evidence before implementing an event-name check. A simulator-selected outcome or app return by itself is not final live payment evidence. See raw lines 116–136 and 254–274.
- No merchant live-approval procedure, production app-to-app return callback, QR iOS Component configuration, Collect flow or deprecation date is specified in this raw page. Their details require separate guides rather than inference from this example. See raw lines 15–274.

## Detail locators

- **Sessions requirements and base session:** raw lines 25–41.
- **iOS Smart Intent schemes and privacy/50-scheme limit:** raw lines 43–92 and 150–199.
- **Component initialization and delegate examples:** raw lines 94–114 and 201–220.
- **Advanced requirements and source-link mismatch:** raw lines 138–148.
- **Advanced Intent `appId` and test `v72` request:** raw lines 222–252.
- **Simulator, web-only QR mention and outcome checks:** raw lines 116–136 and 254–274.

## Related

- [[adyen-online-payments]]
- [[adyen-ios-sdk]]
- [[adyen-webhooks]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/upi/2026-09-15|UPI overview]] — broader Intent/QR/Collect scope and historical Collect transition notice; distinct from this iOS Component page.
- [[raw/adyen/docs/payment-methods/upi/api-only/2026-09-15|UPI API-only]] — separate API flow and historical Collect details.

## Raw Sources

- [[raw/adyen/docs/payment-methods/upi/ios-component/2026-09-15|UPI iOS Component — captured 2026-09-15]]
