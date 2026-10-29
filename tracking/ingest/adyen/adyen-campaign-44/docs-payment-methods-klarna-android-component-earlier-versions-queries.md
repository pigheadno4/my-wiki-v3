# C44 worker query check: Klarna Android Component earlier versions

## Q1 — purpose, scope, non-inference

**Query:** Which Android Klarna guide is this and what does it establish?

**Answer:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-klarna-android-component-earlier-versions]] routes to a 2026-09-15 captured guide for v4.x.x Android Redirect Component with Advanced flow. It does not prove current merchant method availability or live payment success. The pinned full raw is `raw/adyen/docs/payment-methods/klarna/android-component/earlier-versions/2026-09-15.md`. Verified locators: raw 15–32 (identity and requirement), 46–79 (discovery), 1622–1649 (test/live).

## Q2 — flow, prerequisites, warnings

**Query:** How does the v4.x.x Android Klarna payment progress and what must be checked?

**Answer:** Merchant adds Klarna in Customer Area, uses supported country/currency and product type, sends shopper details and line items through server /payments, passes redirect action to Android, then posts returned component details to /payments/details. An Authorised result still needs capture under the guide's 24-hour shipping or 90-day manual-capture rule; a received capture request awaits CAPTURE webhook. Legacy /capture shipping/partial examples differ from the main Checkout /captures path. The redirect and See also anchors point to Sessions despite the Advanced prerequisite. Verified locators: raw 81–142, 866–933, 935–947, 1393–1426, 1428–1506, 1653.
