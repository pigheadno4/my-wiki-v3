# Zip Android Redirect Component earlier versions worker retrieval queries

## Q1 — Purpose, version and scope

**Query:** What is this Zip Android Component guide, and how should its v4 title be read alongside the Sessions tab?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-zip-android-component-earlier-versions.md` → `raw/adyen/docs/payment-methods/zip/android-component/earlier-versions/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/zip/android-component/earlier-versions`; full pinned raw `raw/adyen/docs/payment-methods/zip/android-component/earlier-versions/2026-09-15.md`, `# Zip Redirect Component v4.x.x integration` lines 15–33, `## Show Zip in your payment form` lines 35–45 and `### Tab: /sessions` lines 58–60. The title is v4.x.x, but the body calls Sessions default for Components v5.0.0+; do not combine them into one exact-version implementation. The snapshot does not prove current merchant enablement or successful payment.

## Q2 — Central flow, qualifications and warnings

**Query:** How does the guide describe AU/AUD Zip discovery, redirect/return finality, and recurring token creation?

**Expected route:** Same root → Adyen index → online-payments concept → Zip earlier-version source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path: `## Show Zip in your payment form` lines 35–43, `## Make a payment` lines 47–60, `### Tab: /payments` lines 707–740, `## Handle the redirect` lines 1419–1450, `## Present the payment result` lines 1452–1472, `## Recurring payments` lines 1474–1507 and `## Test and go live` lines 1707–1713. Preserve AU/AUD discovery, `zip` and Component return URL, optional pickup field, redirect action and server-side details call. `Pending`/`Received` need AUTHORISATION webhook finality; nonreturning shoppers use webhooks. Token creation requires initial payment settlement and a recurring.token.created webhook; future requests use stored ID plus shopper reference and recurring fields. The Advanced curl example includes literal hint markup, so is not copy-ready. The blank Required cells do not independently make every shopper field mandatory.
