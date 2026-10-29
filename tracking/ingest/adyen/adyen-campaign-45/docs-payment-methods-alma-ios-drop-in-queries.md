# Alma iOS Drop-in retrieval check

- Canonical source stem: `source-adyen-docs-payment-methods-alma-ios-drop-in`.
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-alma-ios-drop-in.md` → `raw/adyen/docs/payment-methods/alma/ios-drop-in/2026-09-15.md`.

## Q1 — Purpose, scope, and inference limit

**Query:** What does the Alma iOS Drop-in page add, and do its FR/EUR examples prove live merchant eligibility?

**Expected:** It is method-specific guidance for existing iOS Drop-in Sessions or Advanced integrations. The related overview scopes Alma to FR/EUR and three/four installments. Sessions requires Checkout API v68+ and Customer Area setup; Advanced requires its base integration, redirect action handling and Customer Area setup. The TEST examples do not prove current enablement, completed return or payment outcome; live use requires submitting an Alma request in live Customer Area. Evidence: raw `# Alma iOS Drop-in` lines 15–34, `## Advanced flow Drop-in` lines 99–109 and `## Test and go live` lines 91–97/187–193.

## Q2 — Optional fields, redirect, and example warnings

**Query:** Which Alma request fields and installment control are optional, what does the Advanced response mean, and what caveats apply to the examples?

**Expected:** Both method-specific tables leave telephone, shopper email, billing address and delivery address Required cells blank. Advanced adds optional `additionalData.alma.installments_count`, set to 3 or 4 or omitted for shopper choice. No additional method-specific Drop-in configuration is required. The Advanced `RedirectShopper`/`action.type: redirect` response is an intermediate action, not final authorization. Sessions uses an app-scheme return URL placeholder while Advanced uses HTTPS, without explaining actual iOS return handling. Both curl examples put `-X POST` and `-d` on separate lines without continuation, so they are illustrative rather than verified copy-ready commands. The page does not specify capture/refund/final async behavior. Evidence: raw field tables lines 42–47/123–129; configuration lines 85–89/111–115; return URLs lines 63/145; curl lines 51–57/133–139; response lines 171–185.
