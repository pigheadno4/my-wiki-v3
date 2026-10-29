# Walley Android Drop-in earlier versions worker retrieval queries

## Q1 — Purpose, version and regional scope

**Query:** What does the Walley Android Drop-in earlier-version page cover, and how should its v4.x.x title be read with the all-version requirement?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-walley-android-drop-in-earlier-versions.md` → `raw/adyen/docs/payment-methods/walley/android-drop-in/earlier-versions/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/walley/android-drop-in/earlier-versions`; full pinned raw `raw/adyen/docs/payment-methods/walley/android-drop-in/earlier-versions/2026-09-15.md`, title/requirements lines 15–28 and `## Show Walley in your payment form` lines 30–43. Preserve DK/DKK, FI/EUR, NO/NOK, SE/SEK, walley B2C versus walley_b2b B2B, and Denmark/DKK B2C-only. The v4.x.x title and “all versions” statement coexist; neither proves exact-version compatibility or merchant live eligibility.

## Q2 — Redirect, outcome and example warnings

**Query:** How does Android Drop-in pass Walley payment data to the server, return from redirect, and resolve pending results?

**Expected route:** Same root → Adyen index → online-payments concept → Walley earlier-version source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path: `## Make a payment` lines 49–58, `### API response` lines 340–358, `## Check the payment result` lines 360–393, `## Show the payment result` lines 395–414 and `## Test and go live` lines 416–429. Preserve client `paymentComponentData.paymentMethod`, server `/payments`, redirect action, `RedirectComponent.getReturnUrl(context)` 1024-character limit, app-return `actionComponentData.details` to server `/payments/details`, and AUTHORISATION webhook finality for Pending/Received and nonreturning shoppers. Manual capture remains conditional. The `/payments` examples use NO/EUR (lines 69–76) although discovery lists NO/NOK (line 40); do not copy that regional pair. Example order-line values do not visibly reconcile to amount 1000 (lines 69–99).
