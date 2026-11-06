---
title: "GitHub: braintree/credit-card-type"
type: source
date_ingested: 2026-08-29
date_updated: 2026-11-07
original_format: github-repo
raw_files:
  - "github/braintree/credit-card-type/snapshots/2026-11-07-b1ca702/manifest.json"
  - "github/braintree/credit-card-type/releases/credit-card-type/10.3.0/2026-11-07/manifest.json"
  - "github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/manifest.json"
tags: [braintree, credit-card-type, card-brand, bin, iin, typescript, commonjs, github-repository]
---

## Overview

`credit-card-type@10.3.0` is the first retained exact-SHA baseline for Braintree's standalone card-brand detector. It identifies likely brands from partial or complete card-number prefixes and supplies formatting and security-code metadata for checkout UI.

The package is not a card-validation or payment-processing SDK. It does not perform Luhn validation, verify expiry or security codes, tokenize a card, check merchant acceptance, select a co-badged processing network, or authorize a payment.

Latest ingested implementation: `credit-card-type@10.3.1`, SHA `b1ca7027bcba9377382abaf7db8d6902c8842ec1`, delta ingested 2026-11-07. The complete 10.3.0 baseline and its same-SHA notes revision remain preserved below.

## Baseline and Package Boundary

The retained package resolves to SHA `fbd8ed80a411fa9b238055208c19a7323cd38e21`, tagged `v10.3.0` on 2026-06-30. It is TypeScript compiled to CommonJS targeting ES5, publishes generated `dist/index.js` and `dist/index.d.ts`, and declares no runtime dependencies. The generated `dist/` tree is reviewed as a package target but is not retained; the complete non-test `src/` tree is the implementation authority for this snapshot.

The package can run independently of Braintree payment processing. Its output is UI and decision-support metadata, not evidence that a brand or network is enabled for a merchant.

## Detection Model

The default export accepts a string-like card number and evaluates each configured brand's numeric patterns or numeric ranges:

1. A partial number can match the beginning of a longer pattern or range.
2. Each matching brand is cloned into the result so callers do not directly receive the built-in configuration object.
3. A match receives `matchStrength` when the supplied number is at least as long as the matching pattern.
4. The detector returns one best match only when every candidate has a complete-pattern strength; the candidate with the longest pattern wins.
5. Otherwise, it returns every matching candidate in the configured test order.

An empty string returns all configured brands. A non-string input returns an empty array. The detector stops after the first matching pattern for each brand, so the retained pattern order also affects the strength attached to that brand.

This model intentionally supports type-as-you-go ambiguity. A broad Visa prefix and a more specific Elo prefix can coexist until the full Elo pattern supplies a stronger match.

## Built-In Brand Metadata

The exact snapshot defines 15 built-in brands:

| Brand ID | Display name | Number lengths | Security code |
| --- | --- | --- | --- |
| `visa` | Visa | 16, 18, 19 | CVV, 3 |
| `mastercard` | Mastercard | 16 | CVC, 3 |
| `american-express` | American Express | 15 | CID, 4 |
| `diners-club` | Diners Club | 14, 16, 19 | CVV, 3 |
| `discover` | Discover | 16, 19 | CID, 3 |
| `troy` | Troy | 16 | CVV, 3 |
| `jcb` | JCB | 16-19 | CVV, 3 |
| `unionpay` | UnionPay | 14-19 | CVN, 3 |
| `naranja` | Naranja | 16 | CVV, 3 |
| `verve` | Verve | 16, 18, 19 | CVV, 3 |
| `maestro` | Maestro | 12-19 | CVC, 3 |
| `elo` | Elo | 16 | CVE, 3 |
| `mir` | Mir | 16-19 | CVP2, 3 |
| `hiper` | Hiper | 16 | CVC, 3 |
| `hipercard` | Hipercard | 16 | CVC, 4 |

