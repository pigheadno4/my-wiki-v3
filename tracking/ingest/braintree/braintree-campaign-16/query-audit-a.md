# Braintree C16 Query Audit — Group A

- Scope: Transaction Lifecycle + Managing Authorizations.
- Audited: `2026-09-23` UTC after both source promotions.
- Evidence: both selected raw pages read completely; source and retrieval routes inspected.

## Transaction Lifecycle

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-server-sdk]]` → `[[source-braintree-transaction-lifecycle]]` → `[[raw/braintree/articles/get-started/transaction-lifecycle-2026-09-16]]`.

1. **Query:** Where is Braintree Transaction Lifecycle documented?
   - **Object/action match:** Provider-level successful-transaction status progression, not the complete status-code reference.
   - **Direct answer:** The source entry above links the complete collected Transaction Lifecycle article.
   - **Exact raw locator:** `# Transaction Lifecycle`, lines 14–20; successive status headings, lines 23–42.
   - **Verdict:** PASS; provider-index direct catalog entry awaits aggregate close.

2. **Query:** How does this page distinguish transaction status stages without equating submission with final settlement or funding?
   - **Object/action match:** Authorization hold, settlement initiation, processor communication, merchant-account settlement, and later bank routing.
   - **Direct answer:** `Authorized` is bank approval and a hold, not removal of funds. `Submitted for Settlement` starts removal and is the Control Panel creation default. `Settling` begins processor communication and has bank-dependent duration. `Settled` is shown when funds hit the merchant account and are then routed to the merchant bank account; the page does not establish bank-account arrival time. Other unsuccessful/interrupted statuses are left to a separate reference.
   - **Exact raw locator:** `Authorized`, lines 23–25; `Submitted for Settlement`, lines 28–32; `Settling`, lines 35–37; `Settled`, lines 40–42; `Other statuses`, lines 45–47.
   - **Verdict:** PASS.

## Managing Authorizations

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-control-panel]]` → `[[source-braintree-control-panel-managing-authorizations]]` → `[[raw/braintree/articles/control-panel/transactions/managing-authorizations-2026-09-16]]`.

3. **Query:** Where is Braintree Control Panel Managing Authorizations documented?
   - **Object/action match:** A page in the Control Panel documentation tree, but its operative verify/store, repeat, adjustment and submission steps are API/SDK or merchant-integration actions; it does not define a Control Panel button.
   - **Direct answer:** The concept links the dedicated Managing Authorizations source, which links the complete collected article.
   - **Exact raw locator:** `# Managing Authorizations`, lines 14–16; `## Authorization options`, lines 27–35.
   - **Verdict:** PASS; provider-index direct catalog entry awaits aggregate close.

4. **Query:** Which authorization-management options, eligibility and timing boundaries does this Control Panel article document?
   - **Object/action match:** Expiring authorization options and qualified amount adjustments, without claiming a UI operation or universal current eligibility.
   - **Direct answer:** Verify and store is recommended: verify card when applicable, vault the method, then create a charge when ready, with no later funds/account guarantee. Repeated authorization is discouraged and needs merchant logic using payment-method-specific expiry, voiding and reauthorizing, then submitting only the latest transaction; it may create duplicate pending holds and extra fees. Select merchants/processors can adjust before settlement via Auth Adjustment API or during submission; issuer-declined changes yield validation errors and leave the original `Authorized`. The collected page limits adjustments to Visa/Mastercard with Visa category restrictions, while its US-only and wider regional lists conflict and cannot establish a single reliable current region list. Authorization/capture fees are market-qualified.
   - **Exact raw locator:** expiry/fee notes lines 16–22; option ranking lines 27–35; verify/store steps and limitations lines 38–60; repeated authorization lines 63–94; adjustment behavior and conflicting region statements lines 97–156.
   - **Verdict:** PASS, with the region conflict explicitly surfaced rather than resolved by inference.

## Bounded gap sweep

- Inspected nearby source/concept routes and the selected raws for stage and authorization language. The status-reference and API-operation links provide navigation, not additional factual evidence for these four answers.
- Both sources have exact raw backlinks and reciprocal concept routes. No omitted stage boundary, unsupported Control Panel action, broken link or unresolved material conflict in the answer. Group A: **4/4 PASS**.
