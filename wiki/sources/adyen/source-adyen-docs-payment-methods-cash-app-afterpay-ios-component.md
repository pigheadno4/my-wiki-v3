---
title: "Adyen Cash App Afterpay iOS Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-afterpay/ios-component"
raw_files:
  - "adyen/docs/payment-methods/cash-app-afterpay/ios-component/2026-09-15.md"
tags: [adyen, cash-app-afterpay, ios, components, redirect, united-states]
---

## Overview

This captured guide adds Cash App Afterpay to an existing iOS Components integration. Its title and description call it an “Afterpay Redirect Component,” while the body scopes the method to Cash App Afterpay and uses `afterpaytouch_US` in the US/USD examples. It covers Sessions and Advanced server flows, iOS Component setup, capture timing, refunds, discounts and test/live setup. These examples do not prove current eligibility or a successful live payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- Build a matching iOS Components Sessions or Advanced flow and add Cash App Afterpay in Customer Area. The `/sessions` tab is the default with Components v5.0.0 or later; the `/payments` tab is for an additional use case. Both endpoint tables mark shopper name, email, shopper reference, country code, billing and delivery addresses, and `lineItems` required; telephone is optional if provided. `shopperReference` has a minimum length of three characters.
- **Example conflict:** the US/USD request examples use empty shopper first/last names and an empty `shopperReference`, despite the required-field tables and the three-character minimum. Do not copy those as valid values. The Advanced `/payments` examples specify `paymentMethod.type=afterpaytouch_US`; the Sessions example uses `my-app://adyen` as a return URL, which is an example app scheme rather than a configured universal callback.
- **Component version split:** iOS Components v5.0.0+ checks for `.other("afterpaytouch_US")`, creates an `InstantPaymentComponent`, and delegates to the session in Sessions flow or to `self` in Advanced flow before `initiatePayment()`. The earlier v4.x.x snippet uses `AfterpayPaymentMethod` and `AfterpayComponent`. The page says there are no additional method-specific Component configuration steps. The return/redirect must be handled by the selected base integration; presenting a Component does not establish payment finality.
- Capture may be automatic or manual according to merchant account configuration. A shipment-based delay requires capture-delay setup or manual capture; partial capture requires manual capture. The stated capture deadline is **13 days after authorization**; otherwise Cash App Afterpay cancels and refunds the first installment charged at authorization. **Test authorizations expire in one day**, so manual test capture must occur within one day. A manual capture request specifies `amount.value`; `lineItems` is optional. One partial capture automatically cancels the unclaimed amount unless the account is enabled for multiple partial captures. Multiple partial captures require Support setup and create a separate invoice per capture.
- Uncaptured payments can be cancelled; captured ones require refund to return funds. Full/partial refund specifies `amount.value`, with optional `lineItems`. For discounts, the page instructs adding a negative line amount. Its example can be read as USD 1 off each of two Item #2 units (400 + 2×300 − 2×100 = 800 minor units), matching the stated total; the snippet also contains ellipsis and a missing comma before the discount object, so it is not ready-to-send JSON.
- Testing uses a US Afterpay sandbox shopper account and test card; live acceptance requires a Cash App Afterpay request in the live Customer Area. The related method overview limits this regional product to US/USD and describes a four-installment redirect path; it does not make this child guide applicable to AU/NZ Afterpay or UK Clearpay.

## Detail locators

- Raw `# Afterpay Redirect Component`, lines 15–45: identity, integration prerequisites and Sessions default. Raw `## API reference`, lines 47–56 and 740–753: required/optional fields and shopper-reference minimum; raw request examples lines 64–80, 762–779 show empty values and `afterpaytouch_US`.
- Raw `## Component configuration`, lines 1210–1265: v5+ Sessions/Advanced delegates, v4 Component and no added configuration.
- Raw `## Capture the payment`, lines 1267–1286: merchant capture configuration, 13-day and one-day test windows, partial-capture balance and Support gate. Raw `## Refunds and cancellations`, lines 1288–1297: cancel/refund and optional item data.
- Raw `## Discounts`, lines 1299–1333: negative line, example interpretation and syntax warning. Raw `## Test and go live`, lines 1335–1353: sandbox and live setup.

## Related

- [[source-adyen-docs-payment-methods-cash-app-afterpay]] — US/USD product overview and regional naming
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-afterpay/ios-component/2026-09-15|Cash App Afterpay iOS Component guide, captured 2026-09-15]]
