# Braintree C17 fixed query audit — Group A

## Result

**Initial: FAIL; final: PASS after bounded paired repair.** All four fixed query questions were individually **PASS**. Both selected source pages and both selected pinned raws were read completely, and both raw SHA-256 values match the C17 manifest. The initial gap was that the Reporting Overview and dedicated Transaction-Level Fee Report preserved contradictory country-eligibility statements without reciprocal warnings.

This audit reports only what the 2026-09-16 collected pages state. It does not claim current report availability or eligibility.

## Canonical retrieval route and pin check

The actual route for both Group A pages is:

`wiki/index.md:11` → `wiki/braintree-index.md:176` → `wiki/concepts/braintree-control-panel.md` → promoted source → exact pinned raw.

At audit time the working provider route went through `[[braintree-control-panel]]`; direct C17 source catalog entries were added at campaign close. Line numbers below are audit-time navigation observations; raw locators are stable.

| Page | Concept → source | Source → pinned raw | Manifest/hash |
| --- | --- | --- | --- |
| Reporting Overview | `wiki/concepts/braintree-control-panel.md:28` | `wiki/sources/braintree/source-braintree-control-panel-reporting-overview.md:59` → `raw/braintree/articles/control-panel/reporting/overview-2026-09-16.md` | `9cf4ac60ec449df443d8d8b314b4146374b6810305fae018d34b349bcda5a2e0`, exact match |
| Transaction Summary | `wiki/concepts/braintree-control-panel.md:23` | `wiki/sources/braintree/source-braintree-control-panel-reporting-transaction-summary.md:42` → `raw/braintree/articles/control-panel/reporting/transaction-summary-2026-09-16.md` | `3088bbbc3614cb68e3a9997f636c3ae99ed5dfb5562bccc0a734849d0c62088e`, exact match |

## Four fixed questions

### 1. Where is Braintree Control Panel Reporting Overview documented?

- **Object/action match:** Control Panel reporting-category overview and navigation, not the general Control Panel Overview, an SDK/API report object, or any one dedicated report's operation.
- **Direct answer:** Follow the canonical route above to `source-braintree-control-panel-reporting-overview`, whose canonical provider URL is `https://developer.paypal.com/braintree/articles/control-panel/reporting/overview` and whose exact evidence is the pinned raw above.
- **Exact raw locator:** `# Overview`, raw lines 14–16; category sections span `## Decline analysis` through `## Statements`, raw lines 19–70.
- **Verdict:** **PASS**.

### 2. Which reporting categories and Dashboard-versus-reconciliation boundaries, if any, does this overview establish?

- **Object/action match:** State only the categories and qualifications in the reporting overview; do not import Dashboard behavior from the separate general Control Panel page or report-specific behavior that this overview does not state.
- **Direct answer:** The overview routes to Decline Analysis, Expiring Cards, Settlement Batch Summary, Transaction-Level Fee report, Transaction Summary, 1099-K, and Statements. It says overall availability depends on account setup and business location. It describes Decline Analysis as Advanced Search-based decline-rate analysis sortable by processor response or BIN; Expiring Cards as Vault cards expired or expiring in a specified range; Settlement Batch Summary as transactions processed in a batch grouped by payment method, with optional email; Transaction Summary as current successful/unsuccessful categorization for a date range and processing trends; and 1099-K as limited to applicable US-domiciled Braintree Direct merchants for tax purposes. Statements vary by setup/country, often include pricing, fee, processing, and disbursement details, and **may** help with reconciliation. The page never mentions the Dashboard, so it establishes no Dashboard-versus-reconciliation rule and does not establish that statements are sufficient for reconciliation. Its US-only Transaction-Level Fee eligibility statement must remain attributed to this overview and unresolved because the same-date dedicated page conflicts (see gap sweep).
- **Exact raw locators:** overall availability `# Overview`, lines 14–16; Decline Analysis lines 19–23; Expiring Cards lines 26–29; Settlement Batch Summary lines 32–36; Transaction-Level Fee report lines 39–44; Transaction Summary lines 47–51; 1099-K lines 54–58; Statements lines 61–70. Dashboard is absent from the complete 73-line raw.
- **Verdict:** **PASS** for the fixed question; see the cross-page **FAIL** below.

### 3. Where is Braintree Control Panel Transaction Summary documented?

