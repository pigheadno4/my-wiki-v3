# Braintree C17 fixed query audit — Group C

Scope: exactly the four fixed Group C questions for Decline Analysis and Expiring and Expired Cards. Both promoted source pages and both pinned raws were read completely. The repository remained read-only.

## `control-panel-reporting-decline-analysis`

Actual concept-led route: `wiki/index.md` (`## PSP Indexes`, line 11 → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts`, line 187 → `[[braintree-control-panel]]`) → `wiki/concepts/braintree-control-panel.md` (`## Sources`, line 21 → `[[source-braintree-control-panel-reporting-decline-analysis]]`) → `wiki/sources/braintree/source-braintree-control-panel-reporting-decline-analysis.md` (`raw_files`, lines 7–8; `## Raw Sources`, lines 46–48) → `raw/braintree/articles/control-panel/reporting/decline-analysis-2026-09-16.md`.

1. **Where is Braintree Decline Analysis report documented?**
   - **Object/action match:** Braintree Control Panel workflow for searching processor-declined transactions and analyzing downloaded results, not authorization-response retry policy or the separate general Declines article.
   - **Direct answer:** The promoted `source-braintree-control-panel-reporting-decline-analysis.md` retrieval entry routes to the complete collected `# Decline Analysis` raw at the path above.
   - **Exact locator:** raw provenance and canonical identity at lines 1 and 6–7; page identity at line 14; purpose at line 16.
   - **Verdict:** PASS.

2. **Which decline-analysis views and limits does this page state, without importing retry rules?**
   - **Object/action match:** search and CSV-analysis views for observed processor declines, not a prescription to retry a transaction or a rule for retry eligibility, timing, or count.
   - **Direct answer:** The workflow filters Transaction Search to `Processor Declined`, permits a date-range adjustment and CSV download, and sends card-verification users to a separate verification search when expected declines are missing. One analysis view groups downloaded results by `Processor Response Text`; repeated attempts using the same payment method can skew the decline rate, so duplicate CSV values can be removed to clarify unique declines. The second view groups by `First Six of Credit Card` and uses BIN lookup to investigate patterns by card type, location, possible prohibited transactions, or issuing bank. The article says richer customer transaction data can improve analysis and separately routes fraudulent-transaction decline reduction to Fraud Tools. It states no retry eligibility, timing, or advice.
   - **Exact locator:** `## Running a decline search`, lines 19–34; `## Analyzing the results`, lines 39–41; `### Processor responses`, lines 44–48; `### Bank identification numbers`, lines 51–57; `## Reducing declines`, lines 60–62.
   - **Verdict:** PASS.

## `control-panel-reporting-expiring-cards`

Actual concept-led route: `wiki/index.md` (`## PSP Indexes`, line 11 → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts`, line 187 → `[[braintree-control-panel]]`) → `wiki/concepts/braintree-control-panel.md` (`## Sources`, line 19 → `[[source-braintree-control-panel-reporting-expiring-cards]]`) → `wiki/sources/braintree/source-braintree-control-panel-reporting-expiring-cards.md` (`raw_files`, lines 7–8; `## Raw Sources`, lines 43–45) → `raw/braintree/articles/control-panel/reporting/expiring-cards-2026-09-16.md`.

3. **Where is Braintree Expiring and Expired Cards report documented?**
   - **Object/action match:** Braintree Control Panel report for Vault cards that have expired or will expire, not the Node `expiringBetween` request, Account Updater webhook, or Account Updater service guide.
   - **Direct answer:** The promoted `source-braintree-control-panel-reporting-expiring-cards.md` retrieval entry routes to the complete collected `# Expiring and Expired Cards` raw at the path above.
   - **Exact locator:** raw provenance and canonical identity at lines 1 and 6–7; page identity at line 14; report purpose at line 16.
   - **Verdict:** PASS.

4. **What can this report identify, and what update or action does it not itself establish?**
   - **Object/action match:** report visibility over expired or soon-to-expire Vault cards, not card maintenance, customer outreach, or enrollment in an updater service.
   - **Direct answer:** The report lists cards that have expired or will expire in a selected time frame. A merchant can run it from **Reports** → **Vault** → **Expiring Cards**, choose a custom range, or use **View All Expired**. The article presents recurring billing as a use case and says a merchant can use the list to send reminders; it does not say the report sends those reminders. Separately, depending on account setup, most Braintree Direct merchants domiciled in the US or transacting primarily with US customers may be able to enable Account Updater to request vaulted-payment-method updates automatically. The report itself does not update cards, contact customers, enable or invoke Account Updater, or guarantee updated card details.
   - **Exact locator:** report identity, time-frame scope and merchant reminder example at line 16; `## Running an Expiring Cards report`, lines 19–28; separate qualified Account Updater option under `## Reducing expired cards`, lines 31–33.
   - **Verdict:** PASS.

## Shared gap sweep and reciprocal-link check

- **Pinned evidence:** complete selected raws match the C17 manifest hashes: Decline Analysis `5e38f313311dcdef1b603582c9639a92855df4e2366c84268b9a6da2181a0756`; Expiring Cards `3d11429f83ff6ff6d8863c4d68ff02fe55e8bc7995e116825f01588c89fa5248`.
- **Bounded gap sweep:** filename/topic checks also surfaced the separate 596-line Control Panel `transactions/declines` article, the Node `credit-card/expiring-between` request, the Account Updater guide and Account Updater webhook reference. They are different objects/actions and were not needed to answer these four fixed questions. The Expiring Cards source labels the linked Account Updater guide navigation-only; no fact was imported from it. The Reporting Overview and BIN source contain navigation routes to the selected raws but add no required fact.
- **Reciprocal routes:** `braintree-control-panel` lists each promoted source once; each source links back to `braintree-control-panel` and to its exact pinned raw. Decline Analysis also has a reciprocal `payment-reconciliation-reporting` route; Expiring Cards also has a reciprocal `recurring-payments` route. The required root → provider index → concept → source → raw chains resolve independently of any direct provider-source catalog close. At the final audit snapshot, the provider index also contained direct source rows at lines 19–20.
- **Completeness:** all 4/4 fixed questions include object/action match, direct answer, exact raw locator and verdict. No retry rules were imported, and no automatic report-driven card update or reminder was asserted. No repair or additional promotion is required.

**Group verdict: PASS (4/4).**
