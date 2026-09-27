# Braintree C17 ten-page selection review

Status: COMPLETE — exact manifest execution approved 2026-09-26 and closed 2026-09-27. The selection
below was metadata-only before execution. C16 was closed and pushed at `107bf1ab`.

## Purpose and boundary

Extend retrieval from C16 transaction operations into Control Panel reporting
and notification administration: all eight collected pages in the Reporting
folder, plus Webhooks and Audit Webhooks. The ten pinned raws total **666
logical lines**. They are proposed `source_required` candidates, not claims
that their contents have been semantically verified. Selection used only
paths, titles, provenance headers, hashes, existing source ownership and line
counts. Each worker and initial reviewer must read its assigned raw in full
after a separate approval. The 596-line Declines article remains outside this
round. The 2026-09-16 collection date is not proof of current product, beta,
tax, fee or reporting behavior.

The batch keeps two easily confused domains separate: a Control Panel report
is not necessarily a settlement/funding ledger or an API response, and an
Audit Webhook is not automatically equivalent to a transaction notification.
Preserve bank/processor, date, permission, beta and merchant-eligibility
qualifications that the selected pages actually contain; do not assume them
from titles. Routine fields, tables and report steps should remain in raw with
verified locators unless needed to prevent a misleading retrieval answer.

## Exact jobs and fixed query questions

Queue order starts the longest or cross-boundary pages early; it does not
prejudge their facts. `manifest.json` pins each raw path, SHA-256, canonical
URL and absent source target.

| Job | Lines | Navigation question | Detail question |
| --- | ---: | --- | --- |
| control-panel-audit-webhooks | 121 | Where is Braintree Control Panel Audit Webhooks documented? | Which audit-webhook events, permissions and setup/delivery boundaries does this collected article document? |
| control-panel-reporting-transaction-level-fee-report | 106 | Where is Braintree Transaction-Level Fee Report documented? | What fee-report purpose, access/availability, timing and reconciliation boundaries does this page document? |
| control-panel-reporting-overview | 73 | Where is Braintree Control Panel Reporting Overview documented? | Which reporting categories and Dashboard-versus-reconciliation boundaries, if any, does this overview establish? |
| control-panel-reporting-settlement-batch-summary | 73 | Where is Braintree Control Panel Settlement Batch Summary documented? | What does this settlement-batch report represent, and which date, status or funding boundaries does the page state? |
| control-panel-webhooks | 69 | Where is Braintree Control Panel Webhooks documented? | Which Control Panel webhook configuration, permission and notification boundaries does the page document? |
| control-panel-reporting-decline-analysis | 63 | Where is Braintree Decline Analysis report documented? | Which decline-analysis views and limits does this page state, without importing retry rules? |
| control-panel-reporting-1099-k | 55 | Where is Braintree Control Panel 1099-K reporting documented? | Which form-availability, eligibility and reporting qualifications does the collected page state? |
| control-panel-reporting-transaction-summary | 37 | Where is Braintree Control Panel Transaction Summary documented? | Which summary measures, filters or timing boundaries does this page actually document? |
| control-panel-reporting-grant-api-report | 35 | Where is Braintree Grant API Report (Beta) documented? | What does this beta report cover, and which availability or visibility limits are explicit? |
| control-panel-reporting-expiring-cards | 34 | Where is Braintree Expiring and Expired Cards report documented? | What can this report identify, and what update or action does it not itself establish? |

## Fixed query groups

A: Reporting Overview + Transaction Summary.
B: Settlement Batch Summary + Transaction-Level Fee Report.
C: Decline Analysis + Expiring and Expired Cards.
D: 1099-K + Grant API Report (Beta).
E: Control Panel Webhooks + Audit Webhooks.

Two exact questions per page, four per group, **20 total**. For each selected
raw, record a complete read, an actual root/provider-index → concept → source
→ raw route, object/action match, direct answer, exact raw locator and verdict;
perform one bounded gap sweep per group. The three `audit_job_ids` are
exemplars inside these groups, not an extra audit.

## Approval and execution boundary

- Before execution, recheck ten hashes and URLs, source/URL ownership and
  target absence, C16 completion, the 131-source baseline (115 website + 16
  GitHub), and actual native-agent capacity.
- If this exact manifest is approved, use the established three dynamic child
  slots, Sol medium workers, different Sol high first reviewers, maximum three
  attempts, coordinator-only repository writes, per-page approval and bounded
  targeted corrections. No worktrees or schema changes.
- Promote approved concept routes before their corresponding sources; update
  company, provider index, provider log and source count once at close. Keep
  website documentation and GitHub implementation evidence separate.
- Preparation authorizes no ingestion, raw collection, code/rule changes,
  commit or push for C17. Execution requires explicit approval of this exact
  manifest.