- **Object/action match:** Control Panel Transaction Summary report and its run/interpretation flow, not the Dashboard itself, a transaction search/API response, or the separate Settlement Batch Summary API object.
- **Direct answer:** Follow the canonical route above to `source-braintree-control-panel-reporting-transaction-summary`, whose canonical provider URL is `https://developer.paypal.com/braintree/articles/control-panel/reporting/transaction-summary` and whose exact evidence is the pinned raw above.
- **Exact raw locator:** `# Transaction Summary`, raw lines 14–18; report operation at `## Running a Transaction Summary`, lines 21–29; interpretation at `## Interpreting Transaction Summary results`, lines 32–36.
- **Verdict:** **PASS**.

### 4. Which summary measures, filters or timing boundaries does this page actually document?

- **Object/action match:** Describe the Control Panel report's current-status totals and only its explicit grouping/date controls; do not infer settlement, funding, refresh, latency, timezone, or finality semantics.
- **Direct answer:** The report gives a high-level view of transactions currently categorized as successful or unsuccessful within a selected date range. The user chooses how to group results and selects the date range. In the result table, chosen Group by fields form rows, transaction statuses form columns, and displayed amounts represent transactions **currently** in each status. Statuses can change, so Braintree presents the report for processing-trend identification and explicitly says it should not be used for reconciliation. The page documents no named date field, timezone, preset interval, refresh cadence, reporting latency, settlement/funding timing, or final status.
- **Exact raw locators:** purpose/current categorization/Dashboard comparison `# Transaction Summary`, line 16; trend and non-reconciliation warning line 18; grouping/date-range controls `## Running a Transaction Summary`, lines 21–29; row/column/current-status amount semantics `## Interpreting Transaction Summary results`, lines 32–36.
- **Verdict:** **PASS**.

## Bounded gap sweep

The sweep was limited to `raw/braintree/**/*.md` matches for the exact report names and Reporting Overview. The same-snapshot dedicated Transaction-Level Fee Report raw and its promoted source were read completely because they directly conflict with the selected overview. Other matches were regional reconciliation/report-format pages, general exploration navigation, or processor-specific pricing/statement pages; they were excluded rather than generalized into current Control Panel eligibility.

**Failure:** `raw/braintree/articles/control-panel/reporting/overview-2026-09-16.md:39–44` says the Transaction-Level Fee report is available to US merchants only across the named pricing models. The dedicated raw at `raw/braintree/articles/control-panel/reporting/transaction-level-fee-report-2026-09-16.md:17–18` instead says IC+ is available by default in the US and Australia, while flat-rate/blended is available by default in the US, Australia, and Brazil. Both are same-collection evidence; neither proves current eligibility. The promoted pages accurately preserve their respective raw claims and snapshot boundaries, but neither explicitly records the contradiction.

### Smallest evidence-accurate repair wording

- **Selected Reporting Overview source:** add:

  > [!warning] Collected eligibility conflict
  > This overview says the Transaction-Level Fee report is US-only (overview lines 39–44), while the dedicated Transaction-Level Fee Report page lists IC+ availability for US/Australia and flat-rate or blended availability for US/Australia/Brazil (dedicated page lines 17–18). The collected pages conflict; neither establishes current eligibility.

- **Reciprocal repair on the Transaction-Level Fee Report source:** add:

  > [!warning] Collected eligibility conflict
  > In the same 2026-09-16 collection, the Reporting Overview says this report is US-only (overview lines 39–44), while this dedicated page lists IC+ availability for US/Australia and flat-rate or blended availability for US/Australia/Brazil (lines 17–18). The collected pages conflict; neither establishes current eligibility.

- **Selected Transaction Summary source:** no repair needed; its current-status and non-reconciliation boundaries are explicit and evidence-accurate.

## Reciprocal-link check

- Root → provider index and provider index → concept: present at `wiki/index.md:11` and `wiki/braintree-index.md:176`.
- Provider concept → both Group A sources: present at `wiki/concepts/braintree-control-panel.md:23,28`.
- Cross-cutting concept → both Group A sources: present at `wiki/concepts/payment-reconciliation-reporting.md:111,115`.
- Both sources → provider and cross-cutting concepts: present at Overview lines 43–45 and Transaction Summary lines 36–38.
- Both sources → exact raw: present and resolvable at source lines 59 and 42.
- Direct provider-index → C17 source entries: added in the campaign-close catalog update.

## Repair close

An independent narrow review approved reciprocal conflict warnings. The coordinator added the reviewed warnings to the Reporting Overview and Transaction-Level Fee Report sources, added each opposing fully read raw under `raw_files` and `## Raw Sources`, and removed the fee raw from the overview's navigation-only list. Both raw statements remain visible without claiming which controls current eligibility. No Transaction Summary change was needed. Group A final verdict: **4/4 PASS, consistency gap repaired**.
