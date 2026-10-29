---
title: "Cash App Afterpay Web Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-afterpay/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/cash-app-afterpay/web-drop-in/2026-09-15.md"
tags: [adyen, cash-app-afterpay, web, drop-in, buy-now-pay-later]
---

## Overview

This 2026-09-15 capture of Adyen's Cash App Afterpay guide explains how to add the method to an existing **Web Drop-in** integration. It covers Sessions and Advanced server-side flows, checkout request data, capture and refund behavior, discounts, and testing. The page is a guide for this method and surface, not evidence of current merchant eligibility or a successful live payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Start with an existing Sessions or Advanced Web Drop-in integration and add Cash App Afterpay in Customer Area. The guide says shopper details are used for risk checks and requires purchased-item information in the payment request (raw lines 21–42). The `/sessions` path is described as the default for Drop-in v5.0.0 or later; `/payments` is presented for an additional use case (raw lines 44–50, 745–758).
- Both endpoint tables mark shopperName, shopperEmail, shopperReference (at least three characters), countryCode, billingAddress, deliveryAddress, and lineItems as required; telephoneNumber is listed without a required mark and described as provided if available (raw lines 52–61, 749–758). The US/USD `/payments` example uses `paymentMethod.type: afterpaytouch_US`; preserve that API type without treating it as a different product from the page title (raw lines 760–819).
- There are no Cash App Afterpay-specific Drop-in configuration steps in this guide (raw lines 1215–1217). The examples include a `returnUrl` value of `my-app://adyen`, which is an example value and does not establish a suitable Web return URL for a merchant deployment (raw lines 65–120, 760–820).
- Capture is automatic after authorization or manual according to merchant-account configuration. Delayed capture needs capture-delay setup or manual capture; partial capture needs manual capture. Production authorization must be captured within **13 days**; otherwise Cash App Afterpay cancels and refunds the first installment. Test authorizations expire in **one day** (raw lines 1219–1227).
- For manual capture, amount.value is full or partial and lineItems is optional. A partial capture automatically cancels the unclaimed remainder, except when the account is enabled for multiple partial captures; that capability requires Support setup and makes a new invoice for each capture. Cancel before capture; refund after capture, with full or partial amount and optional lineItems (raw lines 1229–1249).
- The discount section says “1 USD on Item #2,” while its two-unit sample applies a -100 minor-unit discount entry with quantity 2 and totals USD 8.00. This is consistent with USD 1 **per unit** but ambiguous if read as USD 1 for the line; the sample also lacks a comma between the Item #2 and Discount objects. Treat it as illustrative rather than copy-ready JSON (raw lines 1251–1285).

## Detail locators

- Requirements and endpoint fields: raw `## Requirements` lines 21–42 and `## API reference` lines 44–61, 745–758. The `/sessions` curl example is at lines 63–120, and the `/payments` curl example at lines 760–820; other SDK examples are at lines 122–743 and 822–1213.
- Configuration and lifecycle: raw `## Drop-in configuration` lines 1215–1217, `## Capture the payment` lines 1219–1238, and `## Refunds and cancellations` lines 1240–1249.
- Discount example and test/live gates: raw `## Discounts` lines 1251–1285 and `## Test and go live` lines 1287–1305. Testing calls for an Afterpay sandbox shopper account with US selected; live use requires a Cash App Afterpay request in live Customer Area.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-cash-app-afterpay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-afterpay/web-drop-in/2026-09-15|Cash App Afterpay Web Drop-in guide, captured 2026-09-15]]
