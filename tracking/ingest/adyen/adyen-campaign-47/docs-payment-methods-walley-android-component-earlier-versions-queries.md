# Fixed retrieval queries — Walley Android Redirect Component earlier versions

## Q1 — Identity, scope, and version boundary

**Query:** What does the captured Walley Android Component earlier-versions page cover, and can its all-versions statement establish current-version behavior?

**Expected:** The page at `https://docs.adyen.com/payment-methods/walley/android-component/earlier-versions` is titled “Walley Redirect Component v4.x.x integration” (raw lines 6, 15). It describes an existing Android Components integration, a Redirect Component and return handling, but its requirements also state Walley works with all Components versions (lines 19–25). Preserve both statements without treating this historical earlier-versions route as verification of a current SDK integration or live payment. Test Customer Area activation requires contacting Support (line 26). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-walley-android-component-earlier-versions.md` → `raw/adyen/docs/payment-methods/walley/android-component/earlier-versions/2026-09-15.md`. Canonical stem: `https://docs.adyen.com/payment-methods/walley/android-component/earlier-versions`.

## Q2 — B2C/B2B redirect and finality

**Query:** How does this guide discover Walley B2C/B2B, send the shopper through redirect, and determine the result?

**Expected:** `/paymentMethods` uses DK/DKK, FI/EUR, NO/NOK or SE/SEK and channel `android`; response types are `walley` B2C and `walley_b2b` B2B, with DK or DKK B2C only (raw lines 28–47). The Component's payment-method data goes to server `/payments`; the return URL comes from `RedirectComponent.getReturnUrl(context)` and has a 1024-character limit. Its prose calls the field `returnURL`, so verify schema with the base guide (51–60). Pass the `RedirectShopper` action to the app; after return, POST `actionComponentData.details` to `/payments/details` (62–111). `Pending`/`Received` are not final; wait for AUTHORISATION webhook, including if shopper fails to return. `Authorised` is sent to bank for processing, with manual capture still needed if configured; AUTHORISATION true/false webhooks distinguish outcomes (113–132). Test `CivRegNo` and B2B company details are scoped to test scenarios (134–147). Route: root → provider → online-payments concept → source → pinned raw above.
