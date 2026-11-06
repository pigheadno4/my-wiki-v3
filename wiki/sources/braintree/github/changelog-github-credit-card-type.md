---
title: "GitHub changelog: braintree/credit-card-type"
type: source
date_ingested: 2026-08-29
date_updated: 2026-11-07
original_format: github-repo
raw_files:
  - "github/braintree/credit-card-type/snapshots/2026-11-07-b1ca702/manifest.json"
  - "github/braintree/credit-card-type/releases/credit-card-type/10.3.0/2026-11-07/manifest.json"
  - "github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/manifest.json"
tags: [braintree, credit-card-type, card-brand, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/credit-card-type`. Cumulative implementation knowledge belongs in [[source-github-credit-card-type]] and the linked immutable snapshot.

## `credit-card-type@10.3.1` (2026-10-13; ingested 2026-11-07)

`credit-card-type@10.3.0` -> `credit-card-type@10.3.1`; SHA `b1ca7027bcba9377382abaf7db8d6902c8842ec1`. Approved serial delta `github-84021be2188f8cfe1577`, started only after the preceding notes-only item completed and validated. All baseline and note-revision history remains below.

**Findings:** adds inclusive Elo prefixes `650057-650081` and `651680-651704`; the latter extends existing coverage adjacent to `651652-651679`. No new brand, public API, matching algorithm, card-length/CVV definition or runtime dependency. Package metadata changes only its version; the raw cumulative changelog is unchanged.

**Impact:** complete six-digit Elo patterns now outrank broad Discover `65` and Maestro `6` under default configuration; short-prefix ambiguity remains. Static source-derived examples and unchanged adjacent Troy boundaries are recorded in [[source-github-credit-card-type]], not represented as executed tests. This fills the standalone dependency evidence gap for Braintree Web 3.148.0's 10.3.1 pin without claiming merchant acceptance, network routing, hosted runtime or payment proof.

**Migration:** no mandatory migration stated. Check new endpoints/interiors, adjacent prefixes, UI brand treatment and any custom detector overrides; keep validation and accepted-network policy independent. Existing normalization, unknown-type and boxed-String caveats remain preserved.

**Reading and updates:** all eleven assigned paths read in full, plus affected matching dependencies/prior definitions. Two modified/twelve unchanged retained files; all 28 sizes/SHA-256/Git blob IDs and packet/release/comparison hashes pass. All four upstream dispositions reconcile without gaps/unclassified changes. Two concepts updated first, followed by source/changelog/company/catalog/logs; source_count unchanged, no new comparison page. No upstream suite/build/install/browser/payment execution or generated-dist verification.

**Evidence:** [snapshot](../../../../raw/github/braintree/credit-card-type/snapshots/2026-11-07-b1ca702/manifest.json), [release manifest](../../../../raw/github/braintree/credit-card-type/releases/credit-card-type/10.3.1/2026-11-07/manifest.json), [release note](../../../../raw/github/braintree/credit-card-type/releases/credit-card-type/10.3.1/2026-11-07/release-notes.md), [comparison manifest](../../../../tracking/github/repos/braintree/credit-card-type/comparisons/credit-card-type/10.3.0--10.3.1/comparison.json), [readable comparison](../../../../tracking/github/repos/braintree/credit-card-type/comparisons/credit-card-type/10.3.0--10.3.1/comparison.md) and [patch](../../../../tracking/github/repos/braintree/credit-card-type/comparisons/credit-card-type/10.3.0--10.3.1/diff.patch).

## `credit-card-type@10.3.0` Release-Notes Revision (ingested 2026-11-07)

Approved serial delta, work item `github-33914676c405b863373a`; same SHA `fbd8ed80a411fa9b238055208c19a7323cd38e21` and same 14-file snapshot. The newly available upstream note says `- add support for troy cards`, confirming the already-ingested feature without changing code, public APIs, dependencies or payment-acceptance evidence. No new implementation comparison applies.

The original record had no note body and used the June 30 commit-backed date. The new record reports GitHub publication `2026-10-13T16:20:11Z`; neither is today's collection/ingest date. The original August ingest, June-dated baseline entry, empty note and raw manifest remain preserved. Do not retroactively call the new note available at the original ingestion.

All five assigned paths read in full; snapshot/release/packet identities and hashes verified. Existing concept updated first, followed by source/changelog/company/catalog/logs; source_count unchanged. No build, upstream tests, payment run, commit or push. Exact grounding excerpts and dates: [[source-github-credit-card-type]].

Evidence: [revised release manifest](../../../../raw/github/braintree/credit-card-type/releases/credit-card-type/10.3.0/2026-11-07/manifest.json), [new note](../../../../raw/github/braintree/credit-card-type/releases/credit-card-type/10.3.0/2026-11-07/release-notes.md), [original release record](../../../../raw/github/braintree/credit-card-type/releases/credit-card-type/10.3.0/2026-08-29/manifest.json), [unchanged snapshot](../../../../raw/github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/manifest.json).

## `credit-card-type@10.3.0` (2026-06-30)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `credit-card-type` | Initial baseline | `10.3.0` | `fbd8ed80a411fa9b238055208c19a7323cd38e21` | Full |

**Exact release change:** Adds Troy as a built-in card brand, including its prefix/range patterns, 16-digit length, formatting gaps, three-digit CVV metadata, public constant and TypeScript identifiers, and default detection order.

**Developer or merchant impact:** Applications using the package can identify Troy while a shopper enters a card number and can format the number and security-code prompt from the returned metadata. This does not enable Troy processing, validate a PAN, or prove that a merchant or processor accepts the network.

**Migration action:** No mandatory migration is documented. Consumers that exhaustively switch over brand IDs or display names should add `troy`, update UI assets where needed, and test ambiguous prefixes against their own accepted-brand policy.

**Updated source sections:** Baseline and package boundary; detection model; built-in brand metadata; public API and mutable configuration; input and documentation boundaries; release and historical context.

**Evidence boundary:** This is the first retained exact-SHA baseline, so there is no comparison manifest. The upstream release-note body is unavailable; the repository changelog and exact source establish the Troy change.

**Evidence:**

- Release manifest: `raw/github/braintree/credit-card-type/releases/credit-card-type/10.3.0/2026-08-29/manifest.json`
- Release notes: `raw/github/braintree/credit-card-type/releases/credit-card-type/10.3.0/2026-08-29/release-notes.md`
- Snapshot manifest: `raw/github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/manifest.json`
- Repository changelog: `raw/github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/files/CHANGELOG.md`
- Built-in brand definitions: `raw/github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/files/src/lib/card-types.ts`
- Public detector and constants: `raw/github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/files/src/index.ts`
- Public brand types: `raw/github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/files/src/types.ts`

## Historical v10 Context

- `10.2.0` adds Naranja and introduces conventional-commit tooling.
- `10.1.2` updates the Node type dependency.
- `10.1.1` updates development dependencies and the repository's Node version.
- `10.1.0` adds Verve.
- `10.0.2` and `10.0.1` update development or transitive dependencies.
- `10.0.0` moves repository tooling to Node 18, TypeScript 5, Prettier 3, and eslint-plugin-prettier 5.

These entries come from the retained `10.3.0` repository changelog. They are useful cumulative history but are not separately collected implementation snapshots or byte-level comparisons.

## Earlier Major-Version Context

- v9 adds TypeScript types, removes Bower support, and says boxed `String` input support was dropped.
- v8 replaces separate exact/prefix configuration with the current pattern-array model.
- v7 adds Elo and `updateCard`; v6 adds Mir and custom-card support.
- v5 introduces a two-tier exact-versus-partial ambiguity model; v4 changes the detector to return an array of candidates.
- v2 adds Maestro and UnionPay and changes a single `length` value to a `lengths` array.

These are changelog statements, not exact retained snapshots. The boxed-`String` statement conflicts with the retained v10 runtime check and is documented in [[source-github-credit-card-type]].
