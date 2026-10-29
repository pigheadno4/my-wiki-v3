# Fixed queries — Walley Android Drop-in

## Q1 — purpose and version scope

**Query:** Which Walley Android integration does the captured page cover, and what must not be inferred?

**Expected answer:** The page at `https://docs.adyen.com/payment-methods/walley/android-drop-in` is a 2026-09-15-captured method add-on expressly for Android Drop-in **v5.0.0**, released October 2023; it points earlier SDK users to a separate earlier-version guide. It discusses existing Sessions/Advanced Drop-in integrations and does not establish current merchant enablement, later-version behavior, or successful payment (full pinned `raw/adyen/docs/payment-methods/walley/android-drop-in/2026-09-15.md`, `# Walley Drop-in integration` lines 15–21 and `## Requirements` lines 23–39). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-walley-android-drop-in.md`.

## Q2 — request/configuration and test distinctions

**Query:** What Walley-specific fields or Drop-in configuration are required for Android v5 Sessions versus Advanced, and which extra fields appear only in test guidance?

**Expected answer:** Both flows need existing Android Drop-in v5.0.0+ setup and Walley added in Customer Area. This child page says no extra Walley fields in Sessions `/sessions` or Advanced `/payments`, and no extra Walley Drop-in configuration in either flow (`raw/adyen/docs/payment-methods/walley/android-drop-in/2026-09-15.md`, `## Requirements` lines 23–39, `## API reference` lines 41–49, `## Drop-in Configuration` lines 51–67). For Walley **test scenarios** through `/payments`, place `CivRegNo` in `socialSecurityNumber`; for a **B2B test transaction**, provide `company.name` and `company.registrationNumber` as illustrated (`## Test and go live` lines 69–82). Do not turn those test fields into unconditional live requirements. The separate Walley overview `wiki/sources/adyen/source-adyen-docs-payment-methods-walley.md` and pinned `raw/adyen/docs/payment-methods/walley/2026-09-15.md` lines 23–32 hold B2C/B2B types and country/currency/capture limits; a generic child “See also” tokenization link does not override its recurring crosses. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-walley-android-drop-in.md`.
