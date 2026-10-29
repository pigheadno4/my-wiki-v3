# Clearpay Web Drop-in retrieval check

- Canonical source stem: `source-adyen-docs-payment-methods-clearpay-web-drop-in`.
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-clearpay-web-drop-in.md` → `raw/adyen/docs/payment-methods/clearpay/web-drop-in/2026-09-15.md`.

## Q1 — Purpose, scope, and inference limit

**Query:** What does this Clearpay Web Drop-in guide add, and do its GB/GBP examples or live request establish enablement?

**Expected:** It adds Clearpay-specific steps to existing Web Drop-in Sessions or Advanced flows. The linked overview scopes Clearpay to GB/GBP and marks recurring unavailable; the guide's TEST examples do not prove merchant eligibility or live success. Sessions requires Checkout API v68+, redirect handling and Customer Area setup; Advanced requires its own base flow and redirect setup. Live acceptance requires submitting a Clearpay request in live Customer Area; submission is not approval evidence. Evidence: raw `# Clearpay Web Drop-in` lines 15–36; Advanced requirements lines 221–231; TEST examples lines 55–77/262–287; live lines 219/433.

## Q2 — Required fields, lifecycle and warnings

**Query:** Which request fields and redirect action matter, and what are the capture, refund and source-example limits?

**Expected:** Both request tables require name, email, shopper reference (minimum three characters), country, billing/delivery addresses and line items; telephone is optional. Advanced example supplies `paymentMethod.type: clearpay`. `RedirectShopper`/`action.type: redirect` is not a final outcome. Capture can be automatic or manual by account configuration; partial capture needs manual capture. Capture deadline is 13 days, first installment is charged at authorisation and refunded on cancellation after noncapture; TEST authorisations expire after one day. Initial partial capture cancels remainder unless multiple partial captures are enabled by Support, with a new invoice per capture. Uncaptured can cancel; captured needs refund, with full/partial `amount.value` and optional `lineItems`. Advanced prerequisite URL has an unresolved platform template; both curl examples lack line continuation between `-X POST` and `-d`; discount prose calls it GBP 1, but the example has quantity 2 at -100 minor units each and changes GBP 10 (1000) to GBP 8 (800), a GBP 2 reduction; its JSON also lacks a comma. Evidence: raw field tables lines 44–53/251–260; response lines 326–340; capture lines 128–149/342–363; refund lines 151–162/365–376; URL line 229; curl lines 57–63/264–270; discounts lines 164–200/378–414.
