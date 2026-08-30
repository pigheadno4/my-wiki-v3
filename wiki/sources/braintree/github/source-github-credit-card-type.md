---
title: "GitHub: braintree/credit-card-type"
type: source
date_ingested: 2026-08-29
original_format: github-repo
raw_files:
  - "github/braintree/credit-card-type/snapshots/2026-08-29-fbd8ed8/manifest.json"
tags: [braintree, credit-card-type, card-brand, bin, iin, typescript, commonjs, github-repository]
---

## Overview

`credit-card-type@10.3.0` is the first retained exact-SHA baseline for Braintree's standalone card-brand detector. It identifies likely brands from partial or complete card-number prefixes and supplies formatting and security-code metadata for checkout UI.

The package is not a card-validation or payment-processing SDK. It does not perform Luhn validation, verify expiry or security codes, tokenize a card, check merchant acceptance, select a co-badged processing network, or authorize a payment.

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

## Related

- [[changelog-github-credit-card-type]] - package-qualified release ledger
- [[card-brand-detection]] - generic inference, ambiguity, UI, and validation boundaries
- [[braintree-web-sdk]] - Braintree browser checkout and Hosted Fields context
- [[co-badged-cards]] - cardholder network choice beyond brand detection
- [[braintree]] - company and knowledge-status page

## Raw Sources

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
