# Braintree C10 ten-page execution plan

Status: COMPLETE; exact-manifest execution approved on 2026-09-21.
C01–C09 remain closed. User requested considering expansion from five to ten;
this proposal changes campaign size and fixed query count, not concurrency or gates.

**Goal:** Test ten-page campaign overhead amortization on previously unowned website raws.
**Architecture:** Existing Sol medium workers, different Sol high reviewers, three dynamic child slots including auditors; coordinator-only repository writes.
**Tech Stack:** Existing Python runtime, native agents, Markdown/JSON; no code changes.
**Spec:** rules/psp/braintree-ingest.md, adopted metronome-ingest.md and C10 dispatch-contract.md.

## Exact selection and query questions

| Job | Logical lines | Navigation question | Detail question |
| --- | ---: | --- | --- |
| payment-method-create-node | 209 | Where is Node payment-method creation for an existing customer documented? | What prerequisites and payment-type qualifications are stated, and where are duplicate prevention, verification and nonce/raw-data rules? |
| payment-method-update-node | 239 | Where is Node updating of a stored payment method documented? | Where are billing-address, PayPal-token, default-selection and verification qualifications; what omission or nonce behavior is explicitly stated? |
| subscription-search-node | 193 | Where is searching subscriptions using Node documented? | How are results consumed and filters located, and what result-limitation notice must be retained? |
| subscription-retry-charge-node | 79 | Where is manually retrying a past-due subscription charge documented? | What amount, result and settlement behavior do the displayed examples and qualifications establish? |
| payment-method-grant-node | 38 | Where is granting a payment method using Node documented? | What availability restriction, participating identities and scope are explicitly established? |
| payment-method-revoke-node | 30 | Where is revoking a payment-method grant documented? | What access limitation and revocation effect or result guidance does this page state, distinct from deleting a payment method? |
| webhooks-transaction-node | 44 | Where are Node transaction webhook kinds documented? | What payment-method availability and event/payload qualifications are stated, and which rendered details remain missing? |
| webhooks-account-updater-node | 36 | Where is the Account Updater notification reference? | Which merchants can receive it, and where are the trigger and payload attributes documented? |
| webhooks-fraud-protection-node | 31 | Where are Fraud Protection webhook notifications documented? | What event conditions and payload scope does this page establish without inferring universal fraud coverage? |
| address-find-node | 21 | Where is Node lookup of a customer address documented? | What identifiers and callback arguments are shown, and what response details are not supplied by this page? |

Total 920 logical raw lines. Selection used headings/opening excerpts and metadata,
not complete semantic reading. Exact raw paths and canonical URLs have no current
source owner across wiki/sources; all source targets absent. Pinned hashes, URLs
and targets are in manifest.json. No claim about historical alias equivalence.

Provisional main routes: braintree-server-sdk for request pages, braintree-webhooks
for notifications. Each full-read concept audit may refine routes or identify a
real gap; no new concept by default. Preserve payment-type and limited-release
scope. The transaction webhook opening has damaged rendering: do not reconstruct
missing operations. Check actual conflicts with existing webhook scope rather than
silently normalize them; full-read related authority only when needed.

## Execution checklist after approval

- [x] Recheck all hashes, absent targets and canonical/raw owners; confirm C09 closed and current capacity. Initialize only braintree/braintree-campaign-10; record actual UTC start.
- [x] Persist each trusted order before dispatch. Each worker fully reads one raw, audits concepts index-first and returns one narrow source, 3–5 exact located quotes and supported suggestions. Status candidate_ready, no extra result keys, no repository edits.
- [x] Different Sol high reviewer fully reads each initial candidate's evidence. Review retained truth, consequential warnings and routes, not optional parameter inventories. Maximum three attempts; bounded targeted corrections where justified, no reviewer waiver.
- [x] Serially promote approved concept suggestions then exact sources. Dispatch each ready two-page audit group before aggregate/report work, subject to actual slots and existing review/worker priority. No batch barrier; auditors share the same three-slot cap.
- [x] Aggregate company/index/log/count once. Baseline61 =45 website+16 GitHub; expected71 =55+16 if all ten approve and no concurrent source changes. Recalculate actual count.
- [x] Run the single20-question audit and one campaign-wide mechanical close: exact candidates, hashes/canonical identities, ownership, required/reciprocal links, approved snippets, duplicate catalogs, counts and touched typed pages. No additional three-page audit or documentation-only unit suite.
- [x] Close runtime and write quality-audit.md/retrospective.md with observed timings, first handoff/content-review rates and retries/repairs. Record elapsed per accepted page alongside total wall time using existing timestamps; no new telemetry fields or token estimates.

## Five fixed query groups

A: Payment Method Create + Update (4 questions).
B: Subscription Search + Retry Charge (4 questions).
C: Payment Method Grant + Revoke (4 questions).
D: Transaction Webhooks + Account Updater Webhooks (4 questions).
E: Fraud Protection Webhooks + Address Find (4 questions).

Together these are one20-question audit, not five extra audits. Three manifest
exemplar IDs remain for runtime compatibility; do not run an additional sample.
No more auditors than ready groups or available slots. Record one route/page,
compact answers and one shared gap-sweep/completeness check per group.

## Files, success criteria and boundaries

Create the ten exact manifest source targets and existing runtime/attempt/audit/
retrospective artifacts here. Shared writes: approved concept sections,
wiki/braintree-index.md, wiki/braintree-log.md, wiki/companies/braintree.md.
No shared file writes by workers. Preserve unrelated GitHub work.

Expansion is successful if all promoted pages retain evidence/links and the larger
campaign needs no additional coordination mechanism. Compare first-pass rate and
per-page elapsed time, but page mixes differ: no causal speed claim or promise that
ten pages finish in the same12–13 minutes. Failed jobs follow existing retry/reject
rules; do not silently widen scope or keep retrying beyond three attempts.

No raw edits, collection, GitHub ingest, historical refresh, runtime/rule changes,
new registry/scheduler/classifier, worktrees, commit/push or automatic next campaign.
Execution was separately approved; campaign completed2026-09-21T11:42:03Z.
