# Fixed retrieval checks — docs-payment-methods-zip-android-drop-in

## Q1 — Purpose and version scope

**Query:** What does the Zip Android Drop-in page cover, and which Android version does it target?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-zip-android-drop-in.md` → `raw/adyen/docs/payment-methods/zip/android-drop-in/2026-09-15.md`.

**Answer:** This is a Zip-specific add-on to an existing Android Drop-in integration, for v5.0.0 or later; the page says v5.0.0 was released in October 2023 and directs earlier versions to a separate guide (raw lines 15–21). It does not prove current account enablement or a completed payment. Canonical stem: `https://docs.adyen.com/payment-methods/zip/android-drop-in`.

## Q2 — Sessions/Advanced additions and live gate

**Query:** Does Zip Android Drop-in v5 require extra request fields or configuration, and what are the test/live steps?

**Expected route:** same root → provider → concept → source → pinned raw.

**Answer:** Both Sessions and Advanced require an existing Android Drop-in v5.0.0+ integration and Zip added in Customer Area (23–39). Zip adds no extra fields to the Sessions `/sessions` request or Advanced `/payments` request (41–49), and no extra Drop-in configuration in either flow (51–59). These method-specific statements do not remove base integration requirements. Sessions then creates a checkout session and Advanced launches Drop-in through the linked base routes (61–67). Use Zip test credentials and test Customer Area to check test payments (69–73); submit a separate Zip request in live Customer Area before live acceptance (75). This short page does not itself detail redirect, capture, refunds or recurring behavior. Canonical stem: `https://docs.adyen.com/payment-methods/zip/android-drop-in`; pinned raw: `raw/adyen/docs/payment-methods/zip/android-drop-in/2026-09-15.md`.
