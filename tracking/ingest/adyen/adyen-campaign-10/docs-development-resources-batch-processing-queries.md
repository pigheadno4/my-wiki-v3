# Fixed retrieval checks: Adyen batch processing overview

## Q1 — Purpose and scope

**Query:** What is Adyen batch processing in this overview, and what can file upload not prove?

**Expected answer:** The dated development-resources overview describes uploading an input file to submit many payment or modification requests in bulk, with refunds and failed-capture retries as examples. It advises API use for regular payments/modifications because preparing files often takes manual work. This landing page does not prove merchant enablement, file acknowledgment, per-record acceptance, authorization, capture, refund, payout or safe retry of a pending operation. Its metadata says last modified in 2019.

**Raw locators:** `# Batch processing`, lines 15–21; `## Batch processing options`, lines 23–30. **Canonical retrieval route:** [[source-adyen-docs-development-resources-batch-processing]] → [[raw/adyen/docs/development-resources/batch-processing/2026-09-15|pinned raw]].

## Q2 — Central routes, prerequisites and outcome warning

**Query:** How do the Customer Area and SFTP batch routes differ, and what separate result evidence would be needed?

**Expected answer:** Customer Area is modification-only simple CSV, with different merchant accounts allowed in one file and UI help for missing fields/errors. SFTP lists Authorisation, Modification, RefundWithData, Payout, PayoutModification, AccountUpdater and StoreToken; it uses complex CSV with headers/footers/counters/multiline records, one request type and one merchant account per file, plus SFTP setup and PGP encryption. The overview links to detailed procedures but does not state acknowledgment or final per-record result semantics. Transport or acknowledgment, if later documented, must be kept separate from financial outcome; inspect the relevant route-specific request, acknowledgment and result files before making an outcome claim.

**Raw locators:** `## Batch processing options`, lines 23–30; `## Choose an option`, lines 32–40. **Canonical retrieval route:** [[source-adyen-docs-development-resources-batch-processing]] → [[raw/adyen/docs/development-resources/batch-processing/2026-09-15|pinned raw]].

**Cross-source qualification:** The separately reviewed SFTP guide says Support can enable modifications for multiple merchant accounts without defining whether one-merchant-account-per-file composition changes. Preserve this unresolved scope alongside the overview table; see [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files]] pinned raw lines 23–25 versus overview line 30.
