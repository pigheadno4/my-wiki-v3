# Clearpay Web chooser worker retrieval queries

## Q1 — Purpose and scope

**Query:** What does the Clearpay for Web page provide, and where are implementation details?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-clearpay-web.md` → `raw/adyen/docs/payment-methods/clearpay/web/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/clearpay/web`; full pinned raw `raw/adyen/docs/payment-methods/clearpay/web/2026-09-15.md`, `# Clearpay for Web` lines 15–27 and `## See also` lines 29–36. This is a chooser linking method-specific and main integration guides, not an implementation recipe or payment-outcome record.

## Q2 — Central routes and prerequisites

**Query:** Which Web UI paths and base flows are linked, and what does the Components label say?

**Expected route:** Same root → Adyen index → online-payments concept → Clearpay Web chooser source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path; `### How do you want to integrate?` lines 19–27 and `## See also` lines 29–36. The page links Drop-in and Components child guides, describes Redirect for the Components route, and directs readers to create a Web Sessions or Advanced base integration first. It does not establish API/Web SDK versions, required fields, merchant availability, capture/refund support or result finality.
