# Scalapay iOS Component retrieval checks

## Q1 — Purpose, scope and what not to infer

**Canonical source stem:** `source-adyen-docs-payment-methods-scalapay-ios-component`
**Full pinned raw:** `raw/adyen/docs/payment-methods/scalapay/ios-component/2026-09-15.md`
**Verified locators:** `# Scalapay Redirect Component`, lines 15–19; `## Requirements`, lines 21–39; `## Component configuration`, lines 430–485; `## Test and go live`, lines 487–493.
**Route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-scalapay-ios-component.md` → pinned raw.
**Answer boundary:** This is an iOS Components add-on, not a complete capture/refund or result guide. Its snapshot does not establish present account eligibility, completed payment or settlement; the separate overview holds the captured EUR feature matrix.

## Q2 — Central capability, prerequisites and warnings

**Verified locators:** Sessions/Advanced requirements and pricing lines 25–39; `/sessions` field table lines 45–55; `/payments` table and IT `scalapay_3x` example lines 57–96; versioned component setup lines 430–485; live request lines 487–493.
**Answer boundary:** Start from existing Components flow and add Scalapay in Customer Area; check account-manager pricing eligibility before activation. Required country and shopper name are in both tables; listed countries are IT/FR/PT/ES. Advanced flight/lodging fields are optional alternative scenario data. v5+ uses `InstantPaymentComponent`; v4 uses `ScalapayComponent`. The requirement links contain unresolved encoded platform templates, so use the explicit iOS integration route in See also. TEST examples and live-request wording do not prove eligibility or payment success.
