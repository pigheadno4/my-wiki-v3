# Fixed retrieval checks — docs-payment-methods-zip-android

## Q1 — Purpose and scope

**Query:** What is the Zip for Android page, and does it establish payment behavior?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-zip-android.md` → `raw/adyen/docs/payment-methods/zip/android/2026-09-15.md`.

**Answer:** It is a chooser for Android Drop-in and Redirect Component method guides (raw lines 15–27). It does not itself establish request fields, eligibility, capture, recurring behavior or successful payment. Canonical stem: `https://docs.adyen.com/payment-methods/zip/android`.

## Q2 — Child and base routes

**Query:** Where should an Android developer go for Zip Drop-in or Redirect Component, and what base routes are linked?

**Expected route:** same root → provider → concept → source → pinned raw.

**Answer:** The Drop-in option links /payment-methods/zip/android-drop-in and is described as all-in-one UI (21–23). The Components option links /payment-methods/zip/android-component and is described as Redirect Component (25–27). The page also links base Android Drop-in and Components Sessions-flow guides (29); consult child method guides for version and flow-specific behavior. Canonical stem: `https://docs.adyen.com/payment-methods/zip/android`; pinned raw: `raw/adyen/docs/payment-methods/zip/android/2026-09-15.md`.
