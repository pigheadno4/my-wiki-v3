# Braintree C16 ten-page selection review

Status: COMPLETE — exact C16 manifest execution approved and closed 2026-09-23. C15 is
closed and pushed at `4670d34c`. The preparation note below describes the
pre-execution selection, not a claim that workers had read the pages then.

## Purpose and selection boundary

Extend retrieval from C15's response/error references to Braintree's collected
transaction-lifecycle and Control Panel transaction-operation articles. This is
one lifecycle page plus nine pages from the same Control Panel Transactions
folder. The ten pinned raws total **734 logical lines**. The 596-line Declines
article and 297-line Statuses reference remain outside this round so the pilot
does not silently widen its reading/review cost.

Selection used paths, titles, provenance headers and line counts, not full raw
semantic reading. These pages are proposed `source_required` candidates, not
claims that their contents have already been verified. Each worker and initial
reviewer must read its assigned raw completely after separate manifest approval.
The currently collected snapshot date is 2026-09-16; none of its settings or
support claims should be presented as current merely because the raw exists.

## Exact jobs and fixed query questions

Queue order puts the longest and operationally qualified pages early, while
shorter pages can complete in parallel. `manifest.json` pins every path, hash,
canonical URL and absent source target.

| Job | Lines | Navigation question | Detail question |
| --- | ---: | --- | --- |
| control-panel-managing-authorizations | 164 | Where is Braintree Control Panel Managing Authorizations documented? | Which authorization-management options, eligibility and timing boundaries does this Control Panel article document? |
| control-panel-email-receipts | 117 | Where is Braintree Control Panel Email Receipts documented? | Which transaction/refund receipt triggers, configuration and delivery limitations does this article document? |
| control-panel-bank-identification-numbers | 90 | Where is Braintree Control Panel Bank Identification Numbers documented? | Which BIN information and Control Panel lookup/use boundaries does this article document? |
| control-panel-duplicate-checking | 75 | Where is Braintree Duplicate Transaction Checking documented? | What duplicate-transaction matching and configuration boundaries does this article document? |
| control-panel-transaction-create | 62 | Where is Braintree Control Panel Create Transactions documented? | When can a merchant create a transaction in the Control Panel, and what payment-method and settlement limits apply? |
| control-panel-transaction-clone | 60 | Where is Braintree Control Panel Clone Transactions documented? | Which existing transactions can be cloned in the Control Panel, and what is copied versus entered anew? |
| transaction-lifecycle | 48 | Where is Braintree Transaction Lifecycle documented? | How does this page distinguish transaction status stages without equating submission with final settlement or funding? |
| control-panel-gateway-rejections | 47 | Where is Braintree Control Panel Gateway Rejections documented? | How does a gateway rejection differ from a processor decline, and what happens if authorization preceded rejection? |
| control-panel-transaction-issues | 37 | Where is Braintree Control Panel Transaction Issues documented? | How are transaction issues distinguished from declines/rejections, and which notification or investigation routes are documented? |
| control-panel-descriptors | 34 | Where is Braintree Control Panel Descriptors documented? | Which descriptor types and visibility/configuration boundaries does this article document? |

## Fixed query groups

A: Transaction Lifecycle + Managing Authorizations.
B: Control Panel Create + Clone Transactions.
C: Duplicate Transaction Checking + Gateway Rejections.
D: Transaction Issues + Email Receipts.
E: Descriptors + Bank Identification Numbers.

Two exact questions per page, four per group, **20 total**. Record full selected
raw reads, one actual root/provider-index → concept → source → raw route per
page, object/action match, direct answer, exact locator, verdict and one
bounded gap sweep per group. `audit_job_ids` retain the existing three
exemplar IDs; they do not add another three-page audit.

## Approval and execution boundary

- Before execution, recheck all ten hashes/URLs, ownership/target absence,
  C15 completion, the 121-source baseline and actual native-agent capacity.
- With this exact-manifest approval, use the existing three dynamic child slots,
  Sol medium workers, different Sol high first reviewers, maximum three
  attempts and coordinator-only repository writes. No worktrees or schema
  changes. One full raw per worker and reviewer, 3–5 exact located quotes,
  narrow retrieval source, then approved concept/source promotion.
- Distinguish Control Panel actions from server-SDK/API actions; preserve
  authorization, settlement submission, settlement and funding as separate
  stages. Do not import facts from unread Declines, Statuses or other links.
  `Raw Sources` is fully read evidence; `Related raw API references` is
  navigation only. Resolve a discovered relevant conflict with bounded extra
  evidence rather than assuming these articles override prior sources.
- Aggregate company/index/log/count once, run one mechanical close and the
  fixed 20-query audit. Execution approval adds no raw collection, code/rule
  changes, GitHub ingest, commit or push authority.
