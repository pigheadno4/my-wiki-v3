# Credit Card Type Collection Review - 2026-11-07

## Authorization and Result

User authorized a repository recheck and findings before ingestion. Ran the existing future-release collector without changing rules, registry paths or budgets. It stopped with two items awaiting approval; neither is approved or claimed. No wiki knowledge, commit or push.

## 1. Existing 10.3.0 Release-Notes Revision

- Work item `github-33914676c405b863373a`, recommended delta/normal.
- Same package/version and SHA `fbd8ed80a411fa9b238055208c19a7323cd38e21`; reuses the immutable 2026-08-29 14-file snapshot. No code changes.
- The earlier release record had no upstream note body. A new immutable 2026-11-07 release record now retains `- add support for troy cards`, corroborating the already-ingested Troy feature.
- The new GitHub record reports publication at 2026-10-13T16:20:11Z. Keep that distinct from the earlier retained history's June date and August ingestion; do not rewrite original raw records or treat today's note collection as a new package release.
- Packet: `ingest-packets/github-33914676c405b863373a/packet.json`; new record: `raw/github/braintree/credit-card-type/releases/credit-card-type/10.3.0/2026-11-07/manifest.json`.

## 2. credit-card-type@10.3.1

- Work item `github-84021be2188f8cfe1577`, recommended delta/normal.
- Exact SHA `b1ca7027bcba9377382abaf7db8d6902c8842ec1`, GitHub publication 2026-10-13T19:32:04Z, collected 2026-11-07.
- New snapshot `raw/github/braintree/credit-card-type/snapshots/2026-11-07-b1ca702/manifest.json`: 14 files / 34,399 bytes. Prior snapshot: 14 files / 34,351 bytes. Two modified, 12 unchanged, none added/removed.
- Complete changed retained files read: package.json changes only package version; `src/lib/card-types.ts` adds Elo ranges `[650057, 650081]` and `[651680, 651704]`. The latter extends coverage adjacent to the existing `[651652, 651679]` range. No new card brand, public API, matching algorithm, card-length/CVV definition or runtime dependency change.
- All four upstream changes reconcile: the two retained files, version-only lockfile changes and excluded tests. Full comparison patch read; tests add range endpoints/interior values and nearby Troy checks, but were not executed. Runtime detector and matching dependencies were read for context. Generated dist and excluded tests remain outside the capsule.
- The newly covered six-digit Elo patterns are more specific than the unchanged broad Discover `65` and Maestro `6` patterns. This is card-brand recognition metadata, not PAN validation, merchant/network acceptance, co-badged routing or authorization evidence. No SDK build, package install, upstream test suite or payment run.
- Braintree Web 3.148.0 separately pins credit-card-type 10.3.1; this repository explains that dependency's change without merging repository histories or claiming every consumer's checkout behavior has been exercised.
- Packet: `ingest-packets/github-84021be2188f8cfe1577/packet.json`; comparison: `comparisons/credit-card-type/10.3.0--10.3.1/comparison.json`; release record: `raw/github/braintree/credit-card-type/releases/credit-card-type/10.3.1/2026-11-07/manifest.json`.

## Verification

- All 28 prior/current file sizes, SHA-256 and Git blob IDs pass; only package.json and card-types.ts differ.
- Both packet Markdown/snapshot identities, both new release-note hashes and comparison Markdown/patch digests pass. Both packets have zero gaps/unclassified changes. Effective reading lists include five and eleven paths respectively, including cumulative wiki context.
- Existing source/changelog remain byte-identical to HEAD. Last ingest date remains 2026-08-29 until an approved ingest finishes. No approval, claim or completion command was run.
- Offline GitHub validation retains the same 13 unrelated historical structural errors, none for this repository, and reports exactly these two pending items. Scoped whitespace check passes.

Next recommendation: separately approve both as serial deltas, first the 10.3.0 notes revision, then 10.3.1. Preserve the original baseline, note-availability history and existing documentation/runtime caveats. The small packets can use normal full assigned-file reading without a focused-reading exception.
