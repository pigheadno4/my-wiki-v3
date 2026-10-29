# Alma iOS Component worker retrieval queries

## Q1 — Purpose and scope

**Query:** What does the Alma iOS Component guide add, and which flow prerequisites does it specify?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-alma-ios-component.md` → `raw/adyen/docs/payment-methods/alma/ios-component/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/alma/ios-component`; full pinned raw `raw/adyen/docs/payment-methods/alma/ios-component/2026-09-15.md`, `# Alma iOS Component` lines 15–23, `## Sessions flow Component` lines 25–35 and `## Advanced flow Component` lines 120–130. The guide extends an existing iOS Components integration; Sessions requires Checkout API v68+. The Advanced requirement link says Components but points to `integration=Drop-in`; its other links say Components. No current eligibility or transaction outcome follows.

## Q2 — Capability, prerequisites and warnings

**Query:** Which Alma fields and installment choice does the page specify for iOS Components, and what does the redirect response mean?

**Expected route:** Same root → Adyen index → online-payments concept → Alma iOS Component source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path; Sessions field table lines 39–48, `## Initialize the Component for Alma` lines 94–112, Advanced table lines 161–171, Advanced response lines 213–227, and `## Test and go live` lines 114–118 and 229–233. The TEST curl examples omit a shell continuation after `-X POST` before `-d` at raw lines 57–58 and 180–181, so neither literal command is copy-ready. The listed telephone/email/address fields have blank Required cells; optional `alma.installments_count` is 3 or 4, or omitted for shopper choice. Both flows use `InstantPaymentComponent` with different delegates. `RedirectShopper` is an intermediate action; the FR/EUR examples and return-URL schemes are not universal eligibility or scheme rules.
