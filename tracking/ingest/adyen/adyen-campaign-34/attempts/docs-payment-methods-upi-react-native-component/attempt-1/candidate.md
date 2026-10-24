---
title: "Adyen UPI React Native Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/upi/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/upi/react-native-component/2026-09-15.md"
tags: [adyen, upi, react-native, components, india]
---

## Overview

This [[adyen]] page at the **React Native Component** URL is titled “UPI React Component” in its raw heading. It gives UPI-specific additions to an existing React Native **Components** integration and explicitly says **Sessions flow is unsupported**; the documented route is Advanced only. See [[adyen-online-payments]]. It covers UPI Intent request fields and testing, not a native QR/Collect implementation, a React Native SDK minimum or a live payment outcome. See raw lines 15–31 and 49–101.

## Advanced requirements and request

- Requires an existing Advanced React Native Components integration, UPI added in Customer Area, and handling of additional `action.type: await`. It says no UPI-specific configuration parameters are needed. The Integration type link is inconsistent with its label: `platform=React+Native&integration=Drop-in` despite saying **Components**. The action-handling link is Components-scoped but its anchor is `handle-the-redirect` although the explicit action type is **await**. Select the intended Advanced Components main flow from its own evidence. See raw lines 31–47.
- For **UPI Intent** (`paymentMethod.type: upi_intent`), `paymentMethod.appId` is required and denotes the shopper's third-party application provider. The table lists provider IDs including `gpay`, `phonepe`, `bhim`, `paytm`, `amazonpay`, `cred`, `wapay` (WhatsApp Pay), `jupiter`, `navi`, `supermoney`, `mobikwik` and `freecharge`. A listed provider ID is not evidence of app installation or merchant eligibility. See raw lines 49–57.
- The example calls **TEST** `/v72/payments` with `INR`, country `IN`, `upi_intent`, `appId: gpay`, merchant account and return URL. This is an illustrative request, not an explicit minimum Checkout version for this page or proof of app return, authorization or settlement. The page has no separate React Native SDK-version requirement. See raw lines 59–79.

## Testing and outcome boundary

- The TEST checklist sends **UPI Intent** to Adyen's Payment Simulator; its QR sentence is explicitly **“on web”**, so it does not describe a React Native QR Component flow. The tester chooses an outcome, checks integration handling, then checks webhook and Customer Area record, with modification testing recommended. Its webhook `eventCode` spelling is literally **`AUTHORISED`** in this checklist (raw line 98). The separately retained UPI API-only outcome tables instead say **`AUTHORISATION`** (raw API-only lines 112–117, 216–221, 382–387), while that guide's own TEST checklists repeat `AUTHORISED`. These snapshots conflict; neither checklist establishes the webhook implementation contract. Verify the authoritative webhook schema or live evidence before relying on an event name. See raw lines 81–101.
- Redirecting to a simulator, choosing an outcome or presenting a return URL is not proof of a successful live payment. This guide gives no Collect migration/deprecation date or actual native app-return callback procedure. See raw lines 59–101.

## Detail locators

- **React Native URL versus raw “React Component” title and unsupported Sessions:** raw lines 5–29.
- **Advanced prerequisites, action and anomalous main-guide link:** raw lines 31–47.
- **Intent `appId` TPAP list:** raw lines 49–57.
- **Illustrative TEST `v72` request and return URL:** raw lines 59–79.
- **Simulator, web-only QR mention and checklist event spelling:** raw lines 81–101.

## Related

- [[adyen-online-payments]]
- [[adyen-react-native-sdk]]
- [[adyen-webhooks]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/upi/2026-09-15|UPI overview]] — broader Intent/QR/Collect and dated transition context; separate from this Component page.
- [[raw/adyen/docs/payment-methods/upi/api-only/2026-09-15|UPI API-only]] — separate flow/outcome tables and conflicting event-name spellings.

## Raw Sources

- [[raw/adyen/docs/payment-methods/upi/react-native-component/2026-09-15|UPI React Native Component URL — captured 2026-09-15]]
