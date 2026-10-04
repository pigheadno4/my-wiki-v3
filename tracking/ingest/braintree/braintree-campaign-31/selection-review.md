# Braintree C31 local-payment guides selection

Status: COMPLETE — twenty approved sources, 14/20 first-pass approvals, twenty full plus six targeted reviews, 40/40 fixed queries and 24/24 typed validation passed. Runtime closed 2026-10-04T02:29:40Z; catalog 292 = 275 website + 17 GitHub. C31 is not committed or pushed; C30 remains pushed as b14252f090a6277a075ed19ca611785cc6082a1c.

## Scope and controls

Twenty currently unreferenced canonical website raws from Local Payment Methods: overview, three platform configurations, two native custom-client guides, Node server/testing, three Pay upon Invoice variants, and nine named-method guides. WeChat Pay is deferred to keep this exact scope at 20; this is not a judgment about its content or ingest need.

Baseline 272 sources = 255 website + 17 GitHub; twenty approved new sources would yield 292 = 275 + 17. Primary raw volume 1,827 lines versus C30 2,197: more pages but less primary text, so this is not a controlled capacity/throughput A/B. Preparation uses metadata/ownership/hash checks, not semantic claims from unread raw.

Keep five shared rolling child slots excluding coordinator, across workers/reviewers/auditors, bounded by actual host capacity. Sol medium workers, different Sol high initial reviewers; mandatory complete initial raw reads, 3–5 exact primary-raw quotes, maximum three attempts, bounded targeted corrections and per-page approval. No worktrees, classifier, additional reviewer layer, scheduler/schema/validator change or test-suite rerun.

Manifest longest-first ordering is metadata-based. Short pages may be redirects, unsupported-platform notices, sparse setup or substantial qualification: workers must read completely and summarize only what is actually present. Do not fill missing behavior from siblings or infer current support.

## Pinned pages

| Job | Primary lines | Exact raw path |
| --- | ---: | --- |
| lpm-pay-upon-invoice-javascript-v3 | 313 | raw/braintree/docs/guides/local-payment-methods/pay-upon-invoice/javascript/v3-2026-09-16.md |
| lpm-client-side-custom-android-v5 | 223 | raw/braintree/docs/guides/local-payment-methods/client-side-custom/android/v5-2026-09-16.md |
| lpm-client-side-custom-ios-v7 | 152 | raw/braintree/docs/guides/local-payment-methods/client-side-custom/ios/v7-2026-09-16.md |
| lpm-testing-go-live-node | 135 | raw/braintree/docs/guides/local-payment-methods/testing-go-live/node-2026-09-16.md |
| lpm-bancomatpay | 131 | raw/braintree/docs/guides/local-payment-methods/bancomatpay-2026-09-16.md |
| lpm-server-side-node | 131 | raw/braintree/docs/guides/local-payment-methods/server-side/node-2026-09-16.md |
| lpm-mbway | 130 | raw/braintree/docs/guides/local-payment-methods/mbway-2026-09-16.md |
| lpm-boleto-bancario | 80 | raw/braintree/docs/guides/local-payment-methods/boleto-bancario-2026-09-16.md |
| lpm-trustly | 79 | raw/braintree/docs/guides/local-payment-methods/trustly-2026-09-16.md |
| lpm-multibanco | 77 | raw/braintree/docs/guides/local-payment-methods/multibanco-2026-09-16.md |
| lpm-oxxo | 77 | raw/braintree/docs/guides/local-payment-methods/oxxo-2026-09-16.md |
| lpm-overview | 72 | raw/braintree/docs/guides/local-payment-methods/overview-2026-09-16.md |
| lpm-configuration-android-v5 | 40 | raw/braintree/docs/guides/local-payment-methods/configuration/android/v5-2026-09-16.md |
| lpm-configuration-ios-v7 | 37 | raw/braintree/docs/guides/local-payment-methods/configuration/ios/v7-2026-09-16.md |
| lpm-configuration-javascript-v3 | 32 | raw/braintree/docs/guides/local-payment-methods/configuration/javascript/v3-2026-09-16.md |
| lpm-alipay | 26 | raw/braintree/docs/guides/local-payment-methods/alipay-2026-09-16.md |
| lpm-grabpay | 26 | raw/braintree/docs/guides/local-payment-methods/grabpay-2026-09-16.md |
| lpm-satispay | 26 | raw/braintree/docs/guides/local-payment-methods/satispay-2026-09-16.md |
| lpm-pay-upon-invoice-android-v5 | 21 | raw/braintree/docs/guides/local-payment-methods/pay-upon-invoice/android/v5-2026-09-16.md |
| lpm-pay-upon-invoice-ios-v7 | 19 | raw/braintree/docs/guides/local-payment-methods/pay-upon-invoice/ios/v7-2026-09-16.md |

