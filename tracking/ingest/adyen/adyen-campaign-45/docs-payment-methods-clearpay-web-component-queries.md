# Clearpay Web Component retrieval checks

## Q1 — Purpose, scope and what not to infer

**Canonical source stem:** `source-adyen-docs-payment-methods-clearpay-web-component`
**Full pinned raw:** `raw/adyen/docs/payment-methods/clearpay/web-component/2026-09-15.md`
**Verified locators:** `# Clearpay Web Component`, lines 15–23; `## Sessions flow Component`, line 25; `## Advanced flow Component`, line 233; `## Capture the payment`, lines 148–167 and 366–385.
**Route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-clearpay-web-component.md` → pinned raw.
**Answer boundary:** This is a Clearpay add-on for existing Web Components Sessions or Advanced integration. GB/GBP TEST examples, redirect response and sandbox setup do not prove broader market coverage, live account eligibility or completed payment.

## Q2 — Central capability, prerequisites and warnings

**Verified locators:** Sessions prerequisites/fields lines 29–53; Redirect import/init lines 118–144; Advanced prerequisites/fields lines 235–282; redirect response lines 348–362; capture/refund lines 366–396; live request line 449.
**Answer boundary:** Add Clearpay in Customer Area, use an existing Web Components server flow with redirect handling, supply required shopper and order fields, and mount the Redirect Component. No extra method configuration is stated. The example `{ type:clearpay }` (lines 143, 264) is not a verified runnable JS literal. Sessions and Advanced curl examples split `-X POST` and `-d` without a shell continuation (lines 57–63, 286–292), so they are not verified copy-ready. Capture within 13 days (one day in TEST); partial capture requires manual capture and normally cancels the remainder unless multiple partial capture is enabled through Support. Cancel before capture; refund after capture. Discount prose says GBP 1 but quantity 2 at -100 minor units gives GBP 2 and changes total 1000 to 800; examples also contain an ellipsis and omit a comma between line items (lines 182–212, 400–430). Do not treat them as validated requests. The Advanced response shows redirect action, not final result.
