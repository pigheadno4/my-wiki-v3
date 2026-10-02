# PayPal JS shared-SHA ingest review

Date: 2026-10-02
Work item: `github-5b2a7f87f06b9859f5c8`
SHA: `d9966e6dd9a5bb880341a7df1809329e82906a41`
Mode: user-approved delta; inline serial ingest.
Releases: `@paypal/paypal-js@11.1.1` -> `@paypal/paypal-js@11.2.0`; `@paypal/react-paypal-js@10.5.1` -> `@paypal/react-paypal-js@10.5.2`.

## Reading and grounding

- [x] Read packet Markdown and JSON, and all 37 paths assigned by the packet and effective next-ingest result in full. User explicitly chose full reading, not a focused-reading exception.
- [x] Read complete current source/changelog history, both cumulative raw changelogs, both release manifest/note pairs, both complete snapshot manifests, all 23 changed/new retained files, and both comparison manifest/Markdown/patch sets.
- [x] Manifest records were displayed as lossless key-column/value tables, including every hash, blob ID, size, path, package, purpose and classification. No unchanged-manifest or cumulative-history hash-only reading substitute was used. Repeated packet inventories and upstream dispositions are exactly identical across package views; reviewed shared content once, with equality verified.
- [x] Closed truncated output ranges with bounded rereads before wiki writing. The complete comparison patches also supply affected prior-code context.
- [x] Extracted five verbatim grounding excerpts before source writing: constants.ts lines 9, 10, 11; core v6 index.ts line 15; React v6 getOwnProperty.ts line 12. Recorded exact quotes in the source page.
- [x] Verified packet Markdown and snapshot-manifest hashes and all 165 current snapshot file hashes/sizes, totaling 1,119,051 bytes. Two package views each report 10 added, 13 modified and 142 unchanged paths; unique counts are 23 changed/new and 142 unchanged.

## Mode and findings

Contained v6 loader/configuration hardening, no changed retained public payment declarations or new session API. Upstream changes have dispositions; no packet evidence gap or unclassified retained change. The security release note does not establish an unbounded exploit impact; this review reports only the exact guards, without an independent remote-code-execution mitigation guarantee. Delta remains appropriate.

- Core pure-error sequence: initial plus two retries. Pure-timeout sequence: initial plus one retry, 15 seconds per attempt. Mixed paths share the attempt count; do not add budgets independently.
- Retry delays cap the exponential base at 400 milliseconds before up-to-50-percent jitter; cache busting uses `paypal-sdk-retry`.
- In-flight sharing is namespace-keyed, not all-options/environment-keyed. Missing global on load rejects immediately; retry-delay namespace reuse does not recheck version. Removing a timed-out tag does not cancel already-sent browser requests or prove prevention of late evaluation.
- Release notes and raw core changelog instead say five retries and 10 seconds. Explicit contradiction recorded in source, changelog and checkout concept.
- React guards selected provider/server settings and legacy namespaces; it does not guard every option. Dependency becomes `^11.2.0`.
- No new saved-payment editing wrapper. Independent Braintree runtime/sample history remains separate.
- Retained mock/HTML harness additions are not merchant features or executed tests; the mock was modified upstream but newly retained by this snapshot.

## Wiki cycle

- [x] Concept audit and checkout concept update before source writing.
- [x] Add core 11.2.0 and React 10.5.2 sections, examples, exact evidence and grounding to the cumulative source; preserve all older version sections.
- [x] Add package-qualified shared-SHA changelog entry with impact, migration and full-reading boundary.
- [x] Update company and PayPal index descriptions; no new source page or substantive cross-company comparison, so source_count unchanged and no new comparison page.
- [x] Contradiction check and provider/root log updates; preserve unrelated session changes.
- [x] Focused wiki validation, collection validation, history-preservation check and terminal work-item completion.

## Validation and completion

- `validate_wiki.py` passes for the five schema-bearing pages: checkout concept, cumulative source, changelog, company and provider log.
- The initial seven-file invocation reported missing frontmatter only for `wiki/paypal-index.md` and `wiki/log.md`. These established index/root-log formats are excluded by the validator's default scan; no frontmatter or validator changes were made. Separate link checks pass across all seven pages (834 wikilinks and local Markdown targets).
- All 24 historical package-version sections and all prior repository changelog entries are preserved verbatim. Initial broad history-check assertions included newly extended navigation sections; the corrected checks isolate historical version/entry bodies and pass.
- `git diff --check` passes. Collection validation passes before and after completion: 151 snapshots, 136 release records, 94 comparisons, 150 work items, no structural errors.
- `complete-ingest --item github-5b2a7f87f06b9859f5c8` returned terminal state `ingested`, approved mode `delta`, and the two expected package-qualified releases at the approved SHA.

No package build, upstream test execution, browser/payment test, commit or push authorized/performed for this item. Deterministic wiki validation is not runtime evidence.
