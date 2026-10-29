---
title: "Adyen Afterpay Web Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/afterpaytouch/web-component"
raw_files:
  - "adyen/docs/payment-methods/afterpaytouch/web-component/2026-09-15.md"
tags: [adyen, afterpay, afterpaytouch, web-components, online-payments]
---

## Overview

This captured [[adyen]] guide adds the Afterpay `afterpaytouch` redirect method to an **existing Web Components** integration. It splits the additions by Sessions and Advanced server-side flows; its examples do not constitute a complete standalone integration. The guide includes request additions, Component initialization, redirect response, capture deadlines and test/live gates. [[adyen-online-payments]]

## Key takeaways

- **Flow prerequisites:** Sessions requires an existing Web Components Sessions integration, Checkout API v68 or later, redirect handling for `action.type: redirect`, and Afterpay added in Customer Area (raw lines 25–36). Advanced likewise requires an existing Advanced Web Components integration, redirect handling and the Customer Area setup; its requirement table does not repeat the Sessions v68 minimum (raw lines 813–821).
- **Request additions:** Both flow tables mark `shopperName`, `shopperEmail`, `shopperReference` (minimum three characters), `countryCode`, `billingAddress`, `deliveryAddress` and `lineItems` required, while `telephoneNumber` is conditional on being provided. The Advanced `/payments` table additionally requires `paymentMethod` with `afterpaytouch`; Sessions adds the fields to `/sessions` (raw lines 40–53, 849–863). The AU/AUD requests are examples, not a complete regional availability matrix.
- **Component and redirect:** Both flow sections import `Redirect` and say to initialize the Redirect class. The Sessions section says no additional Afterpay configuration parameters are needed; the Advanced section does not make that explicit statement. Advanced shows a response with `resultCode: RedirectShopper` and `action.type: redirect`; this is a redirect instruction, not final payment success (raw lines 739–767, 823–845, 1578–1592). The initialization snippets render `type:afterpaytouch` without quotes, so use the prose and method table as the guide, not those snippets as copy-ready JavaScript.
- **Capture and cancellation:** Capture may be automatic or manual depending on merchant-account configuration. The guide says Afterpay payments must be captured within 13 days of authorization; if uncaptured by then, Afterpay cancels the payment and refunds the shopper's first installment, which it says is charged during authorization. Test authorizations expire in one day. Partial capture requires manual capture; an unclaimed remainder is automatically cancelled unless the account is enabled for multiple partial captures, which requires contacting Support and creates a new invoice per capture (raw lines 771–790; repeated under Advanced at 1594–1613).
- **Test/live gates:** The guide calls for an Afterpay sandbox shopper account and test card; it lists Australia, New Zealand, US and Canada for sandbox-account country selection. This test-account list is not a live merchant-method availability statement. Before accepting live Afterpay payments, the guide instructs a request in live Customer Area (raw lines 792–811 and 1615–1634).

## Detail locators

- Sessions requirements, required request fields and optional telephone: pinned raw lines 25–53; multi-language Sessions request examples: lines 55–737.
- Sessions Redirect import/configuration/initialization: pinned raw lines 739–767.
- Advanced requirements and request-field table: pinned raw lines 813–863; multi-language Advanced payment examples: lines 865–1576.
- Advanced redirect response example: pinned raw lines 1578–1592.
- Capture, partial-capture and test/live boundaries: pinned raw lines 771–811 and 1594–1634.

## Related

- [[adyen-online-payments]] — online payment architecture and source routes.
- [[source-adyen-docs-payment-methods-afterpaytouch]] — regional Afterpay overview and lifecycle directory.

## Raw Sources

- [[raw/adyen/docs/payment-methods/afterpaytouch/web-component/2026-09-15|Afterpay Web Component, captured 2026-09-15]]
