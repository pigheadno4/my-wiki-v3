# Fixed retrieval checks — docs-payment-methods-atome-web-drop-in

## Q1 — Purpose and scope

**Query:** What does Adyen's Atome Web Drop-in guide cover, and can its redirect example prove a successful payment?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-atome-web-drop-in.md` → `raw/adyen/docs/payment-methods/atome/web-drop-in/2026-09-15.md`.

**Answer:** It is a method-specific add-on to existing Web Drop-in Sessions and Advanced flows, not a full base guide (raw 15–25). Its Advanced response is `RedirectShopper` with a redirect action despite the “successful payment” heading, so it does not establish authorization, capture or settlement (1532–1544). The snapshot cannot prove current account eligibility. Canonical stem: `https://docs.adyen.com/payment-methods/atome/web-drop-in`.

## Q2 — Countries, request fields, refund and test/live constraints

**Query:** Which Atome Web Drop-in flow requirements, country/currency pairs, refund and test/live steps should be retained?

**Expected route:** same root → provider → concept → source → pinned raw.

**Answer:** Sessions requires existing Web Drop-in Sessions, Checkout API v68+, redirect handling and Customer Area enablement (29–36); Advanced requires existing Advanced Drop-in, redirect handling and enablement (780–786). Both require name, email, phone, billing address, line items and countryCode, with delivery address optional when same as billing; use MY/MYR or SG/SGD (44–52, 806–815). Advanced also requires paymentMethod.type atome (808). Both flow sections document partial refund amount via /refunds (744–752, 1546–1554). Testing needs an Atome sandbox shopper account from Adyen, separately by location, with test Customer Area status checks (756–772, 1558–1574); live enablement needs Support (774, 1576). Warn that the Advanced prerequisite URL has an unresolved encoded platform template (784); use the nearby Web-specific redirect/payment links for navigation (785, 803), without assuming the prerequisite URL resolves. Also warn that the Sessions Web sample uses an app-scheme returnUrl (70), Advanced uses HTTPS (836), both curl examples omit a continuation before -d (63–64, 826–827), and the Advanced redirect response is mislabeled successful (1532–1544). Consult the separate method overview for the portable-electronics restriction and automatic-capture note; this add-on does not repeat them. Canonical stem: `https://docs.adyen.com/payment-methods/atome/web-drop-in`; pinned raw: `raw/adyen/docs/payment-methods/atome/web-drop-in/2026-09-15.md`.
