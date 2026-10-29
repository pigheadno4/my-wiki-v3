# Fixed retrieval checks — PaySafeCard API-only

## Q1 — Purpose and evidence boundary

**Query:** What does the captured PaySafeCard API-only guide cover, and what does it establish about merchant eligibility or a completed payment?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paysafecard-api-only.md` → `raw/adyen/docs/payment-methods/paysafecard/api-only/2026-09-15.md`.

**Answer:** It is a Web Advanced-flow API-only add-on covering method discovery, shopperReference, a redirect action and details return, test code and live Support activation. It assumes a base API-only integration and Customer Area setup. The separately listed country and currency codes plus NL/EUR request are documentation examples, not a full combination matrix or proof that a particular merchant is enabled. The child countryCode row says AE, GB, GIB and SRB, while the separately approved overview labels the corresponding country-code entries UAE, UK, GI and RS. The active API/account contract must resolve these tokens; neither captured list proves current validity. An example Authorised response is not evidence of a real payment.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/paysafecard/api-only`; full pinned raw `raw/adyen/docs/payment-methods/paysafecard/api-only/2026-09-15.md`, `# PaySafeCard for API only` lines 15–21, `## Requirements` lines 23–29, `## Get PaySafeCard as an available payment method` lines 44–51 and 329–340, `## Test and go live` lines 625–633. For the token discrepancy, follow the approved `wiki/sources/adyen/source-adyen-docs-payment-methods-paysafecard.md` route to its pinned `raw/adyen/docs/payment-methods/paysafecard/2026-09-15.md` country table, especially lines 51, 76 and 83–84; compare child raw line 50.

## Q2 — Redirect and incomplete request examples

**Query:** Which PaySafeCard request field and redirect/result steps are documented, and why should the captured payment snippets not be copied as complete requests?

**Expected route:** Same root → Adyen index → online-payments concept → PaySafeCard API-only source → pinned child raw; for country-code token interpretation also route through `wiki/sources/adyen/source-adyen-docs-payment-methods-paysafecard.md` → `raw/adyen/docs/payment-methods/paysafecard/2026-09-15.md`.

**Answer:** The method-specific `/payments` table marks shopperReference required. The flow prose calls for item information, but the table and payment examples omit item fields; the request examples also omit paymentMethod although discovery returns paysafecard, and several SDK snippets never construct paymentRequest. The curl samples lack shell continuation after `-X POST`. The /payments example returns RedirectShopper plus a redirect action, which must be followed through action.url. On website return, URL-decode redirectResult and send it in details to `/payments/details`; use the returned resultCode and pspReference. Mobile browser recommendations are scoped to mobile integrations. Live acceptance additionally needs Adyen Support activation. Country-code tokens differ between child raw line 50 (AE/GB/GIB/SRB) and overview raw lines 51, 76, 83–84 (GI/RS/UAE/UK), so do not treat either captured list as an unqualified accepted-value contract.

**Evidence locator:** Same canonical stem and full pinned raw path; `## How it works` lines 31–36, `## Add additional parameters to your /payments request` lines 342–370 and SDK examples through line 566, redirect/details lines 568–623, live gate line 633.
