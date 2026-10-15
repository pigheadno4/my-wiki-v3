# Data Protection API retrieval checks

## Q1 — Purpose and scope

**Query:** What data does Adyen's Data Protection API request erase, and does it erase my merchant database or all financial records?

**Answer:** The page describes a GDPR subject-erasure request to Adyen for shopper-related data tied to a specific original payment authorisation, selected by `merchantAccount` and `pspReference`. Adyen says transaction-data deletion follows the Merchant Agreement and shopper-related fields are redacted in Customer Area. This page does not establish deletion of merchant-held data or unconditional removal of every transaction/financial record. It is a 2026-09-15 snapshot of a page last modified 2023-05-31, not present-day proof of legal compliance. **Raw locators:** `raw/adyen/docs/development-resources/data-protection-api/2026-09-15.md:15-31`, `:59-61`. **Canonical route:** [[source-adyen-docs-development-resources-data-protection-api]] → [[raw/adyen/docs/development-resources/data-protection-api/2026-09-15]]; [[adyen-tokenization]] for the distinct token lifecycle.

## Q2 — Request lifecycle and recurring qualification

**Query:** Does `SUCCESS` mean deletion is finished, and does `forceErasure` cancel the recurring transaction?

**Answer:** No. The merchant submits `POST /requestSubjectErasure` for the original payment; the sample uses an API key at a TEST host, with a separate live-domain instruction. `SUCCESS` is receipt for asynchronous processing. If `ACTIVE_RECURRING_TOKEN_EXISTS` is returned, the guide says `forceErasure: true` can proceed with shopper-data deletion for this payment, but it does not cancel the existing recurring transaction. The optional follow-up is to check the specific payment in Customer Area for `REDACTED` fields and a redaction date. This is distinct from Checkout API stored-token deletion. **Raw locators:** `raw/adyen/docs/development-resources/data-protection-api/2026-09-15.md:23-42`, `:44-63`; token distinction: [[source-adyen-docs-online-payments-tokenization-managing-tokens]]. **Canonical route:** [[source-adyen-docs-development-resources-data-protection-api]] → [[raw/adyen/docs/development-resources/data-protection-api/2026-09-15]]; [[adyen-tokenization]].
