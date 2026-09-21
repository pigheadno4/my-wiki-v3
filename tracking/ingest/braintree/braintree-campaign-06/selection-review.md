# Braintree C06 five-page selection plan

Status: exact-manifest execution approved on 2026-09-20; completed 2026-09-20. C01–C05 remain closed.

Goal: extend website retrieval to customer updates, transaction lookup and
subscription lookup/cancellation/events. Keep existing models, runtime, schemas,
three dynamic slots and independent review; no new validation mechanism.
Spec: rules/psp/braintree-ingest.md and C06 dispatch-contract.md.

## Selected pages and fixed query audit

| Job | Lines | Type / provisional concept route | Navigation question | Detail question |
| --- | ---: | --- | --- | --- |
| customer-update-node | 249 | Update guide / braintree-server-sdk | Where is Node customer updating by ID documented? | Where are omitted-attribute behavior, existing versus new payment-method updates, default selection and verification qualifications documented? |
| transaction-find-node | 45 | Lookup API / braintree-server-sdk | Where is Node transaction lookup by ID documented? | What result-limitation notice is stated and where is the Marketplace escrow-status example? |
| subscription-cancel-node | 37 | Lifecycle API / braintree-server-sdk | Where is Node subscription cancellation documented? | What billing effect and result or error guidance does this page state? |
| webhooks-subscription-node | 37 | Event reference / braintree-webhooks | Where are subscription notification kinds and payload routes documented? | Where are event-trigger qualifications and payload-content limits documented? |
| subscription-find-node | 35 | Lookup API / braintree-server-sdk | Where is lookup of a single subscription by ID documented? | Where are callback and Promise invocation forms, result handling and the result-limitation notice documented? |

Total: 403 raw lines including metadata. Exact nested paths and canonical URLs
have no matching current source owner; proposed source targets absent. SHA-256
values pinned in manifest.json. No claim about arbitrary historical aliases.
Selection used headings/opening excerpts, not complete semantic reads. Each worker
and first reviewer must still read its assigned raw completely.

## Boundaries and execution after approval

- [x] Recheck pinned hashes, absent targets and actual agent capacity; initialize
  only braintree/braintree-campaign-06 from the approved manifest.
- [x] Sol medium workers: one complete raw, index-led concept audit, narrow source,
  3–5 located exact quotes and structured shared suggestions; no repository writes.
- [x] Different Sol high first reviewers: retained meaning, warnings, evidence and
  links; bounded corrections reuse original roles with targeted review.
- [x] Coordinator promotes approved concept updates then exact sources serially;
  company/index/log/count aggregate once, preserving unrelated GitHub work.
- [x] One ten-question audit and one mechanical close check; record initial
  first-pass approvals separately from post-audit repairs, and all observed timings.

Preserve customer-update omitted-attribute behavior and existing/new/default
payment-method distinctions. Subscription cancellation is not customer or
payment-method deletion: do not import forfeiture/refund/timing claims. Keep
Marketplace escrow and event-specific qualifications. Preserve both result-limitation
policy notices without interpretation of unread external legal text. Subscription
Find prose omits a method name, but code examples exist: use exact code evidence,
not reconstruction. Concept routes remain provisional until the full-read audit.

## Small operational focus

Fill available slots with ready work before retrospective prose. Reviews have
priority while retaining a worker when queued work remains. Never reserve idle
reviewers or wait for a whole batch. Audit reports use one route per page and
compact question/answer/locator/verdict entries, followed by one completeness check.
Do not shorten required full raw reading. If native dispatch fails, retain the
persisted order, check actual agents, and reuse an eligible idle role only when
its model/independence requirements match; no duplicate dispatch or CLI fallback.
Do not build a thread-management subsystem.

No collection/repair, GitHub ingest, past-campaign refresh, next campaign,
commit or push is authorized by this plan. Preparation is not execution approval.
