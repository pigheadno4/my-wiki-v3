# Braintree C17 fixed query audit — Group B

## Result

**Initial: FAIL; final: PASS after bounded paired repair.** All four fixed query questions were individually **PASS**, both selected raw files and both selected source pages were read completely, and each raw SHA-256 matches the C17 manifest. The initial gap was an unmarked country-eligibility contradiction between Reporting Overview and the dedicated Transaction-Level Fee Report.

This audit reports only what the 2026-09-16 collected pages state. It does not claim current applicability.

## Canonical retrieval route and pin check

The actual route for both pages is:

`wiki/index.md:11` → `wiki/braintree-index.md:176` → `wiki/concepts/braintree-control-panel.md` → promoted source → exact raw link.

At audit time the working provider route went through `[[braintree-control-panel]]`; direct C17 source catalog entries were added at campaign close. Line numbers below are audit-time navigation observations; raw locators are stable.

| Page | Concept → source | Source → pinned raw | Manifest/hash |
| --- | --- | --- | --- |
| Settlement Batch Summary | `wiki/concepts/braintree-control-panel.md:23` | `wiki/sources/braintree/source-braintree-control-panel-reporting-settlement-batch-summary.md:45` → `raw/braintree/articles/control-panel/reporting/settlement-batch-summary-2026-09-16.md` | `90f350f4cbbb9408c809b1e7ddd10d33dfe64bcee7667d2a1470e0072caf9502`, exact match |
| Transaction-Level Fee Report | `wiki/concepts/braintree-control-panel.md:25` | `wiki/sources/braintree/source-braintree-control-panel-reporting-transaction-level-fee-report.md:46` → `raw/braintree/articles/control-panel/reporting/transaction-level-fee-report-2026-09-16.md` | `d4ead89667e34a29add4dbec9dc4378b5801dd9ab3326a1ea503f8bcf4b376f7`, exact match |

## Four fixed questions

### 1. Where is Braintree Control Panel Settlement Batch Summary documented?

- **Object/action match:** Control Panel report documentation and report operation, not the separate Node.js Settlement Batch Summary API request/response object.
- **Direct answer:** Follow the canonical route above to `source-braintree-control-panel-reporting-settlement-batch-summary`, whose canonical provider URL is `https://developer.paypal.com/braintree/articles/control-panel/reporting/settlement-batch-summary` and whose exact evidence is the pinned raw file above.
- **Exact raw locator:** `# Settlement Batch Summary`, raw line 14; report-running section at `## Running a Settlement Batch Summary`, raw lines 19–35.
- **Verdict:** **PASS**.

### 2. What does this settlement-batch report represent, and which date, status or funding boundaries does the page state?

- **Object/action match:** Describe the Control Panel report's represented batch totals and its explicit scope/boundaries; do not import API response semantics, individual lifecycle transitions, or bank-ledger proof.
- **Direct answer:** The page says transactions already submitted for settlement are sent to processors in settlement batches, and the report displays total sales and credits per batch. Users can scope it by date range, merchant account, and payment-type exclusions. Access requires the Create, Run, and Download Reports permission; marketplace sub-merchant accounts are excluded and CSV export is capped at 40,000 rows. The page establishes only the starting status `submitted for settlement`; it does not establish later or final transaction status. The batch cutoff is account-dependent and cannot be changed. Excluding PayPal may better reconcile the report to Braintree disbursements, and merchants using their own Amex account may exclude Amex because those funds are not in Braintree deposits; neither statement proves that a batch or transaction funded.
- **Exact raw locators:** representation/scope `# Settlement Batch Summary`, line 16; run/date/export/permission `## Running a Settlement Batch Summary`, lines 21–31; marketplace exclusion `NOTE`, lines 34–35; PayPal/Amex funding qualifications `### Excluding PayPal or American Express transactions`, lines 40–42; cutoff boundary `### Settlement batch cutoff times`, lines 45–47.
- **Verdict:** **PASS**.

### 3. Where is Braintree Transaction-Level Fee Report documented?

- **Object/action match:** Control Panel downloadable fee report and its run/download operation, not a settlement-status endpoint, fee invoice, or funding ledger.
- **Direct answer:** Follow the canonical route above to `source-braintree-control-panel-reporting-transaction-level-fee-report`, whose canonical provider URL is `https://developer.paypal.com/braintree/articles/control-panel/reporting/transaction-level-fee-report` and whose exact evidence is the pinned raw file above.
- **Exact raw locator:** `# Transaction-Level Fee Report`, raw line 14; operation at `## Running a Transaction-Level Fee report`, raw lines 33–47.
- **Verdict:** **PASS**.

### 4. What fee-report purpose, access/availability, timing and reconciliation boundaries does this page document?

