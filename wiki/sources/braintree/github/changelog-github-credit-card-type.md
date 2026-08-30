---
title: "GitHub changelog: braintree/credit-card-type"
type: source
date_ingested: 2026-08-29
original_format: github-repo
raw_files:
  - "github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/manifest.json"
tags: [braintree, credit-card-type, card-brand, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/credit-card-type`. Cumulative implementation knowledge belongs in [[source-github-credit-card-type]] and the linked immutable snapshot.

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