## Fixed query coverage

For each of the 20 pages, ask two questions (40 total):
1. Where is the exact named method/document type/platform/version route? Follow root index → provider index → relevant concept/source → pinned raw. Website guides are not exact-SHA package evidence.
2. Answer the page-type question below from fully read evidence, preserving stated qualifications and recording when requested behavior is absent. Do not import sibling behavior to fill a sparse page.

- Overview: What principal local-payment flow or applicability boundary is stated?
- Configuration: What platform-specific configuration responsibility and consequential prerequisite/warning is stated?
- Native custom client: What client responsibility/server handoff and consequential prerequisite or outcome boundary is stated?
- Node server: What server-side responsibility or transition and consequential qualification is stated?
- Testing/go-live: What test-to-production boundary and consequential warning is stated? Routine fixtures remain raw locators.
- Pay upon Invoice variants: What central named-method/platform behavior or explicit absence/redirect is actually documented, and what material prerequisite/qualification applies?
- Named-method page: What method-specific flow or applicability restriction is stated? If it is only a redirect or unavailable notice, report that rather than fabricating an integration procedure.

Disjoint groups: A overview + configuration-javascript-v3; B configuration-android-v5 + configuration-ios-v7; C client-side-custom-android-v5 + client-side-custom-ios-v7; D server-side-node + testing-go-live-node; E pay-upon-invoice-javascript-v3 + pay-upon-invoice-android-v5; F pay-upon-invoice-ios-v7 + alipay; G bancomatpay + mbway; H boleto-bancario + oxxo; I multibanco + trustly; J grabpay + satispay. All IDs use the lpm- prefix. Each group has 4 questions; ten groups share the same five-slot budget, overlapping ready promotions. Three manifest audit IDs are exemplars, not another audit layer.

## Short provider and prevention notes

Coordinator reads CLAUDE.md, ingest.md, Braintree authorization and adopted Metronome retrieval contract. Delegated workers/reviewers read ingest-roles.md, trusted input.json and these concise notes.

Start root index → braintree-index → braintree-payment-methods; relevant supporting routes may include web/Android/iOS/server SDK, webhooks and payment-platform concepts. Existing article owner source-braintree-payment-methods-local-payment-methods is not replaced by the developer-guide overview. Method/platform guides retain separate source ownership. Add a new concept only for a genuine topic gap found during full-read concept audit; no advance assumption that every named method needs one.

Preserve exact method, platform/version, client/server, merchant/customer, currency, instant/non-instant, sandbox/production and snapshot scope as stated. Nonce/token, initiation, authorization, completion notification, settlement, funding and reversals are not interchangeable. Investigate actual conflicts without trying to reconcile unsupported/current claims; do not assume uniform applicability across local methods.

C30 prevention changes are short dispatch instructions, not new infrastructure:
- Resolve every required raw navigation against an existing dated file. The manifest table supplies exact selected targets; find other collected targets explicitly. Generic directory links are not valid file routes.
- This runtime verifies the 3–5 quote slots against the primary pinned raw only. Supporting factual authorities must be fully read, listed in raw_files and Raw Sources, with exact locators in the source; do not put supporting-only quotations in primary quote slots.
- Concept descriptions default to document type/version plus purpose. Avoid attributing all mixed-page behavior to one named product or platform. Use exact heading anchors and unique update IDs.
- Fully read evidence belongs to Raw Sources; unread navigation belongs to Related raw API references. Never add backlinks to raw; reverse lookup derives from raw_files.

## Close and timing

Immediately dispatch persisted orders; fill eligible freed slots before report/promotion narrative, review-first with existing worker reserve and targeted retry priority. Coordinator serially promotes reviewer-approved concept changes then exact candidate. Aggregate company/index/log/count once; no default third full coordinator read.

One campaign-wide close covers all 20 candidates/hashes/provenance/approved updates/reciprocal links, exhaustive unique catalogs and recursive counts, touched typed-page validation and scoped whitespace. Ten compact fixed query groups give actual answers/routes/locators/verdicts and shared gap findings once per group; no report polishing or added semantic audit.

Compare runtime, time per approved page, first-pass rate, targeted/full retries, primary lines and source words with C30. Track explicit observed stage milestones and distinguish overlap/post-close reporting; add no timing fields. More pages should amortize shared close work, but do not promise shorter total runtime.

## Preparation checks

Twenty unique paths, URLs, job IDs and source targets; pinned hashes match; primary raws and canonical URLs currently have no source owner, targets absent, baseline recursive count 272. Configuration passes existing review/routing schema checks. No campaign.json/jobs.json/attempts/monitor created and no model tasks dispatched. Recheck before separately approved execution. No collection, GitHub ingestion, commit/push of this preparation or next-campaign execution.