- **Object/action match:** State the dedicated report page's pricing-model-specific contents and timing; do not turn post-disbursement availability into settlement or funding mechanics.
- **Direct answer:** The report provides transaction and associated-fee details, with content depending on pricing model. In this collected page, default availability is US/Australia for IC+ and US/Australia/Brazil for flat-rate or blended pricing. Access requires the Create, Run, and Download Reports permission; the user selects a merchant account/date range, runs, and downloads the report. It supports credit/debit cards, Venmo, Apple Pay, and Google Pay, while excluding directly processed Amex and all PayPal transactions. Flat-rate/blended rows contain actual Braintree fees and appear three calendar days after the settled amount is disbursed; the page identifies transaction-level reconciliation as a use. IC+ rows contain interchange estimates, appear five calendar days after that disbursement, may be reclassified, and must not be used for reconciliation; actual interchange is passed through as a consolidated month-end sum, so exact transaction-level interchange assessments are unavailable. The timing uses disbursement as a clock but does not document settlement or bank-disbursement mechanics.
- **Exact raw locators:** default availability `# Transaction-Level Fee Report > AVAILABILITY`, lines 17–18; purpose/methods lines 22–30; permission/run/download `## Running a Transaction-Level Fee report`, lines 33–43; exclusions `NOTE`, lines 46–47; flat-rate/blended actual fees, three-day timing and reconciliation use `## Flat rate and blended pricing models`, lines 52–63; IC+ estimate warning and five-day timing `## IC+ pricing models`, lines 66–87; reclassification/month-end/no-reconciliation boundary `### Interchange fee estimates`, lines 101–105.
- **Verdict:** **PASS** for the dedicated-page question; see the cross-page **FAIL** below.

## Bounded gap sweep

The sweep was limited to `raw/braintree/**/*.md` matches for the two exact report names. The directly conflicting Reporting Overview raw and its promoted source were then read completely. Other matches were SDK/API or regional/provider-specific objects and were excluded from the answer rather than generalized.

**Failure:** `raw/braintree/articles/control-panel/reporting/overview-2026-09-16.md:39–44` says the Transaction-Level Fee report is available to US merchants only across the named pricing models. The dedicated raw at `raw/braintree/articles/control-panel/reporting/transaction-level-fee-report-2026-09-16.md:17–18` instead says IC+ is available by default in the US and Australia, while flat-rate/blended is available by default in the US, Australia, and Brazil. Both are same-collection evidence; neither proves current eligibility. The dedicated promoted source accurately reports its own raw and has a snapshot caveat, while the overview source accurately reports its own raw and says to follow dedicated pages, but neither explicitly records the contradiction.

### Smallest evidence-accurate repair wording

- **Selected Settlement Batch Summary source:** no repair needed; its existing report/API/funding warning is adequate.
- **Selected Transaction-Level Fee Report source:** add:

  > [!warning] Collected eligibility conflict
  > In the same 2026-09-16 collection, the Reporting Overview says this report is US-only (overview lines 39–44), while this dedicated page lists IC+ availability for US/Australia and flat-rate or blended availability for US/Australia/Brazil (lines 17–18). The collected pages conflict; neither establishes current eligibility.

- **Reciprocal repair on the Reporting Overview source:** because the project convention requires contradictions to be visible on both affected pages, add:

  > [!warning] Collected eligibility conflict
  > This overview says the report is US-only (lines 39–44), while the dedicated Transaction-Level Fee Report page lists IC+ availability for US/Australia and flat-rate or blended availability for US/Australia/Brazil (dedicated page lines 17–18). The collected pages conflict; neither establishes current eligibility.

## Reciprocal-link check

- Provider concept → both sources: present at `wiki/concepts/braintree-control-panel.md:23,25`.
- Both sources → provider concept and `[[payment-reconciliation-reporting]]`: present at source lines `39–40` and `42` respectively.
- Cross-cutting concept → both sources: present at `wiki/concepts/payment-reconciliation-reporting.md:113–114`.
- Both sources → exact raw: present and resolvable at source lines `45` and `46`.
- Root → provider index and provider index → concept: present at `wiki/index.md:11` and `wiki/braintree-index.md:176`.
- Direct provider-index → C17 source entries: added in the campaign-close catalog update.

## Repair close

An independent narrow review approved reciprocal conflict warnings. The coordinator added the reviewed warnings to the Reporting Overview and Transaction-Level Fee Report sources, added each opposing fully read raw under `raw_files` and `## Raw Sources`, and removed the fee raw from the overview's navigation-only list. Both raw statements remain visible without claiming which controls current eligibility. No Settlement Batch Summary change was needed. Group B final verdict: **4/4 PASS, consistency gap repaired**.
