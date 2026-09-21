# Braintree C03 five-page selection plan

Status: COMPLETE on 2026-09-19; exact-manifest execution approved. C01 and C02 remain closed.

Goal: extend retrieval coverage to five un-ingested website raws without changing
models, review policy, schemas or validators. Use existing campaign runtime and
provider capsule; no code implementation, GitHub ingestion, collection, commit or push.
Spec: rules/psp/braintree-ingest.md and C03 dispatch-contract.md.

## Selected pages and fixed audit questions

| Job | Lines | Type / likely concept route | Navigation question | Detail question |
| --- | ---: | --- | --- | --- |
| transaction-submit-for-settlement-node | 166 | API / braintree-server-sdk | Where is explicit Node transaction submission for settlement documented? | Where are settlement-amount adjustments, availability qualifications and supplemental-data examples documented? |
| authorization-overview | 66 | Capability comparison / braintree-web-sdk | Where can I compare client tokens and tokenization keys for client authorization? | Where are capability differences and selection guidance documented? |
| client-token-generate-node | 54 | API / braintree-server-sdk | Where is Node client-token generation documented? | Where is the customer-ID variant documented, and what qualifications does this page state? |
| transaction-void-node | 32 | Lifecycle API / braintree-server-sdk | Where is the Node transaction-void operation documented? | Which eligible states and authorization-reversal qualification does the page state? |
| authorization-client-token | 23 | Concept / braintree-web-sdk | Where is a client token and its server-to-client role explained? | What validity or reuse qualifications does this guide state? |

Total: 341 raw lines including metadata. All exact nested raw paths and canonical
URLs currently lack a matching source owner; proposed source targets are absent.
Hashes are pinned in manifest.json. This excludes exact current ownership, not
arbitrary historical aliases. Selection uses metadata/headings/opening excerpts,
not a substitute for workers' and initial reviewers' full reads.

## Execution steps after approval

- [x] Recheck pinned hashes, absent targets and actual agent capacity; initialize
  only braintree/braintree-campaign-03 from this manifest.
- [x] Dispatch longest-first within the three dynamic slots; each worker handles
  one raw end-to-end, index-led concept audit, 3–5 quotes and one isolated candidate.
- [x] Different Sol high reviewers approve each candidate and shared suggestion;
  bounded same-evidence corrections reuse the original worker/reviewer.
- [x] Coordinator serially applies approved concepts then exact source candidates.
  Aggregate company/index/log/count once, preserving unrelated work.
- [x] Run the ten fixed questions once and one aggregate mechanical close check;
  record results and stage timings in existing campaign artifacts.

## Small operational focus

Fill eligible slots before promotion or retrospective prose. Keep role handoffs
and final audit reports compact, while retaining required evidence and qualifications.
Use the existing subject/condition/action drafting check for source AND concepts;
no new checklist, registry, monitoring fields or additional audit round.
Report first-pass count, targeted/full retries, query misses and stage durations.
Do not promise a speedup from a five-page sample with a different content mix.
Concept routes above are provisional until the complete-read concept audit;
create a concept only for a genuine uncovered topic.
