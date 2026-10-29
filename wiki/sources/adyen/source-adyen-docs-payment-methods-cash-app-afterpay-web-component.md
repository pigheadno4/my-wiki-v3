---
title: "Adyen Cash App Afterpay Web Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-afterpay/web-component"
raw_files:
  - "adyen/docs/payment-methods/cash-app-afterpay/web-component/2026-09-15.md"
tags: [adyen, cash-app-afterpay, web, components, capture, refunds, discounts]
---

## Overview

This [[adyen|Adyen]] guide, fetched and marked last modified 2026-09-15, adds **Cash App Afterpay** to an existing **Web Components** integration. It covers Sessions and Advanced request paths, versioned Component mounting, capture and refund lifecycle, discounts, and test/live setup. See [[adyen-online-payments]] and the separate [[source-adyen-docs-payment-methods-cash-app-afterpay|method overview]]. The captured page does not prove live account enablement or a completed payment.

## Key takeaways

- **Integration and fields:** Start with an existing Sessions or Advanced Web Components integration and add Cash App Afterpay in Customer Area. The guide says to collect shopper details for risk checks, provide purchased-item information and use a supported country/currency combination. `/sessions` is default with Components v5.0.0+; `/payments` is shown for an additional use case. Both tables mark shopper full name, email, `shopperReference` of at least three characters, country code, billing and delivery addresses, and line items required; telephone number is optional. The TEST examples use US/USD; the Advanced example uses `paymentMethod.type: afterpaytouch_US`. Treat the examples as region-specific, not a global method list.
- **Component versions:** Mount the Web Component on a checkout DOM element. For Adyen Web v6.0.0+, the example uses `new Afterpay(checkout).mount('#afterpaytouch_US-container')`; for v5.x.x or earlier it uses `checkout.create('afterpaytouch_US').mount(...)`. The request examples and mounting code span different versions and should be matched to the actual SDK/API.
- **Capture and expiry:** Merchant configuration determines whether payments capture automatically after authorization or are manually captured. To capture after shipment, arrange capture delay or manual capture; **partial capture requires manual capture**. Cash App Afterpay must be captured within **13 days** of authorization. The shopper is charged the first installment during authorization; if uncaptured by day 13, Cash App Afterpay cancels the payment and refunds that installment. TEST authorizations expire after **one day**, so manual test captures must occur within one day.
- **Partial capture and refund:** Manual capture specifies full or partial `amount.value`; `lineItems` are optional. Ordinarily, unclaimed amount after partial capture cancels automatically. On accounts enabled for **multiple partial captures**, the remainder stays available; Support must enable this, and every partial capture creates a new invoice. Cancel before capture; refund after capture. Full or partial refund uses `amount.value`, with optional line items.
- **Discount and sample warnings:** The guide describes a negative line item for discounts. Its example has quantity 2 for item #2 and a -100 amount for each of two discount units, yielding the shown 800 total under a per-unit interpretation, but the displayed JSON has an ellipsis and is missing a comma between item objects; use it as an illustration, not copy-ready JSON. The TEST shopper-account procedure uses the Afterpay sandbox and test cards; live acceptance requires a separate Cash App Afterpay request in **live** Customer Area. The separate overview supplies regional naming and method-level capability limits.

## Detail locators

- Purpose, prerequisites and risk-check/country instructions: pinned raw lines 15–43. Sessions v5+ and required/optional table: lines 45–62; TEST v69 US/USD examples: lines 64–744.
- Advanced `/payments` field table and TEST v72 `afterpaytouch_US` examples: lines 746–1214. Web v6/v5 mounting: lines 1216–1246.
- Capture configuration, 13-day and one-day TEST expiry, partial capture/remainder: lines 1248–1267. Cancel/refund: lines 1269–1278. Discount description and malformed example: lines 1280–1314. Sandbox and live setup: lines 1316–1334.

## Related

- [[adyen-online-payments]] — provider integration concept
- [[source-adyen-docs-payment-methods-cash-app-afterpay]] — method overview and regional naming

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-afterpay/web-component/2026-09-15|Cash App Afterpay Web Component guide, fetched 2026-09-15]]
