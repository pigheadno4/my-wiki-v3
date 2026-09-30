# Braintree C22 ten-page selection review

Status: PREPARED — not approved for execution. Selection is metadata-only.

## Purpose and boundary

Propose ten unowned, already-collected Braintree PayPal pages as retrieval routes: seven payment-method articles and three explicitly JavaScript v3 guide pages. The pinned files total **1,142 file lines** by `wc -l`. Selection checked paths, embedded URLs, SHA-256 hashes, missing source targets and absence of primary source ownership. It did **not** read the raw pages in full or infer capabilities from titles. Workers and initial reviewers must each read their assigned complete raw after exact-manifest approval.

The PayPal overview, setup, processing, funding, disputes, best practices and shared-data articles have different documentation roles; do not merge their authority. Keep JavaScript v3 checkout-with-vault, Pay Later and messaging instructions version-scoped and separate from C21's broad Pay Later Offers and PayPal Credit pages. Preserve material warnings and contradictions; route routine steps, parameters and examples to exact raw locations. The Braintree baseline at preparation is **181 sources** = 165 website + 16 GitHub; recheck it before execution because other repository work may continue. This selection does not decide current product support or merchant eligibility.

## Exact jobs and fixed query questions

`manifest.json` pins each raw path, hash, embedded canonical URL and new source target. Longer pages start earlier so a short page can use a free slot while a longer review continues.

| Job | Lines | Navigation question | Detail question |
| --- | ---: | --- | --- |
| paypal-best-practices | 265 | Where is Braintree's PayPal Best Practices article? | Which practices, conditions and warnings does this article itself state? |
| paypal-disputes | 236 | Where is the Braintree PayPal Disputes article? | What PayPal-specific dispute flow and limitations does this article itself state? |
| paypal-pay-later-offers-javascript-v3 | 145 | Where is the Braintree Pay Later JavaScript v3 guide? | What version-scoped offer setup and presentation boundaries does this page itself state? |
| paypal-setup-guide | 116 | Where is Braintree's PayPal Setup Guide article? | What setup sequence and prerequisites does this article itself state? |
| paypal-checkout-with-vault-javascript-v3 | 95 | Where is the Braintree Checkout with Vault JavaScript v3 guide? | What flow, prerequisites and limitations does this versioned page itself state? |
| paypal-processing | 93 | Where is Braintree's PayPal Processing article? | What processing and lifecycle boundaries does this article itself state? |
| paypal-funding-reconciliation | 59 | Where is Braintree's PayPal Funding and Reconciliation article? | What funding and reconciliation distinctions does this article itself state? |
| paypal-overview | 52 | Where is Braintree's PayPal payment-method overview? | What purpose, availability and scope does this article itself state? |
| paypal-shared-data | 42 | Where is the Braintree Data Shared with PayPal article? | What data-sharing scope and qualifications does this article itself state? |
| paypal-messaging-javascript-v3 | 39 | Where is the Braintree PayPal Messaging JavaScript v3 guide? | What version-scoped messaging setup and presentation boundary does this page itself state? |

## Fixed query groups

A: Best Practices + Overview. B: Disputes + Processing. C: Setup Guide + Checkout with Vault JavaScript v3. D: Funding and Reconciliation + Shared Data. E: Pay Later Offers JavaScript v3 + Messaging JavaScript v3. Two exact questions per page, four per group, **20 total**. For each page, record a complete read, index → concept → source → exact raw route, object/action match, direct answer, exact raw locator and verdict. Make one bounded gap sweep per group. The three `audit_job_ids` are exemplars, not additional audits.

## Approval and execution boundary

- Recheck exact hashes, URLs, source ownership/target absence, C21 closure, baseline count and native-agent capacity before runtime initialization. If another task has changed shared Braintree files, reconcile ownership before dispatch.
- Execution requires separate approval of **this exact C22 manifest**. Then use at most three dynamic child slots, Sol medium workers and different Sol high initial reviewers, per-page approval and at most three attempts; no reviewer waiver.
- The coordinator alone promotes approved concept routes and source candidates, then updates company/index/log/count once at close. Website docs and GitHub implementation evidence remain separate.
- Preparation authorizes no worker dispatch, raw collection, source creation, commit or push.
