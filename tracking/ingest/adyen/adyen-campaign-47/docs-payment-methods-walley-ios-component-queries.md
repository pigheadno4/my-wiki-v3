# Walley iOS Component worker retrieval queries

## Q1 — Purpose and version scope

**Query:** What does the Walley iOS Component guide add, and how do the v5+ and v4.x.x setup paths differ?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-walley-ios-component.md` → `raw/adyen/docs/payment-methods/walley/ios-component/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/walley/ios-component`; full pinned raw `raw/adyen/docs/payment-methods/walley/ios-component/2026-09-15.md`, `# Walley iOS Component` lines 15–26 and `## Component configuration` lines 344–399. The page says all Component versions but gives distinct v5+ InstantPaymentComponent and v4.x.x WalleyComponent examples. It does not prove current merchant enablement or a real payment.

## Q2 — Fields, B2B and sample warnings

**Query:** Which Walley shopper/order fields are required for iOS Sessions and Payments, when is company data required, and are the payment examples copy-ready?

**Expected route:** Same root → Adyen index → online-payments concept → Walley iOS Component source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path: `## API reference` lines 28–62, Payments curl lines 64–100, v5+ Component examples lines 346–381, v4.x.x example lines 383–399, and `## Test and go live` lines 401–414. Preserve working mobile phone with country code, email, line-item details and 50-character description cap. `company.name` is only required for walley_b2b; registration number is B2B-relevant but unmarked. The shown v5+ lookup uses walley B2C, not walley_b2b. Payment examples have empty `paymentMethod.type` (line 78); NO/EUR sample (lines 73–80) conflicts with the related Walley Android discovery table's NO/NOK pairing. No live acceptance or final payment result is shown.