Each brand also defines formatting-gap positions and its exact prefix/range patterns. These values describe detector behavior at this release; they are not an authoritative current network BIN registry.

## Public API and Mutable Configuration

- `creditCardType(number)` returns zero or more cloned candidate configurations.
- `getTypeInfo(type)` retrieves a cloned configuration by brand ID.
- `types` exposes the built-in symbolic constants.
- `addCard(config)` adds a custom brand or overrides a built-in brand's configuration.
- `updateCard(type, updates)` shallow-merges top-level updates into a cloned built-in or custom configuration and rejects changes to the `type` identifier.
- `removeCard(type)` removes a brand from the active test order.
- `changeOrder(type, position)` changes matching and unresolved-result priority.
- `resetModifications()` restores the original order and clears custom configurations.

These mutations are module-level state. A change affects later detector calls in the same loaded module until reset. `getTypeInfo` returns a clone, so mutating the returned object alone does not update detector state.

## Input and Documentation Boundaries

The README instructs callers to normalize card numbers and avoid letters or special characters. The exact runtime does not perform that complete normalization: `isValidInputType` checks only for a primitive or boxed string, while pattern matching uses string comparison and `parseInt` for ranges. Consumers therefore need their own explicit input normalization and validation.

> [!warning] Retained documentation and runtime conflicts
> The README says an unknown `getTypeInfo` value returns `undefined`, but the exact implementation passes the missing value through `clone`, which returns `null`. The repository changelog says `9.0.0` dropped support for card numbers constructed with `new String(number)`, while the retained `10.3.0` input check still accepts `cardNumber instanceof String`. Tests are excluded from this capsule, so callers should verify these edge cases against the exact packaged artifact before relying on them.

## Release and Historical Context

Exact `10.3.0` adds Troy and its prefix ranges, constant, type union, display name, CVV metadata, and default test-order position. The retained repository changelog says earlier v10 releases added Naranja in `10.2.0` and Verve in `10.1.0`. Version `10.0.0` records Node, TypeScript, Prettier, and lint-tool upgrades rather than a documented detector API break.

Older changelog entries describe important behavior transitions, including TypeScript types in v9, the current pattern-array model in v8, custom cards in v6, ambiguity returning arrays in v4, and Maestro/UnionPay support in v2. Those entries are historical context only; no separate exact-SHA snapshot is retained for those versions.

## Evidence Boundaries

The 14-file capsule includes the complete non-test TypeScript implementation, README, changelog, package and compiler metadata, license, and security policy. Tests, fixtures, generated `dist/`, package lock data, CI, and development tooling are excluded.

This evidence proves repository behavior at the retained SHA. It does not prove npm registry contents, browser compatibility in a merchant application, current BIN allocation, PCI scope, network acceptance, Braintree merchant configuration, or successful payment processing.

## 10.3.0 Release-Notes Revision Ingested 2026-11-07

Approved delta work item `github-33914676c405b863373a` adds the newly available [upstream note](../../../../raw/github/braintree/credit-card-type/releases/credit-card-type/10.3.0/2026-11-07/release-notes.md), `- add support for troy cards`, for the same `credit-card-type@10.3.0` SHA `fbd8ed80a411fa9b238055208c19a7323cd38e21`. It corroborates the existing Troy implementation findings, not a new implementation, feature rollout or payment-acceptance claim. All 14 retained source files are unchanged; the original snapshot and empty-note record remain immutable.

The [original August record](../../../../raw/github/braintree/credit-card-type/releases/credit-card-type/10.3.0/2026-08-29/manifest.json) has `notes_available: false` and a June 30 date matching the snapshot's commit timestamp. The [new record](../../../../raw/github/braintree/credit-card-type/releases/credit-card-type/10.3.0/2026-11-07/manifest.json) has `notes_available: true` and GitHub publication `2026-10-13T16:20:11Z`. The original baseline's June date is retained history, not evidence that GitHub published that release on June 30 or that the tag's creation time was verified. November 7 is the notes collection/ingest date; August 29 remains the initial baseline ingest date.

