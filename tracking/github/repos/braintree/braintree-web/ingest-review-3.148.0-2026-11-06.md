# Braintree Web 3.148.0 Ingest Review

## Authorization and Identity

- User approved the recommended delta ingestion with focused reading, preserving all earlier history. Collection, ingestion and publication remain separate gates. No commit/push is authorized by this approval.
- Work item `github-b0a5af655a25673da0cb`: `braintree-web@3.147.0` -> `braintree-web@3.148.0`; current exact SHA `0b989560481a1274a8fda27e426f6297d3bde552`, prior SHA `f3357c49c7b71f079d031c3ddf89cdfe444f6511`.
- Notes label 2026-11-02; GitHub publication is 2026-11-04T17:26:41Z; collection 2026-11-05; ingest 2026-11-06. The raw dates remain unchanged.
- Packet: `ingest-packets/github-b0a5af655a25673da0cb/packet.json`; comparison: `comparisons/braintree-web/3.147.0--3.148.0/comparison.json`. Original packet and raw evidence were not modified.

## Completed Sequence

- [x] Read the complete cumulative source/changelog, release record/notes and comparison; review changed source/content sections and affected prior code under the approved focus exception. Fully read the Instant Verification implementation/constants, public v6 entry, package manifest, shared story helper, edit story and retained FrameService dependency. Unchanged ranges/files, historical raw changelog and generated inventories were checked mechanically, not represented as complete semantic full-file reads.
- [x] Verify all 666 prior/current file sizes, SHA-256 and Git blob IDs; packet Markdown/snapshot, release-note and comparison Markdown/patch digests. Snapshot: 333 files / 2,239,903 bytes; 20 modified, 313 unchanged, none added/removed. Reconcile all 23 upstream dispositions: 20 retained plus lockfile/two test exclusions; zero packet gaps/unclassified changes.
- [x] Extract five exact located quotes before wiki edits: public `shopperSessionId` JSDoc line 21; SDK identity getter line 46; ID forwarding line 669; teardown Promise.all line 4269; Instant Verification shim line 20. All five later checked against the exact raw lines.
- [x] Audit existing concepts; update `braintree-web-sdk` and `paypal-braintree-integration` first. Existing modular SDK coverage suffices for Instant Verification; no new concept or cross-company comparison needed.
- [x] Add version-qualified source/changelog findings, then company/catalog/log entries. Preserve all earlier implementation sections and the complete prior release-ledger tail; source_count remains 797. No source/catalog duplicates.
- [x] Check contradictions: qualify release-note propagation against shared SDK-identity state and cached-instance branches; retain the earlier locale discrepancy. Distinguish dependency pins from uncollected dependency implementation, nonce/analytics from payment results, and notes/publication/collection/ingestion dates.
- [x] Validate six structured wiki pages, separate frontmatter-free index/root-log links and placeholders, Markdown evidence links/line anchors, five verbatim quotes, old-history preservation and whitespace. Work item advanced serially through approved -> ingesting -> ingested; generated state accepts 3.148.0 and next scheduled check is 2026-11-12.

## Findings

1. PayPal v6 teardown now invokes FrameService cleanup after awaiting the client and currently assigned frame-service promise. Rejected prerequisites bypass cleanup. Source inspection also identifies early authorization-only teardown capturing an undefined frame-service promise before client resolution assigns it; do not claim race-free deferred cleanup, complete hosted-resource destruction or safe repeated teardown.
2. Optional shopper-session metadata can reach newly created delegated SDK instances. Its map is shared across wrappers and tied to exact `window.paypal` identity: SDK loading/replacement can invalidate a previously recorded ID, another wrapper can overwrite it, and existing/in-flight instance branches do not update it. It is not authenticated buyer/payment-token context. No independent PayPal JS/React update is inferred.
3. Instant Verification strips only the exact trailing literal `?customer_id=` from string authorization fingerprints before redirect `at`; nonstrings and nonmatching suffixes stay unchanged. No general query normalization or JWT validation is established.
4. Direct `credit-card-type` pin changes 10.2.0 -> 10.3.1; dependency internals are outside this capsule.
5. Fourteen Storybook files add teardown controls; saved-payment cleanup covers both the vaulting wrapper and edit wrapper. The sample changes do not introduce returning-buyer support for the first time.

## Verification Boundaries

- Helper-only Node VM checks: two SDK-identity/overwrite cases and six fingerprint input cases pass. Only extracted helpers and a stub window were executed; no SDK imports, browser, hosted runtime, network or payment calls. The early-teardown boundary is source analysis, not a hosted reproduction.
- `validate_wiki.py` passes for all six structured touched pages. Passing index/root log directly to it reports their two pre-existing missing-frontmatter conventions; its normal whole-wiki route excludes these files. Separate checks verify their wikilinks/placeholders and unchanged formatting convention rather than adding unrelated metadata.
- Offline GitHub validation has 13 pre-existing unrelated structural errors: six historical packet budget failures and their invalid-packet consequences, plus the Adyen PHP 30.1.0 ledger omission. No change to those rules, budgets, packets or unrelated wiki knowledge is part of this ingest.
- Final post-completion run confirms exactly those same 13 errors, none for this repository/item, and zero pending work items. Six structured pages pass again after the final wording review; scoped whitespace check passes.
- No code/rules/registry change, new unit-suite run, upstream install/build/test, hosted checkout or payment execution. Other sessions' dirty files and shared-log work remain untouched.

## Publication Authorization

On 2026-11-06 the user separately approved the scoped commit/push after the ingestion findings. Use an isolated Git index with only this collection/ingest and its generated tracking refresh. Stage the root log from HEAD plus this ingest entry, excluding unrelated reorderings/BYD work and the separate Adyen campaign. Date-derived due-action changes in the generated index do not represent new collections.

Next after publication: verify the exact remote SHA, then choose the next repository recheck separately; do not start collection or ingestion automatically.
