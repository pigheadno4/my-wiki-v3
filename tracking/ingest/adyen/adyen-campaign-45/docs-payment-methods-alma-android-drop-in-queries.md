# Alma Android Drop-in retrieval checks

## Q1 — Purpose, scope and what not to infer

**Canonical source stem:** `source-adyen-docs-payment-methods-alma-android-drop-in`
**Full pinned raw:** `raw/adyen/docs/payment-methods/alma/android-drop-in/2026-09-15.md`
**Verified locators:** `# Alma Android Drop-in`, lines 15–23; `## Sessions flow Drop-in`, line 25; `## Advanced flow Drop-in`, line 99; redirect example lines 169–183.
**Route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-alma-android-drop-in.md` → pinned raw.
**Answer boundary:** This is an Android Drop-in method add-on. FR/EUR TEST request and redirect examples do not prove current account enablement, completed app return or final payment success.

## Q2 — Central capability, prerequisites and warnings

**Verified locators:** Sessions requirements and optional fields lines 29–47; app-scheme return placeholder line 63; Advanced requirements and optional installment count lines 101–127; HTTPS return example line 143; redirect response lines 169–183.
**Answer boundary:** Start with matching Android Drop-in Sessions/Advanced flow and Alma in Customer Area; Sessions specifies Checkout API v68+. The method tables leave phone, email and addresses unmarked as required. Advanced optional installment count may be 3/4 or omitted for shopper choice. No extra Alma configuration is stated. Sessions uses `adyencheckout://your.package.name` while Advanced uses HTTPS without a completed return shown. Both curl samples split `-X POST` and `-d` without continuation (lines 51–57, 131–137), so they are not verified copy-ready. Live use requires a Customer Area request.
