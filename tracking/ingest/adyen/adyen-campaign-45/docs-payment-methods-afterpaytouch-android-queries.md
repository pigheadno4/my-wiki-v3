# Afterpay Android chooser worker retrieval queries

## Q1 — Purpose and scope

**Query:** What does the Afterpay for Android page provide, and what must be read for implementation details?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-afterpaytouch-android.md` → `raw/adyen/docs/payment-methods/afterpaytouch/android/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/afterpaytouch/android`; full pinned raw `raw/adyen/docs/payment-methods/afterpaytouch/android/2026-09-15.md`, `# Afterpay for Android` lines 15–27 and `## See also` lines 29–36. This is a chooser linking child and base guides, not a field-level implementation recipe or payment-success proof.

## Q2 — Central route and prerequisites

**Query:** Which Android UI paths and base flows are linked, and what does the Components label actually say?

**Expected route:** Same root → Adyen index → online-payments concept → Afterpay Android chooser source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path; `### How do you want to integrate?` lines 19–27 and `## See also` lines 29–36. The page links Drop-in and Components child guides, names `InstantPaymentComponent` for redirect, and tells readers to build the main integration first using Android Sessions or Advanced guides. It does not itself establish SDK/API versions, request requirements, merchant enablement, capture/refund support or outcome.
