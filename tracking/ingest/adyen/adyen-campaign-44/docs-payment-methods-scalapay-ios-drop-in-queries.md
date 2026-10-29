# Scalapay iOS Drop-in retrieval checks

## Q1 — Purpose, scope and what not to infer

**Canonical source stem:** `source-adyen-docs-payment-methods-scalapay-ios-drop-in`
**Full pinned raw:** `raw/adyen/docs/payment-methods/scalapay/ios-drop-in/2026-09-15.md`
**Verified locators:** `# Scalapay Drop-in integration`, lines 15–19; `## Requirements`, lines 21–39; `## Drop-in configuration`, lines 430–432; `## Test and go live`, lines 434–440.
**Route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-scalapay-ios-drop-in.md` → pinned raw.
**Answer boundary:** This is an iOS Drop-in add-on, not a complete capture/refund or result guide. Its snapshot does not establish present account eligibility or a successful payment. The separate overview holds the captured EUR feature matrix and marks recurring unsupported.

## Q2 — Central capability, prerequisites and warnings

**Verified locators:** Sessions/Advanced requirements and pricing lines 25–39; `/sessions` table lines 45–55; `/payments` table and IT `scalapay_3x` example lines 57–96, including the iOS app-scheme `returnUrl` placeholder `my-app://` at line 94; no extra configuration lines 430–432; test/live lines 434–440.
**Answer boundary:** Start from existing iOS Drop-in flow and add Scalapay in Customer Area; check Enterprise-pricing eligibility with the account manager before activation. Both endpoint tables require country and shopper name, with IT/FR/PT/ES listed; Advanced flight/lodging fields are optional alternatives. The Advanced example uses `my-app://` as an iOS app-scheme return URL placeholder (raw line 94); it does not show a completed redirect-return outcome or establish that the placeholder is a working merchant app URL. The page requires no Scalapay-specific Drop-in configuration. TEST examples and live-request wording do not prove eligibility, capture or settlement; generic tokenization navigation does not establish recurring Scalapay support.
