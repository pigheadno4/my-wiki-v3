# Braintree C20 ten-page selection review

Status: COMPLETE — the exact manifest was approved and the campaign closed on
2026-09-27. The selection below was metadata-only before execution.

## Purpose and boundary

Extend website retrieval to eight unowned fraud-tool guides and two unowned
Control Panel security guides. These ten pinned raw files total **1,060 file
lines** by `wc -l`. Selection used paths, embedded source URLs, SHA-256 hashes,
source-target absence and absence of primary source ownership only. Titles and
URLs do not prove product capabilities. Assigned workers and initial reviewers
must read their entire raw page after exact-manifest approval.

Keep basic checks, 3D Secure, named premium fraud products and chargeback tools
separate. Control Panel login/key security is not a payment fraud tool. Do not
generalize approval, protection or liability from a navigation page or sibling
product. Sources should route to immutable raw and retain material warnings;
procedural detail remains in raw. The 2026-09-16 collection date is not proof
of current behavior.

## Exact jobs and fixed query questions

`manifest.json` pins each raw path, SHA-256, embedded canonical URL and proposed
source target. Longer and cross-boundary pages start earlier.

| Job | Lines | Navigation question | Detail question |
| --- | ---: | --- | --- |
| control-panel-security-two-factor-authentication | 165 | Where is Braintree Control Panel two-factor authentication documented? | Which access, setup and recovery boundaries does this page itself document? |
| fraud-tools-basic-risk-threshold-rules | 164 | Where are Braintree risk-threshold rules documented? | Which configuration, scoring or decision boundaries does the collected page describe? |
| fraud-tools-premium-fraud-protection-advanced | 141 | Where is Fraud Protection Advanced documented? | What purpose, setup, outcome and eligibility boundaries does this page itself state? |
| fraud-tools-premium-kount-custom | 125 | Where is Kount Custom documented? | Which integration and decision responsibilities does this page assign, with what limits? |
| fraud-tools-basic-avs-cvv-rules | 113 | Where are AVS and CVV rules documented? | What checks, rule settings and result boundaries does this page itself document? |
| fraud-tools-3d-secure | 98 | Where is Braintree 3D Secure documented? | What authentication purpose, integration route and limits does this page itself explain? |
| fraud-tools-premium-chargeback-protection | 98 | Where are chargeback protection tools documented? | Which named tools, eligibility conditions and protection limits does this page itself state? |
| fraud-tools-premium-effortless-chargeback-protection | 71 | Where is Effortless Chargeback Protection documented? | What purpose, eligibility and limits does this specific page state? |
| fraud-tools-premium-fraud-protection | 49 | Where is Fraud Protection documented? | What scope and qualifications does this page state, distinct from Advanced? |
| control-panel-security-rotating-api-keys | 36 | Where is Braintree API-key rotation documented? | Which rotation triggers and access boundaries does this page itself state? |

## Fixed query groups

A: Two-Factor Authentication + Rotating API Keys.
B: Risk Threshold Rules + AVS/CVV Rules.
C: Fraud Protection Advanced + Fraud Protection.
D: Kount Custom + 3D Secure.
E: Chargeback Protection Tools + Effortless Chargeback Protection.

Two exact questions per page, four per group, **20 total**. For each page,
record a complete read, root/provider-index → concept → source → raw route,
object/action match, direct answer, exact raw locator and verdict. Make one
bounded gap sweep per group. The three `audit_job_ids` are exemplars, not
additional audits.

## Approval and execution boundary

- Recheck all hashes/URLs, source ownership and target absence, C19 closure,
  the 161-source baseline (145 website + 16 GitHub), and native-agent capacity
  immediately before execution.
- Only after approval of this exact manifest, use the existing three dynamic
  child slots, Sol medium workers and different Sol high initial reviewers,
  at most three attempts, and coordinator-only repository writes.
- Promote approved concept routes before sources; update the company page,
  provider index/log and counts once at close. Website docs remain distinct
  from GitHub implementation evidence.
- This exact manifest was separately approved before runtime initialization.
  C20 execution does not authorize new collection, commit, push or C21.
