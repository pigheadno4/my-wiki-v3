---
title: "Adyen UPI Android Drop-in integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/upi/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/upi/android-drop-in/2026-09-15.md"
tags: [adyen, upi, android, drop-in, intent]
---

## Overview

This [[adyen]] guide adds UPI to an existing **Android Drop-in** integration under **Sessions** or **Advanced** server-side flows. It states an optional submit-button setting, a conditional Advanced **Intent app ID** and TEST simulator checks. The QR simulator step in this Android page is explicitly marked **“on web”**; the page does not establish an Android QR scan implementation, UPI Collect migration rule or LIVE onboarding procedure. A simulator selection or client action is not proof of final authorization, capture or settlement. [[adyen-online-payments]]

## Key takeaways

- **Sessions:** The page requires existing Android Drop-in Sessions with **Checkout API v68 or later** and UPI added in Customer Area. It says no extra UPI parameters for the base `/sessions` request. The UPI configuration table lists `setSubmitButtonVisible` with no required mark to control button display. The base Sessions request still applies; no separate action-handling prerequisite is stated in this table. See raw lines 23–60.
- **Advanced:** The page requires existing Android Drop-in Advanced, handling an additional `action.type: await` action and UPI in Customer Area. It lists the same optional submit-button setting. For a `/payments` request using `paymentMethod.type: upi_intent`, the table requires `paymentMethod.appId` identifying the shopper's TPAP; the listed app IDs and TEST v72 `gpay`/INR example are flow-specific. The v72 sample is not stated as a general Advanced minimum, and Intent's app ID should not be applied to QR. The await-action link itself ends in a `#handle-the-redirect` anchor, so follow the action type text and applicable base guide rather than treating the anchor as an action-type synonym. See raw lines 86–148.
- **Snippet limit:** Both Kotlin configuration snippets contain an extra bare opening brace before `setSubmitButtonVisible(value)`. They are illustrative and need SDK/version verification before reuse; the page does not state a mandatory UPI configuration object. See raw lines 44–60 and 100–116.
- **TEST simulator and outcome check:** The page says UPI Intent redirects to an Adyen-hosted simulator; it separately says UPI QR **“on web”** uses a scanned QR to reach the simulator. Testers select an outcome and validate handling and Customer Area listing. The generic webhook step prescribes `eventCode: AUTHORISED` for the selected outcome, which does not explain non-authorized selections. Do not infer that every simulator result produces AUTHORISED or that a listed transaction proves a final successful payment. Testing payment modifications is recommended afterward. See raw lines 62–84 and 150–170.
- **Scope:** The substantive page does not give a Collect migration cutoff/date, UPI AutoPay mandate flow or a separate live enablement checklist despite its “Test and go live” headings. See raw lines 15–170.

## Detail locators

- Sessions requirements, base request and optional configuration: raw lines 23–60.
- Advanced await action, conditional Intent app ID and sample: raw lines 86–148.
- Duplicated TEST simulator and webhook-check wording: raw lines 62–84 and 150–170.

## Related

- [[adyen-online-payments]]
- [[adyen-android-sdk]]
- [[source-adyen-docs-payment-methods-upi]]
- [[source-adyen-docs-payment-methods-upi-api-only]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/upi/android-drop-in/2026-09-15|Adyen UPI Android Drop-in guide]]
