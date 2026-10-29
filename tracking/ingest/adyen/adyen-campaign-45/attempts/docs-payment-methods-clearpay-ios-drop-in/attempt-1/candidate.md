---
title: "Clearpay iOS Drop-in | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/clearpay/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/clearpay/ios-drop-in/2026-09-15.md"
tags: [adyen, clearpay, ios, drop-in, redirect, capture]
---

## Overview

This 2026-09-15-captured [[adyen]] guide adds **Clearpay** to an existing **iOS Drop-in** integration, with distinct Sessions and Advanced server-flow sections. It describes method-specific additions, not a complete base integration or proof of merchant enablement. The linked [[source-adyen-docs-payment-methods-clearpay]] overview scopes Clearpay to GB/GBP and distinguishes regional Afterpay products; the guide's GB/GBP TEST examples do not establish a particular merchant's current eligibility. See [[adyen-online-payments]].

## Key takeaways

- **Sessions prerequisites and fields:** The Sessions section requires an existing iOS Drop-in Sessions flow, Checkout API **v68 or later**, and Clearpay added in Customer Area (raw lines 25–34). Its `/sessions` table marks `shopperName`, `shopperEmail`, `shopperReference` (minimum three characters), `countryCode`, `billingAddress`, `deliveryAddress` and `lineItems` required; `telephoneNumber` is optional if provided (raw lines 36–51). The GB/GBP TEST `/v71/sessions` example has `-X POST` and `-d` on separate shell lines without continuation, so it is not a copyable verified command (raw lines 53–112).
- **Advanced prerequisites and fields:** The Advanced section requires an existing iOS Drop-in Advanced flow, **redirect handling** for `action.type: redirect`, and Clearpay added in Customer Area (raw lines 213–223). Its `/payments` table repeats the required shopper, country, address and item fields with optional telephone; the TEST example supplies `paymentMethod.type: clearpay` and GB/GBP (raw lines 231–310). Its curl command has the same missing continuation between `-X POST` and `-d` (raw lines 250–256). The example response is `RedirectShopper` with `action.type: redirect`, which is a redirect step rather than final authorisation or capture (raw lines 312–326).
- **Drop-in configuration:** Both flow sections say no additional Clearpay-specific configuration parameters are needed (raw lines 114–118, 225–229). This does not replace the base integration or Advanced redirect handling.
- **Capture and first installment:** Depending on merchant-account configuration, capture is automatic after authorisation or manual. Capture delay or manual capture is needed to capture after goods are sent, and **manual capture is required for partial capture**. The page states capture within **13 days** after authorisation; the first installment is charged during authorisation, and if uncaptured by that deadline Clearpay cancels and refunds it. TEST authorisations expire in **one day**, so manual test capture must occur in that day (raw lines 120–130, 328–338).
- **Partial capture and refund:** Manual `/payments/{paymentPspReference}/captures` specifies full or partial `amount.value` and optional `lineItems`. An initial partial capture normally cancels unclaimed balance; an account enabled for **multiple partial captures** retains it. The latter requires contacting Support and makes a new invoice per capture (raw lines 132–141, 340–349). An uncaptured payment may be cancelled; a captured payment needs refund to return funds. Full/partial `/payments/{paymentPspReference}/refunds` specifies `amount.value` and optionally `lineItems` (raw lines 143–154, 351–362).
- **Discount example warning:** The page says discount line items should have negative amounts and shows a GBP 1 discount on Item #2. The displayed JSON lacks a comma between the second item and the discount item (and uses an ellipsis), so it is illustrative rather than runnable JSON (raw lines 156–192, 364–400).
- **Test and live gate:** Testing calls for Clearpay sandbox and a test shopper account, with country/region-specific sandbox details; the page says the sandbox shows Adyen as merchant name (raw lines 194–209, 402–417). Before live acceptance it says to submit a Clearpay request in live Customer Area (raw lines 211, 419). Submission, sandbox status lookup and examples do not prove live approval or a completed payment.

## Detail locators

- Sessions requirements, field table, TEST example and no-extra-config statement: pinned raw lines 25–118.
- Sessions capture, partial-capture Support gate, refund, discount and test/live sections: pinned raw lines 120–211.
- Advanced requirements, no-extra-config statement, field table and redirect example: pinned raw lines 213–326.
- Advanced capture, partial-capture Support gate, refund, discount and test/live sections: pinned raw lines 328–419.

## Related

- [[adyen-online-payments]] — provider online checkout context.
- [[source-adyen-docs-payment-methods-clearpay]] — GB/GBP product and regional-brand scope.

## Raw Sources

- [[raw/adyen/docs/payment-methods/clearpay/ios-drop-in/2026-09-15|Clearpay iOS Drop-in guide, captured 2026-09-15]]
