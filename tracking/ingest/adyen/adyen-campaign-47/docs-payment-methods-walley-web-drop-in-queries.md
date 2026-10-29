# Walley Web Drop-in worker retrieval queries

## Q1 — Purpose and prerequisite scope

**Query:** What does the Walley Web Drop-in page add, and what minimum Drop-in version and setup does it require?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-walley-web-drop-in.md` → `raw/adyen/docs/payment-methods/walley/web-drop-in/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/walley/web-drop-in`; full pinned raw `raw/adyen/docs/payment-methods/walley/web-drop-in/2026-09-15.md`, `# Walley Drop-in integration` lines 15–19, `## Requirements` lines 21–26 and `## Drop-in configuration` lines 344–346. The Web guide requires at least v3.23.0, Support setup in test Customer Area, and no additional Walley-specific Drop-in configuration; it does not prove a current live merchant or a completed payment.

## Q2 — Request fields and sample limits

**Query:** Which Walley shopper, line-item and conditional B2B fields are needed, which method type should B2C or B2B use, when must an Authorised payment be captured, and what is wrong with the Web Drop-in examples?

**Expected route:** Same root → Adyen index → online-payments concept → Walley Web Drop-in source → pinned child raw; for product type, DK/DKK and capture timing, follow [[source-adyen-docs-payment-methods-walley]] → `raw/adyen/docs/payment-methods/walley/2026-09-15.md`.

**Evidence locator:** Same canonical stem and full pinned raw path: `## API reference` Sessions lines 30–45 and Payments lines 47–62, curl example lines 64–104, and `## Test and go live` lines 348–361. Preserve working mobile number with country code, email, line-item fields and 50-character description maximum. `company.name` is only required for walley_b2b, while registration number is B2B-relevant but unmarked. All shown Payments language examples leave `paymentMethod.type` empty (for example line 78), so no copy-ready method request exists here; NO/EUR and item totals in the samples do not establish supported combinations or a real order. The related approved overview at `raw/adyen/docs/payment-methods/walley/2026-09-15.md`, lines 23–32, names B2C `walley`, B2B `walley_b2b`, limits Denmark or DKK to B2C, and requires capture of Authorised payments within 90 days. Attribute those to the overview, not this Web child; the overview's countries/currencies are not a complete pairing matrix or proof of merchant eligibility. Test instructions include CivRegNo/socialSecurityNumber and B2B company data.
