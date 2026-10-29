# Fixed retrieval queries — Walley for Android

## Q1 — Purpose and evidence boundary

**Query:** What does the captured Walley for Android page provide, and what does it not establish?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-walley-android.md` → `raw/adyen/docs/payment-methods/walley/android/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/walley/android`; full pinned raw `raw/adyen/docs/payment-methods/walley/android/2026-09-15.md`, `# Walley for Android` lines 15–17 and `## How do you want to integrate?` lines 19–29. It is an Android integration chooser, not a complete payment recipe or proof of current Walley enablement, outcome, or live processing.

## Q2 — Method-specific and base routes

**Query:** Which Android UI paths does this Walley chooser link, and where should implementation details be read?

**Expected route:** Same root → Adyen index → online-payments concept → Walley Android chooser source → pinned raw; then the linked Walley Android Drop-in or Components child source for its own separately grounded details.

**Evidence locator:** Same canonical stem and full pinned raw path. The chooser links method-specific Drop-in as an all-in-one UI route at lines 21–23 and method-specific Components as a Redirect Component route at lines 25–27; line 29 links general Android Sessions guides for Drop-in and Components. The chooser supplies no field/version/capture/finality or eligibility rule; consult the relevant child and Walley method overview before making such claims.
