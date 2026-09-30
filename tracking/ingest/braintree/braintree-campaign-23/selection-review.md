# Braintree C23 ten-page selection review

Status: PREPARED — not approved for execution. Selection is metadata-only.

## Purpose and boundary

Propose ten unowned, already-collected Braintree Marketplace pages as retrieval routes: four article-level pages and six developer guides, five of those explicitly Node-scoped. The pinned files total **979 file lines** by `wc -l`. Selection checked paths, embedded canonical URLs, SHA-256 hashes, absent source targets and absence of existing `raw_files` ownership. It did **not** read the pages in full or infer capabilities from titles. Each worker and initial reviewer must fully read its assigned pinned raw after exact-manifest approval.

Keep article-level orientation, onboarding, processing and funding separate from developer-guide and Node task authority. Existing escrow and sub-merchant webhook sources provide context but do not establish these unread pages' behavior. Candidate concept routing may warrant a new `braintree-marketplace` concept after the required full-read concept audit; preparation does not create it. Preserve any discovered eligibility, lifecycle, funding, version or cross-page conflict without inferring current product support. The baseline at preparation is **192 Braintree sources** = 175 website + 17 GitHub; recheck before execution because other work may continue.

## Exact jobs and fixed query questions

`manifest.json` pins each raw path, hash, embedded URL and new source target. Longer pages start earlier so shorter work can fill later free slots.

| Job | Lines | Navigation question | Detail question |
| --- | ---: | --- | --- |
| marketplace-guide-onboarding-node | 260 | Where is Braintree's Marketplace Node onboarding guide? | What onboarding sequence, conditions and boundaries does this Node guide itself state? |
| marketplace-guide-testing-go-live-node | 121 | Where is the Marketplace Node testing and go-live guide? | What testing and launch boundaries does this guide itself state? |
| marketplace-guide-update-node | 114 | Where is the Marketplace Node update guide? | What update action, prerequisites and limitations does this guide itself state? |
| marketplace-article-funding | 100 | Where is Braintree's Marketplace funding article? | What funding flow and qualifications does this article itself state? |
| marketplace-article-onboarding | 81 | Where is Braintree's Marketplace onboarding article? | What onboarding roles and conditions does this article itself state? |
| marketplace-article-processing | 71 | Where is Braintree's Marketplace processing article? | What processing flow and limits does this article itself state? |
| marketplace-guide-create-node | 68 | Where is the Marketplace Node create guide? | What create action and prerequisites does this guide itself state? |
| marketplace-guide-confirmation-node | 63 | Where is the Marketplace Node confirmation guide? | What confirmation step and state boundaries does this guide itself state? |
| marketplace-guide-overview | 55 | Where is Braintree's Marketplace developer-guide overview? | What purpose and navigation scope does this developer guide itself state? |
| marketplace-article-overview | 46 | Where is Braintree's Marketplace article overview? | What product orientation and scope does this article itself state? |

## Fixed query groups

A: Article Overview + Guide Overview. B: Article Onboarding + Node Onboarding. C: Node Create + Node Confirmation. D: Article Processing + Node Update. E: Article Funding + Node Testing/Go Live. Two exact questions per page, four per group, **20 total**. For each page, record a complete pinned-raw read, index → concept → source → exact raw route, requested object/action match, direct answer, exact raw locator and verdict. Make one bounded gap sweep per group. The three `audit_job_ids` are exemplars, not an extra audit layer.

## Approval and execution boundary

- Recheck exact hashes, URLs, source ownership and target absence, C22 closure, source-count baseline, shared-file ownership and native-agent capacity before runtime initialization.
- Execution requires separate approval of **this exact C23 manifest**. Then use at most three dynamic child slots, Sol medium workers and different Sol high initial reviewers, per-page approval and at most three attempts; no reviewer waiver.
- The coordinator alone promotes approved concept routes and source candidates, then updates company/index/log/count once at close. Website documents and GitHub implementation evidence remain separate.
- Preparation authorizes no worker dispatch, raw collection, source creation, commit or push.
