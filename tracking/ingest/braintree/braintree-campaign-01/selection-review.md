# Braintree C01 selection and preparation

Status: COMPLETE on 2026-09-19; all five sources approved and promoted, final
query audit 10/10 PASS. See monitor.md, quality-audit.md and retrospective.md.
Preparation approved on 2026-09-19. This is a website-doc pilot, not GitHub ingest.

## Exact sample and predetermined audit

| Job | Raw lines | Navigation question | Detail question |
| --- | ---: | --- | --- |
| transaction-sale-node | 512 | Where do I find the Node operation for creating a transaction? | What payment-source alternatives are documented, and how does the example request immediate submission for settlement? |
| get-started | 134 | Where can I find the initial Braintree integration flow and prerequisites? | Where are client/server responsibilities and the checkout sequence documented, and what does each side do? |
| webhooks-overview | 63 | Where do I start when integrating Braintree webhook notifications? | What does this overview state about user permissions and volume, and where are those qualifications documented? |
| control-panel-overview | 49 | Where can I learn the role of the Braintree Control Panel? | What environment distinctions are documented, and where can I find the dashboard information? |
| credit-cards-client-javascript-v3 | 23 | Which client-side credit-card integration guidance applies to JavaScript v3? | Does JavaScript v3 support Card Fields, and which alternative does this page direct developers to? |

781 raw lines total. Counts include collection comments and upstream metadata;
they are workload metadata, not a substitute for full worker/reviewer reads.
The short JavaScript page is deliberate: short length does not mean low semantic
risk. Do not replace it or relax quote grounding merely to favor a throughput metric.

## Preflight evidence

- All five raw files exist, with hashes pinned in manifest.json; exact Source
  URL comments match the manifest canonical URLs.
- All five source targets are new. A current `wiki/sources/**/*.md` scan found
  neither their exact nested raw paths nor exact canonical URL tokens (trailing
  slash normalized). This establishes no detected owner in this checkout,
  not proof against every possible historical alias or other worktree.
- Existing Braintree index/log/company pages and SDK concepts are reused.
  Candidate concept routes include braintree-server-sdk and braintree-web-sdk;
  webhooks/control-panel topic gaps are decided from full reads and the concept
  audit, not invented from metadata. No GitHub page is replaced.
- The 90 failed collection targets are outside this sample and remain a
  separate collection issue. No failed or unvalidated response becomes evidence.

## Runtime compatibility

Resolved on 2026-09-19: manifest.provider now selects the state directory, and
all coordinator attempt paths use the same campaign path resolver. For this
campaign use `--campaign braintree/braintree-campaign-01`. Unqualified selectors
and manifests without provider retain the Metronome default. Stored campaign IDs
remain unqualified; no result/state schema or registry is added.

Tests exercise identical campaign IDs independently under Metronome, Braintree,
Stripe, Adyen and PayPal, including dispatch, interruption, retry, candidate
acceptance, independent review and closure. This is runtime compatibility, not
provider-specific semantic validation or authorization for those other PSPs.
The live C01 campaign has not been initialized by these temporary-fixture tests.

Verification on 2026-09-19: 147 ingestion/runtime tests passed, including the
provider-isolation fixtures. The exact C01 manifest initialized successfully in
a temporary root and all five live raw hashes still match. `git diff --check`
passed. Full repository discovery ran 784 tests with two errors in
`test_collect_github_repos`: `test_next_ingest_claims_oldest_approved_item` and
`test_status_approval_and_next_ingest_include_attachment_required_reading` both
reach a missing temporary `tracking/github/repo-registry.toml`. No GitHub code
was changed to address these out-of-scope failures; the full suite is not green.

## Execution and measurement

After approval and runtime readiness: dispatch trusted per-page orders; fill
the three dynamic slots; review first attempts independently; apply approved
concept routes before each exact source candidate; aggregate shared catalogs
once. Run the ten questions above as the single final retrieval audit, then
one campaign-wide mechanical close check. No extra full-content audit.

Record worker, review, correction, waiting/handoff, promotion/shared close,
query audit and mechanical validation times in existing campaign artifacts.
Distinguish overlapping role durations from end-to-end wall time. Report first
pass count, full/targeted retries and retrieval misses. C46's 21m18s and 5/5
first-pass rate are context only: its 8,760 raw lines differ from this sample,
so a faster C01 does not establish a causal or corpus-wide speedup.
