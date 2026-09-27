# Braintree C17 fixed query audit — Group D

Scope: exactly the four fixed Group D questions for 1099-K and Grant API Report (Beta). Both promoted source pages and both pinned raws were read completely. The repository remained read-only.

## `control-panel-reporting-1099-k`

Actual concept-led route: `wiki/index.md` (`## PSP Indexes`, line 11 → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts`, line 187 → `[[braintree-control-panel]]`) → `wiki/concepts/braintree-control-panel.md` (`## Sources`, line 24 → `[[source-braintree-control-panel-reporting-1099-k]]`) → `wiki/sources/braintree/source-braintree-control-panel-reporting-1099-k.md` (`raw_files`, lines 7–8; `## Raw Sources`, lines 40–42) → `raw/braintree/articles/control-panel/reporting/1099-k-2026-09-16.md`.

1. **Where is Braintree Control Panel 1099-K reporting documented?**
   - **Object/action match:** Braintree's collected Control Panel tax-form reporting page, not a general IRS rule, PayPal's separate 1099-K, an Amex form, or a transaction/settlement report.
   - **Direct answer:** The promoted `source-braintree-control-panel-reporting-1099-k.md` retrieval entry routes to the complete collected `# 1099-K` raw at the path above.
   - **Exact locator:** raw provenance and canonical identity at lines 1 and 6–7; page identity at line 14; qualified form provision and Control Panel availability at line 16.
   - **Verdict:** PASS.

2. **Which form-availability, eligibility and reporting qualifications does the collected page state?**
   - **Object/action match:** availability, access, delivery, calculation, and processor/form boundaries for this collected Braintree 1099-K page; not current tax advice or a universal merchant entitlement.
   - **Direct answer:** Depending on account setup and business location, Braintree says it may be able to provide a 1099-K and, when applicable, makes it available in the Control Panel. Control Panel access requires `View Statements`; Account Admin has that permission by default. The previous year's statement is generated at the end of January and remains available until at least October 15. If it is absent from the Control Panel, only a US Braintree Direct merchant that processed transactions in the previous tax year is promised email or postal delivery. Totals use gross sales volume and exclude credits, refunds, and chargebacks; incorrect information is routed to Braintree for correction. PayPal transactions are excluded and receive a separate PayPal form. Aggregated Amex is included in Braintree monthly totals, while a merchant with its own direct Amex account receives a separate Amex form for those transactions. These are statements preserved from the 2026-09-16 snapshot, not proof of current availability, deadlines, eligibility, or tax requirements.
   - **Exact locator:** `# 1099-K`, line 16; `## Viewing your 1099-K in the Control Panel`, lines 21–35; `## Reconciling 1099-K totals`, lines 40–44; `### PayPal transactions` and `### American Express transactions`, lines 47–54.
   - **Verdict:** PASS.

## `control-panel-reporting-grant-api-report`

Actual concept-led route: `wiki/index.md` (`## PSP Indexes`, line 11 → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts`, line 187 → `[[braintree-control-panel]]`) → `wiki/concepts/braintree-control-panel.md` (`## Sources`, line 22 → `[[source-braintree-control-panel-reporting-grant-api-report]]`) → `wiki/sources/braintree/source-braintree-control-panel-reporting-grant-api-report.md` (`raw_files`, lines 7–8; `## Raw Sources`, lines 44–46) → `raw/braintree/articles/control-panel/reporting/grant-api-report-2026-09-16.md`.

3. **Where is Braintree Grant API Report (Beta) documented?**
   - **Object/action match:** the Braintree Control Panel Grant API summary report labeled Beta, not payment-method grant/revoke API operations, OAuth setup, or Grant API webhook notifications.
   - **Direct answer:** The promoted `source-braintree-control-panel-reporting-grant-api-report.md` retrieval entry routes to the complete collected `# Grant API Report (Beta)` raw at the path above.
   - **Exact locator:** raw provenance and canonical identity at lines 1 and 6–7; report identity at line 14; limited-release qualification at lines 17–18.
   - **Verdict:** PASS.

4. **What does this beta report cover, and which availability or visibility limits are explicit?**
   - **Object/action match:** Control Panel reporting for recipient transaction count and volume, not the behavior or eligibility of grant, revoke, OAuth, or webhook APIs.
   - **Direct answer:** The page labels the report **Beta** and says the Grant API was “currently in a limited release” in the collected snapshot. The report gives transaction count and transaction volume for each recipient, grouped by currency. A recipient appears only after consenting through the OAuth flow. A user runs it under **Reports**, selects a date range, and runs **Grant API Summary**. The page does not establish report freshness, exports, reconciliation completeness, transaction-type coverage, API operation behavior, or current/general availability; the 2026-09-16 snapshot preserves the beta/limited-release statement without proving today's availability.
   - **Exact locator:** `# Grant API Report (Beta) > **AVAILABILITY**`, lines 14–18; report measures, grouping, and OAuth-consent visibility at line 22; `## Running a Grant API report`, lines 25–34.
   - **Verdict:** PASS.

## Shared gap sweep and reciprocal-link check

- **Pinned evidence:** complete selected raws match the C17 manifest hashes: 1099-K `7a1cac6f4b83c5ec747043f52c52dda857687717c025985e1def3142ed438193`; Grant API Report `bccba529695b12b3e1e7872ad9b8b4c0d473dadb7cffef53637f91090871cc17`.
- **Provider catalog:** the current `wiki/braintree-index.md` now also contains direct provider-source rows for 1099-K and Grant API Report at lines 21–22. Those direct rows are accurate, but the audited concept-led routes above do not depend on them.
- **Bounded gap sweep:** filename/topic checks surfaced the Reporting Overview, the OAuth overview, Grant API webhook reference, and payment-method grant/revoke references. The OAuth and operation/notification pages are different objects/actions and are not needed for these four answers; the Grant source correctly labels the OAuth raw navigation-only and links separate operation and notification source routes. The Reporting Overview separately says the 1099-K is available only to applicable Braintree Direct merchants domiciled in the US (overview raw lines 54–58). That is a narrower adjacent-page qualification, not a statement in the dedicated 1099-K page; it is already retained by the promoted Reporting Overview source. Therefore an answer about overall product eligibility should read both sources, while this fixed question about what the dedicated collected page states passes as scoped.
- **Reciprocal routes:** `braintree-control-panel` lists both promoted sources once; each source links back to `braintree-control-panel` and to its exact pinned raw through both `raw_files` and `## Raw Sources`. The 1099-K source also has a reciprocal `payment-reconciliation-reporting` route. Canonical URLs in both source pages, manifest entries, and raw provenance agree.
- **Completeness:** all 4/4 fixed questions include object/action match, direct answer, exact raw locator, and verdict. No current 1099-K or Grant API availability is asserted. No blocking failure or repair is required; the only bounded gap is the adjacent Reporting Overview's narrower US Braintree Direct qualification, which is already promoted and must be consulted for a broader eligibility query.

**Group verdict: PASS (4/4).**
