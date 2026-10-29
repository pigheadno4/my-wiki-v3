---
title: "Adyen Afterpay Android Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/afterpaytouch/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/afterpaytouch/android-drop-in/2026-09-15.md"
tags: [adyen, afterpay, afterpaytouch, android, drop-in, online-payments]
---

## Overview

This captured [[adyen]] guide describes adding Afterpay to an **existing Android Drop-in** integration, with separate Sessions and Advanced server-side flow instructions. It covers method-specific request fields, a redirect response for Advanced, capture limits and test/live gates. It is an add-on to the main Android integration guides, not a standalone SDK or payment-outcome proof. [[adyen-online-payments]]

## Key takeaways

- **Prerequisites by flow:** The Sessions section requires an existing Android Drop-in Sessions integration using Checkout API v68 or later and adding Afterpay in Customer Area. The Advanced section requires an existing Android Drop-in Advanced integration, redirect handling for `action.type: redirect`, and adding Afterpay in Customer Area; its requirements table does not repeat the Sessions API minimum (raw lines 25–34, 787–795).
- **Request fields and configuration:** In both `/sessions` and `/payments` tables, the page marks `shopperName`, `shopperEmail`, `shopperReference` (minimum three characters), `countryCode`, `billingAddress`, `deliveryAddress` and `lineItems` required; `telephoneNumber` is included if provided. The Advanced `/payments` table also requires `paymentMethod: afterpaytouch`. Both sections say no additional Afterpay Drop-in configuration parameters are needed (raw lines 38–51, 737–741, 797–822). The AU/AUD sample payloads illustrate a request and do not establish a region-wide eligibility rule.
- **Redirect boundary:** The Advanced sample response has `resultCode: RedirectShopper` and `action.type: redirect`. This describes the next shopper action, not final authorization, capture or settlement. For the return and result flow, follow the linked main Android integration guide (raw lines 789–795, 1534–1548).
- **Capture deadlines and effect:** Depending on merchant account configuration, capture is automatic after authorization or manual. The guide says Afterpay payments must be captured within 13 days of authorization; during authorization the shopper is charged the first installment, and if payment is not captured within 13 days, Afterpay cancels it and refunds that installment. Test authorizations expire in one day, so manual test capture must happen within one day (raw lines 745–753; repeated at 1550–1558).
- **Partial capture:** Partial capture requires manual capture. The capture request specifies `amount.value` and may include `lineItems`; the remaining unclaimed amount is automatically cancelled after a partial capture unless the account is enabled for multiple partial captures. The guide says to contact Support for that setup, which creates a new invoice for each capture (raw lines 755–764; repeated at 1560–1569).
- **Test/live gate:** Testing calls for an Afterpay sandbox shopper account and test card. The sandbox country selector lists Australia, New Zealand, US and Canada; this list is a test-account instruction, not a live acceptance matrix. The guide says to request Afterpay in live Customer Area before accepting live payments (raw lines 766–785; repeated at 1571–1590).

## Detail locators

- Guide identity and add-on scope: pinned raw lines 15–23.
- Sessions requirements, request table and multi-language examples: pinned raw lines 25–735.
- Sessions no-extra-configuration, capture and test/live sections: pinned raw lines 737–785.
- Advanced requirements, no-extra-configuration, request table and multi-language examples: pinned raw lines 787–1532.
- Advanced redirect response, capture and test/live sections: pinned raw lines 1534–1590.

## Related

- [[adyen-online-payments]] — provider online payment architecture and source routes.
- [[source-adyen-docs-payment-methods-afterpaytouch]] — Afterpay regional/product overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/afterpaytouch/android-drop-in/2026-09-15|Afterpay Android Drop-in, captured 2026-09-15]]
