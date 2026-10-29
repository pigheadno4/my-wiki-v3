# C45 Clearpay Android Component retrieval queries

Canonical source stem: `source-adyen-docs-payment-methods-clearpay-android-component`

Full pinned raw path: `raw/adyen/docs/payment-methods/clearpay/android-component/2026-09-15.md`

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-clearpay-android-component]]` → `[[raw/adyen/docs/payment-methods/clearpay/android-component/2026-09-15]]`.

## Q1 — purpose and scope

**Query:** What does the Clearpay Android Component guide cover, and what does its GB/GBP example establish?

**Answer path:** Opening lines 15–23 scope the page to Clearpay additions for an existing Android Components integration. Sessions and Advanced each have request, Component, capture, refund, discount and test/live sections. The linked Clearpay overview `raw/adyen/docs/payment-methods/clearpay/2026-09-15.md` lines 23–31 identifies UK branding and GB/GBP in its method matrix. GB/GBP TEST examples here do not establish a specific merchant's live eligibility, successful authorisation, capture, refund or settlement.

## Q2 — central capability, prerequisites and warnings

**Query:** What are the Android Component request and redirect prerequisites, and how do capture, refund and discounts differ?

**Answer path:** Sessions requirements lines 29–36 specify existing Components, Checkout API v68+, redirect handling and Customer Area addition; `/sessions` table lines 40–53 marks shopper/country/address/item fields required, phone optional. Advanced requirements lines 289–295, `/payments` table lines 385–398 and example lines 400–462 use method `clearpay`; redirect response lines 464–478 is initial, not final. Component sections lines 116–198 and 297–381 import `instant` (plus Compose module when used) and use `InstantPaymentComponent` without extra method configuration. Capture sections lines 200–221 and 480–501 state 13-day capture and one-day test expiry, with manual partial capture and remainder cancellation unless multiple partial captures enabled. Refund/cancel sections lines 223–232 and 503–512 distinguish pre-capture cancellation from post-capture refund. Discount sections lines 234–268 and 514–548 say negative amount but show £1 prose versus a two-unit -100 discount and 200-minor-unit order decrease, plus a missing comma; verify before copying. Curl request examples at lines 58–63 and 403–408 also omit a continuation before `-d`. Test/live sections lines 270–285 and 550–565 require sandbox setup and a live Customer Area request.
