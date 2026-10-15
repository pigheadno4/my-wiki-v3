# C10 fixed queries — docs-development-resources-migrating-payment-data, attempt 2

## Q1 — Purpose, scope, and inference boundary

**Query:** Does the migration page describe exporting Adyen data, changing merchant of record, or guarantee an imported card can immediately be charged?

**Expected answer:** It is a dated guide to importing prior-PSP payment data into Adyen for history/analysis and staged card-detail migration. Export in the process is from the old PSP to Adyen. It does not allocate seller/payee or merchant-of-record status, prove consent or PCI compliance, report per-record import success, or guarantee account activation or a successful recurring charge. Its no-charge and usual 10-day-or-more statements are 2019-modified provider guidance, not current commercial terms or an SLA.

**Evidence:** `raw/adyen/docs/development-resources/migrating-payment-data/2026-09-15.md:15-21`, `raw/adyen/docs/development-resources/migrating-payment-data/2026-09-15.md:23-55`.

**Canonical retrieval route:** `[[adyen-index]]` → `[[adyen-tokenization]]` → `[[source-adyen-docs-development-resources-migrating-payment-data]]` → pinned raw.

## Q2 — Central capability, prerequisites, and warnings

**Query:** What coordination, reference mapping, encryption and staging does Adyen's old-PSP migration overview require?

**Expected answer:** The merchant supports tokenization and recurring charges across both PSPs during transition, chooses an internal Adyen `shopperReference`, checks mapping with the old PSP, and coordinates the file-transfer method with the old PSP and Adyen. If the old PSP can export the required format, contact Adyen Support for a custom PGP key; otherwise the old PSP encrypts its format with Adyen's PGP key for custom manipulation. Adyen recommends routing new sign-ups/tokenizations to Adyen first, importing old card details, then switching old-customer charges. If new tokenizations cannot move immediately, request the interim tokens from the old PSP. Recurring and referral data require separate CSV files, and their guides describe different fields. Per-detail import results are described in the recurring-import guide; the referral-list guide does not describe an acceptance report. The encrypted transfer and completed steps do not independently verify per-record import or payment outcomes.

**Evidence:** `raw/adyen/docs/development-resources/migrating-payment-data/2026-09-15.md:23-53`; `[[source-adyen-docs-development-resources-migrating-payment-data-import-payment-details-for-recurring-payments]]`; `[[source-adyen-docs-development-resources-migrating-payment-data-import-data-into-referral-lists]]`.

**Canonical retrieval route:** `[[adyen-index]]` → `[[adyen-tokenization]]` → `[[source-adyen-docs-development-resources-migrating-payment-data]]` → pinned raw.
