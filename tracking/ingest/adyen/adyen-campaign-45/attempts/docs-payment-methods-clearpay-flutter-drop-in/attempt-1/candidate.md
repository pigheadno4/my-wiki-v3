---
title: "Adyen Clearpay Flutter Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/clearpay/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/clearpay/flutter-drop-in/2026-09-15.md"
tags: [adyen, clearpay, flutter, drop-in, buy-now-pay-later, online-payments]
---

## Overview

This captured [[adyen]] guide adds Clearpay to an **existing Flutter Drop-in** integration, with separate Sessions and Advanced server-side flow instructions. It covers shopper and order request data, redirect handling, capture, refund/cancel, discounts, and test/live setup. The GBP/GB requests are examples, not a live merchant-eligibility claim. [[adyen-online-payments]]

## Key takeaways

- **Prerequisites and source link mismatch:** Sessions calls for an existing Flutter Drop-in Sessions flow, Checkout API v68 or later, redirect handling for `action.type: redirect`, and contacting Support to add Clearpay in Customer Area. Its link labelled “Sessions flow Flutter Drop-in integration” points to an `advanced-flow` URL, while the redirect and session-creation links point to `sessions-flow`. Advanced calls for an existing Flutter Drop-in Advanced flow and redirect handling, and says to add Clearpay in Customer Area. Do not treat the Sessions prerequisite link target as changing the required flow (raw lines 25–42, 209–231).
- **Request data and configuration:** Both `/sessions` and `/payments` tables mark `shopperName`, `shopperEmail`, `shopperReference` (minimum three characters), `countryCode`, `billingAddress`, `deliveryAddress` and `lineItems` required, and list `telephoneNumber` if provided. Both say no extra Clearpay Drop-in configuration parameters are needed. The Advanced table does **not** have a `paymentMethod` row, but its `/payments` example includes `paymentMethod.type: clearpay`; use this as a sample/table discrepancy rather than silently treating the sample as a new table requirement (raw lines 40–53, 116–120, 221–255).
- **Redirect and result boundary:** The Advanced example response shows `resultCode: RedirectShopper` with `action.type: redirect`, an intermediate shopper action, not a completed authorization, capture, refund or settlement (raw lines 308–322).
- **Capture and partial capture:** Account configuration determines automatic versus manual capture; partial capture requires manual capture. Clearpay must be captured within 13 days after authorization. The guide says the first installment is charged during authorization, and if uncaptured within 13 days Clearpay cancels the payment and refunds that installment. Test authorizations expire in one day. A partial capture normally cancels the unclaimed remainder, except when the account is enabled for multiple partial captures through Support; that mode creates a new invoice for each capture (raw lines 124–143; repeated at 326–345).
- **Cancel, refund, discount:** Before capture, the guide routes to cancellation; after capture, returning funds routes to refund. Its refund request specifies `amount.value` and may include `lineItems`. For discounts, prose says to include a negative amount added to the original price. The illustrated “1 GBP on Item #2” payload uses a negative line item with `quantity: 2` and `amountIncludingTax: -100`; it also contains `...` and a missing comma between item objects, so it is not copy-ready JSON and does not independently establish discount arithmetic (raw lines 145–190; repeated at 349–396).
- **Environment gates:** Testing requires the Clearpay sandbox and a test shopper account; the page says sandbox environment and test details vary by country/region, and that the sandbox shows Adyen as merchant name. It instructs a Clearpay request in live Customer Area before live acceptance (raw lines 192–207; repeated at 398–413).

## Detail locators

- Identity and Sessions requirements/request table: pinned raw lines 15–53.
- Sessions request example, configuration and lifecycle: pinned raw lines 55–207.
- Advanced requirements, request table/example and redirect response: pinned raw lines 209–322.
- Advanced capture, refunds, discount and test/live: pinned raw lines 324–413.

## Related

- [[adyen-online-payments]] — online payment architecture and method routes.
- [[source-adyen-docs-payment-methods-clearpay]] — Clearpay regional/method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/clearpay/flutter-drop-in/2026-09-15|Clearpay Flutter Drop-in, captured 2026-09-15]]
