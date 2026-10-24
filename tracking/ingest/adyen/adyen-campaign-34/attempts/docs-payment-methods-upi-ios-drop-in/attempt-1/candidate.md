---
title: "Adyen UPI iOS Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/upi/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/upi/ios-drop-in/2026-09-15.md"
tags: [adyen, upi, ios, drop-in, india]
---

## Overview

This [[adyen]] guide adds UPI-specific steps to an **existing iOS Drop-in** integration in separate Sessions and Advanced flows. Its iOS-specific implementation covers **UPI Intent** app discovery and, for Advanced, an Intent `appId` request field. The test checklist's QR reference is explicitly **on web**; this page does not specify an iOS QR or Collect integration, a Collect migration/deprecation date, an iOS manual-return callback, or an iOS SDK minimum. Those require separate source guides rather than inference here. See [[adyen-online-payments]]. This captured guide and test request do not prove current availability or a successful live payment. See raw lines 15–23, 25–234.

## Sessions flow

- Requires an existing Sessions iOS Drop-in integration, Checkout API **v68 or later**, and UPI added in Customer Area. The guide says there are no UPI-specific extra fields in the base `/sessions` request. See raw lines 25–40.
- For UPI Intent, Smart Intent detects installed UPI apps only if their URL schemes are declared in the merchant iOS app's `Info.plist` `LSApplicationQueriesSchemes`. The guide lists twelve app/scheme pairs as a dated snapshot (for example Google Pay/`tez` and PhonePe/`phonepe`). iOS privacy rules restrict detection to declared schemes, the list is limited to **50** schemes per app, and the Component handles no detected UPI apps. A listed provider or declared scheme is not proof that the app is installed, usable or a payment has completed. See raw lines 42–91.

## Advanced flow

- Requires an existing Advanced iOS Drop-in integration, UPI in Customer Area and handling of the additional `action.type: await`. Its action-handling link's anchor says “handle-the-redirect”; preserve the explicit **await** type and verify the base flow's actual action handling rather than treating the anchor text as another action type. The Advanced table does not repeat the Sessions v68+ requirement. See raw lines 117–127.
- The same Smart Intent scheme declaration and 50-scheme/no-app conditions are repeated for Advanced. See raw lines 129–178.
- For the Advanced **UPI Intent** option (`paymentMethod.type: upi_intent`), `paymentMethod.appId` is required and identifies the shopper's third-party application provider; the table enumerates IDs such as `gpay`, `phonepe` and `wapay` (WhatsApp Pay). The illustrative **test** `/v72/payments` request uses `INR`, country `IN`, `appId: gpay`, and a merchant return URL. The v72 URL is an example endpoint, not an explicit minimum for the entire Advanced integration. A return URL and submitted request are not payment-outcome proof. See raw lines 180–210.

## Test and outcome boundary

- In a **test** integration, UPI Intent redirects to Adyen's Payment Simulator; its UPI QR step says **“on web”** and therefore cannot establish an iOS QR Drop-in procedure. The tester chooses an outcome, checks integration handling, then confirms the matching **`AUTHORISED` webhook** and Customer Area Payments record; the guide also recommends modification tests. Simulator selection, redirection and app return do not by themselves prove authorization or live success. See raw lines 93–115 and 212–234.
- This page contains no QR/Collect iOS steps, Collect cut-off date, production deep-link/manual-return setup, specific iOS SDK version, or live enablement approval process. Follow the linked main flow and separate method sources for those questions. See raw lines 15–234.

## Detail locators

- **Sessions requirements and no-extra-session fields:** raw lines 25–40.
- **Intent provider schemes, privacy and 50-scheme cap:** raw lines 42–91 and 129–178.
- **Advanced `await` action and prerequisite:** raw lines 117–127.
- **Intent `appId` and illustrative test v72 request:** raw lines 180–210.
- **Simulator, web-only QR mention and webhook/status verification:** raw lines 93–115 and 212–234.

## Related

- [[adyen-online-payments]]
- [[adyen-ios-sdk]]
- [[adyen-webhooks]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/upi/2026-09-15|UPI overview]] — broader Intent/QR/Collect and dated migration context; distinct from this iOS Drop-in guide.
- [[raw/adyen/docs/payment-methods/upi/api-only/2026-09-15|UPI API-only]] — separate API/Collect request detail and dated notices.

## Raw Sources

- [[raw/adyen/docs/payment-methods/upi/ios-drop-in/2026-09-15|UPI iOS Drop-in — captured 2026-09-15]]
