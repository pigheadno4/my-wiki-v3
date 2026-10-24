---
title: "Adyen UPI Flutter Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/upi/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/upi/flutter-drop-in/2026-09-15.md"
tags: [adyen, upi, flutter, drop-in, india]
---

## Overview

This 2026-09-15 UPI guide gives **method-specific additions** to existing Flutter Drop-in integrations in Sessions and Advanced server flows. It says to add UPI in Adyen Customer Area and leaves base server/action/webhook integration to the main flow. Its TEST simulator instructions and sample request do not establish live method eligibility, successful authorization, capture or settlement. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** the page states an existing Flutter Drop-in Sessions integration with Checkout API **v68 or later**, and no extra UPI-specific `/sessions` request or client configuration parameters. Its 'Sessions flow' integration-type link mistakenly points to an **Advanced-flow** URL; its create-session link points to Sessions. Use the flow-specific prose and validate the linked main guide rather than switching integration type from that one URL.
- **Advanced:** the page states an existing Flutter Drop-in Advanced integration, UPI added in Customer Area, and handling of additional `action.type: await`. The action-handling link uses a `#handle-the-redirect` anchor, which is a link-label mismatch rather than proof that every UPI action is a redirect. It says no extra UPI client configuration. For UPI Intent, `paymentMethod.appId` is required in `/payments` and identifies a third-party UPI app; the sample TEST **v72** request uses `upi_intent`, `gpay`, country IN, currency INR and a return URL. This page does not give a complete QR or Collect request procedure.
- **TEST:** both branches point to Adyen's Payment Simulator. Their checklist says Intent redirects to a simulator page and **UPI QR (on web)** scans a QR code to reach it; the QR wording is explicitly web-scoped and does not establish a Flutter QR display implementation. The shopper/operator chooses an outcome to test and checks webhook-server receipt plus a Customer Area Payment-list entry. These are validation instructions, not evidence that a payment was run or reached a final state.
- The repeated simulator checklist spells webhook `eventCode` **AUTHORISED**, while the separately captured [[source-adyen-docs-payment-methods-upi-api-only]] identifies final one-off UPI webhook as **AUTHORISATION**. Keep that source mismatch visible; do not build result parsing from the checklist alone. This page gives no observed final webhook, no current LIVE onboarding/availability detail and no payment modification outcome; testing modifications is only a recommendation.

## Detail locators

- Method add-on scope, Sessions prerequisites and v68 gate: raw lines 19–35. Sessions URL mismatch and no method-specific `/sessions`/configuration fields: raw lines 33–47.
- Sessions simulator Intent/QR instructions and `AUTHORISED` checklist: raw lines 49–69. Advanced existing-flow/`await` prerequisite and redirect-anchor link: raw lines 71–81. Intent `appId` conditional requirement, allowed IDs and TEST v72 example: raw lines 89–119. Advanced simulator/checklist repetition: raw lines 121–141.

## Related

- [[adyen-online-payments]] — parent server-flow and outcome context.
- [[source-adyen-docs-payment-methods-upi-api-only]] — separately captured one-off UPI Intent, QR and Collect guide; it uses AUTHORISATION in payment-result sections, unlike this page's simulator checklist.

## Raw Sources

- [[raw/adyen/docs/payment-methods/upi/flutter-drop-in/2026-09-15|UPI Flutter Drop-in guide, captured 2026-09-15]]
