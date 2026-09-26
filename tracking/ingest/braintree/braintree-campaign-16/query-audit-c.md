# Braintree C16 Query Audit — Group C

- Scope: Duplicate Transaction Checking + Gateway Rejections.
- Audited: `2026-09-23` UTC after both source promotions.
- Evidence: both selected raw pages read completely; source and root/provider-index → concept routes inspected.

## Duplicate Transaction Checking

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-control-panel]]` → `[[source-braintree-control-panel-duplicate-checking]]` → `[[raw/braintree/articles/control-panel/transactions/duplicate-checking-2026-09-16]]`.

1. **Query:** Where is Braintree Duplicate Transaction Checking documented?
   - **Object/action match:** Gateway screening of repeated transaction requests, configured in Control Panel; not an API idempotency method.
   - **Direct answer:** The source and raw article at the route above document the feature.
   - **Exact raw locator:** `# Duplicate Transaction Checking`, lines 14–22; `## Duplicate checking logic`, lines 27–63.
   - **Verdict:** PASS; direct provider-index cataloging awaits aggregate close.

2. **Query:** What duplicate-transaction matching and configuration boundaries does this article document?
   - **Object/action match:** All-conditions/time-window gateway rejection with method-specific comparison and admin configuration.
   - **Direct answer:** Screening is on by default with a 30-second window in Sandbox and Production, adjustable or disableable by Account Admin users. Within that window, a suspected duplicate must meet every relevant general condition: same amount, conditionally same order ID or recurring-billing subscription ID, and successful initial status from the listed set. It must additionally match DPAN for Apple/Google Pay, payer email for PayPal, or card number and expiry for credit cards. In-flight duplicates are rejected immediately; if the original later declines, neither is automatically retried. The article recommends form-level prevention too, and does not promise exactly-once API execution.
   - **Exact raw locator:** purpose/default lines 16–22; time/all-conditions lines 27–31; general conditions and in-flight warning lines 34–46; method-specific conditions lines 51–58; admin configuration lines 61–72.
   - **Verdict:** PASS.

## Gateway Rejections

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-control-panel]]` → `[[source-braintree-control-panel-gateway-rejections]]` → `[[raw/braintree/articles/control-panel/transactions/gateway-rejections-2026-09-16]]`.

3. **Query:** Where is Braintree Control Panel Gateway Rejections documented?
   - **Object/action match:** Gateway-rule rejection for transactions or verifications, not processor decline.
   - **Direct answer:** The source above links the complete collected Gateway Rejections raw article.
   - **Exact raw locator:** `# Gateway Rejections`, lines 14–41; `## A note on Application Incomplete`, lines 44–46.
   - **Verdict:** PASS; direct provider-index cataloging awaits aggregate close.

4. **Query:** How does a gateway rejection differ from a processor decline, and what happens if authorization preceded rejection?
   - **Object/action match:** Gateway-setting block versus customer-bank block, before-processor versus after-authorization timing.
   - **Direct answer:** This page attributes gateway rejection to gateway settings and decline to the customer's bank. A transaction or verification can be rejected before processor submission or after authorization. If authorized first, Braintree automatically voids the transaction, but a bank may acknowledge the void late or never; the customer may contact their bank about removing the authorization. Rejected requests become `Gateway Rejected` with a reason. This does not imply an immediate disappearance of a pending hold.
   - **Exact raw locator:** rejection/decline note lines 17–18; timing and automatic void line 22; bank acknowledgment lines 25–26; status/reasons lines 30–41.
   - **Verdict:** PASS.

## Bounded gap sweep

- Checked the selected raw links and current source/concept routes for duplicate versus gateway-rejection scope. The separate Declines page is navigation-only and supplies no fact in these answers.
- Both source/raw backlinks and reciprocal concept entries resolve. No wrong-object answer, missing timing warning, broken route or material contradiction found. Group C: **4/4 PASS**.