Grounding excerpts (all line 1): `- add support for troy cards` in the new release-notes file; `"notes_available":false` in the original release manifest; `"release_date":"2026-10-13T16:20:11Z"` in the new release manifest. All five assigned files (including complete cumulative source/changelog context) were read; the note, manifest and snapshot hashes pass. No source comparison is needed because this is a release-note revision, not a new SHA. Existing normalization, unknown-type, boxed-String and payment-processing boundaries remain intact. No SDK build, upstream suite or payment execution.

## `credit-card-type@10.3.1` Elo Range Delta

Published 2026-10-13T19:32:04Z; collected and delta ingested 2026-11-07 after completing the 10.3.0 notes revision. Work item `github-84021be2188f8cfe1577` compares prior SHA `fbd8ed80a411fa9b238055208c19a7323cd38e21` with `b1ca7027bcba9377382abaf7db8d6902c8842ec1`.

The complete changed [card definitions](../../../../raw/github/braintree/credit-card-type/snapshots/2026-11-07-b1ca702/files/src/lib/card-types.ts) add two inclusive Elo prefix ranges:

```typescript
[650057, 650081],
[651680, 651704],
```

The second range is adjacent to the existing `651652-651679` range. Elo keeps its existing 16-digit length, formatting gaps `[4, 8, 12]` and three-digit `CVE` label. No new brand, public API, detection algorithm or runtime dependency is added; all other card definitions are unchanged. The only other retained change is [package.json](../../../../raw/github/braintree/credit-card-type/snapshots/2026-11-07-b1ca702/files/package.json), whose version becomes 10.3.1. The upstream cumulative changelog is unchanged, so absence of a new entry there is not evidence that the released range change is absent.

### Detection Impact and Integration Boundary

The unchanged [candidate accumulator](../../../../raw/github/braintree/credit-card-type/snapshots/2026-11-07-b1ca702/files/src/lib/add-matching-cards-to-results.ts), [matching helper](../../../../raw/github/braintree/credit-card-type/snapshots/2026-11-07-b1ca702/files/src/lib/matches.ts) and [best-match reducer](../../../../raw/github/braintree/credit-card-type/snapshots/2026-11-07-b1ca702/files/src/lib/find-best-match.ts) use complete pattern length to resolve candidates. Under default configuration, the new six-digit Elo ranges outrank Discover's broad `65` and Maestro's broad `6`. Short prefixes can still produce several candidates; this is not an unconditional early Elo classification.

Source-derived examples below are static reasoning, not executed runtime tests or valid test-card numbers:

| Prefix | 10.3.0 default detector | 10.3.1 default detector |
| --- | --- | --- |
| `650057`, `650069`, `650081` | Discover | Elo |
| `651680`, `651692`, `651704` | Discover | Elo |
| `650052`, `650082` | Troy | Troy |
| `651679` | Elo | Elo |

Existing custom-card and ordering mutations can change the active configuration; input normalization remains the consumer's responsibility. Recognition does not prove Luhn validity, BIN allocation, co-badged network selection, merchant enablement or transaction authorization. All earlier unknown-type/boxed-String/documentation discrepancies remain unchanged.

The independent Braintree Web 3.148.0 snapshot pins this 10.3.1 dependency. The utility evidence explains that bounded Elo change rather than inferring it from a version bump alone. Keep the two repository histories independent: no live Hosted Fields, gateway or payment execution was performed. See [[source-github-braintree-web]] and [[braintree-web-sdk]].

### Migration, Reading and Evidence

No mandatory application migration is stated. Consumers upgrading from 10.3.0 should check formatting/artwork/accepted-brand UI for the added range endpoints and interiors, adjacent Troy prefixes, short-prefix ambiguity and custom overrides. Updating detection does not enable Elo processing. This is not a security advisory or an npm-artifact verification.

