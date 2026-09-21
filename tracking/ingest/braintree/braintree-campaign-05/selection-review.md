# Braintree C05 five-page selection plan

Status: COMPLETE on 2026-09-20; exact-manifest execution approved. C01–C04 remain closed.

Goal: add five website retrieval entries for Customer and stored Payment Method
operations using the existing runtime and review policy. No new framework,
validator, registry, reviewer tier or default expansion into neighboring raws.
Spec: rules/psp/braintree-ingest.md and C05 dispatch-contract.md.

## Selected pages and fixed query audit

| Job | Lines | Type / provisional concept route | Navigation question | Detail question |
| --- | ---: | --- | --- | --- |
| customer-create-node | 252 | Creation guide / braintree-server-sdk | Where is Node customer creation, with or without a payment method, documented? | Where are customer-ID, billing-address, card-verification and custom-field variants documented, and what evidence gaps must be retained? |
| payment-method-find-node | 43 | Lookup API / braintree-server-sdk | Where is lookup of a stored payment method by token documented? | What result-limitation notice is stated and where is the PayPal-account example? |
| webhooks-payment-method-node | 29 | Event reference / braintree-webhooks | Where are payment-method revocation notifications and their payload routes documented? | Which triggers and payment-method scope does this page state? |
| customer-delete-node | 22 | Destructive API / braintree-server-sdk | Where is Node customer deletion by ID documented? | What effects on associated payment methods and subscriptions does the page state? |
| customer-find-node | 20 | Thin incomplete reference / braintree-server-sdk | Where is lookup of a single customer by ID documented? | Does the collected page contain a usable Node invocation example, and what evidence is missing? |

Total: 366 raw lines including metadata. All five nested paths and canonical
URLs have no exact current wiki source owner/match; proposed targets are absent.
Hashes are pinned in manifest.json. No claim about arbitrary historical aliases.
Selection used headings/opening excerpts; short Customer Find/Delete fitted in
those excerpts. Workers and initial reviewers still read every assigned raw fully.

## Known evidence limits

- Customer Find contains a missing-code placeholder instead of an invocation.
  Source should expose that absence as an evidence limitation, not reproduce a
  fake example or infer an SDK signature. Ground its limited purpose, ID input
  and missing-example observation with exact short excerpts; no invented filler.
- Customer Create's opening note omits action/option names. Do not reconstruct it.
- Payment Method Find links a policy limiting results. Preserve the notice;
  unread external legal text is not authority for added legal interpretation.
- Revocation notifications have concrete payment-method/trigger scope. Deletion
  has consequential cascade effects. Preserve both and retain advisory modals
  such as should/may in source AND concept proposals.

## Execution after exact-manifest approval

- [x] Recheck hashes, absent targets and agent capacity; initialize only
  braintree/braintree-campaign-05 using the approved manifest.
- [x] Sol medium workers, one complete raw per candidate, index-led concept audit,
  3–5 exact located quotes and structured shared suggestions; read-only repository.
- [x] Different Sol high reviewers approve each candidate and concept proposal;
  original roles handle bounded same-evidence corrections through targeted review.
- [x] Coordinator serially applies approved concepts then sources, aggregating
  company/index/log/count once and preserving other sessions' GitHub work.
- [x] Run the ten questions once and one aggregate mechanical close check;
  retain timings, first-pass rate, corrections and post-audit repairs separately.

## Operational focus

Use three dynamic child slots, ready-review priority with an active-worker
reserve when work remains. Fill eligible slots before promotion/report prose.
No batch barrier; compact audit reports without reducing evidence checks.
Candidate scope is retrieval, not full API specification; details get verified
raw locators. Relevant actual conflicts require investigation, not automatic
full reading of every neighboring page. Concept routes are provisional until
full-read audit; add a concept only for a genuine uncovered topic.
C05 has more raw lines than C04; do not promise faster closure from the workload.

No collection repair/retry, GitHub ingest, C01–C04 refresh, historical migration,
next campaign, commit or push is authorized by preparation or execution here.
