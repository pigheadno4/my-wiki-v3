# Fixed retrieval queries — Cash App Afterpay Android Drop-in earlier versions

## Q1 — Identity and scope

**Query:** Which Android version and server flow does this Cash App Afterpay guide cover?

**Expected:** The guide at `https://docs.adyen.com/payment-methods/cash-app-afterpay/android-drop-in/earlier-versions` is for Android Drop-in **v4.x.x** and its Requirements row says **Advanced flow**. The introductory and final Android Drop-in links point to Sessions-flow URLs, so the Advanced requirement governs this versioned page. It is US/USD and `afterpaytouch_US`, not AU/NZ Afterpay or UK Clearpay. A captured guide does not prove current merchant entitlement or live success. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-cash-app-afterpay-android-drop-in-earlier-versions.md` → `raw/adyen/docs/payment-methods/cash-app-afterpay/android-drop-in/earlier-versions/2026-09-15.md`. Evidence: raw lines 15–41, 72–88, 681–685; related `wiki/sources/adyen/source-adyen-docs-payment-methods-cash-app-afterpay.md`.

## Q2 — Redirect result and capture

**Query:** What must the merchant do after Drop-in redirects for Cash App Afterpay, and what are the capture and partial-modification limits?

**Expected:** Drop-in returns `paymentComponentData.paymentMethod` for the server `/payments` request with shopper/contact/address/items; telephone optional (raw lines 43–63). The response action redirects; after app return, Drop-in provides `actionComponentData.details` for server `/payments/details`. Pending/Received are not final and require AUTHORISATION webhook; if no app return, rely on webhook success (raw lines 520–591). Capture mode depends on account, partial capture requires manual; 13-day capture deadline, first installment refund on expiry, and one-day test authorization window (raw lines 593–601). Ordinary partial capture cancels unclaimed balance, but multiple-partial-capture-enabled accounts retain it; Support setup required and each capture creates an invoice (raw lines 603–612). Uncaptured cancel, captured refund (raw lines 614–623). Discount example can represent USD 1 per each of two Item #2 units, but the ellipsis/missing comma make it non-executable (raw lines 625–659). Live acceptance needs live Customer Area request (raw line 679). Route: root → provider index → `wiki/concepts/adyen-online-payments.md` → source → pinned raw.