All eleven assigned paths were read in full, including both manifests, the complete two changed files, release record/note, complete comparison JSON/Markdown/patch and cumulative source/changelog. Affected unchanged matching dependencies were also read. All 28 prior/current files pass size, SHA-256 and Git blob-ID checks; 14 current files total 34,399 bytes, two modified and twelve unchanged. All four upstream changes reconcile: the two retained changes, version-only excluded lockfile and excluded tests. Changed test hunks were read in the complete comparison, not executed or collected as full test files. No generated dist, raw/packet mutation, supplement, package installation, build or upstream suite.

Grounding excerpts:

- `[650057, 650081],` - current `src/lib/card-types.ts:211`.
- `[651680, 651704],` - current `src/lib/card-types.ts:219`.
- `"version": "10.3.1",` - current `package.json:3`.
- `- fix: add new ranges for Elo card types (thanks @Victor-Vechi!)` - current release-notes.md:1.

## Related

- [[changelog-github-credit-card-type]] - package-qualified release ledger
- [[card-brand-detection]] - generic inference, ambiguity, UI, and validation boundaries
- [[braintree-web-sdk]] - Braintree browser checkout and Hosted Fields context
- [[co-badged-cards]] - cardholder network choice beyond brand detection
- [[braintree]] - company and knowledge-status page

## Raw Sources

- [10.3.1 snapshot](../../../../raw/github/braintree/credit-card-type/snapshots/2026-11-07-b1ca702/manifest.json), [release identity](../../../../raw/github/braintree/credit-card-type/releases/credit-card-type/10.3.1/2026-11-07/manifest.json) and [release note](../../../../raw/github/braintree/credit-card-type/releases/credit-card-type/10.3.1/2026-11-07/release-notes.md)
- [10.3.0 to 10.3.1 comparison manifest](../../../../tracking/github/repos/braintree/credit-card-type/comparisons/credit-card-type/10.3.0--10.3.1/comparison.json), [readable comparison](../../../../tracking/github/repos/braintree/credit-card-type/comparisons/credit-card-type/10.3.0--10.3.1/comparison.md) and [complete patch](../../../../tracking/github/repos/braintree/credit-card-type/comparisons/credit-card-type/10.3.0--10.3.1/diff.patch)

- [10.3.0 revised release manifest](../../../../raw/github/braintree/credit-card-type/releases/credit-card-type/10.3.0/2026-11-07/manifest.json) and [newly available release note](../../../../raw/github/braintree/credit-card-type/releases/credit-card-type/10.3.0/2026-11-07/release-notes.md) - evidence revision, same original SHA

- Snapshot manifest: `raw/github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/manifest.json`
- Release manifest: `raw/github/braintree/credit-card-type/releases/credit-card-type/10.3.0/2026-08-29/manifest.json`
- Release notes: `raw/github/braintree/credit-card-type/releases/credit-card-type/10.3.0/2026-08-29/release-notes.md` (upstream body unavailable)
- README: `raw/github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/files/README.md`
- Repository changelog: `raw/github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/files/CHANGELOG.md`
- Package metadata: `raw/github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/files/package.json`
- Compiler configuration: `raw/github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/files/tsconfig.json`
- Public detector and mutation API: `raw/github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/files/src/index.ts`
- Public types: `raw/github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/files/src/types.ts`
- Built-in brands and patterns: `raw/github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/files/src/lib/card-types.ts`
- Candidate accumulation: `raw/github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/files/src/lib/add-matching-cards-to-results.ts`
- Best-match reduction: `raw/github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/files/src/lib/find-best-match.ts`
- Pattern and range matching: `raw/github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/files/src/lib/matches.ts`
- Input-type check: `raw/github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/files/src/lib/is-valid-input-type.ts`
- Clone helper: `raw/github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/files/src/lib/clone.ts`
- Security policy: `raw/github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/files/SECURITY.md`
- License: `raw/github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/files/LICENSE`
